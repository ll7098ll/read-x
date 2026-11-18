import {randomUUID} from 'node:crypto';
import {auditSigner} from './audit-keys.mjs';
import {ACCESS_META} from '../shared/access-meta.mjs';

const zero='0'.repeat(64),fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const envelope=row=>JSON.stringify(['readx-access-v1',row.seq,row.key_id,row.prev_hash,row.body]);
const cpPayload=c=>JSON.stringify(['readx-access-checkpoint-v1',c.databaseId,c.seq,c.hash,c.createdAt,c.keyId]);
const validDay=d=>typeof d==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(d)&&Number.isFinite(Date.parse(d))&&new Date(d).toISOString().slice(0,10)===d;
const day=at=>new Date(at+9*3600000).toISOString().slice(0,10);

export function createAccessLog({db,dbPath,keyring,readOnly=false}){
  if(!readOnly)db.exec(`CREATE TABLE IF NOT EXISTS access_log_identity (id INTEGER PRIMARY KEY CHECK(id=1), database_id TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS access_log (seq INTEGER PRIMARY KEY, tenant_id TEXT NOT NULL, at INTEGER NOT NULL, category TEXT NOT NULL, status INTEGER NOT NULL, actor_id TEXT, body TEXT NOT NULL, prev_hash TEXT NOT NULL, hash TEXT NOT NULL, key_id TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS access_log_subjects (seq INTEGER NOT NULL REFERENCES access_log(seq), tenant_id TEXT NOT NULL, subject_id TEXT NOT NULL, PRIMARY KEY(seq,subject_id));
    CREATE INDEX IF NOT EXISTS access_log_tenant ON access_log(tenant_id,at,seq);
    CREATE INDEX IF NOT EXISTS access_log_subject ON access_log_subjects(tenant_id,subject_id,seq);
    CREATE TRIGGER IF NOT EXISTS access_log_no_update BEFORE UPDATE ON access_log BEGIN SELECT RAISE(ABORT,'access log is append only'); END;
    CREATE TRIGGER IF NOT EXISTS access_log_no_delete BEFORE DELETE ON access_log BEGIN SELECT RAISE(ABORT,'access log is append only'); END;
    CREATE TRIGGER IF NOT EXISTS access_subject_no_update BEFORE UPDATE ON access_log_subjects BEGIN SELECT RAISE(ABORT,'access log is append only'); END;
    CREATE TRIGGER IF NOT EXISTS access_subject_no_delete BEFORE DELETE ON access_log_subjects BEGIN SELECT RAISE(ABORT,'access log is append only'); END;
    CREATE TRIGGER IF NOT EXISTS access_identity_no_update BEFORE UPDATE ON access_log_identity BEGIN SELECT RAISE(ABORT,'access identity is immutable'); END;
    CREATE TRIGGER IF NOT EXISTS access_identity_no_delete BEFORE DELETE ON access_log_identity BEGIN SELECT RAISE(ABORT,'access identity is immutable'); END;
    CREATE TRIGGER IF NOT EXISTS access_log_chain BEFORE INSERT ON access_log WHEN NEW.seq != COALESCE((SELECT MAX(seq)+1 FROM access_log),1) OR NEW.prev_hash != COALESCE((SELECT hash FROM access_log ORDER BY seq DESC LIMIT 1),'${zero}') BEGIN SELECT RAISE(ABORT,'access log chain mismatch'); END;`);
  if(!readOnly)db.prepare('INSERT OR IGNORE INTO access_log_identity VALUES(1,?)').run(randomUUID());
  const databaseId=db.prepare('SELECT database_id FROM access_log_identity WHERE id=1').get()?.database_id;
  if(!databaseId)throw Error('접속기록 저장소 식별자가 없습니다.');
  const signer=auditSigner({dbPath,keyring,hasRecords:!!db.prepare('SELECT 1 FROM access_log LIMIT 1').get()}),tail=()=>db.prepare('SELECT * FROM access_log ORDER BY seq DESC LIMIT 1').get();
  let expected=null;
  const verify=checkpoint=>{
    let seq=0,hash=zero,anchored=!checkpoint,indexedCount=0;const keyIds=new Set();
    if(checkpoint&&(checkpoint.databaseId!==databaseId||!Number.isSafeInteger(checkpoint.seq)||checkpoint.seq<0||!signer.verify(cpPayload(checkpoint),checkpoint.signature,checkpoint.keyId)))throw Error('접속기록 외부 기준점이 맞지 않습니다.');
    if(checkpoint?.seq===0&&checkpoint.hash===zero)anchored=true;
    for(const row of db.prepare('SELECT * FROM access_log ORDER BY seq').iterate()){
      if(row.seq!==seq+1||row.prev_hash!==hash||!signer.verify(envelope(row),row.hash,row.key_id))throw Error('접속기록 무결성 검사에 실패했습니다.');
      const event=JSON.parse(row.body);
      if(event.databaseId!==databaseId||event.tenantId!==row.tenant_id||event.at!==row.at||event.category!==row.category||event.status!==row.status||event.actorId!==row.actor_id||!Array.isArray(event.subjects))throw Error('접속기록 색인과 본문이 일치하지 않습니다.');
      const indexed=db.prepare('SELECT subject_id FROM access_log_subjects WHERE seq=? AND tenant_id=? ORDER BY subject_id').all(row.seq,row.tenant_id).map(v=>v.subject_id);
      if(JSON.stringify(indexed)!==JSON.stringify(event.subjects))throw Error('접속기록 대상 색인이 일치하지 않습니다.');
      indexedCount+=indexed.length;
      seq=row.seq;hash=row.hash;keyIds.add(row.key_id);if(checkpoint?.seq===seq&&checkpoint.hash===hash)anchored=true;
    }
    if(db.prepare('SELECT COUNT(*) n FROM access_log_subjects').get().n!==indexedCount)throw Error('접속기록 대상 색인이 일치하지 않습니다.');
    if(!anchored)throw Error('접속기록이 별도 보관한 기준점보다 짧거나 변경되었습니다.');
    return {ok:true,count:seq,head:{seq,hash},keyIds:[...keyIds],externalCheckpoint:!!checkpoint};
  };
  const initial=verify();expected=initial.head;
  const assertHead=()=>{const row=tail();if(row?.seq>expected.seq){const old=expected.seq?db.prepare('SELECT hash FROM access_log WHERE seq=?').get(expected.seq)?.hash:zero;if(old!==expected.hash)throw Error('접속기록 이전 기준점이 변경되었습니다.');expected=verify().head;}if((row?.seq||0)!==expected.seq||(row?.hash||zero)!==expected.hash||row&&!signer.verify(envelope(row),row.hash,row.key_id))throw Error('접속기록 끝부분이 변경되었습니다.');};
  const append=event=>{
    if(readOnly)throw Error('읽기 전용 접속기록 도구입니다.');assertHead();
    const row={seq:expected.seq+1,key_id:signer.activeId,prev_hash:expected.hash,body:JSON.stringify({v:1,databaseId,...event,eventId:randomUUID()})};row.hash=signer.sign(envelope(row));
    db.prepare('INSERT INTO access_log VALUES(?,?,?,?,?,?,?,?,?,?)').run(row.seq,event.tenantId,event.at,event.category,event.status,event.actorId,row.body,row.prev_hash,row.hash,row.key_id);
    for(const id of event.subjects)db.prepare('INSERT INTO access_log_subjects VALUES(?,?,?)').run(row.seq,event.tenantId,id);
    return {seq:row.seq,hash:row.hash};
  };
  const committed=()=>{const row=tail();expected={seq:row?.seq||0,hash:row?.hash||zero};};
  const checkpoint=(at=Date.now())=>{const {head}=verify();const c={v:1,databaseId,...head,createdAt:at,keyId:signer.activeId};return {...c,signature:signer.sign(cpPayload(c))};};
  const verifyArchive=(rows,c)=>{
    if(!Array.isArray(rows)||!c||c.databaseId!==databaseId||c.seq!==rows.length||!signer.verify(cpPayload(c),c.signature,c.keyId))throw Error('접속기록 보관본 기준점이 맞지 않습니다.');
    let seq=0,hash=zero;
    for(const row of rows){
      if(row.seq!==++seq||row.prev_hash!==hash||!signer.verify(envelope(row),row.hash,row.key_id))throw Error('접속기록 보관본 순서·서명이 맞지 않습니다.');
      const e=JSON.parse(row.body);
      if(e.databaseId!==databaseId||e.tenantId!==row.tenant_id||e.at!==row.at||e.category!==row.category||e.status!==row.status||e.actorId!==row.actor_id||!Array.isArray(e.subjects)||e.subjects.some(id=>typeof id!=='string')||JSON.stringify(e.subjects)!==JSON.stringify([...new Set(e.subjects)].sort()))throw Error('접속기록 보관본 본문·색인이 맞지 않습니다.');
      hash=row.hash;
    }
    if(c.hash!==hash)throw Error('접속기록 보관본 끝부분이 다릅니다.');
    const local=verify().head;
    for(const row of rows.slice(0,Math.min(local.seq,rows.length))){const own=db.prepare('SELECT * FROM access_log WHERE seq=?').get(row.seq);if(own.hash!==row.hash||own.body!==row.body)throw Error('복원 DB와 접속기록 보관본의 공통 기록이 다릅니다.');}
    return {archivedSeq:c.seq,localSeq:local.seq};
  };
  // Restore only signed original records. Never re-sign history or replace a prefix.
  const mergeArchive=(rows,c)=>{
    if(readOnly)throw Error('읽기 전용 접속기록 도구입니다.');
    const checked=verifyArchive(rows,c);
    let imported=0;db.exec('SAVEPOINT readx_access_archive_merge');
    try{
      for(const row of rows.slice(checked.localSeq)){
        db.prepare('INSERT INTO access_log VALUES(?,?,?,?,?,?,?,?,?,?)').run(row.seq,row.tenant_id,row.at,row.category,row.status,row.actor_id,row.body,row.prev_hash,row.hash,row.key_id);
        for(const id of JSON.parse(row.body).subjects)db.prepare('INSERT INTO access_log_subjects VALUES(?,?,?)').run(row.seq,row.tenant_id,id);
        imported++;
      }
      verify(c);db.exec('RELEASE readx_access_archive_merge');return {imported,archivedSeq:c.seq};
    }catch(e){db.exec('ROLLBACK TO readx_access_archive_merge; RELEASE readx_access_archive_merge');throw e;}
  };
  const filters=(u,body,at)=>{
    const startDate=body.startDate||day(at-6*86400000),endDate=body.endDate||day(at);
    if(!validDay(startDate)||!validDay(endDate)||startDate>endDate||Date.parse(endDate)-Date.parse(startDate)>90*86400000)fail(400,'접속기록은 한 번에 90일 이내로 조회해 주세요.');
    if(body.beforeSeq!=null&&(!Number.isSafeInteger(body.beforeSeq)||body.beforeSeq<1))fail(400,'다음 페이지 위치를 확인해 주세요.');
    if(body.category&&!['read','write','authentication','download','print','audit'].includes(body.category))fail(400,'올바른 업무 구분을 선택해 주세요.');
    if(body.outcome&&!['succeeded','denied','failed'].includes(body.outcome))fail(400,'올바른 처리 결과를 선택해 주세요.');
    for(const key of ['actorId','subjectId'])if(body[key]&&(typeof body[key]!=='string'||body[key].length>100))fail(400,'계정 식별자를 확인해 주세요.');
    let sql='FROM access_log a WHERE a.tenant_id=? AND a.at>=? AND a.at<=?',params=[u.tenantId,Date.parse(startDate+'T00:00:00+09:00'),Date.parse(endDate+'T23:59:59.999+09:00')];
    if(body.beforeSeq){sql+=' AND a.seq<?';params.push(body.beforeSeq);}if(body.category){sql+=' AND a.category=?';params.push(body.category);}if(body.actorId){sql+=' AND a.actor_id=?';params.push(body.actorId);}
    if(body.outcome)sql+=body.outcome==='succeeded'?' AND a.status<400':body.outcome==='denied'?' AND a.status>=400 AND a.status<500':' AND a.status>=500';
    if(body.subjectId){sql+=' AND EXISTS(SELECT 1 FROM access_log_subjects x WHERE x.seq=a.seq AND x.tenant_id=a.tenant_id AND x.subject_id=?)';params.push(body.subjectId);}
    return {sql,params,startDate,endDate};
  };
  const route=({user:u,state,path,method,body,at})=>{
    if(u.role!=='teacher'||!u.isOwner)fail(403,'접속기록은 학원 운영자만 확인할 수 있습니다.');
    if(method!=='POST')fail(405,'접속기록 조회 조건을 확인해 주세요.');
    const integrity=verify();
    if(path==='/audit/check')return {integrity,notice:'DB 내부 검사입니다. 별도 보관 기준점·키 분리·백업 운영 검증을 함께 수행해 주세요.'};
    if(path==='/audit/checkpoint')return {checkpoint:checkpoint(at),notice:'원본 DB·서버와 분리된 변경 방지 저장소에 보관하고 복원 시 검증하세요.'};
    if(path==='/audit/reviews'){
      if(!Number.isSafeInteger(body.fromSeq)||!Number.isSafeInteger(body.toSeq)||body.fromSeq<1||body.fromSeq>body.toSeq||body.toSeq>integrity.count||!['clear','investigate','resolved'].includes(body.finding)||typeof body.reference!=='string'||!/^[a-zA-Z0-9][a-zA-Z0-9._:/-]{2,99}$/.test(body.reference))fail(400,'실제 확인한 기록 범위·결과·점검 문서 번호를 확인해 주세요.');
      const count=db.prepare('SELECT COUNT(*) n FROM access_log WHERE tenant_id=? AND seq BETWEEN ? AND ?').get(u.tenantId,body.fromSeq,body.toSeq).n;if(!count)fail(400,'해당 학원의 확인할 기록이 없습니다.');
      return {ok:true,reviewedRecords:count,[ACCESS_META]:{review:{fromSeq:body.fromSeq,toSeq:body.toSeq,finding:body.finding,reference:body.reference},records:count}};
    }
    if(!['/audit/query','/audit/export'].includes(path))fail(404,'접속기록 요청을 찾을 수 없습니다.');
    const f=filters(u,body,at),limit=path==='/audit/export'?1000:100,rows=db.prepare('SELECT a.seq,a.body,a.hash,a.prev_hash,a.key_id '+f.sql+' ORDER BY a.seq DESC LIMIT ?').all(...f.params,limit+1),more=rows.length>limit;
    const entries=rows.slice(0,limit).map(r=>({seq:r.seq,...JSON.parse(r.body),hash:r.hash,keyId:r.key_id}));
    const actors=state.users.filter(v=>v.tenantId===u.tenantId).map(v=>({id:v.id,name:v.name,role:v.role,active:v.active}));
    const result={entries,nextBeforeSeq:more?entries.at(-1).seq:null,startDate:f.startDate,endDate:f.endDate,integrity,accounts:actors,notice:'인쇄 요청·파일 전달 기록이며 실제 인쇄 완료나 외부 파일 파기를 증명하지 않습니다.'};
    if(path==='/audit/export')return {json:JSON.stringify({v:1,entries,nextBeforeSeq:result.nextBeforeSeq,startDate:f.startDate,endDate:f.endDate,notice:result.notice}),records:entries.length,nextBeforeSeq:result.nextBeforeSeq,[ACCESS_META]:{subjects:[...new Set(entries.flatMap(e=>e.subjects))],records:entries.length}};
    return result;
  };
  return {append,committed,assertHead,verify,checkpoint,verifyArchive,mergeArchive,route,databaseId};
}
