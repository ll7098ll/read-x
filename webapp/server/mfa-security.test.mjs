import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer,request} from 'node:http';
import {randomBytes} from 'node:crypto';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
import {DatabaseSync} from 'node:sqlite';
import {createExamService} from './exam-service.mjs';
import {totp,encodeBase32,decodeBase32,matchTotp} from './totp.mjs';
import {createMfaProtector} from './mfa-keys.mjs';
import {passwordOK} from './credentials.mjs';
const password='Mfa-Synthetic-Test-2026!';

test('TOTP matches all 18 RFC 6238 vectors and enforces skew and replay boundaries',()=>{
  const times=[59,1111111109,1111111111,1234567890,2000000000,20000000000];
  const expected={sha1:['94287082','07081804','14050471','89005924','69279037','65353130'],sha256:['46119246','68084774','67062674','91819424','90698825','77737706'],sha512:['90693936','25091201','99943326','93441116','38618901','47863826']};
  for(const [algorithm,n]of [['sha1',20],['sha256',32],['sha512',64]]){const raw=Buffer.from('1234567890'.repeat(7).slice(0,n)),secret=encodeBase32(raw);assert.deepEqual(decodeBase32(secret),raw);times.forEach((time,i)=>assert.equal(totp(secret,time*1000,{digits:8,algorithm}),expected[algorithm][i]));}
  const key=encodeBase32(Buffer.from('12345678901234567890')),at=1234567890000,counter=Math.floor(at/30000),code=totp(key,at);
  assert.equal(matchTotp(key,code,at),counter);assert.equal(matchTotp(key,code,at,counter),null);assert.equal(matchTotp(key,totp(key,(counter+1)*30000),at),counter+1);assert.equal(matchTotp(key,totp(key,(counter+2)*30000),at),null);assert.equal(matchTotp(key,'12345',at),null);
});

test('MFA seed encryption is bound to account and supports key rotation without plaintext database storage',()=>{
  const k1=randomBytes(32).toString('base64'),k2=randomBytes(32).toString('base64'),user={id:'one',tenantId:'academy'},secret=encodeBase32(randomBytes(32));
  const old=createMfaProtector({dbPath:':memory:',keyring:{activeId:'old',keys:{old:k1}}}),record=old.seal(secret,user);
  assert.equal(JSON.stringify(record).includes(secret),false);assert.equal(JSON.stringify(record).includes(k1),false);assert.equal(old.open(record,user),secret);assert.throws(()=>old.open(record,{...user,id:'other'}));
  const rotated=createMfaProtector({dbPath:':memory:',keyring:{activeId:'new',keys:{old:k1,new:k2}}});assert.equal(rotated.open(record,user),secret);assert.equal(rotated.seal(secret,user).keyId,'new');assert.throws(()=>createMfaProtector({dbPath:':memory:',keyring:{activeId:'new',keys:{new:k2}}}).open(record,user));
  const env=process.env.READX_MFA_KEYS;delete process.env.READX_MFA_KEYS;try{assert.throws(()=>createMfaProtector({dbPath:':memory:',production:true}),/READX_MFA_KEYS/);}finally{if(env!==undefined)process.env.READX_MFA_KEYS=env;}
});

async function fixture(t,options={}) {
  let at=Date.now(),service,server,origin,closed=true;
  const ring=options.mfaKeyring||{activeId:'test',keys:{test:randomBytes(32).toString('base64')}};
  const open=async()=>{service=createExamService({dbPath:':memory:',timer:false,now:()=>at,...options,mfaKeyring:ring});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));origin=`http://127.0.0.1:${server.address().port}`;closed=false;};
  const close=async()=>{if(closed)return;closed=true;server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};t.after(close);await open();
  const client=()=>{let cookie='';return async(path,body,expected=200)=>{const r=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});if(r.headers.get('set-cookie'))cookie=r.headers.get('set-cookie').split(';')[0];const d=await r.json();assert.equal(r.status,expected,path+': '+JSON.stringify(d));return d;};};
  const owner=client(),setup=await owner('/setup',{name:'가상 운영자',username:'owner',password});
  let ownerSecret;
  const enroll=async(c=owner,currentPassword=password)=>{const e=await c('/auth/mfa/enroll',{currentPassword});const r=await c('/auth/mfa/confirm',{enrollmentId:e.enrollmentId,code:totp(e.secret,at)});if(c===owner)ownerSecret=e.secret;return {...e,codes:r.recoveryCodes};};
  const proof=()=>{at+=30000;return {currentPassword:password,mfaCode:totp(ownerSecret,at)};};
  return {owner,setup,client,enroll,close,proof,now:()=>at,advance:(ms=30000)=>{at+=ms;},restart:async()=>{await close();await open();}};
}

