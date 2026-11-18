"""Listen, speak, hear a live partner and respond; no simulated student scores."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_07'
OUT=ROOT/'output/expansion-v2-07'
CELLS={'plan-G1-oral-02':['S2','S3'],'plan-G2-oral-01':['S2','S5'],
       'plan-G3-oral-04':['S3','S5'],'plan-G4-oral-03':['S3','S5'],
       'plan-G5-oral-01':['S3','S5'],'plan-G6-oral-02':['S3','S5']}
SKILLS=list(CELLS)
def C(prompt,answer,why,bad,quotes):
    t=M(prompt,answer,bad,quotes);t['why']=why;return t
def D(criterion,full,partial,zero):return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})
def S(prompt,answer,quotes,criteria):
    assert len(criteria)==3
    t=O('spoken_response',prompt,answer,quotes,'목표 수행의 일부만 말하거나 상대의 답을 반영하지 못함','직접 말하지 않거나 들은 내용과 반대로 단정함');t['analyticRubric']=criteria;return t

def E(skill,stage,title,turns,instruction,partner,guide,tasks):
    emit(skill,stage,'A',title,'\n'.join(role+': '+text for role,text in turns),guide,tasks)
    s=SETS[-1];s['batch']='expansion-v2-07'
    s['listening']=dict(id=s['id']+'-A1',version=1,turns=[dict(role=role,text=text,paragraphId=p['id']) for p,(role,text) in zip(s['paragraphs'],turns)],script='\n\n'.join(role+'입니다. '+text for role,text in turns),studentInstruction=instruction,transcriptVisibility='teacher_only',timeAlignment='not_measured',authorship='synthetic_builtin_voice',listeningReview='pending')
    s['listeningHash']=hashlib.sha256(json.dumps(s['listening'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    question=s['grade'] in (1,6)
    s['partnerCard']=dict(title='첫 말 뒤에 사용하는 상대의 응답 카드',visibility='teacher_only_after_question' if question else 'teacher_only_after_explanation',kind='clarification_reply' if question else 'followup_prompt',reply=partner,instruction='학생이 먼저 직접 말한 뒤 제공한다. 질문 과제는 해당 정보를 실제로 물었을 때만 답한다. 다른 내용을 물으면 그 내용에 맞게 이미 제공된 정보만 확인하고, 없는 답은 임의로 만들어 주지 않는다. 설명 과제는 첫 설명 뒤 이 후속 말로 응답을 확인한다. 학생이 상대 답을 다시 듣고 이어 말할 기회를 준다.')
    s['partnerCardHash']=hashlib.sha256(json.dumps(s['partnerCard'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    if s['id']=='PV2-G6-oral-02-S5-A':
        s['partnerCard']['instruction']+=' 다른 변화에 관해 물으면 위 응답을 제공한다. 비교 기간·집계 방법만 물으면 이 자료에는 그 상세 기록이 없어 더 확인해야 한다고 답한다. 아직 묻지 않은 온라인 창구의 정보는 먼저 주지 않는다. 그런 적절한 질문과 미확인 답의 후속 확인도 완전 수행으로 수용한다.'
        s['partnerCardHash']=hashlib.sha256(json.dumps(s['partnerCard'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        for ref in q['evidence']:
            ref.update(evidenceKind='audio',assetId=s['listening']['id'],turnIndex=next(i for i,p in enumerate(s['paragraphs']) if p['id']==ref['paragraphId']))
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
        q['acceptableResponses']='같은 뜻의 다른 말·보완대체 의사소통을 수용하고 지원 형태를 기록한다. 정답 문장 암송·목소리 크기·말의 빠르기·시선만으로 점수를 정하지 않는다. 실제 들은 말·첫 발화·상대 응답·후속 발화를 구별한다.'
        if q['kind']=='spoken_response':
            q.update(responseMode='live_speech_with_partner',partnerReplyRef=dict(materialId=s['id'],version=1),performanceInstruction='안내 음성을 들은 뒤 선생님이나 짝에게 직접 말하세요. 상대가 답할 차례를 기다리고, 답을 들은 뒤 확인하거나 고쳐 말하세요. 아래 칸은 말한 뒤 남기는 메모이며 직접 말하기 관찰을 대신하지 않습니다.',observationFields=['처음 들은 횟수·반복 재생·대본 또는 보조 문항 노출','학생이 실제로 한 첫 발화 원문','대독·낱말·문장 틀·보완대체 의사소통 등 받은 지원','상대가 실제로 한 응답과 제공 시점','학생의 후속 확인·수정·유지 이유 또는 남은 질문'])
    assert s['questions'][0]['kind']=='spoken_response'
    s['presentationOrder']=[q['id'] for q in s['questions']]
    s['learnerStageLabel']={1:{'S2':'상대 말을 듣고 차례대로 묻기','S3':'두 말의 순서를 잇고 확인하기'},2:{'S2':'누가 무엇을 하는지 듣기','S5':'잘못 전한 말을 듣고 바로잡기'},3:{'S3':'서로의 이유를 잇고 제안하기','S5':'다른 조건을 듣고 조정하기'},4:{'S3':'핵심과 순서로 안내하기','S5':'근거의 범위를 지켜 발표하기'},5:{'S3':'관점과 이유를 나누어 정리하기','S5':'다른 근거의 뜻을 비교하기'},6:{'S3':'주장의 대상을 확인하며 묻기','S5':'단정의 근거를 확인하며 묻기'}}[s['grade']][stage]
    s['textDemand'].update(format='역할 이름을 밝힌 창작 듣기 대화',lengthReview='화면 본문은 교사용 대본. 음성 길이·화자 수·정보량과 재생 지원을 별도 기록. 읽기 지문 길이 규준으로 승인하지 않음.')
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='학생용 대본 제외. 재생·대독·문장 틀·뒤 문항 노출을 기록. 첫 발화와 상대 응답 뒤 수행을 분리.')
    s['oralPerformance']=dict(primaryQuestionId=s['questions'][0]['id'],firstResponse='선택형·해설 전에 직접 말하기 관찰. 현재 HTML은 뒤 문항의 노출을 봉인하지 않으므로 노출 시점을 기록.',followup='응답자 카드 이후 실제 후속 발화를 관찰. 읽거나 적은 답만으로 대화 수행을 완료 처리하지 않음.',teacherApproval='pending',notAssessed=['실제 학생 발화·점수·상대 반응을 미리 만들어 채우지 않음','합성 음성의 발음·쉼·속도와 학년 적합성은 청취 검토 대기','다른 의견을 듣고 반드시 동의하거나 의견을 바꾸어야 높은 점수라고 판단하지 않음'])
    if s['id'] in ('PV2-G3-oral-04-S5-A','PV2-G5-oral-01-S5-A'):
        s['version']=2;s['listening']['version']=2
        s['listeningHash']=hashlib.sha256(json.dumps(s['listening'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        for q in s['questions']:
            q['version']=2
            for ref in q['evidence']:ref['version']=2
            if q.get('partnerReplyRef'):q['partnerReplyRef']['version']=2
        s['oralPerformance']['revisionReason']='정답만 길게 보인 보조 선택형2개의 정답 표현을 핵심 뜻이 유지되게 간추림. 대본과 발화 과제·관찰 준거는 보존.'
        s['teacherGuide']+=' 원고v2: 보조 선택형 정답을 핵심 뜻에 맞게 간추려 정답 길이의 단서를 줄였다.'
    s['source'].update(authorship='자체 창작 가상 대화·모임·기록',factualBasis='모든 행사·수치·의견은 본문에 제공한 가상 학습 상황. 실제 기관 조사·어린이 발화·지역 운영 지침이 아님.')
    s['teacherGuide']+=' 첫 발화와 후속 발화를 구별하고 선택형만 맞혀 말하기를 완료 처리하지 않는다. 상대를 바라보는 방식·목소리 크기·성격이나 무조건적인 동의로 채점하지 않는다.'

def curriculum(s,registry):
    g=s['grade'];code={1:'2국01-03',2:'2국01-01',3:'4국01-06',4:'4국01-05',5:'6국01-02',6:'6국01-03'}[g];r=registry[code]
    scope={1:'상대 말 뒤 자신의 차례에 질문하고 상대 답을 들어 확인하는 대화 부분',2:'대상·행동과 순서를 고려하여 듣고 다시 말하는 부분',3:'의견과 이유를 비교하고 다른 조건에 맞춰 제안을 조정하는 토의 부분',4:'목적과 주제에 맞게 들은 정보를 정리해 말하는 발표 부분',5:'관점과 근거를 파악하고 적용 범위를 비교하며 듣는 부분',6:'주장과 관련한 대상을 구체적으로 질문하고 답을 듣고 확인하는 부분'}[g]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component',roleLabel='듣기·말하기 성취요소 일부 후보',includedComponent=scope,notAssessed=['아직 실제 학생의 직접 수행·교사 승인을 얻지 않음','원고 공급·선택형 정답만으로 전체 성취기준 달성을 판정하지 않음'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문 대조. 최신 통합 고시 전량 비교·독립 교사 승인 별도 대기.',decision='direct_component_candidate',scope=scope,remainingGap='',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['oral_v2_lower','oral_v2_middle','oral_v2_upper']:importlib.import_module(name).author(E,C,O,S,D)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True);p=DEST/'sets.json'
    p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-07',scope='듣기·말하기 새6수행의 두 단계씩12자료. 음성 초안·실제 발화 관찰 과제와 실제 학생 수행 완료를 구별.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    request=dict(reportName='oral-synthesis-result',purpose='국어 듣기·말하기 창작 대화의 합성 음성 초안. 발음·쉼·속도 청취와 실제 학생·교사 검토 대기.',sourcePath=p.relative_to(ROOT).as_posix(),sourceSnapshotHash=hashlib.sha256(p.read_bytes()).hexdigest(),requests=[dict(id=s['listening']['id'],materialId=s['id'],text=s['listening']['script'],usage='listening_material') for s in SETS])
    (DEST/'listening_requests.json').write_text(json.dumps(request,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored oral:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions');return p

if __name__=='__main__':build()
