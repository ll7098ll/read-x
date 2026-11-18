import {readFileSync,lstatSync,realpathSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {isAbsolute,join} from 'node:path';
import {privateRuntimePath,assertPlainFile} from './maintenance-lock.mjs';

export const operationKinds=['verify','backup','audit','restore_drill'];
export const opsError=(code,message)=>Object.assign(Error(message),{code,status:503});
export const validTime=n=>Number.isSafeInteger(n)&&n>=0&&n<=8640000000000000;
const reference=s=>typeof s==='string'&&/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(s);
const ordered=v=>Array.isArray(v)?v.map(ordered):v&&typeof v==='object'?Object.fromEntries(Object.keys(v).sort().map(k=>[k,ordered(v[k])])):v;
export const policyHash=p=>createHash('sha256').update(JSON.stringify(ordered(p))).digest('hex');

export function readOperationsPolicy(path,{now=Date.now()}={}){
 try{
  if(!path||!isAbsolute(path)||!validTime(now))throw Error();
  const file=privateRuntimePath(path);assertPlainFile(file);if(lstatSync(file).size>65536)throw Error();
  const value=JSON.parse(readFileSync(file,'utf8'));
  if(value.v!==1||value.kind!=='readx-operations-policy'||!reference(value.id)||!Number.isSafeInteger(value.revision)||value.revision<1||typeof value.databaseId!=='string'||value.databaseId.length>100||!value.databaseId||value.enabled!==true||!reference(value.reviewReference)||typeof value.reviewedBy!=='string'||!value.reviewedBy.trim()||value.reviewedBy.length>100||!Number.isFinite(Date.parse(value.reviewedAt))||Date.parse(value.reviewedAt)>now)throw Error();
  const policy=structuredClone(value);
  for(const key of ['dbPath','journalPath','recoveryAnchorPath','auditAnchorPath','ledgerPath']){
   if(typeof policy[key]!=='string'||!isAbsolute(policy[key]))throw Error();policy[key]=privateRuntimePath(policy[key]);assertPlainFile(policy[key]);
  }
  for(const key of ['backupDirectory','auditDirectory','drillDirectory']){
   if(typeof policy[key]!=='string'||!isAbsolute(policy[key]))throw Error();const info=lstatSync(policy[key]);if(!info.isDirectory()||info.isSymbolicLink())throw Error();
   policy[key]=realpathSync(policy[key]);privateRuntimePath(join(policy[key],'operations-boundary'));
  }
  const paths=['dbPath','journalPath','recoveryAnchorPath','auditAnchorPath','ledgerPath'].map(k=>policy[k].toLowerCase());if(new Set(paths).size!==paths.length)throw Error();
  if(!Number.isSafeInteger(policy.retryAfterMs)||policy.retryAfterMs<60000||policy.retryAfterMs>86400000)throw Error();
  if(!Number.isSafeInteger(policy.heartbeatMaxAgeMs)||policy.heartbeatMaxAgeMs<60000||policy.heartbeatMaxAgeMs>30*86400000)throw Error();
  if(!Number.isSafeInteger(policy.runningMaxAgeMs)||policy.runningMaxAgeMs<60000||policy.runningMaxAgeMs>86400000)throw Error();
  if(!policy.jobs||Object.keys(policy.jobs).length!==operationKinds.length)throw Error();
  for(const kind of operationKinds){
   const job=policy.jobs[kind];if(!job||!Number.isSafeInteger(job.everyMs)||job.everyMs<60000||job.everyMs>366*86400000||!Number.isSafeInteger(job.maxAgeMs)||job.maxAgeMs<job.everyMs||job.maxAgeMs>2*366*86400000)throw Error();
   if(['backup','audit'].includes(kind)&&(!Number.isSafeInteger(job.retentionMs)||job.retentionMs<job.maxAgeMs||!validTime(now+job.retentionMs)))throw Error();
  }
  if(policy.jobs.backup.retentionMs<policy.jobs.restore_drill.maxAgeMs||policy.jobs.audit.retentionMs<policy.jobs.restore_drill.maxAgeMs)throw Error();
  if(policy.jobs.backup.retentionMs<policy.jobs.restore_drill.maxAgeMs||policy.jobs.audit.retentionMs<policy.jobs.restore_drill.maxAgeMs)throw Error();
  return {policy,hash:policyHash(policy),file};
 }catch{throw opsError('OPS_POLICY_INVALID','운영 정책의 경로·주기·보존기간·실제 검토 정보를 확인해 주세요.');}
}

export function readOperationsAnchor(path){
 try{const file=privateRuntimePath(path);assertPlainFile(file);if(lstatSync(file).size>65536)throw Error();return JSON.parse(readFileSync(file,'utf8'));}
 catch{throw opsError('OPS_ANCHOR_INVALID','별도 보관한 운영 기준점을 확인해 주세요.');}
}
