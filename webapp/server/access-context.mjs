import {isIP} from 'node:net';
import {ACCESS_META} from '../shared/access-meta.mjs';
export const exportPurposes=['teaching','guardian_consultation','operations_review','data_subject_request','incident_review'];
const normalize=ip=>typeof ip==='string'&&ip.startsWith('::ffff:')&&isIP(ip.slice(7))===4?ip.slice(7):ip;
export function trustedProxies(value=process.env.READX_TRUSTED_PROXY_IPS||''){
  const ips=typeof value==='string'?value.split(',').map(v=>normalize(v.trim())).filter(Boolean):value.map(normalize);
  if(ips.some(ip=>!isIP(ip)))throw Error('신뢰 프록시는 정확한 IP 주소 목록이어야 합니다.');return new Set(ips);
}
export function accessAddress(req,trusted=trustedProxies()){
  const peer=normalize(req.socket?.remoteAddress);if(typeof peer!=='string'||!isIP(peer))return {address:null,source:'unavailable'};
  if(!trusted.has(peer)||!req.headers['x-forwarded-for'])return {address:peer,source:'socket'};
  const raw=req.headers['x-forwarded-for'];if(typeof raw!=='string'||raw.length>2048)return {address:peer,source:'invalid-forwarding'};
  const ips=raw.split(',').map(v=>normalize(v.trim()));if(ips.some(ip=>!isIP(ip)))return {address:peer,source:'invalid-forwarding'};
  let i=ips.length-1;while(i>0&&trusted.has(ips[i]))i--;return {address:ips[i],source:'trusted-proxy'};
}
const exact=new Set(['/rights/requests','/rights/query','/rights/retention/query','/session','/setup','/login','/logout','/recover','/dashboard','/roster','/form','/assignments','/account/password','/account/device-key','/org/dashboard','/org/settings','/org/classes','/org/teachers','/org/parents','/org/guardian-links','/org/attendance','/org/consultations','/privacy/notice','/privacy/dashboard','/privacy/policies','/privacy/verifications','/privacy/consents','/privacy/withdraw','/learning/catalog','/learning/approvals','/learning/dashboard','/learning/assignments','/learning/placement','/learning/placement/start','/learning/placement/answer','/learning/placement/submit','/learning/placement/approve','/learning/placement/oral','/learning/course','/learning/course/preview','/learning/course/activate','/learning/course/check/start','/learning/course/check/save','/learning/course/check/submit','/learning/course/check/review','/learning/course/remediate','/overview','/overview/export','/overview/print','/audit/query','/audit/export','/audit/check','/audit/checkpoint','/audit/reviews','/auth/mfa/status','/auth/mfa/enroll','/auth/mfa/confirm','/auth/mfa/cancel','/auth/mfa/challenge','/auth/mfa/recovery-codes','/auth/mfa/disable']);
for(const endpoint of ['','/item','/review','/create','/run','/start','/pulse','/answer','/submit','/observe','/calibrate','/export'])exact.add('/learning/pilot'+endpoint);
for(const endpoint of ['','/configure','/preview'])exact.add('/learning/calibration'+endpoint);
const patterns=[/^\/rights\/retention\/([^/]+)\/(?:download|extend|purge)$/,/^\/rights\/requests\/([^/]+)(?:\/(?:verify|preview|resolve|download|appeal|cancel|restriction-preview|erasure-preview|lift))?$/,/^\/org\/accounts\/([^/]+)(\/reset)?$/, /^\/org\/classes\/([^/]+)$/, /^\/privacy\/verifications\/([^/]+)\/revoke$/, /^\/assignments\/([^/]+)\/(?:start|release|statistics)$/, /^\/attempts\/([^/]+)(?:\/(?:answers|submit|review|followups|print))?$/, /^\/followups\/([^/]+)\/(?:review|complete|feedback)$/, /^\/learning\/catalog\/([^/]+)$/, /^\/learning\/assignments\/([^/]+)\/start$/, /^\/learning\/runs\/([^/]+)(?:\/(?:save|submit|review|revoke))?$/];
export function accessOperation(path,method){
  const match=patterns.map(p=>p.exec(path)).find(Boolean),route=exact.has(path)?path:match?path.replace(match[1],':id'):'unknown';
  const category=path.endsWith('/export')||path.endsWith('/download')||path==='/audit/checkpoint'?'download':path.endsWith('/print')?'print':path.startsWith('/audit/')?'audit':['/login','/logout','/setup','/recover','/session','/account/password','/account/device-key'].includes(path)||path.startsWith('/auth/mfa/')?'authentication':method==='GET'||['/overview','/learning/course/preview','/learning/pilot/item','/learning/pilot/run','/learning/calibration/preview','/rights/query','/rights/retention/query'].includes(path)?'read':'write';
  return {route,category,resourceId:match&&/^[a-f0-9-]{36}$/i.test(match[1])?match[1]:null};
}
export function collectSubjects(result,state,tenantId){
  const known=new Set(state.users.filter(u=>u.tenantId===tenantId).map(u=>u.id)),subjects=new Set(),seen=new WeakSet();
  const ids=new Set(['id','userId','studentId','parentId','actor','actorId','subjectId']),arrays=new Set(['childIds','studentIds','subjects']);
  const visit=value=>{if(!value||typeof value!=='object'||seen.has(value))return;seen.add(value);if(Array.isArray(value)){value.forEach(visit);return;}for(const [key,v]of Object.entries(value)){if(ids.has(key)&&known.has(v))subjects.add(v);if(arrays.has(key)&&Array.isArray(v))v.forEach(id=>{if(known.has(id))subjects.add(id);});if(v&&typeof v==='object')visit(v);}};
  visit(result);visit(result?.[ACCESS_META]);return [...subjects].sort();
}
export function exportContext(user,body){
  if(user.role!=='teacher')return {purpose:user.role==='parent'?'guardian_access':'self_access',reference:null};
  if(!exportPurposes.includes(body.purpose))throw Object.assign(Error('파일·인쇄 이용 목적을 선택해 주세요.'),{status:400});
  const reference=typeof body.reference==='string'?body.reference.trim():'';
  if(reference&&!/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(reference)||['data_subject_request','incident_review'].includes(body.purpose)&&!reference)throw Object.assign(Error('본인 확인·점검 문서의 참조 번호를 입력해 주세요. 이름이나 답안은 입력하지 마세요.'),{status:400});
  return {purpose:body.purpose,reference:reference||null};
}
