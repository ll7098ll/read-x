import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';
import {placementForm,placementFormAtVersion,publicForm} from '../server/placement-content.mjs';
import {courseBundle,courseOrder,courseNames} from '../server/course-content.mjs';
import {matchesAssessmentEvidence,editorialReviewVersion} from '../server/assessment-review.mjs';
const root=fileURLToPath(new URL('../..',import.meta.url)),out=resolve(root,'output','assessment-review-2026-11-17');
mkdirSync(out,{recursive:true});
const lessons=JSON.parse(readFileSync(new URL('../src/data/corpusLessons.generated.json',import.meta.url)));
const ledger=[],forms=[],issues=[];
const diff=(q,old,paragraphs,previous)=>({
 contentChanged:JSON.stringify([q.prompt,paragraphs,[...q.options].sort(),q.options[q.answer]])!==JSON.stringify([old.prompt,previous,[...old.options].sort(),old.options[old.answer]]),
 evidenceChanged:JSON.stringify(q.evidence)!==JSON.stringify(old.evidence),
 orderChanged:!q.options.every((o,i)=>o===old.options[i])
});
function verify(row){
 const q=row.question;
 assert.equal(q.editorialReview.version,editorialReviewVersion,row.key);
 assert.ok(q.explanation.length>=12,row.key);assert.ok(q.sampleResponse.length>=6,row.key);assert.ok(q.scoringGuide.full,row.key);
 assert.ok(q.evidence.length&&q.evidence.every(i=>row.paragraphs[i]),row.key);
 assert.ok(q.evidenceQuotes.every(e=>e.text===row.paragraphs[e.paragraph]),row.key);
 if(q.options.length){assert.equal(new Set(q.options).size,q.options.length,row.key);assert.ok(q.options[q.answer],row.key);assert.equal(q.optionReasons.length,q.options.length,row.key);assert.ok(q.optionReasons.every(Boolean),row.key);}
 if(row.kind==='check'){assert.ok(matchesAssessmentEvidence(q,q.evidence),row.key);assert.equal(matchesAssessmentEvidence(q,[99]),false,row.key);}
 ledger.push(row);
}
for(let grade=1;grade<=6;grade++){
 const known=new Set();
 for(const branch of [null,'support','extend']){
  const form=placementForm(grade,branch),old=placementFormAtVersion(grade,branch,'g16-placement-2');
  forms.push(form);
  for(const pub of publicForm(form).questions)for(const k of ['answer','evidence','explanation','optionReasons','sampleResponse','scoringGuide','editorialReview'])assert.equal(k in pub,false,`${grade}/${k}`);
  const mc=form.questions.filter(q=>q.options.length),counts=Array.from({length:mc[0].options.length},(_,i)=>mc.filter(q=>q.answer===i).length);
  assert.ok(Math.max(...counts)-Math.min(...counts)<=1,`정답 위치 편향: ${grade}/${branch}`);
  for(const q of form.questions){
   const phase=q.options.length?(form.passages.slice(0,grade<=2?2:3).some(p=>p.id===q.passageId)?'common':branch):branch;
   const key=`diagnostic:g${grade}:${phase}:${q.id}`;if(known.has(key))continue;known.add(key);
   const p=form.passages.find(p=>p.id===q.passageId),prior=old.questions.find(x=>x.id===q.id),op=old.passages.find(x=>x.id===q.passageId);
   verify({key,kind:'diagnostic',grade,branch:phase,skill:q.skill,title:p.title,paragraphs:p.paragraphs,question:q,changes:diff(q,prior,p.paragraphs,op.paragraphs)});
  }
 }
 for(const course of courseOrder){
  const current=courseBundle(grade,course,lessons),old=courseBundle(grade,course,lessons,{reviewed:false});
  current.checks.forEach((q,i)=>verify({key:`check:g${grade}:${course}:${i}`,kind:'check',grade,skill:course,title:q.title,paragraphs:q.paragraphs,question:q,changes:diff(q,old.checks[i],q.paragraphs,old.checks[i].paragraphs)}));
 }
}
assert.equal(ledger.filter(r=>r.kind==='diagnostic').length,172);assert.equal(ledger.filter(r=>r.kind==='check').length,288);assert.equal(ledger.length,460);
const byGrade=Array.from({length:6},(_,i)=>{const rows=ledger.filter(r=>r.grade===i+1);return {grade:i+1,items:rows.length,diagnostic:rows.filter(r=>r.kind==='diagnostic').length,checks:48,difficulty:Object.fromEntries(['입문','기본','도전'].map(b=>[b,rows.filter(r=>r.question.difficulty.band===b).length])),longestPassageChars:Math.max(...rows.map(r=>r.question.difficulty.chars))};});
const summary={reviewVersion:editorialReviewVersion,method:'AI 문항별 편집 검토·본문 대조 + 자동 무결성 검사',humanTeacherApproval:false,empiricalDifficultyCalibrated:false,reviewed:ledger.length,diagnostic:172,checks:288,
 contentRevised:ledger.filter(r=>r.changes.contentChanged).length,evidenceRevised:ledger.filter(r=>r.changes.evidenceChanged).length,positionRebalanced:ledger.filter(r=>r.kind==='diagnostic'&&r.changes.orderChanged).length,
 explanationsAdded:460,byGrade,openIssues:issues,passed:true};
