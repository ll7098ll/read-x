import { upgradeOrganization,activeAccount } from '../shared/organization.mjs';
import { DatabaseSync } from 'node:sqlite';
import { mkdirSync,readFileSync } from 'node:fs';
import { dirname } from 'node:path';
import { createHash, randomBytes, randomUUID } from 'node:crypto';
import {passwordHash,passwordOK} from './credentials.mjs';
import { createLearningService } from './learning-service.mjs';
import { createMfaSecurity } from './mfa-security.mjs';
import { RESPONSE_STATUS } from '../shared/http-response.mjs';
import {ACCESS_META} from '../shared/access-meta.mjs';
import {createAccessLog} from './access-log.mjs';
import {createRightsService} from './rights-service.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';
import {assertNotMaintaining,acquireFileLease,privateRuntimePath,assertPlainFile} from './maintenance-lock.mjs';
import {createProcessingService} from './processing-service.mjs';
import {accessOperation,accessAddress,trustedProxies,collectSubjects,exportContext} from './access-context.mjs';
import { createExamEngine, newState } from '../shared/exam-engine.mjs';
export { scoreAttempt } from '../shared/exam-engine.mjs';

const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
const hash = value => createHash('sha256').update(value).digest('hex');

export function createExamService({ dbPath, now = Date.now, allowSetup = process.env.READX_RUNTIME!=='production', timer = true, privacyMode = 'enforced', mfaKeyring,auditKeyring,dataKeyring,proxyIps,recoveryKeyring,recoveryJournalPath,recoveryAnchor,auditAnchor,recoveryWriteHook } = {}) {
  if(process.env.READX_RUNTIME==='production'&&allowSetup)fail(500,'운영 서버의 웹 초기 설정은 허용되지 않습니다. 서버의 첫 운영자 등록 도구를 사용해 주세요.');
  if (!['enforced','synthetic'].includes(privacyMode) || process.env.READX_RUNTIME === 'production' && privacyMode !== 'enforced') fail(500,'운영 서버에서는 보호자 확인·동의를 강제해야 합니다.');
  const production=process.env.READX_RUNTIME==='production';
  const readAnchor=(path,label)=>{try{const file=privateRuntimePath(path);assertPlainFile(file);return JSON.parse(readFileSync(file,'utf8'));}catch{throw Error(label+' 별도 기준점 파일을 확인해 주세요.');}};
  recoveryAnchor||=process.env.READX_RECOVERY_ANCHOR?readAnchor(process.env.READX_RECOVERY_ANCHOR,'삭제 원장'):undefined;auditAnchor||=process.env.READX_AUDIT_ANCHOR?readAnchor(process.env.READX_AUDIT_ANCHOR,'접속기록'):undefined;
  assertNotMaintaining(dbPath);
  if (dbPath !== ':memory:') mkdirSync(dirname(dbPath), { recursive: true });
  if(dbPath!==':memory:')dbPath=privateRuntimePath(dbPath);
  const db = new DatabaseSync(dbPath);
  db.exec('PRAGMA journal_mode=WAL; PRAGMA busy_timeout=5000; PRAGMA secure_delete=ON; CREATE TABLE IF NOT EXISTS exam_state (id INTEGER PRIMARY KEY CHECK(id=1), body TEXT NOT NULL)');
  db.prepare('INSERT OR IGNORE INTO exam_state VALUES (1, ?)').run(JSON.stringify(newState()));
  const load = () => JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);
  const save = s => db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));
  const learning = createLearningService({ db, randomUUID });
  let security;
  db.exec('BEGIN IMMEDIATE');
  try { const state=load(); upgradeOrganization(state,randomUUID,now(),privacyMode); if(process.env.READX_RUNTIME === 'production' && state.organizations.some(o=>o.privacyMode!=='enforced')) fail(500,'가상 자료 검증 DB를 운영 DB로 사용할 수 없습니다.');security=createMfaSecurity({dbPath,keyring:mfaKeyring,state}); learning.upgrade(state); save(state); db.exec('COMMIT'); } catch(error) { db.exec('ROLLBACK'); db.close(); throw error; }
  let access;try{access=createAccessLog({db,dbPath,keyring:auditKeyring});}catch(e){db.close();throw e;}
  const assertAnchors=s=>{if(production&&s.users.length&&(!recoveryAnchor||!auditAnchor))throw Object.assign(Error('운영 계정에 접근하기 전에 별도 보관한 삭제 원장·접속기록 기준점 구성이 필요합니다.'),{status:503,code:'RECOVERY_SYNC_REQUIRED'});};
  try{assertAnchors(load());if(auditAnchor)access.verify(auditAnchor);}catch(e){db.close();throw e;}
  let activeRelease=()=>{};let recovery;try{recovery=createRecoveryJournal({db,dbPath,keyring:recoveryKeyring,journalPath:recoveryJournalPath,anchor:recoveryAnchor,beforeAppend:recoveryWriteHook});recovery.sync();if(recovery.path)activeRelease=acquireFileLease(recovery.path+'.active.lock','active-server');}catch(e){db.close();throw e;}
  let proxies;try{proxies=trustedProxies(proxyIps);}catch(e){activeRelease();db.close();throw e;}
  const processing=createProcessingService({db});
  let rights;try{rights=createRightsService({db,dbPath,keyring:dataKeyring,processing,recovery,confirmAccount:c=>security.confirmAccount({...c,passwordOK})});}catch(e){activeRelease();db.close();throw e;}
  const { route, expire } = createExamEngine({ extensionRoute: c=>c.path.startsWith('/audit/')?access.route(c):c.path.startsWith('/rights/')?rights.route(c):learning.route(c), allowSetup, privacyMode, randomBytes, randomUUID, hash, passwordHash, passwordOK, secureCookie: process.env.READX_COOKIE_SECURE === '1', security });
  const sweep = () => { try { assertNotMaintaining(dbPath);recovery.sync(); } catch {return;} db.exec('BEGIN IMMEDIATE'); try { assertNotMaintaining(dbPath);const s = load(); expire(s, now()); save(s); db.exec('COMMIT'); } catch { db.exec('ROLLBACK'); } };
  const interval = timer ? setInterval(sweep, 15000) : null;
  interval?.unref();
  const handler = async (req, res) => {
    res.setHeader('Content-Type', 'application/json; charset=utf-8');
    res.setHeader('Cache-Control', 'no-store'); res.setHeader('X-Content-Type-Options', 'nosniff');
    let transaction = false,body={},context,at=now();const requestId=randomUUID();res.setHeader('X-Request-Id',requestId);
    const identify=s=>{const token=/(?:^|;\s*)readx_exam=([a-f0-9]{64})(?:;|$)/.exec(req.headers.cookie||'')?.[1],session=token&&s.sessions[hash(token)];return session?.expiresAt>at?s.users.find(v=>v.id===session.userId&&activeAccount(v,at)):null;};
    const prepare=s=>{const path=new URL(req.url,'http://localhost').pathname.replace(/^\/api\/exam/,'');const user=identify(s),token=/(?:^|;\s*)readx_exam=([a-f0-9]{64})(?:;|$)/.exec(req.headers.cookie||'')?.[1],attempted=!user&&['/login','/recover'].includes(path)&&typeof body?.username==='string'&&body.username.length<=40?s.users.find(v=>v.username===body.username.trim().toLowerCase()):null;return {user,session:token&&s.sessions[hash(token)],attempted:attempted?{id:attempted.id,tenantId:attempted.tenantId}:null,path,...accessOperation(path,req.method),...accessAddress(req,proxies)};};
    const record=(s,result,status,bytes)=>{
      const u=context?.user||status<400&&result?.user,tenantId=u?.tenantId||context?.attempted?.tenantId||'system',meta=result?.[ACCESS_META],subjects=collectSubjects(status<400?result:{studentId:body?.studentId,parentId:body?.parentId,studentIds:body?.studentIds},s,tenantId);
      if(!subjects.length&&(u?.id||context?.attempted?.id))subjects.push(u?.id||context.attempted.id);
      if(u&&status<400&&['/privacy/consents','/privacy/withdraw','/privacy/verifications','/org/attendance','/org/consultations','/learning/placement/approve','/learning/placement/oral','/learning/course/preview','/learning/course/activate','/learning/course/check/review','/learning/course/remediate'].includes(context.path)){
        for(const id of collectSubjects({studentId:body?.studentId,parentId:body?.parentId},s,tenantId))if(!subjects.includes(id))subjects.push(id);
      }
      if(u&&context?.resourceId){
        const id=context.resourceId,object=s.attempts.find(v=>v.id===id&&v.tenantId===tenantId)||s.assignments.find(v=>v.id===id&&v.tenantId===tenantId)||s.followups.find(v=>v.id===id&&v.tenantId===tenantId)||s.privacy?.verifications.find(v=>v.id===id&&v.tenantId===tenantId)||s.users.find(v=>v.id===id&&v.tenantId===tenantId);
        for(const subject of collectSubjects(object,s,tenantId))if(!subjects.includes(subject))subjects.push(subject);
        for(const table of ['learning_runs','learning_assignments']){const row=db.prepare(`SELECT body FROM ${table} WHERE id=? AND tenant_id=?`).get(tenantId+':'+id,tenantId);if(row)for(const subject of collectSubjects(JSON.parse(row.body),s,tenantId))if(!subjects.includes(subject))subjects.push(subject);}
      }
      return {requestId,tenantId,at,actorId:u?.id||null,actorRole:u?.role||'anonymous',attemptedAccountId:context?.attempted?.id||null,method:['GET','POST','HEAD'].includes(req.method)?req.method:'OTHER',route:context?.route||'unknown',resourceId:context?.resourceId||null,category:context?.category||'write',status,bytes,address:context?.address||null,addressSource:context?.source||'unavailable',subjects:subjects.sort(),records:Number.isSafeInteger(meta?.records)?meta.records:null,...context?.export,...(meta?.review?{review:meta.review}:{})};
    };
    try {
      assertNotMaintaining(dbPath);recovery.sync();
      if (!['GET', 'HEAD'].includes(req.method)) {
        const origin = req.headers.origin;
        if (origin) {
          let source; try { source = new URL(origin); } catch { fail(403, '같은 서비스 화면에서 요청해 주세요.'); }
          if (!['http:', 'https:'].includes(source.protocol) || source.host !== req.headers.host) fail(403, '같은 서비스 화면에서 요청해 주세요.');
        }
        if (!req.headers['content-type']?.startsWith('application/json')) fail(415, 'JSON 요청이 필요합니다.');
        const maxBody = /\/learning\/runs\/[^/]+\/save$/.test(req.url) ? 2097152 : 65536;
        let raw = ''; for await (const chunk of req) { raw += chunk; if (Buffer.byteLength(raw) > maxBody) fail(413, '요청이 너무 큽니다.'); }
        try { body = JSON.parse(raw || '{}'); } catch { fail(400, '올바른 JSON 요청이 아닙니다.'); }
        if (!body || Array.isArray(body) || typeof body !== 'object') fail(400, '요청 형식을 확인해 주세요.');
      }
      db.exec('BEGIN IMMEDIATE'); transaction = true;assertNotMaintaining(dbPath);
      const s = load();assertAnchors(s);at=now();expire(s, at);context=prepare(s);
      // Authorization and MFA still run inside the engine; purpose validation
      // never grants access or includes a download before its audit commit.
      access.assertHead();
      const verified=!context.user||!security.guard(s,context.user,context.session,at);
      if(verified)processing.before({s,u:context.user,path:context.path,method:req.method,body,at});
      const working=verified?processing.stateForRead(s,context.user,context.path,req.method,at):s;
      const result = processing.sanitize(route(working, req, res, body, at),s,context.path,at);
      if((result[RESPONSE_STATUS]||200)<400&&context.user&&['download','print'].includes(context.category))context.export=exportContext(context.user,body);
      const status=result[RESPONSE_STATUS]||200,encoded=JSON.stringify(result);access.append(record(s,result,status,Buffer.byteLength(encoded)));
      save(s); db.exec('COMMIT');transaction=false;access.committed();
      try{recovery.sync();}catch(e){e.committed=true;throw e;}
      res.statusCode=status;res.end(encoded);
    } catch (e) {
      if (transaction) db.exec('ROLLBACK');
      let status=e.status||500;
      if(e.code!=='MAINTENANCE_REQUIRED'&&(e.code!=='RECOVERY_SYNC_REQUIRED'||e.committed))try{db.exec('BEGIN IMMEDIATE');const s=load();context||=prepare(s);access.assertHead();access.append(record(s,null,status,0));db.exec('COMMIT');access.committed();}catch{try{db.exec('ROLLBACK');}catch{}status=500;console.error('Access log could not be committed.');}
      res.statusCode = status;
      if (!e.status) console.error('Exam service failed:', e instanceof SyntaxError?'저장 자료의 형식 검사 실패':e.message);
      res.end(JSON.stringify({ error: e.code==='RECOVERY_SYNC_REQUIRED'?(e.committed?'변경은 DB에 저장되었지만 별도 삭제 원장 동기화를 확인하지 못했습니다. 서비스 복구 후 같은 요청 상태를 다시 확인해 주세요.':'별도 삭제 원장 동기화·복원 검증이 필요해 서비스 이용을 중지했습니다.'):e.code==='MAINTENANCE_REQUIRED'?'복구·정리 작업을 확인하는 동안 서비스 이용이 일시 중지됩니다.':status<500 ? e.message : '서버 저장에 실패했습니다. 잠시 후 다시 시도해 주세요.',...(['RECOVERY_SYNC_REQUIRED','MAINTENANCE_REQUIRED','RESTORE_CREDENTIALS_REQUIRED'].includes(e.code)?{code:e.code}:status===423?{code:'PROCESSING_RESTRICTED'}:{}) }));
    }
  };
  let closed=false;return { handler, close() { if(closed)return;closed=true;if (interval) clearInterval(interval); db.close();activeRelease(); } };
}
