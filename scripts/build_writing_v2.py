"""Reproduce and verify the thirty-six original writing-production drafts."""
import hashlib,json,re
from author_writing_v2 import build,DEST,OUT,SKILLS,ROOT
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def check_writing(sets):
    checks={}
    for s in sets:
        q=next(q for q in s['questions'] if q['id']==s['writingProtocol']['primaryQuestionId'])
        checks[s['id']+'_production_first']=q['kind']=='writing' and s['presentationOrder'][0]==q['id']
        checks[s['id']+'_reader_purpose_criteria']=all(q['writerContext'][k] for k in ['reader','purpose','length']) and len(q['rubric']) in (2,3)
        if s['grade']==2:checks[s['id']+'_experience_origin']=q['writerContext']['responseOrigin']=='learner_experience_or_labelled_fiction'
    byid={s['id']:s for s in sets}
    s=byid['PV2-G5-writing-08-S2-A'];body=' '.join(p['text'] for p in s['paragraphs']);q=s['questions'][0]
    checks['G5_S2_four_equals_two_plus_two']=all(x in body for x in ['장난감은 네 개','두 개는 바퀴를 고쳐','나머지 두 개는 부품']) and '네 개 중 두 개' in q['expectedAnswer'] and '나머지 두 개' in q['expectedAnswer']
    s=byid['PV2-G5-writing-08-S3-A'];body=' '.join(p['text'] for p in s['paragraphs']);q=s['questions'][0]
    checks['G5_S3_five_three_two_scope']='다섯 명 중 세 명' in body and '다른 두 명' in body and '다섯 명 중 세 명' in q['expectedAnswer'] and '모두의 이유는 모르지만' in q['expectedAnswer']
    s=byid['PV2-G6-writing-10-S6-A'];q=s['questions'][0]
    checks['G6_S6_same_time_in_two_formats']='오후 세 시부터 세 시 삼십 분' in q['expectedAnswer'] and '15:00~15:30' in q['expectedAnswer']
    checks['G6_S6_two_outputs_one_task']=sum(t['kind']=='writing' for t in s['questions'])==1 and '두 글' in q['prompt']
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    comparison=[ROOT/'data/content_authoring'/folder/'sets.json' for folder in ['pilot_v2','expansion_v2_01','expansion_v2_02']]
    report=validate(source,OUT,SKILLS,1,comparison)
    report['writingConsistencyChecks']=check_writing(sets)
    report['stageFitReviewDecisions']=[dict(questionId=w['id'],decision='보조 근거 찾기 문항이므로 직접 인용 답을 허용. 주 쓰기는 독자·자료 범위를 적용하는 생산 과제로 별도 검토.',state='AI_editorial_review_not_teacher_approval') for w in report['stageFitWarnings'] if next(q for s in sets for q in s['questions'] if q['id']==w['id'])['kind']=='evidence_selection']
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-03');workbook=verify(source,OUT)
    notes=(OUT/'교사용_쓰기_관찰표.txt').read_text(encoding='utf-8')
    assert all(s['id'] in notes for s in sets)
    summary=dict(asOf='2026-11-17',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),
      sets=len(sets),tasks=sum(len(s['questions']) for s in sets),writingProductionTasks=sum(q['kind']=='writing' for s in sets for q in s['questions']),
      writingRubricCriteria=sum(len(q['rubric']) for s in sets for q in s['questions'] if q['kind']=='writing'),
      newSkills=len(SKILLS),newSkillStageCells=len({(s['microSkillId'],s['stage']) for s in sets}),writingConsistencyChecks=len(report['writingConsistencyChecks']),
      passed=report['passed'] and workbook['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
