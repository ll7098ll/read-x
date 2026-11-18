import React, { useEffect, useRef, useState } from "react";
import { ArrowRight, Check, PenLine, Undo2, X } from "lucide-react";
import { annotationKinds, type JourneyAnnotation } from "../../services/learningJourney";
import { makeTextAnchor, resolveMarkRange, validAnnotation, type TextAnchor } from "../../services/annotations";
import type { JourneyPassage } from "../../data/learningJourney";

export function MarkedSentence({ text, marks }: { text: string; marks: { quote: string; kind: string; anchor?: TextAnchor }[] }) {
  const ranges = marks.flatMap(m => { const range = resolveMarkRange(text, m); return range ? [{ ...m, ...range }] : []; });
  const points = [...new Set([0, text.length, ...ranges.flatMap(r => [r.start, r.end])])].sort((a, b) => a - b);
  return <>{points.slice(0, -1).map((start, i) => {
    const active = ranges.filter(r => r.start <= start && r.end >= points[i + 1]);
    const part = text.slice(start, points[i + 1]);
    return active.length ? <mark key={start} className={active.map(a => `lj-mark-${a.kind}`).join(" ")} title={active.map(a => annotationKinds[a.kind as keyof typeof annotationKinds]?.label).join(" · ")}>{part}</mark> : <React.Fragment key={start}>{part}</React.Fragment>;
  })}</>;
}

export function selectedTextAnchor(container: HTMLElement, sentenceId: string, text: string): TextAnchor | null {
  const selection = window.getSelection();
  if (!selection?.rangeCount || selection.isCollapsed) return null;
  const range = selection.getRangeAt(0);
  if (!container.contains(range.startContainer) || !container.contains(range.endContainer)) return null;
  const before = document.createRange();
  before.selectNodeContents(container); before.setEnd(range.startContainer, range.startOffset);
  return makeTextAnchor(sentenceId, text, before.toString().length, before.toString().length + range.toString().length);
}

function RangePicker({ text, sentenceId, value, onChange, label }: { text: string; sentenceId: string; value: TextAnchor; onChange: (anchor: TextAnchor) => void; label: string }) {
  const tokens = [...text.matchAll(/\S+\s*/g)].map(m => ({ text: m[0], start: m.index!, end: m.index! + m[0].trimEnd().length }));
  const change = (start: number, end: number) => { const a = makeTextAnchor(sentenceId, text, start, end); if (a) onChange(a); };
  return <div className="rx-range-picker">
    <div className="rx-range-quote"><span>{label}</span><q>{text.slice(value.start, value.end)}</q></div>
    <div className="rx-range-fields"><label>시작 어절<select value={tokens.findIndex(t => t.start <= value.start && t.end >= value.start)} onChange={e => { const t = tokens[+e.target.value]; change(t.start, Math.max(t.end, value.end)); }}>{tokens.map((t, i) => <option key={t.start} value={i}>{i + 1}. {t.text.trim()}</option>)}</select></label><label>끝 어절<select value={tokens.findIndex(t => t.start < value.end && t.end >= value.end)} onChange={e => { const t = tokens[+e.target.value]; change(Math.min(value.start, t.start), t.end); }}>{tokens.map((t, i) => <option key={t.start} value={i}>{i + 1}. {t.text.trim()}</option>)}</select></label></div>
    <small>드래그한 범위를 사용하거나 시작·끝 어절로 조절해요.</small>
  </div>;
}

