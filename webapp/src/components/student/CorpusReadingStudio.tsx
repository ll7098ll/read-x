import React, { useEffect, useState } from "react";
import type { ProgressiveLesson } from "../../data/progressiveReading";
import { readingLevels, readingLevelLabels, type ReadingLevel } from "../../data/readingPolicy";
import { useReadingWorkspace } from "../../store/useReadingWorkspace";
import { useCoursewareStore } from "../../store/useCoursewareStore";
import { ProgressiveLessonPlayer } from "./ProgressiveReadingStudio";

export function CorpusReadingStudio({lesson,initialLevel,onBack}:{lesson:ProgressiveLesson;initialLevel?:ReadingLevel;onBack?:()=>void}) {
  const [level,setLevel]=useState<ReadingLevel>(()=>initialLevel || useReadingWorkspace.getState().sessions[lesson.id]?.["selected-level"] as ReadingLevel || "standard");
  const safeLevel=readingLevels.includes(level)?level:"standard";
  useEffect(()=>{
    useReadingWorkspace.getState().save(lesson.id,"selected-level",safeLevel);
    const match=lesson.sourcePassageId?.match(/^passage:(.+):001$/);
    if(match){
      useReadingWorkspace.getState().save(match[1],"revised-reading",{lessonId:lesson.id,level:safeLevel});
      useReadingWorkspace.getState().visit(match[1]);
    }
  },[lesson.id,lesson.sourcePassageId,safeLevel]);
  return <div className="pr-studio">
    <header className="pr-heading"><div><p className="rx-eyebrow">나의 읽기 수업 · {lesson.grade}학년</p><h1>{lesson.title}</h1><p>시범 → 같이 해보기 → 스스로 해보기. 내 판단과 본문의 근거를 연결해요.</p></div><button className="rx-button" onClick={onBack || (()=>useCoursewareStore.getState().setStudentMode("portal"))}>학습 목록으로</button></header>
    <details className="reading-settings"><summary><span>읽기 수준</span><b>{readingLevelLabels[safeLevel]}</b><span>변경하기</span></summary><div className="pr-selectors"><fieldset><legend>읽을 글의 수준</legend>{readingLevels.map(l=><button key={l} aria-pressed={safeLevel===l} onClick={()=>setLevel(l)}>{readingLevelLabels[l]}</button>)}</fieldset><p>도움글은 핵심 관계를, 기준글은 비교 사례를, 도전글은 반례와 판단의 한계까지 읽어요. 수준별로 응답을 따로 보관해요.</p></div></details>
    <ProgressiveLessonPlayer key={`${lesson.id}-${safeLevel}`} lesson={lesson} level={safeLevel}/>
  </div>;
}