test('default staff sessions cannot read or mutate private routes until MFA enrollment; status does not disclose seed or codes',async t=>{
  const f=await fixture(t);assert.equal(f.setup.auth.stage,'enroll');
  for(const path of ['/dashboard','/org/dashboard','/learning/catalog','/learning/dashboard','/learning/placement','/overview','/form','/privacy/dashboard'])assert.equal((await f.owner(path,undefined,403)).code,'MFA_REQUIRED');
  for(const path of ['/account/device-key','/roster','/assignments','/overview/export','/org/teachers'])await f.owner(path,{},403);
  const e=await f.enroll();assert.equal(e.codes.length,10);assert.equal((await f.owner('/session')).auth.stage,'full');assert.ok((await f.owner('/dashboard')).user.isOwner);
  for(const path of ['/session','/auth/mfa/status','/org/dashboard']){const d=JSON.stringify(await f.owner(path));assert.equal(d.includes(e.secret),false);assert.equal(e.codes.some(code=>d.includes(code)),false);}
  await f.owner('/auth/mfa/disable',{currentPassword:password,code:totp(e.secret,f.now())},409);
});

test('first factor cannot evict an authenticated device; replay, session scope and single-device full login are enforced',async t=>{
  const f=await fixture(t),e=await f.enroll(),other=f.client();assert.equal((await other('/login',{username:'owner',password})).auth.stage,'challenge');
  assert.ok((await f.owner('/dashboard')).user);await other('/dashboard',undefined,403);await other('/auth/mfa/enroll',{currentPassword:password,code:totp(e.secret,f.now())},403);
  await other('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())},400);f.advance();await other('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())});
  await f.owner('/dashboard',undefined,401);assert.equal((await other('/session')).auth.stage,'full');
  const third=f.client();await third('/login',{username:'owner',password});await third('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())},400);await other('/dashboard');
  f.advance(8*3600000);await other('/dashboard',undefined,401);
});

test('new staff must change initial password, then register MFA; ordinary account edits cannot disable MFA',async t=>{
  const f=await fixture(t);await f.enroll();const classroom=(await f.owner('/org/dashboard')).classes[0];
  await f.owner('/org/teachers',{name:'우회 시도',username:'no_stepup',password,classIds:[classroom.id]},400);
  const teacher=(await f.owner('/org/teachers',{name:'가상 교사',username:'teacher',password,classIds:[classroom.id],...f.proof()})).user;assert.equal(teacher.mustChangePassword,true);
  const c=f.client();await c('/login',{username:'teacher',password});await c('/auth/mfa/enroll',{currentPassword:password},409);await c('/account/password',{currentPassword:password,newPassword:password},400);
  const own=password+'-Own';await c('/account/password',{currentPassword:password,newPassword:own});await c('/dashboard',undefined,403);await f.enroll(c,own);await c('/dashboard');
  const profile=(await f.owner('/org/dashboard')).users.find(u=>u.id===teacher.id);await f.owner('/org/accounts/'+teacher.id,{...profile,active:true,reason:'권한 우회 검사',mfa:null,role:'parent'});
  await c('/login',{username:'teacher',password:own});assert.equal((await c('/session')).auth.stage,'challenge');
});

test('backup recovery is single-use, forces a new authenticator and invalidates old factor and backup set',async t=>{
  const f=await fixture(t),e=await f.enroll(),c=f.client();await c('/login',{username:'owner',password});await c('/auth/mfa/challenge',{method:'backup',code:e.codes[0]});
  assert.equal((await c('/session')).auth.stage,'recovery-enroll');await c('/overview',undefined,403);await f.owner('/dashboard',undefined,401);
  const replay=f.client();await replay('/login',{username:'owner',password});await replay('/auth/mfa/challenge',{method:'backup',code:e.codes[0]},400);assert.equal((await c('/session')).auth.stage,'recovery-enroll');
  const next=await f.enroll(c);assert.notEqual(next.secret,e.secret);assert.equal((await c('/session')).auth.stage,'full');
  const other=f.client();await other('/login',{username:'owner',password});await other('/auth/mfa/challenge',{method:'backup',code:e.codes[0]},400);await other('/auth/mfa/challenge',{method:'backup',code:e.codes[1]},400);
  f.advance();await other('/auth/mfa/challenge',{method:'totp',code:totp(next.secret,f.now())});
});

