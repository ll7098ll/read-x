import React from 'react';
import test from 'node:test';
import assert from 'node:assert/strict';
import { renderToStaticMarkup } from 'react-dom/server';
import { miniExamForms, transferChecks } from '../src/data/miniExams';
import { answerMiniQuestion, createMiniAttempt, goalProgress, kstDay, miniHistory, miniItems, miniScore, submitMiniAttempt, transferSuccess, validMiniForm, validQuestion } from '../src/services/miniExam';
import { ASSESSMENT_STORAGE_KEY, assessmentStorage, useAssessmentStorageStatus, useStudentAssessment, validateAssessmentSnapshot } from '../src/store/useStudentAssessment';
import { AssessmentEntryCards, MiniExamPlayer, MiniExamResult, StudentAssessmentHub } from '../src/components/student/StudentAssessmentHub';
import type { MiniExamAttempt, TransferAttempt } from '../src/types/miniExam';
import { useCoursewareStore } from '../src/store/useCoursewareStore';

const at = Date.parse('2026-10-15T02:00:00Z');
const form = miniExamForms[0];
const clean = () => useStudentAssessment.setState({ attempts: [], checks: [], remediations: [], view: 'overview', screen: { kind: 'dashboard' }, activePassage: 0 });
function completed(correct = true, id = 'exam', now = at): MiniExamAttempt {
  let a = createMiniAttempt(form, [], now, id);
  for (const { question: q } of miniItems(form)) a = answerMiniQuestion(a, q.id, correct ? q.answer : (q.answer + 1) % 5, now + 1000);
  return submitMiniAttempt(a, now + 60000);
}
function passedCheck(index: number, now: number): TransferAttempt {
  const check = transferChecks.filter(c => c.grade === 5 && c.goal === 'compare')[index];
  return { id: `check-${index}`, learnerId: 'local-practice', check, startedAt: now - 1000, submittedAt: now,
    fresh: true, choice: check.question.answer, evidence: [...check.question.evidence] };
}

