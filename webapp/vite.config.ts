import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { viteSingleFile } from 'vite-plugin-singlefile';
import { examApiPlugin } from './server/vite-exam-plugin.mjs';

export default defineConfig(({ mode }) => {
  const demo = loadEnv(mode, process.cwd(), "VITE_").VITE_EXAM_MODE === "demo";
  return {
  plugins: [react(), ...(demo ? [] : [examApiPlugin()]), {
    name: 'private-exam-content-boundary',
    generateBundle(_options, bundle) {
      if (demo) return;
      for (const output of Object.values(bundle)) {
        if (output.type !== 'chunk') continue;
        for (const id of Object.keys(output.modules)) {
          if (/shared[\\/](g5-01|exam-engine|local-exam-client)\.mjs$/.test(id))
            this.error('운영 번들에 비공개 시험 자료가 포함되었습니다: ' + id);
        }
      }
    },
  }, viteSingleFile()],
  base: './',
  server: {
    fs: { deny: ['.env', '.env.*', '*.{crt,pem}', '**/.git/**', '**/server/**', '**/.exam-data/**'] },
  },
  build: {
    outDir: 'dist',
    emptyOutDir: true,
  },
  };
});
