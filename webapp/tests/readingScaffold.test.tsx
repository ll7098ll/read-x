import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import { getJourneyPassages, legacyJourneyPassages, journeyTasks, modelSteps } from "../src/data/learningJourney";
import { readingLevels, assessPassage, passageMetrics } from "../src/data/readingPolicy";
import { createJourneyAttempt, enterJourneyStage, saveJourneyAnnotation, editJourneyResponse, submitJourneyResponse, responseChanged } from "../src/services/learningJourney";
import { MarkedSentence } from "../src/components/student/ReadingAnnotations";
import { useLearningJourney } from "../src/store/useLearningJourney";

const at = "2026-10-14T12:00:00Z";
test("12개 대표 지문은 수준별 분량을 충족하고 단계별 근거·시범이 보존된다", () => {
  for (const level of readingLevels) {
    const passages = getJourneyPassages({ version: 2, readingLevel: level });
    for (const p of Object.values(passages)) {
      const paragraphs = p.paragraphs.map(p => p.sentences.map(s => s.text).join(" "));
      assert.equal(assessPassage(paragraphs, 5, level).lengthLabel, "분량 범위 안", p.id);
      const ids = p.paragraphs.flatMap(p => p.sentences.map(s => s.id));
      assert.equal(ids.length, new Set(ids).size);
    }
    for (const t of Object.values(journeyTasks)) assert.ok([...t.acceptableEvidence, ...t.supportingEvidence].every(id => passages[t.passage].paragraphs.some(p => p.sentences.some(s => s.id === id))));
    for (const m of modelSteps) assert.ok(passages.solution.paragraphs.some(p => p.sentences.some(s => s.id === m.anchor && s.text.includes(m.marking.quote))));
  }
});
test("정의에 다른 문단의 올바른 예를 보탠 응답은 불필요한 오답으로 처리하지 않는다", () => {
  let a = enterJourneyStage(createJourneyAttempt("examples", at), "guided", []).attempt;
  a = editJourneyResponse(a, "guided", { evidence: ["solution-2", "solution-supported-2-1"], answer: "용매는 녹이는 물질이며 설탕물의 물이 그 예다.", reason: "정의와 설탕을 녹인 경우를 연결했기 때문이다." });
  a = submitJourneyResponse(a, "guided", "examples-submit", at);
  assert.equal(a.responses.guided!.submissions[0].evidenceMatch, true);
  assert.equal(a.responses.guided!.submissions[0].review, undefined);
});
test("이전 짧은 글의 기록은 같은 원문을 사용하며 수준을 바꿔도 새 글로 집계하지 않는다", () => {
  assert.equal(getJourneyPassages({ version: 1 }), legacyJourneyPassages);
  const first = enterJourneyStage(createJourneyAttempt("a", at, "supported"), "independent", []);
  const second = enterJourneyStage(createJourneyAttempt("b", at, "challenge"), "independent", first.seen);
  assert.deepEqual(Object.values(second.attempt.exposures), ["practiced"]);
  const oldSeen = enterJourneyStage(createJourneyAttempt("c", at), "independent", ["readx-definition-library@1"]);
  assert.deepEqual(Object.values(oldSeen.attempt.exposures), ["practiced"]);
});
test("구절·연결 대상 검증, 제출 시 표시 보존, 삭제 뒤 이전 응답 유지", async () => {
  let a = enterJourneyStage(createJourneyAttempt("annotated", at), "independent", []).attempt;
  const passageId = getJourneyPassages(a).library.id;
  const note = { id: "note", passageId, sentenceId: "library-2", quote: "청구기호", kind: "link" as const, note: "뜻과 사용하는 예를 연결했어요.", linkedSentenceId: "library-4" };
  assert.equal(saveJourneyAnnotation(a, { ...note, linkedSentenceId: "solution-2" }), a);
  assert.equal(saveJourneyAnnotation(a, { ...note, quote: "없는 구절" }), a);
  assert.equal(saveJourneyAnnotation(a, { ...note, note: " " }), a);
  a = saveJourneyAnnotation(a, note);
  a = editJourneyResponse(a, "independent", { evidence: ["library-2"], answer: "책의 자리를 찾는 기호", reason: "역할을 설명하기 때문" });
  a = submitJourneyResponse(a, "independent", "submitted", at);
  assert.equal(a.responses.independent!.submissions[0].annotations![0].note, note.note);
  assert.equal(responseChanged(a.responses.independent!, []), true);
  useLearningJourney.setState({ attempts: [a], activeId: a.id });
  useLearningJourney.getState().removeAnnotation("note");
  const serialized = localStorage.getItem("readx_learning_journey_demo_v1")!;
  useLearningJourney.setState({ attempts: [], activeId: null });
  localStorage.setItem("readx_learning_journey_demo_v1", serialized);
  await useLearningJourney.persist.rehydrate();
  const restored = useLearningJourney.getState().attempts[0];
  assert.equal(restored.readingLevel, "standard");
  assert.deepEqual(restored.annotations, []);
  assert.equal(restored.responses.independent!.submissions[0].annotations!.length, 1);
  useLearningJourney.setState({ attempts: [], activeId: null, seenPassages: [] });
});
test("본문 계수는 표식을 제외하고 빈 글을 처리하며 중첩 표시는 원문을 중복하지 않는다", () => {
  assert.equal(passageMetrics(["<b>가 나</b>", "다 라."]).chars, 8);
  assert.equal(passageMetrics([]).wordsPerSentence, 0);
  const html = renderToStaticMarkup(<MarkedSentence text="녹는 물질을 용질이라고 합니다." marks={[{ quote: "녹는 물질", kind: "evidence" }, { quote: "물질", kind: "target" }]} />);
  assert.equal(html.replace(/<[^>]*>/g, ""), "녹는 물질을 용질이라고 합니다.");
});
