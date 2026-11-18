import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { mkdtempSync, rmSync, readFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createExamService } from './exam-service.mjs';
import { createHttpExamClient } from '../shared/http-exam-client.mjs';
import { courseBundle, courseOrder } from './course-content.mjs';
import { placementForm, placementFormAtVersion, publicForm, legacyPlacementForm, courseLessons } from './placement-content.mjs';
import { DatabaseSync } from 'node:sqlite';
const lessons=JSON.parse(readFileSync(new URL('../src/data/corpusLessons.generated.json',import.meta.url)));
import {gradeProfiles,learningGrades} from '../shared/learning-config.mjs';
const password='Course-Testing-2026!';
async function fixture(t,grade=3,course='connect',oralPlacement=false){
 const dir=mkdtempSync(join(tmpdir(),'readx-course-'));let at=Date.now(),server,service;
 const boot=async()=>{service=createExamService({dbPath:join(dir,'course.sqlite'),privacyMode:'synthetic',timer:false,now:()=>at});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));};
 const stop=async()=>{server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};await boot();
 t.after(async()=>{await stop();rmSync(dir,{recursive:true,force:true});});
 const client=()=>{let cookie='';return createHttpExamClient({fetcher:async(path,options)=>{const origin=`http://127.0.0.1:${server.address().port}`;const res=await fetch(origin+path,{...options,headers:{...options.headers,Cookie:cookie,Origin:origin}});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];return res;}});};
 const teacher=client(),student=client(),other=client(),parent=client();
 await teacher('/setup',{name:'교사',username:'teacher',password});
 const enrolled=await teacher('/roster',{student:{name:'코스 학생',username:'student',password},parent:{name:'보호자',username:'parent',password}});
 await teacher('/roster',{student:{name:'다른 학생',username:'other',password}});
 const login=async()=>{await student('/login',{username:'student',password});await teacher('/login',{username:'teacher',password});await other('/login',{username:'other',password});await parent('/login',{username:'parent',password});};await login();
 let p=(await student('/learning/placement/start',{grade})).placement;
 for(let phase=0;phase<2;phase++){
  for(const q of placementForm(grade,p.branch).questions.filter(q=>!p.answers[q.id]))p=(await student('/learning/placement/answer',{revision:p.revision,questionId:q.id,...(q.options.length?{choice:q.answer}:{text:oralPlacement?'':'본문의 두 정보를 연결해서 설명합니다.',evidence:q.evidence,...(oralPlacement?{responseMode:'oral_requested'}:{})})})).placement;
  p=(await student('/learning/placement/submit',{revision:p.revision})).placement;
 }
 if(oralPlacement){for(const q of placementForm(grade,p.branch).questions.filter(q=>!q.options.length)){const d=await teacher('/learning/placement/oral',{studentId:p.studentId,questionId:q.id,revision:p.revision,transcript:'글의 단서를 보고 그렇게 생각했어요.',support:'independent'});p=d.placement;}}
 const lessonId=courseLessons[grade][course],preview=await teacher(`/learning/catalog/${lessonId}`);
 await teacher('/learning/approvals',{lessonId,contentHash:preview.contentHash,note:'첫 수업 자료 검토',pilot:true});
 await teacher('/learning/placement/approve',{studentId:p.studentId,revision:p.revision,course,level:'standard',lessonId,note:'시작 배치 확인',explanationReviews:['success','success'],...(grade<=2?{readingObservation:{state:'follow_up',note:'첫 수업에서 실제 읽기를 관찰합니다.'}}:{})});
 const initialize=async()=>{const v=await teacher('/learning/course/preview',{studentId:p.studentId});return (await teacher('/learning/course/activate',{studentId:p.studentId,revision:v.revision,contentHash:v.bundle.hash,approved:true,note:'수업과 독립 확인 자료를 모두 검토했습니다.'})).course;};
 return {teacher,student,other,parent,studentId:enrolled.student.id,dbPath:join(dir,'course.sqlite'),initialize,tick:async(days=1)=>{at+=days*86400000;await login();},restart:async()=>{await stop();await boot();},now:()=>at};
}
async function train(f,assignmentId){
 const d=await f.student(`/learning/assignments/${assignmentId}/start`,{}),run=structuredClone(d.run),qs=d.lesson.levelQuestions?.[d.assignment.level]||d.lesson.questions;
 for(const q of qs)run.responses[q.id]={choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'필요한 근거를 연결해서 설명했습니다.',hintLevel:0,revealed:false,submissions:[{id:'s-'+q.id,choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'필요한 근거를 연결해서 설명했습니다.',hintLevel:0}]};
 const saved=await f.student(`/learning/runs/${d.id}/save`,{revision:d.revision,mutationId:'training',run,writing:'오늘의 관계와 판단을 정리했습니다.'});await f.student(`/learning/runs/${d.id}/submit`,{revision:saved.revision});
}
async function check(f,plan,purpose='independent',{wrong=false,review=true}={}){
 const started=await f.student('/learning/course/check/start',{planId:plan.id,purpose}),a=started.check,c=courseBundle(plan.grade,plan.course,lessons).checks.find(c=>c.id===a.content.id);
 assert.equal('answer'in a.content,false);assert.equal('evidence'in a.content,false);assert.equal('checkBank'in started.course.plan,false);
 const submitted=await f.student('/learning/course/check/submit',{checkId:a.id,revision:a.revision,answer:{choice:wrong?(c.answer+1)%c.options.length:c.answer,evidence:c.evidence,reason:'본문의 정보를 근거로 판단을 설명합니다.'}});
 if(!review)return submitted;
 return f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:a.id,revision:submitted.check.revision,outcome:'success',note:'근거와 설명을 확인했습니다.'});
}
test('six course bundles: distinct families, exact keys, training prerequisites, no missing source or rubric',()=>{
 const families=new Set();
 for(const grade of learningGrades)for(const course of courseOrder){const b=courseBundle(grade,course,lessons);assert.equal(b.training.length,3);assert.equal(b.checks.length,8);assert.ok(b.training.every(l=>l.grade===grade));
  for(const c of b.checks){assert.equal(c.options.length,gradeProfiles[grade].choiceCount);assert.equal(new Set(c.options).size,gradeProfiles[grade].choiceCount);assert.ok(c.options[c.answer]);assert.ok(c.evidence.every(i=>c.paragraphs[i]));assert.ok(c.rubric);if(grade===3){assert.ok(!families.has(c.familyId));families.add(c.familyId);}}
 }
 assert.equal(families.size,48);
});
for(const grade of [1,2])test(`초${grade} 말로 설명: 교사 관찰 전·도움받은 응답은 독립 성취로 승격하지 않는다`,async t=>{
 const f=await fixture(t,grade,'connect',true),r=await f.initialize(),p=r.plan;
 for(const tr of p.training)await train(f,tr.assignmentId);
 const a=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check;
 const c=courseBundle(grade,'connect',lessons).checks[0];
 const submitted=(await f.student('/learning/course/check/submit',{checkId:a.id,revision:0,answer:{choice:c.answer,evidence:c.evidence,reason:'',responseMode:'oral_requested'},oralObservation:{transcript:'학생이 적었다고 주장한 내용',support:'independent'}})).check;
 await assert.rejects(f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:a.id,revision:submitted.revision,outcome:'success',note:'관찰 없는 자동 성공 시도'}),/실제 말한 내용/);
 let record=(await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:a.id,revision:submitted.revision,outcome:'success',note:'질문 도움을 준 뒤 설명했습니다.',oralObservation:{transcript:'젖은 곳을 피하려고 했어요.',support:'prompted'}})).course;
 assert.equal(record.plan.attainment.successes,0);
 let old=record.plan.checks[0];
 record=(await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:a.id,revision:old.revision,outcome:'success',note:'도움 이력은 보존해야 합니다.',oralObservation:{transcript:'다시 적은 설명',support:'independent'}})).course;
 assert.equal(record.plan.checks[0].oralObservation.support,'prompted');assert.equal(record.plan.attainment.successes,0);
 const b=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check,d=courseBundle(grade,'connect',lessons).checks[1];
 const answer=(await f.student('/learning/course/check/submit',{checkId:b.id,revision:0,answer:{choice:d.answer,evidence:d.evidence,reason:'',responseMode:'oral_requested'}})).check;
 record=(await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:b.id,revision:answer.revision,outcome:'success',note:'학생이 직접 읽고 설명하고 교사는 받아 적기만 했습니다.',oralObservation:{transcript:'문을 열려고 열쇠가 필요했어요.',support:'independent'}})).course;
 assert.equal(record.plan.attainment.successes,1);assert.equal(record.plan.checks[1].firstAnswer.reason,'');
});
test('existing grade-4 diagnostics and approved check snapshots retain their original versions after expansion',async t=>{
 const f=await fixture(t,4),record=await f.initialize();
 const db=new DatabaseSync(f.dbPath),row=db.prepare('SELECT id,tenant_id,body FROM learning_placements').get(),old=JSON.parse(row.body);
 const legacy={...old,version:'g34-pilot-1',status:'in_progress',branch:null,answers:{},revision:0};delete legacy.formSnapshot;delete legacy.assignmentId;delete legacy.decision;
 db.prepare('UPDATE learning_placements SET body=? WHERE id=?').run(JSON.stringify(legacy),row.id);
 const courseRow=db.prepare('SELECT id,body FROM learning_courses').get(),course=JSON.parse(courseRow.body);course.plan.policyVersion='g34-course-1';course.plan.checkBank[0].prompt='이전 승인 버전의 질문';db.prepare('UPDATE learning_courses SET body=? WHERE id=?').run(JSON.stringify(course),courseRow.id);db.close();
 let p=(await f.student('/learning/placement')).placement;assert.equal(p.form.version,'g34-pilot-1');assert.equal(p.form.passages.find(x=>x.id==='library').paragraphs.length,2);assert.equal('formSnapshot'in p,false);
 for(const q of legacyPlacementForm(4).questions)p=(await f.student('/learning/placement/answer',{questionId:q.id,choice:q.answer,revision:p.revision})).placement;
 p=(await f.student('/learning/placement/submit',{revision:p.revision})).placement;assert.equal(p.form.version,'g34-pilot-1');await f.restart();assert.deepEqual((await f.student('/learning/placement')).placement.form,p.form);
 for(const q of legacyPlacementForm(4,p.branch).questions.filter(q=>!p.answers[q.id]))p=(await f.student('/learning/placement/answer',{questionId:q.id,revision:p.revision,...(q.options.length?{choice:q.answer}:{text:'이전 문항의 근거를 연결해 설명했습니다.',evidence:q.evidence})})).placement;
 p=(await f.student('/learning/placement/submit',{revision:p.revision})).placement;assert.equal(p.recommendation.policyVersion,'g34-pilot-1');
 for(const tr of record.plan.training)await train(f,tr.assignmentId);
 const check=(await f.student('/learning/course/check/start',{planId:record.plan.id,purpose:'independent'})).check;assert.equal(check.content.prompt,'이전 승인 버전의 질문');assert.equal((await f.student('/learning/course')).course.plan.policyVersion,'g34-course-1');
});
test('a course check already presented in a pilot is skipped as independent mastery evidence',async t=>{
 const f=await fixture(t),r=await f.initialize(),p=r.plan;
 for(const tr of p.training)await train(f,tr.assignmentId);
 const db=new DatabaseSync(f.dbPath),state=JSON.parse(db.prepare('SELECT body FROM exam_state').get().body),student=state.users.find(s=>s.id===f.studentId);
 db.prepare('INSERT INTO pilot_runs VALUES(?,?,?)').run(student.tenantId+':pilot-seen',student.tenantId,JSON.stringify({id:'pilot-seen',studentId:f.studentId,teacherId:'synthetic',items:[{key:'pilot-first',familyId:'course-source:connect:0'}],presented:{'pilot-first':Date.now()}}));db.close();
 const check=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check;
 assert.equal(check.content.familyId,'course-source:connect:1');
});

