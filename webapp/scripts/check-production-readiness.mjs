import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { productionRequirements } from '../server/production-requirements.mjs';

export async function checkProductionReadiness({manifestPath=fileURLToPath(new URL('../../docs/PRODUCTION_READINESS_2026-11-14.json',import.meta.url)),bundlePath=fileURLToPath(new URL('../dist/index.html',import.meta.url))}={}) {
  const nonempty=v=>typeof v==='string'&&v.trim().length>0;
  const issues=[];let manifest;
  try { manifest=JSON.parse(await readFile(manifestPath,'utf8')); }
  catch { return {ready:false,issues:['운영 준비 증거 목록을 읽지 못했습니다.']}; }
  if(manifest.schemaVersion!==1)issues.push('운영 준비 증거 목록의 버전을 확인해 주세요.');
  if(!nonempty(manifest.operator?.legalName)||!nonempty(manifest.operator?.privacyContact)||!nonempty(manifest.operator?.operationsContact))issues.push('실제 운영 명의와 개인정보·운영 담당 연락처가 미정입니다.');
  const controls=Array.isArray(manifest.controls)?manifest.controls:[];
  if(new Set(controls.map(c=>c.id)).size!==controls.length)issues.push('운영 준비 항목의 식별자가 중복되어 있습니다.');
  for(const [id,title] of productionRequirements){
    const c=controls.find(c=>c.id===id);
    if(!c||c.status!=='reviewed'||!nonempty(c.reviewer)||!c.reviewedAt||!Number.isFinite(Date.parse(c.reviewedAt))||Date.parse(c.reviewedAt)>Date.now()||!Array.isArray(c.evidence)||!c.evidence.length){issues.push(`${id}: ${title}의 검토 증거가 완료되지 않았습니다.`);continue;}
    for(const evidence of c.evidence){
      try {const bytes=await readFile(resolve(dirname(manifestPath),evidence.path));const digest=createHash('sha256').update(bytes).digest('hex');if(digest!==evidence.sha256)issues.push(`${id}: 검토한 증거 파일과 현재 파일이 다릅니다.`);}
      catch {issues.push(`${id}: 검토 증거 파일을 확인하지 못했습니다.`);}
    }
  }
  try {const digest=createHash('sha256').update(await readFile(bundlePath)).digest('hex');if(manifest.bundleSha256!==digest)issues.push('검토 승인된 웹앱과 현재 배포 산출물이 다릅니다.');}
  catch {issues.push('배포할 웹앱 산출물이 없습니다.');}
  return {ready:issues.length===0,issues,controls:productionRequirements.length,notice:'이 검사는 검토 증거의 존재와 일치 여부를 확인합니다. 법률 검토·실측 보안 점검·현장 검증의 내용을 대신하지 않습니다.'};
}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  const result=await checkProductionReadiness({manifestPath:process.env.READX_READINESS_MANIFEST});console.log(JSON.stringify(result,null,2));if(!result.ready)process.exitCode=1;
}
