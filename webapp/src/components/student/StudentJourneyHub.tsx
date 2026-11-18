import { ExamEntryCard } from "../exam/ExamEntryCard";
import { enterExam } from "../../services/examNavigation";
import { CurriculumLibrary } from "../common/CurriculumLibrary";
import { ProgressiveReadingEntry } from "./ProgressiveReadingStudio";
import { ThinkingPortfolio, RecentThinkingFeedback } from "../common/ThinkingPortfolio";
import { AssessmentEntryCards } from "./StudentAssessmentHub";
import { useStudentAssessment } from "../../store/useStudentAssessment";
import type { AssessmentView } from "../../types/miniExam";
import { LearningIllustration } from "../brand/LearningIllustration";
import React, { useState } from "react";
import {
  ArrowRight,
  BookOpen,
  Bookmark,
  Check,
  ChevronRight,
  PenLine,
  Sparkles,
  Search,
  Clock3,
  LibraryBig,
} from "lucide-react";
import { findLesson, masterData } from "../../data/lessonCatalog";
import { revisedLessonForSlot } from "../../data/corpusReading";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { useReadingWorkspace } from "../../store/useReadingWorkspace";
import { useLearningJourney } from "../../store/useLearningJourney";
import { JOURNEY_SLOT, JOURNEY_GOAL } from "../../data/learningJourney";
import { PageHeading, EmptyState, ThinkingPath } from "../common/DesignSystem";
import {
  JourneyEntryCard,
  LearningEvidenceReport,
} from "../common/LearningEvidenceReport";
import type {
  GradeData,
  SlotLessonPackage,
  StudentAssignment,
} from "../../types/courseware";
import { VocabDuelArena } from "./VocabDuelArena";
import { GalaxyExpeditionMap } from "./GalaxyExpeditionMap";
import { OnboardingCatModal } from "./OnboardingCatModal";

