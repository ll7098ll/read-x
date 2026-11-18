import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { mkdtemp, rm } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { createExamService, scoreAttempt } from './exam-service.mjs';
import { exam, allItems, publicForm, transfers, validateContent } from './content/g5-01.mjs';

const password = 'Integration-Test-2026';
async function fixture(t, options = {}) {
  let time = Date.UTC(2026, 9, 24, 1);
  const service = createExamService({privacyMode: 'synthetic', dbPath: ':memory:', now: () => time, timer: false, ...options });
  const server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  t.after(async () => { await new Promise(r => server.close(r)); service.close(); });
  const origin = `http://127.0.0.1:${server.address().port}`;
  const client = () => {
    let cookie = '';
    return async (path, body, expected = 200, extra = {}) => {
      const response = await fetch(`${origin}/api/exam${path}`, { method: body === undefined ? 'GET' : 'POST', headers: { 'Content-Type': 'application/json', Cookie: cookie, Origin: origin, ...extra }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });
      if (response.headers.get('set-cookie')) cookie = response.headers.get('set-cookie').split(';')[0];
      const result = await response.json();
      assert.equal(response.status, expected, `${path}: ${JSON.stringify(result)}`); return result;
    };
  };
  const teacher = client(); await teacher('/setup', { name: '검증 교사', username: 'teacher', password, className: '초5 검증반' });
  const one = await teacher('/roster', { student: { name: '학생 하나', username: 'student1', password }, parent: { name: '보호자 하나', username: 'parent1', password } });
  const two = await teacher('/roster', { student: { name: '학생 둘', username: 'student2', password }, parent: { name: '보호자 둘', username: 'parent2', password } });
  const student1 = client(), student2 = client(), parent1 = client(), parent2 = client();
  await student1('/login', { username: 'student1', password }); await student2('/login', { username: 'student2', password });
  await parent1('/login', { username: 'parent1', password }); await parent2('/login', { username: 'parent2', password });
  const assigned = await teacher('/assignments', { title: '초5 통합 검증', opensAt: time - 60000, closesAt: time + 3600000, studentIds: [one.student.id, two.student.id] });
  return { teacher, student1, student2, parent1, parent2, client, one, two, assignment: assigned.assignment, setTime: value => { time = value; }, now: () => time };
}

test('content has 24 original items, 12/8/4 coverage, valid evidence and complete option rationales', () => {
  validateContent();
  assert.deepEqual(exam.passages.map(p => p.questions.length), [4, 4, 4, 4, 4, 4]);
  const items = allItems();
  assert.deepEqual(['독서', '문학', '언어·매체'].map(d => items.filter(q => q.domain === d).length), [12, 8, 4]);
  assert.deepEqual(items.map(q => q.answer), [2, 1, 3, 4, 0, 2, 3, 1, 0, 4, 2, 1, 3, 0, 2, 4, 1, 3, 2, 0, 4, 1, 3, 0]);
  for (const p of exam.passages) assert.ok(p.paragraphs.reduce((n, p) => n + p.text.length, 0) > 110);
  assert.equal(transfers.length, 6);
  const serialized = JSON.stringify(publicForm());
  for (const name of ['"answer":', '"reasons":', '"evidence":', '"explanation":']) assert.ok(!serialized.includes(name), name);
  const result = scoreAttempt({ answers: { 'g5-01-q1': 2 }, startedAt: 0, submittedAt: 1000 }, exam);
  assert.equal(result.percent, 4.2); assert.equal(result.unanswered, 23); assert.equal(result.wrong, 0);
});

