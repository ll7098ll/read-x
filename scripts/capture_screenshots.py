# -*- coding: utf-8 -*-
"""
Playwright + PIL 기반 교과서 & 교사용 지도서 고해상도(2x Retina) 실제 화면 캡쳐 스크립트
"""

import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("github_upload_package/assets/screenshots")
OUT_DIR.mkdir(parents=True, exist_ok=True)
BASE_OUTPUT = Path("output").resolve()
SAMPLES_DIR = Path("samples").resolve()


def file_url(path_obj: Path) -> str:
    return path_obj.resolve().as_uri()


def capture_spread(page, html_path: Path, spread_id: str, save_name: str, show_answers: bool = False):
    url = file_url(html_path)
    page.goto(url, wait_until="networkidle")
    page.evaluate("() => document.fonts.ready")
    if show_answers:
        page.evaluate("""() => {
            if (!document.body.classList.contains('show-answers')) {
                toggleAnswerKey();
            }
        }""")
    else:
        page.evaluate("""() => {
            if (document.body.classList.contains('show-answers')) {
                toggleAnswerKey();
            }
        }""")

    if spread_id:
        page.evaluate(f"() => filterSpread('{spread_id}', null)")
        time.sleep(0.25)
        loc = page.locator(f"#{spread_id}")
        out_file = OUT_DIR / save_name
        loc.screenshot(path=str(out_file))
    else:
        time.sleep(0.25)
        out_file = OUT_DIR / save_name
        page.screenshot(path=str(out_file), full_page=False)
    print(f"[CAPTURED] {save_name} ({out_file.stat().st_size:,} bytes)")


