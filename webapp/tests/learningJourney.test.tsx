import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import {
  journeyPassages,
  journeyTasks,
  journeyStages,
  modelSteps,
  getJourneyPassages,
} from "../src/data/learningJourney";
import {
  createJourneyAttempt,
  enterJourneyStage,
  editJourneyResponse,
  submitJourneyResponse,
  journeyObservations,
  responseChanged,
} from "../src/services/learningJourney";
import { useLearningJourney } from "../src/store/useLearningJourney";
import { LearningJourneyStudio } from "../src/components/student/LearningJourneyStudio";
import { LearningEvidenceReport } from "../src/components/common/LearningEvidenceReport";

const now = "2026-10-14T12:00:00Z";
const fresh = () => createJourneyAttempt("test-attempt", now);
function independent(seen: string[] = []) {
  let a = enterJourneyStage(fresh(), "independent", seen).attempt;
  return editJourneyResponse(a, "independent", {
    evidence: ["library-2"],
    answer: "책을 구별하고 서가에서 찾도록 붙인 기호입니다.",
    reason: "기호의 역할을 직접 설명하는 문장이기 때문입니다.",
  });
}

test("수업의 구절 식별자는 고유하며 시범·활동 근거가 해당 지문에 존재한다", () => {
  const ids = Object.values(journeyPassages).flatMap((p) =>
    p.paragraphs.flatMap((x) => x.sentences.map((s) => s.id)),
  );
  assert.equal(ids.length, new Set(ids).size);
  for (const t of Object.values(journeyTasks)) {
    const local = journeyPassages[t.passage].paragraphs.flatMap((p) =>
      p.sentences.map((s) => s.id),
    );
    assert.ok(t.acceptableEvidence.every((e) => local.includes(e)));
    assert.equal(t.hints.length, 3);
  }
  assert.ok(modelSteps.every((m) => ids.includes(m.anchor)));
  assert.notEqual(
    journeyTasks.independent.passage,
    journeyTasks.transfer.passage,
  );
});

test("도움을 사용한 뒤 돌아가거나 0으로 바꿔도 독립 수행으로 기록되지 않는다", () => {
  let a = editJourneyResponse(independent(), "independent", { helpLevel: 2 });
  a = editJourneyResponse(a, "independent", { helpLevel: 0 });
  a = enterJourneyStage(a, "start", []).attempt;
  a = enterJourneyStage(a, "independent", []).attempt;
  a = submitJourneyResponse(a, "independent", "helped", now);
  const o = journeyObservations(a)[0];
  assert.equal(o.support, "guided");
  assert.equal(a.responses.independent!.helpLevel, 2);
  assert.equal(o.outcome, "pending_review");
});

test("교사 확인 전 서술 응답은 정답 근거를 선택해도 자동 성공이 되지 않는다", () => {
  const a = submitJourneyResponse(independent(), "independent", "first", now);
  assert.equal(a.responses.independent!.submissions[0].evidenceMatch, true);
  assert.equal(journeyObservations(a)[0].outcome, "pending_review");
  assert.equal(journeyObservations(a)[0].support, "independent");
  assert.equal(journeyObservations(a)[0].passageExposure, "new");
  assert.equal(a.responses.independent!.submissions[0].passageVersion, 2);
  assert.match(
    a.responses.independent!.submissions[0].evidenceQuotes["library-2"],
    /청구기호/,
  );
});

test("해설 후 수정과 새 시도의 기존 지문은 새 글 독립 확인으로 승격하지 않는다", () => {
  let a = submitJourneyResponse(independent(), "independent", "first", now);
  const first = structuredClone(a.responses.independent!.submissions[0]);
  a = editJourneyResponse(a, "independent", {
    answer: "책의 주제 등에 따라 책을 구별하고 위치를 찾는 기호입니다.",
  });
  assert.equal(responseChanged(a.responses.independent!), true);
  a = submitJourneyResponse(a, "independent", "revised", now);
  assert.deepEqual(a.responses.independent!.submissions[0], first);
  assert.equal(journeyObservations(a)[1].passageExposure, "practiced");
  const b = submitJourneyResponse(
    independent(["readx-definition-library@1"]),
    "independent",
    "repeat",
    now,
  );
  assert.equal(journeyObservations(b)[0].passageExposure, "practiced");
});

