import {existsSync,lstatSync,openSync,writeFileSync,fsyncSync,closeSync,readFileSync,unlinkSync,realpathSync} from 'node:fs';
import {hostname} from 'node:os';
import {randomUUID} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {resolve,dirname,sep,join} from 'node:path';
const fail=message=>{throw Object.assign(Error(message),{status:503,code:'MAINTENANCE_REQUIRED'});};
export function assertPlainFile(path){const s=lstatSync(path,{throwIfNoEntry:false});if(s){if(!s.isFile()||s.isSymbolicLink())fail('운영 제어 파일은 일반 파일이어야 합니다.');}}
export function canonicalFile(path){const absolute=resolve(path);return resolve(realpathSync(dirname(absolute)),absolute.slice(dirname(absolute).length+1));}
export function assertNotMaintaining(dbPath){if(dbPath===':memory:')return;for(const suffix of ['.maintenance.lock','.restore.pending'])if(lstatSync(dbPath+suffix,{throwIfNoEntry:false}))fail('복구·정리 작업을 확인하는 동안 서비스 이용이 일시 중지됩니다.');}
export function acquireFileLease(path,kind,{reclaimDead=true}={}){
 assertPlainFile(path);
 if(reclaimDead&&existsSync(path)){
  let old;try{old=JSON.parse(readFileSync(path,'utf8'));}catch{fail('손상된 운영 잠금은 자동으로 해제하지 않습니다.');}
  if(old.v!==1||old.kind!==kind||typeof old.nonce!=='string')fail('알 수 없는 운영 잠금은 자동으로 해제하지 않습니다.');
  let alive=true;if(old.hostname===hostname()&&Number.isSafeInteger(old.pid)&&old.pid>0){try{process.kill(old.pid,0);}catch(e){if(e.code==='ESRCH')alive=false;}}
  if(!alive&&typeof old.nonce==='string'){assertPlainFile(path);if(JSON.parse(readFileSync(path,'utf8')).nonce===old.nonce)unlinkSync(path);}
 }
 const record={v:1,pid:process.pid,hostname:hostname(),nonce:randomUUID(),kind,at:Date.now()};let fd;
 try{fd=openSync(path,'wx',0o600);writeFileSync(fd,JSON.stringify(record)+'\n');fsyncSync(fd);}catch{fail('다른 복구·정리 작업의 잠금이 있거나 잠금을 저장할 수 없습니다.');}finally{if(fd!==undefined)closeSync(fd);}
 return ()=>{assertPlainFile(path);if(!existsSync(path)||JSON.parse(readFileSync(path,'utf8')).nonce!==record.nonce)fail('운영 잠금 소유권이 바뀌었습니다.');unlinkSync(path);};
}

export function privateRuntimePath(path){const file=canonicalFile(path),app=resolve(fileURLToPath(new URL('..',import.meta.url))),low=v=>process.platform==='win32'?v.toLowerCase():v;if(low(file).startsWith(low(app+sep))&&!low(file).startsWith(low(join(app,'.exam-data')+sep)))throw Error('운영 DB·키·복구 파일을 공개 소스·웹 산출물 경로에 둘 수 없습니다.');return file;}
