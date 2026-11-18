import { createExamEngine, newState } from './exam-engine.mjs';

export const DEMO_STORAGE_KEY = 'readx:exam-demo:v1';

// The static Site and local preview share this browser-local adapter.
// Account API credentials and server records are never read here.
export function createLocalExamClient({ storage, now = Date.now, uuid = () => crypto.randomUUID(),
  token = () => Array.from(crypto.getRandomValues(new Uint8Array(32)), b => b.toString(16).padStart(2, '0')).join(''),
  lock = async action => action() }) {
  const engine = createExamEngine({ demo: true, randomUUID: uuid, randomBytes: () => ({ toString: token }), hash: value => value });
  return (path, body, role = 'student') => lock(() => {
    let saved;
    try {
      const raw = storage.getItem(DEMO_STORAGE_KEY);
      saved = raw ? JSON.parse(raw) : { version: 1, state: newState(), cookie: '' };
      if (saved.version !== 1 || !Array.isArray(saved.state?.users) || !Array.isArray(saved.state?.attempts) || !saved.state.sessions) throw new Error();
    } catch { throw new Error('이 브라우저의 체험 기록을 읽지 못했습니다. 저장 공간 사용 설정을 확인해 주세요.'); }
    const at = now();
    engine.expire(saved.state, at);
    const req = { url: '/api/exam-demo/session', method: 'GET', headers: { cookie: saved.cookie, 'x-readx-demo-role': role }, socket: {} };
    const res = { setHeader(name, value) { if (name === 'Set-Cookie') { saved.cookie = value.split(';')[0]; req.headers.cookie = saved.cookie; } } };
    engine.route(saved.state, req, res, {}, at);
    req.url = `/api/exam-demo${path}`; req.method = body === undefined ? 'GET' : 'POST';
    const result = engine.route(saved.state, req, res, body || {}, at);
    try { storage.setItem(DEMO_STORAGE_KEY, JSON.stringify(saved)); }
    catch { throw new Error('브라우저 저장 공간에 기록하지 못했습니다. 답안은 저장되지 않았으니 저장 공간을 확인한 뒤 다시 시도해 주세요.'); }
    return structuredClone(result);
  });
}
