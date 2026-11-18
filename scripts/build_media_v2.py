"""Build and verify authored media, including actual images and element-level references."""
import hashlib,json
from author_media_v2 import build,DEST,OUT,ROOT,CELLS,SKILLS
from media_v2_assets import build as assets
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks={};units={s['id']:s for s in sets}
    for s in sets:
        checks[s['id']+'_primary_first']=s['presentationOrder'][0]==s['mediaReview']['primaryQuestionId']==s['questions'][0]['id'] and s['questions'][0]['kind']!='single_choice'
        checks[s['id']+'_specific_criteria']=len(s['questions'][0]['rubric'])>=2 and s['mediaReview']['teacherApproval']=='pending'
    def unit(g,n,stage):return units[f'PV2-G{g}-media-{n}-{stage}-A']
    def part(g,n,stage,p,key):return next(e['text'] for e in unit(g,n,stage)['mediaPanels'][p-1]['elements'] if e['id']==key)
    checks['G1_location_limited_permission']='복도에서는' in part(1,'01','S3',1,'rule') and '놀이방 안에서만' in part(1,'01','S3',2,'rule')
    checks['G2_cross_table_key']='수요일 | 종이접기 | 오후 4시'==part(2,'03','S3',1,'wed') and '종이접기 | 솔방'==part(2,'03','S3',2,'fold')
    checks['G2_unknown_not_friday']='나래 | 자석 | 미정'==part(2,'03','S5',1,'na') and '아직 정하지 않음' in part(2,'03','S5',1,'note')
    checks['G3_place_only_revision']='장소만 수정' in part(3,'06','S3',2,'change') and '11월21일 오전10시' in part(3,'06','S3',1,'event') and '11월21일 오전10시' in part(3,'06','S3',2,'event')
    checks['G3_repost_not_new_revision']='11월18일' in part(3,'06','S5',3,'post') and '11월12일' in part(3,'06','S5',3,'photo') and '오후2시' in part(3,'06','S5',2,'event')
    checks['G4_excerpt_missing_scope']='앞부분 생략' in part(4,'04','S3',1,'clip') and '마른 씨앗은 모두' in part(4,'04','S3',2,'dry') and '말리고 있다' in part(4,'04','S3',2,'wet')
    checks['G4_response_population_disjoint']=24==8+16 and '24명' in part(4,'04','S5',2,'target') and '8명' in part(4,'04','S5',2,'response') and '16명' in part(4,'04','S5',2,'missing')
    checks['G5_current_age_scope']='초3~6' in part(5,'05','S3',2,'scope') and 'v1' in part(5,'05','S3',3,'source') and 'v2' in part(5,'05','S3',2,'version')
    refs=[part(5,'05','S5',i,'source') for i in range(1,4)]
    checks['G5_shared_old_origin']=all('2025년' in r and 'T31' in r for r in refs)
    a,b=unit(6,'03','S4')['mediaPanels']
    checks['G6_same_words_distinct_emphasis']=[e['text'] for e in a['elements']]==[e['text'] for e in b['elements']] and [e['style'] for e in a['elements']]!=[e['style'] for e in b['elements']]
    checks['G6_scope_not_universal']='누구나' in part(6,'03','S5',1,'headline') and '사전 예약한 초3~6' in part(6,'03','S5',2,'scope') and '20명' in part(6,'03','S5',2,'limit')
    checks['no_invented_reader_results']=all('실제 모든 독자' in s['mediaReview']['notAssessed'][1] for s in sets)
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,6)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
    report['mediaConsistencyChecks']=inspect_cases(sets)
    manifest=assets(source,OUT)
    report['mediaAssetManifest']=dict(path=(OUT/'media-assets.json').relative_to(ROOT).as_posix(),sha256=hashlib.sha256((OUT/'media-assets.json').read_bytes()).hexdigest(),assets=len(manifest['assets']))
    visual=OUT/'visual-review.json';visual_state='pending'
    if visual.exists():
        recorded=json.loads(visual.read_text(encoding='utf-8'))
        if recorded['contentSnapshotHash']==report['contentSnapshotHash'] and recorded['mediaAssetsHash']==report['mediaAssetManifest']['sha256']:
            visual_state='AI_static_review_recorded_not_teacher_approval'
            report['staticVisualReview']=dict(path=visual.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(visual.read_bytes()).hexdigest(),state=visual_state)
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-06');workbook=verify(source,OUT)
    notes=['교사용 매체 읽기 관찰표 · 실제 학생 답·시각 반응은 아직 없음','주 응답 전에 어떤 자료 형태를 제공했는지 기록한다. 문자 대체는 같은 정보의 접근 방법이며 오답 단서나 정답 해설이 아니다.','']
    for s in sets:
        q=s['questions'][0]
        notes += [s['id']+' | '+s['title'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric']),'[학생 첫 응답 원문]','[이미지 / 문자 대체 / 대독 중 제공한 형태]','[짚은 그림·표의 칸·작성일·수정 이력·조건]','[학생이 추가 확인을 제안한 내용]','[보조 문항·다른 자료·해설 노출 시점]','[실제 독자 반응을 관찰했다면 원문 응답; 미관찰이면 미확인]','[교사 판정·추가 확인·남은 미확인]','']
    (OUT/'교사용_매체_읽기_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(stages) for stages in CELLS.values()),mediaPanels=len(manifest['assets']),visibleElements=sum(len(p['elements']) for s in sets for p in s['mediaPanels']),primaryAnalyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),mediaConsistencyChecks=len(report['mediaConsistencyChecks']),mediaEvidenceReferences=sum(e.get('evidenceKind')=='media' for s in sets for q in s['questions'] for e in q['evidence']),passed=report['passed'] and workbook['passed'],staticVisualReview=visual_state,teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
