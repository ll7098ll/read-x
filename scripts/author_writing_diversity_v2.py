"""New writing functions with original, self-contained scenarios and actual production."""
from pathlib import Path
import hashlib, importlib, json
from author_pilot_v2 import E as emit, O, SETS
from author_writing_v2 import C, D, W

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'data/content_authoring/expansion_v2_09'
OUT = ROOT / 'output/expansion-v2-09'
SKILLS = [f'plan-G{g}-writing-{n}' for g, n in [(1,'09'),(2,'08'),(3,'08'),(4,'10'),(5,'07'),(6,'11')]]
CELLS = {sid: ['S2','S3','S5'] for sid in SKILLS}
LABELS = {
 1: {'S2':'알릴 내용을 정확히 쓰기','S3':'차례와 조건을 이어 안내하기','S5':'잘못된 안내 고쳐 쓰기'},
 2: {'S2':'생각에 까닭 붙이기','S3':'까닭과 선택 이어 쓰기','S5':'까닭이 맞는지 살펴 쓰기'},
 3: {'S2':'같은 기준으로 비교해 쓰기','S3':'과정과 결과 이어 설명하기','S5':'비교와 원인 설명 살펴 쓰기'},
 4: {'S2':'중심을 남겨 간추리기','S3':'여러 내용 묶어 다시 쓰기','S5':'요약에서 빠진 조건 고치기'},
 5: {'S2':'뜻과 구별되는 특징 설명하기','S3':'작동 과정과 조건 이어 쓰기','S5':'설명의 범위와 예외 고치기'},
 6: {'S2':'기록과 다른 내용 고치기','S3':'문단의 역할과 흐름 고치기','S5':'근거에 맞게 결론 고치기'},
}

def E(skill, stage, title, text, guide, tasks):
    emit(skill, stage, 'A', title, text, guide, tasks)
    s = SETS[-1]
    s['batch'] = 'expansion-v2-09'
    s['learnerStageLabel'] = LABELS[s['grade']][stage]
    s['textDemand'].update(format='자체 창작 쓰기 상황·가상 기록·원문·초고', lengthReview='쓰기 자극 자료. 실제 장문 읽기 공급 또는 검증된 학년 난도로 환산하지 않음.')
    s['taskDemand'].update(operation=s['learnerStageLabel'], support='계획 메모는 제공하되 완성 문장·예시 답은 첫 쓰기 뒤 교사용. 대독·받아쓰기·뒤 문항 노출은 별도 기록.')
    primary = []
    for q, t in zip(s['questions'], tasks):
        q['version'] = 1
        if q['kind'] == 'single_choice':
            q['explanation'] = t['why']
            q['options'][q['correctIndex']]['reason'] = t['why']
            q['options'].sort(key=lambda o: hashlib.sha256((q['id']+'\0'+o['text']).encode()).hexdigest())
            q['correctIndex'] = next(i for i,o in enumerate(q['options']) if o['text'] == t['answer'])
        if q['kind'] == 'writing':
            primary.append(q['id'])
            q.update(planningPrompt=t['planningPrompt'], rubric=t['analyticRubric'], writerContext=t['writerContext'])
            q['acceptableResponses'] = '교사용 예시는 유일한 답이 아니다. 필수 의미·자료 범위·독자·목적을 충족하는 다른 표현과 구성을 수용한다. 예시와 같은 선택·어휘를 요구하지 않는다. 맞춤법은 별도 관찰하고 내용 점수를 일괄 0점으로 만들지 않는다.'
    assert len(primary) == 1, s['id']
    s['presentationOrder'] = primary + [q['id'] for q in s['questions'] if q['id'] not in primary]
    s['writingProtocol'] = dict(primaryQuestionId=primary[0], firstResponse='예시·선택지·보조 문항을 보기 전 초고를 별도 보관',
      observationFields=['독자·목적과 계획 메모','학생의 첫 초고 원문','실제로 적용한 준거','학생의 수정고 원문','고친 부분과 이유','대독·낱말 풀이·공동 구성·뒤 문항과 예시 노출','학생 직접 쓰기 / 타인 받아쓰기 구별','가상 기록 / 학생이 실제 겪은 일 구별'],
      supportPolicy='구두 답을 성인이 적었거나 함께 문장을 만들었다면 그 도움을 기록한다. 선택형 정답 또는 구두 설명만으로 독립 쓰기를 인정하지 않는다.',
      storageLimit='HTML 입력 칸은 초고·수정고 구별을 지원하지만 첫 응답 불변 저장·제출 잠금·교사 승인을 보장하지 않음.')
    s['teacherGuide'] += ' 주 쓰기를 먼저 받는다. 보조 문항을 본 뒤 수정한 답은 첫 초고와 구별한다. 관찰 양식은 실제 학생 답안이 없는 상태로 비워 둔다. 길이 안내는 권장 분량이며 내용이 충분한 다른 문장 수를 자동 감점하지 않는다.'
    reasons = {
      'PV2-G4-writing-10-S3-A':'보조 과제의 실제 요구가 짝짓기보다 범주 분류이므로 문항 종류를 분류로 바로잡음.',
      'PV2-G5-writing-07-S2-A':'표에 적힌 대여자와 물건의 실제 현재 상태를 구별하도록 예시 답의 확인 범위를 좁힘.',
      'PV2-G6-writing-11-S3-A':'예시 답에서 기록에 없는 나누어 살폈다는 수행 완료 진술을 덜고 실제 제시된 수집 정보만 남김.',
      'PV2-G6-writing-11-S5-A':'문의 미접수의 범위를 같은 시간 이용 문의로 명료화하여 모든 문의·불편의 부재로 확대하지 않음.',
    }
    if s['id'] in reasons:
        s['version'] = 2
        for q in s['questions']:
            q['version'] = 2
            for ref in q['evidence']: ref['version'] = 2
        # The shared draftRevision contract requires a changed body. These edits
        # change answer scope or question kind while preserving the stimulus.
        s['writingReview'] = dict(fromVersion=1,toVersion=2,asOf='2026-11-18',revisionReason=reasons[s['id']],previousSnapshotPath='data/content_authoring/expansion_v2_09/revision_history/2026-11-18-before-editorial-review.json',previousSnapshotHash='6175c81291535cd328c6b0824492f48fb5151e859794a0fc30d99f06d19703ec')
        s['teacherGuide'] += ' 원고 v2 수정: '+reasons[s['id']]

