import lessonSamples from "./academyLessonSamples.json";
import type { Rubric } from "../services/reportMetrics";

export const DEMO_DATE = "2026.10.14 수요일";
export const demoAcademy = {
  name: "리드엑스 생각숲 학원",
  branch: "서초 캠퍼스",
  label: "가상 학원",
};
export const demoClasses = [
  {
    id: "sprout",
    name: "새싹 읽기반",
    grade: 3,
    teacher: "김서현",
    time: "14:00",
    room: "생각 1실",
    goal: "글에 나온 사실 찾기",
  },
  {
    id: "connect",
    name: "생각 연결반",
    grade: 4,
    teacher: "이도윤",
    time: "15:00",
    room: "생각 2실",
    goal: "앞뒤 내용을 연결하기",
  },
  {
    id: "explore",
    name: "탐구 읽기반",
    grade: 5,
    teacher: "김서현",
    time: "16:00",
    room: "생각 1실",
    goal: "과정과 원인 설명하기",
  },
  {
    id: "leap",
    name: "도약 표현반",
    grade: 6,
    teacher: "박지우",
    time: "17:00",
    room: "생각 2실",
    goal: "조건과 근거 비교하기",
  },
];
export type DemoStudent = {
  id: string;
  name: string;
  classId: string;
  grade: number;
  status: "submitted" | "learning" | "scheduled";
  reviewed: boolean;
  published: boolean;
  attendance: "present" | "late" | "expected";
  focus: string;
  help: string;
  initialAnswer: string;
  revisedAnswer: string;
  teacherNote: string;
};
const names = [
  "김하린",
  "이서준",
  "박지안",
  "최민재",
  "정소율",
  "윤도현",
  "김지호",
  "이서아",
  "박시우",
  "최예린",
  "정도윤",
  "윤하윤",
  "김민준",
  "이윤서",
  "박서진",
  "최수아",
  "정지후",
  "윤채원",
  "김현우",
  "이유나",
  "박준서",
  "최다은",
  "정시윤",
  "윤서연",
];
const initialAnswers = [
  "물체와 물질은 둘 다 물건을 부르는 말이에요.",
  "자석이 서로 가까워졌다는 뜻이에요.",
  "모래와 소금이 모두 거름종이에 남았어요.",
  "봉지 안에 물방울이 생겼다는 뜻이에요.",
];
export const demoStudents: DemoStudent[] = names.map((name, i) => {
  const c = demoClasses[Math.floor(i / 6)],
    lesson = lessonSamples[Math.floor(i / 6)],
    order = i % 6;
  return {
    id: `demo-student-${String(i + 1).padStart(2, "0")}`,
    name,
    classId: c.id,
    grade: c.grade,
    status: order < 4 ? "submitted" : order === 4 ? "learning" : "scheduled",
    reviewed: order === 1 || order === 3,
    published: order === 1,
    attendance: order === 5 ? "expected" : order === 4 ? "late" : "present",
    focus:
      order % 2 === 0
        ? "근거와 설명을 이어 말하기"
        : "새 글에서 스스로 적용하기",
    help: order % 2 === 0 ? "문단 위치 힌트 1회" : "도움 없이",
    initialAnswer: initialAnswers[Math.floor(i / 6)],
    revisedAnswer: lesson.answer,
    teacherNote:
      order % 2 === 0
        ? "관련 문장을 찾은 뒤, 그 문장이 답을 뒷받침하는 이유까지 말해 보았어요. 다음 시간에는 위치 안내 없이 두 근거를 연결해 봅시다."
        : "글의 조건을 놓치지 않고 근거를 연결했어요. 다른 주제에서도 같은 읽기 방법을 스스로 사용해 볼 차례예요.",
  };
});
export const defaultDemoStudentId = "demo-student-14";
export const demoConsultations = [
  {
    id: "consult-1",
    studentId: "demo-student-03",
    date: "10.14",
    time: "18:00",
    topic: "근거는 찾지만 설명을 망설여요",
    note: "정답을 바로 알려주기보다, 아이가 고른 문장에서 질문의 대상을 다시 짚도록 안내합니다.",
  },
  {
    id: "consult-2",
    studentId: "demo-student-14",
    date: "10.15",
    time: "17:30",
    topic: "다음 읽기 목표와 가정 대화",
    note: "익숙한 과학 글에서 사용한 방법을 사회 글에도 적용해 보는 계획을 나눕니다.",
  },
  {
    id: "consult-3",
    studentId: "demo-student-20",
    date: "10.15",
    time: "18:00",
    topic: "내 말로 쓰는 습관 이어가기",
    note: "완성된 문장 수보다 근거가 설명에 들어 있는지 함께 확인합니다.",
  },
];
export const demoStudent = (id: string) =>
  demoStudents.find((s) => s.id === id) ||
  demoStudents.find((s) => s.id === defaultDemoStudentId)!;
export const demoLesson = (student: DemoStudent) =>
  lessonSamples.find((l) => l.grade === student.grade)!;
export type DemoReview = {
  note: string;
  next: string;
  savedAt: string;
  rubric?: Rubric;
};
export function demoMetrics(
  students: DemoStudent[],
  reviews: Record<string, DemoReview> = {},
  releases: Record<string, boolean> = {},
) {
  const submitted = students.filter((s) => s.status === "submitted");
  return {
    total: students.length,
    present: students.filter((s) => s.attendance !== "expected").length,
    completed: submitted.length,
    pending: submitted.filter((s) => !s.reviewed && !reviews[s.id]).length,
    shared: students.filter((s) => releases[s.id] || s.published).length,
    reviewed: submitted.filter((s) => s.reviewed || reviews[s.id]).length,
  };
}
