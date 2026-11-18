import { ExamEntryCard } from "../exam/ExamEntryCard";
import { enterExam } from "../../services/examNavigation";
import { TeacherQuantifiedReport } from "../common/QuantifiedReport";
import {
  DemoContext,
  TeacherDemoOverview,
  TeacherDemoReview,
  TeacherDemoRoster,
} from "../common/AcademyDemo";
import { useDemoAcademy } from "../../store/useDemoAcademy";
import { demoStudents, demoMetrics } from "../../data/demoAcademy";
import { CurriculumLibrary } from "../common/CurriculumLibrary";
import { PracticeOverview, ThinkingPortfolio, useThinkingPending } from "../common/ThinkingPortfolio";
import { LearningIllustration } from "../brand/LearningIllustration";
import React, { useState } from "react";
import {
  ArrowRight,
  BookOpen,
  Search,
  Plus,
  Users,
  NotebookPen,
  LibraryBig,
  Check,
  Eye,
} from "lucide-react";
import type {
  CommercialMasterData,
  SlotLessonPackage,
} from "../../types/courseware";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { usePracticeState } from "../../store/useReadingWorkspace";
import { PageHeading, EmptyState, Dialog } from "../common/DesignSystem";
import { findLesson } from "../../data/lessonCatalog";
import {
  JourneyEntryCard,
  LearningEvidenceReport,
} from "../common/LearningEvidenceReport";
import { useLearningJourney } from "../../store/useLearningJourney";

