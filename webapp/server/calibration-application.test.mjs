import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {randomUUID} from 'node:crypto';
import {createLearningService} from './learning-service.mjs';
import {placementForm,placementFormAtVersion,publicForm,courseLessons,recommend} from './placement-content.mjs';
import {calibratedRecommendation,rankedChecks,checkSelectionComparison} from './calibration-application.mjs';
const checks={difficulty:true,answer:true,evidence:true,explanation:true};
function fixture(t){
 const db=new DatabaseSync(':memory:'),service=createLearningService({db,randomUUID});t.after(()=>db.close());let at=Date.UTC(2026,10,18);
 const teacher={id:'teacher',tenantId:'academy',role:'teacher',classIds:['class']},students=Array.from({length:23},(_,n)=>({id:'s'+n,name:'가상 학생 '+n,tenantId:'academy',role:'student',classId:'class',consentStatus:'synthetic'}));
 const state={users:[teacher,...students],classes:[{id:'class',name:'가상 반',tenantId:'academy',active:true,revision:0}],audit:[]};
 const call=(user,path,body)=>service.route({user,state,path,method:body===undefined?'GET':'POST',body:body||{},at:at++});
 const catalog=call(teacher,'/learning/pilot').catalog,words=catalog.filter(i=>i.grade===1&&i.branch==='common'&&i.skill==='words').map(i=>i.key),evidence=catalog.find(i=>i.grade===1&&i.branch==='common'&&i.skill==='evidence').key;
 const check='check:g1:words:4',keys=[...words,evidence,check];
 const inspect=key=>call(teacher,'/learning/pilot/item',{itemKey:key});
 const seed=()=>{
  for(const key of keys){const d=inspect(key);call(teacher,'/learning/pilot/review',{itemKey:key,contentHash:d.item.contentHash,revision:0,status:'approved',checks,note:'가상 검수: 본문과 정답·근거·해설을 확인했습니다.'});}
  const session=call(teacher,'/learning/pilot/create',{name:'가상 보정 원자료',itemKeys:keys,studentIds:students.slice(0,20).map(s=>s.id),mutationId:randomUUID()});
  const runs=call(teacher,'/learning/pilot').learners.filter(r=>r.sessionId===session.sessionId);
  for(let n=0;n<20;n++){
   let r=call(students[n],'/learning/pilot/start',{runId:runs.find(r=>r.studentId===students[n].id).runId}).run;
   for(const key of keys){const q=inspect(key).item.question;r=call(students[n],'/learning/pilot/answer',{runId:r.id,itemKey:key,revision:r.revision,answer:{choice:n<(words.includes(key)?4:12)?q.answer:(q.answer+1)%q.options.length,text:'가상 응답',evidence:q.evidence,support:'independent',omitted:false}}).run;}
   r=call(students[n],'/learning/pilot/submit',{runId:r.id,revision:r.revision}).run;
   for(const key of keys)r=call(teacher,'/learning/pilot/observe',{runId:r.id,itemKey:key,revision:r.revision,assistance:'independent',priorExposure:'new',rubric:'success',note:'가상 첫 독립 수행 관찰'}).run;
  }
  for(const key of keys){const d=inspect(key);assert.equal(d.statistics.independentN,20);call(teacher,'/learning/pilot/calibrate',{itemKey:key,datasetHash:d.statistics.datasetHash,revision:0,confirmed:true,note:'가상 독립 표본 20명의 보정 승인'});}
  return runs;
 };
 const configure=(enabled=true)=>{const setting=state.classes[0].calibrationApplication;return call(teacher,'/learning/calibration/configure',{classId:'class',revision:setting?.revision||0,enabled,note:'새 진단과 계획에 승인 보정 사용'});};
 const teacherPlacement=s=>call(teacher,'/learning/placement').placements.find(r=>r.studentId===s.id);
 const answerPhase=(s,r,wrongWords=false)=>{const form=teacherPlacement(s).form;let wrong=false;for(const q of form.questions.filter(q=>!r.answers[q.id])){const bad=wrongWords&&!wrong&&q.skill==='words';if(bad)wrong=true;r=call(s,'/learning/placement/answer',{revision:r.revision,questionId:q.id,...(q.options.length?{choice:bad?(q.answer+1)%q.options.length:q.answer}:{text:'본문의 두 단서를 연결했어요.',evidence:q.evidence})}).placement;}return call(s,'/learning/placement/submit',{revision:r.revision}).placement;};
 const place=(s=students[20],wrong=false)=>{let r=call(s,'/learning/placement/start',{grade:1}).placement;r=answerPhase(s,r,wrong);r=answerPhase(s,r);const lessonId=courseLessons[1].words,preview=call(teacher,'/learning/catalog/'+lessonId);call(teacher,'/learning/approvals',{lessonId,contentHash:preview.contentHash,note:'가상 첫 수업 검토',pilot:true});return call(teacher,'/learning/placement/approve',{studentId:s.id,revision:r.revision,course:'words',level:'standard',lessonId,note:'가상 교사 최종 배치',explanationReviews:['success','success'],readingObservation:{state:'follow_up',note:'첫 수업에서 읽기 관찰'}}).placement;};
 const activate=s=>{const p=call(teacher,'/learning/course/preview',{studentId:s.id});return call(teacher,'/learning/course/activate',{studentId:s.id,revision:p.revision,contentHash:p.bundle.hash,approved:true,note:'가상 코스와 선정 전후 검토'}).course;};
 const train=(s,plan)=>{for(const t of plan.training.slice(0,2)){const d=call(s,'/learning/assignments/'+t.assignmentId+'/start',{}),run=structuredClone(d.run),qs=d.lesson.levelQuestions?.[d.assignment.level]||d.lesson.questions;for(const q of qs)run.responses[q.id]={choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문 단서를 설명합니다.',hintLevel:0,revealed:false,submissions:[{id:randomUUID(),choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문 단서를 설명합니다.',hintLevel:0}]};const saved=call(s,'/learning/runs/'+d.id+'/save',{revision:d.revision,mutationId:randomUUID(),run,writing:'배운 내용을 정리했습니다.'});call(s,'/learning/runs/'+d.id+'/submit',{revision:saved.revision});}};
 return {db,service,call,state,teacher,students,words,evidence,check,keys,inspect,seed,configure,teacherPlacement,answerPhase,place,activate,train};
}

