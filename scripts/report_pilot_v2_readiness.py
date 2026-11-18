"""Keep authored pilot quantities separate from approval, calibration, and full-bank coverage."""
from pathlib import Path
import json,hashlib,collections
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pilot-v2'

def report():
    source=ROOT/'data/content_authoring/pilot_v2/sets.json';snapshot=hashlib.sha256(source.read_bytes()).hexdigest()
    data=json.loads(source.read_text(encoding='utf-8'));sets=data['sets']
    blueprint=json.loads((ROOT/'data/content_authoring/architecture_v2/blueprint.json').read_text(encoding='utf-8'))
    checks=json.loads((OUT/'verification.json').read_text(encoding='utf-8'))
    workbook=json.loads((OUT/'workbook-verification.json').read_text(encoding='utf-8'))
    audio=json.loads((OUT/'audio/listening-verification.json').read_text(encoding='utf-8'))
    for evidence in [checks,workbook,audio]:assert evidence['passed'] and evidence['contentSnapshotHash']==snapshot
    for name,edition in workbook['editions'].items():assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==edition['sha256']
    actual_skills={s['microSkillId'] for s in sets};cells={(s['microSkillId'],s['stage']) for s in sets}
    source_missing=[dict(id=s['id'],skillId=s['microSkillId'],grade=s['grade'],name=s['skillName'],reviewDecision=s['source'].get('curriculumAudit',{}).get('decision','not_reviewed'),reason=s['source'].get('curriculumAudit',{}).get('remainingGap','원문 및 목표 범위 검토 필요')) for s in sets if not s['source'].get('officialStandards')]
    source_unchecked=[s['id'] for s in sets if not s['source'].get('officialStandards') and not s['source'].get('curriculumAudit')]
    related_only=[s['id'] for s in sets if s['source'].get('curriculumAudit',{}).get('decision')=='related_only_goal_scope_review']
    approved=sum(s['review']['teacherApproval']=='approved' for s in sets)
    calibrated=sum(s['review']['studentCalibration'] in ('verified','calibrated') for s in sets)
    audio_pending=[a['id'] for a in audio['assets'] if a['listeningReview']!='approved']
    proposal=blueprint['counts']
    from report_content_bank_v2 import report as bank_report
    bank=bank_report()
    result=dict(asOf=max(data['asOf'],bank['asOf']),contentSnapshotHash=snapshot,
      scope='국어 체계2차 대표 제작분의 검토 보고서. 전체 은행 확장 합계는 fullBankDrafts와 별도 원장에 기록. 기존 batch03·앱 전체·실제 수업 성과 제외.',
      goalCompletion='not_proven',publicationReady=False,
      representativeDrafts=dict(targetSets=144,targetQuestions=624,authoredSets=len(sets),authoredQuestions=sum(len(s['questions']) for s in sets),
       draftQuantityMilestoneMet=len(sets)==144 and sum(len(s['questions']) for s in sets)==624 and len(actual_skills)==12,
       grades=dict(collections.Counter(str(s['grade']) for s in sets)),skills=len(actual_skills),skillStageCells=len(cells)),
      proposedBank=dict(proposedSkills=proposal['skills'],proposedStageCells=proposal['stageCells'],proposedSets=proposal['targetSets'],proposedQuestions=proposal['targetQuestions'],
       pilotAuthoredSkills=len(actual_skills),pilotAuthoredStageCells=len(cells),totalAuthoredSkills=bank['authored']['skills'],totalAuthoredStageCells=bank['authored']['skillStageCells'],notAuthoredCandidateSkills=bank['remaining']['candidateSkills'],notAuthoredCandidateStageCells=bank['remaining']['candidateStageCells'],
       note=f'계획 칸은 승인된 전체 교육과정 목록이 아니다. 전체 초안{bank["authored"]["sets"]}묶음은 같은 수의 장문 또는 승인 공급을 뜻하지 않는다.'),
      fullBankDrafts=dict(readinessPath='output/content-bank-v2/readiness.json',coveragePath='output/content-bank-v2/coverage.json',authored=bank['authored'],remaining=bank['remaining'],review=bank['review']),
      technicalEvidence=dict(contentChecks='passed',workbookStructureAndSeparation='passed',numericChecks=len(checks['numericChecks']),readingChecks=len(checks['readingChecks']),
       audioAssets=len(audio['assets']),listeningClips=audio['authoredListeningSets'],readingModelClips=audio['authoredReadingModelSets'],audioStructure='passed',browserRuntime=workbook['browserRuntime']),
      pendingGates=dict(independentTeacherReview=dict(approvedSets=approved,pendingSets=len(sets)-approved,state='pending'),
       studentCalibration=dict(calibratedSets=calibrated,pendingSets=len(sets)-calibrated,state='pending'),
       pronunciationAndPacingReview=dict(pendingAssets=audio_pending,state='pending'),
       curriculumSourceAlignment=dict(sourceCheckedCandidates=len(sets)-len(source_missing),sourceLinkedSets=len(sets)-len(source_unchecked),sourceScopeAuditedSets=sum(bool(s['source'].get('curriculumAudit')) for s in sets),relatedOnlyGoalScopeReviewSets=len(related_only),sourceUncheckedSets=source_unchecked,missingDirectCandidateRefs=source_missing,state='source_links_classified_not_teacher_approval',note=f'국어 성취기준 연결 후보{len(sets)-len(source_missing)}와 보조·타교과 연계{len(related_only)}를 구별. 원문과 관계를 분류한 것이 학년 배치·전체 기준의 직접 측정 승인인 것은 아님.'),
       stageAndGradeFit=dict(state='not_independently_verified',note='원고 단계와 실제 난도를 동일시하지 않음. 첫 읽기·지원 뒤 읽기와 실제 질문·수정 설명 관찰 필요.'),
       runtime=dict(state=workbook['browserRuntime'],note='실제 브라우저의 오디오 재생·필터·저장·인쇄 동작과 접근성을 검증했다고 주장하지 않음.')),
      nextWork=[f'직접 국어 측정 주장을 보류한 {len(related_only)}자료의 내부 교수 목표·선수 교과 기능·활동 범위 검토','정답 없는 원고를 활용한 목표·단계·정답 유일성 재검토 및 연관 자료 수정',f'{len(audio_pending)}음성의 발음·쉼·속도 청취 검토와 실제 첫 수행 관찰 준비',f'제안된{proposal["skills"]}수행의 유효한 빈 칸과 사실 근거·장르·소재 부족을 검토하며 전체 공급 확대'])
    (OUT/'readiness.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    audit_rows=[dict(id=s['id'],version=s['version'],grade=s['grade'],skillId=s['microSkillId'],skillName=s['skillName'],stage=s['stage'],decision=s['source'].get('curriculumAudit',{}).get('decision','earlier_unit_candidate_pending_teacher'),scope=s['source'].get('curriculumAudit',{}).get('scope',s['review'].get('curriculumAlignment','')),remainingGap=s['source'].get('curriculumAudit',{}).get('remainingGap',''),references=s['source'].get('curriculumAudit',{}).get('links',s['source'].get('officialStandards',[])),teacherApproval=s['review']['teacherApproval']) for s in sets]
    audit_export=dict(asOf=data['asOf'],contentSnapshotHash=snapshot,sourceBasis='교육부고시2022-33 로컬 원문 및 해당 해설. 최신 통합본 전체 대조 및 교사 승인과 구별.',scopeAuditedThisPass=sum(bool(s['source'].get('curriculumAudit')) for s in sets),officialKoreanCandidateSets=len(sets)-len(source_missing),relatedOnlyGoalScopeReviewSets=len(related_only),sourceUncheckedSets=source_unchecked,materials=audit_rows)
    (OUT/'curriculum-scope.json').write_text(json.dumps(audit_export,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(draftQuantityMilestoneMet=result['representativeDrafts']['draftQuantityMilestoneMet'],authoredSets=len(sets),approvedSets=approved,calibratedSets=calibrated,sourceUncheckedSets=len(source_unchecked),relatedOnlyScopeReviewSets=len(related_only),audioListeningReviewsPending=len(audio_pending),notAuthoredCandidateCells=result['proposedBank']['notAuthoredCandidateStageCells'],goalCompletion=result['goalCompletion']),ensure_ascii=False))
    return result

if __name__=='__main__':report()
