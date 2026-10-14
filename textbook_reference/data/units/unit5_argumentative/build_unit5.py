# -*- coding: utf-8 -*-
"""
5단원 논설문 (unit5_argumentative) 16차시 통합 빌드 및 검증 스크립트
"""

import os
import sys
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from data.units.unit5_argumentative.batch1_v1 import BATCH1
from data.units.unit5_argumentative.batch2_v2 import BATCH2
from data.units.unit5_argumentative.batch3_v3 import BATCH3
from data.units.unit5_argumentative.batch4_w import BATCH4
from scripts.html_builder import build_unit_html_files


def main():
    os.chdir(ROOT_DIR)
    lessons = BATCH1 + BATCH2 + BATCH3 + BATCH4
    assert len(lessons) == 16, f"Expected 16 lessons, got {len(lessons)}"

    # JSON 저장
    json_path = os.path.join("data", "units", "unit5_argumentative", "lessons_all.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved {json_path} ({len(lessons)} lessons, {os.path.getsize(json_path):,} bytes)")

    # HTML 2종 빌드
    student_path, teacher_path = build_unit_html_files("논설문", lessons)
    print(f"[OK] Built Student Textbook: {student_path} ({os.path.getsize(student_path):,} bytes)")
    print(f"[OK] Built Teacher Guide:    {teacher_path} ({os.path.getsize(teacher_path):,} bytes)")

    # 무결성 검증
    with open(student_path, encoding="utf-8") as f:
        s_html = f.read()
    with open(teacher_path, encoding="utf-8") as f:
        t_html = f.read()

    t_ans_count = s_html.count('class="t-ans"') + s_html.count('class="t-ans-block"')
    spread_count_s = s_html.count('class="spread-wrapper"')
    spread_count_t = t_html.count('class="spread-wrapper"')
    page_count_s = s_html.count('class="page ')
    page_count_t = t_html.count('class="page ')

    print(f"[VERIFY] Student spreads: {spread_count_s} (pages: {page_count_s}), .t-ans tags: {t_ans_count}")
    print(f"[VERIFY] Teacher spreads: {spread_count_t} (pages: {page_count_t})")


if __name__ == "__main__":
    main()
