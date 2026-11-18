"""Context-sensitive Korean sentence work; no math-style difficulty labels."""
from pathlib import Path
import hashlib, importlib, json
from author_pilot_v2 import E as emit, M, O, SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_05'
OUT=ROOT/'output/expansion-v2-05'
SKILLS=[f'plan-G{g}-language-{n}' for g,n in [(1,'08'),(2,'10'),(3,'06'),(4,'10'),(5,'08'),(6,'11')]]
CELLS={sid:['S2','S3','S4','S5'] for sid in SKILLS}
LABELS={1:['누가 무엇을 하는지 짚기','대상과 행동 잇기','생략된 대상 찾기','장면에 맞게 고치기'],
        2:['문장 끝 살피기','말과 대답 연결하기','묻는 말에 담긴 부탁 풀기','상황에 맞는 말 고르기'],
        3:['문장의 역할 짚기','서술어와 대상 연결하기','빠진 말 문맥에서 찾기','뜻을 보존하며 고치기'],
        4:['이어 주는 말 짚기','내용의 관계 잇기','연결에 담긴 뜻 풀기','관계가 맞는지 따지기'],
        5:['꾸미는 말 짚기','꾸미는 범위 비교하기','문맥으로 뜻 가려내기','모호한 표현 고치기'],
        6:['조건과 부정 짚기','조건의 범위 연결하기','부정의 뜻 문맥에서 풀기','단정과 누락 고치기']}

def C(prompt,answer,why,bad,quotes):
    t=M(prompt,answer,bad,quotes);t['why']=why;return t

def D(criterion,full,partial,zero):
    return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})

def A(kind,prompt,answer,quotes,criteria):
    t=O(kind,prompt,answer,quotes,'의미 또는 근거의 일부만 설명함','문맥과 반대되거나 근거 없이 단정함')
    t['analyticRubric']=criteria;return t

def E(skill,stage,title,text,guide,tasks):
    emit(skill,stage,'A',title,text,guide,tasks)
    s=SETS[-1];s['batch']='expansion-v2-05';s['learnerStageLabel']=LABELS[s['grade']][int(stage[1])-2]
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='주 응답 뒤에 보조 문항을 사용. 대독·받아쓰기·뒤 문항 및 해설 노출을 따로 기록.')
    s['textDemand'].update(format='자체 창작 장면·대화·문장 비교 자료',lengthReview='짧은 언어 집중 자료. 공인 학년 규준·장문 독해 충족 주장은 보류.')
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
        if q['kind']!='single_choice':
            q['acceptableResponses']='같은 문장만 정답으로 강요하지 않는다. 제시된 상황과 보존할 뜻을 만족하는 다른 표현도 수용한다. 문맥이 부족하면 가능한 해석과 추가 확인을 구별한 답을 수용한다.'
    if s['id']=='PV2-G5-language-08-S3-A':
        s['version']=2
        for q in s['questions']:
            q['version']=2
            for ref in q['evidence']:ref['version']=2
        s['revisionNotes']=['무대에 선 사람을 밝히는 예시 답에 긴 수식 표현을 다시 사용해 모호함이 남았으므로 독립 문장으로 풀어 씀. 한 문장 제한을 없애고 대상과 만난 사람의 관계를 보존하도록 수정.']
        s['teacherGuide']+=' 원고 v2: 예시 답에서도 꾸미는 대상이 모호하게 남는 문제를 고쳐 문장을 나누었다. 학생에게 한 문장만 쓰도록 제한하지 않는다.'
    if s['id'] in ('PV2-G2-language-10-S2-A','PV2-G2-language-10-S4-A','PV2-G3-language-06-S3-A'):
        s['version']=2
        for q in s['questions']:
            q['version']=2
            for ref in q['evidence']:ref['version']=2
        s['revisionNotes']=['장면과 동떨어진 오답을 줄이고 장소·날짜와 시각, 방법·상태 질문과 행동 부탁, 말 차례와 문장 역할의 실제 혼동을 대조하도록 선지 보완.']
        s['teacherGuide']+=' 원고 v2: 장면과 동떨어진 오답 대신 이 기능에서 실제로 혼동할 수 있는 관계를 선지로 대조했다.'
    assert tasks[0].get('analyticRubric')
    s['presentationOrder']=[q['id'] for q in s['questions']]
    s['languageReview']=dict(primaryQuestionId=s['questions'][0]['id'],responseMode='읽고 남긴 서면 설명·재표현',
      interpretationPolicy='문법 형식·문맥의 의미·전달 목적을 구별. 생략이나 여러 해석 가능성을 곧바로 비문으로 단정하지 않음.',
      notAssessed=['실제 발음·억양·듣기·말하기 상호작용은 서면 답안만으로 측정하지 않음','문법 용어 암기나 이 자료 하나로 학년 전체 언어 능력을 승인하지 않음'],teacherApproval='pending')
    s['teacherGuide']+=' 먼저 주 응답을 받고 뒤의 선택형과 해설 노출을 기록한다. 예시와 다른 표현은 뜻과 문맥을 기준으로 확인한다.'

def curriculum(s,registry):
    g=s['grade'];code={1:'2국04-03',2:'2국04-03',3:'4국04-03',4:'4국04-04',5:'6국04-06',6:'6국04-06'}[g]
    direct=g in (2,3,4);r=registry[code]
    scope={1:'짧은 문장에서 대상과 행동을 연결하는 문장 이해 준비 활동',2:'상황의 뜻에 맞게 문장 끝과 문장 부호를 살피고 문장을 쓰는 일부 수행',3:'누가·무엇을·어찌하다의 기본 짜임을 이해하고 사용하는 일부 수행',4:'글과 대화의 접속 표현을 이해하고 의도한 관계에 맞게 사용하는 일부 수행',5:'여러 해석이 가능한 문장을 독자와 목적에 맞게 명확히 쓰는 보조 활동',6:'조건·부정의 범위를 문맥과 대조하고 분명하게 쓰는 보조 활동'}[g]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='언어 성취요소 일부 후보' if direct else '문장 이해·명료한 표현의 보조',includedComponent=scope,notAssessed=s['languageReview']['notAssessed']+['전체 성취기준 달성과 언어에 대한 태도·호기심은 별도 확인'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문 대조. 최신 통합 고시 전량 비교·독립 교사 승인 별도 대기.',decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=scope,remainingGap='' if direct else '생략·중의성은 그 자체로 문법 오류가 아님. 준비·명료화 활동을 해당 성취기준의 직접 측정이라고 주장하지 않음.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct and q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['language_v2_lower','language_v2_middle','language_v2_upper']:importlib.import_module(name).author(E,C,O,A,D)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True)
    p=DEST/'sets.json';p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-05',scope='언어 새6수행의 S2~S5,24자료. S1·S6 및 반복·독립 확인 자료까지 모두 공급한 것은 아님.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored language:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions');return p

if __name__=='__main__':build()
