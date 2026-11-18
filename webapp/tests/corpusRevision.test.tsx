import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import { corpusLessons, revisedLessonForSlot } from "../src/data/corpusReading";
import { masterData } from "../src/data/lessonCatalog";
import { progressiveLessonAtLevel, progressivePassage, thinkingLadder } from "../src/data/progressiveReading";
import { readingLevels, assessPassage } from "../src/data/readingPolicy";
import { createProgressiveRun, editProgressiveResponse, submitProgressiveResponse, canAdvanceProgressive, advanceProgressive, restartProgressive } from "../src/services/progressiveReading";
import { ProgressiveLessonPlayer, ProgressiveReadingStudio } from "../src/components/student/ProgressiveReadingStudio";
import { CorpusReadingStudio } from "../src/components/student/CorpusReadingStudio";
import { useReadingWorkspace } from "../src/store/useReadingWorkspace";

test("144편·432수준의 분량, 근거, 720기본문항과 80도전 교체 문항을 검증한다",()=>{
  assert.equal(corpusLessons.length,144);
  assert.deepEqual([1,2,3,4,5,6].map(g=>corpusLessons.filter(l=>l.grade===g).length),[20,20,26,26,26,26]);
  const uniqueQuestions=new Set<string>();
  let replacements=0;
  for(const original of corpusLessons){
    assert.equal(original.version,2);
    if(original.levelQuestions?.challenge) replacements++;
    for(const level of readingLevels){
      const lesson=progressiveLessonAtLevel(original,level);
      const p=progressivePassage(lesson,level);
      const texts=p.paragraphs.map(p=>p.sentences[0].text);
      assert.equal(assessPassage(texts,lesson.grade,level).lengthLabel,"분량 범위 안",p.id);
      assert.equal(new Set(p.paragraphs.map(p=>p.id)).size,p.paragraphs.length);
      assert.deepEqual(lesson.questions.map(q=>q.skill),[...thinkingLadder]);
      assert.equal(lesson.questions.length,5);
      for(const [i,q] of lesson.questions.entries()){
        uniqueQuestions.add(q.id);
        assert.ok(q.evidence.length && q.evidence.every(id=>p.paragraphs.some(p=>p.id===id)),q.id);
        assert.equal(q.hints.length,3);
        if(i<4){assert.equal(q.responseKind,"explanation");assert.equal(q.options.length,0);}
        else {
          assert.ok(q.scenario && q.scenario.length>20);
          assert.equal(q.options.length,lesson.grade<=2?3:lesson.grade<=4?4:5);
          assert.equal(new Set(q.options).size,q.options.length);
          assert.equal(q.optionReasons.length,q.options.length);
          assert.ok(q.options[q.answer]);
        }
      }
      for(const m of lesson.model) assert.ok(p.paragraphs.find(p=>p.id===m.paragraph)?.sentences[0].text.includes(m.quote));
      if(level==="challenge" && original.levelQuestions?.challenge){
        const q=lesson.questions[3];
        assert.notEqual(q.id,original.questions[3].id);
        assert.ok(q.evidence.some(id=>original.layers.challenge.some(p=>p.id===id)),q.id);
      }
    }
  }
  assert.equal(replacements,80);assert.equal(uniqueQuestions.size,800);
});

test("기존 96개 수업 주소 모두 원래 학년·지문 식별자를 유지해 개정본에 연결된다",()=>{
  for(const slot of masterData.expository_slots_96!){
    const lesson=revisedLessonForSlot(slot.slot_id);
    assert.ok(lesson,slot.slot_id);assert.equal(lesson.grade,slot.grade_num);
    assert.equal(lesson.sourcePassageId,`passage:${slot.slot_id}:001`);
    assert.ok(lesson.id.startsWith("corpus-v2:"));
  }
});

test("서술 응답은 선택지 없이 저장되며 내용 정답을 판정하지 않고 수정·도움 기록을 보존한다",()=>{
  const lesson=progressiveLessonAtLevel(corpusLessons.find(l=>l.grade===4)!,"challenge");
  const q=lesson.questions[3];
  let run=editProgressiveResponse({...createProgressiveRun(),phase:"questions",index:3,reached:3},q.id,{reason:"  내 설명을 교사와 검토합니다.  ",evidence:q.evidence});
  run=submitProgressiveResponse(run,lesson,"challenge",q.id,"one","2026-10-15T00:00:00Z");
  const first=structuredClone(run.responses[q.id].submissions[0]);
  assert.equal(first.choice,null);assert.equal(first.choiceMatch,null);assert.equal(first.explanationReview,"pending");
  assert.equal(first.passageExposure,"practiced");assert.equal(first.support,"independent");
  assert.equal(first.reason,"내 설명을 교사와 검토합니다.");assert.ok(canAdvanceProgressive(run,lesson));
  assert.equal(submitProgressiveResponse(run,lesson,"challenge",q.id,"duplicate","now"),run);
  run=editProgressiveResponse(run,q.id,{reason:"조건을 더 보태 고친 설명입니다.",hintLevel:1});
  assert.equal(canAdvanceProgressive(run,lesson),false);
  run=submitProgressiveResponse(run,lesson,"challenge",q.id,"two","now");
  assert.deepEqual(run.responses[q.id].submissions[0],first);
  assert.equal(run.responses[q.id].submissions[1].support,"guided");
  assert.equal(run.responses[q.id].submissions[1].revised,true);
  assert.equal(advanceProgressive(run,lesson).index,4);
  assert.deepEqual(restartProgressive(run).archives[0].responses[q.id].submissions[0],first);
});

