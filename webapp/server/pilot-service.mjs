import {canTeachClass,activeAccount} from '../shared/organization.mjs';
import {restrictionIds} from '../shared/processing-restrictions.mjs';
import {pilotCatalog,pilotHash,pilotPublicItem} from './pilot-content.mjs';
import {placementFormAtVersion} from './placement-content.mjs';
import {pilotRows,itemStatistics,learnerStatistics,pilotPolicy,supportRank,mergeSupport} from './pilot-statistics.mjs';
import {ACCESS_META} from '../shared/access-meta.mjs';
const fail=(status,message)=>{throw Object.assign(Error(message),{status});};
const text=(v,max=2000)=>typeof v==='string'&&v.trim()&&v.length<=max;
const uuid=v=>typeof v==='string'&&/^[a-zA-Z0-9-]{16,100}$/.test(v);
export function createPilotService({db,lessons,randomUUID}){
 for(const t of ['pilot_sessions','pilot_runs','pilot_item_reviews','pilot_calibrations'])db.exec(`CREATE TABLE IF NOT EXISTS ${t}(id TEXT PRIMARY KEY,tenant_id TEXT NOT NULL,body TEXT NOT NULL)`);
 db.exec('CREATE INDEX IF NOT EXISTS pilot_runs_tenant ON pilot_runs(tenant_id)');
 const catalog=pilotCatalog(lessons),byKey=new Map(catalog.map(i=>[i.key,i]));
 const all=(table,tenant)=>db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r=>JSON.parse(r.body));
 const get=(table,id,tenant)=>{const row=db.prepare(`SELECT body FROM ${table} WHERE id=? AND tenant_id=?`).get(tenant+':'+id,tenant);return row?JSON.parse(row.body):null;};
 const put=(table,r,tenant)=>db.prepare(`INSERT INTO ${table} VALUES(?,?,?) ON CONFLICT(id) DO UPDATE SET body=excluded.body`).run(tenant+':'+r.id,tenant,JSON.stringify(r));
 const item=key=>{const i=byKey.get(key);if(!i)fail(404,'문항을 확인해 주세요.');return i;};
 const reviewId=(u,i)=>u.id+':'+i.key+':'+i.contentHash;
 const safeRun=run=>{const {items,observations,pulse,reviewHistory,exposure,...r}=run;return {...r,items:items.map(pilotPublicItem),reviewedItems:Object.keys(observations||{}).length};};
 const safeSummary=run=>({id:run.id,sessionId:run.sessionId,name:run.name,grade:run.grade,status:run.status,total:run.items.length,startedAt:run.startedAt,submittedAt:run.submittedAt});
 return ({user:u,state,path,method,body,at})=>{
  if(u.role==='parent')fail(403,'파일럿 원자료는 학생과 담당 교사가 확인합니다.');
  const blocked=restrictionIds(state,at);
  const allowed=s=>s?.tenantId===u.tenantId&&s.role==='student'&&!blocked.has(s.id)&&activeAccount(s,at)&&(u.role==='teacher'?canTeachClass(u,s.classId):s.id===u.id);
  const student=id=>{const s=state.users.find(s=>s.id===id);if(!allowed(s))fail(404,'담당 재원 학생을 확인해 주세요.');return s;};
  const teacher=()=>{if(u.role!=='teacher')fail(403,'교사 권한이 필요합니다.');};
  const ownRun=id=>{const r=get('pilot_runs',id,u.tenantId);if(!r)fail(404,'파일럿 기록을 찾을 수 없습니다.');student(r.studentId);if(u.role==='teacher'&&r.teacherId!==u.id)fail(404,'배정한 파일럿을 확인해 주세요.');return r;};
  const audit=(action,id)=>state.audit.push({at,actor:u.id,action,id});
  const runs=()=>all('pilot_runs',u.tenantId).filter(r=>r.teacherId===u.id&&allowed(state.users.find(s=>s.id===r.studentId)));
  const currentReview=i=>get('pilot_item_reviews',reviewId(u,i),u.tenantId);
  const analysis=()=>{const records=runs(),rows=pilotRows(records);return {records,rows,statistics:catalog.map(i=>itemStatistics(i,rows))};};
  const calibration=(i,stats)=>{const saved=get('pilot_calibrations',reviewId(u,i),u.tenantId);return saved?{...saved,current:saved.datasetHash===stats.datasetHash&&currentReview(i)?.status==='approved'}:null;};
  const runView=r=>({...r,studentName:state.users.find(s=>s.id===r.studentId)?.name,rows:pilotRows([r])});
  if(path==='/learning/pilot'&&method==='GET'){
   if(u.role==='student')return {runs:all('pilot_runs',u.tenantId).filter(r=>r.studentId===u.id).map(safeSummary)};
   teacher();const a=analysis();
   return {policy:pilotPolicy,catalog:catalog.map(i=>{const stat=a.statistics.find(s=>s.itemKey===i.key);return {key:i.key,grade:i.grade,kind:i.kind,skill:i.skill,branch:i.branch,title:i.title,prompt:i.question.prompt,contentHash:i.contentHash,editorialBand:i.question.difficulty.band,review:currentReview(i),statistics:stat,calibration:calibration(i,stat)};}),
    students:state.users.filter(allowed).map(s=>({id:s.id,name:s.name,classId:s.classId})),
    sessions:all('pilot_sessions',u.tenantId).filter(s=>s.teacherId===u.id).map(s=>({id:s.id,name:s.name,grade:s.grade,itemKeys:s.items.map(i=>i.key),createdAt:s.createdAt,students:s.studentIds.filter(id=>allowed(state.users.find(s=>s.id===id)))})),
    learners:a.records.map(r=>({...learnerStatistics(r,a.rows),studentName:state.users.find(s=>s.id===r.studentId)?.name,name:r.name}))};
  }
  if(path==='/learning/pilot/item'&&method==='POST'){
   teacher();const i=item(body.itemKey),a=analysis(),stats=a.statistics.find(s=>s.itemKey===i.key);
   return {item:i,review:currentReview(i),statistics:stats,calibration:calibration(i,stats)};
  }
  if(path==='/learning/pilot/review'&&method==='POST'){
   teacher();const i=item(body.itemKey),old=currentReview(i);
   if(body.contentHash!==i.contentHash||body.revision!==(old?.revision||0))fail(409,'최신 문항과 교사 검수 기록을 불러와 주세요.');
   if(!['approved','needs_revision'].includes(body.status)||!text(body.note)||body.status==='approved'&&!['difficulty','answer','evidence','explanation'].every(k=>body.checks?.[k]===true))fail(400,'난이도·정답·근거·해설을 확인하고 검수 의견을 남겨 주세요.');
   const r={id:reviewId(u,i),teacherId:u.id,itemKey:i.key,contentHash:i.contentHash,revision:(old?.revision||0)+1,status:body.status,checks:Object.fromEntries(['difficulty','answer','evidence','explanation'].map(k=>[k,body.checks?.[k]===true])),note:body.note.trim(),by:u.id,at,history:[...(old?.history||[]),...(old?[{...old,history:undefined}]:[])]};
   put('pilot_item_reviews',r,u.tenantId);audit('pilot.item.review',i.key);return {review:r};
  }
  if(path==='/learning/pilot/create'&&method==='POST'){
   teacher();
   if(!uuid(body.mutationId)||!text(body.name,100)||!Array.isArray(body.itemKeys)||!body.itemKeys.length||body.itemKeys.length>32||new Set(body.itemKeys).size!==body.itemKeys.length||!Array.isArray(body.studentIds)||!body.studentIds.length||body.studentIds.length>100||new Set(body.studentIds).size!==body.studentIds.length)fail(400,'수업 이름·문항(최대 32개)·학생(최대 100명)을 확인해 주세요.');
   const fingerprint=pilotHash({name:body.name.trim(),itemKeys:body.itemKeys,studentIds:body.studentIds});
   const previous=all('pilot_sessions',u.tenantId).find(s=>s.teacherId===u.id&&s.mutationId===body.mutationId);
   if(previous){if(previous.fingerprint!==fingerprint)fail(409,'중복 배정 요청의 내용이 다릅니다.');return {sessionId:previous.id};}
   body.studentIds.forEach(student);const items=body.itemKeys.map(item);
   if(new Set(items.map(i=>i.grade)).size!==1)fail(400,'한 파일럿에는 같은 학년의 문항을 배정해 주세요.');
   if(new Set(items.map(i=>pilotHash({paragraphs:i.paragraphs,prompt:i.question.prompt,options:i.question.options}))).size!==items.length)fail(400,'같은 본문과 질문의 중복 문항은 한 번만 배정해 주세요.');
   if(items.some(i=>currentReview(i)?.status!=='approved'))fail(409,'모든 문항의 교사 검수를 승인한 뒤 배정해 주세요.');
   const a=analysis(),snapshots=items.map(i=>{const c=calibration(i,a.statistics.find(s=>s.itemKey===i.key));return {...structuredClone(i),teacherReview:structuredClone(currentReview(i)),...(c?.current?{pilotCalibration:structuredClone(c)}:{})};});
   const session={id:randomUUID(),teacherId:u.id,name:body.name.trim(),grade:items[0].grade,items:snapshots,studentIds:body.studentIds,createdAt:at,mutationId:body.mutationId,fingerprint,policy:pilotPolicy};put('pilot_sessions',session,u.tenantId);
   for(const studentId of body.studentIds)put('pilot_runs',{id:randomUUID(),sessionId:session.id,teacherId:u.id,studentId,classId:student(studentId).classId,grade:session.grade,name:session.name,items:snapshots,status:'assigned',revision:0,answers:{},presented:{},times:{},exposure:{},observations:{},createdAt:at},u.tenantId);
   audit('pilot.create',session.id);return {sessionId:session.id,studentIds:body.studentIds};
  }
  if(path==='/learning/pilot/run'&&method==='POST'){teacher();return {run:runView(ownRun(body.runId))};}
  if(path==='/learning/pilot/start'&&method==='POST'){
   if(u.role!=='student')fail(403,'학생 계정으로 시작해 주세요.');const r=ownRun(body.runId);
   if(r.status==='assigned'){
    const earlier=all('pilot_runs',u.tenantId).filter(v=>v.studentId===u.id&&v.id!==r.id&&v.startedAt!=null),placement=get('learning_placements',u.id,u.tenantId),course=get('learning_courses',u.id,u.tenantId);
    for(const i of r.items){const seenPilot=earlier.some(v=>v.items.some(x=>x.familyId===i.familyId&&v.presented[x.key]));
     const seenCourse=course?.exposures?.some(e=>e.familyId===i.familyId);
     const seenDiagnostic=i.kind==='diagnostic'&&placement?.grade===i.grade&&(placement.formSnapshot||placementFormAtVersion(placement.grade,placement.branch,placement.version)).questions.some(q=>q.passageId===i.question.passageId&&placement.answers[q.id]);
     r.exposure[i.key]=seenPilot||seenCourse||seenDiagnostic?'repeat':'new';}
    r.status='in_progress';r.startedAt=at;put('pilot_runs',r,u.tenantId);audit('pilot.start',r.id);
   }return {run:safeRun(r)};
  }
  if(path==='/learning/pilot/pulse'&&method==='POST'){
   if(u.role!=='student')fail(403,'학생 계정으로 진행해 주세요.');const r=ownRun(body.runId);
   if(r.status!=='in_progress')return {times:r.times};
   if(!r.items.some(i=>i.key===body.itemKey)||!uuid(body.lease)||typeof body.active!=='boolean')fail(400,'현재 문항과 활동 상태를 확인해 주세요.');
   // A lease belongs to one visible browser. Other tabs cannot claim elapsed
   // time while its heartbeat is alive. Missing heartbeats never add long gaps.
   if(r.pulse&&r.pulse.lease!==body.lease&&at-r.pulse.at<pilotPolicy.heartbeatGapMs)return {times:r.times,leaseBusy:true};
   if(r.pulse?.lease===body.lease&&r.pulse.active&&at-r.pulse.at>=0&&at-r.pulse.at<=pilotPolicy.heartbeatGapMs)r.times[r.pulse.itemKey]=(r.times[r.pulse.itemKey]||0)+(at-r.pulse.at);
   r.pulse={lease:body.lease,itemKey:body.itemKey,active:body.active,at};if(body.active)r.presented[body.itemKey]??=at;
   put('pilot_runs',r,u.tenantId);return {times:r.times};
  }
  if(path==='/learning/pilot/answer'&&method==='POST'){
   if(u.role!=='student')fail(403,'학생 계정으로 응답해 주세요.');const r=ownRun(body.runId),i=r.items.find(i=>i.key===body.itemKey);
   if(r.status!=='in_progress'||!i)fail(409,'진행 중인 문항을 확인해 주세요.');
   const a=body.answer,oral=i.grade<=2&&!i.question.options.length&&a?.responseMode==='oral_requested';if(!a||typeof a.omitted!=='boolean'||!Object.hasOwn(supportRank,a.support)||typeof a.text!=='string'||a.text.length>2000||!Array.isArray(a.evidence)||a.evidence.some(v=>!Number.isInteger(v)||v<0||v>=i.paragraphs.length)||!a.omitted&&(i.question.options.length?!(Number.isInteger(a.choice)&&a.choice>=0&&a.choice<i.question.options.length):!oral&&!a.text.trim()))fail(400,'선택·설명·도움 여부를 확인해 주세요.');
   const next={choice:a.omitted||!i.question.options.length?null:a.choice,text:a.text.trim(),evidence:[...new Set(a.evidence)].sort(),omitted:a.omitted,...(oral?{responseMode:'oral_requested'}:{}),support:mergeSupport(r.answers[i.key]?.support||'independent',a.support)};
   if(JSON.stringify(r.answers[i.key])===JSON.stringify(next))return {run:safeRun(r)};
   if(body.revision!==r.revision)fail(409,'다른 화면의 답이 변경되었습니다. 최신 파일럿을 불러와 주세요.');
   r.answers[i.key]=next;r.presented[i.key]??=at;r.revision++;put('pilot_runs',r,u.tenantId);return {run:safeRun(r)};
  }
  if(path==='/learning/pilot/submit'&&method==='POST'){
   if(u.role!=='student')fail(403,'학생 계정으로 제출해 주세요.');const r=ownRun(body.runId);if(r.status==='submitted')return {run:safeRun(r)};
   if(r.status!=='in_progress'||!Object.keys(r.presented).length)fail(409,'파일럿 문항을 먼저 열어 주세요.');if(body.revision!==r.revision)fail(409,'최신 답안을 불러와 주세요.');
   if(r.pulse?.active&&at-r.pulse.at>=0&&at-r.pulse.at<=pilotPolicy.heartbeatGapMs)r.times[r.pulse.itemKey]=(r.times[r.pulse.itemKey]||0)+at-r.pulse.at;
   delete r.pulse;r.status='submitted';r.submittedAt=at;r.revision++;put('pilot_runs',r,u.tenantId);audit('pilot.submit',r.id);return {run:safeRun(r)};
  }
  if(path==='/learning/pilot/observe'&&method==='POST'){
   teacher();const r=ownRun(body.runId),i=r.items.find(i=>i.key===body.itemKey);if(r.status!=='submitted'||!i||r.presented[i.key]==null)fail(409,'제출된 실제 응시 문항을 확인해 주세요.');
   if(body.revision!==r.revision)fail(409,'최신 관찰 기록을 불러와 주세요.');
   if(!['unknown',...Object.keys(supportRank)].includes(body.assistance)||!['new','repeat','unknown'].includes(body.priorExposure)||!['success','needs_support','unscorable'].includes(body.rubric)||!text(body.note)||body.observedMs!=null&&(!Number.isInteger(body.observedMs)||body.observedMs<=0||body.observedMs>7200000))fail(400,'실제 도움·이전 노출·설명 판단·관찰 의견과 시간을 확인해 주세요.');
   const oral=r.answers[i.key]?.responseMode==='oral_requested';if(oral&&!text(body.transcript))fail(400,'학생이 실제로 말한 내용을 받아 적어 주세요.');
   const old=r.observations[i.key];r.reviewHistory||=[];if(old)r.reviewHistory.push({itemKey:i.key,...old});
   const maxAssistance=mergeSupport(old?.maxAssistance||'independent',Object.hasOwn(supportRank,body.assistance)?body.assistance:'independent');
   const assistance=body.assistance==='unknown'?'unknown':maxAssistance;
   r.observations[i.key]={assistance,maxAssistance,...(oral?{transcript:body.transcript.trim()}:{}),priorExposure:old?.priorExposure==='repeat'?'repeat':body.priorExposure,rubric:body.rubric,note:body.note.trim(),observedMs:body.observedMs??null,by:u.id,at,revision:(old?.revision||0)+1};
   r.revision++;put('pilot_runs',r,u.tenantId);audit('pilot.observe',r.id);return {run:runView(r)};
  }
  if(path==='/learning/pilot/calibrate'&&method==='POST'){
   teacher();const i=item(body.itemKey),stats=analysis().statistics.find(s=>s.itemKey===i.key),old=get('pilot_calibrations',reviewId(u,i),u.tenantId);
   if(body.datasetHash!==stats.datasetHash||body.revision!==(old?.revision||0))fail(409,'표본 또는 보정 이력이 달라졌습니다. 최신 분석을 불러와 주세요.');
   if(currentReview(i)?.status!=='approved'||stats.status!=='proposal'||body.confirmed!==true||!text(body.note))fail(409,'교사 검수·첫 독립 수행 20명 이상과 보정 의견을 확인해 주세요.');
   const c={id:reviewId(u,i),teacherId:u.id,itemKey:i.key,contentHash:i.contentHash,datasetHash:stats.datasetHash,band:stats.suggestedBand,n:stats.independentN,p:stats.p,interval:stats.interval,medianActiveMs:stats.medianActiveMs,policy:pilotPolicy,by:u.id,at,note:body.note.trim(),revision:(old?.revision||0)+1,history:[...(old?.history||[]),...(old?[{...old,history:undefined}]:[])]};
   put('pilot_calibrations',c,u.tenantId);audit('pilot.calibrate',i.key);return {calibration:{...c,current:true}};
  }
  if(path==='/learning/pilot/export'&&method==='POST'){
   teacher();const a=analysis();return {exportedAt:at,policy:pilotPolicy,learners:a.records.map(r=>({...learnerStatistics(r,a.rows),studentName:state.users.find(s=>s.id===r.studentId)?.name})),observations:a.rows,items:a.statistics,[ACCESS_META]:{subjects:[...new Set(a.records.map(r=>r.studentId))],records:a.rows.length}};
  }
  fail(404,'파일럿 요청을 찾을 수 없습니다.');
 };
}
