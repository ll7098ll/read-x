import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {placementForm,placementFormAtVersion,publicForm} from './placement-content.mjs';
import {courseBundle,courseOrder} from './course-content.mjs';
import {matchesAssessmentEvidence,editorialReviewVersion} from './assessment-review.mjs';
const lessons=JSON.parse(readFileSync(new URL('../src/data/corpusLessons.generated.json',import.meta.url)));
const check=(grade,course,index)=>courseBundle(grade,course,lessons).checks[index];

test('all 460 unique diagnostic/check variants have source-accurate keys, explanations and uncalibrated editorial difficulty',()=>{
 let count=0;const diagnostic=new Set();
 function verify(q,paragraphs){
  count++;assert.equal(q.editorialReview.version,editorialReviewVersion);
  assert.equal(q.editorialReview.empiricalDifficulty,'미보정');assert.match(q.difficulty.basis,/보정하기 전/);
  assert.ok(q.explanation.length>=12);assert.ok(q.sampleResponse);assert.ok(q.scoringGuide.full);assert.ok(q.scoringGuide.doNotRequire);
  assert.ok(q.evidence.length);assert.deepEqual(q.evidenceQuotes,q.evidence.map(i=>({paragraph:i,text:paragraphs[i]})));
  assert.ok(q.evidenceQuotes.every(e=>typeof e.text==='string'&&e.text.length));
  if(q.options.length){assert.ok(q.options[q.answer]);assert.equal(new Set(q.options).size,q.options.length);assert.equal(q.optionReasons.length,q.options.length);assert.ok(q.optionReasons.every(r=>r.length>=12));}
 }
 for(let g=1;g<=6;g++){
  const common=placementForm(g);
  for(const branch of [null,'support','extend']){
   const form=placementForm(g,branch);
   assert.deepEqual(form.questions.slice(0,common.questions.length),common.questions,'branch must preserve answered common items');
   const mc=form.questions.filter(q=>q.options.length),distribution=mc[0].options.map((_,i)=>mc.filter(q=>q.answer===i).length);
   assert.ok(Math.max(...distribution)-Math.min(...distribution)<=1);
   for(const q of form.questions){const key=`${g}:${common.questions.some(c=>c.id===q.id)?'common':branch}:${q.id}`;if(diagnostic.has(key))continue;diagnostic.add(key);verify(q,form.passages.find(p=>p.id===q.passageId).paragraphs);}
   const pub=publicForm(form);for(const q of pub.questions)for(const k of ['answer','evidence','evidenceQuotes','explanation','optionReasons','sampleResponse','scoringGuide','editorialReview','difficulty','corrections'])assert.equal(k in q,false,`private diagnostic field: ${k}`);
   assert.ok(pub.passages.every(p=>!('questions'in p)));
  }
  for(const course of courseOrder)for(const q of courseBundle(g,course,lessons).checks){verify(q,q.paragraphs);assert.ok(matchesAssessmentEvidence(q,q.evidence));assert.equal(matchesAssessmentEvidence(q,[99]),false);}
 }
 assert.equal(diagnostic.size,172);assert.equal(count,460);
});

test('ambiguous preferences, return conditions, repeated draft information and forecast assumptions are corrected',()=>{
 assert.match(check(1,'evaluate',1).paragraphs[0],/사과는 좋아하지 않고 배/);
 const returning=check(1,'integrate',1);assert.match(returning.paragraphs[0],/오는 날/);assert.match(returning.paragraphs[1],/오늘은.*안 가고 내일/);assert.deepEqual(returning.evidence,[0,1]);
 const draft=check(2,'integrate',4);assert.match(draft.paragraphs[1],/“작품 이름은 봄입니다\.” 사용한 재료는 종이/);assert.equal(draft.options[draft.answer],'종이로 만들었다는 말');
 for(const g of [3,4])assert.match(check(g,'integrate',0).paragraphs[1],/실내.*확정/);
 assert.match(check(5,'connect',6).paragraphs[1],/담당자가 자리를 비워서/);
 const integrated=check(6,'integrate',7);assert.match(integrated.prompt,/모두 반영/);assert.match(integrated.options[integrated.answer],/전체 30명.*10명 중 6명.*20명 중 8명/);
});

test('grade-4 visit units and grade-2 table evidence agree with actual source rows',()=>{
 const form=placementForm(4),shade=form.passages.find(p=>p.id==='shade'),questions=form.questions.filter(q=>q.passageId==='shade');
 assert.match(shade.paragraphs[0],/횟수/);assert.doesNotMatch(shade.paragraphs.join(' '),/\d+명/);
 assert.equal(questions[1].options[questions[1].answer],'6회');assert.match(questions[2].options[questions[2].answer],/이용 횟수/);
 const table=check(2,'evidence',5);assert.deepEqual(table.evidence,[2]);assert.ok(table.evidenceQuotes[0].text.includes(table.options[table.answer]));
});

test('new checks accept sufficient evidence with additional paragraphs; version-2 snapshots keep exact-set scoring',()=>{
 const current=check(4,'interpret',3),old=courseBundle(4,'interpret',lessons,{reviewed:false}).checks[3];
 assert.deepEqual(current.evidence,[1]);assert.ok(matchesAssessmentEvidence(current,[0,1]));assert.equal(matchesAssessmentEvidence(current,[0]),false);
 assert.equal(matchesAssessmentEvidence(current,[-1,1]),false);assert.equal(matchesAssessmentEvidence(current,[1.5]),false);assert.equal(matchesAssessmentEvidence(current,null),false);
 assert.equal(matchesAssessmentEvidence({...old,evidence:[1]},[0,1]),false);assert.ok(matchesAssessmentEvidence(old,old.evidence));
 const previous=placementFormAtVersion(4,'extend','g16-placement-2');assert.equal(previous.version,'g16-placement-2');assert.ok(previous.questions.every(q=>!q.editorialReview));
 assert.notDeepEqual(previous.questions,placementForm(4,'extend').questions);
});
