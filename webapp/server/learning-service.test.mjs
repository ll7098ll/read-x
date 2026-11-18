import { createHttpExamClient } from '../shared/http-exam-client.mjs';
import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { createExamService } from './exam-service.mjs';

const password = 'Learning-Integration-2026';
async function fixture(t, { dbPath = ':memory:' } = {}) {
  let time = Date.now();
  const service = createExamService({privacyMode: 'synthetic', dbPath, timer: false, now: () => time });
  const server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  let closed = false;
  const stop = async () => { if (closed) return; closed = true; await new Promise(r => server.close(r)); service.close(); };
  t.after(stop);
  const origin = `http://127.0.0.1:${server.address().port}`;
  const client = () => {
    let cookie = '';
    const transport = createHttpExamClient({ fetcher: async (path, options) => {
      const res = await fetch(origin+path, { ...options, headers: { ...options.headers, Cookie:cookie, Origin:origin } });
      if (res.headers.get('set-cookie')) cookie=res.headers.get('set-cookie').split(';')[0]; return res;
    } });
    return async (path, body, expected = 200) => {
      if (expected === 200) return transport(path, body);
      const res = await fetch(origin+'/api/exam'+path, { method: body === undefined ? 'GET' : 'POST', headers: { Cookie: cookie, Origin: origin, 'Content-Type':'application/json' }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });
      if (res.headers.get('set-cookie')) cookie = res.headers.get('set-cookie').split(';')[0];
      const data = await res.json(); assert.equal(res.status, expected, JSON.stringify(data)); return data;
    };
  };
  const teacher = client(), student = client(), parent = client(), other = client();
  await teacher('/setup', { name:'교사', username:'teacher', password });
  const enrolled = await teacher('/roster', { student: { name:'학생', username:'student', password }, parent: { name:'보호자', username:'parent', password } });
  await teacher('/roster', { student: { name:'다른 학생', username:'other', password } });
  await student('/login', { username:'student', password }); await parent('/login', { username:'parent', password }); await other('/login', { username:'other', password });
  const catalog = await teacher('/learning/catalog');
  const preview = await teacher(`/learning/catalog/${catalog.lessons[0].id}`);
  const create = () => teacher('/learning/assignments', { lessonId:preview.lesson.id, studentIds:[enrolled.student.id], level:'standard', dueAt:Date.now()+86400000 });
  return { teacher, student, parent, other, enrolled, preview, create, stop, setTime: at => { time=at; } };
}
const approve = f => f.teacher('/learning/approvals', { lessonId:f.preview.lesson.id, contentHash:f.preview.contentHash, note:'지문과 문항의 학년 적합성 및 정답 근거를 검토했습니다.', pilot:true });

test('teacher approval, immutable first answers, server grading, submission and frozen parent release', async t => {
  const f = await fixture(t);
  await f.teacher('/learning/assignments', { lessonId:f.preview.lesson.id, studentIds:[f.enrolled.student.id], level:'standard', dueAt:Date.now()+86400000 },409);
  await approve(f); const { assignment } = await f.create();
  const first = await f.student(`/learning/assignments/${assignment.id}/start`,{});
  assert.equal((await f.student(`/learning/assignments/${assignment.id}/start`,{})).id,first.id);
  await f.other(`/learning/runs/${first.id}`,undefined,404);
  await f.parent(`/learning/runs/${first.id}`,undefined,404);
  const run = structuredClone(first.run), qs = first.lesson.questions;
  for (const q of qs) run.responses[q.id] = { choice:q.responseKind==='explanation'?null:q.answer, evidence:q.evidence, reason:'본문의 조건을 연결해 설명했습니다.', hintLevel:1, revealed:false, submissions:[{ id:'sub-'+q.id, choice:q.responseKind==='explanation'?null:q.answer, evidence:q.evidence, reason:'본문의 조건을 연결해 설명했습니다.', hintLevel:1, choiceMatch:false, evidenceMatch:false, support:'independent' }] };
  const body = { revision:0, mutationId:'save-one', run, writing:'오늘 배운 조건과 관계를 내 말로 설명한 글입니다.' };
  const saved = await f.student(`/learning/runs/${first.id}/save`,body);
  assert.equal(saved.run.responses[qs[0].id].submissions[0].hintLevel,1);
  assert.equal(saved.run.responses[qs[0].id].submissions[0].support,'guided');
  assert.equal(saved.run.responses[qs[0].id].submissions[0].choiceMatch,qs[0].responseKind==='explanation'?null:true);
  assert.equal((await f.student(`/learning/runs/${first.id}/save`,body)).revision,1);
  await f.student(`/learning/runs/${first.id}/save`,{ ...body, mutationId:'stale' },409);
  const tampered = structuredClone(saved.run); tampered.responses[qs[0].id].submissions[0].reason='첫 답 변조';
  await f.student(`/learning/runs/${first.id}/save`,{revision:1,mutationId:'tamper',run:tampered,writing:saved.writing},409);
  const submitted = await f.student(`/learning/runs/${first.id}/submit`,{revision:1});
  assert.equal(submitted.status,'submitted'); assert.equal(submitted.report.reviewed,0);
  await f.student(`/learning/runs/${first.id}/save`,{...body,revision:2,mutationId:'late'},409);
  const reviews = Object.fromEntries(qs.map(q=>[q.id,{outcome:'success',note:'근거와 설명이 적절합니다.'}]));
  const published = await f.teacher(`/learning/runs/${first.id}/review`,{revision:2,reviews,note:'공개된 의견',publish:true});
  assert.equal((await f.parent(`/learning/runs/${first.id}`)).report.reviewed,5);
  assert.equal((await f.parent('/learning/dashboard')).runs.length,1);
  await f.teacher(`/learning/runs/${first.id}/review`,{revision:published.revision,reviews,note:'아직 공개하지 않은 수정 의견'});
  assert.equal((await f.parent(`/learning/runs/${first.id}`)).note,'공개된 의견');
  await f.teacher(`/learning/runs/${first.id}/revoke`,{});
  await f.parent(`/learning/runs/${first.id}`,undefined,404);
  assert.equal((await f.parent('/learning/dashboard')).runs.length,0);
});

