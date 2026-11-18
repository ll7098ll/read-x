import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { DatabaseSync } from 'node:sqlite';
import { createExamService } from './exam-service.mjs';
import { upgradeOrganization } from '../shared/organization.mjs';
import { newState } from '../shared/exam-engine.mjs';
import { randomUUID } from 'node:crypto';
import { totp } from './totp.mjs';

const password='Synthetic-Consent-Test-2026!';
const newPassword='Guardian-Own-Test-Password-2026!';
const notice = (previousPolicyId=null, version='검증용 1') => ({ previousPolicyId, version, operatorLegalName:'가상 사업자', privacyContact:'검사 전용 연락처', purpose:'가상 자료 기능 검증', items:'가상 학생 별명·응답·근거·보호자 계정', retention:'검사 종료 시 가상 DB 삭제', refusal:'거부 가능, 학생 학습은 시작되지 않음', childNotice:'어른에게 물어보고 생각을 남겨요.', guardianNotice:'검사용 대면 확인 이력, 계정 설정에서 철회', enrollmentBasisReference:'TEST-BASIS-001 가상 자료 전용', reviewReference:'TEST-REVIEW-001 가상 자료 전용', reviewed:true,
  optional:[{id:'test_optional',title:'검사용 선택 수집',purpose:'선택 거부 검사',items:'가상 값',retention:'검사 종료까지',refusal:'동의하지 않아도 필수 학습 가능'}] });
async function fixture(t,options={}) {
  let at=Date.UTC(2026,10,14,1);const service=createExamService({dbPath:':memory:',timer:false,now:()=>at,...options});
  const server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));
  let closed=false;const close=async()=>{if(closed)return;closed=true;server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};t.after(close);
  const origin=`http://127.0.0.1:${server.address().port}`;
  const client=()=>{let cookie='';return async(path,body,expected=200)=>{const r=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});if(r.headers.get('set-cookie'))cookie=r.headers.get('set-cookie').split(';')[0];const d=await r.json();assert.equal(r.status,expected,path+': '+JSON.stringify(d));return d;};};
  const owner=client(),setup=await owner('/setup',{name:'가상 원장',username:'owner',password});
  const enrollStaff=async c=>{let currentPassword=password;if((await c('/session')).user.mustChangePassword){currentPassword=password+'-Own';await c('/account/password',{currentPassword:password,newPassword:currentPassword});}const e=await c('/auth/mfa/enroll',{currentPassword});await c('/auth/mfa/confirm',{enrollmentId:e.enrollmentId,code:totp(e.secret,at)});return e.secret;};
  const ownerSecret=await enrollStaff(owner);
  const proof=(secret=ownerSecret)=>{at+=30000;return {currentPassword:password,mfaCode:totp(secret,at)};};
  const classroom=(await owner('/org/dashboard')).classes[0];
  const publish=async()=>{const old=(await owner('/privacy/dashboard')).policy;return (await owner('/privacy/policies',{...notice(old?.id||null,old?'검증용 '+randomUUID():'검증용 1'),...proof()})).policy;};
  const register=async(suffix='1')=>owner('/roster',{registrationReference:'TEST-ENROLL-'+suffix,student:{name:'가상 학생'+suffix,username:'student'+suffix,password},parent:{name:'가상 보호자'+suffix,username:'parent'+suffix,password}});
  const verify=async(one,overrides={},expected=200)=>{const d=await owner('/privacy/dashboard');return (await owner('/privacy/verifications',{studentId:one.student.id,parentId:one.parent.id,method:'in_person',reference:'TEST-VERIFY-001',reason:'가상 자료 검증',confirmed:true,previousVerificationId:d.verifications.filter(v=>v.studentId===one.student.id&&!v.revokedAt).at(-1)?.id||null,...proof(),...overrides},expected)).verification;};
  const prepare=async()=>{const policy=await publish(),one=await register(),verification=await verify(one),parent=client(),student=client();await parent('/login',{username:'parent1',password});await parent('/account/password',{currentPassword:password,newPassword});return {policy,one,verification,parent,student};};
  const grant=(p,policy,id,overrides={},expected=200)=>p('/privacy/consents',{studentId:id,requestId:randomUUID(),policyId:policy.id,policyHash:policy.contentHash,required:true,optional:{test_optional:false},...overrides},expected);
  const assign=(id,expected=200)=>owner('/assignments',{studentIds:[id],opensAt:at-1000,closesAt:at+3600000},expected);
  return {owner,setup,classroom,client,publish,register,verify,prepare,grant,assign,close,enrollStaff,proof,now:()=>at,setTime:value=>{at=value;}};
}

