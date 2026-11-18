import React, { useId, useState } from 'react';
import { ArrowRight, Check, Lightbulb, RotateCcw } from 'lucide-react';

/** A local example: an evidence selection is never a mastery score. */
export function ReadingMethodDemo() {
  const id = useId();
  const [mode, setMode] = useState<'model' | 'practice'>('model');
  const [picked, setPicked] = useState<number | null>(null);
  const [hint, setHint] = useState(false);
  const sentences = ['운동장에 비가 내렸어요.', '그래서 체육 수업을 교실에서 했어요.'];
  return <div className="readx-method-demo">
    <div className="readx-demo-top"><span className="readx-badge"><span/> 오늘의 읽는 방법</span><span>원인과 결과</span></div>
    <h3>‘그래서’ 앞뒤를 연결해 봐요.</h3>
    <div className="readx-segment" role="group" aria-label="읽기 시범과 연습 전환">
      <button aria-pressed={mode === 'model'} onClick={() => setMode('model')}>1. 시범 보기</button>
      <button aria-pressed={mode === 'practice'} onClick={() => setMode('practice')}>2. 직접 해 보기</button>
    </div>
    <div className="readx-demo-paper" aria-label="연습 지문">
      {sentences.map((sentence, i) => <button key={sentence} className={`readx-sentence ${(mode === 'model' && i === 0) || (mode === 'practice' && picked === i) ? 'is-selected' : ''}`} disabled={mode === 'model'} aria-pressed={mode === 'model' ? i === 0 : picked === i} onClick={() => setPicked(i)}><span className="readx-line-no">0{i + 1}</span><span>{sentence}</span>{mode === 'practice' && picked === i && <Check size={17}/>}</button>)}
    </div>
    <div className="readx-thought" aria-live="polite"><Lightbulb size={19}/><div><b>{mode === 'model' ? '이렇게 생각해요' : '체육 수업을 교실에서 한 까닭은 무엇일까요?'}</b><p>{mode === 'model' ? '‘그래서’ 뒤에는 일어난 일이 있어요. 앞 문장으로 돌아가니, 비가 내린 것이 까닭이네요.' : picked === 0 ? '맞아요. 비가 내린 것이 까닭이에요. 앞의 까닭과 뒤의 결과를 연결했어요.' : picked === 1 ? '이 문장은 일어난 결과예요. ‘그래서’ 앞 문장에서 까닭을 찾아볼까요?' : '까닭을 알려 주는 문장 하나를 눌러 보세요.'}</p></div></div>
    <div className="readx-demo-bottom">{mode === 'model' ? <button className="readx-button readx-button-primary" onClick={() => setMode('practice')}>나도 단서 찾아보기 <ArrowRight size={17}/></button> : <><button className="readx-button readx-button-quiet" aria-expanded={hint} aria-controls={id} onClick={() => setHint(v => !v)}>{hint ? '힌트 접기' : '어디를 볼까요?'}</button><button className="readx-icon-button" aria-label="선택과 힌트 초기화" onClick={() => { setPicked(null); setHint(false); }}><RotateCcw size={18}/></button></>}</div>
    {mode === 'practice' && hint && <p className="readx-hint" id={id}>‘그래서’의 앞 문장에 “왜?”의 답이 있어요.</p>}
  </div>;
}
