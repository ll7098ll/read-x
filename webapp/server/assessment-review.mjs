import { courseNotes } from './assessment-review-notes.mjs';
import { diagnosticNotes, explanationSamples } from './diagnostic-review-notes.mjs';
export const editorialReviewVersion='assessment-editorial-2026-11-17-v1';
const skillNames={words:'문맥 속 낱말',evidence:'명시 정보',connect:'인과·조건',interpret:'근거 있는 해석',evaluate:'판단의 범위',integrate:'자료 간 조건 통합'};
const partial={words:'문맥에 맞는 뜻을 설명했는지 확인한다.',evidence:'대상·시점·수치·예외를 보존했는지 확인한다.',connect:'원인과 결과의 방향 또는 적용 조건을 연결했는지 확인한다.',interpret:'관찰된 단서와 추론을 구별하고 연결했는지 확인한다.',evaluate:'자료에서 확인한 범위와 아직 확인하지 못한 것을 구별했는지 확인한다.',integrate:'두 자료의 조건을 함께 반영했는지 확인한다.'};
const upperFoils={
 '5:evaluate:0':['두 변경의 영향을 분리하지 않았다','소음이 줄었으므로 안내판만의 효과가 확정됐다','두 조치를 함께 했으므로 각 효과도 같다고 본다','놀이를 멈췄으므로 안내판은 어떤 영향도 없다'],
 '5:evaluate:1':['다른 모둠도 포함한 조사 범위를 확인한다','다섯 명 중 네 명이므로 전교생도 같은 비율이다','같은 다섯 답을 복사하면 조사 범위가 넓어진다','한 모둠 결과가 있으므로 다른 모둠 확인은 불필요하다'],
 '5:evaluate:2':['관찰하지 않은 거리와 상황까지 확대했다','출발 시각이 같으므로 다른 거리의 순위도 같다','오늘 먼저 왔으므로 다른 날도 언제나 먼저 온다','거리 조건이 같았으므로 오늘 순위도 알 수 없다'],
 '5:evaluate:3':['시간과 이해 능력을 같은 지표로 보았다','시간이 두 배이므로 이해한 양도 두 배라고 본다','읽은 시간이 늘었으므로 난도 확인은 필요 없다','이해 기록이 없으므로 읽은 시간 기록도 틀렸다'],
 '5:evaluate:4':['다른 체형의 사용자도 추가로 확인해야 한다','세 학생이 편했으므로 모든 체형에도 적합하다','새 의자이므로 사용자의 체형과 관계없이 편하다','같은 세 명이 다시 답하면 모든 체형이 확인된다'],
 '5:evaluate:5':['방문 횟수를 서로 다른 사람 수로 바꾸었다','재방문을 세었으므로 서로 다른 사람도 정확히 30명이다','사람 수를 안 셌으므로 방문 횟수도 기록되지 않았다','재방문은 사람 수를 늘리므로 반드시 30명보다 많다'],
 '5:evaluate:6':['위치는 같게 하고 두께만 다르게 비교한다','위치와 두께를 모두 바꿔 좋은 결과만 남긴다','수건 이름만 바꾸면 두께만의 효과가 확인된다','먼저 마른 수건만 재면 위치 차이를 없앨 수 있다'],
 '5:evaluate:7':['먼저 떠난 사람과 남은 사람의 생각이 다를 수 있다','만족 비율이 높으므로 먼저 떠난 사람도 만족했다','응답하지 않은 사람을 만족에 더해도 범위는 같다','끝까지 남은 사람의 답만 모든 참가자를 대표한다'],
 '6:evaluate:0':['동시 조치의 단독 영향을 분리할 근거가 부족하다','소음 감소가 있으므로 안내판의 단독 효과도 확정된다','함께 시행한 두 조치는 각각 같은 효과를 낸다','따로 비교하지 않았으므로 소음이 줄었다는 기록도 거짓이다'],
 '6:evaluate:1':['응답 범위와 선택 방식의 대표성이 확인되지 않았다','표본에서 80%이므로 전교생 선호율도 80%이다','자발적으로 답하면 모든 학생의 의견이 확인된다','학교 전체를 안 물었으므로 다섯 명 중 네 명이라는 계산도 틀렸다'],
 '6:evaluate:2':['다른 거리와 상황으로 확대할 근거를 살핀다','오늘의 순위가 있으면 모든 미래 순위도 같다','출발 시각이 같으므로 장거리 결과도 보장된다','다른 조건이 달라도 순위에는 영향을 줄 수 없다'],
 '6:evaluate:3':['관찰한 시간을 측정하지 않은 능력으로 바꾸었다','시간이 두 배이므로 이해 능력도 두 배로 확인됐다','난도를 안 재도 시간이 늘면 이해 증가량을 알 수 있다','능력 자료가 없으므로 시간 자료 자체도 쓸 수 없다'],
 '6:evaluate:4':['체형과 사용 시간의 범위를 더 확인해야 한다','세 사람의 한 시간 후기는 모든 체형의 장시간 사용을 대표한다','같은 세 명의 답을 복사하면 사용 시간도 길게 조사한 것이다','한 시간 편했으므로 더 긴 사용에서도 불편할 수 없다'],
 '6:evaluate:5':['방문은 30회이며 서로 다른 사람 수는 확인하지 않았다','방문이 30회였으므로 서로 다른 학생도 정확히 30명이다','동일인 방문을 포함했으므로 방문 기록은 모두 취소한다','사람 수를 조사하지 않았으므로 방문 장소도 알 수 없다'],
 '6:evaluate:6':['다른 조건을 맞추고 두께 차이를 비교한다','두께와 위치를 매번 함께 바꾸어 두께만의 효과를 정한다','먼저 마른 결과만 남겨 위치 영향을 통제한다','수건 이름만 바꾸어 관찰하면 두께의 영향이 분리된다'],
 '6:evaluate:7':['무응답을 만족으로 바꾸지 않고 빠진 집단의 영향을 본다','응답하지 않았으므로 불만이 없었다고 보고 만족으로 센다','남은 사람의 만족 비율을 전체 참가자에게 그대로 적용한다','무응답자를 빼면 조사한 범위도 전체 참가자로 넓어진다'],
 '5:integrate:7':['우리 반 10명 중 6명이며 다른 반은 확인하지 않았다','우리 반 결과가 60%이므로 다른 반도 같은 비율이다','학교 전체를 조사했더니 10명 중 6명이 걸어왔다','다른 반 자료가 없으므로 우리 반의 6명 기록도 사용할 수 없다']
};
const evidenceOverrides={
 '1:interpret:5':[0], '2:evidence:5':[2], '2:interpret:5':[0],
 '4:connect:7':[0], '4:interpret:3':[1], '4:interpret:4':[1], '4:interpret:6':[1], '4:interpret:7':[1],
 '5:connect:4':[0], '5:interpret:6':[1], '6:connect:4':[0], '6:interpret:6':[1]
};
function setChoices(q,choices){const position=q.answer;q.options=choices.map((_,i)=>choices[(i-position+choices.length)%choices.length]);q.answer=position;}
function difficulty(grade,skill,paragraphs,prompt,evidence){
 const chars=paragraphs.join('').length,conditions=(paragraphs.join(' ').match(/다만|이상|이하|경우|조건|않으면|없으면|때만|하지만|제외/g)||[]).length;
 const long=chars>[0,100,160,240,300,380,460][grade],multi=evidence.length>1;
 const band=long||conditions>=3?'도전':multi||['interpret','evaluate','integrate'].includes(skill)?'기본':'입문';
 return {band,basis:'편집상 요구 분석 · 학생 정답률로 보정하기 전',chars,paragraphs:paragraphs.length,conditions,requiredParagraphs:evidence.length,
  process:skillNames[skill]||'자기 설명',cautions:[...(long?['분량 부담을 수업에서 확인']:[]),...(/\d/.test(paragraphs.join(''))&&/몇|수량|수는|칸|더 준비|추가로/.test(prompt)?['간단한 계산 부담과 읽기 수행을 구별']:[]),...(grade<=2?['긴 문장·맞춤법보다 단서와 판단 연결을 확인']:[])]};
}
function addGuide(q,grade,skill,paragraphs,reason,evidence,{open=false,sample=reason}={}){
 if(!reason)throw Error(`문항별 해설이 없습니다: ${grade}/${q.id}`);
 q.evidence=[...evidence];
 q.evidenceQuotes=evidence.map(paragraph=>({paragraph,text:paragraphs[paragraph]}));
 if(q.evidenceQuotes.some(x=>!x.text))throw Error('근거 참조 오류: '+q.id);
 q.explanation=reason;q.sampleResponse=sample;
 q.optionReasons=q.options.map((option,i)=>i===q.answer?reason:`“${option}”로는 문항이 묻는 답을 뒷받침할 수 없습니다. ${reason}`);
 q.difficulty=difficulty(grade,skill,paragraphs,q.prompt,evidence);
 q.scoringGuide={full:`${partial[skill]||'본문의 단서 두 가지를 판단과 연결했는지 확인한다.'} 정답 문구를 그대로 쓰지 않아도 같은 뜻이면 인정한다.`,partial:'관련 정보는 찾았지만 관계·조건·범위가 빠지면 추가 질문 후 새 자료에서 확인한다.',doNotRequire:grade<=2?'긴 문장, 동일한 표현, 정확한 맞춤법을 통과 조건으로 삼지 않는다.':'해설과 똑같은 문장이나 분량을 통과 조건으로 삼지 않는다.',evidencePolicy:open?'참고 근거 범위이며 전부 선택할 의무는 없다. 실제 설명에 사용한 충분한 근거를 교사가 확인한다.':'필요 근거를 포함하면 관련 문단을 더 선택했다는 이유만으로 오답 처리하지 않는다. 근거를 실제로 연결했는지는 교사가 설명에서 확인한다.'};
 q.editorialReview={version:editorialReviewVersion,method:'AI 편집 검토 + 본문·선지 대조 + 자동 참조 검증',status:'교사 수업 검토 대상',empiricalDifficulty:'미보정'};
 return q;
}
export function reviewCourseCheck(grade,course,original,index){
 const q=structuredClone(original),key=`${grade}:${course}:${index}`;q.corrections=[];
 if(key==='2:integrate:4'){q.paragraphs=['약속: 작품 이름과 재료를 적어요.','내가 쓴 소개글: “작품 이름은 봄입니다.” 사용한 재료는 종이예요.'];q.corrections.push('소개글 원문과 별도 재료 정보를 구분하여 이미 적힌 정보를 다시 보태라는 모순 수정');}
 if(key==='1:evaluate:1'){q.paragraphs=['지우는 사과가 좋대요. 민수는 사과는 좋아하지 않고 배가 좋대요.'];q.corrections.push('배를 좋아한다는 사실만으로 사과를 싫어한다고 단정하지 않도록 선호를 명시');}
 if(key==='1:integrate:1'){q.paragraphs=['약속: 학교에 오는 날 책을 돌려줘요.','내 일정: 오늘은 학교에 안 가고 내일 학교에 가요.'];q.corrections.push('두 자료를 함께 읽어야 날짜를 정할 수 있도록 과제 보완');}
 if(key==='3:integrate:0'){q.paragraphs[1]='모임 날 비가 와서 실내 모임으로 확정되었다. 실내에서는 돗자리를 쓰지 않는다.';q.corrections.push('비 예보와 실제 실내 전환을 구분해 준비물 정답의 불확실성 해소');}
 if(key==='4:integrate:0'){q.paragraphs[1]='모임 날 비가 와서 주최 측이 실내 모임으로 확정했다.';q.corrections.push('예보만으로 실내가 확정된 것처럼 해석하던 문제 수정');}
 if(key==='5:connect:6'){q.paragraphs[1]='담당자가 자리를 비워서 학생은 책 제목을 적어 신청함에 넣었다.';q.corrections.push('신청 행동의 실제 조건인 담당자 부재를 본문에 명시');}
 if(key==='6:integrate:7'){q.paragraphs[0]='발표에는 두 반의 결과를 각각 밝히고 전체 조사 인원도 함께 말한다. 반별 비율을 단순 평균하지 않는다.';q.prompt='두 자료의 정보를 모두 반영한 발표는?';setChoices(q,['전체 30명이며 가 반 10명 중 6명, 나 반 20명 중 8명이 걸어왔다','전체 30명이며 두 반 모두 60%가 걸어왔다','전체 20명이며 가 반 10명 중 6명, 나 반 20명 중 8명이 걸어왔다','전체 30명이며 가 반 10명 중 8명, 나 반 20명 중 6명이 걸어왔다']);q.corrections.push('두 자료의 조건과 집단별·전체 인원을 함께 보존하는 통합 과제로 강화');}
 if(upperFoils[key]){setChoices(q,upperFoils[key]);q.corrections.push('고학년 오답을 부분 조건·범위 혼동을 진단하는 선지로 보완');}
 const evidence=evidenceOverrides[key]||q.evidence;
 if(JSON.stringify(evidence)!==JSON.stringify(q.evidence))q.corrections.push('충분한 최소 근거 문단으로 채점 기준 수정');
 q.evidenceAlternatives=[evidence];q.evidenceMode='contains-required-set';q.version=3;
 return addGuide(q,grade,course,q.paragraphs,courseNotes[grade][course][index],evidence);
}
export function reviewDiagnostic(raw){
 const form=structuredClone(raw);form.version='g16-placement-3';
 if(form.grade===4){const p=form.passages.find(p=>p.id==='shade');p.paragraphs[0]='운동장 쉼터를 이용한 횟수를 같은 시간 동안 세었다. 월요일: 그늘 자리 12회, 햇볕 자리 4회. 화요일: 그늘 자리 10회, 햇볕 자리 6회.';p.paragraphs[1]='두 날 모두 그늘 자리의 이용 횟수가 더 많았다. 날씨와 이용 이유는 기록하지 않았다.';
  const qs=form.questions.filter(q=>q.passageId==='shade');qs[1].prompt='화요일 햇볕 자리의 이용 횟수는?';qs[1].options=qs[1].options.map(x=>x.replace(/명/g,'회'));
  qs[2].options=['두 날 모두 그늘 자리 이용 횟수가 더 많았다','월요일에는 햇볕 자리 이용 횟수가 더 많았다','화요일에는 두 자리의 이용 횟수가 같았다','두 날 모두 두 자리의 이용 횟수가 0이었다'];qs[2].answer=0;
 }
 let cursor=0;
 form.questions=form.questions.map(q=>{
  const p=form.passages.find(p=>p.id===q.passageId),open=!q.options.length;
  const index=open?Number(q.id.split('-').at(-1)):Number(q.id.split('-q').at(-1));
  const reason=open?explanationSamples[form.grade][form.branch][index]:diagnosticNotes[form.grade][q.passageId][index];
  let evidence=q.evidence;
  if(form.grade===4&&q.passageId==='shade'&&index===1)evidence=[0];
  if(form.grade===4&&q.passageId==='library'&&index===2)evidence=[2];
  if(['3','4'].includes(String(form.grade))&&q.passageId==='shade'&&index===0)evidence=[0];
  if(form.grade===1&&q.passageId==='g1-d-star'&&index===0)evidence=[0];
  if(!open){const correct=q.options[q.answer],wrong=q.options.filter((_,i)=>i!==q.answer);q.answer=(cursor+form.grade)%q.options.length;cursor++;setChoices(q,[correct,...wrong]);}
  const revised=addGuide(q,form.grade,q.skill,p.paragraphs,reason,evidence,{open,sample:reason});
  revised.corrections=form.grade===4&&q.passageId==='shade'?['재이용 횟수와 사람 수를 섞어 쓰던 문장·단위 수정']:[];
  return revised;
 });
 form.passages=form.passages.map(p=>({...p,questions:form.questions.filter(q=>q.passageId===p.id)}));
 return form;
}
export function matchesAssessmentEvidence(content,selected){
 if(!Array.isArray(selected)||!Array.isArray(content.paragraphs)||selected.some(i=>!Number.isInteger(i)||i<0||i>=content.paragraphs.length))return false;
 if(content.evidenceMode==='contains-required-set')return content.evidenceAlternatives.some(set=>set.every(i=>selected.includes(i)));
 return JSON.stringify([...new Set(selected)].sort())===JSON.stringify([...content.evidence].sort());
}
export function publicAssessmentQuestion(q){const {id,skill,prompt,options,passageId,grade,oralAllowed,version}=q;return {id,skill,prompt,options,passageId,grade,oralAllowed,version};}
