import type { JourneyPassage } from "../data/learningJourney";

export const annotationKinds = {
  target: { symbol: "□", label: "대상", prompt: "어떤 대상을 살펴보고 있나요?" },
  evidence: { symbol: "밑줄", label: "근거", prompt: "이 말이 내 생각을 어떻게 뒷받침하나요?" },
  link: { symbol: "→", label: "연결", prompt: "두 구절을 어떤 관계로 연결했나요?" },
  condition: { symbol: "[ ]", label: "조건", prompt: "언제, 어디까지 성립하는 말인가요?" },
  question: { symbol: "?", label: "질문", prompt: "무엇을 다시 확인하고 싶나요?" },
} as const;
export type AnnotationKind = keyof typeof annotationKinds;
export type TextAnchor = { sentenceId: string; start: number; end: number; quote: string; prefix: string; suffix: string };
export type AnnotationRevision = { quote: string; note: string; kind: AnnotationKind; anchor?: TextAnchor; linkedAnchor?: TextAnchor; at: string };
export type ReadingAnnotation = {
  id: string; passageId: string; sentenceId: string; quote: string;
  kind: AnnotationKind; note: string; linkedSentenceId?: string;
  anchor?: TextAnchor; linkedAnchor?: TextAnchor; passageVersion?: number;
  author?: "student"; createdAt?: string; updatedAt?: string; revisions?: AnnotationRevision[];
};

export function makeTextAnchor(sentenceId: string, text: string, start: number, end: number): TextAnchor | null {
  if (!Number.isInteger(start) || !Number.isInteger(end) || start < 0 || end > text.length || start >= end || !text.slice(start, end).trim()) return null;
  // DOM Range offsets and stored text both use UTF-16; reject boundaries inside a surrogate pair.
  const insidePair = (n: number) => n > 0 && n < text.length && /[\uD800-\uDBFF]/.test(text[n - 1]) && /[\uDC00-\uDFFF]/.test(text[n]);
  if (insidePair(start) || insidePair(end)) return null;
  return { sentenceId, start, end, quote: text.slice(start, end), prefix: text.slice(Math.max(0, start - 20), start), suffix: text.slice(end, end + 20) };
}

export function resolveMarkRange(text: string, mark: { quote: string; anchor?: TextAnchor }): { start: number; end: number } | null {
  if (mark.anchor) {
    const a = mark.anchor;
    return makeTextAnchor(a.sentenceId, text, a.start, a.end) && text.slice(a.start, a.end) === mark.quote && a.quote === mark.quote ? { start: a.start, end: a.end } : null;
  }
  const start = mark.quote ? text.indexOf(mark.quote) : -1;
  // Legacy ambiguous quotes remain readable as notes instead of highlighting the wrong occurrence.
  return start >= 0 && text.indexOf(mark.quote, start + 1) < 0 ? { start, end: start + mark.quote.length } : null;
}

export function validAnnotation(passage: JourneyPassage, a: ReadingAnnotation): boolean {
  const sentences = passage.paragraphs.flatMap(p => p.sentences);
  const source = sentences.find(s => s.id === a.sentenceId);
  if (a.passageId !== passage.id || (a.passageVersion !== undefined && a.passageVersion !== passage.version) || !source || !a.note.trim() || !(a.kind in annotationKinds) || !a.quote.trim()) return false;
  if (a.anchor ? a.anchor.sentenceId !== a.sentenceId || !resolveMarkRange(source.text, a) : !source.text.includes(a.quote)) return false;
  if (a.kind === "link") {
    const target = sentences.find(s => s.id === (a.linkedAnchor?.sentenceId || a.linkedSentenceId));
    if (!target) return false;
    if (a.linkedAnchor) {
      if (!resolveMarkRange(target.text, { quote: a.linkedAnchor.quote, anchor: a.linkedAnchor })) return false;
      if (a.anchor && a.anchor.sentenceId === a.linkedAnchor.sentenceId && a.anchor.start === a.linkedAnchor.start && a.anchor.end === a.linkedAnchor.end) return false;
    } else if (target.id === source.id) return false;
  }
  return true;
}

export function updateAnnotationList(current: ReadingAnnotation[], annotation: ReadingAnnotation) {
  return [...current.filter(a => a.id !== annotation.id), annotation];
}

export function rememberAnnotations<T extends { annotations?: ReadingAnnotation[]; annotationHistory?: ReadingAnnotation[][] }>(state: T, annotations: ReadingAnnotation[]): T {
  return { ...state, annotations, annotationHistory: [...(state.annotationHistory || []), state.annotations || []].slice(-20) };
}

export function undoAnnotations<T extends { annotations?: ReadingAnnotation[]; annotationHistory?: ReadingAnnotation[][] }>(state: T): T {
  const history = state.annotationHistory || [];
  return history.length ? { ...state, annotations: history[history.length - 1], annotationHistory: history.slice(0, -1) } : state;
}