def create_hero_composite():
    """대표 캡쳐 이미지들을 조합하여 GitHub 상단 히어로 쇼케이스 배너 생성."""
    img_names = [
        "02_unit1_poetry_spread.png",
        "05_unit2_narrative_spread.png",
        "07_unit3_essay_spread.png",
        "08_unit4_expository_spread.png",
        "10_unit5_argumentative_spread.png",
        "12_teacher_guide_poetry.png",
    ]
    loaded = []
    for n in img_names:
        p = OUT_DIR / n
        if p.exists():
            loaded.append(Image.open(p).convert("RGB"))
    if len(loaded) < 6:
        return

    # 3x2 그리드 캔버스 (2400 x 1420)
    cw, ch = 2400, 1420
    canvas = Image.new("RGB", (cw, ch), (22, 31, 36))
    draw = ImageDraw.Draw(canvas)

    # 상단 바 장식
    draw.rectangle([0, 0, cw, 16], fill=(243, 156, 18))

    cell_w, cell_h = 760, 640
    positions = [
        (30, 45), (820, 45), (1610, 45),
        (30, 735), (820, 735), (1610, 735),
    ]
    border_colors = [
        (142, 68, 173),   # 1단원 시 (퍼플)
        (200, 90, 23),    # 2단원 이야기 (오렌지)
        (30, 132, 73),    # 3단원 수필 (그린)
        (26, 82, 118),    # 4단원 설명문 (블루)
        (146, 43, 33),    # 5단원 논설문 (레드)
        (243, 156, 18),   # 교사용 지도서 (골드)
    ]

    for idx, im in enumerate(loaded):
        x, y = positions[idx]
        # 비율 유지 리사이즈 후 중앙 크롭/패딩
        im_copy = im.copy()
        im_copy.thumbnail((cell_w - 8, cell_h - 8), Image.Resampling.LANCZOS)
        bg_card = Image.new("RGB", (cell_w, cell_h), border_colors[idx])
        inner = Image.new("RGB", (cell_w - 8, cell_h - 8), (30, 39, 46))
        ox = (cell_w - 8 - im_copy.width) // 2
        oy = (cell_h - 8 - im_copy.height) // 2
        inner.paste(im_copy, (ox, oy))
        bg_card.paste(inner, (4, 4))
        canvas.paste(bg_card, (x, y))

    hero_path = OUT_DIR / "00_hero_banner_composite.png"
    canvas.save(hero_path, format="PNG", optimize=True)
    print(f"[CAPTURED] 00_hero_banner_composite.png ({hero_path.stat().st_size:,} bytes)")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        context = browser.new_context(viewport={"width": 1560, "height": 1180}, device_scale_factor=2)
        page = context.new_page()

        # 1. 마스터 포털 (index.html)
        page.goto(file_url(BASE_OUTPUT / "index.html"), wait_until="networkidle")
        page.evaluate("() => document.fonts.ready")
        time.sleep(0.3)
        p1 = OUT_DIR / "01_master_portal_overview.png"
        page.screenshot(path=str(p1), full_page=False)
        print(f"[CAPTURED] 01_master_portal_overview.png ({p1.stat().st_size:,} bytes)")

        # 2. 1단원 시 (학생용 1차시 구부러진 길 펼침면)
        capture_spread(page, BASE_OUTPUT / "unit1_poetry_student_textbook.html", "u1-l1", "02_unit1_poetry_spread.png", show_answers=False)

        # 3. 1단원 시 (교사용 정답 오버레이 ON 상태 — 5차시 봄길 추론)
        capture_spread(page, BASE_OUTPUT / "unit1_poetry_student_textbook.html", "u1-l5", "03_unit1_poetry_answer_on.png", show_answers=True)

        # 4. 1단원 시 (16차시 W5 2층 시어 조탁 노트 & 교정부호)
        capture_spread(page, BASE_OUTPUT / "unit1_poetry_student_textbook.html", "u1-l16", "04_unit1_poetry_writing.png", show_answers=True)

        # 5. 2단원 이야기 (3차시 꼴뚜기 역순행 구성 & 이야기 산 도해조직자)
        capture_spread(page, BASE_OUTPUT / "unit2_narrative_student_textbook.html", "u2-l3", "05_unit2_narrative_spread.png", show_answers=False)

        # 6. 2단원 이야기 (10차시 V3-2 4인 교실 모의 법정 양팔 저울 & 판결문)
        capture_spread(page, BASE_OUTPUT / "unit2_narrative_student_textbook.html", "u2-l10", "06_unit2_narrative_mock_trial.png", show_answers=True)

        # 7. 3단원 수필 (5차시 V2-1 법정 무소유 & 장영희 괜찮아 오브제·관용표현 추론)
        capture_spread(page, BASE_OUTPUT / "unit3_essay_student_textbook.html", "u3-l5", "07_unit3_essay_spread.png", show_answers=False)

        # 8. 4단원 설명문 (3차시 V1-3 북극과 남극 비교·대조 & 기후 연쇄 인과 도미노)
        capture_spread(page, BASE_OUTPUT / "unit4_expository_student_textbook.html", "u4-l3", "08_unit4_expository_spread.png", show_answers=False)

        # 9. 4단원 설명문 (11차시 V3-3 스마트 팜 3종 다중매체 교차검증 & 코넬식 독립읽기)
        capture_spread(page, BASE_OUTPUT / "unit4_expository_student_textbook.html", "u4-l11", "09_unit4_expository_multimedia.png", show_answers=True)

        # 10. 5단원 논설문 (3차시 V1-3 자율선택급식 파르테논 3단 논증 구조 도해)
        capture_spread(page, BASE_OUTPUT / "unit5_argumentative_student_textbook.html", "u5-l3", "10_unit5_argumentative_spread.png", show_answers=False)

        # 11. 5단원 논설문 (11차시 V3-3 Y축 절단 그래프 왜곡 팩트체크 & 생성형 AI 저작권 판례 토론)
        capture_spread(page, BASE_OUTPUT / "unit5_argumentative_student_textbook.html", "u5-l11", "11_unit5_factcheck_ai_debate.png", show_answers=True)

        # 12. 교사용 지도서 — 1단원 시 (1차시 6대 모듈)
        capture_spread(page, BASE_OUTPUT / "unit1_poetry_teacher_guide.html", "tg-u1-l1", "12_teacher_guide_poetry.png", show_answers=True)

        # 13. 교사용 지도서 — 2단원 이야기 (10차시 모의법정 지도안)
        capture_spread(page, BASE_OUTPUT / "unit2_narrative_teacher_guide.html", "tg-u2-l10", "13_teacher_guide_narrative.png", show_answers=True)

        # 14. 교사용 지도서 — 5단원 논설문 (11차시 통계왜곡·AI토론 지도안)
        capture_spread(page, BASE_OUTPUT / "unit5_argumentative_teacher_guide.html", "tg-u5-l11", "14_teacher_guide_argumentative.png", show_answers=True)

        # 15. 레이아웃 카탈로그 13종 샘플북 (samples/sample_textbook_layout_preview.html)
        sample_html = SAMPLES_DIR / "sample_textbook_layout_preview.html"
        if sample_html.exists():
            page.goto(file_url(sample_html), wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.evaluate("() => filterSpread('sp-8', null)")
            time.sleep(0.25)
            p15 = OUT_DIR / "15_layout_catalog_13types.png"
            page.locator("#sp-8").screenshot(path=str(p15))
            print(f"[CAPTURED] 15_layout_catalog_13types.png ({p15.stat().st_size:,} bytes)")

        browser.close()

    create_hero_composite()


if __name__ == "__main__":
    main()
