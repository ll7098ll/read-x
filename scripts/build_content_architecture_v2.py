"""Planning candidates and quotas only. Does not generate or approve learning content."""
from pathlib import Path
import json,collections,csv
ROOT=Path(__file__).resolve().parents[1]
STAGES=[('S1','뜻 익히기',2,3),('S2','단서 짚기',4,4),('S3','관계 엮기',6,4),('S4','의미 풀기',4,4),('S5','근거 따지기',3,5),('S6','새롭게 엮기',1,6)]
TRACKS={
 'language':dict(label='말소리·낱말·문장',count=12,bands=[
 ['글자와 소리 대응','낱말 끊어 읽기','짧은 문장 정확히 읽기','비슷한 소리 구별','낱말의 같은 부분','문맥에서 낱말 뜻','여러 뜻의 낱말','대상과 행동 연결','조사에 따른 뜻','문장 끝과 뜻','이것이 가리키는 대상','이어 주는 말'],
 ['낱말 부분의 뜻','낱말 사이 포함 관계','다의어 문맥 판별','비슷한 말의 차이','낯선 말 뜻 짐작','문장 성분의 역할','주어와 서술어 호응','꾸미는 말의 범위','지시어 연결','접속어와 관계','부정 표현의 범위','문맥에 맞는 고쳐쓰기'],
 ['학습어의 뜻과 쓰임','형태소와 문맥 대조','추상어의 구체적 의미','다의어와 전문적 의미','유의어의 어감 차이','문장 성분과 의미','복잡한 문장 호응','수식 범위와 중의성','담화의 지시 관계','접속과 논리 전환','조건·부정의 범위','객관적 표현과 인용']]),
 'information':dict(label='정보 읽기',count=14,bands=[
 ['설명 대상 찾기','대상의 특징 찾기','대상과 특징 연결','필요한 정보 선택','중심 내용 찾기','중심과 자세한 내용','차례에 맞게 읽기','두 대상 비교','까닭과 결과 연결','한 조건 적용','단순한 예외 확인','빠진 내용 짐작','짧게 간추리기','설명 목적 찾기'],
 ['세부 정보 정확히 확인','중심 생각 파악','중심과 뒷받침 구분','핵심어로 간추리기','조건 보존 요약','문단 순서와 기능','정의와 예시 연결','비교 기준 적용','인과 관계 연결','분류 기준 확인','조건과 예외 적용','생략된 관계 추론','주장과 근거 연결','내용과 표현 검토'],
 ['핵심 정보와 경쟁 정보','중심 명제와 범위','개념 정의와 적용','중심·세부 위계','복합 구조 요약','문단 기능과 전개','원리와 사례 적용','복수 기준 비교','다중 인과와 한계','조건·예외 우선순위','근거의 충분성','출처와 정보 신뢰성','관점 간 공통·차이','문제 해결에 정보 활용']]),
 'literature':dict(label='문학 읽기',count=10,bands=[
 ['인물과 배경 찾기','중요한 사건 찾기','사건의 차례','말과 행동 연결','인물의 마음 짐작','마음이 달라진 까닭','시의 소리와 반복','감각으로 표현한 장면','사물에 마음을 담은 표현','작품과 경험 나누기'],
 ['배경과 사건의 관계','사건의 원인과 결과','인물 말과 행동 해석','인물의 마음 변화','인물 사이 관계','시의 화자와 상황','감각과 비유의 효과','장면과 분위기','작품의 중심 의미','다른 해석의 근거'],
 ['서술 정보와 시점','인물의 선택과 갈등','관계 변화와 사건 구조','시간 전환과 의미','말과 행동의 불일치','화자의 태도와 정서','상징·함축의 근거','표현 방식과 효과','해석 비교와 타당성','작품과 사회·삶의 연결']]),
 'media':dict(label='매체와 자료 읽기',count=8,bands=[
 ['생활 표지의 뜻','그림과 글 연결','간단한 표에서 찾기','그림 기호의 단위','안내 지도와 방향','화면의 버튼과 행동','광고와 알림의 목적','두 안내의 같은 점과 차이'],
 ['본문과 표 대응','그래프 범례와 단위','그림·지도 통합','자료의 부분과 전체','수치와 설명의 일치','작성 날짜와 변경','매체의 의도와 독자','자료 간 일치·충돌'],
 ['여러 자료의 범위 비교','단위·분모·비율 해석','시각적 강조의 효과','누락 정보와 대표성','출처·시점·버전 검증','측정값과 주장 구별','상충 자료의 조정','목적에 따른 정보 재구성']]),
 'writing':dict(label='자기 표현과 쓰기',count=12,bands=[
 ['쓸 대상과 독자 정하기','쓰는 목적 정하기','관찰 정보 모으기','필요한 내용 고르기','이름과 특징 문장 쓰기','사건을 차례로 쓰기','처음·가운데·끝 짜기','까닭을 붙여 설명하기','알림과 안내 쓰기','경험과 느낌 쓰기','빠진 정보 보충','틀린 정보와 표현 고치기'],
 ['독자와 목적 계획','자료의 사실 확인','관련 내용 생성','정보 선별과 묶기','설명 구조 선택','개요와 문단 조직','중심·뒷받침 문장','인과·비교 설명 쓰기','근거를 붙인 의견','요약과 재표현','내용·조직 고쳐쓰기','호응·지시·접속 고쳐쓰기'],
 ['독자·목적·매체 설계','다중 출처 정보 수집','신뢰성과 사용 범위 확인','주제와 내용 범위 조절','복합 개요 조직','문단의 기능과 연결','정의·원리 설명 쓰기','자료 인용과 설명 통합','주장·근거·반론 구성','독자에 맞게 재표현','내용·논리·조직 수정','표현·호응·인용 수정']]),
 'oral':dict(label='듣기와 말하기',count=4,bands=[
 ['듣고 대상과 행동 확인','차례를 지켜 질문·응답','본 것을 또렷이 설명','친구의 말에 이유로 답하기'],
 ['듣고 핵심과 이유 정리','모르는 내용을 질문','근거와 순서로 발표','다른 의견을 듣고 조정'],
 ['관점과 근거를 들으며 정리','주장을 확인하는 질문','자료를 활용한 발표','반론을 듣고 설명 수정']])}
