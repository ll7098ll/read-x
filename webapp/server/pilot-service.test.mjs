import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {randomUUID} from 'node:crypto';
import {mkdtempSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createServer} from 'node:http';
import {createLearningService} from './learning-service.mjs';
import {createExamService} from './exam-service.mjs';
import {pilotRows,itemStatistics,wilson} from './pilot-statistics.mjs';
import {buildRightsBundle} from './rights-bundle.mjs';
const checks={difficulty:true,answer:true,evidence:true,explanation:true};
function fixture(t){
 const db=new DatabaseSync(':memory:'),service=createLearningService({db,randomUUID});t.after(()=>db.close());let at=Date.UTC(2026,10,17);
 const teacher={id:'teacher',tenantId:'academy',role:'teacher',classIds:['class-a']},students=Array.from({length:25},(_,n)=>({id:'student-'+n,tenantId:'academy',role:'student',classId:'class-a',name:'가상 학생 '+n,consentStatus:'synthetic'})),state={users:[teacher,...students],audit:[],classes:[{id:'class-a',tenantId:'academy',active:true}]};
 const call=(user,suffix='',body)=>service.route({user,state,path:'/learning/pilot'+suffix,method:body===undefined?'GET':'POST',body:body||{},at});
 const inspect=key=>call(teacher,'/item',{itemKey:key}),key='check:g3:evidence:0';
 const approve=(k=key)=>{const d=inspect(k);return call(teacher,'/review',{itemKey:k,contentHash:d.item.contentHash,revision:d.review?.revision||0,status:'approved',checks,note:'교사가 본문과 정답·근거·설명을 직접 대조했습니다.'});};
 const create=(ids=students.map(s=>s.id),keys=[key])=>{const d=call(teacher,'/create',{name:'가상 수업 파일럿',itemKeys:keys,studentIds:ids,mutationId:randomUUID()});return call(teacher).learners.filter(r=>r.sessionId===d.sessionId);};
 const observe=(r,k=key,extra={})=>{const current=call(teacher,'/run',{runId:r.id}).run;return call(teacher,'/observe',{runId:r.id,itemKey:k,revision:current.revision,assistance:'independent',priorExposure:'new',rubric:'success',note:'학생의 실제 수행을 관찰했습니다.',...extra}).run;};
 const complete=(s,id,k=key,{correct=true,timed=true,support='independent',omit=false}={})=>{
  let r=call(s,'/start',{runId:id}).run;const i=inspect(k).item,lease=randomUUID();call(s,'/pulse',{runId:id,itemKey:k,lease,active:true});
  if(timed){at+=7000;call(s,'/pulse',{runId:id,itemKey:k,lease,active:false});}
  r=call(s,'/answer',{runId:id,itemKey:k,revision:r.revision,answer:{choice:correct?i.question.answer:(i.question.answer+1)%i.question.options.length,text:'본문 단서를 근거로 판단했습니다.',evidence:i.question.evidence,omitted:omit,support}}).run;
  return call(s,'/submit',{runId:id,revision:r.revision}).run;
 };
 return {db,service,teacher,students,state,call,inspect,key,approve,create,observe,complete,tick:ms=>{at+=ms;}};
}

test('460 versioned pilot items require a concrete teacher review; assignment is idempotent and student snapshots omit keys',t=>{
 const f=fixture(t),d=f.call(f.teacher);assert.equal(d.catalog.length,460);
 assert.throws(()=>f.create([f.students[0].id]),/교사 검수/);
 const i=f.inspect(f.key).item;
 assert.throws(()=>f.call(f.teacher,'/review',{itemKey:f.key,contentHash:i.contentHash,revision:0,status:'approved',checks:{answer:true},note:'정답만 확인했습니다.'}),/난이도/);
 f.approve();const body={name:'하나의 수업',itemKeys:[f.key],studentIds:[f.students[0].id],mutationId:randomUUID()},created=f.call(f.teacher,'/create',body);
 assert.equal(f.call(f.teacher,'/create',body).sessionId,created.sessionId);assert.throws(()=>f.call(f.teacher,'/create',{...body,name:'다른 수업'}),/중복 배정/);
 const row=f.call(f.teacher).learners[0],r=f.call(f.students[0],'/start',{runId:row.runId}).run;
 assert.equal(r.items[0].key,f.key);for(const k of ['answer','question','contentHash','explanation','teacherReview','pilotCalibration'])assert.equal(k in r.items[0],false,k);
 assert.equal('observations'in r,false);assert.equal('exposure'in r,false);
 assert.throws(()=>f.call(f.students[1],'/start',{runId:row.runId}),/담당 재원/);
 assert.throws(()=>f.call(f.students[0],'/item',{itemKey:f.key}),/교사 권한/);
});