test('unassigned, malformed, incomplete and unauthorized learning writes never become completed work', async t => {
  const f = await fixture(t); await approve(f); const {assignment}=await f.create();
  await f.other(`/learning/assignments/${assignment.id}/start`,{},404);
  await f.student('/learning/catalog',undefined,403);
  const r=await f.student(`/learning/assignments/${assignment.id}/start`,{});
  await f.student(`/learning/runs/${r.id}/submit`,{revision:0},400);
  const malformed=structuredClone(r.run);malformed.phase='complete';
  await f.student(`/learning/runs/${r.id}/save`,{revision:0,mutationId:'invalid',run:malformed,writing:'아직 미완료'},400);
  const q=r.lesson.questions[0];malformed.phase='questions';malformed.responses[q.id]={choice:0,evidence:['other-passage'],reason:'다른 글',hintLevel:0,revealed:false,submissions:[]};
  await f.student(`/learning/runs/${r.id}/save`,{revision:0,mutationId:'invalid-evidence',run:malformed,writing:''},400);
  await f.teacher(`/learning/runs/${r.id}/review`,{revision:0,note:'학습 중 공개',publish:true},409);
  assert.equal((await f.student(`/learning/runs/${r.id}`)).revision,0);
});

test('queued later hints do not rewrite the hint level of the first response',async t=>{
  const f=await fixture(t);await approve(f);const {assignment}=await f.create();
  const r=await f.student(`/learning/assignments/${assignment.id}/start`,{}),q=r.lesson.questions[0],run=structuredClone(r.run);
  const choice=q.responseKind==='explanation'?null:q.answer;
  run.responses[q.id]={choice,evidence:q.evidence,reason:'도움 후 고친 설명',hintLevel:3,revealed:false,submissions:[
    {id:'offline-first',choice,evidence:q.evidence,reason:'도움 전 첫 설명',hintLevel:0},
    {id:'offline-second',choice,evidence:q.evidence,reason:'도움 후 고친 설명',hintLevel:3},
  ]};
  const saved=await f.student(`/learning/runs/${r.id}/save`,{revision:0,mutationId:'queued',run,writing:'기기에서 작성한 설명'});
  assert.equal(saved.run.responses[q.id].submissions[0].hintLevel,0);
  assert.equal(saved.run.responses[q.id].submissions[1].hintLevel,3);
  assert.equal(saved.run.responses[q.id].hintLevel,3);
});


test('late work stays recoverable and teacher deadline extension restores submission eligibility', async t => {
  const f=await fixture(t);await approve(f);const {assignment}=await f.create();
  const r=await f.student(`/learning/assignments/${assignment.id}/start`,{});
  f.setTime(assignment.dueAt+1000);
  await f.student('/login',{username:'student',password});
  await f.teacher('/login',{username:'teacher',password});
  await f.student(`/learning/runs/${r.id}/submit`,{revision:0},409);
  await f.student(`/learning/assignments/${assignment.id}/extend`,{dueAt:assignment.dueAt+86400000,reason:'학생 연장 요청'},403);
  const updated=await f.teacher(`/learning/assignments/${assignment.id}/extend`,{dueAt:assignment.dueAt+86400000,reason:'추가 읽기 시간 제공'});
  assert.equal(updated.assignment.dueAt,assignment.dueAt+86400000);
  assert.equal((await f.student(`/learning/runs/${r.id}`)).id,r.id);
  await f.student(`/learning/runs/${r.id}/submit`,{revision:0},400); // eligible again, but incomplete activities still block submission
});

test('assignment, approval, learner draft and revision survive SQLite service restart', async t => {
  const {mkdtemp,rm}=await import('node:fs/promises');const {join,resolve}=await import('node:path');const {tmpdir}=await import('node:os');
  const dir=await mkdtemp(join(tmpdir(),'readx-learning-test-'));
  if (!resolve(dir).startsWith(resolve(tmpdir()))) throw Error('Unexpected temporary directory');
  let reopened;
  t.after(async()=>{ if(reopened){await new Promise(r=>reopened.server.close(r));reopened.service.close();} await rm(dir,{recursive:true,force:true});});
  const dbPath=join(dir,'learning.sqlite');const f=await fixture(t,{dbPath});await approve(f);const {assignment}=await f.create();
  const r=await f.student(`/learning/assignments/${assignment.id}/start`,{});
  await f.student(`/learning/runs/${r.id}/save`,{revision:0,mutationId:'persist',run:r.run,writing:'서버 재시작 후에도 보존할 초안'});
  await f.stop();
  const service=createExamService({privacyMode: 'synthetic',dbPath,timer:false});const server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));
  reopened={server,service};
  const origin=`http://127.0.0.1:${server.address().port}`;
  const login=await fetch(origin+'/api/exam/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:'student',password})});
  assert.equal(login.status,200);const cookie=login.headers.get('set-cookie').split(';')[0];
  const restored=await (await fetch(origin+`/api/exam/learning/runs/${r.id}`,{headers:{Cookie:cookie}})).json();
  assert.equal(restored.writing,'서버 재시작 후에도 보존할 초안');assert.equal(restored.revision,1);assert.equal(restored.assignment.id,assignment.id);
});