test('default mode requires reviewed notice, registration reference, guardian verification and fresh guardian password',async t=>{
  const f=await fixture(t);
  await f.owner('/roster',{student:{name:'가상 학생',username:'student1',password}},409);
  const p=await f.publish();await f.owner('/roster',{student:{name:'가상 학생',username:'student1',password}},409);
  const one=await f.register();assert.equal(one.student.consentStatus,'verification_pending');assert.deepEqual(one.parent.childIds,[]);
  const student=f.client(),parent=f.client();await student('/login',{username:'student1',password},401);await f.assign(one.student.id,400);
  await parent('/login',{username:'parent1',password});await f.grant(parent,p,one.student.id,{},403);
  await f.verify(one);await f.grant(parent,p,one.student.id,{},409);
  await parent('/account/password',{currentPassword:password,newPassword});
  await f.grant(parent,p,one.student.id,{required:false},400);await f.grant(parent,p,one.student.id,{optional:{}},400);await f.grant(parent,p,one.student.id,{policyHash:'stale'},409);
  await f.grant(parent,p,one.student.id);const login=await student('/login',{username:'student1',password});assert.equal(login.user.consentStatus,'granted');
  assert.deepEqual((await parent('/session')).user.childIds,[one.student.id]);await f.assign(one.student.id);
  const access=await f.owner('/audit/query',{});assert.ok(access.entries.some(r=>r.route==='/privacy/consents'&&r.status===200&&r.subjects.includes(one.student.id)));
  const pd=await parent('/privacy/dashboard');assert.equal(pd.consents[0].optional.test_optional,false);assert.equal(pd.consents[0].policy.version,p.version);assert.equal(pd.verifications[0].reference,undefined);assert.equal(pd.policy.reviewReference,undefined);
  const anon=f.client(),publicData=await anon('/privacy/notice');assert.equal(publicData.policies[0].version,p.version);assert.equal(JSON.stringify(publicData).includes('TEST-REVIEW'),false);assert.equal(JSON.stringify(publicData).includes(one.student.name),false);
});

test('withdrawal revokes live child access, parent reports and exports; replay cannot reactivate; optional refusal permits learning',async t=>{
  const f=await fixture(t),{policy,one,parent,student}=await f.prepare();const requestId=randomUUID();
  const consent=await f.grant(parent,policy,one.student.id,{requestId});await f.grant(parent,policy,one.student.id,{requestId});assert.equal((await parent('/privacy/dashboard')).consents.length,1);
  await f.grant(parent,policy,one.student.id,{requestId,optional:{test_optional:true}},409);
  await student('/login',{username:'student1',password});const a=(await f.assign(one.student.id)).assignment,r=(await student(`/assignments/${a.id}/start`,{})).attempt;
  await student(`/attempts/${r.id}/submit`,{});await f.owner(`/assignments/${a.id}/release`,{});await f.owner(`/attempts/${r.id}/review`,{note:'가상 공개 의견',publish:true});
  assert.ok((await parent(`/attempts/${r.id}`)).report);assert.equal((await parent('/overview')).records.length,1);
  await parent('/privacy/withdraw',{studentId:one.student.id,requestId:randomUUID()});
  await student('/dashboard',undefined,401);await student('/login',{username:'student1',password},401);await parent(`/attempts/${r.id}`,undefined,404);
  assert.equal((await parent('/overview/export',{})).records,0);assert.deepEqual((await parent('/session')).user.childIds,[]);await f.assign(one.student.id,400);
  const duplicate=await f.grant(parent,policy,one.student.id,{requestId});assert.equal(duplicate.consentId,consent.consentId);await student('/login',{username:'student1',password},401);
  await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});assert.ok((await parent(`/attempts/${r.id}`)).report);
});

test('a new policy invalidates previous consent, keeps exact old notices and blocks reading assignment as well as exams',async t=>{
  const f=await fixture(t),{policy,one,parent,student}=await f.prepare();await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});
  const catalog=await f.owner('/learning/catalog'),l=await f.owner('/learning/catalog/'+catalog.lessons[0].id);await f.owner('/learning/approvals',{lessonId:l.lesson.id,contentHash:l.contentHash,note:'가상 자료 검증',pilot:true});
  const body={lessonId:l.lesson.id,studentIds:[one.student.id],level:'standard',dueAt:f.now()+3600000};
  const assignment=(await f.owner('/learning/assignments',body)).assignment,run=await student(`/learning/assignments/${assignment.id}/start`,{});
  const next=await f.publish();await student(`/learning/runs/${run.id}`,undefined,401);await f.owner('/learning/assignments',body,400);await f.assign(one.student.id,400);
  await f.grant(parent,policy,one.student.id,{},409);const d=await parent('/privacy/dashboard');assert.equal(d.students[0].consentStatus,'policy_changed');assert.equal(d.consents[0].policy.contentHash,policy.contentHash);assert.equal(d.policy.contentHash,next.contentHash);
  await f.owner('/privacy/policies',{...notice(policy.id,'stale write'),...f.proof()},409);
  await f.grant(parent,next,one.student.id);await student('/login',{username:'student1',password});assert.equal((await student(`/learning/runs/${run.id}`)).id,run.id);
});

