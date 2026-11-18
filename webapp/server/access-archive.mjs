import {DatabaseSync} from 'node:sqlite';
import {createHash,randomBytes,randomUUID} from 'node:crypto';
import {existsSync,readFileSync,writeFileSync,openSync,fsyncSync,closeSync,linkSync,unlinkSync,statSync} from 'node:fs';
import {resolve} from 'node:path';
import {fileURLToPath} from 'node:url';
import {backupCrypto} from './backup-crypto.mjs';
import {createAccessLog} from './access-log.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';
import {privateRuntimePath,assertPlainFile,assertNotMaintaining,acquireFileLease} from './maintenance-lock.mjs';
const magic=Buffer.from('READX-AUDIT-1\n'),maxBytes=64*1024*1024;
const digest=b=>createHash('sha256').update(b).digest('hex');
const ref=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const uuid=v=>typeof v==='string'&&/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/i.test(v);
const purgeTypes=['access_archive_purge_prepared','access_archive_purged'];
const validTime=v=>Number.isSafeInteger(v)&&Math.abs(v)<=8640000000000000;
export function createAccessArchive({dbPath,outPath,backupKeyring,auditKeyring,auditAnchor,reviewReference,expiresAt,confirmed=false,now=Date.now()}){
 if(!validTime(now))throw Error('실제 보관 검토 시각을 확인해 주세요.');
 if(!ref(reviewReference)||confirmed!==true)throw Error('실제 접속기록 보관 검토 문서와 명시적 확인이 필요합니다.');
 if(!Number.isSafeInteger(expiresAt)||expiresAt<=now||expiresAt>8640000000000000)throw Error('검토한 미래 접속기록 보관 종료일이 필요합니다.');
 const file=privateRuntimePath(dbPath),out=privateRuntimePath(outPath);assertPlainFile(file);assertPlainFile(out);assertNotMaintaining(file);
 if(!existsSync(file)||existsSync(out))throw Error('기존 DB와 새 보관 파일 경로가 필요합니다. 기존 파일을 덮어쓰지 않습니다.');
 if(process.env.READX_RUNTIME==='production'&&!auditAnchor)throw Error('운영 접속기록 보관에는 별도 기준점이 필요합니다.');
 const crypt=backupCrypto({dbPath:file,keyring:backupKeyring}),release=acquireFileLease(file+'.maintenance.lock','db-maintenance'),partial=out+'.partial-'+randomUUID();let db;
 try{
  db=new DatabaseSync(file);db.exec('PRAGMA busy_timeout=5000; BEGIN IMMEDIATE');
  for(const name of ['exam_state','access_log_identity','access_log','access_log_subjects'])if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(name))throw Error('확인된 프로젝트 접속기록 DB가 필요합니다.');
  const access=createAccessLog({db,dbPath:file,keyring:auditKeyring});access.verify(auditAnchor);
  const size=db.prepare('SELECT COALESCE(SUM(length(CAST(body AS BLOB))+512),0) n FROM access_log').get().n;
  if(size>maxBytes-4096)throw Error('접속기록 보관본 크기 제한을 초과했습니다. 운영 보관 분할 검토가 필요합니다.');
  const archiveId=randomUUID();access.append({requestId:randomUUID(),tenantId:'system',at:now,actorId:'local-server-admin',actorRole:'server-administrator',method:'LOCAL',route:'local/access-archive.prepare',resourceId:archiveId,category:'audit',status:202,bytes:0,address:null,addressSource:'local-server',subjects:[],records:0,review:{reference:reviewReference,archiveId,expiresAt}});db.exec('COMMIT');access.committed();db.exec('BEGIN IMMEDIATE');
  const checkpoint=access.checkpoint(now),rows=db.prepare('SELECT * FROM access_log ORDER BY seq').all(),payload=Buffer.from(JSON.stringify({v:1,kind:'readx-access-archive',archiveId,createdAt:now,expiresAt,checkpoint,rows}));
  if(payload.length>maxBytes)throw Error('접속기록 보관본 크기 제한을 초과했습니다.');
  const iv=randomBytes(12),header=Buffer.from(JSON.stringify({v:1,kind:'readx-access-archive',keyId:crypt.activeId,iv:iv.toString('base64')})),length=Buffer.alloc(4);length.writeUInt32BE(header.length);
  const prefix=Buffer.concat([magic,length,header]),cipher=crypt.cipher(iv);cipher.setAAD(prefix);const encrypted=Buffer.concat([prefix,cipher.update(payload),cipher.final(),cipher.getAuthTag()]);
  writeFileSync(partial,encrypted,{flag:'wx',mode:0o600});const fd=openSync(partial,'r+');try{fsyncSync(fd);}finally{closeSync(fd);}
  // Publish a new immutable pathname only after the complete ciphertext is durable.
  linkSync(partial,out);unlinkSync(partial);db.exec('COMMIT');
  return {ok:true,archiveId,path:out,sha256:digest(encrypted),bytes:encrypted.length,checkpoint,reviewReference,createdAt:now,expiresAt,encrypted:true,records:rows.length,automaticScheduleConfigured:false,offsiteStorageVerified:false};
 }finally{db?.close();if(existsSync(partial)){assertPlainFile(partial);unlinkSync(partial);}release();}
}

