"""Build language drafts, preserve ambiguity limits, verify standalone artifacts."""
import hashlib,json
from author_language_v2 import build,DEST,OUT,ROOT,CELLS,SKILLS
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks={};byid={s['id']:s for s in sets}
    for s in sets:
        q=s['questions'][0]
        checks[s['id']+'_primary_first']=s['presentationOrder'][0]==q['id'] and q['kind']!='single_choice' and s['languageReview']['primaryQuestionId']==q['id']
        checks[s['id']+'_response_criteria']=len(q['rubric'])>=2 and s['languageReview']['teacherApproval']=='pending'
    def source(g,n,stage):return ' '.join(p['text'] for p in byid[f'PV2-G{g}-language-{n}-{stage}-A']['paragraphs'])
    def answer(g,n,stage):return byid[f'PV2-G{g}-language-{n}-{stage}-A']['questions'][0]['expectedAnswer']
    checks['G1_give_receive_not_reversed']='나리가 준서에게' in answer(1,'08','S5') and '받은 인형' in source(1,'08','S5')
    checks['G2_question_form_request_context']='양손으로 큰 종이' in source(2,'10','S4') and '문을 닫아 줘' in answer(2,'10','S4')
    checks['G2_same_ending_distinct_contexts']='창문이 보이지 않았어요' in source(2,'10','S5') and '창문이 열린 것을 보고' in source(2,'10','S5')
    checks['G3_order_not_role']='작은 깃발을 하준이가 들었다' in source(3,'06','S3') and '가와 나 모두 하준이' in answer(3,'06','S3')
    checks['G3_ellipsis_not_universal_error']='모든 문맥에서 비문' in byid['PV2-G3-language-06-S5-A']['teacherGuide']
    checks['G4_sequence_not_single_cause']='같은 날 안내 표지도' in source(4,'10','S4') and '조명만의 영향은 확정할 수 없다' in answer(4,'10','S4')
    checks['G4_intent_not_absolute_ungrammatical']='언제나 비문이라고 하지 않는다' in byid['PV2-G4-language-10-S5-A']['teacherGuide']
    checks['G5_two_stage_actors']='서준이는 무대에서' in source(5,'08','S3') and '동생은 무대에서 노래했다' in source(5,'08','S3')
    checks['G5_revision_does_not_repeat_ambiguous_modifier']='가:서준이는 무대에서 연주했다. 나는 서준이의 동생을 객석에서 만났다.' in answer(5,'08','S3')
    checks['G5_coordination_two_visitors']='두 사람이 따로 서명했다' in source(5,'08','S4') and '서진이를 가르치는 박 선생님도' in answer(5,'08','S4')
    checks['G5_transport_both_ribbon_one']='상자에는 리본을 달지 않고' in source(5,'08','S5') and '상자도 함께 가져와' in answer(5,'08','S5')
    checks['G6_reservation_and_deadline']='시작 10분 전까지' in source(6,'11','S2') and '하율은 늦어' in answer(6,'11','S2') and '서후는 예약하지 않아' in answer(6,'11','S2')
    checks['G6_if_and_only_distinct']='다른 조건이 없다' in source(6,'11','S3') and '선착순 20명' in source(6,'11','S3') and '25번째' in source(6,'11','S3')
    checks['G6_two_negation_readings']='두 명이 왔고 두 명은 오지 않았다' in source(6,'11','S4') and '온 사람이 한 명도 없었다' in source(6,'11','S4')
    checks['G6_exception_not_all_activities']='설명회에는 참석할 수 있다' in source(6,'11','S5') and '예외를 보충했고' in answer(6,'11','S5')
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,5)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
    report['languageConsistencyChecks']=inspect_cases(sets)
    report['stageFitReviewDecisions']=[dict(questionId=w['id'],decision='주 응답은 별도의 의미 설명·재표현이고 이 보조 문항은 본문의 명시적 근거 선택이므로 직접 인용을 허용.',state='AI_editorial_review_not_teacher_approval') for w in report['stageFitWarnings'] if next(q for s in sets for q in s['questions'] if q['id']==w['id'])['kind']=='evidence_selection']
    ledger=ROOT/'research/language_v2_sources_2026-11-18.json'
    report['languageResearchLedger']=dict(path=str(ledger.relative_to(ROOT)).replace('\\','/'),sha256=hashlib.sha256(ledger.read_bytes()).hexdigest(),scope='교사용 개념 집필 참고, 학년 규준·정답 유일성 검증과 구별')
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-05');workbook=verify(source,OUT)
    notes=['교사용 언어·표현 관찰표 · 실제 학생 응답과 교사 승인은 아직 없음','주 응답을 먼저 받고 다른 문장도 제시된 뜻을 보존하면 수용한다.','']
    for s in sets:
        q=s['questions'][0]
        notes += [s['id']+' | '+s['title'],s['learnerStageLabel'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric']),'[학생 첫 응답 원문]','[지문에서 확인한 대상·행동·범위·조건]','[고쳐 쓴 문장과 보존한 뜻]','[다른 해석·추가 확인이 필요한 부분]','[대독·받아쓰기·뒤 문항·해설 노출]','[교사 추가 확인·판정·미확인]','']
    (OUT/'교사용_언어_표현_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(stages) for stages in CELLS.values()),primaryExplanations=len(sets),primaryAnalyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),languageConsistencyChecks=len(report['languageConsistencyChecks']),languageResearchLedger=report['languageResearchLedger'],passed=report['passed'] and workbook['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
