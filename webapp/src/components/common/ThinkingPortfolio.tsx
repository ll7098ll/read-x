import React, { useMemo, useState } from "react";
import { ArrowRight, BookOpen, Check, MessageCircle, PenLine } from "lucide-react";
import { useLearningJourney } from "../../store/useLearningJourney";
import { useReadingWorkspace, useReadingStorageStatus } from "../../store/useReadingWorkspace";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { progressiveLessons, progressiveLessonAtLevel, progressivePassage } from "../../data/progressiveReading";
import { corpusLessons } from "../../data/corpusReading";
import { readingLevels, readingLevelLabels } from "../../data/readingPolicy";
import type { ProgressiveRun, ProgressiveSubmission } from "../../services/progressiveReading";
import { AnnotationNotes, MarkedSentence } from "../student/ReadingAnnotations";
import { LearningEvidenceReport } from "./LearningEvidenceReport";

export function collectThinkingRecords(sessions: Record<string, Record<string, unknown>>) {
  return Object.entries(sessions).flatMap(([key, session]) => {
    const run = session["progressive-v1"] as ProgressiveRun | undefined;
    if (!run?.responses || !Array.isArray(run.annotations)) return [];
    const source = [...corpusLessons, ...progressiveLessons].find(l => readingLevels.some(level => key === `${l.id}-${level}`));
    const level = readingLevels.find(l => key.endsWith(`-${l}`));
    if (!source || !level) return [];
    const lesson = progressiveLessonAtLevel(source, level);
    const runs = [{ responses: run.responses, archiveIndex: -1 }, ...(run.archives || []).map((a, archiveIndex) => ({ responses: a.responses, archiveIndex }))];
    return runs.flatMap(({ responses, archiveIndex }) => Object.entries(responses).flatMap(([questionId, response]) => {
      const last = response?.submissions?.slice(-1)[0];
      const q = last?.questionSnapshot || lesson.questions.find(q => q.id === questionId);
      return last && q ? [{ key, archiveIndex, lesson, level, q, response, last, passage: last.passageSnapshot || progressivePassage(lesson, level) }] : [];
    }));
  }).sort((a,b) => b.last.at.localeCompare(a.last.at));
}

function reviewRecord(key: string, archiveIndex: number, questionId: string, submissionId: string, review: NonNullable<ProgressiveSubmission["review"]>) {
  const current=useReadingWorkspace.getState().sessions[key]?.["progressive-v1"] as ProgressiveRun | undefined;
  if(!current)return;
  const responses=archiveIndex<0?current.responses:current.archives[archiveIndex]?.responses;
  const response=responses?.[questionId];
  if(!response)return;
  const updated={...responses,[questionId]:{...response,submissions:response.submissions.map(s=>s.id===submissionId?{...s,review}:s)}};
  useReadingWorkspace.getState().save(key,"progressive-v1",archiveIndex<0?{...current,responses:updated}:{...current,archives:current.archives.map((a,i)=>i===archiveIndex?{...a,responses:updated}:a)});
}

export function useThinkingPending() {
  const attempts=useLearningJourney(s=>s.attempts);
  const sessions=useReadingWorkspace(s=>s.sessions);
  return attempts.flatMap(a=>Object.values(a.responses)).filter(r=>r.submissions.length&&!r.submissions[r.submissions.length-1].review).length+collectThinkingRecords(sessions).filter(r=>!r.last.review).length;
}

