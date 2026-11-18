import test from "node:test";
import assert from "node:assert/strict";
import {
  summarizeReport,
  journeyReportRecords,
  validRubric,
  reportCsv,
  type ReportRecord,
} from "../src/services/reportMetrics";
import {
  demoReportRecords,
  reportPeriods,
  todayRecordId,
} from "../src/data/demoReportRecords";
import { demoStudents } from "../src/data/demoAcademy";
import { useDemoAcademy } from "../src/store/useDemoAcademy";
import { createJourneyAttempt } from "../src/services/learningJourney";

const base: ReportRecord = {
  id: "a",
  learnerId: "one",
  date: "2026-10-14",
  title: "근거 확인",
  goal: "goal",
  initial: {
    choiceCorrect: false,
    evidenceCorrect: true,
    hints: 0,
    independent: true,
    fresh: true,
    transfer: true,
    confirmed: true,
  },
  rubric: [2, 1, 2, 1],
  revised: false,
};
test("리포트는 첫 응답과 분모를 보존하고 재전송·미제출·미평가를 구분한다", () => {
  const rows = [
    base,
    base,
    { ...base, id: "b", initial: null, rubric: null },
    {
      ...base,
      id: "c",
      initial: {
        ...base.initial!,
        choiceCorrect: null,
        evidenceCorrect: null,
        confirmed: null,
      },
      rubric: null,
    },
  ];
  const s = summarizeReport(rows);
  assert.equal(s.assigned, 3);
  assert.equal(s.submitted, 2);
  assert.deepEqual(s.answer, { numerator: 0, denominator: 1, percent: 0 });
  assert.deepEqual(s.evidence, { numerator: 1, denominator: 1, percent: 100 });
  assert.equal(s.transferPending, 1);
  assert.equal(s.transfer.denominator, 1);
  assert.equal(s.rubricAverage, 6);
  assert.equal(s.pending, 1);
  assert.equal(summarizeReport([]).answer.percent, null);
});
test("도움·재노출·안내 조건의 정답은 새 글 독립 수행 집계로 승격되지 않는다", () => {
  const rows = [
    base,
    { ...base, id: "hint", initial: { ...base.initial!, hints: 1 } },
    { ...base, id: "seen", initial: { ...base.initial!, fresh: false } },
    {
      ...base,
      id: "guided",
      initial: { ...base.initial!, independent: false },
    },
    { ...base, id: "practice", initial: { ...base.initial!, transfer: false } },
  ];
  assert.deepEqual(summarizeReport(rows).transfer, {
    numerator: 1,
    denominator: 1,
    percent: 100,
  });
  assert.equal(summarizeReport(rows).help.denominator, 5);
});
test("기간 경계와 학급 합산은 문항 수를 기준으로 계산하고 0점을 채점으로 인정한다", () => {
  const rows = [
    {
      ...base,
      id: "start",
      date: "2026-10-08",
      rubric: [0, 0, 0, 0] as [number, number, number, number],
    },
    ...Array.from({ length: 3 }, (_, i) => ({
      ...base,
      id: `x${i}`,
      learnerId: "two",
      initial: { ...base.initial!, choiceCorrect: true },
    })),
    { ...base, id: "outside", date: "2026-10-07" },
  ];
  const s = summarizeReport(rows, "2026-10-08", "2026-10-14");
  assert.equal(s.answer.percent, 75);
  assert.equal(s.answer.denominator, 4);
  assert.equal(s.reviewed, 4);
  assert.equal(s.rubricAverage, 4.5);
  assert.equal(validRubric([2, 2, 2, 3]), false);
  assert.equal(validRubric([2, 2, "", 2]), false);
});
test("실제 학습의 수정 제출과 최근 교사 확인은 최초 정답·전이 확인을 덮어쓰지 않는다", () => {
  const a = createJourneyAttempt("report", "2026-10-14T00:00:00Z");
  const first = {
    id: "s1",
    at: a.createdAt,
    evidence: ["quote"],
    answer: "처음 답",
    reason: "이유",
    helpLevel: 0,
    passageId: "test",
    passageVersion: 1,
    evidenceQuotes: { quote: "본문" },
    support: "independent" as const,
    exposure: "new" as const,
    evidenceMatch: false,
  };
  a.responses.transfer = {
    answer: "수정",
    reason: "이유",
    evidence: [],
    helpLevel: 0,
    submissions: [
      first,
      {
        ...first,
        id: "s2",
        answer: "고친 답",
        exposure: "practiced",
        evidenceMatch: true,
        review: { outcome: "success", note: "수정 확인", at: a.createdAt },
      },
    ],
  };
  const s = summarizeReport(journeyReportRecords(a));
  assert.equal(s.evidence.percent, 0);
  assert.equal(s.transferPending, 1);
  assert.equal(s.transfer.percent, null);
  assert.equal(s.corrections, 1);
  assert.equal(s.answer.percent, null);
});
test("가상 원장의 합산·교사 채점·공개 후 학부모 점수는 같은 기록으로 계산한다", () => {
  const student = demoStudents[2],
    period = reportPeriods[0],
    store = useDemoAcademy.getState();
  useDemoAcademy.setState({ reviews: {}, releases: {} });
  const all = demoReportRecords();
  assert.equal(new Set(all.map((r) => r.id)).size, 24 * 32);
  const before = summarizeReport(
    demoReportRecords([student]),
    period.start,
    period.end,
  );
  assert.equal(
    store.saveReview(student.id, "조건을 확인함", "근거 설명", [2, 2, 2, 2]),
    true,
  );
  const reviews = useDemoAcademy.getState().reviews;
  const teacher = demoReportRecords([student], reviews).find(
    (r) => r.id === todayRecordId(student),
  )!;
  const parentBefore = demoReportRecords([student], reviews, {}, "parent").find(
    (r) => r.id === todayRecordId(student),
  )!;
  assert.deepEqual(teacher.rubric, [2, 2, 2, 2]);
  assert.equal(parentBefore.rubric, null);
  assert.equal(store.releaseReport(student.id), true);
  const releases = useDemoAcademy.getState().releases;
  assert.deepEqual(
    demoReportRecords([student], reviews, releases, "parent"),
    demoReportRecords([student], reviews, releases),
  );
  const after = summarizeReport(
    demoReportRecords([student], reviews),
    period.start,
    period.end,
  );
  assert.equal(after.reviewed, before.reviewed + 1);
  assert.deepEqual(after.evidence, before.evidence);
  assert.deepEqual(after.transfer, before.transfer);
});
test("CSV는 화면 원장의 건수와 일치하고 누락과 0점을 구분한다", () => {
  const csv = reportCsv(
    [base, { ...base, id: "b", initial: null, rubric: null }],
    { one: '가상 "학생"' },
  );
  assert.equal(csv.split("\r\n").length, 3);
  assert.match(csv, /가상 ""학생""/);
  assert.match(csv, /가상 예시/);
  assert.match(csv, /첫 선택 정답/);
});
test("기본 예시 채점도 공개 전에는 학부모 평균에 포함하지 않는다", () => {
  const student = demoStudents[3];
  assert.equal(student.reviewed, true);
  assert.equal(student.published, false);
  const teacher = demoReportRecords([student]).find(
    (r) => r.id === todayRecordId(student),
  )!;
  const parent = demoReportRecords([student], {}, {}, "parent").find(
    (r) => r.id === todayRecordId(student),
  )!;
  assert.deepEqual(teacher.rubric, [2, 2, 1, 2]);
  assert.equal(parent.rubric, null);
});
