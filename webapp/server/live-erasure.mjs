import {eraseOwned} from './erase-owned.mjs';
import {createHash,randomUUID} from 'node:crypto';
import {directRestriction,parentDependencies} from '../shared/processing-restrictions.mjs';
const fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const hash=v=>createHash('sha256').update(JSON.stringify(v)).digest('hex');
const ref=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const text=v=>typeof v==='string'&&v.trim().length>=3&&v.trim().length<=1000;
export const erasureGroups=['profile','learning','pilot','exams','attendance','consultations','privacy','enrollment','rights'];
export const residualGroups=['access_log','rights_receipt','authored_records'];
export const knownTables=new Set(['exam_state','access_log_identity','access_log','access_log_subjects','learning_assignments','learning_runs','learning_releases','learning_approvals','learning_placements','learning_courses','pilot_sessions','pilot_runs','pilot_item_reviews','pilot_calibrations','privacy_requests','privacy_request_bundles','retained_personal_records','retained_personal_bodies','recovery_events','recovery_state']);
const tableGroups={learning:['learning_runs','learning_releases','learning_placements','learning_courses'],pilot:['pilot_runs']};
const profileFields=['id','tenantId','role','name','username','classId','classIds','className','childIds','isOwner','active','studentStatus','validUntil','revision','registrationReference','registrationAt','consentStatus'];

