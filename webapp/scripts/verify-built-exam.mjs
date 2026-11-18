import { readFile } from 'node:fs/promises';
import { exam, transfers } from '../server/content/g5-01.mjs';
import {courseNotes} from '../server/assessment-review-notes.mjs';
import {diagnosticNotes,explanationSamples} from '../server/diagnostic-review-notes.mjs';
const html = await readFile(new URL('../dist/index.html', import.meta.url), 'utf8');
if (process.env.VITE_EXAM_MODE === 'demo') {
  console.log('Explicit demo build: private-content boundary applies to production only.');
} else {
  const strings=value=>typeof value==='string'?[value]:Object.values(value).flatMap(strings);
  const privateTexts = [...exam.passages.flatMap(p => p.questions.flatMap(q => q.reasons)), ...transfers.map(t => t.explanation),...strings(courseNotes),...strings(diagnosticNotes),...strings(explanationSamples)];
  for (const text of privateTexts) {
    if (text && (html.includes(text) || html.includes(JSON.stringify(text).slice(1, -1)))) throw new Error('운영 산출물에 비공개 해설이 포함되어 있습니다.');
  }
  for (const marker of ['readx:exam-demo:v1', 'readx_exam_demo=', 'assessment-editorial-2026-11-17-v1']) {
    if (html.includes(marker)) throw new Error('운영 산출물에 체험 엔진이 포함되어 있습니다.');
  }
  console.log('Production exam bundle: private explanations and demo engine absent.');
}
