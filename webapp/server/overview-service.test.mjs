import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { createExamService } from './exam-service.mjs';
import { exam, transfers } from './content/g5-01.mjs';
import { overviewCsv } from './overview-service.mjs';

const password='Overview-Integration-2026';
async function fixture(t) {
  let at=Date.UTC(2026,10,13,15,30);
  const service=createExamService({privacyMode: 'synthetic',dbPath:':memory:',timer:false,now:()=>at});
  const server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));
  t.after(async()=>{await new Promise(r=>server.close(r));service.close();});
  const origin=`http://127.0.0.1:${server.address().port}`;
  const client=()=>{let cookie='';return async(path,body,expected=200)=>{const res=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];const data=await res.json();assert.equal(res.status,expected,JSON.stringify(data));return data;};};
  const teacher=client();await teacher('/setup',{name:'검증 원장',username:'owner',password,className:'A반'});
  const classA=(await teacher('/org/dashboard')).classes[0],classB=(await teacher('/org/classes',{name:'B반'})).class;
  const one=await teacher('/roster',{classId:classA.id,student:{name:'=SUM(1,2)',username:'student1',password},parent:{name:'보호자',username:'parent',password}});
  const two=await teacher('/roster',{classId:classA.id,student:{name:'학생 둘',username:'student2',password}});
  await teacher('/org/teachers',{name:'B 교사',username:'teacher_b',password,classIds:[classB.id]});
  const student=client(),parent=client(),otherTeacher=client();await student('/login',{username:'student1',password});await parent('/login',{username:'parent',password});await otherTeacher('/login',{username:'teacher_b',password});
  const l=(await teacher('/learning/catalog')).lessons.find(l=>l.grade===5),preview=await teacher('/learning/catalog/'+l.id);
  await teacher('/learning/approvals',{lessonId:l.id,contentHash:preview.contentHash,note:'집계 연결 검사용 시범 승인',pilot:true});
  const assign=async(ids=[one.student.id,two.student.id])=>(await teacher('/learning/assignments',{lessonId:l.id,studentIds:ids,level:'standard',dueAt:at+86400000})).assignment;
  const filters={startDate:'2026-11-14',endDate:'2026-11-15'};
  const relogin=async()=>{for(const [c,name] of [[teacher,'owner'],[student,'student1'],[parent,'parent'],[otherTeacher,'teacher_b']])await c('/login',{username:name,password});};
  return {teacher,student,parent,otherTeacher,one,two,classA,classB,assign,filters,relogin,setTime:v=>{at=v;},now:()=>at};
}
async function submittedReading(f) {
  const assignment=await f.assign(),r=await f.student(`/learning/assignments/${assignment.id}/start`,{}),run=structuredClone(r.run);
  const qs=r.lesson.questions,first=qs.find(q=>q.responseKind!=='explanation'),paragraphs=['supported','standard'].flatMap(l=>r.lesson.layers[l]);
  for(const [i,q] of qs.entries())run.responses[q.id]={choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'공개 전에는 보이지 않아야 하는 응답',hintLevel:i===1?2:0,revealed:false,submissions:[{id:'first-'+q.id,choice:q.responseKind==='explanation'?null:q.answer,evidence:q.evidence,reason:'공개 전에는 보이지 않아야 하는 응답',hintLevel:i===1?2:0}]};
  const wrong=(first.answer+1)%first.options.length,wrongEvidence=[paragraphs.find(p=>!first.evidence.includes(p.id)).id];
  Object.assign(run.responses[first.id],{choice:wrong,evidence:wrongEvidence});Object.assign(run.responses[first.id].submissions[0],{choice:wrong,evidence:wrongEvidence});
  let saved=await f.student(`/learning/runs/${r.id}/save`,{revision:0,mutationId:'first-save',run,writing:'자기 설명 원문'});
  const revised=structuredClone(saved.run);revised.responses[first.id].choice=first.answer;revised.responses[first.id].evidence=first.evidence;revised.responses[first.id].reason='고친 설명';revised.responses[first.id].hintLevel=1;
  revised.responses[first.id].submissions.push({id:'second-first',choice:first.answer,evidence:first.evidence,reason:'고친 설명',hintLevel:1});
  saved=await f.student(`/learning/runs/${r.id}/save`,{revision:saved.revision,mutationId:'revised-save',run:revised,writing:'수정한 자기 설명'});
  const submitted=await f.student(`/learning/runs/${r.id}/submit`,{revision:saved.revision});
  const reviews=Object.fromEntries(qs.map((q,i)=>[q.id,{outcome:i===4?'needs_support':'success',note:'검토 의견 '+i}]));
  return {assignment,run:submitted,qs,reviews};
}