function ReviewNote({ draftKey, text }: { draftKey: string; text: string }) {
  const lesson = findLesson(draftKey.split(":")[0]);
  const [comment, setComment] = usePracticeState(
    draftKey.split(":")[0],
    "review:" + draftKey,
    "",
  );
  const [saved, setSaved] = useState(false);
  return (
    <article className="rx-draft">
      <div className="rx-list-heading">
        <h3>
          {lesson && "real_csat_test" in lesson
            ? lesson.real_csat_test.passage_title
            : "생각 연습"}
        </h3>
        <span className="rx-badge">기기 내 초안</span>
      </div>
      <blockquote className="rx-response-quote">{text}</blockquote>
      <label className="rx-field">
        검토 메모
        <textarea
          value={comment}
          onChange={(e) => {
            setComment(e.target.value);
            setSaved(false);
          }}
          placeholder="학생이 찾은 근거와 연결한 이유를 살펴보고 메모하세요."
          rows={3}
        />
      </label>
      <button className="rx-button" onClick={() => setSaved(true)}>
        <Check size={16} />
        {saved ? "메모를 보관했어요" : "기기에 메모 보관"}
      </button>
      <p className="rx-fine-print">
        메모는 이 기기에 자동 보관됩니다. 학생에게 전송되지 않습니다.
      </p>
    </article>
  );
}
export function TeacherJourneyHub({ data }: { data: CommercialMasterData }) {
  const {
    assignments,
    responseDrafts,
    assignTaskToStudent,
    selectGradeAndSlot,
    setActiveRole,
  } = useCoursewareStore();
  const [tab, setTab] = useState(useDemoAcademy.getState().teacherView),
    [query, setQuery] = useState(""),
    [grade, setGrade] = useState(3);
  const [selected, setSelected] = useState<SlotLessonPackage | null>(null);
  const [note, setNote] = useState(
    "글에서 찾은 근거와 그 이유를 내 말로 설명해 보세요.",
  );
  const [message, setMessage] = useState("");
  const demoState = useDemoAcademy();
  const demoPending = demoMetrics(demoStudents, demoState.reviews).pending;
  const journeyAttempts = useLearningJourney((s) => s.attempts);
  const thinkingPending = useThinkingPending();
  const journeyPending = journeyAttempts
    .flatMap((a) => Object.values(a.responses))
    .filter(
      (r) => r.submissions.length && !r.submissions.slice(-1)[0].review,
    ).length;
  const journeyHasRecords = journeyAttempts.some((a) =>
    Object.values(a.responses).some((r) => r.submissions.length),
  );
  const roster = data.teacher_class_roster || [];
  const drafts = Object.entries(responseDrafts).filter(([, text]) =>
    text.trim(),
  );
  const lessons = (data.expository_slots_96 || []).filter(
    (s) =>
      s.grade_num === grade &&
      (
        s.real_csat_test.passage_title +
        s.sub_skill_name +
        s.curriculum_concept.subject
      ).includes(query),
  );
  const preview = (slot: SlotLessonPackage) => {
    selectGradeAndSlot(slot.grade_num, slot.slot_id, "studio");
    setActiveRole("student");
    window.scrollTo(0, 0);
  };
  const assign = () => {
    if (!selected) return;
    const ok = assignTaskToStudent({
      title: selected.real_csat_test.passage_title,
      slotId: selected.slot_id,
      type: "reading",
      assignedBy: "체험 선생님",
      dueDate: "체험 과제",
      trapWarning: note,
    });
    if (ok) {
      setMessage("이 기기의 학생 체험 과제함에 수업을 추가했습니다.");
      setSelected(null);
    } else
      setMessage(
        "이 자료를 추가할 수 없습니다. 게시 상태와 수업 코드를 확인해 주세요.",
      );
  };
  return (
    <div className="rx-teacher-page">
      <PageHeading
        eyebrow="선생님 수업실"
        title="좋은 수업은, 생각을 살피는 일"
        description="수업을 준비하고 학생이 남긴 근거와 설명을 함께 살펴보세요."
        action={
          <button
            className="rx-button rx-button-primary"
            onClick={() => setTab("library")}
          >
            <Plus size={18} />
            수업 준비하기
          </button>
        }
      />
      <nav className="rx-tabs" aria-label="교사 메뉴">
        {[
          ["today", "오늘 수업"],
          ["exams", "모의고사 운영"],
          ["library", "수업 준비"],
          ["review", "학생 응답 검토"],
          ["reports", "학습 리포트"],
          ["class", "우리 반"],
        ].map(([id, label]) => (
          <button
            key={id}
            aria-current={tab === id ? "page" : undefined}
            onClick={() => id === "exams" ? enterExam("teacher") : setTab(id)}
          >
            <LearningIllustration kind={id} />
            {label}
            {id === "review" && thinkingPending > 0 && <span>{thinkingPending}</span>}
          </button>
        ))}
      </nav>
      <details className="workspace-exam-shortcut"><summary>모의고사 운영 바로가기</summary><ExamEntryCard role="teacher"/></details>
      {tab === "curriculum" && <CurriculumLibrary />}
      {tab === "reports" && <><ThinkingPortfolio audience="teacher"/><details className="rx-demo-secondary"><summary>가상 학급의 기간별 리포트 예시</summary><TeacherQuantifiedReport /></details></>}
      {message && (
        <p className="rx-success" role="status">
          <Check size={18} />
          {message}
          <button onClick={() => setMessage("")} aria-label="알림 닫기">
            ×
          </button>
        </p>
      )}
      {tab === "today" && (
        <>
          <PracticeOverview onReview={()=>setTab("review")}/>
          <JourneyEntryCard />
          <details className="rx-demo-secondary"><summary>가상 학급 수업 운영 예시 보기</summary><DemoContext role="teacher"/><TeacherDemoOverview onTab={setTab} /></details>
        </>
      )}
      {tab === "library" && (
        <section className="rx-surface rx-records">
          <div className="rx-section-title">
            <div>
              <p className="rx-eyebrow">LESSON LIBRARY</p>
              <h2>다음 수업을 골라보세요</h2>
            </div>
            <span className="rx-badge">{lessons.length}개 자료</span>
          </div>
          <div className="rx-next-route"><div><h3>사고 시범과 교과 지문을 함께 준비해요</h3><p>읽기 방법을 먼저 살펴보고, 학생에게 맞는 소재와 활동을 고르세요.</p></div><button className="rx-button" onClick={()=>setTab("curriculum")}>교과 지문 찾기 <ArrowRight size={16}/></button></div>
          <JourneyEntryCard/>
          <div className="rx-filter-bar">
            <label className="rx-field">
              학년
              <select
                value={grade}
                onChange={(e) => setGrade(Number(e.target.value))}
              >
                {[1, 2, 3, 4, 5, 6].map((g) => (
                  <option key={g} value={g}>
                    {g}학년
                  </option>
                ))}
              </select>
            </label>
            <label className="rx-search">
              <Search size={18} />
              <input
                aria-label="교사 수업 자료 검색"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="제목, 교과 또는 읽기 목표 검색"
              />
            </label>
          </div>
          <div className="rx-course-grid">
            {lessons.map((s) => (
              <article className="rx-course-card" key={s.slot_id}>
                <span className="rx-badge">{s.curriculum_concept.subject}</span>
                <h3>{s.real_csat_test.passage_title}</h3>
                <p>{s.sub_skill_name}</p>
                <div className="rx-course-actions">
                  <button className="rx-button" onClick={() => preview(s)}>
                    <Eye size={16} />
                    학생 화면
                  </button>
                  <button
                    className="rx-button rx-button-primary"
                    onClick={() => setSelected(s)}
                  >
                    <Plus size={16} />
                    과제 추가
                  </button>
                </div>
              </article>
            ))}
          </div>
          {lessons.length === 0 && (
            <EmptyState
              title="검색 결과가 없습니다"
              description="학년이나 검색어를 바꿔보세요."
            />
          )}
        </section>
      )}
      {tab === "review" && (
        <>
          <ThinkingPortfolio audience="teacher" />
          <details className="rx-demo-secondary"><summary>가상 학생의 검토·공개 흐름 예시</summary><TeacherDemoReview /></details>
          <details className="ad-local-records">
            <summary>이 기기에서 직접 작성한 연습 기록</summary>
            {drafts.map(([key, text]) => (
              <ReviewNote key={key} draftKey={key} text={text} />
            ))}
          </details>
        </>
      )}
      {tab === "class" && (
        <TeacherDemoRoster onReview={() => setTab("review")} />
      )}
      {selected && (
        <Dialog title="체험 과제 추가" onClose={() => setSelected(null)}>
          <span className="rx-badge">{selected.grade}</span>
          <h3 className="rx-dialog-title">
            {selected.real_csat_test.passage_title}
          </h3>
          <p className="rx-muted">{selected.sub_skill_name}</p>
          <label className="rx-field">
            수업 안내
            <textarea
              rows={3}
              value={note}
              onChange={(e) => setNote(e.target.value)}
            />
          </label>
          <p className="rx-inline-note">
            이 기기의 학생 체험 과제함에 추가됩니다. 실제 학생에게 배정하거나
            전송하지 않습니다.
          </p>
          <div className="rx-dialog-actions">
            <button className="rx-button" onClick={() => setSelected(null)}>
              취소
            </button>
            <button className="rx-button rx-button-primary" onClick={assign}>
              체험 과제함에 추가 <ArrowRight size={16} />
            </button>
          </div>
        </Dialog>
      )}
    </div>
  );
}
