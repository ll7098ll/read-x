import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createExamService } from './exam-service.mjs';

const root = fileURLToPath(new URL('..', import.meta.url));
const dist = resolve(root, 'dist');
try { await stat(resolve(dist, 'index.html')); } catch { console.error('먼저 npm run build를 실행해 주세요.'); process.exit(1); }
const service = createExamService({ dbPath: process.env.READX_EXAM_DB || resolve(root, '.exam-data', 'readx.sqlite') });
const server = createServer(async (req, res) => {
  const path = new URL(req.url, 'http://localhost').pathname;
  if (path.startsWith('/api/exam/')) return service.handler(req, res);
  if (!['GET', 'HEAD'].includes(req.method)) { res.writeHead(405); res.end(); return; }
  try {
    const file = resolve(dist, '.' + decodeURIComponent(path === '/' ? '/index.html' : path));
    if (!file.startsWith(dist + sep)) { res.writeHead(403); res.end(); return; }
    const data = await readFile(file);
    const type = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.woff2': 'font/woff2' }[extname(file)] || 'application/octet-stream';
    res.writeHead(200, { 'Content-Type': type, 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-cache' }); res.end(req.method === 'HEAD' ? undefined : data);
  } catch { res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' }); res.end('파일을 찾을 수 없습니다.'); }
});
const port = Number(process.env.READX_EXAM_PORT || 5186), host = process.env.READX_EXAM_HOST || '127.0.0.1';
server.listen(port, host, () => console.log(`ReadX 모의고사: http://${host}:${port}/#/exams`));
server.on('error', error => { console.error(error.message); service.close(); process.exitCode = 1; });
for (const signal of ['SIGINT', 'SIGTERM']) process.once(signal, () => { server.close(() => { service.close(); process.exit(0); }); });
