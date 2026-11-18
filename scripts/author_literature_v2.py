"""Original poems and stories with evidence-bounded, nonexclusive literary interpretation."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_04'
OUT=ROOT/'output/expansion-v2-04'
CELLS={'plan-G1-literature-07':['S2','S3'],'plan-G2-literature-04':['S3','S4'],
       'plan-G3-literature-01':['S3','S4'],'plan-G4-literature-06':['S3','S4'],
       'plan-G5-literature-02':['S4','S5'],'plan-G6-literature-04':['S4','S5']}
SKILLS=list(CELLS)

def C(prompt,answer,why,bad,quotes):
    task=M(prompt,answer,bad,quotes);task['why']=why
    return task

def D(criterion,full,partial,zero):return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})

def A(kind,prompt,answer,quotes,criteria):
    task=O(kind,prompt,answer,quotes,'근거 또는 연결 의미 중 일부만 표현함','작품과 반대되거나 근거 없는 단정만 함')
    task['analyticRubric']=criteria
    return task

def E(skill,stage,variant,title,text,guide,tasks,poems=()):
    emit(skill,stage,variant,title,text,guide,tasks)
    s=SETS[-1];s['batch']='expansion-v2-04'
    s['learnerStageLabel']={1:{'S2':'반복되는 말 짚기','S3':'말의 반복과 움직임 잇기'},
      2:{'S3':'말과 행동 함께 읽기','S4':'말 뒤의 뜻 짐작하기'},
      3:{'S3':'장소와 행동 연결하기','S4':'배경의 역할 풀어 보기'},
      4:{'S3':'말하는 자리 비교하기','S4':'목소리의 주인 짐작하기'},
      5:{'S4':'선택의 이유와 갈등 풀기','S5':'인물 평가의 근거 따지기'},
      6:{'S4':'시간이 바뀐 장면 잇기','S5':'과거와 아직 오지 않은 일 구별하기'}}[s['grade']][stage]
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='완성 해석·정답은 응답 전에 제공하지 않음. 교사의 대독·받아쓰기·뒤 문항 노출은 별도 기록.')
    s['textDemand'].update(format='자체 창작시' if poems else '자체 창작 이야기',lengthReview='문학 갈래의 실제 글자 수·시 행 수를 별도 기록. 학년 규준·장문 코스 충족 승인은 교사 검토 대기.')
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
        if q['kind']!='single_choice':q['acceptableResponses']='예시는 유일한 해석이나 문장이 아니다. 작품의 구체적 단서와 해석의 관계가 설명되고 작품과 모순되지 않으면 다른 느낌·해석을 수용한다. 작품에 없는 심리·작가의 실제 경험을 확정한 답과 구별한다.'
    assert tasks[0].get('analyticRubric'),s['id']
    s['presentationOrder']=[q['id'] for q in s['questions']]
    s['literaryReview']=dict(primaryQuestionId=s['questions'][0]['id'],responseMode='작품을 읽고 남긴 서면 설명. 대독·구두 답의 받아쓰기 지원 시 별도 기록.',
      interpretationPolicy='다른 해석의 구체적 근거를 확인하며 예시 답의 감정말·인물 평가와 같은지만으로 채점하지 않음.',
      notAssessed=['실제 낭송·목소리의 변화·말하기 상호작용을 텍스트 답안만으로 판정하지 않음','문학에 대한 흥미·작가의 실제 경험·학생의 성격을 확정하지 않음'],teacherApproval='pending')
    if not poems:s['literaryReview']['workParagraphIds']=[p['id'] for p in s['paragraphs'] if not p['text'].startswith('가상 독자 의견:')]
    if poems:
        assets=[]
        for i,(heading,count) in enumerate(poems,1):
            start=next(j for j,p in enumerate(s['paragraphs']) if p['text']==heading);lines=s['paragraphs'][start+1:start+1+count]
            assert len(lines)==count and all(not p['text'].startswith('시 ') for p in lines)
            assets.append(dict(id=s['id']+'-P'+str(i),title=heading.split(':',1)[1].strip(),headingParagraphId=s['paragraphs'][start]['id'],
              lineParagraphIds=[p['id'] for p in lines],lines=[p['text'] for p in lines],authorship='자체 창작시'))
        s['poems']=assets;s['poetryHash']=hashlib.sha256(json.dumps(assets,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    s['source'].update(authorship='자체 창작 문학 작품 및 명시된 가상 독자 의견',factualBasis='허구의 인물·사건·화자. 특정 작가·기관·실제 경험의 원문이나 기록으로 주장하지 않음.')
    s['teacherGuide']+=' 주 해석 응답을 선택형보다 먼저 받는다. 예시와 다른 감상은 작품 단서를 확인하여 판단하고 실제 학생 답을 미리 만들어 채우지 않는다.'

def curriculum(s,registry):
    grade=s['grade'];code={1:'2국05-01',2:'2국02-04',3:'4국05-01',4:'4국05-04',5:'6국05-03',6:'6국05-03'}[grade]
    direct=grade in (2,3,5,6);r=registry[code];raw=(ROOT/r['sourcePath']).read_bytes()
    scope={1:'시의 반복 말과 움직임을 연결하는 말놀이·낭송의 준비 활동',2:'인물의 말·행동에서 생각과 의도를 짐작하는 부분',3:'작품의 장소·상황과 인물 행동·사건의 관계를 이해하는 부분',
      4:'시의 표현을 통해 화자와 상황을 짐작하는 감상 보조 활동',5:'인물의 선택·갈등과 사건 전개를 연결해 이해하는 부분',6:'시간이 바뀐 장면과 사건의 관계를 파악하는 부분'}[grade]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256(raw).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='문학·읽기 성취요소 일부 후보' if direct else '문학 감상의 준비·보조',includedComponent=scope,
      notAssessed=s['literaryReview']['notAssessed']+(['자신의 경험과 인물의 마음을 비교하는 전체 수행은 측정하지 않음'] if grade==2 else [])+['이 자료 하나로 성취기준 전체 달성·학년 난도를 승인하지 않음'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문·해설 대조. 최신 통합 고시 전량 대조 및 독립 교사 승인은 별도 대기.',decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=scope,remainingGap='' if direct else '서면 반복 말·화자 해석만으로 실제 낭송 또는 감각 표현 활용의 전체 수행을 측정하지 않음.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct and q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['literature_v2_lower','literature_v2_middle','literature_v2_upper']:importlib.import_module(name).author(E,C,O,A,D)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True)
    path=DEST/'sets.json';path.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-04',scope='문학 새6수행의 두 단계씩 집필한12자료. 여섯 단계 전체 공급 완료가 아님.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored literature:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions')
    return path

if __name__=='__main__':build()
