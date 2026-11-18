import {restrictionIds} from '../shared/processing-restrictions.mjs';
import { createOverviewService } from './overview-service.mjs';
import { createPlacementService } from './placement-service.mjs';
import { createCourseService } from './course-service.mjs';
import { createCalibrationApplication } from './calibration-application.mjs';
import { createPilotService } from './pilot-service.mjs';
import { canTeachClass, classForStudents } from '../shared/organization.mjs';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';

const lessons = JSON.parse(readFileSync(new URL('../src/data/corpusLessons.generated.json', import.meta.url), 'utf8'));
const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
const levels = ['supported', 'standard', 'challenge'];
const clean = (value, max) => typeof value === 'string' && value.length <= max ? value.trim() : '';
const hash = value => createHash('sha256').update(JSON.stringify(value)).digest('hex');
const blank = () => ({ phase: 'model', modelStep: 0, index: 0, reached: 0, responses: {}, annotations: [], archives: [] });
const questions = (lesson, level) => lesson.levelQuestions?.[level] || lesson.questions;
const paragraphs = (lesson, level) => levels.slice(0, levels.indexOf(level) + 1).flatMap(l => lesson.layers[l]);
const summary = a => ({ id: a.id, classId:a.classId, title: a.title, lessonId: a.lesson.id, lessonTitle: a.lesson.title, grade: a.lesson.grade, level: a.level, studentIds: a.studentIds, createdAt: a.createdAt, dueAt: a.dueAt, contentHash: a.contentHash });

