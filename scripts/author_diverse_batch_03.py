"""Explicitly authored short reading workshops; never grants publication approval."""
from pathlib import Path
import json, hashlib, re, collections, html

ROOT = Path(__file__).resolve().parents[1]
UNITS = []

def add(grade, title, subject, genre, goal, paragraphs, choice, short, organizer, writing, model, vocabulary, independent, transfer, clinic):
    number = sum(u['grade'] == grade for u in UNITS) + 1
    uid = f'B03-G{grade}-{number:02}'
    def material(suffix, title, paragraphs, purpose):
        pid = f'{uid}-{suffix}'
        return dict(id=pid, version=1, familyId=pid, title=title, purpose=purpose,
                    paragraphs=[dict(id=f'{pid}-s{i+1}', text=p) for i,p in enumerate(paragraphs)],
                    charCount=len(' '.join(paragraphs)), contentHash=hashlib.sha256('\n'.join(paragraphs).encode()).hexdigest(),
                    provenance='자체 창작 학습 상황·가상 기록. 실제 기관·조사·과학 실험 결과를 인용하지 않음.')
    a = material('A', title, paragraphs, 'practice')
    def evidence(mat, quote):
        matches=[p for p in mat['paragraphs'] if quote in p['text']]
        assert len(matches)==1, (uid,quote)
        p=matches[0]
        return dict(passageId=mat['id'],version=1,sentenceId=p['id'],quote=quote,start=p['text'].index(quote))
    def rubric(criteria):
        return [dict(criterion=c,levels={'0':f'{c}에 필요한 정보가 없거나 본문과 모순됨','1':f'{c}에 필요한 정보 일부만 포함하거나 관계 설명이 불분명함','2':f'{c}에 필요한 정보와 관계를 모두 정확하게 표현함'}) for c in criteria]
    cp,correct,distractors,quote,explanation=choice
    options=[dict(text=correct,reason=explanation,errorTag=None)]+[dict(text=t,reason=r,errorTag=None,errorTagReview='교사 검토 시 오답 특징 분류') for t,r in distractors]
    assert len(options)==(3 if grade<=2 else 4 if grade<=4 else 5)
    offset=(len(UNITS)+grade)%len(options)
    options=options[offset:]+options[:offset]
    q1=dict(id=uid+'-Q1',kind='single_choice',prompt=cp,options=options,correctIndex=next(i for i,o in enumerate(options) if o['text']==correct),
            explanation=explanation,evidence=[evidence(a,quote)],hints=['문제에서 확인하라는 대상을 먼저 찾아요.',f'본문의 “{quote[:10]}” 부분 주변을 다시 읽어요.','각 선택지를 본문의 조건과 하나씩 맞추고 없는 조건은 지워 보세요.'])
    sp,answer,squote,criteria=short
    q2=dict(id=uid+'-Q2',kind='explanation',prompt=sp,expectedAnswer=answer,rubric=rubric(criteria),evidence=[evidence(a,squote)],
            hints=['답만 쓰지 말고 그렇게 생각한 단서도 찾아요.','질문과 관련된 두 정보를 나누어 적어요.','단서 → 알 수 있는 것 순서로 연결해 보세요.'])
    kind,op,items,expected,oquote=organizer
    q3=dict(id=uid+'-Q3',kind=kind,prompt=op,items=items,expectedAnswer=expected,evidence=[evidence(a,oquote)],
            rubric=rubric(['제시한 요소를 빠짐없이 배치','본문에 맞는 순서·분류·대응 관계']),hints=['요소마다 본문에서 해당하는 부분을 찾아요.','분류 기준이나 순서를 먼저 한 문장으로 말해요.','배치한 뒤 본문과 거꾸로 대조해요.'])
    wp,plan,example,wcriteria=writing
    q4=dict(id=uid+'-Q4',kind='writing',prompt=wp,planningPrompt=plan,expectedAnswer=example,rubric=rubric(wcriteria),
            workflow=['계획','초고','준거로 검토','수정고','고친 이유'],evidence=[evidence(a,squote)],
            revisionPrompt='본문과 다른 내용, 빠뜨린 정보, 연결이 어색한 부분을 준거별로 확인하고 고친 이유를 적으세요.')
    checks=[]
    for suffix, spec, purpose in [('B',independent,'independent_check'),('C',transfer,'transfer_check')]:
        t,text,prompt,ans,eq,crit=spec
        mat=material(suffix,t,text.split('\n'),purpose)
        checks.append(dict(material=mat,question=dict(id=uid+'-Q'+('5' if suffix=='B' else '6'),kind='explanation',prompt=prompt,
            expectedAnswer=ans,evidence=[evidence(mat,eq)],rubric=rubric(crit),hints=[],feedbackVisibility='after_first_response',support='independent')))
    goal_id=f'G{grade}-{goal}'
    source=json.loads((ROOT/f'data/item_bank/g{grade}_item_bank.json').read_text(encoding='utf-8-sig'))
    goals={s['slot_id']:s for s in source['expository_slots']}
    goals.update({s['code']:s for s in source['common_slots']})
    assert goal_id in goals
    source_goal=goals[goal_id]
    mq,thought=model
    UNITS.append(dict(id=uid,version=1,grade=grade,title=title,subject=subject,genre=genre,goalId=goal_id,
        sourceGoal=source_goal.get('mager_goal',source_goal.get('mager_reading')),
        goalAlignment='candidate_needs_teacher_review',curriculumAlignment={'status':'not_claimed','standardIds':[]},
        format='짧은 자료 집중 수업',lengthException='설명문 장문 코스의 수준별 본문이 아닌, 단일 기능 중심의 짧은 자료 읽기. 학년 적합성 교사 검토 대기.',
        material=a,questions=[q1,q2,q3,q4],model=[dict(evidence=evidence(a,mq),thought=thought)],
        vocabulary=[dict(word=w,meaning=m) for w,m in vocabulary],checks=checks,
        clinic=dict(observation='본문의 정보 또는 관계를 놓친 응답이 있을 때 추가 확인',prompt=clinic[0],expectedAnswer=clinic[1],support='guided'),
        teacherGuide=dict(preparation='본문과 문항을 먼저 읽고 근거 위치·낱말 부담 확인',
            flow=['목표와 핵심어 확인','인용 구절을 짚으며 시범','Q1~Q3 수행과 도움 기록','Q4 계획·초고·수정','B와 C를 별도 시점에 처음 제시'],
            discussion=sp,partialResponseProbe='어느 문장을 보고 그렇게 생각했나요? 빠진 정보가 있는지 함께 확인해 볼까요?',
            estimatedMinutes=25 if grade<=2 else 35,timingBasis='편집 예상, 실측 아님'),
        parentGuide=dict(goal=f'「{title}」 자료에서 근거를 찾아 자기 말로 설명하는 활동입니다.',
            homeQuestion=sp,reportPolicy='실제 응답·도움·검토 상태에 연결한 뒤 공개. 무응답에서 능력을 추정하지 않음.'),
        review=dict(state='draft',teacherReview='pending',studentCalibration='pending',publication='unpublished',author='AI 자체 집필',independentReviewer=False)))