def curriculum(s, registry):
    g = s['grade']; code = {1:'2국03-02',2:'2국03-02',3:'4국03-02',4:'4국03-01',5:'6국03-01',6:'6국03-05'}[g]
    direct = g in (2,3,5,6)
    scope = {
      1:'주어진 알림·순서·조건을 문장으로 옮기는 쓰기 준비·보조. 학생 자신의 생각·느낌 표현 전체를 직접 측정하지 않음',
      2:'주어진 상황에서 학생이 선택한 생각과 까닭을 문장으로 표현하는 부분. 쓰기 흥미·태도는 별도 관찰',
      3:'가상 작업·비교 기록의 절차와 결과를 정확히 보고하는 글의 일부. 직접 관찰·실험 수행은 측정하지 않음',
      4:'핵심 내용·관계·조건을 남겨 요약·재표현하는 쓰기 보조. 중심·뒷받침 문단 쓰기 전체를 직접 측정하지 않음',
      5:'주어진 도구·규칙의 정의·특성·작동 조건을 선정해 설명하는 글의 일부',
      6:'초고를 기록·주제·문단 역할에 비추어 내용·논리·조직을 고쳐 쓰는 부분. 자신의 쓰기 전 과정 조정 전체는 측정하지 않음',
    }[g]
    r = registry[code]; primary = s['writingProtocol']['primaryQuestionId']
    ref = dict(id=s['id']+'-C1', code=code, subject=r['subject'], statement=r['statement'], gradeBand=r['gradeBand'], sourcePath=r['sourcePath'], sourceLine=r['sourceLine'], noticeVersion=r['noticeVersion'], sourceHash=hashlib.sha256((ROOT/r['sourcePath']).read_bytes()).hexdigest(), alignmentState='source_text_checked_candidate', role='direct_component' if direct else 'learning_support', roleLabel='쓰기 일부 성취요소 후보' if direct else '쓰기 준비·보조', includedComponent=scope, notAssessed=['이 자료 하나로 성취기준 전체 달성·학년 난도를 승인하지 않음','실제 독자와 공유·지속적인 쓰기 태도·학생의 실제 경험은 이 가상 자료만으로 확인하지 않음','보조 선택형 정답을 주 쓰기 수행으로 환산하지 않음'], questionIds=[primary])
    audit = dict(version=1, checkedOn='2026-11-18', basis='로컬 국어 2022-33 원문·해설 대조. 최신 통합 고시 전량 비교·독립 교사 승인 대기.', decision='direct_component_candidate' if direct else 'related_only_goal_scope_review', scope=scope, remainingGap='' if direct else '안내·요약의 실제 기능과 연결한 성취기준의 직접 수행 범위가 다름. 정식 목표 범위와 학년 배치 검토가 남음.', links=[ref], teacherApproval='pending')
    s['source'].update(officialStandards=[ref] if direct else [], curriculumAudit=audit, curriculumAuditHash=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest())
    if not direct: s['review']['goalMapping'] = 'needs_formal_goal_scope_review'
    for q in s['questions']:
        q['curriculumCoverage'] = dict(state='component_candidate' if direct and q['id']==primary else 'preparation_or_related_activity', linkIds=[ref['id']] if q['id']==primary else [], notFullStandardAchievement=True)

def build():
    SETS.clear()
    for name in ['writing_diversity_v2_lower','writing_diversity_v2_middle','writing_diversity_v2_upper']:
        importlib.import_module(name).author(E,C,O,W,D)
    registry = {r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    for s in SETS:
        curriculum(s, registry)
        s['source'].update(authorship='독립 집필한 가상 상황·관찰 기록·초고·규칙·설명. 교사용 예시 답은 학생 실제 답안이 아님.', factualBasis='문제 안에 필요한 정보와 규칙을 제공. 실제 기관·과학 관찰·조사·학생 발언의 기록으로 주장하지 않음.')
    DEST.mkdir(parents=True, exist_ok=True)
    p=DEST/'sets.json'
    p.write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-18',batch='expansion-v2-09',scope='새 쓰기6수행의 S2·S3·S5에18자료·78문항/과제. 실제 쓰기18·보조60. 교사 승인·실제 학생 수행·전체 단계 공급과 구별.',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored writing diversity:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'tasks')
    return p

if __name__ == '__main__': build()
