import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {DatabaseSync} from 'node:sqlite';
import {randomBytes,randomUUID} from 'node:crypto';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createExamService} from './exam-service.mjs';
import {createPrivacyVault} from './privacy-vault.mjs';
import {buildRightsBundle,bundleHash,redactBundle} from './rights-bundle.mjs';
import {totp} from './totp.mjs';
const password='Rights-synthetic-2026!',ring=()=>({activeId:'test',keys:{test:randomBytes(32).toString('base64')}});
async function fixture(t){
 const dir=await mkdtemp(join(tmpdir(),'readx-rights-')),dbPath=join(dir,'test.sqlite'),dataKeyring=ring(),mfaKeyring=ring();let at=Date.now(),service,server,origin,closed=true;
 const open=async()=>{service=createExamService({dbPath,dataKeyring,mfaKeyring,privacyMode:'synthetic',timer:false,now:()=>at});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));origin=`http://127.0.0.1:${server.address().port}`;closed=false;};
 const close=async()=>{if(closed)return;closed=true;server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};t.after(async()=>{await close();await rm(dir,{recursive:true,force:true});});await open();
 const client=()=>{let cookie='';return async(path,body,expected=200)=>{const res=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];const d=await res.json();assert.equal(res.status,expected,path+': '+JSON.stringify(d));return d;};};
 const owner=client(),setup=await owner('/setup',{name:'가상 원장',username:'owner',password}),roster=await owner('/roster',{student:{name:'요청 대상 가상 학생',username:'student',password},parent:{name:'요청 가상 보호자',username:'parent',password}}),other=await owner('/roster',{student:{name:'다른 학생 비공개',username:'other',password}});
 const parent=client(),student=client();await parent('/login',{username:'parent',password});await student('/login',{username:'student',password});
 const state=fn=>{const db=new DatabaseSync(dbPath),s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);if(fn){fn(s,db);db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));}db.close();return s;};
 const create=async(type='access',extra={})=>(await parent('/rights/requests',{requestId:randomUUID(),subjectId:roster.student.id,type,details:'PRIVATE-RIGHTS-DETAIL: 본인 기록 확인 요청',scopes:['profile','consultations'],currentPassword:password,...extra})).request;
 const action=async(r,path,body={},expected=200)=>(await owner(`/rights/requests/${r.id}/${path}`,{revision:r.revision,mutationId:randomUUID(),currentPassword:password,...body},expected)).request;
 const verify=r=>action(r,'verify',{method:'in_person',reference:'IDENTITY-001',confirmed:true});
 const preview=(r,scopes=r.scopes)=>owner(`/rights/requests/${r.id}/preview`,{scopes,currentPassword:password});
 const provide=async(r,extra={})=>{const p=await preview(r);return action(r,'resolve',{outcome:'provide',scopes:r.scopes,sourceHash:p.sourceHash,redactions:[],response:'검토한 본인 기록을 제공합니다.',reviewReference:'REVIEW-001',reviewed:true,...extra});};
 return {owner,parent,student,client,create,action,verify,preview,provide,roster,other,setup,state,dbPath,dir,dataKeyring,close,restart:async()=>{await close();await open();},now:()=>at,advance:ms=>{at+=ms;}};
}

