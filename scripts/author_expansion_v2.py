"""First full-bank expansion: six new skills, six stages each, explicitly authored tasks."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_01'
OUT=ROOT/'output/expansion-v2-01'
SKILLS=['plan-G1-information-07','plan-G2-literature-03','plan-G3-literature-07',
        'plan-G4-language-09','plan-G5-information-11','plan-G6-literature-01']
MODULES=['expansion_v2_g1_sequence','expansion_v2_g2_events','expansion_v2_g3_senses',
         'expansion_v2_g4_reference','expansion_v2_g5_evidence','expansion_v2_g6_narrator']

def C(prompt,answer,why,bad,quotes):
    task=M(prompt,answer,bad,quotes);task['why']=why
    return task

def E(skill,stage,variant,title,text,guide,tasks):
    emit(skill,stage,variant,title,text,guide,tasks)
    s=SETS[-1]
    s['batch']='expansion-v2-01'
    positions=int(stage[1:])-1
    domain_labels={
      1:['차례말 익히기','행동의 차례 짚기','앞뒤 행동 잇기','빠진 차례 풀기','차례 설명 따지기','새 안내의 차례 엮기'],
      2:['사건의 차례 익히기','앞뒤 사건 짚기','인물의 사건 잇기','되짚은 시간 풀기','사건 설명 따지기','새 장면으로 이어 쓰기'],
      3:['감각 표현 익히기','시구의 감각 짚기','표현과 장면 엮기','비유의 의미 풀기','해석의 근거 따지기','새 장면을 감각으로 쓰기'],
      4:['지시 표현 익히기','가리키는 대상 짚기','문장 사이 대상 잇기','가리키는 내용 풀기','지시 표현의 명료성 따지기','새 대본을 명료하게 쓰기'],
      5:['근거의 역할 익히기','확인한 범위 짚기','여러 기록 엮기','빠진 근거 풀기','주장의 충분성 따지기','자료를 종합해 검토하기'],
      6:['서술 방법 익히기','서술된 정보 짚기','시점별 정보 엮기','서술의 틈 풀기','해석의 근거 따지기','관점을 바꾸어 엮기']
    }
    s['learnerStageLabel']=domain_labels[s['grade']][positions]
    s['taskDemand']['operation']=s['learnerStageLabel']
    s['taskDemand']['support']='본문에 방법 설명 포함' if stage=='S1' else '응답 전 정답 풀이 없음; 교사가 추가한 도움은 별도 기록'
    if s['grade']==3:s['taskDemand']['evidenceDistance']='시구 사이 및 작품과 감상·새 쓰기 상황 사이'
    if stage=='S6':
        primary=next(q for q in s['questions'] if q['kind']=='writing')
        s['presentationOrder']=[primary['id']]+[q['id'] for q in s['questions'] if q is not primary]
        s['teacherGuide']+=' 새 쓰기를 선택형·보조 문항보다 먼저 제시한다. 뒤 문항을 본 뒤의 수정은 첫 독립 응답과 구별해 기록한다.'
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
        if q['kind']=='writing':
            q['planningPrompt']={
                1:'문 장식과 책상 장식을 나누고 각 행동의 차례를 메모한 뒤 쓰세요.',
                2:'이미 일어난 사건과 아직 하고 싶은 일을 나누고, 조각을 받은 일에 이어질 장면을 계획하세요.',
                3:'현관의 빛깔이나 발에 닿는 느낌을 먼저 메모하고, 자기 표현으로 초고를 쓰세요.',
                4:'일지와 배 모형 각각의 행동·마지막 장소를 메모하고 안내 순서에 맞게 쓰세요.',
                5:'수량 기록과 응답 집단을 확인하고, 주장할 수 있는 범위·한계·다음 확인을 계획하세요.',
                6:'하준이 본 것·들은 것·모르는 것을 나누어 사건의 차례와 함께 계획하세요.'}[s['grade']]
            # Content and the relation to evidence are scored separately.
            dims={
              1:('두 장식의 행동과 차례 구별','두 과정의 행동을 빠뜨리거나 섞지 않고 차례를 보존한다.','한 행동이 빠지지만 두 과정은 구별한다.','두 과정의 행동을 서로 섞거나 앞뒤를 바꾼다.',
                 '두 장식 안내의 구별','문에 거는 장식과 책상에 세우는 장식을 구별해 적는다.','두 장식을 적지만 한쪽의 이름이나 구분이 모호하다.','어느 장식의 차례인지 알 수 없게 하나로 합친다.'),
              2:('이어지는 사건의 일관성','조각을 받은 일과 전시 뒤 만남을 보존하며 새 장면을 잇는다.','만남은 이어지지만 조각 사건과의 연결이 약하다.','앞선 사건과 모순되거나 새 장면이 없다.',
                 '상상한 장면의 표현','새 행동이나 대화를 구체적으로 쓰고 아직 하지 않은 일을 끝난 사실과 구별한다.','새 장면은 있지만 대화나 행동이 모호하다.','원문을 반복하거나 내일의 일을 이미 끝난 일로만 쓴다.'),
              3:('새 장면과 자기 표현','저녁빛과 젖은 신발이 있는 현관 장면을 원시 복사 없이 쓴다.','현관 장면은 있으나 상황 요소 하나가 빠진다.','원시를 복사하거나 다른 상황만 쓴다.',
                 '감각 표현의 구체성','빛깔·모양·촉감 등으로 무엇이 어떻게 느껴지는지 드러낸다.','감각은 드러나지만 대상이나 느낌이 모호하다.','감각 표현 없이 좋다·예쁘다만 나열한다.'),
              4:('행동과 처리 조건 보존','일지 펼치기·돛 설명·두 소품의 마지막 처리를 보존한다.','설명은 맞지만 마지막 처리 한 부분이 빠진다.','펼칠 수 없는 모형을 펼치거나 마지막 처리를 바꾼다.',
                 '지시 대상의 명료성','일지와 배 모형, 기록함과 전시대가 혼동 없이 드러난다.','한 지시 대상이나 장소를 문맥으로 다시 추적해야 한다.','누가 무엇을 어디에 두는지 두 가지 이상으로 읽힌다.'),
              5:('확인 사실과 주장 범위','수량 변화와 제한된 응답을 보존하고 기존 대비 이해 향상을 입증한 것으로 쓰지 않는다.','대체로 맞지만 응답 집단이나 수량의 범위가 한 곳 모호하다.','감소량·응답수·전체 이해 효과를 혼동한다.',
                 '한계와 다음 확인의 연결','빠진 비교나 이해 측정을 짚고 그 한계를 줄일 다음 확인과 인쇄 판단을 근거로 제안한다.','한계는 적었지만 다음 확인 또는 인쇄 판단의 근거가 약하다.','확인하지 못한 내용을 확정하거나 근거 없는 결론만 쓴다.'),
              6:('사건과 관점의 일관성','조명 부탁·약속 신호·공연 뒤 만남을 하준의 시점과 시간 흐름에 맞게 보존한다.','사건 한 부분이 빠지지만 시점과 흐름은 유지한다.','다은의 사건을 이름만 바꾸어 옮기거나 흐름을 뒤집는다.',
                 '서술할 수 있는 정보의 범위','관찰·들은 말·짐작을 구별하고 보이지 않은 얼굴이나 속마음을 직접 지식으로 쓰지 않는다.','대체로 구별하지만 한 문장에서 짐작이 사실처럼 보인다.','다은의 속마음과 표정을 하준이 직접 아는 사실로 쓴다.')
            }[s['grade']]
            q['rubric']=[dict(criterion=dims[i],levels={'0':dims[i+3],'1':dims[i+2],'2':dims[i+1]}) for i in (0,4)]

def add_poems(s):
    if s['microSkillId']!='plan-G3-literature-07':return
    layouts={'S1':[(0,4)],'S2':[(0,5)],'S3':[(0,4),(5,4)],'S4':[(0,5)],'S5':[(0,5)],'S6':[(0,4),(5,4)]}
    poems=[]
    for i,(start,count) in enumerate(layouts[s['stage']],1):
        heading=s['paragraphs'][start];lines=s['paragraphs'][start+1:start+1+count]
        poems.append(dict(id=s['id']+'-P'+str(i),title=heading['text'].split(':',1)[-1].strip(),
          headingParagraphId=heading['id'],lineParagraphIds=[p['id'] for p in lines],lines=[p['text'] for p in lines],authorship='자체 창작시'))
    s['poems']=poems;s['poetryHash']=hashlib.sha256(json.dumps(poems,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def add_scope(s,standards):
    grade=s['grade'];stage=s['stage'];qids=[q['id'] for q in s['questions']]
    code={1:'2국02-03',2:'2국05-02',3:'4국05-04',4:'4국04-04',5:'6국02-03',6:'6국05-03'}[grade]
    role='direct_component';selected=qids
    included={1:'짧은 안내에서 차례를 읽는 이해 보조 활동',2:'이야기의 사건을 읽고 느낀 점을 행동 근거와 연결해 표현하는 부분',
      3:'감각적 표현을 찾아 장면과 효과를 감상하고 새 상황에서 표현하는 부분',4:'글에 쓰인 지시 표현의 대상·내용을 이해하고 명료하게 고치는 부분',
      5:'주장 범위에 비추어 근거가 확인한 것과 미확인한 것을 구별하는 타당성 검토 부분',6:'인물·사건을 파악하며 서술자가 알 수 있는 정보 범위를 살피는 감상 보조 활동'}[grade]
    excluded={1:['글 전체의 중심 내용 파악을 직접 측정하지 않음','실제 소리 내어 읽기와 유창성 수행은 측정하지 않음'],
      2:['독서 흥미나 감상 태도의 장기적 변화는 측정하지 않음','이야기 순서 이해만으로 감상 표현 전체를 판정하지 않음'],
      3:['실제 낭송과 장기간의 감상 태도는 측정하지 않음','비유의 모든 종류를 분류하는 능력은 측정하지 않음'],
      4:['높임 표현과 접속 표현 전체는 측정하지 않음','실제 대화 상황의 지시 사용은 측정하지 않음'],
      5:['모든 갈래의 내용·표현 평가 능력을 대표하지 않음','실제 현장 조사 설계의 실행·인과 효과는 검증하지 않음'],
      6:['인물·사건·배경 파악의 전체 달성을 직접 판정하지 않음','서술 시점의 전문 분류를 공식 학년 성취기준으로 신설하지 않음']}[grade]
    if grade in (1,6):role='learning_support'
    if grade==2:
        selected=[qids[i] for i in {'S1':[2],'S2':[3],'S3':[],'S4':[],'S5':[4],'S6':[4,5]}[stage]]
        if stage=='S6':
            code='2국05-03';included='인물의 모습·행동·마음을 앞선 사건과 연결하여 이어지는 이야기로 상상해 표현하는 부분'
        if not selected:role='learning_support';selected=qids;included='이야기 흐름과 앞뒤 사건을 복원하는 감상 준비 활동'
    r=standards[code];payload=(ROOT/r['sourcePath']).read_bytes()
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],
      sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256(payload).hexdigest(),
      alignmentState='source_text_checked_candidate',role=role,roleLabel='성취요소 일부 후보' if role=='direct_component' else '학습 준비·보조',
      includedComponent=included,notAssessed=excluded,questionIds=selected)
    gap='' if role=='direct_component' else '공식 성취기준의 직접 수행 증거로 사용하지 않는다. 교수 목표 범위의 교사 검토가 필요하다.'
    audit=dict(version=1,checkedOn='2026-11-17',basis='로컬 교육부 2022-33 원문 대조. 최신 통합 고시 전량 비교와 교사 승인은 별도 대기.',
      decision='direct_component_candidate' if role=='direct_component' else 'related_only_goal_scope_review',scope=included,
      remainingGap=gap,links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if role=='direct_component' else [],curriculumAudit=audit,
      curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    for q in s['questions']:
        direct=role=='direct_component' and q['id'] in selected
        q['curriculumCoverage']=dict(state='component_candidate' if direct else 'preparation_or_related_activity',
          linkIds=[ref['id']] if q['id'] in selected else [],notFullStandardAchievement=True)
    if role!='direct_component':s['review']['goalMapping']='needs_formal_goal_scope_review'

def build():
    SETS.clear()
    for module in MODULES:importlib.import_module(module).author(E,C,O)
    standards={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:
        add_poems(s);add_scope(s,standards)
        if s['grade']==5:s['source']['factualBasis']='자체 창작 기관의 가상 기록. 실제 기관의 설문·운영 결과나 일반적 효과로 주장하지 않음.'
        if s['grade'] in (2,6):s['source']['authorship']='자체 창작 이야기·대화·상황'
        if s['grade']==3:s['source']['authorship']='자체 창작시와 감상 상황'
    archive_path='data/content_authoring/expansion_v2_01/revision_history/2026-11-17-before-order-review.json'
    archive=json.loads((ROOT/archive_path).read_text(encoding='utf-8'))
    reasons={
      'PV2-G1-information-07-S2-A':'마지막으로 뒤에 행동이 더 이어지던 설명을 고치고 차례말 문항과 근거를 마지막 행동에 맞춤.',
      'PV2-G1-information-07-S5-A':'그림 아래라는 위치만으로 그림 그리기의 시간 우선성을 채점하지 않도록 그림을 그린 다음이라는 순서 근거를 명시.',
      'PV2-G6-literature-01-S1-A':'자료명과 서술 표현이 섞이지 않도록 나는·지수는을 인용 부호로 구별.'}
    for s in SETS:
        if s['id'] not in reasons:continue
        old=next(u for u in archive['sets'] if u['id']==s['id'])
        s['version']=2
        for q in s['questions']:
            q['version']=2
            for e in q['evidence']:e['version']=2
        s['review']['draftRevision']=dict(asOf='2026-11-17',fromVersion=1,toVersion=2,reason=reasons[s['id']],
          previousSnapshotPath=archive_path,previousContentHash=old['contentHash'],previousDataSnapshotHash=archive['sourceSnapshotHash'])
    DEST.mkdir(parents=True,exist_ok=True)
    document=dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-17',batch='expansion-v2-01',
      scope='전체 은행 확장 1차: 새 6수행, 수행별 여섯 단계에 독립 자료 한 묶음씩. 대표 파일럿과 중복 합산하지 않음.',sets=SETS)
    path=DEST/'sets.json';path.write_text(json.dumps(document,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored expansion:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions')
    return path

if __name__=='__main__':build()
