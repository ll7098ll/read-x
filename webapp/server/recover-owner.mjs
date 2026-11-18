import {assertNotMaintaining,privateRuntimePath} from './maintenance-lock.mjs';
import {recordLocalAccess} from './local-access-event.mjs';
import { DatabaseSync } from 'node:sqlite';
import { randomBytes, createHash, randomUUID } from 'node:crypto';
import { existsSync } from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { upgradeOrganization } from '../shared/organization.mjs';

// Local server administrator recovery only. It cannot create a user or grant ownership.
const args = process.argv.slice(2), username = args[args.indexOf('--username')+1];
const supplied = args.indexOf('--db');
const dbPath = supplied >= 0 ? resolve(args[supplied+1]) : process.env.READX_EXAM_DB || fileURLToPath(new URL('../.exam-data/readx.sqlite', import.meta.url));
if (!args.includes('--username') || !username || !existsSync(dbPath)) { console.error('사용법: node server/recover-owner.mjs --username 기존원장아이디 [--db 기존DB파일]'); process.exit(1); }
assertNotMaintaining(dbPath);privateRuntimePath(dbPath);const db = new DatabaseSync(dbPath);
try {
  db.exec('BEGIN IMMEDIATE');
  assertNotMaintaining(dbPath);const s = JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);
  const at = Date.now(); upgradeOrganization(s, randomUUID, at);
  const u = s.users.find(u => u.username === username.toLowerCase() && u.role === 'teacher' && u.isOwner && u.active);
  if (!u) throw new Error('활성 상태의 기존 원장 계정만 복구할 수 있습니다.');
  const refIndex=args.indexOf('--restore-reference'),restoreReference=refIndex>=0?args[refIndex+1]:'';
  if(u.restoreCredentialHold&&(!args.includes('--restore-identity-and-role-verified')||!restoreReference||!/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(restoreReference)))throw Error('복원 원장의 본인·현재 운영 권한을 실제 확인하고 --restore-identity-and-role-verified --restore-reference 검토번호를 지정해 주세요.');
  const code = randomBytes(32).toString('hex');
  s.recoveryCodes = s.recoveryCodes.filter(r => r.userId !== u.id);
  s.recoveryCodes.push({ userId:u.id, hash:createHash('sha256').update(code).digest('hex'), expiresAt:at+15*60000, issuedBy:'local-server-admin',...(u.restoreCredentialHold?{restoreVerified:true,restoreReference}:{}) });
  s.audit.push({at,actor:'local-server-admin',tenantId:u.tenantId,subjectId:u.id,action:'account.recovery.local'});
  db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s)); recordLocalAccess({db,dbPath:dbPath,user:u,at,action:'local/password-recovery'});db.exec('COMMIT');
  console.log('15분 동안 한 번 사용할 수 있는 원장 계정 복구 코드:'); console.log(code);
} catch (error) { try { db.exec('ROLLBACK'); } catch {} console.error(error.message); process.exitCode=1; }
finally { db.close(); }
