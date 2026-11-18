import './privacyDefaults.test';
import './draftCache.test';
import './overview.test';
import React from 'react';
import './learningJourney.test';
import './readingScaffold.test';
import './progressiveReading.test';
import './corpusRevision.test';
import './curriculumIntegration.test';
import './miniExam.test';
import './annotationExperience.test';
import './examIntegration.test';
import { renderToStaticMarkup } from 'react-dom/server';
import test from 'node:test';
import assert from 'node:assert/strict';
import raw from '../src/data/commercialMasterData.json';
import { masterData, findLesson } from '../src/data/lessonCatalog';
import { normalizeSlotPackage, normalizeCommonSlot, validateSlotPackage } from '../src/services/contentSchema';
import { resolveActiveGradeAndSlotData } from '../src/services/firebaseDbService';
import { useCoursewareStore, DEMO_STORAGE_KEY } from '../src/store/useCoursewareStore';
import { AdaptiveClinicStudio } from '../src/components/student/AdaptiveClinicStudio';
import { ClinicDrill, CommonFoundationStudio } from '../src/components/student/ClinicActivities';
import { EBSRQuestionCard } from '../src/components/tei/EBSRQuestionCard';
import { GraphicOrganizerBuilder } from '../src/components/tei/GraphicOrganizerBuilder';
import { WritingWorkbench } from '../src/components/tei/WritingWorkbench';
import { SplitScreenStudio } from '../src/components/student/SplitScreenStudio';
import { buildContentLibrary, passagesForGoal } from '../src/data/contentLibrary';
import { summarizeProcessEvidence } from '../src/services/processEvidence';
import type { ProcessObservation } from '../src/types/contentLibrary';
import { useReadingWorkspace, useReadingStorageStatus, practiceStorage } from '../src/store/useReadingWorkspace';

const slots = masterData.expository_slots_96!;
test('96개 수업의 이관은 원본 지문·정답·세부목표를 보존하며 재실행해도 같다', () => {
  assert.equal(slots.length, 96);
  for (let i = 0; i < slots.length; i++) {
    const before = JSON.stringify(raw.expository_slots_96[i]);
    const normalized = normalizeSlotPackage(raw.expository_slots_96[i]);
    assert.deepEqual(normalizeSlotPackage(normalized), normalized);
    assert.deepEqual(normalized.real_csat_test.paragraphs, raw.expository_slots_96[i].real_csat_test.paragraphs);
    assert.equal(normalized.mager_goal, raw.expository_slots_96[i].mager_goal);
    for (const [q, question] of normalized.real_csat_test.questions.entries()) {
      assert.deepEqual(question.options.map(o => [o.text, o.is_correct]), raw.expository_slots_96[i].real_csat_test.questions[q].options.map(o => [o.text, o.is_correct]));
    }
    assert.equal(JSON.stringify(raw.expository_slots_96[i]), before);
  }
});

test('96 × 5 = 480 활동 렌더와 36개 기초 수업 렌더가 성공한다', () => {
  let rendered = 0;
  for (const slot of slots) {
    const { activeGradeData, resolutionError } = resolveActiveGradeAndSlotData(masterData, slot.grade_num - 1, slot.slot_id, {});
    assert.equal(resolutionError, null);
    const views = [<AdaptiveClinicStudio gradeData={activeGradeData} />, <EBSRQuestionCard data={slot.commercial.ebsr_question} />,
      <GraphicOrganizerBuilder data={slot.commercial.graphic_organizer} />, <WritingWorkbench data={slot.commercial.writing_workbench} />,
      <ClinicDrill drill={slot.prescription_clinic.step1_2_drill} />];
    for (const view of views) { assert.ok(renderToStaticMarkup(view).length > 0, slot.slot_id); rendered++; }
  }
  assert.equal(rendered, 480);
  for (const common of masterData.common_slots_36!) assert.ok(renderToStaticMarkup(<CommonFoundationStudio data={common} />));
});

test('없는 과제·다른 학년·잘못된 편집본이 다른 지문으로 대체되지 않는다', () => {
  for (const id of ['G5-EXP-I1-1', 'G6-EXP-V1-1', 'G5-COM-A9']) {
    const result = resolveActiveGradeAndSlotData(masterData, 4, id, {});
    assert.equal(result.activeSlotPackage, null); assert.equal(result.activeCommonSlot, null); assert.ok(result.resolutionError);
  }
  const malformed = { ...slots[0], grade_num: 2 };
  const bad = resolveActiveGradeAndSlotData(masterData, 0, slots[0].slot_id, { [slots[0].slot_id]: malformed });
  assert.ok(bad.resolutionError); assert.equal(bad.activeSlotPackage, null);
  const common = resolveActiveGradeAndSlotData(masterData, 4, 'G5-COM-A3', {});
  assert.equal(common.activeCommonSlot?.code, 'G5-COM-A3'); assert.equal(common.activeSlotPackage, null); assert.equal(common.resolutionError, null);
});

