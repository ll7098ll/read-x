import {existsSync,readFileSync,openSync,writeFileSync,fsyncSync,closeSync,statSync,constants} from 'node:fs';
import {dirname,isAbsolute,resolve,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import {randomUUID} from 'node:crypto';
import {recoverySigner} from './recovery-keys.mjs';
import {assertPlainFile,canonicalFile,acquireFileLease} from './maintenance-lock.mjs';
const zero='0'.repeat(64);
const failure=()=>Object.assign(Error('별도 삭제 원장과 DB가 일치하지 않습니다. 격리 복원·동기화 검증을 완료해 주세요.'),{status:503,code:'RECOVERY_SYNC_REQUIRED'});
const wire=f=>JSON.stringify(['readx-recovery-v1',f.databaseId,f.seq,f.keyId,f.previous,f.event]);
const anchorWire=f=>JSON.stringify(['readx-recovery-anchor-v1',f.databaseId,f.seq,f.hash,f.keyId,f.createdAt]);
const id=v=>typeof v==='string'&&v.length>0&&v.length<=150;
export function createRecoveryJournal({db,dbPath,journalPath,keyring,anchor,production=process.env.READX_RUNTIME==='production',initialize=true,adoptLegacy=false,beforeAppend}){
 const databaseId=db.prepare('SELECT database_id FROM access_log_identity WHERE id=1').get()?.database_id;if(!databaseId)throw failure();
 const requested=journalPath||process.env.READX_RECOVERY_JOURNAL;
 if(production&&(!requested||!isAbsolute(requested)||dbPath===':memory:'))throw Error('운영 DB와 분리된 절대 경로 READX_RECOVERY_JOURNAL이 필요합니다.');
 const path=dbPath===':memory:'?null:canonicalFile(requested||dbPath+'.recovery.ndjson');
 if(production&&dirname(path)===dirname(canonicalFile(dbPath)))throw Error('운영 삭제 원장을 운영 DB 디렉터리와 분리해 주세요.');
 if(path){assertPlainFile(path);const root=resolve(fileURLToPath(new URL('..',import.meta.url))),low=v=>process.platform==='win32'?v.toLowerCase():v;if(low(path).startsWith(low(root+sep))&&!low(path).startsWith(low(resolve(root,'.exam-data')+sep)))throw Error('삭제 원장을 공개 소스·웹 산출물 경로에 두지 마세요.');}
 const hadTable=!!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name='recovery_state'").get(),hadState=hadTable&&!!db.prepare('SELECT 1 FROM recovery_state LIMIT 1').get();
 if(!hadState&&!adoptLegacy&&JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body).users.some(u=>u.deletedAt))throw Error('이전 삭제 계정의 별도 원장 이관 검토가 필요합니다. 복구 관리 도구로 실제 상태를 확인해 주세요.');
 const signer=recoverySigner({dbPath,keyring,hasRecords:hadState||!!(path&&existsSync(path)),production});
 db.exec('CREATE TABLE IF NOT EXISTS recovery_events (seq INTEGER PRIMARY KEY AUTOINCREMENT,event_id TEXT NOT NULL UNIQUE,event TEXT NOT NULL); CREATE TABLE IF NOT EXISTS recovery_state (id INTEGER PRIMARY KEY CHECK(id=1),seq INTEGER NOT NULL,hash TEXT NOT NULL,database_id TEXT NOT NULL)');
 let memory=[];
 const frame=(seq,previous,event)=>{const f={v:1,databaseId,seq,keyId:signer.activeId,previous,event};return {...f,hash:signer.sign(wire(f))};};
 const append=f=>{
  beforeAppend?.(f);
  if(!path){memory.push(f);return;}
  assertPlainFile(path);let fd;try{fd=openSync(path,constants.O_WRONLY|constants.O_APPEND);writeFileSync(fd,JSON.stringify(f)+'\n');fsyncSync(fd);}finally{if(fd!==undefined)closeSync(fd);}
 };
 const verify=()=>{
  let frames;
  if(path){assertPlainFile(path);if(!existsSync(path)||statSync(path).size>64*1024*1024)throw failure();const raw=readFileSync(path,'utf8');if(!raw.endsWith('\n'))throw failure();try{frames=raw.trimEnd().split('\n').map(line=>JSON.parse(line));}catch{throw failure();}}
  else frames=memory;
  let previous=zero;for(let seq=0;seq<frames.length;seq++){const f=frames[seq];if(f.v!==1||f.databaseId!==databaseId||f.seq!==seq||f.previous!==previous||!signer.verify(wire(f),f.hash,f.keyId)||seq===0&&f.event?.type!=='identity')throw failure();previous=f.hash;}
  if(!frames.length)throw failure();
  if(anchor&&(anchor.databaseId!==databaseId||!Number.isSafeInteger(anchor.seq)||!frames[anchor.seq]||frames[anchor.seq].hash!==anchor.hash||!signer.verify(anchorWire(anchor),anchor.signature,anchor.keyId)))throw failure();
  return frames;
 };
 if(!path||!existsSync(path)){
  if(hadState||!initialize)throw failure();const first=frame(0,zero,{type:'identity'});
  if(path){let fd;try{fd=openSync(path,'wx',0o600);writeFileSync(fd,JSON.stringify(first)+'\n');fsyncSync(fd);}finally{if(fd!==undefined)closeSync(fd);}}else memory=[first];
 }
 const initial=verify();if(!hadState)db.prepare('INSERT INTO recovery_state VALUES(1,0,?,?)').run(initial[0].hash,databaseId);
 const queue=event=>{
  if(!['erase_owned','retained_purged','retained_extended','backup_purge_prepared','backup_purged','access_archive_purge_prepared','access_archive_purged'].includes(event.type)||!id(event.tenantId)||!id(event.subjectId)||!Number.isSafeInteger(event.at))throw Error('삭제 원장 사건 범위를 확인해 주세요.');
  if(Buffer.byteLength(JSON.stringify(event))>1024*1024)throw Error('삭제 원장 사건의 크기를 초과했습니다.');
  const eventId=randomUUID();db.prepare('INSERT INTO recovery_events(event_id,event) VALUES(?,?)').run(eventId,JSON.stringify({...event,eventId}));
 };
 const sync=()=>{
  const release=path?acquireFileLease(path+'.write.lock','recovery-journal'):()=>{};
  try{
   let frames=verify();const checkpoint=db.prepare('SELECT * FROM recovery_state WHERE id=1').get(),rows=db.prepare('SELECT * FROM recovery_events ORDER BY seq').all();
   if(checkpoint.database_id!==databaseId||!frames[checkpoint.seq]||frames[checkpoint.seq].hash!==checkpoint.hash||frames.length-1>rows.length)throw failure();
   for(let i=0;i<rows.length;i++){
    const row=rows[i],event=JSON.parse(row.event);if(row.seq!==i+1||event.eventId!==row.event_id)throw failure();
    if(frames[row.seq]){if(JSON.stringify(frames[row.seq].event)!==JSON.stringify(event))throw failure();}
    else{const f=frame(row.seq,frames.at(-1).hash,event);append(f);frames.push(f);}
   }
   const head=frames.at(-1);if(checkpoint.seq!==head.seq||checkpoint.hash!==head.hash)db.prepare('UPDATE recovery_state SET seq=?,hash=? WHERE id=1').run(head.seq,head.hash);return {databaseId,seq:head.seq,hash:head.hash};
  }catch(e){if(e.code==='RECOVERY_SYNC_REQUIRED')throw e;throw failure();}finally{release();}
 };
 const checkpoint=(at=Date.now())=>{const head=verify().at(-1),c={v:1,databaseId,seq:head.seq,hash:head.hash,keyId:signer.activeId,createdAt:at};return {...c,signature:signer.sign(anchorWire(c))};};
 return {queue,sync,verify,checkpoint,databaseId,path};
}
