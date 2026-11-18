"""Original visual media and typed references to visible elements."""
from pathlib import Path
import hashlib,importlib,json
from copy import deepcopy
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_06'
OUT=ROOT/'output/expansion-v2-06'
CELLS={'plan-G1-media-01':['S2','S3'],'plan-G2-media-03':['S3','S5'],
       'plan-G3-media-06':['S3','S5'],'plan-G4-media-04':['S3','S5'],
       'plan-G5-media-05':['S3','S5'],'plan-G6-media-03':['S4','S5']}
SKILLS=list(CELLS)

def P(panel,element):return dict(panel=panel,element=element)
def C(prompt,answer,why,bad,quotes):
    t=M(prompt,answer,bad,quotes);t['why']=why;return t
def D(criterion,full,partial,zero):return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})
def A(kind,prompt,answer,quotes,criteria):
    t=O(kind,prompt,answer,quotes,'대상·범위·근거의 일부만 표현함','자료와 반대되거나 근거 없는 단정만 함');t['analyticRubric']=criteria;return t
def panel(title,*elements,kind='card'):
    return dict(title=title,kind=kind,elements=[dict(id=e[0],text=e[1],style=e[2] if len(e)>2 else 'body',**(e[3] if len(e)>3 else {})) for e in elements])

def E(skill,stage,title,text,guide,tasks,panels):
    cleaned=deepcopy(tasks)
    for t in cleaned:
        t['quotes']=[q for q in t['quotes'] if isinstance(q,str)]
    emit(skill,stage,'A',title,text,guide,cleaned)
    s=SETS[-1];s['batch']='expansion-v2-06'
    s['mediaPanels']=deepcopy(panels)
    for i,p in enumerate(s['mediaPanels'],1):
        p['id']=s['id']+'-MP'+str(i)
        for e in p['elements']:
            if e.get('icon'):e['imageDescription']={'talk':'말풍선 그림','cup':'물잔 그림','ball':'공 그림','no_ball':'빗금을 친 공 그림'}[e['icon']]
        p['accessibleDescription']=p['title']+'。'+'。'.join((e['imageDescription']+' · ' if e.get('imageDescription') else '')+({'large':'큰 글씨: ','small':'작은 글씨: '}.get(e['style'],''))+e['text'] for e in p['elements'])
    s['mediaHash']=hashlib.sha256(json.dumps(s['mediaPanels'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if not any(isinstance(x,str) for x in t['quotes']):q['evidence']=[]
        for ref in t['quotes']:
            if isinstance(ref,dict):
                p=s['mediaPanels'][ref['panel']-1];e=next(e for e in p['elements'] if e['id']==ref['element'])
                q['evidence'].append(dict(evidenceKind='media',materialId=s['id'],version=1,assetId=p['id'],elementId=e['id'],quote=e['text']))
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
        if q['kind']!='single_choice':q['acceptableResponses']='예시의 문장과 달라도 보이는 자료의 범위와 조건을 보존하면 수용한다. 시각적 강조의 예상 효과와 실제 독자 반응을 구별하며 근거 없는 확정은 수용하지 않는다.'
    s['learnerStageLabel']={1:{'S2':'표지의 말과 그림 짚기','S3':'장소와 행동 연결하기'},2:{'S3':'두 표의 정보 연결하기','S5':'표와 설명 맞춰 보기'},3:{'S3':'바뀐 안내 이어 읽기','S5':'올린 날짜와 바꾼 날짜 가리기'},4:{'S3':'일부와 전체 함께 읽기','S5':'잘린 정보의 범위 따지기'},5:{'S3':'출처와 수정 이력 잇기','S5':'전달 경로와 원문 따지기'},6:{'S4':'강조가 만드는 인상 풀기','S5':'강조와 빠진 조건 살피기'}}[s['grade']][stage]
    s['textDemand'].update(format='자체 제작 시각 매체·동일 정보의 문자 대체',lengthReview='장문 지문 수와 구별. 본문 글자 수 외 이미지의 문자·표·배치 부담을 별도로 기록.')
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='이미지와 같은 정보의 문자 대체 제공. 사용한 형태·대독·뒤 문항 및 해설 노출 기록.')
    s['mediaReview']=dict(primaryQuestionId=s['questions'][0]['id'],firstResponse='주 설명·재표현을 보조 선택형보다 먼저 받음. 현재 HTML은 뒤 문항 노출을 봉인하지 않으므로 실제 노출을 기록.',responseMode='이미지 또는 동일 정보의 문자 대체를 읽고 남긴 서면 답',notAssessed=['실제 인터넷 검색·클릭·게시·공유를 수행했다고 판정하지 않음','특정 배치가 실제 모든 독자에게 같은 반응을 일으켰다고 판정하지 않음'],teacherApproval='pending')
    s['presentationOrder']=[q['id'] for q in s['questions']]
    if s['id']=='PV2-G6-media-03-S4-A':
        s['version']=2
        for q in s['questions']:
            q['version']=2
            for ref in q['evidence']:ref['version']=2
        s['mediaReview']['revisionReason']='포스터 비교의 제목에 강조 정보의 해석을 미리 붙이지 않도록 가·나만 남겨 중립화. 실제 글씨 크기와 조건을 읽어 설명하게 함.'
        s['teacherGuide']+=' 원고 v2: 무료 강조·비용 범위 제시라는 비교 제목을 가·나로 고쳐 제목에서 해석을 미리 알려 주지 않도록 했다.'
    s['source'].update(authorship='자체 창작 가상 표지·표·게시물·포스터',factualBasis='모든 기관·행사·게시물·수치는 학습용 가상 자료. 실제 운영 기관·뉴스·조사 결과의 재현이 아님.')
    s['teacherGuide']+=' 이미지와 문자 대체 중 어떤 형태로 답했는지 기록한다. 주 응답을 먼저 받고 보조 문항과 해설 노출을 구별한다.'

def curriculum(s,registry):
    g=s['grade'];code={1:'2국06-01',2:'2국02-03',3:'4국06-01',4:'4국06-01',5:'6국06-02',6:'6국06-02'}[g]
    direct=g>=5;r=registry[code]
    scope={1:'생활 표지의 말·그림을 읽는 매체 경험 보조',2:'표에 명시된 정보를 찾아 연결하고 설명과 대조하는 읽기 보조',3:'게시 날짜·수정 내용의 관계를 확인하는 매체 선택 준비',4:'부분 자료의 빠진 범위를 전체와 대조하는 매체 선택 준비',5:'출처·원문·수정 이력·독립 근거를 대조하는 신뢰성 평가 일부',6:'시각적 강조와 조건의 제시를 비교하며 정보 매체의 신뢰성을 판단하는 일부'}[g]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='매체 신뢰성 일부 후보' if direct else '매체 읽기의 준비·보조',includedComponent=scope,notAssessed=s['mediaReview']['notAssessed']+['성취기준 전체 달성·매체 흥미·태도는 별도 확인'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문 대조. 최신 통합 고시 전량 대조·독립 교사 승인 대기.',decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=scope,remainingGap='' if direct else '정지된 가상 자료의 읽기이며 실제 인터넷 탐색·자료 선택, 중심 내용 확인·흥미와 태도의 전체 수행을 직접 측정하지 않음.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct and q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['media_v2_lower','media_v2_middle','media_v2_upper']:importlib.import_module(name).author(E,C,O,A,D,P,panel)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True)
    p=DEST/'sets.json';p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-06',scope='매체 새6수행의 두 단계씩12자료. 실제 검색·공유·독자 반응 관찰과 전체 공급 완료는 별도.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored media:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions');return p

if __name__=='__main__':build()
