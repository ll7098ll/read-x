import { MetricCards, ReportMethodology } from "./QuantifiedReport";
import {
  journeyReportRecords,
  summarizeReport,
} from "../../services/reportMetrics";
import { LearningIllustration } from "../brand/LearningIllustration";
import React, { useState } from "react";
import { ArrowRight, BookOpen, Check, Link2, PenLine } from "lucide-react";
import {
  getSentence,
  JOURNEY_GOAL,
  JOURNEY_SLOT,
  journeyTasks,
  journeyStages,
  type TaskId,
} from "../../data/learningJourney";
import { useLearningJourney } from "../../store/useLearningJourney";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { useReadingStorageStatus } from "../../store/useReadingWorkspace";
import type { JourneySubmission } from "../../services/learningJourney";
import { annotationKinds } from "../../services/learningJourney";
import { readingLevelLabels } from "../../data/readingPolicy";

function LocalReview({
  attemptId,
  task,
  submission,
}: {
  attemptId: string;
  task: TaskId;
  submission: JourneySubmission;
}) {
  const [outcome, setOutcome] = useState(submission.review?.outcome || "");
  const [note, setNote] = useState(submission.review?.note || "");
  const [saved, setSaved] = useState(false);
  return (
    <div className="lj-review-form">
      <p>
        검토 기준 · 낱말의 뜻을 왜곡하지 않고 설명했는가? 선택한 구절과 이유가
        설명을 뒷받침하는가?
      </p>
      <label className="lj-field">
        <span>이번 응답 검토</span>
        <select
          value={outcome}
          onChange={(e) => {
            setOutcome(e.target.value);
            setSaved(false);
          }}
        >
          <option value="">아직 판단하지 않음</option>
          <option value="success">이번 응답에서 목표 수행을 확인함</option>
          <option value="needs_support">추가 지도·확인이 필요함</option>
        </select>
      </label>
      <label className="lj-field">
        <span>관찰 근거와 다음에 도울 점</span>
        <textarea
          rows={2}
          value={note}
          onChange={(e) => {
            setNote(e.target.value);
            setSaved(false);
          }}
          placeholder="실제 구절과 학생의 표현을 바탕으로 기록해 주세요."
        />
      </label>
      <button
        className="rx-button"
        disabled={!outcome || !note.trim()}
        onClick={() => {
          useLearningJourney.getState().review(attemptId, task, submission.id, {
            outcome: outcome as "success" | "needs_support",
            note,
            at: new Date().toISOString(),
          });
          setSaved(true);
        }}
      >
        <Check size={15} />
        {saved ? "검토 기록 반영됨" : "기기에 검토 기록 남기기"}
      </button>
      <small>
        이 기기의 체험 기록에 반영됩니다. 실제 학생에게 전송되지 않습니다.
      </small>
    </div>
  );
}

export function JourneyEntryCard() {
  const { attempts, activeId } = useLearningJourney();
  const attempt = attempts.find((a) => a.id === activeId);
  const open = () => {
    useCoursewareStore.getState().selectGradeAndSlot(5, JOURNEY_SLOT, "journey");
    useCoursewareStore.getState().setActiveRole("student");
  };
  return (
    <section className="lj-entry">
      <div className="lj-entry-icon">
        <LearningIllustration kind="book" />
      </div>
      <div>
        <p className="lj-eyebrow">생각을 배우는 수업 · 초5 대표 읽기</p>
        <h2>{JOURNEY_GOAL}</h2>
        <p>
          {attempt
            ? `${journeyStages.find((s) => s.id === attempt.stage)?.label}부터 이어갈 수 있어요.`
            : "시범을 보고, 함께 연습하고, 다른 글에서 혼자 설명해 봐요."}
        </p>
      </div>
      <button className="rx-button rx-button-primary" onClick={open}>
        {attempt ? "학습 이어가기" : "생각 수업 시작"} <ArrowRight size={17} />
      </button>
    </section>
  );
}

