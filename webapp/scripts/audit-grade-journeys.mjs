import { readFileSync,writeFileSync,mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import assert from 'node:assert/strict';
import { learningGrades,courseOrder,gradeProfiles } from '../shared/learning-config.mjs';
import { courseBundle } from '../server/course-content.mjs';
import { placementForm,publicForm } from '../server/placement-content.mjs';
const lessons=JSON.parse(readFileSync(new URL('../src/data/corpusLessons.generated.json',import.meta.url)));
const root=fileURLToPath(new URL('../..',import.meta.url)),result={grades:[],courseCount:0,trainingLinks:0,checkVariants:0,independentSourceFamilies:0};
const families=new Set();
for(const grade of learningGrades){
 const profile=gradeProfiles[grade],forms=[null,'support','extend'].map(branch=>placementForm(grade,branch));
 assert.equal(forms[0].questions.length,profile.commonCount);
 for(const form of forms.slice(1))assert.equal(form.questions.length,profile.totalCount);
 for(const form of forms){assert.equal(new Set(form.questions.map(q=>q.id)).size,form.questions.length);assert.ok(publicForm(form).questions.every(q=>!('answer'in q)&&!('evidence'in q)&&!('rubric'in q)));for(const q of form.questions){assert.ok(form.passages.find(p=>p.id===q.passageId));if(q.options.length)assert.equal(new Set(q.options).size,profile.choiceCount);}}
 const courses=courseOrder.map(course=>{
  const b=courseBundle(grade,course,lessons);assert.equal(b.training.length,3);assert.ok(b.training.every(l=>l.grade===grade));assert.equal(b.checks.length,8);
  for(const c of b.checks){assert.equal(c.grade,grade);assert.equal(new Set(c.options).size,profile.choiceCount);assert.ok(c.options[c.answer]);assert.ok(c.evidence.every(i=>c.paragraphs[i]));families.add(c.familyId);}
  result.courseCount++;result.trainingLinks+=3;result.checkVariants+=8;
  return {course,name:b.name,trainingIds:b.training.map(l=>l.id),checks:b.checks.length,hash:b.hash};
 });
 result.grades.push({grade,diagnostic:{common:profile.commonCount,branch:profile.branchCount,explanations:2,total:profile.totalCount,oralAllowed:profile.oralAllowed},courses});
}
// Rewording/regrading a source cannot turn it into another independent family.
result.independentSourceFamilies=families.size;
assert.equal(result.courseCount,36);assert.equal(result.trainingLinks,108);assert.equal(result.checkVariants,288);assert.equal(families.size,48);
const out=resolve(root,'output','all-grade-journeys');mkdirSync(out,{recursive:true});writeFileSync(resolve(out,'content-audit.json'),JSON.stringify({...result,passed:true},null,2));
console.log(`All-grade content audit: ${result.courseCount} courses; ${result.trainingLinks} training links; ${result.checkVariants} grade variants, ${families.size} independent families.`);
