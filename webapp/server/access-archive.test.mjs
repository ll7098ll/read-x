import test from 'node:test';
import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {spawnSync} from 'node:child_process';
import {fileURLToPath} from 'node:url';
import {DatabaseSync,backup} from 'node:sqlite';
import {createHash,randomBytes} from 'node:crypto';
import {mkdtemp,rm,readFile,writeFile,copyFile,access,mkdir} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createExamService} from './exam-service.mjs';
import {createAccessLog} from './access-log.mjs';
import {createAccessArchive,readAccessArchive,purgeAccessArchive} from './access-archive.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';
import {createEncryptedBackup,restoreEncryptedBackup} from './encrypted-backup.mjs';
import {maintainDatabase} from './recovery-maintenance.mjs';
import {acquireFileLease} from './maintenance-lock.mjs';
const ring=()=>({activeId:'test',keys:{test:randomBytes(32).toString('base64')}}),sha=b=>createHash('sha256').update(b).digest('hex');
const password='Archive-synthetic-2026!';
async function fixture(t){
 const dir=await mkdtemp(join(tmpdir(),'readx-access-archive-')),dbPath=join(dir,'source.sqlite'),keys={dataKeyring:ring(),mfaKeyring:ring(),auditKeyring:ring(),recoveryKeyring:ring(),backupKeyring:ring()};
 const service=createExamService({dbPath,...keys,timer:false,privacyMode:'synthetic'}),server=createServer(service.handler);await new Promise(r=>server.listen(0,'127.0.0.1',r));let closed=false;
 const close=async()=>{if(closed)return;closed=true;server.closeAllConnections();await new Promise(r=>server.close(r));service.close();};t.after(async()=>{await close();await rm(dir,{recursive:true,force:true});});
 let cookie='';const origin=`http://127.0.0.1:${server.address().port}`;
 const api=async(path,body)=>{const res=await fetch(origin+'/api/exam'+path,{method:body?'POST':'GET',headers:{Cookie:cookie,Origin:origin,'Content-Type':'application/json'},...(body?{body:JSON.stringify(body)}:{})});if(res.headers.get('set-cookie'))cookie=res.headers.get('set-cookie').split(';')[0];const value=await res.json();assert.equal(res.status,200,JSON.stringify(value));return value;};
 await api('/setup',{name:'Private Owner Name',username:'owner',password});await api('/roster',{student:{name:'Private Student Name',username:'student',password}});
 const options={dbPath,...keys,journalPath:dbPath+'.recovery.ndjson',reviewReference:'ARCHIVE-REVIEW-001',confirmed:true,expiresAt:Date.now()+86400000};
 const archive=(name='records.readxaudit')=>createAccessArchive({...options,outPath:join(dir,name)});
 const image=async name=>{const out=join(dir,name),db=new DatabaseSync(dbPath);try{await backup(db,out);}finally{db.close();}return out;};
 const head=()=>{const db=new DatabaseSync(dbPath);try{return createAccessLog({db,dbPath,keyring:keys.auditKeyring,readOnly:true}).checkpoint();}finally{db.close();}};
 return {dir,dbPath,keys,options,api,archive,image,head,close};
}

test('encrypted archive restores exact signed HTTP access history after an old database image',async t=>{
 const f=await fixture(t),old=await f.image('old.sqlite');await f.api('/dashboard');await f.api('/overview',{});const made=f.archive(),saved=readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring});
 assert.equal(made.offsiteStorageVerified,false);assert.equal(made.automaticScheduleConfigured,false);const bytes=await readFile(made.path);for(const secret of [password,'Private Student Name',f.keys.backupKeyring.keys.test,saved.rows.at(-1).body])assert.equal(bytes.includes(Buffer.from(secret)),false);
 const restored=maintainDatabase({...f.options,dbPath:old,action:'replay',auditAnchor:made.checkpoint,accessArchivePath:made.path,accessArchiveSha256:made.sha256});assert.equal(restored.accessArchive.imported,3);
 const db=new DatabaseSync(old);try{const log=createAccessLog({db,dbPath:old,keyring:f.keys.auditKeyring,readOnly:true});assert.ok(log.verify(made.checkpoint).ok);const rows=db.prepare('SELECT * FROM access_log WHERE seq<=? ORDER BY seq').all(saved.rows.length);assert.deepEqual(rows.map(r=>({...r})),saved.rows.map(r=>({...r})));const state=JSON.parse(db.prepare('SELECT body FROM exam_state WHERE id=1').get().body);assert.ok(state.users.every(u=>u.restoreCredentialHold));}finally{db.close();}
});