test("다른 글의 근거·빈 응답·같은 이벤트 재전송을 거절하고 이전 근거를 보존한다", () => {
  const invalid = editJourneyResponse(independent(), "independent", {
    evidence: ["solution-2"],
  });
  assert.deepEqual(invalid.responses.independent!.evidence, []);
  assert.equal(
    submitJourneyResponse(invalid, "independent", "invalid", now),
    invalid,
  );
  const a = submitJourneyResponse(independent(), "independent", "once", now);
  assert.equal(submitJourneyResponse(a, "independent", "once", now), a);
  assert.equal(submitJourneyResponse(a, "independent", "twice", now), a);
  const edited = editJourneyResponse(a, "independent", {
    evidence: ["library-3"],
  });
  assert.deepEqual(edited.responses.independent!.submissions[0].evidence, [
    "library-2",
  ]);
});

test("기기 저장 재수화가 현재 위치·도움·노출·교사 메모·수정본을 복원한다", async () => {
  useLearningJourney.setState({
    attempts: [independent()],
    activeId: "test-attempt",
    seenPassages: ["readx-definition-library@1"],
  });
  const s = useLearningJourney.getState();
  s.edit("independent", { helpLevel: 1 });
  s.submit("independent");
  s.write("처음 문장");
  s.saveRevision();
  s.write("고친 문장");
  s.saveRevision();
  const a = useLearningJourney.getState().attempts[0];
  s.review(a.id, "independent", a.responses.independent!.submissions[0].id, {
    outcome: "success",
    note: "정의와 근거의 연결을 확인함",
    at: now,
  });
  const serialized = localStorage.getItem("readx_learning_journey_demo_v1")!;
  useLearningJourney.setState({
    attempts: [],
    activeId: null,
    seenPassages: [],
  });
  localStorage.setItem("readx_learning_journey_demo_v1", serialized);
  await useLearningJourney.persist.rehydrate();
  const restored = useLearningJourney.getState().attempts[0];
  assert.equal(restored.stage, "independent");
  assert.equal(restored.responses.independent!.helpLevel, 1);
  assert.equal(restored.revisions.length, 2);
  assert.equal(journeyObservations(restored)[0].outcome, "success");
  assert.equal(journeyObservations(restored)[0].support, "guided");
  assert.deepEqual(useLearningJourney.getState().seenPassages, [
    "readx-definition-library@1",
  ]);
});

test("8개 학습 과정과 교사·학부모·학생 기록 화면이 저장된 응답으로 렌더된다", () => {
  // SSR reads Zustand's initial snapshot; point it at each explicit test fixture.
  const initialSnapshot = useLearningJourney.getInitialState();
  const originalInitial = { ...initialSnapshot };
  try {
    const a = submitJourneyResponse(
      independent(),
      "independent",
      "render",
      now,
    );
    for (const stage of journeyStages) {
      useLearningJourney.setState({
        attempts: [{ ...a, stage: stage.id }],
        activeId: a.id,
      });
      Object.assign(initialSnapshot, useLearningJourney.getState());
      const html = renderToStaticMarkup(<LearningJourneyStudio />);
      assert.match(html, new RegExp(stage.label));
      assert.ok(!html.includes("NaN"));
    }
    for (const audience of ["teacher", "parent", "student"] as const) {
      const html = renderToStaticMarkup(
        <LearningEvidenceReport audience={audience} />,
      );
      assert.match(html, /책을 구별하고 서가에서 찾도록/);
      assert.match(html, /설명 검토 전/);
    }
    useLearningJourney.setState({
      attempts: [],
      activeId: null,
      seenPassages: [],
    });
  } finally {
    Object.assign(initialSnapshot, originalInitial);
  }
});
