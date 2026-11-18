import test from 'node:test';
import assert from 'node:assert/strict';
import { createHttpExamClient } from '../shared/http-exam-client.mjs';

test('HTTP adapter uses same-origin session and preserves server permission failures', async () => {
  const calls = [];
  const api = createHttpExamClient({ fetcher: async (url, options) => {
    calls.push({ url, ...options });
    return new Response(JSON.stringify(options.method === 'GET' ? { user: null } : { error: '교사 권한이 필요합니다.' }), { status: options.method === 'GET' ? 200 : 403 });
  } });
  assert.deepEqual(await api('/session'), { user: null });
  await assert.rejects(api('/assignments', { studentIds: ['one'] }), e => e.status === 403 && e.message === '교사 권한이 필요합니다.');
  assert.equal(calls[0].url, '/api/exam/session');
  assert.equal(calls[0].credentials, 'same-origin');
  assert.equal(calls[0].cache, 'no-store');
  assert.deepEqual(JSON.parse(calls[1].body), { studentIds: ['one'] });
});

test('network outage, timeout and non-JSON host response never become local success', async () => {
  await assert.rejects(createHttpExamClient({ fetcher: async () => { throw new TypeError('offline'); } })('/session'), e => e.status === 503);
  await assert.rejects(createHttpExamClient({ fetcher: async () => new Response('<html>static site</html>') })('/session'), e => e.status === 502);
  const api = createHttpExamClient({ timeoutMs: 10, fetcher: (_url, { signal }) => new Promise((_resolve, reject) => signal.addEventListener('abort', () => reject(new Error('aborted')))) });
  await assert.rejects(api('/session'), e => e.status === 503);
});


test('browser HTTP adapter connects teacher assignment, student submission and parent release', async t => {
  const { createServer } = await import('node:http');
  const { createExamService } = await import('./exam-service.mjs');
  const { exam } = await import('./content/g5-01.mjs');
  const service = createExamService({privacyMode: 'synthetic', dbPath: ':memory:', timer: false });
  const server = createServer(service.handler);
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  t.after(async () => { await new Promise(r => server.close(r)); service.close(); });
  const origin = `http://127.0.0.1:${server.address().port}`;
  const client = () => {
    let cookie = '';
    return createHttpExamClient({ fetcher: async (url, options) => {
      const res = await fetch(origin + url, { ...options, headers: { ...options.headers, Origin: origin, Cookie: cookie } });
      if (res.headers.get('set-cookie')) cookie = res.headers.get('set-cookie').split(';')[0];
      return res;
    } });
  };
  const teacher = client(), student = client(), parent = client(), stranger = client();
  const password = 'Http-Integration-2026';
  await teacher('/setup', { name: '실제 연결 교사', username: 'http_teacher', password });
  const enrolled = await teacher('/roster', { student: { name: '연결 학생', username: 'http_student', password }, parent: { name: '연결 보호자', username: 'http_parent', password } });
  await student('/login', { username: 'http_student', password });
  await parent('/login', { username: 'http_parent', password });
  const now = Date.now();
  const { assignment } = await teacher('/assignments', { title: 'HTTP 실제 연결', opensAt: now - 1000, closesAt: now + 3600000, studentIds: [enrolled.student.id] });
  const { attempt } = await student(`/assignments/${assignment.id}/start`, {});
  await student(`/attempts/${attempt.id}/answers`, { changes: [{ id: exam.passages[0].questions[0].id, choice: exam.passages[0].questions[0].answer, seq: 1 }] });
  await student(`/attempts/${attempt.id}/submit`, {});
  assert.equal((await student(`/attempts/${attempt.id}`)).report, null);
  await assert.rejects(parent(`/attempts/${attempt.id}`), e => e.status === 404);
  await assert.rejects(stranger('/dashboard'), e => e.status === 401);
  await teacher(`/assignments/${assignment.id}/release`, {});
  assert.equal((await student(`/attempts/${attempt.id}`)).report.percent, 4.2);
  await teacher(`/attempts/${attempt.id}/review`, { note: '첫 문항의 근거를 정확히 확인했습니다.', publish: true });
  const result = await parent(`/attempts/${attempt.id}`);
  assert.equal(result.report.correct, 1);
  assert.equal(result.attempt.note, '첫 문항의 근거를 정확히 확인했습니다.');
  await teacher(`/attempts/${attempt.id}/review`, { note: '내부 수정 의견', revoke: true });
  await assert.rejects(parent(`/attempts/${attempt.id}`), e => e.status === 404);
  await student('/logout', {});
  await assert.rejects(student('/dashboard'), e => e.status === 401);
});
