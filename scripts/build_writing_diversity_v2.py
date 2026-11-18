"""Build and inspect actual writing tasks; technical checks do not approve pedagogy."""
import hashlib, json
from author_writing_diversity_v2 import build, DEST, OUT, ROOT, SKILLS, CELLS
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks = {}
    for s in sets:
        q=s['questions'][0]
        checks[s['id']+'_production_first'] = q['kind']=='writing' and s['presentationOrder'][0]==s['writingProtocol']['primaryQuestionId']==q['id']
        checks[s['id']+'_specific_rubric_context'] = len(q['rubric'])>=2 and all(q['writerContext'][k] for k in ['reader','purpose','length'])
        if s.get('writingReview'):
            revision=s['writingReview'];raw=(ROOT/revision['previousSnapshotPath']).read_bytes()
            old=next(u for u in json.loads(raw)['sets'] if u['id']==s['id'])
            checks[s['id']+'_archived_answer_revision'] = hashlib.sha256(raw).hexdigest()==revision['previousSnapshotHash'] and old['version']==revision['fromVersion']==1 and s['version']==revision['toVersion']==2 and any((a.get('expectedAnswer'),a['kind'],a.get('options'),a['prompt'])!=(b.get('expectedAnswer'),b['kind'],b.get('options'),b['prompt']) for a,b in zip(old['questions'],s['questions']))
    units = {(s['grade'],s['stage']):s for s in sets}
    def body(g,st): return ' '.join(p['text'] for p in units[g,st]['paragraphs'])
    def key(g,st): return units[g,st]['questions'][0]['expectedAnswer']
    checks['G1_S3_drying_before_envelope'] = all(t in key(1,'S3') for t in ['먼저 노란 받침','풀이 마르면','자기 이름'])
    checks['G1_S5_changed_time_place_unchanged_day'] = all(t in key(1,'S5') for t in ['수요일','점심 뒤','교실']) and '복도' not in key(1,'S5')
    checks['G2_S2_alternative_supported_choice_accepted'] = '다른 선택도' in key(2,'S2') and '선호 차이' in key(2,'S2')
    checks['G2_S3_tomorrow_not_today'] = '오늘은 빌릴 수 없어요.' in body(2,'S3') and '탁자 없이' in key(2,'S3')
    checks['G2_S5_no_forced_preference'] = '다른 선택도' in key(2,'S5') and '모두에게' in key(2,'S5')
    checks['G3_S2_four_viewers_both_samples'] = '네 명이 두 자막을 모두' in body(3,'S2') and '네 명은 모두 나를' in key(3,'S2')
    checks['G3_S3_same_release_not_push'] = '두 번의 바닥 높이와 공을 놓는 방법을 같게' in body(3,'S3') and '같은 방법' in key(3,'S3')
    checks['G3_S5_two_changes_different_people'] = all(t in key(3,'S5') for t in ['글씨 크기와 위치','방문자도 달라','여섯 명','두 명'])
    checks['G4_S2_summary_preserves_selection_reason'] = '선택을 바꾼' in key(4,'S2') and '원래 장면과 연결' in key(4,'S2')
    checks['G4_S3_distinct_accounts_not_unique_rule'] = '사람별로 구별' in key(4,'S3') and '유일한 방법으로 정하지 않았다' in key(4,'S3')
    checks['G4_S5_material_member_support_scope'] = all(t in key(4,'S5') for t in ['종이 자료','회원 계정','텍스트가 없는','즉시 제공되는 것은 아니다'])
    checks['G5_S2_definition_not_location_tracker'] = '현재 물건의 정확한 위치까지 알 수는 없다' in key(5,'S2')
    checks['G5_S3_lock_not_content_validation'] = '틀린 짝을 자동으로 고치지 않는다' in key(5,'S3') and '잠금을 빼고' in key(5,'S3')
    checks['G5_S5_two_conditions_not_or'] = '둘 다 갖추어야' in body(5,'S5') and all(t in key(5,'S5') for t in ['나는 인물이 겹치지','다는 장소가 달라'])
    checks['G6_S2_request_not_confirmed_or_cancelled'] = all(t in key(6,'S2') for t in ['추가 신청 여부는 아직','배정이 확인되지','금요일 저녁 모임 게시판'])
    checks['G6_S3_two_paragraphs_current_not_past'] = len(key(6,'S3').split('\n'))==2 and '과거 소리를 알 수는 없었다' in key(6,'S3')
    checks['G6_S5_six_four_one_one'] = 4+1+1==6 and all(t in key(6,'S5') for t in ['여섯 팀 중 네 팀','한 팀은 작은 글씨','한 팀은 답하지'])
    checks['G6_S5_no_baseline_no_isolated_effect'] = '전 주 문의 수가 없어' in key(6,'S5') and '쪽지만의 효과도 분리해 알기 어렵다' in key(6,'S5')
    checks['G6_S5_keep_support_future_plan'] = all(t in key(6,'S5') for t in ['글씨를 키우기','말 확인과 도움 창구도 유지','더 기록할 계획'])
    checks['G6_S3_no_unrecorded_completed_analysis'] = '나누어 살폈다' not in key(6,'S3')
    checks['G6_S5_choice_scoped_to_booking_conflict'] = '동시간 이용 문의는 없었지만' in units[6,'S5']['questions'][1]['options'][units[6,'S5']['questions'][1]['correctIndex']]['text']
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    return checks

