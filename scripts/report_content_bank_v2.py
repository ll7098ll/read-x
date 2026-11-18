"""Count only current, verified, disjoint authored batches; retain full-bank pending scope."""
from pathlib import Path
import collections,hashlib,json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/content-bank-v2'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def report():
    registry=json.loads((ROOT/'data/content_authoring/architecture_v2/authored_batches.json').read_text(encoding='utf-8'))
    blueprint=json.loads((ROOT/'data/content_authoring/architecture_v2/blueprint.json').read_text(encoding='utf-8'))
    proposed={s['id'] for s in blueprint['skills']};proposed_cells={(c['skillId'],c['stage']) for c in blueprint['cells']}
    sets=[];batches=[];used_ids=set();used_questions=set();used_texts=set();dependency_hashes={};audio_records=[];audio_ids=set()
    for batch in registry['batches']:
        path=ROOT/batch['source'];out=ROOT/batch['artifacts'];snapshot=digest(path)
        source=json.loads(path.read_text(encoding='utf-8'));current=source['sets']
        checks=json.loads((out/'verification.json').read_text(encoding='utf-8'))
        workbook=json.loads((out/'workbook-verification.json').read_text(encoding='utf-8'))
        for evidence in (checks,workbook):assert evidence['passed'] and evidence['contentSnapshotHash']==snapshot,batch['id']+' stale checks'
        for filename,edition in workbook['editions'].items():assert digest(out/filename)==edition['sha256'],batch['id']+' changed workbook'
        audio_inputs={s['listening']['id']:s['listening']['script'] for s in current if s.get('listening')}
        audio_inputs.update({s['reading']['id']:s['reading']['modelScript'] for s in current if s.get('reading')})
        audio_usage={s['listening']['id']:('listening_material',s['id']) for s in current if s.get('listening')}
        audio_usage.update({s['reading']['id']:('reading_model_after_first_read',s['id']) for s in current if s.get('reading')})
        if audio_inputs:
            audio=json.loads((out/'audio/listening-verification.json').read_text(encoding='utf-8'))
            assert audio['passed'] and audio['contentSnapshotHash']==snapshot,batch['id']+' stale audio report'
            assert {a['id'] for a in audio['assets']}==set(audio_inputs),batch['id']+' audio supply mismatch'
            for asset in audio['assets']:
                assert asset['id'] not in audio_ids,asset['id']+' duplicate audio'
                audio_ids.add(asset['id'])
                assert (asset['usage'],asset['materialId'])==audio_usage[asset['id']],asset['id']+' audio purpose/material mismatch'
                assert digest(ROOT/asset['path'])==asset['sha256'],asset['id']+' changed WAV'
                assert hashlib.sha256(audio_inputs[asset['id']].encode()).hexdigest()==asset['intendedTextHash'],asset['id']+' changed speech input'
                audio_records.append(asset)
        if checks.get('languageResearchLedger'):
            dep=checks['languageResearchLedger']
            assert digest(ROOT/dep['path'])==dep['sha256'],batch['id']+' stale language research dependency'
        if checks.get('mediaAssetManifest'):
            dep=checks['mediaAssetManifest'];assert digest(ROOT/dep['path'])==dep['sha256'],batch['id']+' changed media manifest'
            media=json.loads((ROOT/dep['path']).read_text(encoding='utf-8'))
            assert media['contentSnapshotHash']==snapshot
            for asset in media['assets']:assert digest(ROOT/asset['png'])==asset['pngHash'],asset['id']+' changed media asset'
        if checks.get('staticVisualReview'):
            dep=checks['staticVisualReview'];assert digest(ROOT/dep['path'])==dep['sha256'],batch['id']+' changed static visual review'
            visual=json.loads((ROOT/dep['path']).read_text(encoding='utf-8'))
            assert visual['contentSnapshotHash']==snapshot and visual['mediaAssetsHash']==checks['mediaAssetManifest']['sha256']
        for s in current:
            assert s['id'] not in used_ids and s['microSkillId'] in proposed,s['id']+' duplicate/unknown'
            assert s['contentHash'] not in used_texts,s['id']+' duplicated body'
            assert (s['microSkillId'],s['stage']) in proposed_cells,s['id']+' unplanned cell'
            used_ids.add(s['id']);used_texts.add(s['contentHash'])
            if s['source'].get('factLedgerPath'):
                dep=s['source']['factLedgerPath']
                if dep not in dependency_hashes:dependency_hashes[dep]=digest(ROOT/dep)
                assert dependency_hashes[dep]==s['source']['factLedgerHash'],s['id']+' stale fact source dependency'
            for q in s['questions']:
                assert q['id'] not in used_questions,q['id']+' duplicate question'
                used_questions.add(q['id'])
        sets.extend(current)
        batches.append(dict(id=batch['id'],role=batch['role'],source=batch['source'],contentSnapshotHash=snapshot,
          sets=len(current),questions=sum(len(s['questions']) for s in current),skills=len({s['microSkillId'] for s in current}),
          skillStageCells=len({(s['microSkillId'],s['stage']) for s in current}),browserRuntime=workbook['browserRuntime'],
          studentWorkbook=batch['artifacts']+'/학생용_문제집.html',teacherWorkbook=batch['artifacts']+'/교사용_해설집.html'))
    skills={s['microSkillId'] for s in sets};cells={(s['microSkillId'],s['stage']) for s in sets}
    approved=[s for s in sets if s['review']['teacherApproval']=='approved'];calibrated=[s for s in sets if s['review']['studentCalibration'] in ('verified','calibrated')]
    counts=blueprint['counts']
    rows=[]
    for sk in blueprint['skills']:
        subset=[s for s in sets if s['microSkillId']==sk['id']]
        rows.append(dict(skillId=sk['id'],grade=sk['grade'],name=sk['name'],track=sk['track'],
          authoredSets=len(subset),authoredQuestions=sum(len(s['questions']) for s in subset),
          stages={stage:sum(s['stage']==stage for s in subset) for stage in ['S1','S2','S3','S4','S5','S6']},
          approvedSets=sum(s['review']['teacherApproval']=='approved' for s in subset)))
    result=dict(asOf=registry['asOf'],scope='국어 V2 대표 제작분과 전체 은행 확장분의 현재 원고 합계. 기존 batch03·계획·버전 이력 제외.',
      goalCompletion='not_proven',publicationReady=False,batches=batches,
      authored=dict(sets=len(sets),questions=len(used_questions),skills=len(skills),skillStageCells=len(cells),
        skillsWithAllSixStages=sum(all((sid,stage) in cells for stage in ['S1','S2','S3','S4','S5','S6']) for sid in skills),
        factualSourceCheckedDraftSets=sum(bool(s['source'].get('factChecks')) for s in sets),factualAnchors=sum(len(s['source'].get('factChecks',[])) for s in sets),
        writingProductionProtocolSets=sum(bool(s.get('writingProtocol')) for s in sets),
        literaryInterpretationProtocolSets=sum(bool(s.get('literaryReview')) for s in sets),
        languageInterpretationProtocolSets=sum(bool(s.get('languageReview')) for s in sets),
        mediaReadingProtocolSets=sum(bool(s.get('mediaReview')) for s in sets),mediaPanels=sum(len(s.get('mediaPanels',[])) for s in sets),
        listeningSets=sum(bool(s.get('listening')) for s in sets),oralReadingSets=sum(bool(s.get('reading')) for s in sets),liveSpeechTasks=sum(q['kind']=='spoken_response' for s in sets for q in s['questions']),
        audioDraftAssets=len(audio_records),audioDurationSeconds=round(sum(a['durationSeconds'] for a in audio_records),3),
        byGrade={str(g):dict(sets=sum(s['grade']==g for s in sets),questions=sum(len(s['questions']) for s in sets if s['grade']==g),skills=len({s['microSkillId'] for s in sets if s['grade']==g})) for g in range(1,7)},
        poems=sum(len(s.get('poems',[])) for s in sets),poetryLines=sum(len(p['lines']) for s in sets for p in s.get('poems',[]))),
      proposed=dict(skills=counts['skills'],skillStageCells=counts['stageCells'],sets=counts['targetSets'],questions=counts['targetQuestions'],status='editorial_proposal_not_approved_curriculum'),
      remaining=dict(candidateSkills=len(proposed-skills),candidateStageCells=len(proposed_cells-cells),
        plannedSets=counts['targetSets']-len(sets),plannedQuestions=counts['targetQuestions']-len(used_questions)),
      review=dict(approvedSets=len(approved),calibratedSets=len(calibrated),independentTeacherReviewPending=len(sets)-len(approved),
        studentCalibrationPending=len(sets)-len(calibrated),
        audioListeningReviewsPending=sum(a.get('listeningReview')!='approved' for a in audio_records),
        koreanComponentCandidateSets=sum(bool(s['source'].get('officialStandards')) for s in sets),
        relatedOnlyScopeReviewSets=sum(s['source'].get('curriculumAudit',{}).get('decision')=='related_only_goal_scope_review' for s in sets),
        sourceUncheckedSets=[s['id'] for s in sets if not s['source'].get('officialStandards') and not s['source'].get('curriculumAudit')]),
      countingRule=registry['countingRule'])
    result['limits']=['자동 검사는 실제 교사 승인·문항 정답의 유일성·학생 난도 보정을 대체하지 않는다.',
      '여섯 단계는 학습 역할이며 공인 능력 등급이 아니다. 영역별 이름을 붙여도 실제 수행 차이를 따로 검토한다.',
      '원문 연결 후보는 부분 수행 또는 준비·보조 관계다. 성취기준 전체의 달성 승인이 아니다.',
      '장문·기능 집중 자료·시·소리 내어 읽기 등을 같은 길이의 지문 수로 계산하지 않는다.',
      '전체 공급 확대·최신 통합 고시 대조·음성 청취·실제 수업 및 브라우저 동작 검증이 남아 있다.']
    source_families=collections.defaultdict(list)
    for s in sets:
        for family in s['source'].get('sourceExposureFamilyIds',[]):source_families[family].append(s['id'])
    result['sharedFactualExposureFamilies']={key:ids for key,ids in source_families.items() if len(ids)>1}
    result['limits'].append('같은 출처·사실 배경을 공유하는 원고는 사전 노출을 확인해야 하며 서로 무관한 독립 확인 자료로 자동 계산하지 않는다.')
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'readiness.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'coverage.json').write_text(json.dumps(dict(asOf=registry['asOf'],batches=batches,skills=rows),ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(authored=result['authored'],remaining=result['remaining'],review=result['review'],goalCompletion=result['goalCompletion']),ensure_ascii=False))
    return result

if __name__=='__main__':report()
