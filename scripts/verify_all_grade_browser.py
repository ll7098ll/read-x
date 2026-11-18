"""Full-grade QA against preview-course-ui.mjs; synthetic in-memory accounts only."""
import json
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
root=Path(__file__).resolve().parents[1]
out=root/'output'/'all-grade-journeys'
out.mkdir(parents=True,exist_ok=True)
origin='http://127.0.0.1:5195'
def api(ctx,path,body=None):
    res=ctx.request.get(origin+'/api/exam'+path) if body is None else ctx.request.post(origin+'/api/exam'+path,data=body,headers={'Origin':origin})
    assert res.ok,(path,res.status,res.text())
    return res.json()
forms=json.loads(subprocess.check_output(['node','--input-type=module','-e',"import {placementForm} from './webapp/server/placement-content.mjs';console.log(JSON.stringify(Object.fromEntries([1,2,3,4,5,6].map(g=>[g,[placementForm(g),placementForm(g,'extend')]]))))"],cwd=root,encoding='utf-8'))
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    teacher=browser.new_context(viewport={'width':1280,'height':900})
    teacher_user='course-teacher'
    password='Course-Preview-2026!'
    api(teacher,'/login',{'username':teacher_user,'password':password})
    tp=teacher.new_page();errors=[];tp.on('pageerror',lambda e:errors.append(str(e)))
    results=[]
    for grade in [1,2,3,4,5,6]:
        username='g'+str(grade)+'-'+str(int(time.time()*1000))
        sid=api(teacher,'/roster',{'student':{'name':f'초{grade} 검증 학생','username':username,'password':password}})['student']['id']
        ctx=browser.new_context(viewport={'width':390,'height':844})
        api(ctx,'/login',{'username':username,'password':password})
        page=ctx.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
        page.goto(origin+'/#/student/classes')
        page.get_by_label('재학 학년').select_option(str(grade))
        page.get_by_role('radio',name='연필',exact=True).check()
        page.get_by_role('button',name='시작 진단',exact=True).click()
        expect(page.get_by_role('button',name='이 답 저장',exact=True)).to_be_visible()
        page.screenshot(path=str(out/f'g{grade}-test-mobile.png'),full_page=True)
        r=api(ctx,'/learning/placement')['placement']
        assert 'formSnapshot' not in r
        assert len(r['form']['questions'])==(6 if grade<=2 else 12)
        assert all('explanation' not in q and 'optionReasons' not in q for q in r['form']['questions'])
        assert len(r['form']['questions'][0]['options'])==(3 if grade<=2 else 4)
        for phase,full in enumerate(forms[str(grade)]):
            for q in full['questions']:
                if q['id'] in r['answers']:continue
                if not q['options'] and grade==1:continue
                a={'choice':q['answer']} if q['options'] else {'text':'본문의 정보와 조건을 연결해 판단했습니다.','evidence':q['evidence']}
                r=api(ctx,'/learning/placement/answer',{'questionId':q['id'],'revision':r['revision'],**a})['placement']
            page.reload()
            if phase==0:
                page.get_by_role('button',name='추가 진단으로',exact=True).click()
                expect(page.get_by_role('button',name='진단 제출하고 코스 추천받기',exact=True)).to_be_visible()
                r=api(ctx,'/learning/placement')['placement']
            else:
                if grade==1:
                    for i in range(2):
                        page.get_by_role('checkbox',name='말로 설명하고 선생님이 기록해요',exact=True).check()
                        # first checkbox is the oral request; all remaining checkboxes are paragraph evidence.
                        for checkbox in page.locator('.placement-diagnostic fieldset input[type=checkbox]').all()[1:]:checkbox.check()
                        page.get_by_role('button',name='이 답 저장',exact=True).click()
                        expect(page.get_by_text('서버에 저장된 답이에요.',exact=True)).to_be_visible()
                        if i==0:page.get_by_role('button',name='다음 문제',exact=True).click()
                page.get_by_role('button',name='진단 제출하고 코스 추천받기',exact=True).click()
                expect(page.get_by_text('선생님이 자기 설명과 추천 코스를 확인하고 첫 수업을 준비하고 있어요.')).to_be_visible()
                r=api(ctx,'/learning/placement')['placement']
        page.screenshot(path=str(out/f'g{grade}-diagnostic-mobile.png'),full_page=True)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        tp.goto(origin+'/#/teacher/classes')
        tp.get_by_role('button',name='진단 현황 새로고침',exact=True).click()
        tp.get_by_label('진단 학생',exact=True).select_option(sid)
        if grade==1:
            for label in ['첫 번째 말로 설명 관찰','두 번째 말로 설명 관찰']:
                field=tp.get_by_role('group',name=label,exact=True)
                field.get_by_label('학생이 실제 말한 내용').fill('글의 단서를 보고 그렇게 생각했어요.')
                field.get_by_label('설명할 때의 도움').select_option('independent')
                field.get_by_role('button',name='말로 설명 관찰 저장').click()
                expect(field.get_by_role('button',name='말로 설명 관찰 저장')).to_be_enabled()
        if grade<=2:
            tp.get_by_label('실제 읽기 관찰',exact=True).select_option('follow_up')
            tp.get_by_label('읽기 관찰 내용 또는 추가 관찰 계획').fill('첫 수업에서 학생이 실제로 읽는 모습을 확인합니다.')
        tp.get_by_label('자기 설명 1 검토').select_option('success')
        tp.get_by_label('자기 설명 2 검토').select_option('success')
        tp.get_by_label('첫 수업',exact=True).select_option(index=1)
        expect(tp.get_by_text('첫 수업 본문·시범·문항 검토',exact=True)).to_be_visible()
        tp.get_by_label('배치 이유와 첫 2회 확인할 것').fill('학년별 글과 진단 응답을 검토하고 근거 설명을 확인합니다.')
        tp.get_by_role('checkbox',name='본문·문항·근거와 학년 적합성을 검토했고 시범 수업을 승인합니다.').check()
        tp.get_by_role('button',name='배치 확정하고 첫 수업 배정',exact=True).click()
        tp.get_by_role('button',name='4주 계획 검토하기',exact=True).click()
        tp.get_by_label('계획·이동 승인 의견').fill('학년별 수업과 확인 자료를 검토했습니다.')
        tp.get_by_role('checkbox',name='수업과 확인 자료의 적합성을 검토했습니다.').check()
        tp.get_by_role('button',name='4주 계획 시작',exact=True).click()
        expect(tp.locator('.course-sessions > li')).to_have_count(8)
        record=api(ctx,'/learning/course')['course'];plan=record['plan']
        assert plan['grade']==grade
        assert plan['course']==('evaluate' if grade>=5 else 'connect')
        for tr in plan['training']:
            d=api(ctx,f"/learning/assignments/{tr['assignmentId']}/start",{})
            assert d['lesson']['grade']==grade
            run=d['run'];qs=d['lesson'].get('levelQuestions',{}).get(d['assignment']['level'],d['lesson']['questions'])
            for q in qs:
                choice=None if q.get('responseKind')=='explanation' else q['answer']
                run['responses'][q['id']]={'choice':choice,'evidence':q['evidence'],'reason':'본문의 단서를 보고 설명했습니다.','hintLevel':0,'revealed':False,'submissions':[{'id':'all-grade-'+q['id'],'choice':choice,'evidence':q['evidence'],'reason':'본문의 단서를 보고 설명했습니다.','hintLevel':0}]}
            saved=api(ctx,f"/learning/runs/{d['id']}/save",{'revision':d['revision'],'mutationId':'all-grade-training','run':run,'writing':'오늘 배운 것을 짧게 적었습니다.'})
            api(ctx,f"/learning/runs/{d['id']}/submit",{'revision':saved['revision']})
        full=api(teacher,'/learning/course/preview',{'studentId':sid})['bundle']
        page.reload()
        page.wait_for_load_state('networkidle')
        (out/f'g{grade}-before-check.txt').write_text(page.locator('body').inner_text(),encoding='utf-8')
        page.get_by_role('button',name='새 글에서 독립 확인하기',exact=True).click()
        player=page.locator('.course-player');key=full['checks'][0]
        player.get_by_role('radio').nth(key['answer']).check()
        for i in key['evidence']:player.get_by_role('checkbox').nth(i).check()
        if grade==1:player.get_by_role('checkbox',name='말로 설명하고 선생님이 기록해요',exact=True).check()
        else:player.get_by_label('근거와 연결한 내 설명').fill('글의 정보와 조건을 근거로 판단했습니다.')
        player.get_by_role('button',name='확인 답안 제출',exact=True).click()
        expect(player.get_by_text('선생님이 설명을 검토하고 있어요.')).to_be_visible()
        expect(player.locator('.assessment-guide')).to_have_count(0)
        assert 'feedback' not in api(ctx,'/learning/course')['course']['plan']['checks'][0]
        tp.reload();tp.get_by_label('진단 학생',exact=True).select_option(sid)
        row=tp.locator('.course-check-row').first;row.locator('summary').first.click()
        guide=row.locator('.assessment-guide');guide.locator('summary').click()
        expect(guide.get_by_text(key['explanation'],exact=True).first).to_be_visible()
        expect(guide.get_by_text('본문 근거',exact=True)).to_be_visible()
        if grade==1:
            row.get_by_label('학생이 실제 말한 내용').fill('길이 젖어서 장화를 신었어요.')
            row.get_by_label('설명할 때의 도움').select_option('independent')
        row.get_by_label('설명 검토',exact=True).select_option('success')
        row.get_by_label('지도 의견').fill('학생의 실제 근거 설명을 확인했습니다.')
        row.get_by_role('button',name='성취 확인 검토 저장').click()
        expect(row.get_by_text('새 글 독립 확인',exact=False).first).to_be_visible()
        record=api(ctx,'/learning/course')['course']
        assert record['plan']['attainment']['successes']==1
        assert record['plan']['checks'][0]['feedback']['explanation']==key['explanation']
        page.reload()
        expect(page.locator('.course-journey').get_by_text('나의 4주 학습 계획',exact=True)).to_be_visible()
        page.get_by_role('button',name='답안·의견 보기',exact=True).click()
        released=page.locator('.course-player .assessment-guide');released.locator('summary').click()
        expect(released.get_by_text(key['explanation'],exact=True).first).to_be_visible()
        page.screenshot(path=str(out/f'g{grade}-plan-mobile.png'),full_page=True)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        results.append({'grade':grade,'diagnosticCount':len(r['form']['questions']),'course':plan['course'],'sessions':8,'firstCheckPassed':True,'teacherGuideAndReleasedFeedback':True,'oralObserved':grade==1})
        ctx.close()
        print(f'Grade {grade} browser journey passed',flush=True)
    assert not errors,errors
    (out/'browser-verification.json').write_text(json.dumps({'passed':True,'grades':results,'browserErrors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
