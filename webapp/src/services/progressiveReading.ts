import { progressivePassage, type ProgressiveLesson } from "../data/progressiveReading";
import type { ReadingLevel } from "../data/readingPolicy";
import type { JourneyAnnotation } from "./learningJourney";
import type { JourneyPassage } from "../data/learningJourney";

export type ProgressiveSubmission = {
  id: string; at: string; choice: number | null; evidence: string[]; reason: string; hintLevel: number;
  choiceMatch: boolean | null; evidenceMatch: boolean; explanationReview: "pending";
  support: "guided" | "independent"; revised: boolean; passageId: string; level: ReadingLevel;
  annotations: JourneyAnnotation[]; passageExposure: "practiced";
  passageSnapshot?: JourneyPassage;
  questionSnapshot?: ProgressiveLesson["questions"][number];
  review?: { outcome: "success" | "needs_support"; note: string; at: string };
};
export type ProgressiveResponse = { choice: number | null; evidence: string[]; reason: string; hintLevel: number; revealed: boolean; submissions: ProgressiveSubmission[] };
export type ProgressiveRun = {
  phase: "model" | "questions" | "complete"; modelStep: number; index: number; reached: number;
  responses: Record<string, ProgressiveResponse>; annotations: JourneyAnnotation[];
  annotationHistory?: JourneyAnnotation[][];
  archives: { responses: Record<string, ProgressiveResponse>; annotations: JourneyAnnotation[] }[];
};
export const blankProgressiveResponse = (): ProgressiveResponse => ({choice:null,evidence:[],reason:"",hintLevel:0,revealed:false,submissions:[]});
export const createProgressiveRun = (): ProgressiveRun => ({phase:"model",modelStep:0,index:0,reached:0,responses:{},annotations:[],archives:[]});
export function editProgressiveResponse(run: ProgressiveRun, questionId: string, update: Partial<Pick<ProgressiveResponse,"choice"|"evidence"|"reason"|"hintLevel"|"revealed">>): ProgressiveRun {
  const current = run.responses[questionId] || blankProgressiveResponse();
  return {...run,responses:{...run.responses,[questionId]:{...current,...update,
    hintLevel:Math.max(current.hintLevel,Math.min(3,update.hintLevel??0)),
    revealed:current.revealed || (!!update.revealed && current.submissions.length>0),
  }}};
}
export function progressiveResponseChanged(r: ProgressiveResponse, annotations: JourneyAnnotation[]) {
  const last = r.submissions.slice(-1)[0];
  return !last || last.choice !== r.choice || last.reason !== r.reason || last.hintLevel !== r.hintLevel
    || JSON.stringify(last.evidence)!==JSON.stringify(r.evidence) || JSON.stringify(last.annotations)!==JSON.stringify(annotations);
}
export function submitProgressiveResponse(run: ProgressiveRun, lesson: ProgressiveLesson, level: ReadingLevel, questionId: string, id: string, at: string): ProgressiveRun {
  const q = lesson.questions.find(q=>q.id===questionId);
  const r = run.responses[questionId];
  const passage = progressivePassage(lesson,level);
  const validEvidence = passage.paragraphs.map(p=>p.id);
  if (!q || !r || (q.responseKind !== "explanation" && (r.choice === null || !Number.isInteger(r.choice) || !q.options[r.choice])) || !r.reason.trim() || !r.evidence.length
    || r.evidence.some(e=>!validEvidence.includes(e)) || !progressiveResponseChanged(r,run.annotations) || r.submissions.some(s=>s.id===id)) return run;
  const index = lesson.questions.indexOf(q);
  const submission: ProgressiveSubmission = {
    id,at,choice:q.responseKind === "explanation" ? null : r.choice,evidence:[...new Set(r.evidence)],reason:r.reason.trim(),hintLevel:r.hintLevel,
    choiceMatch:q.responseKind === "explanation" ? null : r.choice===q.answer,evidenceMatch:q.evidence.every(e=>r.evidence.includes(e)),explanationReview:"pending",
    support:index<2 || level==="supported" || r.hintLevel>0 || r.revealed || r.submissions.length>0 ? "guided" : "independent",
    revised:r.submissions.length>0,passageId:passage.id,level,annotations:structuredClone(run.annotations),passageExposure:"practiced",passageSnapshot:structuredClone(passage),questionSnapshot:structuredClone(q),
  };
  return {...run,responses:{...run.responses,[questionId]:{...r,choice:submission.choice,evidence:submission.evidence,reason:submission.reason,submissions:[...r.submissions,submission]}}};
}
export function canAdvanceProgressive(run: ProgressiveRun, lesson: ProgressiveLesson) {
  const r = run.responses[lesson.questions[run.index].id];
  const last = r?.submissions.slice(-1)[0];
  const open = lesson.questions[run.index].responseKind === "explanation";
  // For explanations, advancing records practice only; it never declares mastery or a correct answer.
  return !!last && !progressiveResponseChanged(r,run.annotations) && (((open || last.choiceMatch) && last.evidenceMatch) || r.revealed);
}
export function advanceProgressive(run: ProgressiveRun, lesson: ProgressiveLesson): ProgressiveRun {
  if (!canAdvanceProgressive(run,lesson)) return run;
  return run.index===lesson.questions.length-1 ? {...run,phase:"complete"} : {...run,index:run.index+1,reached:Math.max(run.reached,run.index+1)};
}
export function restartProgressive(run: ProgressiveRun): ProgressiveRun {
  return {...createProgressiveRun(),archives:[...run.archives,{responses:run.responses,annotations:run.annotations}]};
}
