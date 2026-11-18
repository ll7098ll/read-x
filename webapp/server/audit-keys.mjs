import {randomBytes,createHmac,timingSafeEqual} from 'node:crypto';
import {existsSync,lstatSync,readFileSync,writeFileSync} from 'node:fs';

export function auditSigner({dbPath,keyring,hasRecords=false,production=process.env.READX_RUNTIME==='production'}={}) {
  let config=keyring;
  if(!config&&process.env.READX_AUDIT_KEYS){try{config=JSON.parse(process.env.READX_AUDIT_KEYS);}catch{throw Error('READX_AUDIT_KEYS 형식을 확인해 주세요.');}}
  if(!config){
    if(production)throw Error('운영 서버에는 별도 READX_AUDIT_KEYS가 필요합니다.');
    if(dbPath===':memory:')config={activeId:'memory',keys:{memory:randomBytes(32).toString('base64')}};
    else{
      const path=dbPath+'.audit-keys.json';
      if(existsSync(path)){if(!lstatSync(path).isFile()||lstatSync(path).isSymbolicLink())throw Error('개발용 접속기록 키는 일반 파일이어야 합니다.');try{config=JSON.parse(readFileSync(path,'utf8'));}catch{throw Error('개발용 접속기록 키를 읽지 못했습니다.');}}
      else{if(hasRecords)throw Error('기존 접속기록을 검증할 키가 없습니다. 별도 보관한 키를 복원해 주세요.');config={activeId:'development',keys:{development:randomBytes(32).toString('base64')}};writeFileSync(path,JSON.stringify(config),{flag:'wx',mode:0o600});}
    }
  }
  const validId=id=>typeof id==='string'&&/^[a-zA-Z0-9_-]{1,50}$/.test(id);
  if(!config||!validId(config.activeId)||!config.keys||typeof config.keys!=='object'||Array.isArray(config.keys)||!Object.hasOwn(config.keys,config.activeId)||Object.keys(config.keys).length>10)throw Error('접속기록 키 구성을 확인해 주세요.');
  const keys=new Map();for(const [id,key]of Object.entries(config.keys)){
    if(!validId(id)||typeof key!=='string'||!/^[a-zA-Z0-9+/]{43}=$/.test(key)||Buffer.from(key,'base64').length!==32)throw Error('접속기록 키는 32바이트 Base64 형식이어야 합니다.');keys.set(id,Buffer.from(key,'base64'));
  }
  const sign=(value,keyId=config.activeId)=>{if(!keys.has(keyId))throw Error('이전 접속기록을 검증할 키가 없습니다.');return createHmac('sha256',keys.get(keyId)).update(value).digest('hex');};
  return {activeId:config.activeId,sign,verify(value,signature,keyId){return typeof signature==='string'&&/^[a-f0-9]{64}$/.test(signature)&&timingSafeEqual(Buffer.from(sign(value,keyId),'hex'),Buffer.from(signature,'hex'));}};
}