test('reviewed access bundle is encrypted, redacted, frozen across changes and restart, and delivered only after fresh authentication',async t=>{
 const f=await fixture(t);f.state(s=>s.consultations.push({id:randomUUID(),tenantId:f.roster.student.tenantId,studentId:f.roster.student.id,note:'PRIVATE-NOTE: 제3자 이름이 들어간 가상 상담'}));let r=await f.verify(await f.create());const p=await f.preview(r),path=p.redactableFields.find(p=>p.path.endsWith('/note')).path;
 await f.action(r,'resolve',{outcome:'provide',scopes:r.scopes,sourceHash:p.sourceHash,redactions:[path],response:'일부 문구 제외',reviewReference:'REVIEW-001',reviewed:true},400);
 r=await f.action(r,'resolve',{outcome:'provide',scopes:r.scopes,sourceHash:p.sourceHash,redactions:[path],omissionReference:'REDACTION-001',response:'본인 기록 제공',reviewReference:'REVIEW-001',reviewed:true});assert.equal(r.status,'provided');
 await f.parent(`/rights/requests/${r.id}/download`,{},400);const file=await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password});assert.equal(file.hash,bundleHash(JSON.parse(file.json)));assert.ok(file.json.includes('[별도 검토로 제외]'));assert.equal(file.json.includes('PRIVATE-NOTE'),false);assert.equal(file.json.includes(f.other.student.name),false);assert.equal(file.json.includes('password'),false);
 f.state(s=>{s.users.find(u=>u.id===f.roster.student.id).name='사본 제공 후 바뀐 이름';});await f.restart();assert.equal((await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password})).json,file.json);
 const db=new DatabaseSync(f.dbPath),raw=JSON.stringify([db.prepare('SELECT * FROM privacy_requests').all(),db.prepare('SELECT * FROM privacy_request_bundles').all()]),logs=JSON.stringify(db.prepare('SELECT body FROM access_log').all());db.close();assert.equal(raw.includes('PRIVATE-RIGHTS-DETAIL'),false);assert.equal(raw.includes('PRIVATE-NOTE'),false);assert.equal(logs.includes('PRIVATE-RIGHTS-DETAIL'),false);assert.equal(logs.includes(password),false);
});

test('review snapshots detect concurrent changes and stale revisions; callbacks cannot finalize deletion or restriction without real action',async t=>{
 const f=await fixture(t);let r=await f.verify(await f.create());const p=await f.preview(r);f.state(s=>{s.users.find(u=>u.id===f.roster.student.id).name='동시 변경';});await f.action(r,'resolve',{outcome:'provide',scopes:r.scopes,sourceHash:p.sourceHash,redactions:[],response:'제공',reviewReference:'REVIEW-001',reviewed:true},409);
 for(const kind of ['deletion','restriction']){let q=await f.verify(await f.create(kind));await f.action(q,'resolve',{outcome:'deleted',response:'완료라고 위장',reviewReference:'REVIEW-001',reviewed:true},409);q=await f.action(q,'resolve',{outcome:'needs_action',response:'보존 근거와 실제 조치 검토 중',reviewReference:'REVIEW-001',reviewed:true});assert.equal(q.status,'action_required');assert.ok(f.state().users.find(u=>u.id===f.roster.student.id).active);}
});

test('withdrawal of learning access does not remove verified rights; guardian revocation blocks pending and published request data',async t=>{
 const f=await fixture(t);f.state(s=>{s.privacy.verifications.push({id:'verified-guardian',tenantId:f.roster.student.tenantId,studentId:f.roster.student.id,parentId:f.roster.parent.id,at:f.now(),method:'in_person'});s.users.find(u=>u.id===f.roster.parent.id).childIds=[];});
 let r=await f.verify(await f.create());r=await f.provide(r);assert.ok((await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password})).json);
 f.state(s=>{s.privacy.verifications[0].revokedAt=f.now();});await f.parent(`/rights/requests/${r.id}`,undefined,404);await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password},404);assert.equal((await f.parent('/rights/requests')).requests.length,0);await f.owner(`/rights/requests/${r.id}/preview`,{scopes:r.scopes,currentPassword:password},409);
});

test('ordinary teacher and another guardian cannot process or view requests, and offline intake requires documented identity',async t=>{
 const f=await fixture(t),r=await f.create(),classId=f.state().classes[0].id;await f.owner('/org/teachers',{name:'일반 교사',username:'teacher',password,classIds:[classId]});const teacher=f.client();await teacher('/login',{username:'teacher',password});await teacher(`/rights/requests/${r.id}`,undefined,404);
 const second=f.client();await f.owner('/org/parents',{name:'다른 보호자',username:'parent2',password});await second('/login',{username:'parent2',password});await second('/rights/requests',undefined,409);await second('/account/password',{currentPassword:password,newPassword:password+'Own'});await second('/rights/requests',{requestId:randomUUID(),type:'access',subjectId:f.roster.student.id,scopes:['profile'],details:'우회 시도',currentPassword:password+'Own'},403);
 const base={requestId:randomUUID(),type:'deletion',subjectId:f.other.student.id,details:'외부 접수',origin:'offline',currentPassword:password};await f.owner('/rights/requests',base,400);assert.equal((await f.owner('/rights/requests',{...base,intakeReference:'PAPER-001',identityChecked:true})).request.origin,'offline');
});

