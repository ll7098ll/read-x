# -*- coding: utf-8 -*-
"""
2단원: 이야기 (Narrative, unit2_narrative) 통합 빌드 및 검증 스크립트
- Batch 1~4 (총 16차시) 결합 ➔ data/units/unit2_narrative/lessons_all.json 저장
- scripts.html_builder.build_unit_html_files('이야기', lessons) 호출하여
  output/unit2_narrative_student_textbook.html 및 output/unit2_narrative_teacher_guide.html 생성
"""

import os
import sys
import json

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from data.units.unit2_narrative.batch1_v1 import BATCH1
from data.units.unit2_narrative.batch2_v2 import BATCH2
from data.units.unit2_narrative.batch3_v3 import BATCH3
from data.units.unit2_narrative.batch4_w import BATCH4
from scripts.html_builder import build_unit_html_files


def main():
    os.chdir(ROOT_DIR)
    lessons = BATCH1 + BATCH2 + BATCH3 + BATCH4
    assert len(lessons) == 16, f"Expected 16 lessons, got {len(lessons)}"

    json_path = os.path.join("data", "units", "unit2_narrative", "lessons_all.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f"[OK] Saved 16 lessons JSON -> {json_path} ({os.path.getsize(json_path):,} bytes)")

    student_path, teacher_path = build_unit_html_files("이야기", lessons, out_dir="output")
    print(f"[OK] Generated Student Textbook HTML -> {student_path} ({os.path.getsize(student_path):,} bytes)")
    print(f"[OK] Generated Teacher Guide HTML    -> {teacher_path} ({os.path.getsize(teacher_path):,} bytes)")

    # 품질 검증
    total_t_ans = 0
    for idx, l in enumerate(lessons, 1):
        s_blob = json.dumps(l, ensure_ascii=False)
        cnt = s_blob.count("t-ans")
        total_t_ans += cnt
        tg = l.get("teacher_guide", {})
        assert tg.get("board_plan_summary"), f"Lesson {idx} missing board_plan_summary"
        assert tg.get("ido_think_aloud_script"), f"Lesson {idx} missing ido_think_aloud_script"
        assert len(tg.get("wedo_qa_list", [])) >= 2, f"Lesson {idx} needs >=2 QAR items"
        assert len(tg.get("misconceptions", [])) >= 2, f"Lesson {idx} needs >=2 misconceptions"
        assert tg.get("rubric", {}).get("high"), f"Lesson {idx} missing rubric"
        print(f"  - Lesson {idx:02d} ({l['lesson_title'][:24]}...): .t-ans count = {cnt}, TG modules = PASS")

    print(f"[VERIFIED] Total .t-ans answer overlays across 16 lessons = {total_t_ans}")


if __name__ == "__main__":
    main()
