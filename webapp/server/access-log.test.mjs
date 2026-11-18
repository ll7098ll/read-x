import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {randomBytes} from 'node:crypto';
import {createServer} from 'node:http';
import {mkdtemp,rm,writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {execFileSync} from 'node:child_process';
import {createExamService} from './exam-service.mjs';
import {createAccessLog} from './access-log.mjs';
import {accessAddress,trustedProxies,collectSubjects,accessOperation} from './access-context.mjs';
import {auditSigner} from './audit-keys.mjs';
const password='Access-log-synthetic-2026!',ring=()=>({activeId:'test',keys:{test:randomBytes(32).toString('base64')}});
async function fixture(t,options={}){
 const dir=await mkdtemp(join(tmpdir(),'readx-access-')),dbPath=join(dir,'test.sqlite'),auditKeyring=ring();let service,server,origin,closed=true;
 const open=async()=>{service=createExamService({dbPath,timer:false,privacyMode:'synthetic',auditKeyring,...options});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));origin=`http://127.0.0.1:${server.address().port}`;closed=false;};
 const close=async()=>{if(closed)return;closed=true;server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};t.after(async()=>{await close();await rm(dir,{recursive:true,force:true});});await open();
 const client=()=>{let cookie='';return async(path,body,expected=200,headers={})=>{const r=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,'Content-Type':'application/json',Origin:origin,...headers},...(body===undefined?{}:{body:JSON.stringify(body)})});if(r.headers.get('set-cookie'))cookie=r.headers.get('set-cookie').split(';')[0];const d=await r.json();assert.equal(r.status,expected,path+': '+JSON.stringify(d));return d;};};
 const owner=client(),setup=await owner('/setup',{name:'가상 운영자',username:'owner',password});const state=()=>{const db=new DatabaseSync(dbPath),s=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);db.close();return s;};
 const entries=()=>{const db=new DatabaseSync(dbPath),rows=db.prepare('SELECT seq,body FROM access_log ORDER BY seq').all().map(r=>({seq:r.seq,...JSON.parse(r.body)}));db.close();return rows;};
 return {owner,setup,client,state,entries,dbPath,dir,auditKeyring,close,restart:async()=>{await close();await open();}};
}

test('HTTP reads, writes, failed access and downloads commit minimal metadata without credentials or answers',async t=>{
 const f=await fixture(t),roster=await f.owner('/roster',{student:{name:'가상 원생',username:'student',password},parent:{name:'가상 보호자',username:'parent',password}});await f.owner('/dashboard',undefined,200,{'X-Forwarded-For':'198.51.100.99'});
 await f.owner('/overview',{});await f.owner('/overview/export',{},400);await f.owner('/overview/export',{purpose:'teaching'});
 const student=f.client();await student('/login',{username:'student',password});await student('/org/dashboard',undefined,403);await student('/audit/query',{},403);
 const rows=f.entries(),download=rows.find(r=>r.route==='/overview/export'&&r.status===200);assert.equal(download.purpose,'teaching');assert.equal(download.records,0);assert.ok(rows.some(r=>r.category==='write'&&r.route==='/roster'&&r.subjects.includes(roster.student.id)));assert.ok(rows.some(r=>r.route==='/org/dashboard'&&r.status===403));
 assert.equal(rows.find(r=>r.route==='/dashboard').address,'127.0.0.1');assert.equal(JSON.stringify(rows).includes(password),false);assert.equal(JSON.stringify(rows).includes('가상 원생'),false);assert.equal(JSON.stringify(rows).includes('readx_exam='),false);
 const read=await f.owner('/overview',{});assert.equal('csv'in read,false);await f.restart();assert.equal((await f.owner('/audit/check',{})).integrity.ok,true);
});

test('current guardian release is rechecked for export and print; attempt review is attributed to the student',async t=>{
 const f=await fixture(t),roster=await f.owner('/roster',{student:{name:'가상 원생',username:'student',password},parent:{name:'가상 보호자',username:'parent',password}}),student=f.client(),parent=f.client();await student('/login',{username:'student',password});await parent('/login',{username:'parent',password});
 const now=Date.now(),a=(await f.owner('/assignments',{studentIds:[roster.student.id],opensAt:now-10000,closesAt:now+3600000})).assignment,attempt=(await student(`/assignments/${a.id}/start`,{})).attempt;await student(`/attempts/${attempt.id}/submit`,{});await f.owner(`/assignments/${a.id}/release`,{});await f.owner(`/attempts/${attempt.id}/review`,{note:'가상 지도 의견',publish:true});
 assert.ok((await parent(`/attempts/${attempt.id}/print`,{})).report);await f.owner(`/attempts/${attempt.id}/review`,{note:'비공개 의견',revoke:true});await parent(`/attempts/${attempt.id}/print`,{},404);
 assert.ok(f.entries().find(r=>r.route==='/attempts/:id/review'&&r.subjects.includes(roster.student.id)));assert.ok(f.entries().some(r=>r.category==='print'&&r.actorId===roster.parent.id&&r.status===404));assert.equal(JSON.stringify(f.entries()).includes('가상 지도 의견'),false);
});

