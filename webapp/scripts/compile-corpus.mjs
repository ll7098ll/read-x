import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { createHash } from "node:crypto";

export async function compileCorpus(root, app) {
  const directory = path.join(root, "data/curriculum_2022/revisions");
  const baseline = JSON.parse(await readFile(path.join(directory,"baseline-v1.json"),"utf8"));
  const lessons=[];
  for(let grade=1;grade<=6;grade++){
    const source=path.join(directory,`grade-${grade}.json`);
    lessons.push(...JSON.parse(await readFile(source,"utf8")));
  }
  const byId=new Map(lessons.map(l=>[l.sourcePassageId,l]));
  if(byId.size!==lessons.length) throw new Error("Duplicate revision IDs");
  if(lessons.length!==144 || baseline.passages.some(p=>!byId.has(p.id))) throw new Error("All 144 revisions are required");
  const levels=["supported","standard","challenge"];
  for(const lesson of lessons){
    const old=baseline.passages.find(p=>p.id===lesson.sourcePassageId);
    if(!old || old.grade!==lesson.grade || old.contentHash!==lesson.editorialReview.baselineHash) throw new Error(`Baseline mismatch: ${lesson.id}`);
    const core=lesson.layers.supported;
    if(lesson.questions.length!==5 || levels.some(l=>!lesson.layers[l]?.length)) throw new Error(`Incomplete revision: ${lesson.id}`);
    for(const q of lesson.questions){
      if(!q.evidence.length || q.evidence.some(id=>!core.some(p=>p.id===id))) throw new Error(`Missing evidence: ${q.id}`);
      if(q.responseKind!=="explanation" && (!q.options[q.answer] || q.optionReasons.length!==q.options.length || !q.scenario)) throw new Error(`Invalid application: ${q.id}`);
    }
    for(const model of lesson.model) if(!core.find(p=>p.id===model.paragraph)?.text.includes(model.quote)) throw new Error(`Missing model anchor: ${lesson.id}`);
    for(const [level,questions] of Object.entries(lesson.levelQuestions || {})) {
      const paragraphs=levels.slice(0,levels.indexOf(level)+1).flatMap(l=>lesson.layers[l]);
      if(questions.length!==5) throw new Error(`Invalid level tasks: ${lesson.id}`);
      for(const q of questions) if(q.evidence.some(id=>!paragraphs.some(p=>p.id===id))) throw new Error(`Missing level evidence: ${q.id}`);
    }
  }
  const passages=baseline.passages.map(old=>{
    const lesson=byId.get(old.id);
    if(!lesson) return old;
    const readingVariants=Object.fromEntries(levels.map((level,i)=>[level,levels.slice(0,i+1).flatMap(l=>lesson.layers[l].map(p=>p.text))]));
    const {table,teacherThinkingModel,independentCheck,writingPrompt,diagnostic,...metadata}=old;
    return {...metadata,version:2,originalPurpose:old.purpose,purpose:"practice",title:lesson.title,paragraphs:readingVariants.standard,readingVariants,
      revisedLessonId:lesson.id,reviewState:"needs_review",editorialReview:lesson.editorialReview,
      contentHash:createHash("sha256").update(readingVariants.standard.join("\n")).digest("hex"),
      diagnostic:{purpose:"scaffolded_practice",items:lesson.questions},
      teacherThinkingModel:{evidenceQuote:lesson.model[0].quote,reasoning:lesson.model[0].thought}};
  });
  const challengeReplacements=lessons.filter(l=>l.levelQuestions?.challenge).length;
  const corpus={...baseline,version:2,revisionCoverage:{revised:lessons.length,total:baseline.passages.length,levelVariants:lessons.length*3,practiceQuestions:lessons.length*5,challengeReplacements},passages};
  await writeFile(path.join(app,"src/data/corpusLessons.generated.json"),JSON.stringify(lessons));
  await writeFile(path.join(root,"data/curriculum_2022/passage_corpus.json"),JSON.stringify(corpus,null,2)+"\n");
  return corpus;
}