test('teacher assignment → two students → item statistics → parent release → remediation', async t => {
  const f = await fixture(t);
  const a1 = (await f.student1(`/assignments/${f.assignment.id}/start`, {})).attempt;
  const a2 = (await f.student2(`/assignments/${f.assignment.id}/start`, {})).attempt;
  assert.equal((await f.student1(`/assignments/${f.assignment.id}/start`, {})).attempt.id, a1.id, 'start is idempotent');
  const before = await f.student1(`/attempts/${a1.id}`);
  assert.equal(before.report, null); assert.ok(!JSON.stringify(before.form).includes('"answer":'));
  await f.student1('/form', undefined, 403);
  await f.student1(`/attempts/${a2.id}`, undefined, 404);
  await f.parent1(`/attempts/${a1.id}`, undefined, 404);
  await f.teacher(`/assignments/${f.assignment.id}/release`, {}, 409);
  await f.student1(`/attempts/${a1.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 0, seq: 1 }] });
  const changed = await f.student1(`/attempts/${a1.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 2, seq: 2 }] });
  assert.equal(changed.answers['g5-01-q1'], 2);
  const stale = await f.student1(`/attempts/${a1.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 0, seq: 1 }] });
  assert.equal(stale.answers['g5-01-q1'], 2, 'stale write cannot overwrite');
  await f.student1(`/attempts/${a1.id}/answers`, { changes: allItems().slice(1).map(q => ({ id: q.id, choice: q.number === 3 ? 0 : q.answer, seq: 1 })), flags: ['g5-01-q3'] });
  await f.student2(`/attempts/${a2.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 1, seq: 1 }] });
  await f.student1(`/attempts/${a1.id}/submit`, {}); await f.student1(`/attempts/${a1.id}/submit`, {});
  await f.student2(`/attempts/${a2.id}/submit`, {});
  await f.student1(`/attempts/${a1.id}/answers`, { changes: [] }, 409);
  assert.equal((await f.student1(`/attempts/${a1.id}`)).report, null, 'submitted result still private');
  const stats = await f.teacher(`/assignments/${f.assignment.id}/statistics`);
  assert.equal(stats.count, 2); assert.equal(stats.rows[0].correct, 1);
  assert.equal(stats.rows[2].unanswered.length, 1);
  assert.equal(stats.rows[2].choices.reduce((n, c) => n + c.count, 0) + stats.rows[2].unanswered.length, 2);
  await f.teacher(`/assignments/${f.assignment.id}/release`, {});
  const studentReport = await f.student1(`/attempts/${a1.id}`);
  assert.equal(studentReport.report.correct, 23); assert.equal(studentReport.report.percent, 95.8);
  assert.equal((await f.student2(`/attempts/${a2.id}`)).report.percent, 0);
  await f.teacher(`/attempts/${a1.id}/review`, { note: '3번의 상태 확인 순서를 다시 살펴봅시다.', publish: true });
  const parentReport = await f.parent1(`/attempts/${a1.id}`);
  assert.deepEqual(parentReport.report, studentReport.report);
  await f.parent2(`/attempts/${a1.id}`, undefined, 404);
  assert.deepEqual((await f.parent1('/dashboard')).assignments[0].studentIds, [f.one.student.id]);
  await f.teacher(`/attempts/${a1.id}/review`, { note: '아직 공개하지 않은 의견' });
  assert.equal((await f.parent1(`/attempts/${a1.id}`)).attempt.note, '3번의 상태 확인 순서를 다시 살펴봅시다.');
  const fu = (await f.teacher(`/attempts/${a1.id}/followups`, { questionId: 'g5-01-q3' })).followup;
  assert.equal((await f.student1(`/attempts/${a1.id}`)).followups[0].transfer, undefined);
  await f.student2(`/followups/${fu.id}/review`, { reflection: '다른 학생' }, 404);
  await f.student1(`/followups/${fu.id}/complete`, { choice: 0, evidence: '근거' }, 409);
  await f.student1(`/followups/${fu.id}/review`, { reflection: '예약보다 책 상태를 먼저 확인해야 한다.' });
  await f.student1(`/followups/${fu.id}/complete`, { choice: 0, evidence: '바람이 빠진 공은 먼저 점검함에 넣는다.' });
  const finished = await f.parent1(`/attempts/${a1.id}`);
  assert.equal(finished.followups[0].result.correct, true); assert.equal(finished.followups[0].fresh, true);
  assert.equal(finished.report.percent, 95.8, 'followup never changes exam score');
  await f.student1(`/followups/${fu.id}/feedback`, { outcome: 'supported', comment: '학생의 자기 승인' }, 403);
  await f.teacher(`/followups/${fu.id}/feedback`, { outcome: 'supported', comment: '우선 적용할 조건을 본문에서 정확히 찾았습니다.' });
  assert.equal((await f.parent1(`/attempts/${a1.id}`)).followups[0].teacherReview.outcome, 'supported');
  assert.equal((await f.student1(`/attempts/${a1.id}`)).followups[0].teacherReview.teacherName, '검증 교사');
  const repeated = (await f.teacher(`/attempts/${a1.id}/followups`, { questionId: 'g5-01-q4' })).followup;
  await f.student1(`/followups/${repeated.id}/review`, { reflection: '같은 글로 추가 연습한다.' });
  assert.equal((await f.student1(`/attempts/${a1.id}`)).followups[1].fresh, false);
  await f.teacher(`/attempts/${a1.id}/review`, { note: '공개 회수', revoke: true });
  await f.parent1(`/attempts/${a1.id}`, undefined, 404);
});

