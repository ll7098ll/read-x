import { checkProductionReadiness } from '../scripts/check-production-readiness.mjs';
const result=await checkProductionReadiness({manifestPath:process.env.READX_READINESS_MANIFEST});
const issues=[...result.issues];
try { const url=new URL(process.env.READX_PUBLIC_ORIGIN);if(url.protocol!=='https:'||url.username||url.password||url.search||url.hash||url.pathname!=='/')issues.push('운영 접속 주소는 HTTPS여야 합니다.'); } catch { issues.push('운영 접속 주소 READX_PUBLIC_ORIGIN이 필요합니다.'); }
if(process.env.READX_COOKIE_SECURE!=='1')issues.push('운영 세션의 Secure 쿠키 설정이 필요합니다.');
if(!process.env.READX_EXAM_DB)issues.push('검증 DB와 분리된 운영 DB 경로가 필요합니다.');
if(!process.env.READX_MFA_KEYS)issues.push('별도로 보관한 운영 MFA 암호화 키 구성이 필요합니다.');
if(!process.env.READX_AUDIT_KEYS)issues.push('분리해서 보관한 접속기록 검증 키 구성이 필요합니다.');
if(!process.env.READX_DATA_KEYS)issues.push('분리해서 보관한 개인정보 요청 암호화 키 구성이 필요합니다.');
if(!process.env.READX_RECOVERY_KEYS)issues.push('독립적으로 보관한 삭제·복원 원장 검증 키가 필요합니다.');
if(!process.env.READX_RECOVERY_JOURNAL)issues.push('운영 DB 밖에 보관하는 별도 삭제 원장 경로가 필요합니다.');
if(!process.env.READX_BACKUP_KEYS)issues.push('백업 파일과 분리 보관한 독립 백업 암호화 키 구성이 필요합니다.');
if(!process.env.READX_RECOVERY_ANCHOR||!process.env.READX_AUDIT_ANCHOR)issues.push('분리 보관한 삭제 원장·접속기록 기준점 파일 경로가 필요합니다.');
if(issues.length){console.error('실제 개인정보 운영 준비가 완료되지 않았습니다.\n'+issues.join('\n'));process.exit(1);}
process.env.READX_RUNTIME='production';
await import('./start.mjs');
