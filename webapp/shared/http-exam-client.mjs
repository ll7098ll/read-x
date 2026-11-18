// No local grading or fallback: a successful response means the server accepted it.
export function createHttpExamClient({ fetcher = (...args) => fetch(...args), timeoutMs = 15000 } = {}) {
  return async (path, body) => {
    if (!/^\/[a-z0-9/:_-]+$/i.test(path)) throw new Error('요청 경로를 확인해 주세요.');
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetcher(`/api/exam${path}`, {
        method: body === undefined ? 'GET' : 'POST', credentials: 'same-origin', cache: 'no-store',
        signal: controller.signal,
        ...(body === undefined ? {} : { headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) }),
      });
      let data;
      try { data = await response.json(); }
      catch { throw Object.assign(new Error('서버 응답을 확인하지 못했습니다. 연결 상태를 확인한 뒤 다시 시도해 주세요.'), { status: response.ok ? 502 : response.status }); }
      if (!response.ok) throw Object.assign(new Error(data.error || '요청을 처리하지 못했습니다.'), { status: response.status, code: data.code });
      return data;
    } catch (error) {
      if (error.status) throw error;
      throw Object.assign(new Error('서버에 연결하지 못했습니다. 답안 저장은 확인되지 않았습니다. 연결 후 다시 시도해 주세요.'), { status: 503 });
    } finally { clearTimeout(timer); }
  };
}