test('logging failure rolls back the underlying operation and cannot return private data',async t=>{
 const f=await fixture(t),before=f.state().organizations[0],db=new DatabaseSync(f.dbPath);db.exec("CREATE TRIGGER fail_access BEFORE INSERT ON access_log BEGIN SELECT RAISE(ABORT,'test unavailable'); END;");
 await f.owner('/org/settings',{name:'저장되면 안 되는 변경',revision:before.revision},500);assert.equal(f.state().organizations[0].name,before.name);await f.owner('/dashboard',undefined,500);db.exec('DROP TRIGGER fail_access');db.close();assert.ok((await f.owner('/dashboard')).user);
});

test('owner queries, stable pages, export limits and immutable review references obey account scope',async t=>{
 const f=await fixture(t),classId=f.state().classes[0].id;await f.owner('/org/teachers',{name:'가상 일반 교사',username:'teacher',password,classIds:[classId]});const teacher=f.client();await teacher('/login',{username:'teacher',password});await teacher('/audit/query',{},403);
 for(let i=0;i<103;i++)await f.owner('/dashboard');const page=await f.owner('/audit/query',{});assert.equal(page.entries.length,100);assert.ok(page.nextBeforeSeq);const next=await f.owner('/audit/query',{beforeSeq:page.nextBeforeSeq});assert.ok(next.entries.every(r=>r.seq<page.nextBeforeSeq));
 await f.owner('/audit/reviews',{fromSeq:1,toSeq:page.entries[0].seq,finding:'clear',reference:'REVIEW-001'});assert.equal(f.entries().at(-1).review.reference,'REVIEW-001');
 const file=await f.owner('/audit/export',{purpose:'incident_review',reference:'CASE-001'});assert.equal(JSON.parse(file.json).entries.length,file.records);await f.owner('/audit/export',{purpose:'incident_review'},400);await f.owner('/audit/query',{startDate:'2026-02-30'},400);
});

test('HMAC chain rejects mutations, forged indexes, key loss and rollback against an external checkpoint',()=>{
 const db=new DatabaseSync(':memory:'),keys=ring(),log=createAccessLog({db,dbPath:':memory:',keyring:keys}),event={tenantId:'tenant',at:Date.now(),category:'read',status:200,actorId:'actor',subjects:['student']};
 const append=()=>{db.exec('BEGIN');log.append(event);db.exec('COMMIT');log.committed();};append();const cp=log.checkpoint();append();assert.equal(log.verify(cp).count,2);assert.throws(()=>db.exec('DELETE FROM access_log WHERE seq=2'),/append only/);assert.throws(()=>db.exec("UPDATE access_log SET status=500 WHERE seq=1"),/append only/);
 db.exec('BEGIN');db.prepare('INSERT INTO access_log_subjects VALUES(?,?,?)').run(1,'wrong-tenant','forged');assert.throws(()=>log.verify(),/색인/);db.exec('ROLLBACK');
 const rotated={activeId:'next',keys:{...keys.keys,next:randomBytes(32).toString('base64')}};assert.equal(createAccessLog({db,dbPath:':memory:',keyring:rotated}).verify(cp).ok,true);assert.throws(()=>createAccessLog({db,dbPath:':memory:',keyring:ring()}));
 db.exec('DROP TRIGGER access_log_no_delete; DROP TRIGGER access_subject_no_delete; DELETE FROM access_log_subjects; DELETE FROM access_log;');assert.throws(()=>createAccessLog({db,dbPath:':memory:',keyring:keys}).verify(cp),/기준점/);db.close();
 const missing=process.env.READX_AUDIT_KEYS;delete process.env.READX_AUDIT_KEYS;try{assert.throws(()=>auditSigner({dbPath:':memory:',production:true}),/READX_AUDIT_KEYS/);}finally{if(missing!==undefined)process.env.READX_AUDIT_KEYS=missing;}
});

