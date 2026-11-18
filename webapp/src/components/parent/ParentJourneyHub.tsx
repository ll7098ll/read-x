import { ExamEntryCard } from "../exam/ExamEntryCard";
import { enterExam } from "../../services/examNavigation";
import { ParentDemoDashboard } from "./ParentDemoDashboard";
import { LearningIllustration } from "../brand/LearningIllustration";
import React, { useState } from "react";
import {
  ArrowRight,
  BookOpen,
  MessageCircle,
  PenLine,
  Printer,
  Quote,
  Sprout,
} from "lucide-react";
import { PageHeading, EmptyState, ThinkingPath } from "../common/DesignSystem";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { findLesson } from "../../data/lessonCatalog";
import { LearningEvidenceReport } from "../common/LearningEvidenceReport";
import { ThinkingPortfolio } from "../common/ThinkingPortfolio";
import { useLearningJourney } from "../../store/useLearningJourney";
import { JOURNEY_SLOT, JOURNEY_GOAL } from "../../data/learningJourney";
import type { GradeData, SubskillMeta } from "../../types/courseware";

function ParentPracticeHub({
  gradeData,
}: {
  gradeData: GradeData;
  subskillMeta: SubskillMeta[];
}) {
  const { responseDrafts, assignments } = useCoursewareStore();
  const [tab, setTab] = useState("summary");
  const journeyAttempts = useLearningJourney((s) => s.attempts);
  const drafts = [
    ...Object.entries(responseDrafts),
    ...journeyAttempts
      .filter((a) => a.writing.trim())
      .map(
        (a) =>
          [`${JOURNEY_SLOT}:journey-${a.id}`, a.writing] as [string, string],
      ),
  ].filter(([, value]) => value.trim());
  return (
    <div className="rx-parent-page">
      <PageHeading
        eyebrow="우리 아이의 배움"
        title="아이의 생각을 만나는 시간"
        description="무엇을 읽고, 어떻게 생각했는지. 배움의 과정을 함께 살펴보세요."
        action={
          <button className="rx-button no-print" onClick={() => window.print()}>
            <Printer size={17} />
            리포트 인쇄
          </button>
        }
      />
      <nav className="rx-tabs no-print" aria-label="학부모 메뉴">
        {[
          ["summary", "배움 요약"],
          ["exams", "모의고사 리포트"],
          ["notes", "생각 기록"],
          ["conversation", "함께 나눌 질문"],
        ].map(([id, label]) => (
          <button
            key={id}
            aria-current={tab === id ? "page" : undefined}
            onClick={() => id === "exams" ? enterExam("parent") : setTab(id)}
          >
            <LearningIllustration kind={id} />
            {label}
          </button>
        ))}
      </nav>
      <details className="workspace-exam-shortcut"><summary>모의고사 리포트 바로가기</summary><ExamEntryCard role="parent"/></details>
      {tab === "summary" && (
        <>
          <ThinkingPortfolio audience="parent" />
          <details className="rx-demo-secondary"><summary>읽기 안내와 가정에서 이어갈 질문</summary>
          <section className="rx-parent-hero print-card">
            <div>
              <span className="rx-dark-badge">우리 아이의 배움 · 체험</span>
              <h2>
                작은 발견이 쌓여,
                <br />
                설명할 수 있는 힘으로.
              </h2>
              <p>
                점수 한 줄보다 아이가 찾아낸 근거와 직접 쓴 문장을 먼저 만나요.
              </p>
            </div>
            <div className="rx-parent-hero-mark" aria-hidden="true">
              <Sprout size={94} strokeWidth={1} />
              <span>GROW WITH READX</span>
            </div>
          </section>
          <div className="rx-parent-summary">
            <article className="rx-surface print-card">
              <span className="rx-step-icon is-blue">
                <BookOpen size={22} />
              </span>
              <h2>지금 연습하는 것</h2>
              <p>{gradeData.sub_skill_name}</p>
              <small>{gradeData.real_csat_test.passage_title}</small>
            </article>
            <article className="rx-surface print-card">
              <span className="rx-step-icon is-green">
                <PenLine size={22} />
              </span>
              <h2>직접 남긴 생각</h2>
              <p>
                {drafts.length ? (
                  <>
                    기기에 보관된 초안 <b>{drafts.length}개</b>
                  </>
                ) : (
                  "아직 작성된 초안이 없어요"
                )}
              </p>
              <small>체험 기기의 기록이며 교사 제출 결과는 아닙니다.</small>
            </article>
            <article className="rx-surface print-card">
              <span className="rx-step-icon is-gold">
                <MessageCircle size={22} />
              </span>
              <h2>다음에 도울 한 가지</h2>
              <p>“어느 문장에서 그렇게 생각했니?”</p>
              <small>답을 알려주기 전에 아이가 찾은 이유를 들어주세요.</small>
            </article>
          </div>
          <section className="rx-surface rx-records print-card">
            <div className="rx-section-title">
              <div>
                <p className="rx-eyebrow">A GLIMPSE OF THINKING</p>
                <h2>아이의 문장으로 보는 배움</h2>
              </div>
              <button
                className="rx-text-link no-print"
                onClick={() => setTab("notes")}
              >
                기록 모두 보기 <ArrowRight size={16} />
              </button>
            </div>
            {drafts.length ? (
              <blockquote className="rx-quote">
                <Quote size={24} />
                <p>{drafts[drafts.length - 1][1]}</p>
                <cite>이 기기에서 작성한 체험 초안</cite>
              </blockquote>
            ) : (
              <EmptyState
                title="한 문장이 배움의 기록이 됩니다"
                description="학생 화면에서 ‘내 말로 쓰기’를 하면 작성한 초안이 이곳에도 나타납니다."
              />
            )}
            <p className="rx-inline-note">
              공식 진단·성장 결과와 선생님 의견은 실제 학습 기록과 교사 검토가
              연결된 뒤 제공됩니다.
            </p>
          </section>
          <section className="rx-family-conversation">
            <div>
              <MessageCircle size={26} />
              <h2>오늘 저녁, 이런 이야기를 나눠 보세요.</h2>
              <p>“오늘 읽은 글에서 가장 기억에 남는 건 뭐야?”</p>
            </div>
            <button
              className="rx-button no-print"
              onClick={() => setTab("conversation")}
            >
              질문 더 보기 <ArrowRight size={16} />
            </button>
          </section>
          </details>
        </>
      )}
      {tab === "notes" && (
        <section className="rx-surface rx-records">
          <PageHeading
            eyebrow="THINKING NOTES"
            title="직접 쓴 문장을 모았어요"
            description="작성한 내용 그대로 보여주는 기기 내 체험 기록입니다."
          />
          {drafts.length ? (
            drafts.map(([key, text]) => {
              const lesson = findLesson(key.split(":")[0]);
              return (
                <article className="rx-draft print-card" key={key}>
                  <h3>
                    {key.includes(":journey-")
                      ? JOURNEY_GOAL
                      : lesson && "real_csat_test" in lesson
                        ? lesson.real_csat_test.passage_title
                        : "생각 연습"}
                  </h3>
                  <p>{text}</p>
                  <small>교사 검토 전 · 기기 저장</small>
                </article>
              );
            })
          ) : (
            <EmptyState
              title="아직 생각 기록이 없어요"
              description="첫 번째 글을 쓴 뒤 다시 방문해 주세요."
            />
          )}
        </section>
      )}
      {tab === "conversation" && (
        <section className="rx-surface rx-records">
          <PageHeading
            eyebrow="A LITTLE CONVERSATION"
            title="정답을 묻기보다, 생각을 들어주세요"
            description="읽은 글과 아이의 속도에 맞춰 한 가지 질문만 골라도 좋아요."
          />
          <ThinkingPath />
          <div className="rx-coaching-list">
            {[
              [
                "발견을 물어요",
                "어느 부분이 가장 기억에 남니?",
                "아이가 고른 문장을 함께 읽어주세요.",
              ],
              [
                "이유를 이어요",
                "그 문장이 왜 중요하다고 생각했어?",
                "글에 나온 표현을 가리키며 말할 시간을 주세요.",
              ],
              [
                "새롭게 설명해요",
                "친구에게 알려준다면 어떻게 말할까?",
                "아이의 말을 먼저 듣고, 이어서 한 가지만 물어보세요.",
              ],
            ].map(([title, q, desc], i) => (
              <article key={title}>
                <span>0{i + 1}</span>
                <div>
                  <small>{title}</small>
                  <h2>“{q}”</h2>
                  <p>{desc}</p>
                </div>
              </article>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}

export function ParentJourneyHub(props: { gradeData: GradeData; subskillMeta: SubskillMeta[] }) { return <><ParentPracticeHub {...props}/><details className="rx-demo-secondary"><summary>가상 학급의 주간·월간 운영 예시 살펴보기</summary><ParentDemoDashboard practice={<ParentPracticeHub {...props}/>} /></details></>; }
