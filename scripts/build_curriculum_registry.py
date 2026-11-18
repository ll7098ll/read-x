from pathlib import Path
import collections, json, re

ROOT = Path(__file__).resolve().parents[1]
EXTRACTED = ROOT / 'research/curriculum_2022/extracted'
OUT = ROOT / 'data/curriculum_2022'
manifest = json.loads((EXTRACTED / 'source_manifest.json').read_text(encoding='utf-8'))
SUBJECTS = {'국':'국어','도':'도덕','사':'사회','수':'수학','과':'과학','실':'실과','체':'체육','음':'음악','미':'미술','영':'영어','바':'바른 생활','슬':'슬기로운 생활','즐':'즐거운 생활'}
pattern = re.compile(r'^\[([246])('+'|'.join(SUBJECTS)+r')(\d{2})[-–−‐‑](\d{2})\]\s*(.+)$')
standards = {}
for source in sorted(manifest, key=lambda s:s['annex']):
    area = ''
    for line_no, line in enumerate((EXTRACTED / f"annex_{source['annex']:02}.txt").read_text(encoding='utf-8').splitlines(), 1):
        h = re.match(r'^\(\d+\)\s*(.*)', line)
        if h: area = h[1]
        m = pattern.match(line)
        if not m: continue
        code = f'{m[1]}{m[2]}{m[3]}-{m[4]}'
        if code in standards:
            standards[code]['explanatoryOccurrences'].append({'text':m[5], 'line':line_no})
            continue
        standards[code] = {'id':code, 'subject':SUBJECTS[m[2]], 'gradeBand':[int(m[1])-1,int(m[1])],
            'area':area,'statement':m[5], 'sourceId':source['sourceId'], 'sourceLine':line_no,
            'sourcePath':f"research/curriculum_2022/extracted/annex_{source['annex']:02}.txt",
            'noticeVersion':'2022-33', 'explanatoryOccurrences':[],
            'semester':None, 'semesterBasis':'국가 교육과정은 학년군 기준. 학기별 교과서 배치 별도 연결.'}
rows = list(standards.values())
assert not [s['id'] for s in rows if re.match(r'^(은|는|을|를)\s',s['statement'])], 'Explanatory prose must not replace a standard.'
(OUT / 'achievement_standards.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
groups = collections.defaultdict(list)
for row in rows: groups[(row['subject'],tuple(row['gradeBand']),row['area'])].append(row)
lines = []
for (subject, band, area), items in groups.items():
    lines.append(f"{subject} {band[0]}~{band[1]} / {area} / {items[0]['id']}~{items[-1]['id']} ({len(items)})")
    lines.extend(f"  {s['id']} {s['statement']}" for s in items)
(EXTRACTED / 'elementary_standards.txt').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'total':len(rows),'subjects':dict(collections.Counter(s['subject'] for s in rows))},ensure_ascii=False))