test('guardian revocation, re-verification and expiry cannot inherit an old grant or be bypassed with account activation or old links API',async t=>{
  const f=await fixture(t),{policy,one,verification,parent,student}=await f.prepare();await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});
  await f.owner(`/privacy/verifications/${verification.id}/revoke`,{reason:'관계 재확인',...f.proof()});await student('/dashboard',undefined,401);
  await f.owner('/org/guardian-links',{parentId:one.parent.id,studentIds:[one.student.id],revision:0,reason:'우회 검사',...f.proof()},409);
  const profile=(await f.owner('/org/dashboard')).users.find(v=>v.id===one.student.id);await f.owner('/org/accounts/'+profile.id,{...profile,active:true,studentStatus:'enrolled',reason:'활성으로 동의 우회 검사'});
  await student('/login',{username:'student1',password},401);const next=await f.verify(one,{validUntil:f.now()+60000});await student('/login',{username:'student1',password},401);
  await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});f.setTime(f.now()+60000);await student('/dashboard',undefined,401);await f.grant(parent,policy,one.student.id,{},403);
  const another=await f.register('2');await f.verify(one,{parentId:another.parent.id});await f.grant(parent,policy,one.student.id,{},403);
  assert.notEqual(next.id,verification.id);
});

test('teacher and other guardian cannot forge verification or consent, and ordinary teacher sees only own class',async t=>{
  const f=await fixture(t),{policy,one,parent}=await f.prepare();
  const b=(await f.owner('/org/classes',{name:'가상 B반'})).class;await f.owner('/org/teachers',{name:'가상 다른반 교사',username:'teacher_b',password,classIds:[b.id],...f.proof()});const teacher=f.client();await teacher('/login',{username:'teacher_b',password});
  await f.enrollStaff(teacher);
  assert.deepEqual((await teacher('/privacy/dashboard')).students,[]);await teacher('/privacy/policies',notice(),403);await teacher('/privacy/verifications',{studentId:one.student.id,parentId:one.parent.id},403);await f.grant(teacher,policy,one.student.id,{},403);
  const two=await f.register('2'),other=f.client();await other('/login',{username:'parent2',password});await f.grant(other,policy,one.student.id,{},403);assert.deepEqual((await other('/privacy/dashboard')).students,[]);
  await f.verify(two);await f.verify(one,{parentId:two.parent.id},409);
  await f.grant(parent,policy,two.student.id,{},403);
  await teacher('/org/parents',{name:'가상 침입',username:'intruder_parent',password},403);
  await f.owner('/org/parents',{name:'가상 미근거 보호자',username:'no_reference',password},409);
  const later=(await f.owner('/org/parents',{name:'가상 나중 보호자',username:'later_parent',password,registrationReference:'TEST-PARENT-ENROLL',childIds:[one.student.id],isOwner:true})).user;
  assert.equal(later.role,'parent');assert.notEqual(later.isOwner,true);assert.equal(later.mustChangePassword,true);assert.deepEqual(later.childIds,[]);
});

test('consent and notices survive restart; production rejects a synthetic DB',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-consent-'));t.after(()=>rm(dir,{recursive:true,force:true}));const dbPath=join(dir,'test.sqlite');
  const f=await fixture(t,{dbPath}),{policy,one,parent}=await f.prepare();await f.grant(parent,policy,one.student.id);await f.close();
  const service=createExamService({dbPath,timer:false});service.close();const db=new DatabaseSync(dbPath);let state=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);assert.equal(state.privacy.consents.length,1);assert.equal(state.privacy.policies[0].contentHash,policy.contentHash);assert.equal(state.privacy.consents[0].optional.test_optional,false);db.close();
  const oldRuntime=process.env.READX_RUNTIME;process.env.READX_RUNTIME='production';try {
    assert.throws(()=>createExamService({dbPath:':memory:',privacyMode:'synthetic',timer:false}),/강제/);
    const syntheticPath=join(dir,'synthetic.sqlite');process.env.READX_RUNTIME='test';const synthetic=await fixture(t,{dbPath:syntheticPath,privacyMode:'synthetic'});await synthetic.close();process.env.READX_RUNTIME='production';assert.throws(()=>createExamService({dbPath:syntheticPath,timer:false}),/검증 DB/);
  }finally{if(oldRuntime===undefined)delete process.env.READX_RUNTIME;else process.env.READX_RUNTIME=oldRuntime;}
});

