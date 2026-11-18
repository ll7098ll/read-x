"""Uses only preview-course-ui.mjs, in-memory synthetic accounts and its isolated test clock."""
import json
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
root=Path(__file__).resolve().parents[1]
out=root/'output'/'course-journey'
out.mkdir(parents=True,exist_ok=True)
origin='http://127.0.0.1:5195'
def api(ctx,path,body=None):
    res=ctx.request.get(origin+'/api/exam'+path) if body is None else ctx.request.post(origin+'/api/exam'+path,data=body,headers={'Origin':origin})
    assert res.ok,(path,res.status,res.text())
    return res.json()
forms=json.loads(subprocess.check_output(['node','--input-type=module','-e',"import {placementForm} from './webapp/server/placement-content.mjs';console.log(JSON.stringify([placementForm(3),placementForm(3,'extend')]))"],cwd=root,encoding='utf-8'))
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    teacher=browser.new_context(viewport={'width':1280,'height':900})
    student=browser.new_context(viewport={'width':390,'height':844})
    def login():
        api(teacher,'/login',{'username':'course-teacher','password':'Course-Preview-2026!'})
        api(student,'/login',{'username':'course-student','password':'Course-Preview-2026!'})
    login()
    r=api(student,'/learning/placement/start',{'grade':3})['placement']
    for form in forms:
        for q in form['questions']:
            if q['id'] in r['answers']:continue
            answer={'choice':q['answer']} if q['options'] else {'text':'본문의 두 정보를 연결해 설명합니다.','evidence':q['evidence']}
            r=api(student,'/learning/placement/answer',{'questionId':q['id'],'revision':r['revision'],**answer})['placement']
        r=api(student,'/learning/placement/submit',{'revision':r['revision']})['placement']
    sid=r['studentId']
    lesson=api(teacher,'/learning/catalog/corpus-v2:P22-G3-S1-01')
    api(teacher,'/learning/approvals',{'lessonId':lesson['lesson']['id'],'contentHash':lesson['contentHash'],'note':'시작 수업 검토','pilot':True})
    api(teacher,'/learning/placement/approve',{'studentId':sid,'revision':r['revision'],'course':'connect','level':'standard','lessonId':lesson['lesson']['id'],'note':'관계 연결부터 시작합니다.','explanationReviews':['success','success']})
    tp=teacher.new_page();sp=student.new_page();errors=[]
    for page in [tp,sp]:page.on('pageerror',lambda e:errors.append(str(e)))
    tp.goto(origin+'/#/teacher/classes')
    tp.get_by_label('진단 학생',exact=True).select_option(sid)
    tp.get_by_role('button',name='4주 계획 검토하기',exact=True).click()
    tp.get_by_label('계획·이동 승인 의견').fill('수업 세 개와 새 글 확인 자료를 검토했습니다.')
    tp.get_by_role('checkbox',name='수업과 확인 자료의 적합성을 검토했습니다.').check()
    tp.get_by_role('button',name='4주 계획 시작',exact=True).click()
    expect(tp.locator('.course-sessions > li')).to_have_count(8)
    record=api(student,'/learning/course')['course'];plan=record['plan']
    assert 'checkBank' not in plan
    for tr in plan['training']:
        d=api(student,f"/learning/assignments/{tr['assignmentId']}/start",{})
        run=d['run'];qs=d['lesson'].get('levelQuestions',{}).get(d['assignment']['level'],d['lesson']['questions'])
        for q in qs:
            choice=None if q.get('responseKind')=='explanation' else q['answer']
            run['responses'][q['id']]={'choice':choice,'evidence':q['evidence'],'reason':'근거와 관계를 연결해서 설명합니다.','hintLevel':0,'revealed':False,'submissions':[{'id':'qa-'+q['id'],'choice':choice,'evidence':q['evidence'],'reason':'근거와 관계를 연결해서 설명합니다.','hintLevel':0}]}
        saved=api(student,f"/learning/runs/{d['id']}/save",{'revision':d['revision'],'mutationId':'qa-save','run':run,'writing':'오늘 배운 관계를 정리했습니다.'})
        api(student,f"/learning/runs/{d['id']}/submit",{'revision':saved['revision']})
    full=api(teacher,'/learning/course/preview',{'studentId':sid})['bundle']
    for i in range(5):
        if i==3:
            assert student.request.post(origin+'/__qa/advance',data={'days':7}).ok
            login()
        c=api(student,'/learning/course/check/start',{'planId':plan['id'],'purpose':'independent'})['check']
        key=next(x for x in full['checks'] if x['id']==c['content']['id'])
        submitted=api(student,'/learning/course/check/submit',{'checkId':c['id'],'revision':c['revision'],'answer':{'choice':key['answer'],'evidence':key['evidence'],'reason':'본문의 원인과 결과를 연결해서 판단했습니다.'}})['check']
        api(teacher,'/learning/course/check/review',{'studentId':sid,'checkId':c['id'],'revision':submitted['revision'],'outcome':'success','note':'근거와 연결 설명을 확인했습니다.'})
    sp.goto(origin+'/#/student/classes')
    expect(sp.locator('.course-sessions > li')).to_have_count(8)
    sp.screenshot(path=str(out/'four-week-mobile.png'),full_page=True)
    assert sp.evaluate('document.documentElement.scrollWidth <= innerWidth')
    sp.get_by_role('button',name='새 상황 적용 열기',exact=True).click()
    player=sp.locator('.course-player')
    key=full['checks'][5]
    player.get_by_role('radio').nth(key['answer']).check()
    for i in key['evidence']:player.get_by_role('checkbox').nth(i).check()
    player.get_by_label('근거와 연결한 내 설명').fill('신청자 8명은 진행 조건 6명 이상이므로 앞치마를 준비합니다.')
    player.get_by_role('button',name='확인 답안 저장',exact=True).click()
    expect(player.get_by_role('button',name='계획으로 돌아가기')).to_be_enabled()
    player.get_by_role('button',name='확인 답안 제출',exact=True).click()
    expect(player.get_by_text('선생님이 설명을 검토하고 있어요.')).to_be_visible()
    tp.reload()
    tp.get_by_label('진단 학생',exact=True).select_option(sid)
    row=tp.locator('.course-check-row').filter(has_text='새 상황 적용')
    row.locator('summary').first.click()
    row.get_by_label('설명 검토').select_option('success')
    row.get_by_label('지도 의견').fill('새 자료의 조건을 모두 연결해 설명했습니다.')
    row.get_by_role('button',name='성취 확인 검토 저장').click()
    tp.get_by_role('button',name='의미 풀기 단계 이동 검토',exact=True).click()
    tp.get_by_label('계획·이동 승인 의견').fill('서로 다른 날의 독립 수행과 새 상황 적용을 확인했습니다.')
    tp.get_by_role('checkbox',name='수업과 확인 자료의 적합성을 검토했습니다.').check()
    tp.get_by_role('button',name='다음 단계로 이동하고 새 계획 배정',exact=True).click()
    expect(tp.get_by_role('button',name='의미 풀기 단계 이동 검토',exact=True)).to_have_count(0)
    sp.reload()
    expect(sp.locator('.course-journey').get_by_text('의미 풀기 · 현재 코스',exact=True)).to_be_visible()
    sp.screenshot(path=str(out/'next-stage-mobile.png'),full_page=True)
    tp.screenshot(path=str(out/'teacher-plan-desktop.png'),full_page=True)
    assert not errors,errors
    (out/'verification.json').write_text(json.dumps({'passed':True,'browserErrors':errors,'scenarios':['plan approval','8 sessions','different-day evidence','independent transfer save','teacher review','next stage','mobile layout']},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
print('4-week course browser journey passed')

