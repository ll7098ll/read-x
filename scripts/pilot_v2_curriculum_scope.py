"""Source-checked curriculum scope decisions, never blanket achievement or teacher approval."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
TARGETS={'plan-G1-literature-05','plan-G2-language-07','plan-G3-information-08','plan-G4-information-05','plan-G2-writing-11','plan-G4-media-02'}
ROLE_LABELS=dict(direct_component='국어 성취요소 일부',learning_support='국어 학습 보조',related_application='다른 국어 활동 연계',cross_subject_component='다른 교과 성취요소 일부',later_grade_articulation='상위 학년 연계 참고',optional_followup='후속 활동 연계',not_direct_evidence='직접 측정 근거로 사용하지 않음')
ARCHIVE='data/content_authoring/pilot_v2/revision_history/2026-11-17-before-scope-review.json'
REVISIONS={'PV2-G2-language-07-S1-A':'같은 글자로 쓴 말의 뜻 구별을 한 낱말의 여러 뜻이라는 정의와 구별',
 'PV2-G3-information-08-S5-A':'본문이 비교 기준 오류와 정답 수치를 먼저 해설하던 부분을 경쟁 주장으로 수정',
 'PV2-G3-information-08-S5-B':'독자 목적과 분량의 관계를 미리 판정하던 해설을 판단 전 상황으로 수정'}

def enrich(sets):
    standards={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    archive=json.loads((ROOT/ARCHIVE).read_text(encoding='utf-8'));previous={s['id']:s for s in archive['sets']}
    for s in sets:
        if s['id'] in REVISIONS:
            old=previous[s['id']]
            assert old['version']==1 and old['contentHash']!=s['contentHash'],s['id']+' revision history mismatch'
            assert old['contentHash']==hashlib.sha256('\n'.join(p['text'] for p in old['paragraphs']).encode()).hexdigest()
            s['version']=2
            for q in s['questions']:
                q['version']=2
                for e in q['evidence']:e['version']=2
            s['review']['draftRevision']=dict(asOf='2026-11-17',fromVersion=1,toVersion=2,reason=REVISIONS[s['id']],previousSnapshotPath=ARCHIVE,previousContentHash=old['contentHash'],previousDataSnapshotHash=archive['sourceSnapshotHash'])
        if s['microSkillId'] not in TARGETS:continue
        links=[];primary=[];allq=[q['id'] for q in s['questions']];writing=[q['id'] for q in s['questions'] if q['kind']=='writing']
        def link(code,role,included,not_assessed,qids=None):
            r=standards[code];file=ROOT/r['sourcePath'];line=file.read_text(encoding='utf-8').splitlines()[r['sourceLine']-1]
            assert code in line and r['statement'] in line,(code,'source changed')
            ref=dict(id=s['id']+'-C'+str(len(links)+1),code=code,subject=r['subject'],statement=r['statement'],gradeBand=r['gradeBand'],sourcePath=r['sourcePath'],sourceLine=r['sourceLine'],noticeVersion=r['noticeVersion'],sourceHash=hashlib.sha256(file.read_bytes()).hexdigest(),alignmentState='source_text_checked_candidate',role=role,roleLabel=ROLE_LABELS[role],includedComponent=included,notAssessed=not_assessed,questionIds=allq if qids is None else qids)
            links.append(ref)
            if role=='direct_component':
                assert s['grade'] in ref['gradeBand'] and ref['subject']=='국어'
                primary.append(ref)
            return ref
        sid=s['microSkillId'];gap='';scope='';extra={}
        if sid=='plan-G1-literature-05':
            link('2국02-04','direct_component','마음말·행동·상황 단서를 통해 인물의 마음을 표현하고 짐작하는 부분',['인물의 마음이나 생각과 자신의 경험·생각 비교 전체','다양한 실제 주변 인물에게의 일반화'])
            scope='인물의 마음 읽기 요소의 단계별 준비·적용. 자기 경험과 비교하는 수행까지 측정했다고 보지 않음.'
        elif sid=='plan-G2-language-07':
            link('2국02-03','learning_support','문맥에서 쓰인 말의 뜻을 구별해 글 이해를 돕는 어휘 보조 활동',['중심 내용 확인 전체 수행','동음이의어·다의어의 공식 문법 분류'])
            link('4국04-01','not_direct_evidence','검토했으나 단어 간 의미 관계라는 문구만으로 본 자료의 모든 뜻 구별을 직접 측정한다고 판정하지 않음',['초2 직접 성취기준 배치','동음이의어와 다의어를 같은 개념으로 평가'],[])
            gap='1~2학년군의 이번 원문 대조에서 이 세부 어휘 활동을 직접 측정하는 문법 코드를 확정하지 않음. 내부 읽기 보조 목표로 검토.'
            scope='같은 글자로 쓴 말의 문맥 뜻을 구별하는 활동. 모든 예를 한 낱말의 다의어로 분류하지 않음.'
            extra=dict(lexicalScopeNote='동음이의어와 다의어를 구분하는 사전 처리와 초2 문맥 뜻 학습을 구별한다. 학생에게 두 전문 용어의 분류를 요구하지 않는다.',externalClarification=dict(authority='국립국어원 온라인가나다',checkedOn='2026-11-17',url='https://www.korean.go.kr/front/onlineQna/onlineQnaView.do?mn_id=216&pageIndex=1&qna_seq=307385',use='사전의 서로 다른 표제어와 한 표제어 안의 여러 뜻풀이를 혼동하지 않는 교사용 범위 설명'))
        elif sid=='plan-G3-information-08':
            if s['stage']=='S5':
                link('4국02-04','direct_component','비교 수치의 사실과 홍보 판단을 나누고 홍보 의견과 자신의 판단 근거를 비교하는 부분',['이 성취기준의 모든 글 유형과 관점 비교','유창하게 소리 내어 읽기'])
            else:
                link('4국02-04','learning_support','같은 기준의 사실 정보를 정리하고 목적에 따른 판단을 비교하기 위한 준비 전략',['사실·의견 구분 및 필자와 자신의 의견 비교 전체를 독립 측정했다고 보는 주장'])
                gap='사물 특징 비교와 선택 기준 적용을 사실·의견 및 필자 관점 비교 전체 성취와 동일시하지 않음. 읽기 전략의 내부 목표 범위를 검토.'
            link('4국03-03','related_application','선택 이유를 쓰는 과제를 의견과 이유 표현으로 연계할 수 있음',['주변 대상에 대한 독립 의견 글쓰기 전체 과정'],writing)
            link('4국02-01','not_direct_evidence','해설은 어조·억양 등 의미를 표현하는 유창한 읽기까지 다루며 본 자료는 그 낭독을 관찰하지 않음',['자료 비교 정답을 낭독 유창성 점수로 바꾸기'],[])
            scope='비교 기준·단위·목적과 판단 근거의 읽기 전략. S5의 홍보 의견 검토를 다른 단계의 사물 비교 전체와 구별함.'
        elif sid=='plan-G4-information-05':
            link('4국02-02','direct_component','핵심 안내를 간추릴 때 대상·시간·예외·변경 조건을 보존하는 부분',['중심 생각 찾기와 간추리기의 모든 글 유형','조건을 포함한 짧은 기능 자료가 학년 장문 읽기를 모두 대표한다는 주장'])
            scope='내용 간추리기 중 조건 보존 요소. 개념 확인과 조건 선택은 쓰기 요약 수행의 준비와 구별함.'
        elif sid=='plan-G2-writing-11':
            direct=s['stage']=='S6' and s['variant']=='B'
            link('2국03-03','direct_component' if direct else 'learning_support','물병의 식별 특징과 찾아갈 곳을 소개하는 글 쓰기 부분' if direct else '주변 소재를 독자가 알 수 있게 표현하는 데 필요한 정보 보충 연습',['모든 안내문 고쳐쓰기가 이 성취기준 전체와 같다는 주장','자신이 직접 소재를 발견·관찰해 독립 소개글을 쓰는 전체 과정'],writing if direct else allq)
            link('4국03-05','later_grade_articulation','자기 글의 빠진 정보를 점검하는 활동을 이후 학년의 쓰기 과정 점검과 연결해 논의',['상위 학년군 기준을 초2의 직접 성취기준으로 표기','이번 활동만으로 쓰기 자신감이나 과정 전체의 성취를 확정'],writing)
            scope='주변 물건 소개 과제와 알림·순서 글의 정보 보충을 구별. 소개 글을 실제 작성하는 S6-B만 직접 요소 후보로 둠.'
            if not direct:gap='알림·순서 글 고쳐쓰기를 1~2학년군 소개 글쓰기 전체의 직접 측정으로 두지 않음. 필요한 정보 보충의 내부 교수 목표로 검토.'
        elif sid=='plan-G4-media-02':
            link('4수04-01','cross_subject_component','그림그래프·막대그래프의 범례·단위·눈금을 해석하는 부분',['실제 자료 수집과 그래프를 직접 나타내는 전체 과정','수학 성취를 국어 직접 성취로 계산'])
            link('4국06-02','optional_followup','그래프와 설명을 활용한 발표 자료 제작으로 후속 연계 가능',['현재 그래프 해석 정답만으로 발표 자료 제작을 측정했다는 주장'],[])
            scope='그래프 해석은 수학 연계 요소로 표시하고 국어에서는 자료와 설명의 대응·범위를 다루는 응용 활동으로 검토.'
            gap='그림·막대 해석을 국어의 발표 자료 만들기 성취와 동일시하지 않음. 국어 독립 측정 목표와 수학 선수 기능의 배치를 검토.'
        audit=dict(version=1,checkedOn='2026-11-17',basis='로컬 교육부고시2022-33 원문·해설의 해당 행. 최신 통합본 전체 대조나 교사 승인을 뜻하지 않음.',decision='direct_component_candidate' if primary else 'related_only_goal_scope_review',scope=scope,remainingGap=gap,links=links,teacherApproval='pending',**extra)
        s['source']['officialStandards']=primary
        s['source']['curriculumAudit']=audit
        s['source']['curriculumAuditHash']=hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
        s['review']['curriculumAlignment']=scope+' '+gap+' 원문 대조와 측정 범위 분류이며 독립 교사 검토 대기.'
        if not primary:s['review']['goalMapping']='needs_formal_goal_scope_review'
        accepted=[r for r in links if r['role']!='not_direct_evidence']
        for q in s['questions']:
            measured=bool(primary) and s['stage'] not in ('S1','S2') and (q['kind'] in ('writing','explanation','revision','single_choice'))
            q['curriculumCoverage']=dict(linkIds=[r['id'] for r in accepted if q['id'] in r['questionIds']],state='component_candidate' if measured else 'preparation_or_related_activity',notFullStandardAchievement=True)
