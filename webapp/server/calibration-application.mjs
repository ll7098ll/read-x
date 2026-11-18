import {canTeachClass,activeAccount} from '../shared/organization.mjs';
import {restrictionIds} from '../shared/processing-restrictions.mjs';
import {courseNames} from '../shared/learning-config.mjs';
import {placementForm,placementVersion,profileFor,recommend} from './placement-content.mjs';
import {courseBundle} from './course-content.mjs';
import {pilotCatalog,pilotHash} from './pilot-content.mjs';
import {pilotRows,itemStatistics,pilotPolicy} from './pilot-statistics.mjs';
export const applicationPolicy={version:'approved-calibration-application-1',referenceAccuracy:.7,maxScoreOffset:.15,branchThreshold:.6,placementThreshold:.7,reserveBackup:true};
const fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const bands={입문:0,기본:1,도전:2};
const clamp=(v,min,max)=>Math.max(min,Math.min(max,v));
const targetBand=level=>level==='supported'?0:level==='challenge'?2:1;
const bareQuestion=q=>{const {pilotCalibration,applicationItemKey,applicationItemHash,...raw}=q;return raw;};
export function calibratedProfile(form,answers){return profileFor(form,answers).map(p=>{
 const qs=form.questions.filter(q=>q.options.length&&q.skill===p.skill),used=qs.filter(q=>q.pilotCalibration);
 const offset=used.reduce((sum,q)=>sum+q.pilotCalibration.scoreOffset,0)/p.total;
 return {...p,rawAccuracy:p.correct/p.total,scoreOffset:offset,adjustedAccuracy:clamp(p.correct/p.total+offset,0,1),appliedCount:used.length};
});}
export function calibratedBranch(form,answers,policy=applicationPolicy){return calibratedProfile(form,answers).some(p=>p.adjustedAccuracy<policy.branchThreshold)?'support':'extend';}
export function calibratedRecommendation(form,answers,policy=applicationPolicy){
 const baseline=recommend(form,answers),profile=calibratedProfile(form,answers);
 if(!profile.some(p=>p.appliedCount))return baseline;
 const need=profile.find(p=>p.adjustedAccuracy<policy.placementThreshold),course=need?.skill||(form.grade>=5?'evaluate':'connect');
 return {...baseline,course,courseName:courseNames[course],level:profile[0].adjustedAccuracy<policy.branchThreshold?'supported':'standard',profile,
  reason:'승인된 문항 난도 보정을 반영한 추천입니다. 선생님이 원응답과 자기 설명을 함께 확인합니다.',supplements:profile.filter(p=>p.skill!==course&&p.adjustedAccuracy<policy.placementThreshold).map(p=>p.label)};
}
export function recommendationComparison(form,answers,policy=applicationPolicy){return {scope:'same-administered-answers',baseline:recommend(form,answers),applied:calibratedRecommendation(form,answers,policy),profiles:calibratedProfile(form,answers)};}
// Uncalibrated candidates keep their original relative order. Only a verified
// change in distance from the target difficulty can move a calibrated item.
export function rankedChecks(candidates,level){
 const target=targetBand(level);
 return candidates.map((q,index)=>{const c=q.pilotCalibration,delta=c?Math.abs(bands[c.band]-target)-Math.abs(bands[c.editorialBand]-target):0;return {q,priority:index+delta*candidates.length,index};}).sort((a,b)=>a.priority-b.priority||a.index-b.index).map(x=>x.q);
}
export function checkSelectionComparison(candidates,level,backupId){const ranked=backupId?[...rankedChecks(candidates.filter(q=>q.id!==backupId),level),...candidates.filter(q=>q.id===backupId)]:rankedChecks(candidates,level);return {targetLevel:level,backupId,baseline:candidates.map(q=>q.id),applied:ranked.map(q=>q.id),items:candidates.map(q=>({id:q.id,title:q.title,editorialBand:q.difficulty?.band||null,effectiveBand:q.pilotCalibration?.band||q.difficulty?.band||null,applied:!!q.pilotCalibration}))};}