// Each assignment, learner run and release has its own durable row. The caller's
// transaction also includes the shared account/session state and audit events.
export function createLearningService({ db, randomUUID }) {
  for (const table of ['learning_assignments', 'learning_runs', 'learning_releases', 'learning_approvals'])
    db.exec(`CREATE TABLE IF NOT EXISTS ${table} (id TEXT PRIMARY KEY, tenant_id TEXT NOT NULL, body TEXT NOT NULL)`);
  for (const table of ['learning_assignments','learning_runs','learning_releases','learning_approvals']) {
    for (const row of db.prepare(`SELECT id,tenant_id,body FROM ${table}`).all()) { const id = JSON.parse(row.body).id, key = row.tenant_id+':'+id; if(row.id!==key) db.prepare(`UPDATE ${table} SET id=? WHERE id=? AND tenant_id=?`).run(key,row.id,row.tenant_id); }
  }
  db.exec('CREATE INDEX IF NOT EXISTS learning_runs_tenant ON learning_runs(tenant_id)');
  const overview = createOverviewService({db});
  const all = (table, tenant) => db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r => JSON.parse(r.body));
  const get = (table, id, tenant) => { const r = db.prepare(`SELECT body FROM ${table} WHERE id=? AND tenant_id=?`).get(tenant+':'+id, tenant); return r && JSON.parse(r.body); };
  const put = (table, value, tenant) => db.prepare(`INSERT INTO ${table}(id,tenant_id,body) VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET body=excluded.body`).run(tenant+':'+value.id, tenant, JSON.stringify(value));
  const report = (run, assignment) => {
    const rows = questions(assignment.lesson, assignment.level).map(q => {
      const submissions = run.run.responses[q.id]?.submissions || [];
      return { questionId: q.id, prompt: q.prompt, skill: q.skill, submissions, review: run.reviews?.[q.id] || null };
    });
    return { rows, submitted: rows.filter(r => r.submissions.length).length, total: rows.length, reviewed: rows.filter(r => r.review).length, writing: run.writing, note: run.note || '' };
  };
  const view = (run, assignment, viewer) => ({ ...run, assignment: {...summary(assignment),studentIds:viewer?.role==='teacher'?assignment.studentIds:[run.studentId],dueAt:Math.max(run.dueAtOverride||0,assignment.dueAt)}, lesson: assignment.lesson, report: report(run, assignment) });
  const validateRun = (input, previous, assignment, at) => {
    if (!input || !['model', 'questions', 'complete'].includes(input.phase) || !Number.isInteger(input.index) || input.index < 0 || input.index >= questions(assignment.lesson, assignment.level).length || !Number.isInteger(input.modelStep) || input.modelStep < 0 || input.modelStep >= assignment.lesson.model.length) fail(400, '수업 진행 정보를 확인해 주세요.');
    const qs = questions(assignment.lesson, assignment.level), ps = paragraphs(assignment.lesson, assignment.level);
    const ids = ps.map(p => p.id), responses = {}, allSubmissionIds = new Set();
    const notes = input.annotations || [];
    if (!Array.isArray(notes) || notes.length > 100) fail(400, '생각 표시 수를 확인해 주세요.');
    const annotations = notes.map(n => {
      const p = ps.find(p => p.id === n.sentenceId);
      if (n.passageId !== `${assignment.lesson.id}-${assignment.level}`) fail(400, '다른 지문의 생각 표시는 사용할 수 없습니다.');
      for (const a of [n.anchor, n.linkedAnchor].filter(Boolean)) {
        const target = ps.find(p => p.id === a.sentenceId);
        if (!target || !Number.isInteger(a.start) || !Number.isInteger(a.end) || a.start < 0 || a.start >= a.end || a.end > target.text.length || target.text.slice(a.start, a.end) !== a.quote) fail(400, '생각 표시 위치를 확인해 주세요.');
      }
      if (!p || !['target', 'evidence', 'link', 'condition', 'question'].includes(n.kind) || !clean(n.id, 150) || !clean(n.note || '', 2000) || (n.quote && !p.text.includes(n.quote))) fail(400, '본문과 생각 표시를 확인해 주세요.');
      return { ...n, note: clean(n.note, 2000) };
    });
    for (const q of qs) {
      const r = input.responses?.[q.id], old = previous.responses[q.id];
      if (!r) { if (old) fail(409, '이전 응답 기록을 지울 수 없습니다.'); continue; }
      if (!Array.isArray(r.evidence) || r.evidence.some(id => !ids.includes(id)) || typeof r.reason !== 'string' || r.reason.length > 5000 || !(r.choice === null || Number.isInteger(r.choice) && r.choice >= 0 && r.choice < q.options.length) || !Number.isInteger(r.hintLevel) || r.hintLevel < 0 || r.hintLevel > 3 || !Array.isArray(r.submissions) || r.submissions.length > 50) fail(400, '응답·근거·도움 기록을 확인해 주세요.');
      const oldSubs = old?.submissions || [];
      if (r.submissions.length < oldSubs.length) fail(409, '처음 답과 수정 이력을 보존해 주세요.');
      const subs = r.submissions.map((s, i) => {
        if (!clean(s.id, 150) || allSubmissionIds.has(s.id)) fail(400, '응답 식별자가 중복되었거나 올바르지 않습니다.');
        allSubmissionIds.add(s.id);
        if (i < oldSubs.length) {
          const prior = oldSubs[i];
          if (s.id !== prior.id || s.choice !== prior.choice || s.reason !== prior.reason || JSON.stringify(s.evidence) !== JSON.stringify(prior.evidence)) fail(409, '제출했던 응답을 덮어쓸 수 없습니다.');
          return prior;
        }
        if (!clean(s.reason, 5000) || !Array.isArray(s.evidence) || !s.evidence.length || s.evidence.some(id => !ids.includes(id)) || (q.responseKind !== 'explanation' && !(Number.isInteger(s.choice) && s.choice >= 0 && s.choice < q.options.length))) fail(400, '판단과 근거, 설명을 함께 남겨 주세요.');
        const hintLevel = Math.max(old?.hintLevel || 0, Math.min(3, Number(s.hintLevel) || 0));
        return { id: s.id, at: new Date(at).toISOString(), choice: q.responseKind === 'explanation' ? null : s.choice, reason: s.reason.trim(), evidence: [...new Set(s.evidence)], hintLevel,
          choiceMatch: q.responseKind === 'explanation' ? null : s.choice === q.answer, evidenceMatch: q.evidence.every(id => s.evidence.includes(id)), explanationReview: 'pending',
          support: qs.indexOf(q) < 2 || assignment.level === 'supported' || hintLevel > 0 || old?.revealed || r.revealed || i > 0 ? 'guided' : 'independent',
          revised: i > 0, level: assignment.level, passageExposure: 'practiced', annotations: structuredClone(annotations) };
      });
      responses[q.id] = { choice: q.responseKind === 'explanation' ? null : r.choice, evidence: [...new Set(r.evidence)], reason: r.reason, hintLevel: Math.max(old?.hintLevel || 0, r.hintLevel), revealed: !!old?.revealed || (!!r.revealed && subs.length > 0), submissions: subs };
    }
    if (input.phase === 'complete' && qs.some(q => !responses[q.id]?.submissions.length)) fail(400, '모든 활동에 응답한 뒤 수업을 마쳐 주세요.');
    return { phase: input.phase, modelStep: input.modelStep, index: input.index, reached: Math.max(previous.reached, Math.min(qs.length - 1, Number(input.reached) || 0)), responses, annotations, archives: [] };
  };
  const upgrade = state => { for(const tenant of [...new Set(state.users.map(u=>u.tenantId))]) for (const a of all('learning_assignments',tenant).filter(a=>!a.classId)) { a.classId=state.users.find(v=>v.id===a.teacherId)?.classIds?.[0] || state.users.find(v=>v.id===a.studentIds[0])?.classId; put('learning_assignments',a,tenant); } };
  const route = ({ user: u, state, path, method, body, at }) => {
    upgrade(state);
    const blocked=restrictionIds(state,at),visibleAll=table=>all(table,u.tenantId).filter(r=>!blocked.has(r.studentId)&&!r.processingWithheld).map(r=>Array.isArray(r.studentIds)?{...r,studentIds:r.studentIds.filter(id=>!blocked.has(id))}:r).filter(r=>!r.studentIds||r.studentIds.length);
    if(path.startsWith('/learning/calibration')) return calibration.route({user:u,state,path,method,body,at});
    if(path.startsWith('/learning/pilot')) return pilot({user:u,state,path,method,body,at});
    if(path.startsWith('/learning/placement')) return placement({user:u,state,path,method,body,at});
    if(path.startsWith('/learning/course')) return course({user:u,state,path,method,body,at});
    if(path.startsWith('/overview'))return overview.route({user:u,state,path,method,body,at});
    const teacher = () => { if (u.role !== 'teacher') fail(403, '교사 권한이 필요합니다.'); };
    const audit = (action, id) => state.audit.push({ at, actor: u.id, action, id });
    if (path === '/learning/catalog' && method === 'GET') {
      teacher();
      const approvals = all('learning_approvals', u.tenantId);
      return { lessons: lessons.map(l => ({ id: l.id, title: l.title, grade: l.grade, goalIds: l.goalIds, version: l.version, approved: approvals.some(a => a.id === l.id && a.contentHash === hash(l)), editorialStatus: '교사 검토와 학년별 시범 대상' })) };
    }
    const catalog = /^\/learning\/catalog\/([^/]+)$/.exec(path);
    if (catalog && method === 'GET') { teacher(); const l = lessons.find(l => l.id === catalog[1]); if (!l) fail(404, '수업을 찾을 수 없습니다.'); return { lesson: l, contentHash: hash(l) }; }
    if (path === '/learning/approvals' && method === 'POST') {
      teacher(); const l = lessons.find(l => l.id === body.lessonId);
      if (!l || hash(l) !== body.contentHash || !clean(body.note, 2000) || body.pilot !== true) fail(400, '지문·문항을 검토한 의견과 시범 수업 승인이 필요합니다.');
      put('learning_approvals', { id: l.id, contentHash: hash(l), note: body.note.trim(), reviewedBy: u.id, reviewedAt: at, scope: 'teacher-approved-pilot' }, u.tenantId);
      audit('learning.approve', l.id); return { ok: true };
    }
    if (path === '/learning/dashboard' && method === 'GET') {
      const accessible = a => u.role === 'teacher' ? canTeachClass(u,a.classId) : a.studentIds.some(id => u.role === 'student' ? id === u.id : u.childIds.includes(id));
      const assignments = visibleAll('learning_assignments').filter(accessible);
      const runs = visibleAll('learning_runs').filter(r => u.role === 'teacher' ? assignments.some(a=>a.id===r.assignmentId) : u.role === 'student' && r.studentId === u.id);
      const released = visibleAll('learning_releases').filter(r => u.role === 'parent' && u.childIds.includes(r.studentId));
      return { assignments: assignments.map(a => ({ ...summary(a), studentIds: a.studentIds.filter(id => u.role === 'teacher' || (u.role === 'student' ? id === u.id : u.childIds.includes(id))) })), runs: [...runs.map(r => ({ id: r.id, assignmentId: r.assignmentId, studentId: r.studentId, status: r.status, revision: r.revision, updatedAt: r.updatedAt, publishedAt: r.publishedAt })), ...released.map(r => ({ id: r.id, assignmentId: r.assignmentId, studentId: r.studentId, status: 'published', updatedAt: r.publishedAt, publishedAt: r.publishedAt }))] };
    }
    if (path === '/learning/assignments' && method === 'POST') {
      teacher(); const l = lessons.find(l => l.id === body.lessonId), approval = l && get('learning_approvals', l.id, u.tenantId);
      if (!l || !approval || approval.contentHash !== hash(l)) fail(409, '교사 검토와 시범 승인 후 배정할 수 있습니다.');
      const ids = [...new Set(Array.isArray(body.studentIds) ? body.studentIds : [])];
      if (!ids.length || ids.some(id => !state.users.some(s => s.id === id && s.tenantId === u.tenantId && s.role === 'student')) || !levels.includes(body.level) || !Number.isFinite(body.dueAt) || body.dueAt <= at) fail(400, '학생·글 수준·마감 시각을 확인해 주세요.');
      const classId=classForStudents(state,u,ids,body.classId,at);
      const a = { id: randomUUID(), tenantId: u.tenantId, classId, teacherId: u.id, title: clean(body.title, 100) || l.title, lesson: structuredClone(l), contentHash: hash(l), approval: structuredClone(approval), studentIds: ids, level: body.level, dueAt: body.dueAt, createdAt: at };
      put('learning_assignments', a, u.tenantId); audit('learning.assign', a.id); return { assignment: summary(a) };
    }
    const extend = /^\/learning\/assignments\/([^/]+)\/extend$/.exec(path);
    if (extend && method === 'POST') {
      teacher(); const a = get('learning_assignments', extend[1], u.tenantId);
      if (!a || !canTeachClass(u,a.classId)) fail(404, '담당 수업을 찾을 수 없습니다.');
      if (!Number.isFinite(body.dueAt) || body.dueAt <= Math.max(at, a.dueAt) || !clean(body.reason, 1000)) fail(400, '새 제출 기한과 연장 사유를 확인해 주세요.');
      a.extensions ||= []; a.extensions.push({ previousDueAt: a.dueAt, dueAt: body.dueAt, at, actor: u.id, reason: body.reason.trim() }); a.dueAt = body.dueAt;
      put('learning_assignments', a, u.tenantId); audit('learning.extend', a.id); return { assignment: summary(a) };
    }
    const start = /^\/learning\/assignments\/([^/]+)\/start$/.exec(path);
    if (start && method === 'POST') {
      const a = get('learning_assignments', start[1], u.tenantId);
      if (!a || u.role !== 'student' || !a.studentIds.includes(u.id)) fail(404, '배정된 수업을 찾을 수 없습니다.');
      const old = visibleAll('learning_runs').find(r => r.assignmentId === a.id && r.studentId === u.id);
      if (old) return view(old, a, u);
      if (at > a.dueAt) fail(409, '수업 제출 기간이 지났습니다. 선생님에게 문의해 주세요.');
      const r = { id: randomUUID(), assignmentId: a.id, studentId: u.id, studentName: u.name, status: 'in_progress', revision: 0, run: blank(), writing: '', writingHistory: [], reviews: {}, createdAt: at, updatedAt: at };
      put('learning_runs', r, u.tenantId); return view(r, a, u);
    }
    const match = /^\/learning\/runs\/([^/]+)(?:\/(save|submit|review|revoke))?$/.exec(path);
    if (match) {
      const r = get('learning_runs', match[1], u.tenantId);
      if (!r) fail(404, '수업 기록을 찾을 수 없습니다.');
      const a = get('learning_assignments', r.assignmentId, u.tenantId);
      if (u.role === 'parent') {
        const published = get('learning_releases', r.id, u.tenantId);
        if (method !== 'GET' || match[2] || !published || published.processingWithheld || !u.childIds.includes(r.studentId)) fail(404, '공개된 자녀 기록이 없습니다.');
        return {...published.snapshot,assignment:{...published.snapshot.assignment,studentIds:[r.studentId]}};
      }
      if (!(u.role === 'teacher' && canTeachClass(u,a.classId)) && !(u.role === 'student' && r.studentId === u.id)) fail(404, '본인의 수업 기록만 확인할 수 있습니다.');
      if (!match[2] && method === 'GET') return view(r, a, u);
      if (match[2] === 'save' && method === 'POST') {
        if (u.role !== 'student' || r.status !== 'in_progress') fail(409, '진행 중인 본인 수업만 수정할 수 있습니다.');
        if (!clean(body.mutationId, 150)) fail(400, '저장 요청 식별자가 필요합니다.');
        if (r.lastMutationId === body.mutationId) return view(r, a, u);
        if (body.revision !== r.revision) fail(409, '다른 화면에서 기록이 바뀌었습니다. 현재 입력을 보관하고 다시 불러와 주세요.');
        if (typeof body.writing !== 'string' || body.writing.length > 10000) fail(400, '글은 10000자 이내로 작성해 주세요.');
        r.run = validateRun(body.run, r.run, a, at);
        if (r.writing !== body.writing) r.writingHistory.push({ text: body.writing, at });
        r.writing = body.writing; r.updatedAt = at; r.revision++; r.lastMutationId = body.mutationId;
        put('learning_runs', r, u.tenantId); return view(r, a, u);
      }
      if (match[2] === 'submit' && method === 'POST') {
        if (u.role !== 'student') fail(403, '학생이 자신의 수업을 제출해야 합니다.');
        if (r.status !== 'in_progress') return view(r, a, u);
        if (body.revision !== r.revision) fail(409, '최신 답안을 저장한 뒤 제출해 주세요.');
        if (at > (Math.max(r.dueAtOverride||0,a.dueAt))) fail(409, '제출 기간이 지났습니다. 입력은 보존되어 있으니 선생님에게 문의해 주세요.');
        if (questions(a.lesson, a.level).some(q => !r.run.responses[q.id]?.submissions.length) || !r.writing.trim()) fail(400, '모든 활동과 내 말로 설명하기를 작성해 주세요.');
        r.status = 'submitted'; r.submittedAt = at; r.updatedAt = at; r.revision++;
        put('learning_runs', r, u.tenantId); audit('learning.submit', r.id); return view(r, a, u);
      }
      if (match[2] === 'review' && method === 'POST') {
        teacher(); if (r.status === 'in_progress') fail(409, '학생 제출 후 검토해 주세요.');
        if (body.revision !== r.revision) fail(409, '다른 화면에서 검토가 바뀌었습니다. 최신 기록을 확인해 주세요.');
        const qs = questions(a.lesson, a.level);
        for (const [id, review] of Object.entries(body.reviews || {})) {
          if (!review || typeof review !== 'object' || !qs.some(q => q.id === id) || !['success', 'needs_support'].includes(review.outcome) || !clean(review.note, 2000)) fail(400, '문항별 판단과 지도 의견을 작성해 주세요.');
          r.reviews[id] = { outcome: review.outcome, note: review.note.trim(), at, teacherName: u.name };
        }
        r.note = clean(body.note, 2000); r.updatedAt = at; r.revision++;
        if (body.publish) {
          if (qs.some(q => !r.reviews[q.id]) || !r.note) fail(400, '모든 활동 검토와 종합 의견을 마친 뒤 공개해 주세요.');
          r.publishedAt = at; r.status = 'reviewed';
          put('learning_releases', { id: r.id, assignmentId: a.id, studentId: r.studentId, publishedAt: at, snapshot: view(r, a) }, u.tenantId);
        }
        put('learning_runs', r, u.tenantId); audit('learning.review', r.id); return view(r, a, u);
      }
      if (match[2] === 'revoke' && method === 'POST') {
        teacher(); db.prepare('DELETE FROM learning_releases WHERE id=? AND tenant_id=?').run(u.tenantId+':'+r.id, u.tenantId);
        delete r.publishedAt; put('learning_runs', r, u.tenantId); audit('learning.revoke', r.id); return { ok: true };
      }
    }
    fail(404, '학습 요청을 찾을 수 없습니다.');
  };
  const calibration = createCalibrationApplication({db,lessons});
  const placement = createPlacementService({ db, lessons, delegate: route, calibration });
  const course = createCourseService({ db, lessons, delegate: route, randomUUID, calibration });
  const pilot = createPilotService({ db, lessons, randomUUID });
  return { route, upgrade };
}
