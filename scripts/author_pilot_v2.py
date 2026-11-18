"""Explicit six-stage pilot authoring. No automatic text padding or publication approval."""
from pathlib import Path
import json,re,hashlib,importlib
ROOT=Path(__file__).resolve().parents[1]
SETS=[]
LABELS={'S1':'뜻 익히기','S2':'단서 짚기','S3':'관계 엮기','S4':'의미 풀기','S5':'근거 따지기','S6':'새롭게 엮기'}

def M(prompt,answer,bad,quotes):
    return dict(kind='single_choice',prompt=prompt,answer=answer,distractors=bad,quotes=[quotes] if isinstance(quotes,(str,dict)) else quotes)

def O(kind,prompt,answer,quotes,partial,wrong):
    return dict(kind=kind,prompt=prompt,answer=answer,quotes=[quotes] if isinstance(quotes,(str,dict)) else quotes,partial=partial,wrong=wrong)

def E(skill,stage,variant,title,text,guide,tasks):
    blueprint=json.loads((ROOT/'data/content_authoring/architecture_v2/blueprint.json').read_text(encoding='utf-8'))
    s=next(s for s in blueprint['skills'] if s['id']==skill)
    uid=f'PV2-G{s["grade"]}-{skill.split("-")[-2]}-{skill.split("-")[-1]}-{stage}-{variant}'
    paras=[]
    for i,p in enumerate(text.split('\n')):
        paras.append(dict(id=f'{uid}-p{i+1}',text=p,sentences=[dict(id=f'{uid}-p{i+1}-s{j+1}',text=t) for j,t in enumerate(re.split(r'(?<=[.!?])\s+',p))]))
    def refs(quotes):
        result=[]
        for quote in quotes:
            if isinstance(quote,dict):
                result.append(dict(evidenceKind='graph',materialId=uid,version=1,assetId=uid+'-G'+str(quote['graph']),elementId=quote['element']))
                continue
            found=[(p,t) for p in paras for t in p['sentences'] if quote in t['text']]
            assert len(found)==1,(uid,quote,found)
            p,t=found[0]
            result.append(dict(materialId=uid,version=1,paragraphId=p['id'],sentenceId=t['id'],quote=quote,start=t['text'].index(quote)))
        return result
    questions=[]
    for i,t in enumerate(tasks):
        q=dict(id=f'{uid}-Q{i+1}',kind=t['kind'],prompt=t['prompt'],evidence=refs(t['quotes']),
          acceptableResponses='예시와 표현이 달라도 핵심 의미와 근거 관계를 충족하면 수용한다. 문자열 일치만으로 채점하지 않는다.',
          feedbackVisibility='after_first_response')
        if t['kind']=='single_choice':
            options=[dict(text=t['answer'],reason='자료 근거: '+' / '.join(x if isinstance(x,str) else f"그래프{x['graph']} {x['element']}" for x in t['quotes']))]+[dict(text=a,reason=r) for a,r in t['distractors']]
            assert len(options)==(3 if s['grade']<=2 else 4 if s['grade']<=4 else 5),(uid,t['prompt'])
            rotate=(len(SETS)+i)%len(options);options=options[rotate:]+options[:rotate]
            q.update(options=options,correctIndex=next(n for n,o in enumerate(options) if o['text']==t['answer']))
        else:
            q.update(expectedAnswer=t['answer'],rubric=[dict(criterion=t['prompt'],levels={'0':t['wrong'],'1':t['partial'],'2':t['answer']})])
            if t['kind']=='writing':q.update(workflow=['계획','초고','준거 검토','수정고','수정 이유'],planningPrompt='대상·핵심 정보·보존할 조건을 메모한 뒤 초고를 쓰세요.')
        questions.append(q)
    expected={'S1':3,'S2':4,'S3':4,'S4':4,'S5':5,'S6':6}[stage]
    assert len(questions)==expected,(uid,len(questions),expected)
    demands={
      'S1':dict(operation='뜻과 예 구별',evidenceDistance='가까움',support='방법 설명'),
      'S2':dict(operation='명시된 단서 선택',evidenceDistance='한 문장 또는 인접 문장',support='시범 후 연습'),
      'S3':dict(operation='복수 정보 연결',evidenceDistance='문단 사이',support='관계 틀 선택 제공'),
      'S4':dict(operation='생략 관계·의미 설명',evidenceDistance='문단 사이',support='응답 전 풀이 없음'),
      'S5':dict(operation='경쟁 해석·누락·범위 검토',evidenceDistance='자료 또는 진술 대조',support='응답 전 풀이 없음'),
      'S6':dict(operation='새 상황의 자료 통합·재표현',evidenceDistance='복수 자료',support='독립 수행')}[stage]
    SETS.append(dict(id=uid,version=1,microSkillId=skill,skillName=s['name'],grade=s['grade'],track=s['track'],
      stage=stage,stageLabel=LABELS[stage],variant=variant,title=title,purpose='transfer_check' if stage=='S6' else 'practice',
      familyId=uid,paragraphs=paras,charCount=len(' '.join(p['text'] for p in paras)),
      contentHash=hashlib.sha256('\n'.join(p['text'] for p in paras).encode()).hexdigest(),
      textDemand=dict(format='짧은 기능 집중 자료',gradeCondition=s['gradeCondition'],lengthReview='별도 장르·기능 분량, 장문 코스 기준 충족을 주장하지 않음'),
      taskDemand=demands,teacherGuide=guide,guideVisibility='teacher_only_after_response' if stage in ('S4','S5','S6') else 'instruction',
      questions=questions,source=dict(authorship='자체 창작 상황 및 문장',factualBasis='문제 안에 필요한 규칙·상황을 제공',officialStandards=[]),
      review=dict(state='draft',goalMapping='needs_teacher_review',teacherApproval='pending',studentCalibration='pending',publication='unpublished')))

def build():
    SETS.clear()
    for module in ['pilot_v2_g1_feelings','pilot_v2_g2_words','pilot_v2_g3_comparison','pilot_v2_g4_summary','pilot_v2_g5_argument','pilot_v2_g6_sources','pilot_v2_g2_complete','pilot_v2_g4_graphs','pilot_v2_g5_poetry','pilot_v2_g3_questions','pilot_v2_g6_rebuttal','pilot_v2_g1_reading']:importlib.import_module(module).author(E,M,O)
    from pilot_v2_editorial_assets import enrich
    enrich(SETS)
    dest=ROOT/'data/content_authoring/pilot_v2';dest.mkdir(parents=True,exist_ok=True)
    (dest/'sets.json').write_text(json.dumps(dict(schemaVersion='readx-six-stage-pilot-1',asOf='2026-11-17',sets=SETS),ensure_ascii=False,indent=2),encoding='utf-8')
    snapshot=hashlib.sha256((dest/'sets.json').read_bytes()).hexdigest()
    request=dict(reportName='listening-synthesis-result',purpose='듣기 자료와 첫 읽기 뒤 사용하는 읽기 모델의 음성 초안. 발음·쉼·속도 청취 검토 및 교사·학생 검증 대기.',sourceSnapshotHash=snapshot,
      requests=[dict(id=s['listening']['id'],materialId=s['id'],text=s['listening']['script'],usage='listening_material') for s in SETS if s.get('listening')]+
       [dict(id=s['reading']['id'],materialId=s['id'],text=s['reading']['modelScript'],usage='reading_model_after_first_read') for s in SETS if s.get('reading')])
    (dest/'listening_requests.json').write_text(json.dumps(request,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Authored pilot:',len(SETS),'sets;',sum(len(s['questions']) for s in SETS),'questions')
    return SETS

if __name__=='__main__':build()