def build():
    from diverse_batch_03_g1_g2 import author as lower
    from diverse_batch_03_g3_g4 import author as middle
    from diverse_batch_03_g5_g6 import author as upper
    for author in [lower,middle,upper]: author(add)
    from diverse_batch_03_levels import enrich
    def challenge_material(u, extra):
        from copy import deepcopy
        m=deepcopy(u['material'])
        m['id']=u['id']+'-D'
        m['title']=u['title']+' · 추가 조건'
        m['paragraphs'].append(dict(id='',text=extra))
        for i,p in enumerate(m['paragraphs']):p['id']=m['id']+f'-p{i+1}'
        text=' '.join(p['text'] for p in m['paragraphs'])
        m['charCount']=len(text)
        m['contentHash']=hashlib.sha256('\n'.join(p['text'] for p in m['paragraphs']).encode()).hexdigest()
        return m
    def evidence(m,quote):
        p=next(p for p in m['paragraphs'] if quote in p['text'])
        return dict(passageId=m['id'],version=1,sentenceId=p['id'],quote=quote,start=p['text'].index(quote))
    enrich(UNITS,challenge_material,evidence)
    tables={
      'B03-G3-01':(['요일','가 모둠 그림 수 (한 그림=2개)','나 모둠 그림 수 (한 그림=4개)'],[['월',4,2],['화',6,3]]),
      'B03-G4-02':(['요일','대여 시작','대여 마감','반납 마감'],[['월','13시','14시','당일16시'],['수','14시','15시','당일16시']]),
      'B03-G4-04':(['장소','들은 소리','관찰 시간'],[['도서실 앞','작은 대화','1분'],['운동장 옆','공 튀는 소리','3분'],['음악실 앞','악기 연습','2분']]),
      'B03-G5-01':(['안내소','첫째 이용자','둘째 이용자','셋째 이용자','넷째 이용자'],[['가',2,2,2,14],['나',5,5,5,5]]),
      'B03-G5-02':(['날짜','안내원 수','방문객 수','문의 수'],[['첫날',2,300,30],['둘째 날',4,120,18]]),
      'B03-G5-04':(['보관함','칸','손잡이','빈 무게(g)'],[['가','작은 칸6개','없음',200],['나','큰 칸2개','있음',350]]),
      'B03-G6-02':(['안','기본 사용','줄이는 양','추가 사용'],[['가',100,20,0],['나',100,30,15]]),
      'B03-G6-04':(['시점','조사 인원','컵 지참 인원'],[['화요일',40,12],['목요일',20,10]])}
    for u in UNITS:
        if u['id'] in tables:
            headers,rows=tables[u['id']]
            u['material']['tables']=[dict(id=u['id']+'-T1',caption='본문의 가상 기록을 정리한 표',headers=headers,rows=rows)]
            # The challenge may correct a value, so retain the source table only on A.
        for q in u['questions']+[c['question'] for c in u['checks']]+[u['challenge']['question']]:
            if q['kind']!='single_choice':
                q['acceptableResponses']='예시 답과 표현이 달라도 각 준거의 의미와 근거 관계를 충족하면 수용한다. 맞춤법만으로 내용 점수를 낮추지 않는다.'
                q['partialResponseProbe']='답에서 각 조건이 어떻게 쓰였는지 본문을 짚어 설명해 주세요.'
        u['clinic']['triggerPolicy']='선택 하나로 원인을 확정하지 않고 근거 설명을 추가 확인한 뒤 배정한다.'
    # Paragraph and sentence identities are distinct; resolve every quote to a sentence.
    for u in UNITS:
        materials=[u['material'],u['challenge']['material']]+[c['material'] for c in u['checks']]
        for m in materials:
            for i,p in enumerate(m['paragraphs']):
                p['id']=m['id']+f'-p{i+1}'
                p['sentences']=[dict(id=p['id']+f'-s{j+1}',text=t) for j,t in enumerate(re.split(r'(?<=[.!?])\s+',p['text']))]
        refs=[e for q in u['questions']+[u['challenge']['question']]+[c['question'] for c in u['checks']] for e in q['evidence']]
        refs += [x['evidence'] for x in u['model']]
        by_id={m['id']:m for m in materials}
        for e in refs:
            m=by_id[e['passageId']]
            matches=[(p,s) for p in m['paragraphs'] for s in p['sentences'] if e['quote'] in s['text']]
            assert len(matches)==1,(u['id'],e['quote'])
            p,s=matches[0]
            e.update(paragraphId=p['id'],sentenceId=s['id'],start=s['text'].index(e['quote']))
    return UNITS

if __name__=='__main__':
    units=build()
    dest=ROOT/'data/content_authoring/batch_03'
    dest.mkdir(parents=True,exist_ok=True)
    (dest/'units.json').write_text(json.dumps(dict(schemaVersion='readx-authoring-1',batch='03',authoredAt='2026-11-14',units=units),ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Authored {len(units)} units')
