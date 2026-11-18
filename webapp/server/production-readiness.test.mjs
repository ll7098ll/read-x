import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp,rm,writeFile } from 'node:fs/promises';
import { resolve,join } from 'node:path';
import { tmpdir } from 'node:os';
import { checkProductionReadiness } from '../scripts/check-production-readiness.mjs';
import { productionRequirements } from './production-requirements.mjs';

test('운영 준비 증거에서 필수 항목을 삭제해도 준비 완료로 처리되지 않는다',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-readiness-'));if(!resolve(dir).startsWith(resolve(tmpdir())))throw Error('Unexpected temp directory');
  t.after(()=>rm(dir,{recursive:true,force:true}));
  const path=join(dir,'manifest.json');await writeFile(path,JSON.stringify({schemaVersion:1,operator:{legalName:'검사 전용',privacyContact:'검사 전용',operationsContact:'검사 전용'},controls:[]}));
  const result=await checkProductionReadiness({manifestPath:path,bundlePath:join(dir,'not-built.html')});assert.equal(result.ready,false);
  for(const [id] of productionRequirements)assert.ok(result.issues.some(issue=>issue.includes(id)));
});
test('검토 완료라고 표시해도 증거와 배포 파일이 다르면 운영 준비 검사를 통과하지 못한다',async t=>{
  const dir=await mkdtemp(join(tmpdir(),'readx-evidence-'));if(!resolve(dir).startsWith(resolve(tmpdir())))throw Error('Unexpected temp directory');
  t.after(()=>rm(dir,{recursive:true,force:true}));
  const path=join(dir,'manifest.json'),bundle=join(dir,'index.html');await writeFile(bundle,'검사 전용 변경된 파일');
  await writeFile(path,JSON.stringify({schemaVersion:1,operator:{legalName:'검사 전용',privacyContact:'검사 전용',operationsContact:'검사 전용'},bundleSha256:'outdated',controls:productionRequirements.map(([id])=>({id,status:'reviewed',reviewer:'검사 전용',reviewedAt:'2026-01-01',evidence:[{path:'index.html',sha256:'outdated'}]}))}));
  const result=await checkProductionReadiness({manifestPath:path,bundlePath:bundle});assert.equal(result.ready,false);assert.ok(result.issues.some(i=>i.includes('배포 산출물')));assert.ok(result.issues.some(i=>i.includes('증거 파일')));
});
