"""Deliver audio, live speaking tasks and blank observations without invented learners."""
import hashlib,json
from author_oral_v2 import build,DEST,OUT,ROOT,CELLS,SKILLS
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify
from verify_pilot_v2_audio import verify as verify_audio

def inspect_cases(sets):
    checks={};byid={s['id']:s for s in sets}
    for s in sets:
        q=s['questions'][0]
        checks[s['id']+'_live_before_choices']=q['kind']=='spoken_response' and s['presentationOrder'][0]==q['id'] and q['responseMode']=='live_speech_with_partner'
        checks[s['id']+'_actual_followup']=len(q['rubric'])==3 and len(q['observationFields'])>=5 and s['partnerCard']['visibility'].startswith('teacher_only_after_')
    def unit(g,n,stage):return byid[f'PV2-G{g}-oral-{n}-{stage}-A']
    def text(g,n,stage):return ' '.join(t['text'] for t in unit(g,n,stage)['listening']['turns'])
    checks['G1_new_quantity_only_after_question']='한 자루' not in text(1,'02','S2') and '한 자루' in unit(1,'02','S2')['partnerCard']['reply']
    checks['G1_current_location_not_storage']='책상 위' in text(1,'02','S3') and '옆 주머니' not in text(1,'02','S3') and '옆 주머니' in unit(1,'02','S3')['partnerCard']['reply']
    checks['G2_last_actor_self_reference']=unit(2,'01','S2')['listening']['turns'][1]['role']=='다연' and '내가 덮개를 닫을게' in text(2,'01','S2')
    checks['G2_reuse_not_disposal']='두 가지 모두 다음 놀이에 다시' in text(2,'01','S5') and '종이심을 버리고' in unit(2,'01','S5')['listening']['turns'][1]['text']
    checks['G3_information_supports_change_or_keep']='유지' in unit(3,'04','S3')['questions'][0]['rubric'][2]['levels']['2'] and '가림막' in unit(3,'04','S3')['partnerCard']['reply']
    checks['G3_space_unknown_not_assumed_fit']='크기는 아직 재지 않았어' in unit(3,'04','S5')['partnerCard']['reply'] and '확인한 뒤' in unit(3,'04','S5')['questions'][0]['rubric'][2]['levels']['2']
    checks['G4_local_game_not_postal_rule']='놀이 보관함' in text(4,'03','S3') and '실제 우편 발송 규칙이 아닌' in unit(4,'03','S3')['teacherGuide']
    checks['G4_cards_not_unique_people']='한 장에는 한 가지' in text(4,'03','S5') and '같은 사람이 여러 장' in text(4,'03','S5')
    checks['G5_individual_needs_not_universal']='나는 손에 짐이' in text(5,'01','S3') and '소리를 들을 수 없는 곳' in text(5,'01','S3')
    checks['G5_observation_reason_unknown']='직접 묻지 않았어' in text(5,'01','S5') and '스스로 참여한 열두 명' in text(5,'01','S5')
    checks['G6_sampling_unknown_in_initial']='어떤 방법으로 골라' in text(6,'02','S3') and '음악방 앞' not in text(6,'02','S3') and '음악방 앞' in unit(6,'02','S3')['partnerCard']['reply']
    checks['G6_alternative_valid_question_supported']='비교 기간·집계 방법만 물으면' in unit(6,'02','S5')['partnerCard']['instruction'] and '아직 모른다는 답' in unit(6,'02','S5')['questions'][0]['rubric'][2]['levels']['2']
    checks['G6_missing_record_not_no_change']='이 기록에 없어요' in text(6,'02','S5') and '온라인으로도' in unit(6,'02','S5')['partnerCard']['reply']
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    audio=verify_audio('oral-synthesis-result.json','listening-verification.json',OUT/'audio')
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,7)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
    report['oralConsistencyChecks']=inspect_cases(sets)
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-07');workbook=verify(source,OUT)
    notes=['교사용 듣기·말하기 관찰표 · 실제 학생 발화·점수는 아직 없음','첫 듣기 → 첫 발화 → 상대 답 → 후속 발화를 구별한다. 대본·문장 틀·보조 문항 노출을 기록한다.','']
    for s in sets:
        q=s['questions'][0]
        notes += [s['id']+' | '+s['title'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric'])]+['['+f+']' for f in q['observationFields']]+['[교사 준거별 관찰·남은 미확인]','']
    (OUT/'교사용_듣기말하기_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(v) for v in CELLS.values()),listeningAssets=len(audio['assets']),audioDurationSeconds=round(sum(a['durationSeconds'] for a in audio['assets']),3),liveSpeechTasks=len(sets),analyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),oralConsistencyChecks=len(report['oralConsistencyChecks']),audioListeningReviewsPending=len(audio['assets']),passed=report['passed'] and workbook['passed'] and audio['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
