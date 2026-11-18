"""Verify eighteen factual explanation drafts and bounded reading applications."""
import hashlib,json
from author_explanation_v2 import build,DEST,OUT,ROOT,CELLS,SKILLS,LEDGER
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks={};units={s['id']:s for s in sets}
    for s in sets:
        checks[s['id']+'_primary_first']=s['presentationOrder'][0]==s['explanationReview']['primaryQuestionId']==s['questions'][0]['id'] and s['questions'][0]['kind']!='single_choice'
        checks[s['id']+'_specific_criteria']=len(s['questions'][0]['rubric'])>=2 and len(s['source']['factChecks'])>=2
    def unit(g,n,st):return units[f'PV2-G{g}-information-{n}-{st}-A']
    def text(g,n,st):return ' '.join(p['text'] for p in unit(g,n,st)['paragraphs'])
    checks['G1_one_species_not_all']='한 종류' in text(1,'06','S2')
    checks['G1_feather_fat_flipper_functions']=all(w in text(1,'06','S3') for w in ['깃털','지방층','지느러미'])
    checks['G1_bat_wing_membrane']='손가락뼈' in text(1,'06','S5') and '피부막' in text(1,'06','S5')
    checks['G2_no_earflap_not_no_ear']='귀구멍은 있지만' in text(2,'08','S2')
    checks['G2_air_water_oxygen_distinct']='큰돌고래는 폐로' in text(2,'08','S3') and '아가미로 지나가는 물속의 산소' in text(2,'08','S3')
    checks['G2_moth_day_color_exceptions']='낮에 날아다니는 나방도' in text(2,'08','S5') and '화려한 색과 무늬' in text(2,'08','S5')
    checks['G3_cell_positions_not_all_raised']='매번 여섯 점을 모두 올리는 것은 아니다' in text(3,'06','S2')
    checks['G3_digitizing_example_not_institution_record']='실제 기관의 작업 순서를 그대로 옮긴 기록은 아니다' in text(3,'06','S3')
    checks['G3_context_not_certain_use']='물건의 쓰임이 모두 확정되는 것은 아니다' in text(3,'06','S5')
    checks['G4_full_moon_not_every_eclipse']='보름달이 뜰 때마다 월식이 생기지는 않는다' in text(4,'11','S2')
    checks['G4_rainbow_scope_and_position']='햇빛으로 보이는 무지개' in text(4,'11','S3') and '뒤쪽' in text(4,'11','S3') and '앞쪽' in text(4,'11','S3')
    checks['G4_seed_light_difference']='어둠이 필요한 종류' in text(4,'11','S5') and '즉시 싹튼다고 약속할 수는 없다' in text(4,'11','S5')
    checks['G5_projection_shared_exposure']='USGS-PROJECTIONS' in unit(5,'08','S2')['source']['sourceExposureFamilyIds'] and 'USGS-PROJECTIONS' in unit(5,'08','S5')['source']['sourceExposureFamilyIds']
    checks['G5_specific_photo_not_all_photos']='학습용 가상 자료의 설명' in text(5,'08','S3') and '별도의 높이 숫자나 등고선은 넣지 않았다' in text(5,'08','S3')
    checks['G5_conformal_local_not_global']='매우 작은 부분의 모양' in text(5,'08','S5') and '넓은 지역 전체' in text(5,'08','S5')
    checks['G6_false_and_missing_rings']='한 해에 여분의 띠' in text(6,'11','S2') and '표본의 일부에서 나타나지' in text(6,'11','S2')
    checks['G6_lights_multiple_sources']='어선·산업 시설·가스 연소·불' in text(6,'11','S3') and '전력 공급도 확대' in text(6,'11','S3')
    checks['G6_model_and_fiction_not_real_detection']='모형은 가능한 원인을 비교' in text(6,'11','S5') and '이 사례는 실제 행성의 관측 결과가 아니다' in text(6,'11','S5')
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,8)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
    report['explanationConsistencyChecks']=inspect_cases(sets)
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-08');workbook=verify(source,OUT)
    notes=['교사용 설명글 읽기 관찰표 · 실제 학생 응답은 아직 없음','사실·일반 원리와 가상 사례의 구별, 조건·예외·미확인 보존을 실제 답에서 확인한다.','']
    for s in sets:
        q=s['questions'][0]
        notes += [s['id']+' | '+s['title'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric']),'[학생 첫 응답 원문]','[학생이 짚은 문단·구절과 연결 이유]','[사실 / 가상 사례 / 아직 미확인의 구별]','[낱말 풀이·대독·보조 문항·해설 노출]','[교사 추가 확인·판정·남은 미확인]','']
    (OUT/'교사용_설명글_읽기_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(v) for v in CELLS.values()),factualAnchors=report['factualAnchors'],sourcePages=len({r['id'] for s in sets for r in s['source']['factualReferences']}),primaryAnalyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),explanationConsistencyChecks=len(report['explanationConsistencyChecks']),byGrade={str(g):dict(sets=sum(s['grade']==g for s in sets),questions=sum(len(s['questions']) for s in sets if s['grade']==g),minChars=min(s['charCount'] for s in sets if s['grade']==g),maxChars=max(s['charCount'] for s in sets if s['grade']==g)) for g in range(1,7)},passed=report['passed'] and workbook['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False))
if __name__=='__main__':main()
