# -*- coding: utf-8 -*-
"""
4단원: 설명문 (unit4_expository) 통합 빌드 및 검증 스크립트
- BATCH1 (1~4차시: V1-1 ~ V1-4)
- BATCH2 (5~8차시: V2-1 ~ V2-4)
- BATCH3 (9~11차시: V3-1 ~ V3-3)
- BATCH4 (12~16차시: W1 ~ W5)
➔ data/units/unit4_expository/lessons_all.json 저장
➔ output/unit4_expository_student_textbook.html 및 output/unit4_expository_teacher_guide.html 생성
"""

import os
import sys
import json
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent
ROOT_DIR = CUR_DIR.parent.parent
for p in (str(CUR_DIR), str(ROOT_DIR)):
    if p not in sys.path:
        sys.path.insert(0, p)

os.chdir(str(ROOT_DIR))

from batch1_v1 import BATCH1
from batch2_v2 import BATCH2
from batch3_v3 import BATCH3
from batch4_w import BATCH4
from scripts.html_builder import build_unit_html_files


def main():
    lessons = BATCH1 + BATCH2 + BATCH3 + BATCH4
    assert len(lessons) == 16, f"Expected 16 lessons, got {len(lessons)}"

    # Verify codes & required keys
    for idx, item in enumerate(lessons):
        l_no = idx + 1
        assert item["lesson_no"] == l_no, f"Lesson number mismatch at index {idx}: {item['lesson_no']}"
        for req_key in [
            "lesson_title",
            "student_goal",
            "left_page_body_html",
            "activity_1",
            "activity_2",
            "activity_3",
            "writing_seed",
            "self_check",
            "teacher_guide",
        ]:
            assert req_key in item and item[req_key], f"Missing required key {req_key} in lesson {l_no}"

        # Verify teacher_guide 6 modules
        tg = item["teacher_guide"]
        for tg_key in [
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
            assert tg_key in tg and tg[tg_key], f"Missing teacher_guide key {tg_key} in lesson {l_no}"

    # Save lessons_all.json
    json_path = str(CUR_DIR / "lessons_all.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved 16 lessons to {json_path} ({os.path.getsize(json_path):,} bytes)")

    # Build HTML files
    student_html_path, teacher_html_path = build_unit_html_files("설명문", lessons, out_dir=str(ROOT_DIR / "output"))
    print(f"[OK] Generated Student Textbook HTML: {student_html_path} ({os.path.getsize(student_html_path):,} bytes)")
    print(f"[OK] Generated Teacher Guide HTML:    {teacher_html_path} ({os.path.getsize(teacher_html_path):,} bytes)")

    # Count .t-ans occurrences in student HTML
    with open(student_html_path, "r", encoding="utf-8") as f:
        s_content = f.read()
    t_ans_count = s_content.count('class="t-ans"')
    spread_count = s_content.count('class="spread-wrapper"')
    print(f"[VERIFY] Student spreads: {spread_count} (32 pages: p.97~128), .t-ans tags: {t_ans_count}")


if __name__ == "__main__":
    main()
