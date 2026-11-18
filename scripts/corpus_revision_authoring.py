"""Explicitly authored revision records. No length padding or generated factual prose."""
from pathlib import Path
import json, hashlib, re

ROOT=Path(__file__).resolve().parents[1]
BASE=json.loads((ROOT/'data/curriculum_2022/revisions/baseline-v1.json').read_text(encoding='utf-8'))
ORIGINAL={p['id']:p for p in BASE['passages']}
STAGES=['직접 확인','정보 연결','추론','근거 판단','새 상황 적용']
ROWS=[]

def original(key):
    pid=key if key.startswith(('P22-','passage:')) else f'passage:{key}:001'
    return '\n'.join(re.sub(r'<[^>]+>','',p) for p in ORIGINAL[pid]['paragraphs']).replace('기록는','기록은')

def Q(prompt, answer, refs, quote):
    return dict(prompt=prompt, answer=answer, refs=[refs] if isinstance(refs,int) else refs, quote=quote)

def add(key,title,core,standard,challenge,questions,application,vocabulary,review,sources=None):
    pid=key if key.startswith(('P22-','passage:')) else f'passage:{key}:001'
    old=ORIGINAL[pid]
    paras=[p.strip() for p in core.strip().split('\n') if p.strip()]
    expanded=[p.strip() for p in standard.strip().split('\n') if p.strip()]
    advanced=[p.strip() for p in challenge.strip().split('\n') if p.strip()]
    assert len(questions)==4 and expanded and advanced
    def ref(n): return f'{pid}:v2:p{n}'
    tasks=[]
    for i,q in enumerate(questions):
        assert all(1<=n<=len(paras) for n in q['refs']), (pid,q)
        assert any(q['quote'] in paras[n-1] for n in q['refs']), (pid,q['quote'])
        tasks.append(dict(id=f'{pid}:v2:q{i+1}',skill=STAGES[i],responseKind='explanation',prompt=q['prompt'],
            options=[],answer=-1,evidence=[ref(n) for n in q['refs']],explanation=q['answer'],optionReasons=[],
            hints=[f"질문에서 '{q['prompt']}'에 답하는 데 필요한 조건을 찾아요.",
                   f"{'·'.join(map(str,q['refs']))}문단을 이어 읽고, 질문의 조건과 맞추어 보세요.",
                   f"‘{q['quote']}’라는 단서로 무엇을 알 수 있고 무엇은 아직 알 수 없을까요?"],
            rubric=[q['answer'],'본문의 필요한 근거와 설명이 연결되는지 교사가 검토합니다.'],anchor=q['quote']))
    scenario,prompt,options,refs,explanation,reasons=application
    assert len(options)==(3 if old['grade']<=2 else 4 if old['grade']<=4 else 5)
    assert len(reasons)==len(options)
    # Rotate the authored correct-first options deterministically; answer positions are balanced.
    position=len(ROWS)%len(options)
    rotated=options[-position:]+options[:-position] if position else options
    why=reasons[-position:]+reasons[:-position] if position else reasons
    tasks.append(dict(id=f'{pid}:v2:q5',skill=STAGES[4],prompt=prompt,scenario=scenario,options=rotated,answer=position,
        evidence=[ref(n) for n in refs],hints=['보기에서 달라진 조건을 먼저 표시해요.',f"{'·'.join(map(str,refs))}문단의 원리와 보기의 조건을 짝지어요.",'선택지가 조건 하나를 빠뜨리거나 글에 없는 결론까지 말하지 않았는지 살펴요.'],
        explanation=explanation,optionReasons=why))
    model=[]
    for i in range(2):
        q=questions[i]; n=next(n for n in q['refs'] if q['quote'] in paras[n-1])
        model.append(dict(paragraph=ref(n),quote=q['quote'],kind='target' if i==0 else 'evidence',
            thought=(f"먼저 질문을 읽어 볼게. ‘{q['prompt']}’ 단서는 여기야. ‘{q['quote']}’에 표시했어. {q['answer']}" if i==0 else
                     f"이제 ‘{q['quote']}’를 앞에서 찾은 내용과 이어 보자. {q['answer']}")))
    q=questions[1]; n=next(n for n in q['refs'] if q['quote'] in paras[n-1])
    model.append(dict(paragraph=ref(n),quote=q['quote'],kind='link',thought=f"내 설명이 근거에 맞는지 돌아볼게. {q['answer']} 표시한 말에 없는 조건을 보태지는 않았는지도 확인하자."))
    numbered=[dict(id=ref(i+1),text=t) for i,t in enumerate(paras+expanded+advanced)]
    row=dict(id=f'corpus-v2:{pid}',sourcePassageId=pid,sourceVersion=old['version'],version=2,grade=old['grade'],
        title=title,concept=old['subject']+' · '+(' / '.join(old.get('conceptNames',[]))),goalIds=old['goalIds'],
        layers=dict(supported=numbered[:len(paras)],standard=numbered[len(paras):len(paras)+len(expanded)],challenge=numbered[len(paras)+len(expanded):]),
        vocabulary=[dict(word=w,meaning=d) for w,d in vocabulary],model=model,questions=tasks,
        editorialReview=dict(baselineHash=old['contentHash'],changes=review,reviewer='AI 집필·검토',independentReviewer=False,
            factualSources=sources or [],teacherReview='pending',studentCalibration='pending',
            levelDesign='도움글: 핵심 개념과 관계. 기준글: 사례·비교 보강. 도전글: 예외·조건·판단 범위 확장. 같은 문항에 대한 도움을 별도로 기록.'))
    ROWS.append(row)

def save(grade):
    rows=[r for r in ROWS if r['grade']==grade]
    from revision_enrichment import enrich
    enrich(rows)
    expected={p['id'] for p in BASE['passages'] if p['grade']==grade}
    assert {r['sourcePassageId'] for r in rows}==expected,expected-{r['sourcePassageId'] for r in rows}
    path=ROOT/f'data/curriculum_2022/revisions/grade-{grade}.json'
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Grade {grade}: {len(rows)} passages / {len(rows)*5} tasks authored')
