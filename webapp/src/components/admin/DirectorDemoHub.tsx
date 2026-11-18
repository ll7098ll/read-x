import { DirectorQuantifiedReport } from "../common/QuantifiedReport";
import { PracticeOverview } from "../common/ThinkingPortfolio";
import React, { useState } from "react";
import { ArrowRight, CalendarDays, Check, Clock3 } from "lucide-react";
import { PageHeading } from "../common/DesignSystem";
import {
  DemoContext,
  DemoMetrics,
  DemoStudentList,
} from "../common/AcademyDemo";
import { LearningIllustration } from "../brand/LearningIllustration";
import {
  demoAcademy,
  demoClasses,
  demoStudents,
  demoStudent,
  demoMetrics,
  demoConsultations,
} from "../../data/demoAcademy";
import { useDemoAcademy } from "../../store/useDemoAcademy";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { useReadingStorageStatus } from "../../store/useReadingWorkspace";

function ConsultationNote({ id }: { id: string }) {
  const c = demoConsultations.find((c) => c.id === id)!,
    student = demoStudent(c.studentId);
  const { consultationNotes, saveConsultation, selectStudent } =
    useDemoAcademy();
  const [note, setNote] = useState(consultationNotes[id] || c.note),
    [saved, setSaved] = useState(false);
  const failed = useReadingStorageStatus((s) => s.failed);
  return (
    <section className="ad-card">
      <p className="rx-eyebrow">COUNSELING NOTE</p>
      <h2>{student.name} 보호자 상담</h2>
      <p className="ad-subtitle">
        {c.date} {c.time} · {c.topic}
      </p>
      <label className="rx-field">
        상담 준비 메모
        <textarea
          value={note}
          rows={6}
          onChange={(e) => {
            setNote(e.target.value);
            setSaved(false);
          }}
        />
      </label>
      <div className="ad-actions">
        <button
          className="rx-button rx-button-primary"
          onClick={() => {
            saveConsultation(id, note);
            setSaved(true);
          }}
        >
          <Check size={16} /> 상담 메모 보관
        </button>
        <button
          className="rx-button"
          onClick={() => {
            selectStudent(student.id);
            useCoursewareStore.getState().setActiveRole("parent");
          }}
        >
          학생 리포트 보기 <ArrowRight size={16} />
        </button>
      </div>
      {saved && (
        <p role="status" className="ad-success">
          {failed
            ? "브라우저에 보관하지 못했습니다. 메모를 따로 복사해 주세요."
            : "예시 상담 메모를 이 브라우저에 보관했어요."}
        </p>
      )}
    </section>
  );
}
export function DirectorDemoHub() {
  const [tab, setTab] = useState("overview"),
    [classId, setClassId] = useState("all"),
    [query, setQuery] = useState(""),
    [consult, setConsult] = useState(demoConsultations[0].id),
    [reportFilter, setReportFilter] = useState("pending");
  const { reviews, releases, selectStudent, selectClass } = useDemoAcademy();
  const setRole = useCoursewareStore((s) => s.setActiveRole);
  const pending = demoStudents.filter(
    (s) => s.status === "submitted" && !s.reviewed && !reviews[s.id],
  );
  const students = demoStudents.filter(
    (s) =>
      (classId === "all" || s.classId === classId) && s.name.includes(query),
  );
  const reports = demoStudents.filter(
    (s) =>
      s.status === "submitted" &&
      (reportFilter === "pending"
        ? !s.reviewed && !reviews[s.id]
        : reportFilter === "shared"
          ? s.published || releases[s.id]
          : s.reviewed || reviews[s.id]),
  );
  const teacher = (id: string) => {
    selectStudent(id);
    useDemoAcademy.getState().setTeacherView("review");
    setRole("teacher");
  };
  return (
    <div className="ad-director">
      <PageHeading
        eyebrow="ACADEMY DIRECTOR"
        title="좋은 배움이 이어지는 학원을 만듭니다"
        description="반별 수업과 학생의 생각, 교사의 피드백을 한곳에서 살펴보세요."
      />
      <DemoContext role="director" />
      <nav className="rx-tabs" aria-label="학원 원장 메뉴">
        {[
          ["overview", "학원 현황", "target"],
          ["classes", "반·학생 관리", "guided"],
          ["reports", "학습·리포트", "writing"],
          ["analytics", "학습 분석", "target"],
          ["consult", "상담 일정", "grow"],
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
      {tab === "analytics" && <DirectorQuantifiedReport />}
      {tab === "overview" && (
        <>
          <PracticeOverview onReview={()=>setRole("teacher")}/>
          <div className="ad-director-hero">
            <div>
              <p className="rx-eyebrow">{demoAcademy.branch} · 10월 둘째 주</p>
              <h2>
                24개의 생각이,
                <br />
                각자의 속도로 자라고 있어요.
              </h2>
              <p>
                오늘은 {pending.length}명의 응답을 검토하면 다음 배움을 이어갈
                수 있어요.
              </p>
              <button
                className="rx-button rx-button-gold"
                onClick={() => setTab("reports")}
              >
                검토 현황 살펴보기 <ArrowRight size={17} />
              </button>
            </div>
            <LearningIllustration kind="grow" />
          </div>
          <DemoMetrics />
          <div className="ad-columns">
            <section className="ad-card">
              <div className="ad-section-head">
                <div>
                  <p className="rx-eyebrow">TODAY’S TIMETABLE</p>
                  <h2>오늘의 수업</h2>
                </div>
                <CalendarDays size={22} />
              </div>
              <div className="ad-schedule">
                {demoClasses.map((c) => {
                  const m = demoMetrics(
                    demoStudents.filter((s) => s.classId === c.id),
                    reviews,
                    releases,
                  );
                  return (
                    <button
                      key={c.id}
                      onClick={() => {
                        selectClass(c.id);
                        setClassId(c.id);
                        setTab("classes");
                      }}
                    >
                      <time>{c.time}</time>
                      <div>
                        <b>{c.name}</b>
                        <span>
                          {c.teacher} 선생님 · {c.room} · {c.grade}학년
                        </span>
                        <p>{c.goal}</p>
                      </div>
                      <span className="ad-status is-review">
                        검토 {m.pending}명
                      </span>
                      <ArrowRight size={17} />
                    </button>
                  );
                })}
              </div>
            </section>
            <aside className="ad-card">
              <p className="rx-eyebrow">FOLLOW UP</p>
              <h2>수업 다음의 연결</h2>
              <div className="ad-followup">
                <LearningIllustration kind="writing" />
                <h3>검토에서 피드백까지</h3>
                <p>
                  제출된 답을 읽고 다음 목표를 남기면 학부모가 아이의 배움을
                  이해하기 쉬워집니다.
                </p>
                <button
                  className="rx-text-link"
                  onClick={() => setTab("reports")}
                >
                  피드백 현황 <ArrowRight size={16} />
                </button>
              </div>
              <div className="ad-followup">
                <h3>다가오는 보호자 상담</h3>
                <p>
                  {demoConsultations[0].date} {demoConsultations[0].time} ·{" "}
                  {demoStudent(demoConsultations[0].studentId).name}
                </p>
                <button
                  className="rx-text-link"
                  onClick={() => setTab("consult")}
                >
                  상담 메모 준비하기 <ArrowRight size={16} />
                </button>
              </div>
            </aside>
          </div>
        </>
      )}
      {tab === "classes" && (
        <>
          <div className="ad-class-cards">
            {demoClasses.map((c) => {
              const m = demoMetrics(
                demoStudents.filter((s) => s.classId === c.id),
                reviews,
                releases,
              );
              return (
                <button
                  key={c.id}
                  onClick={() => setClassId(classId === c.id ? "all" : c.id)}
                  aria-pressed={classId === c.id}
                >
                  <LearningIllustration kind="book" />
                  <h3>{c.name}</h3>
                  <p>
                    {c.grade}학년 · {c.teacher} 선생님
                  </p>
                  <strong>
                    {m.completed}
                    <small> / {m.total}명 제출</small>
                  </strong>
                  <div className="ad-track">
                    <i style={{ width: `${(m.completed / m.total) * 100}%` }} />
                  </div>
                  <span>피드백 완료 {m.reviewed}명</span>
                </button>
              );
            })}
          </div>
          <section className="ad-card">
            <div className="ad-section-head">
              <h2>반별 학생</h2>
              <label className="ad-search">
                학생 이름
                <input
                  aria-label="예시 학생 이름 검색"
                  placeholder="이름으로 찾기"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                />
              </label>
              <select
                aria-label="원장 반 필터"
                value={classId}
                onChange={(e) => setClassId(e.target.value)}
              >
                <option value="all">전체 반</option>
                {demoClasses.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.name}
                  </option>
                ))}
              </select>
            </div>
            <DemoStudentList
              students={students}
              onSelect={(s) => teacher(s.id)}
            />
            {!students.length && <p>조건에 맞는 예시 학생이 없습니다.</p>}
            <p className="rx-fine-print">
              학생을 선택하면 해당 반의 교사 화면으로 연결됩니다.
            </p>
          </section>
        </>
      )}
      {tab === "reports" && (
        <>
          <DemoMetrics />
          <section className="ad-card">
            <div className="ad-section-head">
              <div>
                <p className="rx-eyebrow">LEARNING CONNECTION</p>
                <h2>학습 기록이 피드백으로 이어지도록</h2>
              </div>
              <select
                aria-label="리포트 현황 필터"
                value={reportFilter}
                onChange={(e) => setReportFilter(e.target.value)}
              >
                <option value="pending">검토 대기</option>
                <option value="reviewed">검토 완료</option>
                <option value="shared">리포트 공개</option>
              </select>
            </div>
            <DemoStudentList
              students={reports}
              onSelect={(s) => teacher(s.id)}
            />
            {!reports.length && <p>현재 선택한 상태의 학생이 없습니다.</p>}
            <p className="rx-fine-print">
              이 화면의 수치는 가상 학생의 예시 제출·검토 상태에서 집계합니다.
            </p>
          </section>
        </>
      )}
      {tab === "consult" && (
        <div className="ad-review-layout">
          <aside className="ad-card">
            <p className="rx-eyebrow">UPCOMING CONVERSATIONS</p>
            <h2>다가오는 상담 3건</h2>
            <div className="ad-consult-list">
              {demoConsultations.map((c) => (
                <button
                  key={c.id}
                  onClick={() => setConsult(c.id)}
                  aria-pressed={consult === c.id}
                >
                  <span>
                    <Clock3 size={15} />
                    {c.date} {c.time}
                  </span>
                  <b>{demoStudent(c.studentId).name} 보호자</b>
                  <p>{c.topic}</p>
                </button>
              ))}
            </div>
          </aside>
          <ConsultationNote key={consult} id={consult} />
        </div>
      )}
    </div>
  );
}
