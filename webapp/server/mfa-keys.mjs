import { randomBytes,createCipheriv,createDecipheriv } from 'node:crypto';
import { readFileSync,writeFileSync,existsSync,lstatSync } from 'node:fs';
const validId=v=>typeof v==='string'&&/^[a-zA-Z0-9_-]{1,50}$/.test(v);

export function createMfaProtector({dbPath,keyring,hasSecrets=false,production=process.env.READX_RUNTIME==='production'}={}) {
  let config=keyring;
  if(!config&&process.env.READX_MFA_KEYS){try{config=JSON.parse(process.env.READX_MFA_KEYS);}catch{throw Error('READX_MFA_KEYS 형식이 올바르지 않습니다.');}}
  if(!config){
    if(production)throw Error('운영 서버에는 별도로 보관한 READX_MFA_KEYS 설정이 필요합니다.');
    if(dbPath===':memory:')config={activeId:'memory',keys:{memory:randomBytes(32).toString('base64')}};
    else {
      const file=dbPath+'.mfa-keys.json';
      if(existsSync(file)){if(lstatSync(file).isSymbolicLink())throw Error('개발용 MFA 키는 일반 파일이어야 합니다.');try{config=JSON.parse(readFileSync(file,'utf8'));}catch{throw Error('개발용 MFA 키 파일을 읽을 수 없습니다.');}}
      else {if(hasSecrets)throw Error('기존 MFA를 복구할 키가 없습니다. 키 백업을 복원해야 합니다.');config={activeId:'development',keys:{development:randomBytes(32).toString('base64')}};writeFileSync(file,JSON.stringify(config),{flag:'wx',mode:0o600});}
    }
  }
  if(!config||!validId(config.activeId)||!config.keys||typeof config.keys!=='object'||Array.isArray(config.keys)||!Object.hasOwn(config.keys,config.activeId)||Object.keys(config.keys).length>10)throw Error('MFA 키 구성과 활성 키를 확인해 주세요.');
  const keys=new Map();for(const [id,value] of Object.entries(config.keys)){
    if(!validId(id)||typeof value!=='string'||!/^[A-Za-z0-9+/]{43}=$/.test(value)||Buffer.from(value,'base64').length!==32)throw Error('MFA 키는 32바이트 Base64 형식이어야 합니다.');keys.set(id,Buffer.from(value,'base64'));
  }
  const context=u=>Buffer.from(JSON.stringify(['readx-mfa-v1',u.tenantId,u.id]));
  return {
    seal(secret,u){const iv=randomBytes(12),cipher=createCipheriv('aes-256-gcm',keys.get(config.activeId),iv);cipher.setAAD(context(u));const encrypted=Buffer.concat([cipher.update(secret,'utf8'),cipher.final()]);return {v:1,keyId:config.activeId,iv:iv.toString('base64'),ciphertext:encrypted.toString('base64'),tag:cipher.getAuthTag().toString('base64')};},
    open(record,u){
      try{if(record?.v!==1||!keys.has(record.keyId))throw Error();const iv=Buffer.from(record.iv,'base64'),tag=Buffer.from(record.tag,'base64');if(iv.length!==12||tag.length!==16)throw Error();const decipher=createDecipheriv('aes-256-gcm',keys.get(record.keyId),iv);decipher.setAAD(context(u));decipher.setAuthTag(tag);return Buffer.concat([decipher.update(Buffer.from(record.ciphertext,'base64')),decipher.final()]).toString('utf8');}
      catch{throw Error('MFA 키로 기존 인증 정보를 확인하지 못했습니다. 키 구성과 백업을 확인해 주세요.');}
    },
    activeId:config.activeId,
  };
}