test('검증기는 파손된 필드·중복 식별자·없는 정답·잘못된 근거를 거절한다', () => {
  const mutations = [
    (s: any) => s.real_csat_test.questions[0].options[0].no = undefined,
    (s: any) => s.real_csat_test.questions[0].options[1].no = s.real_csat_test.questions[0].options[0].no,
    (s: any) => s.commercial.ebsr_question.part_a_options = undefined,
    (s: any) => s.commercial.graphic_organizer.word_bank = [],
    (s: any) => s.commercial.writing_workbench.conditions = null,
    (s: any) => s.prescription_clinic.step1_2_drill.blanks[0].correct = '없는 정답',
    (s: any) => s.commercial.question_scaffolding[0].spotlight_quote = '원문에 없는 인용',
    (s: any) => s.slot_id = 'G6-EXP-V1-1',
    (s: any) => s.schema_version = '9.0',
  ];
  for (const mutate of mutations) {
    const value = structuredClone(slots[0]); mutate(value);
    assert.equal(validateSlotPackage(value).isValid, false);
    assert.throws(() => normalizeSlotPackage(value));
  }
  for (const value of [null, 42, [], {}, { real_csat_test: { questions: [null] } }]) assert.equal(validateSlotPackage(value).isValid, false);
});

test('공통기초 36개 정답은 정확히 하나의 선택지와 일치한다', () => {
  assert.equal(masterData.common_slots_36!.length, 36);
  for (const slot of masterData.common_slots_36!) assert.equal(slot.choices.filter(c => c === slot.correct).length, 1);
  assert.throws(() => normalizeCommonSlot({ ...masterData.common_slots_36![0], correct: '없는 정답' }));
});

test('정답이 없는 구조 자료와 자유 작문을 자동 채점 문제로 바꾸지 않는다', () => {
  assert.equal(slots.filter(s => s.commercial.graphic_organizer.activityType === 'reference').length, 77);
  assert.equal(slots.filter(s => s.commercial.writing_workbench.activityType === 'free_response').length, 77);
  const slot = slots.find(s => s.commercial.writing_workbench.activityType === 'free_response')!;
  const html = renderToStaticMarkup(<WritingWorkbench data={slot.commercial.writing_workbench} draftKey="test-writing" />);
  assert.match(html, /textarea/); assert.match(html, /교사의 확인/);
  const grade = resolveActiveGradeAndSlotData(masterData, slot.grade_num - 1, slot.slot_id, {}).activeGradeData;
  const studio = renderToStaticMarkup(<SplitScreenStudio gradeData={grade} />);
  assert.match(studio, /함께 생각하는 안내/); assert.match(studio, /내 말로 쓰기/);
});

test('체험 기록 격리, 가짜 점수 가산 금지, 잘못된 저장·배정·완료 거절', () => {
  assert.match(DEMO_STORAGE_KEY, /demo/);
  const store = useCoursewareStore.getState();
  const before = JSON.stringify(store.smartScores);
  store.boostSmartScore(5, 1000); store.updateSubskillScore('G5-EXP-V1-1', 100);
  assert.equal(JSON.stringify(useCoursewareStore.getState().smartScores), before);
  assert.deepEqual(useCoursewareStore.getState().dynamicSubskillScores, {});
  const task = store.assignments[0];
  store.completeStudentAssignment(task.id, 92);
  assert.equal(useCoursewareStore.getState().assignments[0].status, 'pending');
  assert.equal(store.assignTaskToStudent({ ...task, slotId: 'G5-EXP-I1-1' }), false);
  assert.equal(store.saveCustomSlotToDb({ ...slots[0], grade_num: 6 }), false);
  for (const assignment of store.assignments) assert.ok(findLesson(assignment.slotId));
  store.saveResponseDraft('one:writing', '내가 찾은 근거'); store.saveResponseDraft('two:writing', '다른 수업');
  assert.equal(useCoursewareStore.getState().responseDrafts['one:writing'], '내가 찾은 근거');
});

