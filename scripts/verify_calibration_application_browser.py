"""End-to-end QA with preview-calibration-ui.mjs synthetic memory accounts."""
import json
from uuid import uuid4
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
root=Path(__file__).resolve().parents[1]
out=root/'output'/'calibration-application-2026-11-18';out.mkdir(parents=True,exist_ok=True)
origin='http://127.0.0.1:5198';password='Calibration-Preview-2026!'
def api(ctx,path,body=None):
    r=ctx.request.get(origin+'/api/exam'+path) if body is None else ctx.request.post(origin+'/api/exam'+path,data=body,headers={'Origin':origin})
    assert r.ok,(path,r.status,r.text())
    return r.json()
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    teacher=browser.new_context(viewport={'width':1440,'height':1000})
    api(teacher,'/login',{'username':'calibration-teacher','password':password})
    catalog=api(teacher,'/learning/pilot')['catalog']
    words=[i['key'] for i in catalog if i['grade']==1 and i.get('branch')=='common' and i['skill']=='words']
    common_evidence=[i['key'] for i in catalog if i['grade']==1 and i.get('branch')=='common' and i['skill']=='evidence']
    extra_evidence=[i['key'] for i in catalog if i['grade']==1 and i.get('branch')=='extend' and i['skill']=='evidence']
    assert len(words)==len(common_evidence)==len(extra_evidence)==2
    check='check:g1:evidence:4';keys=words+common_evidence+extra_evidence+[check]
    content={key:api(teacher,'/learning/pilot/item',{'itemKey':key})['item'] for key in keys}
    for key,i in content.items():
        api(teacher,'/learning/pilot/review',{'itemKey':key,'contentHash':i['contentHash'],'revision':0,'status':'approved','checks':{'difficulty':True,'answer':True,'evidence':True,'explanation':True},'note':'가상 적용 QA 문항 검수'})
    roster=api(teacher,'/learning/pilot')['students'];by_name={s['name']:s for s in roster}
    source_ids=[by_name['가상 적용 학생 '+str(n+1)]['id'] for n in range(20)]
    session=api(teacher,'/learning/pilot/create',{'name':'가상 적용 원자료','itemKeys':keys,'studentIds':source_ids,'mutationId':str(uuid4())})['sessionId']
    records={r['studentId']:r for r in api(teacher,'/learning/pilot')['learners'] if r['sessionId']==session}
    for n in range(20):
        ctx=browser.new_context();api(ctx,'/login',{'username':'calibration-student-'+str(n),'password':password})
        r=api(ctx,'/learning/pilot/start',{'runId':records[source_ids[n]]['runId']})['run']
        for key,i in content.items():
            correct_n=4 if key in words else 12 if key==check or key==common_evidence[0] else 18
            choice=i['question']['answer'] if n<correct_n else (i['question']['answer']+1)%len(i['question']['options'])
            r=api(ctx,'/learning/pilot/answer',{'runId':r['id'],'itemKey':key,'revision':r['revision'],'answer':{'choice':choice,'text':'가상 QA 응답','evidence':i['question']['evidence'],'support':'independent','omitted':False}})['run']
        r=api(ctx,'/learning/pilot/submit',{'runId':r['id'],'revision':r['revision']})['run']
        for key in keys:
            r=api(teacher,'/learning/pilot/observe',{'runId':r['id'],'itemKey':key,'revision':r['revision'],'assistance':'independent','priorExposure':'new','rubric':'success','note':'가상 QA 첫 독립 수행'})['run']
        ctx.close()
    for key in keys:
        d=api(teacher,'/learning/pilot/item',{'itemKey':key});assert d['statistics']['independentN']==20
        api(teacher,'/learning/pilot/calibrate',{'itemKey':key,'datasetHash':d['statistics']['datasetHash'],'revision':0,'confirmed':True,'note':'가상 QA 20명 보정 승인'})
    print('Seven current teacher-approved calibrations seeded from 20 first independent students',flush=True)
    target=by_name['가상 적용 학생 21']['id'];errors=[]
    tp=teacher.new_page();tp.set_default_timeout(60000);tp.on('pageerror',lambda e:errors.append(str(e)));tp.goto(origin+'/#/teacher/classes',wait_until='networkidle')
    tp.get_by_role('button',name='보정 난도 적용·전후 비교 열기',exact=True).click()
    panel=tp.get_by_role('region',name='보정 난도 실제 적용',exact=True)
    panel.get_by_label('비교할 학생',exact=True).select_option(target)
    panel.get_by_label('비교할 자료 학년',exact=True).select_option('1')
    panel.get_by_role('button',name='적용 전후 미리보기',exact=True).click()
    expect(panel.get_by_text('적용 가능한 문항 7개',exact=False)).to_be_visible()
    panel.get_by_label('이 반의 새 진단·코스에 내 승인 보정 사용',exact=True).check()
    panel.get_by_label('적용·중지 운영 의견',exact=True).fill('가상 QA: 유효 보정만 새 진단·코스에 사용합니다.')
    with tp.expect_response(lambda r:r.url.endswith('/learning/calibration/configure')) as configured:
        panel.get_by_role('button',name='보정 적용 설정 저장',exact=True).click()
    assert configured.value.ok
    expect(panel.get_by_text('현재 설정: 보정 사용',exact=False)).to_be_visible()
    student=browser.new_context(viewport={'width':390,'height':844});api(student,'/login',{'username':'calibration-student-20','password':password})
    sp=student.new_page();sp.on('pageerror',lambda e:errors.append(str(e)));sp.goto(origin+'/#/student/classes')
    sp.get_by_label('재학 학년').select_option('1');sp.get_by_role('radio',name='연필',exact=True).check();sp.get_by_role('button',name='시작 진단',exact=True).click()
    expect(sp.get_by_role('button',name='이 답 저장',exact=True)).to_be_visible()
    r=api(student,'/learning/placement')['placement']
    full=next(p for p in api(teacher,'/learning/placement')['placements'] if p['studentId']==target)['form']
    assert full['questions'][0]['skill']=='evidence'
    for key in ['calibrationContext','applicationComparison','branchForms']:assert key not in r
    assert all('pilotCalibration' not in q for q in r['form']['questions'])
    sp.screenshot(path=str(out/'calibrated-diagnostic-mobile.png'),full_page=True)
    first_word=True
    for q in full['questions']:
        wrong=q['skill']=='words' and first_word
        if wrong:first_word=False
        r=api(student,'/learning/placement/answer',{'revision':r['revision'],'questionId':q['id'],'choice':(q['answer']+1)%len(q['options']) if wrong else q['answer']})['placement']
    sp.reload();sp.get_by_role('button',name='추가 진단으로',exact=True).click();expect(sp.get_by_role('button',name='진단 제출하고 코스 추천받기',exact=True)).to_be_visible()
    r=api(student,'/learning/placement')['placement'];assert r['branch']=='extend'
    full=next(p for p in api(teacher,'/learning/placement')['placements'] if p['studentId']==target)['form'];wrong_evidence=False
    for q in full['questions']:
        if q['id'] in r['answers']:continue
        if q['options']:
            wrong=q['skill']=='evidence' and not wrong_evidence
            if wrong:wrong_evidence=True
            answer={'choice':(q['answer']+1)%len(q['options']) if wrong else q['answer']}
        else:answer={'text':'글의 단서를 연결해 판단했어요.','evidence':q['evidence']}
        r=api(student,'/learning/placement/answer',{'revision':r['revision'],'questionId':q['id'],**answer})['placement']
    sp.reload();sp.get_by_role('button',name='진단 제출하고 코스 추천받기',exact=True).click();expect(sp.get_by_text('선생님이 자기 설명과 추천 코스를 확인하고 첫 수업을 준비하고 있어요.')).to_be_visible()
    placed=next(p for p in api(teacher,'/learning/placement')['placements'] if p['studentId']==target);comp=placed['applicationComparison']
    assert comp['common']['baselineBranch']=='support' and comp['common']['appliedBranch']=='extend'
    assert comp['result']['baseline']['course']=='connect' and comp['result']['applied']['course']=='evidence'
    tp.reload();tp.get_by_label('진단 학생',exact=True).select_option(target)
    journey=tp.locator('.placement-journey');expect(journey.get_by_text('추가 진단 선정: 기존 지원형 → 적용 확장형',exact=True)).to_be_visible()
    journey.locator('.calibration-comparison').first.screenshot(path=str(out/'placement-before-after.png'))
    lesson=next(l for l in placed['candidates'] if l['course']==placed['recommendation']['course'])
    lp=api(teacher,'/learning/catalog/'+lesson['id']);api(teacher,'/learning/approvals',{'lessonId':lesson['id'],'contentHash':lp['contentHash'],'pilot':True,'note':'가상 첫 수업 검토'})
    api(teacher,'/learning/placement/approve',{'studentId':target,'revision':placed['revision'],'course':placed['recommendation']['course'],'level':placed['recommendation']['level'],'lessonId':lesson['id'],'note':'가상 QA 보정 추천과 실제 설명 확인','explanationReviews':['success','success'],'readingObservation':{'state':'follow_up','note':'가상 읽기 관찰 계획'}})
    tp.reload();tp.get_by_label('진단 학생',exact=True).select_option(target);tp.get_by_role('button',name='4주 계획 검토하기',exact=True).click()
    preview=api(teacher,'/learning/course/preview',{'studentId':target});selection=preview['bundle']['selectionComparison']['independent'];assert selection['baseline'][0]=='g1-evidence-check-0' and selection['applied'][0]=='g1-evidence-check-4'
    course_preview=tp.locator('.course-preview');course_preview.locator('.calibration-comparison > summary').click();course_preview.locator('.calibration-comparison').screenshot(path=str(out/'check-selection-before-after.png'))
    tp.get_by_label('계획·이동 승인 의견').fill('가상 QA 보정 선정 전후와 학년 적합성 확인');tp.get_by_role('checkbox',name='수업과 확인 자료의 적합성을 검토했습니다.').check();tp.get_by_role('button',name='4주 계획 시작',exact=True).click();expect(tp.locator('.course-sessions > li')).to_have_count(8)
    course=api(student,'/learning/course')['course'];plan=course['plan'];assert 'calibrationContext' not in plan and 'selectionComparison' not in plan
    for tr in plan['training'][:2]:
        d=api(student,'/learning/assignments/'+tr['assignmentId']+'/start',{});run=d['run'];qs=d['lesson'].get('levelQuestions',{}).get(d['assignment']['level'],d['lesson']['questions'])
        for q in qs:
            choice=None if q.get('responseKind')=='explanation' else q['answer'];run['responses'][q['id']]={'choice':choice,'reason':'본문 단서를 연결했어요.','evidence':q['evidence'],'hintLevel':0,'revealed':False,'submissions':[{'id':str(uuid4()),'choice':choice,'reason':'본문 단서를 연결했어요.','evidence':q['evidence'],'hintLevel':0}]}
        saved=api(student,'/learning/runs/'+d['id']+'/save',{'revision':d['revision'],'mutationId':str(uuid4()),'run':run,'writing':'가상 학습 정리'});api(student,'/learning/runs/'+d['id']+'/submit',{'revision':saved['revision']})
    sp.reload();sp.get_by_role('button',name='새 글 독립 확인 열기',exact=True).first.click();expect(sp.locator('.course-player')).to_be_visible()
    own=api(student,'/learning/course')['course']['plan']['checks'][0];assert own['content']['id']=='g1-evidence-check-4' and 'selectionComparison' not in own and 'pilotCalibration' not in own['content']
    sp.locator('.course-player').screenshot(path=str(out/'selected-check-mobile.png'))
    print('Actual diagnostic branch, recommended course and selected check changed as expected',flush=True)
    source=api(teacher,'/learning/pilot/run',{'runId':records[source_ids[0]]['runId']})['run']
    for key in words:
        source=api(teacher,'/learning/pilot/observe',{'runId':source['id'],'itemKey':key,'revision':source['revision'],'assistance':'prompted','priorExposure':'new','rubric':'success','note':'가상 QA: 질문 도움 재확인으로 독립 19명'})['run']
    second=browser.new_context();api(second,'/login',{'username':'calibration-student-21','password':password});new=api(second,'/learning/placement/start',{'grade':1})['placement']
    teacher_new=next(p for p in api(teacher,'/learning/placement')['placements'] if p['studentId']==by_name['가상 적용 학생 22']['id']);ctx=teacher_new['calibrationContext'];assert all(k not in ctx['items'] for k in words);assert all(any(f['key']==k and f['reason']=='insufficient_sample' and f['n']==19 for f in ctx['fallback']) for k in words)
    wrong_word=False
    for q in teacher_new['form']['questions']:
        wrong=q['skill']=='words' and not wrong_word
        if wrong:wrong_word=True
        new=api(second,'/learning/placement/answer',{'revision':new['revision'],'questionId':q['id'],'choice':(q['answer']+1)%len(q['options']) if wrong else q['answer']})['placement']
    new=api(second,'/learning/placement/submit',{'revision':new['revision']})['placement'];assert new['branch']=='support'
    frozen=next(c for c in api(teacher,'/learning/course')['courses'] if c['studentId']==target)['plan'];assert frozen['calibrationContext']['digest']==preview['bundle']['calibrationContext']['digest']
    tp.get_by_role('button',name='보정 난도 적용·전후 비교 열기',exact=True).click()
    panel=tp.get_by_role('region',name='보정 난도 실제 적용',exact=True)
    panel.get_by_label('비교할 학생',exact=True).select_option(by_name['가상 적용 학생 22']['id'])
    panel.get_by_label('비교할 자료 학년',exact=True).select_option('1')
    panel.get_by_role('button',name='적용 전후 미리보기',exact=True).click()
    panel.get_by_text('기존 기준 유지 사유',exact=True).click()
    expect(panel.get_by_text('현재 독립 19명',exact=False)).to_have_count(2)
    panel.locator('.pilot-detail').screenshot(path=str(out/'insufficient-sample-before-after.png'))
    assert not errors,errors
    (out/'browser-verification.json').write_text(json.dumps({'passed':True,'syntheticOnly':True,'approvedItems':7,'independentStudents':20,'commonBranch':{'baseline':'support','applied':'extend'},'courseRecommendation':{'baseline':'connect','applied':'evidence'},'selectedCheck':{'baseline':'g1-evidence-check-0','applied':'g1-evidence-check-4'},'insufficient19FallsBack':True,'approvedSnapshotPreserved':True,'privateMetadataHidden':True,'browserErrors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
print('Calibration application browser verification passed')
