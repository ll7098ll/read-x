"""Build a self-contained, offline editorial workbook with local response capture."""
from pathlib import Path
import json, html

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/content_authoring/batch_03/units.json').read_text(encoding='utf-8'))
template=Path(__file__).with_name('diverse_batch_03_preview.html').read_text(encoding='utf-8')
out=ROOT/'output/content-batch-03'
out.mkdir(parents=True,exist_ok=True)
(out/'콘텐츠_검토_문제집.html').write_text(template.replace('__CONTENT__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
lines=['# 다양한 주제 읽기와 쓰기 문제집','', '초1~6 각 4묶음 · 자체 창작 · 교사 검토 대기','',
       'A는 수업 자료, B는 독립 확인, C는 전이 확인이며 도전 자료는 A와 같은 계열입니다. 아래에는 정답과 검토 자료도 함께 포함되어 있습니다.','']
for u in data['units']:
    lines.extend([f"## 초{u['grade']} {u['title']}",'',f"영역: {u['subject']} / 장르: {u['genre']} / 참고 목표: {u['goalId']}",''])
    groups=[('A 기본 자료',u['material'],u['questions']),('도전 조건',u['challenge']['material'],[u['challenge']['question']])]+[(('B 독립 확인' if i==0 else 'C 전이 확인'),c['material'],[c['question']]) for i,c in enumerate(u['checks'])]
    for label,m,questions in groups:
        lines.extend([f'### {label}',''])
        paras=m['paragraphs'][-1:] if label=='도전 조건' else m['paragraphs']
        for p in paras:lines.extend([p['text'],''])
        for t in m.get('tables',[]):
            lines.extend(['| '+' | '.join(t['headers'])+' |','| '+' | '.join(['---']*len(t['headers']))+' |'])
            lines.extend('| '+' | '.join(map(str,row))+' |' for row in t['rows'])
            lines.append('')
        for q in questions:
            lines.extend([f"**{q['id']} {q['prompt']}**",''])
            if q['kind']=='single_choice':
                for i,o in enumerate(q['options']):lines.append(f"{i+1}. {o['text']}")
                lines.extend(['',f"정답: {q['correctIndex']+1}",q['explanation'],''])
                for i,o in enumerate(q['options']):lines.append(f"- {i+1}번: {o['reason']}")
            else:
                if q.get('items'):lines.extend([f"- {i+1}: {v}" for i,v in enumerate(q['items'])])
                lines.extend(['',f"예시 답: {q['expectedAnswer']}",''])
                for r in q['rubric']:lines.append(f"- 준거: {r['criterion']} / 0: {r['levels']['0']} / 1: {r['levels']['1']} / 2: {r['levels']['2']}")
            lines.extend(['']+[f"- 근거: {e['sentenceId']} · {e['quote']}" for e in q['evidence']]+[''])
    lines.extend(['### 시범과 보충','',u['model'][0]['thought'],'',u['clinic']['prompt'],'',f"보충 예시 답: {u['clinic']['expectedAnswer']}",''])
(out/'전체_콘텐츠와_해설.md').write_text('\n'.join(lines),encoding='utf-8')
print(out/'콘텐츠_검토_문제집.html')
