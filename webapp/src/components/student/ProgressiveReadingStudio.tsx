import React, { useEffect, useRef, useState } from "react";
import { ReadingDisplay } from '../common/ReadingDisplay';
import { ArrowRight, BookOpen, Check, Lightbulb, RotateCcw, MessageCircle } from "lucide-react";
import { progressiveLessons, progressivePassage, progressiveLessonAtLevel, thinkingLadder, type ProgressiveLesson } from "../../data/progressiveReading";
import { corpusLessons } from "../../data/corpusReading";
import { readingLevels, readingLevelLabels, passageMetrics, type ReadingLevel } from "../../data/readingPolicy";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { usePracticeState, useReadingStorageStatus, useReadingWorkspace } from "../../store/useReadingWorkspace";
import { AnnotationEditor, AnnotationNotes, MarkedSentence, AnnotationUndo, selectedTextAnchor } from "./ReadingAnnotations";
import { rememberAnnotations, undoAnnotations, updateAnnotationList, type TextAnchor } from "../../services/annotations";
import type { JourneyAnnotation } from "../../services/learningJourney";
import { createProgressiveRun, blankProgressiveResponse, editProgressiveResponse, submitProgressiveResponse, progressiveResponseChanged, advanceProgressive, canAdvanceProgressive, restartProgressive, type ProgressiveRun, type ProgressiveResponse } from "../../services/progressiveReading";

export function ProgressiveReadingEntry() {
  return <section className="pr-entry"><div><p className="rx-eyebrow">사고 시범과 내 생각 표시 · 1~6학년</p><h2>찾는 읽기에서, 판단하는 읽기로</h2><p>시범을 보고, 구절에 생각을 남기고, 내 판단을 근거와 연결해요.</p><span>글에서 찾기 → 관계 연결 → 내 말로 설명 → 새 보기 적용</span></div><button className="rx-button rx-button-primary" onClick={()=>{useReadingWorkspace.getState().save("progressive-preferences","grade",useCoursewareStore.getState().activeGradeIdx+1);useCoursewareStore.getState().setStudentMode("progressive");}}>읽는 방법 연습하기 <ArrowRight size={18}/></button></section>;
}

export function ProgressiveReadingStudio() {
  const activeGrade = useCoursewareStore(s=>s.activeGradeIdx+1);
  const [grade,setGrade] = usePracticeState("progressive-preferences","grade",activeGrade);
  const [level,setLevel] = usePracticeState<ReadingLevel>("progressive-preferences","level","standard");
  const [selectedId,setSelectedId] = usePracticeState("progressive-preferences","lesson-id","");
  const safeGrade = [1,2,3,4,5,6].includes(grade) ? grade : 5;
  const available = [...corpusLessons,...progressiveLessons].filter(l=>l.grade===safeGrade);
  const lesson = available.find(l=>l.id===selectedId) || available[0];
  const safeLevel = readingLevels.includes(level) ? level : "standard";
  return <div className="pr-studio">
    <header className="pr-heading"><div><p className="rx-eyebrow">READ · CONNECT · REASON</p><h1>한 걸음씩, 깊이 읽기</h1><p>무엇을 찾았는지에서 왜 그렇게 판단했는지까지.</p></div><button className="rx-button" onClick={()=>useCoursewareStore.getState().setStudentMode("portal")}>학습 목록</button></header>
    <div className="pr-selectors"><label>읽을 학년<select value={lesson.grade} onChange={e=>setGrade(Number(e.target.value))}>{[1,2,3,4,5,6].map(g=><option key={g} value={g}>{g}학년</option>)}</select></label><label>읽을 지문<select value={lesson.id} onChange={e=>setSelectedId(e.target.value)}><optgroup label="개정 교과 지문">{available.filter(l=>l.sourcePassageId).map(l=><option key={l.id} value={l.id}>{l.title}</option>)}</optgroup><optgroup label="읽기 전략 연습">{available.filter(l=>!l.sourcePassageId).map(l=><option key={l.id} value={l.id}>{l.title}</option>)}</optgroup></select></label><fieldset><legend>글의 수준</legend>{readingLevels.map(l=><button key={l} aria-pressed={safeLevel===l} onClick={()=>setLevel(l)}>{readingLevelLabels[l]}</button>)}</fieldset><p>개정 지문 144편을 학년과 수준에 맞춰 읽어요. 확인·연결에서 추론·근거 판단·새 보기 적용으로 이어져요.</p></div>
    <ProgressiveLessonPlayer key={`${lesson.id}-${safeLevel}`} lesson={lesson} level={safeLevel}/>
  </div>;
}