test('unconfigured classrooms retain the exact original forms and calculations',t=>{
 const f=fixture(t),s=f.students[20],r=f.call(s,'/learning/placement/start',{grade:1}).placement;assert.deepEqual(r.form,publicForm(placementForm(1)));assert.equal('calibrationContext'in r,false);
 assert.deepEqual(calibratedRecommendation(placementForm(3),{}),recommend(placementForm(3),{}));
});
test('approved, current samples change actual diagnostic order and branch, with private before/after comparison',t=>{
 const f=fixture(t);f.seed();f.configure();const s=f.students[20];let r=f.call(s,'/learning/placement/start',{grade:1}).placement;
 assert.notDeepEqual(r.form.questions.map(q=>q.id),placementForm(1).questions.map(q=>q.id));
 for(const q of r.form.questions)for(const key of ['pilotCalibration','applicationItemKey','applicationItemHash'])assert.equal(key in q,false);
 const common=r.form.questions;r=f.answerPhase(s,r,true);assert.equal(r.branch,'extend');assert.deepEqual(r.form.questions.slice(0,common.length),common);
 const teacher=f.teacherPlacement(s);assert.equal(teacher.applicationComparison.common.baselineBranch,'support');assert.equal(teacher.applicationComparison.common.appliedBranch,'extend');assert.equal('applicationComparison'in r,false);assert.equal('branchForms'in r,false);
 r=f.answerPhase(s,r);assert.ok(f.teacherPlacement(s).applicationComparison.result.profiles.some(p=>p.appliedCount>0));
});
test('bounded difficulty offsets can change the actual recommended course without inventing counterfactual answers',()=>{
 const qs=['words','words','words','evidence','connect'].map((skill,n)=>({id:String(n),skill,options:['맞음','다름'],answer:0,...(n===0?{pilotCalibration:{scoreOffset:.15}}:{})})),form={grade:3,version:'g16-placement-3',questions:qs};
 const answers=Object.fromEntries(qs.map(q=>[q.id,{choice:q.id==='0'?1:0}]));assert.equal(recommend(form,answers).course,'words');assert.equal(calibratedRecommendation(form,answers).course,'connect');
 assert.equal(calibratedRecommendation({...form,questions:qs.map(q=>({...q,pilotCalibration:{scoreOffset:.15}}))},{}).course,'words');
});
test('sufficient calibration changes real check selection and survives class disable in an approved plan',t=>{
 const f=fixture(t);f.seed();f.configure();const s=f.students[20];f.place(s);const preview=f.call(f.teacher,'/learning/course/preview',{studentId:s.id});
 assert.equal(preview.bundle.selectionComparison.independent.baseline[0],'g1-words-check-0');assert.equal(preview.bundle.selectionComparison.independent.applied[0],'g1-words-check-4');
 const c=f.activate(s),digest=c.plan.calibrationContext.digest;f.configure(false);f.train(s,c.plan);
 const opened=f.call(s,'/learning/course/check/start',{planId:c.plan.id,purpose:'independent'});assert.equal(opened.check.content.id,'g1-words-check-4');assert.equal('selectionComparison'in opened.check,false);assert.equal('pilotCalibration'in opened.check.content,false);assert.equal('calibrationContext'in opened.course.plan,false);
 const teacher=f.call(f.teacher,'/learning/course').courses.find(c=>c.studentId===s.id);assert.equal(teacher.plan.calibrationContext.digest,digest);assert.equal(teacher.plan.checks[0].selectionComparison.baselineSelected,'g1-words-check-0');assert.equal(teacher.plan.checks[0].selectionComparison.selected,'g1-words-check-4');
});
test('19 current independent samples retain the original criteria even when the saved approval says 20',t=>{
 const f=fixture(t);f.seed();f.configure();f.students[0].active=false;const s=f.students[20],p=f.call(f.teacher,'/learning/calibration/preview',{studentId:s.id,grade:1});
 assert.equal(p.context.active,false);assert.ok(p.context.fallback.filter(r=>r.reason==='insufficient_sample').length>=4);
 let r=f.call(s,'/learning/placement/start',{grade:1}).placement;assert.deepEqual(r.form,publicForm(placementForm(1)));r=f.answerPhase(s,r,true);assert.equal(r.branch,'support');
});
test('started diagnostics pin approved samples and both branch forms; later sample loss affects only new attempts',t=>{
 const f=fixture(t);f.seed();f.configure();const s=f.students[20];let r=f.call(s,'/learning/placement/start',{grade:1}).placement;const old=f.teacherPlacement(s).calibrationContext.digest;f.students[0].active=false;
 r=f.answerPhase(s,r,true);assert.equal(r.branch,'extend');assert.equal(f.teacherPlacement(s).calibrationContext.digest,old);
 const fresh=f.call(f.students[21],'/learning/placement/start',{grade:1}).placement;assert.deepEqual(fresh.form,publicForm(placementForm(1)));
});
test('source-data changes invalidate unapproved previews, so activation must use a freshly reviewed selection',t=>{
 const f=fixture(t),runs=f.seed();f.configure();const s=f.students[20];f.place(s);const preview=f.call(f.teacher,'/learning/course/preview',{studentId:s.id});
 const run=f.call(f.teacher,'/learning/pilot/run',{runId:runs[0].runId}).run;f.call(f.teacher,'/learning/pilot/observe',{runId:run.id,itemKey:f.check,revision:run.revision,assistance:'independent',priorExposure:'new',rubric:'success',observedMs:12000,note:'관찰 시간 보완'});
 assert.throws(()=>f.call(f.teacher,'/learning/course/activate',{studentId:s.id,revision:preview.revision,contentHash:preview.bundle.hash,approved:true,note:'이전 미리보기 승인 시도'}),/검토하고 승인/);
 const next=f.call(f.teacher,'/learning/course/preview',{studentId:s.id});assert.equal(next.bundle.selectionComparison.independent.applied[0],'g1-words-check-0');assert.ok(next.bundle.calibrationContext.fallback.some(i=>i.key===f.check&&i.reason==='stale_data'));
});
test('existing diagnostics and already approved plans are not retroactively calibrated',t=>{
 const f=fixture(t);f.seed();const s=f.students[20];f.place(s,true);assert.equal(f.teacherPlacement(s).applicationComparison,undefined);const c=f.activate(s);f.configure();f.train(s,c.plan);
 assert.equal(f.call(s,'/learning/course/check/start',{planId:c.plan.id,purpose:'independent'}).check.content.id,'g1-words-check-0');
});
test('scope changes require current revisions and reject students, parents, other classrooms and competing sources',t=>{
 const f=fixture(t);f.configure();assert.throws(()=>f.call(f.teacher,'/learning/calibration/configure',{classId:'class',revision:0,enabled:false,note:'이전 설정 덮어쓰기'}),/최신 설정/);
 assert.throws(()=>f.call(f.students[20],'/learning/calibration'),/교사 권한/);assert.throws(()=>f.call({...f.teacher,id:'foreign',classIds:[]},'/learning/calibration/preview',{studentId:f.students[20].id,grade:1}),/담당 반/);
 assert.throws(()=>f.call({...f.teacher,id:'second'},'/learning/calibration/configure',{classId:'class',revision:1,enabled:true,note:'다른 교사의 설정 교체'}),/기존 적용 담당/);
});


