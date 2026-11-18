"""Only preview-pilot-ui.mjs: synthetic memory DB, never production students."""
import json
from uuid import uuid4
from pathlib import Path
from playwright.sync_api import sync_playwright,expect
root=Path(__file__).resolve().parents[1]
out=root/'output'/'classroom-pilot-2026-11-18'
out.mkdir(parents=True,exist_ok=True)
origin='http://127.0.0.1:5196'
password='Pilot-Preview-2026!'
key='check:g3:evidence:0'
name='초3 단서 파일럿 QA'
def api(ctx,path,body=None):
    r=ctx.request.get(origin+'/api/exam'+path) if body is None else ctx.request.post(origin+'/api/exam'+path,data=body,headers={'Origin':origin})
    assert r.ok,(path,r.status,r.text())
    return r.json()
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    teacher=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
    api(teacher,'/login',{'username':'pilot-teacher','password':password})
    tp=teacher.new_page();tp.set_default_timeout(60000);errors=[];tp.on('pageerror',lambda e:errors.append(str(e)))
    tp.goto(origin+'/#/teacher/classes',wait_until='networkidle')
    tp.get_by_role('button',name='교사 검수·수업 파일럿 열기',exact=True).click()
    workspace=tp.get_by_role('region',name='수업 파일럿',exact=True)
    workspace.get_by_label('파일럿 자료 학년',exact=True).select_option('3')
    workspace.get_by_label('파일럿 용도',exact=True).select_option('check')
    workspace.get_by_label('파일럿 목표',exact=True).select_option('evidence')
    workspace.get_by_role('button',name='검수·분석 '+key,exact=True).click()
    detail=workspace.locator('.pilot-detail').first
    for label in ['학년별 난이도 확인','정답의 유일성 확인','본문 근거 확인','해설·채점 준거 확인']:
        detail.get_by_label(label,exact=True).check()
    detail.get_by_label('문항 검수 의견',exact=True).fill('가상 QA: 학년 부담과 정답·근거·해설을 대조했습니다.')
    detail.get_by_role('button',name='문항 검수 저장',exact=True).click()
    expect(detail.get_by_role('button',name='문항 검수 저장',exact=True)).to_be_enabled()
    workspace.get_by_label('수업에 넣기 '+key,exact=True).check()
    workspace.get_by_label('파일럿 수업 이름',exact=True).fill(name)
    state=api(teacher,'/learning/pilot')
    assert len(state['students'])==22
    for s in state['students']:
        workspace.get_by_label(s['name'],exact=True).check()
    workspace.get_by_role('button',name='파일럿 수업 배정',exact=True).click()
    expect(workspace.locator('.pilot-table tbody tr')).to_have_count(22)
    print('Teacher review and assignment passed',flush=True)
    state=api(teacher,'/learning/pilot')
    item=api(teacher,'/learning/pilot/item',{'itemKey':key})['item']
    records={r['studentName']:r for r in state['learners']}
    student=browser.new_context(viewport={'width':390,'height':844})
    api(student,'/login',{'username':'pilot-student-0','password':password})
    sp=student.new_page();sp.on('pageerror',lambda e:errors.append(str(e)))
    sp.goto(origin+'/#/student/classes');sp.bring_to_front()
    sp.get_by_role('button',name='배정된 수업 파일럿 열기',exact=True).click()
    sp.get_by_role('button',name='파일럿 시작',exact=True).click()
    player=sp.locator('.pilot-player')
    expect(player.get_by_role('radio').nth(item['question']['answer'])).to_be_visible()
    player.get_by_role('radio').nth(item['question']['answer']).check()
    player.get_by_label('내 설명',exact=True).fill('본문에 적힌 정보를 찾아 판단했어요.')
    for i in item['question']['evidence']:
        player.get_by_label(str(i+1)+'문단',exact=True).check()
    sp.wait_for_timeout(5600) # One real foreground heartbeat interval.
    player.get_by_role('button',name='파일럿 답 저장',exact=True).click()
    expect(player.get_by_role('button',name='1 · 저장',exact=True)).to_be_visible()
    r=api(student,'/learning/pilot/start',{'runId':records['가상 파일럿 학생 1']['runId']})['run']
    assert r['times'][key]>=4000
    assert all(k not in r['items'][0] for k in ['answer','question','explanation','pilotCalibration'])
    sp.reload()
    sp.get_by_role('button',name='배정된 수업 파일럿 열기',exact=True).click()
    with sp.expect_response(lambda response: response.url.endswith('/learning/pilot/pulse')) as resumed_pulse:
        sp.get_by_role('button',name='파일럿 이어 하기',exact=True).click()
    assert not resumed_pulse.value.json().get('leaseBusy',False)
    expect(sp.locator('.pilot-player').get_by_role('radio').nth(item['question']['answer'])).to_be_checked()
    player.screenshot(path=str(out/'student-response-mobile.png'),timeout=60000)
    sp.get_by_label('저장한 응답으로 이번 파일럿을 마칠게요.',exact=True).check()
    sp.get_by_role('button',name='파일럿 제출',exact=True).click()
    expect(sp.get_by_role('button',name='내 응답 보기',exact=True)).to_be_visible()
    assert sp.evaluate('document.documentElement.scrollWidth<=innerWidth')
    sp.screenshot(path=str(out/'student-pilot-mobile.png'),full_page=True)
    print('Student response, active timing and resume passed',flush=True)
    tp.bring_to_front()
    workspace.get_by_role('button',name='파일럿 새로고침',exact=True).click()
    workspace.get_by_role('button',name='관찰 기록 가상 파일럿 학생 1 '+name,exact=True).click()
    run_panel=workspace.locator('.pilot-detail').last
    expect(run_panel.get_by_role('heading',name='가상 파일럿 학생 1 · '+name+' 관찰',exact=True)).to_be_visible()
    run_panel.locator('summary').first.click()
    field=run_panel.get_by_role('group',name='이 문항의 실제 관찰',exact=True)
    field.get_by_label('관찰한 도움',exact=True).select_option('independent')
    field.get_by_label('이전 자료 노출',exact=True).select_option('new')
    field.get_by_label('관찰 의견·시간 보완 이유',exact=True).fill('가상 QA: 처음 보는 자료에서 도움 없이 응답했습니다.')
    with tp.expect_response(lambda response: response.url.endswith('/learning/pilot/observe') and response.request.method=='POST') as saved_observation:
        field.get_by_role('button',name='학생 관찰 저장',exact=True).click()
    assert saved_observation.value.ok
    expect(detail.get_by_text('보정 제안: 표본 수집 중.',exact=False)).to_be_visible()
    expect(detail.get_by_role('button',name='난도 보정 승인',exact=True)).to_be_disabled()
    # Nineteen further independent first responses plus helped/unknown controls.
    for n in range(1,22):
        ctx=browser.new_context()
        api(ctx,'/login',{'username':'pilot-student-'+str(n),'password':password})
        sid=records['가상 파일럿 학생 '+str(n+1)]['runId']
        r=api(ctx,'/learning/pilot/start',{'runId':sid})['run']
        answer={'choice':item['question']['answer'] if n<16 or n>=20 else (item['question']['answer']+1)%len(item['question']['options']),'text':'가상 QA 응답','evidence':item['question']['evidence'],'support':'prompted' if n==20 else 'independent','omitted':False}
        r=api(ctx,'/learning/pilot/answer',{'runId':sid,'itemKey':key,'revision':r['revision'],'answer':answer})['run']
        r=api(ctx,'/learning/pilot/submit',{'runId':sid,'revision':r['revision']})['run']
        if n!=21:
            api(teacher,'/learning/pilot/observe',{'runId':sid,'itemKey':key,'revision':r['revision'],'assistance':'independent','priorExposure':'new','rubric':'success','note':'가상 QA 초시계 관찰 입력 테스트','observedMs':20000})
        ctx.close()
    print('Synthetic independent/helped/unknown cohorts recorded',flush=True)
    workspace.get_by_role('button',name='파일럿 새로고침',exact=True).click()
    expect(detail.get_by_text('독립 분석 20/20명',exact=False)).to_be_visible()
    detail.get_by_label('보정 판단과 수업 적용 의견',exact=True).fill('가상 QA: 독립 20명의 80% 정답률과 불확실성을 검토했습니다.')
    detail.get_by_label('표본·도움·이전 노출·정답률 구간을 검토했습니다.',exact=True).check()
    detail.get_by_role('button',name='난도 보정 승인',exact=True).click()
    expect(detail.get_by_text('현재 관찰 자료와 일치',exact=False)).to_be_visible()
    calibrated=api(teacher,'/learning/pilot/item',{'itemKey':key})
    assert calibrated['statistics']['independentN']==20
    assert calibrated['statistics']['p']==.8
    assert calibrated['statistics']['assisted']==1
    assert calibrated['statistics']['unknownHelp']==1
    assert calibrated['calibration']['current'] is True
    assert calibrated['calibration']['band']=='입문'
    detail.screenshot(path=str(out/'teacher-item-analysis.png'),timeout=60000)
    tp.screenshot(path=str(out/'teacher-calibration-desktop.png'),full_page=True)
    with tp.expect_download() as pending:
        workspace.get_by_role('button',name='파일럿 관찰·분석 JSON 내려받기',exact=True).click()
    pending.value.save_as(str(out/'synthetic-observations.json'))
    exported=json.loads((out/'synthetic-observations.json').read_text(encoding='utf-8'))
    assert len(exported['learners'])==22
    assert next(i for i in exported['items'] if i['itemKey']==key)['independentN']==20
    workspace.get_by_label('수업에 넣기 '+key,exact=True).check()
    workspace.get_by_label('파일럿 수업 이름',exact=True).fill('보정 난도 배정본 QA')
    workspace.get_by_label('가상 파일럿 학생 1',exact=True).check()
    workspace.get_by_role('button',name='파일럿 수업 배정',exact=True).click()
    expect(workspace.locator('.pilot-table tbody tr')).to_have_count(23)
    second=next(r for r in api(teacher,'/learning/pilot')['learners'] if r['name']=='보정 난도 배정본 QA')
    snapshot=api(teacher,'/learning/pilot/run',{'runId':second['runId']})['run']['items'][0]
    assert snapshot['pilotCalibration']['n']==20
    # Changing an observed source value makes the previous approval stale.
    first=api(teacher,'/learning/pilot/run',{'runId':records['가상 파일럿 학생 1']['runId']})['run']
    api(teacher,'/learning/pilot/observe',{'runId':first['id'],'itemKey':key,'revision':first['revision'],'assistance':'independent','priorExposure':'new','rubric':'success','note':'가상 QA: 시간 보완으로 기존 보정 이력 재검토 확인','observedMs':30000})
    workspace.get_by_role('button',name='파일럿 새로고침',exact=True).click()
    expect(detail.get_by_text('자료 변경 · 재검토 필요',exact=False)).to_be_visible()
    tp.set_viewport_size({'width':390,'height':844})
    assert tp.evaluate('document.documentElement.scrollWidth<=innerWidth')
    tp.screenshot(path=str(out/'teacher-pilot-mobile.png'),full_page=True)
    # Low-grade explanation can be requested orally without keyboard writing.
    oral_key='diagnostic:g1:support:explain-0'
    oi=api(teacher,'/learning/pilot/item',{'itemKey':oral_key})
    api(teacher,'/learning/pilot/review',{'itemKey':oral_key,'contentHash':oi['item']['contentHash'],'revision':0,'status':'approved','checks':{'difficulty':True,'answer':True,'evidence':True,'explanation':True},'note':'가상 QA 저학년 구두 설명 검수'})
    oral_sid=next(x['id'] for x in state['students'] if x['name']=='가상 파일럿 학생 22')
    api(teacher,'/learning/pilot/create',{'name':'초1 말로 설명 QA','itemKeys':[oral_key],'studentIds':[oral_sid],'mutationId':str(uuid4())})
    oral_ctx=browser.new_context(viewport={'width':390,'height':844})
    api(oral_ctx,'/login',{'username':'pilot-student-21','password':password})
    op=oral_ctx.new_page();op.on('pageerror',lambda e:errors.append(str(e)))
    op.goto(origin+'/#/student/classes');op.bring_to_front()
    op.get_by_role('button',name='배정된 수업 파일럿 열기',exact=True).click()
    op.get_by_role('article').filter(has_text='초1 말로 설명 QA').get_by_role('button',name='파일럿 시작',exact=True).click()
    oral_player=op.locator('.pilot-player')
    oral_player.get_by_label('말로 설명하고 선생님이 기록해요',exact=True).check()
    expect(oral_player.get_by_label('내 설명',exact=True)).to_be_disabled()
    oral_player.get_by_role('button',name='파일럿 답 저장',exact=True).click()
    expect(oral_player.get_by_role('button',name='1 · 저장',exact=True)).to_be_visible()
    oral_player.screenshot(path=str(out/'student-oral-mobile.png'))
    op.get_by_label('저장한 응답으로 이번 파일럿을 마칠게요.',exact=True).check()
    op.get_by_role('button',name='파일럿 제출',exact=True).click()
    expect(op.get_by_role('button',name='내 응답 보기',exact=True)).to_have_count(2)
    tp.bring_to_front();workspace.get_by_role('button',name='파일럿 새로고침',exact=True).click()
    workspace.get_by_role('button',name='관찰 기록 가상 파일럿 학생 22 초1 말로 설명 QA',exact=True).click()
    oral_panel=workspace.locator('.pilot-detail').last
    expect(oral_panel.get_by_role('heading',name='가상 파일럿 학생 22 · 초1 말로 설명 QA 관찰',exact=True)).to_be_visible()
    oral_panel.locator('summary').first.click()
    field=oral_panel.get_by_role('group',name='이 문항의 실제 관찰',exact=True)
    field.get_by_label('학생이 실제로 말한 내용',exact=True).fill('글의 단서를 보고 그렇게 생각했어요.')
    field.get_by_label('관찰한 도움',exact=True).select_option('independent')
    field.get_by_label('이전 자료 노출',exact=True).select_option('new')
    field.get_by_label('관찰 의견·시간 보완 이유',exact=True).fill('가상 QA 교사는 받아 적기만 했습니다.')
    with tp.expect_response(lambda response: response.url.endswith('/learning/pilot/observe') and response.request.method=='POST') as saved_observation:
        field.get_by_role('button',name='학생 관찰 저장',exact=True).click()
    assert saved_observation.value.ok
    expect(field.get_by_role('button',name='학생 관찰 저장',exact=True)).to_be_enabled()
    assert api(teacher,'/learning/pilot/item',{'itemKey':oral_key})['statistics']['independentN']==1
    assert not errors,errors
    (out/'browser-verification.json').write_text(json.dumps({'passed':True,'syntheticOnly':True,'catalogItems':460,'students':22,'independentN':20,'p':.8,'assistedExcluded':1,'unknownHelpExcluded':1,'teacherCalibrationApproved':True,'newAssignmentSnapshot':True,'changedDataMarkedStale':True,'studentResumeAndActiveTimer':True,'jsonExport':True,'lowGradeOralObserved':True,'mobileOverflow':False,'browserErrors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
print('Classroom pilot: teacher review, student response/resume/time, observation, 20-person calibration, export and stale-data checks passed')
