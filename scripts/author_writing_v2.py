"""Original writing production tasks, each with a specific audience and analytic criteria."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_03'
OUT=ROOT/'output/expansion-v2-03'
SKILLS=['plan-G1-writing-05','plan-G2-writing-10','plan-G3-writing-07',
        'plan-G4-writing-11','plan-G5-writing-08','plan-G6-writing-10']

def C(prompt,answer,why,bad,quotes):
    task=M(prompt,answer,bad,quotes);task['why']=why
    return task

def D(criterion,full,partial,zero):
    return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})

def W(prompt,answer,quotes,plan,criteria,reader,purpose,length,origin='provided_scenario'):
    task=O('writing',prompt,answer,quotes,'필수 내용 일부만 표현함','필수 내용이 없거나 자료·목적에 어긋남')
    task.update(planningPrompt=plan,analyticRubric=criteria,writerContext=dict(reader=reader,purpose=purpose,length=length,responseOrigin=origin))
    return task

def E(skill,stage,variant,title,text,guide,tasks):
    emit(skill,stage,variant,title,text,guide,tasks)
    s=SETS[-1];s['batch']='expansion-v2-03'
    labels={
      1:['이름과 특징 익히기','알맞은 특징 골라 쓰기','대상과 특징 엮어 쓰기','읽는 사람을 생각해 보충하기','어긋난 특징 고치기','새 대상을 소개하기'],
      2:['일과 느낌 구별하기','경험의 한 장면 쓰기','일의 흐름과 느낌 잇기','느낌이 생긴 까닭 풀기','내 표현 다시 살피기','새 독자에게 경험 전하기'],
      3:['중심과 뒷받침 익히기','중심에 맞는 내용 쓰기','문장을 문단으로 엮기','빠진 뒷받침 보충하기','중심에 맞게 다듬기','새 자료로 문단 짜기'],
      4:['고쳐 쓸 기준 익히기','빠진 내용 찾아 고치기','흐름을 살려 고치기','독자 반응으로 보완하기','수정 의견 따져 고치기','새 글을 스스로 다듬기'],
      5:['자료와 내 설명 구별하기','출처를 밝혀 가져오기','인용과 설명 이어 쓰기','범위를 지키며 풀어 쓰기','인용의 정확성 따지기','여러 자료로 설명 엮기'],
      6:['독자에 맞는 말 익히기','필요한 정보 남겨 쓰기','형식에 맞게 재구성하기','낯선 말을 풀어 쓰기','바뀐 뜻 살펴 고치기','새 독자와 매체로 바꾸기']
    }
    s['learnerStageLabel']=labels[s['grade']][int(stage[1:])-1]
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='S1의 방법·예 설명 외 응답 전 완성 답 제공 없음. 추가 도움·뒤 문항 노출은 따로 기록.')
    s['textDemand'].update(format='쓰기 상황·내용 카드·초고·가상 독자 반응',lengthReview='생산 과제의 자극 자료. 설명문 장문 코스의 공급량으로 계산하지 않음.')
    primary=[]
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda option:hashlib.sha256((q['id']+'\0'+option['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,option in enumerate(q['options']) if option['text']==t['answer'])
        if q['kind']=='writing':
            q['planningPrompt']=t['planningPrompt'];q['rubric']=t['analyticRubric'];q['writerContext']=t['writerContext'];primary.append(q['id'])
            if s['grade']==2:q['planningPrompt']='글의 출발점(본인 경험 / 가상 인물)을 먼저 적어요. '+q['planningPrompt']
            q['acceptableResponses']='예시는 유일한 문장이 아니다. 필수 의미·독자·목적·자료 범위를 충족하는 다른 표현과 적절한 구성을 수용한다. 맞춤법은 별도 관찰하며 내용 점수를 일괄 0점으로 만들지 않는다.'
    assert len(primary)==1,s['id']
    s['presentationOrder']=primary+[q['id'] for q in s['questions'] if q['id'] not in primary]
    s['writingProtocol']=dict(primaryQuestionId=primary[0],firstResponse='모범 답·선택지·보조 문항을 보기 전의 초고를 따로 보관',
      observationFields=['독자·목적에 대한 계획','학생의 초고 원문','검토한 준거','학생의 수정고 원문','고친 부분과 이유','받은 도움·예시·뒤 문항 노출','직접 쓴 글인지 받아쓴 글인지','본인 경험인지 가상 상황인지'],
      supportPolicy='글을 대신 적어 주거나 함께 문장을 구성한 경우 도움의 종류를 기록. 구두 응답만으로 독립 쓰기를 수행했다고 집계하지 않음.',
      storageLimit='이 문제집의 입력 칸은 초고·수정고를 구별하지만 제출 잠금·첫 응답의 불변 보관·교사 승인 기능을 보장하지 않음.')
    s['teacherGuide']+=' 학생이 쓰는 과제를 선택형보다 먼저 제시한다. 뒤 문항이나 예시를 본 뒤의 수정은 첫 초고와 구별한다. 실제 답안이 없으면 관찰란과 점수를 채우지 않는다.'
    if s['grade']==2:s['teacherGuide']+=' 본인 경험과 가상 인물의 장면을 구별해 기록한다. 가상 인물 글만으로 학생 자신의 경험 표현 전체를 달성했다고 판정하지 않는다.'

def add_curriculum(s,standards):
    grade=s['grade'];code={1:'2국03-03',2:'2국03-02',3:'4국03-01',4:'4국03-01',5:'6국03-01',6:'6국03-04'}[grade]
    official=standards[code];raw=(ROOT/official['sourcePath']).read_bytes()
    primary=s['writingProtocol']['primaryQuestionId']
    scope={1:'주어진 대상의 이름과 특징을 연결해 소개 문장을 쓰는 부분',2:'선택한 작은 경험에서 일과 느낌을 문장으로 표현하는 부분. 본인 경험으로 수행했는지 별도 확인',
      3:'중심 문장과 관련된 뒷받침 문장을 갖추어 문단을 생산하는 부분',4:'내용·문장·문단의 흐름을 검토해 고쳐 쓰는 부분',
      5:'대상의 특성을 설명하며 인용과 자신의 설명을 연결하는 부분. 주장 글 전체를 측정하지 않음',6:'독자·매체에 필요한 내용을 남기고 낱말·구성을 바꾸어 쓰는 부분'}[grade]
    ref=dict(id=s['id']+'-C1',code=code,subject=official['subject'],statement=official['statement'],gradeBand=official['gradeBand'],
      sourcePath=official['sourcePath'],sourceLine=official['sourceLine'],noticeVersion=official['noticeVersion'],sourceHash=hashlib.sha256(raw).hexdigest(),
      alignmentState='source_text_checked_candidate',role='direct_component',roleLabel='쓰기 성취요소 일부 후보',includedComponent=scope,
      notAssessed=['서면 선택형·보조 응답만으로 실제 쓰기 수행을 인정하지 않음','쓰기에 대한 흥미·자신감·공유 태도의 지속적 변화는 측정하지 않음','이 자료 하나로 성취기준 전체 달성·학년 난도를 승인하지 않음'],questionIds=[primary])
    audit=dict(version=1,checkedOn='2026-11-17',basis='로컬 2022-33 국어 원문·해설 대조. 최신 통합 고시 전량 대조와 교사 승인은 별도 대기.',decision='direct_component_candidate',scope=scope,remainingGap='',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if q['id']==primary else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==primary else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for module in ['writing_v2_lower','writing_v2_middle','writing_v2_upper']:importlib.import_module(module).author(E,C,O,W,D)
    standards={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:
        add_curriculum(s,standards)
        s['source']['authorship']='자체 창작 쓰기 상황·내용 카드·초고·가상 기록. 본인 경험 선택 시 실제 내용은 학습자가 작성.'
        s['source']['factualBasis']='활동에 필요한 정보는 자극 자료 안에 제공. 실제 기관·조사·교사 의견·학생 응답으로 주장하지 않음.'
    DEST.mkdir(parents=True,exist_ok=True)
    source=DEST/'sets.json';source.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-17',batch='expansion-v2-03',
      scope='새 쓰기6수행의 여섯 단계에 한 자료씩. 실제 쓰기36과 보조120, 합계36자료·156과제. 실제 학생 답안·교사 승인 없음.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored writing:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'tasks')
    return source

if __name__=='__main__':build()
