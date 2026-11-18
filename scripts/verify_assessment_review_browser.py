"""Verify generated local teaching artifacts; no user account or production data."""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

root=Path(__file__).resolve().parents[1]
out=root/'output'/'assessment-review-2026-11-17'
ledger=json.loads((out/'item-ledger.json').read_text(encoding='utf-8'))
with sync_playwright() as p:
    browser=p.chromium.launch(channel='msedge',headless=True)
    page=browser.new_page(viewport={'width':1280,'height':900})
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((out/'index.html').as_uri())
    for href in page.locator('a').evaluate_all('(links)=>links.map(a=>a.getAttribute("href"))'):
        assert (out/href).is_file(),href
    page.goto((out/'teacher-review.html').as_uri())
    expect(page.locator('main > article')).to_have_count(460)
    expect(page.locator('#count')).to_have_text('460과제')
    page.locator('#grade').select_option('2')
    expect(page.locator('main > article:not(.hidden)')).to_have_count(70)
    page.locator('#kind').select_option('check')
    page.locator('#skill').select_option('integrate')
    expect(page.locator('main > article:not(.hidden)')).to_have_count(8)
    page.locator('#search').fill('소개글 원문')
    expect(page.locator('main > article:not(.hidden)')).to_have_count(1)
    page.screenshot(path=str(out/'teacher-guide-desktop.png'),full_page=True)
    page.emulate_media(media='print')
    assert page.locator('main > article').evaluate_all('(nodes)=>nodes.filter(n=>getComputedStyle(n).display!=="none").length')==1
    page.emulate_media(media='screen')
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth')
    page.screenshot(path=str(out/'teacher-guide-mobile.png'),full_page=True)
    checked=[]
    for file in sorted(out.glob('student-*.html')):
        page.goto(file.as_uri())
        expect(page.locator('.key')).to_have_count(0)
        assert '정답·설명' not in page.locator('body').inner_text()
        if file.name.startswith('student-diagnostic-'):
            grade=int(file.name.split('-g')[1][0])
            expect(page.locator('h3')).to_have_count(14 if grade<=2 else 22)
        else:
            expect(page.locator('article')).to_have_count(8)
        assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),file.name
        checked.append(file.name)
    assert len(checked)==48
    page.goto((out/'student-check-g2-integrate.html').as_uri())
    page.screenshot(path=str(out/'student-check-mobile.png'),full_page=True)
    assert not errors,errors
    (out/'artifact-browser-verification.json').write_text(json.dumps({'passed':True,'teacherItems':460,'studentBooklets':len(checked),'filtersAndPrint':True,'mobileOverflow':False,'browserErrors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
    browser.close()
print('460 teacher entries and 48 student booklets passed browser verification')
