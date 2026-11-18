import { RubricProfile } from "./QuantifiedReport";
import {
  demoReportRecords,
  reportPeriods,
  baselineRubric,
} from "../../data/demoReportRecords";
import {
  summarizeReport,
  rubricCriteria,
  validRubric,
  type Rubric,
} from "../../services/reportMetrics";
import React, { useState } from "react";
import {
  ArrowRight,
  Check,
  CalendarDays,
  MessageCircle,
  BookOpen,
  Clock3,
  Users,
  FileCheck2,
} from "lucide-react";
import {
  demoAcademy,
  demoClasses,
  demoStudents,
  demoStudent,
  demoLesson,
  demoMetrics,
  DEMO_DATE,
  type DemoStudent,
} from "../../data/demoAcademy";
import { useDemoAcademy } from "../../store/useDemoAcademy";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { useReadingStorageStatus } from "../../store/useReadingWorkspace";
import { LearningIllustration } from "../brand/LearningIllustration";
import type { RoleType } from "../../types/courseware";

export function DemoContext({
  role,
}: {
  role: "director" | "teacher" | "parent";
}) {
  const setRole = useCoursewareStore((s) => s.setActiveRole);
  return (
    <section className="ad-context no-print">
      <div>
        <span className="ad-demo-label">운영 체험 · 예시 데이터</span>
        <b>{demoAcademy.name}</b>
        <p>
          가상 학생 24명의 수업·피드백·리포트가 연결되어 있어요. {DEMO_DATE}{" "}
          기준
        </p>
      </div>
      <label>
        다른 역할로 보기
        <select
          aria-label="운영 체험 역할"
          value={role}
          onChange={(e) => setRole(e.target.value as RoleType)}
        >
          <option value="director">학원 원장</option>
          <option value="teacher">담당 교사</option>
          <option value="parent">학부모</option>
        </select>
      </label>
    </section>
  );
}
export function DemoClassPicker() {
  const { selectedClassId, selectClass } = useDemoAcademy();
  return (
    <label className="ad-picker">
      살펴볼 반
      <select
        aria-label="예시 반 선택"
        value={selectedClassId}
        onChange={(e) => selectClass(e.target.value)}
      >
        {demoClasses.map((c) => (
          <option key={c.id} value={c.id}>
            {c.name} · {c.grade}학년 · {c.teacher} 선생님
          </option>
        ))}
      </select>
    </label>
  );
}
export function DemoStatus({ student: s }: { student: DemoStudent }) {
  const reviews = useDemoAcademy((x) => x.reviews);
  const reviewed = s.reviewed || !!reviews[s.id];
  return (
    <span
      className={`ad-status ${s.status === "submitted" ? (reviewed ? "is-done" : "is-review") : "is-wait"}`}
    >
      {s.status === "submitted"
        ? reviewed
          ? "검토 완료"
          : "검토 필요"
        : s.status === "learning"
          ? "학습 중"
          : "수업 예정"}
    </span>
  );
}
export function DemoMetrics({
  students = demoStudents,
}: {
  students?: DemoStudent[];
}) {
  const { reviews, releases } = useDemoAcademy();
  const m = demoMetrics(students, reviews, releases);
  return (
    <div className="ad-metrics">
      {[
        [
          Users,
          "오늘의 출석",
          `${m.present} / ${m.total}`,
          "예시 출석부 · 지각 포함",
        ],
        [
          BookOpen,
          "응답 제출",
          `${m.completed} / ${m.total}`,
          "오늘 배정된 수업 기준",
        ],
        [
          FileCheck2,
          "교사 검토 대기",
          `${m.pending}명`,
          "답과 근거를 함께 확인해요",
        ],
        [
          MessageCircle,
          "리포트 공개",
          `${m.shared}명`,
          "학부모 체험 화면에 연결",
        ],
      ].map(([Icon, label, value, sub]: any) => (
        <article key={label}>
          <div>
            <Icon size={19} />
            {label}
          </div>
          <strong>{value}</strong>
          <p>{sub}</p>
        </article>
      ))}
    </div>
  );
}
export function DemoStudentList({
  students,
  onSelect,
  selectedId,
}: {
  students: DemoStudent[];
  onSelect: (s: DemoStudent) => void;
  selectedId?: string;
}) {
  return (
    <div className="ad-student-list">
      {students.map((s) => (
        <button
          key={s.id}
          onClick={() => onSelect(s)}
          aria-pressed={selectedId === s.id}
          className={selectedId === s.id ? "is-selected" : ""}
        >
          <span className={`ad-avatar tone-${s.grade}`}>{s.name.slice(1)}</span>
          <span className="ad-student-name">
            <b>{s.name}</b>
            <small>
              {s.grade}학년 · {s.focus}
            </small>
          </span>
          <DemoStatus student={s} />
          <ArrowRight size={15} />
        </button>
      ))}
    </div>
  );
}
export function DemoStageProfile({ student: s }: { student: DemoStudent }) {
  const { reviews, releases } = useDemoAcademy();
  const p = reportPeriods[0];
  return (
    <RubricProfile
      summary={summarizeReport(
        demoReportRecords([s], reviews, releases),
        p.start,
        p.end,
      )}
    />
  );
}
export function DemoEvidence({ student: s }: { student: DemoStudent }) {
  const lesson = demoLesson(s);
  return (
    <div className="ad-evidence">
      <p className="rx-eyebrow">
        {lesson.title} · 본문 v{lesson.version}
      </p>
      <h3>{lesson.question}</h3>
      <details className="ad-source-passage">
        <summary>함께 읽은 글 펼쳐보기</summary>
        {lesson.paragraphs.map((paragraph, index) => (
          <p key={index}>
            <b>{index + 1}문단</b> {paragraph}
          </p>
        ))}
      </details>
      <div className="ad-before">
        <span>처음 쓴 설명</span>
        <p>{s.initialAnswer}</p>
      </div>
      <div className="ad-quote">
        <span>다시 살펴본 본문 근거</span>
        <blockquote>“{lesson.evidence}”</blockquote>
      </div>
      <div className="ad-after">
        <span>연습 후 내 말로 설명</span>
        <p>{s.revisedAnswer}</p>
      </div>
      <p className="ad-support">
        연습 과정 예시 · {s.help} · 처음 응답과 수정한 응답을 구분합니다.
      </p>
    </div>
  );
}
export function TeacherDemoOverview({
  onTab,
}: {
  onTab: (tab: string) => void;
}) {
  const { selectedClassId, selectStudent } = useDemoAcademy();
  const cls = demoClasses.find((c) => c.id === selectedClassId)!;
  const students = demoStudents.filter((s) => s.classId === selectedClassId);
  const lesson = demoLesson(students[0]);
  return (
    <>
      <DemoClassPicker />
      <DemoMetrics students={students} />
      <div className="ad-columns">
        <section className="ad-card">
          <div className="ad-section-head">
            <div>
              <p className="rx-eyebrow">TODAY’S CLASS</p>
              <h2>{cls.name}의 읽기 시간</h2>
            </div>
            <span className="ad-status is-done">
              {cls.time} · {cls.room}
            </span>
          </div>
          <div className="ad-lesson-banner">
            <LearningIllustration kind="model" />
            <div>
              <span>
                {cls.grade}학년 과학 · {cls.teacher} 선생님
              </span>
              <h3>{lesson.title}</h3>
              <p>{cls.goal}</p>
            </div>
          </div>
          <DemoStudentList
            students={students}
            onSelect={(s) => {
              selectStudent(s.id);
              onTab("review");
            }}
          />
        </section>
        <aside className="ad-card ad-next">
          <p className="rx-eyebrow">TEACHER’S NEXT STEP</p>
          <h2>
            오늘은 이 생각을
            <br />
            함께 살펴보세요.
          </h2>
          <LearningIllustration kind="guided" />
          <p>
            근거 문장을 찾았더라도, 그 문장이 답과 어떻게 연결되는지 설명했는지
            확인해 주세요.
          </p>
          <div className="ad-task-note">
            <b>검토할 때 세 가지</b>
            <ol>
              <li>처음 쓴 답과 고친 답 비교</li>
              <li>본문 근거와 받은 도움 확인</li>
              <li>다음 글에서 연습할 한 가지 선택</li>
            </ol>
          </div>
          <button
            className="rx-button rx-button-primary"
            onClick={() => onTab("review")}
          >
            학생 응답 검토하기 <ArrowRight size={17} />
          </button>
          <button className="rx-button" onClick={() => onTab("library")}>
            다음 수업 준비하기 <ArrowRight size={17} />
          </button>
        </aside>
      </div>
    </>
  );
}
function ReviewEditor({ student: s }: { student: DemoStudent }) {
  const { reviews, releases, saveReview, releaseReport } = useDemoAcademy();
  const [note, setNote] = useState(reviews[s.id]?.note || s.teacherNote),
    [next, setNext] = useState(reviews[s.id]?.next || s.focus),
    [message, setMessage] = useState("");
  const [ratings, setRatings] = useState<(number | "")[]>(
    reviews[s.id]?.rubric || baselineRubric(s) || ["", "", "", ""],
  );
  const rubricReady = validRubric(ratings);
  const partialRubric = ratings.some((v) => v !== "") && !rubricReady;
  const failed = useReadingStorageStatus((s) => s.failed);
  const reviewed = !!reviews[s.id] || s.reviewed,
    shared = !!releases[s.id] || s.published;
  const openParent = () => {
    useDemoAcademy.getState().selectStudent(s.id);
    useCoursewareStore.getState().setActiveRole("parent");
  };
  const rubricDirty =
    JSON.stringify(ratings) !==
    JSON.stringify(
      reviews[s.id]?.rubric || baselineRubric(s) || ["", "", "", ""],
    );
  const dirty =
    rubricDirty ||
    note !== (reviews[s.id]?.note || s.teacherNote) ||
    next !== (reviews[s.id]?.next || s.focus);
  return (
    <section className="ad-card">
      <div className="ad-section-head">
        <div>
          <p className="rx-eyebrow">STUDENT THINKING RECORD</p>
          <h2>{s.name}의 생각을 살펴봐요</h2>
        </div>
        <DemoStatus student={s} />
      </div>
      {s.status !== "submitted" ? (
        <div className="ad-await">
          <LearningIllustration kind="book" />
          <h3>
            {s.status === "learning"
              ? "지금 읽고 생각을 정리하고 있어요"
              : "아직 수업을 시작하기 전이에요"}
          </h3>
          <p>
            제출된 예시 학생을 선택하면 답·근거·피드백 흐름을 체험할 수
            있습니다.
          </p>
        </div>
      ) : (
        <>
          <DemoEvidence student={s} />
          <fieldset className="qr-score-editor">
            <legend>수정 응답의 기준별 채점 · 각 0~2점</legend>
            <p>
              본문과 학생의 설명을 대조해 판단해 주세요. 네 항목을 모두 선택하면
              설명 점수에 반영됩니다.
            </p>
            <div>
              {rubricCriteria.map((c, i) => (
                <label key={c.name}>
                  {c.name}
                  <select
                    aria-label={`${c.name} 점수`}
                    value={ratings[i]}
                    onChange={(e) => {
                      setRatings((old) =>
                        old.map((v, j) =>
                          i === j
                            ? e.target.value === ""
                              ? ""
                              : Number(e.target.value)
                            : v,
                        ),
                      );
                      setMessage("");
                    }}
                  >
                    <option value="">미채점</option>
                    {c.levels.map((l, n) => (
                      <option key={n} value={n}>
                        {n}점 · {l}
                      </option>
                    ))}
                  </select>
                </label>
              ))}
            </div>
            <strong>
              {rubricReady
                ? `${ratings.reduce<number>((n, v) => n + Number(v), 0)} / 8점`
                : "기준별 채점 대기"}
            </strong>
            {partialRubric && <p>채점하려면 네 항목을 모두 선택해 주세요.</p>}
          </fieldset>
          <div className="ad-review-fields">
            <label className="rx-field">
              학생에게 남길 피드백
              <textarea
                rows={4}
                value={note}
                onChange={(e) => {
                  setNote(e.target.value);
                  setMessage("");
                }}
              />
            </label>
            <label className="rx-field">
              다음 수업의 한 가지 목표
              <select
                value={next}
                onChange={(e) => {
                  setNext(e.target.value);
                  setMessage("");
                }}
              >
                <option>근거와 설명을 이어 말하기</option>
                <option>새 글에서 스스로 적용하기</option>
                <option>질문의 조건을 다시 확인하기</option>
              </select>
            </label>
          </div>
          <div className="ad-actions">
            <button
              className="rx-button rx-button-primary"
              disabled={!note.trim() || partialRubric}
              onClick={() => {
                if (
                  saveReview(
                    s.id,
                    note,
                    next,
                    rubricReady ? (ratings as Rubric) : undefined,
                  )
                )
                  setMessage(
                    "검토를 저장했어요. 이 브라우저의 예시 현황에 반영됩니다.",
                  );
              }}
            >
              <Check size={16} /> 검토 저장
            </button>
            <button
              className="rx-button"
              disabled={!reviewed || dirty || shared}
              onClick={() => {
                if (releaseReport(s.id))
                  setMessage(
                    "학부모 체험 리포트에 반영했어요. 실제 알림은 발송되지 않습니다.",
                  );
              }}
            >
              {shared ? "리포트 반영됨" : "학부모 리포트에 반영"}
            </button>
            <button className="rx-text-link" onClick={openParent}>
              이 학생의 학부모 화면 <ArrowRight size={16} />
            </button>
          </div>
          {message && (
            <p role="status" className="ad-success">
              {message}
            </p>
          )}
          {failed && (
            <p role="alert" className="rx-error">
              기기 저장을 사용할 수 없습니다. 창을 닫기 전에 메모를 복사해
              주세요.
            </p>
          )}
          <p className="rx-fine-print">
            체험용 피드백입니다. 변경 내용은 이 브라우저에서만 보관되며, 실제
            학생·학부모에게 전송되지 않습니다.
          </p>
        </>
      )}
    </section>
  );
}
export function TeacherDemoReview() {
  const { selectedClassId, selectedStudentId, selectStudent, reviews } =
    useDemoAcademy();
  const [pendingOnly, setPendingOnly] = useState(false);
  const students = demoStudents.filter((s) => s.classId === selectedClassId);
  const selected =
    students.find((s) => s.id === selectedStudentId) || students[0];
  const visible = pendingOnly
    ? students.filter(
        (s) => s.status === "submitted" && !s.reviewed && !reviews[s.id],
      )
    : students;
  return (
    <>
      <DemoClassPicker />
      <div className="ad-review-layout">
        <aside className="ad-card">
          <div className="ad-section-head">
            <h2>학생 응답</h2>
            <span>{visible.length}명</span>
          </div>
          <label className="ad-checkbox">
            <input
              type="checkbox"
              checked={pendingOnly}
              onChange={(e) => {
                setPendingOnly(e.target.checked);
                if (e.target.checked) {
                  const firstPending = students.find(
                    (s) =>
                      s.status === "submitted" && !s.reviewed && !reviews[s.id],
                  );
                  if (firstPending) selectStudent(firstPending.id);
                }
              }}
            />{" "}
            검토가 필요한 학생만
          </label>
          <DemoStudentList
            students={visible}
            selectedId={selected.id}
            onSelect={(s) => selectStudent(s.id)}
          />
          {!visible.length && <p>이 반의 검토를 모두 마쳤어요.</p>}
        </aside>
        <ReviewEditor key={selected.id} student={selected} />
      </div>
    </>
  );
}
export function TeacherDemoRoster({ onReview }: { onReview: () => void }) {
  const { selectedClassId, selectStudent } = useDemoAcademy();
  const students = demoStudents.filter((s) => s.classId === selectedClassId);
  return (
    <>
      <DemoClassPicker />
      <section className="ad-card">
        <div className="ad-section-head">
          <div>
            <p className="rx-eyebrow">OUR CLASS</p>
            <h2>이름 너머의 읽기 습관</h2>
          </div>
          <span className="rx-badge">가상 학생 {students.length}명</span>
        </div>
        <div className="ad-roster-grid">
          {students.map((s) => (
            <article key={s.id}>
              <div className="ad-section-head">
                <span className={`ad-avatar tone-${s.grade}`}>
                  {s.name.slice(1)}
                </span>
                <DemoStatus student={s} />
              </div>
              <h3>
                {s.name} <small>{s.grade}학년</small>
              </h3>
              <p>{s.focus}</p>
              <DemoStageProfile student={s} />
              <button
                className="rx-button"
                onClick={() => {
                  selectStudent(s.id);
                  onReview();
                }}
              >
                응답과 피드백 보기 <ArrowRight size={16} />
              </button>
            </article>
          ))}
        </div>
      </section>
    </>
  );
}
