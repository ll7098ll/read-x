from pathlib import Path
import collections, hashlib, html, json, re
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/curriculum_2022'
OUT=ROOT/'outputs/01a138a0-43ff-7451-bf36-fcef9c677ac6'
OUT.mkdir(parents=True,exist_ok=True)
registry=json.loads((DATA/'curriculum_registry.json').read_text(encoding='utf-8'))
standards=json.loads((DATA/'achievement_standards.json').read_text(encoding='utf-8'))
drafts=[]
for draft_file in sorted(DATA.glob('passage_drafts_batch_*.json')):
 batch=draft_file.stem.rsplit('_',1)[-1]
 for draft in json.loads(draft_file.read_text(encoding='utf-8')):
  draft['batch']=batch
  drafts.append(draft)
raw=json.loads((ROOT/'webapp/src/data/commercialMasterData.json').read_text(encoding='utf-8'))
goals={s['slot_id']:s for s in raw['expository_slots_96']}
legacy=[]
for s in raw['expository_slots_96']:
    p=s['real_csat_test']
    paras=[re.sub('<[^>]+>','',x) for x in p['paragraphs']]
    legacy.append({'id':f"passage:{s['slot_id']}:001",'version':1,'grade':s['grade_num'],'semester':None,
      'subject':s['curriculum_concept']['subject'],'conceptNames':[s['curriculum_concept']['concept']],
      'goalIds':[s['slot_id']],'title':p['passage_title'],'paragraphs':paras,'charCount':sum(map(len,paras)),
      'origin':'기존 자료','purpose':'legacy_unclassified','reviewState':'needs_review',
      'sourceNote':'기존 JSON의 소재·학년 주장 보존. 공식 개념 매핑 및 사실·난도 재검수 필요.',
      'contentHash':hashlib.sha256('\n'.join(paras).encode()).hexdigest()})
for d in drafts:
    assert all(g in goals for g in d['goalIds'])
    d['origin']='신규 집필'
    d['goalName']=goals[d['goalIds'][0]]['sub_skill_name']
    d['legacyPerformanceGoal']=goals[d['goalIds'][0]]['mager_goal']
    d['rubricNote']=('문항별 관찰 준거와 도움 수준을 기록합니다. 교사 검토·학생 반응 보정 전이며 전체 숙달을 자동 판정하지 않습니다.' if 'diagnostic' in d else '세부목표 계열 연결 후보. 기존 수행 준거 전체와 새 지문 활동의 일치 검토 필요.')
all_passages=drafts+legacy
assert len({p['id'] for p in all_passages})==len(all_passages)
assert len({p['contentHash'] for p in all_passages})==len(all_passages)
for pair_id in {p['pairId'] for p in drafts}:
  pair=[p for p in drafts if p['pairId']==pair_id]
  assert len(pair)==2
  assert pair[0]['goalIds']==pair[1]['goalIds']
  assert {p['purpose'] for p in pair}=={'guided_practice','transfer_check'}
  assert len({p['conceptNames'][0] for p in pair})==2
  for p in pair:
   assert p['teacherThinkingModel']['evidenceQuote'] in '\n'.join(p['paragraphs'])
   assert p['independentCheck']['evidenceQuote'] in '\n'.join(p['paragraphs'])
   assert p['reviewState'] in ('needs_review','editorial_checked_needs_teacher_review') and p['publicationState']=='unpublished'
corpus={'schemaVersion':'1.0','asOf':'2026-10-14','passages':all_passages,
 'counts':{'newDrafts':len(drafts),'legacyDrafts':len(legacy),'uniqueTexts':len(all_passages),'approved':0},
 'note':'초안 수량. 판매용 검수 완료 수량이 아니며 앱 게시 데이터로 자동 반영하지 않음.'}
