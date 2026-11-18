import {createCipheriv,createDecipheriv,randomBytes} from 'node:crypto';
import {existsSync,lstatSync,readFileSync,writeFileSync} from 'node:fs';
export function backupCrypto({dbPath,keyring,restore=false,production=process.env.READX_RUNTIME==='production'}){
 let config=keyring;if(!config&&process.env.READX_BACKUP_KEYS){try{config=JSON.parse(process.env.READX_BACKUP_KEYS);}catch{throw Error('READX_BACKUP_KEYS 형식을 확인해 주세요.');}}
 if(!config){if(production||restore)throw Error('백업 원본과 분리해 보관한 READX_BACKUP_KEYS가 필요합니다.');const path=dbPath+'.backup-keys.json';if(existsSync(path)){if(!lstatSync(path).isFile()||lstatSync(path).isSymbolicLink())throw Error('개발 백업 키는 일반 파일이어야 합니다.');try{config=JSON.parse(readFileSync(path,'utf8'));}catch{throw Error('개발 백업 키를 읽지 못했습니다.');}}else{config={activeId:'development',keys:{development:randomBytes(32).toString('base64')}};writeFileSync(path,JSON.stringify(config),{flag:'wx',mode:0o600});}}
 const valid=id=>typeof id==='string'&&/^[a-zA-Z0-9_-]{1,50}$/.test(id);if(!config||!valid(config.activeId)||!config.keys||typeof config.keys!=='object'||Array.isArray(config.keys)||!Object.hasOwn(config.keys,config.activeId)||Object.keys(config.keys).length>10)throw Error('백업 키 구성을 확인해 주세요.');
 const keys=new Map();for(const [id,key]of Object.entries(config.keys)){if(!valid(id)||typeof key!=='string'||!/^[a-zA-Z0-9+/]{43}=$/.test(key)||Buffer.from(key,'base64').length!==32)throw Error('백업 키는 32바이트 Base64 형식이어야 합니다.');keys.set(id,Buffer.from(key,'base64'));}
 return {activeId:config.activeId,cipher(iv){return createCipheriv('aes-256-gcm',keys.get(config.activeId),iv);},decipher(id,iv){if(!keys.has(id))throw Error('이 백업을 복호화할 이전 키가 없습니다.');return createDecipheriv('aes-256-gcm',keys.get(id),iv);}};
}
