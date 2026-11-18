import { canTeachClass, activeAccount } from '../shared/organization.mjs';
import { courseBundle, courseOrder, courseNames, coursePolicy } from './course-content.mjs';
import { rankedChecks, checkSelectionComparison } from './calibration-application.mjs';
import { matchesAssessmentEvidence } from './assessment-review.mjs';
const fail=(status,message)=>{throw Object.assign(new Error(message),{status});};
const day=at=>new Date(at+9*3600000).toISOString().slice(0,10);
const dayMs=86400000;
const clean=v=>typeof v==='string'&&v.trim().length>0&&v.length<=2000;
const successful=a=>a.status==='reviewed'&&a.choiceMatch&&a.evidenceMatch&&a.review?.outcome==='success'&&(a.answer?.responseMode!=='oral_requested'||a.oralObservation?.support==='independent');
export function attainment(plan,at){
 const recent=plan.checks.filter(a=>a.purpose==='independent'&&a.submittedAt>=at-28*dayMs);
 const last=recent.slice(-5),passed=last.filter(successful);
 const independent=last.length===5&&passed.length>=4&&successful(last.at(-1))&&new Set(last.map(a=>day(a.submittedAt))).size>=2&&new Set(last.map(a=>a.familyId)).size===5;
 const transfer=plan.checks.some(a=>a.purpose==='transfer'&&successful(a));
 const maintenance=plan.checks.filter(a=>a.purpose==='maintenance');
 const pending=plan.checks.some(a=>a.status==='submitted');
 return {independent,transfer,maintained:maintenance.some(successful),needsRecheck:maintenance.length>0&&maintenance.at(-1).status==='reviewed'&&!successful(maintenance.at(-1)),pending,
  ready:independent&&transfer&&!pending,successes:passed.length,total:last.length,days:new Set(last.map(a=>day(a.submittedAt))).size,
  reason:pending?'선생님 확인 대기':!independent?'서로 다른 날과 새 글에서 독립 수행을 확인해요':!transfer?'새 상황에서 적용을 확인해요':'다음 단계로 이동할 수 있어요'};
}
export function createCourseService({db,lessons,delegate,randomUUID,calibration}){
 db.exec('CREATE TABLE IF NOT EXISTS learning_courses (id TEXT PRIMARY KEY, tenant_id TEXT NOT NULL, body TEXT NOT NULL)');
 const get=(table,id,tenant)=>{const row=db.prepare(`SELECT body FROM ${table} WHERE id=? AND tenant_id=?`).get(`${tenant}:${id}`,tenant);return row?JSON.parse(row.body):null;};
 const all=(table,tenant)=>db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r=>JSON.parse(r.body));
 const put=(u,r)=>db.prepare('INSERT INTO learning_courses VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET body=excluded.body').run(`${u.tenantId}:${r.studentId}`,u.tenantId,JSON.stringify(r));
 const placement=u=>get('learning_placements',u.id,u.tenantId);
 const current=u=>get('learning_courses',u.id,u.tenantId);
 const sourceAssignment=(u,id)=>get('learning_assignments',id,u.tenantId);
 const runFor=(u,id)=>all('learning_runs',u.tenantId).find(r=>r.studentId===u.id&&r.assignmentId===id);
 const safeCheck=a=>{const c=a.content;const content=Object.fromEntries(['id','familyId','title','paragraphs','prompt','options','grade','oralAllowed','version'].filter(k=>k in c).map(k=>[k,c[k]]));const feedback=a.status==='reviewed'&&c.explanation?{answer:c.answer,evidence:c.evidence,evidenceQuotes:c.evidenceQuotes,explanation:c.explanation,optionReasons:c.optionReasons,sampleResponse:c.sampleResponse,scoringGuide:c.scoringGuide}:undefined;const {selectionComparison,...safe}=a;return {...safe,content,...(feedback?{feedback}:{})};};
 const view=(u,r,at,teacher)=>{
  if(!r)return null;
  const show=p=>{const {checkBank,calibrationContext,selectionComparison,...publicPlan}=p;return {...publicPlan,...(teacher?{calibrationContext,selectionComparison}:{}),checks:teacher?p.checks:p.checks.map(safeCheck),attainment:attainment(p,at),
   training:p.training.map(t=>({...t,status:runFor(u,t.assignmentId)?.status||'not_started'})),remediations:(p.remediations||[]).map(t=>({...t,status:runFor(u,t.assignmentId)?.status||'not_started'}))};};
  return {...r,serverNow:at,plan:show(r.plan),history:r.history.map(show),nextCourse:courseOrder[courseOrder.indexOf(r.plan.course)+1]||null};
 };
 const makePlan=(u,course,level,at,bundle,existing)=>{
  const id=randomUUID();
  const training=bundle.training.map((lesson,i)=>{
   const a=i===0&&existing?sourceAssignment(u,existing):delegate({user:u.teacher,state:u.state,path:'/learning/assignments',method:'POST',body:{lessonId:lesson.id,studentIds:[u.id],classId:u.classId,level,dueAt:at+42*dayMs,title:`${bundle.name} · ${i+1}회 학습`},at}).assignment;
   if(!a||a.lessonId&&a.lessonId!==lesson.id||a.lesson&&a.lesson.id!==lesson.id)fail(409,'기존 첫 수업과 계획의 자료가 다릅니다.');
   if(i===0&&existing&&a.dueAt<at+42*dayMs)delegate({user:u.teacher,state:u.state,path:`/learning/assignments/${a.id}/extend`,method:'POST',body:{dueAt:at+42*dayMs,reason:'승인한 4주 학습 계획과 결석 후 이어 학습을 위한 기한 조정'},at});
   return {lessonId:lesson.id,title:lesson.title,assignmentId:a.id};
  });
  const kinds=['training','training','independent','training','independent','independent','transfer','maintenance'];
  const offsets=[0,3,7,10,14,17,21,24];
  return {id,course,name:bundle.name,grade:bundle.grade,profile:bundle.profile,level,policyVersion:coursePolicy,startedAt:at,contentHash:bundle.hash,...(bundle.calibrationContext?{calibrationContext:bundle.calibrationContext,selectionComparison:bundle.selectionComparison}:{}),checkBank:structuredClone(bundle.checks),training,checks:[],
   sessions:kinds.map((kind,i)=>({number:i+1,week:Math.floor(i/2)+1,kind,scheduledAt:at+offsets[i]*dayMs,trainingIndex:kind==='training'?[0,1,3].indexOf(i):null,checkCount:kind==='independent'?(i===5?1:2):kind==='training'?0:1})),status:'learning'};
 };
 return ({user:u,state,path,method,body,at})=>{
  const target=id=>{const s=state.users.find(s=>s.id===id&&s.tenantId===u.tenantId&&s.role==='student');if(!s||!canTeachClass(u,s.classId)||!activeAccount(s,at))fail(404,'담당 재원 학생을 확인해 주세요.');return s;};
  const audit=(action,id)=>state.audit.push({at,actor:u.id,action,id});
  const studentOnly=()=>{if(u.role!=='student')fail(403,'학생 계정으로 진행해 주세요.');};
  if(path==='/learning/course'&&method==='GET'){
   if(u.role==='parent')fail(403,'학습 계획과 확인 답안은 학생과 담당 교사가 확인합니다.');
   if(u.role==='teacher')return {courses:state.users.filter(s=>s.role==='student'&&s.tenantId===u.tenantId&&canTeachClass(u,s.classId)).map(s=>({studentId:s.id,studentName:s.name,placement:placement(s)?.decision||null,...view(s,current(s),at,true)}))};
   return {course:view(u,current(u),at,false)};
  }
  if(path==='/learning/course/preview'&&method==='POST'){
   const s=target(body.studentId),r=current(s),p=placement(s);if(!p?.decision)fail(409,'시작 코스를 먼저 배치해 주세요.');
   const next=body.next===true;
   if(next&&(!r||!attainment(r.plan,at).ready))fail(409,'독립 수행과 새 상황 적용, 교사 검토를 먼저 확인해 주세요.');
   const course=next?courseOrder[courseOrder.indexOf(r.plan.course)+1]:r?.plan.course||p.decision.course;
   if(!course)fail(409,'준비된 여섯 코스를 모두 마쳤습니다.');
   const base=courseBundle(p.grade,course,lessons),context=calibration?.resolve({...s,grade:p.grade},state,at);
   return {bundle:context?calibration.applyBundle(base,context,p.decision.level):base,revision:r?.revision??0,next};
  }
  if(path==='/learning/course/activate'&&method==='POST'){
   const s=target(body.studentId),p=placement(s),r=current(s);if(!p?.decision)fail(409,'시작 코스를 먼저 배치해 주세요.');
   if(r&&!body.next)return {course:view(s,r,at,true)};
   if(r&&body.next&&body.previousPlanId===r.history.at(-1)?.id)return {course:view(s,r,at,true)};
   if(body.revision!==(r?.revision??0))fail(409,'최신 학습 계획을 불러와 주세요.');
   if(body.next&&(!r||body.previousPlanId!==r.plan.id||!attainment(r.plan,at).ready))fail(409,'다음 단계 이동에 필요한 성취 확인이 부족합니다.');
   const course=body.next?courseOrder[courseOrder.indexOf(r.plan.course)+1]:p.decision.course;
   if(!course)fail(409,'준비된 코스를 모두 마쳤습니다.');
   const base=courseBundle(p.grade,course,lessons),context=calibration?.resolve({...s,grade:p.grade},state,at);
   const bundle=context?calibration.applyBundle(base,context,p.decision.level):base;
   if(bundle.hash!==body.contentHash||body.approved!==true||!clean(body.note))fail(400,'수업과 새 글 확인 자료를 검토하고 승인 의견을 남겨 주세요.');
   for(const lesson of bundle.training)delegate({user:u,state,path:'/learning/approvals',method:'POST',body:{lessonId:lesson.id,contentHash:delegate({user:u,state,path:`/learning/catalog/${lesson.id}`,method:'GET',body:{},at}).contentHash,note:body.note,pilot:true},at});
   const plan=makePlan({...s,teacher:u,state},course,p.decision.level,at,bundle,body.next?null:p.assignmentId);
   const record=r||{studentId:s.id,revision:0,history:[],exposures:[],decisions:[]};
   if(r){r.plan.status='confirmed';record.history.push(r.plan);}
   const from=r?.plan.id||null;
   record.plan=plan;record.revision++;record.decisions.push({at,by:u.id,note:body.note,from,to:plan.id,contentHash:bundle.hash,policyVersion:coursePolicy});
   put(s,record);audit('course.activate',plan.id);return {course:view(s,record,at,true)};
  }
  if(path==='/learning/course/check/start'&&method==='POST'){
   studentOnly();const r=current(u);if(!r)fail(409,'선생님이 4주 계획을 먼저 확인해야 합니다.');
   const plan=[r.plan,...r.history].find(p=>p.id===body.planId);if(!plan)fail(404,'본인 학습 계획을 확인해 주세요.');
   const purpose=body.purpose;if(!['independent','transfer','maintenance'].includes(purpose)||plan!==r.plan&&purpose!=='maintenance')fail(400,'확인 활동의 종류를 확인해 주세요.');
   const pending=plan.checks.find(a=>a.status==='in_progress');if(pending){if(pending.purpose!==purpose)fail(409,'풀고 있는 확인 활동을 먼저 마쳐 주세요.');return {check:safeCheck(pending),course:view(u,r,at,false)};}
   const trainingDone=plan.training.slice(0,2).every(t=>{const run=runFor(u,t.assignmentId);return run&&run.status!=='in_progress';});
   if(!trainingDone)fail(409,'첫 두 학습 수업을 제출한 뒤 새 글에서 확인해 주세요.');
   const result=attainment(plan,at);
   if(purpose==='independent'&&result.independent)fail(409,'독립 수행을 이미 확인했습니다. 새 상황 적용으로 이어가 주세요.');
   if(purpose==='independent'&&result.total>=5&&result.days<2&&day(plan.checks.filter(a=>a.purpose==='independent').at(-1).submittedAt)===day(at))fail(409,'다음 수업일에 다른 글로 확인해 주세요. 오늘은 새로운 확인 자료를 소모하지 않습니다.');
   if(purpose==='transfer'&&!plan.training.every(t=>{const run=runFor(u,t.assignmentId);return run&&run.status!=='in_progress';}))fail(409,'계획의 세 학습 수업을 모두 제출해 주세요.');
   if(purpose==='transfer'&&(!result.independent||plan.checks.some(a=>a.purpose==='transfer'&&successful(a))))fail(409,'독립 수행을 확인한 뒤 새 상황 적용을 진행해 주세요.');
   const transfer=plan.checks.find(a=>a.purpose==='transfer'&&successful(a));
   if(purpose==='maintenance'&&(!transfer||at<transfer.submittedAt+7*dayMs))fail(409,'새 상황 적용 성공 뒤 7일이 지나면 유지 확인을 진행합니다.');
   if(purpose==='maintenance'&&plan.checks.some(a=>a.purpose==='maintenance'&&successful(a)))fail(409,'유지 확인을 이미 마쳤습니다.');
   const indices=purpose==='independent'?[0,1,2,3,4,7]:purpose==='transfer'?[5,7]:[6,7];
   const pilotSeen=new Set(all('pilot_runs',u.tenantId).filter(p=>p.studentId===u.id).flatMap(p=>p.items.filter(i=>p.presented[i.key]!=null).map(i=>i.familyId)));
   const candidates=indices.map(i=>plan.checkBank[i]).filter(c=>!r.exposures.some(e=>e.familyId===c.familyId)&&!pilotSeen.has(c.familyId));
   const frozenOrder=plan.selectionComparison?.[purpose]?.applied;
   const ranked=frozenOrder?[...candidates].sort((a,b)=>frozenOrder.indexOf(a.id)-frozenOrder.indexOf(b.id)):rankedChecks(candidates,plan.level);
   const content=ranked[0];
   if(!content)fail(409,'미노출 확인 자료가 부족합니다. 선생님에게 새 자료를 요청해 주세요.');
   const check={id:randomUUID(),planId:plan.id,grade:plan.grade,purpose,familyId:content.familyId,status:'in_progress',content:structuredClone(content),revision:0,startedAt:at};
   if(plan.calibrationContext)check.selectionComparison={...checkSelectionComparison(candidates,plan.level,plan.checkBank[7].id),applied:ranked.map(q=>q.id),selected:content.id,baselineSelected:candidates[0]?.id,applicationDigest:plan.calibrationContext.digest};
   plan.checks.push(check);r.exposures.push({familyId:content.familyId,checkId:check.id,at});r.revision++;put(u,r);audit('course.check.start',check.id);return {check:safeCheck(check),course:view(u,r,at,false)};
  }
  if(path==='/learning/course/check/save'&&method==='POST'||path==='/learning/course/check/submit'&&method==='POST'){
   studentOnly();const r=current(u);const plan=r&&[r.plan,...r.history].find(p=>p.checks.some(a=>a.id===body.checkId));const check=plan?.checks.find(a=>a.id===body.checkId);
   if(!check)fail(404,'본인의 확인 활동을 찾을 수 없습니다.');
   if(check.status!=='in_progress')return {check:safeCheck(check),course:view(u,r,at,false)};
   if(body.revision!==check.revision)fail(409,'다른 화면에서 답이 바뀌었습니다. 최신 기록을 불러와 주세요.');
   const a=body.answer,c=check.content;
   const oral=check.grade<=2&&a?.responseMode==='oral_requested';
   if(!a||!Number.isInteger(a.choice)||a.choice<0||a.choice>=c.options.length||typeof a.reason!=='string'||a.reason.length>2000||!Array.isArray(a.evidence)||a.evidence.some(i=>!Number.isInteger(i)||i<0||i>=c.paragraphs.length))fail(400,'선택과 근거, 설명을 확인해 주세요.');
   if(path.endsWith('/submit')&&(!oral&&!a.reason.trim()||!a.evidence.length))fail(400,'근거와 자기 설명을 작성한 뒤 제출해 주세요.');
   check.answer={choice:a.choice,reason:a.reason.trim(),evidence:[...new Set(a.evidence)].sort(),...(oral?{responseMode:'oral_requested'}:{})};check.revision++;
   if(path.endsWith('/submit')){check.status='submitted';check.submittedAt=at;check.choiceMatch=a.choice===c.answer;check.evidenceMatch=matchesAssessmentEvidence(c,check.answer.evidence);check.firstAnswer=structuredClone(check.answer);}
   r.revision++;put(u,r);return {check:safeCheck(check),course:view(u,r,at,false)};
  }
  if(path==='/learning/course/check/review'&&method==='POST'){
   const s=target(body.studentId),r=current(s),plan=r&&[r.plan,...r.history].find(p=>p.checks.some(a=>a.id===body.checkId)),check=plan?.checks.find(a=>a.id===body.checkId);
   if(!check||check.status==='in_progress')fail(409,'제출된 확인 답안을 선택해 주세요.');
   if(body.revision!==check.revision)fail(409,'최신 검토 기록을 불러와 주세요.');
   if(!['success','needs_support'].includes(body.outcome)||!clean(body.note))fail(400,'설명 판단과 지도 의견을 남겨 주세요.');
   if(check.answer.responseMode==='oral_requested'){
    const o=body.oralObservation||check.oralObservation;
    if(!o||!clean(o.transcript)||!['independent','prompted','read_aloud'].includes(o.support))fail(400,'실제 말한 내용과 도움 여부를 관찰해 기록해 주세요.');
    check.oralHistory||=[];if(check.oralObservation)check.oralHistory.push(check.oralObservation);
    const rank={independent:0,prompted:1,read_aloud:2},support=check.oralObservation&&rank[check.oralObservation.support]>rank[o.support]?check.oralObservation.support:o.support;
    check.oralObservation={transcript:o.transcript.trim(),support,reportedSupport:o.support,by:u.id,at};
   }
   check.reviewHistory||=[];if(check.review)check.reviewHistory.push(check.review);
   check.review={outcome:body.outcome,note:body.note.trim(),by:u.id,at};check.status='reviewed';check.revision++;r.revision++;put(s,r);audit('course.check.review',check.id);return {course:view(s,r,at,true)};
  }
  if(path==='/learning/course/remediate'&&method==='POST'){
   const s=target(body.studentId),r=current(s),plan=r&&[r.plan,...r.history].find(p=>p.checks.some(a=>a.id===body.checkId)),failed=plan?.checks.find(a=>a.id===body.checkId&&a.status==='reviewed'&&!successful(a));
   if(!failed)fail(409,'추가 지도가 필요한 현재 코스의 확인 기록을 선택해 주세요.');
   plan.remediations||=[];
   if(plan.remediations.some(t=>t.checkId===failed.id))return {course:view(s,r,at,true)};
   const lessonId=plan.training[2].lessonId;
   const {assignment}=delegate({user:u,state,path:'/learning/assignments',method:'POST',body:{lessonId,studentIds:[s.id],classId:s.classId,level:'supported',dueAt:at+14*dayMs,title:`${plan.name} · 보충 학습`},at});
   plan.remediations.push({assignmentId:assignment.id,checkId:failed.id,title:`${plan.name} 보충`,at});r.revision++;put(s,r);audit('course.remediate',failed.id);return {course:view(s,r,at,true)};
  }
  fail(404,'학습 계획 요청을 찾을 수 없습니다.');
 };
}