test('encrypted full-backup restore accepts a separate newer audit archive but cannot bypass missing history',async t=>{
 const f=await fixture(t),made=await createEncryptedBackup({...f.options,outPath:join(f.dir,'old.readxbackup'),expiresAt:Date.now()+86400000});await f.api('/dashboard');const history=f.archive();
 const restore=name=>({...f.options,archivePath:made.path,targetDbPath:join(f.dir,name),expectedSha256:made.sha256,auditAnchor:history.checkpoint});
 await assert.rejects(restoreEncryptedBackup(restore('without.sqlite')),/기준점보다/);await access(join(f.dir,'without.sqlite.restore.pending'));
 const result=await restoreEncryptedBackup({...restore('with.sqlite'),accessArchivePath:history.path,accessArchiveSha256:history.sha256});assert.equal(result.recovery.accessArchive.imported,3);assert.equal(result.oldCredentialsRevoked,true);assert.equal(result.guardianReverificationRequired,true);
});

test('modified, truncated, renamed and wrong-key archives fail authentication or custody hash checks',async t=>{
 const f=await fixture(t),made=f.archive(),bytes=await readFile(made.path),path=join(f.dir,'changed.readxaudit');
 const read=(expectedSha256=made.sha256,backupKeyring=f.keys.backupKeyring)=>readAccessArchive({archivePath:path,expectedSha256,backupKeyring});
 const changed=Buffer.from(bytes);changed[changed.length-20]^=1;await writeFile(path,changed);assert.throws(()=>read(),/해시/);assert.throws(()=>read(sha(changed)),/인증/);
 await writeFile(path,bytes.subarray(0,bytes.length-10));assert.throws(()=>read(sha(bytes.subarray(0,bytes.length-10))));await writeFile(path,bytes);assert.throws(()=>read(made.sha256,ring()));
 assert.throws(()=>readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring,now:made.expiresAt}),/보존기간/);
});

test('foreign database, stale archive and corrupted audit signing key keep restored databases quarantined',async t=>{
 const f=await fixture(t),old=await f.image('old.sqlite'),stale=f.archive();await f.api('/dashboard');const current=f.archive('current.readxaudit'),foreign=await fixture(t),other=foreign.archive();
 for(const [name,archive,anchor,key]of [['stale',stale,current.checkpoint,f.keys.auditKeyring],['foreign',other,current.checkpoint,f.keys.auditKeyring],['wrong-signing-key',current,current.checkpoint,ring()]]){
  const target=join(f.dir,name+'.sqlite');await copyFile(old,target);assert.throws(()=>maintainDatabase({...f.options,dbPath:target,action:'replay',auditAnchor:anchor,auditKeyring:key,accessArchivePath:archive.path,accessArchiveSha256:archive.sha256}));await access(target+'.restore.pending');
 }
 assert.throws(()=>maintainDatabase({...f.options,dbPath:old,action:'replay',accessArchivePath:current.path,accessArchiveSha256:current.sha256}),/별도 기준점/);
});