(DATA/'passage_corpus.json').write_text(json.dumps(corpus,ensure_ascii=False,indent=2),encoding='utf-8')
queue=[]
for concept in registry['concepts']:
    linked=[p for p in drafts if concept['id'] in p['conceptIds']]
    queue.append({'conceptId':concept['id'],'subject':concept['subject'],'conceptName':concept['name'],
      'candidatePlacementIds':concept['placements'],'existingNewDraftIds':[p['id'] for p in linked],
      'writingState':'draft_needs_review' if linked else 'not_started',
      'nextAction':'개념·학기·세부목표 검수' if linked else '학기 배치와 읽기 세부목표를 확인한 뒤 첫 지문 집필',
      'scopeNote':'집필 계획 항목이며 지문 수량에 포함하지 않음. 기존 96편은 개념 연결 재검수 전이므로 차감하지 않음.'})
(DATA/'passage_writing_queue.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf-8')
# Structural checks are not educational validation.
verification={'standards':len(standards),'subjectCount':len({s['subject'] for s in standards}),
 'semesterSubjectPlacements':len(registry['placements']),'conceptCandidates':len(registry['concepts']),
 'newDrafts':len(drafts),'existingDrafts':len(legacy),'uniqueFullTexts':len(all_passages),'approvedFullTexts':0,
 'referenceChecks':'all referenced standard and goal IDs exist; new passage evidence quotes occur in text',
 'pairChecks':f"{len({p['pairId'] for p in drafts})} pairs, two concepts and one literacy goal per pair",
 'unassignedStandards':registry['unmappedStandardIds'],
 'charCountsByGrade':{str(g):[min(d['charCount'] for d in drafts if d['grade']==g),max(d['charCount'] for d in drafts if d['grade']==g)] for g in range(1,7)},
 'limits':['난도와 교육 효과 미보정','교과 개념-성취기준의 개별 대응 검수 필요','학기 배치안은 전국 공통 확정표가 아님','사회·음악 일부개정 각론 대조 미완료']}
