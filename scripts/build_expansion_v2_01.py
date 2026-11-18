"""Reproduce the expansion, with source/key consistency checks and separated workbooks."""
import hashlib,json,re
from author_expansion_v2 import build,DEST,OUT,SKILLS,ROOT
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as workbook
from verify_pilot_v2_workbook import verify

def check_records(sets):
    byid={s['id']:s for s in sets};checks={}
    def s(grade,track,number,stage):return byid[f'PV2-G{grade}-{track}-{number}-{stage}-A']
    def text(unit):return '\n'.join(p['text'] for p in unit['paragraphs'])
    def values(unit,kind):return [int(n) for n in re.findall(r'\d+',next(q['expectedAnswer'] for q in unit['questions'] if q['kind']==kind))]
    unit=s(5,'information','11','S2');body=text(unit)
    all_n=int(re.search(r'관람객 (\d+)명',body)[1]);four=int(re.search(r'고른 사람은 (\d+)명',body)[1]);six=int(re.search(r'여섯 시를 고른 사람은 (\d+)명',body)[1])
    checks['G5_S2_response_groups']=all_n==four+six and values(unit,'matching')==[all_n,four,six]
    unit=s(5,'information','11','S3');body=text(unit)
    count=int(re.search(r'같은 학생 (\d+)명',body)[1]);faster,same=map(int,re.search(r'(\d+)명은 두 번째에 더 빨랐고 (\d+)명은',body).groups())
    key=next(q['expectedAnswer'] for q in unit['questions'] if q['kind']=='revision')
    checks['G5_S3_comparison_groups']=count==faster+same and [int(n) for n in re.findall(r'\d+',key)]==[count,faster,same]
    unit=s(5,'information','11','S4');body=text(unit)
    completed=int(re.search(r'완료자가 (\d+)명',body)[1]);reviews,high=map(int,re.search(r'후기 (\d+)개 중 (\d+)개',body).groups())
    checks['G5_S4_unique_reviewers']='한 사람은 후기를 한 개만' in body
    checks['G5_S4_counts_and_nonresponse']=0<=high<=reviews<=completed and values(unit,'table_completion')==[completed,reviews,high,completed-reviews]
    unit=s(5,'information','11','S5');body=text(unit)
    earlier,later=map(int,re.search(r'첫 주 문의는 (\d+)건, 둘째 주는 (\d+)건',body).groups())
    key=next(q['expectedAnswer'] for q in unit['questions'] if q['kind']=='revision')
    checks['G5_S5_fewer_recorded_inquiries']=earlier>later>=0 and [int(n) for n in re.findall(r'\d+',key)]==[earlier,later]
    unit=s(5,'information','11','S6');body=text(unit)
    start_old,start_new=map(int,re.search(r'기존 안내책 (\d+)부와 새 안내책 (\d+)부',body).groups())
    old,new=map(int,re.search(r'기존은 (\d+)부, 새것은 (\d+)부',body).groups())
    checks['G5_S6_book_counts']=values(unit,'table_completion')==[start_old,old,start_old-old,start_new,new,start_new-new]
    sampled=int(re.search(r'응답한 (\d+)명',body)[1]);yes,unknown=map(int,re.search(r'(\d+)명은 그렇다, (\d+)명은',body).groups())
    checks['G5_S6_survey_groups']=sampled==yes+unknown and sampled<=start_new-new
    for unit in sets:
        if unit['stage']=='S6':
            first=next(q for q in unit['questions'] if q['id']==unit['presentationOrder'][0])
            checks[unit['id']+'_new_writing_first']=first['kind']=='writing'
    assert all(checks.values()),checks
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    report=validate(source,OUT,SKILLS,1,[ROOT/'data/content_authoring/pilot_v2/sets.json'])
    report['sourceKeyConsistencyChecks']=check_records(sets)
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    workbook(source,OUT,'expansion-v2-01');render=verify(source,OUT)
    # Recheck original assets after generalising their renderer/validator entry points.
    assert render['passed'] and report['passed']
    summary=dict(asOf='2026-11-17',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),
      sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),
      passed=True,sourceKeyConsistencyChecks=len(report['sourceKeyConsistencyChecks']),
      teacherApproval='pending',studentCalibration='pending',browserRuntime=render['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
