import {knownTables} from './live-erasure.mjs';
import {DatabaseSync} from 'node:sqlite';
import {createHash,randomUUID} from 'node:crypto';
import {existsSync,readFileSync,statSync,openSync,fsyncSync,closeSync,writeFileSync,unlinkSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve,join} from 'node:path';
import {createAccessLog} from './access-log.mjs';
import {readAccessArchive,assertAccessArchiveRestorable} from './access-archive.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';
import {replayRecovery} from './recovery-replay.mjs';
import {createPrivacyVault} from './privacy-vault.mjs';
import {erasureRecoveryEvent} from './recovery-events.mjs';
import {ownedTables} from './erase-owned.mjs';
import {acquireFileLease,assertPlainFile,canonicalFile,privateRuntimePath} from './maintenance-lock.mjs';
const ref=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const integrity=db=>{const rows=db.prepare('PRAGMA integrity_check').all();if(rows.length!==1||Object.values(rows[0])[0]!=='ok')throw Error('SQLite 무결성 검증이 실패했습니다.');};
const checkpoint=db=>{const r=db.prepare('PRAGMA wal_checkpoint(TRUNCATE)').get();if(r.busy!==0)throw Error('다른 DB 연결이 WAL 정리를 막고 있습니다. 작업을 완료로 처리하지 않습니다.');};
function adopt({db,dbPath,journal,dataKeyring,at,reviewReference}){
 const s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body),vault=createPrivacyVault({dbPath,keyring:dataKeyring,hasRecords:true}),known=new Set(journal.verify().slice(1).filter(f=>f.event.type==='erase_owned').map(f=>f.event.jobId));let adopted=0;
 db.exec('BEGIN IMMEDIATE');try{
  for(const u of s.users.filter(u=>u.deletedAt&&!known.has(u.erasureId))){
   let r;for(const row of db.prepare('SELECT * FROM privacy_requests WHERE tenant_id=? AND subject_id=?').all(u.tenantId,u.id)){const value=vault.open(JSON.parse(row.payload),{tenantId:u.tenantId,id:row.id});if(value.id!==row.id||value.subjectId!==row.subject_id||value.tenantId!==row.tenant_id||value.status!==row.status||value.revision!==row.revision)throw Error('이전 삭제 요청 색인 검증이 실패했습니다.');if(value.execution?.kind==='live_erasure'&&value.execution.jobId===u.erasureId)r=value;}
   if(!r||!r.execution.liveVerification)throw Error('이전 삭제 계정과 검증된 원본 삭제 요청을 연결할 수 없습니다.');
   if(ownedTables.some(table=>db.prepare(`SELECT 1 FROM ${table} WHERE tenant_id=? AND json_extract(body,'$.studentId')=? LIMIT 1`).get(u.tenantId,u.id))||['attempts','followups','attendance','consultations','enrollments'].some(key=>s[key].some(v=>v.studentId===u.id)))throw Error('이전 삭제 계정의 운영 자료가 남아 있어 자동 이관할 수 없습니다.');
   journal.queue({...erasureRecoveryEvent(db,r,u.role),origin:'adopted_existing',adoptedAt:at,reviewReference});adopted++;
  }
  db.exec('COMMIT');return adopted;
 }catch(e){db.exec('ROLLBACK');throw e;}
}
export function maintainDatabase({dbPath,journalPath,recoveryKeyring,dataKeyring,auditKeyring,backupKeyring,accessArchivePath,accessArchiveSha256,anchor,auditAnchor,action,reviewReference,confirmed=false,initializeAnchorBaseline=false,now=Date.now()}){
 if(!['verify','sync','compact','replay','adopt','checkpoint'].includes(action)||!ref(reviewReference)||confirmed!==true)throw Error('작업 종류·실제 복원 검토 문서 번호·명시적 확인이 필요합니다.');
 if(initializeAnchorBaseline&&(action!=='adopt'||existsSync(dbPath+'.recovery.ndjson')||existsSync(journalPath||process.env.READX_RECOVERY_JOURNAL||'')))throw Error('초기 기준점 검토는 기존 원장을 덮어쓰는 용도로 사용할 수 없습니다.');
 if(process.env.READX_RUNTIME==='production'&&(!anchor||!auditAnchor)&&!initializeAnchorBaseline)throw Error('운영 복구에는 별도 보관한 삭제 원장·접속기록 기준점이 필요합니다.');
 if((accessArchivePath||accessArchiveSha256)&&(action!=='replay'||!accessArchivePath||!accessArchiveSha256||!auditAnchor))throw Error('접속기록 병합은 별도 기준점·보관본 해시를 지정한 격리 복원에서만 가능합니다.');
 const file=canonicalFile(dbPath);assertPlainFile(file);if(!existsSync(file))throw Error('기존 프로젝트 DB가 필요합니다.');
 const release=acquireFileLease(file+'.maintenance.lock','db-maintenance');let db;
 const pending=file+'.restore.pending';if(['replay','adopt'].includes(action)){assertPlainFile(pending);if(!existsSync(pending)){const fd=openSync(pending,'wx',0o600);try{writeFileSync(fd,JSON.stringify({v:1,kind:'restore-pending',at:now,reference:reviewReference})+'\n');fsyncSync(fd);}finally{closeSync(fd);}}}
 try{
  db=new DatabaseSync(file);if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name='exam_state'").get()||!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name='access_log_identity'").get())throw Error('확인된 프로젝트 DB가 아닙니다.');db.exec('PRAGMA busy_timeout=5000; PRAGMA secure_delete=ON; BEGIN IMMEDIATE; COMMIT');integrity(db);
  if(['replay','adopt'].includes(action)&&db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").all().some(r=>!knownTables.has(r.name)))throw Error('새 저장 영역의 복원 후 삭제 기준을 먼저 검토해야 합니다.');
  const access=createAccessLog({db,dbPath:file,keyring:auditKeyring});let accessArchive;
  const journal=createRecoveryJournal({db,dbPath:file,journalPath,keyring:recoveryKeyring,anchor,initialize:action==='adopt',adoptLegacy:action==='replay'||action==='adopt'});
  if(accessArchivePath){
   const saved=readAccessArchive({archivePath:accessArchivePath,expectedSha256:accessArchiveSha256,backupKeyring,now});
   assertAccessArchiveRestorable({archive:saved,journal});
   db.exec('BEGIN IMMEDIATE');try{accessArchive=access.mergeArchive(saved.rows,saved.checkpoint);access.verify(auditAnchor);db.exec('COMMIT');access.committed();}catch(e){db.exec('ROLLBACK');throw e;}
  }else access.verify(auditAnchor);
  let result={};
  if(action==='adopt')journal.sync();
  if(action==='adopt')result.adopted=adopt({db,dbPath:file,journal,dataKeyring,at:now,reviewReference});
  if(action==='replay')result.replay=replayRecovery({db,dbPath:file,journal,dataKeyring,at:now,reviewReference});
  const head=journal.sync();
  db.exec('BEGIN IMMEDIATE');access.append({requestId:randomUUID(),tenantId:'system',at:now,actorId:'local-server-admin',actorRole:'server-administrator',method:'LOCAL',route:'local/recovery-'+action,resourceId:null,category:'audit',status:200,bytes:0,address:null,addressSource:'local-server',subjects:[],records:0,review:{reference:reviewReference,journalSeq:head.seq}});db.exec('COMMIT');access.committed();
  if(['compact','replay'].includes(action)){checkpoint(db);db.exec('VACUUM');checkpoint(db);result.sqliteVacuumCompleted=true;}
  integrity(db);access.verify();const recoveryCheckpoint=journal.checkpoint(now),accessCheckpoint=access.checkpoint(now);checkpoint(db);db.close();db=null;
  const fd=openSync(file,'r+');try{fsyncSync(fd);}finally{closeSync(fd);}
  const walBytes=existsSync(file+'-wal')?statSync(file+'-wal').size:0;if(walBytes!==0)throw Error('정리 후 WAL이 비어 있지 않습니다.');
  if(['replay','adopt'].includes(action)){assertPlainFile(pending);unlinkSync(pending);}
  return {ok:true,action,recoveryCheckpoint,accessCheckpoint,...(accessArchive?{accessArchive}:{}),anchorBaselineInitialized:initializeAnchorBaseline,databaseId:head.databaseId,journalSeq:head.seq,journalHash:head.hash,sqliteIntegrity:true,walBytes,databaseSha256:createHash('sha256').update(readFileSync(file)).digest('hex'),...result,mediaSanitizationCertified:false,externalBackupsDisposed:false};
 }finally{db?.close();release();}
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const args=process.argv.slice(2),value=f=>{const i=args.indexOf(f);return i<0?'':args[i+1];};
 try{const anchor=value('--anchor'),auditAnchor=value('--audit-anchor');const result=maintainDatabase({dbPath:value('--db'),journalPath:value('--journal')||undefined,action:value('--action'),accessArchivePath:value('--access-archive')||undefined,accessArchiveSha256:value('--access-archive-sha256')||undefined,reviewReference:value('--review-reference'),confirmed:args.includes('--confirmed'),initializeAnchorBaseline:args.includes('--initialize-anchor-baseline'),anchor:anchor?JSON.parse(readFileSync(anchor,'utf8')):undefined,auditAnchor:auditAnchor?JSON.parse(readFileSync(auditAnchor,'utf8')):undefined});const directory=value('--checkpoint-dir');if(directory){const recoveryFile=privateRuntimePath(join(directory,'recovery-anchor.json')),auditFile=privateRuntimePath(join(directory,'audit-anchor.json'));if(existsSync(recoveryFile)||existsSync(auditFile))throw Error('기준점 파일을 덮어쓰지 않습니다. 새 보관 디렉터리를 선택해 주세요.');for(const [path,data]of [[recoveryFile,result.recoveryCheckpoint],[auditFile,result.accessCheckpoint]]){const fd=openSync(path,'wx',0o600);try{writeFileSync(fd,JSON.stringify(data,null,2)+'\n');fsyncSync(fd);}finally{closeSync(fd);}}result.checkpointFiles={recovery:recoveryFile,audit:auditFile};}console.log(JSON.stringify(result,null,2));}
 catch(e){console.error('복구·정리 검증을 완료하지 못했습니다: '+e.message);process.exitCode=1;}
}
