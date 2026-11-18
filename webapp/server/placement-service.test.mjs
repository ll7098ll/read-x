import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createExamService } from './exam-service.mjs';
import { createHttpExamClient } from '../shared/http-exam-client.mjs';
import { placementForm, profileFor, recommend, courseLessons } from './placement-content.mjs';
import {gradeProfiles,learningGrades} from '../shared/learning-config.mjs';
const password='Placement-Test-2026';
async function fixture(t){
 const dir=mkdtempSync(join(tmpdir(),'readx-placement-'));
 let service,server;
 const boot=async()=>{service=createExamService({dbPath:join(dir,'test.sqlite'),privacyMode:'synthetic',timer:false});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));};
 await boot();
 const stop=async()=>{await new Promise(r=>server.close(r));service.close();};
 t.after(async()=>{await stop();rmSync(dir,{recursive:true,force:true});});
 const client=()=>{let cookie='';const http=createHttpExamClient({fetcher:async(path,options)=>{const origin=`http://127.0.0.1:${server.address().port}`;const res=await fetch(origin+path,{...options,headers:{...options.headers,Cookie:cookie,Origin:origin}});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];return res;}});return http;};
 const teacher=client(),student=client(),other=client(),parent=client();
 await teacher('/setup',{name:'교사',username:'teacher',password});
 const enrolled=await teacher('/roster',{student:{name:'진단 학생',username:'student',password},parent:{name:'보호자',username:'parent',password}});
 await teacher('/roster',{student:{name:'다른 학생',username:'other',password}});
 await student('/login',{username:'student',password});await other('/login',{username:'other',password});await parent('/login',{username:'parent',password});
 return {teacher,student,other,parent,enrolled,restart:async()=>{await stop();await boot();}};
}
async function answerAll(client,r,wrong=false){
 const full=placementForm(r.grade,r.branch);
 for(const q of full.questions.filter(q=>!r.answers[q.id])){
   const answer=q.options.length?{choice:wrong?(q.answer+1)%q.options.length:q.answer}:{text:'설명'};
   if(!q.options.length)Object.assign(answer,{text:'비가 많이 와서 다리를 막았고, 돌아가는 길은 더 오래 걸립니다.',evidence:q.evidence});
   r=(await client('/learning/placement/answer',{revision:r.revision,questionId:q.id,...answer})).placement;
 }
 return r;
}
for(const grade of learningGrades)test(`초${grade}: 진단 분기 → 교사 배치 → 첫 수업 저장·제출, 재시작·중복 요청`,async t=>{
 const f=await fixture(t);
 let r=(await f.student('/learning/placement/start',{grade})).placement;
 assert.equal(r.form.questions.length,gradeProfiles[grade].commonCount);assert.equal('formSnapshot'in r,false);assert.ok(r.form.questions.every(q=>!('answer'in q)&&!('evidence'in q)));
 await assert.rejects(f.student('/learning/placement/submit',{revision:0}),/모든 문항/);
 const q=placementForm(grade).questions[0];
 r=(await f.student('/learning/placement/answer',{revision:0,questionId:q.id,choice:q.answer})).placement;
 assert.equal((await f.student('/learning/placement/answer',{revision:0,questionId:q.id,choice:q.answer})).placement.revision,1);
 await assert.rejects(f.student('/learning/placement/answer',{revision:0,questionId:q.id,choice:(q.answer+1)%q.options.length}),/다른 화면/);
 await f.restart();assert.equal((await f.student('/learning/placement')).placement.revision,1);
 r=await answerAll(f.student,r,grade===3);
 r=(await f.student('/learning/placement/submit',{revision:r.revision})).placement;
 assert.equal(r.branch,grade===3?'support':'extend');assert.equal(r.form.questions.length,gradeProfiles[grade].totalCount);
 r=await answerAll(f.student,r,grade===3);
 r=(await f.student('/learning/placement/submit',{revision:r.revision})).placement;
 assert.equal(r.status,'awaiting_teacher');assert.equal(r.recommendation.course,grade===3?'words':grade>=5?'evaluate':'connect');
 assert.equal((await f.other('/learning/placement')).placement,null);
 await assert.rejects(f.parent('/learning/placement'),/학생과 담당 교사/);
 await assert.rejects(f.student('/learning/placement/answer',{revision:r.revision,questionId:q.id,choice:0}),/진행 중/);
 const teacherRecord=(await f.teacher('/learning/placement')).placements[0];assert.equal(teacherRecord.form.questions[0].answer,q.answer);
 const lessonId=courseLessons[grade][r.recommendation.course];
 const body={studentId:r.studentId,revision:r.revision,course:r.recommendation.course,level:r.recommendation.level,lessonId,note:'진단과 설명을 검토했으며 첫 2회에 근거 연결을 확인합니다.',explanationReviews:['success','needs_support'],...(grade<=2?{readingObservation:{state:'follow_up',note:'첫 수업에서 실제 읽기를 관찰합니다.'}}:{})};
 await assert.rejects(f.teacher('/learning/placement/approve',body),/시범 승인/);
 await assert.rejects(f.other('/learning/placement/approve',body),/담당 재원 학생/);
 const preview=await f.teacher(`/learning/catalog/${lessonId}`);
 await f.teacher('/learning/approvals',{lessonId,contentHash:preview.contentHash,note:'본문과 정답 근거를 검토했습니다.',pilot:true});
 const approved=(await f.teacher('/learning/placement/approve',body)).placement;
 assert.equal((await f.teacher('/learning/placement/approve',body)).placement.assignmentId,approved.assignmentId);
 assert.equal((await f.student('/learning/dashboard')).assignments.length,1);
 assert.equal(approved.status,'provisional');assert.deepEqual(approved.initialAnswers,r.answers);
 await assert.rejects(f.other(`/learning/assignments/${approved.assignmentId}/start`,{}),/배정된 수업/);
 const first=await f.student(`/learning/assignments/${approved.assignmentId}/start`,{});
 assert.equal(first.lesson.grade,grade);assert.equal((await f.student(`/learning/assignments/${approved.assignmentId}/start`,{})).id,first.id);
 const run=structuredClone(first.run),qs=first.lesson.levelQuestions?.[first.assignment.level]||first.lesson.questions;
 for(const q of qs)run.responses[q.id]={choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문의 근거와 관계를 연결해 설명합니다.',hintLevel:0,revealed:false,submissions:[{id:'first-'+q.id,choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'본문의 근거와 관계를 연결해 설명합니다.',hintLevel:0}]};
 const saved=await f.student(`/learning/runs/${first.id}/save`,{revision:0,mutationId:'first-save',run,writing:'오늘은 필요한 근거를 찾아 연결하는 방법을 배웠습니다.'});
 assert.equal((await f.student(`/learning/runs/${first.id}/submit`,{revision:saved.revision})).status,'submitted');
 assert.ok((await f.teacher('/learning/dashboard')).runs.some(r=>r.id===first.id&&r.status==='submitted'));
});
test('진단 문항 무결성과 기능별 배치: 어휘 강점·관계 어려움을 구별한다',()=>{
 for(const grade of learningGrades)for(const branch of [null,'support','extend']){
  const form=placementForm(grade,branch);assert.equal(new Set(form.questions.map(q=>q.id)).size,form.questions.length);
  for(const q of form.questions){const p=form.passages.find(p=>p.id===q.passageId);assert.ok(p);assert.ok(q.evidence.every(i=>p.paragraphs[i]));if(q.options.length){assert.equal(q.options.length,gradeProfiles[grade].choiceCount);assert.equal(new Set(q.options).size,gradeProfiles[grade].choiceCount);assert.ok(q.options[q.answer]);}}
 }
 const form=placementForm(4,'extend'),answers=Object.fromEntries(form.questions.map(q=>[q.id,{choice:q.skill==='connect'?(q.answer+1)%q.options.length:q.answer}]));
 assert.equal(recommend(form,answers).course,'connect');assert.equal(recommend(form,answers).level,'standard');assert.equal(profileFor(form,answers)[0].correct,5);
});