test('enrollment is session-bound and expiring; factor changes, code regeneration and password changes require fresh MFA',async t=>{
  const f=await fixture(t),first=await f.owner('/auth/mfa/enroll',{currentPassword:password}),second=f.client();await second('/login',{username:'owner',password});await second('/auth/mfa/confirm',{enrollmentId:first.enrollmentId,code:totp(first.secret,f.now())},409);
  const pending=await second('/auth/mfa/enroll',{currentPassword:password});await second('/auth/mfa/cancel',{enrollmentId:pending.enrollmentId});await second('/auth/mfa/confirm',{enrollmentId:pending.enrollmentId,code:totp(pending.secret,f.now())},409);
  const e=await f.enroll(second);await second('/auth/mfa/recovery-codes',{currentPassword:password,code:totp(e.secret,f.now())},400);f.advance();const r=await second('/auth/mfa/recovery-codes',{currentPassword:password,code:totp(e.secret,f.now())});assert.equal(r.recoveryCodes.length,10);
  await second('/account/password',{currentPassword:password,newPassword:password+'-new'},400);f.advance();await second('/account/password',{currentPassword:password,newPassword:password+'-new',code:totp(e.secret,f.now())});assert.equal((await second('/session')).auth.stage,'full');
  const again=f.client();await again('/login',{username:'owner',password:password+'-new'});assert.equal((await again('/session')).auth.stage,'challenge');
});

test('failed factor limits survive rollback boundaries and server restart; encrypted seeds and codes stay out of database plaintext',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-mfa-'));let f;t.after(async()=>{await f?.close();await rm(dir,{recursive:true,force:true});});const dbPath=join(dir,'test.sqlite');f=await fixture(t,{dbPath});const e=await f.enroll(),c=f.client();await c('/login',{username:'owner',password});
  for(let i=0;i<7;i++)await c('/auth/mfa/challenge',{method:'totp',code:'invalid'},400);await f.restart();await c('/auth/mfa/challenge',{method:'totp',code:'invalid'},429);f.advance();await c('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())},429);
  const db=new DatabaseSync(dbPath);const raw=db.prepare('SELECT body FROM exam_state WHERE id=1').get().body;db.close();assert.equal(raw.includes(e.secret),false);assert.equal(e.codes.some(code=>raw.includes(code)),false);assert.equal(JSON.parse(raw).users[0].mfaFailures.count,8);
  f.advance(16*60000);await c('/login',{username:'owner',password});await c('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())});
});

test('local administrator recovery cannot create users or grant ownership and requires password before restricted reenrollment',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-mfa-recovery-'));let f;t.after(async()=>{await f?.close();await rm(dir,{recursive:true,force:true});});const dbPath=join(dir,'test.sqlite');f=await fixture(t,{dbPath});const enrollment=await f.enroll();
  assert.throws(()=>execFileSync(process.execPath,['server/recover-mfa.mjs','--db',dbPath,'--username','absent','--reason','가상 확인','--reference','TEST-001','--verified-identity'],{stdio:'pipe'}));
  const output=execFileSync(process.execPath,['server/recover-mfa.mjs','--db',dbPath,'--username','owner','--reason','가상 본인 확인','--reference','TEST-002','--verified-identity'],{encoding:'utf8',stdio:'pipe'});const code=output.trim().split(/\r?\n/).at(-1);assert.match(code,/^[a-f0-9]{64}$/);
  await f.owner('/dashboard',undefined,401);const c=f.client();await c('/login',{username:'owner',password:'wrong'},401);await c('/login',{username:'owner',password});f.advance();await c('/auth/mfa/challenge',{method:'totp',code:totp(enrollment.secret,f.now())},400);await c('/auth/mfa/challenge',{method:'server-recovery',code});await c('/dashboard',undefined,403);await f.enroll(c);assert.equal((await c('/dashboard')).user.isOwner,true);assert.equal((await c('/org/dashboard')).audit.find(a=>a.action==='auth.mfa.recovery.local').actor,'local-server-admin');
  const other=f.client();await other('/login',{username:'owner',password});await other('/auth/mfa/challenge',{method:'server-recovery',code},400);
});

