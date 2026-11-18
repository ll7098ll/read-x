import { canTeachClass, activeAccount } from '../shared/organization.mjs';
import { placementForm, placementFormAtVersion, legacyPlacementForm, publicForm, profileFor, recommend, placementVersion, courseLessons } from './placement-content.mjs';
import { calibratedBranch, calibratedRecommendation, calibratedProfile, recommendationComparison } from './calibration-application.mjs';
import { gradeProfiles, courseNames, courseOrder, learningGrades } from '../shared/learning-config.mjs';
const fail=(status,message)=>{throw Object.assign(new Error(message),{status});};
export function createPlacementService({db, lessons, delegate, calibration}) {
  db.exec('CREATE TABLE IF NOT EXISTS learning_placements (id TEXT PRIMARY KEY, tenant_id TEXT NOT NULL, body TEXT NOT NULL)');
  const get=u=>{const row=db.prepare('SELECT body FROM learning_placements WHERE id=? AND tenant_id=?').get(`${u.tenantId}:${u.id}`,u.tenantId);return row?JSON.parse(row.body):null;};
  const put=(u,r)=>db.prepare('INSERT INTO learning_placements VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET body=excluded.body').run(`${u.tenantId}:${u.id}`,u.tenantId,JSON.stringify(r));
  const form=r=>r.formSnapshot||placementFormAtVersion(r.grade,r.branch,r.version);
  const view=(r,teacher=false)=>{if(!r)return r;const {formSnapshot,branchForms,calibrationContext,applicationComparison,...record}=r;
    const recommendation=!teacher&&record.recommendation?{...record.recommendation,profile:record.recommendation.profile.map(({skill,label,correct,total})=>({skill,label,correct,total}))}:record.recommendation;
    return {...record,...(recommendation?{recommendation}:{}),...(teacher?{calibrationContext,applicationComparison}:{}),form:teacher?form(r):publicForm(form(r)),candidates:r.recommendation?Object.entries(courseLessons[r.grade]).map(([course,id])=>{const l=lessons.find(l=>l.id===id);return l&&{id:l.id,course,title:l.title,goalIds:l.goalIds};}).filter(Boolean):[]};};
  return ({user:u,state,path,method,body,at})=>{
    const audit=(action,id)=>state.audit.push({at,actor:u.id,action,id});
    if(path==='/learning/placement' && method==='GET') {
      if(u.role==='parent')fail(403,'진단 원응답은 학생과 담당 교사가 확인합니다.');
      if(u.role==='teacher')return {placements:state.users.filter(s=>s.tenantId===u.tenantId&&s.role==='student'&&canTeachClass(u,s.classId)).map(s=>{const r=get(s);return r?{...view(r,true),studentName:s.name}:null;}).filter(Boolean)};
      return {placement:view(get(u))};
    }
    if(path==='/learning/placement/start' && method==='POST') {
      if(u.role!=='student')fail(403,'학생 계정으로 시작해 주세요.');
      const old=get(u);if(old)return {placement:view(old)};
      if(!learningGrades.includes(body.grade))fail(400,'초1~6 학년을 선택해 주세요.');
      const r={id:u.id,studentId:u.id,grade:body.grade,version:placementVersion,formSnapshot:placementForm(body.grade),status:'in_progress',branch:null,answers:{},revision:0,createdAt:at,updatedAt:at};
      const context=calibration?.resolve({...u,grade:body.grade},state,at);
      if(context?.enabled){
        r.calibrationContext=context;
        r.formSnapshot=calibration.applyForm(r.formSnapshot,context);
        r.branchForms=Object.fromEntries(['support','extend'].map(branch=>[branch,calibration.applyForm(placementForm(body.grade,branch),context)]));
        r.applicationComparison={policy:context.policy,active:context.active,baselineOrder:placementForm(body.grade).questions.map(q=>q.id),appliedOrder:r.formSnapshot.questions.map(q=>q.id)};
      }
      const pilotFamilies=db.prepare("SELECT body FROM pilot_runs WHERE tenant_id=? AND json_extract(body,'$.studentId')=?").all(u.tenantId,u.id).flatMap(row=>{const p=JSON.parse(row.body);return p.items.filter(i=>i.kind==='diagnostic'&&i.grade===r.grade&&p.presented[i.key]!=null).map(i=>i.familyId);});
      if(pilotFamilies.length)r.priorPilotExposure={families:[...new Set(pilotFamilies)],checkedAt:at};
      put(u,r);audit('placement.start',r.id);return {placement:view(r)};
    }
    if(path==='/learning/placement/answer' && method==='POST') {
      if(u.role!=='student')fail(403,'학생 계정으로 응답해 주세요.');
      const r=get(u);if(!r||r.status!=='in_progress')fail(409,'진행 중인 진단이 없습니다.');
      const q=form(r).questions.find(q=>q.id===body.questionId);
      if(!q)fail(400,'현재 진단 문항을 확인해 주세요.');
      const oral=!q.options.length&&r.grade<=2&&body.responseMode==='oral_requested';
      const answer=q.options.length?{choice:body.choice}:{text:typeof body.text==='string'?body.text.trim():'',evidence:body.evidence,...(oral?{responseMode:'oral_requested'}:{})};
      if(q.options.length ? !Number.isInteger(answer.choice)||answer.choice<0||answer.choice>=q.options.length : !oral&&!answer.text||answer.text.length>2000||!Array.isArray(answer.evidence)||!answer.evidence.length||answer.evidence.some(i=>!Number.isInteger(i)||i<0||i>=form(r).passages.find(p=>p.id===q.passageId).paragraphs.length))fail(400,'답과 필요한 근거를 확인해 주세요.');
      // Retrying a response is safe; concurrent edits must refresh the server revision.
      if(JSON.stringify(r.answers[q.id]?.response)===JSON.stringify(answer))return {placement:view(r)};
      if(body.revision!==r.revision)fail(409,'다른 화면에서 답이 바뀌었습니다. 최신 기록을 불러와 주세요.');
      r.answers[q.id]={...answer,response:answer,at};r.revision++;r.updatedAt=at;put(u,r);return {placement:view(r)};
    }
    if(path==='/learning/placement/submit' && method==='POST') {
      if(u.role!=='student')fail(403,'학생 계정으로 제출해 주세요.');
      const r=get(u);if(!r)fail(404,'진단을 시작해 주세요.');
      if(r.status!=='in_progress')return {placement:view(r)};
      if(body.revision!==r.revision)fail(409,'최신 답안을 불러와 주세요.');
      if(form(r).questions.some(q=>!r.answers[q.id]))fail(400,'모든 문항에 응답한 뒤 확인해 주세요.');
      if(!r.branch){const currentForm=form(r),profile=profileFor(currentForm,r.answers),baselineBranch=profile.some(p=>p.correct/p.total<0.6)?'support':'extend';
        r.branch=r.calibrationContext?calibratedBranch(currentForm,r.answers,r.calibrationContext.policy):baselineBranch;
        if(r.applicationComparison)r.applicationComparison.common={baselineBranch,appliedBranch:r.branch,profiles:calibratedProfile(currentForm,r.answers)};
        r.formSnapshot=r.branchForms?.[r.branch]||placementFormAtVersion(r.grade,r.branch,r.version);
      }
      else {r.recommendation=r.calibrationContext?calibratedRecommendation(form(r),r.answers,r.calibrationContext.policy):recommend(form(r),r.answers);if(r.applicationComparison)r.applicationComparison.result=recommendationComparison(form(r),r.answers,r.calibrationContext.policy);r.status='awaiting_teacher';r.submittedAt=at;r.initialAnswers=structuredClone(r.answers);}
      r.revision++;r.updatedAt=at;put(u,r);audit('placement.submit',r.id);return {placement:view(r)};
    }
    if(path==='/learning/placement/oral'&&method==='POST'){
      const student=state.users.find(s=>s.id===body.studentId&&s.tenantId===u.tenantId&&s.role==='student');
      if(!student||!canTeachClass(u,student.classId)||!activeAccount(student,at))fail(404,'담당 재원 학생을 확인해 주세요.');
      const r=get(student),q=r&&form(r).questions.find(q=>q.id===body.questionId&&!q.options.length);
      if(!r||r.grade>2||r.status!=='awaiting_teacher'||!q||r.answers[q.id]?.responseMode!=='oral_requested')fail(409,'말로 설명을 요청한 저학년 제출 답안을 확인해 주세요.');
      if(body.revision!==r.revision)fail(409,'최신 진단 기록을 불러와 주세요.');
      if(typeof body.transcript!=='string'||!body.transcript.trim()||body.transcript.length>2000||!['independent','prompted','read_aloud'].includes(body.support))fail(400,'실제 말한 내용과 도움 여부를 기록해 주세요.');
      r.oralObservations||={};r.oralHistory||=[];if(r.oralObservations[q.id])r.oralHistory.push({questionId:q.id,...r.oralObservations[q.id]});
      r.oralObservations[q.id]={transcript:body.transcript.trim(),support:body.support,by:u.id,at};r.revision++;put(student,r);audit('placement.oral',q.id);return {placement:view(r,true)};
    }
    if(path==='/learning/placement/approve' && method==='POST') {
      const student=state.users.find(s=>s.id===body.studentId&&s.tenantId===u.tenantId&&s.role==='student');
      if(!student||!canTeachClass(u,student.classId)||!activeAccount(student,at))fail(404,'담당 재원 학생을 확인해 주세요.');
      const r=get(student);if(!r||!r.recommendation)fail(409,'제출된 진단이 없습니다.');
      if(r.assignmentId)return {placement:view(r,true)};
      if(body.revision!==r.revision)fail(409,'최신 진단 기록을 불러와 주세요.');
      const lesson=lessons.find(l=>l.id===body.lessonId&&l.grade===r.grade);
      if(courseLessons[r.grade]?.[body.course]!==body.lessonId)fail(400,'선택한 코스에 연결된 첫 수업을 확인해 주세요.');
      if(!lesson||!courseOrder.includes(body.course)||!['supported','standard','challenge'].includes(body.level)||typeof body.note!=='string'||!body.note.trim()||body.note.length>2000)fail(400,'코스·첫 수업·글 수준과 배치 이유를 확인해 주세요.');
      if(r.grade<=2){if(form(r).questions.some(q=>r.answers[q.id]?.responseMode==='oral_requested'&&!r.oralObservations?.[q.id]))fail(409,'학생의 실제 말로 설명을 관찰해 기록해 주세요.');if(!['observed','follow_up'].includes(body.readingObservation?.state)||typeof body.readingObservation?.note!=='string'||!body.readingObservation.note.trim()||body.readingObservation.note.length>2000)fail(400,'실제 읽기 관찰 또는 추가 관찰 계획을 기록해 주세요.');}
      if(!Array.isArray(body.explanationReviews)||body.explanationReviews.length!==2||body.explanationReviews.some(v=>!['success','needs_support'].includes(v)))fail(400,'자기 설명 두 과제를 검토해 주세요.');
      // Existing assignment route enforces exact-content approval and class authorization.
      const result=delegate({user:u,state,path:'/learning/assignments',method:'POST',body:{lessonId:lesson.id,studentIds:[student.id],level:body.level,dueAt:at+14*86400000,title:`${courseNames[body.course]} · 첫 수업`},at});
      r.decision={course:body.course,level:body.level,lessonId:lesson.id,note:body.note.trim(),explanationReviews:body.explanationReviews,...(r.grade<=2?{readingObservation:body.readingObservation}:{}),by:u.id,at,policyVersion:r.version};
      r.assignmentId=result.assignment.id;r.status='provisional';r.revision++;r.updatedAt=at;put(student,r);audit('placement.approve',r.id);return {placement:view(r,true)};
    }
    fail(404,'진단 요청을 찾을 수 없습니다.');
  };
}