test("도전 문항은 추가 사례 근거가 필요하고 도움글에서 도전 문단 제출을 허용하지 않는다",()=>{
  const original=corpusLessons.find(l=>l.grade===3)!;
  const lesson=progressiveLessonAtLevel(original,"challenge"),q=lesson.questions[3];
  let run=editProgressiveResponse({...createProgressiveRun(),phase:"questions",index:3,reached:3},q.id,{reason:"확인한 설명",evidence:[original.layers.supported[0].id]});
  run=submitProgressiveResponse(run,lesson,"challenge",q.id,"partial","now");
  assert.equal(run.responses[q.id].submissions[0].evidenceMatch,false);
  assert.equal(canAdvanceProgressive(run,lesson),false);
  const coreQ=original.questions[3];
  const bad=editProgressiveResponse(createProgressiveRun(),coreQ.id,{reason:"다른 수준 근거",evidence:q.evidence});
  assert.equal(submitProgressiveResponse(bad,original,"supported",coreQ.id,"invalid","now"),bad);
});

test("432개 수준에서 선택한 문항과 본문을 렌더하고 응답 전 예시 답변을 숨긴다",()=>{
  for(const original of corpusLessons)for(const level of readingLevels){
    const lesson=progressiveLessonAtLevel(original,level),q=lesson.questions[3];
    useReadingWorkspace.getState().save(`${lesson.id}-${level}`,"progressive-v1",{...createProgressiveRun(),phase:"questions",index:3,reached:3});
    const html=renderToStaticMarkup(<ProgressiveLessonPlayer lesson={original} level={level}/>);
    assert.ok(html.includes(q.prompt),q.id);
    assert.ok(!html.includes(q.explanation),q.id);
    assert.ok(!html.includes('type="radio"'),q.id);
    assert.ok(!html.includes("NaN"));
    assert.ok(html.includes(original.layers.supported[0].text));
  }
  useReadingWorkspace.setState({sessions:{},lastSlotId:null});
});

test("단계별 읽기 학년 선택에는 해당 학년의 모든 개정 지문과 기존 전략 연습을 제공한다",()=>{
  useReadingWorkspace.getState().save("progressive-preferences","grade",6);
  const html=renderToStaticMarkup(<ProgressiveReadingStudio/>);
  for(const l of corpusLessons.filter(l=>l.grade===6)) assert.ok(html.includes(l.title));
  assert.ok(html.includes("개정 지문 144편"));assert.ok(html.includes("읽기 전략 연습"));
  useReadingWorkspace.setState({sessions:{},lastSlotId:null});
});

test("자료실에서 고른 수준은 이전 수업의 수준 선호보다 우선하고 해당 본문을 연다",()=>{
  const lesson=corpusLessons.find(l=>l.sourcePassageId==="passage:G5-EXP-V2-2:001")!;
  useReadingWorkspace.getState().save(lesson.id,"selected-level","supported");
  const html=renderToStaticMarkup(<CorpusReadingStudio lesson={lesson} initialLevel="challenge"/>);
  assert.match(html,/aria-pressed="true"[^>]*>도전글/);
  assert.ok(html.includes(lesson.layers.challenge.at(-1)!.text));
  useReadingWorkspace.setState({sessions:{},lastSlotId:null});
});

test("사고구술은 사례 소개 문장 대신 실제 수치·조건에 표시하고 충분한 직접 근거를 인정한다",()=>{
  const speed=corpusLessons.find(l=>l.sourcePassageId==="P22-G6-S1-01")!;
  assert.ok(speed.model[0].quote.includes("20미터를 10초"));
  const ecology=revisedLessonForSlot("G5-EXP-V2-2")!;
  assert.ok(ecology.model[1].quote.includes("오염이나 서식 공간 변화"));
  const q=ecology.questions[1];
  let run=editProgressiveResponse({...createProgressiveRun(),phase:"questions",index:1,reached:1},q.id,{reason:"같은 시기에 오염도 있었다면 한 원인으로 단정하기 어렵습니다.",evidence:[ecology.layers.supported[2].id]});
  run=submitProgressiveResponse(run,ecology,"standard",q.id,"direct","now");
  assert.ok(canAdvanceProgressive(run,ecology));
});
