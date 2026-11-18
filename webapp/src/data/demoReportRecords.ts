import {
  demoStudents,
  demoLesson,
  type DemoStudent,
  type DemoReview,
} from "./demoAcademy";
import {
  validRubric,
  type Rubric,
  type ReportRecord,
} from "../services/reportMetrics";

export const reportPeriods = [
  {
    id: "week",
    label: "최근 7일",
    start: "2026-10-08",
    end: "2026-10-14",
    previousStart: "2026-10-01",
    previousEnd: "2026-10-07",
  },
  {
    id: "previous",
    label: "직전 7일",
    start: "2026-10-01",
    end: "2026-10-07",
    previousStart: "2026-09-24",
    previousEnd: "2026-09-30",
  },
  {
    id: "month",
    label: "최근 4주",
    start: "2026-09-17",
    end: "2026-10-14",
    previousStart: "",
    previousEnd: "",
  },
];
export const reportWeeks = [
  { label: "9/17–23", start: "2026-09-17", end: "2026-09-23" },
  { label: "9/24–30", start: "2026-09-24", end: "2026-09-30" },
  { label: "10/1–7", start: "2026-10-01", end: "2026-10-07" },
  { label: "10/8–14", start: "2026-10-08", end: "2026-10-14" },
];
export const baselineRubric = (s: DemoStudent): Rubric | null =>
  s.reviewed ? [2, 2, 1, 2] : null;
export const todayRecordId = (s: DemoStudent) => `${s.id}:w3:a7`;
/** Deterministic synthetic event log; every report number is calculated from these rows. */
export function demoReportRecords(
  students = demoStudents,
  reviews: Record<string, DemoReview> = {},
  releases: Record<string, boolean> = {},
  audience: "teacher" | "parent" = "teacher",
): ReportRecord[] {
  return students.flatMap((s) => {
    const index = demoStudents.findIndex((x) => x.id === s.id),
      lesson = demoLesson(s);
    return reportWeeks.flatMap((week, w) =>
      Array.from({ length: 8 }, (_, j) => {
        const today = w === 3 && j === 7;
        const day = new Date(week.start + "T12:00:00Z");
        day.setUTCDate(day.getUTCDate() + Math.min(j, 6));
        const submitted = today
          ? s.status === "submitted"
          : j < (w === 3 ? 5 + (index % 2) : 5 + ((index + w) % 3));
        const seed = (index * 3 + j * 2 + w) % 9,
          helped = j < 2 && (index + w) % 3 !== 0;
        const fresh = j >= 3,
          independent = !helped && j >= 2,
          transfer = j >= 4;
        const rubric: Rubric = [
          seed < 6 ? 2 : 1,
          seed < 3 + w ? 2 : 1,
          seed < 5 ? 2 : 0,
          seed < 4 + w ? 2 : 1,
        ];
        const firstConfirmed =
          (j + index) % 5 === 0 ? null : rubric.every((v) => v === 2);
        const canReadToday =
          audience === "teacher" || s.published || releases[s.id];
        const saved = reviews[s.id]?.rubric;
        const grade = today
          ? !canReadToday
            ? null
            : validRubric(saved)
              ? saved
              : baselineRubric(s)
          : (j + index) % 5 === 0
            ? null
            : rubric;
        return {
          id: `${s.id}:w${w}:a${j}`,
          learnerId: s.id,
          date: day.toISOString().slice(0, 10),
          title: today
            ? lesson.title
            : `${s.grade}학년 읽기 · ${j < 4 ? "근거 연습" : "새 글 적용"} ${j + 1}`,
          goal: lesson.goalId,
          initial: submitted
            ? {
                choiceCorrect: today || j % 3 === 2 ? null : seed < 4 + w,
                evidenceCorrect: today ? false : seed < 5 + w,
                hints: today
                  ? s.help === "도움 없이"
                    ? 0
                    : 1
                  : helped
                    ? 1 + (j % 2)
                    : 0,
                independent: today ? s.help === "도움 없이" : independent,
                fresh: today ? false : fresh,
                transfer: today ? false : transfer,
                confirmed: today ? null : firstConfirmed,
              }
            : null,
          rubric: submitted ? grade : null,
          revised: submitted && (today || seed >= 5),
        };
      }),
    );
  });
}
