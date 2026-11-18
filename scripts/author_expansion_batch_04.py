"""48 individually authored units. Structural helpers never invent source facts."""
from pathlib import Path
from copy import deepcopy
import json,hashlib,re,importlib
import author_diverse_batch_03 as base
import diverse_batch_03_levels as level_tools
ROOT=Path(__file__).resolve().parents[1]
CHALLENGES=[]

def U(g,title,subject,genre,goal,text,mc,short,organizer,writing,new_b,new_c,challenge,model,vocab):
    # Reuse the established content contract, keeping every actual passage/question explicit.
    prompt,answer,quote,criteria=short
    base.add(g,title,subject,genre,goal,text.split('\n'),mc,short,organizer,writing,(mc[3],model),vocab,new_b,new_c,
             ('다음 답을 근거 문장으로 확인하고 빠진 정보를 한 가지 보완하세요: '+answer,answer))
    u=base.UNITS[-1]
    u['clinic']['prompt']=f'“{quote}”를 찾아, {prompt}'
    u['clinic']['expectedAnswer']=answer
    CHALLENGES.append(challenge)

def build():
    base.UNITS.clear();CHALLENGES.clear()
    for g in range(1,7):importlib.import_module(f'expansion_04_g{g}').author(U)
    units=json.loads(json.dumps(base.UNITS,ensure_ascii=False).replace('B03-','B04-'))
    def material(u,extra):
        m=deepcopy(u['material']);m['id']=u['id']+'-D';m['title']=u['title']+' · 도전'
        m['paragraphs'].append(dict(id='',text=extra))
        for i,p in enumerate(m['paragraphs']):p['id']=m['id']+f'-p{i+1}'
        m['charCount']=len(' '.join(p['text'] for p in m['paragraphs']))
        m['contentHash']=hashlib.sha256('\n'.join(p['text'] for p in m['paragraphs']).encode()).hexdigest()
        return m
    def evidence(m,q):
        p=next(p for p in m['paragraphs'] if q in p['text'])
        return dict(passageId=m['id'],version=1,sentenceId=p['id'],quote=q,start=p['text'].index(q))
    level_tools.SPECS=CHALLENGES
    level_tools.enrich(units,material,evidence)
    for u in units:
        mats=[u['material'],u['challenge']['material']]+[c['material'] for c in u['checks']]
        for m in mats:
            for i,p in enumerate(m['paragraphs']):
                p['id']=m['id']+f'-p{i+1}'
                p['sentences']=[dict(id=p['id']+f'-s{j+1}',text=s) for j,s in enumerate(re.split(r'(?<=[.!?])\s+',p['text']))]
        refs=[e for q in u['questions']+[u['challenge']['question']]+[c['question'] for c in u['checks']] for e in q['evidence']]+[m['evidence'] for m in u['model']]
        byid={m['id']:m for m in mats}
        for e in refs:
            found=[(p,s) for p in byid[e['passageId']]['paragraphs'] for s in p['sentences'] if e['quote'] in s['text']]
            assert len(found)==1,(u['id'],e['quote'])
            p,s=found[0];e.update(paragraphId=p['id'],sentenceId=s['id'],start=s['text'].index(e['quote']))
        for q in u['questions']+[u['challenge']['question']]+[c['question'] for c in u['checks']]:
            if q['kind']!='single_choice':q['acceptableResponses']='표현이 달라도 본문의 의미와 준거를 충족하면 수용. 단순 문자열 일치 채점 금지.'
        u['clinic']['triggerPolicy']='실제 응답의 근거 설명을 추가 확인한 뒤 교사가 배정'
    dest=ROOT/'data/content_authoring/batch_04';dest.mkdir(parents=True,exist_ok=True)
    doc=dict(schemaVersion='readx-authoring-1',batch='04',authoredAt='2026-11-14',units=units)
    (dest/'units.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2),encoding='utf-8')
    previous=json.loads((ROOT/'data/content_authoring/batch_03/units.json').read_text(encoding='utf-8'))['units']
    combined={**doc,'batch':'03-04','units':previous+units}
    (dest/'combined.json').write_text(json.dumps(combined,ensure_ascii=False,indent=2),encoding='utf-8')
    print('New:',len(units),'Combined:',len(combined['units']))
    return combined

if __name__=='__main__':build()