test('active heartbeat timing excludes background, long disconnects and a competing browser lease',t=>{
 const f=fixture(t);f.approve();const row=f.create([f.students[0].id])[0],s=f.students[0],id=row.runId,a=randomUUID(),b=randomUUID();f.call(s,'/start',{runId:id});
 const pulse=(lease,active)=>f.call(s,'/pulse',{runId:id,itemKey:f.key,lease,active});pulse(a,true);f.tick(5000);assert.equal(pulse(a,true).times[f.key],5000);
 f.tick(1000);assert.equal(pulse(b,true).leaseBusy,true);f.tick(5000);assert.equal(pulse(a,false).times[f.key],11000);
 f.tick(60000);assert.equal(pulse(a,true).times[f.key],11000);f.tick(40000);assert.equal(pulse(a,true).times[f.key],11000);f.tick(3000);assert.equal(pulse(a,false).times[f.key],14000);
});

test('first independent students drive a sample-bound calibration; help, unknown, repeat and new content versions stay separate',t=>{
 const f=fixture(t);f.approve();const learners=f.create();
 for(let n=0;n<23;n++){const row=learners.find(r=>r.studentId===f.students[n].id),r=f.complete(f.students[n],row.runId,f.key,{correct:n<16,support:n===20?'prompted':'independent'});if(n!==21)f.observe(r,f.key,n===22?{priorExposure:'repeat'}:{});}
 let d=f.inspect(f.key),s=d.statistics;assert.equal(s.independentN,20);assert.equal(s.correct,16);assert.equal(s.p,.8);assert.equal(s.suggestedBand,'입문');assert.ok(s.interval[0]<.8&&s.interval[1]>.8);assert.equal(s.assisted,1);assert.equal(s.unknownHelp,1);assert.equal(s.repeat,1);assert.equal(s.medianActiveMs,7000);
 assert.throws(()=>f.call(f.teacher,'/calibrate',{itemKey:f.key,datasetHash:'stale',revision:0,note:'확인',confirmed:true}),/최신 분석/);
 const body={itemKey:f.key,datasetHash:s.datasetHash,revision:0,note:'첫 독립 수행 20명, 정답률 구간과 학급 특성을 검토했습니다.',confirmed:true};f.call(f.teacher,'/calibrate',body);assert.equal(f.inspect(f.key).calibration.current,true);
 const next=f.create([f.students[24].id])[0],snapshot=f.db.prepare('SELECT body FROM pilot_runs WHERE id=?').get('academy:'+next.runId);assert.equal(JSON.parse(snapshot.body).items[0].pilotCalibration.n,20);assert.equal(f.inspect(f.key).calibration.current,true,'assigning an unstarted run does not invalidate evidence');
 const r=f.call(f.teacher,'/run',{runId:learners[0].runId}).run;f.observe(r,f.key,{observedMs:10000,note:'초시계 관찰값으로 보완했습니다.'});assert.equal(f.inspect(f.key).calibration.current,false);assert.throws(()=>f.call(f.teacher,'/calibrate',{...body,revision:1}),/최신 분석/);
 const rows=pilotRows([r]);assert.equal(itemStatistics({...d.item,contentHash:'different-version'},rows).independentN,0);
});

test('help and repeat history cannot be promoted by re-review or successful retry; submitted responses stay immutable',t=>{
 const f=fixture(t);f.approve();let row=f.create([f.students[0].id])[0],r=f.complete(f.students[0],row.runId,f.key,{correct:false,support:'prompted'});
 f.observe(r,f.key,{assistance:'read_aloud'});f.observe(r,f.key,{assistance:'unknown'});f.observe(r,f.key,{assistance:'independent'});assert.equal(f.inspect(f.key).statistics.independentN,0);
 assert.equal(f.call(f.teacher,'/run',{runId:r.id}).run.observations[f.key].assistance,'read_aloud');
 assert.throws(()=>f.call(f.students[0],'/answer',{runId:r.id,itemKey:f.key,revision:r.revision,answer:{choice:0,text:'정답으로 변경',evidence:[0],support:'independent',omitted:false}}),/진행 중/);
 row=f.create([f.students[0].id])[0];r=f.complete(f.students[0],row.runId);f.observe(r);const d=f.inspect(f.key);assert.equal(d.statistics.firstStudents,1);assert.equal(d.statistics.independentN,0);assert.equal(d.statistics.attempts,2);
});

