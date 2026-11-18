import {restrictionIds} from '../shared/processing-restrictions.mjs';
import { canTeachClass } from '../shared/organization.mjs';
import { scoreAttempt } from '../shared/exam-engine.mjs';
import {ACCESS_META} from '../shared/access-meta.mjs';

const fail = (status, message) => { throw Object.assign(new Error(message), { status }); };
export const ratio = (numerator, denominator) => ({ numerator, denominator, percent: denominator ? Math.round(numerator / denominator * 1000) / 10 : null });
const day = at => new Date(at + 9 * 3600000).toISOString().slice(0, 10);
const validDay = value => /^\d{4}-\d{2}-\d{2}$/.test(value || '') && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0, 10) === value;
const week = at => { const date = new Date(day(at)+'T00:00:00Z'); date.setUTCDate(date.getUTCDate() - (date.getUTCDay()+6)%7); return date.toISOString().slice(0,10); };
const csvCell = value => { const s = String(value ?? ''); return '"'+(/^[\s]*[=+@-]/.test(s) ? "'"+s : s).replaceAll('"','""')+'"'; };
const statusNames = { not_started:'시작 전', in_progress:'학습 중', submitted:'제출·검토 대기', reviewed:'교사 검토', published:'보호자 공개', awaiting_release:'아직 공개된 결과 없음' };
export function overviewCsv(data) {
  const pair = r => r.denominator ? [r.numerator,r.denominator] : ['',''];
  const rows = [['구분','학생','반','과제','배정일','상태','활동 응답','활동 전체','첫 선택 정답','선택 채점 가능','첫 필요 근거 포함','근거 확인 가능','도움 사용','첫 응답 수','교사 설명 확인','교사 검토 수','평가 정답','평가 전체']];
  for (const r of data.records) rows.push([r.kind==='lesson'?'읽기 수업':'모의고사',r.studentName,r.className,r.title,day(r.assignedAt),statusNames[r.status],...pair(r.metrics.activities),...pair(r.metrics.firstChoice),...pair(r.metrics.firstEvidence),...pair(r.metrics.hints),...pair(r.metrics.teacherExplanation),...pair(r.metrics.examAccuracy)]);
  return '\ufeff'+rows.map(row=>row.map(csvCell).join(',')).join('\r\n');
}
const metrics = observations => {
  const first = observations.filter(o=>o.first), choice = first.filter(o=>typeof o.first.choiceMatch==='boolean'), evidence = first.filter(o=>typeof o.first.evidenceMatch==='boolean'), reviewed = observations.filter(o=>o.review);
  return { firstChoice:ratio(choice.filter(o=>o.first.choiceMatch).length,choice.length), firstEvidence:ratio(evidence.filter(o=>o.first.evidenceMatch).length,evidence.length), hints:ratio(first.filter(o=>o.first.hintLevel>0).length,first.length),
    teacherExplanation:ratio(reviewed.filter(o=>o.review.outcome==='success').length,reviewed.length), revisions:observations.filter(o=>o.submissions>1).length };
};
function summarize(records, parent, at) {
  const reading=records.filter(r=>r.kind==='lesson'),exams=records.filter(r=>r.kind==='exam'),observations=reading.flatMap(r=>r.observations);
  return { assigned:records.length, readingAssigned:reading.length, examsAssigned:exams.length,
    completion:parent?null:ratio(records.filter(r=>r.submittedAt).length,records.length), published:ratio(records.filter(r=>r.publishedAt).length,records.length),
    activities:ratio(reading.reduce((n,r)=>n+r.metrics.activities.numerator,0),reading.reduce((n,r)=>n+r.metrics.activities.denominator,0)), ...metrics(observations),
    examAccuracy:ratio(exams.reduce((n,r)=>n+r.metrics.examAccuracy.numerator,0),exams.reduce((n,r)=>n+r.metrics.examAccuracy.denominator,0)),
    pendingReview:parent?null:reading.filter(r=>r.submittedAt&&r.reviewedCount<r.questionCount).length,
    overdue:parent?null:records.filter(r=>!r.submittedAt&&r.dueAt<at).length };
}