test('overview preserves first answers, distinguishes missing and zero, and uses published guardian snapshots',async t=>{
  const f=await fixture(t),r=await submittedReading(f);
  const teacher=await f.teacher('/overview',f.filters),student=await f.student('/overview',f.filters),before=await f.parent('/overview',f.filters);
  assert.equal(teacher.totals.completion.numerator,1);assert.equal(teacher.totals.completion.denominator,2);
  assert.equal(student.totals.completion.denominator,1);
  const choices=r.qs.filter(q=>q.responseKind!=='explanation').length;
  assert.equal(student.totals.firstChoice.denominator,choices);assert.equal(student.totals.firstChoice.numerator,choices-1);
  assert.equal(student.totals.firstEvidence.numerator,4);assert.equal(student.totals.firstEvidence.denominator,5);
  assert.equal(student.totals.hints.numerator,1);assert.equal(student.totals.hints.denominator,5);
  assert.equal(student.totals.firstChoice.percent,0);assert.equal(student.totals.revisions,1);assert.equal(student.totals.teacherExplanation.percent,null);
  assert.equal(before.totals.firstChoice.percent,null);assert.equal(before.records[0].runId,null);
  assert.ok(!JSON.stringify(before).includes('공개 전에는 보이지 않아야 하는 응답'));
  let published=await f.teacher(`/learning/runs/${r.run.id}/review`,{revision:r.run.revision,reviews:r.reviews,note:'공개 의견',publish:true});
  const guardian=await f.parent('/overview',f.filters),own=await f.student('/overview',f.filters),scoped=await f.teacher('/overview',{...f.filters,studentId:f.one.student.id});
  for(const key of ['firstChoice','firstEvidence','hints','teacherExplanation']){assert.deepEqual(guardian.totals[key],own.totals[key]);assert.deepEqual(scoped.totals[key],own.totals[key]);}
  assert.equal(guardian.totals.teacherExplanation.percent,80);
  const altered={...r.reviews,[r.qs[0].id]:{outcome:'needs_support',note:'비공개 수정 의견'}};
  published=await f.teacher(`/learning/runs/${r.run.id}/review`,{revision:published.revision,reviews:altered,note:'비공개 종합 수정'});
  const frozen=await f.parent('/overview',f.filters);assert.equal(frozen.totals.teacherExplanation.percent,80);assert.ok(!JSON.stringify(frozen).includes('비공개'));
  assert.equal((await f.student('/overview',f.filters)).totals.teacherExplanation.percent,60);
  await f.teacher(`/learning/runs/${r.run.id}/revoke`,{});assert.equal((await f.parent('/overview',f.filters)).totals.teacherExplanation.denominator,0);
});

test('Korean date boundaries, class and student permissions and exported records match the report',async t=>{
  const f=await fixture(t);await f.assign();f.setTime(Date.UTC(2026,10,14,15,30));await f.relogin();await f.assign([f.one.student.id]);
  const first=await f.teacher('/overview',{startDate:'2026-11-14',endDate:'2026-11-14'});assert.equal(first.records.length,2);
  const second=await f.teacher('/overview',{startDate:'2026-11-15',endDate:'2026-11-15'});assert.equal(second.records.length,1);
  assert.equal(second.weekly[0].start,'2026-11-09');
  assert.equal(first.csv,undefined);await f.teacher('/overview/export',{startDate:'2026-11-14',endDate:'2026-11-14'},400);
  const exported=await f.teacher('/overview/export',{startDate:'2026-11-14',endDate:'2026-11-14',purpose:'teaching'});assert.equal(exported.csv,overviewCsv(first));assert.equal(exported.records,first.records.length);
  assert.ok(exported.csv.includes("'=SUM(1,2)"));assert.equal(exported.csv.split('\r\n').length,3);
  await f.otherTeacher('/overview',{...f.filters,classId:f.classA.id},403);await f.otherTeacher('/overview',{...f.filters,studentId:f.one.student.id},403);
  assert.equal((await f.otherTeacher('/overview',f.filters)).records.length,0);
  await f.parent('/overview',{...f.filters,studentId:f.two.student.id},403);await f.teacher('/overview',{startDate:'2026-02-30',endDate:'2026-11-14'},400);
  assert.ok(!JSON.stringify(first).includes('NaN'));assert.equal(first.totals.firstChoice.percent,null);
});

