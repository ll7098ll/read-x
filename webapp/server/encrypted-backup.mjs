import {DatabaseSync,backup} from 'node:sqlite';
import {createHash,randomUUID,randomBytes} from 'node:crypto';
import {createReadStream,createWriteStream,existsSync,openSync,readSync,writeFileSync,readFileSync,fsyncSync,closeSync,mkdtempSync,lstatSync,statSync,linkSync,unlinkSync,rmdirSync,readdirSync,constants} from 'node:fs';
import {resolve,dirname,join,basename,sep} from 'node:path';
import {fileURLToPath} from 'node:url';
import {Writable} from 'node:stream';
import {pipeline} from 'node:stream/promises';
import {backupCrypto} from './backup-crypto.mjs';
import {createAccessLog} from './access-log.mjs';
import {createRecoveryJournal} from './recovery-journal.mjs';
import {maintainDatabase} from './recovery-maintenance.mjs';
import {canonicalFile,assertPlainFile,assertNotMaintaining,acquireFileLease} from './maintenance-lock.mjs';
const magic=Buffer.from('READX-BACKUP-1\n'),maxBytes=16*1024*1024*1024;
const ref=v=>typeof v==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(v);
const fail=message=>{throw Error(message);};
async function digestFile(path){const digest=createHash('sha256');for await(const bytes of createReadStream(path))digest.update(bytes);return digest.digest('hex');}
function privatePath(path){const file=canonicalFile(path),app=resolve(fileURLToPath(new URL('..',import.meta.url))),lower=v=>process.platform==='win32'?v.toLowerCase():v;if(lower(file).startsWith(lower(app+sep))&&!lower(file).startsWith(lower(join(app,'.exam-data')+sep)))fail('백업·복원 원본을 공개 웹앱 소스·산출물 디렉터리에 두지 마세요.');return file;}
function fresh(path){assertPlainFile(path);if(existsSync(path))fail('기존 파일을 덮어쓰지 않습니다. 새 백업·복원 경로를 선택해 주세요.');}
function stageIn(parent){const dir=mkdtempSync(join(parent,'.readx-backup-stage-')),nonce=randomUUID();writeFileSync(join(dir,'stage.json'),JSON.stringify({v:1,kind:'readx-backup-stage',nonce}),{flag:'wx',mode:0o600});return {dir,nonce,file:join(dir,'backup.sqlite')};}
function removeOwnStage(stage){
 const dir=resolve(stage.dir);if(!basename(dir).startsWith('.readx-backup-stage-')||!lstatSync(dir).isDirectory()||lstatSync(dir).isSymbolicLink())fail('임시 복구 디렉터리의 경계를 확인할 수 없습니다.');
 const meta=JSON.parse(readFileSync(join(dir,'stage.json'),'utf8'));if(meta.kind!=='readx-backup-stage'||meta.nonce!==stage.nonce)fail('임시 복구 디렉터리 소유권이 바뀌었습니다.');
 const allowed=new Set(['stage.json','backup.sqlite','backup.sqlite-wal','backup.sqlite-shm','backup.sqlite.restore.pending']);for(const name of readdirSync(dir))if(!allowed.has(name))fail('알 수 없는 파일이 있는 복구 디렉터리는 자동 제거하지 않습니다.');
 for(const name of readdirSync(dir)){const path=join(dir,name);assertPlainFile(path);unlinkSync(path);}rmdirSync(dir);
}
function flush(path){const fd=openSync(path,'r+');try{fsyncSync(fd);}finally{closeSync(fd);}}
function checkedImage(path,{auditKeyring,auditCheckpoint,databaseId,journalHead}){
 const db=new DatabaseSync(path,{readOnly:true});try{
  const rows=db.prepare('PRAGMA integrity_check').all();if(rows.length!==1||Object.values(rows[0])[0]!=='ok')fail('백업 SQLite 무결성이 일치하지 않습니다.');
  const access=createAccessLog({db,dbPath:path,keyring:auditKeyring,readOnly:true}),verified=access.verify(auditCheckpoint);if(databaseId!==db.prepare('SELECT database_id FROM access_log_identity WHERE id=1').get()?.database_id||verified.head.seq!==auditCheckpoint.seq||verified.head.hash!==auditCheckpoint.hash)fail('백업의 DB·접속기록 기준점이 다릅니다.');
  const r=db.prepare('SELECT * FROM recovery_state WHERE id=1').get();if(r.seq!==journalHead.seq||r.hash!==journalHead.hash||r.database_id!==databaseId)fail('백업의 삭제 원장 기준점이 다릅니다.');
 }finally{db.close();}
}
function localEvent(access,at,action,reviewReference,backupId,status){access.append({requestId:randomUUID(),tenantId:'system',at,actorId:'local-server-admin',actorRole:'server-administrator',method:'LOCAL',route:'local/'+action,resourceId:backupId,category:'audit',status,bytes:0,address:null,addressSource:'local-server',subjects:[],records:0,review:{reference:reviewReference,backupId}});}
export async function createEncryptedBackup({dbPath,outPath,journalPath,backupKeyring,recoveryKeyring,auditKeyring,reviewReference,confirmed=false,expiresAt,now=Date.now()}){
 if(!Number.isSafeInteger(expiresAt)||expiresAt<=now||expiresAt>8640000000000000)fail('실제 검토한 미래 백업 보존 종료일이 필요합니다.');
 if(!ref(reviewReference)||confirmed!==true)fail('실제 백업 보관·복구 검토 문서와 명시적 확인이 필요합니다.');
 const file=privatePath(dbPath),out=privatePath(outPath);assertPlainFile(file);if(!existsSync(file))fail('기존 DB가 필요합니다.');assertNotMaintaining(file);fresh(out);
 const crypt=backupCrypto({dbPath:file,keyring:backupKeyring}),release=acquireFileLease(file+'.maintenance.lock','db-maintenance'),stage=stageIn(dirname(file)),partial=out+'.partial-'+randomUUID();let db;
 try{
  db=new DatabaseSync(file);for(const name of ['exam_state','access_log_identity','recovery_state'])if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(name))fail('검증된 삭제 원장과 프로젝트 DB가 필요합니다.');db.exec('PRAGMA busy_timeout=5000; BEGIN IMMEDIATE; COMMIT');const access=createAccessLog({db,dbPath:file,keyring:auditKeyring}),journal=createRecoveryJournal({db,dbPath:file,journalPath,keyring:recoveryKeyring,initialize:false}),journalHead=journal.sync(),backupId=randomUUID();
  db.exec('BEGIN IMMEDIATE');localEvent(access,now,'backup.prepare',reviewReference,backupId,202);db.exec('COMMIT');access.committed();const auditCheckpoint=access.checkpoint(now);
  let imageAuditKeys=auditKeyring;if(!imageAuditKeys){try{imageAuditKeys=JSON.parse(process.env.READX_AUDIT_KEYS||readFileSync(file+'.audit-keys.json','utf8'));}catch{fail('백업 이미지 검증용 접속기록 키를 읽지 못했습니다.');}}
  await backup(db,stage.file);checkedImage(stage.file,{auditKeyring:imageAuditKeys,auditCheckpoint,databaseId:journal.databaseId,journalHead});
  const size=statSync(stage.file).size;if(size<512||size>maxBytes)fail('백업 이미지 크기 제한을 확인해 주세요.');
  const iv=randomBytes(12),header={v:1,format:'readx-sqlite-backup',backupId,databaseId:journal.databaseId,createdAt:now,expiresAt,keyId:crypt.activeId,iv:iv.toString('base64'),plaintextBytes:size,plaintextSha256:await digestFile(stage.file),journalHead,auditCheckpoint},body=Buffer.from(JSON.stringify(header));if(body.length>65536)fail('백업 머리글의 크기를 초과했습니다.');const length=Buffer.alloc(4);length.writeUInt32BE(body.length);const prefix=Buffer.concat([magic,length,body]),cipher=crypt.cipher(iv);cipher.setAAD(prefix);
  writeFileSync(partial,prefix,{flag:'wx',mode:0o600});await pipeline(createReadStream(stage.file),cipher,createWriteStream(partial,{flags:constants.O_WRONLY|constants.O_APPEND}));const fd=openSync(partial,constants.O_WRONLY|constants.O_APPEND);try{writeFileSync(fd,cipher.getAuthTag());fsyncSync(fd);}finally{closeSync(fd);}
  linkSync(partial,out);unlinkSync(partial);flush(out);const sha256=await digestFile(out);db.exec('BEGIN IMMEDIATE');localEvent(access,Date.now(),'backup.created',reviewReference,backupId,200);db.exec('COMMIT');access.committed();
  return {ok:true,backupId,databaseId:journal.databaseId,path:out,sha256,bytes:statSync(out).size,createdAt:now,expiresAt,journalHead,auditCheckpoint,encrypted:true,plaintextStageRemovedOnReturn:true,offsiteStorageVerified:false,restoreDrillCompleted:false};
 }finally{db?.close();if(existsSync(partial)){assertPlainFile(partial);unlinkSync(partial);}removeOwnStage(stage);release();}
}
function readEnvelope(path){
 const fd=openSync(path,'r');try{const first=Buffer.alloc(magic.length+4);if(readSync(fd,first,0,first.length,0)!==first.length||!first.subarray(0,magic.length).equals(magic))fail('지원하는 암호화 백업 형식이 아닙니다.');const length=first.readUInt32BE(magic.length);if(length<2||length>65536)fail('백업 머리글 길이가 올바르지 않습니다.');const bytes=Buffer.alloc(length);if(readSync(fd,bytes,0,length,first.length)!==length)fail('백업 머리글이 잘렸습니다.');const header=JSON.parse(bytes.toString('utf8')),prefix=Buffer.concat([first,bytes]);if(header.v!==1||header.format!=='readx-sqlite-backup'||!Number.isSafeInteger(header.plaintextBytes)||header.plaintextBytes<512||header.plaintextBytes>maxBytes||statSync(path).size!==prefix.length+header.plaintextBytes+16||typeof header.iv!=='string'||Buffer.from(header.iv,'base64').length!==12||!/^[a-f0-9]{64}$/.test(header.plaintextSha256))fail('백업 크기·버전·암호화 정보를 확인해 주세요.');const tag=Buffer.alloc(16);if(readSync(fd,tag,0,16,prefix.length+header.plaintextBytes)!==16)fail('백업 인증 태그가 없습니다.');return {header,prefix,tag};}finally{closeSync(fd);}
}
export async function verifyEncryptedBackup({archivePath,expectedSha256,backupKeyring,databaseId,now=Date.now()}){
 if(typeof expectedSha256!=='string'||!/^[a-f0-9]{64}$/.test(expectedSha256))fail('검증한 백업 해시가 필요합니다.');
 const path=privatePath(archivePath);assertPlainFile(path);if(await digestFile(path)!==expectedSha256)fail('백업 파일 해시가 다릅니다.');
 const {header,prefix,tag}=readEnvelope(path),crypt=backupCrypto({keyring:backupKeyring,restore:true}),decipher=crypt.decipher(header.keyId,Buffer.from(header.iv,'base64'));decipher.setAAD(prefix);decipher.setAuthTag(tag);
 await pipeline(createReadStream(path,{start:prefix.length,end:prefix.length+header.plaintextBytes-1}),decipher,new Writable({write(chunk,encoding,done){done();}}));
 if(header.databaseId!==databaseId||!Number.isSafeInteger(header.expiresAt)||header.expiresAt<=now)fail('이 DB의 유효한 보존기간 내 백업이 아닙니다.');
 return {ok:true,backupId:header.backupId,databaseId:header.databaseId,expiresAt:header.expiresAt,authenticated:true,sqliteIntegrityChecked:false};
}
export async function restoreEncryptedBackup({archivePath,targetDbPath,expectedSha256,journalPath,backupKeyring,recoveryKeyring,dataKeyring,auditKeyring,accessArchivePath,accessArchiveSha256,anchor,auditAnchor,reviewReference,confirmed=false,now=Date.now()}){
 if(!ref(reviewReference)||confirmed!==true||typeof expectedSha256!=='string'||!/^[a-f0-9]{64}$/.test(expectedSha256))fail('검증한 백업 해시·복원 검토 문서·명시적 확인이 필요합니다.');
 const archive=privatePath(archivePath),target=privatePath(targetDbPath);assertPlainFile(archive);fresh(target);fresh(target+'.restore.pending');if(await digestFile(archive)!==expectedSha256)fail('선택한 백업 파일 해시가 다릅니다.');
 if(!dataKeyring&&!process.env.READX_DATA_KEYS||!recoveryKeyring&&!process.env.READX_RECOVERY_KEYS||!auditKeyring&&!process.env.READX_AUDIT_KEYS)fail('복원 전에 분리 보관한 개인정보·삭제 원장·접속기록 키를 구성해 주세요.');
 const crypt=backupCrypto({keyring:backupKeyring,restore:true}),stage=stageIn(dirname(target));writeFileSync(target+'.restore.pending',JSON.stringify({v:1,kind:'restore-pending',reference:reviewReference})+'\n',{flag:'wx',mode:0o600});flush(target+'.restore.pending');
 try{
  const {header,prefix,tag}=readEnvelope(archive),decipher=crypt.decipher(header.keyId,Buffer.from(header.iv,'base64'));decipher.setAAD(prefix);decipher.setAuthTag(tag);
  await pipeline(createReadStream(archive,{start:prefix.length,end:prefix.length+header.plaintextBytes-1}),decipher,createWriteStream(stage.file,{flags:'wx',mode:0o600}));
  if(!Number.isSafeInteger(header.expiresAt)||header.expiresAt<=now)fail('보존기간이 지난 백업은 일반 복원 경로로 재사용할 수 없습니다.');
  if(await digestFile(stage.file)!==header.plaintextSha256)fail('복호화한 백업 이미지 해시가 다릅니다.');checkedImage(stage.file,{auditKeyring,auditCheckpoint:header.auditCheckpoint,databaseId:header.databaseId,journalHead:header.journalHead});
  const probe=new DatabaseSync(stage.file);try{const external=createRecoveryJournal({db:probe,dbPath:stage.file,journalPath,keyring:recoveryKeyring,initialize:false,adoptLegacy:true,anchor});if(external.verify().some(f=>['backup_purge_prepared','backup_purged'].includes(f.event.type)&&f.event.backupId===header.backupId))fail('만료 파기 대상으로 확인한 백업은 다시 복원할 수 없습니다.');}finally{probe.close();}
  const replay=maintainDatabase({dbPath:stage.file,journalPath,action:'replay',reviewReference,confirmed:true,recoveryKeyring,dataKeyring,auditKeyring,backupKeyring,accessArchivePath,accessArchiveSha256,anchor,auditAnchor,now});
  linkSync(stage.file,target);flush(target);assertPlainFile(target+'.restore.pending');unlinkSync(target+'.restore.pending');
  return {ok:true,backupId:header.backupId,databaseId:header.databaseId,path:target,sourceSha256:expectedSha256,recovery:replay,oldCredentialsRevoked:true,guardianReverificationRequired:true,productionReadinessCertified:false};
 }finally{removeOwnStage(stage);}
}
export async function purgeEncryptedBackup({dbPath,archivePath,expectedSha256,journalPath,backupKeyring,recoveryKeyring,auditKeyring,reviewReference,confirmed=false,now=Date.now()}){
 if(!ref(reviewReference)||confirmed!==true||typeof expectedSha256!=='string'||!/^[a-f0-9]{64}$/.test(expectedSha256))fail('검토한 만료 파일 해시·파기 문서와 명시적 확인이 필요합니다.');
 const file=privatePath(dbPath),archive=privatePath(archivePath);assertPlainFile(file);assertNotMaintaining(file);const release=acquireFileLease(file+'.maintenance.lock','db-maintenance');let db;
 try{
  db=new DatabaseSync(file);if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name='recovery_state'").get())fail('확인된 프로젝트 DB가 필요합니다.');const access=createAccessLog({db,dbPath:file,keyring:auditKeyring}),journal=createRecoveryJournal({db,dbPath:file,journalPath,keyring:recoveryKeyring,initialize:false});journal.sync();
  const pathHash=createHash('sha256').update(archive).digest('hex'),events=journal.verify().slice(1).map(f=>f.event);let prepared=events.filter(e=>e.type==='backup_purge_prepared'&&e.pathHash===pathHash&&e.sha256===expectedSha256).at(-1),header;
  if(existsSync(archive)){
   assertPlainFile(archive);if(await digestFile(archive)!==expectedSha256)fail('제거할 백업 파일의 해시가 다릅니다.');const crypt=backupCrypto({keyring:backupKeyring,restore:true}),envelope=readEnvelope(archive);header=envelope.header;const decipher=crypt.decipher(header.keyId,Buffer.from(header.iv,'base64'));decipher.setAAD(envelope.prefix);decipher.setAuthTag(envelope.tag);await pipeline(createReadStream(archive,{start:envelope.prefix.length,end:envelope.prefix.length+header.plaintextBytes-1}),decipher,new Writable({write(chunk,encoding,done){done();}}));
   if(header.databaseId!==journal.databaseId||!Number.isSafeInteger(header.expiresAt)||header.expiresAt>now)fail('이 DB의 보존기간이 끝난 검증 백업만 제거할 수 있습니다.');
   if(!prepared){prepared={type:'backup_purge_prepared',tenantId:'system',subjectId:header.backupId,backupId:header.backupId,operationId:randomUUID(),pathHash,sha256:expectedSha256,expiresAt:header.expiresAt,at:now,reviewReference};db.exec('BEGIN IMMEDIATE');journal.queue(prepared);localEvent(access,now,'backup.purge-prepared',reviewReference,header.backupId,202);db.exec('COMMIT');access.committed();journal.sync();}
   if(await digestFile(archive)!==expectedSha256)fail('검토 중 백업 파일이 변경되었습니다. 다시 확인해 주세요.');unlinkSync(archive);
  }else{
   if(!prepared)fail('없는 파일에 대한 검증된 만료 파기 준비 기록이 없습니다.');
   if(events.some(e=>e.type==='backup_purged'&&e.operationId===prepared.operationId))return {ok:true,alreadyPurged:true,backupId:prepared.backupId,fileAbsent:true,mediaSanitizationCertified:false};
  }
  if(existsSync(archive))fail('만료 백업 파일의 제거를 확인하지 못했습니다.');
  db.exec('BEGIN IMMEDIATE');journal.queue({type:'backup_purged',tenantId:'system',subjectId:prepared.backupId,backupId:prepared.backupId,operationId:prepared.operationId,pathHash,sha256:expectedSha256,at:now,reviewReference});localEvent(access,now,'backup.file-unlinked',reviewReference,prepared.backupId,200);db.exec('COMMIT');access.committed();journal.sync();
  return {ok:true,backupId:prepared.backupId,fileAbsent:true,recoveryReceiptRecorded:true,mediaSanitizationCertified:false,otherCopiesDisposed:false};
 }finally{db?.close();release();}
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const args=process.argv.slice(2),value=f=>{const i=args.indexOf(f);return i<0?'':args[i+1];};
 try{const common={journalPath:value('--journal')||undefined,accessArchivePath:value('--access-archive')||undefined,accessArchiveSha256:value('--access-archive-sha256')||undefined,reviewReference:value('--review-reference'),confirmed:args.includes('--confirmed')};let result;
  if(value('--action')==='backup')result=await createEncryptedBackup({...common,dbPath:value('--db'),outPath:value('--out'),expiresAt:Date.parse(value('--expires-at'))});
  else if(value('--action')==='purge')result=await purgeEncryptedBackup({...common,dbPath:value('--db'),archivePath:value('--archive'),expectedSha256:value('--expected-sha256')});
  else if(value('--action')==='restore')result=await restoreEncryptedBackup({...common,archivePath:value('--archive'),targetDbPath:value('--target'),expectedSha256:value('--expected-sha256'),anchor:value('--anchor')?JSON.parse(readFileSync(value('--anchor'),'utf8')):undefined,auditAnchor:value('--audit-anchor')?JSON.parse(readFileSync(value('--audit-anchor'),'utf8')):undefined});
  else fail('작업은 --action backup, restore 또는 purge입니다.');console.log(JSON.stringify(result,null,2));
 }catch(e){console.error('암호화 백업·복원 작업을 완료하지 못했습니다: '+e.message);process.exitCode=1;}
}