test('editorial keys stay private until teacher review, then released feedback matches the approved snapshot',async t=>{
 const f=await fixture(t,4,'interpret'),r=await f.initialize(),p=r.plan;
 for(const tr of p.training)await train(f,tr.assignmentId);
 const c=courseBundle(4,'interpret',lessons).checks[0];
 const started=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check;
 for(const k of ['answer','evidence','explanation','optionReasons','evidenceQuotes','scoringGuide','editorialReview','difficulty'])assert.equal(k in started.content,false);
 assert.equal('feedback'in started,false);
 const submitted=(await f.student('/learning/course/check/submit',{checkId:started.id,revision:0,answer:{choice:c.answer,evidence:c.evidence,reason:'본문 단서를 판단과 연결했습니다.'}})).check;
 assert.equal('feedback'in submitted,false);assert.equal(JSON.stringify((await f.student('/learning/course')).course).includes(c.explanation),false);
 const reviewed=(await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:started.id,revision:submitted.revision,outcome:'success',note:'학생의 단서와 설명을 확인했습니다.'})).course.plan.checks[0];
 assert.equal(reviewed.content.explanation,c.explanation);
 const released=(await f.student('/learning/course')).course.plan.checks[0];
 assert.equal(released.feedback.explanation,c.explanation);assert.deepEqual(released.feedback.evidenceQuotes,c.evidenceQuotes);assert.equal(released.feedback.answer,c.answer);assert.equal('explanation'in released.content,false);
});