function decodeAccessArchive({archivePath,expectedSha256,backupKeyring}){
 if(typeof expectedSha256!=='string'||!/^[a-f0-9]{64}$/.test(expectedSha256))throw Error('별도 보관한 접속기록 파일 해시가 필요합니다.');
 const path=privateRuntimePath(archivePath);assertPlainFile(path);const size=statSync(path).size;
 if(size<magic.length+4+16||size>maxBytes+65536)throw Error('접속기록 보관 파일 크기가 올바르지 않습니다.');
 const bytes=readFileSync(path);if(digest(bytes)!==expectedSha256)throw Error('접속기록 보관 파일 해시가 다릅니다.');
 if(!bytes.subarray(0,magic.length).equals(magic))throw Error('지원하는 암호화 접속기록 형식이 아닙니다.');
 const length=bytes.readUInt32BE(magic.length),start=magic.length+4+length;
 if(length<2||length>4096||start+16>=bytes.length)throw Error('접속기록 보관 파일 머리글이 잘못되었습니다.');
 let h;try{h=JSON.parse(bytes.subarray(magic.length+4,start).toString('utf8'));}catch{throw Error('접속기록 보관 머리글 형식을 확인해 주세요.');}
 if(h.v!==1||h.kind!=='readx-access-archive'||typeof h.iv!=='string'||!/^[A-Za-z0-9+/]{16}$/.test(h.iv))throw Error('접속기록 보관 파일 암호화 정보가 다릅니다.');
 const crypt=backupCrypto({keyring:backupKeyring,restore:true}),decipher=crypt.decipher(h.keyId,Buffer.from(h.iv,'base64'));decipher.setAAD(bytes.subarray(0,start));decipher.setAuthTag(bytes.subarray(-16));
 let value;try{const plaintext=Buffer.concat([decipher.update(bytes.subarray(start,-16)),decipher.final()]);value=JSON.parse(plaintext.toString('utf8'));}catch{throw Error('접속기록 보관본 복호화·인증에 실패했습니다.');}
 if(value?.v!==1||value?.kind!=='readx-access-archive'||!uuid(value.archiveId)||!value.checkpoint||!Array.isArray(value.rows)||!validTime(value.createdAt)||!validTime(value.expiresAt)||value.expiresAt<=value.createdAt)throw Error('접속기록 보관본 내용이 올바르지 않습니다.');
 return value;
}
export function readAccessArchive(options){
 const value=decodeAccessArchive(options),now=options.now??Date.now();
 if(!validTime(now))throw Error('실제 복원 검토 시각을 확인해 주세요.');
 if(!Number.isSafeInteger(value.expiresAt)||value.expiresAt<=now)throw Error('보존기간이 지난 접속기록 보관본은 일반 복원에 재사용할 수 없습니다.');
 return value;
}

export function assertAccessArchiveRestorable({archive,journal}){
 if(!journal||archive.checkpoint.databaseId!==journal.databaseId)throw Error('접속기록 보관본과 별도 삭제 원장의 DB가 다릅니다.');
 if(journal.verify().some(f=>purgeTypes.includes(f.event.type)&&f.event.archiveId===archive.archiveId))throw Error('파기 대상으로 확정한 접속기록 보관본은 다시 복원할 수 없습니다.');
}

