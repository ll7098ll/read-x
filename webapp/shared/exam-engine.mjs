import { upgradeOrganization, canTeachClass, classForStudents, activeAccount, organizationRoute } from './organization.mjs';
import { currentPolicy, publicPolicy, privacyRoute, refreshPrivacy } from './privacy.mjs';
import { exam, allItems, publicForm, transfers } from './g5-01.mjs';
import {restrictionIds} from './processing-restrictions.mjs';

const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
const safeUser = ({ id, name, username, role, tenantId, className, childIds, isOwner, classId, classIds, active, studentStatus, validUntil, revision, consentStatus, mustChangePassword, restoreCredentialHold, mfa }) => ({ id, name, username, role, tenantId, className, childIds, isOwner, classId, classIds, active, studentStatus, validUntil, revision, consentStatus, mustChangePassword, restoreCredentialHold:!!restoreCredentialHold, mfaEnabled:!!mfa?.secret });
const text = (value, max = 100) => typeof value === 'string' && value.trim().length <= max ? value.trim() : '';
export const newState = () => ({ schema: 1, users: [], sessions: {}, assignments: [], attempts: [], followups: [], audit: [] });
const pct = (n, d) => d ? Math.round(n / d * 1000) / 10 : null;

export function scoreAttempt(attempt, form) {
  const rows = allItems(form).map(q => ({ ...q, choice: attempt.answers[q.id] ?? null,
    outcome: attempt.answers[q.id] == null ? 'unanswered' : attempt.answers[q.id] === q.answer ? 'correct' : 'wrong' }));
  const correct = rows.filter(r => r.outcome === 'correct').length;
  const summarize = key => [...new Set(rows.map(r => r[key]))].map(label => {
    const items = rows.filter(r => r[key] === label); const n = items.filter(r => r.outcome === 'correct').length;
    return { label, correct: n, total: items.length, percent: pct(n, items.length) };
  });
  return { correct, total: rows.length, unanswered: rows.filter(r => r.outcome === 'unanswered').length, percent: pct(correct, rows.length),
    wrong: rows.filter(r => r.outcome === 'wrong').length, rows, domains: summarize('domain'), skills: summarize('skill'), goals: summarize('goal'),
    version: 1, elapsedSec: Math.max(0, Math.round((attempt.submittedAt - attempt.startedAt) / 1000)) };
}