test('optional MFA can be removed only with password and a fresh factor; enforced staff policy cannot be changed by request fields',async t=>{
  const f=await fixture(t,{privacyMode:'synthetic'});assert.equal(f.setup.auth.stage,'full');const e=await f.enroll();f.advance();await f.owner('/auth/mfa/disable',{currentPassword:'wrong',code:totp(e.secret,f.now())},400);await f.owner('/auth/mfa/disable',{currentPassword:password,code:totp(e.secret,f.now())});
  await f.owner('/logout',{});assert.equal((await f.owner('/login',{username:'owner',password})).auth.stage,'full');
  const mandatory=await fixture(t);await mandatory.enroll();const settings=await mandatory.owner('/org/settings',{name:'검사 학원',revision:0,privacyMode:'synthetic'});assert.equal(settings.organization.privacyMode,'enforced');await mandatory.owner('/auth/mfa/disable',{currentPassword:password,role:'parent',privacyMode:'synthetic'},409);
});

test('restricted enrollment and challenge sessions expire and old pending setup cannot activate a factor',async t=>{
  const f=await fixture(t),pending=await f.owner('/auth/mfa/enroll',{currentPassword:password});f.advance(11*60000);await f.owner('/auth/mfa/confirm',{enrollmentId:pending.enrollmentId,code:totp(pending.secret,f.now())},401);
  await f.owner('/login',{username:'owner',password});await f.enroll();const c=f.client();await c('/login',{username:'owner',password});f.advance(6*60000);await c('/auth/mfa/challenge',{method:'totp',code:'123456'},401);assert.equal((await f.owner('/auth/mfa/status')).pendingExpiresAt,null);
});

test('password reset issuance and staff provisioning require fresh proof, and password recovery cannot remove MFA',async t=>{
  const f=await fixture(t),e=await f.enroll();await f.owner(`/org/accounts/${f.setup.user.id}/reset`,{reason:'우회 검사'},400);
  const issued=await f.owner(`/org/accounts/${f.setup.user.id}/reset`,{reason:'가상 본인 확인',...f.proof()});const anon=f.client();const changed=password+'-Reset';await anon('/recover',{username:'owner',code:issued.code,newPassword:changed});
  await anon('/login',{username:'owner',password:changed});assert.equal((await anon('/session')).auth.stage,'challenge');await anon('/dashboard',undefined,403);f.advance();await anon('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())});assert.equal((await anon('/session')).user.mfaEnabled,true);
});

test('an unverified MFA session never discloses linked children or classroom metadata',async t=>{
  const f=await fixture(t,{privacyMode:'synthetic'}),roster=await f.owner('/roster',{student:{name:'가상 학생',username:'child',password},parent:{name:'가상 보호자',username:'guardian',password}}),c=f.client();
  await c('/login',{username:'guardian',password});const e=await f.enroll(c);assert.deepEqual((await c('/session')).user.childIds,[roster.student.id]);await c('/logout',{});
  const partial=await c('/login',{username:'guardian',password});assert.deepEqual(partial.user.childIds,[]);assert.equal(partial.user.className,'');assert.equal(JSON.stringify(partial).includes(roster.student.id),false);assert.deepEqual((await c('/session')).user.childIds,[]);
  f.advance();await c('/auth/mfa/challenge',{method:'totp',code:totp(e.secret,f.now())});assert.deepEqual((await c('/session')).user.childIds,[roster.student.id]);
});

test('first owner bootstrap accepts private stdin only, stores a password hash and refuses existing users or unrelated databases',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-bootstrap-'));t.after(()=>rm(dir,{recursive:true,force:true}));const dbPath=join(dir,'new.sqlite');
  const body={name:'가상 첫 운영자',username:'first_owner',password,className:'확인용 반'},run=(path,input)=>execFileSync(process.execPath,['server/bootstrap-owner.mjs','--db',path],{input:JSON.stringify(input)+'\n',encoding:'utf8',stdio:'pipe'});
  const out=run(dbPath,body);assert.equal(out.includes(password),false);assert.match(out,/등록했습니다/);
  const db=new DatabaseSync(dbPath),raw=db.prepare('SELECT body FROM exam_state WHERE id=1').get().body;db.close();const s=JSON.parse(raw);
  assert.equal(s.users.length,1);assert.equal(s.users[0].isOwner,true);assert.equal(s.organizations[0].privacyMode,'enforced');assert.equal(raw.includes(password),false);assert.equal(passwordOK(password,s.users[0].password),true);assert.equal(passwordOK(password,'invalid'),false);
  assert.equal(s.audit.at(-1).actor,'local-server-admin');assert.equal(s.audit.at(-1).tenantId,s.users[0].tenantId);
  assert.throws(()=>run(dbPath,{...body,username:'second_owner'}),/계정이 있는 DB/);
  const unrelated=join(dir,'unrelated.sqlite'),other=new DatabaseSync(unrelated);other.exec('CREATE TABLE unrelated(value TEXT)');other.close();assert.throws(()=>run(unrelated,body),/기존 DB가 아닙니다/);
  assert.throws(()=>execFileSync(process.execPath,['server/bootstrap-owner.mjs','--db',join(dir,'invalid.sqlite')],{input:'{"password":"PRIVATE-INVALID-INPUT"\n',encoding:'utf8',stdio:'pipe'}),e=>!e.stdout.includes('PRIVATE-INVALID-INPUT')&&!e.stderr.includes('PRIVATE-INVALID-INPUT'));
  assert.throws(()=>run(join(dir,'oversize.sqlite'),{...body,padding:'x'.repeat(9000)}),/길이 제한/);
  const service=createExamService({dbPath,timer:false}),server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));
  try{const origin=`http://127.0.0.1:${server.address().port}`,login=await fetch(origin+'/api/exam/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:body.username,password})});assert.equal(login.status,200);assert.equal((await login.json()).auth.stage,'enroll');assert.equal((await fetch(origin+'/api/exam/dashboard',{headers:{Cookie:login.headers.get('set-cookie').split(';')[0]}})).status,403);}
  finally{server.closeAllConnections();await new Promise(r=>server.close(r));service.close();}
});

