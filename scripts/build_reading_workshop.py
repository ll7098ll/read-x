"""Offline review workbook for the authored reading lessons, without automatic diagnosis."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/01a138a0-43ff-7451-bf36-fcef9c677ac6'
rows=json.loads((ROOT/'data/curriculum_2022/passage_drafts_batch_02.json').read_text(encoding='utf-8'))
template=Path(__file__).with_name('reading_workshop_template.html').read_text(encoding='utf-8')
data=json.dumps(rows,ensure_ascii=False).replace('</','<\\/')
(OUT/'reading-workshop-batch-02.html').write_text(template.replace('__LESSON_DATA__',data),encoding='utf-8')
print(f'Workshop: {len(rows)} passages, {sum(len(p["diagnostic"]["items"]) for p in rows)} diagnostic items')