export function ProgressiveLessonPlayer({lesson:sourceLesson,level}:{lesson:ProgressiveLesson;level:ReadingLevel}) {
  const lesson = progressiveLessonAtLevel(sourceLesson,level);
  const [run,setRun] = usePracticeState<ProgressiveRun>(`${lesson.id}-${level}`,"progressive-v1",createProgressiveRun());
  return <ProgressiveLessonView sourceLesson={sourceLesson} level={level} run={run} setRun={setRun}/>;
}

export function ProgressiveLessonView({sourceLesson,level,run,setRun,serverManaged=false}:{sourceLesson:ProgressiveLesson;level:ReadingLevel;run:ProgressiveRun;setRun:React.Dispatch<React.SetStateAction<ProgressiveRun>>;serverManaged?:boolean}) {
  const lesson = progressiveLessonAtLevel(sourceLesson,level);
  const failed = useReadingStorageStatus(s=>s.failed);
  const [pane,setPane] = useState<"text"|"activity">("text");
  const [editing,setEditing] = useState("");
  const [editingNote,setEditingNote] = useState<JourneyAnnotation>();
  const [selectedAnchor,setSelectedAnchor] = useState<TextAnchor>();
  const feedback = useRef<HTMLDivElement>(null);
  const modelAnchor = useRef<HTMLElement>(null);
  const activity = useRef<HTMLElement>(null);
  const textPanel = useRef<HTMLElement>(null);
  const previousView = useRef(`${run.phase}:${run.modelStep}:${run.index}`);
  useEffect(()=>{
    const view = `${run.phase}:${run.modelStep}:${run.index}`;
    if (view === previousView.current) return;
    previousView.current = view;
    const frame = requestAnimationFrame(()=>{
      if(run.phase === "model") modelAnchor.current?.scrollIntoView({block:"start"});
      else if(run.phase === "questions") {
        activity.current?.scrollTo({top:0});
        activity.current?.scrollIntoView({block:"start"});
      }
    });
    return ()=>cancelAnimationFrame(frame);
  },[run.phase,run.modelStep,run.index]);
  const passage = progressivePassage(lesson,level);
  const q = lesson.questions[run.index];
  const openResponse = q.responseKind === "explanation";
  const r = run.responses[q.id] || blankProgressiveResponse();
  const last = r.submissions.slice(-1)[0];
  const dirty = progressiveResponseChanged(r,run.annotations);
  const metrics = passageMetrics(passage.paragraphs.map(p=>p.sentences[0].text));
  const model = lesson.model[run.modelStep];
  const modelPhase = run.phase==="model";
  const young = lesson.grade<=2;
  const stepLabels = young ? ["글에서 찾기","이어 보기","생각해 보기","까닭 살피기","새 상황에 쓰기"] : thinkingLadder;
  const guided = run.index<2 || level==="supported";
  const openNote = (id:string, note?:JourneyAnnotation, anchor?:TextAnchor) => {setEditing(id);setEditingNote(note);setSelectedAnchor(anchor);};
  const useNote = (a:JourneyAnnotation) => {const paragraph=passage.paragraphs.find(p=>p.sentences.some(s=>s.id===a.sentenceId));edit({reason:r.reason.includes(a.note)?r.reason:[r.reason,a.note].filter(Boolean).join("\n"),evidence:[...new Set([...r.evidence,...(paragraph?[paragraph.id]:[])])]});setPane("activity");};
  const edit = (update:Parameters<typeof editProgressiveResponse>[2])=>setRun(s=>editProgressiveResponse(s,q.id,update));
  const next = ()=>{setRun(s=>advanceProgressive(s,lesson));setEditing("");setPane("activity");};
  const completed = Object.values(run.responses).filter(r=>r.submissions.length);
  const revealAvailable = last && (openResponse || r.submissions.length>=2 || r.hintLevel===3 || (last.choiceMatch&&last.evidenceMatch));
  if(run.phase==="complete") return <section className="pr-complete"><p className="rx-eyebrow">오늘의 생각 기록</p><h2>다섯 가지 방법으로 한 편을 읽었어요.</h2><p>같은 본문을 읽고 새 보기까지 적용한 연습이에요. 선택과 근거 확인 결과이며, 글로 쓴 설명은 선생님과 함께 검토해요.</p><div className="pr-result-summary"><b>{completed.length}개 단계에 응답</b><span>내 생각 표시 {run.annotations.length}개</span><span>이전 연습 {run.archives.length}회 보관</span></div>
    {lesson.questions.map((question,i)=>{const answer=run.responses[question.id];const latest=answer?.submissions.slice(-1)[0];return <details key={question.id} className="pr-record"><summary>{i+1}. {question.skill} <span>{question.responseKind === "explanation" ? latest?.review ? "서술 응답 · 교사 확인" : "서술 응답 · 교사 검토 전" : latest?.choiceMatch&&latest.evidenceMatch?"선택·필요 근거 확인":"다시 연습할 부분"}</span></summary>{answer?.submissions.map((s,j)=><article key={s.id}><b>{j===0?"첫 응답":`${j}번째 수정`} · {s.support==="guided"?"도움과 함께":"질문 도움 없이"}</b><p>고른 답: {s.choice === null ? "서술 응답" : question.options[s.choice]}</p><p>근거: {s.evidence.map(id=>`${passage.paragraphs.findIndex(p=>p.id===id)+1}문단`).join(", ")}</p><p>내 설명: {s.reason}</p><small>도움 {s.hintLevel}단계 · 설명 검토 전</small></article>)}</details>;})}
    {!!run.annotations.length&&<details className="pr-record"><summary>내가 표시한 구절과 생각 {run.annotations.length}개</summary><AnnotationNotes annotations={run.annotations} passage={passage}/></details>}
    {!serverManaged && <button className="rx-button rx-button-primary" onClick={()=>setRun(s=>restartProgressive(s))}><RotateCcw size={17}/> 기록을 보관하고 다시 연습</button>}</section>;
  return <ReadingDisplay>
    {!serverManaged && <p className={failed?"lj-save-error":"pr-save"} role="status">{failed?"기기에 저장하지 못했어요. 중요한 내용을 복사해 주세요.":"학년·글 수준별로 이 기기에 자동 저장"}</p>}
    <ol className="lj-grr" aria-label="점진적 읽기 과정">{["시범","같이 해보기","스스로 해보기"].map((s,i)=><li key={s} aria-current={(modelPhase?0:run.index<2?1:2)===i?"step":undefined}><span>{i+1}</span><b>{s}</b></li>)}</ol>
    {(!modelPhase||completed.length>0)&&<nav className="pr-ladder" aria-label="사고의 다섯 계단"><button aria-current={modelPhase?"step":undefined} onClick={()=>{setRun(s=>({...s,phase:"model"}));setPane("text");}}>생각 시범</button>{stepLabels.map((skill,i)=><button key={skill} disabled={i>run.reached || (modelPhase&&completed.length===0&&run.modelStep<2)} aria-current={!modelPhase&&i===run.index?"step":undefined} onClick={()=>{setRun(s=>({...s,phase:"questions",index:i}));setPane("activity");setEditing("");}}>{i+1}. {skill}</button>)}</nav>}
    {!!run.archives.length&&<details className="pr-record"><summary>이전 연습 기록 {run.archives.length}회</summary>{run.archives.map((archived,i)=><details key={i}><summary>{i+1}번째 연습</summary>{lesson.questions.map(question=><article key={question.id}><b>{question.skill}</b>{archived.responses[question.id]?.submissions.map((s,j)=><div key={s.id}><p>{j===0?"처음 답":"수정한 답"}: {s.choice === null ? "서술 응답" : question.options[s.choice]}</p><p>내 설명: {s.reason}</p><small>도움 {s.hintLevel}단계 · 설명 검토 전</small></div>)}</article>)}</details>)}</details>}
    <div className="pr-mobile-tabs"><button aria-pressed={pane==="text"} onClick={()=>setPane("text")}><BookOpen size={16}/> 지문과 표시</button><button aria-pressed={pane==="activity"} onClick={()=>setPane("activity")}>{modelPhase?"시범 따라가기":`${run.index+1}. ${stepLabels[run.index]}`}</button>{!modelPhase&&<p>{q.prompt}</p>}</div>
    <div className="pr-workspace" data-pane={pane}>
      <article ref={textPanel} className="pr-paper"><p className="rx-eyebrow">{lesson.grade}학년 · {readingLevelLabels[level]} · {lesson.concept}</p><h2>{lesson.title}</h2><p className="pr-meta">{metrics.chars.toLocaleString()}자 · {metrics.paragraphs}문단</p><div className="lj-annotation-legend"><b>{modelPhase?"선생님 시범":"내 생각 표시"}</b><span>□ 대상</span><span>밑줄 · 근거</span><span>→ 연결</span></div>{!modelPhase&&<AnnotationUndo available={!!run.annotationHistory?.length} onUndo={()=>setRun(undoAnnotations)}/>}
        {passage.paragraphs.map((p,i)=>{const s=p.sentences[0];const notes=run.annotations.filter(a=>a.sentenceId===s.id);return <section ref={modelPhase&&model.paragraph===p.id?modelAnchor:undefined} key={p.id} className={`pr-paragraph ${r.evidence.includes(p.id)&&!modelPhase?"pr-paragraph-selected":""}`}><span className="pr-number">{i+1}</span><p className="rx-selectable-text" onMouseUp={e=>{if(!modelPhase){const anchor=selectedTextAnchor(e.currentTarget,s.id,s.text);if(anchor)openNote(s.id,undefined,anchor);}}} onTouchEnd={e=>{if(!modelPhase){const anchor=selectedTextAnchor(e.currentTarget,s.id,s.text);if(anchor)openNote(s.id,undefined,anchor);}}}><MarkedSentence text={s.text} marks={modelPhase&&model.paragraph===p.id?[model]:notes}/></p>
          {modelPhase&&model.paragraph===p.id&&<aside className="lj-inline-model"><b>선생님의 생각 · {run.modelStep+1}/3</b><p>“{model.thought}”</p></aside>}
          <AnnotationNotes annotations={notes} passage={passage} onRemove={!modelPhase?id=>setRun(s=>rememberAnnotations(s,s.annotations.filter(a=>a.id!==id))):undefined} onEdit={!modelPhase?a=>openNote(a.sentenceId,a):undefined} onUse={!modelPhase?useNote:undefined}/>
          {!modelPhase&&<div className="pr-paragraph-actions"><button aria-pressed={r.evidence.includes(p.id)} onClick={()=>edit({evidence:r.evidence.includes(p.id)?r.evidence.filter(id=>id!==p.id):[...r.evidence,p.id]})}>{r.evidence.includes(p.id)?<Check size={14}/>:null}{i+1}문단 근거 {r.evidence.includes(p.id)?"해제":"선택"}</button><button onClick={()=>openNote(s.id)}>{i+1}문단에 생각 표시</button></div>}
          {editing===s.id&&!modelPhase&&<AnnotationEditor key={`${editing}-${editingNote?.id||selectedAnchor?.start||"new"}`} passage={passage} sentenceId={s.id} guided={guided} annotation={editingNote} initialAnchor={selectedAnchor} onClose={()=>setEditing("")} onSave={a=>{setRun(s=>rememberAnnotations(s,updateAnnotationList(s.annotations,a)));}}/>}
        </section>;})}
        {(modelPhase||guided)&&<details className="lj-vocabulary"><summary>낱말을 풀어 읽어요</summary>{lesson.vocabulary.map(v=><p key={v.word}><b>{v.word}</b> · {v.meaning}</p>)}</details>}
      </article>
      <aside ref={activity} className="pr-activity">
        {modelPhase?<section className="pr-model"><p className="rx-eyebrow"><Lightbulb size={17}/> 선생님의 사고구술</p><h2>표시한 까닭을 따라 말해 봐요.</h2><blockquote>{model.quote}</blockquote><p>본문의 표시와 생각 말풍선을 함께 읽어요. 단서가 생각으로 이어지는 과정을 소리 내어 따라 해 보세요.</p><div className="lj-model-dots">{lesson.model.map((m,i)=><button key={i} aria-label={`시범 ${i+1}`} aria-pressed={run.modelStep===i} onClick={()=>{setRun(s=>({...s,modelStep:i}));setPane("text");}}>{i+1}</button>)}</div><button className="rx-button rx-button-primary" onClick={()=>{if(run.modelStep<2){setRun(s=>({...s,modelStep:s.modelStep+1}));setPane("text");}else{setRun(s=>({...s,phase:"questions"}));setPane("activity");}}}>{run.modelStep<2?"다음 생각 따라가기":"이제 같이 해보기"}<ArrowRight size={17}/></button></section>:
        <section className="pr-question"><p className="rx-eyebrow">{run.index<2?"같이 해보기":"스스로 해보기"} · {run.index+1}/5 · {stepLabels[run.index]}</p><h2>{q.prompt}</h2>{run.index===4&&<p className="pr-transfer-label">{young?"배운 방법을 다른 상황에도 써 봐요.":lesson.grade>=5?"수능형 사고 연습 · 새 보기에 원리 적용하기":"새 보기에 조건과 원리 적용하기"}</p>}{q.scenario&&<div className="pr-scenario"><b>보기</b><p>{q.scenario}</p></div>}
          {!openResponse && <fieldset className="pr-options"><legend>1. 내 판단을 골라요</legend>{q.options.map((option,i)=><label key={option}><input type="radio" name={q.id} checked={r.choice===i} onChange={()=>edit({choice:i})}/><span className="pr-option-number">{i+1}</span><span>{option}</span></label>)}</fieldset>}
          <div className="pr-evidence"><b>{openResponse ? "1" : "2"}. 본문에서 근거 문단을 골라요</b>{r.evidence.length?<p>{r.evidence.map(id=>`${passage.paragraphs.findIndex(p=>p.id===id)+1}문단`).join(" · ")} 선택</p>:<p>지문 아래의 ‘문단 근거 선택’을 눌러요.</p>}<button className="rx-button" onClick={()=>{setPane("text");requestAnimationFrame(()=>textPanel.current?.scrollIntoView({block:"start"}));}}>지문에서 근거 고르기</button></div>
          <label className="lj-field"><span><b>{openResponse ? "2. 내 답과 그렇게 생각한 까닭을 써요" : young?"3. 왜 이 답을 골랐나요?":"3. 근거가 내 판단을 어떻게 뒷받침하나요?"}</b></span><textarea rows={3} value={r.reason} onChange={e=>edit({reason:e.target.value})} placeholder={young?"글에 ___라고 나와서 이렇게 생각했어요.":guided?"나는 ___에 표시했어. 이 내용과 ___을 연결하면 ___라고 생각할 수 있어.":"본문의 조건과 내 판단을 연결해 설명해요."}/></label>
          {young&&<p className="lj-muted">먼저 말로 설명해요. 짧게 쓰거나 선생님과 함께 적어도 괜찮아요.</p>}
          {guided&&<p className="lj-say-aloud">적기 전에 소리 내어 말해 봐요. “어떤 말을 보았지? 무엇과 연결했지? 그래서 왜 이 답일까?”</p>}
          <div className="lj-help"><button disabled={r.hintLevel>=3} onClick={()=>edit({hintLevel:r.hintLevel+1})}>{r.hintLevel?"다음 도움 받기":"생각을 돕는 질문"} · {r.hintLevel}/3</button>{q.hints.slice(0,r.hintLevel).map((hint,i)=><p key={hint}><b>{i+1}</b>{hint}</p>)}</div>
          <button className="rx-button rx-button-primary pr-submit" disabled={(!openResponse && r.choice===null)||!r.evidence.length||!r.reason.trim()||!dirty} onClick={()=>{setRun(s=>submitProgressiveResponse(s,lesson,level,q.id,crypto.randomUUID(),new Date().toISOString()));requestAnimationFrame(()=>feedback.current?.focus());}}>{last?"생각을 고쳐 다시 확인":"판단과 근거 확인"}</button>
          {last&&<div className="pr-feedback" ref={feedback} tabIndex={-1} role="status"><h3>{openResponse ? last.review ? "내 설명에 선생님 피드백이 도착했어요." : "내 설명을 기록했어요. 내용은 선생님과 검토해요." : last.choiceMatch&&last.evidenceMatch?"선택과 필요한 근거가 맞게 연결됐어요.":last.choiceMatch?"선택은 맞아요. 필요한 근거도 찾아볼까요?":"생각이 갈린 지점을 다시 살펴봐요."}</h3><p>{openResponse ? last.evidenceMatch ? "풀이에 필요한 문단이 포함되어 있어요. 이 표시는 설명의 정답 판정이 아니에요." : "설명에 필요한 다른 문단도 찾아보세요. 예시 풀이와 내 생각을 비교할 수 있어요." : last.choiceMatch?q.evidence.every(e=>last.evidence.includes(e))?"필요한 문단이 포함되어 있어요. 내 설명이 그 근거와 맞는지는 선생님과 함께 확인해요.":"답이 맞아도 그 답을 뒷받침하는 문단이 빠질 수 있어요.":q.optionReasons[last.choice ?? -1]}</p>
            {last.review&&<div className="rx-feedback-note"><MessageCircle size={17}/><div><b>선생님 피드백</b><p>{last.review.note}</p></div></div>}{dirty&&<p>지금 고친 답은 아직 확인하지 않았어요.</p>}{!revealAvailable&&!last.choiceMatch&&<p>도움 질문을 따라 한 번 더 생각해 보세요. 다시 시도하거나 도움 세 개를 살펴본 뒤 해설을 열 수 있어요.</p>}
            {revealAvailable&&!r.revealed&&<button className="rx-button" onClick={()=>edit({revealed:true})}>{openResponse ? "예시 설명과 내 생각 비교하기" : "풀이와 오답의 까닭 보기"}</button>}
            {r.revealed&&<div className="pr-explanation"><b>{openResponse ? "비교할 예시 설명 · 다른 표현도 가능해요" : `정답 ${q.answer+1} · ${q.options[q.answer]}`}</b><p>{q.explanation}</p>{q.options.map((option,i)=><p key={option}><b>{i+1}번</b> {q.optionReasons[i]}</p>)}<p>필요한 근거: {q.evidence.map(id=>`${passage.paragraphs.findIndex(p=>p.id===id)+1}문단`).join(" + ")}</p></div>}
            {canAdvanceProgressive(run,lesson)&&<button className="rx-button rx-button-primary" onClick={next}>{run.index===4?"내 생각 기록 보기":openResponse?"설명 검토를 남기고 다음 계단으로":last.choiceMatch&&last.evidenceMatch?"다음 계단으로":"해설을 읽고 다음 연습으로"}<ArrowRight size={16}/></button>}
            <small>정답 선택은 읽기 능력 전체의 판정이 아니에요. 처음 답과 도움·수정 기록을 함께 남겨요.</small>
          </div>}
        </section>}
      </aside>
    </div>
  </ReadingDisplay>;
}