writeFileSync(resolve(out,'review-summary.json'),JSON.stringify(summary,null,2));
writeFileSync(resolve(out,'item-ledger.json'),JSON.stringify(ledger,null,2));
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const css='body{font-family:Arial,"Malgun Gothic",sans-serif;color:#18362b;max-width:1100px;margin:30px auto;padding:0 20px;line-height:1.8;overflow-wrap:anywhere}header,article{padding:22px;border:1px solid #d5ddd6;border-radius:14px;margin:18px 0}article p{white-space:pre-line}blockquote{background:#f2f6ee;padding:12px;margin:12px 0}small{color:#53665c}.toolbar{position:sticky;top:0;background:white;padding:14px;display:flex;gap:10px;flex-wrap:wrap}input,select,button{font:inherit;padding:8px;max-width:100%}li{margin:8px 0}.key{color:#17653b;font-weight:bold}.hidden{display:none}@media print{.toolbar,.no-print{display:none}article{break-inside:avoid;border-radius:0}body{max-width:none;margin:0}}';
const itemHTML=r=>{const q=r.question;return `<article data-grade="${r.grade}" data-kind="${r.kind}" data-skill="${r.skill}" data-band="${q.difficulty.band}"><small>${esc(r.key)} · 초${r.grade} · ${esc(courseNames[r.skill]||r.skill)} · 편집 ${q.difficulty.band}</small><h2>${esc(r.title)}</h2>${r.paragraphs.map((p,i)=>`<p><b>${i+1}문단.</b> ${esc(p)}</p>`).join('')}<h3>${esc(q.prompt)}</h3>${q.options.length?`<ol>${q.options.map((o,i)=>`<li class="${i===q.answer?'key':''}">${esc(o)}${i===q.answer?' ✓':''}<br><small>${esc(q.optionReasons[i])}</small></li>`).join('')}</ol>`:''}<h3>정답·설명</h3><p>${esc(q.explanation)}</p><h3>본문 근거</h3>${q.evidenceQuotes.map(e=>`<blockquote>${e.paragraph+1}문단: ${esc(e.text)}</blockquote>`).join('')}<p>학생 표현 예: ${esc(q.sampleResponse)}</p><p>${esc(q.scoringGuide.full)} ${esc(q.scoringGuide.partial)}</p><p>${esc(q.scoringGuide.doNotRequire)}</p><p>${esc(q.scoringGuide.evidencePolicy)}</p><p>난도 검토: ${esc(q.difficulty.process)} · ${q.difficulty.chars}자 · ${q.difficulty.paragraphs}문단. ${esc(q.difficulty.cautions.join(' / '))}</p>${q.corrections?.length?`<p>수정: ${esc(q.corrections.join(' / '))}</p>`:''}</article>`;};
const html=`<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>초1~6 평가 자료 교사용 전수 검수본</title><style>${css}</style><body><header><h1>초1~6 평가 자료 · 교사용 검수본</h1><p>진단 172과제 + 성취 확인 288과제 = 460과제. 공통 진단은 중복 집계하지 않았으며 서술 과제는 분기별로 구분했습니다.</p><p>AI 편집 검토와 자동 검증 결과입니다. 편집 난도는 실제 학생 난도·전국 규준이 아닙니다. 교사가 학급과 학생의 읽기·어휘 부담을 확인해 사용합니다.</p><p>이 파일에는 정답이 있습니다. 학생에게는 별도 진단 활동지를 사용하세요. 종이 응답은 앱의 성취·노출 이력에 자동 반영되지 않습니다.</p><p>내용 수정 ${summary.contentRevised}과제 · 근거 기준 수정 ${summary.evidenceRevised}과제 · 모든 과제에 해설·표현 예·채점 안내를 보완했습니다.</p></header><div class="toolbar"><label>학년 <select id="grade"><option value="">전체</option>${[1,2,3,4,5,6].map(g=>`<option>${g}</option>`).join('')}</select></label><label>용도 <select id="kind"><option value="">전체</option><option value="diagnostic">진단</option><option value="check">성취 확인</option></select></label><label>목표 <select id="skill"><option value="">전체</option>${courseOrder.map(c=>`<option value="${c}">${courseNames[c]}</option>`).join('')}</select></label><label>찾기 <input id="search" placeholder="문항·주제·근거 검색"></label><button onclick="window.print()">선택한 검수본 인쇄</button><span id="count"></span></div><main>${ledger.map(itemHTML).join('')}</main><script>const articles=[...document.querySelectorAll('article')];function filter(){let count=0;for(const a of articles){const match=['grade','kind','skill'].every(k=>!document.getElementById(k).value||a.dataset[k]===document.getElementById(k).value)&&a.textContent.includes(document.getElementById('search').value);a.classList.toggle('hidden',!match);if(match)count++}document.getElementById('count').textContent=count+'과제'}for(const e of document.querySelectorAll('select,input'))e.addEventListener('input',filter);filter()</script></body></html>`;
writeFileSync(resolve(out,'teacher-review.html'),html);
for(const form of forms.filter(f=>f.branch)){
 const commonCount=form.grade<=2?6:12;
 const phases=[['1. 공통 진단',form.questions.slice(0,commonCount)],['2. 추가 진단',form.questions.slice(commonCount).filter(q=>q.options.length)],['3. 내 말로 설명하기',form.questions.filter(q=>!q.options.length)]];
 const sections=phases.map(([label,questions])=>`<h2>${label}</h2>${form.passages.filter(p=>questions.some(q=>q.passageId===p.id)).map(p=>`<article><h2>${esc(p.title)}</h2>${p.paragraphs.map((text,i)=>`<p>${i+1}. ${esc(text)}</p>`).join('')}${questions.filter(q=>q.passageId===p.id).map(q=>`<h3>${esc(q.prompt)}</h3>${q.options.length?`<ol>${q.options.map(o=>`<li>□ ${esc(o)}</li>`).join('')}</ol>`:'<p>내 설명: __________________________________________________</p><p>근거 문단: ________________________________________________</p>'}`).join('')}</article>`).join('')}`).join('');
 const student=`<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>초${form.grade} ${form.branch==='support'?'지원형':'확장형'} 진단 활동지</title><style>${css}textarea{width:100%;min-height:70px}@media print{article{break-before:page}h3{break-after:avoid}}</style><body><header><h1>초${form.grade} 읽기 시작 진단</h1><p>교사 배정용 ${form.branch==='support'?'지원형':'확장형'} 활동지 · ${form.version}</p><p>이름 __________ 날짜 __________</p><p>앞의 공통 문제를 먼저 풀고 쉬었다가 이어 풀어도 됩니다. ${form.grade<=2?'설명은 짧은 말이나 낱말로 써도 됩니다. 말로 설명했다면 선생님이 실제 말을 적습니다.':''}</p></header>${sections}<p>종이 활동지는 수업용입니다. 앱의 정식 응시 결과·배치에 자동 합산하지 않습니다.</p></body></html>`;
 writeFileSync(resolve(out,`student-diagnostic-g${form.grade}-${form.branch}.html`),student);
}