(OUT/'verification.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2),encoding='utf-8')

def esc(x):return html.escape(str(x))
def options(values):return ''.join(f'<option value="{esc(v)}">{esc(v)}</option>' for v in values)
def subject_tags(subject):
 tags=[name for name in sorted({s['subject'] for s in standards}) if name in subject]
 if '통합' in subject:tags.append('통합교과')
 return ','.join(tags)
purpose={'guided_practice':'함께 배우기','transfer_check':'새 글에서 확인','legacy_unclassified':'기존 자료 · 용도 미분류'}
placement_cards=[]
for p in registry['placements']:
 source=registry['sources'][p['placementSourceId']]
 placement_cards.append(f'''<article class="concept-card searchable" data-grade="{p['grade']}" data-term="{p['semester']}" data-subject="{esc(p['subject'])}">
 <div class="meta">{p['grade']}학년 {p['semester']}학기 · {esc(p['subject'])}</div><h3>{esc(p['units'])}</h3>
 <p class="status">{esc(p['placementStatus'])}</p><div class="chips">{''.join('<span>'+esc(n)+'</span>' for n in p['conceptNames'])}</div>
 <details><summary>배치 근거와 성취기준 묶음</summary><p><a href="{esc(source['url'])}" target="_blank" rel="noreferrer">{esc(source['title'])}</a> · {esc(source['scope'])}</p><p>{esc(', '.join(p['relatedStandardIds']))}</p><p>개별 개념과 각 성취기준의 일대일 대응은 검수 전입니다.</p></details></article>''')
passage_cards=[]
for p in all_passages:
 table=p.get('table'); table_html=''
 if table:
  table_html='<table><caption>'+esc(table['caption'])+'</caption><thead><tr>'+''.join('<th>'+esc(x)+'</th>' for x in table['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(c)+'</td>' for c in r)+'</tr>' for r in table['rows'])+'</tbody></table>'
 teaching=''
 if p['origin']=='신규 집필':
  t=p['teacherThinkingModel'];q=p['independentCheck']
  teaching=f'''<details class="teacher"><summary>교사용 사고 시범·확인 질문·쓰기 과제</summary>
    <p class="status">{'함께 배우는 글에서 시범으로 활용' if p['purpose']=='guided_practice' else '새 글 확인에서는 응답 전에 이 안내를 보여 주지 않음'}</p>
    <h4>본문 단서</h4><blockquote>{esc(t['evidenceQuote'])}</blockquote><h4>생각을 연결하는 시범</h4><p>{esc(t['reasoning'])}</p>
    <h4>확인 질문</h4><p>{esc(q['prompt'])}</p><h4>기대 응답</h4><p>{esc(q['expectedAnswer'])}</p><h4>자기 말로 쓰기</h4><p>{esc(p['writingPrompt'])}</p>
    <p class="muted">{esc(p['rubricNote'])} 단일 응답으로 숙달을 확정하지 않습니다.</p></details>'''
 term=f"{p['semester']}학기" if p['semester'] else '학기 미확인'
 if p.get('batch')=='02':
  teaching+=f'<p><a href="reading-workshop-batch-02.html#{esc(p["id"])}">이 지문의 진단 문항·사고 활동·관찰 기록 열기</a></p>'
 passage_cards.append(f'''<article id="{esc(p['id'])}" class="passage searchable" data-grade="{p['grade']}" data-term="{p['semester'] or ''}" data-subject="{esc(subject_tags(p['subject']))}" data-origin="{esc(p['origin'])}">
  <div class="meta">{p['grade']}학년 · {term} · {esc(p['subject'])} · {purpose[p['purpose']]}</div><h2>{esc(p['title'])}</h2>
  <p class="status">{esc(p['origin'])} · 검수 전 · {p['charCount']}자(공백 포함, 표 제외)</p>
  <p class="muted">소재: {esc(', '.join(p['conceptNames']))} / 목표 계열: {esc(', '.join(p['goalIds']))}</p>
  {''.join('<p class="body">'+esc(s)+'</p>' for s in p['paragraphs'])}{table_html}{teaching}</article>''')
standard_rows=''.join(f'<tr class="searchable" data-grade="{s["gradeBand"][0]},{s["gradeBand"][1]}" data-term="" data-subject="{esc(s["subject"])}"><td>{esc(s["id"])}</td><td>{esc(s["subject"])}</td><td>{s["gradeBand"][0]}~{s["gradeBand"][1]}</td><td>{esc(s["area"])}</td><td>{esc(s["statement"])}</td><td>{esc(s["sourceId"])}<br>추출문 {s["sourceLine"]}행</td></tr>' for s in standards)
source_links=''.join(f'<li><a href="{esc(s["url"])}" target="_blank" rel="noreferrer">{esc(s["title"])}</a> — {esc(s["scope"])}</li>' for s in registry['sources'].values())
page='''<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>교과 개념과 읽기 지문 원장</title>
<style>
:root{font-family:"Malgun Gothic",sans-serif;color:#24343b;background:#f5f4ef}*{box-sizing:border-box}body{margin:0}header{background:#173f43;color:#fff;padding:36px max(24px,calc((100vw - 1180px)/2))}h1{font-size:30px;margin:8px 0 16px}header p{max-width:850px;line-height:1.8;color:#d4e4df}.eyebrow{font-size:12px;letter-spacing:2px}.stats{display:flex;gap:32px;flex-wrap:wrap}.stats strong{font-size:27px;display:block}.stats span{font-size:13px;color:#d4e4df}main{max-width:1228px;margin:auto;padding:24px}.note{background:#fff5dc;border-left:4px solid #cc9b3d;padding:16px;line-height:1.8;font-size:14px}.tools{position:sticky;top:0;z-index:2;background:#f5f4ef;padding:14px 0;border-bottom:1px solid #d2ddd8}.tabs,.filters{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}button,input,select{font:inherit;border:1px solid #bfccc8;border-radius:8px;padding:10px 14px;background:white}button{cursor:pointer}button[aria-selected=true]{background:#173f43;color:white}input{flex:1;min-width:180px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}.concept-card,.passage{background:white;border:1px solid #d9e1dc;border-radius:14px;padding:24px}.concept-card h3{font-size:18px;line-height:1.6}.meta{font-size:13px;color:#407268;font-weight:bold}.status{font-size:13px;color:#806125}.chips{display:flex;gap:6px;flex-wrap:wrap}.chips span{font-size:13px;background:#eef4f0;padding:7px 9px;border-radius:6px}details{border-top:1px solid #dfe5e2;margin-top:18px;padding-top:14px;line-height:1.8;font-size:14px}summary{cursor:pointer;font-weight:bold}.passage{max-width:900px;margin:0 auto 24px}.passage h2{font-size:26px;line-height:1.5}.body{font-size:18px;line-height:2.05;word-break:keep-all}.muted{color:#64716e;font-size:13px;line-height:1.7}.teacher{background:#f5f8f5;padding:18px;border-radius:8px}h4{margin-bottom:4px}blockquote{border-left:3px solid #7ea299;padding:10px 14px;margin:10px 0;background:white}table{border-collapse:collapse;width:100%;background:white}th,td{text-align:left;padding:12px;border-bottom:1px solid #dde5e0;line-height:1.7}th{background:#e5eee8}caption{text-align:left;font-size:13px;padding:12px 0}.table-wrap{overflow:auto}.count{margin:10px 0 20px;font-size:14px}a{color:#246b68}.hidden,[hidden]{display:none!important}#standards td{font-size:13px;min-width:90px}#standards td:nth-child(5){min-width:420px}.sources{margin-top:35px;font-size:14px;line-height:1.8}footer{font-size:13px;line-height:1.8;padding:24px 0;color:#65756d}@media(max-width:720px){.grid{grid-template-columns:1fr}main{padding:14px}header{padding:28px 20px}h1{font-size:24px}.body{font-size:17px}.passage{padding:20px}.stats{gap:18px}.tools{position:static}}@media print{.tools,header,.note,.count,.sources,footer{display:none}.passage{break-after:page;border:0}.teacher{break-inside:avoid}body{background:white}}
</style><header><div class="eyebrow">READX-RAY · CONTENT LIBRARY · 2026.10.14</div><h1>교과 개념에서 읽기 사고 과정으로</h1><p>학년과 학기를 살펴 소재를 고르고, 같은 세부목표를 다른 글에 적용합니다. 원문 근거, 학기 배치, 집필 초안을 구분해 관리하는 콘텐츠 원장입니다.</p><div class="stats"><div><strong>826</strong><span>개념·기능 후보</span></div><div><strong>611</strong><span>기준 원장의 성취기준</span></div><div><strong>24 + 96</strong><span>신규 초안 + 기존 지문</span></div><div><strong>0</strong><span>판매용 검수 완료</span></div></div></header><main>
<p class="note">학기별지도 96개 묶음 중 24개는 해당 출판사의 단원 목차 확인, 6개는 통합교과 주제 배치 확인, 66개는 편집 배치안입니다. 세부 개념 연결은 검수 전입니다. 성취기준은 2022-33호 원문 추출본이며 사회·음악의 일부개정 대조가 남아 있습니다.</p>
<div class="tools"><nav class="tabs"><button data-tab="concepts" aria-selected="true">학기별 개념 지도</button><button data-tab="passages" aria-selected="false">지문 읽기</button><button data-tab="standards" aria-selected="false">성취기준 원장</button></nav><div class="filters"><select id="grade" aria-label="학년"><option value="">모든 학년</option>GRADE</select><select id="term" aria-label="학기"><option value="">모든 학기</option><option value="1">1학기</option><option value="2">2학기</option></select><select id="subject" aria-label="교과"><option value="">모든 교과</option>SUBJECT</select><select id="origin" aria-label="지문 출처" hidden><option value="신규 집필">신규 집필 24편</option><option value="">전체 120편</option><option value="기존 자료">기존 자료 96편</option></select><input id="query" placeholder="개념, 제목, 본문, 성취기준 검색" aria-label="검색"></div></div><div id="count" class="count" aria-live="polite"></div>
<section id="concepts" class="grid">CONCEPTS</section><section id="passages" hidden>PASSAGES</section><section id="standards" hidden><p class="muted">국가 기준의 학년군 원장입니다. 학기 필터는 적용하지 않습니다. 수식 객체와 표 배열은 원본 HWP에서 확인해야 합니다.</p><div class="table-wrap"><table><thead><tr><th>코드</th><th>교과</th><th>학년군</th><th>영역</th><th>성취기준 추출문</th><th>원문 위치</th></tr></thead><tbody>STANDARDS</tbody></table></div></section>
<details class="sources"><summary>원천 자료와 적용 범위</summary><ul>SOURCES</ul><p>2026-1호에 따른 초1~2 변경 적용일은 2028년 3월 1일입니다. 이 원장은 2026년 운영 기준과 미래 개정을 구분합니다. 국어는 읽기 목표와 소재가 겹칠 수 있고, 영어 항목은 국어 지문의 소재 후보이며 영어 읽기 평가로 보지 않습니다.</p></details>
<footer>새 지문의 교사용 시범은 펼쳐서 확인할 수 있습니다. ‘새 글에서 확인’에서는 응답 전에 시범을 보여 주지 않습니다. 새 지문과 기존 지문 모두 사실·난도·세부목표 적합성 검수 후 게시해야 합니다.</footer></main>
<script>let active='concepts';const ids=['grade','term','subject','origin','query'];const el=id=>document.getElementById(id);function filter(){let count=0;const grade=el('grade').value,term=el('term').value,subject=el('subject').value,origin=el('origin').value,q=el('query').value.trim().toLowerCase();document.querySelectorAll('#'+active+' .searchable').forEach(card=>{const ok=(!grade||(card.dataset.grade||'').split(',').includes(grade))&&(!term||active==='standards'||card.dataset.term===term)&&(!subject||(card.dataset.subject||'').split(',').includes(subject))&&(!q||card.textContent.toLowerCase().includes(q))&&(active!=='passages'||!origin||card.dataset.origin===origin);card.hidden=!ok;if(ok)count++});el('count').textContent=count+'개 '+(active==='passages'?'지문':active==='standards'?'성취기준':'학년·학기·교과 묶음')+' 표시';}document.querySelectorAll('[data-tab]').forEach(button=>button.addEventListener('click',()=>{active=button.dataset.tab;document.querySelectorAll('[data-tab]').forEach(b=>b.setAttribute('aria-selected',String(b===button)));['concepts','passages','standards'].forEach(id=>el(id).hidden=id!==active);el('origin').hidden=active!=='passages';el('term').disabled=active==='standards';filter()}));ids.forEach(id=>el(id).addEventListener(id==='query'?'input':'change',filter));filter();</script></html>'''
for k,v in {'GRADE':''.join(f'<option value="{g}">{g}학년</option>' for g in range(1,7)),
 'SUBJECT':options(sorted({s['subject'] for s in standards}|{'통합교과'})), 'CONCEPTS':''.join(placement_cards),
 'PASSAGES':''.join(passage_cards),'STANDARDS':standard_rows,'SOURCES':source_links}.items():page=page.replace(k,v)
page=page.replace('24 + 96',f'{len(drafts)} + {len(legacy)}').replace('신규 집필 24편',f'신규 집필 {len(drafts)}편').replace('전체 120편',f'전체 {len(all_passages)}편')
page=page.replace('<main>','<main><p><a href="reading-workshop-batch-02.html">새로 추가한 24편의 진단·읽기 활동 수업자료 열기</a></p>',1)
(OUT/'curriculum-library.html').write_text(page,encoding='utf-8')
print(json.dumps(verification,ensure_ascii=False,indent=2))
