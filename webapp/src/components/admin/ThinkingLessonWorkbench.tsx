import React, { useState } from "react";
import { ArrowRight, BookOpen, Check, RotateCcw } from "lucide-react";
import { modelSteps, getSentence, JOURNEY_GOAL } from "../../data/learningJourney";
import { useThinkingScript } from "../../store/useThinkingScript";
import { useReadingStorageStatus } from "../../store/useReadingWorkspace";
import { Dialog } from "../common/DesignSystem";
import { MarkedSentence } from "../student/ReadingAnnotations";

export function ThinkingLessonWorkbench() {
  const script=useThinkingScript();
  const [selected,setSelected]=useState(0);
  const [saved,setSaved]=useState(false);
  const [preview,setPreview]=useState(false);
  const failed=useReadingStorageStatus(s=>s.failed);
  const model=modelSteps[selected];
  const sentence=getSentence(model.anchor);
  return <section className="rx-script-workbench">
    <div className="rx-section-title"><div><p className="rx-eyebrow">본문과 생각을 함께 설계하는 수업</p><h2>사고 시범 편집실</h2></div><span className="rx-badge">대표 수업 · 기기 내 초안</span></div>
    <p>{JOURNEY_GOAL}</p>
    <div className="rx-script-grid"><nav aria-label="편집할 사고 시범">{modelSteps.map((m,i)=><button key={m.anchor+i} aria-pressed={selected===i} onClick={()=>setSelected(i)}><span>0{i+1}</span><b>{m.label}</b><small>{m.marking.label}</small></button>)}</nav><div className="rx-script-editor"><p className="rx-note-origin">시범이 짚는 본문 · {model.marking.label}</p><blockquote>{sentence&&<MarkedSentence text={sentence.text} marks={[model.marking]}/>}</blockquote><label className="lj-field"><span>어디를 왜 읽는지 보여주는 사고구술</span><textarea rows={4} value={script.draft[selected]??model.thought} onChange={e=>{script.edit(selected,e.target.value);setSaved(false);}}/></label><p className="rx-muted">단서 → 연결한 까닭 → 자기점검이 드러나도록 적어 주세요. 현재는 시범 대본만 편집하며 본문과 근거 위치는 고정합니다.</p></div></div>
    <div className="rx-script-checks"><span><Check size={15}/> 본문에 연결된 시범 3장</span><span><Check size={15}/> 함께·도움 줄이기·독립·전이 과제</span><span><BookOpen size={15}/> 교육·사실 검수 전 초안</span></div>
    <div className="rx-composer-actions"><button className="rx-button" onClick={()=>{script.reset();setSaved(false);}}><RotateCcw size={16}/>기본 대본으로</button><button className="rx-button rx-button-primary" disabled={script.draft.some(t=>!t.trim())} onClick={()=>{script.apply();setSaved(true);}}>이 기기의 생각 시범에 반영 <ArrowRight size={16}/></button><button className="rx-button" onClick={()=>setPreview(true)}>학생 화면 미리보기</button></div>
    {preview&&<Dialog title="학생에게 보이는 생각 시범" onClose={()=>setPreview(false)}><p className="rx-eyebrow">시범 {selected+1} / 3 · {model.label}</p><blockquote className="rx-script-preview-source">{sentence&&<MarkedSentence text={sentence.text} marks={[model.marking]}/>}</blockquote><aside className="lj-inline-model"><b>선생님의 생각 · {model.marking.label}</b><p>“{script.draft[selected]??model.thought}”</p></aside><p className="rx-muted">작성 중인 초안의 미리보기입니다. 학생의 진행 위치와 응답은 바꾸지 않습니다.</p></Dialog>}
    {saved&&<p className="rx-script-saved" role="status">{failed?"기기에 저장하지 못했습니다. 대본을 복사해 주세요.":"이 기기의 다음 시범에 반영했습니다. 정식 게시 승인을 대신하지 않습니다."}</p>}
  </section>;
}