test('exam scores wait for release and transfer confirmation requires fresh work and teacher evidence review',async t=>{
  const f=await fixture(t),a=(await f.teacher('/assignments',{studentIds:[f.one.student.id],opensAt:f.now()-1000,closesAt:f.now()+3600000})).assignment;
  const {attempt}=await f.student(`/assignments/${a.id}/start`,{}),items=exam.passages.flatMap(p=>p.questions);
  await f.student(`/attempts/${attempt.id}/answers`,{changes:items.slice(0,2).map(q=>({id:q.id,choice:q.answer,seq:1}))});await f.student(`/attempts/${attempt.id}/submit`,{});
  assert.equal((await f.teacher('/overview',f.filters)).totals.examAccuracy.numerator,2);
  assert.equal((await f.student('/overview',f.filters)).totals.examAccuracy.denominator,0);
  await f.teacher(`/assignments/${a.id}/release`,{});assert.equal((await f.student('/overview',f.filters)).totals.examAccuracy.denominator,24);assert.equal((await f.parent('/overview',f.filters)).totals.examAccuracy.denominator,0);
  await f.teacher(`/attempts/${attempt.id}/review`,{note:'공개 평가 의견',publish:true});
  const {followup}=await f.teacher(`/attempts/${attempt.id}/followups`,{questionId:items[2].id});
  await f.student(`/followups/${followup.id}/review`,{reflection:'원문 근거를 다시 확인했습니다.'});
  const transfer=transfers.find(v=>v.goal===followup.goal);
  await f.student(`/followups/${followup.id}/complete`,{choice:transfer.answer,evidence:transfer.evidence});
  assert.equal((await f.parent('/overview',f.filters)).followups.confirmedTransfer.denominator,0);
  await f.teacher(`/followups/${followup.id}/feedback`,{outcome:'supported',comment:'새 글 근거를 확인했습니다.'});
  const report=await f.parent('/overview',f.filters);assert.equal(report.totals.examAccuracy.percent,8.3);assert.deepEqual(report.followups.confirmedTransfer,{numerator:1,denominator:1,percent:100});
  await f.student(`/followups/${followup.id}/complete`,{choice:transfer.answer,evidence:transfer.evidence});
  await f.student(`/followups/${followup.id}/complete`,{choice:(transfer.answer+1)%transfer.options.length,evidence:'검토 후 답과 근거 변경'},409);
  await f.student(`/followups/${followup.id}/review`,{reflection:'검토 후 원문 복습 기록 변경'},409);
  const {followup:again}=await f.teacher(`/attempts/${attempt.id}/followups`,{questionId:items[3].id});
  await f.student(`/followups/${again.id}/review`,{reflection:'같은 목표의 글을 다시 열었습니다.'});
  await f.student(`/followups/${again.id}/complete`,{choice:transfer.answer,evidence:transfer.evidence});
  await f.teacher(`/followups/${again.id}/feedback`,{outcome:'supported',comment:'재노출 글 확인'});
  const repeated=await f.parent('/overview',f.filters);assert.equal(repeated.followups.completed,2);assert.equal(repeated.followups.confirmedTransfer.denominator,1);
});

test('CSV formula protection also covers leading whitespace and quotes',()=>{
  const blank={activities:{numerator:0,denominator:0},firstChoice:{numerator:0,denominator:0},firstEvidence:{numerator:0,denominator:0},hints:{numerator:0,denominator:0},teacherExplanation:{numerator:0,denominator:0},examAccuracy:{numerator:0,denominator:0}};
  const csv=overviewCsv({records:[{kind:'lesson',studentName:'  +cmd',className:'A',title:'"quoted"',assignedAt:Date.UTC(2026,10,14),status:'not_started',metrics:blank}]});
  assert.ok(csv.includes("'  +cmd"));assert.ok(csv.includes('""quoted""'));assert.ok(csv.startsWith('\ufeff'));
});
