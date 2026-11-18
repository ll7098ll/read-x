import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=fileURLToPath(new URL('../dist/',import.meta.url));let count=0;
async function inspect(dir){for(const entry of await readdir(dir,{withFileTypes:true})){const path=join(dir,entry.name);if(entry.isDirectory()){await inspect(path);continue;}if(!/\.(html|css)$/.test(entry.name))continue;const text=await readFile(path,'utf8');count++;
  if(/<(?:link|script|img|iframe|source)\b[^>]*(?:href|src)\s*=\s*["'](?:https?:)?\/\//i.test(text)||/@import\s+(?:url\(\s*)?["']?(?:https?:)?\/\//i.test(text))throw Error('외부 자동 로딩 리소스를 검토하고 로컬 자산으로 전환해 주세요: '+entry.name);
}}
await inspect(root);console.log(`Built HTML/CSS automatic external-resource check: ${count} files passed.`);