test('approved name correction changes the actual profile, revokes prior sessions and preserves history; appeals and retries are durable',async t=>{
 const f=await fixture(t),body={requestId:randomUUID(),type:'correction',subjectId:f.roster.student.id,details:'표시 이름 정정',correction:{field:'profile.name',value:'정정한 이름'},currentPassword:password};const first=await f.parent('/rights/requests',body),retry=await f.parent('/rights/requests',body);assert.equal(first.request.id,retry.request.id);await f.parent('/rights/requests',{...body,details:'변경 재전송'},409);
 let r=await f.verify(first.request);const mutation={revision:r.revision,mutationId:randomUUID(),outcome:'apply_name',nameBeforeHash:r.nameBeforeHash,response:'현재 계정 표시 이름 반영',reviewReference:'CORRECTION-001',reviewed:true,currentPassword:password};r=(await f.owner(`/rights/requests/${r.id}/resolve`,mutation)).request;assert.equal(r.status,'corrected');assert.equal(f.state().users.find(u=>u.id===f.roster.student.id).name,'정정한 이름');await f.student('/dashboard',undefined,401);
 const again=(await f.owner(`/rights/requests/${r.id}/resolve`,mutation)).request;assert.equal(again.history.length,r.history.length);
 await f.owner(`/rights/requests/${r.id}/appeal`,{revision:r.revision,mutationId:randomUUID(),message:'계정 본인이 아님',currentPassword:password},403);
 r=(await f.parent(`/rights/requests/${r.id}/appeal`,{revision:r.revision,mutationId:randomUUID(),message:'추가 확인 요청',currentPassword:password})).request;assert.equal(r.status,'submitted');await f.restart();assert.equal((await f.parent(`/rights/requests/${r.id}`)).request.history.length,r.history.length);
});

test('MFA is mandatory for enrolled owners to verify, preview and release; failed confirmation counts persist',async t=>{
 const f=await fixture(t),r=await f.create(),e=await f.owner('/auth/mfa/enroll',{currentPassword:password});await f.owner('/auth/mfa/confirm',{enrollmentId:e.enrollmentId,code:totp(e.secret,f.now())});
 await f.action(r,'verify',{method:'in_person',reference:'IDENTITY-001',confirmed:true},400);f.advance(30000);const verified=await f.action(r,'verify',{method:'in_person',reference:'IDENTITY-001',confirmed:true,mfaCode:totp(e.secret,f.now())});assert.equal(verified.status,'verified');
 await f.owner(`/rights/requests/${r.id}/preview`,{scopes:['profile'],currentPassword:password},400);await f.restart();assert.equal(f.state().users.find(u=>u.id===f.setup.user.id).mfaFailures.count,1);
});

test('vault rejects wrong account context, ciphertext changes, missing keys and supports old-key reads during rotation',()=>{
 const keys=ring(),c={tenantId:'academy',id:'request'},vault=createPrivacyVault({dbPath:':memory:',keyring:keys}),secret={details:'보호할 요청'},record=vault.seal(secret,c);assert.equal(JSON.stringify(record).includes(secret.details),false);assert.deepEqual(vault.open(record,c),secret);assert.throws(()=>vault.open(record,{...c,id:'another'}));assert.throws(()=>vault.open({...record,ciphertext:'AAAA'},c));const next=createPrivacyVault({dbPath:':memory:',keyring:{activeId:'next',keys:{...keys.keys,next:randomBytes(32).toString('base64')}}});assert.deepEqual(next.open(record,c),secret);assert.equal(next.seal(secret,c).keyId,'next');assert.throws(()=>createPrivacyVault({dbPath:':memory:',keyring:ring()}).open(record,c));
 const original=process.env.READX_DATA_KEYS;delete process.env.READX_DATA_KEYS;try{assert.throws(()=>createPrivacyVault({dbPath:':memory:',production:true}),/READX_DATA_KEYS/);}finally{if(original!==undefined)process.env.READX_DATA_KEYS=original;}
 assert.throws(()=>redactBundle({profile:{id:'immutable',name:'내 이름'}},['/profile/id']));assert.throws(()=>redactBundle({profile:{}},['/profile/__proto__/name']));
});

