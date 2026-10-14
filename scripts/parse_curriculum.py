import sys
import os
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

CURR_PATH = os.path.join('courseware', 'research', 'courseware_track1_curriculum_concepts_96slots.md')

with open(CURR_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()

slots_found = []
for idx, line in enumerate(lines):
    m = re.search(r'`([1-6])-설명-([^`]+)`', line)
    if m:
        grade = int(m.group(1))
        code = m.group(2)
        cols = [c.strip() for c in line.split('|')[1:-1]]
        title_concept = cols[3] if len(cols) > 3 else ''
        if not title_concept:
            continue
        slots_found.append({
            'grade': grade,
            'code': code,
            'slot_id': f"G{grade}-EXP-{code}",
            'subskill_req': cols[1] if len(cols) > 1 else '',
            'subject_unit': cols[2] if len(cols) > 2 else '',
            'title_concept': title_concept,
            'structure': cols[4] if len(cols) > 4 else '',
            'visual_spec': cols[5] if len(cols) > 5 else '',
            'task_point': cols[6] if len(cols) > 6 else ''
        })

print(f"Total matched valid slots: {len(slots_found)}")
by_grade = {}
for s in slots_found:
    by_grade.setdefault(s['grade'], []).append(s)

for g, items in by_grade.items():
    print(f"Grade {g}: {len(items)} slots -> {[x['code'] for x in items]}")

OUT_PATH = os.path.join('courseware', 'data', 'parsed_96_curriculum_specs.json')
with open(OUT_PATH, 'w', encoding='utf-8') as f:
    json.dump(slots_found, f, ensure_ascii=False, indent=2)
print(f"Saved parsed specs to {OUT_PATH}")
