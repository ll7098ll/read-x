import {assertNotMaintaining,privateRuntimePath} from './maintenance-lock.mjs';
import {recordLocalAccess} from './local-access-event.mjs';
import { DatabaseSync } from 'node:sqlite';
import { randomBytes,randomUUID,createHash } from 'node:crypto';
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { upgradeOrganization,activeAccount } from '../shared/organization.mjs';

// A local server administrator must verify identity outside this application.
// This grants only a short-lived second-factor recovery, never a user or role.
const args=process.argv.slice(2),value=flag=>{const i=args.indexOf(flag);return i>=0?args[i+1]:'';};
const username=value('--username'),file=value('--db'),reason=value('--reason'),reference=value('--reference');
if(!file||!existsSync(resolve(file))||!/^[a-zA-Z0-9._-]{3,40}$/.test(username)||!reason?.trim()||reason.length>1000||!reference?.trim()||reference.length>300||!args.includes('--verified-identity')){
  console.error('사용법: node server/recover-mfa.mjs --db 기존DB --username 기존아이디 --reason 확인사유 --reference 별도확인문서번호 --verified-identity');process.exit(1);
}
assertNotMaintaining(resolve(file));privateRuntimePath(resolve(file));const db=new DatabaseSync(resolve(file));
try{
  db.exec('BEGIN IMMEDIATE');assertNotMaintaining(resolve(file));const s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body),at=Date.now();upgradeOrganization(s,randomUUID,at);
  const u=s.users.find(v=>v.username===username.toLowerCase()&&activeAccount(v,at)&&v.mfa?.secret);
  if(!u)throw Error('추가 인증이 등록된 활성 기존 계정만 복구할 수 있습니다.');
  const code=randomBytes(32).toString('hex');s.mfaRecoveries=(s.mfaRecoveries||[]).filter(r=>r.userId!==u.id&&r.expiresAt>at);
  s.mfaRecoveries.push({userId:u.id,hash:createHash('sha256').update(u.id+':'+code).digest('hex'),issuedAt:at,expiresAt:at+15*60000,issuedBy:'local-server-admin',reason:reason.trim(),reference:reference.trim()});
  u.mfa.recoveryRequired=true;u.mfa.version=randomUUID();u.mfaFailures=null;delete u.pendingMfa;delete u.deviceDraftKey;
  for(const [key,session]of Object.entries(s.sessions))if(session.userId===u.id)delete s.sessions[key];
  s.audit.push({at,actor:'local-server-admin',tenantId:u.tenantId,subjectId:u.id,action:'auth.mfa.recovery.local',reason:reason.trim(),reference:reference.trim()});
  db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));recordLocalAccess({db,dbPath:resolve(file),user:u,at,action:'local/mfa-recovery'});db.exec('COMMIT');
  console.log('본인 확인 후 안전한 방법으로 전달할 일회용 추가 인증 복구 코드 (15분 유효):');console.log(code);
}catch(e){try{db.exec('ROLLBACK');}catch{}console.error(e.message);process.exitCode=1;}finally{db.close();}
