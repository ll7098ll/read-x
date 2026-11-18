import {existsSync,readFileSync,statSync,openSync,writeFileSync,fsyncSync,closeSync} from 'node:fs';
import {randomUUID} from 'node:crypto';
import {recoverySigner} from './recovery-keys.mjs';
import {assertPlainFile,acquireFileLease} from './maintenance-lock.mjs';
import {opsError,validTime,operationKinds} from './operations-policy.mjs';

const zero='0'.repeat(64),maxBytes=64*1024*1024;
const wire=f=>JSON.stringify(['readx-operations-v1',f.ledgerId,f.seq,f.keyId,f.previous,f.event]);
const anchorWire=c=>JSON.stringify(['readx-operations-anchor-v1',c.ledgerId,c.seq,c.hash,c.keyId,c.createdAt]);
const failed=()=>opsError('OPS_LEDGER_INVALID','운영 실행 기록·키·별도 기준점 검증이 필요합니다.');
export function createOperationsLedger({policy,keyring,anchor,initialize=false,at=Date.now()}){
 const path=policy.ledgerPath;assertPlainFile(path);
 const signer=recoverySigner({dbPath:policy.dbPath,keyring,hasRecords:existsSync(path)});
 const frame=(ledgerId,seq,previous,event)=>{const f={v:1,kind:'readx-operations-frame',ledgerId,seq,keyId:signer.activeId,previous,event};return {...f,hash:signer.sign(wire(f))};};
 if(!existsSync(path)){
  if(!initialize||anchor||!validTime(at))throw failed();
  const f=frame(randomUUID(),0,zero,{type:'identity',policyId:policy.id,databaseId:policy.databaseId,at});
  const fd=openSync(path,'wx',0o600);try{writeFileSync(fd,JSON.stringify(f)+'\n');fsyncSync(fd);}finally{closeSync(fd);}
 }
 const read=()=>{
  try{
   assertPlainFile(path);if(statSync(path).size>maxBytes)throw failed();const raw=readFileSync(path,'utf8');if(!raw.endsWith('\n'))throw failed();
   const frames=raw.trimEnd().split('\n').map(JSON.parse);if(!frames.length)throw failed();let previous=zero,lastAt=0;
   for(const [seq,f]of frames.entries()){
    if(f.v!==1||f.kind!=='readx-operations-frame'||f.ledgerId!==frames[0].ledgerId||f.seq!==seq||f.previous!==previous||!validTime(f.event?.at)||f.event.at<lastAt||!signer.verify(wire(f),f.hash,f.keyId))throw failed();previous=f.hash;lastAt=f.event.at;
    if(seq===0&&(f.event.type!=='identity'||f.event.policyId!==policy.id||f.event.databaseId!==policy.databaseId))throw failed();
    if(seq>0&&!['policy_approved','heartbeat','job_started','job_succeeded','job_failed','job_interrupted'].includes(f.event.type))throw failed();
    if(f.event.type.startsWith('job_')&&(!operationKinds.includes(f.event.job)||typeof f.event.attemptId!=='string'))throw failed();
   }
   if(anchor&&(anchor.ledgerId!==frames[0].ledgerId||!frames[anchor.seq]||frames[anchor.seq].hash!==anchor.hash||!signer.verify(anchorWire(anchor),anchor.signature,anchor.keyId)))throw failed();
   return frames;
  }catch{throw failed();}
 };
 read();
 const append=event=>{
  const release=acquireFileLease(path+'.write.lock','operations-ledger');try{
   const frames=read(),tail=frames.at(-1);if(!validTime(event.at)||event.at<tail.event.at)throw opsError('OPS_CLOCK_INVALID','운영 시각이 이전 기록보다 앞섭니다. 서버 시각을 확인해 주세요.');
   const f=frame(tail.ledgerId,tail.seq+1,tail.hash,event),bytes=JSON.stringify(f)+'\n';if(Buffer.byteLength(bytes)>65536||statSync(path).size+Buffer.byteLength(bytes)>maxBytes)throw opsError('OPS_CAPACITY_REQUIRED','운영 실행 기록의 분리 보관·용량 검토가 필요합니다.');
   assertPlainFile(path);const fd=openSync(path,'a');try{writeFileSync(fd,bytes);fsyncSync(fd);}finally{closeSync(fd);}return f;
  }finally{release();}
 };
 const checkpoint=(now=Date.now())=>{const tail=read().at(-1),c={v:1,kind:'readx-operations-anchor',ledgerId:tail.ledgerId,seq:tail.seq,hash:tail.hash,keyId:signer.activeId,createdAt:now};return {...c,signature:signer.sign(anchorWire(c))};};
 return {read,append,checkpoint};
}
