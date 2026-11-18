import { LearningIllustration } from "../brand/LearningIllustration";
import React, { useEffect, useRef, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  BookOpen,
  Check,
  ChevronRight,
  CircleHelp,
  Eye,
  Lightbulb,
  MessageCircle,
  Link2,
  PenLine,
  RotateCcw,
  SlidersHorizontal,
  Sparkles,
} from "lucide-react";
import {
  journeyStages,
  getJourneyPassages,
  journeyTasks,
  modelSteps,
  JOURNEY_GOAL,
  JOURNEY_SLOT,
  getSentence,
  isTaskStage,
  type JourneyStage,
} from "../../data/learningJourney";
import { emptyResponse, responseChanged, type JourneyAnnotation } from "../../services/learningJourney";
import type { TextAnchor } from "../../services/annotations";
import { useLearningJourney } from "../../store/useLearningJourney";
import {
  useReadingWorkspace,
  useReadingStorageStatus,
} from "../../store/useReadingWorkspace";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { LearningEvidenceReport } from "../common/LearningEvidenceReport";
import { ReadXSymbol } from "../brand/ReadXBrand";
import { AnnotationEditor, AnnotationNotes, MarkedSentence, AnnotationUndo, selectedTextAnchor } from "./ReadingAnnotations";
import { assessPassage, readingLevels, readingLevelLabels } from "../../data/readingPolicy";
import { journeyVocabulary } from "../../data/journeyTextExtensions";
import { useModelScript } from "../../store/useThinkingScript";