export function purgeAccessArchive({dbPath,archivePath,expectedSha256,journalPath,backupKeyring,auditKeyring,recoveryKeyring,anchor,auditAnchor,reviewReference,confirmed=false,holdsCleared=false,now=Date.now(),beforeJournalAppend}){
 if(!validTime(now))throw Error('실제 파기 검토 시각을 확인해 주세요.');
 if(!ref(reviewReference)||confirmed!==true||holdsCleared!==true||typeof expectedSha256!=='string'||!/^[a-f0-9]{64}$/.test(expectedSha256))throw Error('실제 보존 예외 검토·파기 문서·보관본 해시와 명시적 확인이 필요합니다.');
 if(process.env.READX_RUNTIME==='production'&&(!anchor||!auditAnchor))throw Error('운영 파기에는 별도 삭제 원장·접속기록 기준점이 필요합니다.');
 const file=privateRuntimePath(dbPath),archive=privateRuntimePath(archivePath);assertPlainFile(file);assertPlainFile(archive);assertNotMaintaining(file);
 if(!existsSync(file))throw Error('기존 프로젝트 DB가 필요합니다.');
 const release=acquireFileLease(file+'.maintenance.lock','db-maintenance');let db;
 try{
  db=new DatabaseSync(file);for(const name of ['exam_state','access_log_identity','access_log','access_log_subjects','recovery_state'])if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(name))throw Error('검증된 프로젝트 DB와 별도 삭제 원장이 필요합니다.');
  db.exec('PRAGMA busy_timeout=5000');const access=createAccessLog({db,dbPath:file,keyring:auditKeyring});access.verify(auditAnchor);
  const journal=createRecoveryJournal({db,dbPath:file,journalPath,keyring:recoveryKeyring,anchor,initialize:false,beforeAppend:beforeJournalAppend});journal.sync();
  const pathHash=digest(archive),events=journal.verify().slice(1).map(f=>f.event),completed=e=>events.some(v=>v.type==='access_archive_purged'&&v.operationId===e.operationId);
  let prepared=events.filter(e=>e.type==='access_archive_purge_prepared'&&e.pathHash===pathHash&&e.sha256===expectedSha256).at(-1);
  const record=(event,route,status)=>{
   db.exec('BEGIN IMMEDIATE');try{journal.queue(event);access.append({requestId:randomUUID(),tenantId:'system',at:now,actorId:'local-server-admin',actorRole:'server-administrator',method:'LOCAL',route,resourceId:event.archiveId,category:'audit',status,bytes:0,address:null,addressSource:'local-server',subjects:[],records:0,review:{reference:reviewReference,operationId:event.operationId}});db.exec('COMMIT');access.committed();}catch(e){db.exec('ROLLBACK');throw e;}
   journal.sync();
  };
  if(existsSync(archive)){
   const value=decodeAccessArchive({archivePath:archive,expectedSha256,backupKeyring});access.verifyArchive(value.rows,value.checkpoint);
   if(value.checkpoint.databaseId!==journal.databaseId||value.expiresAt>now)throw Error('이 DB의 보존기간이 끝난 접속기록 보관본만 제거할 수 있습니다.');
   if(!prepared||completed(prepared)){
    prepared={type:'access_archive_purge_prepared',tenantId:'system',subjectId:value.archiveId,archiveId:value.archiveId,operationId:randomUUID(),pathHash,sha256:expectedSha256,expiresAt:value.expiresAt,at:now,reviewReference,holdsCleared:true};
    record(prepared,'local/access-archive.purge-prepared',202);
   }
   assertPlainFile(archive);if(digest(readFileSync(archive))!==expectedSha256)throw Error('검토 중 접속기록 보관 파일이 변경되었습니다.');unlinkSync(archive);
  }else{
   if(!prepared||!uuid(prepared.archiveId)||!uuid(prepared.operationId)||!Number.isSafeInteger(prepared.expiresAt)||prepared.expiresAt>now||prepared.holdsCleared!==true)throw Error('없는 파일에 대한 검증된 만료 파기 준비 기록이 없습니다.');
   if(completed(prepared))return {ok:true,archiveId:prepared.archiveId,operationId:prepared.operationId,alreadyPurged:true,fileAbsent:true,mediaSanitizationCertified:false,otherCopiesDisposed:false,databaseAccessLogsPurged:false};
  }
  if(existsSync(archive))throw Error('만료 접속기록 보관 파일의 제거를 확인하지 못했습니다.');
  record({...prepared,type:'access_archive_purged',at:now,reviewReference},'local/access-archive.file-unlinked',200);
  return {ok:true,archiveId:prepared.archiveId,operationId:prepared.operationId,fileAbsent:true,recoveryReceiptRecorded:true,mediaSanitizationCertified:false,otherCopiesDisposed:false,databaseAccessLogsPurged:false};
 }finally{db?.close();release();}
}

if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const args=process.argv.slice(2),value=f=>{const i=args.indexOf(f);return i<0?'':args[i+1];};
 try{
  const anchor=value('--anchor'),auditAnchor=value('--audit-anchor'),action=value('--action')||'create',common={dbPath:value('--db'),reviewReference:value('--review-reference'),confirmed:args.includes('--confirmed'),auditAnchor:auditAnchor?JSON.parse(readFileSync(auditAnchor,'utf8')):undefined};let result;
  if(action==='create')result=createAccessArchive({...common,outPath:value('--out'),expiresAt:Date.parse(value('--expires-at'))});
  else if(action==='purge')result=purgeAccessArchive({...common,archivePath:value('--archive'),expectedSha256:value('--expected-sha256'),journalPath:value('--journal')||undefined,anchor:anchor?JSON.parse(readFileSync(anchor,'utf8')):undefined,holdsCleared:args.includes('--holds-cleared')});
  else throw Error('접속기록 보관 작업은 create 또는 purge입니다.');
  console.log(JSON.stringify(result,null,2));
 }
 catch(e){console.error('접속기록 보관·파기를 완료하지 못했습니다: '+e.message);process.exitCode=1;}
}