test('record/index tampering or a validly signed divergent prefix cannot replace local history',async t=>{
 const f=await fixture(t),old=await f.image('old.sqlite');await f.api('/dashboard');const made=f.archive(),saved=readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring}),db=new DatabaseSync(old);
 try{
  const log=createAccessLog({db,dbPath:old,keyring:f.keys.auditKeyring}),before=log.checkpoint();
  const damaged=structuredClone(saved.rows);damaged.at(-1).tenant_id='other';assert.throws(()=>log.mergeArchive(damaged,saved.checkpoint));assert.equal(log.checkpoint().seq,before.seq);
  const e=JSON.parse(saved.rows.at(-1).body);db.exec('BEGIN IMMEDIATE');log.append({...e,route:'local/signed-fork'});db.exec('COMMIT');log.committed();assert.throws(()=>log.mergeArchive(saved.rows,saved.checkpoint),/공통/);assert.equal(log.verify().count,before.seq+1);
 }finally{db.close();}
});

test('failed archive merge rolls back every imported row and index; repeat merge preserves originals',async t=>{
 const f=await fixture(t),old=await f.image('old.sqlite');await f.api('/dashboard');await f.api('/overview',{});const made=f.archive(),saved=readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring}),db=new DatabaseSync(old);
 try{
  const log=createAccessLog({db,dbPath:old,keyring:f.keys.auditKeyring}),before=log.checkpoint();db.exec(`CREATE TRIGGER block_archive BEFORE INSERT ON access_log WHEN NEW.seq=${before.seq+2} BEGIN SELECT RAISE(ABORT,'archive-test'); END;`);
  assert.throws(()=>log.mergeArchive(saved.rows,saved.checkpoint),/archive-test/);assert.equal(log.verify().count,before.seq);db.exec('DROP TRIGGER block_archive');assert.equal(log.mergeArchive(saved.rows,saved.checkpoint).imported,3);log.committed();assert.equal(log.mergeArchive(saved.rows,saved.checkpoint).imported,0);assert.ok(log.verify(made.checkpoint).ok);
 }finally{db.close();}
});

test('archives cannot overwrite custody files or export while database maintenance is active',async t=>{
 const f=await fixture(t),made=f.archive(),before=await readFile(made.path);assert.throws(()=>f.archive(),/덮어쓰지/);assert.deepEqual(await readFile(made.path),before);
 const release=acquireFileLease(f.dbPath+'.maintenance.lock','db-maintenance');try{assert.throws(()=>f.archive('locked.readxaudit'),e=>e.code==='MAINTENANCE_REQUIRED');}finally{release();}
 assert.throws(()=>createAccessArchive({...f.options,confirmed:false,outPath:join(f.dir,'unreviewed.readxaudit')}),/명시적/);
});

test('archives retain old signing/encryption key IDs across verified key rotation',async t=>{
 const f=await fixture(t),old=await f.image('old.sqlite'),first=f.archive();await f.close();
 f.keys.auditKeyring.keys.next=randomBytes(32).toString('base64');f.keys.auditKeyring.activeId='next';f.keys.backupKeyring.keys.next=randomBytes(32).toString('base64');f.keys.backupKeyring.activeId='next';
 const db=new DatabaseSync(f.dbPath);try{const log=createAccessLog({db,dbPath:f.dbPath,keyring:f.keys.auditKeyring});const e=JSON.parse(db.prepare('SELECT body FROM access_log ORDER BY seq DESC LIMIT 1').get().body);db.exec('BEGIN IMMEDIATE');log.append({...e,route:'local/key-rotation'});db.exec('COMMIT');log.committed();}finally{db.close();}
 assert.ok(readAccessArchive({archivePath:first.path,expectedSha256:first.sha256,backupKeyring:f.keys.backupKeyring}));const current=f.archive('rotated.readxaudit');assert.equal(maintainDatabase({...f.options,dbPath:old,action:'replay',accessArchivePath:current.path,accessArchiveSha256:current.sha256,auditAnchor:current.checkpoint}).accessArchive.imported,3);
 assert.throws(()=>readAccessArchive({archivePath:first.path,expectedSha256:first.sha256,backupKeyring:{activeId:'next',keys:{next:f.keys.backupKeyring.keys.next}}}),/이전 키/);
});