for(let grade=1;grade<=6;grade++)for(const course of courseOrder){
 const rows=ledger.filter(r=>r.kind==='check'&&r.grade===grade&&r.skill===course);
 const student=`<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>초${grade} ${esc(courseNames[course])} 확인 활동지</title><style>${css}@media print{article{break-before:page}}</style><body><header><h1>초${grade} · ${esc(courseNames[course])}</h1><p>교사가 배정한 확인 활동만 풀어요. 이름 __________ 날짜 __________</p><p>1~5번은 독립 확인, 6번은 새 상황 적용, 7번은 유지 확인, 8번은 교사가 배정하는 대체 확인입니다. 한꺼번에 모두 배부하지 않습니다.</p><p>처음 보는 글에서 힌트 없이 읽고 설명해요. ${grade<=2?'짧은 말이나 낱말로 설명해도 됩니다. 말로 설명하면 선생님이 그대로 적어요.':''}</p></header>${rows.map((r,i)=>`<article><small>확인 ${i+1} · ${esc(r.question.id)}</small><h2>${esc(r.title)}</h2>${r.paragraphs.map((text,j)=>`<p>${j+1}. ${esc(text)}</p>`).join('')}<h3>${esc(r.question.prompt)}</h3><ol>${r.question.options.map(o=>`<li>□ ${esc(o)}</li>`).join('')}</ol><p>근거 문단: ________________________________________________</p><p>내 설명: __________________________________________________</p><p>__________________________________________________________</p><p>선생님 기록: 직접 읽고 설명 □ / 질문 도움 □ / 대신 읽어 줌 □</p></article>`).join('')}<p>종이 수행은 앱의 성취·문항 노출 이력에 자동 반영되지 않습니다. 같은 글을 이미 본 학생에게 앱에서 독립 확인용으로 다시 배정하지 않습니다.</p></body></html>`;
 writeFileSync(resolve(out,`student-check-g${grade}-${course}.html`),student);
}
const index=`<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>학년별 평가 자료 모음</title><style>${css}</style><body><header><h1>초1~6 평가 자료 모음</h1><p>진단 172 + 성취 확인 288 = 460과제의 편집 검수본입니다. AI 검토와 자동 검증을 거쳤으며, 담당 교사의 최종 수업 검토와 실제 학생 응답에 따른 난도 보정은 별도입니다.</p><p><a href="teacher-review.html">교사용 정답·근거·해설·채점 안내 열기</a> · <a href="review-summary.json">검수 집계</a></p><p>학생용 자료에는 정답을 넣지 않았습니다. 종이로 먼저 공개한 문항은 앱에서 새 글 독립 성취 근거로 다시 사용하지 않습니다.</p></header>${[1,2,3,4,5,6].map(g=>`<article><h2>초${g}</h2><p>진단: <a href="student-diagnostic-g${g}-support.html">지원형</a> · <a href="student-diagnostic-g${g}-extend.html">확장형</a></p><p>성취 확인: ${courseOrder.map(c=>`<a href="student-check-g${g}-${c}.html">${esc(courseNames[c])}</a>`).join(' · ')}</p></article>`).join('')}</body></html>`;
writeFileSync(resolve(out,'index.html'),index);

console.log(JSON.stringify(summary));
