import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import { progressiveLessons, progressivePassage, thinkingLadder } from "../src/data/progressiveReading";
import { readingLevels, assessPassage } from "../src/data/readingPolicy";
import { createProgressiveRun, editProgressiveResponse, submitProgressiveResponse, advanceProgressive, canAdvanceProgressive, restartProgressive } from "../src/services/progressiveReading";
import { ProgressiveLessonPlayer } from "../src/components/student/ProgressiveReadingStudio";
import { useReadingWorkspace } from "../src/store/useReadingWorkspace";

const at = "2026-10-14T12:00:00Z";
const lesson = progressiveLessons[5];
const q = lesson.questions[4];
function answer(choice=q.answer) {return editProgressiveResponse({...createProgressiveRun(),phase:"questions",index:4,reached:4},q.id,{choice,evidence:q.evidence,reason:"주제 조건을 먼저 적용한 뒤 횟수로 순서를 정하되 정확성은 알 수 없다."});}

test("전 학년 18개 지문 변형과 30개 문항은 분량·선택지·근거·사고구술 참조를 충족한다",()=>{
  assert.equal(progressiveLessons.length,6);
  const ids=new Set<string>();
  for(const l of progressiveLessons){
    assert.deepEqual(l.questions.map(q=>q.skill),[...thinkingLadder]);
    for(const level of readingLevels){
      const p=progressivePassage(l,level);
      assert.equal(assessPassage(p.paragraphs.map(p=>p.sentences[0].text),l.grade,level).lengthLabel,"분량 범위 안",p.id);
      assert.equal(new Set(p.paragraphs.map(p=>p.id)).size,p.paragraphs.length);
      for(const m of l.model) assert.ok(p.paragraphs.find(p=>p.id===m.paragraph)?.sentences[0].text.includes(m.quote));
      for(const question of l.questions) assert.ok(question.evidence.every(id=>p.paragraphs.some(p=>p.id===id)));
    }
    for(const question of l.questions){
      assert.ok(!ids.has(question.id));ids.add(question.id);
      assert.equal(question.options.length,l.grade<=2?3:l.grade<=4?4:5);
      assert.equal(question.optionReasons.length,question.options.length);
      assert.equal(new Set(question.options).size,question.options.length);
      assert.ok(Number.isInteger(question.answer)&&question.answer>=0&&question.answer<question.options.length);
      assert.equal(question.hints.length,3);
    }
    assert.ok(l.questions[4].scenario);
  }
  assert.equal(ids.size,30);
});
test("새 보기 정답이어도 서술 평가를 자동 확정하거나 처음 본 지문으로 집계하지 않는다",()=>{
  const s=submitProgressiveResponse(answer(),lesson,"standard",q.id,"one",at).responses[q.id].submissions[0];
  assert.equal(s.choiceMatch,true);assert.equal(s.evidenceMatch,true);
  assert.equal(s.explanationReview,"pending");assert.equal(s.passageExposure,"practiced");assert.equal(s.support,"independent");
});
test("선택만 맞거나 다른 학년 근거·빈 설명은 다음 단계 통과가 되지 않는다",()=>{
  let a=editProgressiveResponse(answer(),q.id,{evidence:["g1-p1"]});
  assert.equal(submitProgressiveResponse(a,lesson,"standard",q.id,"bad",at),a);
  a=editProgressiveResponse(answer(),q.id,{reason:" "});assert.equal(submitProgressiveResponse(a,lesson,"standard",q.id,"blank",at),a);
  a=editProgressiveResponse(answer(),q.id,{evidence:["g6-p1"]});
  a=submitProgressiveResponse(a,lesson,"standard",q.id,"partial",at);
  assert.equal(a.responses[q.id].submissions[0].choiceMatch,true);
  assert.equal(canAdvanceProgressive(a,lesson),false);
});
test("도움과 해설 후 수정 이력은 낮춰도 없어지지 않고 첫 응답을 보존한다",()=>{
  let a=editProgressiveResponse(answer(0),q.id,{hintLevel:2});
  a=editProgressiveResponse(a,q.id,{hintLevel:0});assert.equal(a.responses[q.id].hintLevel,2);
  a=submitProgressiveResponse(a,lesson,"standard",q.id,"first",at);
  const first=structuredClone(a.responses[q.id].submissions[0]);
  a=editProgressiveResponse(a,q.id,{choice:q.answer,revealed:true});
  a=submitProgressiveResponse(a,lesson,"standard",q.id,"second",at);
  assert.deepEqual(a.responses[q.id].submissions[0],first);
  assert.equal(a.responses[q.id].submissions[1].support,"guided");
  assert.equal(a.responses[q.id].submissions[1].revised,true);
  assert.equal(submitProgressiveResponse(a,lesson,"standard",q.id,"third",at),a);
});
test("막힌 단계는 해설을 읽은 뒤 다음 연습으로 갈 수 있고 재시작은 이전 기록을 보존한다",()=>{
  let a=submitProgressiveResponse(answer(0),lesson,"standard",q.id,"wrong",at);
  assert.equal(advanceProgressive(a,lesson),a);
  a=editProgressiveResponse(a,q.id,{revealed:true});
  const done=advanceProgressive(a,lesson);assert.equal(done.phase,"complete");
  const next=restartProgressive(done);assert.equal(next.archives.length,1);
  assert.equal(next.archives[0].responses[q.id].submissions[0].choice,0);
  assert.equal(next.phase,"model");
});
test("독립 단계의 답·오답 해설은 응답 전 렌더에 포함하지 않는다",()=>{
  const key=`${lesson.id}-standard`;
  useReadingWorkspace.getState().save(key,"progressive-v1",{...createProgressiveRun(),phase:"questions",index:4,reached:4});
  const html=renderToStaticMarkup(<ProgressiveLessonPlayer lesson={lesson} level="standard"/>);
  assert.ok(html.includes(q.scenario!));assert.ok(!html.includes(q.explanation));
  assert.ok(!html.includes(q.optionReasons[0]));assert.ok(!html.includes(lesson.model[0].thought));
  assert.match(html,/disabled/);
});
test("18개 글의 시범과 90개 단계 화면이 독립 저장 키로 렌더된다",()=>{
  for(const l of progressiveLessons)for(const level of readingLevels){
    const key=`${l.id}-${level}`;
    useReadingWorkspace.getState().save(key,"progressive-v1",createProgressiveRun());
    assert.ok(renderToStaticMarkup(<ProgressiveLessonPlayer lesson={l} level={level}/>).includes(l.model[0].thought));
    for(let index=0;index<5;index++){
      useReadingWorkspace.getState().save(key,"progressive-v1",{...createProgressiveRun(),phase:"questions",index,reached:index});
      const html=renderToStaticMarkup(<ProgressiveLessonPlayer lesson={l} level={level}/>);
      assert.ok(html.includes(l.questions[index].prompt));assert.ok(!html.includes("NaN"));
    }
  }
  useReadingWorkspace.setState({sessions:{},lastSlotId:null});
});
