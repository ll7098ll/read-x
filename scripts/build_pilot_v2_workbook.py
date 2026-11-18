"""Render separate student/teacher HTML and text artifacts without a server."""
from pathlib import Path
import json,html,base64,hashlib
ROOT=Path(__file__).resolve().parents[1]
esc=lambda x:html.escape(str(x),quote=True)
LABELS=dict(single_choice='선택',matching='짝짓기',explanation='설명',classification='분류',evidence_selection='근거 찾기',writing='쓰기',table_completion='표 정리',ordering='순서',question_generation='질문 만들기',revision='고쳐쓰기',spoken_response='직접 말하기',oral_reading='소리 내어 읽기')
CSS='''
*{box-sizing:border-box}body{margin:0;background:#f3f6f8;color:#20384b;font-family:system-ui,"Malgun Gothic",sans-serif}header{background:#173b49;color:white;padding:30px max(24px,calc((100% - 1100px)/2))}h1{font-size:28px}header p{color:#deeaed;line-height:1.8}.toolbar{max-width:1100px;margin:20px auto;display:flex;gap:14px;flex-wrap:wrap;padding:0 16px}select,button,textarea{font:inherit}select,button{padding:10px;border:1px solid #bbcbd3;background:white;color:#20384b;border-radius:8px}main{max-width:1100px;margin:20px auto;padding:0 16px}.set{background:white;border:1px solid #d7e1e6;border-radius:16px;padding:28px;margin:24px 0}.meta{font-size:14px;color:#4d6774}.text{background:#fffcf4;padding:20px;border-radius:12px;margin:22px 0}.text p{font-size:20px;line-height:2.05;margin:12px 0}h2{font-size:24px}h3{font-size:18px;line-height:1.8}.question{border-top:1px solid #dce5e8;padding:18px 0}label.choice{display:block;line-height:1.9;padding:8px 12px;border:1px solid #d5e0e5;border-radius:8px;margin:8px 0}label.choice:has(input:checked){background:#e6f2ee;border-color:#236958}textarea{display:block;width:100%;min-height:95px;border:1px solid #afc2cd;border-radius:8px;padding:12px;line-height:1.8;margin:8px 0 16px}details{background:#edf4f6;border-radius:10px;padding:14px;margin:12px 0;line-height:1.9}summary{cursor:pointer;font-weight:600}table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}td,th{border:1px solid #c3d2d9;text-align:left;vertical-align:top;padding:10px}ol li{line-height:1.85}button:focus-visible,select:focus-visible,input:focus-visible,textarea:focus-visible,summary:focus-visible{outline:3px solid #bd6800;outline-offset:3px}#status{padding:0 16px;max-width:1100px;margin:auto;color:#765000}footer{text-align:center;font-size:14px;padding:24px;color:#4d6774}[hidden]{display:none!important}@media(max-width:650px){.set{padding:18px}.text{padding:15px}.text p{font-size:19px}header{padding:20px}}@media print{header,.toolbar,#status,footer{display:none}body{background:white}.set{border:0;padding:0;break-before:page}.question{break-inside:avoid}.text p{font-size:12pt}textarea{min-height:85px}}
'''
CSS+='figure.graph{margin:20px 0;padding:12px;border:1px solid #d2e0e5;border-radius:12px;text-align:center;break-inside:avoid}figure.graph img{display:block;width:100%;max-width:740px;height:auto;margin:auto}figcaption{font-size:14px;color:#526775;line-height:1.7}'
CSS+='.media-panel{margin:24px 0;border:1px solid #b9cdd6;padding:16px;border-radius:12px;break-inside:avoid}.media-panel img{width:100%;max-width:900px;height:auto;display:block;margin:auto}.media-alternative{font-size:18px;line-height:1.8;border-top:1px solid #ccdce3;margin-top:16px;padding-top:12px}.media-alternative p{margin:8px 0}'
CSS+='.poem{margin:12px 0 26px;padding:18px 24px;border-left:3px solid #91b5b3;break-inside:avoid}.poem h3{margin:0 0 20px;color:#28585d}.text p.poem-line{margin:0;line-height:1.85;white-space:pre-wrap}@media(max-width:650px){.poem{padding:14px 12px}}'
CSS+='.listening-player{padding:16px;background:#eef6f6;border:1px solid #bdd6d8;border-radius:12px;margin:18px 0}.listening-player audio{width:100%;margin:10px 0}.observation-line{min-height:40px;border-bottom:1px dotted #8197a3;line-height:1.8}'
CSS+='.reading-target p.reading-line{font-size:27px;line-height:2;letter-spacing:.04em;word-spacing:.18em;margin:16px 0}.reading-label{font-size:15px;color:#4e6b74;margin:18px 0 4px}.reading-model audio{display:block;width:100%;margin:12px 0}.reading-observation td{min-width:90px;height:45px}@media print{.reading-target p.reading-line{font-size:17pt}.reading-model audio{display:none}}'
JS='''
const skill=document.getElementById('skill'),stage=document.getElementById('stage'),status=document.getElementById('status');
function filter(){let n=0;document.querySelectorAll('.set').forEach(s=>{s.hidden=!!((skill.value&&s.dataset.skill!==skill.value)||(stage.value&&s.dataset.stage!==stage.value));if(!s.hidden)n++});status.textContent=n+'개 자료 묶음 표시'}skill.onchange=filter;stage.onchange=filter;
let saved={};try{const x=JSON.parse(localStorage.getItem('readx-pilot-v2')||'{}');if(x&&typeof x==='object'&&!Array.isArray(x))saved=x}catch{status.textContent='저장 기록을 불러오지 못했습니다.'}
document.querySelectorAll('[data-response]').forEach(el=>{const key=el.dataset.response;if(el.type==='radio')el.checked=saved[key]===el.value;else el.value=saved[key]||'';el.addEventListener('input',()=>{saved[key]=el.value;try{localStorage.setItem('readx-pilot-v2',JSON.stringify(saved))}catch{status.textContent='브라우저 저장이 제한됩니다. 인쇄나 답안 내려받기를 이용하세요.'}})});
document.getElementById('download').onclick=()=>{const blob=new Blob([JSON.stringify({source:'pilot-v2',savedAt:new Date().toISOString(),responses:saved},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='국어_단계별_연습_답안.json';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500)};
const expand=document.getElementById('expand');if(expand)expand.onclick=()=>{document.querySelectorAll('details').forEach(d=>d.open=true)};
'''

