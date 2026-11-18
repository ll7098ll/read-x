import { create } from 'zustand';
import { createJSONStorage, persist, type StateStorage } from 'zustand/middleware';
import { miniExamForms, transferChecks } from '../data/miniExams';
import { answerMiniQuestion, createMiniAttempt, miniItems, newPracticeId, submitMiniAttempt, validMiniForm, validQuestion } from '../services/miniExam';
import type { AssessmentScreen, AssessmentView, MiniExamAttempt, MiniGrade, Remediation, TransferAttempt } from '../types/miniExam';

export const ASSESSMENT_STORAGE_KEY = 'readx_student_assessment_v1';
export const useAssessmentStorageStatus = create<{ error: string }>(() => ({ error: '' }));
let corruptStorage = false;
export const assessmentStorage: StateStorage = {
  getItem: key => {
    try {
      const raw = localStorage.getItem(key);
      if (raw) JSON.parse(raw);
      return raw;
    } catch {
      corruptStorage = true;
      useAssessmentStorageStatus.setState({ error: '저장된 기록을 불러오지 못했어요. 현재 활동은 임시로 유지됩니다. 원래 기록은 덮어쓰지 않아요.' });
      return null;
    }
  },
  setItem: (key, value) => {
    if (corruptStorage) return;
    try { localStorage.setItem(key, value); useAssessmentStorageStatus.setState({ error: '' }); }
    catch { useAssessmentStorageStatus.setState({ error: '기기에 저장하지 못했어요. 창을 닫기 전에 기록 내보내기로 보관해 주세요.' }); }
  },
  removeItem: key => { try { localStorage.removeItem(key); } catch { useAssessmentStorageStatus.setState({ error: '저장 공간에 접근하지 못했어요.' }); } },
};

type State = {
  attempts: MiniExamAttempt[]; checks: TransferAttempt[]; remediations: Remediation[];
  view: AssessmentView; screen: AssessmentScreen; activePassage: number;
  setView: (view: AssessmentView) => void; open: (screen: AssessmentScreen) => void; setPassage: (index: number) => void;
  start: (grade: MiniGrade, now?: number) => string;
  answer: (id: string, questionId: string, choice: number, now?: number) => void;
  flag: (id: string, questionId: string) => void;
  submit: (id: string, now?: number) => void; expire: (now?: number) => void;
  beginRemediation: (attemptId: string, questionId: string, now?: number) => void;
  advanceRemediation: (id: string) => void; answerRemediation: (id: string, choice: number, now?: number) => void;
  beginCheck: (checkId: string, now?: number) => void;
  editCheck: (id: string, update: Partial<Pick<TransferAttempt, 'choice' | 'evidence'>>) => void;
  submitCheck: (id: string, now?: number) => void;
};
function seenFamilies(state: Pick<State, 'attempts' | 'checks'>) {
  return [...new Set([...state.attempts.flatMap(a => a.form.passages.map(p => p.familyId)), ...state.checks.map(a => a.check.familyId)])];
}
function validSavedAttempt(a: MiniExamAttempt) {
  return !!a && typeof a.id === 'string' && a.learnerId === 'local-practice' && validMiniForm(a.form)
    && Number.isFinite(a.startedAt) && Number.isFinite(a.deadlineAt) && a.deadlineAt === a.startedAt + a.form.durationSec * 1000
    && ['in_progress', 'submitted', 'auto_submitted'].includes(a.status)
    && (a.status === 'in_progress' || Number.isFinite(a.submittedAt)) && a.answers && a.firstAnswers
    && [a.answers, a.firstAnswers].every(answers => Object.entries(answers).every(([key, v]) => miniItems(a.form).some(i => i.question.id === key) && Number.isInteger(v) && v >= 0 && v < 5))
    && Array.isArray(a.flagged) && Array.isArray(a.freshFamilies);
}
function validSavedCheck(c: TransferAttempt) {
  return !!c && c.learnerId === 'local-practice' && typeof c.id === 'string' && [5, 6].includes(c.check?.grade)
    && Array.isArray(c.check.paragraphs) && validQuestion(c.check.question, c.check.paragraphs.map(p => p.id))
    && typeof c.check.familyId === 'string' && Number.isFinite(c.startedAt) && typeof c.fresh === 'boolean'
    && (c.choice === null || Number.isInteger(c.choice) && c.choice >= 0 && c.choice < 5)
    && Array.isArray(c.evidence) && c.evidence.every(id => c.check.paragraphs.some(p => p.id === id))
    && (c.submittedAt === undefined || Number.isFinite(c.submittedAt));
}
export function validateAssessmentSnapshot(value: any): boolean {
  try { return !!value && Array.isArray(value.attempts) && value.attempts.every(validSavedAttempt)
    && Array.isArray(value.checks) && value.checks.every(validSavedCheck)
    && Array.isArray(value.remediations) && value.remediations.every((r: Remediation) => r && typeof r.id === 'string'
      && Number.isFinite(r.startedAt) && Number.isInteger(r.step) && r.step >= 0 && r.step <= 2
      && Number.isInteger(r.tries) && r.tries >= 0 && [5, 6].includes(r.grade)
      && value.attempts.some((a: MiniExamAttempt) => a.id === r.attemptId && a.status !== 'in_progress' && miniItems(a.form).some(i => i.question.id === r.questionId && i.question.goal === r.goal)))
    && new Set(value.attempts.map((a: MiniExamAttempt) => a.id)).size === value.attempts.length
    && new Set(value.checks.map((a: TransferAttempt) => a.id)).size === value.checks.length
    && new Set(value.checks.map((a: TransferAttempt) => a.check.id)).size === value.checks.length;
  } catch { return false; }
}