export function LearningJourneyStudio() {
  const store = useLearningJourney();
  const modelScript = useModelScript();
  const attempt = store.attempts.find((a) => a.id === store.activeId);
  const failed = useReadingStorageStatus((s) => s.failed);
  const [pane, setPane] = useState<"text" | "activity">("activity");
  const [fontSize, setFontSize] = useState(22);
  const [theme, setTheme] = useState("paper");
  const [preview, setPreview] = useState<string | null>(null);
  const [focusQuote, setFocusQuote] = useState("");
  const [annotating, setAnnotating] = useState("");
  const [markMode, setMarkMode] = useState(true);
  const [editingAnnotation, setEditingAnnotation] = useState<JourneyAnnotation>();
  const [initialAnchor, setInitialAnchor] = useState<TextAnchor>();
  const [modelTrail, setModelTrail] = useState(true);
  const selectedRange = useRef<TextAnchor | null>(null);
  const heading = useRef<HTMLHeadingElement>(null);
  const feedback = useRef<HTMLDivElement>(null);
  const quoteRefs = useRef<Record<string, HTMLButtonElement | null>>({});
  useEffect(() => {
    if (!useLearningJourney.getState().activeId)
      useLearningJourney.getState().start();
    useReadingWorkspace.getState().visit(JOURNEY_SLOT);
  }, []);
  useEffect(() => {
    if (focusQuote) {
      quoteRefs.current[focusQuote]?.focus();
      quoteRefs.current[focusQuote]?.scrollIntoView({
        block: "center",
        behavior: "auto",
      });
    }
  }, [focusQuote, preview, pane]);
  useEffect(() => {
    if (attempt?.stage !== "model") return;
    const frame = requestAnimationFrame(() => quoteRefs.current[modelScript[attempt.modelStep].anchor]?.scrollIntoView({ block: "center", behavior: "auto" }));
    return () => cancelAnimationFrame(frame);
  }, [attempt?.stage, attempt?.modelStep]);
  if (!attempt)
    return (
      <section className="lj-loading" role="status">
        생각하는 수업을 준비하고 있어요.
      </section>
    );
  const index = journeyStages.findIndex((s) => s.id === attempt.stage);
  const journeyPassages = getJourneyPassages(attempt);
  const step = journeyStages[index];
  const taskId = isTaskStage(attempt.stage) ? attempt.stage : null;
  const task = taskId ? journeyTasks[taskId] : null;
  const response = taskId
    ? attempt.responses[taskId] || emptyResponse()
    : emptyResponse();
  const check = taskId === "independent" || taskId === "transfer";
  const latest = response.submissions.slice(-1)[0];
  const taskAnnotations = (attempt.annotations || []).filter(a => task && a.passageId === journeyPassages[task.passage].id);
  const dirty = responseChanged(response, taskAnnotations);
  const passageKey = preview || task?.passage || "solution";
  const passage = journeyPassages[passageKey];
  const level = attempt.readingLevel || "standard";
  const metrics = assessPassage(passage.paragraphs.map(p => p.sentences.map(s => s.text).join(" ")), 5, level);
  const annotations = (attempt.annotations || []).filter(a => a.passageId === passage.id);
  const selectable = !!taskId && task?.passage === passageKey;
  const showReader =
    !["start", "reflection", "writing"].includes(attempt.stage) || !!preview;
  const model = modelScript[attempt.modelStep];
  const go = (stage: JourneyStage) => {
    store.navigate(stage);
    setPreview(null);
    setFocusQuote("");
    setAnnotating("");
    setMarkMode(true);
    setPane("activity");
    requestAnimationFrame(() => {
      heading.current?.focus();
      heading.current?.scrollIntoView({ block: "start" });
    });
  };
  const next = () =>
    go(journeyStages[Math.min(index + 1, journeyStages.length - 1)].id);
  const source = (id: string) => {
    const key = Object.entries(journeyPassages).find(([, p]) =>
      p.paragraphs.some((x) => x.sentences.some((s) => s.id === id)),
    )?.[0];
    if (key) {
      setPreview(key);
      setFocusQuote(id);
      setPane("text");
    }
  };
  const openAnnotation = (id: string, annotation?: JourneyAnnotation, anchor?: TextAnchor) => {
    setEditingAnnotation(annotation); setInitialAnchor(anchor); setAnnotating(id);
    selectedRange.current = null;
  };
  const useThought = (a: JourneyAnnotation) => {
    if (!taskId) return;
    store.edit(taskId, { reason: response.reason.includes(a.note) ? response.reason : [response.reason, a.note].filter(Boolean).join("\n"), evidence: [...new Set([...response.evidence, a.sentenceId, ...(a.linkedSentenceId ? [a.linkedSentenceId] : [])])] });
    setPane("activity");
  };
  const allEvidence = [
    ...new Set(
      ["guided", "faded"].flatMap(
        (t) => attempt.responses[t as "guided" | "faded"]?.evidence || [],
      ),
    ),
  ];
  const previousRevision = attempt.revisions.slice(-1)[0];
  const evidenceChanged =
    previousRevision &&
    JSON.stringify(previousRevision.evidence) !== JSON.stringify(allEvidence);
  const trace = (expanded = false) => (
    <details className="lj-trace" open={expanded || undefined}>
      <summary>
        <Link2 size={16} /> 내 생각의 흔적 <span>근거에서 설명까지</span>
      </summary>
      {Object.entries(attempt.responses).filter(
        ([, r]) => r.evidence.length || r.answer,
      ).length ? (
        Object.entries(attempt.responses)
          .filter(([, r]) => r.evidence.length || r.answer)
          .map(([id, r]) => (
            <article key={id}>
              <small>
                {journeyStages.find((s) => s.id === id)?.label} · 내가 남긴 생각
              </small>
              {r.evidence.map((e) => (
                <button className="lj-source" key={e} onClick={() => source(e)}>
                  <Link2 size={14} />
                  {getSentence(e, attempt)?.text}
                </button>
              ))}
              <p>{r.answer || "아직 설명을 쓰지 않았어요."}</p>
              {r.reason && <p className="lj-muted">고른 이유 · {r.reason}</p>}
              {(attempt.annotations || []).filter(a => a.passageId === journeyPassages[journeyTasks[id as keyof typeof journeyTasks].passage].id).map(a => <div className="lj-margin-note" key={a.id}><button className="lj-source" onClick={() => source(a.sentenceId)}>{a.quote}</button><p>{a.note}</p></div>)}
            </article>
          ))
      ) : (
        <p className="lj-muted">직접 고른 근거와 쓴 설명이 이곳에 이어져요.</p>
      )}
    </details>
  );

  return (
    <div className="lj-studio">
      <div className="lj-meta">
        <span>
          <span className="lj-dot" /> 생각을 배우는 읽기 <b>정의·세부 정보</b>
        </span>
        <span role="status" className={failed ? "lj-save-error" : ""}>
          {failed
            ? "기기 저장 실패 · 창을 닫기 전 내용을 복사해 주세요"
            : "이 기기에 자동 저장"}
        </span>
      </div>
      {attempt.version === 1 && <div className="lj-version-notice"><p>이전 분량으로 저장된 수업이에요. 더 긴 글과 수준 선택을 사용하려면 새 연습을 시작해요.</p><button className="rx-button" onClick={() => { store.start(); setPreview(null); }}>기록을 보관하고 새 지문 시작</button></div>}
      <header className="lj-heading">
        <div>
          <p className="rx-eyebrow">TODAY’S READING GOAL</p>
          <h1>{JOURNEY_GOAL}</h1>
        </div>
        <span className="lj-unit">
          01 <span>/ 사고 과정 수업</span>
        </span>
      </header>
      <ol className="lj-grr" aria-label="세 단계 읽기">
        {[{ label: "시범", detail: "표시하는 까닭 듣기", stages: ["start", "model"] }, { label: "같이 해보기", detail: "표시하고 생각 말하기", stages: ["guided", "faded", "writing"] }, { label: "스스로 해보기", detail: "새 글에 직접 적용하기", stages: ["independent", "transfer", "reflection"] }].map((phase, i) => <li key={phase.label} aria-current={phase.stages.includes(attempt.stage) ? "step" : undefined}><span>{i + 1}</span><div><b>{phase.label}</b><small>{phase.detail}</small></div></li>)}
      </ol>
      <details className="rx-course-outline"><summary>{step.label} · 전체 학습 과정 살펴보기</summary><nav className="lj-progress" aria-label="수업 과정">
        {journeyStages.map((s, i) => (
          <button
            key={s.id}
            disabled={i > attempt.reached}
            aria-current={s.id === attempt.stage ? "step" : undefined}
            onClick={() => go(s.id)}
          >
            <LearningIllustration kind={s.id} />
            <span className="lj-stage-label">
              <small>{String(i + 1).padStart(2, "0")}</small>
              {s.label}
            </span>
          </button>
        ))}
      </nav></details>
      <section className="lj-step-heading">
        <div>
          <p className="lj-eyebrow">
            {step.label}{" "}
            <span>· {String(index + 1).padStart(2, "0")} / 08</span>
          </p>
          <h2 ref={heading} tabIndex={-1}>
            {step.title}
          </h2>
          <p>{step.description}</p>
        </div>
        {index > 0 && (
          <button
            className="lj-back"
            onClick={() => go(journeyStages[index - 1].id)}
          >
            <ArrowLeft size={16} /> 이전 과정
          </button>
        )}
      </section>

      {attempt.stage === "start" ? (
        <div className="lj-intro">
          <section className="lj-intro-main">
            <fieldset className="lj-level-picker"><legend>5학년 · 오늘 읽을 글</legend><p>읽기 목표는 같고, 분량과 추가 개념이 달라요.</p>
              {readingLevels.map(l => <button key={l} type="button" aria-pressed={level === l && attempt.version === 2} onClick={() => { if (l !== level || attempt.version === 1) store.start(l); }}><b>{readingLevelLabels[l]}</b><small>{l === "supported" ? "짧은 설명 · 쉬운 예" : l === "standard" ? "비교 · 조건 함께 읽기" : "반례 · 설명의 범위 살피기"}</small></button>)}
              <small>글을 바꾸면 새 연습 기록을 만들어요. 같은 소재를 다시 읽은 기록은 남아요.</small>
            </fieldset>
            <span className="lj-intro-symbol">
              <ReadXSymbol />
            </span>
            <p className="lj-eyebrow">오늘 배울 읽기 방법</p>
            <h2>
              무엇을 설명하는 말인지
              <br />
              <em>정확히 연결해 봐요.</em>
            </h2>
            <p>
              뜻을 묻는 낱말을 확인하고, 글에서 설명을 찾고,
              <br className="lj-desktop-break" /> 내 말이 원문과 맞는지
              비교해요.
            </p>
            <button
              className="rx-button rx-button-primary rx-button-lg"
              onClick={() => go("model")}
            >
              생각하는 방법부터 보기 <ArrowRight size={18} />
            </button>
            <button
              className="lj-text-button"
              onClick={() => go("independent")}
            >
              방법을 알고 있어요. 혼자 먼저 해볼래요 <ChevronRight size={16} />
            </button>
          </section>
          <aside className="lj-intro-aside">
            <p className="lj-eyebrow">작은 도움에서, 스스로 읽기까지</p>
            {[
              [
                Eye,
                "생각하는 방법을 보고",
                "선생님이 어디를 왜 읽는지 따라가요.",
              ],
              [
                PenLine,
                "직접 찾고 설명하고",
                "내가 고른 근거가 나의 문장으로 이어져요.",
              ],
              [
                Sparkles,
                "다른 글에도 사용해요",
                "과학에서 생활, 사회로 주제를 넓혀 봐요.",
              ],
            ].map(([Icon, title, text]: any, i) => (
              <div key={title}>
                <span>{<Icon size={21} />}</span>
                <div>
                  <small>0{i + 1}</small>
                  <h3>{title}</h3>
                  <p>{text}</p>
                </div>
              </div>
            ))}
            <p className="lj-intro-note">
              어려울 때는 도움을 펼쳐도 괜찮아요.
              <br />
              도움을 받은 부분도 소중한 학습 기록이에요.
            </p>
          </aside>
        </div>
      ) : (
        <>
          {showReader && (
            <div className="lj-mobile-switch" aria-label="학습 화면 전환">
              <button
                aria-pressed={pane === "text"}
                onClick={() => setPane("text")}
              >
                <BookOpen size={17} /> 글 읽기{" "}
                {response.evidence.length > 0 &&
                  `· 근거 ${response.evidence.length}`}
              </button>
              <button
                aria-pressed={pane === "activity"}
                onClick={() => setPane("activity")}
              >
                <PenLine size={17} /> {step.label}
              </button>
              {pane === "text" && task && (
                <p className="lj-mobile-question">{task.prompt}</p>
              )}
            </div>
          )}
          <div
            className={`lj-workspace ${showReader ? "" : "lj-workspace-wide"}`}
            data-pane={pane}
          >
            {showReader && (
              <section
                className="lj-reader"
                data-theme={theme}
                aria-label="읽기 본문"
              >
                <div className="lj-reader-top">
                  <span>
                    <BookOpen size={16} /> {passage.subject}
                  </span>
                  <details className="lj-settings">
                    <summary>
                      <SlidersHorizontal size={16} /> 읽기 설정
                    </summary>
                    <div>
                      <label>
                        글자 크기{" "}
                        <input
                          aria-label="본문 글자 크기"
                          type="range"
                          min="18"
                          max="28"
                          value={fontSize}
                          onChange={(e) => setFontSize(+e.target.value)}
                        />
                      </label>
                      <label>
                        배경{" "}
                        <select
                          value={theme}
                          onChange={(e) => setTheme(e.target.value)}
                        >
                          <option value="paper">종이</option>
                          <option value="sepia">따뜻하게</option>
                          <option value="dark">어둡게</option>
                        </select>
                      </label>
                    </div>
                  </details>
                </div>
                <h2>{passage.title}</h2>
                <p className="lj-reading-metrics">5학년 · {attempt.version === 1 ? "이전 짧은 글" : readingLevelLabels[level]} · {metrics.chars.toLocaleString()}자 · {metrics.words}어절 · {metrics.paragraphs}문단</p>
                <div className="lj-annotation-legend"><b>{attempt.stage === "model" ? "선생님 시범" : "내 생각 표시"}</b><span>□ 대상</span><span>밑줄 · 근거</span><span>→ 연결</span></div>
                {selectable && <AnnotationUndo available={!!attempt.annotationHistory?.length} onUndo={store.undoAnnotation}/>}
                {selectable && <div className="lj-reader-modes"><button aria-pressed={!markMode} onClick={() => { setMarkMode(false); setAnnotating(""); }}>문장을 근거로 고르기</button><button aria-pressed={markMode} onClick={() => setMarkMode(true)}>구절에 생각 표시하기</button></div>}
                <p className="lj-reader-caption">
                  {selectable
                    ? markMode ? "구절을 드래그하거나 문장을 눌러 표시해요. 선택한 이유는 내 설명으로 가져올 수 있어요." : "근거로 쓸 문장을 눌러 선택해요. 다시 누르면 해제돼요."
                    : attempt.stage === "model"
                      ? "시범에서 살펴보는 구절을 본문과 함께 읽어요."
                      : "내가 고른 근거를 원문에서 다시 확인해요."}
                </p>
                <div className="lj-passage" style={{ fontSize }}>
                  {passage.paragraphs.map((p, i) => (
                    <div className="lj-paragraph" key={p.id}>
                      <span
                        className="lj-para-number"
                        aria-label={`${i + 1}문단`}
                      >
                        {String(i + 1).padStart(2, "0")}
                      </span>
                      <p>
                        {p.sentences.map((s) => (
                          <React.Fragment key={s.id}>
                            <button
                              ref={(el) => {
                                quoteRefs.current[s.id] = el;
                              }}
                              className={`lj-sentence ${response.evidence.includes(s.id) ? "is-selected" : ""} ${attempt.stage === "model" && model.anchor === s.id ? "is-model" : ""} ${focusQuote === s.id ? "is-focused" : ""}`}
                              aria-pressed={
                                selectable && !markMode
                                  ? response.evidence.includes(s.id)
                                  : undefined
                              }
                              aria-label={
                                selectable
                                  ? markMode ? `${s.text} 생각 표시` : `${s.text} 근거 ${response.evidence.includes(s.id) ? "해제" : "선택"}`
                                  : s.text
                              }
                              onMouseUp={(e) => { const text = e.currentTarget.querySelector<HTMLElement>(".rx-selectable-text"); selectedRange.current = text && selectable ? selectedTextAnchor(text, s.id, s.text) : null; }}
                              onTouchEnd={(e) => { const text = e.currentTarget.querySelector<HTMLElement>(".rx-selectable-text"); const range = text && selectable ? selectedTextAnchor(text, s.id, s.text) : null; if (range) { setMarkMode(true); openAnnotation(s.id, undefined, range); } }}
                              onClick={() => {
                                if (selectable && (markMode || selectedRange.current)) openAnnotation(s.id, undefined, selectedRange.current || undefined);
                                else if (taskId && selectable)
                                  store.edit(taskId, {
                                    evidence: response.evidence.includes(s.id)
                                      ? response.evidence.filter(
                                          (id) => id !== s.id,
                                        )
                                      : [...response.evidence, s.id],
                                  });
                                else setFocusQuote(s.id);
                              }}
                            >
                              <span className="rx-selectable-text"><MarkedSentence text={s.text} marks={attempt.stage === "model" ? (modelTrail ? modelSteps.slice(0, attempt.modelStep + 1) : [model]).filter(m => m.anchor === s.id).map(m => m.marking) : annotations.filter(a => a.sentenceId === s.id)} /></span>
                              {response.evidence.includes(s.id) && (
                                <Check size={14} aria-label="선택한 근거" />
                              )}
                            </button>{" "}
                          </React.Fragment>
                        ))}
                      </p>
                      {attempt.stage === "model" && p.sentences.some(s => s.id === model.anchor) && <aside className="lj-inline-model"><b>{model.marking.label} · 선생님 생각</b><p>“{model.thought}”</p>{attempt.modelStep === 2 && <p className="lj-model-relation">□ 용질 → 녹는 물질 → 예: 소금</p>}</aside>}
                      <AnnotationNotes annotations={annotations.filter(a => p.sentences.some(s => s.id === a.sentenceId))} passage={passage} onRemove={selectable ? store.removeAnnotation : undefined} onEdit={selectable ? a => openAnnotation(a.sentenceId, a) : undefined} onUse={selectable ? useThought : undefined}/>
                      {selectable && p.sentences.some(s => s.id === annotating) && <AnnotationEditor key={`${attempt.id}-${annotating}-${editingAnnotation?.id || initialAnchor?.start || "new"}`} passage={passage} sentenceId={annotating} annotation={editingAnnotation} initialAnchor={initialAnchor} guided={attempt.stage === "guided"} onSave={store.annotate} onClose={() => setAnnotating("")} />}
                    </div>
                  ))}
                </div>
                {!check && <details className="lj-vocabulary"><summary>읽기를 돕는 낱말</summary>{journeyVocabulary.filter(v => readingLevels.indexOf(v.level) <= readingLevels.indexOf(level) && passage.paragraphs.some(p => p.sentences.some(s => s.text.includes(v.word)))).map(v => <p key={v.word}><b>{v.word}</b> · {v.meaning}</p>)}</details>}
                <div className="lj-reader-foot">
                  <span>
                    {attempt.stage === "model"
                      ? "밑줄 · 선생님이 살펴보는 부분"
                      : response.evidence.length
                        ? `내가 고른 근거 ${response.evidence.length}개`
                        : "글을 다시 읽어도 괜찮아요"}
                  </span>
                  <span>ReadX · 읽기의 발견</span>
                </div>
                {preview && (
                  <button
                    className="lj-text-button"
                    onClick={() => {
                      setPreview(null);
                      setFocusQuote("");
                      setPane("activity");
                    }}
                  >
                    내 작업으로 돌아가기 <ArrowRight size={15} />
                  </button>
                )}
              </section>
            )}

            <div className="lj-activity">
              {attempt.stage === "model" && (
                <section className="lj-model-card">
                  <div className="lj-card-kicker">
                    <Lightbulb size={18} /> 선생님의 생각{" "}
                    <span>시범 {attempt.modelStep + 1} / 3</span>
                  </div>
                  <h3>{model.label}</h3>
                  <blockquote>“{model.quote}”</blockquote>
                  <p className="lj-thought">본문 옆의 생각 말풍선을 읽고, 표시한 까닭을 자신의 말로 따라 해 봐요.</p>
                  <div className="lj-model-dots" aria-label="시범 순서">
                    {modelSteps.map((m, i) => (
                      <button
                        key={i}
                        aria-label={`${i + 1}. ${m.label}`}
                        aria-pressed={attempt.modelStep === i}
                        onClick={() => store.model(i)}
                      >
                        {i + 1}
                      </button>
                    ))}
                  </div>
                  <p className="lj-muted">
                    본문의 표시된 부분과 선생님의 생각을 비교해 봐요.
                  </p>
                  <label className="rx-model-trail"><input type="checkbox" checked={modelTrail} onChange={e => setModelTrail(e.target.checked)}/> 앞에서 살핀 표시도 함께 보기</label>
                  <button
                    className="rx-button rx-button-primary"
                    onClick={() =>
                      attempt.modelStep < 2
                        ? store.model(attempt.modelStep + 1)
                        : next()
                    }
                  >
                    {attempt.modelStep < 2
                      ? "다음 생각 보기"
                      : "이제 같이 해보기"}{" "}
                    <ArrowRight size={17} />
                  </button>
                </section>
              )}

              {taskId && task && (
                <section className="lj-task-card">
                  <div className="lj-card-kicker">
                    <PenLine size={17} /> 내가 해볼 일{" "}
                    <span>
                      {check
                        ? response.helpLevel
                          ? "도움과 함께 연습"
                          : "혼자 확인해요"
                        : step.label}
                    </span>
                  </div>
                  <h3>{task.prompt}</h3>
                  {check && (
                    <p className="lj-check-note">
                      {attempt.exposures[
                        `${journeyPassages[task.passage].id}@${journeyPassages[task.passage].version}`
                      ] === "practiced"
                        ? "전에 열어본 글이에요. 이번 응답은 다시 연습한 기록으로 남아요."
                        : "설명은 선생님이 근거와 함께 확인해요. 도움을 펼치면 도움을 받은 연습으로 남아요."}
                    </p>
                  )}
                  <div className="lj-evidence-input">
                    <label>
                      01 <b>글에서 고른 근거</b>
                    </label>
                    {response.evidence.length ? (
                      response.evidence.map((id) => (
                        <div className="lj-selected-quote" key={id}>
                          <button
                            onClick={() => {
                              setFocusQuote(id);
                              setPane("text");
                            }}
                          >
                            <Link2 size={14} />
                            {getSentence(id, attempt)?.text}
                          </button>
                          <button
                            aria-label={`근거 삭제: ${getSentence(id, attempt)?.text}`}
                            onClick={() =>
                              store.edit(taskId, {
                                evidence: response.evidence.filter(
                                  (x) => x !== id,
                                ),
                              })
                            }
                          >
                            ×
                          </button>
                        </div>
                      ))
                    ) : (
                      <button
                        className="lj-pick-prompt"
                        onClick={() => {
                          setPane("text");
                          requestAnimationFrame(() =>
                            quoteRefs.current[
                              passage.paragraphs[0].sentences[0].id
                            ]?.focus(),
                          );
                        }}
                      >
                        <BookOpen size={18} /> 본문에서 설명하는 문장을 골라요{" "}
                        <ArrowRight size={15} />
                      </button>
                    )}
                  </div>
                  <label className="lj-field">
                    <span>
                      02 <b>{task.target}의 뜻을 내 말로 설명해요</b>
                    </span>
                    <textarea
                      rows={3}
                      value={response.answer}
                      onChange={(e) =>
                        store.edit(taskId, { answer: e.target.value })
                      }
                      placeholder="고른 근거와 연결해 설명해 보세요."
                    />
                  </label>
                  {attempt.version >= 2 && <p className="lj-muted">뜻을 찾은 뒤에는 다른 문단의 예와 비교해 보세요. 정의를 뒷받침하는 사례도 근거로 함께 고를 수 있어요.</p>}
                  <label className="lj-field">
                    <span>
                      03 <b>이 구절을 고른 이유는 무엇인가요?</b>
                    </span>
                    <textarea
                      rows={2}
                      value={response.reason}
                      onChange={(e) =>
                        store.edit(taskId, { reason: e.target.value })
                      }
                      placeholder="이 구절이 내 설명의 근거가 되는 이유를 적어요."
                    />
                  </label>
                  {!!taskAnnotations.length && <div className="rx-use-thought"><span>표시하며 남긴 이유를 가져와 다듬어요.</span>{taskAnnotations.map(a => <button type="button" key={a.id} onClick={() => useThought(a)}>“{a.quote}”의 생각 가져오기 <ArrowRight size={14}/></button>)}</div>}
                  {taskId === "guided" && <p className="lj-say-aloud">먼저 소리 내어 말해 봐요. “나는 ___에 표시했어. 이 말이 ___을 설명하니까 ___라고 생각해.”</p>}
                  <div className="lj-help">
                    <button
                      onClick={() =>
                        store.edit(taskId, {
                          helpLevel: Math.min(3, response.helpLevel + 1),
                        })
                      }
                      disabled={response.helpLevel === 3}
                    >
                      <CircleHelp size={17} />
                      {response.helpLevel === 0
                        ? check
                          ? "도움을 받고 연습하기"
                          : "생각을 돕는 질문 보기"
                        : response.helpLevel < 3
                          ? "조금 더 도움받기"
                          : "도움 질문을 모두 펼쳤어요"}
                      <span>{response.helpLevel}/3</span>
                    </button>
                    {task.hints.slice(0, response.helpLevel).map((hint, i) => (
                      <p key={hint}>
                        <b>{i + 1}</b>
                        {hint}
                      </p>
                    ))}
                  </div>
                  {dirty && (
                    <button
                      className="rx-button rx-button-primary lj-main-action"
                      disabled={
                        !response.evidence.length ||
                        !response.answer.trim() ||
                        !response.reason.trim() ||
                        !dirty
                      }
                      onClick={() => {
                        store.submit(taskId);
                        requestAnimationFrame(() => feedback.current?.focus());
                      }}
                    >
                      {latest
                        ? "고친 설명으로 다시 확인하기"
                        : "근거와 설명 함께 확인하기"}{" "}
                      <ArrowRight size={17} />
                    </button>
                  )}
                  {(!response.evidence.length ||
                    !response.answer.trim() ||
                    !response.reason.trim()) && (
                    <p className="lj-muted">
                      근거, 내 설명, 고른 이유를 남기면 함께 확인할 수 있어요.
                    </p>
                  )}
                  {latest && (
                    <div
                      className="lj-feedback"
                      role="status"
                      ref={feedback}
                      tabIndex={-1}
                    >
                      <span className="lj-eyebrow">원문과 비교하기</span>
                      <h4>
                        {latest.evidenceMatch
                          ? "뜻을 직접 설명하는 구절을 골랐어요."
                          : "고른 구절이 낱말의 뜻을 직접 설명하는지 살펴봐요."}
                      </h4>
                      {latest.review && <div className="rx-feedback-note"><MessageCircle size={17}/><div><b>선생님이 남긴 다음 질문</b><p>{latest.review.note}</p></div></div>}
                      <p>{task.feedback}</p>
                      <p className="lj-muted">
                        근거 위치를 비교한 안내예요. 내 설명과 이유는 교사
                        검토가 필요해요.
                        {dirty && " 수정 중인 내용은 다시 확인해 주세요."}
                      </p>
                      <button
                        className="rx-button rx-button-primary"
                        disabled={dirty}
                        onClick={next}
                      >
                        {taskId === "guided"
                          ? "도움을 줄여서 해보기"
                          : taskId === "faded"
                            ? "내 생각을 문장으로 잇기"
                            : taskId === "independent"
                              ? "다른 주제에 사용해 보기"
                              : "내 학습 돌아보기"}{" "}
                        <ArrowRight size={16} />
                      </button>
                    </div>
                  )}
                </section>
              )}

              {attempt.stage === "writing" && (
                <section className="lj-writing-card">
                  <div className="lj-card-kicker">
                    <PenLine size={18} /> 내 생각을 잇는 작업 공간{" "}
                    <span>읽기 → 쓰기</span>
                  </div>
                  <div className="lj-writing-grid">
                    <div>{trace(true)}</div>
                    <div>
                      <h3>용매와 증발을 처음 듣는 친구에게 설명해 볼까요?</h3>
                      <p>
                        앞에서 읽은 두 글을 떠올리며 각각의 뜻을 정리해요. 내가
                        고른 근거와 설명이 맞는지도 살펴봐요.
                      </p>
                      {evidenceChanged && (
                        <p className="lj-change-note">
                          앞에서 고른 근거가 바뀌었어요. 저장한 설명도 맞는지
                          확인해 봐요.
                        </p>
                      )}
                      <label className="lj-field">
                        <span>
                          <b>나의 설명</b>
                        </span>
                        <textarea
                          rows={8}
                          value={attempt.writing}
                          onChange={(e) => store.write(e.target.value)}
                          placeholder="용매는 …&#10;증발은 …&#10;이렇게 설명한 근거는 …"
                        />
                      </label>
                      <button
                        className="rx-button"
                        disabled={
                          !attempt.writing.trim() ||
                          (previousRevision?.text === attempt.writing &&
                            !evidenceChanged)
                        }
                        onClick={store.saveRevision}
                      >
                        <Check size={16} />
                        {attempt.revisions.length
                          ? "고친 문장 남기기"
                          : "첫 문장 남기기"}
                      </button>
                      {attempt.revisions.length > 0 && (
                        <details className="lj-revisions">
                          <summary>
                            처음 문장과 수정 기록 · {attempt.revisions.length}개
                          </summary>
                          {attempt.revisions.map((r, i) => (
                            <blockquote key={`${i}-${r.at}`}>
                              <small>
                                {i === 0 ? "처음 쓴 문장" : `${i}번째 수정`}
                              </small>
                              <p>{r.text}</p>
                            </blockquote>
                          ))}
                        </details>
                      )}
                      <div className="lj-self-check">
                        <h4>원문과 나란히 확인해요</h4>
                        <p>
                          낱말의 뜻을 바꾸지 않았나요?
                          <br />
                          예시만 쓰지 않고 뜻을 설명했나요?
                          <br />
                          내가 고른 구절이 설명을 뒷받침하나요?
                        </p>
                      </div>
                      <button
                        className="rx-button rx-button-primary"
                        disabled={!attempt.writing.trim()}
                        onClick={() => {
                          store.saveRevision();
                          next();
                        }}
                      >
                        이제 혼자 확인해 보기 <ArrowRight size={17} />
                      </button>
                    </div>
                  </div>
                </section>
              )}

              {attempt.stage === "reflection" && (
                <section className="lj-reflection">
                  <div className="lj-reflection-hero">
                    <span>
                      <Sparkles size={26} />
                    </span>
                    <div>
                      <h3>고른 근거가, 나만의 설명으로 이어졌어요.</h3>
                      <p>
                        과정을 마친 것과 읽기 능력을 확인한 것은 달라요. 남긴
                        설명은 선생님이 함께 살펴봅니다.
                      </p>
                    </div>
                  </div>
                  <LearningEvidenceReport
                    audience="student"
                    attemptId={attempt.id}
                  />
                  <label className="lj-field">
                    <span>
                      <b>다음 글에서도 기억하고 싶은 읽기 방법</b>
                    </span>
                    <textarea
                      rows={2}
                      value={attempt.reflection}
                      onChange={(e) => store.reflect(e.target.value)}
                      placeholder="다음에는 어떤 부분을 먼저 살펴볼까요?"
                    />
                  </label>
                  <div className="lj-finish-actions">
                    <button
                      className="rx-button rx-button-primary"
                      onClick={() =>
                        useCoursewareStore.getState().setStudentMode("portal")
                      }
                    >
                      배움터로 돌아가기 <ArrowRight size={17} />
                    </button>
                    <button
                      className="rx-button"
                      onClick={() => {
                        store.start(level);
                        setPreview(null);
                      }}
                    >
                      <RotateCcw size={16} /> 같은 수업 다시 연습
                    </button>
                  </div>
                  <p className="lj-muted">
                    이전 기록은 보존됩니다. 다시 열어본 글은 새 글 확인으로
                    계산하지 않아요.
                  </p>
                </section>
              )}
              {!["writing", "reflection"].includes(attempt.stage) && trace()}
            </div>
          </div>
        </>
      )}
    </div>
  );
}