export function PracticeOverview({ onReview }: { onReview: () => void }) {
  const attempts = useLearningJourney(s => s.attempts);
  const sessions = useReadingWorkspace(s => s.sessions);
  const progressive = useMemo(() => collectThinkingRecords(sessions), [sessions]);
  const latest = attempts.flatMap(a => Object.values(a.responses).flatMap(r => r.submissions.length ? [r.submissions[r.submissions.length - 1]] : []));
  const pending = latest.filter(s => !s.review).length + progressive.filter(r => !r.last.review).length;
  const revisions = latest.filter(s => s.exposure === "practiced").length + progressive.filter(r => r.response.submissions.length > 1).length;
  return <section className="rx-process-overview"><div><p className="rx-eyebrow">학생이 남긴 생각에서 시작하는 지도</p><h2>어느 구절에서 생각이 갈렸을까요?</h2><p>이 기기에 작성한 실제 연습의 표시·이유·수정을 함께 확인해요.</p></div><div className="rx-overview-counts"><span><b>{pending}</b>검토할 응답</span><span><b>{latest.length + progressive.length}</b>기록된 활동</span><span><b>{revisions}</b>다시 살필 응답</span></div><button type="button" className="rx-button rx-button-primary" onClick={onReview}>생각 살펴보기 <ArrowRight size={16}/></button></section>;
}

export function RecentThinkingFeedback({ onOpen }: { onOpen: () => void }) {
  const attempts=useLearningJourney(s=>s.attempts);
  const sessions=useReadingWorkspace(s=>s.sessions);
  const feedback=[...attempts.flatMap(a=>Object.values(a.responses).flatMap(r=>r.submissions.slice(-1).flatMap(s=>s.review?[s.review]:[]))),...collectThinkingRecords(sessions).flatMap(r=>r.last.review?[r.last.review]:[])].sort((a,b)=>b.at.localeCompare(a.at))[0];
  if(!feedback)return null;
  return <section className="rx-home-feedback"><MessageCircle size={22}/><div><span>선생님과 이어가는 생각</span><p>{feedback.note}</p></div><button className="rx-text-link" onClick={onOpen}>내 생각과 함께 보기 <ArrowRight size={16}/></button></section>;
}

function ProgressiveReview({ submission, onSave }: { submission: ProgressiveSubmission; onSave: (review: NonNullable<ProgressiveSubmission["review"]>) => void }) {
  const [outcome,setOutcome] = useState(submission.review?.outcome || "");
  const [note,setNote] = useState(submission.review?.note || "");
  const failed = useReadingStorageStatus(s => s.failed);
  const [saved,setSaved] = useState(false);
  return <div className="lj-review-form"><b>이 응답에서 확인한 읽기 방법</b><p>고른 구절과 설명이 연결되는지, 조건과 관계를 적절히 살폈는지 확인해 주세요.</p><label className="lj-field"><span>수행 확인</span><select value={outcome} onChange={e=>{setOutcome(e.target.value);setSaved(false);}}><option value="">검토 전</option><option value="success">이번 수행에서 확인함</option><option value="needs_support">추가 지도와 확인이 필요함</option></select></label><label className="lj-field"><span>구절·이유에 대한 피드백과 다음 질문</span><textarea rows={3} value={note} onChange={e=>{setNote(e.target.value);setSaved(false);}} placeholder="어느 구절을 다시 보면 좋을지 구체적으로 남겨요."/></label><button className="rx-button rx-button-primary" disabled={!outcome || !note.trim()} onClick={()=>{onSave({outcome:outcome as "success" | "needs_support",note:note.trim(),at:new Date().toISOString()});setSaved(true);}}><Check size={16}/>검토와 피드백 남기기</button>{saved&&<p role="status">{failed?"기기에 저장하지 못했습니다. 피드백을 복사해 주세요.":"이 기기의 학생·학부모 기록에 피드백을 반영했어요."}</p>}</div>;
}