test('체험 초안은 재수화 후 복구되며 이전 저장소는 삭제하지 않는다', async () => {
  localStorage.setItem('readxray_pro_production_store_v4', 'legacy-preserved');
  useCoursewareStore.getState().saveResponseDraft('persist:writing', '근거를 연결한 문장');
  assert.equal(JSON.parse(localStorage.getItem(DEMO_STORAGE_KEY)!).state.responseDrafts['persist:writing'], '근거를 연결한 문장');
  await useCoursewareStore.persist.rehydrate();
  assert.equal(useCoursewareStore.getState().responseDrafts['persist:writing'], '근거를 연결한 문장');
  assert.equal(localStorage.getItem('readxray_pro_production_store_v4'), 'legacy-preserved');
});

test('세부목표 하나에 여러 지문을 연결하고 이미 읽은 지문을 제외할 수 있다', () => {
  const library = buildContentLibrary(masterData);
  assert.equal(library.passages.length, 96);
  assert.equal(new Set(library.goals.map(g => g.id)).size, 96);
  assert.ok(library.concepts.every(c => c.reviewState === 'needs_review' && c.standardRefs.length === 0));
  const first = library.passages[0];
  library.passages.push({ ...first, id: 'alternate-passage', title: '테스트용 다른 소재', reviewState: 'approved' });
  const selected = passagesForGoal(library, first.goalIds[0], { excludeIds: [first.id], approvedOnly: true });
  assert.deepEqual(selected.map(p => p.id), ['alternate-passage']);
  assert.equal(library.goals.length, 96);
});

test('사고 과정의 관찰은 학생·세부목표·도움·전이를 구분하고 중복 수신을 제외한다', () => {
  const base: ProcessObservation = { eventId:'e1', learnerId:'student-a', goalId:'goal-a', passageId:'p1', passageVersion:1,
    activityId:'a1', stage:'connect', support:'guided', purpose:'practice', passageExposure:'new', outcome:'success', response:'인과 연결', evidenceRefs:['paragraph:2'], observedAt:'2026-10-14T00:00:00Z' };
  const result = summarizeProcessEvidence([base, base, { ...base, eventId:'e2', learnerId:'other' },
    { ...base, eventId:'e3', goalId:'other' }, { ...base, eventId:'e4', support:'independent', purpose:'transfer_check', passageId:'p2' },
    { ...base, eventId:'e5', stage:'express', outcome:'pending_review' }], 'student-a', 'goal-a');
  const connecting = result.find(s => s.stage === 'connect')!;
  assert.equal(connecting.observations, 2); assert.equal(connecting.guidedSuccess, 1); assert.equal(connecting.independentSuccess, 1);
  assert.deepEqual(connecting.transferPassageIds, ['p2']);
  assert.equal(result.find(s => s.stage === 'notice')!.state, 'no_evidence');
  assert.equal(result.find(s => s.stage === 'express')!.independentSuccess, 0);
});

// Resume state must remain lesson-scoped and survive a fresh store hydration.
test('이어하기는 수업별 근거·문항·탭을 분리하고 재수화 뒤 복구한다', async () => {
  const workspace = useReadingWorkspace.getState();
  workspace.save('G5-EXP-V1-1','paragraphs',[0,2]);
  workspace.save('G5-EXP-V1-1','tab','writing');
  workspace.save('G3-EXP-V1-1','paragraphs',[1]);
  workspace.visit('G3-EXP-V1-1');
  const snapshot = localStorage.getItem('readx_reading_workspace_v1')!;
  useReadingWorkspace.setState({sessions:{},lastSlotId:null});
  localStorage.setItem('readx_reading_workspace_v1',snapshot);
  await useReadingWorkspace.persist.rehydrate();
  assert.deepEqual(useReadingWorkspace.getState().sessions['G5-EXP-V1-1'],{paragraphs:[0,2],tab:'writing'});
  assert.deepEqual(useReadingWorkspace.getState().sessions['G3-EXP-V1-1'].paragraphs,[1]);
  assert.equal(useReadingWorkspace.getState().lastSlotId,'G3-EXP-V1-1');
});

test('연습 저장 실패를 숨기지 않고 현재 입력을 보존하며 다음 저장에서 회복한다', () => {
  const original = localStorage.setItem;
  localStorage.setItem = () => { throw new Error('QuotaExceededError'); };
  try {
    assert.doesNotThrow(()=>useReadingWorkspace.getState().save('G5-EXP-V1-1','notes',['남길 메모']));
    assert.equal(useReadingStorageStatus.getState().failed,true);
    assert.deepEqual(useReadingWorkspace.getState().sessions['G5-EXP-V1-1'].notes,['남길 메모']);
  } finally { localStorage.setItem = original; }
  practiceStorage.setItem('practice-recovery-test','recovered');
  assert.equal(useReadingStorageStatus.getState().failed,false);
  localStorage.removeItem('practice-recovery-test');
});
import "./curriculumIntegration.test";
import "./academyDemo.test";
import "./reportMetrics.test";
