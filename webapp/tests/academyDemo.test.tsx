import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import {
  demoStudents,
  demoClasses,
  demoLesson,
  demoMetrics,
} from "../src/data/demoAcademy";
import { useDemoAcademy } from "../src/store/useDemoAcademy";
import { useCoursewareStore } from "../src/store/useCoursewareStore";
import { useReadingWorkspace } from "../src/store/useReadingWorkspace";
import { DirectorDemoHub } from "../src/components/admin/DirectorDemoHub";
import { TeacherDemoOverview } from "../src/components/common/AcademyDemo";
import { ParentDemoDashboard } from "../src/components/parent/ParentDemoDashboard";

test("가상 학원 집계는 4개 반·24명의 실제 예시 상태와 일치한다", () => {
  assert.equal(new Set(demoStudents.map((s) => s.id)).size, 24);
  assert.deepEqual(demoMetrics(demoStudents), {
    total: 24,
    present: 20,
    completed: 16,
    pending: 8,
    shared: 4,
    reviewed: 8,
  });
  for (const cls of demoClasses) {
    const students = demoStudents.filter((s) => s.classId === cls.id);
    assert.equal(students.length, 6);
    assert.equal(demoMetrics(students).pending, 2);
    const lesson = demoLesson(students[0]);
    assert.equal(lesson.grade, cls.grade);
    assert.ok(lesson.paragraphs.join(" ").includes(lesson.evidence));
  }
});

test("미제출·미검토 리포트 공개를 막고 검토 이후 모든 역할의 집계를 연결한다", () => {
  useDemoAcademy.setState({ reviews: {}, releases: {} });
  const store = useDemoAcademy.getState(),
    student = demoStudents[0];
  assert.equal(store.releaseReport(student.id), false);
  assert.equal(
    store.saveReview(demoStudents[4].id, "학습 중", "근거 확인"),
    false,
  );
  assert.equal(store.saveReview(student.id, "   ", "근거 확인"), false);
  assert.equal(
    store.saveReview(student.id, " 근거를 연결했어요. ", "혼자 적용하기"),
    true,
  );
  assert.equal(store.releaseReport(student.id), true);
  const state = useDemoAcademy.getState();
  assert.equal(state.reviews[student.id].note, "근거를 연결했어요.");
  assert.deepEqual(demoMetrics(demoStudents, state.reviews, state.releases), {
    total: 24,
    present: 20,
    completed: 16,
    pending: 7,
    shared: 5,
    reviewed: 9,
  });
});

test("운영 체험 저장은 직접 학습 기록을 건드리지 않고 학생·반을 함께 복원한다", async () => {
  const learner = JSON.stringify(useCoursewareStore.getState());
  const workspace = JSON.stringify(useReadingWorkspace.getState());
  useDemoAcademy.getState().selectStudent("demo-student-03");
  useDemoAcademy
    .getState()
    .saveConsultation("consult-1", "다음 상담에서 근거 설명 확인");
  const stored = localStorage.getItem("readx_academy_mock_v1")!;
  useDemoAcademy.setState({
    selectedStudentId: "demo-student-14",
    selectedClassId: "explore",
    consultationNotes: {},
  });
  localStorage.setItem("readx_academy_mock_v1", stored);
  await useDemoAcademy.persist.rehydrate();
  const state = useDemoAcademy.getState();
  assert.equal(state.selectedStudentId, "demo-student-03");
  assert.equal(state.selectedClassId, "sprout");
  assert.equal(
    state.consultationNotes["consult-1"],
    "다음 상담에서 근거 설명 확인",
  );
  assert.equal(JSON.stringify(useCoursewareStore.getState()), learner);
  assert.equal(JSON.stringify(useReadingWorkspace.getState()), workspace);
});

test("원장·교사·학부모 첫 화면에 학원 현황과 읽기 과정 예시가 제공된다", () => {
  const director = renderToStaticMarkup(<DirectorDemoHub />);
  const teacher = renderToStaticMarkup(
    <TeacherDemoOverview onTab={() => {}} />,
  );
  const parent = renderToStaticMarkup(
    <ParentDemoDashboard practice={<p>직접 연습 기록</p>} />,
  );
  assert.match(director, /24개의 생각/);
  assert.match(director, /상담 일정/);
  assert.match(teacher, /탐구 읽기반/);
  assert.match(teacher, /김민준/);
  assert.match(parent, /이윤서의 생각/);
  assert.match(parent, /수치로 보는 학습 과정/);
  assert.match(parent, /예시 데이터/);
});