def questions_in_order(s):
 byid={q['id']:q for q in s['questions']}
 return [byid[qid] for qid in s.get('presentationOrder',list(byid))]

def material_html(s,teacher=False):
 if s.get('reading'):
  reading=s['reading'];parts=['<div class="text reading-target"><p>'+esc(reading['studentInstruction'])+'</p>']
  for p in s['paragraphs']:
   if p['id'] in reading['displayLabels']:parts.append('<div class="reading-label">'+esc(reading['displayLabels'][p['id']])+'</div>')
   parts.append('<p class="reading-line" data-reading-line="'+esc(p['id'])+'">'+esc(p['text'])+'</p>')
  parts.append('</div>');return ''.join(parts)
 if s.get('listening'):
  result='<div class="text"><p>'+esc(s['listening']['studentInstruction'])+'</p><p>음성을 듣고 선생님이나 짝에게 직접 말하세요. 인쇄한 자료는 선생님이 안내를 읽어 줍니다.</p></div>'
  if teacher:result+='<details class="listening-transcript"><summary>교사용 듣기 대본 · 학생에게 사전 제시하지 않음</summary>'+''.join('<p>'+esc(p['text'])+'</p>' for p in s['paragraphs'])+'</details>'
  return result
 byheading={p['headingParagraphId']:p for p in s.get('poems',[])}
 claimed={pid for p in s.get('poems',[]) for pid in p['lineParagraphIds']}
 rows={p['id']:p['text'] for p in s['paragraphs']};parts=['<div class="text">']
 for p in s['paragraphs']:
  if p['id'] in byheading:
   poem=byheading[p['id']]
   parts.append('<section class="poem" data-poem="'+esc(poem['id'])+'" aria-label="'+esc(poem['title'])+'"><h3>'+esc(p['text'])+'</h3>')
   parts.extend('<p class="poem-line" data-line="'+esc(pid)+'">'+esc(rows[pid])+'</p>' for pid in poem['lineParagraphIds'])
   parts.append('</section>')
  elif p['id'] not in claimed:parts.append('<p>'+esc(p['text'])+'</p>')
 parts.append('</div>');return ''.join(parts)

