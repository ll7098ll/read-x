"""Verify authored artifacts and expose remaining scope; never simulates teacher approval."""
from pathlib import Path
import json,re,hashlib,collections,difflib
ROOT=Path(__file__).resolve().parents[1]
PILOT_IDS=['plan-G1-language-03','plan-G1-literature-05','plan-G2-language-07','plan-G2-writing-11',
 'plan-G3-information-08','plan-G3-oral-02','plan-G4-information-05','plan-G4-media-02',
 'plan-G5-writing-09','plan-G5-literature-06','plan-G6-media-07','plan-G6-oral-04']

def validate(source=None,out=None,skill_ids=None,variants_per_stage=2,comparison_sources=(),expected_stage_counts=None):
    source=Path(source) if source else ROOT/'data/content_authoring/pilot_v2/sets.json'
    out=Path(out) if out else ROOT/'output/pilot-v2'
    selected_ids=list(skill_ids) if skill_ids is not None else PILOT_IDS
    expected_stage_counts=expected_stage_counts if expected_stage_counts is not None else {sid:{stage:variants_per_stage for stage in ['S1','S2','S3','S4','S5','S6']} for sid in selected_ids}
    assert set(expected_stage_counts)==set(selected_ids)
    quotas=dict(S1=3,S2=4,S3=4,S4=4,S5=5,S6=6)
    target_sets=sum(sum(stages.values()) for stages in expected_stage_counts.values())
    target_questions=sum(quotas[stage]*n for stages in expected_stage_counts.values() for stage,n in stages.items())
    raw=json.loads(source.read_text(encoding='utf-8'))
    sets=raw['sets'];blueprint=json.loads((ROOT/'data/content_authoring/architecture_v2/blueprint.json').read_text(encoding='utf-8'))
    skills={s['id']:s for s in blueprint['skills']};errors=[];warnings=[];length_candidates=[];ids=set();hashes={};source_cache={};fact_ledgers={}
    standards={r['id']:r for r in json.loads((ROOT/'data/curriculum_2022/achievement_standards.json').read_text(encoding='utf-8'))}
    def ck(ok,msg):
        if not ok:errors.append(msg)
    def check_source(ref,label):
        path=ref['sourcePath']
        if path not in source_cache:
            payload=(ROOT/path).read_bytes();source_cache[path]=(payload.decode('utf-8').splitlines(),hashlib.sha256(payload).hexdigest())
        lines,digest=source_cache[path];line=lines[ref['sourceLine']-1]
        ck(ref['code'] in line and ref['statement'] in line,label+' standard source text')
        ck(digest==ref['sourceHash'],label+' standard source hash')
        official=standards.get(ref['code']);ck(official is not None,label+' standard not in source registry')
        if official:
            ck(all(ref[k]==official['id' if k=='code' else k] for k in ['code','statement','gradeBand','sourcePath','sourceLine','noticeVersion']),label+' source registry mismatch')
    for s in sets:
        ck(s['id'] not in ids,s['id']+' duplicate');ids.add(s['id'])
        ck(s['microSkillId'] in skills,s['id']+' unknown planning skill')
        ck(s['grade']==skills[s['microSkillId']]['grade'],s['id']+' grade mismatch')
        text='\n'.join(p['text'] for p in s['paragraphs']);h=hashlib.sha256(text.encode()).hexdigest()
        ck(h==s['contentHash'],s['id']+' hash mismatch');ck(h not in hashes,s['id']+' identical text');hashes[h]=s['id']
        ck(s['charCount']==len(' '.join(p['text'] for p in s['paragraphs'])),s['id']+' character count')
        if s.get('literaryReview'):
            literary=s['literaryReview'];primary=next((q for q in s['questions'] if q['id']==literary['primaryQuestionId']),None)
            ck(primary is not None and primary['kind']!='single_choice',s['id']+' missing literary interpretation response')
            if primary:ck(2<=len(primary['rubric'])<=4,primary['id']+' missing analytic interpretation criteria')
            ck(s['presentationOrder'][0]==literary['primaryQuestionId'] and set(s['presentationOrder'])=={q['id'] for q in s['questions']},s['id']+' literary response must precede choices')
            ck(literary['interpretationPolicy'] and literary['notAssessed'] and literary['teacherApproval']=='pending',s['id']+' interpretation scope and approval')
        if s.get('writingProtocol'):
            protocol=s['writingProtocol'];primary=[q for q in s['questions'] if q['id']==protocol['primaryQuestionId']]
            ck(len(primary)==1 and primary[0]['kind']=='writing',s['id']+' missing writing production task')
            if primary:
                q=primary[0];context=q.get('writerContext',{})
                ck(all(context.get(k) for k in ['reader','purpose','length','responseOrigin']),q['id']+' writing situation incomplete')
                ck(2<=len(q['rubric'])<=4,q['id']+' writing analytic criteria')
            ck(s['presentationOrder'][0]==protocol['primaryQuestionId'] and set(s['presentationOrder'])=={q['id'] for q in s['questions']},s['id']+' writing must precede choices and auxiliary questions')
            ck(len(protocol['observationFields'])>=6 and protocol['supportPolicy'] and protocol['storageLimit'],s['id']+' missing writing observation conditions')
        if s['source'].get('factChecks'):
            path=s['source']['factLedgerPath']
            if path not in fact_ledgers:
                payload=(ROOT/path).read_bytes();fact_ledgers[path]=(json.loads(payload),hashlib.sha256(payload).hexdigest())
            ledger,digest=fact_ledgers[path];sources={r['id']:r for r in ledger['sources']}
            ck(digest==s['source']['factLedgerHash'],s['id']+' stale factual ledger')
            declared={r['id']:r for r in s['source']['factualReferences']}
            ck(set(declared)=={r['sourceId'] for r in s['source']['factChecks']},s['id']+' factual source coverage')
            for sid,ref in declared.items():
                ck(sid in sources and all(ref[k]==sources[sid][k] for k in ['publisher','title','url','locator']),s['id']+' factual source identity')
                ck(ref['url'].startswith('https://'),s['id']+' invalid source URL')
            for fact in s['source']['factChecks']:
                source_fact=sources[fact['sourceId']]['facts'].get(fact['factId'])
                ck(source_fact==fact['checkedStatement'],s['id']+' factual claim differs from source ledger')
                found=[(p,t) for p in s['paragraphs'] for t in p['sentences'] if fact['quote'] in t['text']]
                ck(len(found)==1 and found[0][0]['id']==fact['paragraphId'] and found[0][1]['id']==fact['sentenceId'],s['id']+' factual anchor mismatch')
        if s.get('reading'):
            reading=s['reading']
            ck(s['readingHash']==hashlib.sha256(json.dumps(reading,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' reading hash')
            ck(reading['id'] not in ids,reading['id']+' duplicate model id');ids.add(reading['id'])
            ck(reading['modelScript']=='\n\n'.join(p['text'] for p in s['paragraphs']),s['id']+' reading model/visible text mismatch')
            ck(reading['paragraphIds']==[p['id'] for p in s['paragraphs']],s['id']+' reading paragraph order')
            ck(reading['words']==[dict(paragraphId=p['id'],index=i+1,printedWord=word) for p in s['paragraphs'] for i,word in enumerate(p['text'].split())],s['id']+' reading observation reference')
            ck(set(reading['displayLabels'])<=set(reading['paragraphIds']),s['id']+' reading label reference')
            ck(reading['modelVisibility']=='after_first_read' and reading['firstReadObservation']=='required_before_model' and reading['listeningReview']=='pending',s['id']+' model exposure policy')
            order=s['presentationOrder'];questions={q['id']:q for q in s['questions']}
            ck(len(order)==len(questions) and set(order)==set(questions),s['id']+' reading question order')
            ck(sum(q['kind']=='oral_reading' for q in s['questions'])==1 and questions[order[0]]['kind']=='oral_reading',s['id']+' first read before choices')
        if s.get('listening'):
            listening=s['listening'];bypara={p['id']:p['text'] for p in s['paragraphs']}
            ck(s['listeningHash']==hashlib.sha256(json.dumps(listening,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' listening hash')
            ck(listening['id'] not in ids,listening['id']+' duplicate audio id');ids.add(listening['id'])
            ck(listening['transcriptVisibility']=='teacher_only' and listening['listeningReview']=='pending',s['id']+' listening state')
            ck(listening['script']=='\n\n'.join(t['role']+'입니다. '+t['text'] for t in listening['turns']),s['id']+' script/turn mismatch')
            ck(all(bypara.get(t['paragraphId'])==t['role']+': '+t['text'] for t in listening['turns']),s['id']+' transcript/turn mismatch')
            ck(s['partnerCard']['visibility'] in ('teacher_only_after_question','teacher_only_after_explanation') and s['partnerCard']['reply'],s['id']+' partner card')
            ck(sum(q['kind']=='spoken_response' for q in s['questions'])==1,s['id']+' missing primary speech task')
            if s.get('oralTaskType')=='revise_explanation':
                clarify=s['stage']=='S4' and s['variant']=='A'
                ck(s['partnerCard']['kind']==('clarification_reply' if clarify else 'followup_prompt'),s['id']+' partner intervention kind')
                ck(s['partnerCard']['visibility']==('teacher_only_after_question' if clarify else 'teacher_only_after_explanation'),s['id']+' partner intervention timing')
            ck(s['partnerCardHash']==hashlib.sha256(json.dumps(s['partnerCard'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' partner card hash')
            order=s['presentationOrder'];questions={q['id']:q for q in s['questions']}
            ck(len(order)==len(questions) and set(order)==set(questions),s['id']+' presentation order')
            if s['stage'] in ('S4','S5','S6'):ck(questions[order[0]]['kind']=='spoken_response',s['id']+' choices before independent speech')
        if s.get('poems'):
            ck(s['poetryHash']==hashlib.sha256(json.dumps(s['poems'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' poetry hash')
            bypara={p['id']:p['text'] for p in s['paragraphs']};used=set()
            for poem in s['poems']:
                ck(poem['id'] not in ids,poem['id']+' duplicate poem id');ids.add(poem['id'])
                ck(poem['title'] in bypara.get(poem['headingParagraphId'],''),poem['id']+' title missing')
                ck(len(poem['lines'])>=4 and len(poem['lineParagraphIds'])==len(poem['lines']),poem['id']+' poem lines')
                ck([bypara.get(pid) for pid in poem['lineParagraphIds']]==poem['lines'],poem['id']+' line text changed')
                ck(not used.intersection(poem['lineParagraphIds']),poem['id']+' duplicate poem lines');used.update(poem['lineParagraphIds'])
        for t in s.get('tables',[]):
            ck(all(len(row)==len(t['headers']) for row in t['rows']),t['id']+' table dimensions')
            ck(t['id'] not in ids,t['id']+' duplicate table id');ids.add(t['id'])
        if s.get('tables'):
            ck(s['tableHash']==hashlib.sha256(json.dumps(s['tables'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' table hash')
        media={m['id']:m for m in s.get('mediaPanels',[])}
        if media:
            ck(len(media)==len(s['mediaPanels']),s['id']+' duplicate media panel')
            ck(s['mediaHash']==hashlib.sha256(json.dumps(s['mediaPanels'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' media hash')
            for m in media.values():
                ck(m['id'] not in ids,m['id']+' duplicate asset id');ids.add(m['id'])
                ck(m['title'] and m['accessibleDescription'] and m['elements'],m['id']+' media content')
                ck(len({e['id'] for e in m['elements']})==len(m['elements']) and all(e['text'] and e['style'] in ('large','header','body','small') for e in m['elements']),m['id']+' media elements')
        graphs={g['id']:g for g in s.get('graphs',[])}
        if graphs:
            ck(s['graphHash']==hashlib.sha256(json.dumps(s['graphs'],ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' graph hash')
        for g in s.get('graphs',[]):
            ck(g['id'] not in ids,g['id']+' duplicate graph id');ids.add(g['id'])
            ck(len(g['labels'])==len(g['values']) and len(set(g['labels']))==len(g['labels']),g['id']+' graph dimensions')
            ck(g['unit'] and g['accessibleDescription'] and all(v>=0 for v in g['values']),g['id']+' graph content')
            if g['kind']=='pictograph':
                ck(g['symbolValue']>0 and all(v%g['symbolValue']==0 for v in g['values']),g['id']+' incomplete symbol')
                if g.get('hiddenLegend'):
                    ck('= ?'+g['unit'] in g['elements']['legend'] and '별 1개 = '+str(g['symbolValue']) not in g['accessibleDescription'],g['id']+' missing-legend answer leak')
                if g.get('legendOverride'):
                    ck(g.get('intentionalPresentation')=='wrong_legend_unit_for_review' and g['legendOverride']=='별 1개 = 5명' and g['unit']=='권',g['id']+' unexplained wrong legend')
            elif g['kind']=='bar':
                ck(g['axisStep']>0 and g['axisMin']<g['axisMax'] and (g['axisMax']-g['axisMin'])%g['axisStep']==0,g['id']+' invalid scale')
                ck(all(g['axisMin']<=v<=g['axisMax'] for v in g['values']),g['id']+' clipped values')
                ck(g['axisMin']==0 or g.get('intentionalPresentation')=='nonzero_axis_for_review',g['id']+' unmarked nonzero axis')
                ck(all(g['axisMin']<=v<=g['axisMax'] and (v-g['axisMin'])%g['axisStep']==0 for v in g.get('hiddenTicks',[])),g['id']+' invalid missing tick')
            else:ck(False,g['id']+' unknown graph type')
        ck(len(s['questions'])==dict(S1=3,S2=4,S3=4,S4=4,S5=5,S6=6)[s['stage']],s['id']+' item quota')
        ck(s['review']['publication']=='unpublished' and s['review']['teacherApproval']=='pending',s['id']+' approval invented')
        for ref in s['source'].get('officialStandards',[]):
            check_source(ref,s['id'])
            ck(s['grade'] in ref['gradeBand'] and ref['alignmentState']=='source_text_checked_candidate',s['id']+' standard grade/status')
        if s['source'].get('curriculumAudit'):
            audit=s['source']['curriculumAudit'];links=audit['links'];linkmap={r['id']:r for r in links}
            ck(s['source']['curriculumAuditHash']==hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),s['id']+' curriculum audit hash')
            ck(len(linkmap)==len(links) and audit['teacherApproval']=='pending',s['id']+' audit identity/approval')
            direct=[r for r in links if r['role']=='direct_component']
            ck(direct==s['source']['officialStandards'],s['id']+' direct and related links mixed')
            ck(audit['decision']==('direct_component_candidate' if direct else 'related_only_goal_scope_review'),s['id']+' audit decision')
            if not direct:ck(bool(audit['remainingGap']),s['id']+' related-only gap hidden')
            for ref in links:
                check_source(ref,s['id']);ck(ref['subject']==standards[ref['code']]['subject'],s['id']+' subject relabelled')
                ck(ref['role'] in ('direct_component','learning_support','related_application','cross_subject_component','later_grade_articulation','optional_followup','not_direct_evidence'),s['id']+' invalid relation')
                ck(ref['includedComponent'] and ref['notAssessed'] and set(ref['questionIds'])<={q['id'] for q in s['questions']},s['id']+' incomplete scope')
                if ref['role']=='direct_component':ck(ref['subject']=='국어' and s['grade'] in ref['gradeBand'],s['id']+' wrong direct domain/grade')
                if s['grade'] not in ref['gradeBand']:ck(ref['role'] in ('later_grade_articulation','not_direct_evidence'),s['id']+' unmarked later grade link')
            accepted={r['id'] for r in links if r['role']!='not_direct_evidence'}
            for q in s['questions']:
                coverage=q.get('curriculumCoverage',{})
                ck(coverage.get('notFullStandardAchievement') is True and set(coverage.get('linkIds',[]))<=accepted,q['id']+' overstated/rejected curriculum coverage')
        if s['review'].get('draftRevision'):
            rev=s['review']['draftRevision'];archived=json.loads((ROOT/rev['previousSnapshotPath']).read_text(encoding='utf-8'))
            old=next(x for x in archived['sets'] if x['id']==s['id'])
            ck(old['version']==rev['fromVersion'] and s['version']==rev['toVersion'] and old['contentHash']==rev['previousContentHash']!=s['contentHash'],s['id']+' revision trace')
            ck(archived['sourceSnapshotHash']==rev['previousDataSnapshotHash'] and old['contentHash']==hashlib.sha256('\n'.join(p['text'] for p in old['paragraphs']).encode()).hexdigest(),s['id']+' archive reference changed')
        if s['stage']=='S6':ck(s['purpose']=='transfer_check' and s['guideVisibility']=='teacher_only_after_response',s['id']+' transfer leak')
        byid={t['id']:t for p in s['paragraphs'] for t in p['sentences']}
        for q in s['questions']:
            ck(q['id'] not in ids,q['id']+' duplicate');ids.add(q['id'])
            ck(q['prompt'] and q['evidence'],q['id']+' incomplete')
            ck(q['feedbackVisibility']=='after_first_response',q['id']+' feedback policy')
            ck(q.get('version',1)==s['version'],q['id']+' question/material version mismatch')
            for e in q['evidence']:
                ck(e['version']==s['version'],q['id']+' evidence version mismatch')
                if e.get('evidenceKind')=='media':
                    m=media.get(e['assetId']);element=next((x for x in m['elements'] if x['id']==e['elementId']),None) if m else None
                    ck(e['materialId']==s['id'] and bool(element) and element['text']==e['quote'],q['id']+' media element reference')
                    continue
                if e.get('evidenceKind')=='audio':
                    listening=s.get('listening',{});turns=listening.get('turns',[])
                    ck(e['assetId']==listening.get('id') and 0<=e['turnIndex']<len(turns),q['id']+' audio reference')
                    if 0<=e['turnIndex']<len(turns):ck(turns[e['turnIndex']]['paragraphId']==e['paragraphId'] and e['quote'] in turns[e['turnIndex']]['text'],q['id']+' audio turn evidence')
                if e.get('evidenceKind')=='graph':
                    g=graphs.get(e['assetId'])
                    ck(e['materialId']==s['id'] and g is not None,q['id']+' graph reference')
                    if g:ck(g['elements'].get(e['elementId'])==e.get('quote') and bool(e.get('quote')),q['id']+' graph evidence element')
                    continue
                t=byid.get(e['sentenceId']);ck(e['materialId']==s['id'] and t is not None,q['id']+' reference')
                if t:ck(t['text'][e['start']:e['start']+len(e['quote'])]==e['quote'],q['id']+' quote location')
            if q['kind']=='single_choice':
                n=3 if s['grade']<=2 else 4 if s['grade']<=4 else 5
                ck(len(q['options'])==n and len({o['text'] for o in q['options']})==n,q['id']+' options')
                ck(0<=q['correctIndex']<n and all(o['reason'] for o in q['options']),q['id']+' answer/reasons')
                ck(q.get('explanation') and q['options'][q['correctIndex']]['reason']==q['explanation'],q['id']+' missing correct-answer explanation')
                lengths=[len(o['text']) for o in q['options']]
                if lengths[q['correctIndex']]>1.4*max(v for n,v in enumerate(lengths) if n!=q['correctIndex']):
                    length_candidates.append(dict(id=q['id'],lengths=lengths,reason='정답만 긴지 편집 검토.1.4는 편집 탐지값이며 난도 기준이 아님.'))
            else:
                ck(q['expectedAnswer'] and q['rubric'],q['id']+' answer/rubric')
                for r in q['rubric']:
                    ck(set(r['levels'])=={'0','1','2'} and len(set(r['levels'].values()))==3,q['id']+' rubric distinctions')
                if s['stage']=='S4' and not s.get('reading') and len(q['expectedAnswer'])>12 and q['expectedAnswer'] in text:
                    warnings.append(dict(id=q['id'],type='interpretation_answer_verbatim',action='stage fit review'))
            if q['kind']=='writing':ck(len(q['workflow'])==5,q['id']+' writing process')
            if q['kind']=='spoken_response':
                ck(q['responseMode']=='live_speech_with_partner' and len(q['observationFields'])>=4 and len(q['rubric'])==3,q['id']+' actual oral performance protocol')
                ck(q['partnerReplyRef']['materialId']==s['id'] and s.get('partnerCard'),q['id']+' observed reply source')
            if q['kind']=='oral_reading':
                ck(q['responseMode']=='live_reading_before_model' and q['modelAudioRef']==s['reading']['id'],q['id']+' first read protocol')
                ck(len(q['observationFields'])>=5 and len(q['rubric'])==3,q['id']+' first/model observation distinction')
    pairs=collections.Counter((s['microSkillId'],s['stage']) for s in sets)
    for sid in {s['microSkillId'] for s in sets}:
        for stage in ['S1','S2','S3','S4','S5','S6']:ck(pairs[(sid,stage)]==expected_stage_counts.get(sid,{}).get(stage,0),sid+' '+stage+' differs from declared stage supply')
    ck({s['microSkillId'] for s in sets}==set(selected_ids),'batch skill coverage differs from declared scope')
    by_set={s['id']:s for s in sets};numeric_checks={};reading_checks={}
    for s in sets:
        if not s.get('reading'):continue
        q=s['questions'][0];correct=q['options'][q['correctIndex']]['text'];key=s['stage']+'-'+s['variant']
        if s['stage']!='S5':
            matches=[i for i,o in enumerate(q['options']) if o['text'] in [p['text'] for p in s['paragraphs']]]
            reading_checks['G1_'+key+'_literal_choice']=len(matches)==1 and matches[0]==q['correctIndex']
        else:
            printed=s['paragraphs'][0]['text'].rstrip('.').split();example=q['prompt'].split('에서')[0].split()
            if s['variant']=='A':
                missing=[w for w in printed if w not in example]
                reading_checks['G1_S5A_missing_word']=len(missing)==1 and missing[0]==correct and example==[w for w in printed if w!=correct]
            else:
                changed=[(a,b) for a,b in zip(printed,example) if a!=b]
                reading_checks['G1_S5B_changed_word']=len(printed)==len(example) and len(changed)==1 and changed[0][1]==correct
        task=next(q for q in s['questions'] if q['kind']=='oral_reading')
        reading_checks['G1_'+key+'_oral_reference']=' '.join(task['expectedAnswer'].split())==' '.join(p['text'] for p in s['paragraphs'])
    for name,ok in reading_checks.items():ck(ok,name+' mismatch')
    def body(s):return ' '.join(p['text'] for p in s['paragraphs'])
    def table(s):return s['tables'][0]['rows']
    if 'PV2-G3-information-08-S2-A' in by_set:
        s=by_set['PV2-G3-information-08-S2-A']
        pairs_source=[list(map(int,m)) for m in re.findall(r'담는 양(\d+)mL, 빈 무게(\d+)g',body(s))]
        numeric_checks['G3_S2A_source_table']=pairs_source==[r[1:] for r in table(s)]
        numeric_checks['G3_S2A_differences']=table(s)[0][1]-table(s)[1][1]==100 and table(s)[0][2]-table(s)[1][2]==50
        s=by_set['PV2-G3-information-08-S3-A']
        numeric_checks['G3_S3A_inside_dimensions']=[list(map(int,m)) for m in re.findall(r'길이(\d+)cm, 너비(\d+)cm',body(s))]==[r[1:3] for r in table(s)]
        numeric_checks['G3_S3A_fit']=table(s)[0][1]>=28>table(s)[1][1]
        s=by_set['PV2-G3-information-08-S3-B'];b=body(s)
        pages=[int(re.search(r'가 연습장은(\d+)쪽',b)[1]),int(re.search(r'나 연습장은(\d+)쪽',b)[1])]
        prices=list(map(int,re.search(r'가격은 가(\d+)원, 나(\d+)원',b).groups()))
        numeric_checks['G3_S3B_pages_prices']=pages==[r[1] for r in table(s)] and prices==[r[3] for r in table(s)]
        s=by_set['PV2-G3-information-08-S5-A'];b=body(s)
        expected=[[int(re.search(r'담는 양(\d+)mL',b)[1]),int(re.search(r'가의 빈 무게가(\d+)g',b)[1])],
                  [int(re.search(r'나의 담는 양이(\d+)mL',b)[1]),int(re.search(r'빈 무게(\d+)g',b)[1])]]
        numeric_checks['G3_S5A_units_source_table']=expected==[r[1:] for r in table(s)]
        s=by_set['PV2-G3-information-08-S6-A'];b=body(s)
        expected=[list(map(int,re.search(name+r' 꾸러미에는.*?(\d+)세트.*?(\d+)원',b).groups())) for name in ['가','나']]
        numeric_checks['G3_S6A_source_table']=expected==[r[1:] for r in table(s)]
        numeric_checks['G3_S6A_selection']=table(s)[0][1]<8<=table(s)[1][1] and table(s)[0][2]<=5500 and table(s)[1][2]<=5500
    if 'PV2-G5-writing-09-S5-B' in by_set:
        s=by_set['PV2-G5-writing-09-S5-B'];b=body(s);rows=table(s)
        found=[int(re.search(r'전체 학생은(\d+)명',b)[1]),int(re.search(r'의견을 남긴 학생은(\d+)명',b)[1]),int(re.search(r'그중(\d+)명이 찬성',b)[1]),int(re.search(r'나머지(\d+)명에게',b)[1])]
        numeric_checks['G5_S5B_source_table']=found==[r[1] for r in rows]
        numeric_checks['G5_S5B_denominators']=rows[2][1]/rows[1][1]*100==75 and rows[2][1]/rows[0][1]*100==25 and rows[1][1]+rows[3][1]==rows[0][1]
        s=by_set['PV2-G6-media-07-S2-B'];b=body(s)
        found=[int(re.search(r'가위(\d+)개가 등록',b)[1]),int(re.search(r'그중(\d+)개를 수리',b)[1]),int(re.search(r'나머지(\d+)개는 바로',b)[1])]
        numeric_checks['G6_S2B_source_table']=found==[r[1] for r in table(s)] and found[1]+found[2]==found[0]
        s=by_set['PV2-G6-media-07-S3-A'];b=body(s)
        found=[int(re.search(p,b)[1]) for p in [r'4월 대출은(\d+)권',r'이야기책 대출은(\d+)권',r'정보책 대출은(\d+)권',r'추천책은(\d+)권']]
        numeric_checks['G6_S3A_source_table']=found==[r[1] for r in table(s)] and found[1]+found[2]==found[0]
        s=by_set['PV2-G6-media-07-S3-B'];b=body(s)
        found=[int(re.search(p,b)[1]) for p in [r'발표 명단에는(\d+)명',r'해설 명단에는(\d+)명',r'같은 학생(\d+)명']]
        numeric_checks['G6_S3B_source_table']=found==[r[1] for r in table(s)[:3]] and sum(found[:2])==table(s)[3][1]
        numeric_checks['G6_S3B_unique_students']=found[0]+found[1]-found[2]==17
        key=next(q['expectedAnswer'] for q in s['questions'] if q['kind']=='table_completion')
        numeric_checks['G6_S3B_answer_key']=int(re.search(r'학생(\d+)',key)[1])==found[0]+found[1]-found[2]
        s=by_set['PV2-G6-media-07-S4-A'];b=body(s)
        numeric_checks['G6_S4A_measurement_scopes']=[int(v) for v in re.findall(r'시간이(\d+)분',b)]==[r[2] for r in table(s)] and [int(v) for v in re.findall(r'모둠원은(\d+)명',b)]==[r[3] for r in table(s)]
        s=by_set['PV2-G6-media-07-S4-B'];b=body(s)
        found=[list(map(int,p)) for p in re.findall(r'참가자(\d+)명 중(\d+)명',b)]
        numeric_checks['G6_S4B_source_table']=found==[[r[1],r[3]] for r in table(s)]
        lower=max(0,found[0][1]+found[1][1]-found[0][0]);upper=min(found[0][1],found[1][1])
        numeric_checks['G6_S4B_overlap_bounds']=lower==8 and upper==20
        key=next(q['expectedAnswer'] for q in s['questions'] if q['prompt'].startswith('두 응답 집단이 전혀'))
        numeric_checks['G6_S4B_answer_key']=int(re.search(r'적어도(\d+)명',key)[1])==lower
        s=by_set['PV2-G6-media-07-S6-A'];b=body(s)
        found=[int(re.search(p,b)[1]) for p in [r'등록 도구는(\d+)개',r'선반의 도구는(\d+)개',r'대출 중(\d+)개',r'수리 중(\d+)개',r'분실 신고(\d+)개']]
        numeric_checks['G6_S6A_states_source_table']=found==[r[1] for r in table(s)] and sum(found[1:])==found[0]
        numeric_checks['G6_S6A_same_time_nonoverlap']='같은 금요일 마감 시각' in b and '같은 시각 선반' in b and '이 세 상태는 서로 겹치지 않는다.' in b
        key=next(q['expectedAnswer'] for q in s['questions'] if q['kind']=='table_completion')
        numeric_checks['G6_S6A_answer_key']=[int(v) for v in re.findall(r'\d+',key)]==found
        s=by_set['PV2-G6-media-07-S6-B']
        p,q=s['paragraphs'][0]['text'],s['paragraphs'][1]['text']
        found=[[int(re.search(r'(\d+)명 전원',t)[1]),int(re.search(r'(\d+)명은 조용한 독서',t)[1]),int(re.search(r'(\d+)명은 대화 공간',t)[1])] for t in [p,q]]
        numeric_checks['G6_S6B_source_table']=found==[r[1:] for r in table(s)] and all(r[1]+r[2]==r[0] for r in found)
        numeric_checks['G6_S6B_group_rates']=found[0][1]/found[0][0]*100==60 and found[1][2]/found[1][0]*100==70
        key=next(q['expectedAnswer'] for q in s['questions'] if q['kind']=='table_completion')
        numeric_checks['G6_S6B_answer_key']=[int(v) for v in re.findall(r'\d+',key)]==[40,24,60,16,40,20,6,30,14,70]
        arguments=[s for s in sets if s['microSkillId']=='plan-G5-writing-09']
        writing_questions=[q for s in arguments for q in s['questions'] if q['kind']=='writing']
        ck(len(writing_questions)==10 and all(len(q['rubric'])==3 for q in writing_questions),'G5 argument analytic criteria')
    if 'PV2-G4-media-02-S1-A' in by_set:
        def gs(key):return by_set['PV2-G4-media-02-'+key]
        def graph(key,i=0):return gs(key)['graphs'][i]
        def mc(key):
            q=gs(key)['questions'][0];return q['options'][q['correctIndex']]['text']
        def answer(key,kind):return next(q['expectedAnswer'] for q in gs(key)['questions'] if q['kind']==kind)
        numeric_checks['G4_S1A_symbol_key']=graph('S1-A')['symbolValue']==2 and mc('S1-A')=='책 두 권'
        numeric_checks['G4_S2A_symbol_and_answer']=graph('S2-A')['values']==[6,8,10] and graph('S2-A')['symbolValue']==2 and mc('S2-A')=='여덟 개' and [int(n) for n in re.findall(r'\d+',answer('S2-A','table_completion'))]==[3,6,4,8,5,10]
        numeric_checks['G4_S2B_axis_and_answer']=graph('S2-B')['axisStep']==5 and mc('S2-B')=='서른 개' and graph('S2-B')['values']==[int(n) for n in re.findall(r'\d+',answer('S2-B','table_completion'))]
        numeric_checks['G4_S3A_same_data_different_symbols']=graph('S3-A')['values']==graph('S3-A',1)['values']==[8,12] and [g['symbolValue'] for g in gs('S3-A')['graphs']]==[2,4]
        numeric_checks['G4_S3A_answer_table']=[int(n) for n in re.findall(r'\d+',answer('S3-A','table_completion'))]==[8,8,12,12]
        numeric_checks['G4_S3B_names_and_source']={k:v for k,v in re.findall(r'(가|나|다) 모둠(\d+)명',body(gs('S3-B')))}=={k:str(v) for k,v in zip(graph('S3-B')['labels'],graph('S3-B')['values'])}
        numeric_checks['G4_S4A_source_and_hidden_legend']=[int(n) for n in re.findall(r'모둠(\d+)권',body(gs('S4-A')))]==graph('S4-A')['values'] and graph('S4-A')['hiddenLegend'] and graph('S4-A')['symbolValue']==4 and mc('S4-A')=='네 권'
        numeric_checks['G4_S4B_equal_spacing_and_key']=graph('S4-B')['hiddenTicks']==[2] and graph('S4-B')['axisStep']==2 and mc('S4-B')=='2'
        numeric_checks['G4_S5A_source_same_data']=[int(n) for n in re.findall(r'(?:월요일|화요일)(\d+)권',body(gs('S5-A')))]==graph('S5-A')['values']==graph('S5-A',1)['values']
        a,b=gs('S5-A')['graphs']
        numeric_checks['G4_S5A_visible_ratio_actual_difference']=a['axisMin']==0 and b['axisMin']==6 and (b['values'][1]-6)==2*(b['values'][0]-6) and a['values'][1]-a['values'][0]==2 and '두 권 많고 두 배는 아니다' in mc('S5-A')
        numeric_checks['G4_S5B_book_units_and_review_draft']=graph('S5-B')['values']==[int(n) for n in re.findall(r'(?:오전|오후)(\d+)권',body(gs('S5-B')))] and graph('S5-B')['unit']=='권' and graph('S5-B')['legendOverride']=='별 1개 = 5명' and mc('S5-B')=='별 한 개의5명이라는 단위를5권으로'
        numeric_checks['G4_S6A_fresh_transfer_values']=graph('S6-A')['values']==[int(n) for n in re.findall(r'(?:장바구니|나 모둠은)(\d+)개',body(gs('S6-A')))]==[8,14] and graph('S6-A')['symbolValue']==2 and '14개로 가8개보다6개' in mc('S6-A')
        numeric_checks['G4_S6A_symbol_key']=[int(n) for n in re.findall(r'\d+',answer('S6-A','matching'))]==[4,8,7,14]
        numeric_checks['G4_S6B_distinct_units_source']=[g['unit'] for g in gs('S6-B')['graphs']]==['권','명'] and graph('S6-B')['values']==[int(n) for n in re.findall(r'(?:오전|오후)(\d+)권',body(gs('S6-B')))] and graph('S6-B',1)['values']==[int(n) for n in re.findall(r'(?:오전|오후)(\d+)명',body(gs('S6-B')))]
        numeric_checks['G4_S6B_table_key']=[int(n) for n in re.findall(r'\d+',answer('S6-B','table_completion'))]==[12,6,18,9]
        writing_questions=[q for s in sets if s['microSkillId']=='plan-G2-writing-11' for q in s['questions'] if q['kind']=='writing']
        ck(len(writing_questions)==10 and all(len(q['rubric'])==2 for q in writing_questions),'G2 completion analytic criteria')
    poetry_sets=[s for s in sets if s['microSkillId']=='plan-G5-literature-06']
    if poetry_sets:
        ck(len(poetry_sets)==12 and sum(len(s.get('poems',[])) for s in poetry_sets)==14,'G5 poetry material coverage')
        writing_questions=[q for s in poetry_sets for q in s['questions'] if q['kind']=='writing']
        ck(len(writing_questions)==10 and all(len(q['rubric'])>=2 for q in writing_questions),'G5 poetry analytic criteria')
        creative=next(q for s in poetry_sets if s['stage']=='S6' and s['variant']=='B' for q in s['questions'] if q['kind']=='writing')
        ck(len(creative['rubric'])==3 and '예시와 다른 마음' in creative['planningPrompt'],'G5 poetry open creative response')
    if 'PV2-G6-oral-04-S2-A' in by_set:
        counts={'서른':30,'열두':12,'아홉':9,'세':3,'열여덟':18,'여덟':8,'다섯':5,'사십':40,'사':4,'팔':8,'두':2,'삼':3,'여섯':6,'이십사':24,'삼십이':32}
        def n(pattern,text):return counts[re.search(pattern,text)[1]]
        def oral(stage):return by_set['PV2-G6-oral-04-'+stage]
        def key(s,kind):return next(q['expectedAnswer'] for q in s['questions'] if q['kind']==kind)
        s=oral('S2-A');a,b=[p['text'] for p in s['paragraphs']]
        total=n(r'우리 반은 (\S+) 명',a);responses=n(r'(\S+) 명이 설문',a);yes=n(r'그중 (\S+) 명이',a);missing=n(r'학생이 (\S+) 명',b);other=n(r'안에서도 (\S+) 명은',b)
        numeric_checks['G6_oral_S2A_source_and_key']=[total,responses,yes,other,missing]==[int(x) for x in re.findall(r'\d+',key(s,'table_completion'))]
        numeric_checks['G6_oral_S2A_disjoint_groups']=yes+other==responses and responses+missing==total and yes<responses<total
        s=oral('S3-A');source_values=[counts[x] for x in re.findall(r'(\S+) 건',s['paragraphs'][0]['text'])]
        numeric_checks['G6_oral_S3A_observation_key']=source_values==[int(x) for x in re.findall(r'\d+',key(s,'classification'))]==[8,3]
        s=oral('S5-A');a=s['paragraphs'][0]['text']
        numeric_checks['G6_oral_S5A_sample_key']=[n(r'참여한 (\S+) 명',a),n(r'중 (\S+) 명',a)]==[int(x) for x in re.findall(r'\d+',key(s,'matching'))]==[5,3]
        s=oral('S6-B');a,b,c=[p['text'] for p in s['paragraphs']]
        participants=n(r'학생 (\S+) 명',a);minutes=n(r'각자 (\S+) 분',a);budget=n(r'금요일 (\S+) 분 모임',a);setup=n(r'합쳐 (\S+) 분',b);sessions=n(r'분씩 (\S+) 번',b);minimum=n(r'적어도 (\S+) 분',c)
        numeric_checks['G6_oral_S6B_source_constraints']=[participants,minutes,budget,setup,sessions,minimum]==[12,4,40,8,2,3]
        numeric_checks['G6_oral_S6B_one_session_infeasible']=participants*minutes+setup==56>budget and participants*minimum+setup==44>budget
        q=s['questions'][0];chosen=q['options'][q['correctIndex']]['text']
        per_group=n(r'(\S+) 명씩',chosen);per_person=n(r'(\S+) 분 발표',chosen);proposed_setup=n(r'정리 (\S+) 분',chosen);groups=n(r'(\S+) 모임에',chosen)
        numeric_checks['G6_oral_S6B_choice_feasible']=per_group*groups==participants and groups<=sessions and per_person>=minimum and proposed_setup==setup and per_group*per_person+proposed_setup<=budget
        numeric_checks['G6_oral_S6B_table_equations']=[int(x) for x in re.findall(r'\d+',key(s,'table_completion'))]==[participants,minutes,participants*minutes,participants*minutes,setup,participants*minutes+setup,per_group,per_person,setup,per_group*per_person+setup]
        spoken=key(s,'spoken_response')
        numeric_checks['G6_oral_S6B_spoken_plan']=n(r'에 (\S+) 명씩',spoken)==per_group and n(r'명씩 (\S+) 분',spoken)==per_person and n(r'합쳐 (\S+) 분',spoken)==per_group*per_person+setup
    for label,ok in numeric_checks.items():ck(ok,label+' mismatch')
    near=[]
    previous=json.loads((ROOT/'data/content_authoring/batch_03/units.json').read_text(encoding='utf-8'))['units']
    comparison=[(s['id'],' '.join(p['text'] for p in s['paragraphs'])) for s in sets]
    old=[(u['material']['id'],' '.join(p['text'] for p in u['material']['paragraphs'])) for u in previous]
    for path in comparison_sources:
        old.extend((s['id'],' '.join(p['text'] for p in s['paragraphs'])) for s in json.loads(Path(path).read_text(encoding='utf-8'))['sets'])
    for i,(aid,a) in enumerate(comparison):
        for bid,b in comparison[i+1:]+old:
            # A shingle screen avoids treating shared function words as content reuse.
            aa={a[j:j+4] for j in range(len(a)-3)};bb={b[j:j+4] for j in range(len(b)-3)}
            similarity=len(aa&bb)/max(1,len(aa|bb))
            if similarity>.35:near.append(dict(a=aid,b=bid,shingleJaccard=round(similarity,3)))
    unique_skills={s['microSkillId'] for s in sets}
    snapshot=hashlib.sha256(source.read_bytes()).hexdigest()
    audio_verified=set();audio_report=out/'audio/listening-verification.json'
    if audio_report.exists():
        audio=json.loads(audio_report.read_text(encoding='utf-8'))
        if audio.get('passed') and audio.get('contentSnapshotHash')==snapshot:
            for asset in audio['assets']:
                path=ROOT/asset['path']
                if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest()==asset['sha256']:audio_verified.add(asset['materialId'])
    manifest=[]
    for sid in selected_ids:
        sk=skills[sid];ss=[s for s in sets if s['microSkillId']==sid]
        manifest.append(dict(skillId=sid,grade=sk['grade'],track=sk['track'],name=sk['name'],
          targetSets=sum(expected_stage_counts[sid].values()),authoredSets=len(ss),authoredQuestions=sum(len(s['questions']) for s in ss),approvedSets=0,
          audioDraftAssets=sum(s['id'] in audio_verified for s in ss),
          assetRequirement='음성·발화 관찰 필요' if sk['track']=='oral' or sid=='plan-G1-language-03' else '텍스트 또는 실제 도표 자산',
          status='draft_under_review' if ss else 'not_authored'))
    progress=dict(scope=f'{len(selected_ids)}수행의 선언한 단계·자료 공급',expectedStageCounts=expected_stage_counts,targetSets=target_sets,targetQuestions=target_questions,
      authoredSets=len(sets),authoredQuestions=sum(len(s['questions']) for s in sets),approvedSets=0,
      remainingSets=target_sets-len(sets),remainingQuestions=target_questions-sum(len(s['questions']) for s in sets),skills=manifest)
    progress['audioDraftSetsTechnicallyVerified']=len(audio_verified)
    progress['listeningAudioDraftSets']=sum(s['id'] in audio_verified and bool(s.get('listening')) for s in sets)
    progress['readingModelAudioDraftSets']=sum(s['id'] in audio_verified and bool(s.get('reading')) for s in sets)
    out.mkdir(parents=True,exist_ok=True)
    report=dict(passed=not errors,errors=errors,stageFitWarnings=warnings,optionLengthCandidates=length_candidates,nearDuplicateCandidates=near,numericChecks=numeric_checks,readingChecks=reading_checks,
      contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),
      curriculumSourceCheckedSets=sum(bool(s['source'].get('officialStandards')) for s in sets),
      factualSourceCheckedDraftSets=sum(bool(s['source'].get('factChecks')) for s in sets),factualAnchors=sum(len(s['source'].get('factChecks',[])) for s in sets),
      curriculumSourceScopeAuditedSets=sum(bool(s['source'].get('curriculumAudit')) for s in sets),curriculumSourceLinkedSets=sum(bool(s['source'].get('officialStandards') or s['source'].get('curriculumAudit')) for s in sets),curriculumRelatedOnlySets=sum(bool(s['source'].get('curriculumAudit')) and not s['source'].get('officialStandards') for s in sets),
      graphCount=sum(len(s.get('graphs',[])) for s in sets),graphEvidenceReferences=sum(e.get('evidenceKind')=='graph' for s in sets for q in s['questions'] for e in q['evidence']),
      poemCount=sum(len(s.get('poems',[])) for s in sets),poetryLineCount=sum(len(p['lines']) for s in sets for p in s.get('poems',[])),
      listeningSets=sum(bool(s.get('listening')) for s in sets),spokenResponseTasks=sum(q['kind']=='spoken_response' for s in sets for q in s['questions']),audioEvidenceReferences=sum(e.get('evidenceKind')=='audio' for s in sets for q in s['questions'] for e in q['evidence']),audioDraftSetsTechnicallyVerified=len(audio_verified),
      oralReadingSets=sum(bool(s.get('reading')) for s in sets),oralReadingTasks=sum(q['kind']=='oral_reading' for s in sets for q in s['questions']),readingWordReferences=sum(len(s['reading']['words']) for s in sets if s.get('reading')),
      writingProductionProtocolSets=sum(bool(s.get('writingProtocol')) for s in sets),
      literaryInterpretationProtocolSets=sum(bool(s.get('literaryReview')) for s in sets),
      mediaReadingProtocolSets=sum(bool(s.get('mediaReview')) for s in sets),mediaPanelCount=sum(len(s.get('mediaPanels',[])) for s in sets),
      questionKinds=dict(collections.Counter(q['kind'] for s in sets for q in s['questions'])),progress=progress,
      limits=['자동 검사는 문항 정답 유일성이나 실제 난도를 증명하지 않는다.','독립 교사 검토·학생 수행 검증·음성 자산은 별도 완료 조건이다.'])
    (out/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    (source.parent/'progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='progress'},ensure_ascii=False,indent=2))
    print('Authored:',progress['authoredSets'],progress['authoredQuestions'],'Remaining:',progress['remainingSets'],progress['remainingQuestions'])
    if errors:raise SystemExit(1)
    return report

if __name__=='__main__':validate()
