# -*- coding: utf-8 -*-
"""
1단원: 시 (Poetry, unit1_poetry) — 전 16차시 통합 JSON 저장 및 HTML 조판 실행 스크립트
"""

import os
import sys
import json
import re

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from data.units.unit1_poetry.batch1_v1 import BATCH1
from data.units.unit1_poetry.batch2_v2 import BATCH2
from data.units.unit1_poetry.batch3_v3 import BATCH3
from data.units.unit1_poetry.batch4_w import BATCH4
from scripts.html_builder import build_unit_html_files

REQUIRED_KEYS = [
    "lesson_title",
    "std_badge",
    "student_goal",
    "marking_items",
    "left_page_body_html",
    "activity_1",
    "arrow_1_to_2",
    "activity_2",
    "arrow_2_to_3",
    "activity_3",
    "writing_seed",
    "self_check",
    "teacher_guide",
]


def validate_lessons(lessons):
    assert len(lessons) == 16, f"Expected 16 lessons, got {len(lessons)}"
    for idx, lesson in enumerate(lessons, start=1):
        for k in REQUIRED_KEYS:
            assert k in lesson and lesson[k], f"Lesson {idx} missing key: {k}"
        # Check .t-ans inside blank-slot and pencil-line
        combined_html = (
            lesson["left_page_body_html"]
            + lesson["activity_1"].get("body_html", "")
            + lesson["activity_2"].get("body_html", "")
            + lesson["activity_3"].get("body_html", "")
        )
        blank_slots = re.findall(r'<span class="blank-slot"[^>]*>(.*?)</span>\s*</span>', combined_html, flags=re.DOTALL)
        assert '<span class="t-ans">' in combined_html, f"Lesson {idx} has no .t-ans tags!"
        tg = lesson["teacher_guide"]
        for tgk in [
            "board_plan_summary",
            "intro_5min",
            "ido_think_aloud_script",
            "wedo_qa_list",
            "youdo_and_wrapup",
            "answer_key_html",
            "misconceptions",
            "scaffolding_down",
            "scaffolding_up",
            "rubric",
        ]:
            assert tgk in tg and tg[tgk], f"Lesson {idx} teacher_guide missing key: {tgk}"
    print("[OK] All 16 lessons passed schema and .t-ans validation!")


def main():
    os.chdir(ROOT_DIR)
    lessons = BATCH1 + BATCH2 + BATCH3 + BATCH4
    validate_lessons(lessons)

    json_path = os.path.join("data", "units", "unit1_poetry", "lessons_all.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved 16 lessons to {json_path} ({os.path.getsize(json_path):,} bytes)")

    student_path, teacher_path = build_unit_html_files("시", lessons, out_dir="output")
    print(f"[OK] Built Student Textbook HTML: {student_path} ({os.path.getsize(student_path):,} bytes)")
    print(f"[OK] Built Teacher Guide HTML:    {teacher_path} ({os.path.getsize(teacher_path):,} bytes)")


if __name__ == "__main__":
    main()