def first_writing_sheets(source, sets):
    """Separate handouts provide a practical first-response route without visible auxiliaries."""
    records=[]
    header='첫 쓰기 과제지 · 보조 문항을 보기 전에\n자료를 읽고 계획한 뒤 첫 글을 쓰세요. 다음 문제나 예시를 본 뒤 고친 글은 별도로 적어요.\n문장 수는 권장 분량이에요. 쓸 내용을 충분히 전하는 것이 중요해요.\n'
    for grade in range(1,7):
        subset=[s for s in sets if s['grade']==grade];blocks=[]
        for s in subset:
            q=s['questions'][0];context=q['writerContext']
            blocks.append('\n'.join([f"초{grade} · {s['learnerStageLabel']} · {s['title']}",s['id'],*['\n'+p['text'] for p in s['paragraphs']], '\n쓰기 과제 '+q['id'],q['prompt'],'독자: '+context['reader'],'목적: '+context['purpose'],'\n계획: '+q['planningPrompt'],'\n[내 계획 메모]\n\n\n[내 첫 글]\n\n\n\n\n[받은 도움·이미 본 문제나 예시가 있으면 적기]\n\n']))
        target=OUT/f'학생용_초{grade}_첫쓰기_과제지.txt'
        target.write_text(header+'\n\n\f\n\n'.join(blocks),encoding='utf-8')
        delivered=target.read_text(encoding='utf-8')
        for s in subset:
            q=s['questions'][0]
            assert delivered.count(q['id'])==1 and q['prompt'] in delivered
            assert all(p['text'] in delivered for p in s['paragraphs'])
            assert q['expectedAnswer'] not in delivered
            assert s['teacherGuide'] not in delivered
            assert all(aux['id'] not in delivered for aux in s['questions'][1:])
        records.append(dict(path=target.relative_to(ROOT).as_posix(),grade=grade,sets=len(subset),primaryTasks=len(subset),sha256=hashlib.sha256(target.read_bytes()).hexdigest()))
    report=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),passed=True,files=records,uniquePrimaryTasks=sum(r['primaryTasks'] for r in records),scope='학년별 첫 쓰기 전용 텍스트 과제지. 원문·독자·목적·계획·주 쓰기만 포함. 보조 문항 ID·교사용 예시 답·지도문 미포함을 파일에서 확인.',limits=['실제 첫 응답 보관·수정 이력 확인은 교사가 별도로 실시해야 함. 불변 저장·시간 잠금 기능은 없음.','텍스트 과제지 생성 검증이며 실제 학생 필기·교사 승인·인쇄 페이지 배치 검증과 구별.'])
    (OUT/'first-writing-delivery.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return report

def main():
    source=build(); sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,9)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{st:1 for st in sts} for sid,sts in CELLS.items()})
    report['writingDiversityConsistencyChecks']=inspect_cases(sets)
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-09');workbook=verify(source,OUT)
    notes=(OUT/'교사용_쓰기_관찰표.txt').read_text(encoding='utf-8')
    assert all(s['id'] in notes for s in sets)
    handouts=first_writing_sheets(source,sets)
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),tasks=sum(len(s['questions']) for s in sets),writingProductionTasks=sum(q['kind']=='writing' for s in sets for q in s['questions']),primaryAnalyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(v) for v in CELLS.values()),writingConsistencyChecks=len(report['writingDiversityConsistencyChecks']),firstWritingHandoutFiles=len(handouts['files']),firstWritingHandoutTasks=handouts['uniquePrimaryTasks'],byGrade={str(g):dict(sets=sum(s['grade']==g for s in sets),tasks=sum(len(s['questions']) for s in sets if s['grade']==g),minChars=min(s['charCount'] for s in sets if s['grade']==g),maxChars=max(s['charCount'] for s in sets if s['grade']==g)) for g in range(1,7)},passed=report['passed'] and workbook['passed'] and handouts['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
