import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync,rmSync,writeFileSync,mkdirSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {randomBytes} from 'node:crypto';
import {verifyPrivateArtifacts} from '../scripts/verify-private-artifacts.mjs';
test('public build gate rejects renamed databases, encrypted backups, keyrings and recovery state while allowing design tokens',t=>{
 const dir=mkdtempSync(join(tmpdir(),'readx-artifact-'));t.after(()=>rmSync(dir,{recursive:true,force:true}));writeFileSync(join(dir,'index.html'),'<!doctype html><title>가상 체험</title>');writeFileSync(join(dir,'tokens.json'),JSON.stringify({palette:{primary:'#116650'}}));assert.equal(verifyPrivateArtifacts(dir).privateArtifacts,0);
 for(const [name,bytes]of [['renamed.bin',Buffer.from('SQLite format 3\0private')],['renamed.bin',Buffer.from('READX-BACKUP-1\nprivate')],['renamed.bin',Buffer.from('READX-AUDIT-1\nprivate')],['runtime.readxaudit','{}'],['runtime.readxaudit.partial-test','{}'],['settings.JSON',JSON.stringify({activeId:'local',keys:{local:randomBytes(32).toString('base64')}})],['state.ndjson',JSON.stringify({databaseId:'private',event:{type:'identity'},keyId:'local'})],['anchor.json',JSON.stringify({databaseId:'private',signature:'signed',keyId:'local',seq:1})],['runtime.recovery-keys.json','{}'],['runtime.backup-keys.json','{}'],['runtime.restore.pending','{}']]){const path=join(dir,name);writeFileSync(path,bytes);assert.throws(()=>verifyPrivateArtifacts(dir));rmSync(path);}
 mkdirSync(join(dir,'.readx-backup-stage-private'));assert.throws(()=>verifyPrivateArtifacts(dir));
});
