import {DatabaseSync} from 'node:sqlite';
import {readFileSync,existsSync} from 'node:fs';
import {resolve} from 'node:path';
import {createAccessLog} from './access-log.mjs';
const args=process.argv.slice(2),value=flag=>{const i=args.indexOf(flag);return i<0?'':args[i+1];};
let db;
try{
  const file=value('--db');if(!file||!existsSync(resolve(file)))throw Error('사용법: node server/verify-access-log.mjs --db 기존DB [--checkpoint 별도보관파일]');
  db=new DatabaseSync(resolve(file),{readOnly:true});db.exec('BEGIN');
  const access=createAccessLog({db,dbPath:resolve(file),readOnly:true}),checkpoint=value('--checkpoint');
  const result=access.verify(checkpoint?JSON.parse(readFileSync(resolve(checkpoint),'utf8')):undefined);db.exec('COMMIT');
  console.log(JSON.stringify(result,null,2));
}catch{try{db?.exec('ROLLBACK');}catch{}console.error('접속기록 검사에 실패했습니다. DB·검증 키·별도 보관 기준점을 확인하고 증거를 보전해 주세요.');process.exitCode=1;}finally{db?.close();}
