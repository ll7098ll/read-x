import {randomBytes,createCipheriv,createDecipheriv} from 'node:crypto';
import {existsSync,lstatSync,readFileSync,writeFileSync} from 'node:fs';
export function createPrivacyVault({dbPath,keyring,hasRecords=false,production=process.env.READX_RUNTIME==='production'}){
 let config=keyring;
 if(!config&&process.env.READX_DATA_KEYS){try{config=JSON.parse(process.env.READX_DATA_KEYS);}catch{throw Error('READX_DATA_KEYS 형식을 확인해 주세요.');}}
 if(!config){
  if(production)throw Error('운영 개인정보 요청에는 별도 READX_DATA_KEYS가 필요합니다.');
  if(dbPath===':memory:')config={activeId:'memory',keys:{memory:randomBytes(32).toString('base64')}};
  else{const path=dbPath+'.data-keys.json';if(existsSync(path)){if(!lstatSync(path).isFile()||lstatSync(path).isSymbolicLink())throw Error('개발 개인정보 키는 일반 파일이어야 합니다.');try{config=JSON.parse(readFileSync(path,'utf8'));}catch{throw Error('개발 개인정보 키를 읽지 못했습니다.');}}else{if(hasRecords)throw Error('기존 개인정보 요청의 복호화 키가 없습니다.');config={activeId:'development',keys:{development:randomBytes(32).toString('base64')}};writeFileSync(path,JSON.stringify(config),{flag:'wx',mode:0o600});}}
 }
 const valid=id=>typeof id==='string'&&/^[a-zA-Z0-9_-]{1,50}$/.test(id);if(!config||!valid(config.activeId)||!config.keys||Array.isArray(config.keys)||!Object.hasOwn(config.keys,config.activeId)||Object.keys(config.keys).length>10)throw Error('개인정보 요청 키 구성을 확인해 주세요.');
 const keys=new Map();for(const [id,k]of Object.entries(config.keys)){if(!valid(id)||typeof k!=='string'||!/^[A-Za-z0-9+/]{43}=$/.test(k)||Buffer.from(k,'base64').length!==32)throw Error('개인정보 요청 키는 32바이트 Base64 형식이어야 합니다.');keys.set(id,Buffer.from(k,'base64'));}
 const aad=c=>Buffer.from(JSON.stringify(['readx-personal-v1',c.tenantId,c.id]));
 return {seal(value,c){const iv=randomBytes(12),cipher=createCipheriv('aes-256-gcm',keys.get(config.activeId),iv);cipher.setAAD(aad(c));const ciphertext=Buffer.concat([cipher.update(JSON.stringify(value),'utf8'),cipher.final()]);return {v:1,keyId:config.activeId,iv:iv.toString('base64'),ciphertext:ciphertext.toString('base64'),tag:cipher.getAuthTag().toString('base64')};},open(record,c){try{if(record?.v!==1||!keys.has(record.keyId))throw Error();const iv=Buffer.from(record.iv,'base64'),tag=Buffer.from(record.tag,'base64');if(iv.length!==12||tag.length!==16)throw Error();const decipher=createDecipheriv('aes-256-gcm',keys.get(record.keyId),iv);decipher.setAAD(aad(c));decipher.setAuthTag(tag);return JSON.parse(Buffer.concat([decipher.update(Buffer.from(record.ciphertext,'base64')),decipher.final()]).toString('utf8'));}catch{throw Error('개인정보 요청의 무결성·복호화 키를 확인하지 못했습니다.');}},activeId:config.activeId};
}
