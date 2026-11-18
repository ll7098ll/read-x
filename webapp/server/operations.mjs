import {DatabaseSync} from 'node:sqlite';
import {randomUUID} from 'node:crypto';
import {existsSync,lstatSync,statSync,writeFileSync,readFileSync,mkdtempSync,readdirSync,unlinkSync,rmdirSync} from 'node:fs';
import {join,resolve,basename,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import {readOperationsPolicy,readOperationsAnchor,operationKinds,opsError,validTime} from './operations-policy.mjs';
import {createOperationsLedger} from './operations-ledger.mjs';
import {assertPlainFile,acquireFileLease,privateRuntimePath} from './maintenance-lock.mjs';
import {maintainDatabase} from './recovery-maintenance.mjs';
import {createEncryptedBackup,restoreEncryptedBackup,verifyEncryptedBackup} from './encrypted-backup.mjs';
import {createAccessArchive,readAccessArchive,assertAccessArchiveRestorable} from './access-archive.mjs';
import {createAccessLog} from './access-log.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';

const knownError=e=>typeof e?.code==='string'&&/^(?:OPS_[A-Z_]+|MAINTENANCE_REQUIRED|RECOVERY_SYNC_REQUIRED|RECOVERY_REPLAY_REQUIRED)$/.test(e.code)?e.code:'JOB_EXECUTION_FAILED';
const invalid=()=>opsError('OPS_LEDGER_INVALID','운영 작업의 시작·완료 기록을 확인해 주세요.');
function history(frames){
 const jobs=Object.fromEntries(operationKinds.map(k=>[k,{last:null,success:null,running:null}]));let approved=null,heartbeat=null;
 for(const {event:e}of frames.slice(1)){
  if(e.type==='policy_approved'){if(e.revision!==(approved?.revision||0)+1||typeof e.policyHash!=='string')throw invalid();approved=e;continue;}
  if(e.type==='heartbeat'){heartbeat=e.at;continue;}
  const j=jobs[e.job];if(!j)throw invalid();
  if(e.type==='job_started'){if(j.running)throw invalid();j.running=e;j.last=e;}
  else{if(!j.running||j.running.attemptId!==e.attemptId)throw invalid();j.running=null;j.last=e;if(e.type==='job_succeeded')j.success=e;}
 }
 return {jobs,approved,heartbeat};
}
function context({policyPath=process.env.READX_OPS_POLICY,recoveryKeyring,opsAnchor,now=Date.now(),initialize=false,checkPolicy=true}={}){
 const config=readOperationsPolicy(policyPath,{now}),{policy}=config;
 opsAnchor||=process.env.READX_OPS_ANCHOR?readOperationsAnchor(process.env.READX_OPS_ANCHOR):undefined;
 if(process.env.READX_RUNTIME==='production'&&!initialize&&!opsAnchor)throw opsError('OPS_CUSTODY_REQUIRED','운영 실행 기록의 별도 기준점이 필요합니다.');
 const ledger=createOperationsLedger({policy,keyring:recoveryKeyring,anchor:opsAnchor,initialize,at:now}),frames=ledger.read();
 if(frames.at(-1).event.at>now)throw opsError('OPS_CLOCK_INVALID','운영 기록과 서버 시각을 확인해 주세요.');
 const state=history(frames);
 if(checkPolicy&&(state.approved?.policyHash!==config.hash||state.approved?.revision!==policy.revision))throw opsError('OPS_POLICY_MISMATCH','정책 변경을 실제 검토하고 새 개정으로 승인해 주세요.');
 return {...config,ledger,state,externalCheckpoint:!!opsAnchor};
}
function sourceIdentity(policy){
 let db;try{db=new DatabaseSync(policy.dbPath,{readOnly:true});if(db.prepare('SELECT database_id FROM access_log_identity WHERE id=1').get()?.database_id!==policy.databaseId)throw Error();}
 catch{throw opsError('OPS_DATABASE_MISMATCH','검토한 정책과 운영 DB가 일치하지 않습니다.');}finally{db?.close();}
}
const sourceOptions=(policy,keys)=>({...keys,dbPath:policy.dbPath,journalPath:policy.journalPath,anchor:readOperationsAnchor(policy.recoveryAnchorPath),auditAnchor:readOperationsAnchor(policy.auditAnchorPath),reviewReference:policy.reviewReference,confirmed:true});
const recoverInterrupted=(ledger,now)=>{for(const [job,j]of Object.entries(history(ledger.read()).jobs))if(j.running)ledger.append({type:'job_interrupted',job,attemptId:j.running.attemptId,at:now,errorCode:'OPS_PREVIOUS_WORKER_INTERRUPTED'});};

export function approveOperationsPolicy({policyPath,recoveryKeyring,opsAnchor,confirmed=false,initialize=false,now=Date.now(),...keys}={}){
 if(confirmed!==true)throw opsError('OPS_REVIEW_REQUIRED','실제 정책·작업 담당 검토를 확인한 후 승인해 주세요.');
 const {policy}=readOperationsPolicy(policyPath,{now}),release=acquireFileLease(policy.ledgerPath+'.run.lock','operations-worker');
 try{
  if(initialize&&existsSync(policy.ledgerPath))throw opsError('OPS_ALREADY_INITIALIZED','기존 운영 실행 기록을 초기화하지 않습니다.');
  sourceIdentity(policy);maintainDatabase({...sourceOptions(policy,{...keys,recoveryKeyring}),action:'verify',now});
  const c=context({policyPath,recoveryKeyring,opsAnchor,now,initialize,checkPolicy:false});
  if(policy.revision!==(c.state.approved?.revision||0)+1)throw opsError('OPS_POLICY_MISMATCH','이전 승인에 이어지는 개정 번호가 필요합니다.');
  recoverInterrupted(c.ledger,now);c.ledger.append({type:'policy_approved',at:now,revision:policy.revision,policyHash:c.hash,reviewReference:policy.reviewReference});
  return {ok:true,policyId:policy.id,revision:policy.revision,checkpoint:c.ledger.checkpoint(now),schedulerInstalled:false,externalNotificationsConfigured:false};
 }finally{release();}
}

function artifactPath(policy,a){
 if(!a||!['backup','audit'].includes(a.kind)||typeof a.file!=='string'||!/^ops-[a-f0-9-]{36}(?:-drill)?\.(?:readxbackup|readxaudit)$/.test(a.file)||!a.file.endsWith(a.kind==='backup'?'.readxbackup':'.readxaudit')||!/^[a-f0-9]{64}$/.test(a.sha256))throw invalid();
 return privateRuntimePath(join(policy[a.kind==='backup'?'backupDirectory':'auditDirectory'],a.file));
}
function present(policy,a){try{const file=artifactPath(policy,a);assertPlainFile(file);return statSync(file).size===a.bytes;}catch{return false;}}
const artifactsFrom=state=>[...new Map(Object.values(state.jobs).flatMap(j=>j.success?.receipt?.artifacts||[]).map(a=>[a.kind+':'+a.file,a])).values()];
async function verifyArtifacts(policy,state,keys,at){
 const artifacts=artifactsFrom(state);if(!artifacts.length)return 0;let db;
 try{
  db=new DatabaseSync(policy.dbPath);db.exec('PRAGMA busy_timeout=5000; BEGIN');
  const access=createAccessLog({db,dbPath:policy.dbPath,keyring:keys.auditKeyring,readOnly:true}),journal=createRecoveryJournal({db,dbPath:policy.dbPath,journalPath:policy.journalPath,keyring:keys.recoveryKeyring,anchor:readOperationsAnchor(policy.recoveryAnchorPath),initialize:false});
  const events=journal.verify().slice(1).map(f=>f.event);
  for(const a of artifacts){
   if(!present(policy,a))throw opsError('OPS_ARTIFACT_MISSING','보관 파일의 부재·크기 변경을 확인해 주세요.');
   const path=artifactPath(policy,a);
   if(a.kind==='backup'){
    const verified=await verifyEncryptedBackup({archivePath:path,expectedSha256:a.sha256,backupKeyring:keys.backupKeyring,databaseId:policy.databaseId,now:at});
    if(events.some(e=>['backup_purge_prepared','backup_purged'].includes(e.type)&&e.backupId===verified.backupId))throw opsError('OPS_ARTIFACT_REVOKED','파기 대상으로 확정한 사본입니다.');
   }else{
    const saved=readAccessArchive({archivePath:path,expectedSha256:a.sha256,backupKeyring:keys.backupKeyring,now:at});access.verifyArchive(saved.rows,saved.checkpoint);assertAccessArchiveRestorable({archive:saved,journal});
   }
  }
  return artifacts.length;
 }finally{db?.close();}
}

export function readOperationsStatus({policyPath=process.env.READX_OPS_POLICY,recoveryKeyring,opsAnchor,dbPath,databaseId,now=Date.now()}={}){
 if(!policyPath)return {configured:false,operationalChecksPassed:false,jobs:[],externalNotificationsConfigured:false,notice:'운영 정책·실행 기록이 아직 연결되지 않았습니다.'};
 const c=context({policyPath,recoveryKeyring,opsAnchor,now}),{policy,state}=c;
 if(dbPath&&privateRuntimePath(dbPath)!==policy.dbPath||databaseId&&databaseId!==policy.databaseId)throw opsError('OPS_DATABASE_MISMATCH','현재 운영 서버의 정책을 확인해 주세요.');
 const workerStale=state.heartbeat==null||now-state.heartbeat>policy.heartbeatMaxAgeMs;
 const jobs=operationKinds.map(kind=>{
  const j=state.jobs[kind],rule=policy.jobs[kind],outcome=j.last?.type||'not_run',stale=!j.success||now-j.success.at>rule.maxAgeMs;
  const artifacts=j.success?.receipt?.artifacts||[],artifactsPresent=artifacts.every(a=>present(policy,a)),runningOverdue=!!j.running&&now-j.running.at>policy.runningMaxAgeMs;
  return {kind,outcome,lastStartedAt:j.running?.at||j.last?.startedAt||null,lastFinishedAt:j.last&&j.last.type!=='job_started'?j.last.at:null,lastSucceededAt:j.success?.at||null,nextDueAt:j.last&&['job_failed','job_interrupted'].includes(j.last.type)?j.last.at+policy.retryAfterMs:j.success?j.success.at+rule.everyMs:now,stale,runningOverdue,artifactsPresent,errorCode:j.last?.errorCode||null,recordedVerification:kind==='restore_drill'?j.success?.receipt?.restoredAndChecked===true:!!j.success};
 });
 return {configured:true,operationalChecksPassed:!workerStale&&jobs.every(j=>!j.stale&&!j.runningOverdue&&j.artifactsPresent&&j.outcome==='job_succeeded'),policyRevision:policy.revision,lastWorkerAt:state.heartbeat,workerStale,jobs,externalCheckpoint:c.externalCheckpoint,externalNotificationsConfigured:false,notice:'기록된 작업 결과와 현재 파일 존재·크기 검사입니다. 파일 내용 인증은 검증 작업에서 수행합니다. 실제 외부 보관·경보 전달·운영 적합성을 인증하지 않습니다.'};
}

function removeDrill(dir,nonce,root){
 if(resolve(dir).startsWith(resolve(root)+sep)!==true||!basename(dir).startsWith('.readx-ops-drill-')||lstatSync(dir).isSymbolicLink()||JSON.parse(readFileSync(join(dir,'stage.json'),'utf8')).nonce!==nonce)throw opsError('OPS_DRILL_CLEANUP_REQUIRED','복원 점검 사본의 경계를 확인해 주세요.');
 const allowed=new Set(['stage.json','restored.sqlite','restored.sqlite-wal','restored.sqlite-shm','restored.sqlite.restore.pending']);
 for(const name of readdirSync(dir))if(!allowed.has(name))throw opsError('OPS_DRILL_CLEANUP_REQUIRED','알 수 없는 복원 점검 파일이 있습니다.');
 for(const name of readdirSync(dir)){const file=join(dir,name);assertPlainFile(file);unlinkSync(file);}rmdirSync(dir);
}

export async function runOperations({policyPath=process.env.READX_OPS_POLICY,opsAnchor,now=Date.now,beforeJob,...keys}={}){
 const c=context({policyPath,recoveryKeyring:keys.recoveryKeyring,opsAnchor,now:now()}),{policy,ledger}=c,release=acquireFileLease(policy.ledgerPath+'.run.lock','operations-worker');
 const results=[],tickArtifacts={};
 try{
  sourceIdentity(policy);recoverInterrupted(ledger,now());ledger.append({type:'heartbeat',at:now()});const state=history(ledger.read());
  const due=Object.fromEntries(operationKinds.map(k=>{const j=state.jobs[k],retry=j.last&&['job_failed','job_interrupted'].includes(j.last.type);return [k,retry?now()-j.last.at>=policy.retryAfterMs:!j.success||now()-j.success.at>=policy.jobs[k].everyMs];}));
  if(due.backup||due.audit||due.restore_drill)due.verify=true;
  const makeBackup=async(attemptId,suffix='')=>{
   const made=await createEncryptedBackup({...sourceOptions(policy,keys),outPath:join(policy.backupDirectory,`ops-${attemptId}${suffix}.readxbackup`),expiresAt:now()+policy.jobs.backup.retentionMs,now:now()});
   return {kind:'backup',file:basename(made.path),sha256:made.sha256,bytes:made.bytes,expiresAt:made.expiresAt,id:made.backupId,auditCheckpoint:made.auditCheckpoint};
  };
  const makeAudit=(attemptId,suffix='')=>{
   const made=createAccessArchive({...sourceOptions(policy,keys),outPath:join(policy.auditDirectory,`ops-${attemptId}${suffix}.readxaudit`),expiresAt:now()+policy.jobs.audit.retentionMs,now:now()});
   return {kind:'audit',file:basename(made.path),sha256:made.sha256,bytes:made.bytes,expiresAt:made.expiresAt,id:made.archiveId,checkpoint:made.checkpoint};
  };
  for(const job of operationKinds){
   if(!due[job])continue;
   if(job!=='verify'&&results.some(r=>r.job==='verify'&&!r.ok)){results.push({job,ok:false,blockedBy:'verify'});continue;}
   const attemptId=randomUUID(),startedAt=now();ledger.append({type:'job_started',job,attemptId,at:startedAt});let receipt;
   try{
    beforeJob?.(job);
    if(job==='verify'){const verified=maintainDatabase({...sourceOptions(policy,keys),action:'verify',now:now()});receipt={sourceIntegrity:true,journalSeq:verified.journalSeq,artifactHashesChecked:await verifyArtifacts(policy,state,keys,now())};}
    if(job==='backup'){tickArtifacts.backup=await makeBackup(attemptId);receipt={artifacts:[tickArtifacts.backup]};}
    if(job==='audit'){tickArtifacts.audit=makeAudit(attemptId);receipt={artifacts:[tickArtifacts.audit]};}
    if(job==='restore_drill'){
     const backup=tickArtifacts.backup||await makeBackup(attemptId,'-drill'),audit=tickArtifacts.audit||makeAudit(attemptId,'-drill');
     const dir=mkdtempSync(join(policy.drillDirectory,'.readx-ops-drill-')),nonce=randomUUID(),target=join(dir,'restored.sqlite');writeFileSync(join(dir,'stage.json'),JSON.stringify({kind:'readx-operations-drill',nonce,attemptId}),{flag:'wx',mode:0o600});
     await restoreEncryptedBackup({...sourceOptions(policy,keys),archivePath:artifactPath(policy,backup),targetDbPath:target,expectedSha256:backup.sha256,accessArchivePath:artifactPath(policy,audit),accessArchiveSha256:audit.sha256,auditAnchor:audit.checkpoint,now:now()});
     const db=new DatabaseSync(target,{readOnly:true});try{const s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);if(Object.keys(s.sessions).length||s.recoveryCodes.length||s.users.some(u=>!u.deletedAt&&!u.restoreCredentialHold||u.deviceDraftKey||u.role==='parent'&&u.childIds.length)||s.privacy.verifications.some(v=>!v.revokedAt))throw opsError('OPS_RESTORE_CHECK_FAILED','복원 계정·보호자 재확인 상태가 맞지 않습니다.');createAccessLog({db,dbPath:target,keyring:keys.auditKeyring,readOnly:true}).verify(audit.checkpoint);}finally{db.close();}
     removeDrill(dir,nonce,policy.drillDirectory);receipt={restoredAndChecked:true,plaintextCopyRemoved:true,mediaSanitizationCertified:false,artifacts:[backup,audit]};
    }
    ledger.append({type:'job_succeeded',job,attemptId,at:now(),startedAt,receipt});results.push({job,ok:true});
   }catch(e){const errorCode=knownError(e);ledger.append({type:'job_failed',job,attemptId,at:now(),startedAt,errorCode});results.push({job,ok:false,errorCode});}
  }
  ledger.append({type:'heartbeat',at:now()});const status=readOperationsStatus({policyPath,recoveryKeyring:keys.recoveryKeyring,opsAnchor,now:now()});
  return {ok:results.every(r=>r.ok)&&status.operationalChecksPassed,results,status,checkpoint:ledger.checkpoint(now()),schedulerInstalled:false,externalNotificationsConfigured:false};
 }finally{release();}
}

if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const args=process.argv.slice(2),value=f=>{const i=args.indexOf(f);return i<0?'':args[i+1];};
 try{
  const options={policyPath:value('--policy')||process.env.READX_OPS_POLICY,opsAnchor:value('--ops-anchor')?readOperationsAnchor(value('--ops-anchor')):undefined},action=value('--action');let result;
  if(action==='initialize'||action==='approve')result=approveOperationsPolicy({...options,initialize:action==='initialize',confirmed:args.includes('--confirmed')});
  else if(action==='run')result=await runOperations(options);
  else if(action==='status')result=readOperationsStatus(options);
  else throw opsError('OPS_ACTION_INVALID','작업은 initialize, approve, run 또는 status입니다.');
  console.log(JSON.stringify(result,null,2));if(result.ok===false||result.operationalChecksPassed===false)process.exitCode=1;
 }catch(e){console.error(JSON.stringify({ok:false,errorCode:knownError(e),notice:'운영 정책·기록·작업 실패를 확인해 주세요. 원본·보관 사본과 증거를 보전하세요.'}));process.exitCode=1;}
}