test('version-2 common diagnostic keeps its original branch and approved checks keep original evidence rules',async t=>{
 const f=await fixture(t,4,'interpret'),r=await f.initialize(),p=r.plan;
 const db=new DatabaseSync(f.dbPath),row=db.prepare('SELECT id,body FROM learning_placements').get(),old=JSON.parse(row.body);
 Object.assign(old,{version:'g16-placement-2',formSnapshot:placementFormAtVersion(4,null,'g16-placement-2'),status:'in_progress',branch:null,answers:{},revision:0});delete old.assignmentId;delete old.decision;
 db.prepare('UPDATE learning_placements SET body=? WHERE id=?').run(JSON.stringify(old),row.id);
 const courseRow=db.prepare('SELECT id,body FROM learning_courses').get(),course=JSON.parse(courseRow.body),bank=courseBundle(4,'interpret',lessons,{reviewed:false}).checks;
 course.plan.policyVersion='g16-course-2';course.plan.checkBank=[bank[3],...bank.filter((_,i)=>i!==3)];db.prepare('UPDATE learning_courses SET body=? WHERE id=?').run(JSON.stringify(course),courseRow.id);db.close();
 let placement=(await f.student('/learning/placement')).placement;
 for(const q of old.formSnapshot.questions)placement=(await f.student('/learning/placement/answer',{questionId:q.id,choice:q.answer,revision:placement.revision})).placement;
 placement=(await f.student('/learning/placement/submit',{revision:placement.revision})).placement;
 assert.equal(placement.form.version,'g16-placement-2');assert.deepEqual(placement.form,JSON.parse(JSON.stringify(publicForm(placementFormAtVersion(4,placement.branch,'g16-placement-2')))));await f.restart();assert.deepEqual((await f.student('/learning/placement')).placement.form,placement.form);
 for(const tr of p.training)await train(f,tr.assignmentId);
 const c=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check;
 const submitted=(await f.student('/learning/course/check/submit',{checkId:c.id,revision:0,answer:{choice:bank[3].answer,evidence:[1],reason:'이전 버전의 일부 근거만 선택했습니다.'}})).check;
 assert.equal(submitted.evidenceMatch,false,'new minimal evidence policy must not rewrite older approved scoring');
 await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:c.id,revision:submitted.revision,outcome:'success',note:'설명은 확인했으나 이전 승인 근거 기준을 유지합니다.'});
 const state=(await f.student('/learning/course')).course;assert.equal(state.plan.policyVersion,'g16-course-2');assert.equal(state.plan.attainment.successes,0);assert.equal('feedback'in state.plan.checks[0],false);
});