test('migration retains old guardian links as unverified candidates, never invents consent',()=>{
  const s=newState();s.users=[{id:'t',tenantId:'org',role:'teacher',className:'반',childIds:[]},{id:'s',tenantId:'org',role:'student',className:'반',childIds:[]},{id:'p',tenantId:'org',role:'parent',childIds:['s']}];
  upgradeOrganization(s,randomUUID,Date.now());assert.equal(s.organizations[0].privacyMode,'enforced');assert.equal(s.users[1].consentStatus,'verification_pending');assert.deepEqual(s.users[2].childIds,[]);assert.equal(s.privacy.candidates[0].studentId,'s');assert.deepEqual(s.privacy.consents,[]);
  upgradeOrganization(s,randomUUID,Date.now());assert.equal(s.privacy.candidates.length,1);
});

test('draft keys belong only to the authenticated account, stay outside roster views and rotate after withdrawal or password change',async t=>{
  const f=await fixture(t),{policy,one,parent,student}=await f.prepare(),anonymous=f.client();
  await anonymous('/account/device-key',{},401);await student('/login',{username:'student1',password},401);
  const ownerKey=await f.owner('/account/device-key',{userId:one.student.id});assert.equal(ownerKey.userId,f.setup.user.id);assert.equal(Buffer.from(ownerKey.key,'base64').length,32);
  await anonymous('/logout',{});await anonymous('/logout',{});assert.equal((await anonymous('/session')).user,null);
  assert.equal((await f.owner('/logout',{expectedUserId:one.student.id})).alreadyChanged,true);assert.equal((await f.owner('/session')).user.id,f.setup.user.id);
  assert.equal(JSON.stringify(await f.owner('/org/dashboard')).includes(ownerKey.key),false);assert.equal(JSON.stringify(await f.owner('/session')).includes(ownerKey.key),false);
  await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});const old=await student('/account/device-key',{});assert.equal(old.userId,one.student.id);assert.equal((await student('/account/device-key',{})).keyId,old.keyId);
  const parentKey=await parent('/account/device-key',{userId:one.student.id});assert.equal(parentKey.userId,one.parent.id);assert.notEqual(parentKey.key,old.key);
  await parent('/privacy/withdraw',{studentId:one.student.id,requestId:randomUUID()});await student('/account/device-key',{},401);
  await f.grant(parent,policy,one.student.id);await student('/login',{username:'student1',password});const fresh=await student('/account/device-key',{});assert.notEqual(fresh.key,old.key);
  await student('/account/password',{currentPassword:password,newPassword:'Draft-New-Password-2026!'});assert.notEqual((await student('/account/device-key',{})).key,fresh.key);
});

test('another tenant in the same database cannot read or change the first tenant guardian records',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-privacy-tenants-'));let f;t.after(async()=>{await f?.close();await rm(dir,{recursive:true,force:true});});const dbPath=join(dir,'test.sqlite');
  f=await fixture(t,{dbPath});const {policy,one,parent}=await f.prepare();await f.grant(parent,policy,one.student.id);
  const db=new DatabaseSync(dbPath),s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body),tenantId=randomUUID();
  const original=s.users.find(v=>v.id===f.setup.user.id),otherOwner={id:randomUUID(),tenantId,username:'other_owner',name:'가상 타기관 원장',password:original.password,role:'teacher',isOwner:true,classIds:[],className:'',childIds:[],active:true,revision:0};s.users.push(otherOwner);s.organizations.push({id:tenantId,name:'가상 별도 기관',privacyMode:'enforced',revision:0,createdAt:f.now()});db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));db.close();
  const foreign=f.client();await foreign('/login',{username:'other_owner',password});const foreignSecret=await f.enrollStaff(foreign);const data=await foreign('/privacy/dashboard');assert.deepEqual(data.consents,[]);assert.deepEqual(data.verifications,[]);assert.deepEqual(data.students,[]);assert.equal(data.policy,undefined);
  await foreign('/privacy/verifications',{studentId:one.student.id,parentId:one.parent.id,method:'in_person',reference:'forged',reason:'검사',confirmed:true,previousVerificationId:null,...f.proof(foreignSecret)},400);
  const verification=(await f.owner('/privacy/dashboard')).verifications[0];await foreign(`/privacy/verifications/${verification.id}/revoke`,{reason:'타기관 변경 시도',...f.proof(foreignSecret)},404);
  await foreign('/privacy/policies',{...notice(policy.id,'타기관 변경'),...f.proof(foreignSecret)},409);
  assert.deepEqual((await parent('/session')).user.childIds,[one.student.id]);assert.equal((await parent('/privacy/dashboard')).consents.length,1);
});