export function LearningEvidenceReport({
  audience,
  attemptId,
}: {
  audience: "student" | "teacher" | "parent";
  attemptId?: string;
}) {
  const { attempts } = useLearningJourney();
  const failed = useReadingStorageStatus((s) => s.failed);
  const [selected, setSelected] = useState("");
  const available = attempts.filter((a) =>
    Object.values(a.responses).some((r) => r.submissions.length),
  );
  const attempt =
    attempts.find((a) => a.id === (attemptId || selected)) ||
    available.slice(-1)[0];
  const rows = attempt
    ? (
        Object.entries(attempt.responses) as [
          TaskId,
          NonNullable<(typeof attempt.responses)[TaskId]>,
        ][]
      ).flatMap(([task, r]) =>
        r.submissions.length
          ? [{ task, r, last: r.submissions.slice(-1)[0]! }]
          : [],
      )
    : [];
  const independent = rows.filter(
    ({ last }) => last.support === "independent" && last.exposure === "new",
  );
  const helped = rows.filter(({ last }) => last.helpLevel > 0);
  const reviewed = rows.filter(({ last }) => last.review);
  const nextMessage = rows.some(
    ({ last }) => last.review?.outcome === "needs_support",
  )
    ? "검토 메모에서 도움이 필요한 부분을 확인하고 다시 연습해요."
    : helped.length
      ? "도움을 받은 질문을 살펴보고, 다음에는 같은 방법을 스스로 사용해 봐요."
      : rows.some(({ last }) => !last.evidenceMatch)
        ? "정의와 예시를 구별해 근거를 고르는 연습을 이어가요."
        : "내 설명이 근거와 맞는지 선생님과 확인한 뒤, 다른 글에서도 사용해 봐요.";
  return (
    <section className="lj-evidence-report">
      <div className="lj-report-heading">
        <div>
          <p className="lj-eyebrow">THINKING RECORD</p>
          <h2>
            {audience === "teacher"
              ? "응답에서 다음 지도를 찾아요"
              : audience === "parent"
                ? "아이가 남긴 근거와 설명"
                : "내가 남긴 생각의 기록"}
          </h2>
        </div>
        {!attemptId && available.length > 1 && (
          <label>
            학습 기록
            <select
              aria-label="살펴볼 학습 기록"
              value={attempt?.id || ""}
              onChange={(e) => setSelected(e.target.value)}
            >
              {available.map((a, i) => (
                <option key={a.id} value={a.id}>
                  {i + 1}번째 학습 ·{" "}
                  {new Date(a.createdAt).toLocaleDateString("ko-KR")}
                </option>
              ))}
            </select>
          </label>
        )}
      </div>
      <p className="lj-muted">{JOURNEY_GOAL} · 이 기기의 체험 기록</p>
      {failed && (
        <p role="alert" className="lj-save-error">
          기기 저장에 실패했어요. 필요한 기록을 복사한 뒤 저장 공간을 확인해
          주세요.
        </p>
      )}
      {!rows.length ? (
        <p className="lj-report-empty">
          생각 수업에서 근거와 설명을 남기면, 도움과 수정 과정을 함께 볼 수
          있어요.
        </p>
      ) : (
        <>
          <details className="rx-report-analysis"><summary>수행 조건과 관찰 지표 자세히 보기</summary><MetricCards
            summary={summarizeReport(journeyReportRecords(attempt!))}
          />
          <p className="lj-muted">
            이 기기의 실제 연습 기록 · 활동별 첫 제출 기준. 선택형 문항이 없는
            수업은 첫 선택 정답률을 표시하지 않습니다. 네 항목 채점표는 운영
            체험 리포트에서 사용할 수 있습니다.
          </p>
          <ReportMethodology /></details>
          <div className="lj-observation-summary">
            <div>
              <b>{rows.length}</b>
              <span>설명을 남긴 활동</span>
            </div>
            <div>
              <b>{independent.length}</b>
              <span>새 글 · 도움 없이 응답</span>
            </div>
            <div>
              <b>{helped.length}</b>
              <span>도움을 펼친 활동</span>
            </div>
            <div>
              <b>
                {reviewed.length} / {rows.length}
              </b>
              <span>교사가 검토한 응답</span>
            </div>
          </div>
          <p className="lj-muted">
            활동별 최근 응답의 수와 수행 조건입니다. 숙련도나 능력 점수가
            아닙니다.
          </p>
          {rows.map(({ task, r, last }) => (
            <details
              className="lj-response-record"
              key={`${attempt!.id}-${task}`}
              open={
                (audience === "student" &&
                  task === rows[rows.length - 1].task) ||
                rows.length === 1 ||
                undefined
              }
            >
              <summary>
                <span>
                  <PenLine size={17} />
                  {journeyStages.find((s) => s.id === task)?.label} ·{" "}
                  {journeyTasks[task].target}
                </span>
                <span className="lj-record-badge">
                  {last.review
                    ? last.review.outcome === "success"
                      ? "이번 수행 확인"
                      : "추가 지도 필요"
                    : "설명 검토 전"}
                </span>
              </summary>
              <div className="lj-record-body">
                <div className="lj-record-conditions">
                  {last.readingLevel && (
                    <span>5학년 · {readingLevelLabels[last.readingLevel]}</span>
                  )}
                  <span>
                    {last.support === "guided"
                      ? "도움과 함께"
                      : last.support === "prompted"
                        ? "도움 줄이는 연습"
                        : "도움 없이 응답"}
                  </span>
                  <span>
                    {last.exposure === "new"
                      ? "처음 연 글의 첫 응답"
                      : "다시 연습한 응답"}
                  </span>
                  {last.helpLevel > 0 && (
                    <span>도움 질문 {last.helpLevel}개</span>
                  )}
                </div>
                <h4>선택한 근거</h4>
                {last.evidence.map((id) => (
                  <blockquote className="lj-record-evidence" key={id}>
                    <Link2 size={14} />
                    {last.evidenceQuotes?.[id] || getSentence(id)?.text}
                  </blockquote>
                ))}
                <h4>나의 설명</h4>
                <p className="lj-student-answer">{last.answer}</p>
                <h4>고른 이유</h4>
                <p>{last.reason}</p>
                {!!last.annotations?.length && (
                  <div className="lj-record-annotations">
                    <h4>응답할 때 남긴 표시와 사고구술</h4>
                    {last.annotations.map((a) => (
                      <blockquote key={a.id}>
                        <b>
                          {annotationKinds[a.kind].symbol} {a.quote}
                        </b>
                        <p>{a.note}</p>
                        {a.linkedSentenceId && (
                          <p>
                            → {a.linkedAnchor?.quote || getSentence(a.linkedSentenceId, attempt)?.text}
                          </p>
                        )}
                        {!!a.revisions?.length && <details><summary>표시와 생각이 바뀐 과정</summary>{a.revisions.map((revision,i)=><div key={`${revision.at}-${i}`}><small>{i===0?"처음 생각":"고치기 전"} · {revision.quote}</small><p>{revision.note}</p></div>)}</details>}
                      </blockquote>
                    ))}
                  </div>
                )}
                {last.helpLevel > 0 && (
                  <details className="lj-used-hints">
                    <summary>사용한 도움 보기</summary>
                    {journeyTasks[task].hints
                      .slice(0, last.helpLevel)
                      .map((h) => (
                        <p key={h}>{h}</p>
                      ))}
                  </details>
                )}
                {r.submissions.length > 1 && (
                  <details className="lj-revisions">
                    <summary>
                      이전 응답 보기 · {r.submissions.length - 1}개
                    </summary>
                    {r.submissions.slice(0, -1).map((s, i) => (
                      <article key={s.id}>
                        <small>
                          {i + 1}번째 응답 ·{" "}
                          {s.support === "independent"
                            ? "도움 없이"
                            : "도움과 함께"}{" "}
                          · {s.exposure === "new" ? "처음 연 글" : "다시 연습"}
                        </small>
                        <p>{s.answer}</p>
                        <p>고른 이유: {s.reason}</p>
                        {s.evidence.map((id) => (
                          <blockquote key={id}>
                            {s.evidenceQuotes?.[id] || getSentence(id)?.text}
                          </blockquote>
                        ))}
                        {s.review && <p>당시 검토: {s.review.note}</p>}
                      </article>
                    ))}
                  </details>
                )}
                {last.review && (
                  <div className="lj-teacher-note">
                    <b>선생님의 검토 메모</b>
                    <p>{last.review.note}</p>
                    <small>이 기기에 남긴 체험 메모</small>
                  </div>
                )}
                {audience === "teacher" && (
                  <LocalReview
                    key={last.id}
                    attemptId={attempt!.id}
                    task={task}
                    submission={last}
                  />
                )}
              </div>
            </details>
          ))}
          {attempt!.revisions.length > 0 && (
            <details className="lj-response-record">
              <summary>
                <span>
                  <PenLine size={17} />
                  근거를 이어 쓴 나의 문장
                </span>
                <span>{attempt!.revisions.length}개 기록</span>
              </summary>
              <div className="lj-record-body">
                {attempt!.revisions.map((r, i) => (
                  <blockquote className="lj-student-answer" key={i}>
                    <small>{i === 0 ? "처음 문장" : `${i}번째 수정`}</small>
                    <p>{r.text}</p>
                  </blockquote>
                ))}
              </div>
            </details>
          )}
          <div className="lj-next-support">
            <b>
              {audience === "parent"
                ? "함께 나눌 이야기"
                : "다음에 도울 한 가지"}
            </b>
            <p>
              {audience === "parent"
                ? "“뜻을 설명하는 문장과 예시를 어떻게 구별했니?” 아이가 고른 구절을 함께 보며 들어주세요."
                : nextMessage}
            </p>
            <small>다음 지도 제안 · 응답과 상황을 보고 조정해 주세요.</small>
          </div>
        </>
      )}
    </section>
  );
}

export function JourneyContentStatus() {
  return (
    <details className="lj-content-status">
      <summary>
        <BookOpen size={18} /> 사고 과정 수업 · 제작 상태{" "}
        <span>대표 목표 1개 / 지문 4편</span>
      </summary>
      <div>
        <p>
          정의·세부 정보 확인 부분을 다루는 체험 수업입니다. 기존 목표 전체의
          성취나 교육과정 매핑을 인증하지 않습니다.
        </p>
        <p>
          생각 시범 3장 · 연습/확인 활동 4개 · 단계별 도움 12개 · 읽기와 쓰기
          연결 · 응답별 교사 검토
        </p>
        <p>
          콘텐츠 버전 2 · 지문 네 편 × 세 수준 · 자체 작성 초안 · 정식 게시 전
          교육·사실·학년 적합성 검토 필요
        </p>
      </div>
    </details>
  );
}
