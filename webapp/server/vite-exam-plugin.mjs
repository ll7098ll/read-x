import { createExamService } from './exam-service.mjs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = fileURLToPath(new URL('..', import.meta.url));
export function examApiPlugin() {
  const attach = server => {
    const service = createExamService({ dbPath: process.env.READX_EXAM_DB || resolve(root, '.exam-data', 'readx.sqlite') });
    server.middlewares.use('/api/exam', service.handler);
    server.httpServer?.once('close', () => { service.close(); });
  };
  return { name: 'readx-exam-api', configureServer: attach, configurePreviewServer: attach };
}