def build(source=None,out=None,bank_id='pilot-v2'):
 source=Path(source) if source else ROOT/'data/content_authoring/pilot_v2/sets.json'
 sets=json.loads(source.read_text(encoding='utf-8'))['sets']
 out=Path(out) if out else ROOT/'output/pilot-v2';out.mkdir(parents=True,exist_ok=True)
 manifest=json.loads((out/'graph-assets.json').read_text(encoding='utf-8')) if any(s.get('graphs') for s in sets) else dict(contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),assets=[])
 assert manifest['contentSnapshotHash']==hashlib.sha256(source.read_bytes()).hexdigest(),'Regenerate graphs for this content snapshot'
 assets={a['id']:a for a in manifest['assets']}
 media_assets={}
 if any(s.get('mediaPanels') for s in sets):
  media_manifest=json.loads((out/'media-assets.json').read_text(encoding='utf-8'))
  assert media_manifest['contentSnapshotHash']==hashlib.sha256(source.read_bytes()).hexdigest(),'Regenerate media panels'
  media_assets={a['id']:a for a in media_manifest['assets']}
 audio_assets={}
 if any(s.get('listening') or s.get('reading') for s in sets):
  listening=json.loads((out/'audio/listening-verification.json').read_text(encoding='utf-8'))
  assert listening['passed'] and listening['contentSnapshotHash']==hashlib.sha256(source.read_bytes()).hexdigest(),'Regenerate and verify listening assets'
  audio_assets={a['id']:a for a in listening['assets']}
 for teacher in [False,True]:
  name='교사용_해설집' if teacher else '학생용_문제집'
  skills={s['microSkillId']:f'초{s["grade"]} · {s["skillName"]}' for s in sets}
  stages={s['stage']:s['stageLabel'] for s in sets}
  p=['<!doctype html><html lang="ko"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',f'<title>국어 여섯 단계 {name}</title><style>{CSS}</style>',
    f'<header><h1>국어 여섯 단계 · {name.replace("_"," ")}</h1><p>뜻 익히기 · 단서 짚기 · 관계 엮기 · 의미 풀기 · 근거 따지기 · 새롭게 엮기</p><p>대표 {len(skills)}수행 / {len(sets)}자료 / {sum(len(s["questions"]) for s in sets)}문항 · 교사 검토 전 원고</p></header>',
    '<div class="toolbar"><label>수행 <select id="skill"><option value="">전체</option>'+''.join(f'<option value="{esc(k)}">{esc(v)}</option>' for k,v in skills.items())+'</select></label>',
    '<label>단계 <select id="stage"><option value="">전체</option>'+''.join(f'<option value="{esc(k)}">{esc(v)}</option>' for k,v in stages.items())+'</select></label>',
    '<button onclick="window.print()">표시한 자료 인쇄</button><button id="download">답안 내려받기</button>'+('<button id="expand">해설 모두 펼치기</button>' if teacher else '')+'</div><p id="status" role="status"></p><main>']
  for s in sets:
   p.extend([f'<article class="set" data-skill="{esc(s["microSkillId"])}" data-stage="{s["stage"]}"><div class="meta">초{s["grade"]} · {esc(s["skillName"])} · {esc(s.get("learnerStageLabel",s["stageLabel"]))} · 자료{s["variant"]}</div><h2>{esc(s["title"])}</h2>',
    material_html(s,teacher)])
   for media in s.get('mediaPanels',[]):
    asset=media_assets[media['id']];png=(ROOT/asset['png']).read_bytes()
    assert hashlib.sha256(png).hexdigest()==asset['pngHash'] and hashlib.sha256(json.dumps(media,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==asset['panelDataHash'],'Media asset changed'
    p.append('<figure class="media-panel"><img data-media="'+esc(media['id'])+'" width="'+str(asset['width'])+'" height="'+str(asset['height'])+'" alt="'+esc(media['accessibleDescription'])+'" src="data:image/png;base64,'+base64.b64encode(png).decode('ascii')+'"><figcaption>'+esc(media['title'])+' · 자체 제작 가상 자료</figcaption><div class="media-alternative" data-media-alternative="'+esc(media['id'])+'"><strong>그림 속 정보의 문자 대체</strong>')
    for element in media['elements']:
     label=(element['imageDescription']+' · ' if element.get('imageDescription') else '')+{'large':'큰 글씨: ','small':'작은 글씨: '}.get(element['style'],'')
     p.append('<p data-media-element="'+esc(media['id']+'/'+element['id'])+'">'+esc(label+element['text'])+'</p>')
    p.append('</div></figure>')
   if s['source'].get('factualReferences'):
    p.append('<p class="factual-credit" data-source-material="'+esc(s['id'])+'">바탕 자료: '+ ' · '.join('<a href="'+esc(ref['url'])+'" target="_blank" rel="noopener noreferrer">'+esc(ref['publisher']+' — '+ref['title'])+'</a>' for ref in s['source']['factualReferences'])+' · 학습용으로 재구성한 글</p>')
    if teacher:
     p.append('<details class="factual-audit"><summary>사실 근거와 학습용 적용 범위</summary>')
     for fact in s['source']['factChecks']:
      p.append('<p>'+esc(fact['sourceId']+' / '+fact['factId'])+' · '+esc(fact['checkedStatement'])+'<br>원고 연결: '+esc(fact['quote'])+(' · 정의·비교 원리의 편집상 적용' if fact['type']=='editorial_application' else '')+'</p>')
     p.append('<p>1차 자료 대조를 거친 편집 초안입니다. 실제 교과·사실 검토자의 승인과 구별하며, 글에서 가상이라고 밝힌 연습 상황을 기관의 실제 관찰 기록으로 소개하지 않습니다.</p></details>')
   if s.get('listening'):
    clip=s['listening'];asset=audio_assets[clip['id']];wav=(ROOT/asset['path']).read_bytes()
    assert asset['usage']=='listening_material' and hashlib.sha256(wav).hexdigest()==asset['sha256'] and hashlib.sha256(clip['script'].encode()).hexdigest()==asset['intendedTextHash'],'Listening asset/input changed'
    p.append('<div class="listening-player"><strong>듣기 자료</strong><audio data-listening="'+esc(clip['id'])+'" controls preload="none" aria-label="'+esc(s['title']+' 듣기 자료')+'" src="data:audio/wav;base64,'+base64.b64encode(wav).decode('ascii')+'">음성 재생을 지원하지 않는 환경에서는 선생님이 교사용 대본을 읽어 주세요.</audio></div>')
    if teacher:
     card=s['partnerCard']
     p.append('<details class="partner-card"><summary>'+esc(card.get('title','첫 질문 뒤에 사용할 응답자 카드'))+'</summary><p>'+esc(card['instruction'])+'</p><p>'+esc(card['reply'])+'</p><p>대본을 먼저 읽거나 표현 틀을 제공했다면 지원받은 수행으로 기록합니다. 목소리 크기나 빠르기만으로 말하기 수행을 판단하지 않습니다.</p></details>')
   for t in s.get('tables',[]):
    p.append('<div style="overflow-x:auto"><table><caption>'+esc(t['caption'])+'</caption><thead><tr>'+''.join('<th scope="col">'+esc(h)+'</th>' for h in t['headers'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+esc(v)+'</td>' for v in row)+'</tr>' for row in t['rows'])+'</tbody></table></div>')
   for g in s.get('graphs',[]):
    asset=assets[g['id']];svg=(ROOT/asset['svg']).read_bytes()
    assert hashlib.sha256(svg).hexdigest()==asset['svgHash'],'Graph asset changed: '+g['id']
    assert hashlib.sha256(json.dumps(g,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==asset['graphDataHash'],'Graph data changed: '+g['id']
    encoded=base64.b64encode(svg).decode('ascii')
    p.append('<figure class="graph"><img data-graph="'+esc(g['id'])+'" src="data:image/svg+xml;base64,'+encoded+'" alt="'+esc(g['accessibleDescription'])+'" width="936" height="572"><figcaption>'+esc(g['title'])+' · 자체 창작 기록</figcaption></figure>')
   if teacher:
    demand=s['taskDemand']
    p.append('<details><summary>지도 초점과 수행 조건</summary><p>'+esc(s['teacherGuide'])+'</p><p>수행: '+esc(demand['operation'])+' / 근거 거리: '+esc(demand['evidenceDistance'])+' / 지원: '+esc(demand['support'])+'</p></details>')
    if s.get('writingProtocol'):
     protocol=s['writingProtocol']
     p.append('<details class="writing-protocol" data-writing-material="'+esc(s['id'])+'"><summary>실제 쓰기 과정 관찰 · 빈 기록란</summary><p>'+esc(protocol['firstResponse'])+'</p>'+''.join('<div class="observation-line">'+esc(field)+': </div>' for field in protocol['observationFields'])+'<p>'+esc(protocol['supportPolicy'])+'</p><p>'+esc(protocol['storageLimit'])+'</p></details>')
    if s['review'].get('draftRevision'):
     revision=s['review']['draftRevision']
     p.append('<details class="draft-revision"><summary>원고 수정 이력</summary><p>v'+esc(revision['fromVersion'])+' → v'+esc(revision['toVersion'])+' · '+esc(revision['asOf'])+'</p><p>'+esc(revision['reason'])+'</p></details>')
    if s['source'].get('curriculumAudit'):
     audit=s['source']['curriculumAudit']
     p.append('<details class="curriculum-audit" data-curriculum-material="'+esc(s['id'])+'"><summary>교육과정 원문과 이번 활동의 범위</summary><p>'+esc(audit['scope'])+'</p><p>'+esc(audit['basis'])+'</p>')
     if audit['remainingGap']:p.append('<p>직접 측정 주장 보류: '+esc(audit['remainingGap'])+'</p>')
     p.append('<table><tr><th>원문·학년군</th><th>연결의 성격</th><th>이 활동과 관련된 부분</th><th>이 자료만으로 확인하지 않는 부분</th></tr>')
     for ref in audit['links']:
      p.append('<tr><td>'+esc(ref['code']+' · '+ref['subject'])+'<br>'+esc(ref['statement'])+'<br>초'+esc(ref['gradeBand'][0])+'~'+esc(ref['gradeBand'][1])+'학년군 · 고시 '+esc(ref['noticeVersion'])+'</td><td>'+esc(ref['roleLabel'])+'</td><td>'+esc(ref['includedComponent'])+'</td><td>'+esc(' / '.join(ref['notAssessed']))+'</td></tr>')
     p.append('</table><p>원문 대조와 AI 범위 검토이며 교사 승인·성취기준 전체 달성 판정이 아닙니다.</p></details>')
    elif s['source'].get('officialStandards'):
     p.append('<details><summary>교육과정 연결 후보</summary><p>'+esc(s['review']['curriculumAlignment'])+'</p>'+''.join('<p>'+esc(r['code'])+' · '+esc(r['statement'])+' (고시 '+esc(r['noticeVersion'])+', 초'+esc(r['gradeBand'][0])+'~'+esc(r['gradeBand'][1])+'학년군 원문)</p>' for r in s['source']['officialStandards'])+'</details>')
   for i,q in enumerate(questions_in_order(s),1):
    p.append(f'<section class="question" data-question="{esc(q["id"])}"><div class="meta">{LABELS[q["kind"]]} · {esc(q["id"])}</div><h3>{i}. {esc(q["prompt"])}</h3>')
    if q.get('writerContext'):
     context=q['writerContext']
     p.append('<p class="writer-context" data-writer-context="'+esc(q['id'])+'">읽는 사람: '+esc(context['reader'])+' · 쓰는 목적: '+esc(context['purpose'])+' · 분량: '+esc(context['length'])+'</p>')
    if q['kind']=='single_choice':
     for j,o in enumerate(q['options']):p.append(f'<label class="choice"><input type="radio" name="{q["id"]}" data-response="{q["id"]}" value="{j}"'+(' disabled' if teacher else '')+f'> {j+1}. {esc(o["text"])}</label>')
    else:
     fields=[('draft','내 답과 본문 근거')]
     if q['kind']=='spoken_response':
      p.append('<p class="speech-instruction">'+esc(q.get('performanceInstruction','먼저 상대에게 직접 질문하고 답을 들어 확인하세요. 아래 칸은 말한 뒤 남기는 메모이며 말하기 관찰을 대신하지 않습니다.'))+'</p>')
      fields=[('draft','말한 뒤 메모 · 선택')]
     if q['kind']=='oral_reading':
      p.append('<p class="reading-instruction">먼저 스스로 읽어요. 선생님은 실제로 읽은 말과 스스로 고친 곳을 기록해요. 모델을 듣거나 도움을 받은 뒤 읽은 말은 따로 남겨요.</p>')
      fields=[('draft','읽은 뒤 남길 메모 · 선택')]
     if q['kind']=='writing':
      p.append('<p>'+esc(q['planningPrompt'])+'</p>')
      if len(q['rubric'])>1:p.append('<p>검토할 점: '+ ' / '.join(esc(r['criterion']) for r in q['rubric'])+'</p>')
      fields=[('plan','계획'),('draft','초고'),('revision','검토 후 수정고'),('reason','고친 이유')]
     for key,label in fields:p.append(f'<label>{label}<textarea aria-label="{esc(q["id"]+" "+label)}" data-response="{q["id"]}-{key}"'+(' readonly' if teacher else '')+'></textarea></label>')
    if teacher:
     p.append('<details><summary>정답·예시 답과 검토 기준</summary>')
     if q['kind']=='single_choice':
      p.append(f'<p>정답: {q["correctIndex"]+1}번</p><ol>'+''.join('<li>'+esc(o['reason'])+'</li>' for o in q['options'])+'</ol>')
     else:
      p.append('<p>예시 답: '+esc(q['expectedAnswer'])+'</p><table><tr><th>준거</th><th>0 · 부적절한 답</th><th>1 · 부분 수행</th><th>2 · 충족 예</th></tr>')
      for r in q['rubric']:p.append('<tr><th scope="row">'+esc(r['criterion'])+'</th>'+''.join('<td>'+esc(r['levels'][str(n)])+'</td>' for n in range(3))+'</tr>')
      p.append('</table><p>'+esc(q['acceptableResponses'])+'</p>')
     p.append('<p>근거: '+ ' / '.join(esc(e['quote']) for e in q['evidence'])+'</p></details>')
     if q.get('curriculumCoverage'):
      coverage=q['curriculumCoverage'];label='성취요소 일부의 수행 후보' if coverage['state']=='component_candidate' else '준비·보조·연계 활동'
      p.append('<p class="curriculum-coverage" data-question-ref="'+esc(q['id'])+'">교육과정 검토 범위: '+label+' · 이 문항만으로 성취기준 전체 달성을 판정하지 않습니다.</p>')
     if q['kind']=='spoken_response':
      p.append('<details class="speech-observation"><summary>실제 말하기 관찰 기록 · 인쇄용</summary>'+''.join('<div class="observation-line">'+esc(field)+': </div>' for field in q['observationFields'])+'</details>')
     if q['kind']=='oral_reading':
      p.append('<details class="reading-observation"><summary>첫 읽기·스스로 수정·지원 뒤 읽기 관찰 · 인쇄용</summary>'+''.join('<div class="observation-line">'+esc(field)+': </div>' for field in q['observationFields'])+'<p>'+esc(s['reading']['pronunciationPolicy'])+'</p><table><tr><th>글에 있는 말</th><th>처음 읽은 말</th><th>모델 전 스스로 수정</th><th>지원 뒤 읽은 말</th></tr>'+''.join('<tr><td data-reading-word="'+esc(word['paragraphId']+'-w'+str(word['index']))+'">'+esc(word['printedWord'])+'</td><td></td><td></td><td></td></tr>' for word in s['reading']['words'])+'</table></details>')
    p.append('</section>')
    if q['kind']=='oral_reading':
     reading=s['reading'];asset=audio_assets[reading['id']];wav=(ROOT/asset['path']).read_bytes()
     assert asset['usage']=='reading_model_after_first_read' and hashlib.sha256(wav).hexdigest()==asset['sha256'] and hashlib.sha256(reading['modelScript'].encode()).hexdigest()==asset['intendedTextHash'],'Reading model/input changed'
     p.append('<details class="reading-model" data-reading-model="'+esc(reading['id'])+'"><summary>먼저 읽은 뒤 선생님과 열어 듣는 소리 예시</summary><p>첫 읽기와 스스로 고친 말을 먼저 기록하세요. 이 예시를 들은 뒤 읽은 기록은 지원 뒤 읽기로 구별합니다. 인쇄 자료는 첫 읽기 뒤 선생님이 예시를 읽어 줄 수 있습니다.</p><audio data-reading-audio="'+esc(reading['id'])+'" controls preload="none" aria-label="'+esc(s['title']+' 첫 읽기 뒤 소리 예시')+'" src="data:audio/wav;base64,'+base64.b64encode(wav).decode('ascii')+'">선생님이 첫 읽기 뒤에 문장을 읽어 주세요.</audio></details>')
   p.append('</article>')
  script=JS.replace('readx-pilot-v2','readx-'+bank_id).replace("source:'pilot-v2'","source:"+json.dumps(bank_id))
  p.append('</main><footer>자체 창작 자료 · 실제 교사 검토와 학생 난도 확인 대기 · 입력한 답안·메모는 이 브라우저에 저장됩니다.</footer><script>'+script+'</script></html>')
  content='\n'.join(p)
  if not teacher:
   assert '정답:' not in content and '예시 답:' not in content and 'correctIndex' not in content
  (out/(name+'.html')).write_text(content,encoding='utf-8')
 (out/'workbook-script.js').write_text(script,encoding='utf-8')
 # Plain text edition supports answer-key-free editorial review in a separate pass.
 lines=['국어 여섯 단계 학생용 원고',f'대표{len({s["microSkillId"] for s in sets})}수행 / {len(sets)}자료 / {sum(len(s["questions"]) for s in sets)}문항','']
 for s in sets:
  lines += [f'초{s["grade"]} | {s.get("learnerStageLabel",s["stageLabel"])} | {s["title"]}']+([s['listening']['studentInstruction'],'[듣기 파일: '+s['listening']['id']+'.wav · 대본은 교사용]'] if s.get('listening') else [p['text'] for p in s['paragraphs']])+['']
  if s['source'].get('factualReferences'):lines+=['[바탕 자료 · 학습용 재구성]']+[ref['publisher']+' — '+ref['title']+' '+ref['url'] for ref in s['source']['factualReferences']]+['']
  for t in s.get('tables',[]):lines += [' / '.join(t['headers'])]+[' / '.join(map(str,row)) for row in t['rows']]+['']
  for g in s.get('graphs',[]):lines += ['[그래프의 보이는 정보] '+g['accessibleDescription'],'']
  for media in s.get('mediaPanels',[]):lines += ['[매체 문자 대체] '+media['accessibleDescription'],'']
  for i,q in enumerate(questions_in_order(s),1):
   lines.append(f'{i}. {q["prompt"]}')
   if q['kind']=='single_choice':lines += [f'  {j+1}) {o["text"]}' for j,o in enumerate(q['options'])]
   if q['kind']=='oral_reading':lines.append('[첫 읽기와 스스로 수정을 먼저 기록한 뒤 사용할 소리 예시: '+s['reading']['id']+'.wav · 지원 뒤 읽기는 별도 기록]')
  lines.append('')
 (out/'학생용_원고.txt').write_text('\n'.join(lines),encoding='utf-8')
 transcript=['교사용 듣기 대본과 응답자 카드 · 학생용 사전 노출 금지','합성 음성의 발음·쉼·속도 청취 검토 대기','']
 for s in sets:
  if not s.get('listening'):continue
  transcript += [s['id']+' | '+s['title'],s['listening']['studentInstruction']]+[p['text'] for p in s['paragraphs']]+['['+s['partnerCard'].get('title','학생 첫 질문 뒤 응답')+'] '+s['partnerCard']['reply'],s['partnerCard']['instruction'],'[관찰] 실제 발화 / 재생 횟수 / 받은 도움 / 상대 답 또는 확인 질문 / 후속 발화','']
 (out/'교사용_듣기_대본.txt').write_text('\n'.join(transcript),encoding='utf-8')
 reading_notes=['교사용 첫 읽기 관찰표 · 아직 실제 학습자 기록은 없음','먼저 읽기 → 모델 전 자기 점검 → 모델·교사 지원 → 지원 뒤 읽기를 분리한다.','진행자는 첫 읽기 전에 목표 문장·정답 낱말을 대신 읽어 주지 않는다.','']
 for s in sets:
  if not s.get('reading'):continue
  reading_notes += [s['id']+' | '+s['title']]+[p['text'] for p in s['paragraphs']]+['[첫 읽은 말]','[스스로 고친 말]','[도움·모델 노출 시점과 횟수]','[지원 뒤 읽은 말]',s['reading']['pronunciationPolicy'],'원문 어절 | 처음 읽기 | 자기 수정 | 지원 뒤 읽기']+[w['printedWord']+' | | |' for w in s['reading']['words']]+['']
 (out/'교사용_읽기_관찰표.txt').write_text('\n'.join(reading_notes),encoding='utf-8')
 writing_notes=['교사용 쓰기 과정 관찰표 · 실제 학생 답안과 점수는 아직 없음','초고·검토·수정고를 구별하고 도움·예시·뒤 문항 노출을 기록한다.','']
 for s in sets:
  if not s.get('writingProtocol'):continue
  q=next(q for q in s['questions'] if q['id']==s['writingProtocol']['primaryQuestionId']);context=q['writerContext']
  writing_notes += [s['id']+' | '+s['title'],q['prompt'],'독자: '+context['reader']+' / 목적: '+context['purpose'],'준거: '+' / '.join(r['criterion'] for r in q['rubric'])]+['['+field+']' for field in s['writingProtocol']['observationFields']]+[s['writingProtocol']['supportPolicy'],'']
 (out/'교사용_쓰기_관찰표.txt').write_text('\n'.join(writing_notes),encoding='utf-8')
 print('Rendered:',len(sets),'sets; student and teacher editions separated')

if __name__=='__main__':build()