test('초5·6 시험지는 각각 새 지문 3개·12문항과 정답·오답 이유·본문 근거를 갖는다', () => {
  assert.equal(miniExamForms.length, 2);
  const ids = new Set<string>();
  for (const f of miniExamForms) {
    assert.ok(validMiniForm(f)); assert.equal(f.passages.length, 3); assert.equal(miniItems(f).length, 12); assert.equal(f.durationSec, 1500);
    for (const p of f.passages) {
      const length = p.paragraphs.map(p => p.text).join(' ').length;
      assert.ok(length >= 800, `${p.id}: ${length}자`);
      for (const q of p.questions) { assert.ok(!ids.has(q.id)); ids.add(q.id); assert.ok(q.optionReasons.every(s => s.length > 5)); }
    }
  }
  for (const c of transferChecks) assert.ok(validQuestion(c.question, c.paragraphs.map(p => p.id)), c.id);
  assert.equal(transferChecks.length, 12); assert.equal(new Set(transferChecks.map(c => c.familyId)).size, 12);
});
test('정답수·오답·미응답과 100점 환산은 실제 시험 전체 분모를 쓴다', () => {
  let a = createMiniAttempt(form, [], at);
  const items = miniItems(form);
  a = answerMiniQuestion(a, items[0].question.id, items[0].question.answer, at + 1);
  a = answerMiniQuestion(a, items[1].question.id, (items[1].question.answer + 1) % 5, at + 2);
  const score = miniScore(submitMiniAttempt(a, at + 5000));
  assert.equal(score.correct, 1); assert.equal(score.wrong, 1); assert.equal(score.unanswered, 10); assert.equal(score.percent, 8.3);
  assert.equal(miniScore(completed()).percent, 100); assert.equal(miniScore(completed(false)).percent, 0);
  assert.ok(score.skills.some(s => s.total === 0) === false);
});
test('새로고침용 마감 시각과 최초 선택을 보존하고 마감 뒤 답안·중복 제출을 잠근다', () => {
  const q = miniItems(form)[0].question;
  let a = createMiniAttempt(form, [], at);
  a = answerMiniQuestion(a, q.id, 2, at + 1); a = answerMiniQuestion(a, q.id, 0, at + 2);
  assert.equal(a.firstAnswers[q.id], 2); assert.equal(a.answers[q.id], 0);
  a = JSON.parse(JSON.stringify(a));
  assert.equal(a.deadlineAt, at + 1500000);
  const expired = answerMiniQuestion(a, q.id, 4, a.deadlineAt);
  assert.equal(expired.status, 'auto_submitted'); assert.equal(expired.answers[q.id], 0); assert.equal(expired.submittedAt, a.deadlineAt);
  assert.equal(answerMiniQuestion(expired, q.id, 1, a.deadlineAt + 1), expired);
  assert.equal(submitMiniAttempt(expired, at + 2000000), expired);
});
test('시험지는 시작할 때 고정되고 잘못된 문항·선택지는 기록되지 않는다', () => {
  const original = structuredClone(form); const a = createMiniAttempt(original, [], at);
  original.passages[0].questions[0].answer = 4;
  assert.equal(a.form.passages[0].questions[0].answer, form.passages[0].questions[0].answer);
  assert.equal(answerMiniQuestion(a, 'missing', 1, at + 1), a);
  assert.equal(answerMiniQuestion(a, form.passages[0].questions[0].id, 99, at + 1), a);
  const bad = structuredClone(form); bad.passages[0].questions[0].evidence = ['absent']; assert.equal(validMiniForm(bad), false);
});
test('한 지문 만점·같은 글 재응시·미완료 확인으로 목표 달성을 만들지 않는다', () => {
  const a = completed();
  let p = goalProgress('compare', 5, [a], [], [], at + 100000);
  assert.equal(p.total, 4); assert.equal(p.families, 1); assert.equal(p.achieved, false);
  const repeat = { ...completed(true, 'repeat', at + 70000), freshFamilies: [] };
  p = goalProgress('compare', 5, [a, repeat], [], [], at + 150000);
  assert.equal(p.total, 4); assert.equal(p.achieved, false);
  const unfinished = { ...passedCheck(0, at + 70000), submittedAt: undefined };
  assert.equal(goalProgress('compare', 5, [a], [unfinished], [], at + 150000).total, 4);
});
test('서로 다른 새 글의 답·근거가 성공해야 목표 기준을 충족하고 과거 달성을 보존한다', () => {
  const a = completed(), checks = [passedCheck(0, at + 70000), passedCheck(1, at + 80000)];
  let p = goalProgress('compare', 5, [a], checks, [], at + 90000);
  assert.equal(p.families, 3); assert.equal(p.state, 'transfer'); assert.equal(p.achieved, true);
  const wrongEvidence = { ...checks[1], evidence: [] };
  assert.equal(transferSuccess(wrongEvidence), false);
  assert.equal(goalProgress('compare', 5, [a], [checks[0], wrongEvidence], [], at + 90000).achieved, false);
  assert.equal(goalProgress('compare', 5, [a], checks.map(c => ({ ...c, fresh: false })), [], at + 90000).achieved, false);
  p = goalProgress('compare', 5, [a], checks, [], at + 40 * 86400000);
  assert.equal(p.achieved, true); assert.equal(p.needsRecheck, true);
  assert.equal(goalProgress('compare', 6, [a], checks, [], at + 90000).total, 0);
});
test('스토어에서 실제 응시·복습·새 글 확인을 저장하고 이력을 하나씩만 만든다', () => {
  clean(); const s = () => useStudentAssessment.getState();
  const id = s().start(5, at), q = form.passages[0].questions[0];
  assert.equal(s().start(5, at + 1), id);
  s().setPassage(2); assert.equal(s().attempts[0].passageIndex, 2);
  s().answer(id, q.id, (q.answer + 1) % 5, at + 2); s().submit(id, at + 1000); s().submit(id, at + 2000);
  s().beginRemediation(id, q.id, at + 3000);
  const review = s().remediations[0];
  s().answerRemediation(review.id, q.answer, at + 4000); assert.equal(s().remediations[0].completedAt, undefined);
  s().advanceRemediation(review.id); s().advanceRemediation(review.id);
  s().answerRemediation(review.id, (q.answer + 1) % 5, at + 5000); s().answerRemediation(review.id, q.answer, at + 6000);
  s().beginRemediation(id, q.id, at + 7000);
  assert.equal(s().remediations.length, 1); assert.equal(s().remediations[0].tries, 2); assert.ok(s().remediations[0].completedAt);
  assert.equal(miniScore(s().attempts[0]).correct, 0);
  const c = transferChecks[0]; s().beginCheck(c.id, at + 8000); const check = s().checks[0];
  s().submitCheck(check.id, at + 9000); assert.equal(s().checks[0].submittedAt, undefined);
  s().editCheck(check.id, { choice: c.question.answer, evidence: c.question.evidence }); s().submitCheck(check.id, at + 10000);
  s().editCheck(check.id, { choice: 4 }); assert.equal(s().checks[0].choice, c.question.answer);
  s().beginCheck(c.id, at + 11000); assert.equal(s().checks.length, 1);
  assert.equal(miniHistory(s().attempts, s().remediations, s().checks, 5).length, 3);
  const raw = JSON.parse(localStorage.getItem(ASSESSMENT_STORAGE_KEY)!);
  assert.ok(validateAssessmentSnapshot(raw.state));
  useStudentAssessment.setState({ attempts: [], checks: [], remediations: [] });
  localStorage.setItem(ASSESSMENT_STORAGE_KEY, JSON.stringify(raw));
  useStudentAssessment.persist.rehydrate();
  assert.equal(s().attempts.length, 1); assert.equal(s().checks.length, 1); assert.equal(s().remediations.length, 1);
  assert.equal(s().attempts[0].passageIndex, 2);
  clean();
});
test('다른 활동에서 이미 본 글 계열은 새 글 확인으로 중복 집계하지 않는다', () => {
  clean(); const s = () => useStudentAssessment.getState();
  const a = transferChecks.find(c => c.grade === 5 && c.goal === 'compare')!;
  const b = transferChecks.find(c => c.grade === 6 && c.goal === 'compare')!;
  s().beginCheck(a.id, at);
  useStudentAssessment.setState({checks:s().checks.map(c=>({...c,check:{...c.check,familyId:b.familyId}}))});
  s().beginCheck(b.id, at + 1000);
  assert.equal(s().checks[0].fresh, true); assert.equal(s().checks[1].fresh, false); clean();
});
test('필수 조건 문단을 누락하면 거절하고 적절한 추가 근거와 대체 근거는 인정한다', () => {
  const compare = transferChecks.find(c => c.id === 'g5-compare-check2')!;
  const run: TransferAttempt = { id:'evidence-test',learnerId:'local-practice',check:compare,startedAt:at,submittedAt:at+1,fresh:true,choice:compare.question.answer,evidence:[compare.paragraphs[0].id] };
  assert.equal(transferSuccess(run),false);
  const evaluate = transferChecks.find(c => c.id === 'g5-evaluate-check2')!;
  const second = {...run,check:evaluate,choice:evaluate.question.answer,evidence:evaluate.paragraphs.map(p=>p.id)};
  assert.equal(transferSuccess(second),true);
  const survey = transferChecks.find(c => c.id === 'g6-evaluate-survey')!;
  for (const paragraph of survey.paragraphs) assert.equal(transferSuccess({...run,check:survey,choice:survey.question.answer,evidence:[paragraph.id]}),true);
  assert.equal(transferSuccess({...run,evidence:['other-passage']}),false);
});
test('응시 화면에는 정답·해설이 없고 제출 후 결과 화면에서만 열린다', () => {
  clean(); const a = createMiniAttempt(form, [], Date.now());
  const q = form.passages[0].questions[0];
  const html = renderToStaticMarkup(<MiniExamPlayer attempt={a}/>);
  assert.ok(html.includes(q.prompt)); assert.ok(!html.includes(q.explanation)); assert.ok(!html.includes(q.optionReasons[0]));
  assert.ok(!html.includes('정답 1번'));
  const result = renderToStaticMarkup(<MiniExamResult attempt={completed()}/>);
  assert.ok(result.includes(q.explanation)); assert.ok(result.includes('문항별 결과와 해설'));
});
test('빈 대시보드·성적·목표·학습이력은 가짜 수치나 NaN 없이 렌더된다', () => {
  clean(); useCoursewareStore.setState({ activeGradeIdx: 4 });
  for (const view of ['overview', 'exams', 'report', 'goals', 'history'] as const) {
    useStudentAssessment.getState().setView(view);
    const html = renderToStaticMarkup(<StudentAssessmentHub/>);
    assert.ok(html.includes('이 브라우저에 저장')); assert.ok(!html.includes('NaN')); assert.ok(!html.includes('백분위'));
  }
  assert.ok(renderToStaticMarkup(<AssessmentEntryCards grade={5}/>).includes('첫 기록을 기다려요'));
  assert.equal(kstDay(Date.parse('2026-10-14T15:00:00Z')), '2026-10-15');
  assert.equal(validateAssessmentSnapshot({ attempts: [{}], checks: [], remediations: [] }), false); clean();
});

test('저장 실패를 알리고 현재 응답을 보존하며 다음 정상 저장에서 회복한다', () => {
  clean(); const s = () => useStudentAssessment.getState(), id = s().start(5, at), q = form.passages[0].questions[0];
  const original = localStorage.setItem;
  localStorage.setItem = () => { throw new Error('quota'); };
  try { s().answer(id, q.id, q.answer, at + 1); assert.ok(useAssessmentStorageStatus.getState().error); assert.equal(s().attempts[0].answers[q.id], q.answer); }
  finally { localStorage.setItem = original; }
  assessmentStorage.setItem(ASSESSMENT_STORAGE_KEY, JSON.stringify({state:{attempts:s().attempts,checks:[],remediations:[]},version:1}));
  assert.equal(useAssessmentStorageStatus.getState().error, '');
  assert.equal(validateAssessmentSnapshot({attempts:[],remediations:[],checks:[{learnerId:'local-practice',id:'bad',choice:1,evidence:[],fresh:true,startedAt:at,check:{grade:5,paragraphs:[null]}}]}), false);
  clean();
});
