"""Build literary works, inspect cases, and deliver primary-response-only handouts."""
import hashlib,json
from author_literary_depth_v2 import build,DEST,OUT,ROOT,SKILLS,CELLS
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def inspect_cases(sets):
    checks={};units={(s['grade'],s['stage']):s for s in sets}
    for s in sets:
        primary=s['questions'][0]
        checks[s['id']+'_interpretation_first']=s['presentationOrder'][0]==s['literaryReview']['primaryQuestionId']==primary['id'] and primary['kind']!='single_choice'
        checks[s['id']+'_analytic_evidence']=len(primary['rubric'])>=2 and len(primary['evidence'])>=2
        if s['literaryReview'].get('revision'):
            revision=s['literaryReview']['revision'];raw=(ROOT/revision['previousSnapshotPath']).read_bytes()
            old=next(u for u in json.loads(raw)['sets'] if u['id']==s['id'])
            changed=s['contentHash']!=old['contentHash'] or any((a['prompt'],a.get('expectedAnswer'),a.get('options'),a.get('rubric'))!=(b['prompt'],b.get('expectedAnswer'),b.get('options'),b.get('rubric')) for a,b in zip(old['questions'],s['questions']))
            checks[s['id']+'_archived_revision']=hashlib.sha256(raw).hexdigest()==revision['previousSnapshotHash'] and old['version']==revision['fromVersion'] and s['version']==revision['toVersion']==old['version']+1 and changed
    def body(g,st):return ' '.join(p['text'] for p in units[g,st]['paragraphs'] if p['id'] in units[g,st]['literaryReview']['workParagraphIds'])
    def key(g,st):return units[g,st]['questions'][0]['expectedAnswer']
    checks['G1_stone_before_wheel_turns']='돌을 빼자 바퀴가 빙글' in body(1,'S2') and '처음에는 멈췄지만' in key(1,'S2')
    checks['G1_flag_stays_at_home']='집에 두고 온' in body(1,'S4') and '돌아갈 길도 먼저' in key(1,'S4')
    checks['G1_bridge_saved_not_relationship_ended']='내일도 건너갈 거야.' in body(1,'S5') and '남겼기' in key(1,'S5')
    checks['G2_three_eight_line_poems']=sum(len(s.get('poems',[])) for s in sets)==3 and all(len(p['lines'])==8 for s in sets for p in s.get('poems',[]))
    checks['G2_address_not_completed']='아직 주소를 못 썼는데' in body(2,'S4')
    checks['G2_old_shoes_not_disposed']='버려졌다고 확정할 근거는 없다' in key(2,'S5')
    checks['G3_joint_story_not_identical_roles']='이야기와 말은 같이, 그림은 내가.' in body(3,'S2')
    checks['G3_open_door_still_waiting']='방 문을 열어 둔 채' in body(3,'S4') and '끝낼 때까지 손을 무릎 위에' in body(3,'S4')
    checks['G3_keep_core_line_add_pause']='중요한 대사의 뜻을 남기면서' in units[3,'S5']['questions'][-1]['expectedAnswer'] and '숨을 고르고 물었다.' in body(3,'S5')
    checks['G4_sensory_contrast_and_attention']=all(x in body(4,'S2') for x in ['소리가 나지 않았다.','매끈해진 천','이번에는 그쪽을 돌아보지'])
    checks['G4_departure_sound_remains']='물소리는 등 뒤에서 아직' in body(4,'S4') and '날짜는 아직 정하지 않았다.' in body(4,'S4')
    checks['G4_trembling_and_not_started']=all(x in body(4,'S5') for x in ['손끝이 조금 떨렸지만','초침은 여전히 같은 간격','아직 시작하지 않았다.'])
    checks['G5_boundary_and_new_space_coexist']=all(x in body(5,'S2') for x in ['만지는 건 먼저 물어봐.','네 걸 만들 자리는 여기로','끊어진 흰 선'])
    checks['G5_blank_title_not_blank_day']='빈 가게와 자동차 소리를 적었다.' in body(5,'S4') and '앞장의 제목을 지우지 않았다.' in body(5,'S4')
    checks['G5_same_thread_and_unfinished_invitation']='같은 실로 다시 묶었다.' in body(5,'S5') and '어느 사진부터 넣을래' in body(5,'S5')
    checks['G6_final_photos_include_context']='방과 손이 함께 담긴 두 장의 사진' in body(6,'S2') and '그 자리는 찍지 않고' in body(6,'S2')
    checks['G6_old_copy_not_overwritten']='오래된 파일을 덮어쓰지는 않았다.' in body(6,'S4') and '이름 없는 새 파일이 나란히' in body(6,'S4')
    checks['G6_recording_not_sent_or_restored']='말이 새로 나타나지는 않았다.' in body(6,'S4') and '보낼 창을 열었다가 닫고' in body(6,'S4')
    checks['G6_revision_proposal_not_final_approval']=all(x in body(6,'S5') for x in ['사진은 뒤쪽으로 옮겨도 되겠어','직접 한번 더 보고 알려 줘.','아직 인쇄소로 보내지 않았다.'])
    checks['reader_opinions_excluded_from_works']=all(not any(p['text'].startswith('가상 독자 의견:') for p in s['paragraphs'] if p['id'] in s['literaryReview']['workParagraphIds']) for s in sets)
    checks['reader_names_not_first_person']=all('독자 ‘가’는' in p['text'] and '독자 ‘나’는' in p['text'] for s in sets for p in s['paragraphs'] if p['text'].startswith('가상 독자 의견:'))
    assert all(checks.values()),[k for k,v in checks.items() if not v]
    return checks