export function createCalibrationApplication({db,lessons}){
 const catalog=pilotCatalog(lessons),byKey=new Map(catalog.map(i=>[i.key,i]));
 const all=(table,tenant)=>db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r=>JSON.parse(r.body));
 const get=(table,id,tenant)=>{const row=db.prepare(`SELECT body FROM ${table} WHERE id=? AND tenant_id=?`).get(tenant+':'+id,tenant);return row?JSON.parse(row.body):null;};
 const resolve=(student,state,at,{forceTeacherId}={})=>{
  const cls=state.classes.find(c=>c.id===student.classId&&c.tenantId===student.tenantId&&c.active),setting=cls?.calibrationApplication;
  const blocked=restrictionIds(state,at),teacherId=forceTeacherId||setting?.teacherId,teacher=state.users.find(u=>u.id===teacherId&&u.tenantId===student.tenantId&&u.role==='teacher');
  const enabled=!!forceTeacherId||setting?.enabled===true,authorized=teacher&&activeAccount(teacher,at)&&!blocked.has(teacher.id)&&canTeachClass(teacher,student.classId);
  const context={policy:applicationPolicy,grade:student.grade,classId:student.classId,sourceTeacherId:teacherId||null,settingRevision:setting?.revision||0,enabled,active:false,items:{},fallback:[],reason:!enabled?'not_enabled':!authorized?'source_unavailable':'no_qualified_items'};
  if(enabled&&authorized){
   const eligibleStudent=s=>s?.tenantId===teacher.tenantId&&s.role==='student'&&activeAccount(s,at)&&!blocked.has(s.id)&&canTeachClass(teacher,s.classId);
   const runs=all('pilot_runs',teacher.tenantId).filter(r=>r.teacherId===teacher.id&&eligibleStudent(state.users.find(s=>s.id===r.studentId))),rows=pilotRows(runs);
   for(const i of catalog.filter(i=>i.grade===student.grade)){
    const id=teacher.id+':'+i.key+':'+i.contentHash,c=get('pilot_calibrations',id,teacher.tenantId),review=get('pilot_item_reviews',id,teacher.tenantId);
    let reason=!c?'not_approved':review?.status!=='approved'?'review_required':null;
    const stats=c&&!reason?itemStatistics(i,rows):null;
    if(stats){reason=stats.independentN<pilotPolicy.minIndependent||c.n<pilotPolicy.minIndependent?'insufficient_sample':c.policy?.version!==pilotPolicy.version?'unsupported_policy':stats.datasetHash!==c.datasetHash?'stale_data':c.n!==stats.independentN||c.p!==stats.p||!Number.isFinite(c.p)||c.p<0||c.p>1||!Object.hasOwn(bands,c.band)||c.band!==stats.suggestedBand?'invalid_calibration':null;}
    if(reason){context.fallback.push({key:i.key,label:i.title+' · '+i.question.prompt,reason,...(stats?{n:stats.independentN}:{})});continue;}
    context.items[i.key]={key:i.key,contentHash:i.contentHash,editorialBand:i.question.difficulty.band,band:c.band,n:stats.independentN,p:c.p,interval:c.interval,revision:c.revision,approvedAt:c.at,datasetHash:c.datasetHash,scoreOffset:clamp(applicationPolicy.referenceAccuracy-c.p,-applicationPolicy.maxScoreOffset,applicationPolicy.maxScoreOffset)};
   }
   context.active=Object.keys(context.items).length>0;if(context.active)context.reason='qualified';
  }
  return {...context,digest:pilotHash(context)};
 };
 const formItem=(form,q)=>{
  const key=q.applicationItemKey||`diagnostic:g${form.grade}:${q.id.startsWith('explain-')?form.branch:placementForm(form.grade).questions.some(c=>c.id===q.id)?'common':form.branch}:${q.id}`;
  const i=byKey.get(key),p=form.passages.find(p=>p.id===q.passageId);if(!i||form.version!==placementVersion||!p)return null;
  return pilotHash({key,sourceVersion:form.version,paragraphs:p.paragraphs,question:bareQuestion(q)})===i.contentHash?i:null;
 };
 const applyForm=(original,context)=>{
  const form=structuredClone(original);
  form.questions=form.questions.map(original=>{const q=bareQuestion(original),i=formItem(form,original),c=i&&context.items[i.key];return c?{...q,applicationItemKey:i.key,applicationItemHash:i.contentHash,pilotCalibration:structuredClone(c)}:q;});
  if(context.active){
   const commonIds=new Set(placementForm(form.grade).questions.map(q=>q.id));
   const common=form.questions.filter(q=>commonIds.has(q.id)),extra=form.questions.filter(q=>!commonIds.has(q.id)&&q.options.length),open=form.questions.filter(q=>!q.options.length);
   const order=qs=>{const pids=[...new Set(qs.map(q=>q.passageId))];return pids.flatMap(id=>rankedChecks(qs.filter(q=>q.passageId===id),'standard'));};
   form.questions=[...order(common),...order(extra),...open];
  }
  form.passages=form.passages.map(p=>({...p,questions:form.questions.filter(q=>q.passageId===p.id)}));return form;
 };
 const applyBundle=(base,context,level)=>{
  if(!context.enabled)return base;
  const checks=base.checks.map((q,index)=>{const i=byKey.get(`check:g${base.grade}:${base.course}:${index}`),c=i&&context.items[i.key];return c?{...q,pilotCalibration:structuredClone(c)}:q;});
  const selectionComparison={independent:checkSelectionComparison([0,1,2,3,4,7].map(i=>checks[i]),level,checks[7].id),transfer:checkSelectionComparison([5,7].map(i=>checks[i]),level,checks[7].id),maintenance:checkSelectionComparison([6,7].map(i=>checks[i]),level,checks[7].id)};
  return {...base,checks,calibrationContext:context,selectionComparison,hash:pilotHash({baseHash:base.hash,contextDigest:context.digest,selectionComparison})};
 };
 const route=({user:u,state,path,method,body,at})=>{
  if(u.role!=='teacher')fail(403,'교사 권한이 필요합니다.');
  const allowedClass=id=>{const cls=state.classes.find(c=>c.id===id&&c.tenantId===u.tenantId&&c.active);if(!cls||!canTeachClass(u,id))fail(404,'담당 반을 확인해 주세요.');return cls;};
  if(path==='/learning/calibration'&&method==='GET')return {policy:applicationPolicy,classes:state.classes.filter(c=>c.tenantId===u.tenantId&&c.active&&canTeachClass(u,c.id)).map(c=>({id:c.id,name:c.name,setting:c.calibrationApplication||null,sourceName:state.users.find(v=>v.id===c.calibrationApplication?.teacherId)?.name||null,canConfigure:!c.calibrationApplication?.teacherId||c.calibrationApplication.teacherId===u.id||!!u.isOwner})),students:state.users.filter(s=>s.tenantId===u.tenantId&&s.role==='student'&&activeAccount(s,at)&&!restrictionIds(state,at).has(s.id)&&canTeachClass(u,s.classId)).map(s=>({id:s.id,name:s.name,classId:s.classId}))};
  if(path==='/learning/calibration/configure'&&method==='POST'){
   const cls=allowedClass(body.classId),old=cls.calibrationApplication;
   if(old?.teacherId&&old.teacherId!==u.id&&!u.isOwner)fail(403,'기존 적용 담당 교사 또는 운영자가 기준을 변경할 수 있습니다.');
   if(body.revision!==(old?.revision||0))fail(409,'반의 적용 설정이 바뀌었습니다. 최신 설정을 불러와 주세요.');
   if(typeof body.enabled!=='boolean'||typeof body.note!=='string'||!body.note.trim()||body.note.length>2000)fail(400,'적용 여부와 운영 의견을 남겨 주세요.');
   cls.calibrationApplication={teacherId:u.id,enabled:body.enabled,revision:(old?.revision||0)+1,note:body.note.trim(),by:u.id,at,history:[...(old?.history||[]),...(old?[{...old,history:undefined}]:[])]};cls.revision=(cls.revision||0)+1;
   state.audit.push({at,actor:u.id,action:'calibration.configure',id:cls.id});return {setting:cls.calibrationApplication};
  }
  if(path==='/learning/calibration/preview'&&method==='POST'){
   const s=state.users.find(s=>s.id===body.studentId&&s.tenantId===u.tenantId&&s.role==='student');if(!s||!activeAccount(s,at)||restrictionIds(state,at).has(s.id))fail(404,'담당 재원 학생을 확인해 주세요.');allowedClass(s.classId);
   if(![1,2,3,4,5,6].includes(body.grade))fail(400,'자료 학년을 확인해 주세요.');
   const context=resolve({...s,grade:body.grade},state,at,{forceTeacherId:u.id}),before=placementForm(body.grade),after=applyForm(before,context),saved=get('learning_placements',s.id,s.tenantId);
   const sameVersion=saved?.grade===body.grade&&saved.formSnapshot?.version===placementVersion;
   const savedForm=sameVersion?saved.formSnapshot:null,ready=savedForm&&savedForm.questions.every(q=>!q.options.length||saved.answers[q.id]);
   const course=ready?calibratedRecommendation(applyForm(savedForm,context),saved.answers).course:(body.grade>=5?'evaluate':'connect');
   const level=ready?calibratedRecommendation(applyForm(savedForm,context),saved.answers).level:'standard';
   const bundle=applyBundle(courseBundle(body.grade,course,lessons),context,level);
   return {studentId:s.id,grade:body.grade,context,diagnostic:{baselineOrder:before.questions.map(q=>q.id),appliedOrder:after.questions.map(q=>q.id),items:before.questions.map(q=>({id:q.id,label:before.passages.find(p=>p.id===q.passageId).title+' · '+q.prompt}))},recommendation:ready?recommendationComparison(applyForm(savedForm,context),saved.answers):null,comparisonUnavailable:!saved?'no_responses':!sameVersion?'older_version':!ready?'incomplete':null,course:{name:bundle.name,level,selectionComparison:bundle.selectionComparison||{independent:checkSelectionComparison([0,1,2,3,4,7].map(i=>bundle.checks[i]),level)}}};
  }
  fail(404,'보정 적용 요청을 찾을 수 없습니다.');
 };
 return {resolve,applyForm,applyBundle,route};
}