export function createExamEngine({ demo = false, allowSetup = true, privacyMode = 'enforced', randomBytes, randomUUID, hash, passwordHash, passwordOK, secureCookie = false, extensionRoute, security } = {}) {
  const authUser=(s,u,session,at)=>{const view={...safeUser(u),processingRestricted:restrictionIds(s,at).has(u.id)};return u.restoreCredentialHold||security&&security.status(s,u,session,at).stage!=='full'?{...view,childIds:[],className:'',classId:undefined,classIds:undefined}:view;};
  const releaseDemo = (s, a, at) => {
    if (!demo) return;
    const assignment = s.assignments.find(v => v.id === a.assignmentId);
    assignment.studentPublishedAt ||= at; assignment.closedAt ||= at;
    a.parentPublishedAt ||= at;
  };
  const expire = (s, at) => {
    security?.expire(s,at);
    const blocked=restrictionIds(s,at);
    for (const a of s.attempts) if (!blocked.has(a.studentId)&&a.status === 'in_progress' && a.deadlineAt <= at) {
      a.status = 'auto_submitted'; a.submittedAt = a.deadlineAt;
      releaseDemo(s, a, a.deadlineAt);
    }
    for (const [id, session] of Object.entries(s.sessions)) if (session.expiresAt <= at) delete s.sessions[id];
  };
  const loginFailures = new Map();
  const makeUser = (s, values, role, tenantId, className, childIds = []) => {
    const name = text(values.name, 40), username = text(values.username, 40).toLowerCase(), password = values.password;
    if (!name || !/^[a-z0-9._-]{3,40}$/.test(username) || typeof password !== 'string' || password.length < 10 || password.length > 128) fail(400, '이름, 영문·숫자 아이디(3~40자), 비밀번호(10~128자)를 확인해 주세요.');
    if (s.users.some(u => u.username === username)) fail(409, '이미 사용 중인 아이디입니다.');
    const user = { id: randomUUID(), name, username, password: passwordHash(password), role, tenantId, className, childIds, active: true, revision: 0 };
    s.users.push(user); return user;
  };
  const issueSession = (s, user, res, at, proof) => {
    const options=security?.options(s,user,at,proof)||{expiresAt:at+12*3600000};
    // An incomplete second factor cannot terminate a previously verified session.
    // Once login is complete, retain the single-device editing policy.
    for (const [id, session] of Object.entries(s.sessions)) if (session.userId === user.id&&(!options.mfaPending||session.mfaPending&&!Number.isFinite(session.recoveryVerifiedAt))) delete s.sessions[id];
    const token = randomBytes(32).toString('hex'),issued={userId:user.id,...options};s.sessions[hash(token)] = issued;
    res.setHeader('Set-Cookie', `readx_exam=${token}; Path=/api/exam; HttpOnly; SameSite=Strict; Max-Age=${Math.floor((options.expiresAt-at)/1000)}${secureCookie ? '; Secure' : ''}`);
    return issued;
  };
  const canRead = (u, a) => u.tenantId === a.tenantId && (u.role === 'teacher' && (demo || canTeachClass(u, a.classId)) || u.role === 'student' && u.id === a.studentId || u.role === 'parent' && u.childIds.includes(a.studentId) && a.parentPublishedAt);
  const assignmentView = (a, viewer) => ({ id: a.id, title: a.title, formId: a.form.id, formVersion: a.form.version, count: allItems(a.form).length,
    durationSec: a.form.durationSec, opensAt: a.opensAt, closesAt: a.closesAt, studentIds: !viewer || viewer.role === 'teacher' ? a.studentIds : a.studentIds.filter(id => viewer.role === 'student' ? id === viewer.id : viewer.childIds.includes(id)), studentPublishedAt: a.studentPublishedAt, closedAt: a.closedAt });
  const attemptView = a => ({ id: a.id, assignmentId: a.assignmentId, studentId: a.studentId, status: a.status, startedAt: a.startedAt,
    deadlineAt: a.deadlineAt, submittedAt: a.submittedAt, answered: Object.values(a.answers).filter(v => v !== null).length,
    lastSavedAt: a.lastSavedAt, parentPublishedAt: a.parentPublishedAt });
  const followupView = (f, u) => {
    const t = transfers.find(t => t.id === f.transferId);
    return { id: f.id, attemptId: f.attemptId, studentId: f.studentId, questionId: f.questionId, goal: f.goal, assignedAt: f.assignedAt,
      reviewedAt: f.reviewedAt, completedAt: f.completedAt, reflection: f.reflection, result: f.completedAt ? { choice: f.choice, evidence: f.evidence, correct: f.correct, answer: t.answer, explanation: t.explanation, expectedEvidence: t.evidence } : null,
      transfer: f.reviewedAt || u.role === 'teacher' ? { id: t.id, title: t.title, text: t.text, prompt: t.prompt, options: t.options } : undefined, fresh: f.fresh, teacherReview: f.teacherReview };
  };
  const demoAssignment = (s, tenantId, at) => {
    const people = s.users.filter(u => u.tenantId === tenantId);
    const a = { id: randomUUID(), tenantId, createdBy: people.find(u => u.role === 'teacher').id,
      title: '초5 1회차 · 모의고사 체험', form: structuredClone(exam),
      studentIds: [people.find(u => u.role === 'student').id], opensAt: at - 60000, closesAt: at + 90 * 86400000, createdAt: at };
    s.assignments.push(a); return a;
  };
  const demoUser = (s, req, res, path, method, at) => {
    const role = req.headers['x-readx-demo-role'] || 'student';
    if (!['student', 'teacher', 'parent'].includes(role)) fail(400, '체험할 화면을 선택해 주세요.');
    const token = /(?:^|;\s*)readx_exam_demo=([a-f0-9]{64})(?:;|$)/.exec(req.headers.cookie || '')?.[1];
    let guest = token && s.sessions[hash(token)];
    if (!guest) {
      if (path !== '/session' || method !== 'GET') fail(401, '체험 연결이 만료되었습니다. 화면을 새로고침해 주세요.');
      const tenantId = randomUUID(), studentId = randomUUID();
      for (const [r, name] of [['student', '체험 학생'], ['teacher', '체험 선생님'], ['parent', '체험 보호자']]) {
        s.users.push({ id: r === 'student' ? studentId : randomUUID(), role: r, name, username: '', tenantId, className: '리드엑스 체험반', childIds: r === 'parent' ? [studentId] : [] });
      }
      const next = randomBytes(32).toString('hex'); guest = { tenantId, expiresAt: at + 30 * 86400000 };
      s.sessions[hash(next)] = guest;
      res.setHeader('Set-Cookie', `readx_exam_demo=${next}; Path=/api/exam-demo; HttpOnly; SameSite=Strict; Max-Age=2592000${secureCookie ? '; Secure' : ''}`);
      demoAssignment(s, tenantId, at);
    }
    return s.users.find(u => u.tenantId === guest.tenantId && u.role === role);
  };
  const route = (s, req, res, body, at) => {
    const path = new URL(req.url, 'http://localhost').pathname.replace(demo ? /^\/api\/exam-demo/ : /^\/api\/exam/, '') || '/';
    const method = req.method;
    if (!demo) upgradeOrganization(s, randomUUID, at, privacyMode);
    const token = /(?:^|;\s*)readx_exam=([a-f0-9]{64})(?:;|$)/.exec(req.headers.cookie || '')?.[1];
    const session = token && s.sessions[hash(token)];
    const u = demo ? demoUser(s, req, res, path, method, at) : session && s.users.find(u => u.id === session.userId && activeAccount(u, at));
    const teacher = () => { if (!u || u.role !== 'teacher') fail(403, '교사 권한이 필요합니다.'); };
    if (path === '/session' && method === 'GET') return { user: u ? authUser(s,u,session,at) : null, setupRequired: !demo && allowSetup && !s.users.length, demo, serverNow: at, ...(u&&security?{auth:security.status(s,u,session,at)}:{}) };
    if (!demo && path === '/privacy/notice' && method === 'GET') return { policies: s.organizations.map(o=>publicPolicy(currentPolicy(s,o.id))).filter(Boolean) };
    if (demo && ['/setup', '/login', '/logout', '/roster'].includes(path)) fail(404, '계정 없이 이용하는 체험 화면입니다.');
    if (demo && path === '/demo/new' && method === 'POST') {
      if (u.role !== 'student') fail(403, '학생 화면에서 새 응시를 시작해 주세요.');
      const available = s.assignments.find(a => a.tenantId === u.tenantId && !a.closedAt && a.opensAt <= at && a.closesAt > at);
      return { assignment: assignmentView(available || demoAssignment(s, u.tenantId, at)) };
    }
    if (path === '/setup' && method === 'POST') {
      if (!allowSetup || s.users.length) fail(409, '초기 설정이 이미 완료되었거나 허용되지 않습니다.');
      if (!['127.0.0.1', '::1', '::ffff:127.0.0.1'].includes(req.socket.remoteAddress)) fail(403, '초기 교사 계정은 서버 컴퓨터에서 만들어 주세요.');
      let setupHost;try{setupHost=new URL('http://'+(req.headers.host||'')).hostname;}catch{fail(403,'초기 설정 주소를 확인해 주세요.');}
      if(!['localhost','127.0.0.1','[::1]'].includes(setupHost))fail(403,'초기 설정은 서버 컴퓨터의 localhost 주소에서 진행해 주세요.');
      const user = makeUser(s, body, 'teacher', randomUUID(), text(body.className, 60) || '초5 우리 반');
      user.isOwner = true; upgradeOrganization(s, randomUUID, at, privacyMode);
      const issued=issueSession(s, user, res, at); return { user: authUser(s,user,issued,at),...(security?{auth:security.status(s,user,issued,at)}:{}) };
    }
    if (path === '/login' && method === 'POST') {
      const username = text(body.username, 40).toLowerCase();
      const key = `${req.socket.remoteAddress}:${username}`;
      const failures = (loginFailures.get(key) || []).filter(t => at - t < 15 * 60000);
      if (failures.length >= 8) fail(429, '로그인 시도가 많습니다. 15분 뒤 다시 시도해 주세요.');
      const user = s.users.find(u => u.username === username);
      if (typeof body.password !== 'string' || body.password.length > 128 || !user || !activeAccount(user, at) || !passwordOK(body.password, user.password)) {
        loginFailures.set(key, [...failures, at]); fail(401, '아이디 또는 비밀번호를 확인해 주세요.');
      }
      loginFailures.delete(key);const issued=issueSession(s, user, res, at); return { user: authUser(s,user,issued,at),...(security?{auth:security.status(s,user,issued,at)}:{}) };
    }
    if (!demo && path === '/recover' && method === 'POST') {
      const username = text(body.username, 40).toLowerCase(), key = 'recover:' + req.socket.remoteAddress + ':' + username;
      const failures = (loginFailures.get(key) || []).filter(t => at-t < 15*60000);
      if (failures.length >= 8) fail(429, '복구 시도가 많습니다. 15분 뒤 다시 시도해 주세요.');
      const account = s.users.find(v => v.username === username);
      const recovery = account && s.recoveryCodes.find(r => r.userId === account.id && r.expiresAt > at);
      if (!recovery || typeof body.code !== 'string' || body.code.length > 128 || recovery.hash !== hash(body.code.trim())) { loginFailures.set(key,[...failures,at]); fail(400,'복구 코드와 아이디를 확인해 주세요.'); }
      if (typeof body.newPassword !== 'string' || body.newPassword.length < 10 || body.newPassword.length > 128) fail(400,'새 비밀번호는 10~128자여야 합니다.');
      if(account.restoreCredentialHold&&recovery.restoreVerified!==true)fail(400,'복원 후 본인·현재 권한을 확인한 새 복구 코드가 필요합니다.');
      if(account.restoreCredentialHold&&passwordOK(body.newPassword,account.password))fail(400,'복원 전 비밀번호와 다른 새 비밀번호를 선택해 주세요.');
      const restored=!!account.restoreCredentialHold;delete account.restoreCredentialHold;if(restored)account.mustChangePassword=false;account.password = passwordHash(body.newPassword); account.revision++;
      delete account.deviceDraftKey;delete account.pendingMfa;
      if (!restored && account.role === 'parent' && s.organizations.find(o=>o.id===account.tenantId).privacyMode !== 'synthetic') account.mustChangePassword = true;
      s.recoveryCodes = s.recoveryCodes.filter(r => r.userId !== account.id);
      s.mfaRecoveries=(s.mfaRecoveries||[]).filter(r=>r.userId!==account.id);
      for (const [id, session] of Object.entries(s.sessions)) if (session.userId === account.id) delete s.sessions[id];
      s.audit.push({at, actor: account.id, action:'account.recovered'}); loginFailures.delete(key); return {ok:true};
    }
    if (!demo && path === '/logout' && method === 'POST') {
      if(body.expectedUserId && u && body.expectedUserId!==u.id)return {ok:true,alreadyChanged:true};
      if(token)delete s.sessions[hash(token)];
      res.setHeader('Set-Cookie',`readx_exam=; Path=/api/exam; HttpOnly; SameSite=Strict; Max-Age=0${secureCookie?'; Secure':''}`);return {ok:true};
    }
    if (!u) fail(401, '로그인이 필요합니다. 다른 기기에 로그인했다면 다시 로그인해 주세요.');
    if(u.restoreCredentialHold&&!path.startsWith('/auth/mfa/'))throw Object.assign(Error('백업 복원 후 본인·현재 권한 확인과 새 복구 코드로 비밀번호 재설정이 필요합니다.'),{status:403,code:'RESTORE_CREDENTIALS_REQUIRED'});
    if(security&&path.startsWith('/auth/mfa/'))return security.route({s,u,session,sessionKey:hash(token),path,method,body,at,res,issueSession,passwordOK});
    if(security&&path==='/account/password'&&method==='POST'&&u.mustChangePassword&&security.status(s,u,session,at).stage==='enroll')return security.changePassword({s,u,body,at,res,issueSession,passwordOK,passwordHash});
    if(security){const denied=security.guard(s,u,session,at);if(denied)return denied;}
    if(security&&path==='/account/password'&&method==='POST')return security.changePassword({s,u,body,at,res,issueSession,passwordOK,passwordHash});
    if(security&&method==='POST'&&security.needsStepUp(s,u,path,body)){const denied=security.stepUp({s,u,body,at,passwordOK});if(denied)return denied;}
    if (!demo && path === '/account/device-key' && method === 'POST') {
      if (!u.deviceDraftKey) { u.deviceDraftKey={id:randomUUID(),key:randomBytes(32).toString('base64'),createdAt:at};s.audit.push({at,actor:u.id,action:'device.key.create'}); }
      return {userId:u.id,keyId:u.deviceDraftKey.id,key:u.deviceDraftKey.key};
    }
    if (!demo && path.startsWith('/privacy/')) return privacyRoute({s,u,path,method,body,at,uuid:randomUUID,hash});
    if (!demo && (path.startsWith('/org/') || path === '/account/password')) return organizationRoute({s,u,path,method,body,at,uuid:randomUUID,makeUser,safeUser,passwordHash,passwordOK,issueSession:(...args)=>issueSession(...args,{verified:security?.isVerified(s,u,session,at)}),hash,token:()=>randomBytes(32).toString('hex'),res});
    if (extensionRoute && (path.startsWith('/learning/') || path.startsWith('/overview')||path.startsWith('/audit/')||path.startsWith('/rights/'))) return extensionRoute({ user: u, state: s, path, method, body, at });
    if (path === '/dashboard' && method === 'GET') {
      const assignments = s.assignments.filter(a => a.tenantId === u.tenantId && (u.role === 'teacher' ? (demo || canTeachClass(u,a.classId)) : a.studentIds.some(id => u.role === 'student' ? id === u.id : u.childIds.includes(id))));
      const attempts = s.attempts.filter(a => canRead(u, a));
      const historicalIds=new Set(assignments.flatMap(a=>a.studentIds));
      const users = s.users.filter(v => v.tenantId === u.tenantId && (u.role === 'teacher' && (demo || u.isOwner || v.id === u.id || v.role === 'student' && (canTeachClass(u,v.classId)||historicalIds.has(v.id)) || v.role === 'parent' && v.childIds.some(id=>s.users.some(st=>st.id===id&&canTeachClass(u,st.classId)))) || v.id === u.id || u.role === 'parent' && u.childIds.includes(v.id)));
      return { user: safeUser(u), serverNow: at, classes: demo ? [] : s.classes.filter(c=>c.tenantId===u.tenantId&&u.role==='teacher'&&canTeachClass(u,c.id)), users: users.map(v=>({...safeUser(v),...(!demo && u.role==='teacher' && !u.isOwner && v.role==='student' && !canTeachClass(u,v.classId)?{username:'',classId:undefined,className:'이전 반',active:false,studentStatus:'transferred',validUntil:undefined}:{}),childIds:v.childIds.filter(id=>u.role!=='teacher'||u.isOwner||users.some(st=>st.id===id&&st.role==='student'))})), assignments: assignments.map(a => assignmentView(a, u)), attempts: attempts.map(attemptView),
        followups: s.followups.filter(f => attempts.some(a => a.id === f.attemptId)).map(f => followupView(f, u)),
        form: { id: exam.id, title: exam.title, count: 24, durationSec: exam.durationSec, editorialNotice: exam.editorialNotice } };
    }
    if (path === '/roster' && method === 'POST') {
      teacher();
      const classId = body.classId || u.classIds?.[0];
      const classroom = s.classes?.find(c=>c.id===classId&&c.tenantId===u.tenantId&&c.active);
      if (!demo && (!classroom || !canTeachClass(u,classId))) fail(403,'담당하는 운영 중인 반을 선택해 주세요.');
      const enforced = !demo && s.organizations.find(o=>o.id===u.tenantId).privacyMode !== 'synthetic';
      if (enforced && (!currentPolicy(s,u.tenantId) || !text(body.registrationReference,300))) fail(409,'운영자가 개인정보 안내문과 사전 등록 근거를 검토·게시한 뒤, 학생 등록 근거의 문서 참조를 입력해 주세요.');
      const student = makeUser(s, body.student || {}, 'student', u.tenantId, classroom?.name || u.className);
      student.classId=classId; student.studentStatus='enrolled';
      if (!demo) s.enrollments.push({id:randomUUID(),tenantId:u.tenantId,studentId:student.id,classId,startedAt:at,actor:u.id});
      const parent = body.parent ? makeUser(s, body.parent, 'parent', u.tenantId, classroom?.name || u.className, enforced ? [] : [student.id]) : null;
      if (enforced) {
        student.registrationReference = body.registrationReference.trim(); student.registrationAt = at;
        if (parent) { parent.mustChangePassword = true; s.privacy.candidates.push({id:randomUUID(),tenantId:u.tenantId,studentId:student.id,parentId:parent.id,at,actor:u.id}); }
        refreshPrivacy(s,at);
      }
      s.audit.push({ at, actor: u.id, action: 'roster.create', studentId: student.id });
      return { student: safeUser(student), parent: parent ? safeUser(parent) : null };
    }
    if (path === '/form' && method === 'GET') { teacher(); return { form: exam }; }
    if (path === '/assignments' && method === 'POST') {
      teacher();
      const ids = [...new Set(Array.isArray(body.studentIds) ? body.studentIds : [])];
      const opensAt = Number(body.opensAt), closesAt = Number(body.closesAt);
      const classId = demo ? undefined : classForStudents(s,u,ids,body.classId,at);
      if (!ids.length || ids.some(id => !s.users.some(v => v.id === id && v.tenantId === u.tenantId && v.role === 'student'))) fail(400, '담당 반의 학생을 선택해 주세요.');
      if (!Number.isFinite(opensAt) || !Number.isFinite(closesAt) || closesAt <= Math.max(opensAt, at) || closesAt - opensAt > 90 * 86400000) fail(400, '시작·마감 시각을 확인해 주세요. 응시 기간은 최대 90일입니다.');
      const a = { id: randomUUID(), tenantId: u.tenantId, classId, createdBy: u.id, title: text(body.title, 100) || exam.title, form: structuredClone(exam), studentIds: ids, opensAt, closesAt, createdAt: at };
      s.assignments.push(a); return { assignment: assignmentView(a) };
    }
    const am = /^\/assignments\/([^/]+)\/(start|release|statistics)$/.exec(path);
    if (am) {
      const a = s.assignments.find(a => a.id === am[1] && a.tenantId === u.tenantId);
      if (!a || (u.role === 'teacher' && !demo && !canTeachClass(u,a.classId))) fail(404, '배정된 시험을 찾을 수 없습니다.');
      if (am[2] === 'start' && method === 'POST') {
        if (u.role !== 'student' || !a.studentIds.includes(u.id)) fail(403, '배정받은 학생만 응시할 수 있습니다.');
        const old = s.attempts.find(v => v.assignmentId === a.id && v.studentId === u.id);
        if (old) return { attempt: attemptView(old) };
        if (at < a.opensAt || at >= a.closesAt || a.closedAt) fail(409, '현재 응시 가능한 시간이 아닙니다.');
        const attempt = { id: randomUUID(), assignmentId: a.id, classId:a.classId, tenantId: u.tenantId, studentId: u.id, startedAt: at, deadlineAt: Math.min(a.closesAt, at + a.form.durationSec * 1000), status: 'in_progress', answers: {}, firstAnswers: {}, itemSeq: {}, flags: [], lastSavedAt: at };
        s.attempts.push(attempt); return { attempt: attemptView(attempt) };
      }
      teacher();
      if (am[2] === 'release' && method === 'POST') {
        if (s.attempts.some(v => v.assignmentId === a.id && !restrictionIds(s,at).has(v.studentId)&&v.status === 'in_progress')) fail(409, '응시 중인 학생이 있습니다. 제출 또는 마감 후 공개해 주세요.');
        a.closedAt ||= at; a.studentPublishedAt ||= at;
        s.audit.push({ at, actor: u.id, action: 'assignment.release', assignmentId: a.id }); return { assignment: assignmentView(a) };
      }
      if (am[2] === 'statistics' && method === 'GET') {
        const attempts = s.attempts.filter(v => v.assignmentId === a.id && v.status !== 'in_progress');
        return { count: attempts.length, assignedCount: a.studentIds.length,
          rows: allItems(a.form).map(q => ({ id: q.id, number: q.number, prompt: q.prompt, goal: q.goal, answer: q.answer,
            correct: attempts.filter(v => v.answers[q.id] === q.answer).length,
            choices: q.options.map((label, i) => ({ label, count: attempts.filter(v => v.answers[q.id] === i).length, studentIds: attempts.filter(v => v.answers[q.id] === i).map(v => v.studentId) })),
            unanswered: attempts.filter(v => v.answers[q.id] == null).map(v => v.studentId) })) };
      }
    }
    const match = /^\/attempts\/([^/]+)(?:\/(answers|submit|review|followups|print))?$/.exec(path);
    if (match) {
      const a = s.attempts.find(a => a.id === match[1]);
      if (!a || !canRead(u, a)) fail(404, '조회할 수 있는 응시 기록이 없습니다.');
      const assignment = s.assignments.find(v => v.id === a.assignmentId);
      const own = () => { if (u.role !== 'student' || u.id !== a.studentId) fail(403, '응시한 학생만 답안을 제출할 수 있습니다.'); };
      if (!match[2] && method === 'GET'||match[2]==='print'&&method==='POST') {
        const released = u.role === 'teacher' || (assignment.studentPublishedAt && (u.role === 'student' || a.parentPublishedAt));
        const result = released && a.status !== 'in_progress' ? scoreAttempt(a, assignment.form) : null;
        return { attempt: { ...attemptView(a), ...(u.role === 'student' ? { answers: a.answers, itemSeq: a.itemSeq, flags: a.flags } : {}), note: u.role === 'parent' ? a.publishedNote : a.note },
          assignment: assignmentView(assignment, u), serverNow: at, studentName: s.users.find(v => v.id === a.studentId)?.name,
          form: u.role === 'student' || result ? publicForm(assignment.form) : null, report: result,
          followups: s.followups.filter(f => f.attemptId === a.id).map(f => followupView(f, u)) };
      }
      if (match[2] === 'answers' && method === 'POST') {
        own();
        if (a.status !== 'in_progress') fail(409, '제출되었거나 제한 시간이 끝난 시험입니다.');
        const changes = body.changes;
        if (!Array.isArray(changes) || changes.length > 100) fail(400, '답안 저장 요청을 확인해 주세요.');
        for (const c of changes) {
          if (!allItems(assignment.form).some(q => q.id === c.id) || !(c.choice === null || Number.isInteger(c.choice) && c.choice >= 0 && c.choice < 5) || !Number.isSafeInteger(c.seq) || c.seq < 1) fail(400, '문항·선택지·저장 순서가 올바르지 않습니다.');
          if (c.seq > (a.itemSeq[c.id] || 0)) {
            if (a.firstAnswers[c.id] === undefined && c.choice !== null) a.firstAnswers[c.id] = c.choice;
            a.answers[c.id] = c.choice; a.itemSeq[c.id] = c.seq;
          }
        }
        if (body.flags !== undefined) {
          if (!Array.isArray(body.flags) || body.flags.some(id => !allItems(assignment.form).some(q => q.id === id))) fail(400, '다시 보기 표시를 확인해 주세요.');
          a.flags = [...new Set(body.flags)];
        }
        a.lastSavedAt = at;
        return { answers: a.answers, itemSeq: a.itemSeq, flags: a.flags, savedAt: at };
      }
      if (match[2] === 'submit' && method === 'POST') {
        own(); if (a.status === 'in_progress') { a.status = 'submitted'; a.submittedAt = at; releaseDemo(s, a, at); }
        return { attempt: attemptView(a) };
      }
      if (match[2] === 'review' && method === 'POST') {
        teacher(); if (a.status === 'in_progress') fail(409, '제출 후 검토해 주세요.');
        a.note = text(body.note, 2000);
        if (body.publish) {
          if (!assignment.studentPublishedAt) fail(409, '회차의 학생 결과를 먼저 공개해 주세요.');
          if (!a.note) fail(400, '보호자에게 전달할 지도 의견을 입력해 주세요.');
          a.parentPublishedAt = at; a.publishedNote = a.note;
        }
        if (body.revoke) delete a.parentPublishedAt;
        s.audit.push({ at, actor: u.id, action: 'attempt.review', attemptId: a.id, publish: !!body.publish, revoke: !!body.revoke });
        return { ok: true };
      }
      if (match[2] === 'followups' && method === 'POST') {
        teacher();
        if (a.status === 'in_progress' || !assignment.studentPublishedAt) fail(409, '회차 결과 공개 후 보충학습을 배정해 주세요.');
        const q = allItems(assignment.form).find(q => q.id === body.questionId);
        if (!q) fail(400, '문항을 찾을 수 없습니다.');
        const old = s.followups.find(f => f.attemptId === a.id && f.questionId === q.id);
        if (old) return { followup: followupView(old, u) };
        const transfer = transfers.find(t => t.goal === q.goal);
        const f = { id: randomUUID(), attemptId: a.id, studentId: a.studentId, questionId: q.id, goal: q.goal, transferId: transfer.id, assignedAt: at };
        s.followups.push(f); return { followup: followupView(f, u) };
      }
    }
    const fm = /^\/followups\/([^/]+)\/(review|complete|feedback)$/.exec(path);
    if (fm && method === 'POST') {
      if (fm[2] === 'feedback') {
        teacher();
        const f = s.followups.find(f => f.id === fm[1]);
        const a = f && s.attempts.find(a => a.id === f.attemptId);
        if (!a || !canRead(u, a)) fail(404, '검토할 수행 기록이 없습니다.');
        if (!f.completedAt || !['supported', 'needs_review'].includes(body.outcome) || !text(body.comment, 1000)) fail(400, '완료된 새 글의 근거 판단과 지도 의견을 입력해 주세요.');
        f.teacherReview = { at, outcome: body.outcome, comment: text(body.comment, 1000), teacherName: u.name };
        s.audit.push({ at, actor: u.id, action: 'followup.feedback', followupId: f.id });
        return { followup: followupView(f, u) };
      }
      const f = s.followups.find(f => f.id === fm[1] && f.studentId === u.id);
      if (!f || u.role !== 'student') fail(404, '배정된 보충학습을 찾을 수 없습니다.');
      if (fm[2] === 'review') {
        const reflection = text(body.reflection, 1000);
        if (!reflection) fail(400, '근거를 보고 다시 알게 된 점을 적어 주세요.');
        if(f.completedAt && f.reflection!==reflection) fail(409,'제출한 보충학습 기록은 바꿀 수 없습니다. 선생님에게 문의해 주세요.');
        f.reflection = reflection; f.reviewedAt ||= at;
        // Mark exposure when the transfer is opened, not just when it is submitted.
        if (f.fresh === undefined) { f.fresh = !s.followups.some(v => v.id !== f.id && v.studentId === f.studentId && v.transferId === f.transferId && v.reviewedAt); }
      } else {
        if (!f.reviewedAt) fail(409, '원래 문항을 먼저 복습해 주세요.');
        const t = transfers.find(t => t.id === f.transferId);
        if (!Number.isInteger(body.choice) || body.choice < 0 || body.choice >= t.options.length || !text(body.evidence, 1000)) fail(400, '답과 본문 근거를 모두 입력해 주세요.');
        if(f.completedAt){ if(f.choice===body.choice&&f.evidence===text(body.evidence,1000))return {followup:followupView(f,u)}; fail(409,'제출한 답과 근거는 바꿀 수 없습니다. 선생님에게 문의해 주세요.'); }
        f.choice = body.choice; f.evidence = text(body.evidence, 1000); f.completedAt = at;
        f.correct = f.choice === t.answer;
        // Written evidence is preserved for teacher review, not automatically marked as mastery.
      }
      return { followup: followupView(f, u) };
    }
    fail(404, '요청한 기능을 찾을 수 없습니다.');
  };
  return { route, expire };
}
