import {requiredRetained,erasureRecoveryEvent} from './recovery-events.mjs';
import {randomUUID,createHash} from 'node:crypto';
import {createPrivacyVault} from './privacy-vault.mjs';
import {buildRightsBundle,bundleScopes,bundleHash,redactBundle,redactionFields} from './rights-bundle.mjs';
import {ACCESS_META} from '../shared/access-meta.mjs';
import {createLiveErasure} from './live-erasure.mjs';
import {directRestriction} from '../shared/processing-restrictions.mjs';
const fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const text=(v,max=2000)=>typeof v==='string'&&v.trim()&&v.trim().length<=max?v.trim():'';
const reference=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const requestKey=v=>typeof v==='string'&&/^[a-zA-Z0-9-]{16,100}$/.test(v);
const terminal=new Set(['provided','corrected','denied','cancelled','restricted','restriction_lifted','live_data_removed']);
const digest=v=>createHash('sha256').update(v).digest('hex');
const fingerprint=body=>digest(JSON.stringify(Object.fromEntries(Object.entries(body).filter(([k])=>!['currentPassword','mfaCode'].includes(k)).sort(([a],[b])=>a.localeCompare(b)))));
const meta=r=>({subjects:[r.subjectId],records:1,...(r.execution?.kind==='live_erasure'?{review:{operation:'erasure.live',jobId:r.execution.jobId,planHash:r.execution.planHash}}:{})});

export function guardianRelation(s,parent,subject,at){
 if(parent?.role!=='parent'||parent.tenantId!==subject?.tenantId||parent.active===false)return null;
 const v=s.privacy.verifications.find(v=>v.tenantId===parent.tenantId&&v.parentId===parent.id&&v.studentId===subject.id&&!v.revokedAt&&(!v.validUntil||v.validUntil>at));if(v)return v.id;
 return s.organizations.find(o=>o.id===parent.tenantId)?.privacyMode==='synthetic'&&parent.childIds.includes(subject.id)?'synthetic:'+parent.id+':'+subject.id:null;
}