test('older item versions are never reused as responses to the current calibrated items',t=>{
 const f=fixture(t);f.configure();const student=f.students[20],old=placementFormAtVersion(1,'support','g16-placement-2');
 f.db.prepare('INSERT INTO learning_placements VALUES(?,?,?)').run('academy:'+student.id,'academy',JSON.stringify({id:student.id,studentId:student.id,grade:1,version:old.version,formSnapshot:old,branch:'support',answers:{},revision:0,status:'in_progress'}));
 const preview=f.call(f.teacher,'/learning/calibration/preview',{studentId:student.id,grade:1});assert.equal(preview.recommendation,null);assert.equal(preview.comparisonUnavailable,'older_version');assert.equal(f.teacherPlacement(student).form.version,'g16-placement-2');
});


test('a calibrated backup remains reserved while primary purpose-matched checks remain available',()=>{
 const regular={id:'primary',title:'주 확인',difficulty:{band:'기본'}},backup={id:'backup',title:'대체',difficulty:{band:'입문'},pilotCalibration:{editorialBand:'입문',band:'기본'}};
 assert.deepEqual(checkSelectionComparison([regular,backup],'standard','backup').applied,['primary','backup']);assert.deepEqual(checkSelectionComparison([backup],'standard','backup').applied,['backup']);
});


test('grade-1 approvals do not alter any grade-2 through grade-6 diagnostic',t=>{
 const f=fixture(t);f.seed();f.configure();
 for(let grade=2;grade<=6;grade++){
  const s={...f.students[22],id:'new-grade-'+grade};f.state.users.push(s);
  const r=f.call(s,'/learning/placement/start',{grade}).placement;assert.deepEqual(r.form,publicForm(placementForm(grade)));assert.equal(f.teacherPlacement(s).calibrationContext.active,false);
 }
});
