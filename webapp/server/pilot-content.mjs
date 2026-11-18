import {createHash} from 'node:crypto';
import {placementForm} from './placement-content.mjs';
import {courseBundle,courseOrder,coursePolicy} from './course-content.mjs';
export const pilotHash=v=>createHash('sha256').update(JSON.stringify(v)).digest('hex');
export function pilotCatalog(lessons){
 const items=[];
 for(let grade=1;grade<=6;grade++){
  const seen=new Set(),common=placementForm(grade);
  for(const branch of [null,'support','extend'])for(const q of placementForm(grade,branch).questions){
   const phase=common.questions.some(c=>c.id===q.id)?'common':branch,key=`diagnostic:g${grade}:${phase}:${q.id}`;
   if(seen.has(key))continue;seen.add(key);
   const p=placementForm(grade,branch).passages.find(p=>p.id===q.passageId);
   items.push({key,grade,kind:'diagnostic',branch:phase,skill:q.skill,familyId:`diagnostic:g${grade}:${p.id}`,title:p.title,paragraphs:p.paragraphs,question:q,sourceVersion:common.version});
  }
  for(const skill of courseOrder)courseBundle(grade,skill,lessons).checks.forEach((q,i)=>items.push({key:`check:g${grade}:${skill}:${i}`,grade,kind:'check',skill,familyId:q.familyId,title:q.title,paragraphs:q.paragraphs,question:q,sourceVersion:coursePolicy}));
 }
 return items.map(item=>({...item,contentHash:pilotHash({key:item.key,sourceVersion:item.sourceVersion,paragraphs:item.paragraphs,question:item.question})}));
}
export const pilotPublicItem=item=>({key:item.key,grade:item.grade,title:item.title,paragraphs:item.paragraphs,kind:item.kind,skill:item.skill,prompt:item.question.prompt,options:item.question.options});