test('bundle excludes credential keys, other students and private course question banks',async t=>{
 const f=await fixture(t),s=f.state(),subject=s.users.find(u=>u.id===f.roster.student.id),db=new DatabaseSync(f.dbPath);db.prepare('INSERT INTO learning_courses VALUES(?,?,?)').run(subject.tenantId+':'+subject.id,subject.tenantId,JSON.stringify({studentId:subject.id,history:[],plan:{id:'plan',checkBank:[{answer:'PRIVATE-ANSWER-KEY'}],training:[],checks:[{id:'check',content:{answer:'PRIVATE-ANSWER-KEY'},answer:{reason:'본인 설명'},review:{by:'OTHER-STAFF',note:'검토 의견'}}]}}));const bundle=JSON.stringify(buildRightsBundle({db,state:s,subject,scopes:['profile','course']}));db.close();assert.equal(bundle.includes(subject.password),false);assert.equal(bundle.includes('PRIVATE-ANSWER-KEY'),false);assert.equal(bundle.includes('OTHER-STAFF'),false);assert.equal(bundle.includes(f.other.student.name),false);assert.ok(bundle.includes('본인 설명'));
});

test('expired snapshots stop delivery and old requests remain reachable through sequence pagination',async t=>{
 const f=await fixture(t);let first=await f.verify(await f.create());first=await f.provide(first);for(let i=0;i<51;i++)await f.create('deletion');
 const page=await f.parent('/rights/requests');assert.equal(page.requests.length,50);assert.ok(page.nextBeforeSeq);const older=await f.parent('/rights/query',{beforeSeq:page.nextBeforeSeq,tenantId:'ignored'});assert.equal(older.requests.length,2);assert.ok(older.requests.some(r=>r.id===first.id));assert.ok(older.requests.every(r=>!page.requests.some(p=>p.id===r.id)));
 f.advance(7*86400000+1);await f.parent('/login',{username:'parent',password});await f.parent(`/rights/requests/${first.id}/download`,{currentPassword:password},410);assert.equal((await f.parent(`/rights/requests/${first.id}`)).request.bundle.available,false);
});

test('cross-tenant owners cannot query or reassign another institution rights requests',async t=>{
 const f=await fixture(t),r=await f.create();f.state(s=>{s.users.push({id:'separate-owner',tenantId:'separate',name:'별도 원장',username:'separate',password:s.users[0].password,role:'teacher',isOwner:true,active:true,childIds:[],classIds:[],revision:0});s.organizations.push({id:'separate',name:'별도 학원',privacyMode:'synthetic',revision:0});});const other=f.client();await other('/login',{username:'separate',password});await other(`/rights/requests/${r.id}`,undefined,404);assert.equal((await other('/rights/query',{tenantId:f.roster.student.tenantId})).requests.length,0);await other('/rights/requests',{requestId:randomUUID(),type:'access',subjectId:f.roster.student.id,scopes:['profile'],details:'다른 기관 접근',origin:'offline',identityChecked:true,intakeReference:'PAPER-001',currentPassword:password},404);
});

