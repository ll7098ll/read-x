"""Check delivery completeness, answer separation, real graph marks, and snapshot freshness."""
from pathlib import Path
from html.parser import HTMLParser
import json,hashlib,base64,subprocess,xml.etree.ElementTree as ET,html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pilot-v2'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

class Workbook(HTMLParser):
    def __init__(self):
        super().__init__();self.sets=[];self.questions=0;self.graphs={};self.tables=0;self.details=0;self.responses=[];self.poems=[];self.poem_lines={};self.active_line=None;self.audios={};self.question_order=[];self.transcripts=0;self.partner_cards=0;self.observations=0;self.speech_instructions={};self.active_speech=None;self.reading_lines={};self.active_reading_line=None;self.reading_words={};self.active_reading_word=None;self.reading_audios={};self.reading_models={};self.reading_observations=0
        self.curriculum_audits=[];self.curriculum_coverage=[];self.draft_revisions=0;self.factual_credits=[];self.factual_audits=0;self.writer_contexts=[];self.writing_protocols=[]
        self.media={};self.media_alternatives=[];self.media_elements={};self.active_media_element=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='article' and a.get('class')=='set':self.sets.append((a['data-skill'],a['data-stage']))
        if tag=='section' and a.get('class')=='question':self.questions+=1;self.question_order.append(a['data-question'])
        if tag=='details' and a.get('class')=='curriculum-audit':self.curriculum_audits.append(a['data-curriculum-material'])
        if tag=='p' and a.get('class')=='curriculum-coverage':self.curriculum_coverage.append(a['data-question-ref'])
        if tag=='details' and a.get('class')=='draft-revision':self.draft_revisions+=1
        if tag=='p' and a.get('class')=='factual-credit':self.factual_credits.append(a['data-source-material'])
        if tag=='details' and a.get('class')=='factual-audit':self.factual_audits+=1
        if tag=='p' and a.get('class')=='writer-context':self.writer_contexts.append(a['data-writer-context'])
        if tag=='details' and a.get('class')=='writing-protocol':self.writing_protocols.append(a['data-writing-material'])
        if tag=='details' and a.get('class')=='listening-transcript':self.transcripts+=1
        if tag=='details' and a.get('class')=='partner-card':self.partner_cards+=1
        if tag=='details' and a.get('class')=='speech-observation':self.observations+=1
        if tag=='details' and a.get('class')=='reading-observation':self.reading_observations+=1
        if tag=='details' and a.get('class')=='reading-model':
            assert 'open' not in a and a['data-reading-model'] not in self.reading_models
            self.reading_models[a['data-reading-model']]=self.question_order[-1]
        if tag=='audio':
            assert a['src'].startswith('data:audio/wav;base64,') and a.get('aria-label') and a['preload']=='none' and 'controls' in a and 'autoplay' not in a
            target=self.reading_audios if 'data-reading-audio' in a else self.audios
            aid=a.get('data-reading-audio',a.get('data-listening'));assert aid and aid not in target
            target[aid]=base64.b64decode(a['src'].split(',',1)[1])
        if tag=='section' and a.get('class')=='poem':self.poems.append(a['data-poem'])
        if tag=='p' and a.get('class')=='poem-line':
            assert a['data-line'] not in self.poem_lines
            self.active_line=a['data-line'];self.poem_lines[self.active_line]=''
        if tag=='p' and a.get('class')=='speech-instruction':
            self.active_speech=self.question_order[-1];assert self.active_speech not in self.speech_instructions
            self.speech_instructions[self.active_speech]=''
        if tag=='p' and a.get('class')=='reading-line':
            self.active_reading_line=a['data-reading-line'];assert self.active_reading_line not in self.reading_lines
            self.reading_lines[self.active_reading_line]=''
        if tag=='td' and 'data-reading-word' in a:
            self.active_reading_word=a['data-reading-word'];assert self.active_reading_word not in self.reading_words
            self.reading_words[self.active_reading_word]=''
        if tag=='table':self.tables+=1
        if tag=='div' and 'data-media-alternative' in a:self.media_alternatives.append(a['data-media-alternative'])
        if tag=='p' and 'data-media-element' in a:
            self.active_media_element=a['data-media-element'];assert self.active_media_element not in self.media_elements
            self.media_elements[self.active_media_element]=''
        if tag=='details':self.details+=1
        if 'data-response' in a:self.responses.append(a['data-response'])
        if tag=='img':
            assert a.get('alt')
            if 'data-media' in a:
                assert a['src'].startswith('data:image/png;base64,') and a['data-media'] not in self.media
                self.media[a['data-media']]=dict(png=base64.b64decode(a['src'].split(',',1)[1]),alt=a['alt'])
            else:
                assert a['src'].startswith('data:image/svg+xml;base64,') and a['data-graph'] not in self.graphs
                self.graphs[a['data-graph']]=dict(svg=base64.b64decode(a['src'].split(',',1)[1]),alt=a['alt'])
    def handle_data(self,data):
        if self.active_line:self.poem_lines[self.active_line]+=data
        if self.active_speech:self.speech_instructions[self.active_speech]+=data
        if self.active_reading_line:self.reading_lines[self.active_reading_line]+=data
        if self.active_reading_word:self.reading_words[self.active_reading_word]+=data
        if self.active_media_element:self.media_elements[self.active_media_element]+=data
    def handle_endtag(self,tag):
        if tag=='p':self.active_line=None;self.active_speech=None;self.active_reading_line=None;self.active_media_element=None
        if tag=='td':self.active_reading_word=None