test('reviewed archive expiry blocks reuse and requires an explicit future retention date',async t=>{
 const f=await fixture(t),old=await f.image('expiry.sqlite'),made=f.archive();assert.throws(()=>readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring,now:made.expiresAt}),/보존기간/);
 assert.throws(()=>maintainDatabase({...f.options,dbPath:old,action:'replay',accessArchivePath:made.path,accessArchiveSha256:made.sha256,auditAnchor:made.checkpoint,now:made.expiresAt}),/보존기간/);await access(old+'.restore.pending');
 assert.throws(()=>createAccessArchive({...f.options,outPath:join(f.dir,'no-expiry.readxaudit'),expiresAt:undefined}),/종료일/);
 assert.throws(()=>createAccessArchive({...f.options,outPath:join(f.dir,'expired.readxaudit'),expiresAt:Date.now()-1000}),/종료일/);
 assert.throws(()=>readAccessArchive({archivePath:made.path,expectedSha256:made.sha256,backupKeyring:f.keys.backupKeyring,now:NaN}),/검토 시각/);
 assert.throws(()=>purgeAccessArchive({...f.options,archivePath:made.path,expectedSha256:made.sha256,holdsCleared:true,now:NaN}),/검토 시각/);
});

test('production archive CLI requires signed custody evidence and writes ciphertext with a usable receipt',async t=>{
 const f=await fixture(t),out=join(f.dir,'cli.readxaudit'),anchor=join(f.dir,'audit-anchor.json');await writeFile(anchor,JSON.stringify(f.head()));
 const env={...process.env,READX_RUNTIME:'production',READX_AUDIT_KEYS:JSON.stringify(f.keys.auditKeyring),READX_BACKUP_KEYS:JSON.stringify(f.keys.backupKeyring)},args=[fileURLToPath(new URL('./access-archive.mjs',import.meta.url)),'--db',f.dbPath,'--out',out,'--expires-at',new Date(f.options.expiresAt).toISOString(),'--review-reference','ARCHIVE-CLI-001','--confirmed'];
 const blocked=spawnSync(process.execPath,args,{env,encoding:'utf8'});assert.equal(blocked.status,1);await assert.rejects(access(out));
 const done=spawnSync(process.execPath,[...args,'--audit-anchor',anchor],{env,encoding:'utf8'});assert.equal(done.status,0,done.stderr);const receipt=JSON.parse(done.stdout);assert.equal(receipt.encrypted,true);assert.equal(readAccessArchive({archivePath:out,expectedSha256:receipt.sha256,backupKeyring:f.keys.backupKeyring}).checkpoint.signature,receipt.checkpoint.signature);
});

const purgeOptions=(f,made)=>({...f.options,archivePath:made.path,expectedSha256:made.sha256,holdsCleared:true,now:made.expiresAt});
const journalEvents=async f=>(await readFile(f.options.journalPath,'utf8')).trimEnd().split('\n').map(JSON.parse).slice(1).map(v=>v.event);

test('reviewed expiry purge removes the verified ciphertext with durable receipts and leaves live access records intact',async t=>{
 const f=await fixture(t),made=f.archive(),opts=purgeOptions(f,made),before=f.head();
 assert.throws(()=>purgeAccessArchive({...opts,holdsCleared:false}),/보존 예외/);assert.throws(()=>purgeAccessArchive({...opts,now:made.expiresAt-1}),/보존기간/);assert.throws(()=>purgeAccessArchive({...opts,expectedSha256:'0'.repeat(64)}),/해시/);assert.throws(()=>purgeAccessArchive({...opts,backupKeyring:ring()}));await access(made.path);
 const result=purgeAccessArchive(opts);assert.equal(result.fileAbsent,true);assert.equal(result.databaseAccessLogsPurged,false);assert.equal(result.mediaSanitizationCertified,false);assert.equal(result.otherCopiesDisposed,false);await assert.rejects(access(made.path));assert.equal(f.head().seq,before.seq+2);
 const events=await journalEvents(f);assert.deepEqual(events.map(e=>e.type),['access_archive_purge_prepared','access_archive_purged']);assert.equal(events[0].archiveId,made.archiveId);assert.equal(events[0].operationId,events[1].operationId);assert.equal(JSON.stringify(events).includes(made.path),false);assert.equal(JSON.stringify(events).includes(password),false);
 const again=purgeAccessArchive(opts);assert.equal(again.alreadyPurged,true);assert.equal(again.operationId,result.operationId);assert.equal(f.head().seq,before.seq+2);
});