test('production never exposes web bootstrap even behind a loopback proxy; development rejects an external Host',async t=>{
  const runtime=process.env.READX_RUNTIME;let service;
  const productionFixture=await mkdtemp(join(tmpdir(),'readx-bootstrap-production-'));
  try{process.env.READX_RUNTIME='production';assert.throws(()=>createExamService({dbPath:':memory:',allowSetup:true,timer:false}),/웹 초기 설정/);service=createExamService({dbPath:join(productionFixture,'db','app.sqlite'),recoveryJournalPath:join(productionFixture,'recovery.ndjson'),recoveryKeyring:{activeId:'recovery',keys:{recovery:randomBytes(32).toString('base64')}},timer:false,dataKeyring:{activeId:'data',keys:{data:randomBytes(32).toString('base64')}},auditKeyring:{activeId:'audit',keys:{audit:randomBytes(32).toString('base64')}},mfaKeyring:{activeId:'test',keys:{test:randomBytes(32).toString('base64')}}});}
  finally{if(runtime===undefined)delete process.env.READX_RUNTIME;else process.env.READX_RUNTIME=runtime;}
  const server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));t.after(async()=>{server.closeAllConnections();await new Promise(r=>server.close(r));service.close();await rm(productionFixture,{recursive:true,force:true});});const origin=`http://127.0.0.1:${server.address().port}`;
  assert.equal((await(await fetch(origin+'/api/exam/session')).json()).setupRequired,false);
  const setup=await fetch(origin+'/api/exam/setup',{method:'POST',headers:{'Content-Type':'application/json',Host:'academy.example'},body:JSON.stringify({name:'가상 사용자',username:'should_fail',password})});assert.equal(setup.status,409);
  const dev=createExamService({dbPath:':memory:',timer:false}),devServer=createServer(dev.handler);await new Promise(r=>devServer.listen(0,'127.0.0.1',r));t.after(async()=>{devServer.closeAllConnections();await new Promise(r=>devServer.close(r));dev.close();});
  // Node fetch normalizes Host; send the proxy/rebinding case over raw HTTP.
  const poisoned=await new Promise((resolve,reject)=>{const r=request({hostname:'127.0.0.1',port:devServer.address().port,path:'/api/exam/setup',method:'POST',headers:{'Content-Type':'application/json',Host:'rebind.example'}},res=>{res.resume();res.on('end',()=>resolve(res.statusCode));});r.on('error',reject);r.end(JSON.stringify({name:'가상 사용자',username:'should_fail',password}));});assert.equal(poisoned,403);
});