test('omission, not reached, missing time and teacher-scored explanation are distinct, including small sample blocking',t=>{
 const f=fixture(t),open='diagnostic:g1:support:explain-0';f.approve(open);const common=f.call(f.teacher).catalog.find(i=>i.grade===1&&i.branch==='common').key;f.approve(common);
 const keys=[open,common];
 const row=f.create([f.students[0].id],keys)[0];let r=f.call(f.students[0],'/start',{runId:row.runId}).run;
 r=f.call(f.students[0],'/answer',{runId:r.id,itemKey:open,revision:r.revision,answer:{choice:null,text:'고양이가 가방 옆에 있어서요.',evidence:[0],support:'independent',omitted:false}}).run;
 r=f.call(f.students[0],'/submit',{runId:r.id,revision:r.revision}).run;
 assert.equal(f.inspect(open).statistics.independentN,0);f.observe(r,open);const stats=f.inspect(open).statistics;assert.equal(stats.independentN,1);assert.equal(stats.correct,1);assert.equal(stats.medianActiveMs,null);assert.equal(stats.suggestedBand,null);
 assert.throws(()=>f.call(f.teacher,'/calibrate',{itemKey:open,datasetHash:stats.datasetHash,revision:0,note:'한 명을 보고 승인',confirmed:true}),/20명/);
 const learner=f.call(f.teacher).learners[0];assert.equal(learner.choiceAccuracy,null);assert.equal(learner.notReached,1);assert.equal(learner.openSuccess,1);
});

test('authorized scope, processing restrictions and self-service copies include observations without answer keys',t=>{
 const f=fixture(t);f.approve();const row=f.create([f.students[0].id])[0],r=f.complete(f.students[0],row.runId);f.observe(r);
 const stranger={...f.teacher,id:'other-teacher',classIds:['another-class']};f.state.users.push(stranger);
 assert.equal(f.call(stranger).learners.length,0);assert.throws(()=>f.call(stranger,'/run',{runId:r.id}),/담당 재원/);
 const otherTenant={...f.teacher,id:'other-tenant',tenantId:'another-academy'};assert.throws(()=>f.call(otherTenant,'/run',{runId:r.id}),/찾을 수/);
 const copy=buildRightsBundle({db:f.db,state:f.state,subject:f.students[0],scopes:['pilot']}),serialized=JSON.stringify(copy);assert.ok(serialized.includes('학생의 실제 수행'));assert.equal(serialized.includes('question'),false);assert.equal(serialized.includes('teacherReview'),false);assert.equal(serialized.includes('teacherId'),false);
 f.students[0].processingRestriction={id:'restricted'};assert.equal(f.call(f.teacher).learners.length,0);assert.equal(f.call(f.teacher,'/export',{}).observations.length,0);assert.throws(()=>f.call(f.teacher,'/run',{runId:r.id}),/담당 재원/);
});

test('an omitted answer is incorrect despite a positive explanation review, while unknown exposure is excluded',t=>{
 const f=fixture(t);f.approve();let row=f.create([f.students[0].id])[0],r=f.complete(f.students[0],row.runId,f.key,{omit:true});f.observe(r);
 let s=f.inspect(f.key).statistics;assert.equal(s.independentN,1);assert.equal(s.correct,0);assert.equal(s.omitted,1);assert.equal(s.p,0);
 row=f.create([f.students[1].id])[0];r=f.complete(f.students[1],row.runId);f.observe(r,f.key,{priorExposure:'unknown'});s=f.inspect(f.key).statistics;assert.equal(s.independentN,1);assert.equal(s.unknownExposure,1);
 f.observe(r,f.key,{priorExposure:'new',rubric:'unscorable',note:'질문에 오류가 있어 분석에서 제외합니다.'});s=f.inspect(f.key).statistics;assert.equal(s.independentN,1);assert.equal(s.unscorable,1);
});

test('presented pilot diagnostic material is flagged when the regular placement begins',t=>{
 const f=fixture(t),k=f.call(f.teacher).catalog.find(i=>i.grade===1&&i.branch==='common').key;f.approve(k);
 const row=f.create([f.students[0].id],[k])[0];f.complete(f.students[0],row.runId,k);
 const p=f.service.route({user:f.students[0],state:f.state,path:'/learning/placement/start',method:'POST',body:{grade:1},at:Date.UTC(2026,10,18)}).placement;
 assert.equal(p.priorPilotExposure.families.length,1);assert.match(p.priorPilotExposure.families[0],/diagnostic:g1:/);
});

