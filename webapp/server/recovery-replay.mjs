import {createHash,randomUUID} from 'node:crypto';
import {eraseOwned} from './erase-owned.mjs';
import {createPrivacyVault} from './privacy-vault.mjs';
const hash=s=>createHash('sha256').update(s).digest('hex');
const fail=message=>{throw Object.assign(Error(message),{code:'RECOVERY_REPLAY_REQUIRED'});};
const reference=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
export function replayRecovery({db,dbPath,journal,dataKeyring,at=Date.now(),reviewReference}){
 if(!reference(reviewReference))fail('실제 복원·삭제 재처리 검토 문서 번호가 필요합니다.');
 const frames=journal.verify(),events=frames.slice(1).map(f=>f.event),head=frames.at(-1),pending=db.prepare('SELECT COUNT(*) n FROM recovery_events').get().n;
 if(pending>head.seq)fail('별도 원장에 전달되지 않은 DB 사건이 있습니다. 원본의 전달 상태를 먼저 복구해 주세요.');
 const vault=createPrivacyVault({dbPath,keyring:dataKeyring,hasRecords:!!db.prepare('SELECT 1 FROM privacy_requests LIMIT 1').get()||!!db.prepare('SELECT 1 FROM retained_personal_records LIMIT 1').get()});
 db.exec('BEGIN IMMEDIATE');
 try{
  const s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body),holds=new Map();if(new Set(s.users.map(u=>u.id)).size!==s.users.length)fail('복원 계정의 식별자가 중복되었습니다.');
  for(const event of events){
   if(['backup_purge_prepared','backup_purged','access_archive_purge_prepared','access_archive_purged'].includes(event.type))continue;
   if(!['erase_owned','retained_purged','retained_extended'].includes(event.type)||!event.tenantId||!event.subjectId)fail('삭제 원장의 사건 범위가 올바르지 않습니다.');
   if(event.type==='erase_owned'){
    if(!['teacher','student','parent'].includes(event.role)||!event.requestId||!event.jobId||event.execution?.kind!=='live_erasure'||!Array.isArray(event.required))fail('삭제 원장에 필요한 복원 정보가 없습니다.');
    const u=s.users.find(u=>u.id===event.subjectId&&u.tenantId===event.tenantId),tombstone={id:event.subjectId,tenantId:event.tenantId,role:event.role,name:'삭제된 계정',username:'deleted.'+event.subjectId,active:false,childIds:[],classIds:[],isOwner:false,revision:(u?.revision||0)+1,deletedAt:event.at,erasureId:event.jobId,processingRestriction:{id:'recovery-'+event.eventId,requestId:event.requestId,at:event.at,by:'recovery',scope:'ordinary_service'}};
    eraseOwned({db,state:s,tenantId:event.tenantId,subjectId:event.subjectId,tombstone,keepRequestId:event.requestId});
    const row=db.prepare('SELECT * FROM privacy_requests WHERE id=? AND tenant_id=?').get(event.requestId,event.tenantId);
    let r;if(row){r=vault.open(JSON.parse(row.payload),{tenantId:event.tenantId,id:event.requestId});if(r.id!==row.id||r.tenantId!==row.tenant_id||r.subjectId!==event.subjectId||r.type!=='deletion'||r.revision!==row.revision||r.status!==row.status)fail('복원할 삭제 요청의 색인이 일치하지 않습니다.');}
    else r={id:event.requestId,tenantId:event.tenantId,subjectId:event.subjectId,requesterId:event.requesterId||null,submittedBy:'recovery',origin:'recovery',clientKey:hash('recovery:'+event.requestId),fingerprint:hash(event.eventId),type:'deletion',details:'별도 삭제 원장에 따라 격리 복원 중 운영 자료를 다시 제거했습니다. 이전 원본 확인·안내 증거는 별도 보관 자료로 점검해야 합니다.',scopes:[],correction:null,revision:0,receivedAt:event.at,targetAt:at,history:[],mutations:[]};
    if(r.execution?.jobId!==event.jobId){r.status='live_data_removed';r.execution=event.execution;r.revision++;r.response='운영 자료 삭제 재적용. 매체·백업·원본 통지 증거는 별도 검토 대상입니다.';r.history.push({at,action:'recovery.reapplied',actorId:'local-server-admin',reference:reviewReference});}
    db.prepare('INSERT INTO privacy_requests(id,tenant_id,subject_id,requester_id,client_key,status,revision,received_at,payload) VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET status=excluded.status,revision=excluded.revision,payload=excluded.payload').run(r.id,r.tenantId,r.subjectId,r.requesterId,r.clientKey,r.status,r.revision,r.receivedAt,JSON.stringify(vault.seal(r,{tenantId:r.tenantId,id:r.id})));
    for(const required of event.required)holds.set(required.id,{...required,tenantId:event.tenantId,subjectId:event.subjectId});
   }else if(event.type==='retained_extended')holds.set(event.recordId,{...event.required,tenantId:event.tenantId,subjectId:event.subjectId});
   else{holds.delete(event.recordId);db.prepare('DELETE FROM retained_personal_bodies WHERE id=? AND tenant_id=?').run(event.recordId,event.tenantId);db.prepare('DELETE FROM retained_personal_records WHERE id=? AND tenant_id=?').run(event.recordId,event.tenantId);}
  }
  for(const required of holds.values()){
   const meta=db.prepare('SELECT * FROM retained_personal_records WHERE id=? AND tenant_id=?').get(required.id,required.tenantId),body=db.prepare('SELECT payload FROM retained_personal_bodies WHERE id=? AND tenant_id=?').get(required.id,required.tenantId);
   if(!meta||!body||meta.subject_id!==required.subjectId||hash(meta.payload)!==required.metadataHash||hash(body.payload)!==required.bodyHash)fail('필요한 최신 별도 보존 자료가 백업에 없습니다. 해당 자료가 포함된 검증 백업을 복원하기 전에는 재개할 수 없습니다.');
   const m=vault.open(JSON.parse(meta.payload),{tenantId:required.tenantId,id:'retained:'+required.id}),b=vault.open(JSON.parse(body.payload),{tenantId:required.tenantId,id:'retained-body:'+required.id+':1'});
   if(m.id!==required.id||m.subjectId!==required.subjectId||m.tenantId!==required.tenantId||m.expiresAt!==meta.expires_at||m.revision!==meta.revision||m.dataHash!==hash(JSON.stringify(b.data))||m.records!==b.data.length||b.id!==m.id||b.group!==m.group||b.jobId!==m.jobId)fail('별도 보존 자료의 본문 검증이 실패했습니다.');
  }
  // Restored sessions, passwords, authenticator generations and guardian grants
  // must never silently reactivate permissions from an old backup.
  s.sessions={};s.recoveryCodes=[];s.mfaRecoveries=[];
  for(const u of s.users){delete u.deviceDraftKey;delete u.pendingMfa;if(u.deletedAt)continue;u.restoreCredentialHold={at,reference:reviewReference};u.mustChangePassword=true;u.revision++;if(u.role==='parent')u.childIds=[];if(u.mfa){u.mfa.recoveryRequired=true;u.mfa.version=randomUUID();u.mfa.backups=[];}}
  for(const v of s.privacy.verifications)if(!v.revokedAt){v.revokedAt=at;v.revokedBy='recovery';v.revokeReason='복원 후 실제 법정대리인 재확인 필요';}
  db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));
  db.exec('DELETE FROM recovery_events');for(const f of frames.slice(1))db.prepare('INSERT INTO recovery_events(seq,event_id,event) VALUES(?,?,?)').run(f.seq,f.event.eventId,JSON.stringify(f.event));
  db.prepare('UPDATE recovery_state SET seq=?,hash=?,database_id=? WHERE id=1').run(head.seq,head.hash,journal.databaseId);db.exec('COMMIT');
  return {ok:true,databaseId:journal.databaseId,journalSeq:head.seq,eraseEvents:events.filter(e=>e.type==='erase_owned').length,requiredRetainedRecords:holds.size,credentialsHeld:true,guardianReverificationRequired:true};
 }catch(e){db.exec('ROLLBACK');throw e;}
}
