"""Source-backed expansion: two original explanations for one selected cell per grade."""
from pathlib import Path
import hashlib,importlib,json
from author_pilot_v2 import E as emit,M,O,SETS
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'data/content_authoring/expansion_v2_02'
OUT=ROOT/'output/expansion-v2-02'
LEDGER=ROOT/'research/nonfiction_v2_sources_2026-11-17.json'
STAGES={'plan-G1-information-03':'S3','plan-G2-information-09':'S3','plan-G3-information-07':'S3',
        'plan-G4-information-10':'S3','plan-G5-information-03':'S4','plan-G6-information-09':'S5'}
SKILLS=list(STAGES)
SOURCES={}

def C(prompt,answer,why,bad,quotes):
    task=M(prompt,answer,bad,quotes);task['why']=why
    return task

def F(skill,stage,variant,title,text,guide,tasks,facts):
    emit(skill,stage,variant,title,text,guide,tasks)
    s=SETS[-1];s['batch']='expansion-v2-02'
    s['learnerStageLabel']={1:'몸의 특징 연결하기',2:'까닭과 변화 잇기',3:'뜻과 사례 연결하기',4:'기준에 맞게 묶기',5:'정의를 새 상황에 적용하기',6:'원인 설명의 범위 따지기'}[s['grade']]
    s['taskDemand'].update(operation=s['learnerStageLabel'],support='정답 풀이 사전 제공 없음; 받은 도움과 배경지식의 영향을 별도 기록')
    s['textDemand'].update(format='여러 문단으로 연결한 사실 기반 설명글',lengthReview='실제 분량은 charCount로 기록. 장문 코스의 학년별 분량·가독성 승인은 교사 검토 대기.')
    refs=[];used=[]
    for source_id,fact_id,quote in facts:
        source=SOURCES[source_id];statement=source['facts'][fact_id]
        found=[(p,t) for p in s['paragraphs'] for t in p['sentences'] if quote in t['text']]
        assert len(found)==1,(s['id'],quote,len(found))
        p,t=found[0]
        refs.append(dict(sourceId=source_id,factId=fact_id,checkedStatement=statement,paragraphId=p['id'],sentenceId=t['id'],quote=quote,
          type='editorial_application' if fact_id in ('scope','inference') else 'source_fact_paraphrase'))
        if source_id not in used:used.append(source_id)
    s['source'].update(authorship='공개 1차 자료의 사실을 확인해 자체 재구성한 한국어 설명글 및 명시된 학습용 상황',
      factualBasis='실제 기관의 기초 설명·기록과 자체 제작 연습 상황을 구별. 원문·사진·도안을 복제하지 않음.',
      factualReferences=[{k:SOURCES[sid][k] for k in ('id','publisher','title','url','locator')} for sid in used],
      factChecks=refs,factLedgerPath=str(LEDGER.relative_to(ROOT)).replace('\\','/'),factLedgerHash=hashlib.sha256(LEDGER.read_bytes()).hexdigest(),
      sourceExposureFamilyIds=used)
    for q,t in zip(s['questions'],tasks):
        q['version']=1
        if q['kind']=='single_choice':q['explanation']=t['why'];q['options'][q['correctIndex']]['reason']=t['why']

def curriculum(s,registry):
    grade=s['grade'];code='2국02-03' if grade<3 else '4국02-02' if grade<5 else '6국02-02' if grade==5 else '6국02-03'
    direct=grade==6
    statement=registry[code];raw=(ROOT/statement['sourcePath']).read_bytes()
    included={1:'대상과 특징을 연결하는 읽기 이해 보조',2:'까닭과 결과를 연결하는 읽기 이해 보조',3:'정의와 예를 연결하는 내용 이해 보조',4:'기준에 따라 정보를 묶는 읽기 이해 보조',5:'개념의 정의를 새 사례와 연결하는 추론 학습 보조',6:'원인·결과 설명의 일반화 범위와 근거 타당성을 평가하는 일부 수행'}[grade]
    ref=dict(id=s['id']+'-C1',code=code,subject=statement['subject'],statement=statement['statement'],gradeBand=statement['gradeBand'],
      sourcePath=statement['sourcePath'],sourceLine=statement['sourceLine'],noticeVersion=statement['noticeVersion'],sourceHash=hashlib.sha256(raw).hexdigest(),
      alignmentState='source_text_checked_candidate',role='direct_component' if direct else 'learning_support',roleLabel='국어 성취요소 일부 후보' if direct else '읽기 이해의 준비·보조',
      includedComponent=included,notAssessed=['과학·문화 지식 자체의 공식 교과 성취를 판정하지 않음','이 자료만으로 국어 성취기준 전체 달성이나 학년 난도를 승인하지 않음'],questionIds=[q['id'] for q in s['questions']])
    audit=dict(version=1,checkedOn='2026-11-17',basis='국어 기준은 로컬 2022-33 원문 대조. 사실 출처 검토와 교육과정 정합성·교사 승인은 별개이며 최신 통합 고시 전량 대조 대기.',
      decision='direct_component_candidate' if direct else 'related_only_goal_scope_review',scope=included,
      remainingGap='' if direct else '핵심·중심 내용 또는 생략 의미의 전체 수행을 직접 측정하는 자료로 주장하지 않는다. 교수 목표 범위를 검토해야 한다.',links=[ref],teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [],curriculumAudit=audit,
      curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct:s['review']['goalMapping']='needs_formal_goal_scope_review'
    for q in s['questions']:q['curriculumCoverage']=dict(state='component_candidate' if direct else 'preparation_or_related_activity',linkIds=[ref['id']],notFullStandardAchievement=True)

def build():
    SETS.clear();SOURCES.clear()
    SOURCES.update({s['id']:s for s in json.loads(LEDGER.read_text(encoding='utf-8'))['sources']})
    for module in ['nonfiction_v2_lower','nonfiction_v2_upper']:importlib.import_module(module).author(F,C,O)
    registry={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:curriculum(s,registry)
    DEST.mkdir(parents=True,exist_ok=True)
    path=DEST/'sets.json';path.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-17',batch='expansion-v2-02',
      scope='사실 기반 설명글 확장. 학년별 새 수행의 선택한 한 단계에 자료 A·B를 집필. 여섯 단계 전체 공급 완료가 아님.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored nonfiction:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions')
    return path

if __name__=='__main__':build()
