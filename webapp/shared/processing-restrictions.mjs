export const RESTRICTION_IDS=Symbol('readx.processing.restriction.ids');
export const directRestriction=u=>!!u?.processingRestriction&&!u.processingRestriction.liftedAt;
export function parentDependencies(s,p,at){const ids=new Set([...(p.childIds||[]),...(p.processingRestriction?.dependentIds||[])]);for(const v of s.privacy?.verifications||[])if(v.tenantId===p.tenantId&&v.parentId===p.id&&!v.revokedAt&&(!v.validUntil||v.validUntil>at))ids.add(v.studentId);return [...ids].filter(id=>s.users.some(u=>u.id===id&&u.tenantId===p.tenantId&&u.role==='student'));}
export function restrictionIds(s,at=Date.now()){
 if(s[RESTRICTION_IDS])return s[RESTRICTION_IDS];
 const ids=new Set(s.users.filter(directRestriction).map(u=>u.id));
 for(const p of s.users.filter(u=>u.role==='parent'&&directRestriction(u)))for(const id of parentDependencies(s,p,at))ids.add(id);
 return ids;
}
export const processingBlocked=()=>Object.assign(Error('일반 서비스 처리가 정지된 계정·기록입니다. 권리 요청 화면에서 진행 상태를 확인해 주세요.'),{status:423,code:'PROCESSING_RESTRICTED'});
