"""Original literary works with new functions, bounded interpretations and visible evidence."""
from pathlib import Path
import hashlib, importlib, json
from author_pilot_v2 import E as emit, O, SETS
from author_literature_v2 import C, A, D

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_10'
OUT=ROOT/'output/expansion-v2-10'
SKILLS=[f'plan-G{g}-literature-{n}' for g,n in [(1,'02'),(2,'09'),(3,'05'),(4,'08'),(5,'07'),(6,'09')]]
CELLS={sid:['S2','S4','S5'] for sid in SKILLS}
LABELS={
 1:{'S2':'이야기를 바꾼 일 짚기','S4':'중요한 일이 한 역할 풀기','S5':'이야기의 중심과 맞춰 보기'},
 2:{'S2':'사람처럼 표현한 말 짚기','S4':'사물에 담긴 마음 풀기','S5':'표현에 어울리는 느낌 살피기'},
 3:{'S2':'인물 사이의 말과 행동 짚기','S4':'달라지는 관계 풀기','S5':'관계를 설명한 근거 따지기'},
 4:{'S2':'장면의 소리와 모습 짚기','S4':'장면에 흐르는 느낌 풀기','S5':'분위기 해석의 근거 살피기'},
 5:{'S2':'되풀이되는 사물과 행동 짚기','S4':'사물에 더해진 의미 풀기','S5':'상징을 하나의 뜻으로 단정하지 않기'},
 6:{'S2':'해석마다 짚은 근거 살피기','S4':'서로 다른 해석 연결하기','S5':'설명할 수 있는 범위 따지기'},
}

