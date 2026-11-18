"""Fact-backed diverse explanations; distinguish source facts from fictional applications."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_08'
OUT=ROOT/'output/expansion-v2-08'
LEDGER=ROOT/'research/explanation_v2_sources_2026-11-18.json'
SKILLS=[f'plan-G{g}-information-{n}' for g,n in [(1,'06'),(2,'08'),(3,'06'),(4,'11'),(5,'08'),(6,'11')]]
CELLS={sid:['S2','S3','S5'] for sid in SKILLS};SOURCES={}
def C(prompt,answer,why,bad,quotes):
    t=M(prompt,answer,bad,quotes);t['why']=why;return t
def D(criterion,full,partial,zero):return dict(criterion=criterion,levels={'0':zero,'1':partial,'2':full})
def A(kind,prompt,answer,quotes,criteria):
    t=O(kind,prompt,answer,quotes,'내용·범위·근거 관계의 일부만 설명함','본문과 모순되거나 없는 정보를 확정함');t['analyticRubric']=criteria;return t
def F(skill,stage,title,text,guide,tasks,facts):
    emit(skill,stage,'A',title,text,guide,tasks);s=SETS[-1];s['batch']='expansion-v2-08'
    s['learnerStageLabel']={1:{'S2':'중심 내용과 자세한 말 짚기','S3':'자세한 말을 한 내용으로 잇기','S5':'중심에 맞는 설명 고르기'},2:{'S2':'같은 기준으로 특징 짚기','S3':'공통점과 차이 연결하기','S5':'비교의 기준과 예외 살피기'},3:{'S2':'문단의 할 일 짚기','S3':'문단을 역할대로 잇기','S5':'문단을 빼도 뜻이 남는지 따지기'},4:{'S2':'현상에 필요한 조건 짚기','S3':'여러 조건을 함께 적용하기','S5':'조건의 차이와 예외 살피기'},5:{'S2':'비교할 기준 나누기','S3':'자료의 서로 다른 특성 잇기','S5':'목적과 기준에 맞게 판단하기'},6:{'S2':'확인한 증거와 빈칸 짚기','S3':'서로 다른 단서 함께 따지기','S5':'근거가 결론을 뒷받침하는지 따지기'}}[s['grade']][stage]
    refs=[];used=[]
    for sid,fid,quote in facts:
        found=[(p,t) for p in s['paragraphs'] for t in p['sentences'] if quote in t['text']];assert len(found)==1,(s['id'],quote,len(found))
        p,t=found[0];refs.append(dict(sourceId=sid,factId=fid,checkedStatement=SOURCES[sid]['facts'][fid],paragraphId=p['id'],sentenceId=t['id'],quote=quote,type='editorial_application' if fid in ('scope','inference') else 'source_fact_paraphrase'))
        if sid not in used:used.append(sid)
    s['source'].update(authorship='1차 기관·연구 자료의 사실을 확인해 자체 구성한 한국어 설명글과 명시된 가상 연습 사례',factualBasis='실제 사실·일반 원리와 가상 관찰·수치·사례를 구별. 원문·사진·도표 복제 없음.',factualReferences=[{k:SOURCES[sid][k] for k in ('id','publisher','title','url','locator')} for sid in used],factChecks=refs,factLedgerPath=LEDGER.relative_to(ROOT).as_posix(),factLedgerHash=hashlib.sha256(LEDGER.read_bytes()).hexdigest(),sourceExposureFamilyIds=list(dict.fromkeys(f for sid in used for f in SOURCES[sid].get('exposureFamilyIds',[sid]))))
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':
            q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']
            q['options'].sort(key=lambda o:hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest());q['correctIndex']=next(i for i,o in enumerate(q['options']) if o['text']==t['answer'])
        if t.get('analyticRubric'):q['rubric']=t['analyticRubric']
    assert tasks[0].get('analyticRubric');s['presentationOrder']=[q['id'] for q in s['questions']]
    s['textDemand'].update(format='사실 기반 설명글 및 표시한 가상 연습',lengthReview='실제 charCount·문단 수를 기록. 사실 검토와 학년 분량·난도 규준 승인은 별개.')
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='주 설명을 보조 선택형보다 먼저 받음. 대독·낱말 풀이·뒤 문항 노출을 별도 기록.')
    s['explanationReview']=dict(primaryQuestionId=s['questions'][0]['id'],scopePolicy='실제 사실·원리와 가상 자료를 구별. 조건·예외·미확인을 지우지 않은 다른 표현도 수용.',teacherApproval='pending')
    reasons={'PV2-G1-information-06-S2-A':'직접 확인한 행동 발췌의 범위에 맞추어 지문에서 별도 지리 정보를 덜어냄.',
      'PV2-G4-information-11-S3-A':'기록 나가 일인칭 나는으로 읽히지 않도록 자료 이름을 명시.',
      'PV2-G5-information-08-S5-A':'정각의 국소 성질을 지도에 나타낸 지점의 범위로 명료화.',
      'PV2-G6-information-11-S2-A':'고리 이상과 패턴 비교 방법의 원천을 각각의 1차 페이지로 분리 연결.',
      'PV2-G6-information-11-S5-A':'모형을 보고한 논문 초록과 같은 연구의 맥락 설명을 원천별로 연결하며 독립된 두 발견으로 세지 않음.'}
    if s['grade']==3:reasons[s['id']]='문단 역할·전개 과제를 중심 생각 간추리기 성취기준의 직접 측정으로 단정하지 않고 준비·보조 관계로 수정.'
    if s['id'] in reasons:
        s['version']=2
        for q in s['questions']:
            q['version']=2
            for ref in q['evidence']:ref['version']=2
        s['explanationReview']['revisionReason']=reasons[s['id']];s['teacherGuide']+=' 원고v2: '+reasons[s['id']]

def curriculum(s,registry):
    g=s['grade'];code={1:'2국02-03',2:'2국02-03',3:'4국02-02',4:'4국02-02',5:'6국02-04',6:'6국02-03'}[g];direct=g in (1,6);r=registry[code]
    scope={1:'중심 내용과 이를 풀어 주는 자세한 내용을 연결하는 부분',2:'같은 기준으로 공통점·차이·예외를 비교하는 읽기 보조',3:'문단의 역할과 전개 관계를 연결하는 읽기 준비·보조',4:'설명글의 조건·예외를 보존해 이해하는 읽기 보조',5:'비교 기준과 목적을 연결하는 문제 해결 읽기 준비',6:'근거의 적용 범위와 결론의 타당성을 검토하는 부분'}[g]
    ref=dict(id=s['id']+'-C1',code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='국어 일부 성취요소 후보' if direct else '읽기 이해의 준비·보조',includedComponent=scope,notAssessed=['과학·사회·기록 지식의 공식 교과 성취는 판정하지 않음','자료 하나로 성취기준 전체·학년 난도를 승인하지 않음'],questionIds=[s['questions'][0]['id']])
    audit=dict(version=1,checkedOn='2026-11-18',basis='로컬 국어2022-33 원문 대조. 최신 통합 고시 전량 비교·독립 교사 승인 대기.',decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=scope,remainingGap='' if direct else '이 기능 집중 자료만으로 중심 내용·복수 관점의 실제 문제 해결 등 연결한 성취기준의 전체 수행을 직접 측정하지 않음.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct and q['id']==s['questions'][0]['id'] else 'preparation_or_related_activity',linkIds=[ref['id']] if q['id']==s['questions'][0]['id'] else [],notFullStandardAchievement=True)
def build():
    SETS.clear();SOURCES.clear();SOURCES.update({s['id']:s for s in json.loads(LEDGER.read_text(encoding='utf-8'))['sources']})
    for name in ['explanation_v2_lower','explanation_v2_middle','explanation_v2_upper']:importlib.import_module(name).author(F,C,O,A,D)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True);p=DEST/'sets.json';p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-08',scope='새6읽기 수행의 S2·S3·S5에18설명 자료. 전체 단계 공급·독립 교사 사실 검토 완료와 구별.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored explanations:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions');return p
if __name__=='__main__':build()
