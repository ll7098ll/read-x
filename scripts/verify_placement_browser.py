"""Isolated browser QA against scripts/preview-product-ui.mjs (synthetic accounts only)."""
import json
import subprocess
import time
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

root = Path(__file__).resolve().parents[1]
out = root / 'output' / 'placement-journey'
out.mkdir(parents=True, exist_ok=True)
origin = 'http://127.0.0.1:5194'
forms = json.loads(subprocess.check_output(['node', '--input-type=module', '-e', "import {placementForm} from './webapp/server/placement-content.mjs'; console.log(JSON.stringify([placementForm(3),placementForm(3,'extend'),placementForm(3,'support')]))"], cwd=root, text=True, encoding='utf-8'))
def api(context, path, body=None):
    response = context.request.get(origin+'/api/exam'+path) if body is None else context.request.post(origin+'/api/exam'+path, data=body, headers={'Origin':origin})
    assert response.ok, (path, response.status, response.text())
    return response.json()
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    teacher=browser.new_context(viewport={'width':1280,'height':900})
    api(teacher,'/login',{'username':'ui-teacher','password':'Preview-Only-2026!'})
    username='placement-'+str(int(time.time()*1000))
    api(teacher,'/roster',{'student':{'name':'배치 검증 학생','username':username,'password':'Preview-Only-2026!'}})
    student = browser.new_context(viewport={'width':1280,'height':900})
    api(student,'/login',{'username':username,'password':'Preview-Only-2026!'})
    page = student.new_page()
    errors=[]
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto(origin+'/#/student/classes')
    expect(page.get_by_role('heading',name='내게 맞는 시작점을 찾아요')).to_be_visible()
    page.get_by_role('radio',name='연필',exact=True).check()
    page.get_by_role('button',name='시작 진단',exact=True).click()
    expect(page.get_by_role('button',name='이 답 저장',exact=True)).to_be_visible()
    page.get_by_role('radio').first.check()
    page.get_by_role('button',name='이 답 저장',exact=True).click()
    expect(page.get_by_text('서버에 저장된 답이에요.',exact=True)).to_be_visible()
    page.screenshot(path=str(out/'diagnostic-desktop.png'),full_page=True)
    page.set_viewport_size({'width':390,'height':844})
    page.screenshot(path=str(out/'diagnostic-mobile.png'),full_page=True)
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.reload()
    expect(page.get_by_role('button',name='이 답 저장',exact=True)).to_be_visible()
    r=api(student,'/learning/placement')['placement']
    def fill(r):
        full=next(f for f in forms if f['branch']==r['branch'])
        for q in full['questions']:
            if q['id'] in r['answers']: continue
            answer={'choice':q['answer']} if q['options'] else {'text':'비 때문에 길을 돌아가므로 평소보다 일찍 출발했습니다.','evidence':q['evidence']}
            r=api(student,'/learning/placement/answer',{'revision':r['revision'],'questionId':q['id'],**answer})['placement']
        return r
    r=fill(r)
    page.reload()
    page.get_by_role('button',name='추가 진단으로',exact=True).click()
    expect(page.get_by_text('추가 진단',exact=False).first).to_be_visible()
    r=fill(api(student,'/learning/placement')['placement'])
    page.reload()
    page.get_by_role('button',name='진단 제출하고 코스 추천받기').click()
    expect(page.get_by_text('선생님이 자기 설명과 추천 코스를 확인하고 첫 수업을 준비하고 있어요.')).to_be_visible()
    tp=teacher.new_page()
    tp.on('pageerror',lambda error:errors.append(str(error)))
    tp.goto(origin+'/#/teacher/classes')
    tp.get_by_label('진단 학생',exact=True).select_option(r['studentId'])
    tp.get_by_label('자기 설명 1 검토').select_option('success')
    tp.get_by_label('자기 설명 2 검토').select_option('success')
    tp.get_by_label('첫 수업',exact=True).select_option(index=1)
    expect(tp.get_by_text('첫 수업 본문·시범·문항 검토',exact=True)).to_be_visible()
    tp.get_by_label('배치 이유와 첫 2회 확인할 것').fill('근거를 연결하는 설명을 첫 두 수업에서 확인합니다.')
    tp.get_by_role('checkbox',name='본문·문항·근거와 학년 적합성을 검토했고 시범 수업을 승인합니다.').check()
    tp.screenshot(path=str(out/'teacher-placement.png'),full_page=True)
    tp.get_by_role('button',name='배치 확정하고 첫 수업 배정',exact=True).click()
    expect(tp.get_by_text('첫 수업이 배정됐습니다. 수업 목록에서 수행을 확인하세요.')).to_be_visible()
    page.get_by_role('button',name='배치 결과 확인하기').click()
    page.get_by_role('button',name='첫 수업 시작·이어 하기 →',exact=True).click()
    page.get_by_role('button',name='시범 따라가기',exact=True).click()
    expect(page.get_by_role('heading',name='표시한 까닭을 따라 말해 봐요.',exact=True)).to_be_visible()
    page.screenshot(path=str(out/'first-lesson-mobile.png'),full_page=True)
    assert not errors, errors
    (out/'verification.json').write_text(json.dumps({'passed':True,'browserErrors':errors,'scenarios':['practice','save','reload','branch','submit','teacher review','course placement','first lesson'],'screenshots':4},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
print('Placement browser journey passed')




