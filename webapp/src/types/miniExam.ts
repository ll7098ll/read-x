export type MiniGrade = 5 | 6;
export type MiniGoalKey = 'compare' | 'cause' | 'evaluate';
export type MiniSkill = '직접 확인' | '정보 연결' | '추론' | '근거 판단' | '새 상황 적용';
export type MiniParagraph = { id: string; text: string };
export type MiniQuestion = {
  id: string; goal: MiniGoalKey; skill: MiniSkill; prompt: string; scenario?: string;
  options: string[]; answer: number; evidence: string[]; explanation: string; optionReasons: string[];
  evidenceAlternatives?: string[][];
};
export type MiniPassage = { id: string; familyId: string; title: string; subject: string; paragraphs: MiniParagraph[]; questions: MiniQuestion[] };
/** Personal practice content. This client-side form is never an official or secure assessment. */
export type MiniExamForm = { id: string; version: number; grade: MiniGrade; title: string; durationSec: number; passages: MiniPassage[]; editorialStatus: 'pilot' };
export type MiniExamAttempt = {
  id: string; learnerId: 'local-practice'; form: MiniExamForm; startedAt: number; deadlineAt: number;
  status: 'in_progress' | 'submitted' | 'auto_submitted'; submittedAt?: number;
  answers: Record<string, number>; firstAnswers: Record<string, number>; flagged: string[]; freshFamilies: string[];
  passageIndex?: number;
};
export type MiniGoal = { key: MiniGoalKey; title: string; criterion: string; steps: [string, string, string] };
export type TransferCheck = { id: string; grade: MiniGrade; goal: MiniGoalKey; familyId: string; title: string; paragraphs: MiniParagraph[]; question: MiniQuestion };
export type TransferAttempt = {
  id: string; learnerId: 'local-practice'; check: TransferCheck; startedAt: number; submittedAt?: number;
  fresh: boolean; choice: number | null; evidence: string[];
};
export type Remediation = {
  id: string; attemptId: string; questionId: string; grade: MiniGrade; goal: MiniGoalKey;
  startedAt: number; step: number; firstChoice: number | null; choice: number | null; tries: number; completedAt?: number;
};
export type AssessmentView = 'overview' | 'exams' | 'report' | 'goals' | 'history';
export type AssessmentScreen = { kind: 'dashboard' } | { kind: 'exam' | 'result' | 'remediation' | 'transfer'; id: string };