test('cipher index tampering and missing data keys fail closed instead of producing an unprotected replacement',async t=>{
 const f=await fixture(t),r=await f.create(),db=new DatabaseSync(f.dbPath),old=db.prepare('SELECT client_key FROM privacy_requests WHERE id=?').get(r.id).client_key;db.prepare('UPDATE privacy_requests SET client_key=? WHERE id=?').run('tampered',r.id);await f.owner(`/rights/requests/${r.id}`,undefined,500);db.prepare('UPDATE privacy_requests SET client_key=? WHERE id=?').run(old,r.id);db.close();await f.close();assert.throws(()=>createExamService({dbPath:f.dbPath,dataKeyring:ring(),privacyMode:'synthetic',timer:false}),/복호화/);await f.restart();assert.equal((await f.parent(`/rights/requests/${r.id}`)).request.id,r.id);
});

test('audit storage failure cannot commit a rights request or return a successful receipt',async t=>{
 const f=await fixture(t),db=new DatabaseSync(f.dbPath);db.exec("CREATE TRIGGER block_rights_audit BEFORE INSERT ON access_log BEGIN SELECT RAISE(ABORT,'synthetic audit outage'); END");await f.parent('/rights/requests',{requestId:randomUUID(),type:'access',subjectId:f.roster.student.id,scopes:['profile'],details:'실패하면 접수되면 안 됨',currentPassword:password},500);assert.equal(db.prepare('SELECT COUNT(*) n FROM privacy_requests').get().n,0);db.exec('DROP TRIGGER block_rights_audit');db.close();
});

test('revoked account links can use documented offline delivery without restoring the guardian account relationship',async t=>{
 const f=await fixture(t);let r=await f.create();await f.owner('/org/guardian-links',{parentId:f.roster.parent.id,studentIds:[],revision:f.state().users.find(u=>u.id===f.roster.parent.id).revision,reason:'가상 연결 해제'});await f.parent('/login',{username:'parent',password});await f.parent(`/rights/requests/${r.id}`,undefined,404);
 r=await f.action(r,'verify',{method:'signed_document',reference:'OFFLINE-IDENTITY-001',confirmed:true,offlineOnly:true});assert.equal(r.verification.offlineOnly,true);r=await f.provide(r);const file=await f.owner(`/rights/requests/${r.id}/download`,{currentPassword:password,purpose:'data_subject_request',reference:'RIGHTS-001'});assert.ok(file.json.includes(f.roster.student.name));assert.deepEqual(f.state().users.find(u=>u.id===f.roster.parent.id).childIds,[]);await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password},404);
});

test('encrypted inline snapshot migration preserves the exact approved copy and metadata queries do not decrypt snapshot bodies',async t=>{
 const f=await fixture(t);let r=await f.verify(await f.create());r=await f.provide(r);const original=await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password});await f.close();const db=new DatabaseSync(f.dbPath),vault=createPrivacyVault({dbPath:f.dbPath,keyring:f.dataKeyring}),row=db.prepare('SELECT * FROM privacy_requests WHERE id=?').get(r.id),stored=vault.open(JSON.parse(row.payload),{tenantId:row.tenant_id,id:r.id}),snapshot=db.prepare('SELECT * FROM privacy_request_bundles WHERE request_id=?').get(r.id);stored.bundle.data=vault.open(JSON.parse(snapshot.payload),{tenantId:row.tenant_id,id:r.id+':bundle:'+snapshot.version});delete stored.bundle.version;db.prepare('UPDATE privacy_requests SET payload=? WHERE id=?').run(JSON.stringify(vault.seal(stored,{tenantId:row.tenant_id,id:r.id})),r.id);db.prepare('DELETE FROM privacy_request_bundles WHERE request_id=?').run(r.id);db.close();await f.restart();assert.equal((await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password})).json,original.json);
 const corrupt=new DatabaseSync(f.dbPath),saved=corrupt.prepare('SELECT payload FROM privacy_request_bundles WHERE request_id=?').get(r.id).payload;corrupt.prepare('UPDATE privacy_request_bundles SET payload=? WHERE request_id=?').run('{}',r.id);assert.ok((await f.parent('/rights/requests')).requests.some(v=>v.id===r.id));await f.parent(`/rights/requests/${r.id}/download`,{currentPassword:password},500);corrupt.prepare('UPDATE privacy_request_bundles SET payload=? WHERE request_id=?').run(saved,r.id);corrupt.close();
});
