import {pilotHash} from './pilot-content.mjs';
export const pilotPolicy={version:'classroom-pilot-1',minIndependent:20,easyAt:.8,coreAt:.5,confidence:.95,heartbeatGapMs:15000};
export const supportRank={independent:0,prompted:1,read_aloud:2,answer_shown:3};
export const mergeSupport=(a,b)=>supportRank[a]>supportRank[b]?a:b;
export function wilson(correct,n){if(!n)return null;const z=1.959963984540054,p=correct/n,d=1+z*z/n,mid=(p+z*z/(2*n))/d,half=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d;return [Math.max(0,mid-half),Math.min(1,mid+half)];}
const median=values=>{if(!values.length)return null;const s=[...values].sort((a,b)=>a-b),m=Math.floor(s.length/2);return s.length%2?s[m]:(s[m-1]+s[m])/2;};
export function pilotRows(runs){return runs.flatMap(run=>run.items.map((item,index)=>{
 const a=run.answers[item.key],o=run.observations?.[item.key],support=o?.assistance==='unknown'||!o?'unknown':mergeSupport(a?.support||'independent',o.assistance);
 const presented=run.presented[item.key]!=null,complete=run.status==='submitted';
 const correct=complete&&presented?(!a||a.omitted?false:item.question.options.length?a.choice===item.question.answer:o?.rubric==='success'):null;
 return {runId:run.id,sessionId:run.sessionId,studentId:run.studentId,classId:run.classId,grade:run.grade,position:index+1,itemKey:item.key,contentHash:item.contentHash,familyId:item.familyId,kind:item.kind,choiceItem:!!item.question.options.length,
  presented,complete,exposure:run.exposure?.[item.key]==='repeat'?'repeat':o?.priorExposure||'unknown',startedAt:run.startedAt,presentedAt:run.presented[item.key]??null,submittedAt:run.submittedAt||null,
  answerState:!presented?'not_reached':!a||a.omitted?'omitted':'answered',choice:a?.choice??null,correct,support,reviewed:!!o,reviewRevision:o?.revision||0,rubric:o?.rubric||'pending',
  activeMs:o?.observedMs??(run.times[item.key]>0?run.times[item.key]:null),timeSource:o?.observedMs!=null?'teacher_observed':run.times[item.key]>0?'active_heartbeat':'missing'};
 }));}
export function itemStatistics(item,rows){
 const all=rows.filter(r=>r.itemKey===item.key&&r.contentHash===item.contentHash);
 // Earliest presentation is selected before eligibility: a helped first attempt
 // cannot be replaced by a later successful independent retry.
 const first=[...all].filter(r=>r.presented).sort((a,b)=>a.presentedAt-b.presentedAt||a.runId.localeCompare(b.runId)).filter((r,i,list)=>list.findIndex(v=>v.studentId===r.studentId)===i);
 const eligible=first.filter(r=>r.complete&&r.reviewed&&r.support==='independent'&&r.exposure==='new'&&r.rubric!=='unscorable');
 const correct=eligible.filter(r=>r.correct).length,n=eligible.length,p=n?correct/n:null,interval=wilson(correct,n),band=p===null?null:p>=pilotPolicy.easyAt?'입문':p>=pilotPolicy.coreAt?'기본':'도전';
 return {itemKey:item.key,contentHash:item.contentHash,attempts:all.length,presented:all.filter(r=>r.presented).length,notReached:all.filter(r=>!r.presented&&r.complete).length,
  firstStudents:first.length,independentN:n,correct,p,interval,medianActiveMs:median(eligible.map(r=>r.activeMs).filter(v=>v!=null)),timedN:eligible.filter(r=>r.activeMs!=null).length,
  assisted:first.filter(r=>r.support!=='unknown'&&r.support!=='independent').length,unknownHelp:first.filter(r=>r.support==='unknown').length,repeat:first.filter(r=>r.exposure==='repeat').length,unknownExposure:first.filter(r=>r.exposure==='unknown').length,
  pending:first.filter(r=>!r.complete||!r.reviewed).length,unscorable:first.filter(r=>r.reviewed&&r.rubric==='unscorable').length,omitted:eligible.filter(r=>r.answerState==='omitted').length,
  choiceCounts:item.question.options.map((_,i)=>eligible.filter(r=>r.choice===i).length),suggestedBand:n>=pilotPolicy.minIndependent?band:null,
  status:n>=pilotPolicy.minIndependent?'proposal':'collecting',boundaryUncertain:!!interval&&[pilotPolicy.coreAt,pilotPolicy.easyAt].some(b=>interval[0]<b&&interval[1]>b),
  datasetHash:pilotHash({policy:pilotPolicy,contentHash:item.contentHash,rows:all.filter(r=>r.presented).sort((a,b)=>a.runId.localeCompare(b.runId))})};
}
export function learnerStatistics(run,rows){
 const own=rows.filter(r=>r.runId===run.id),presented=own.filter(r=>r.complete&&r.presented),mc=presented.filter(r=>r.choiceItem),scoredOpen=presented.filter(r=>!r.choiceItem&&r.reviewed&&r.rubric!=='unscorable');
 return {runId:run.id,sessionId:run.sessionId,studentId:run.studentId,grade:run.grade,status:run.status,assigned:own.length,presented:presented.length,notReached:own.filter(r=>!r.presented&&r.complete).length,
  choiceCorrect:mc.filter(r=>r.correct).length,choiceTotal:mc.length,choiceAccuracy:mc.length?mc.filter(r=>r.correct).length/mc.length:null,
  openSuccess:scoredOpen.filter(r=>r.correct).length,openReviewed:scoredOpen.length,pending:presented.filter(r=>!r.reviewed).length,
  activeMs:own.some(r=>r.activeMs!=null)?own.reduce((sum,r)=>sum+(r.activeMs||0),0):null,timedItems:own.filter(r=>r.activeMs!=null).length,
  assisted:presented.filter(r=>!['independent','unknown'].includes(r.support)).length,unknownHelp:presented.filter(r=>r.support==='unknown').length};
}
