import {createHash,randomUUID} from 'node:crypto';
import {restrictionIds,RESTRICTION_IDS,directRestriction,processingBlocked,parentDependencies} from '../shared/processing-restrictions.mjs';
import {canTeachClass} from '../shared/organization.mjs';
const fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const hash=v=>createHash('sha256').update(JSON.stringify(v)).digest('hex');
const reference=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const rightsPath=path=>path.startsWith('/rights/')||path==='/privacy/notice';
const authPath=path=>['/session','/login','/logout','/setup','/recover','/account/password'].includes(path)||path.startsWith('/auth/mfa/');
const legalPath=path=>path.startsWith('/privacy/')||path.startsWith('/audit/')||path.startsWith('/rights/');
export function createProcessingService({db}){
 const all=(table,tenant)=>db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r=>JSON.parse(r.body));
 const put=(table,r,tenant)=>db.prepare(`UPDATE ${table} SET body=? WHERE id=? AND tenant_id=?`).run(JSON.stringify(r),tenant+':'+r.id,tenant);
 const authorized=(s,u,id,classId)=>{const subject=s.users.find(v=>v.id===id&&v.tenantId===u.tenantId);return subject&&(u.id===id||u.role==='teacher'&&(canTeachClass(u,subject.classId)||classId&&canTeachClass(u,classId))||u.role==='parent'&&u.childIds.includes(id));};
 const assertSubject=(s,u,id,at,classId)=>{if(restrictionIds(s,at).has(id)&&authorized(s,u,id,classId))throw processingBlocked();};
 const before=({s,u,path,method,body,at})=>{
  if(!u||authPath(path)||rightsPath(path))return;
  const blocked=restrictionIds(s,at);
  if(path==='/privacy/verifications'&&u.role==='teacher'&&u.isOwner&&[body?.studentId,body?.parentId].some(id=>s.users.some(v=>v.id===id&&v.tenantId===u.tenantId&&v.deletedAt)))throw processingBlocked();
  if(blocked.has(u.id)&&!(u.role==='parent'&&(path==='/privacy/dashboard'||path==='/privacy/withdraw')))throw processingBlocked();
  if(path==='/privacy/verifications'&&blocked.has(body?.parentId))throw processingBlocked();
  if(legalPath(path)&&path!=='/privacy/consents')return;
  if(path==='/org/dashboard')return;
  for(const id of [body?.studentId,body?.parentId,...(Array.isArray(body?.studentIds)?body.studentIds:[])].filter(Boolean))assertSubject(s,u,id,at);
  const account=/^\/org\/accounts\/([^/]+)/.exec(path);if(account)assertSubject(s,u,account[1],at);
  const record=/^\/(attempts|followups)\/([^/]+)/.exec(path);if(record){const r=s[record[1]].find(v=>v.id===record[2]&&v.tenantId===u.tenantId);if(r)assertSubject(s,u,r.studentId,at,r.classId||s.attempts.find(a=>a.id===r.attemptId)?.classId);}
  const run=/^\/learning\/runs\/([^/]+)/.exec(path);if(run){const row=db.prepare('SELECT body FROM learning_runs WHERE id=? AND tenant_id=?').get(u.tenantId+':'+run[1],u.tenantId);if(row){const r=JSON.parse(row.body),a=db.prepare('SELECT body FROM learning_assignments WHERE id=? AND tenant_id=?').get(u.tenantId+':'+r.assignmentId,u.tenantId);assertSubject(s,u,r.studentId,at,a&&JSON.parse(a.body).classId);}}
  if(path==='/org/consultations'&&body.id){const r=s.consultations.find(v=>v.id===body.id&&v.tenantId===u.tenantId);if(r)assertSubject(s,u,r.studentId,at);}
 };
 const stateForRead=(s,u,path,method,at)=>{
  if(authPath(path)||rightsPath(path)||legalPath(path))return s;
  const read=method==='GET'||path==='/overview'||path==='/overview/export'||path==='/overview/print';if(!read)return s;
  const blocked=restrictionIds(s,at);if(!blocked.size)return s;
  const operational=path==='/org/dashboard',users=s.users.filter(v=>operational||!blocked.has(v.id)).map(v=>({...v,childIds:v.childIds.filter(id=>!blocked.has(id))}));
  return {...s,[RESTRICTION_IDS]:blocked,users,assignments:s.assignments.map(a=>({...a,studentIds:a.studentIds.filter(id=>!blocked.has(id))})).filter(a=>a.studentIds.length),attempts:s.attempts.filter(a=>!blocked.has(a.studentId)),followups:s.followups.filter(f=>!blocked.has(f.studentId)),attendance:s.attendance.filter(r=>!blocked.has(r.studentId)),consultations:s.consultations.filter(r=>!blocked.has(r.studentId))};
 };
 const sanitize=(result,s,path,at)=>{
  if(authPath(path)||legalPath(path))return result;
  const blocked=restrictionIds(s,at);if(!blocked.size)return result;
  const blockedNames=new Set(s.users.filter(u=>blocked.has(u.id)&&u.role==='teacher').map(u=>u.name));
  const walk=(v,key='')=>{
   if(Array.isArray(v))return v.filter(x=>typeof x!=='string'||!blocked.has(x)).map(x=>walk(x,key));
   if(!v||typeof v!=='object')return key==='teacherName'&&blockedNames.has(v)?'이전 담당 교사':v;
   if(path==='/org/dashboard'&&key==='audit')return v;
   if(v.studentId&&blocked.has(v.studentId))throw processingBlocked();
   if(v.id&&blocked.has(v.id)&&s.users.some(u=>u.id===v.id)){
    if(path!=='/org/dashboard')throw processingBlocked();
    return {id:v.id,name:v.name,role:v.role,active:v.active,revision:v.revision,classId:v.classId,className:v.className,childIds:[],processingRestricted:true};
   }
   const out={};for(const [k,x]of Object.entries(v)){if(['by','createdBy','teacherId','reviewedBy','actorId'].includes(k)&&blocked.has(x))continue;out[k]=walk(x,k);}for(const sym of Object.getOwnPropertySymbols(v))out[sym]=v[sym];return out;
  };
  return walk(result);
 };
 const revokedUsers=(s,subject,changed,actorId)=>{const touched=new Set([subject.id,...changed]),classes=new Set(s.users.filter(v=>changed.has(v.id)&&v.role==='student').map(v=>v.classId));return new Set([...touched,...s.users.filter(v=>v.tenantId===subject.tenantId&&(v.role==='parent'&&v.childIds.some(id=>changed.has(id))||v.role==='teacher'&&(v.isOwner||v.classIds?.some(id=>classes.has(id))))).map(v=>v.id)].filter(id=>id!==actorId));};
 const impact=({state:s,subject,request,at,mode='apply',actor})=>{
  const beforeIds=restrictionIds(s,at),copy={...subject},users=s.users.map(v=>v.id===subject.id?copy:v);
  if(mode==='apply')copy.processingRestriction={id:'preview'};else delete copy.processingRestriction;
  const afterIds=restrictionIds({...s,users},at),changed=[...(mode==='apply'?afterIds:beforeIds)].filter(id=>!(mode==='apply'?beforeIds:afterIds).has(id)).sort(),affected=new Set([subject.id,...changed]);
  const rows=['learning_runs','learning_releases','learning_placements','learning_courses','pilot_runs'].map(table=>[table,all(table,subject.tenantId).filter(r=>affected.has(r.studentId)).map(r=>({id:r.id||r.studentId,revision:r.revision||0,status:r.status||null,publishedAt:r.publishedAt||null})).sort((a,b)=>a.id.localeCompare(b.id))]);
  const revoked=revokedUsers(s,subject,new Set(changed),actor?.id),sessions=Object.entries(s.sessions).filter(([,v])=>revoked.has(v.userId)).map(([id,v])=>({id,userId:v.userId})).sort((a,b)=>a.id.localeCompare(b.id));
  const exams=s.attempts.filter(a=>a.tenantId===subject.tenantId&&affected.has(a.studentId)).map(a=>({id:a.id,status:a.status,savedAt:a.lastSavedAt||null,deadlineAt:a.deadlineAt}));
  const proof={mode,requestId:request.id,requestRevision:request.revision,subjectId:subject.id,revision:subject.revision,restrictionId:subject.processingRestriction?.id||null,changed,rows,sessions,exams};
  return {mode,subjectId:subject.id,subjectName:subject.name,scope:'ordinary_service',changedAccounts:changed.map(id=>{const u=s.users.find(v=>v.id===id);return {id,name:u?.name,role:u?.role};}),activeSessions:sessions.length,examRecords:exams.length,readingRecords:rows[0][1].length,pilotRecords:rows[4][1].length,notice:'일반 서비스 이용·조회·배정·제출·공개를 제한합니다. 권리 처리·보안 감사·검토한 보존 목적은 별도이며 개인정보 파기를 뜻하지 않습니다.',impactHash:hash(proof)};
 };
 const change=({state:s,subject,request,body,at,mode='apply',actor})=>{
  if(!reference(body.retentionReference)||body.confirmed!==true)fail(400,'보존·제한 범위 검토 문서와 실제 확인이 필요합니다.');
  if(mode==='apply'&&directRestriction(subject))fail(409,'이미 일반 처리가 정지된 계정입니다. 기존 정지 이력을 확인해 주세요.');
  if(mode==='lift'&&(!directRestriction(subject)||subject.processingRestriction.id!==request.execution?.restrictionId||!reference(body.requesterReference)))fail(409,'현재 정지 이력과 요청자의 해제 의사 확인 문서를 확인해 주세요.');
  if(mode==='apply'&&subject.role==='teacher'&&subject.isOwner&&!s.users.some(v=>v.id!==subject.id&&v.tenantId===subject.tenantId&&v.isOwner&&v.active!==false&&!directRestriction(v)))fail(409,'마지막 운영자는 권한을 인계한 뒤 정지할 수 있습니다.');
  const preview=impact({state:s,subject,request,at,mode,actor});if(body.impactHash!==preview.impactHash)fail(409,'처리 영향이 바뀌었습니다. 최신 범위를 다시 확인해 주세요.');
  const beforeIds=restrictionIds(s,at),old=subject.processingRestriction;
  if(mode==='apply')subject.processingRestriction={id:randomUUID(),requestId:request.id,at,by:actor.id,scope:'ordinary_service',retentionReference:body.retentionReference,...(subject.role==='parent'?{dependentIds:parentDependencies(s,subject,at)}:{})};
  else{subject.restrictionHistory||=[];subject.restrictionHistory.push({...old,liftedAt:at,liftedBy:actor.id,requesterReference:body.requesterReference,retentionReference:body.retentionReference});delete subject.processingRestriction;}
  const afterIds=restrictionIds(s,at),changed=new Set([...(mode==='apply'?afterIds:beforeIds)].filter(id=>!(mode==='apply'?beforeIds:afterIds).has(id))),touched=new Set([subject.id,...changed]);
  for(const u of s.users.filter(v=>touched.has(v.id))){u.revision++;delete u.deviceDraftKey;}
  const revokeIds=revokedUsers(s,subject,changed,actor.id);
  for(const [key,session]of Object.entries(s.sessions))if(revokeIds.has(session.userId)&&session.userId!==actor.id)delete s.sessions[key];
  for(const a of s.attempts.filter(a=>a.tenantId===subject.tenantId&&changed.has(a.studentId))){
   if(mode==='apply'){if(a.status==='in_progress'&&!a.processingPause)a.processingPause={at,remainingMs:Math.max(0,a.deadlineAt-at)};delete a.parentPublishedAt;}
   else if(a.processingPause){if(a.status==='in_progress')a.deadlineAt=at+a.processingPause.remainingMs;delete a.processingPause;}
  }
  const assignments=new Map(all('learning_assignments',subject.tenantId).map(a=>[a.id,a]));
  for(const r of all('learning_runs',subject.tenantId).filter(r=>changed.has(r.studentId))){
   if(mode==='apply'){if(!r.submittedAt&&!r.processingPause){const due=Math.max(r.dueAtOverride||0,assignments.get(r.assignmentId)?.dueAt||0);r.processingPause={at,remainingMs:Math.max(0,(due||at)-at),wasEligible:due>at};}delete r.publishedAt;}
   else if(r.processingPause){if(!r.submittedAt&&r.processingPause.wasEligible)r.dueAtOverride=Math.max(assignments.get(r.assignmentId)?.dueAt||0,at+r.processingPause.remainingMs);delete r.processingPause;}
   r.revision++;put('learning_runs',r,subject.tenantId);
  }
  if(mode==='apply')for(const r of all('pilot_runs',subject.tenantId).filter(r=>changed.has(r.studentId))){delete r.pulse;put('pilot_runs',r,subject.tenantId);}
  if(mode==='apply')for(const r of all('learning_releases',subject.tenantId).filter(r=>changed.has(r.studentId))){r.processingWithheld=true;r.withheldAt=at;put('learning_releases',r,subject.tenantId);}
  s.audit.push({at,actor:actor.id,tenantId:subject.tenantId,subjectId:subject.id,action:'processing.'+mode,requestId:request.id});
  return {kind:'restriction',scope:'ordinary_service',restrictionId:mode==='apply'?subject.processingRestriction.id:old.id,appliedAt:mode==='apply'?at:old.at,...(mode==='lift'?{liftedAt:at}:{}),affectedAccounts:touched.size,retentionReference:body.retentionReference};
 };
 return {before,stateForRead,sanitize,impact,change};
}
