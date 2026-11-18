import { build } from 'esbuild';
import { mkdtemp, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const dir = await mkdtemp(path.join(tmpdir(), 'readxray-tests-'));
try {
  const result = await build({ entryPoints: [path.join(root, 'tests/stabilization.test.tsx')], bundle: true,
    loader: { '.css': 'empty' }, platform: 'node', format: 'cjs', write: false, logLevel: 'silent', define: { 'import.meta.env': '{}' },
    banner: { js: `const testStorage = new Map(); Object.defineProperty(globalThis, 'localStorage', { configurable: true, value: { getItem: k => testStorage.get(k) ?? null, setItem: (k,v) => testStorage.set(k,v), removeItem: k => testStorage.delete(k) } }); globalThis.window = { localStorage: globalThis.localStorage };` } });
  const target = path.join(dir, 'tests.cjs');
  await writeFile(target, result.outputFiles[0].contents);
  const run = spawnSync(process.execPath, ['--test', target], { stdio: 'inherit', cwd: root });
  process.exitCode = run.status ?? 1;
} finally {
  // Only the exact directory created by mkdtemp above, never a computed project path.
  await rm(dir, { recursive: true, force: true });
}
