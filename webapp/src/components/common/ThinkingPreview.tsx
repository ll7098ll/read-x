import React, { useState } from "react";
import { ArrowLeft, ArrowRight, Lightbulb } from "lucide-react";

const example = [
  { source: "온실의 창문은 온도가 28도 이상이면 열린다.", label: "조건을 나누어 보기", thought: "열리는 조건과 닫히는 조건이 다르네. 두 온도를 따로 살펴봐야겠어.", active: [0,1] },
  { source: "열린 창문은 온도가 24도 이하가 되면 닫힌다.", label: "앞의 정보와 연결하기", thought: "26도는 두 온도 사이야. ‘직전 상태’라는 말이 있으니, 바로 전에는 어땠는지 확인해야겠어.", active: [2] },
  { source: "그 사이에서는 직전 상태를 유지한다.", label: "근거로 내 판단 점검하기", thought: "직전에는 열려 있었고, 닫는 조건에 해당하지 않아. 그래서 열린 상태를 유지하는구나.", active: [1,2] },
];
export function ThinkingPreview() {
  const [step,setStep] = useState(0);
  return <div className="rx-thinking-preview">
    <div className="rx-preview-heading"><span><Lightbulb size={16}/> 생각 시범</span><small>조건을 구별하며 읽기 · 짧은 예시</small></div>
    <div className="rx-preview-passage">{example.map((x,i)=><p key={i} className={example[step].active.includes(i)?"is-reading":""}>{x.source}</p>)}</div>
    <p className="rx-preview-question">28도에서 열린 창문이 26도가 되면?</p>
    <div className="rx-preview-thought" aria-live="polite"><span>선생님의 생각 · {example[step].label}</span><p>“{example[step].thought}”</p></div>
    <div className="rx-preview-controls"><button aria-label="이전 생각" disabled={step===0} onClick={()=>setStep(step-1)}><ArrowLeft size={17}/></button><span>생각 {step+1} / 3</span><button aria-label={step===2?"처음 생각 다시 보기":"다음 생각"} onClick={()=>setStep((step+1)%3)}><ArrowRight size={17}/></button></div>
  </div>;
}