// This removes the selected subject's owned data from active application tables.
// Retained evidence is separately encrypted and never joins ordinary dashboards.
// SQLite/WAL/media and external backups require a separate verified disposal run.
export function createLiveErasure({db,vault,processing}){
 db.exec('CREATE TABLE IF NOT EXISTS retained_personal_records (id TEXT PRIMARY KEY,tenant_id TEXT NOT NULL,subject_id TEXT NOT NULL,job_id TEXT NOT NULL,group_id TEXT NOT NULL,expires_at INTEGER NOT NULL,revision INTEGER NOT NULL,payload TEXT NOT NULL); CREATE INDEX IF NOT EXISTS retained_personal_due ON retained_personal_records(tenant_id,expires_at,id); CREATE TABLE IF NOT EXISTS retained_personal_bodies (id TEXT PRIMARY KEY,tenant_id TEXT NOT NULL,payload TEXT NOT NULL)');
 const readRetained=row=>{
  if(!row)return null;const r=vault.open(JSON.parse(row.payload),{tenantId:row.tenant_id,id:'retained:'+row.id});
  if(r.id!==row.id||r.tenantId!==row.tenant_id||r.subjectId!==row.subject_id||r.jobId!==row.job_id||r.group!==row.group_id||r.expiresAt!==row.expires_at||r.revision!==row.revision||!Number.isSafeInteger(r.records)||r.records<1)throw Error('별도 보존 자료의 색인·무결성이 일치하지 않습니다.');return r;
 };
 const readBody=r=>{const row=db.prepare('SELECT payload FROM retained_personal_bodies WHERE id=? AND tenant_id=?').get(r.id,r.tenantId);if(!row)throw Error('별도 보존 본문이 없습니다.');const body=vault.open(JSON.parse(row.payload),{tenantId:r.tenantId,id:'retained-body:'+r.id+':1'});if(body.id!==r.id||body.subjectId!==r.subjectId||body.jobId!==r.jobId||body.group!==r.group||hash(body.data)!==r.dataHash||body.data.length!==r.records)throw Error('별도 보존 본문의 무결성이 일치하지 않습니다.');return body.data;};
 const rows=(table,tenant)=>db.prepare(`SELECT id,body FROM ${table} WHERE tenant_id=? ORDER BY id`).all(tenant).map(row=>({...row,value:JSON.parse(row.body)}));
 const snapshot=(s,subject,request)=>{
  const id=subject.id,tenant=subject.tenantId,buckets=Object.fromEntries(erasureGroups.map(g=>[g,[]]));
  buckets.profile=[{source:'users',key:id,value:Object.fromEntries(profileFields.filter(k=>Object.hasOwn(subject,k)).map(k=>[k,subject[k]]))}];
  for(const [group,tables]of Object.entries(tableGroups))for(const table of tables)for(const row of rows(table,tenant).filter(r=>r.value.studentId===id))buckets[group].push({source:table,key:row.id,value:row.value});
  for(const key of ['attempts','followups','attendance','consultations','enrollments'])for(const value of s[key].filter(v=>(!v.tenantId||v.tenantId===tenant)&&v.studentId===id))buckets[key==='attempts'||key==='followups'?'exams':key==='enrollments'?'enrollment':key].push({source:key,key:value.id||hash(value),value});
  for(const key of ['candidates','verifications','consents'])for(const value of s.privacy[key].filter(v=>v.tenantId===tenant&&(v.studentId===id||v.parentId===id)))buckets.privacy.push({source:'privacy.'+key,key:value.id,value});
  for(const row of db.prepare('SELECT * FROM privacy_requests WHERE tenant_id=? AND subject_id=? AND id<>? ORDER BY seq').all(tenant,id,request.id)){
   const r=vault.open(JSON.parse(row.payload),{tenantId:tenant,id:row.id});if(r.id!==row.id||r.tenantId!==tenant||r.subjectId!==id||r.revision!==row.revision||r.status!==row.status||r.requesterId!==row.requester_id||r.clientKey!==row.client_key||r.receivedAt!==row.received_at)throw Error('삭제 검토 요청 색인이 일치하지 않습니다.');
   buckets.rights.push({source:'privacy_requests',key:r.id,value:r});
   const bundle=db.prepare('SELECT * FROM privacy_request_bundles WHERE request_id=? AND tenant_id=?').get(r.id,tenant);if(bundle){if(bundle.version!==r.bundle?.version)throw Error('삭제 검토 사본 버전이 일치하지 않습니다.');const data=vault.open(JSON.parse(bundle.payload),{tenantId:tenant,id:r.id+':bundle:'+bundle.version});if(hash(data)!==r.bundle.hash)throw Error('삭제 검토 사본이 일치하지 않습니다.');buckets.rights.push({source:'privacy_request_bundles',key:r.id,value:data});}
  }
  if(Buffer.byteLength(JSON.stringify(buckets))>32*1024*1024)fail(413,'한 번의 삭제 검토 범위를 초과했습니다. 운영자의 별도 분할·검증 절차가 필요합니다.');
  const membership={exam:s.assignments.filter(a=>a.tenantId===tenant&&a.studentIds.includes(id)).map(a=>({id:a.id,studentIds:a.studentIds})),pilot:rows('pilot_sessions',tenant).filter(r=>r.value.studentIds.includes(id)).map(r=>({id:r.id,value:r.value})),reading:rows('learning_assignments',tenant).filter(r=>r.value.studentIds.includes(id)).map(r=>({id:r.id,value:r.value})),guardians:s.users.filter(u=>u.tenantId===tenant&&u.childIds.includes(id)).map(u=>({id:u.id,revision:u.revision,childIds:u.childIds}))};
  return {buckets,membership};
 };
 const validatePolicy=(policy,residuals,at)=>{
  const date=v=>Number.isSafeInteger(v)&&v>at&&v<=8640000000000000;
  if(!policy||Array.isArray(policy)||Object.keys(policy).length!==erasureGroups.length||erasureGroups.some(g=>!Object.hasOwn(policy,g)))fail(400,'모든 자료 종류의 삭제·별도 보존 결정을 확인해 주세요.');
  for(const g of erasureGroups){const p=policy[g];if(!p||!['delete','retain'].includes(p.action)||!ref(p.reference)||!text(p.reason)||p.action==='retain'&&!date(p.until)||p.action==='delete'&&p.until!=null)fail(400,'자료별 검토 근거·사유와 보존 종료일을 확인해 주세요.');}
  if(!residuals||Array.isArray(residuals)||Object.keys(residuals).length!==residualGroups.length||residualGroups.some(g=>!Object.hasOwn(residuals,g)||!ref(residuals[g]?.reference)||!text(residuals[g]?.reason)||!date(residuals[g]?.until)))fail(400,'접속기록·권리 처리·공동 기록의 별도 보존 근거와 종료일 검토가 필요합니다.');
 };
 const plan=({state:s,subject,request,body,at,actor})=>{
  if(subject.role==='parent'&&parentDependencies(s,subject,at).length)fail(409,'연결 자녀와 기존 정지 영향이 있습니다. 정당한 보호자 인계·확인·동의와 정지 범위 검토를 먼저 진행해 주세요.');
  if(subject.deletedAt)fail(409,'이미 운영 자료를 삭제한 계정입니다. 처리 결과와 별도 보존 자료를 확인해 주세요.');
  if(subject.role==='teacher'&&subject.isOwner&&!s.users.some(u=>u.id!==subject.id&&u.tenantId===subject.tenantId&&u.role==='teacher'&&u.isOwner&&u.active!==false&&!directRestriction(u)))fail(409,'마지막 운영자는 권한을 인계한 뒤 삭제할 수 있습니다.');
  validatePolicy(body.policy,body.residuals,at);
  if(db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").all().some(r=>!knownTables.has(r.name)))fail(409,'새 저장 영역의 개인정보 삭제 기준을 먼저 검토해야 합니다.');
  const data=snapshot(s,subject,request),stop=!directRestriction(subject)?processing.impact({state:s,subject,request,at,actor}):null;
  const sourceHash=hash({requestId:request.id,revision:request.revision,subjectRevision:subject.revision,data,stop:stop?.impactHash||subject.processingRestriction.id});
  const planHash=hash({sourceHash,policy:body.policy,residuals:body.residuals});
  return {subjectId:subject.id,subjectName:subject.name,sourceHash,planHash,groups:erasureGroups.map(group=>({group,count:data.buckets[group].length,action:body.policy[group].action,...(body.policy[group].action==='retain'?{until:body.policy[group].until}:{})})),stop,notice:'대상 계정의 운영 자료를 제거하고 검토한 자료는 별도 암호화 보존합니다. 접속기록·권리 처리·공동 기록, 디스크·백업과 이미 반출된 자료의 파기는 별도 검증이 필요합니다.',_data:data};
 };
 const preview=c=>{const p=plan(c);delete p._data;return p;};
 const apply=c=>{
  const {state:s,subject,request,body,at,actor}=c;
  if(body.confirmed!==true||!ref(body.freeTextReviewReference)||body.freeTextReviewed!==true||!ref(body.backupReviewReference)||body.backupReviewed!==true)fail(400,'공동 문서의 자유 서술·외부 사본과 백업의 실제 검토 참조가 필요합니다.');
  const p=plan(c);if(body.planHash!==p.planHash)fail(409,'삭제 대상 또는 보존 결정이 바뀌었습니다. 최신 범위를 다시 확인해 주세요.');
  const jobId=randomUUID(),archiveIds=[];
  for(const group of erasureGroups)if(body.policy[group].action==='retain'&&p._data.buckets[group].length){
   const data=p._data.buckets[group],decision=body.policy[group],r={id:randomUUID(),tenantId:subject.tenantId,subjectId:subject.id,jobId,group,revision:0,createdAt:at,expiresAt:decision.until,reference:decision.reference,reason:decision.reason.trim(),history:[{at,by:actor.id,reference:decision.reference,until:decision.until,action:'retained'}],records:data.length,dataHash:hash(data)};
   db.prepare('INSERT INTO retained_personal_records VALUES(?,?,?,?,?,?,?,?)').run(r.id,r.tenantId,r.subjectId,r.jobId,r.group,r.expiresAt,r.revision,JSON.stringify(vault.seal(r,{tenantId:r.tenantId,id:'retained:'+r.id})));db.prepare('INSERT INTO retained_personal_bodies VALUES(?,?,?)').run(r.id,r.tenantId,JSON.stringify(vault.seal({id:r.id,subjectId:r.subjectId,jobId:r.jobId,group:r.group,data},{tenantId:r.tenantId,id:'retained-body:'+r.id+':1'})));archiveIds.push(r.id);
  }
  if(p.stop)processing.change({state:s,subject,request,body:{confirmed:true,retentionReference:body.policy.profile.reference,impactHash:p.stop.impactHash},at,actor});
  const tombstone={id:subject.id,tenantId:subject.tenantId,role:subject.role,name:'삭제된 계정',username:'deleted.'+subject.id,active:false,childIds:[],classIds:[],isOwner:false,revision:subject.revision+1,deletedAt:at,erasureId:jobId,processingRestriction:subject.processingRestriction};
  eraseOwned({db,state:s,tenantId:subject.tenantId,subjectId:subject.id,tombstone,keepRequestId:request.id});
  const remaining=snapshot(s,tombstone,request);if(erasureGroups.some(g=>g!=='profile'&&remaining.buckets[g].length)||remaining.membership.exam.length||remaining.membership.reading.length||remaining.membership.pilot.length||remaining.membership.guardians.length)throw Error('운영 자료 삭제 후 검증이 실패했습니다.');
  s.audit.push({at,tenantId:subject.tenantId,actor:actor.id,subjectId:subject.id,action:'erasure.live.apply',id:jobId,requestId:request.id});
  return {kind:'live_erasure',jobId,scope:'owned_operational_data',at,planHash:p.planHash,groups:p.groups,decisions:structuredClone(body.policy),archiveIds,residuals:structuredClone(body.residuals),freeTextReviewReference:body.freeTextReviewReference,backupReviewReference:body.backupReviewReference,liveVerification:true,mediaAndBackupsVerified:false};
 };
 const retention=({u,body,at,path,method})=>{
  if(path==='/rights/retention/query'&&method==='POST'){
   if(body.before!=null&&(typeof body.before!=='string'||body.before.length>100))fail(400,'목록 위치를 확인해 주세요.');
   const rows=db.prepare('SELECT * FROM retained_personal_records WHERE tenant_id=? AND id>? ORDER BY id LIMIT 51').all(u.tenantId,body.before||'').map(readRetained);
   return {records:rows.slice(0,50).map(r=>({id:r.id,subjectId:r.subjectId,jobId:r.jobId,group:r.group,createdAt:r.createdAt,expiresAt:r.expiresAt,expired:r.expiresAt<=at,revision:r.revision,records:r.records,reference:r.reference,reason:r.reason})),next:rows.length>50?rows[49].id:null};
  }
  const m=/^\/rights\/retention\/([^/]+)\/(download|extend|purge)$/.exec(path);if(!m||method!=='POST')fail(404,'별도 보존 자료를 찾을 수 없습니다.');
  const r=readRetained(db.prepare('SELECT * FROM retained_personal_records WHERE id=? AND tenant_id=?').get(m[1],u.tenantId));if(!r)fail(404,'별도 보존 자료를 찾을 수 없습니다.');
  if(m[2]==='download'){if(r.expiresAt<=at)fail(410,'보존기간이 끝나 제공하지 않습니다. 만료 파기 검토를 진행해 주세요.');if(!ref(body.reviewReference)||body.reviewed!==true)fail(400,'별도 보존 목적의 실제 검토 참조가 필요합니다.');return {json:JSON.stringify({group:r.group,jobId:r.jobId,data:readBody(r)}),subjectId:r.subjectId};}
  if(body.revision!==r.revision)fail(409,'별도 보존 결정이 변경되었습니다. 다시 확인해 주세요.');
  if(!ref(body.reviewReference)||body.reviewed!==true)fail(400,'실제 보존·파기 검토 참조가 필요합니다.');
  if(m[2]==='purge'){if(r.expiresAt>at)fail(409,'보존기간이 남았습니다. 근거 변경에 따른 별도 검토가 필요합니다.');db.prepare('DELETE FROM retained_personal_bodies WHERE id=? AND tenant_id=?').run(r.id,u.tenantId);db.prepare('DELETE FROM retained_personal_records WHERE id=? AND tenant_id=?').run(r.id,u.tenantId);return {purged:true,scope:'live_retained_row',subjectId:r.subjectId,id:r.id,mediaAndBackupsVerified:false};}
  if(!Number.isSafeInteger(body.until)||body.until<=Math.max(r.expiresAt,at)||body.until>8640000000000000||!text(body.reason))fail(400,'연장 종료일과 구체적인 실제 보존 근거를 확인해 주세요.');
  r.history||=[];r.history.push({at,by:u.id,reference:body.reviewReference,until:body.until,previousUntil:r.expiresAt,action:'extended'});r.expiresAt=body.until;r.reference=body.reviewReference;r.reason=body.reason.trim();r.revision++;db.prepare('UPDATE retained_personal_records SET expires_at=?,revision=?,payload=? WHERE id=? AND tenant_id=?').run(r.expiresAt,r.revision,JSON.stringify(vault.seal(r,{tenantId:r.tenantId,id:'retained:'+r.id})),r.id,u.tenantId);return {extended:true,subjectId:r.subjectId,id:r.id};
 };
 return {preview,apply,retention};
}
