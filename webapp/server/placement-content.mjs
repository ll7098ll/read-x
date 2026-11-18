// Authored pilot material. Kept on the server so answer keys are never in student bundles.
import { firstCourseLessons } from '../shared/learning-config.mjs';
import { makeDiagnostic } from './diagnostic-forms.mjs';
import { reviewDiagnostic, publicAssessmentQuestion } from './assessment-review.mjs';
export const placementVersion = 'g16-placement-3';
export const skills = { words: '어휘·문장', evidence: '정보 확인', connect: '관계 연결',interpret:'추론·해석',evaluate:'근거 평가',integrate:'자료 통합' };
export const courseLessons = firstCourseLessons;
const passage = (id, title, paragraphs, rows) => ({ id, title, paragraphs, questions: rows.map((r, i) => {
  const options = [r[2], ...r[3]], offset = (i + id.length) % 4;
  return { id: `${id}-q${i}`, skill: r[0], prompt: r[1], options: options.slice(offset).concat(options.slice(0, offset)), answer: (4-offset)%4, evidence: r[4] };
}) });
const common = [
  passage('garden', '비가 온 뒤의 화분', [
    '민서는 창가에서 화분을 돌보았다. 금요일에는 흙이 말라서 물을 주었다. 토요일에는 창문으로 빗물이 들어와 흙이 촉촉해졌다.',
    '일요일에 민서는 화분에 물을 주려다가 흙을 만져 보았다. 아직 젖어 있어서 물뿌리개를 내려놓았다. 대신 화분받침에 고인 물을 비웠다.'
  ], [
    ['words','“촉촉해졌다”의 뜻으로 알맞은 것은?','조금 젖게 되었다',['단단하게 굳었다','완전히 말랐다','아주 뜨거워졌다'],[0]],
    ['evidence','민서가 금요일에 물을 준 까닭은?','흙이 말랐기 때문에',['비가 왔기 때문에','화분받침이 비었기 때문에','창문을 닫았기 때문에'],[0]],
    ['connect','토요일의 일과 일요일의 행동을 바르게 연결한 것은?','빗물이 흙을 적셔서 다음 날 물을 주지 않았다',['흙이 말라서 받침의 물을 채웠다','창문을 닫아서 흙이 젖었다','물을 주지 않아서 비가 왔다'],[0,1]],
    ['connect','민서의 행동에서 알 수 있는 것은?','흙의 상태를 살펴 물을 줄지 정했다',['매일 같은 양의 물을 주었다','비가 오면 화분을 버렸다','받침에 물이 많을수록 좋다고 생각했다'],[1]]
  ]),
  passage('library', '도서실의 새 안내', [
    '도서실은 월요일부터 금요일까지 오후 1시부터 4시까지 연다. 책은 한 번에 두 권까지 빌릴 수 있다. 빌린 책은 다음 주 같은 요일에 돌려준다.',
    '수요일에는 책장을 점검하므로 새로 책을 빌릴 수 없다. 다 읽은 책을 돌려주는 것은 가능하다. 반납함은 도서실 문 옆에 있다.'
  ], [
    ['words','안내에서 “반납”과 뜻이 가장 가까운 말은?','빌린 것을 돌려줌',['새 물건을 만듦','책을 미리 주문함','책장을 옮김'],[1]],
    ['evidence','한 번에 빌릴 수 있는 책은 몇 권까지인가?','두 권',['한 권','세 권','네 권'],[0]],
    ['connect','수요일 오후 2시에 할 수 있는 일은?','읽은 책을 돌려준다',['새 책 세 권을 빌린다','새 책 한 권을 빌린다','책장을 점검하지 못하게 한다'],[0,1]],
    ['connect','금요일에 빌린 책은 언제까지 돌려주어야 하는가?','다음 주 금요일',['이번 주 토요일','다음 주 월요일','다음 주 수요일'],[0]]
  ]),
  passage('shade', '그늘 쉼터 이용 기록', [
    '운동장 쉼터를 이용한 사람 수를 같은 시간 동안 세었다. 월요일: 그늘 자리 12명, 햇볕 자리 4명. 화요일: 그늘 자리 10명, 햇볕 자리 6명.',
    '두 날 모두 그늘 자리를 이용한 사람이 더 많았다. 기록에는 날씨와 사람들의 나이, 자리를 고른 이유는 적혀 있지 않다.'
  ], [
    ['words','“두 날 모두”가 가리키는 것은?','월요일과 화요일',['화요일과 수요일','오전과 오후','그늘과 햇볕'],[0,1]],
    ['evidence','화요일에 햇볕 자리를 이용한 사람은?','6명',['4명','10명','12명'],[0]],
    ['connect','기록과 맞는 설명은?','두 날 모두 그늘 자리 이용자가 더 많았다',['월요일에는 햇볕 자리가 더 많았다','화요일에는 두 자리의 수가 같았다','두 날 모두 이용자가 없었다'],[0,1]],
    ['connect','이 기록만으로 알 수 없는 것은?','그늘 자리를 고른 이유',['월요일 그늘 자리 이용자 수','화요일 햇볕 자리 이용자 수','더 많이 이용한 자리'],[0,1]]
  ])
];
const support = [
  passage('bag', '가방을 옮긴 까닭', ['지우는 가방을 창가에 두었다. 창문으로 비가 들어왔다.', '지우는 가방이 젖을까 봐 교실 안쪽으로 옮겼다. 그 뒤 창문을 닫았다.'], [
    ['words','“그 뒤”는 언제인가?','가방을 옮긴 다음',['비가 오기 전','가방을 두기 전','창문을 열기 전'],[1]],
    ['evidence','처음 가방이 있던 곳은?','창가',['복도','운동장','도서실'],[0]],
    ['connect','가방을 옮긴 까닭은?','빗물에 젖지 않게 하려고',['가방을 버리려고','창문을 열려고','운동장에 가려고'],[0,1]],
    ['connect','일어난 순서가 맞는 것은?','비가 들어옴 → 가방을 옮김 → 창문을 닫음',['창문을 닫음 → 비가 들어옴 → 가방을 둠','가방을 옮김 → 비가 오기 시작함 → 가방을 둠','창문을 닫음 → 가방을 옮김 → 비가 들어옴'],[0,1]]
  ]),
  passage('seed', '싹을 돌보는 약속', ['씨앗을 심은 뒤에는 흙이 마르면 물을 조금 준다. 흙이 젖어 있으면 물을 더 주지 않는다.', '오늘 아침에는 흙이 말라 있었다. 수아는 물을 조금 주고 관찰 공책에 적었다.'], [
    ['words','“관찰”에 가까운 뜻은?','모습과 변화를 자세히 살핌',['아무렇게나 짐작함','물건을 빌림','씨앗을 버림'],[1]],
    ['evidence','오늘 아침 흙의 상태는?','말라 있었다',['젖어 있었다','얼어 있었다','기록이 없다'],[1]],
    ['connect','수아가 물을 준 까닭은?','흙이 마르면 물을 준다는 약속에 따라서',['공책이 젖어서','흙이 젖어 있어서','물을 많이 버리려고'],[0,1]],
    ['connect','내일 흙이 젖어 있다면 약속에 맞는 행동은?','물을 더 주지 않는다',['물을 아주 많이 준다','씨앗을 꺼낸다','공책을 버린다'],[0]]
  ])
];
const extend = [
  passage('bridge', '다리가 막힌 날', ['도서실에 가는 길은 두 가지다. 다리를 건너면 5분, 공원을 돌아가면 9분이 걸린다. 비가 많이 오면 다리를 막는다.', '오늘은 비가 많이 와서 다리가 막혔다. 유나는 도서실에 늦지 않으려고 평소보다 4분 일찍 출발했다.'], [
    ['words','“평소보다”는 무엇과 비교하는 말인가?','보통 때와',['내일과','다른 사람과','도서실 크기와'],[1]],
    ['evidence','공원을 돌아가면 걸리는 시간은?','9분',['4분','5분','14분'],[0]],
    ['connect','오늘 공원 길로 가야 하는 까닭은?','비가 많이 와서 다리를 막았기 때문에',['공원이 더 빠르기 때문에','도서실이 닫혔기 때문에','다리가 새로 생겼기 때문에'],[0,1]],
    ['connect','4분 일찍 출발한 이유로 알맞은 것은?','돌아가는 길은 평소 다리 길보다 4분 더 걸려서',['다리가 평소보다 4분 빨라져서','도서실이 4분 늦게 열어서','공원이 4분 뒤에 닫혀서'],[0,1]]
  ]),
  passage('poster', '안내문을 고친 뒤', ['동아리는 준비물을 잊는 친구가 많아서 안내문을 고쳤다. 준비물을 첫 줄에 쓰고, 글씨도 크게 바꾸었다.', '다음 모임에서는 준비물을 잊은 친구가 줄었다. 다만 두 가지를 함께 바꿨으므로 글씨 크기만의 효과인지는 이 기록으로 알 수 없다.'], [
    ['words','“다만” 뒤에는 어떤 내용이 이어지는가?','앞의 결과를 해석할 때 주의할 점',['동아리의 이름','준비물의 가격','다음 모임 날짜'],[1]],
    ['evidence','안내문에서 함께 바꾼 것은?','준비물의 위치와 글씨 크기',['모임 장소와 날짜','준비물 종류와 가격','동아리 이름과 인원'],[0]],
    ['connect','기록에 맞게 말한 것은?','안내문을 고친 뒤 준비물을 잊은 친구가 줄었다',['모든 친구가 준비물을 잊었다','글씨만 바꾸었다','모임을 취소했다'],[0,1]],
    ['connect','글씨 크기만의 효과라고 단정하기 어려운 까닭은?','준비물을 적은 위치도 함께 바꿨기 때문에',['친구가 하나도 없어서','글씨를 바꾸지 않아서','안내문을 없앴기 때문에'],[0,1]]
  ])
];
export function legacyPlacementForm(grade, branch = null) {
  if (![3,4].includes(grade)) throw new Error('초3~4 진단만 제공됩니다.');
  const passages = structuredClone([...common, ...(branch ? branch === 'support' ? support : extend : [])]);
  if (grade === 4) passages[0].paragraphs.push('민서는 물을 주는 날짜만 정하기보다 실제 흙의 상태를 확인하는 것이 필요하다고 공책에 적었다.');
  const questions = passages.flatMap(p => p.questions.map(q => ({ ...q, passageId: p.id })));
  if (branch) for (const [i,p] of passages.slice(-2).entries()) questions.push({ id:`explain-${i}`, passageId:p.id, skill:'connect', prompt:'이 글의 사건이나 정보를 두 가지 이상 연결해서 설명하고, 근거가 되는 문단을 골라 주세요.', options:[], evidence:p.paragraphs.map((_,j)=>j), rubric:'두 정보를 정확하게 사용하고 그 관계를 설명했는지 확인합니다. 문장 길이나 맞춤법만으로 읽기 이해를 판단하지 않습니다.' });
  return { version:'g34-pilot-1', grade, branch, passages, questions };
}
export function placementFormAtVersion(grade,branch=null,version=placementVersion){
 if(![1,2,3,4,5,6].includes(grade)||branch!==null&&!['support','extend'].includes(branch))throw new Error('학년과 진단 분기를 확인해 주세요.');
 if(version==='g34-pilot-1')return legacyPlacementForm(grade,branch);
 const raw=makeDiagnostic(grade,branch,legacyPlacementForm);
 return version==='g16-placement-2'?raw:reviewDiagnostic(raw);
}
export const placementForm=(grade,branch=null)=>placementFormAtVersion(grade,branch);
export const publicForm = form => ({ ...form, passages: form.passages.map(({questions,...p})=>p), questions: form.questions.map(publicAssessmentQuestion) });
export function profileFor(form, answers) {
  return Object.keys(skills).map(skill => { const qs=form.questions.filter(q=>q.skill===skill && q.options.length); const correct=qs.filter(q=>answers[q.id]?.choice===q.answer).length; return {skill,label:skills[skill],correct,total:qs.length}; }).filter(p=>p.total>0);
}
export function recommend(form, answers) {
  const profile=profileFor(form,answers), need=profile.find(p=>p.correct/p.total < 0.7);
  const course=need?.skill || (form.grade>=5?'evaluate':'connect');
  return { course, courseName:({words:'뜻 익히기',evidence:'단서 짚기',connect:'관계 엮기',interpret:'의미 풀기',evaluate:'근거 따지기',integrate:'새롭게 엮기'})[course], level:profile[0].correct/profile[0].total<0.6?'supported':'standard', profile,
    reason:need?`${need.label} ${need.correct}/${need.total} 정답으로 이 기능을 먼저 연습하도록 추천합니다.`:'표집한 기능의 정답은 충분했습니다. 추천 코스와 자기 설명을 첫 수업에서 더 확인합니다.',
    supplements:profile.filter(p=>p.skill!==course && p.correct/p.total<0.7).map(p=>p.label), policyVersion:form.version||placementVersion };
}