test('server deadline, login revocation, invalid writes, origin and permission boundaries', async t => {
  const f = await fixture(t);
  const a = (await f.student1(`/assignments/${f.assignment.id}/start`, {})).attempt;
  await f.student1(`/attempts/${a.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 5, seq: 1 }] }, 400);
  await f.student1(`/attempts/${a.id}/answers`, { changes: [{ id: 'unknown', choice: 0, seq: 1 }] }, 400);
  await f.student1('/assignments', {}, 403);
  await f.teacher('/roster', { student: { name: '유령', username: 'student3', password }, parent: { name: '중복', username: 'parent1', password } }, 409);
  assert.ok(!(await f.teacher('/dashboard')).users.some(u => u.username === 'student3'), 'failed parent creation rolls back pupil');
  await f.teacher('/assignments', {}, 403, { Origin: 'https://untrusted.example' });
  const other = f.client(); await other('/login', { username: 'student1', password });
  await f.student1('/dashboard', undefined, 401);
  await other(`/attempts/${a.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 2, seq: 1 }] });
  f.setTime(a.deadlineAt);
  await other(`/attempts/${a.id}/answers`, { changes: [{ id: 'g5-01-q2', choice: 1, seq: 1 }] }, 409);
  const expired = await other(`/attempts/${a.id}`);
  assert.equal(expired.attempt.status, 'auto_submitted'); assert.equal(expired.attempt.submittedAt, a.deadlineAt);
  assert.equal(expired.attempt.answered, 1);
  assert.equal((await f.teacher(`/attempts/${a.id}`)).report.percent, 4.2);
  const anonymous = f.client(); await anonymous('/dashboard', undefined, 401); await anonymous('/setup', {}, 409);
});

test('SQLite keeps account and submitted answers across server restart', async t => {
  const directory = await mkdtemp(join(tmpdir(), 'readx-exam-test-'));
  const dbPath = join(directory, 'test.sqlite');
  let service = createExamService({privacyMode: 'synthetic', dbPath, timer: false });
  let server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  let origin = `http://127.0.0.1:${server.address().port}`;
  let cookie = '';
  const request = async (path, body) => {
    const response = await fetch(`${origin}/api/exam${path}`, { method: body === undefined ? 'GET' : 'POST', headers: { 'Content-Type': 'application/json', Cookie: cookie }, ...(body === undefined ? {} : { body: JSON.stringify(body) }) });
    if (response.headers.get('set-cookie')) cookie = response.headers.get('set-cookie').split(';')[0];
    const data = await response.json(); assert.equal(response.status, 200, JSON.stringify(data)); return data;
  };
  await request('/setup', { name: '재시작 교사', username: 'persistent', password });
  const { student } = await request('/roster', { student: { name: '보존 학생', username: 'saved_student', password } });
  const { assignment } = await request('/assignments', { studentIds: [student.id], opensAt: Date.now() - 1000, closesAt: Date.now() + 3600000 });
  await request('/login', { username: 'saved_student', password });
  const { attempt } = await request(`/assignments/${assignment.id}/start`, {});
  await request(`/attempts/${attempt.id}/answers`, { changes: [{ id: 'g5-01-q1', choice: 2, seq: 1 }], flags: ['g5-01-q2'] });
  await request(`/attempts/${attempt.id}/submit`, {});
  await new Promise(r => server.close(r)); service.close();
  service = createExamService({privacyMode: 'synthetic', dbPath, timer: false }); server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r)); origin = `http://127.0.0.1:${server.address().port}`;
  t.after(async () => { await new Promise(r => server.close(r)); service.close(); await rm(directory, { recursive: true, force: true }); });
  assert.equal((await request('/login', { username: 'persistent', password })).user.name, '재시작 교사');
  const restored = await request(`/attempts/${attempt.id}`);
  assert.equal(restored.attempt.status, 'submitted'); assert.equal(restored.report.correct, 1);
  assert.equal(restored.report.rows[0].choice, 2); assert.equal(restored.report.unanswered, 23);
  await request('/login', { username: 'saved_student', password });
  const pupilRecord = await request(`/attempts/${attempt.id}`);
  assert.equal(pupilRecord.attempt.answers['g5-01-q1'], 2); assert.deepEqual(pupilRecord.attempt.flags, ['g5-01-q2']);
});


test('malformed HTTP requests return useful errors and preserve the working session', async t => {
  const service = createExamService({privacyMode: 'synthetic', dbPath: ':memory:', timer: false });
  const server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  t.after(async () => { await new Promise(r => server.close(r)); service.close(); });
  const origin = `http://127.0.0.1:${server.address().port}`;
  for (const [body, type, source, expected] of [
    ['{}', 'application/json', 'null', 403],
    ['{}', 'application/json', 'https://another.example', 403],
    ['{}', 'text/plain', origin, 415],
    ['{', 'application/json', origin, 400],
    ['[]', 'application/json', origin, 400],
    ['null', 'application/json', origin, 400],
    ['x'.repeat(65537), 'application/json', origin, 413],
  ]) {
    const r = await fetch(`${origin}/api/exam/setup`, { method: 'POST', headers: { 'Content-Type': type, Origin: source }, body });
    assert.equal(r.status, expected); assert.ok((await r.json()).error);
  }
  const session = await fetch(`${origin}/api/exam/session`);
  assert.equal((await session.json()).setupRequired, true);
});
