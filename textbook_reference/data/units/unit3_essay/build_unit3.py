# -*- coding: utf-8 -*-
"""
3단원: 수필 (unit3_essay) 통합 빌드 및 검증 스크립트
- Batch 1~4 (총 16차시 · 32쪽) 데이터를 병합하여 `data/units/unit3_essay/lessons_all.json`에 저장
- `scripts.html_builder.build_unit_html_files('수필', lessons)`를 호출하여
  `output/unit3_essay_student_textbook.html` 및 `output/unit3_essay_teacher_guide.html` 생성
"""

import os
import sys
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from data.units.unit3_essay.batch1_v1 import BATCH1
from data.units.unit3_essay.batch2_v2 import BATCH2
from data.units.unit3_essay.batch3_v3 import BATCH3
from data.units.unit3_essay.batch4_w import BATCH4
from scripts.html_builder import build_unit_html_files


def main():
    lessons = BATCH1 + BATCH2 + BATCH3 + BATCH4
    assert len(lessons) == 16, f"Expected 16 lessons, got {len(lessons)}"

    # 검증: 차시 번호 및 필수 키 확인
    for idx, l_data in enumerate(lessons):
        expected_no = idx + 1
        assert l_data["lesson_no"] == expected_no, f"Lesson index mismatch at {expected_no}"
        for req_key in [
            "code",
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
            assert req_key in l_data and l_data[req_key], f"Missing {req_key} in lesson {expected_no}"

        # .t-ans 포함 여부 확인
        combined_student_html = (
            l_data["left_page_body_html"]
            + l_data["activity_1"].get("body_html", "")
            + l_data["activity_2"].get("body_html", "")
            + l_data["activity_3"].get("body_html", "")
        )
        assert 'class="t-ans"' in combined_student_html, f"Missing .t-ans in lesson {expected_no}"

        tg = l_data["teacher_guide"]
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
            assert tg_key in tg and tg[tg_key], f"Missing teacher_guide.{tg_key} in lesson {expected_no}"

    out_json_path = os.path.join(ROOT_DIR, "data", "units", "unit3_essay", "lessons_all.json")
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)

    student_html, teacher_html = build_unit_html_files("수필", lessons, out_dir=os.path.join(ROOT_DIR, "output"))
    print(f"[SUCCESS] Saved JSON: {out_json_path}")
    print(f"[SUCCESS] Student Textbook HTML: {student_html} ({os.path.getsize(student_html):,} bytes)")
    print(f"[SUCCESS] Teacher Guide HTML: {teacher_html} ({os.path.getsize(teacher_html):,} bytes)")


if __name__ == "__main__":
    main()
