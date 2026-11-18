import React from 'react';
// Content is supplied only by staff APIs or released, reviewed learner feedback.
export function AssessmentGuide({item:q,teacher=true}:any){
 if(!q?.explanation)return null;
 return <details className="assessment-guide"><summary>{teacher?'정답·근거·해설과 채점 준거':'정답과 근거 다시 살펴보기'}</summary>
  {!!q.options?.length&&Number.isInteger(q.answer)&&<p><strong>정답:</strong> {q.answer+1}. {q.options[q.answer]}</p>}
  <p>{q.explanation}</p>
  <h5>본문 근거</h5>{q.evidenceQuotes?.map(e=><blockquote key={e.paragraph}><b>{e.paragraph+1}문단</b> · {e.text}</blockquote>)}
  {!!q.options?.length&&<><h5>선지별 검토</h5><ol>{q.options.map((o,i)=><li key={i}><b>{o}</b><p>{q.optionReasons?.[i]}</p></li>)}</ol></>}
  {teacher&&<><h5>자기 설명 확인</h5><p>표현 예: {q.sampleResponse}</p><p>{q.scoringGuide?.full}</p><p>{q.scoringGuide?.partial}</p><p>{q.scoringGuide?.doNotRequire}</p><p>{q.scoringGuide?.evidencePolicy}</p>
   {q.difficulty&&<p>편집 난도: {q.difficulty.band} · {q.difficulty.process} · {q.difficulty.basis}{q.difficulty.cautions?.length?` · ${q.difficulty.cautions.join(' / ')}`:''}</p>}
   {q.pilotCalibration&&<p>교사 승인 파일럿 난도: {q.pilotCalibration.band} · 첫 독립 수행 {q.pilotCalibration.n}명 · 정답률 {Math.round(q.pilotCalibration.p*100)}% · 해당 표본의 관찰 결과</p>}
   {q.editorialReview&&<small>{q.editorialReview.method} · {q.pilotCalibration?'파일럿 관찰 별도 표시':'실제 학생 난도 미보정'} · 교사 수업 검토 대상</small>}
  </>}
 </details>;
}