test('renamed purged copies cannot bypass restore by choosing a time before expiry; raw and encrypted restore remain quarantined',async t=>{
 const f=await fixture(t),old=await f.image('before-archive-purge.sqlite'),backupFile=await createEncryptedBackup({...f.options,outPath:join(f.dir,'archive-revocation.readxbackup'),expiresAt:Date.now()+2*86400000}),made=f.archive(),renamed=join(f.dir,'renamed.readxaudit');await copyFile(made.path,renamed);purgeAccessArchive(purgeOptions(f,made));
 const common={...f.options,now:made.createdAt,auditAnchor:made.checkpoint,accessArchivePath:renamed,accessArchiveSha256:made.sha256};
 assert.throws(()=>maintainDatabase({...common,dbPath:old,action:'replay'}),/파기 대상으로/);await access(old+'.restore.pending');
 const target=join(f.dir,'encrypted-revoked.sqlite');await assert.rejects(restoreEncryptedBackup({...common,archivePath:backupFile.path,targetDbPath:target,expectedSha256:backupFile.sha256}),/파기 대상으로/);await access(target+'.restore.pending');await assert.rejects(access(target));
 // Replaying newer receipts without using the disposed archive stays compatible.
 const valid=await f.image('without-disposed-archive.sqlite');assert.equal(maintainDatabase({...f.options,dbPath:valid,action:'replay'}).ok,true);
});

test('a journal delivery failure cannot unlink the archive and retry syncs the committed preparation only once',async t=>{
 const f=await fixture(t),made=f.archive(),opts=purgeOptions(f,made);assert.throws(()=>purgeAccessArchive({...opts,beforeJournalAppend:()=>{throw Error('synthetic journal delivery outage');}}),e=>e.code==='RECOVERY_SYNC_REQUIRED');await access(made.path);assert.equal((await journalEvents(f)).length,0);
 const db=new DatabaseSync(f.dbPath);assert.equal(db.prepare('SELECT COUNT(*) n FROM recovery_events').get().n,1);db.close();
 assert.equal(purgeAccessArchive(opts).fileAbsent,true);assert.deepEqual((await journalEvents(f)).map(e=>e.type),['access_archive_purge_prepared','access_archive_purged']);
});

test('failure after unlink resumes from durable preparation without inventing a missing-file receipt',async t=>{
 const f=await fixture(t),made=f.archive(),opts=purgeOptions(f,made),db=new DatabaseSync(f.dbPath);
 try{db.exec("CREATE TRIGGER block_purge_receipt BEFORE INSERT ON access_log WHEN json_extract(NEW.body,'$.route')='local/access-archive.file-unlinked' BEGIN SELECT RAISE(ABORT,'synthetic receipt outage'); END;");assert.throws(()=>purgeAccessArchive(opts),/synthetic receipt outage/);await assert.rejects(access(made.path));assert.deepEqual((await journalEvents(f)).map(e=>e.type),['access_archive_purge_prepared']);db.exec('DROP TRIGGER block_purge_receipt');assert.equal(purgeAccessArchive(opts).recoveryReceiptRecorded,true);assert.equal((await journalEvents(f)).length,2);}finally{db.close();}
 const missing=join(f.dir,'never-verified.readxaudit');assert.throws(()=>purgeAccessArchive({...opts,archivePath:missing}),/준비 기록/);
});