test('read-only CLI validates a separately stored checkpoint and detects altered record bodies',async t=>{
 const f=await fixture(t);await f.owner('/dashboard');const cp=(await f.owner('/audit/checkpoint',{purpose:'operations_review'})).checkpoint,path=join(f.dir,'checkpoint.json');await writeFile(path,JSON.stringify(cp));await f.close();
 const env={...process.env,READX_AUDIT_KEYS:JSON.stringify(f.auditKeyring)},args=['server/verify-access-log.mjs','--db',f.dbPath,'--checkpoint',path];assert.equal(JSON.parse(execFileSync(process.execPath,args,{encoding:'utf8',stdio:'pipe',env})).externalCheckpoint,true);
 const db=new DatabaseSync(f.dbPath);db.exec('DROP TRIGGER access_log_no_update');db.prepare('UPDATE access_log SET body=? WHERE seq=1').run('{}');db.close();assert.throws(()=>execFileSync(process.execPath,args,{stdio:'pipe',env}));
});

test('trusted proxy resolution ignores spoofed prefixes and invalid data; metadata never records raw URLs',()=>{
 const req=(peer,xff)=>({socket:{remoteAddress:peer},headers:{'x-forwarded-for':xff}}),trusted=trustedProxies('127.0.0.1,10.0.0.2');assert.equal(accessAddress(req('127.0.0.1','198.51.100.42'),new Set()).address,'127.0.0.1');assert.equal(accessAddress(req('127.0.0.1','1.2.3.4,198.51.100.42,10.0.0.2'),trusted).address,'198.51.100.42');assert.equal(accessAddress(req('127.0.0.1','password:secret'),trusted).source,'invalid-forwarding');assert.equal(accessAddress({headers:{}}).address,null);assert.throws(()=>trustedProxies('*'));
 assert.equal(accessOperation('/unknown/password-secret?token=private','GET').route,'unknown');assert.deepEqual(collectSubjects({studentId:'foreign',data:{id:'own',writing:'do not log'}},{users:[{id:'own',tenantId:'academy'},{id:'foreign',tenantId:'elsewhere'}]},'academy'),['own']);
});

test('tenant filters cannot select another academy and unsuccessful login is not attributed to an authenticated actor',async t=>{
 const f=await fixture(t),db=new DatabaseSync(f.dbPath),s=f.state(),otherId='other-owner',tenantId='other-academy';s.users.push({id:otherId,tenantId,name:'다른 가상 운영자',username:'other_owner',password:s.users[0].password,role:'teacher',isOwner:true,active:true,revision:0,childIds:[],classIds:[]});s.organizations.push({id:tenantId,name:'다른 가상 기관',privacyMode:'synthetic',revision:0});db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));db.close();
 const other=f.client();await other('/login',{username:'other_owner',password});const result=await other('/audit/query',{tenantId:f.setup.user.tenantId});assert.ok(result.entries.every(e=>e.tenantId===tenantId));assert.equal(JSON.stringify(result).includes(f.setup.user.id),false);
 const anonymous=f.client();await anonymous('/login',{username:'owner',password:'wrong'},401);const denied=f.entries().at(-1);assert.equal(denied.tenantId,f.setup.user.tenantId);assert.equal(denied.actorId,null);assert.equal(denied.actorRole,'anonymous');
});

test('a second organization cannot query or export the first organization records by changing filters',async t=>{
 const f=await fixture(t),db=new DatabaseSync(f.dbPath),s=f.state(),first=s.users[0];s.users.push({id:'separate-owner',tenantId:'separate-academy',name:'별도 가상 운영자',username:'separate',password:first.password,role:'teacher',isOwner:true,active:true,childIds:[],classIds:['separate-class'],revision:0});s.organizations.push({id:'separate-academy',name:'별도 가상 학원',privacyMode:'synthetic',revision:0});s.classes.push({id:'separate-class',tenantId:'separate-academy',name:'별도 반',active:true,revision:0});db.prepare('UPDATE exam_state SET body=? WHERE id=1').run(JSON.stringify(s));db.close();
 const other=f.client();await other('/login',{username:'separate',password});await other('/dashboard');const own=await other('/audit/query',{tenantId:first.tenantId});assert.ok(own.entries.length);assert.ok(own.entries.every(r=>r.tenantId==='separate-academy'));assert.equal(JSON.stringify(own.accounts).includes(first.id),false);
 const attempts=await other('/audit/query',{tenantId:first.tenantId,actorId:first.id,subjectId:first.id});assert.equal(attempts.entries.length,0);const exported=await other('/audit/export',{tenantId:first.tenantId,purpose:'operations_review'});assert.ok(JSON.parse(exported.json).entries.every(r=>r.tenantId==='separate-academy'));
});
