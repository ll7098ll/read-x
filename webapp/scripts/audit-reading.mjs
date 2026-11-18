import { build } from "esbuild";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
const app = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const bundled = await build({ stdin: { contents: `export * from './src/data/readingPolicy'; export {getJourneyPassages} from './src/data/learningJourney'; export * from './src/data/progressiveReading';`, resolveDir: app }, bundle: true, platform: "node", format: "esm", write: false });
const { assessPassage, readingLevels, readingPolicy, getJourneyPassages, progressiveLessons, progressivePassage } = await import(`data:text/javascript;base64,${Buffer.from(bundled.outputFiles[0].contents).toString("base64")}`);
const corpus = JSON.parse(await readFile(path.join(app, "../data/curriculum_2022/passage_corpus.json"), "utf8"));
const baseline = JSON.parse(await readFile(path.join(app,"../data/curriculum_2022/revisions/baseline-v1.json"),"utf8"));
const revised = JSON.parse(await readFile(path.join(app,"src/data/corpusLessons.generated.json"),"utf8"));
const passages = corpus.passages.map(p => ({ id: p.id, grade: p.grade, title: p.title,
  baselineChars: assessPassage(baseline.passages.find(b=>b.id===p.id).paragraphs,p.grade).chars,
  assessment: Object.fromEntries(readingLevels.map(l => [l, assessPassage(p.readingVariants[l], p.grade, l)])),
  teacherReview:p.editorialReview.teacherReview,studentCalibration:p.editorialReview.studentCalibration,
  factualSources:p.editorialReview.factualSources,editorialChanges:p.editorialReview.changes }));
const representative = readingLevels.flatMap(level => Object.values(getJourneyPassages({ version: 2, readingLevel: level })).map(p => ({ id: p.id, level,
  ...assessPassage(p.paragraphs.map(p => p.sentences.map(s => s.text).join(" ")), 5, level) })));
const byGrade = readingPolicy.map(p => {
  const rows = passages.filter(r => r.grade === p.grade);
  const lengths = rows.map(r => r.assessment.standard.chars).sort((a, b) => a - b);
  const middle = Math.floor(lengths.length / 2);
  const oldLengths=rows.map(r=>r.baselineChars).sort((a,b)=>a-b);
  return { grade: p.grade, count: rows.length, baselineMedian:(oldLengths[middle]+oldLengths[Math.floor((rows.length-1)/2)])/2,min: lengths[0], median: (lengths[middle] + lengths[Math.floor((lengths.length - 1) / 2)]) / 2, max: lengths.at(-1), belowStandard: rows.filter(r => r.assessment.standard.lengthLabel === "분량 보강 검토").length };
});
const destination = path.join(app, "../output/reading-design");
const progressive = progressiveLessons.flatMap(lesson => readingLevels.map(level => ({id:lesson.id,grade:lesson.grade,level,...assessPassage(progressivePassage(lesson,level).paragraphs.map(p=>p.sentences[0].text),lesson.grade,level)})));
await mkdir(destination, { recursive: true });
await writeFile(path.join(destination,"graded-lessons.json"),JSON.stringify({status:"editorial_draft_not_calibrated",lessons:progressiveLessons,variants:progressive},null,2));
await writeFile(path.join(destination, "reading-audit.json"), JSON.stringify({ policyStatus: "editorial_proposal_not_calibrated", counting: "본문 공백 포함, 문단 사이 공백 1개, HTML·제목·표 제외", byGrade, representative, progressive, passages }, null, 2));
const levelSummary=readingPolicy.flatMap(p=>readingLevels.map(level=>{
  const rows=passages.filter(r=>r.grade===p.grade).map(r=>r.assessment[level]);
  const lengths=rows.map(r=>r.chars).sort((a,b)=>a-b);
  return {grade:p.grade,level,count:rows.length,min:lengths[0],max:lengths.at(-1),inEditorialRange:rows.filter(r=>r.lengthLabel==="분량 범위 안").length};
}));
const questions=new Map(revised.flatMap(l=>[...l.questions,...Object.values(l.levelQuestions||{}).flat()].map(q=>[q.id,q])));
await writeFile(path.join(destination,"corpus-revision-audit.json"),JSON.stringify({
  status:"AI_editorial_revision_teacher_review_and_student_calibration_pending",
  coverage:corpus.revisionCoverage,uniqueQuestionCount:questions.size,
  explanationQuestions:[...questions.values()].filter(q=>q.responseKind==="explanation").length,
  applicationQuestions:[...questions.values()].filter(q=>q.scenario).length,
  changedPassages:corpus.passages.filter(p=>p.contentHash!==baseline.passages.find(b=>b.id===p.id).contentHash).length,
  preservedBaseline:"data/curriculum_2022/revisions/baseline-v1.json",byGrade,levelSummary,passages
},null,2));
console.table(byGrade);
console.table(levelSummary);
if(corpus.revisionCoverage.revised!==144 || levelSummary.some(r=>r.inEditorialRange!==r.count)) process.exitCode=1;
console.table(representative.map(({ id, chars, words, paragraphs, lengthLabel }) => ({ id, chars, words, paragraphs, lengthLabel })));
if (representative.some(p => p.lengthLabel !== "분량 범위 안")) process.exitCode = 1;
console.table(progressive.map(({grade,level,chars,lengthLabel})=>({grade,level,chars,lengthLabel})));
if (progressive.some(p => p.lengthLabel !== "분량 범위 안")) process.exitCode = 1;