export const useStudentAssessment = create<State>()(persist((set, get) => ({
  attempts: [], checks: [], remediations: [], view: 'overview', screen: { kind: 'dashboard' }, activePassage: 0,
  setView: view => set({ view, screen: { kind: 'dashboard' } }),
  open: screen => set(s => ({ screen, activePassage: 'id' in screen ? s.attempts.find(a => a.id === screen.id)?.passageIndex || 0 : 0 })),
  setPassage: index => set(s => {
    if (!Number.isInteger(index)) return {};
    const a = 'id' in s.screen ? s.attempts.find(a => a.id === ('id' in s.screen ? s.screen.id : '')) : undefined;
    const activePassage = Math.max(0, Math.min(Math.floor(index), (a?.form.passages.length || 1) - 1));
    return { activePassage, attempts: a?.status === 'in_progress' ? s.attempts.map(row => row.id === a.id ? { ...row, passageIndex: activePassage } : row) : s.attempts };
  }),
  start: (grade, now = Date.now()) => {
    get().expire(now);
    const current = get().attempts.find(a => a.form.grade === grade && a.status === 'in_progress');
    if (current) { set({ screen: { kind: 'exam', id: current.id }, activePassage: current.passageIndex || 0 }); return current.id; }
    const form = miniExamForms.find(f => f.grade === grade);
    if (!form) return '';
    const attempt = createMiniAttempt(form, seenFamilies(get()), now);
    set(s => ({ attempts: [...s.attempts, attempt], screen: { kind: 'exam', id: attempt.id }, activePassage: 0 }));
    return attempt.id;
  },
  answer: (id, questionId, choice, now = Date.now()) => set(s => ({ attempts: s.attempts.map(a => a.id === id ? answerMiniQuestion(a, questionId, choice, now) : a) })),
  flag: (id, questionId) => set(s => ({ attempts: s.attempts.map(a => a.id === id && a.status === 'in_progress' && Date.now() < a.deadlineAt && miniItems(a.form).some(i => i.question.id === questionId)
    ? { ...a, flagged: a.flagged.includes(questionId) ? a.flagged.filter(q => q !== questionId) : [...a.flagged, questionId] } : a) })),
  submit: (id, now = Date.now()) => {
    if (!get().attempts.some(a => a.id === id)) return;
    set(s => ({ attempts: s.attempts.map(a => a.id === id ? submitMiniAttempt(a, now) : a), screen: { kind: 'result', id } }));
  },
  expire: (now = Date.now()) => {
    if (get().attempts.some(a => a.status === 'in_progress' && now >= a.deadlineAt)) {
      set(s => ({ attempts: s.attempts.map(a => a.status === 'in_progress' && now >= a.deadlineAt ? submitMiniAttempt(a, now) : a) }));
    }
  },
  beginRemediation: (attemptId, questionId, now = Date.now()) => {
    const a = get().attempts.find(a => a.id === attemptId && a.status !== 'in_progress');
    const q = a && miniItems(a.form).find(i => i.question.id === questionId)?.question;
    if (!a || !q) return;
    const existing = get().remediations.find(r => r.attemptId === attemptId && r.questionId === questionId);
    if (existing) { set({ screen: { kind: 'remediation', id: existing.id } }); return; }
    const r: Remediation = { id: newPracticeId(), attemptId, questionId, grade: a.form.grade, goal: q.goal,
      startedAt: now, step: 0, firstChoice: null, choice: null, tries: 0 };
    set(s => ({ remediations: [...s.remediations, r], screen: { kind: 'remediation', id: r.id } }));
  },
  advanceRemediation: id => set(s => ({ remediations: s.remediations.map(r => r.id === id && !r.completedAt ? { ...r, step: Math.min(2, r.step + 1) } : r) })),
  answerRemediation: (id, choice, now = Date.now()) => {
    const r = get().remediations.find(r => r.id === id);
    const a = r && get().attempts.find(a => a.id === r.attemptId);
    const q = a && miniItems(a.form).find(i => i.question.id === r?.questionId)?.question;
    if (!r || !q || r.completedAt || r.step !== 2 || !Number.isInteger(choice) || choice < 0 || choice > 4) return;
    set(s => ({ remediations: s.remediations.map(row => row.id === id ? { ...row, firstChoice: row.firstChoice ?? choice, choice, tries: row.tries + 1,
      ...(choice === q.answer ? { completedAt: now } : {}) } : row) }));
  },
  beginCheck: (checkId, now = Date.now()) => {
    const check = transferChecks.find(c => c.id === checkId);
    if (!check) return;
    const current = get().checks.find(c => c.check.id === checkId);
    if (current) { set({ screen: { kind: 'transfer', id: current.id } }); return; }
    const run: TransferAttempt = { id: newPracticeId(), learnerId: 'local-practice', check: structuredClone(check), startedAt: now,
      fresh: !seenFamilies(get()).includes(check.familyId), choice: null, evidence: [] };
    set(s => ({ checks: [...s.checks, run], screen: { kind: 'transfer', id: run.id } }));
  },
  editCheck: (id, update) => set(s => ({ checks: s.checks.map(c => {
    if (c.id !== id || c.submittedAt) return c;
    const choice = update.choice === undefined ? c.choice : update.choice;
    if (choice !== null && (!Number.isInteger(choice) || choice < 0 || choice > 4)) return c;
    const evidence = update.evidence ?? c.evidence;
    if (!Array.isArray(evidence) || evidence.some(id => !c.check.paragraphs.some(p => p.id === id))) return c;
    return { ...c, choice, evidence: [...new Set(evidence)] };
  }) })),
  submitCheck: (id, now = Date.now()) => set(s => ({ checks: s.checks.map(c => c.id === id && !c.submittedAt && c.choice !== null && c.evidence.length
    ? { ...c, submittedAt: Math.max(now, c.startedAt) } : c) })),
}), {
  name: ASSESSMENT_STORAGE_KEY, version: 1, storage: createJSONStorage(() => assessmentStorage),
  merge: (saved: any, current) => {
    if (saved === undefined) return current;
    if (!validateAssessmentSnapshot(saved)) {
      corruptStorage = true;
      useAssessmentStorageStatus.setState({ error: '저장된 기록의 형식을 확인하지 못했어요. 원래 기록을 보존하고 임시로 시작합니다.' });
      return current;
    }
    const views: AssessmentView[] = ['overview', 'exams', 'report', 'goals', 'history'];
    const screen = saved.screen;
    const validScreen = screen && (screen.kind === 'dashboard'
      || ['exam', 'result'].includes(screen.kind) && saved.attempts.some((a: MiniExamAttempt) => a.id === screen.id)
      || screen.kind === 'remediation' && saved.remediations.some((r: Remediation) => r.id === screen.id)
      || screen.kind === 'transfer' && saved.checks.some((c: TransferAttempt) => c.id === screen.id));
    return { ...current, attempts: saved.attempts, checks: saved.checks, remediations: saved.remediations,
      view: views.includes(saved.view) ? saved.view : 'overview', screen: validScreen ? screen : { kind: 'dashboard' },
      activePassage: Number.isInteger(saved.activePassage) ? Math.max(0, saved.activePassage) : 0 };
  },
}));
