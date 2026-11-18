import React from "react";
import test from "node:test";
import assert from "node:assert/strict";
import { renderToStaticMarkup } from "react-dom/server";
import { makeTextAnchor, resolveMarkRange, validAnnotation, rememberAnnotations, undoAnnotations, type ReadingAnnotation } from "../src/services/annotations";
import { MarkedSentence } from "../src/components/student/ReadingAnnotations";
import type { JourneyPassage } from "../src/data/learningJourney";
import { progressiveLessons } from "../src/data/progressiveReading";
import { createProgressiveRun, editProgressiveResponse, submitProgressiveResponse, restartProgressive } from "../src/services/progressiveReading";
import { collectThinkingRecords } from "../src/components/common/ThinkingPortfolio";

const text="열린 문과 닫힌 문, 두 문은 상태가 다르다.";
const passage:JourneyPassage={id:"range-test",version:2,title:"문",subject:"읽기",paragraphs:[{id:"p1",sentences:[{id:"s1",text}]}]};
const first=text.indexOf("문"), second=text.indexOf("문",first+1);
const a:ReadingAnnotation={id:"a",passageId:passage.id,passageVersion:2,sentenceId:"s1",quote:"문",anchor:makeTextAnchor("s1",text,second,second+1)!,kind:"evidence",note:"닫힌 쪽을 골랐다."};
test("반복 구절의 두 번째 위치와 모호한 이전 표시를 구별한다",()=>{
  assert.deepEqual(resolveMarkRange(text,a),{start:second,end:second+1});
  assert.equal(resolveMarkRange(text,{quote:"문"}),null);
  const html=renderToStaticMarkup(<MarkedSentence text={text} marks={[a]}/>);
  assert.ok(html.indexOf("<mark")>html.indexOf("닫힌"));
  assert.equal(html.replace(/<[^>]*>/g,""),text);
});
test("같은 문장 안의 서로 다른 구절 연결을 허용하고 자기 자신 연결은 거절한다",()=>{
  const target=makeTextAnchor("s1",text,first,first+1)!;
  assert.equal(validAnnotation(passage,{...a,kind:"link",linkedSentenceId:"s1",linkedAnchor:target}),true);
  assert.equal(validAnnotation(passage,{...a,kind:"link",linkedSentenceId:"s1",linkedAnchor:a.anchor}),false);
});
test("원문 버전과 앵커가 바뀐 표시는 새 위치에 임의로 붙지 않는다",()=>{
  assert.equal(validAnnotation(passage,{...a,passageVersion:1}),false);
  assert.equal(validAnnotation(passage,{...a,anchor:{...a.anchor!,start:0,end:1}}),false);
  assert.equal(resolveMarkRange("바뀐 본문",a),null);
});
test("표시 수정·삭제를 되돌려도 제출 시점 스냅샷은 그대로 유지한다",()=>{
  const submission=structuredClone(a);
  let state:{annotations:ReadingAnnotation[];annotationHistory?:ReadingAnnotation[][]}={annotations:[a]};
  state=rememberAnnotations(state,[{...a,note:"내 생각을 고쳤다."}]);
  state=rememberAnnotations(state,[]);
  state=undoAnnotations(state);
  assert.equal(state.annotations[0].note,"내 생각을 고쳤다.");
  state=undoAnnotations(state);
  assert.equal(state.annotations[0].note,a.note);
  assert.deepEqual(submission,a);
});
test("조건 표식과 UTF-16 범위는 원문을 보존하고 글자 중간 범위를 거절한다",()=>{
  const unicode="문🌱상태";
  assert.equal(makeTextAnchor("s",unicode,2,3),null);
  assert.equal(makeTextAnchor("s",unicode,1,3)?.quote,"🌱");
  assert.ok(renderToStaticMarkup(<MarkedSentence text={text} marks={[{...a,kind:"condition"}]}/>).includes("lj-mark-condition"));
});
test("다시 연습을 시작해도 교사의 기록 목록에서 당시 본문과 질문이 보존된다",()=>{
  const lesson=structuredClone(progressiveLessons[0]);
  lesson.title="제출 당시의 글 제목";
  const q=lesson.questions[0], originalPrompt=q.prompt;
  let run=editProgressiveResponse(createProgressiveRun(),q.id,{choice:q.answer,evidence:q.evidence,reason:"글의 조건과 내 판단을 연결했다."});
  run=submitProgressiveResponse(run,lesson,"standard",q.id,"snapshot-test","2026-10-15T03:00:00Z");
  lesson.title="나중에 바뀐 제목";q.prompt="나중에 바뀐 질문";
  const restarted=restartProgressive(run);
  const records=collectThinkingRecords({[`${lesson.id}-standard`]:{"progressive-v1":restarted}});
  assert.equal(records.length,1);
  assert.equal(records[0].archiveIndex,0);
  assert.equal(records[0].passage.title,"제출 당시의 글 제목");
  assert.equal(records[0].q.prompt,originalPrompt);
});