test('lower-grade oral answers need actual teacher transcription before joining independent calibration',t=>{
 const f=fixture(t),key='diagnostic:g1:support:explain-0';f.approve(key);const row=f.create([f.students[0].id],[key])[0];
 let r=f.call(f.students[0],'/start',{runId:row.runId}).run;
 r=f.call(f.students[0],'/answer',{runId:r.id,itemKey:key,revision:r.revision,answer:{choice:null,text:'',evidence:[0],omitted:false,support:'independent',responseMode:'oral_requested'}}).run;
 r=f.call(f.students[0],'/submit',{runId:r.id,revision:r.revision}).run;
 assert.throws(()=>f.observe(r,key),/실제로 말한/);assert.equal(f.inspect(key).statistics.independentN,0);
 f.observe(r,key,{transcript:'글의 낱말을 보고 그렇게 생각했어요.'});assert.equal(f.inspect(key).statistics.independentN,1);assert.equal(f.inspect(key).statistics.correct,1);
});

test('legacy placement answers without a stored form still exclude a previously read passage from new pilot samples',t=>{
 const f=fixture(t),key=f.call(f.teacher).catalog.find(i=>i.grade===1&&i.branch==='common').key,i=f.inspect(key).item;f.approve(key);
 f.db.prepare('INSERT INTO learning_placements VALUES(?,?,?)').run('academy:'+f.students[0].id,'academy',JSON.stringify({id:f.students[0].id,studentId:f.students[0].id,grade:1,version:'g16-placement-2',branch:null,answers:{[i.question.id]:{choice:0}}}));
 const row=f.create([f.students[0].id],[key])[0],r=f.complete(f.students[0],row.runId,key);f.observe(r,key);assert.equal(f.inspect(key).statistics.independentN,0);assert.equal(f.inspect(key).statistics.repeat,1);
});

test('Wilson intervals behave at zero/all correct rather than implying exact certainty',()=>{
 assert.equal(wilson(0,0),null);assert.ok(Math.abs(wilson(0,20)[0])<1e-10);assert.ok(wilson(0,20)[1]>.16);assert.ok(wilson(20,20)[0]<.84);assert.ok(wilson(20,20)[1]<=1);
});

test('HTTP pilot routes enforce roles, durable restart and audited export purpose',async t=>{
 const dir=mkdtempSync(join(tmpdir(),'readx-pilot-')),dbPath=join(dir,'test.sqlite');let service,server,origin,cookie='';
 const boot=async()=>{service=createExamService({dbPath,privacyMode:'synthetic',timer:false});server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));origin=`http://127.0.0.1:${server.address().port}`;};
 const stop=async()=>{server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};await boot();t.after(async()=>{await stop();rmSync(dir,{recursive:true,force:true});});
 const call=async(path,body,status=200)=>{const res=await fetch(origin+'/api/exam'+path,{method:body===undefined?'GET':'POST',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body===undefined?{}:{body:JSON.stringify(body)})});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];const d=await res.json();assert.equal(res.status,status,JSON.stringify(d));return d;};
 const password='Synthetic-pilot-2026!';await call('/setup',{username:'pilot-teacher',name:'가상 교사',password});const first=(await call('/learning/pilot')).catalog[0],d=await call('/learning/pilot/item',{itemKey:first.key});
 await call('/learning/pilot/review',{itemKey:first.key,contentHash:first.contentHash,revision:0,status:'approved',checks,note:'실제 검수 기록을 저장했습니다.'});
 await call('/learning/pilot/export',{},400);await call('/learning/pilot/export',{purpose:'teaching'});
 await stop();await boot();await call('/login',{username:'pilot-teacher',password});assert.equal((await call('/learning/pilot/item',{itemKey:first.key})).review.status,'approved');
 const db=new DatabaseSync(dbPath),logs=db.prepare('SELECT body FROM access_log').all().map(r=>JSON.parse(r.body));db.close();assert.ok(logs.some(l=>l.route==='/learning/pilot/export'&&l.status===200&&l.purpose==='teaching'));assert.ok(logs.some(l=>l.route==='/learning/pilot/review'&&l.status===200));assert.equal(JSON.stringify(logs).includes(d.item.question.explanation),false);
});