export function createOverviewService({ db }) {
  const all = (table, tenant) => db.prepare(`SELECT body FROM ${table} WHERE tenant_id=?`).all(tenant).map(r=>JSON.parse(r.body));
  const route = ({ user:u, state:s, path, method, body, at }) => {
    if(!['/overview','/overview/export','/overview/print'].includes(path))fail(404,'리포트 요청을 찾을 수 없습니다.');
    if(!['GET','POST'].includes(method))fail(405,'조회 요청을 확인해 주세요.');
    if(path!=='/overview'&&method!=='POST')fail(405,'파일·인쇄 요청을 확인해 주세요.');
    const blocked=restrictionIds(s,at),records=[],releases=all('learning_releases',u.tenantId).filter(r=>!r.processingWithheld),runs=all('learning_runs',u.tenantId),assignments=all('learning_assignments',u.tenantId);
    const startDate=body.startDate || day(at-27*86400000),endDate=body.endDate || day(at);
    if(!validDay(startDate)||!validDay(endDate)||startDate>endDate||Date.parse(endDate)-Date.parse(startDate)>366*86400000) fail(400,'조회 기간은 올바른 날짜로 1년 이내에서 선택해 주세요.');
    const start=Date.parse(startDate+'T00:00:00+09:00'),end=Date.parse(endDate+'T23:59:59.999+09:00'),parent=u.role==='parent';
    const classes=s.classes.filter(c=>c.tenantId===u.tenantId&&(u.role==='teacher'?canTeachClass(u,c.id):true));
    if(body.classId&&(!classes.some(c=>c.id===body.classId)||u.role!=='teacher'))fail(403,'조회 가능한 반을 선택해 주세요.');
    const visibleStudent=id=>!blocked.has(id)&&(u.role==='teacher'||u.role==='student'&&id===u.id||parent&&u.childIds.includes(id));
    if(body.studentId&&!s.users.some(v=>v.id===body.studentId&&v.tenantId===u.tenantId&&v.role==='student'&&visibleStudent(v.id)&&(!body.classId||v.classId===body.classId)&&(u.role!=='teacher'||u.isOwner||canTeachClass(u,v.classId)||[...s.assignments,...assignments].some(a=>a.tenantId===u.tenantId&&a.studentIds.includes(v.id)&&canTeachClass(u,a.classId)))))fail(403,'조회 가능한 학생을 선택해 주세요.');

    const include=(a,id)=>a.createdAt>=start&&a.createdAt<=Math.min(at,end)&&visibleStudent(id)&&(!body.studentId||id===body.studentId)&&(!body.classId||a.classId===body.classId)&&(u.role!=='teacher'||canTeachClass(u,a.classId));
    const identity=(a,id)=>({studentId:id,studentName:s.users.find(v=>v.id===id)?.name||'학생',classId:a.classId,className:s.classes.find(c=>c.id===a.classId&&c.tenantId===u.tenantId)?.name||'이전 반',title:a.title,assignedAt:a.createdAt,dueAt:a.dueAt||a.closesAt});
    for(const a of assignments)for(const id of a.studentIds){
      if(!include(a,id))continue;
      const live=runs.find(r=>r.assignmentId===a.id&&r.studentId===id),release=live&&releases.find(r=>r.id===live.id),r=parent?release?.snapshot:live;
      const submitted=!!r?.submittedAt,qs=a.lesson.levelQuestions?.[a.level]||a.lesson.questions;
      const observations=submitted?qs.map(q=>{const subs=r.run.responses[q.id]?.submissions||[];return {id:r.id+':'+q.id,skill:q.skill,goalId:a.lesson.goalIds?.[0]||a.lesson.id,goalTitle:a.lesson.concept||a.lesson.title,first:subs[0]||null,submissions:subs.length,review:r.reviews?.[q.id]||null};}):[];
      const reviewedCount=observations.filter(o=>o.review).length,status=parent?release?'published':'awaiting_release':!r?'not_started':!submitted?'in_progress':r.publishedAt?'published':reviewedCount===qs.length?'reviewed':'submitted';
      const sample= submitted?qs.map(q=>({q,subs:r.run.responses[q.id]?.submissions||[]})).find(v=>v.subs.length):null;
      records.push({kind:'lesson',id:a.id+':'+id,assignmentId:a.id,runId:r?.id||null,...identity(a,id),dueAt:Math.max(r?.dueAtOverride||0,a.dueAt),level:a.level,lessonTitle:a.lesson.title,status,submittedAt:submitted?r.submittedAt:null,publishedAt:release?.publishedAt||null,
        questionCount:qs.length,reviewedCount,observations,metrics:{activities:ratio(observations.filter(o=>o.first).length,parent&&!release?0:qs.length),...metrics(observations),examAccuracy:ratio(0,0)},
        sample:sample?{prompt:sample.q.prompt,firstReason:sample.subs[0].reason,latestReason:sample.subs.at(-1).reason,teacherNote:r.note||'',writing:r.writing}:null});
    }
    for(const a of s.assignments.filter(a=>a.tenantId===u.tenantId))for(const id of a.studentIds){
      if(!include(a,id))continue;
      const r=s.attempts.find(r=>r.assignmentId===a.id&&r.studentId===id),submitted=r&&r.status!=='in_progress',released=!!(a.studentPublishedAt&&r?.parentPublishedAt),canScore=submitted&&(u.role==='teacher'||u.role==='student'&&a.studentPublishedAt||parent&&released);
      const result=canScore?scoreAttempt(r,a.form):null,status=parent?released?'published':'awaiting_release':!r?'not_started':!submitted?'in_progress':released?'published':'submitted';
      records.push({kind:'exam',id:a.id+':'+id,assignmentId:a.id,runId:parent&&!released?null:r?.id||null,...identity(a,id),status,submittedAt:parent&&!released?null:submitted?r.submittedAt:null,publishedAt:released?r.parentPublishedAt:null,questionCount:a.form.passages.flatMap(p=>p.questions).length,reviewedCount:0,observations:[],
        metrics:{activities:ratio(0,0),...metrics([]),examAccuracy:ratio(result?.correct||0,result?.total||0)},sample:canScore?{teacherNote:parent?r.publishedNote||'':r.note||'',firstReason:'',latestReason:'',writing:''}:null});
    }
    records.sort((a,b)=>b.assignedAt-a.assignedAt||a.id.localeCompare(b.id));
    const totals=summarize(records,parent,at);totals.overdue=parent?null:records.filter(r=>!r.submittedAt&&r.dueAt<at).length;
    const studentIds=[...new Set([...records.map(r=>r.studentId),...s.users.filter(v=>v.tenantId===u.tenantId&&v.role==='student'&&visibleStudent(v.id)&&(!body.classId||v.classId===body.classId)&&(u.role!=='teacher'||canTeachClass(u,v.classId))).map(v=>v.id)])];
    const observations=records.flatMap(r=>r.observations),group=(key,title)=>[...new Set(observations.map(o=>o[key]))].map(id=>{const os=observations.filter(o=>o[key]===id);return {id,title:os[0][title],...metrics(os),responses:os.filter(o=>o.first).length};});
    const weeks=[...new Set(records.map(r=>week(r.assignedAt)))].sort().map(start=>({start,...summarize(records.filter(r=>week(r.assignedAt)===start),parent,at)}));
    const allowedAttempts=new Set(records.filter(r=>r.kind==='exam'&&r.runId&&r.metrics.examAccuracy.denominator).map(r=>r.runId));
    const followups=s.followups.filter(f=>allowedAttempts.has(f.attemptId));
    const confirmed=followups.filter(f=>f.fresh&&f.completedAt&&f.teacherReview);
    const data={asOf:at,startDate,endDate,scope:parent?'공개된 자녀 수행 결과':'본인 또는 담당 범위의 실제 수행 기록',basis:'배정일이 조회 기간에 속하는 과제의 현재 처리 결과',
      organizationName:s.organizations.find(o=>o.id===u.tenantId)?.name||'학원',user:{id:u.id,name:u.name,role:u.role,isOwner:!!u.isOwner},
      classes:u.role==='teacher'?classes.map(c=>({id:c.id,name:c.name,active:c.active})):[],students:studentIds.map(id=>({id,name:s.users.find(v=>v.id===id)?.name||'학생'})),
      totals,weekly:weeks,skills:group('skill','skill'),goals:group('goalId','goalTitle'),
      followups:{assigned:followups.length,completed:followups.filter(f=>f.completedAt).length,confirmedTransfer:ratio(confirmed.filter(f=>f.correct&&f.teacherReview.outcome==='supported').length,confirmed.length)},
      byStudent:studentIds.filter(id=>!body.studentId||id===body.studentId).map(id=>({id,name:s.users.find(v=>v.id===id)?.name||'학생',...summarize(records.filter(r=>r.studentId===id),parent,at)})),
      records:records.map(({observations,...r})=>r)};
    data[ACCESS_META]={subjects:[...new Set(data.records.map(r=>r.studentId))],records:data.records.length};
    if(path==='/overview/export')return {csv:overviewCsv(data),records:data.records.length,[ACCESS_META]:data[ACCESS_META]};
    return data;
  };
  return {route};
}