test('upper grade placement can continue from evidence evaluation to integration with grade-matched new materials',async t=>{
 const f=await fixture(t,6,'evaluate'),r=await f.initialize(),p=r.plan;
 for(const tr of p.training)await train(f,tr.assignmentId);
 for(let i=0;i<5;i++){if(i===3)await f.tick();await check(f,p);}
 await check(f,p,'transfer');const preview=await f.teacher('/learning/course/preview',{studentId:f.studentId,next:true});assert.equal(preview.bundle.course,'integrate');assert.ok(preview.bundle.checks.every(c=>c.grade===6));
 const latest=(await f.student('/learning/course')).course;
 const moved=(await f.teacher('/learning/course/activate',{studentId:f.studentId,next:true,previousPlanId:p.id,revision:latest.revision,contentHash:preview.bundle.hash,approved:true,note:'자료의 범위와 복합 조건을 확인하고 통합으로 이동합니다.'})).course;
 assert.equal(moved.plan.course,'integrate');assert.equal(moved.nextCourse,null);assert.equal(moved.history[0].course,'evaluate');
});
for(const grade of learningGrades)test(`초${grade} 4주 계획, independent+transfer gate, next stage and delayed maintenance`,async t=>{
 const f=await fixture(t,grade),r=await f.initialize(),p=r.plan;
 assert.equal(p.sessions.length,8);assert.deepEqual(p.sessions.map(s=>s.week),[1,1,2,2,3,3,4,4]);
 assert.equal((await f.student('/learning/dashboard')).assignments.length,3);
 assert.equal((await f.initialize()).plan.id,p.id);
 await assert.rejects(f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'}),/두 학습/);
 for(const tr of p.training)await train(f,tr.assignmentId);
 assert.equal((await f.student('/learning/course')).course.plan.attainment.total,0,'practiced lessons do not award mastery');
 await assert.rejects(f.teacher('/learning/course/preview',{studentId:f.studentId,next:true}),/성취|독립 수행/);
 for(let i=0;i<5;i++)await check(f,p);
 let state=(await f.student('/learning/course')).course;assert.equal(state.plan.attainment.independent,false,'five checks on one day do not pass');
 await assert.rejects(f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'}),/다음 수업일/);
 await f.tick();await check(f,p);
 state=(await f.student('/learning/course')).course;assert.equal(state.plan.attainment.independent,true);
 const pending=await check(f,p,'transfer',{review:false});
 await assert.rejects(f.teacher('/learning/course/preview',{studentId:f.studentId,next:true}),/성취|독립/);
 await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:pending.check.id,revision:pending.check.revision,outcome:'success',note:'새 상황에서 정보와 조건을 연결했습니다.'});
 assert.equal((await f.student('/learning/course')).course.plan.attainment.ready,true);
 await assert.rejects(f.student('/learning/course/check/start',{planId:p.id,purpose:'maintenance'}),/7일/);
 const preview=await f.teacher('/learning/course/preview',{studentId:f.studentId,next:true});assert.equal(preview.bundle.course,'interpret');
 state=(await f.student('/learning/course')).course;
 const body={studentId:f.studentId,next:true,previousPlanId:p.id,revision:state.revision,contentHash:preview.bundle.hash,approved:true,note:'성취 근거를 확인하고 의미 풀기로 이동합니다.'};
 const moved=(await f.teacher('/learning/course/activate',body)).course;
 assert.equal(moved.history[0].id,p.id);assert.equal(moved.plan.course,'interpret');assert.equal(moved.decisions.at(-1).from,p.id);
 assert.equal((await f.teacher('/learning/course/activate',body)).course.plan.id,moved.plan.id);
 await f.tick(7);await check(f,p,'maintenance',{wrong:grade===3});await f.restart();
 state=(await f.student('/learning/course')).course;assert.equal(state.history[0].attainment.maintained,grade!==3);assert.equal(state.plan.attainment.total,0);assert.equal(state.plan.course,'interpret');
 if(grade===3){assert.equal(state.history[0].attainment.needsRecheck,true);const failed=state.history[0].checks.find(a=>a.purpose==='maintenance');await f.teacher('/learning/course/remediate',{studentId:f.studentId,checkId:failed.id});assert.equal((await f.student('/learning/course')).course.history[0].remediations.length,1);await assert.rejects(f.student('/learning/course/check/start',{planId:p.id,purpose:'maintenance'}),/자료가 부족/);}
 assert.equal(state.exposures.length,8);
});
test('immutable confirmation, wrong answers cannot be teacher-promoted, save/resume, remedial assignment and access scope',async t=>{
 const f=await fixture(t),r=await f.initialize(),p=r.plan;
 for(const tr of p.training)await train(f,tr.assignmentId);
 const a=(await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check;
 assert.equal((await f.student('/learning/course/check/start',{planId:p.id,purpose:'independent'})).check.id,a.id);
 const answer={choice:0,evidence:[0],reason:'저장한 초안'};
 await f.student('/learning/course/check/save',{checkId:a.id,revision:0,answer});await f.restart();
 let own=(await f.student('/learning/course')).course;assert.deepEqual(own.plan.checks[0].answer,answer);
 await assert.rejects(f.student('/learning/course/check/save',{checkId:a.id,revision:0,answer}),/다른 화면/);
 const c=courseBundle(3,'connect',lessons).checks.find(c=>c.id===a.content.id);
 const submitted=await f.student('/learning/course/check/submit',{checkId:a.id,revision:1,answer:{...answer,choice:(c.answer+1)%c.options.length}});
 await f.student('/learning/course/check/submit',{checkId:a.id,revision:0,answer:{...answer,choice:c.answer}});
 await f.teacher('/learning/course/check/review',{studentId:f.studentId,checkId:a.id,revision:submitted.check.revision,outcome:'success',note:'설명은 적절하나 선택 답은 다시 확인'});
 own=(await f.student('/learning/course')).course;assert.equal(own.plan.attainment.successes,0);assert.equal(own.plan.checks[0].firstAnswer.choice,(c.answer+1)%c.options.length);
 const rem=await f.teacher('/learning/course/remediate',{studentId:f.studentId,checkId:a.id});assert.equal(rem.course.plan.remediations.length,1);
 await f.teacher('/learning/course/remediate',{studentId:f.studentId,checkId:a.id});assert.equal((await f.student('/learning/dashboard')).assignments.length,4);
 await assert.rejects(f.other('/learning/course/check/save',{checkId:a.id,revision:1,answer}),/본인의 확인/);
 await assert.rejects(f.other('/learning/course/activate',{studentId:f.studentId}),/담당 재원/);
 await assert.rejects(f.parent('/learning/course'),/학생과 담당 교사/);
 assert.equal((await f.other('/learning/course')).course,null);
});