def E(skill,stage,title,text,guide,tasks,poem_lines=0):
    emit(skill,stage,'A',title,text,guide,tasks);s=SETS[-1]
    s['batch']='expansion-v2-10';s['learnerStageLabel']=LABELS[s['grade']][stage]
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='주 서면 해석을 보조 선택형보다 먼저 받음. 대독·낱말 풀이·구두 답 받아쓰기·뒤 문항 노출을 별도 기록.')
    s['textDemand'].update(format='자체 창작시' if poem_lines else '자체 창작 단편 이야기',lengthReview='작품 본문과 가상 독자 의견을 구별해 분량을 기록. 실제 학년 난도·장문 수업 분량 승인은 별도 대기.')
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
        if q['kind']!='single_choice':
            q['acceptableResponses']='예시는 유일한 느낌·해석·문장이 아니다. 작품의 구체적 단서와 해석의 연결을 설명하고 반대 단서도 고려하면 다른 답을 수용한다. 인물의 마음·미래·작가의 실제 경험을 작품 밖의 확정 사실로 덧붙인 답과 구별한다.'
    assert tasks[0].get('analyticRubric'),s['id']
    s['presentationOrder']=[q['id'] for q in s['questions']]
    work=[p['id'] for p in s['paragraphs'] if not p['text'].startswith('가상 독자 의견:')]
    s['literaryReview']=dict(primaryQuestionId=s['questions'][0]['id'],responseMode='읽은 작품에 대한 서면 응답. 구두 답을 대신 적었으면 지원 종류를 기록.',interpretationPolicy='여러 해석을 무조건 동일하게 처리하지 않음. 구절·장면과 해석의 연결, 반대 단서, 확인할 수 없는 범위를 살피며 근거 있는 다른 답을 수용.',notAssessed=['실제 낭송·발표·동료와의 의견 교환을 서면 답만으로 인정하지 않음','독자의 성격·가정 경험·지속적 문학 흥미를 추정하지 않음','이번 작품의 사물 의미를 모든 작품에 통하는 상징 사전으로 가르치지 않음'],teacherApproval='pending',workParagraphIds=work)
    if poem_lines:
        heading=s['paragraphs'][0];lines=s['paragraphs'][1:1+poem_lines]
        assert heading['text'].startswith('시: ') and len(lines)==poem_lines
        s['poems']=[dict(id=s['id']+'-P1',title=heading['text'][3:],headingParagraphId=heading['id'],lineParagraphIds=[p['id'] for p in lines],lines=[p['text'] for p in lines],authorship='자체 창작시')]
        s['poetryHash']=hashlib.sha256(json.dumps(s['poems'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    s['source'].update(authorship='독립 집필한 자체 창작 작품과 명시된 가상 독자 의견. 기존 작품·실제 작가 원문을 개작하거나 인용하지 않음.',factualBasis='허구의 인물·사건·공간·독자 의견. 실제 인터뷰·역사·기관 운영·학생 응답으로 주장하지 않음.')
    s['teacherGuide']+=' 작품의 끝까지 먼저 읽고 주 응답을 받는다. 선택지·예시를 본 뒤의 해석은 첫 응답과 구별한다. 가상 독자 의견은 작품 속 사건이나 실제 학생 반응이 아니다. 다른 해석은 단서를 확인해 판단하며 빈 관찰표에 실제 답을 미리 채우지 않는다.'
    reasons={
      'PV2-G1-literature-02-S4-A':'학생 화면의 준거 이름을 중요한 일의 까닭·뒤에 한 일 살피기로 풀어 씀. 설명과 근거의 요구는 유지.',
      'PV2-G1-literature-02-S5-A':'독자 ‘나’의 이름을 일인칭과 구별하고 다리를 그었다를 자연스러운 그렸다는 표현으로 고침.',
      'PV2-G2-literature-09-S4-A':'학생 화면의 준거 이름을 사람처럼 나타낸 모습·시의 말과 내 생각으로 풀어 씀. 원래 해석 요구는 유지.',
      'PV2-G2-literature-09-S5-A':'가상 독자 ‘가’·‘나’를 시 속 일인칭 목소리와 구별해 표시.',
      'PV2-G3-literature-05-S5-A':'가상 독자 이름을 인물이나 일인칭 진술과 혼동하지 않게 표시.',
      'PV2-G4-literature-08-S2-A':'보조 선택형의 오답도 실제 작품의 장면으로 구성해 주의 변화의 근거와 단순 배경·다른 인물 행동을 구별하게 함.',
      'PV2-G4-literature-08-S5-A':'가상 독자 ‘가’·‘나’의 해석을 인물의 실제 말과 구별해 표시.',
      'PV2-G5-literature-07-S5-A':'가상 독자 ‘가’·‘나’의 이름을 일인칭과 구별해 표시.',
      'PV2-G6-literature-09-S2-A':'독자 이름을 명확히 하고 본문에 없는 키의 수치 대신 키 변화 기록이라는 범위로 의견을 고침.',
      'PV2-G6-literature-09-S4-A':'가상 독자 이름과 할아버지를 향한 호칭을 자연스럽게 고치고 선택형을 두 해석의 공존과 한쪽 근거의 구별로 보완.',
      'PV2-G6-literature-09-S5-A':'가상 독자 ‘가’·‘나’의 이름을 나라·세진의 말이나 일인칭과 구별해 표시.',
    }
    if s['id'] in reasons:
        second_pass=s['id'] in ['PV2-G1-literature-02-S5-A','PV2-G2-literature-09-S5-A']
        s['version']=3 if second_pass else 2
        for q in s['questions']:
            q['version']=s['version']
            for ref in q['evidence']:ref['version']=s['version']
        # Question-only changes also need history; the shared draftRevision
        # contract is restricted to changed stimulus bodies.
        reason=reasons[s['id']]
        if second_pass:
            reason+=' 추가 학생 문구 검토: '+('의견과 사건의 대응·뒤 단서 고려를 생각과 이야기 잇기·뒤의 일도 살피기로 풀어 씀.' if s['grade']==1 else '폐기를 운동화를 버림으로, 단정의 범위를 모르는 일 구별로 풀고 독자 의견 안내도 명확히 함.')
        s['literaryReview']['revision']=dict(fromVersion=2 if second_pass else 1,toVersion=s['version'],asOf='2026-11-18',reason=reason,previousSnapshotPath='data/content_authoring/expansion_v2_10/revision_history/'+('2026-11-18-before-learner-wording-review.json' if second_pass else '2026-11-18-before-editorial-review.json'),previousSnapshotHash='931aa3dacbea806c255ee426ada52ff73b3712bef3ebe77f82b0f97e2c9697c5' if second_pass else 'f9c26a81567662ff63118439986cb40c2f90547caa47eedc167e8c6d02f8e74b')
        s['teacherGuide']+=' 원고 v'+str(s['version'])+' 수정: '+reason

def curriculum(s,registry):
    g=s['grade'];code={1:'2국02-03',2:'2국05-02',3:'4국05-01',4:'4국05-04',5:'6국05-03',6:'6국05-04'}[g]
    direct=g in (1,3,4,5);r=registry[code]
    scope={1:'이야기 흐름을 바꾸는 중요한 사건을 짚어 중심 내용과 연결하는 부분',2:'사람처럼 표현한 사물의 말과 느낌을 해석하는 서면 감상 준비. 실제 말하기·서로 듣기는 관찰하지 않음',3:'인물 사이의 말·행동과 사건 흐름에서 관계 변화를 이해하는 부분',4:'장면의 소리·색·움직임 같은 감각 표현을 분위기와 연결해 감상하는 부분. 자기 감정을 감각적으로 생산하는 전체 수행은 별도',5:'이야기에서 반복되는 사물과 인물 행동·사건의 관계를 이해하는 부분. 상징의 공인 분류나 고정 의미를 측정하지 않음',6:'가상 의견을 작품 근거와 비교하는 개인 서면 준비. 실제 독자와 작품 의견을 주고받는 수행은 별도 관찰'}[g]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='읽기·문학 일부 성취요소 후보' if direct else '문학 감상·의견 나눔의 준비·보조',includedComponent=scope,notAssessed=s['literaryReview']['notAssessed']+['이 자료 하나로 성취기준 전체 달성·학년 난도를 승인하지 않음'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문·해설 대조. 최신 통합 고시 전량 비교와 독립 교사 승인은 별도 대기.',decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=scope,remainingGap='' if direct else '개인 서면 해석을 실제 말하기·다른 독자와 의견 나눔의 수행 완료로 인정하지 않음.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct and q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['literary_depth_v2_lower','literary_depth_v2_middle','literary_depth_v2_upper']:importlib.import_module(name).author(E,C,O,A,D)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True);p=DEST/'sets.json'
    p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-10',scope='새 문학6수행의 S2·S4·S5에18자료78문항. 독립 창작 이야기15편·시3편. 실제 학생 감상·교사 승인·여섯 단계 전체 공급과 구별.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored literary depth:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions');return p

if __name__=='__main__':build()
