import { upgradePrivacy, refreshPrivacy, currentPolicy } from './privacy.mjs';
import {restrictionIds} from './processing-restrictions.mjs';
const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
const text = (v, max = 100) => typeof v === 'string' && v.trim().length <= max ? v.trim() : '';
export const activeAccount = (u, at) => !!u && u.active !== false && !(u.role === 'student' && (u.studentStatus && u.studentStatus !== 'enrolled' || u.validUntil && u.validUntil <= at || u.consentStatus && !['granted','synthetic'].includes(u.consentStatus)));
export const canTeachClass = (u, classId) => u?.role === 'teacher' && (u.isOwner || u.classIds?.includes(classId));
export const classForStudents = (s, u, ids, requested, at) => {
  const students = ids.map(id => s.users.find(v => v.id === id && v.tenantId === u.tenantId && v.role === 'student'));
  const classId = requested || students[0]?.classId;
  if (!ids.length || students.some(v => !v || !activeAccount(v, at) || restrictionIds(s,at).has(v.id)||v.classId !== classId) || !canTeachClass(u, classId) || !s.classes.some(c => c.id === classId && c.tenantId === u.tenantId && c.active)) fail(400, '현재 담당하는 같은 반의 이용 가능한 재원 학생을 선택해 주세요.');
  return classId;
};

export function upgradeOrganization(s, uuid, at, privacyMode = 'enforced') {
  s.organizations ||= []; s.classes ||= []; s.enrollments ||= []; s.recoveryCodes ||= []; s.attendance ||= []; s.consultations ||= [];
  for (const tenantId of [...new Set(s.users.map(u => u.tenantId))]) {
    if (!s.organizations.some(o => o.id === tenantId)) s.organizations.push({ id: tenantId, name: '우리 학원', revision: 0, createdAt: at });
    const people = s.users.filter(u => u.tenantId === tenantId);
    if (!people.some(u => u.isOwner !== undefined)) { const first = people.find(u => u.role === 'teacher'); if (first) first.isOwner = true; }
    for (const u of people) {
      if (u.active === undefined) u.active = true;
      u.revision ||= 0;
      if (u.role === 'parent') continue;
      if (!u.classId && !u.classIds) {
        const name = u.className || '우리 반';
        let c = s.classes.find(c => c.tenantId === tenantId && c.name === name);
        if (!c) { c = { id: uuid(), tenantId, name, active: true, revision: 0, createdAt: at }; s.classes.push(c); }
        if (u.role === 'teacher') u.classIds = [c.id];
        else { u.classId = c.id; u.studentStatus = 'enrolled'; s.enrollments.push({ id: uuid(), tenantId, studentId: u.id, classId: c.id, startedAt: at, migrated: true }); }
      }
    }
  }
  for (const a of s.assignments) {
    a.classId ||= s.users.find(u => u.id === a.createdBy)?.classIds?.[0] || s.users.find(u => u.id === a.studentIds[0])?.classId;
  }
  for (const a of s.attempts) a.classId ||= s.assignments.find(v => v.id === a.assignmentId)?.classId;
  upgradePrivacy(s, uuid, at, privacyMode);
}

