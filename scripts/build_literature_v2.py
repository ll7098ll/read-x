"""Verify literary delivery and expose bounded interpretation rather than pretending external approval."""
import hashlib,json
from author_literature_v2 import build,DEST,OUT,ROOT,CELLS,SKILLS
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks={};byid={s['id']:s for s in sets}
    for s in sets:
        primary=next(q for q in s['questions'] if q['id']==s['literaryReview']['primaryQuestionId'])
        checks[s['id']+'_interpretation_first']=s['presentationOrder'][0]==primary['id'] and primary['kind']!='single_choice'
        checks[s['id']+'_bounded_criteria']=len(primary['rubric'])>=2 and bool(s['literaryReview']['notAssessed'])
    s=byid['PV2-G3-literature-01-S4-A'];text=' '.join(p['text'] for p in s['paragraphs'])
    checks['snow_glove_loss_after_overnight_snow']='밤새 눈이 내린 다음 날' in text and '조금 전 놀이터에서 돌아온 뒤' in text and '아까 그네를 타지 않았던' in text and '어제 놀이터에서' not in text
    s=byid['PV2-G5-literature-02-S5-A'];text=' '.join(p['text'] for p in s['paragraphs'])
    checks['map_confirmed_route_and_unchecked_route']='실제 걷기 코스는 확인한 큰길' in text and '아직 끝까지 확인하지 않은 길' in text and '길 끝에 계단이 있는지' in text
    s=byid['PV2-G6-literature-04-S4-A'];text=' '.join(p['text'] for p in s['paragraphs'])
    checks['shop_memory_and_present_have_return_signal']='그때 내 손은 지금보다' in text and '상자 테이프가 뜯기는 소리' in text and '반 토막이었다' in text and '새 종이는 그 선에 맞춰' in text
    s=byid['PV2-G6-literature-04-S5-A'];text=' '.join(p['text'] for p in s['paragraphs'])
    checks['postcard_future_not_already_completed']='여름을 그려 보았다' in text and '아직 한 글자도 적혀 있지 않았다' in text and '날짜가 정해지면 먼저 알려' in text
    checks['six_poems_thirty_three_lines']=sum(len(s.get('poems',[])) for s in sets)==6 and sum(len(p['lines']) for s in sets for p in s.get('poems',[]))==33
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    comparison=[ROOT/'data/content_authoring'/folder/'sets.json' for folder in ['pilot_v2','expansion_v2_01','expansion_v2_02','expansion_v2_03']]
    report=validate(source,OUT,SKILLS,comparison_sources=comparison,expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
    report['literaryConsistencyChecks']=inspect_cases(sets)
    report['stageFitReviewDecisions']=[dict(questionId=w['id'],decision='주 해석은 별도 생산 응답이며 이 보조 문항은 작품의 근거 구절 찾기이므로 직접 인용을 허용.',state='AI_editorial_review_not_teacher_approval') for w in report['stageFitWarnings'] if next(q for s in sets for q in s['questions'] if q['id']==w['id'])['kind']=='evidence_selection']
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-04');workbook=verify(source,OUT)
    catalog=[];notes=['교사용 문학 해석 관찰표 · 실제 학생 응답·점수는 아직 없음','주 해석을 먼저 받고 뒤 문항·대독·받아쓰기 도움을 구별한다.','']
    for s in sets:
        if s.get('poems'):
            for poem in s['poems']:catalog.append(dict(id=poem['id'],materialId=s['id'],grade=s['grade'],stage=s['stage'],genre='시',title=poem['title'],lines=len(poem['lines']),authorship='자체 창작 초안',teacherApproval='pending'))
        else:
            work=[p for p in s['paragraphs'] if p['id'] in s['literaryReview']['workParagraphIds']]
            catalog.append(dict(id=s['id']+'-STORY',materialId=s['id'],grade=s['grade'],stage=s['stage'],genre='이야기',title=s['title'],charCount=len(' '.join(p['text'] for p in work)),materialCharCount=s['charCount'],paragraphs=len(work),authorship='자체 창작 초안',teacherApproval='pending'))
        q=s['questions'][0]
        notes += [s['id']+' | '+s['title'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric']),'[학생의 첫 해석 원문]','[학생이 짚은 구절]','[구절과 해석을 연결한 설명]','[다른 해석을 검토한 말]','[대독·받아쓰기·뒤 문항·해설 노출]','[교사의 추가 확인과 남은 미확인]','']
    (OUT/'작품_목록.json').write_text(json.dumps(dict(asOf='2026-11-18',contentSnapshotHash=report['contentSnapshotHash'],works=catalog),ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'교사용_문학_해석_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),
      newSkills=len(SKILLS),newSkillStageCells=sum(len(stages) for stages in CELLS.values()),narrativeWorks=sum(w['genre']=='이야기' for w in catalog),poems=sum(w['genre']=='시' for w in catalog),
      poetryLines=sum(w.get('lines',0) for w in catalog),interpretationCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),literaryConsistencyChecks=len(report['literaryConsistencyChecks']),
      passed=report['passed'] and workbook['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