def deliver_works(source,sets):
    catalog=[];anthology=['새로 쓴 이야기와 시 · 편집 초안','다음은 허구의 자체 창작 작품입니다. 감상 과제나 실제 학생 답안은 포함하지 않습니다.',''];files=[]
    for s in sets:
        if s.get('poems'):
            poem=s['poems'][0];title=poem['title'];lines=poem['lines'];genre='시';wid=poem['id']
        else:
            title=s['title'];lines=[p['text'] for p in s['paragraphs'] if p['id'] in s['literaryReview']['workParagraphIds']];genre='이야기';wid=s['id']+'-STORY'
        catalog.append(dict(id=wid,materialId=s['id'],grade=s['grade'],stage=s['stage'],genre=genre,title=title,charCount=len(' '.join(lines)),materialCharCount=s['charCount'],paragraphs=len(lines),lines=len(lines) if genre=='시' else 0,authorship='자체 창작 초안',teacherApproval='pending'))
        anthology += [f"초{s['grade']} · {genre} · {title}",wid,'\n'.join(lines) if genre=='시' else '\n\n'.join(lines),'\n']
    path=OUT/'작품_모음.txt';path.write_text('\n'.join(anthology),encoding='utf-8');delivered=path.read_text(encoding='utf-8')
    for s in sets:
        assert all(p['text'] in delivered for p in s['paragraphs'] if p['id'] in s['literaryReview']['workParagraphIds'] and not p['text'].startswith('시: '))
        assert all(p['text'] not in delivered for p in s['paragraphs'] if p['text'].startswith('가상 독자 의견:'))
        assert s['questions'][0]['expectedAnswer'] not in delivered
    files.append(dict(path=path.relative_to(ROOT).as_posix(),role='works_only_anthology',works=len(catalog),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    for g in range(1,7):
        subset=[s for s in sets if s['grade']==g];blocks=[]
        for s in subset:
            q=s['questions'][0]
            blocks.append('\n'.join([f"초{g} · {s['title']} · {s['learnerStageLabel']}",s['id'],'\n\n'.join(p['text'] for p in s['paragraphs']),'\n첫 해석 과제 '+q['id'],q['prompt'],'\n[내 첫 해석]\n\n\n[내가 짚은 작품 구절과 연결한 이유]\n\n\n[다른 해석·아직 알 수 없는 점]\n\n[대독·낱말 풀이·다른 문제나 예시를 미리 보았으면 적기]\n\n']))
        p=OUT/f'학생용_초{g}_첫해석_과제지.txt'
        p.write_text('첫 해석 과제지 · 보조 문항을 보기 전에\n작품 끝까지 읽고 내 생각을 먼저 남겨요. 뒤 문제나 예시를 본 뒤 바뀐 생각은 별도로 기록해요.\n\n'+'\n\f\n'.join(blocks),encoding='utf-8')
        text=p.read_text(encoding='utf-8')
        for s in subset:
            q=s['questions'][0]
            assert text.count(q['id'])==1 and q['prompt'] in text
            assert all(p['text'] in text for p in s['paragraphs'])
            assert q['expectedAnswer'] not in text and s['teacherGuide'] not in text
            assert all(aux['id'] not in text for aux in s['questions'][1:])
        files.append(dict(path=p.relative_to(ROOT).as_posix(),role='primary_interpretation_only',grade=g,primaryTasks=len(subset),questionIds=[s['questions'][0]['id'] for s in subset],sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    snapshot=hashlib.sha256(source.read_bytes()).hexdigest()
    (OUT/'작품_목록.json').write_text(json.dumps(dict(asOf='2026-11-18',contentSnapshotHash=snapshot,works=catalog),ensure_ascii=False,indent=2),encoding='utf-8')
    report=dict(asOf='2026-11-18',contentSnapshotHash=snapshot,passed=True,files=files,uniquePrimaryTasks=sum(f.get('primaryTasks',0) for f in files),scope='작품 모음은 작품만, 첫 해석 과제지는 작품·가상 의견·주 과제만 전달. 보조 문항 ID·예시 답·지도문 미포함을 실제 파일에서 확인.',limits=['학년별 텍스트 과제지의 인쇄 페이지 배치 검증은 별도.','첫 응답 불변 저장·노출 차단·교사 승인 기능은 없으므로 교사가 전용 과제지를 먼저 주고 원문을 보관.','같은 작품의 재출력은 새 작품·독립 확인 자료로 중복 집계하지 않음.'])
    (OUT/'literary-delivery.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    notes=['교사용 문학 해석 관찰표 · 실제 학생 응답·점수는 아직 없음','작품 읽기·첫 해석·보조 문항 뒤 해석을 구별하고 도움을 기록한다.','']
    for s in sets:
        q=s['questions'][0];notes += [s['id']+' | '+s['title'],q['prompt'],'준거: '+' / '.join(r['criterion'] for r in q['rubric']),'[학생 첫 해석 원문]','[학생이 짚은 구절]','[구절과 해석을 연결한 설명]','[반대 단서·다른 해석·미확인]','[대독·받아쓰기·낱말 풀이·보조 문항·해설 노출]','[교사 추가 확인·판정·남은 미확인]','']
    (OUT/'교사용_문학_해석_관찰표.txt').write_text('\n'.join(notes),encoding='utf-8')
    return catalog,report

def main():
    source=build();sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    folders=['pilot_v2']+[f'expansion_v2_{i:02}' for i in range(1,10)]
    report=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring'/f/'sets.json' for f in folders],expected_stage_counts={sid:{stage:1 for stage in sts} for sid,sts in CELLS.items()})
    report['literaryConsistencyChecks']=inspect_cases(sets)
    report['stageFitReviewDecisions']=[dict(questionId=w['id'],decision='이 보조 문항은 구체 근거 찾기이므로 직접 인용을 허용. 주 해석은 별도 준거로 설명·비교 수행을 검토. 경고 자체는 보존.',state='AI_editorial_review_not_teacher_approval') for w in report['stageFitWarnings'] if next(q for s in sets for q in s['questions'] if q['id']==w['id'])['kind']=='evidence_selection']
    (OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    render(source,OUT,'expansion-v2-10');workbook=verify(source,OUT);catalog,delivery=deliver_works(source,sets)
    summary=dict(asOf='2026-11-18',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=sum(len(v) for v in CELLS.values()),narrativeWorks=sum(w['genre']=='이야기' for w in catalog),poems=sum(w['genre']=='시' for w in catalog),poetryLines=sum(w['lines'] for w in catalog),primaryAnalyticCriteria=sum(len(s['questions'][0]['rubric']) for s in sets),literaryConsistencyChecks=len(report['literaryConsistencyChecks']),primaryOnlyHandoutFiles=sum(f['role']=='primary_interpretation_only' for f in delivery['files']),primaryOnlyHandoutTasks=delivery['uniquePrimaryTasks'],byGrade={str(g):dict(sets=sum(s['grade']==g for s in sets),questions=sum(len(s['questions']) for s in sets if s['grade']==g),minWorkChars=min(w['charCount'] for w in catalog if w['grade']==g),maxWorkChars=max(w['charCount'] for w in catalog if w['grade']==g)) for g in range(1,7)},passed=report['passed'] and workbook['passed'] and delivery['passed'],teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