export function organizationRoute({ s, u, path, method, body, at, uuid, makeUser, safeUser, passwordHash, passwordOK, issueSession, hash, token, res }) {
  const owner = () => { if (!u?.isOwner || u.role !== 'teacher') fail(403, '학원 운영 권한이 필요합니다.'); };
  const teacher = () => { if (u.role !== 'teacher') fail(403, '교사 권한이 필요합니다.'); };
  const audit = (action, id, reason) => s.audit.push({ at, actor: u.id, action, id, reason });
  const revokeSessions = id => { for (const [key, session] of Object.entries(s.sessions)) if (session.userId === id) delete s.sessions[key]; };
  const member = id => s.users.find(v => v.id === id && v.tenantId === u.tenantId);
  const scopedStudent = id => { const v = member(id); if (!v || v.role !== 'student' || !canTeachClass(u, v.classId)) fail(404, '담당 학생을 찾을 수 없습니다.'); return v; };
  if (path === '/account/password' && method === 'POST') {
    if (typeof body.currentPassword !== 'string' || body.currentPassword.length > 128 || !passwordOK(body.currentPassword, u.password)) fail(400, '현재 비밀번호를 확인해 주세요.');
    if (typeof body.newPassword !== 'string' || body.newPassword.length < 10 || body.newPassword.length > 128) fail(400, '새 비밀번호는 10~128자여야 합니다.');
    u.password = passwordHash(body.newPassword); delete u.deviceDraftKey;delete u.pendingMfa; u.mustChangePassword = false; u.revision++; s.recoveryCodes = s.recoveryCodes.filter(r => r.userId !== u.id);
    revokeSessions(u.id); issueSession(s, u, res, at); audit('account.password', u.id); return { ok: true };
  }
  if (path === '/org/dashboard' && method === 'GET') {
    teacher();
    const classes = s.classes.filter(c => c.tenantId === u.tenantId && canTeachClass(u, c.id));
    const people = s.users.filter(v => v.tenantId === u.tenantId && (u.isOwner || v.id === u.id || v.role === 'student' && canTeachClass(u, v.classId) || v.role === 'parent' && [...v.childIds,...s.privacy.candidates.filter(c=>c.tenantId===u.tenantId&&c.parentId===v.id).map(c=>c.studentId)].some(id => s.users.some(st => st.id === id && canTeachClass(u, st.classId)))));
    const ids = new Set(people.filter(v => v.role === 'student').map(v => v.id));
    return { organization: s.organizations.find(o => o.id === u.tenantId), user: safeUser(u), classes, users: people.map(v => ({ ...safeUser(v), childIds: v.childIds.filter(id => u.isOwner || ids.has(id)) })),
      attendance: s.attendance.filter(r => r.tenantId === u.tenantId && canTeachClass(u, r.classId)), consultations: s.consultations.filter(r => r.tenantId === u.tenantId && canTeachClass(u, r.classId)),
      audit: u.isOwner ? s.audit.filter(a => a.tenantId ? a.tenantId===u.tenantId : s.users.some(v => v.id === a.actor && v.tenantId === u.tenantId)).slice(-100) : [] };
  }
  if (path === '/org/settings' && method === 'POST') {
    owner(); const o = s.organizations.find(o => o.id === u.tenantId);
    if (!text(body.name, 80) || body.revision !== o.revision) fail(409, '학원 이름과 최신 설정을 확인해 주세요.');
    o.name = body.name.trim(); o.revision++; audit('org.settings', o.id); return { organization: o };
  }
  if (path === '/org/classes' && method === 'POST') {
    owner(); if (!text(body.name, 60)) fail(400, '반 이름을 입력해 주세요.');
    if (s.classes.some(c => c.tenantId === u.tenantId && c.active && c.name === body.name.trim())) fail(409, '같은 이름의 운영 중인 반이 있습니다.');
    const c = { id: uuid(), tenantId: u.tenantId, name: body.name.trim(), active: true, revision: 0, createdAt: at }; s.classes.push(c); audit('class.create', c.id); return { class: c };
  }
  const classMatch = /^\/org\/classes\/([^/]+)$/.exec(path);
  if (classMatch && method === 'POST') {
    owner(); const c = s.classes.find(c => c.id === classMatch[1] && c.tenantId === u.tenantId);
    if (!c) fail(404, '반을 찾을 수 없습니다.');
    if (body.revision !== c.revision || !text(body.name, 60) || typeof body.active !== 'boolean') fail(409, '최신 반 정보와 이름을 확인해 주세요.');
    if (!body.active && s.users.some(v => v.classId === c.id && v.role === 'student' && v.active && v.studentStatus === 'enrolled')) fail(409, '재원 학생을 먼저 다른 반으로 이동하거나 재원 상태를 변경해 주세요.');
    if (s.classes.some(v => v.id !== c.id && v.tenantId === u.tenantId && v.active && v.name === body.name.trim())) fail(409, '같은 이름의 반이 있습니다.');
    c.name = body.name.trim(); c.active = body.active; c.revision++;
    for (const v of s.users.filter(v => v.tenantId === u.tenantId && v.classId === c.id)) v.className = c.name;
    audit('class.update', c.id); return { class: c };
  }
  if (path === '/org/teachers' && method === 'POST') {
    owner(); const ids = [...new Set(Array.isArray(body.classIds) ? body.classIds : [])];
    if (ids.some(id => !s.classes.some(c => c.id === id && c.tenantId === u.tenantId && c.active))) fail(400, '학원에 속한 운영 중인 반을 선택해 주세요.');
    const v = makeUser(s, body, 'teacher', u.tenantId, ''); v.classIds = ids; v.isOwner = !!body.isOwner; v.active = true; v.revision = 0;v.mustChangePassword=s.organizations.find(o=>o.id===u.tenantId).privacyMode!=='synthetic';
    audit('teacher.create', v.id); return { user: safeUser(v) };
  }
  if (path === '/org/parents' && method === 'POST') {
    owner();
    if (s.organizations.find(o=>o.id===u.tenantId).privacyMode !== 'synthetic' && (!currentPolicy(s,u.tenantId) || !text(body.registrationReference,300))) fail(409,'게시된 안내문과 보호자 계정 등록 근거의 문서 참조가 필요합니다.');
    const v = makeUser(s, body, 'parent', u.tenantId, '', []);
    v.mustChangePassword = true; v.registrationReference=text(body.registrationReference,300); v.registrationAt=at;
    audit('parent.create',v.id); return {user:safeUser(v)};
  }
  const accountMatch = /^\/org\/accounts\/([^/]+)(?:\/(reset))?$/.exec(path);
  if (accountMatch && method === 'POST') {
    owner(); const v = member(accountMatch[1]); if (!v) fail(404, '학원 계정을 찾을 수 없습니다.');
    if (!text(body.reason, 1000)) fail(400, '변경 사유를 입력해 주세요.');
    if (accountMatch[2] === 'reset') {
      if(v.restoreCredentialHold&&(body.restoreReviewed!==true||typeof body.restoreReference!=='string'||!/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(body.restoreReference)))fail(400,'복원 계정의 본인·재직·담당 범위와 보호자 관계를 실제 확인한 문서가 필요합니다.');
      const code = token(); s.recoveryCodes = s.recoveryCodes.filter(r => r.userId !== v.id);
      s.recoveryCodes.push({ userId: v.id, hash: hash(code), expiresAt: at + 15 * 60000, issuedBy: u.id,...(v.restoreCredentialHold?{restoreVerified:true,restoreReference:body.restoreReference}:{}) });
      audit('account.recovery.issue', v.id, body.reason.trim()); return { code, expiresAt: at + 15 * 60000, username: v.username };
    }
    if (body.revision !== v.revision) fail(409, '최신 계정 정보를 다시 확인해 주세요.');
    if (typeof body.active !== 'boolean' || !text(body.name, 40)) fail(400, '이름과 계정 활성 상태를 확인해 주세요.');
    const ownerAfter = v.role === 'teacher' && (body.isOwner ?? v.isOwner);
    if (v.isOwner && (!ownerAfter || !body.active) && !s.users.some(other => other.id !== v.id && other.tenantId === u.tenantId && other.isOwner && other.active)) fail(409, '마지막 운영자 계정은 비활성화하거나 권한을 해제할 수 없습니다.');
    if (v.role === 'student') {
      if (!['enrolled', 'leave', 'withdrawn'].includes(body.studentStatus)) fail(400, '재원 상태를 선택해 주세요.');
      const c = s.classes.find(c => c.id === body.classId && c.tenantId === u.tenantId && c.active);
      if (!c) fail(400, '운영 중인 반을 선택해 주세요.');
      if (body.validUntil != null && (!Number.isFinite(body.validUntil) || body.validUntil <= at)) fail(400, '이용 종료 시각을 확인해 주세요.');
      if (v.classId !== c.id) {
        for (const e of s.enrollments.filter(e => e.studentId === v.id && !e.endedAt)) e.endedAt = at;
        s.enrollments.push({ id: uuid(), tenantId: u.tenantId, studentId: v.id, classId: c.id, startedAt: at, actor: u.id, reason: body.reason.trim() });
      }
      v.classId = c.id; v.className = c.name; v.studentStatus = body.studentStatus; v.validUntil = body.validUntil || null;
    }
    if (v.role === 'teacher') {
      if (!Array.isArray(body.classIds) || body.classIds.some(id => !s.classes.some(c => c.id === id && c.tenantId === u.tenantId && c.active))) fail(400, '담당 반을 확인해 주세요.');
      v.classIds = [...new Set(body.classIds)]; v.isOwner = !!ownerAfter;
    }
    v.name = body.name.trim(); v.active = body.active; v.revision++; revokeSessions(v.id);
    if(!v.active||v.role==='student'&&v.studentStatus==='withdrawn'){delete v.deviceDraftKey;delete v.pendingMfa;}
    if (v.role === 'student' && v.studentStatus === 'withdrawn') for (const verification of s.privacy.verifications.filter(r=>r.tenantId===u.tenantId&&r.studentId===v.id&&!r.revokedAt)) { verification.revokedAt=at; verification.revokedBy=u.id; verification.revokeReason='퇴원 처리'; }
    refreshPrivacy(s,at);
    audit('account.update', v.id, body.reason.trim()); return { user: safeUser(v) };
  }
  if (path === '/org/guardian-links' && method === 'POST') {
    owner();
    if (s.organizations.find(o=>o.id===u.tenantId).privacyMode !== 'synthetic') fail(409,'보호자 확인·동의 메뉴에서 법정대리인 확인 또는 연결 해제를 진행해 주세요.');
    const parent = member(body.parentId), ids = [...new Set(Array.isArray(body.studentIds) ? body.studentIds : [])];
    if (!parent || parent.role !== 'parent' || body.revision !== parent.revision || !text(body.reason, 1000) || ids.some(id => member(id)?.role !== 'student')) fail(400, '보호자와 연결 자녀, 변경 사유를 확인해 주세요.');
    parent.childIds = ids; parent.revision++; revokeSessions(parent.id); audit('guardian.links', parent.id, body.reason.trim()); return { user: safeUser(parent) };
  }
  if (path === '/org/attendance' && method === 'POST') {
    teacher(); const v = scopedStudent(body.studentId);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(body.date || '') || !Number.isFinite(Date.parse(body.date)) || new Date(body.date).toISOString().slice(0, 10) !== body.date || !['present','absent','late','excused'].includes(body.status)) fail(400, '출석 일자와 상태를 확인해 주세요.');
    let r = s.attendance.find(r => r.tenantId === u.tenantId && r.studentId === v.id && r.date === body.date);
    if (r && !canTeachClass(u, r.classId)) fail(403, '당시 반의 출석 수정 권한이 없습니다.');
    if (body.revision !== (r?.revision || 0)) fail(409, '출석 기록이 변경되었습니다. 다시 확인해 주세요.');
    if (!r) { r = { id: uuid(), tenantId: u.tenantId, classId: v.classId, studentId: v.id, date: body.date, revision: 0 }; s.attendance.push(r); }
    r.status = body.status; r.note = text(body.note, 1000); r.updatedAt = at; r.revision++; audit('attendance.save', r.id); return { record: r };
  }
  if (path === '/org/consultations' && method === 'POST') {
    teacher(); let r = body.id && s.consultations.find(r => r.id === body.id && r.tenantId === u.tenantId);
    if (body.id && (!r || !canTeachClass(u, r.classId))) fail(404, '담당 상담 기록이 없습니다.');
    if (!text(body.note, 5000)) fail(400, '상담 메모를 작성해 주세요.');
    if (!r) { const v = scopedStudent(body.studentId); r = { id: uuid(), tenantId: u.tenantId, classId: v.classId, studentId: v.id, createdAt: at, revision: 0 }; s.consultations.push(r); }
    if (body.revision !== r.revision) fail(409, '상담 기록이 변경되었습니다. 다시 확인해 주세요.');
    r.note = body.note.trim(); r.updatedAt = at; r.revision++; audit('consultation.save', r.id); return { record: r };
  }
  fail(404, '운영 요청을 찾을 수 없습니다.');
}