GRADES={
 1:'생활어·짧은 문장·직접 관찰 가능한 대상. 두 특징이나 행동을 연결하고 한두 문장으로 표현.',
 2:'짧은 문단·생활 규칙·두 조건. 가까운 정보의 관계와 단순 예외를 설명.',
 3:'문단 중심 생각·기초 교과어·간단한 표. 중심과 세부, 문단 사이 관계를 짧은 글로 설명.',
 4:'여러 문단·생략 관계·조건과 예외. 자료 대응과 범위 차이를 근거로 설명하고 수정.',
 5:'정의·원리·경쟁 근거·복수 조건. 자료의 관점과 한계를 비교하고 조건부로 표현.',
 6:'복합 구조·다중 자료·반례와 불확실성. 새 독자·매체·목적에 맞게 종합하고 수정.'}

def build():
 config=dict(schemaVersion='readx-planning-2',status='proposal_not_authored_content',asOf='2026-11-14',
   stages=[dict(id=i,label=l,setsPerSkill=s,questionsPerSet=q) for i,l,s,q in STAGES],tracks=TRACKS,grades=GRADES,
   purposesPerSkill=dict(practice=14,independent_check=3,transfer_check=2,delayed_check=1),
   note='각 학년60개는 편성 예산이다. 학년군·목표 적합성을 검토하여 합치거나 나누고 물량을 재산정한다.')
 skills=[];cells=[];errors=[]
 for g,condition in GRADES.items():
  raw=json.loads((ROOT/f'data/item_bank/g{g}_item_bank.json').read_text(encoding='utf-8-sig'))
  existing={s['slot_id'] for s in raw['expository_slots']}|{s['code'] for s in raw['common_slots']}
  for track,t in TRACKS.items():
   names=t['bands'][(g-1)//2]
   assert len(names)==t['count']
   for n,name in enumerate(names,1):
    sid=f'plan-G{g}-{track}-{n:02}'
    candidates=[]
    if track=='language':candidates=sorted(x for x in existing if '-COM-' in x)
    if track=='information':candidates=sorted(x for x in existing if '-EXP-V' in x)
    if track=='writing':candidates=sorted(x for x in existing if '-EXP-W' in x)
    if track=='media':candidates=sorted(x for x in existing if x.endswith(('V2-3','V3-1','V3-2','V3-3')))
    skills.append(dict(id=sid,grade=g,track=track,name=name,gradeCondition=condition,
      candidateMacroGoalIds=candidates,mappingState=('needs_individual_mapping' if candidates else 'needs_new_goal_review'),
      standardRefs=[],curriculumAlignment='not_yet_verified',publicationState='planning_only'))
    for stage,label,sets,questions in STAGES:
     cells.append(dict(skillId=sid,grade=g,track=track,stage=stage,stageLabel=label,targetSets=sets,
       targetQuestions=sets*questions,authoredSets=0,approvedSets=0,fitReview='pending'))
 counts=dict(skills=len(skills),stageCells=len(cells),targetSets=sum(c['targetSets'] for c in cells),targetQuestions=sum(c['targetQuestions'] for c in cells))
 assert counts==dict(skills=360,stageCells=2160,targetSets=7200,targetQuestions=29880)
 assert len({s['id'] for s in skills})==360
 for g in GRADES:
  assert sum(s['grade']==g for s in skills)==60
  assert sum(c['targetSets'] for c in cells if c['grade']==g)==1200
  assert sum(c['targetQuestions'] for c in cells if c['grade']==g)==4980
 assert sum(config['purposesPerSkill'].values())==20
 pilot=dict(skills=12,sets=12*6*2,questions=12*sum(q*2 for _,_,_,q in STAGES))
 coverage=dict(stageCells=2160,baselineSets=2160,baselineQuestions=360*sum(q for _,_,_,q in STAGES),
  cumulativeSetsIncludingPilotExtras=2160+12*6,cumulativeQuestionsIncludingPilotExtras=360*sum(q for _,_,_,q in STAGES)+12*sum(q for _,_,_,q in STAGES))
 assert pilot==dict(skills=12,sets=144,questions=624)
 assert coverage['cumulativeSetsIncludingPilotExtras']==2232 and coverage['cumulativeQuestionsIncludingPilotExtras']==9672
 dest=ROOT/'data/content_authoring/architecture_v2';dest.mkdir(parents=True,exist_ok=True)
 for name,value in [('config.json',config),('blueprint.json',dict(status='planning_candidates_only',counts=counts,skills=skills,cells=cells))]:
  (dest/name).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf-8')
 out=ROOT/'output/content-architecture-v2';out.mkdir(parents=True,exist_ok=True)
 with (out/'학년별_콘텐츠_편성표.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f);w.writerow(['학년','영역','수행후보','학년별조건','단계','자료묶음목표','문항목표','상태'])
  byid={s['id']:s for s in skills}
  for c in cells:
   s=byid[c['skillId']];w.writerow([s['grade'],TRACKS[s['track']]['label'],s['name'],s['gradeCondition'],c['stageLabel'],c['targetSets'],c['targetQuestions'],'계획·적합성검토대기'])
 report=dict(passed=True,counts=counts,pilot=pilot,coverage=coverage,
   actualContentGeneratedByThisScript=0,approvedContent=0,
   checks=['학년별60후보','트랙별후보수','후보ID중복없음','학년별묶음·문항예산','목적별예산합계','파일럿산식','대표추가분중복계산방지'],
   note='기계 검사는 편성 수량과 구조만 확인한다. 미세 수행·단계·교육과정 적합성은 검토 대기.')
 (out/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':build()
