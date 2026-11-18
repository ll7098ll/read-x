import type { MiniExamAttempt, MiniExamForm, MiniGoalKey, MiniGrade, MiniQuestion, Remediation, TransferAttempt } from '../types/miniExam';

export const miniSkills = ['직접 확인', '정보 연결', '추론', '근거 판단', '새 상황 적용'] as const;
export const miniGoalKeys: MiniGoalKey[] = ['compare', 'cause', 'evaluate'];
export const miniItems = (form: MiniExamForm) => form.passages.flatMap(p => p.questions.map(q => ({ passage: p, question: q })));
export const newPracticeId = () => globalThis.crypto?.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2)}`;
export const kstDay = (at: number) => new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Seoul', year: 'numeric', month: '2-digit', day: '2-digit' }).format(at);
export const scorePercent = (correct: number, total: number) => total ? Math.round(correct / total * 1000) / 10 : null;

export function validQuestion(q: MiniQuestion, paragraphIds: string[]) {
  return !!q && typeof q.id === 'string' && miniGoalKeys.includes(q.goal) && miniSkills.includes(q.skill)
    && typeof q.prompt === 'string' && Array.isArray(q.options) && q.options.length === 5
    && q.options.every(s => typeof s === 'string' && s.trim()) && new Set(q.options).size === 5
    && Number.isInteger(q.answer) && q.answer >= 0 && q.answer < 5
    && Array.isArray(q.evidence) && q.evidence.length > 0 && q.evidence.every(id => paragraphIds.includes(id))
    && (!q.evidenceAlternatives || q.evidenceAlternatives.every(set => Array.isArray(set) && set.length && set.every(id => paragraphIds.includes(id))))
    && typeof q.explanation === 'string' && Array.isArray(q.optionReasons) && q.optionReasons.length === 5;
}
export function validMiniForm(form: MiniExamForm) {
  if (!form || ![5, 6].includes(form.grade) || !form.id || !Number.isInteger(form.version) || form.version < 1
    || !Number.isFinite(form.durationSec) || form.durationSec <= 0 || !Array.isArray(form.passages) || !form.passages.length) return false;
  const ids: string[] = [];
  for (const p of form.passages) {
    if (!p?.id || !p.familyId || !Array.isArray(p.paragraphs) || !p.paragraphs.length || !Array.isArray(p.questions) || !p.questions.length) return false;
    const paragraphs = p.paragraphs.map(row => row?.id);
    if (new Set(paragraphs).size !== paragraphs.length || p.paragraphs.some(row => !row?.id || typeof row.text !== 'string')) return false;
    if (p.questions.some(q => !validQuestion(q, paragraphs))) return false;
    ids.push(...p.questions.map(q => q.id));
  }
  return new Set(ids).size === ids.length && new Set(form.passages.map(p => p.familyId)).size === form.passages.length;
}
export function createMiniAttempt(form: MiniExamForm, seenFamilies: string[], now: number, id = newPracticeId()): MiniExamAttempt {
  if (!validMiniForm(form) || !Number.isFinite(now)) throw new Error('시험지 구성을 확인해 주세요.');
  return { id, learnerId: 'local-practice', form: structuredClone(form), startedAt: now,
    deadlineAt: now + form.durationSec * 1000, status: 'in_progress', answers: {}, firstAnswers: {}, flagged: [],
    freshFamilies: form.passages.filter(p => !seenFamilies.includes(p.familyId)).map(p => p.familyId) };
}
export function submitMiniAttempt(attempt: MiniExamAttempt, now: number): MiniExamAttempt {
  if (attempt.status !== 'in_progress') return attempt;
  const expired = now >= attempt.deadlineAt;
  return { ...attempt, status: expired ? 'auto_submitted' : 'submitted', submittedAt: Math.max(attempt.startedAt, Math.min(now, attempt.deadlineAt)) };
}
export function answerMiniQuestion(attempt: MiniExamAttempt, questionId: string, choice: number, now: number): MiniExamAttempt {
  if (attempt.status !== 'in_progress') return attempt;
  if (now >= attempt.deadlineAt) return submitMiniAttempt(attempt, now);
  if (!Number.isInteger(choice) || choice < 0 || choice > 4 || !miniItems(attempt.form).some(i => i.question.id === questionId)) return attempt;
  return { ...attempt, answers: { ...attempt.answers, [questionId]: choice },
    firstAnswers: { ...attempt.firstAnswers, [questionId]: attempt.firstAnswers[questionId] ?? choice } };
}
export function miniScore(attempt: MiniExamAttempt) {
  const items = miniItems(attempt.form);
  const results = items.map(({ passage, question }) => ({ passage, question, choice: attempt.answers[question.id] ?? null,
    outcome: attempt.answers[question.id] === undefined ? 'unanswered' as const : attempt.answers[question.id] === question.answer ? 'correct' as const : 'wrong' as const }));
  const correct = results.filter(r => r.outcome === 'correct').length;
  const unanswered = results.filter(r => r.outcome === 'unanswered').length;
  return { results, correct, unanswered, wrong: items.length - correct - unanswered, total: items.length,
    percent: scorePercent(correct, items.length), elapsedSec: Math.max(0, Math.round(((attempt.submittedAt ?? attempt.startedAt) - attempt.startedAt) / 1000)),
    skills: miniSkills.map(skill => { const rows = results.filter(r => r.question.skill === skill); const passed = rows.filter(r => r.outcome === 'correct').length; return { skill, correct: passed, total: rows.length, percent: scorePercent(passed, rows.length) }; }) };
}
export const transferSuccess = (a: TransferAttempt) => a.choice === a.check.question.answer
  && [a.check.question.evidence, ...(a.check.question.evidenceAlternatives || [])].some(set =>
    [...new Set(a.evidence)].sort().join('|') === [...new Set(set)].sort().join('|'));

type Evidence = { id: string; session: string; at: number; family: string; success: boolean; transfer: boolean };
/** Rules are practice indicators for the three explicitly defined selection tasks, not a calibrated literacy index. */
export function goalProgress(goal: MiniGoalKey, grade: MiniGrade, attempts: MiniExamAttempt[], checks: TransferAttempt[], reviews: Remediation[], now: number) {
  const evidence: Evidence[] = [];
  for (const a of attempts.filter(a => a.form.grade === grade && a.status !== 'in_progress')) {
    for (const r of miniScore(a).results.filter(r => r.question.goal === goal && a.freshFamilies.includes(r.passage.familyId))) {
      evidence.push({ id: `${a.id}:${r.question.id}`, session: a.id, at: a.submittedAt!, family: r.passage.familyId, success: r.outcome === 'correct', transfer: false });
    }
  }
  for (const a of checks.filter(a => a.check.grade === grade && a.check.goal === goal && a.submittedAt && a.fresh)) {
    evidence.push({ id: a.id, session: a.id, at: a.submittedAt!, family: a.check.familyId, success: transferSuccess(a), transfer: true });
  }
  const rows = [...new Map(evidence.map(e => [e.id, e])).values()].sort((a, b) => a.at - b.at || a.id.localeCompare(b.id, undefined, { numeric: true }));
  let earned: 'unobserved' | 'collecting' | 'independent' | 'transfer' | 'maintained' = rows.length ? 'collecting' : 'unobserved';
  let transferAt: number | null = null;
  for (let i = 0; i < rows.length; i++) {
    const history = rows.slice(0, i + 1), current = history.filter(e => e.at >= rows[i].at - 28 * 86400000), last = current.slice(-5);
    const independent = last.length === 5 && last.filter(e => e.success).length >= 4 && rows[i].success
      && new Set(current.map(e => e.family)).size >= 3 && new Set(current.map(e => e.session)).size >= 2;
    if (independent && earned !== 'transfer' && earned !== 'maintained') earned = 'independent';
    if (independent && new Set(current.filter(e => e.transfer && e.success).map(e => e.family)).size >= 2) {
      earned = earned === 'maintained' ? earned : 'transfer'; transferAt ??= rows[i].at;
    }
    if (transferAt !== null && rows[i].success && rows[i].transfer && rows[i].at >= transferAt + 7 * 86400000) earned = 'maintained';
  }
  const recent = rows.filter(e => e.at >= now - 28 * 86400000), lastFive = recent.slice(-5);
  const guided = reviews.filter(r => r.grade === grade && r.goal === goal && r.completedAt).length;
  const lastAt = rows.slice(-1)[0]?.at;
  const achieved = ['independent', 'transfer', 'maintained'].includes(earned);
  return { goal, state: earned, achieved, guided, evidence: rows, total: rows.length, success: rows.filter(e => e.success).length,
    recentSuccess: lastFive.filter(e => e.success).length, recentTotal: lastFive.length,
    families: new Set(recent.map(e => e.family)).size, sessions: new Set(recent.map(e => e.session)).size,
    transferFamilies: new Set(rows.filter(e => e.transfer && e.success).map(e => e.family)).size,
    needsRecheck: achieved && (!!lastAt && now - lastAt > 28 * 86400000 || rows.slice(-1)[0]?.success === false), lastAt };
}
export function miniHistory(attempts: MiniExamAttempt[], reviews: Remediation[], checks: TransferAttempt[], grade: MiniGrade) {
  return [
    ...attempts.filter(a => a.form.grade === grade).map(a => ({ id: a.id, kind: a.status === 'in_progress' ? '진행 중인 모의고사' : '모의고사', title: a.form.title,
      at: a.submittedAt ?? a.startedAt, detail: a.status === 'in_progress' ? '이어서 풀 수 있어요' : `${miniScore(a).correct}/${miniScore(a).total} · ${miniScore(a).percent}점`, screen: a.status === 'in_progress' ? 'exam' as const : 'result' as const })),
    ...reviews.filter(r => r.grade === grade).map(r => ({ id: r.id, kind: '보충학습', title: '단서와 관계 다시 익히기', at: r.completedAt ?? r.startedAt, detail: r.completedAt ? '도움받아 복습 완료' : '복습 진행 중', screen: 'remediation' as const })),
    ...checks.filter(c => c.check.grade === grade).map(c => ({ id: c.id, kind: '새 글 확인', title: c.check.title, at: c.submittedAt ?? c.startedAt,
      detail: !c.submittedAt ? '확인 진행 중' : transferSuccess(c) ? '답과 근거 확인 성공' : '답과 근거를 다시 살펴봐요', screen: 'transfer' as const })),
  ].sort((a, b) => b.at - a.at || a.id.localeCompare(b.id));
}
