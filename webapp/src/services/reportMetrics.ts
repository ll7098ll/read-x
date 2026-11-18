import type { JourneyAttempt } from "./learningJourney";
import { journeyTasks, type TaskId } from "../data/learningJourney";

export type Rubric = [number, number, number, number];
export const rubricCriteria = [
  {
    name: "단서 찾기",
    levels: [
      "무관한 근거 또는 근거 없음",
      "필요한 근거 중 일부 제시",
      "질문에 필요한 근거를 모두 제시",
    ],
  },
  {
    name: "관계 연결",
    levels: [
      "근거와 답의 관계를 설명하지 못함",
      "관계를 언급하지만 이유가 불충분",
      "근거가 답을 뒷받침하는 이유를 설명",
    ],
  },
  {
    name: "조건 확인",
    levels: [
      "질문의 핵심 조건을 놓침",
      "일부 조건만 반영",
      "질문의 조건과 대상을 모두 반영",
    ],
  },
  {
    name: "자기 설명",
    levels: [
      "핵심 내용 오류 또는 설명 없음",
      "핵심은 맞지만 설명이 불완전",
      "핵심을 왜곡 없이 자기 문장으로 설명",
    ],
  },
];
export const validRubric = (value: unknown): value is Rubric =>
  Array.isArray(value) &&
  value.length === 4 &&
  value.every((v) => Number.isInteger(v) && v >= 0 && v <= 2);
export type ReportRecord = {
  id: string;
  learnerId: string;
  date: string;
  title: string;
  goal: string;
  initial: null | {
    choiceCorrect: boolean | null;
    evidenceCorrect: boolean | null;
    hints: number;
    independent: boolean;
    fresh: boolean;
    transfer: boolean;
    confirmed: boolean | null;
  };
  rubric: Rubric | null;
  revised: boolean;
};
export type Ratio = {
  numerator: number;
  denominator: number;
  percent: number | null;
};
export const ratio = (numerator: number, denominator: number): Ratio => ({
  numerator,
  denominator,
  percent: denominator ? Math.round((numerator / denominator) * 100) : null,
});
export const percentText = (r: Ratio) =>
  r.percent === null ? "—" : `${r.percent}%`;
export function summarizeReport(
  input: ReportRecord[],
  start = "",
  end = "9999-12-31",
) {
  const seen = new Set<string>();
  const rows = input.filter((r) => {
    const key = `${r.learnerId}:${r.id}`;
    if (r.date < start || r.date > end || seen.has(key)) return false;
    seen.add(key);
    return true;
  });
  const submitted = rows.filter((r) => r.initial);
  const choice = submitted.filter(
    (r) => typeof r.initial!.choiceCorrect === "boolean",
  );
  const evidence = submitted.filter(
    (r) => typeof r.initial!.evidenceCorrect === "boolean",
  );
  const transfer = submitted.filter(
    (r) =>
      r.initial!.transfer &&
      r.initial!.fresh &&
      r.initial!.independent &&
      r.initial!.hints === 0,
  );
  const transferReviewed = transfer.filter(
    (r) => typeof r.initial!.confirmed === "boolean",
  );
  const scored = submitted.filter((r) => validRubric(r.rubric));
  const criterionAverages = rubricCriteria.map((_, i) =>
    scored.length
      ? scored.reduce((n, r) => n + r.rubric![i], 0) / scored.length
      : null,
  );
  return {
    rows,
    submitted: submitted.length,
    assigned: rows.length,
    learners: new Set(rows.map((r) => r.learnerId)).size,
    completion: ratio(submitted.length, rows.length),
    answer: ratio(
      choice.filter((r) => r.initial!.choiceCorrect).length,
      choice.length,
    ),
    evidence: ratio(
      evidence.filter((r) => r.initial!.evidenceCorrect).length,
      evidence.length,
    ),
    help: ratio(
      submitted.filter((r) => r.initial!.hints > 0).length,
      submitted.length,
    ),
    independent: ratio(
      submitted.filter((r) => r.initial!.independent && r.initial!.hints === 0)
        .length,
      submitted.length,
    ),
    transfer: ratio(
      transferReviewed.filter((r) => r.initial!.confirmed).length,
      transferReviewed.length,
    ),
    transferPending: transfer.length - transferReviewed.length,
    reviewed: scored.length,
    pending: submitted.length - scored.length,
    rubricAverage: scored.length
      ? scored.reduce((n, r) => n + r.rubric!.reduce((a, b) => a + b, 0), 0) /
        scored.length
      : null,
    criterionAverages,
    corrections: submitted.filter((r) => r.revised).length,
  };
}
export type ReportSummary = ReturnType<typeof summarizeReport>;
/** Historical first submissions remain the unit of initial accuracy and transfer, even after correction. */
export function journeyReportRecords(attempt: JourneyAttempt): ReportRecord[] {
  return (Object.keys(journeyTasks) as TaskId[]).map((task) => {
    const submissions = attempt.responses[task]?.submissions || [],
      first = submissions[0];
    return {
      id: `${attempt.id}:${task}`,
      learnerId: "local-practice",
      date: (first?.at || attempt.createdAt).slice(0, 10),
      title: journeyTasks[task].target,
      goal: task,
      initial: first
        ? {
            choiceCorrect: null,
            evidenceCorrect: first.evidenceMatch,
            hints: first.helpLevel,
            independent: first.support === "independent",
            fresh: first.exposure === "new",
            transfer: task === "transfer",
            confirmed: first.review ? first.review.outcome === "success" : null,
          }
        : null,
      rubric: null,
      revised: submissions.length > 1,
    };
  });
}

export function reportCsv(
  rows: ReportRecord[],
  names: Record<string, string> = {},
) {
  const cell = (v: unknown) => `"${String(v ?? "").replace(/"/g, '""')}"`;
  const yes = (v: boolean | null | undefined) =>
    typeof v === "boolean" ? (v ? "1" : "0") : "";
  return (
    "\uFEFF" +
    [
      [
        "자료구분",
        "활동ID",
        "학생",
        "날짜",
        "활동",
        "목표",
        "제출",
        "첫 선택 정답",
        "첫 근거 일치",
        "첫 응답 도움 수",
        "처음 보는 글",
        "독립 조건",
        "전이 확인",
        "첫 수행 교사 확인",
        "수정 있음",
        ...rubricCriteria.map((c) => c.name + "(0~2)"),
      ],
      ...rows.map((r) => [
        "가상 예시",
        r.id,
        names[r.learnerId] || r.learnerId,
        r.date,
        r.title,
        r.goal,
        r.initial ? 1 : 0,
        yes(r.initial?.choiceCorrect),
        yes(r.initial?.evidenceCorrect),
        r.initial?.hints,
        yes(r.initial?.fresh),
        yes(r.initial?.independent),
        yes(r.initial?.transfer),
        yes(r.initial?.confirmed),
        r.revised ? 1 : 0,
        ...(r.rubric || ["", "", "", ""]),
      ]),
    ]
      .map((row) => row.map(cell).join(","))
      .join("\r\n")
  );
}
