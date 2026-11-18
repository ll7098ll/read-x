"""Notation for individually authored texts and question/answer/evidence records."""
from corpus_revision_authoring import add,Q

# Selected spans within the first cited paragraph, reviewed against each question.
# Do not highlight a boilerplate introduction in place of the actual evidence.
SPANS={
 'P22-G4-S2-02':{1:(3,3),2:(2,3)},
 'P22-B02-G4-C-02':{2:(2,4)},
 'G4-EXP-W2':{1:(2,2),2:(2,4)},
 'G4-EXP-W3':{2:(2,2)},
 'P22-G5-S1-02':{1:(1,2)},
 'P22-B02-G5-M-02':{1:(2,3)},
 'P22-B02-G5-S-02':{1:(2,2)},
 'G5-EXP-V2-1':{2:(2,3)},
 'G5-EXP-V2-2':{1:(1,1),2:(3,3)},
 'G5-EXP-V2-3':{1:(2,2)},
 'G5-EXP-V3-3':{1:(2,4)},
 'P22-G6-S1-01':{1:(2,2)},
 'P22-G6-S1-02':{1:(2,2)},
 'P22-G6-S2-01':{1:(1,2)},
 'P22-G6-S2-02':{1:(1,2)},
 'P22-B02-G6-S-01':{2:(2,3)},
 'P22-B02-G6-S-02':{1:(2,2),2:(1,2)},
 'G6-EXP-W5':{2:(1,2)},
 'G6-EXP-V3-2':{1:(2,2)},
 'G6-EXP-V3-3':{1:(2,2)},
 'G6-EXP-V2-4':{1:(2,3)},
}

def A(key,title,core,standard,challenge,tasks,scenario,choices,application,words,review,sources=None):
    paragraphs=[p.strip() for p in core.strip().split('\n') if p.strip()]
    qs=[]
    for index,(prompt,answer,refs) in enumerate(tasks,1):
        refs=[refs] if isinstance(refs,int) else refs
        sentences=paragraphs[refs[0]-1].split('. ')
        start,end=SPANS.get(key,{}).get(index,(1,1))
        if start==end==1 and sentences[0].startswith(('다음은','다음 기록')) and len(sentences)>1:
            start=end=2
        anchor='. '.join(sentences[start-1:end]).rstrip('.')+'.'
        if anchor not in paragraphs[refs[0]-1]: anchor=paragraphs[refs[0]-1]
        qs.append(Q(prompt,answer,refs,anchor))
    answer,refs=application
    add(key,title,core,standard,challenge,qs,
        (scenario,'글의 원리와 보기의 조건을 함께 고려한 판단으로 가장 적절한 것은?',
         [c[0] for c in choices],refs,answer,[c[1] for c in choices]),words,review,sources)
