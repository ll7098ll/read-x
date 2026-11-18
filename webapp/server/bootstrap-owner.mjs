import {assertNotMaintaining,privateRuntimePath} from './maintenance-lock.mjs';
import {recordLocalAccess} from './local-access-event.mjs';
import {DatabaseSync} from 'node:sqlite';
import {randomUUID} from 'node:crypto';
import {existsSync,mkdirSync} from 'node:fs';
import {resolve,dirname,isAbsolute} from 'node:path';
import {newState} from '../shared/exam-engine.mjs';
import {upgradeOrganization} from '../shared/organization.mjs';
import {passwordHash} from './credentials.mjs';
import {readPrivateJson} from './private-input.mjs';

const args=process.argv.slice(2),i=args.indexOf('--db'),supplied=i>=0?args[i+1]:null;
if(!supplied||!isAbsolute(supplied)){console.error('사용법: node server/bootstrap-owner.mjs --db 운영DB절대경로');process.exit(1);}
const dbPath=resolve(supplied);let db;
try{
  console.log('첫 운영자 정보의 JSON 한 줄을 stdin으로 입력하세요. 입력은 표시되지 않습니다.');
  const body=await readPrivateJson(),name=typeof body.name==='string'?body.name.trim():'',username=typeof body.username==='string'?body.username.trim().toLowerCase():'';
  if(!name||name.length>40||!/^[a-z0-9._-]{3,40}$/.test(username)||typeof body.password!=='string'||body.password.length<10||body.password.length>128||body.className!=null&&(typeof body.className!=='string'||!body.className.trim()||body.className.trim().length>60))throw Error('이름·아이디·10~128자 비밀번호·반 이름을 확인해 주세요.');
  assertNotMaintaining(dbPath);const existed=existsSync(dbPath);mkdirSync(dirname(dbPath),{recursive:true});privateRuntimePath(dbPath);db=new DatabaseSync(dbPath);
  if(existed&&!db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name='exam_state'").get())throw Error('이 프로젝트의 기존 DB가 아닙니다. 새 DB 경로나 올바른 운영 DB를 선택해 주세요.');
  db.exec('PRAGMA busy_timeout=5000; PRAGMA journal_mode=WAL; BEGIN IMMEDIATE; CREATE TABLE IF NOT EXISTS exam_state (id INTEGER PRIMARY KEY CHECK(id=1),body TEXT NOT NULL)');
  assertNotMaintaining(dbPath);const row=db.prepare('SELECT body FROM exam_state WHERE id=1').get(),s=row?JSON.parse(row.body):newState();
  if(s.users.length)throw Error('계정이 있는 DB에는 첫 운영자를 추가하거나 권한을 부여할 수 없습니다.');
  const at=Date.now(),u={id:randomUUID(),tenantId:randomUUID(),name,username,password:passwordHash(body.password),role:'teacher',isOwner:true,active:true,revision:0,childIds:[],className:body.className?.trim()||'우리 반'};
  s.users.push(u);upgradeOrganization(s,randomUUID,at,'enforced');s.audit.push({at,actor:'local-server-admin',tenantId:u.tenantId,subjectId:u.id,action:'account.bootstrap.local'});
  db.prepare('INSERT INTO exam_state(id,body) VALUES(1,?) ON CONFLICT(id) DO UPDATE SET body=excluded.body').run(JSON.stringify(s));recordLocalAccess({db,dbPath:dbPath,user:u,at,action:'local/bootstrap-owner'});db.exec('COMMIT');
  console.log('첫 운영자를 등록했습니다. 비밀번호로 로그인한 뒤 인증앱을 등록해야 학생 정보에 접근할 수 있습니다.');
}catch(e){try{db?.exec('ROLLBACK');}catch{}console.error(e.name==='AbortError'?'입력이 취소되었거나 길이 제한을 넘었습니다.':e.message);process.exitCode=1;}finally{db?.close();}