test('audit commit failure rolls back purge preparation and preserves the original archive',async t=>{
 const f=await fixture(t),made=f.archive(),opts=purgeOptions(f,made),db=new DatabaseSync(f.dbPath);
 try{db.exec("CREATE TRIGGER block_purge_prepare BEFORE INSERT ON access_log WHEN json_extract(NEW.body,'$.route')='local/access-archive.purge-prepared' BEGIN SELECT RAISE(ABORT,'synthetic prepare outage'); END;");assert.throws(()=>purgeAccessArchive(opts),/synthetic prepare outage/);await access(made.path);assert.equal(db.prepare('SELECT COUNT(*) n FROM recovery_events').get().n,0);assert.equal((await journalEvents(f)).length,0);db.exec('DROP TRIGGER block_purge_prepare');assert.equal(purgeAccessArchive(opts).fileAbsent,true);}finally{db.close();}
});

test('reappearing identical copies get a new removal operation while their archive ID remains revoked',async t=>{
 const f=await fixture(t),made=f.archive(),opts=purgeOptions(f,made),bytes=await readFile(made.path),first=purgeAccessArchive(opts);await writeFile(made.path,bytes);const second=purgeAccessArchive(opts);assert.notEqual(second.operationId,first.operationId);assert.equal(second.archiveId,first.archiveId);await assert.rejects(access(made.path));assert.equal((await journalEvents(f)).length,4);
});

test('foreign archives, missing signing keys and damaged journals cannot authorize file removal',async t=>{
 const f=await fixture(t),other=await fixture(t),made=f.archive(),foreign=other.archive(),opts=purgeOptions(f,made);
 assert.throws(()=>purgeAccessArchive({...opts,archivePath:foreign.path,expectedSha256:foreign.sha256,backupKeyring:other.keys.backupKeyring}));await access(foreign.path);
 assert.throws(()=>purgeAccessArchive({...opts,auditKeyring:ring()}));assert.throws(()=>purgeAccessArchive({...opts,recoveryKeyring:ring()}));
 const original=await readFile(f.options.journalPath);await writeFile(f.options.journalPath,original.subarray(0,original.length-1));assert.throws(()=>purgeAccessArchive(opts));await access(made.path);await writeFile(f.options.journalPath,original);
});

test('production purge CLI enforces exception review and separate signed anchors before unlink',async t=>{
 const f=await fixture(t),now=Date.now(),made=createAccessArchive({...f.options,outPath:join(f.dir,'expired-cli.readxaudit'),now:now-120000,expiresAt:now-60000}),folder=join(f.dir,'independent');await mkdir(folder);const journalPath=join(folder,'erasure.ndjson');await copyFile(f.options.journalPath,journalPath);
 const db=new DatabaseSync(f.dbPath);let anchor;try{anchor=createRecoveryJournal({db,dbPath:f.dbPath,journalPath,keyring:f.keys.recoveryKeyring}).checkpoint();}finally{db.close();}
 const anchorFile=join(folder,'recovery-anchor.json'),auditFile=join(folder,'audit-anchor.json');await writeFile(anchorFile,JSON.stringify(anchor));await writeFile(auditFile,JSON.stringify(f.head()));
 const env={...process.env,READX_RUNTIME:'production',READX_AUDIT_KEYS:JSON.stringify(f.keys.auditKeyring),READX_BACKUP_KEYS:JSON.stringify(f.keys.backupKeyring),READX_RECOVERY_KEYS:JSON.stringify(f.keys.recoveryKeyring)},args=[fileURLToPath(new URL('./access-archive.mjs',import.meta.url)),'--action','purge','--db',f.dbPath,'--archive',made.path,'--expected-sha256',made.sha256,'--journal',journalPath,'--review-reference','ARCHIVE-PURGE-CLI-001','--confirmed'];
 assert.equal(spawnSync(process.execPath,args,{env,encoding:'utf8'}).status,1);assert.equal(spawnSync(process.execPath,[...args,'--holds-cleared'],{env,encoding:'utf8'}).status,1);await access(made.path);
 const done=spawnSync(process.execPath,[...args,'--holds-cleared','--anchor',anchorFile,'--audit-anchor',auditFile],{env,encoding:'utf8'});assert.equal(done.status,0,done.stderr);assert.equal(JSON.parse(done.stdout).fileAbsent,true);await assert.rejects(access(made.path));
});
