import {auditSigner} from './audit-keys.mjs';
import {existsSync,lstatSync,readFileSync,writeFileSync} from 'node:fs';
import {randomBytes} from 'node:crypto';
export function recoverySigner({dbPath,keyring,hasRecords=false,production=process.env.READX_RUNTIME==='production'}){
 let config=keyring;if(!config&&process.env.READX_RECOVERY_KEYS){try{config=JSON.parse(process.env.READX_RECOVERY_KEYS);}catch{throw Error('READX_RECOVERY_KEYS 형식을 확인해 주세요.');}}
 if(!config){
  if(production)throw Error('운영 삭제·복원에는 독립 READX_RECOVERY_KEYS가 필요합니다.');
  if(dbPath===':memory:')config={activeId:'memory',keys:{memory:randomBytes(32).toString('base64')}};
  else{const path=dbPath+'.recovery-keys.json';if(existsSync(path)){if(!lstatSync(path).isFile()||lstatSync(path).isSymbolicLink())throw Error('개발 복구 키는 일반 파일이어야 합니다.');try{config=JSON.parse(readFileSync(path,'utf8'));}catch{throw Error('개발 복구 키를 읽지 못했습니다.');}}else{if(hasRecords)throw Error('삭제·복구 원장을 검증할 키가 없습니다.');config={activeId:'development',keys:{development:randomBytes(32).toString('base64')}};writeFileSync(path,JSON.stringify(config),{flag:'wx',mode:0o600});}}
 }
 // Explicit configuration prevents fallback to the unrelated audit keyring.
 return auditSigner({dbPath,keyring:config,hasRecords,production});
}