export function createRightsService({db,dbPath,keyring,confirmAccount,processing,recovery}){
 db.exec('CREATE TABLE IF NOT EXISTS privacy_requests (seq INTEGER PRIMARY KEY AUTOINCREMENT,id TEXT NOT NULL UNIQUE,tenant_id TEXT NOT NULL,subject_id TEXT NOT NULL,requester_id TEXT,client_key TEXT NOT NULL,status TEXT NOT NULL,revision INTEGER NOT NULL,received_at INTEGER NOT NULL,payload TEXT NOT NULL,UNIQUE(tenant_id,client_key)); CREATE INDEX IF NOT EXISTS privacy_requests_queue ON privacy_requests(tenant_id,seq)');
 db.exec('CREATE TABLE IF NOT EXISTS privacy_request_bundles (request_id TEXT PRIMARY KEY,tenant_id TEXT NOT NULL,version INTEGER NOT NULL,payload TEXT NOT NULL)');
 const hasRetained=['retained_personal_records','retained_personal_bodies'].some(table=>!!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(table)&&!!db.prepare(`SELECT 1 FROM ${table} LIMIT 1`).get());
 const vault=createPrivacyVault({dbPath,keyring,hasRecords:hasRetained||!!db.prepare('SELECT 1 FROM privacy_requests LIMIT 1').get()||!!db.prepare('SELECT 1 FROM privacy_request_bundles LIMIT 1').get()});
 const erasure=createLiveErasure({db,vault,processing});

 const read=row=>{if(!row)return null;const r=vault.open(JSON.parse(row.payload),{tenantId:row.tenant_id,id:row.id});if(r.id!==row.id||r.tenantId!==row.tenant_id||r.subjectId!==row.subject_id||r.requesterId!==row.requester_id||r.status!==row.status||r.revision!==row.revision||r.receivedAt!==row.received_at||r.clientKey!==row.client_key)throw Error('권리 요청 색인이 일치하지 않습니다.');return {...r,seq:row.seq};};
 const get=(id,tenant)=>read(db.prepare('SELECT * FROM privacy_requests WHERE id=? AND tenant_id=?').get(id,tenant));
 const put=r=>{const copy={...r};delete copy.seq;db.prepare('INSERT INTO privacy_requests(id,tenant_id,subject_id,requester_id,client_key,status,revision,received_at,payload) VALUES(?,?,?,?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET status=excluded.status,revision=excluded.revision,payload=excluded.payload').run(r.id,r.tenantId,r.subjectId,r.requesterId,r.clientKey,r.status,r.revision,r.receivedAt,JSON.stringify(vault.seal(copy,{tenantId:r.tenantId,id:r.id})));};
 const saveBundle=(r,data,version)=>db.prepare('INSERT INTO privacy_request_bundles VALUES(?,?,?,?) ON CONFLICT(request_id) DO UPDATE SET version=excluded.version,payload=excluded.payload').run(r.id,r.tenantId,version,JSON.stringify(vault.seal(data,{tenantId:r.tenantId,id:r.id+':bundle:'+version})));
 const removeBundle=r=>db.prepare('DELETE FROM privacy_request_bundles WHERE request_id=? AND tenant_id=?').run(r.id,r.tenantId);
 db.exec('BEGIN IMMEDIATE');try{for(const row of db.prepare('SELECT * FROM privacy_requests').iterate()){const r=read(row);if(r.bundle?.data){const data=r.bundle.data;r.bundle.version=r.revision||1;saveBundle(r,data,r.bundle.version);delete r.bundle.data;put(r);}}db.exec('COMMIT');}catch(e){db.exec('ROLLBACK');throw e;}
 const member=(s,u,id)=>s.users.find(v=>v.id===id&&v.tenantId===u.tenantId);
 const owner=u=>u.role==='teacher'&&u.isOwner&&!directRestriction(u);
 const allowed=(s,u,r,at)=>owner(u)||r.requesterId===u.id&&(r.subjectId===u.id||r.type==='deletion'&&r.execution?.kind==='live_erasure'||!!guardianRelation(s,u,member(s,u,r.subjectId),at));
 const view=(s,u,r,at)=>({id:r.id,seq:r.seq,type:r.type,subjectId:r.subjectId,subjectName:member(s,u,r.subjectId)?.name||'이전 계정',requesterId:r.requesterId,origin:r.origin,status:r.status,revision:r.revision,receivedAt:r.receivedAt,targetAt:r.targetAt,targetNotice:'내부 처리 목표입니다. 법정 기한과 예외를 별도로 검토해야 합니다.',details:r.details,scopes:r.scopes,correction:r.correction,response:r.response||null,
  history:r.history.map(h=>({at:h.at,action:h.action,response:h.response||null})),execution:r.execution?.kind==='live_erasure'?{kind:'live_erasure',scope:r.execution.scope,at:r.execution.at,jobId:r.execution.jobId,groups:r.execution.groups,reviewDecisions:owner(u)?r.execution.decisions:undefined,remainingUntil:Object.fromEntries(Object.entries(r.execution.residuals||{}).map(([k,v])=>[k,v.until])),archives:r.execution.archiveIds.length,liveVerification:r.execution.liveVerification,mediaAndBackupsVerified:false}:r.execution?{kind:r.execution.kind,scope:r.execution.scope,restrictionId:r.execution.restrictionId,appliedAt:r.execution.appliedAt,liftedAt:r.execution.liftedAt,affectedAccounts:r.execution.affectedAccounts}:null,bundle:r.bundle?{hash:r.bundle.hash,expiresAt:r.bundle.expiresAt,scopes:r.bundle.scopes,delivery:r.verification?.offlineOnly?'offline':'account',available:r.status==='provided'&&r.bundle.expiresAt>at&&(!r.verification?.offlineOnly||owner(u))}:null,
  ...(owner(u)?{verification:r.verification||null,nameBeforeHash:bundleHash({name:member(s,u,r.subjectId)?.name,revision:member(s,u,r.subjectId)?.revision}),currentName:member(s,u,r.subjectId)?.name}:{}),[ACCESS_META]:meta(r)});
 const resolveScopes=values=>{if(!Array.isArray(values)||!values.length||values.length>bundleScopes.length||new Set(values).size!==values.length||values.some(v=>!bundleScopes.includes(v)))fail(400,'열람 범위를 선택해 주세요.');return [...values].sort();};
 const auth=(s,u,body,at)=>confirmAccount({s,u,body,at});
 const verifyLive=(s,u,r,at)=>{
  if(!r.verification)fail(409,'먼저 실제 본인·대리인 확인을 기록해 주세요.');
  if(r.verification.offlineOnly){if(!owner(u))fail(409,'이 사본은 학원의 별도 본인 확인·직접 전달 절차로 제공합니다.');return;}
  const requester=member(s,u,r.requesterId),subject=member(s,u,r.subjectId);
  if(r.requesterId&&r.requesterId!==r.subjectId&&(!requester||guardianRelation(s,requester,subject,at)!==r.verification.guardianRelationId))fail(409,'법정대리인 관계가 변경되었습니다. 확인 절차를 다시 진행해 주세요.');
 };
 const route=({user:u,state:s,path,method,body,at})=>{
  if(u.mustChangePassword)fail(409,'초기 비밀번호를 본인 비밀번호로 변경한 뒤 권리 요청을 확인해 주세요.');
  if(path.startsWith('/rights/retention/')){if(!owner(u))fail(403,'별도 보존 자료는 학원 운영자만 검토합니다.');const denied=auth(s,u,body,at);if(denied)return denied;const result=erasure.retention({u,body,at,path,method});if(result.purged||result.extended)recovery.queue({type:result.purged?'retained_purged':'retained_extended',tenantId:u.tenantId,subjectId:result.subjectId,recordId:result.id,at,...(result.extended?{required:requiredRetained(db,result.id)}:{})});if(result.id)s.audit.push({at,actor:u.id,tenantId:u.tenantId,subjectId:result.subjectId,action:'retention.'+path.split('/').at(-1),id:result.id});return {...result,[ACCESS_META]:{subjects:result.subjectId?[result.subjectId]:[...new Set((result.records||[]).map(r=>r.subjectId))],records:result.records?.length??1,...(result.id||result.json?{review:{operation:'retention.'+path.split('/').at(-1),reference:body.reviewReference,id:result.id||path.split('/').at(-2)}}:{})}};}
  if(path==='/rights/requests'&&method==='GET'||path==='/rights/query'&&method==='POST'){
   if(body.beforeSeq!=null&&(!Number.isSafeInteger(body.beforeSeq)||body.beforeSeq<1))fail(400,'이전 요청 위치를 확인해 주세요.');
   const params=[u.tenantId],clauses=['tenant_id=?'];if(!owner(u)){clauses.push('requester_id=?');params.push(u.id);}if(body.beforeSeq){clauses.push('seq<?');params.push(body.beforeSeq);}
   const scanned=db.prepare('SELECT * FROM privacy_requests WHERE '+clauses.join(' AND ')+' ORDER BY seq DESC LIMIT 201').all(...params).map(read),rows=scanned.filter(r=>allowed(s,u,r,at)),selected=rows.slice(0,50);
   const subjects=s.users.filter(v=>v.tenantId===u.tenantId&&(v.id===u.id||owner(u)||guardianRelation(s,u,v,at))).map(v=>({id:v.id,name:v.name,role:v.role}));
   return {requests:selected.map(r=>view(s,u,r,at)),nextBeforeSeq:rows.length>50?selected.at(-1).seq:scanned.length===201?scanned.at(-1).seq:null,subjects,scopes:bundleScopes,notice:'동의 철회·퇴원과 개인정보 파기는 별개입니다. 삭제·처리정지 요청은 보존 근거와 실제 조치를 확인해야 완료할 수 있습니다.'};
  }
  if(path==='/rights/requests'&&method==='POST'){
   if(!requestKey(body.requestId)||!['access','correction','deletion','restriction'].includes(body.type)||!text(body.details))fail(400,'요청 종류·내용·식별자를 확인해 주세요.');
   const subject=member(s,u,body.subjectId);if(!subject)fail(404,'요청 대상을 찾을 수 없습니다.');
   const offline=body.origin==='offline';if(subject.deletedAt&&!offline)fail(409,'삭제된 계정의 추가 권리 요청은 학원에 별도 접수해 주세요.');if(offline&&!owner(u))fail(403,'방문·서면 접수는 학원 운영자가 기록합니다.');
   if(!offline&&subject.id!==u.id&&!guardianRelation(s,u,subject,at))fail(403,'본인 또는 확인된 법정대리인 계정으로 요청해 주세요.');
   if(u.mustChangePassword)fail(409,'초기 비밀번호를 본인 비밀번호로 변경해 주세요.');
   if(offline&&(!reference(body.intakeReference)||body.identityChecked!==true))fail(400,'외부 접수의 실제 확인과 문서 참조를 기록해 주세요.');
   const clientKey=digest(u.id+':'+body.requestId),fp=fingerprint(body),prior=read(db.prepare('SELECT * FROM privacy_requests WHERE tenant_id=? AND client_key=?').get(u.tenantId,clientKey));
   if(prior){if(prior.fingerprint!==fp)fail(409,'같은 요청 식별자로 내용을 바꿀 수 없습니다.');return {request:view(s,u,prior,at),[ACCESS_META]:meta(prior)};}
   const denied=auth(s,u,body,at);if(denied)return denied;
   const scopes=body.type==='access'?resolveScopes(body.scopes):[];
   let correction=null;if(body.type==='correction'){if(!['profile.name','other'].includes(body.correction?.field)||!text(body.correction.value,body.correction.field==='profile.name'?40:2000))fail(400,'정정 항목과 요청 값을 확인해 주세요.');correction={field:body.correction.field,value:body.correction.value.trim()};}
   const r={id:randomUUID(),tenantId:u.tenantId,subjectId:subject.id,requesterId:offline?null:u.id,submittedBy:u.id,origin:offline?'offline':'account',intakeReference:offline?body.intakeReference:null,clientKey,fingerprint:fp,type:body.type,details:body.details.trim(),scopes,correction,status:'submitted',revision:0,receivedAt:at,targetAt:at+7*86400000,history:[{at,action:'submitted',actorId:u.id}],mutations:[]};put(r);s.audit.push({at,actor:u.id,action:'rights.request.create',id:r.id});return {request:view(s,u,get(r.id,u.tenantId),at),[ACCESS_META]:meta(r)};
  }
  const match=/^\/rights\/requests\/([^/]+)(?:\/(verify|preview|resolve|download|appeal|cancel|restriction-preview|erasure-preview|lift))?$/.exec(path);if(!match)fail(404,'권리 요청을 찾을 수 없습니다.');
  const r=get(match[1],u.tenantId);if(!r||!allowed(s,u,r,at))fail(404,'권리 요청을 찾을 수 없습니다.');
  if(!match[2]&&method==='GET')return {request:view(s,u,r,at),[ACCESS_META]:meta(r)};
  if(method!=='POST')fail(405,'요청 방법을 확인해 주세요.');const action=match[2];
  if(['verify','preview','resolve','restriction-preview','erasure-preview','lift'].includes(action)&&!owner(u))fail(403,'학원 운영자만 검토할 수 있습니다.');
  if(action==='erasure-preview'){if(r.type!=='deletion'||!['verified','action_required'].includes(r.status))fail(409,'확인된 삭제 요청을 선택해 주세요.');verifyLive(s,u,r,at);const denied=auth(s,u,body,at);if(denied)return denied;return {plan:erasure.preview({state:s,subject:member(s,u,r.subjectId),request:r,body,at,actor:u}),[ACCESS_META]:meta(r)};}
  if(action==='restriction-preview'){
   if(r.type!=='restriction'||!r.verification)fail(409,'확인된 처리정지 요청을 선택해 주세요.');verifyLive(s,u,r,at);const denied=auth(s,u,body,at);if(denied)return denied;
   if(body.mode==='lift'&&(!r.execution||r.execution.liftedAt))fail(409,'적용한 처리정지 이력을 확인해 주세요.');
   return {impact:processing.impact({state:s,subject:member(s,u,r.subjectId),request:r,at,actor:u,mode:body.mode==='lift'?'lift':'apply'}),[ACCESS_META]:meta(r)};
  }
  if(action==='download'){
   if(r.status!=='provided'||!r.bundle||r.bundle.expiresAt<=at)fail(410,'제공 사본이 없거나 만료되었습니다. 학원에 재검토를 요청해 주세요.');verifyLive(s,u,r,at);const denied=auth(s,u,body,at);if(denied)return denied;
   const row=db.prepare('SELECT * FROM privacy_request_bundles WHERE request_id=? AND tenant_id=?').get(r.id,r.tenantId);if(!row||row.version!==r.bundle.version)throw Error('제공 사본과 요청의 버전이 일치하지 않습니다.');const data=vault.open(JSON.parse(row.payload),{tenantId:r.tenantId,id:r.id+':bundle:'+row.version});if(bundleHash(data)!==r.bundle.hash)throw Error('제공 사본의 무결성이 일치하지 않습니다.');
   return {json:JSON.stringify(data),hash:r.bundle.hash,expiresAt:r.bundle.expiresAt,subjectId:r.subjectId,[ACCESS_META]:meta(r)};
  }
  if(action==='preview'){
   if(!['verified','provided'].includes(r.status)||r.type!=='access')fail(409,'확인된 열람 요청을 선택해 주세요.');verifyLive(s,u,r,at);const denied=auth(s,u,body,at);if(denied)return denied;
   const scopes=resolveScopes(body.scopes);if(scopes.some(v=>!r.scopes.includes(v)))fail(400,'요청받은 범위 안에서 선택해 주세요.');const bundle=buildRightsBundle({db,state:s,subject:member(s,u,r.subjectId),scopes});
   if(Buffer.byteLength(JSON.stringify(bundle))>5*1024*1024)fail(413,'한 사본은 5MB 이내로 범위를 나누어 검토해 주세요.');
   return {bundle,sourceHash:bundleHash(bundle),redactableFields:redactionFields(bundle),revision:r.revision,[ACCESS_META]:meta(r)};
  }
  if(!requestKey(body.mutationId))fail(400,'처리 요청 식별자가 필요합니다.');const fp=fingerprint(body),previous=r.mutations.find(m=>m.id===body.mutationId);
  if(previous){if(previous.fingerprint!==fp)fail(409,'같은 처리 식별자로 내용을 바꿀 수 없습니다.');return {request:view(s,u,r,at),[ACCESS_META]:meta(r)};}
  if(body.revision!==r.revision)fail(409,'요청 이력이 변경되었습니다. 새로고침해 주세요.');if(r.mutations.length>=100)fail(409,'추가 접수로 처리 이력을 분리해 주세요.');const denied=auth(s,u,body,at);if(denied)return denied;
  const subject=member(s,u,r.subjectId);
  if(action==='verify'){
   if(r.status==='live_data_removed'||r.status==='cancelled'||!reference(body.reference)||!['in_person','signed_document','existing_guardian'].includes(body.method)||body.confirmed!==true)fail(400,'실제 본인·대리인 확인 방법과 문서 참조를 기록해 주세요.');
   const requester=member(s,u,r.requesterId),relation=r.requesterId&&r.requesterId!==r.subjectId?guardianRelation(s,requester,subject,at):null;
   const offlineOnly=body.offlineOnly===true;if(offlineOnly&&body.method==='existing_guardian')fail(400,'별도 전달은 실제 대면·서면 확인을 기록해 주세요.');
   if(r.requesterId&&r.requesterId!==r.subjectId&&!relation&&!offlineOnly)fail(409,'법정대리인 확인이 유효하지 않습니다. 외부 접수 절차로 본인·대리인을 다시 확인해 주세요.');
   r.verification={method:body.method,reference:body.reference,guardianRelationId:relation,offlineOnly,by:u.id,at};r.status=r.execution?.kind==='live_erasure'?'live_data_removed':r.execution&&!r.execution.liftedAt?'restricted':'verified';r.response=null;removeBundle(r);delete r.bundle;
  }else if(action==='resolve'){
   if(!['verified','action_required'].includes(r.status)||!text(body.response)||!reference(body.reviewReference)||body.reviewed!==true)fail(400,'확인된 요청의 실제 검토·결과 안내·근거 참조를 기록해 주세요.');verifyLive(s,u,r,at);
   if(body.outcome==='provide'&&r.type==='access'){
    const scopes=resolveScopes(body.scopes);if(scopes.some(v=>!r.scopes.includes(v)))fail(400,'요청 범위를 확인해 주세요.');const source=buildRightsBundle({db,state:s,subject,scopes});if(Buffer.byteLength(JSON.stringify(source))>5*1024*1024)fail(413,'한 사본은 5MB 이내로 범위를 나누어 검토해 주세요.');if(body.sourceHash!==bundleHash(source))fail(409,'열람 대상 자료가 바뀌었습니다. 최신 사본을 다시 검토해 주세요.');
    if((scopes.length<r.scopes.length||body.redactions?.length)&&!reference(body.omissionReference))fail(400,'일부 제외 사유의 검토 문서 참조가 필요합니다.');const data=redactBundle(source,body.redactions||[]),version=r.revision+1;saveBundle(r,data,version);r.bundle={version,hash:bundleHash(data),scopes,expiresAt:at+7*86400000,reviewedBy:u.id,reviewReference:body.reviewReference};r.status='provided';
   }else if(body.outcome==='erase_live'&&r.type==='deletion'){r.execution=erasure.apply({state:s,subject,request:r,body,at,actor:u});r.status='live_data_removed';
   }else if(body.outcome==='apply_restriction'&&r.type==='restriction'){
    r.execution=processing.change({state:s,subject,request:r,body,at,actor:u,mode:'apply'});r.status='restricted';
   }else if(body.outcome==='apply_name'&&r.type==='correction'&&r.correction.field==='profile.name'){
    if(body.nameBeforeHash!==bundleHash({name:subject.name,revision:subject.revision}))fail(409,'현재 이름이 변경되었습니다. 다시 확인해 주세요.');subject.name=r.correction.value;subject.revision++;delete subject.deviceDraftKey;for(const [key,session]of Object.entries(s.sessions))if(session.userId===subject.id)delete s.sessions[key];r.status='corrected';
   }else if(body.outcome==='denied')r.status='denied';
   else if(body.outcome==='deferred')r.status='deferred';
   else if(body.outcome==='needs_action')r.status='action_required';
   else fail(409,'이 요청은 아직 실제 조치를 완료한 것으로 처리할 수 없습니다.');
   r.response=body.response.trim();r.reviewReference=body.reviewReference;
  }else if(action==='lift'){
   if(r.execution?.kind!=='restriction'||r.execution.liftedAt||!text(body.response))fail(409,'현재 적용된 정지와 해제 안내를 확인해 주세요.');verifyLive(s,u,r,at);
   r.execution=processing.change({state:s,subject,request:r,body,at,actor:u,mode:'lift'});r.response=body.response.trim();r.status='restriction_lifted';
  }else if(action==='appeal'){
   if(r.requesterId!==u.id)fail(403,'접수 계정 본인이 이의를 제기할 수 있습니다.');
   if(!['provided','corrected','denied','deferred','action_required','restricted','restriction_lifted','live_data_removed'].includes(r.status)||!text(body.message))fail(400,'이의 제기 내용을 작성해 주세요.');r.status='submitted';r.details+='\n\n[이의 제기] '+body.message.trim();removeBundle(r);delete r.bundle;delete r.verification;r.response=null;
  }else if(action==='cancel'){
   if(r.requesterId!==u.id||terminal.has(r.status)||r.execution&&!r.execution.liftedAt)fail(409,'현재 본인이 제출한 미완료 요청만 취소할 수 있습니다. 적용된 정지는 별도 해제 절차가 필요합니다.');r.status='cancelled';removeBundle(r);delete r.bundle;
  }else fail(404,'처리 요청을 찾을 수 없습니다.');
  r.revision++;r.history.push({at,action,actorId:u.id,...(r.response?{response:r.response}:{})});r.mutations.push({id:body.mutationId,fingerprint:fp});put(r);if(action==='resolve'&&body.outcome==='erase_live')recovery.queue(erasureRecoveryEvent(db,r,subject.role));s.audit.push({at,actor:u.id,action:'rights.'+action,id:r.id});return {request:view(s,u,r,at),[ACCESS_META]:meta(r)};
 };
 return {route};
}
