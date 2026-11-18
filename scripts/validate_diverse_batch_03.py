"""Independent artifact checks, not teacher approval or difficulty calibration."""
from pathlib import Path
import json, hashlib, collections, difflib

ROOT=Path(__file__).resolve().parents[1]

def validate():
    raw=json.loads((ROOT/'data/content_authoring/batch_03/units.json').read_text(encoding='utf-8'))
    units=raw['units']; errors=[]; ids=set(); hashes={}; warnings=[]
    def check(condition,message):
        if not condition:errors.append(message)
    check(len(units)==24,'Expected 24 units')
    check(collections.Counter(u['grade'] for u in units)=={g:4 for g in range(1,7)},'Grade coverage')
    goals=set()
    for path in (ROOT/'data/item_bank').glob('g*_item_bank.json'):
        d=json.loads(path.read_text(encoding='utf-8-sig'))
        goals.update(x['slot_id'] for x in d['expository_slots']);goals.update(x['code'] for x in d['common_slots'])
    for u in units:
        check(u['goalId'] in goals,u['id']+' unknown goal')
        check(u['review']['teacherReview']=='pending' and u['review']['publication']=='unpublished',u['id']+' false approval')
        mats=[u['material'],u['challenge']['material']]+[c['material'] for c in u['checks']]
        byid={m['id']:m for m in mats}
        for m in mats:
            check(m['id'] not in ids,m['id']+' duplicate');ids.add(m['id'])
            text='\n'.join(p['text'] for p in m['paragraphs'])
            h=hashlib.sha256(text.encode()).hexdigest()
            check(h==m['contentHash'],m['id']+' hash mismatch')
            check(h not in hashes,m['id']+' identical material');hashes[h]=m['id']
            check(m['charCount']==len(' '.join(p['text'] for p in m['paragraphs'])),m['id']+' char count')
            for t in m.get('tables',[]):
                check(all(len(row)==len(t['headers']) for row in t['rows']),t['id']+' table shape')
            for p in m['paragraphs']:
                for s in p['sentences']:
                    check(s['id'] not in ids,s['id']+' duplicate');ids.add(s['id'])
        questions=u['questions']+[c['question'] for c in u['checks']]+[u['challenge']['question']]
        for q in questions:
            check(q['id'] not in ids,q['id']+' duplicate');ids.add(q['id'])
            check(q['prompt'] and q['evidence'],q['id']+' incomplete')
            if q['kind']=='single_choice':
                n=3 if u['grade']<=2 else 4 if u['grade']<=4 else 5
                check(len(q['options'])==n,q['id']+' option count')
                check(len({x['text'] for x in q['options']})==n,q['id']+' duplicate options')
                check(0<=q['correctIndex']<n,q['id']+' answer range')
                check(all(o['reason'] for o in q['options']),q['id']+' missing reasons')
            else:
                check(q['expectedAnswer'] and q['rubric'],q['id']+' missing answer/rubric')
                check(all(set(r['levels'])=={'0','1','2'} for r in q['rubric']),q['id']+' rubric levels')
            for e in q['evidence']:
                m=byid.get(e['passageId'])
                s=next((s for p in m['paragraphs'] for s in p['sentences'] if s['id']==e['sentenceId']),None) if m else None
                check(s is not None and e['quote'] in s['text'],q['id']+' quote mismatch')
                if s:check(s['text'][e['start']:e['start']+len(e['quote'])]==e['quote'],q['id']+' quote offset')
        check(u['challenge']['material']['familyId']==u['material']['familyId'],u['id']+' challenge exposure family')
        for c in u['checks']:
            check(c['material']['familyId']!=u['material']['familyId'],u['id']+' new material family')
            check(not c['question']['hints'] and c['question']['feedbackVisibility']=='after_first_response',u['id']+' pre-answer help')
        for m in u['model']:
            check(any(m['evidence']['quote'] in p['text'] for p in u['material']['paragraphs']),u['id']+' model quote')
        for q in u['questions']:
            if q['kind']=='writing':check(len(q['workflow'])==5,u['id']+' writing workflow')
    # Recompute the numerically consequential examples independently of the authoring helper.
    source_tables={u['id']:u['material']['tables'][0]['rows'] for u in units if u['material'].get('tables')}
    avg_rows=source_tables['B03-G5-01'];rate_rows=source_tables['B03-G5-02'];power_rows=source_tables['B03-G6-02'];report_rows=source_tables['B03-G6-04']
    calculations={
      'G3_graph':4*2==2*4==8 and 6*2==3*4==12,
      'G3_half_symbol':2*4+4/2==10,
      'G4_votes_update':11+1==10+2==12,
      'G4_source_total':30+20==50 and 30-5+20==45,
      'G5_average':all(sum(r[1:])/len(r[1:])==5 for r in avg_rows),
      'G5_average_update':sum([2,2,2,14,5])/5==5,
      'G5_rates':[r[3]/r[2]*100 for r in rate_rows]==[10,15],
      'G5_box_weight':200+800==1000 and 350+400==750,
      'G6_power':[r[1]-r[2]+r[3] for r in power_rows]==[80,85] and 100-30+5==75,
      'G6_satisfaction':8/10*100==80 and 60/100*100==60,
      'G6_report':[r[2]/r[1]*100 for r in report_rows]==[30,50] and 10/25*100==40,
      'G6_new_rates':20/50*100==40 and 12/20*100==60 and 24/40*100==60,
    }
    for k,v in calculations.items():check(v,k+' calculation')
    # Duplicate screening excludes the deliberately shared standard/challenge family.
    unique=[m for u in units for m in [u['material']]+[c['material'] for c in u['checks']]]
    candidates=[]
    for i,a in enumerate(unique):
        for b in unique[i+1:]:
            ta=' '.join(p['text'] for p in a['paragraphs']);tb=' '.join(p['text'] for p in b['paragraphs'])
            ratio=difflib.SequenceMatcher(None,ta,tb,autojunk=False).ratio()
            if ratio>.65:candidates.append(dict(a=a['id'],b=b['id'],similarity=round(ratio,3)))
    kinds=collections.Counter(q['kind'] for u in units for q in u['questions']+[c['question'] for c in u['checks']]+[u['challenge']['question']])
    report=dict(passed=not errors,errors=errors,duplicateCandidates=candidates,calculationChecks=calculations,
        counts=dict(units=len(units),uniqueMaterialFamilies=len(unique),displayMaterials=len(units)*4,questions=sum(kinds.values()),clinics=len(units),
                    byGrade=dict(collections.Counter(u['grade'] for u in units)),bySubject=dict(collections.Counter(u['subject'] for u in units)),questionKinds=dict(kinds)),
        limitations=['자동 검사는 정답 유일성·학년 적합성의 교사 검토나 학생 난도 보정을 대신하지 않음.'],
        approval='unpublished; teacher_review_pending; no_student_calibration')
    out=ROOT/'output/content-batch-03';out.mkdir(parents=True,exist_ok=True)
    (out/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if errors:raise SystemExit(1)
    return report

if __name__=='__main__':validate()
