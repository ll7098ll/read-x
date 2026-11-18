import { QuantifiedReport } from "../common/QuantifiedReport";
import { demoReportRecords, reportPeriods } from "../../data/demoReportRecords";
import { summarizeReport } from "../../services/reportMetrics";
import React, { useState } from "react";
import {
  Printer,
  ArrowRight,
  Check,
  MessageCircle,
  CalendarDays,
} from "lucide-react";
import { PageHeading } from "../common/DesignSystem";
import {
  DemoContext,
  DemoEvidence,
} from "../common/AcademyDemo";
import { LearningIllustration } from "../brand/LearningIllustration";
import {
  demoStudents,
  demoStudent,
  demoClasses,
  demoLesson,
} from "../../data/demoAcademy";
import { useDemoAcademy } from "../../store/useDemoAcademy";

export function ParentDemoDashboard({
  practice,
}: {
  practice: React.ReactNode;
}) {
  const { selectedStudentId, selectStudent, reviews, releases } =
    useDemoAcademy();
  const student = demoStudent(selectedStudentId),
    cls = demoClasses.find((c) => c.id === student.classId)!,
    lesson = demoLesson(student);
  const [tab, setTab] = useState("summary"),
    [talked, setTalked] = useState(false);
  const currentShared = student.published || releases[student.id];
  const feedback = currentShared
    ? reviews[student.id]?.note || student.teacherNote
    : "근거를 찾은 뒤 설명을 다시 읽는 습관이 생기고 있어요. 익숙한 글에서 배운 방법을 다른 글에서도 사용해 보겠습니다.";
  const next = currentShared
    ? reviews[student.id]?.next || student.focus
    : student.focus;
  const recentPeriod = reportPeriods[0];
  const recent = summarizeReport(
    demoReportRecords([student], reviews, releases, "parent"),
    recentPeriod.start,
    recentPeriod.end,
  );
  return (
    <div className="ad-parent">
      <PageHeading
        eyebrow="LEARNING, TOGETHER"
        title={`${student.name}의 생각이 자라는 한 주`}
        description="아이가 고른 근거, 달라진 설명, 다음 배움을 함께 만나세요."
        action={
          <button className="rx-button no-print" onClick={() => window.print()}>
            <Printer size={17} /> 리포트 인쇄
          </button>
        }
      />
      <DemoContext role="parent" />
      <div className="ad-child-bar">
        <span className={`ad-avatar tone-${student.grade}`}>
          {student.name.slice(1)}
        </span>
        <div>
          <b>{student.name}</b>
          <p>
            {cls.name} · 초등 {student.grade}학년 · {cls.teacher} 선생님
          </p>
        </div>
        <label className="no-print">
          예시 자녀 바꾸기
          <select
            aria-label="예시 자녀 선택"
            value={student.id}
            onChange={(e) => {
              selectStudent(e.target.value);
              setTalked(false);
            }}
          >
            {demoStudents.map((s) => (
              <option key={s.id} value={s.id}>
                {s.name} · {s.grade}학년
              </option>
            ))}
          </select>
        </label>
      </div>
      <nav className="rx-tabs no-print" aria-label="학부모 메뉴">
        {[
          ["summary", "주간 리포트", "grow"],
          ["notes", "아이의 생각 기록", "writing"],
          ["conversation", "집에서 이어가기", "guided"],
          ["practice", "직접 해본 연습", "book"],
        ].map(([id, label, kind]) => (
          <button
            key={id}
            aria-current={tab === id ? "page" : undefined}
            onClick={() => setTab(id)}
          >
            <LearningIllustration kind={kind} />
            {label}
          </button>
        ))}
      </nav>
      {tab === "summary" && (
        <>
          <section className="ad-parent-hero">
            <div>
              <p className="rx-eyebrow">
                WEEKLY READING REPORT · 10.08 — 10.14
              </p>
              <h2>
                답을 찾는 데서,
                <br />
                <em>이유를 설명하는 데로.</em>
              </h2>
              <p>
                {student.name} 학생은 최근 7일 동안 {recent.submitted}개의 읽기
                활동을 마쳤어요.
                <br />
                배정된 {recent.assigned}개 활동의 첫 응답과 설명 평가를 함께
                살펴보세요.
              </p>
              <span className="ad-status is-done">
                {cls.teacher} 선생님의 주간 관찰 · 예시
              </span>
            </div>
            <LearningIllustration kind="grow" />
          </section>
          <QuantifiedReport students={[student]} audience="parent" />
          <section className="ad-card ad-parent-feedback">
            <span className="ad-avatar teacher-avatar">
              {cls.teacher.slice(1)}
            </span>
            <div>
              <p className="rx-eyebrow">TEACHER’S LETTER</p>
              <h2>{cls.teacher} 선생님의 한마디</h2>
              <p>{feedback}</p>
              <div className="ad-task-note">
                <b>다음 읽기 목표</b>
                <p>{next}</p>
              </div>
              <p className="rx-fine-print">
                {currentShared
                  ? "10.14 수업 피드백까지 반영된 예시입니다."
                  : "지난주 주간 리포트입니다. 오늘 수업 피드백은 교사 검토 후 이어집니다."}
              </p>
            </div>
          </section>
        </>
      )}
      {tab === "notes" && (
        <div className="ad-columns">
          <section className="ad-card">
            <p className="rx-eyebrow">
              A MOMENT OF LEARNING · 지난주 연습 예시
            </p>
            <h2>생각은 이렇게 달라졌어요</h2>
            <DemoEvidence student={student} />
          </section>
          <aside className="ad-card ad-next">
            <LearningIllustration kind="search" />
            <h2>“왜 그렇게 생각했어?”</h2>
            <p>
              처음 설명에서 빠졌던 내용을 본문과 비교한 뒤 다시 썼어요. 도움을
              받은 연습과 혼자 설명한 기록을 구분해서 봐 주세요.
            </p>
            <div className="ad-task-note">
              <b>이 글에서 연습한 목표</b>
              <p>{lesson.goal}</p>
            </div>
            <button
              className="rx-button rx-button-primary"
              onClick={() => setTab("conversation")}
            >
              집에서 나눌 질문 보기 <ArrowRight size={17} />
            </button>
          </aside>
        </div>
      )}
      {tab === "conversation" && (
        <section className="ad-card">
          <p className="rx-eyebrow">FIVE MINUTES, TOGETHER</p>
          <h2>오늘은 한 가지 질문이면 충분해요</h2>
          <div className="ad-talk-grid">
            {[
              [
                "01",
                "글을 다시 만나요",
                `“${lesson.title}”에서 기억에 남는 문장은 무엇이니?`,
                "아이가 고른 문장을 함께 읽어주세요.",
              ],
              [
                "02",
                "생각의 이유를 들어요",
                "그 문장이 네 답을 설명하는 데 왜 도움이 되었어?",
                "바로 고쳐주기보다, 이유를 끝까지 들어주세요.",
              ],
              [
                "03",
                "생활로 이어가요",
                "다른 글에서도 같은 방법을 써볼 수 있을까?",
                "읽은 방법을 아이의 말로 들려달라고 해보세요.",
              ],
            ].map(([n, title, q, help]) => (
              <article key={n}>
                <span>{n}</span>
                <h3>{title}</h3>
                <blockquote>{q}</blockquote>
                <p>{help}</p>
              </article>
            ))}
          </div>
          <button
            className="rx-button rx-button-primary no-print"
            onClick={() => setTalked(true)}
          >
            <Check size={17} />{" "}
            {talked ? "함께 나눈 대화를 표시했어요" : "오늘 대화를 나눴어요"}
          </button>
          {talked && (
            <p className="ad-success" role="status">
              이 화면에서 대화를 표시했어요. 선생님에게 알림이 전송되지는
              않습니다.
            </p>
          )}
          <div className="ad-home-plan">
            <CalendarDays size={22} />
            <div>
              <b>다음 읽기 시간 · 10월 16일 {cls.time}</b>
              <p>
                {cls.name}에서 {next}를 이어갑니다.
              </p>
            </div>
          </div>
        </section>
      )}
      {tab === "practice" && practice}
    </div>
  );
}
