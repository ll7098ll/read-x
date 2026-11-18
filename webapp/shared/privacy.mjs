// This records an operator's documented verification. It does not perform an
// identity check or certify that the operator's process satisfies the law.
const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
const text = (v, max = 2000) => typeof v === 'string' && v.trim() && v.trim().length <= max ? v.trim() : '';
const member = (s, tenantId, id, role) => s.users.find(u => u.tenantId === tenantId && u.id === id && (!role || u.role === role));
const liveAccount = (u, at) => !!u && u.active !== false && !(u.role === 'student' && (u.studentStatus && u.studentStatus !== 'enrolled' || u.validUntil && u.validUntil <= at));
export const currentPolicy = (s, tenantId) => s.privacy?.policies.filter(p => p.tenantId === tenantId).at(-1);
export const publicPolicy = p => p && Object.fromEntries(Object.entries(p).filter(([key]) => !['reviewReference','publishedBy','enrollmentBasisReference'].includes(key)));
const currentVerification = (s, tenantId, studentId, at) => s.privacy.verifications.find(v => v.tenantId === tenantId && v.studentId === studentId && !v.revokedAt && (!v.validUntil || v.validUntil > at) && liveAccount(member(s, tenantId, v.parentId, 'parent'), at));
const lastDecision = (s, tenantId, studentId) => s.privacy.consents.filter(c => c.tenantId === tenantId && c.studentId === studentId).at(-1);

export function refreshPrivacy(s, at) {
  for (const o of s.organizations) {
    const people = s.users.filter(u => u.tenantId === o.id);
    if (o.privacyMode === 'synthetic') {
      for (const u of people.filter(u => u.role === 'student')) u.consentStatus = 'synthetic';
      continue;
    }
    const policy = currentPolicy(s, o.id);
    for (const u of people.filter(u => u.role === 'parent')) u.childIds = [];
    for (const u of people.filter(u => u.role === 'student')) {
      const verification = currentVerification(s, o.id, u.id, at), decision = lastDecision(s, o.id, u.id);
      u.consentStatus = !verification ? 'verification_pending' : !policy ? 'policy_pending' : !decision ? 'consent_pending' : decision.action === 'withdraw' ? 'withdrawn' : decision.policyId !== policy.id || decision.policyHash !== policy.contentHash ? 'policy_changed' : decision.verificationId !== verification.id || decision.parentId !== verification.parentId ? 'consent_pending' : 'granted';
      if (u.consentStatus === 'granted' && liveAccount(u, at)) member(s, o.id, verification.parentId, 'parent').childIds.push(u.id);
    }
  }
}

export function upgradePrivacy(s, uuid, at, mode = 'enforced') {
  s.privacy ||= { policies: [], candidates: [], verifications: [], consents: [] };
  for (const o of s.organizations) {
    if (!o.privacyMode) {
      o.privacyMode = mode;
      // Legacy links are candidates only; never infer consent from an old link.
      if (mode !== 'synthetic') for (const p of s.users.filter(u => u.tenantId === o.id && u.role === 'parent')) {
        for (const studentId of p.childIds || []) s.privacy.candidates.push({ id: uuid(), tenantId: o.id, parentId: p.id, studentId, at, migrated: true });
      }
    }
  }
  refreshPrivacy(s, at);
}