def verify(source=None,out=None):
    source=Path(source) if source else ROOT/'data/content_authoring/pilot_v2/sets.json';snapshot=digest(source)
    OUT=Path(out) if out else ROOT/'output/pilot-v2'
    sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    verification=json.loads((OUT/'verification.json').read_text(encoding='utf-8'))
    manifest=json.loads((OUT/'graph-assets.json').read_text(encoding='utf-8')) if any(s.get('graphs') for s in sets) else dict(contentSnapshotHash=snapshot,assets=[])
    assert verification['passed'] and verification['contentSnapshotHash']==manifest['contentSnapshotHash']==snapshot
    graphs={g['id']:g for s in sets for g in s.get('graphs',[])}
    assert set(graphs)=={a['id'] for a in manifest['assets']}
    media_panels={m['id']:m for s in sets for m in s.get('mediaPanels',[])};media_assets={}
    if media_panels:
        from PIL import Image
        media_manifest=json.loads((OUT/'media-assets.json').read_text(encoding='utf-8'))
        assert media_manifest['contentSnapshotHash']==snapshot
        media_assets={a['id']:a for a in media_manifest['assets']};assert set(media_assets)==set(media_panels)
        for mid,m in media_panels.items():
            asset=media_assets[mid];assert digest(ROOT/asset['png'])==asset['pngHash']
            assert hashlib.sha256(json.dumps(m,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==asset['panelDataHash']
            with Image.open(ROOT/asset['png']) as im:assert im.size==(asset['width'],asset['height']) and im.format=='PNG'
            assert [r['id'] for r in asset['renderedElements']]==[e['id'] for e in m['elements']]
            for row,element in zip(asset['renderedElements'],m['elements']):
                assert row['text']==element['text'] and row['style']==element['style'] and row['icon']==element.get('icon')
                x,y,w,h=row['box'];assert 0<=x<x+w<=asset['width'] and 0<=y<y+h<=asset['height']
                assert [''.join(lines).replace(' ','') for lines in row['lines']]==[cell.replace(' ','') for cell in row['cells']]
    listening_sets=[s for s in sets if s.get('listening')];reading_sets=[s for s in sets if s.get('reading')];audio_assets={}
    if listening_sets or reading_sets:
        audio_report=json.loads((OUT/'audio/listening-verification.json').read_text(encoding='utf-8'))
        assert audio_report['passed'] and audio_report['contentSnapshotHash']==snapshot
        audio_assets={a['id']:a for a in audio_report['assets']}
        assert set(audio_assets)=={s['listening']['id'] for s in listening_sets}|{s['reading']['id'] for s in reading_sets}
        for s in listening_sets:
            a=audio_assets[s['listening']['id']]
            assert digest(ROOT/a['path'])==a['sha256'] and hashlib.sha256(s['listening']['script'].encode()).hexdigest()==a['intendedTextHash']
            assert a['usage']=='listening_material'
        for s in reading_sets:
            a=audio_assets[s['reading']['id']]
            assert a['usage']=='reading_model_after_first_read' and digest(ROOT/a['path'])==a['sha256'] and hashlib.sha256(s['reading']['modelScript'].encode()).hexdigest()==a['intendedTextHash']
    ns={'s':'http://www.w3.org/2000/svg'};mark_checks=0
    for asset in manifest['assets']:
        g=graphs[asset['id']];svg=ROOT/asset['svg']
        assert digest(svg)==asset['svgHash'] and digest(ROOT/asset['png'])==asset['pngHash']
        assert hashlib.sha256(json.dumps(g,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==asset['graphDataHash']
        tree=ET.parse(svg)
        assert tree.find('.//s:script',ns) is None and tree.find('.//s:image',ns) is None
        for i,value in enumerate(g['values']):
            row=tree.find(f'.//s:g[@id="row-{i}"]',ns);assert row is not None
            if g['kind']=='pictograph':assert len(row.findall('.//s:use',ns))==value//g['symbolValue']
            else:assert len(row.findall('.//s:path',ns))==1
            mark_checks+=1
    report={}
    for teacher in (False,True):
        filename='교사용_해설집.html' if teacher else '학생용_문제집.html'
        file=OUT/filename;content=file.read_text(encoding='utf-8');p=Workbook();p.feed(content)
        assert p.sets==[(s['microSkillId'],s['stage']) for s in sets]
        assert p.questions==sum(len(s['questions']) for s in sets) and set(p.graphs)==set(graphs)
        assert set(p.media)==set(media_panels) and p.media_alternatives==list(media_panels)
        assert p.media_elements=={m['id']+'/'+e['id']:(e['imageDescription']+' · ' if e.get('imageDescription') else '')+{'large':'큰 글씨: ','small':'작은 글씨: '}.get(e['style'],'')+e['text'] for m in media_panels.values() for e in m['elements']}
        for mid,render in p.media.items():
            assert hashlib.sha256(render['png']).hexdigest()==media_assets[mid]['pngHash'],mid+' embedded media bytes changed'
            assert render['alt']==media_panels[mid]['accessibleDescription'],mid+' media alternative changed'
        assert p.question_order==[qid for s in sets for qid in s.get('presentationOrder',[q['id'] for q in s['questions']])]
        assert p.factual_credits==[s['id'] for s in sets if s['source'].get('factualReferences')]
        assert p.factual_audits==(sum(bool(s['source'].get('factChecks')) for s in sets) if teacher else 0)
        assert p.writer_contexts==[q['id'] for s in sets for q in sorted(s['questions'],key=lambda q:s.get('presentationOrder',[x['id'] for x in s['questions']]).index(q['id'])) if q.get('writerContext')]
        assert p.writing_protocols==([s['id'] for s in sets if s.get('writingProtocol')] if teacher else [])
        for s in sets:
            assert html.escape(s.get('learnerStageLabel',s['stageLabel']),quote=True) in content
            if teacher or not s.get('listening'):
                for para in s['paragraphs']:assert html.escape(para['text'],quote=True) in content,s['id']+' missing visible text'
            for q in s['questions']:
                assert html.escape(q['prompt'],quote=True) in content,q['id']+' missing prompt'
                if q['kind']=='single_choice':
                    for option in q['options']:assert html.escape(option['text'],quote=True) in content,q['id']+' missing option'
                elif teacher:assert html.escape(q['expectedAnswer'],quote=True) in content,q['id']+' missing teacher answer'
            for ref in s['source'].get('factualReferences',[]):assert 'href="'+html.escape(ref['url'],quote=True)+'"' in content,s['id']+' missing factual source link'
        assert p.speech_instructions=={q['id']:q.get('performanceInstruction','먼저 상대에게 직접 질문하고 답을 들어 확인하세요. 아래 칸은 말한 뒤 남기는 메모이며 말하기 관찰을 대신하지 않습니다.') for s in sets for q in s['questions'] if q['kind']=='spoken_response'}
        assert set(p.audios)=={s['listening']['id'] for s in listening_sets}
        assert set(p.reading_audios)=={s['reading']['id'] for s in reading_sets}
        for aid,wav in {**p.audios,**p.reading_audios}.items():assert hashlib.sha256(wav).hexdigest()==audio_assets[aid]['sha256']
        assert p.reading_models=={s['reading']['id']:next(q['id'] for q in s['questions'] if q['kind']=='oral_reading') for s in reading_sets}
        assert p.reading_lines=={p['id']:p['text'] for s in reading_sets for p in s['paragraphs']}
        poems=[poem for s in sets for poem in s.get('poems',[])]
        assert p.poems==[poem['id'] for poem in poems]
        assert p.poem_lines=={pid:line for poem in poems for pid,line in zip(poem['lineParagraphIds'],poem['lines'])}
        for gid,render in p.graphs.items():
            asset=next(a for a in manifest['assets'] if a['id']==gid)
            assert hashlib.sha256(render['svg']).hexdigest()==asset['svgHash']
            assert render['alt']==graphs[gid]['accessibleDescription']
        for s in sets:
            for q in s['questions']:
                if q['kind']=='single_choice':assert p.responses.count(q['id'])==len(q['options'])
                else:
                    keys=['plan','draft','revision','reason'] if q['kind']=='writing' else ['draft']
                    for k in keys:assert p.responses.count(q['id']+'-'+k)==1
        if not teacher:
            assert p.details==len(reading_sets) and p.tables==sum(len(s.get('tables',[])) for s in sets)
            assert not any(token in content for token in ['correctIndex','expectedAnswer','teacherGuide','curriculumAudit','curriculumCoverage','정답:','예시 답:','정답·예시 답과 검토 기준'])
            assert p.transcripts==p.partner_cards==p.observations==0
            assert not p.curriculum_audits and not p.curriculum_coverage and p.draft_revisions==0
            assert p.reading_observations==0 and not p.reading_words
            plain=(OUT/'학생용_원고.txt').read_text(encoding='utf-8')
            for s in listening_sets:
                for para in s['paragraphs']:assert html.escape(para['text'],quote=True) not in content and para['text'] not in plain
                assert html.escape(s['partnerCard']['reply'],quote=True) not in content
        else:
            assert content.count('정답·예시 답과 검토 기준')==p.questions
            assert p.transcripts==p.partner_cards==p.observations==len(listening_sets)
            assert p.reading_observations==len(reading_sets)
            assert p.reading_words=={word['paragraphId']+'-w'+str(word['index']):word['printedWord'] for s in reading_sets for word in s['reading']['words']}
            assert p.curriculum_audits==[s['id'] for s in sets if s['source'].get('curriculumAudit')]
            assert p.curriculum_coverage==[q['id'] for s in sets for q in sorted(s['questions'],key=lambda q:s.get('presentationOrder',[x['id'] for x in s['questions']]).index(q['id'])) if q.get('curriculumCoverage')]
            assert p.draft_revisions==sum(bool(s['review'].get('draftRevision')) for s in sets)
            for s in listening_sets:
                assert html.escape(s['partnerCard']['reply'],quote=True) in content
                assert all(html.escape(para['text'],quote=True) in content for para in s['paragraphs'])
        report[filename]=dict(sets=len(p.sets),questions=p.questions,graphs=len(p.graphs),tables=p.tables,poems=len(p.poems),poetryLines=len(p.poem_lines),listeningClips=len(p.audios),readingModelClips=len(p.reading_audios),readingLines=len(p.reading_lines),readingObservationForms=p.reading_observations,readingWordReferences=len(p.reading_words),transcripts=p.transcripts,partnerCards=p.partner_cards,observationForms=p.observations,curriculumScopePanels=len(p.curriculum_audits),questionScopeNotes=len(p.curriculum_coverage),draftRevisionNotes=p.draft_revisions,sha256=digest(file))
        report[filename].update(writingSituationBlocks=len(p.writer_contexts),writingObservationForms=len(p.writing_protocols))
        report[filename].update(mediaPanels=len(p.media),mediaElementAlternatives=len(p.media_elements))
    check=subprocess.run(['node','--check',str(OUT/'workbook-script.js')],capture_output=True,text=True)
    assert check.returncode==0,check.stderr
    report=dict(passed=True,contentSnapshotHash=snapshot,editions=report,renderedGraphRowChecks=mark_checks,
                javascriptSyntax='passed',browserRuntime='not_tested',limits=['내용·단계·학년 적합성은 독립 교사 검토와 학생 관찰 대기'])
    (OUT/'workbook-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return report

if __name__=='__main__':verify()