export function AnnotationEditor({ passage, sentenceId, onSave, onClose, guided, initialAnchor, annotation, kinds }: {
  passage: JourneyPassage; sentenceId: string; onSave: (a: JourneyAnnotation) => void; onClose: () => void; guided: boolean;
  initialAnchor?: TextAnchor; annotation?: JourneyAnnotation; kinds?: JourneyAnnotation["kind"][];
}) {
  const sentences = passage.paragraphs.flatMap(p => p.sentences);
  const sentence = sentences.find(s => s.id === sentenceId)!;
  const [kind, setKind] = useState<JourneyAnnotation["kind"]>(annotation?.kind || "evidence");
  const [anchor, setAnchor] = useState<TextAnchor>(() => annotation?.anchor || initialAnchor || makeTextAnchor(sentenceId, sentence.text, 0, sentence.text.length)!);
  const [note, setNote] = useState(annotation?.note || "");
  const [linkedId, setLinkedId] = useState(annotation?.linkedAnchor?.sentenceId || annotation?.linkedSentenceId || sentenceId);
  const [linkedAnchor, setLinkedAnchor] = useState<TextAnchor | undefined>(annotation?.linkedAnchor);
  const [more, setMore] = useState(false);
  const title = useRef<HTMLHeadingElement>(null);
  useEffect(() => { title.current?.focus(); }, []);
  const target = sentences.find(s => s.id === linkedId)!;
  const destination = linkedAnchor || makeTextAnchor(linkedId, target.text, 0, target.text.length)!;
  const basic: JourneyAnnotation["kind"][] = kinds || (guided ? ["target", "evidence", "link"] : ["evidence", "condition", "link"]);
  const tools = more ? Object.keys(annotationKinds) as JourneyAnnotation["kind"][] : [...new Set([...basic, kind])];
  const draft: JourneyAnnotation = { id: annotation?.id || "draft", passageId: passage.id, passageVersion: passage.version, sentenceId, quote: anchor.quote, kind, note: note.trim(), anchor, author: "student", ...(kind === "link" ? { linkedSentenceId: linkedId, linkedAnchor: destination } : {}) };
  return <section className="lj-annotation-editor rx-annotation-composer" aria-label="내 생각 표시 편집">
    <div className="lj-annotation-title"><h3 tabIndex={-1} ref={title}>{annotation ? "내 표시와 생각 고치기" : "이 구절에서 시작한 내 생각"}</h3><button type="button" onClick={onClose} aria-label="생각 표시 닫기"><X size={18}/></button></div>
    <div className="rx-composer-steps"><span>01 구절</span><ArrowRight size={13}/><span>02 표시</span><ArrowRight size={13}/><span>03 이유</span></div>
    <RangePicker text={sentence.text} sentenceId={sentenceId} value={anchor} onChange={setAnchor} label="내가 고른 구절"/>
    <div className="lj-annotation-tools" aria-label="표시 종류">{tools.map(k => <button type="button" key={k} aria-pressed={kind === k} onClick={() => setKind(k)}>{annotationKinds[k].symbol} {annotationKinds[k].label}</button>)}<button type="button" aria-expanded={more} onClick={() => setMore(!more)}>{more ? "기본 도구" : "다른 표시"}</button></div>
    {kind === "link" && <div className="rx-linked-range"><label>이어 읽을 문장<select value={linkedId} onChange={e => { setLinkedId(e.target.value); setLinkedAnchor(undefined); }}>{sentences.map((s, i) => <option key={s.id} value={s.id}>{i + 1}. {s.text}</option>)}</select></label><RangePicker text={target.text} sentenceId={linkedId} value={destination} onChange={setLinkedAnchor} label="연결할 다른 구절"/><p className="rx-relation-preview">“{anchor.quote}” <ArrowRight size={16}/> “{destination.quote}”</p></div>}
    <label className="lj-field"><span>{annotationKinds[kind].prompt}</span><textarea rows={2} value={note} onChange={e => setNote(e.target.value)} placeholder={guided ? "나는 이 말을 보고 ___라고 생각했어. 왜냐하면 ___." : "먼저 말해 보고, 짧게 남겨도 괜찮아요."}/></label>
    <div className="rx-composer-actions"><button type="button" className="rx-button" onClick={onClose}>취소</button><button type="button" className="rx-button rx-button-primary" disabled={!validAnnotation(passage, draft)} onClick={() => {
      const at = new Date().toISOString();
      onSave({ ...draft, id: annotation?.id || crypto.randomUUID(), createdAt: annotation?.createdAt || at, updatedAt: at, revisions: annotation ? [...(annotation.revisions || []), { quote: annotation.quote, kind: annotation.kind, note: annotation.note, anchor: annotation.anchor, linkedAnchor: annotation.linkedAnchor, at: annotation.updatedAt || at }] : [] });
      onClose();
    }}><Check size={16}/> {annotation ? "고친 생각 남기기" : "표시와 생각 남기기"}</button></div>
  </section>;
}

export function AnnotationNotes({ annotations, passage, onRemove, onEdit, onUse }: { annotations: JourneyAnnotation[]; passage: JourneyPassage; onRemove?: (id: string) => void; onEdit?: (a: JourneyAnnotation) => void; onUse?: (a: JourneyAnnotation) => void }) {
  if (!annotations.length) return null;
  return <div className="lj-margin-notes">{annotations.map(a => <article className={`lj-margin-note lj-note-${a.kind}`} key={a.id}>
    <div className="rx-note-origin"><span>내 생각 · {annotationKinds[a.kind].symbol} {annotationKinds[a.kind].label}</span>{!!a.revisions?.length && <span>생각 수정 {a.revisions.length}회</span>}</div>
    <q>{a.quote}</q>
    {a.linkedSentenceId && <p className="rx-relation-preview"><ArrowRight size={15}/>{a.linkedAnchor?.quote || passage.paragraphs.flatMap(p => p.sentences).find(s => s.id === a.linkedSentenceId)?.text || "연결 구절의 원문 확인 필요"}</p>}
    <p>{a.note}</p>
    {!!a.revisions?.length && <details><summary>처음 생각과 비교</summary>{a.revisions.map((r, i) => <blockquote key={`${r.at}-${i}`}><small>{i === 0 ? "처음 생각" : "고치기 전"} · “{r.quote}”</small><p>{r.note}</p></blockquote>)}</details>}
    <div className="rx-note-actions">{onUse && <button type="button" onClick={() => onUse(a)}>내 설명에 가져오기 <ArrowRight size={14}/></button>}{onEdit && <button type="button" onClick={() => onEdit(a)} aria-label={`표시 고치기: ${a.quote}`}><PenLine size={14}/>고치기</button>}{onRemove && <button type="button" onClick={() => onRemove(a.id)} aria-label={`표시 삭제: ${a.quote}`}>지우기</button>}</div>
  </article>)}</div>;
}

export function AnnotationUndo({ available, onUndo }: { available: boolean; onUndo: () => void }) {
  return <button type="button" className="rx-annotation-undo" disabled={!available} onClick={onUndo}><Undo2 size={15}/> 마지막 표시 작업 되돌리기</button>;
}
