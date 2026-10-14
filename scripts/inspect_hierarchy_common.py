import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(os.path.join('courseware', 'data', 'expository_courseware_hierarchy.json'), 'r', encoding='utf-8') as f:
    hierarchy = json.load(f)

common_by_grade = hierarchy.get('common_by_grade', {})
for grade_label, items in common_by_grade.items():
    print(f"[{grade_label}] ({len(items)} items)")
    for it in items:
        print(f"  {it.get('code')}: {it.get('sub_skill_name')} | {it.get('mager_reading', '')[:35]}")