export function privacyRoute({ s, u, path, method, body, at, uuid, hash }) {
  const audit = (action, id) => s.audit.push({ at, actor: u.id, action, id });
  const owner = () => { if (u.role !== 'teacher' || !u.isOwner) fail(403, '학원 운영 권한이 필요합니다.'); };
  const scope = id => { const child = member(s, u.tenantId, id, 'student'); return child && (u.isOwner || u.classIds?.includes(child.classId)); };
  const revokeStudentSessions = id => { for (const [key, session] of Object.entries(s.sessions)) if (session.userId === id) delete s.sessions[key]; const student=member(s,u.tenantId,id,'student');if(student)delete student.deviceDraftKey; };
  const finish = () => { refreshPrivacy(s, at); return { ok: true }; };
  const o = s.organizations.find(o => o.id === u.tenantId);
  if (path === '/privacy/dashboard' && method === 'GET') {
    const teacher = u.role === 'teacher';
    const candidates = s.privacy.candidates.filter(v => v.tenantId === u.tenantId && (teacher ? scope(v.studentId) : v.parentId === u.id));
    const verifications = s.privacy.verifications.filter(v => v.tenantId === u.tenantId && (teacher ? scope(v.studentId) : v.parentId === u.id));
    const consents = s.privacy.consents.filter(v => v.tenantId === u.tenantId && (teacher ? scope(v.studentId) : v.parentId === u.id));
    const allowedIds = new Set(teacher ? s.users.filter(v => v.tenantId === u.tenantId && scope(v.id)).map(v => v.id) : verifications.filter(v => !v.revokedAt && (!v.validUntil || v.validUntil > at)).map(v => v.studentId));
    const policy = currentPolicy(s, u.tenantId);
    return { mode: o.privacyMode, serverNow: at, mustChangePassword: !!u.mustChangePassword,
      policy: u.isOwner ? policy : publicPolicy(policy),
      policies: u.isOwner ? s.privacy.policies.filter(p => p.tenantId === u.tenantId) : [],
      students: s.users.filter(v => v.tenantId === u.tenantId && allowedIds.has(v.id) && v.role === 'student').map(v => ({ id: v.id, name: v.name, consentStatus: v.consentStatus, ...(teacher ? {registrationReference:v.registrationReference,registrationAt:v.registrationAt} : {}) })),
      candidates: teacher ? candidates : [],
      verifications: u.isOwner ? verifications : verifications.map(({ id, studentId, parentId, at, method, validUntil, revokedAt }) => ({ id, studentId, parentId, at, method, validUntil, revokedAt })),
      consents: consents.map(c => ({ ...c, policy: publicPolicy(s.privacy.policies.find(p => p.id === c.policyId && p.tenantId === u.tenantId)) })) };
  }
  if (o.privacyMode === 'synthetic') fail(409, '가상 자료 검증 모드에서는 실제 보호자 동의를 기록할 수 없습니다.');
  if (path === '/privacy/policies' && method === 'POST') {
    owner();
    if ((currentPolicy(s, u.tenantId)?.id || null) !== body.previousPolicyId) fail(409, '안내문이 변경되었습니다. 최신 버전을 확인해 주세요.');
    const fields = ['version','operatorLegalName','privacyContact','purpose','items','retention','refusal','childNotice','guardianNotice','reviewReference','enrollmentBasisReference'];
    const values = Object.fromEntries(fields.map(k => [k, text(body[k], ['version','operatorLegalName','privacyContact'].includes(k) ? 200 : 3000)]));
    if (Object.values(values).some(v => !v) || body.reviewed !== true) fail(400, '운영자·수집 목적과 항목·보유기간·거부 영향·아동 안내·보호자 확인 방법과 사전 등록 근거의 검토 참조를 모두 작성해 주세요.');
    if (s.privacy.policies.some(p => p.tenantId === u.tenantId && p.version === values.version)) fail(409, '이미 사용한 안내문 버전입니다.');
    const optional = body.optional;
    if (!Array.isArray(optional) || optional.length > 10 || optional.some(v => !v || !/^[a-z][a-z0-9_-]{0,39}$/.test(v.id) || !['title','purpose','items','retention','refusal'].every(k => text(v[k]))) || new Set(optional.map(v => v.id)).size !== optional.length) fail(400, '선택 동의 항목을 확인해 주세요.');
    const notice = { ...values, optional: optional.map(v => Object.fromEntries(['id','title','purpose','items','retention','refusal'].map(k => [k,v[k].trim()]))) };
    const policy = { id: uuid(), tenantId: u.tenantId, ...notice, contentHash: hash(JSON.stringify(notice)), publishedAt: at, publishedBy: u.id };
    s.privacy.policies.push(policy);
    for (const v of s.users.filter(v => v.tenantId === u.tenantId && v.role === 'student')) revokeStudentSessions(v.id);
    audit('privacy.policy.publish', policy.id); finish(); return { policy };
  }
  if (path === '/privacy/verifications' && method === 'POST') {
    owner(); const student = member(s,u.tenantId,body.studentId,'student'), parent = member(s,u.tenantId,body.parentId,'parent');
    if (!student || !parent || !liveAccount(parent, at) || !['in_person','signed_document'].includes(body.method) || !text(body.reference, 300) || !text(body.reason, 500) || body.confirmed !== true) fail(400, '학생·보호자와 실제 확인 방법, 보관 문서 참조, 확인 사유를 입력해 주세요.');
    if (body.validUntil != null && (!Number.isFinite(body.validUntil) || body.validUntil <= at)) fail(400, '확인 유효기간을 확인해 주세요.');
    const existing = s.privacy.verifications.filter(v => v.tenantId === u.tenantId && v.studentId === student.id && !v.revokedAt);
    if (body.previousVerificationId !== (existing.at(-1)?.id || null)) fail(409, '보호자 확인 이력이 변경되었습니다. 새로고침해 주세요.');
    if (existing.some(v => v.parentId !== parent.id && (!v.validUntil || v.validUntil > at))) fail(409, '기존 법정대리인 연결을 먼저 해제하고 확인해 주세요.');
    for (const v of existing) { v.revokedAt = at; v.revokedBy = u.id; v.revokeReason = '재확인으로 대체'; }
    const verification = { id: uuid(), tenantId: u.tenantId, studentId: student.id, parentId: parent.id, method: body.method, reference: body.reference.trim(), reason: body.reason.trim(), at, actor: u.id, validUntil: body.validUntil || null };
    s.privacy.verifications.push(verification); revokeStudentSessions(student.id); audit('privacy.guardian.verify', verification.id); finish(); return { verification };
  }
  const revoke = /^\/privacy\/verifications\/([^/]+)\/revoke$/.exec(path);
  if (revoke && method === 'POST') {
    owner(); const v = s.privacy.verifications.find(v => v.id === revoke[1] && v.tenantId === u.tenantId);
    if (!v) fail(404, '확인 이력이 없습니다.');
    if (!text(body.reason, 500)) fail(400, '해제 사유를 입력해 주세요.');
    if (!v.revokedAt) { v.revokedAt = at; v.revokedBy = u.id; v.revokeReason = body.reason.trim(); revokeStudentSessions(v.studentId); audit('privacy.guardian.revoke', v.id); }
    return finish();
  }
  if (['/privacy/consents','/privacy/withdraw'].includes(path) && method === 'POST') {
    if (u.role !== 'parent') fail(403, '확인된 보호자 계정으로 로그인해 주세요.');
    const action = path.endsWith('withdraw') ? 'withdraw' : 'grant';
    if (!text(body.requestId, 100)) fail(400, '요청 식별자가 필요합니다.');
    const fingerprint = hash(JSON.stringify({ action, studentId: body.studentId, policyId: body.policyId, policyHash: body.policyHash, required: body.required, optional: body.optional }));
    const prior = s.privacy.consents.find(c => c.tenantId === u.tenantId && c.parentId === u.id && c.requestId === body.requestId);
    if (prior) { if (prior.fingerprint !== fingerprint) fail(409, '같은 요청 식별자로 내용을 변경할 수 없습니다.'); return { ok:true, consentId:prior.id }; }
    const v = currentVerification(s, u.tenantId, body.studentId, at);
    if (!v || v.parentId !== u.id) fail(403, '학원에서 법정대리인 확인을 먼저 완료해야 합니다.');
    const p = currentPolicy(s, u.tenantId), last = lastDecision(s,u.tenantId,body.studentId);
    if (action === 'grant') {
      if (u.mustChangePassword) fail(409, '초기 비밀번호를 본인 비밀번호로 변경한 뒤 진행해 주세요.');
      if (!p || body.policyId !== p.id || body.policyHash !== p.contentHash) fail(409, '최신 안내문을 다시 읽고 선택해 주세요.');
      if (body.required !== true || !body.optional || Array.isArray(body.optional) || typeof body.optional !== 'object' || Object.keys(body.optional).length !== p.optional.length || p.optional.some(item => typeof body.optional[item.id] !== 'boolean')) fail(400, '필수 동의와 각 선택 항목의 동의 여부를 확인해 주세요.');
    }
    const student = member(s,u.tenantId,body.studentId,'student');
    const c = { id: uuid(), tenantId:u.tenantId, studentId:student.id, studentName:student.name, parentId:u.id, verificationId:v.id, policyId:action === 'grant' ? p.id : last?.policyId || p?.id || null, policyHash:action === 'grant' ? p.contentHash : last?.policyHash || p?.contentHash || null,
      action, required:action === 'grant', optional:action === 'grant' ? Object.fromEntries(p.optional.map(item => [item.id, body.optional[item.id]])) : {}, at, requestId:body.requestId, fingerprint };
    s.privacy.consents.push(c); revokeStudentSessions(student.id); audit('privacy.consent.'+action,c.id); finish(); return {ok:true,consentId:c.id};
  }
  fail(404,'개인정보 요청을 찾을 수 없습니다.');
}