export function StudentJourneyHub({
  gradeData,
  gradeSlots16,
}: {
  gradeData: GradeData;
  gradeSlots16: SlotLessonPackage[];
}) {
  const {
    assignments,
    selectGradeAndSlot,
    setStudentMode,
    responseDrafts,
    savedVocab,
    removeVocabWord,
    customSlotsById,
  } = useCoursewareStore();
  const { lastSlotId, sessions } = useReadingWorkspace();
  const journeyAttempts = useLearningJourney((s) => s.attempts);
  const [tab, setTab] = useState<"today" | "practice" | "records" | "vocab" | "curriculum">(
    "today",
  );
  const [error, setError] = useState("");
  const [library, setLibrary] = useState(false);
  const [query, setQuery] = useState("");
  const [showVocab, setShowVocab] = useState(false),
    [showGalaxy, setShowGalaxy] = useState(false),
    [showCat, setShowCat] = useState(false);
  const pending = assignments.filter((a) => a.status === "pending");
  const readingTitle = (id:string,fallback:string) => customSlotsById[id] ? fallback : revisedLessonForSlot(id)?.title || fallback;
  const lastLesson =
    lastSlotId && sessions[lastSlotId] ? findLesson(lastSlotId) : null;
  const resume =
    lastLesson && "real_csat_test" in lastLesson
      ? {
          slotId: lastSlotId!,
          title: readingTitle(lastSlotId!,lastLesson.real_csat_test.passage_title),
          type: "reading",
        }
      : undefined;
  const featured = resume || pending[0];
  const drafts = [
    ...Object.entries(responseDrafts),
    ...journeyAttempts
      .filter((a) => a.writing.trim())
      .map(
        (a) =>
          [`${JOURNEY_SLOT}:journey-${a.id}`, a.writing] as [string, string],
      ),
  ].filter(([, value]) => value.trim());
  const open = (id: string, type = "reading") => {
    const lesson = findLesson(id);
    if (!lesson) {
      setError("수업을 찾을 수 없어요. 다른 수업을 선택해 주세요.");
      return;
    }
    setError("");
    selectGradeAndSlot(
      lesson.grade_num,
      id,
      id.includes("-COM-") ? "common" : type === "clinic" ? "clinic" : "studio",
    );
    window.scrollTo(0, 0);
  };
  const taskLabel = (task: Pick<StudentAssignment, "slotId">) =>
    task.slotId.includes("-COM-") ? "기초 생각 연습" : "교과 개념 읽기";
  return (
    <div className="rx-student-home">
      <PageHeading
        eyebrow="나의 배움터"
        title="오늘도, 생각이 자라는 시간"
        description="어디를 보았는지, 왜 그렇게 생각했는지. 오늘의 읽기 방법을 배워요."
        action={
          <label className="rx-home-grade">나의 읽기 학년<select value={gradeData.grade_num} onChange={e=>{const g=Number(e.target.value);const lesson=masterData.expository_slots_96?.find(s=>s.grade_num===g);if(lesson){selectGradeAndSlot(g,lesson.slot_id,"portal");useReadingWorkspace.getState().save("progressive-preferences","grade",g);}}}>{[1,2,3,4,5,6].map(g=><option key={g} value={g}>초등 {g}학년</option>)}</select></label>
        }
      />
      <nav className="rx-tabs" aria-label="배움터 메뉴">
        {[
          ["today", "오늘의 학습"],
          ["practice", "읽기 연습"],
          ["exams", "모의고사"],
          ["records", "내 성장"],
        ].map(([id, label]) => (
          <button
            key={id}
            aria-current={tab === id || (id === "practice" && ["curriculum", "vocab"].includes(tab)) ? "page" : undefined}
            onClick={() => {
              if (id === "exams") { enterExam("student"); } else if (["report", "goals", "history"].includes(id)) {
                useStudentAssessment.getState().setView(id as AssessmentView);
                setStudentMode("assessment");
              } else setTab(id as typeof tab);
            }}
          >
            <LearningIllustration kind={id} />
            {label}
            {id === "vocab" && savedVocab.length > 0 && (
              <span>{savedVocab.length}</span>
            )}
          </button>
        ))}
      </nav>
      {["practice", "curriculum", "vocab"].includes(tab) && <nav className="rx-subnav" aria-label="읽기 연습 종류">{[["practice","읽는 방법 연습"],["curriculum","교과 글 찾기"],["vocab","내 단어장"]].map(([id,label])=><button key={id} aria-pressed={tab===id} onClick={()=>setTab(id as typeof tab)}>{label}{id==="vocab"&&savedVocab.length>0?` · ${savedVocab.length}`:""}</button>)}</nav>}
      {tab === "practice" && <><ProgressiveReadingEntry/><section className="rx-practice-guide"><span className="rx-eyebrow">읽기 방법을 내 것으로</span><h2>표시한 구절에서, 이유가 있는 설명으로.</h2><p>같은 글을 여러 방법으로 읽어 보고, 어려웠던 부분은 필요한 도움과 함께 다시 연습해요.</p><ThinkingPath/><button className="rx-button" onClick={()=>setTab("curriculum")}>내 학년에 맞는 글 찾기 <ArrowRight size={16}/></button></section><JourneyEntryCard/></>}
      {tab === "curriculum" && <CurriculumLibrary />}
      {error && (
        <p className="rx-error" role="alert">
          {error}
        </p>
      )}
      {tab === "records" && <><nav className="rx-subnav" aria-label="내 성장 살펴보기"><button aria-pressed="true">생각 기록</button>{[["goals","목표와 다음 확인"],["report","평가 결과"],["history","학습이력"]].map(([view,label])=><button key={view} onClick={()=>{useStudentAssessment.getState().setView(view as AssessmentView);setStudentMode("assessment");}}>{label}</button>)}</nav><ThinkingPortfolio audience="student"/></>}
      {tab === "today" && (
        <>
          <section className="garden-welcome" aria-labelledby="today-reading-title">
            <div className="garden-welcome-copy">
              <p className="garden-eyebrow">오늘의 읽기</p>
              <h2 id="today-reading-title">{resume ? '하던 읽기를 이어가요.' : '오늘, 이 글부터 읽어 볼까요?'}</h2>
              <p>{featured ? readingTitle(featured.slotId, featured.title) : '한 편의 글을 만나고, 나만의 이유를 찾아요.'}</p>
              <button className="garden-button" onClick={() => featured ? open(featured.slotId, featured.type) : setStudentMode('progressive')}>
                {resume ? '이어서 읽기' : '오늘의 읽기 시작'} <ArrowRight size={18}/>
              </button>
              <div className="garden-study-counts" aria-label="이 기기의 학습 기록">
                <span>남은 수업 <b>{pending.length}</b></span><span>남긴 생각 <b>{drafts.length}</b></span><span>모은 낱말 <b>{savedVocab.length}</b></span>
              </div>
            </div>
            <img className="garden-welcome-art" src={`${import.meta.env.BASE_URL}brand/editorial/reading.webp`} width="1536" height="1024" alt="책을 읽으며 생각을 정리하는 학습 장면"/>
          </section>
          <details className="garden-strategy"><summary>읽는 방법을 먼저 배워 볼까요?<span>시범부터 스스로 읽기까지</span></summary><section className="rx-today-strategy"><div className="rx-today-label"><span>오늘 배울 읽기 방법</span><span>시범 → 내 표시와 설명 → 스스로 확인</span></div>{gradeData.grade_num === 5 ? <JourneyEntryCard/> : <ProgressiveReadingEntry/>}</section></details>
          <RecentThinkingFeedback onOpen={()=>setTab("records")}/>
          <div className="rx-student-grid">
            <div>
              {featured?.slotId === JOURNEY_SLOT ? null : featured ? (
                <section className="rx-next-lesson">
                  <div className="rx-next-top">
                    <span className="rx-eyebrow">
                      {resume ? "이어서 읽을 글" : "오늘의 첫 번째 수업"}
                    </span>
                    <span className="rx-dark-badge">{taskLabel(featured)}</span>
                  </div>
                  <h2>{featured.type === "clinic" ? featured.title : readingTitle(featured.slotId,featured.title)}</h2>
                  <p>글에서 단서를 찾고, 그렇게 생각한 이유를 설명해 보세요.</p>
                  <button
                    className="rx-button rx-button-gold rx-button-lg"
                    onClick={() => open(featured.slotId, featured.type)}
                  >
                    {resume ? "이어서 학습하기" : "학습 시작하기"}
                    <ArrowRight size={18} />
                  </button>
                  <div className="rx-next-decoration" aria-hidden="true">
                    <BookOpen strokeWidth={0.7} />
                    <span>+</span>
                  </div>
                  <div className="rx-next-bottom">
                    <span>
                      <Clock3 size={15} />내 속도에 맞춰 차근차근
                    </span>
                    <span>체험 수업</span>
                  </div>
                </section>
              ) : (
                <section className="rx-surface">
                  <EmptyState
                    title="오늘 배정된 수업이 없어요"
                    description="다른 읽기 자료를 둘러보거나 나의 기록을 확인해 보세요."
                    action={
                      <button
                        className="rx-button"
                        onClick={() => setLibrary(true)}
                      >
                        수업 둘러보기
                      </button>
                    }
                  />
                </section>
              )}
              <div className="rx-list-heading">
                <h2>
                  나의 수업 목록 <span>{pending.length}</span>
                </h2>
                <span>이 기기의 체험 과제</span>
              </div>
              <div className="rx-lesson-list">
                {pending.map((task, i) => (
                  <button
                    className="rx-lesson-row"
                    key={task.id}
                    onClick={() => open(task.slotId, task.type)}
                  >
                    <span
                      className={`rx-lesson-number ${task.slotId.includes("-COM-") ? "is-green" : ""}`}
                    >
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <span className="rx-lesson-row-copy">
                      <small>{taskLabel(task)}</small>
                      <b>{task.type === "clinic" ? task.title : readingTitle(task.slotId,task.title)}</b>
                      <span>
                        {sessions[task.slotId]
                          ? "열어본 수업 · 이어할 수 있어요"
                          : task.assignedBy}
                      </span>
                    </span>
                    <ChevronRight size={20} />
                  </button>
                ))}
              </div>
            </div>
            <aside className="rx-learning-aside">
              <div className="rx-aside-top">
                <Sparkles size={20} />
                <span>오늘의 읽기 방법</span>
              </div>
              <h2>
                정답보다 먼저,
                <br />
                이유를 생각해요.
              </h2>
              <ol>
                {[
                  ["글에서 찾기", "어느 문장이 단서가 될까요?"],
                  ["생각 이어 보기", "두 내용은 어떻게 연결될까요?"],
                  ["내 말로 설명하기", "왜 그렇게 생각했나요?"],
                ].map(([title, desc], i) => (
                  <li key={title}>
                    <span>{i + 1}</span>
                    <div>
                      <b>{title}</b>
                      <p>{desc}</p>
                    </div>
                  </li>
                ))}
              </ol>
              <div className="rx-aside-note">
                <PenLine size={18} />
                <p>
                  오늘 쓴 문장은
                  <br />
                  <button onClick={() => setTab("records")}>나의 기록</button>
                  에서 다시 볼 수 있어요.
                </p>
              </div>
            </aside>
          </div>
          <div className="rx-next-route"><div><h2>배운 방법을 다른 글에서도 써 볼까요?</h2><p>표시한 단서를 연결하며 연습하거나, 도움 없이 읽고 확인해요.</p></div><button className="rx-button" onClick={()=>setTab("practice")}>읽기 연습 <ArrowRight size={16}/></button></div>
          <ExamEntryCard role="student"/>
          {gradeData.grade_num >= 5 && <details className="rx-optional"><summary>내 평가와 목표 한눈에 보기</summary><AssessmentEntryCards grade={gradeData.grade_num}/></details>}
          <section className="rx-discover">
            <div>
              <LibraryBig size={23} />
              <div>
                <h2>다른 읽기도 만나 볼까요?</h2>
                <p>
                  {gradeData.grade}의 다양한 교과 개념과 읽기 목표를 살펴보세요.
                </p>
              </div>
            </div>
            <button
              className="rx-button"
              aria-expanded={library}
              onClick={() => setLibrary(!library)}
            >
              {library ? "자료 접기" : "수업 둘러보기"}
              <ChevronRight size={16} />
            </button>
          </section>
          {library && (
            <section className="rx-surface rx-library">
              <label className="rx-search">
                <Search size={18} />
                <input
                  aria-label="수업 검색"
                  placeholder="수업 제목 또는 읽기 목표 검색"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                />
              </label>
              <div className="rx-course-grid">
                {gradeSlots16
                  .filter((s) =>
                    (
                      readingTitle(s.slot_id,s.real_csat_test.passage_title) + s.sub_skill_name
                    ).includes(query),
                  )
                  .map((s) => (
                    <button
                      className="rx-course-card"
                      key={s.slot_id}
                      onClick={() => open(s.slot_id)}
                    >
                      <span className="rx-badge">
                        {s.curriculum_concept.subject}
                      </span>
                      <h3>{readingTitle(s.slot_id,s.real_csat_test.passage_title)}</h3>
                      <p>{s.sub_skill_name}</p>
                      <span className="rx-text-link">
                        읽어보기 <ArrowRight size={15} />
                      </span>
                    </button>
                  ))}
              </div>
              {!gradeSlots16.some((s) =>
                (readingTitle(s.slot_id,s.real_csat_test.passage_title) + s.sub_skill_name).includes(
                  query,
                ),
              ) && (
                <EmptyState
                  title="찾는 수업이 없어요"
                  description="다른 검색어로 찾아보세요."
                />
              )}
            </section>
          )}
          <details className="rx-optional">
            <summary>더 살펴볼 체험 활동</summary>
            <div>
              <button className="rx-button" onClick={() => setShowVocab(true)}>
                어휘 연습
              </button>
              <button className="rx-button" onClick={() => setShowGalaxy(true)}>
                성장 지도 시안
              </button>
              <button className="rx-button" onClick={() => setShowCat(true)}>
                초기 확인 시안
              </button>
              <button
                className="rx-button"
                onClick={() => { useStudentAssessment.getState().setView("exams"); setStudentMode(gradeData.grade_num >= 5 ? "assessment" : "cbt_exam"); }}
              >
                혼자 확인하기
              </button>
            </div>
            <p>
              선택 활동과 진단 화면은 예시입니다. 실제 성취 결과로 사용하지
              않습니다.
            </p>
          </details>
        </>
      )}
      {tab === "records" && (
        <section className="rx-surface rx-records">
          <div className="rx-section-title">
            <div>
              <p className="rx-eyebrow">MY THINKING NOTES</p>
              <h2>내 말로 남긴 생각</h2>
            </div>
            <span className="rx-badge">기기 저장 · {drafts.length}개</span>
          </div>
          <p className="rx-muted">
            학습하면서 작성한 초안이에요. 교사에게 제출된 답안과는 구분해
            보관해요.
          </p>
          {drafts.length ? (
            drafts.map(([key, text]) => {
              const lesson = findLesson(key.split(":")[0]);
              return (
                <article className="rx-draft" key={key}>
                  <span className="rx-eyebrow">생각 기록</span>
                  <h3>
                    {key.includes(":journey-")
                      ? JOURNEY_GOAL
                      : lesson && "real_csat_test" in lesson
                        ? lesson.real_csat_test.passage_title
                        : "나의 생각 연습"}
                  </h3>
                  <p>{text}</p>
                  {lesson && (
                    <button
                      className="rx-text-link"
                      onClick={() => open(key.split(":")[0])}
                    >
                      다시 읽고 고치기 <ArrowRight size={16} />
                    </button>
                  )}
                </article>
              );
            })
          ) : (
            <EmptyState
              title="첫 번째 생각을 기다리고 있어요"
              description="수업의 ‘내 말로 쓰기’에서 글을 쓰면 여기에 보관돼요."
              action={
                <button
                  className="rx-button rx-button-primary"
                  onClick={() => setTab("today")}
                >
                  오늘의 학습으로
                </button>
              }
            />
          )}
        </section>
      )}
      {tab === "vocab" && (
        <section className="rx-surface rx-records">
          <PageHeading
            eyebrow="MY WORDS"
            title="새롭게 만난 낱말"
            description="본문에서 저장한 낱말을 다시 읽어 보세요."
          />
          {savedVocab.length ? (
            <div className="rx-course-grid">
              {savedVocab.map((v) => (
                <article className="rx-course-card" key={v.word}>
                  <Bookmark size={20} />
                  <h3>{v.word}</h3>
                  <p>{v.desc}</p>
                  <button
                    className="rx-text-link"
                    onClick={() => removeVocabWord(v.word)}
                  >
                    외웠어요 · 단어장에서 빼기 <Check size={15} />
                  </button>
                </article>
              ))}
            </div>
          ) : (
            <EmptyState
              title="아직 저장한 낱말이 없어요"
              description="읽기 화면 아래의 핵심 낱말에서 ‘단어장에 담기’를 눌러 보세요."
            />
          )}
        </section>
      )}
      {showVocab && (
        <VocabDuelArena
          vocabList={gradeData.real_csat_test.vocab_notes || []}
          onClose={() => setShowVocab(false)}
        />
      )}
      {showGalaxy && (
        <GalaxyExpeditionMap onClose={() => setShowGalaxy(false)} />
      )}
      {showCat && (
        <OnboardingCatModal
          gradeData={gradeData}
          onClose={() => setShowCat(false)}
        />
      )}
    </div>
  );
}