export function ThinkingPortfolio({ audience }: { audience: "student" | "teacher" | "parent" }) {
  const hasJourney=useLearningJourney(s=>s.attempts.some(a=>Object.values(a.responses).some(r=>r.submissions.length)));
  const sessions = useReadingWorkspace(s => s.sessions);
  const records = useMemo(()=>collectThinkingRecords(sessions),[sessions]);
  const [onlyPending,setOnlyPending] = useState(false);
  const [showAll,setShowAll] = useState(false);
  const filtered = onlyPending ? records.filter(r=>!r.last.review) : records;
  const visible = showAll ? filtered : filtered.slice(0,6);
  return <div className="rx-thinking-portfolio">
    {hasJourney&&<LearningEvidenceReport audience={audience}/>}
    {(records.length>0||!hasJourney)&&<section className="rx-portfolio-section">
      <div className="rx-section-title"><div><p className="rx-eyebrow">근거에서 내 설명까지</p><h2>{audience === "teacher" ? "교과 읽기에서 남긴 생각" : audience === "parent" ? "글을 읽으며 남긴 아이의 생각" : "내가 표시하고 연결한 생각"}</h2></div>{audience === "teacher" && <label className="rx-pending-filter"><input type="checkbox" checked={onlyPending} onChange={e=>setOnlyPending(e.target.checked)}/>검토 전만 보기</label>}</div>
      <p className="rx-muted">같은 글에서의 연습과 도움 조건을 함께 보아요. 이 기기에 직접 작성한 기록입니다.</p>
      {!visible.length && <div className="rx-portfolio-empty"><BookOpen size={26}/><h3>{onlyPending?"검토 대기 응답이 없어요":"아직 남긴 생각이 없어요"}</h3><p>{onlyPending?"모든 응답을 보려면 필터를 해제해 주세요.":"글에 표시하고 내 생각을 설명하면 이곳에서 처음 생각과 수정한 생각을 만날 수 있어요."}</p>{audience === "student" && <button className="rx-button" onClick={()=>useCoursewareStore.getState().setStudentMode("progressive")}>읽기 연습 시작 <ArrowRight size={16}/></button>}</div>}
      {visible.map(record=>{
        const {key,lesson,q,response,last,passage} = record;
        const first = response.submissions[0];
        return <details className="rx-thinking-case" key={last.id} open={audience === "teacher" && !last.review || undefined}>
          <summary><span><PenLine size={17}/><b>{lesson.title}</b><small>{q.skill}</small></span><span className="rx-case-status">{last.review ? last.review.outcome === "success"?"교사 확인":"다음 지도 있음":"설명 검토 전"}</span></summary>
          <div className="rx-case-content"><p className="rx-case-context">{lesson.grade}학년 · {readingLevelLabels[record.level]} · {last.support === "guided"?"도움과 함께":"질문 도움 없이"} · 같은 글의 연습 · {new Date(last.at).toLocaleDateString("ko-KR",{timeZone:"Asia/Seoul"})}</p><h3>{q.prompt}</h3>
            <div className="rx-case-columns"><div className="rx-case-source"><h4>살펴본 본문</h4>{last.passageSnapshot?passage.paragraphs.filter(p=>last.evidence.includes(p.id)||p.sentences.some(s=>last.annotations.some(a=>a.sentenceId===s.id))).map(p=><p key={p.id}>{p.sentences.map(s=><MarkedSentence key={s.id} text={s.text} marks={last.annotations.filter(a=>a.sentenceId===s.id)}/>)}</p>):<p className="rx-muted">이전 형식의 기록입니다. 저장한 원문이 없어 당시 표시한 인용문을 보여드려요.</p>}<AnnotationNotes annotations={last.annotations} passage={last.passageSnapshot||{...passage,paragraphs:[]}}/></div><div><h4>{response.submissions.length>1?"생각은 이렇게 달라졌어요":"내 설명"}</h4>{response.submissions.length>1&&<blockquote className="rx-first-thought"><small>처음 생각</small><p>{first.reason}</p></blockquote>}<blockquote className="rx-current-thought"><small>{response.submissions.length>1?"고친 생각":"직접 남긴 생각"}</small><p>{last.reason}</p></blockquote>{last.review&&<div className="rx-feedback-note"><MessageCircle size={17}/><div><b>선생님 피드백</b><p>{last.review.note}</p></div></div>}
            {audience === "teacher"&&<ProgressiveReview key={`${last.id}-${last.review?.at||"new"}`} submission={last} onSave={review=>reviewRecord(key,record.archiveIndex,q.id,last.id,review)}/>}
            </div></div>
          </div>
        </details>;
      })}
      {filtered.length>6&&<button className="rx-button" onClick={()=>setShowAll(!showAll)}>{showAll?"최근 기록만 보기":`기록 ${filtered.length}개 모두 보기`}</button>}
    </section>}
  </div>;
}
