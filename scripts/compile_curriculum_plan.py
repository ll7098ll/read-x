"""Compile the authored semester map; retain evidence status and unmapped standards."""
from pathlib import Path
import collections, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/curriculum_2022'
standards=json.loads((DATA/'achievement_standards.json').read_text(encoding='utf-8'))
by_id={s['id']:s for s in standards}
sources={
 'MOE':{'title':'교육부 고시 제2022-33호 교과별 원문','url':'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=141&boardSeq=93458&lev=0','scope':'학년군·내용 근거. 학기 배치 근거 아님'},
 'VM34':{'title':'비상 수학 3~4 방정숙 목차','url':'https://text.vivasam.com/detail/94','scope':'해당 출판사 단원 배치'},
 'VM56':{'title':'비상 수학 5~6 방정숙 목차','url':'https://text.vivasam.com/detail/83','scope':'해당 출판사 단원 배치'},
 'VS34':{'title':'비상 사회 3~4 설규주 목차','url':'https://text.vivasam.com/detail/96','scope':'해당 출판사 단원 배치'},
 'VS56':{'title':'비상 사회 5~6 설규주 목차','url':'https://text.vivasam.com/detail/85','scope':'해당 출판사 단원 배치'},
 'VC34':{'title':'비상 과학 3~4 강석진 목차','url':'https://text.vivasam.com/detail/97','scope':'해당 출판사 단원 배치'},
 'VC56':{'title':'비상 과학 5~6 강석진 목차','url':'https://text.vivasam.com/detail/87','scope':'해당 출판사 단원 배치'},
 'GOE1':{'title':'2026 신입생 학부모를 위한 초등학교 안내서','url':'https://www.goegh.kr/dext5editordata/2025/12/20251217_113442804_21888.pdf','scope':'1학년 통합교과 주제의 학기 배치. 개별 개념의 배치 확정 아님'},
 'AMEND26':{'title':'국가교육위원회 고시 제2026-1호','url':'https://www.ne.go.kr/new/user/bbs/BD_selectBbs.do?q_bbsDocNo=20260121102419070&q_bbsSn=1016','scope':'초1~2 건강한 생활 등의 개정 적용은 2028-03-01. 2026 운영 목록과 분리'},
}
placements=[]; concepts={}
for line in (DATA/'semester_plan.psv').read_text(encoding='utf-8').splitlines():
 if not line or line.startswith('#'):continue
 grade,term,subject,units,names,refs,status,source_id=line.split('|')
 grade=int(grade); term=int(term)
 ids=[]
 for ref in refs.split(','):
  matches=[s for s in by_id if s.startswith(ref[:-1])] if ref.endswith('*') else [ref]
  assert matches,ref
  for code in matches:
   assert code in by_id,code
   assert by_id[code]['subject']==subject,(subject,code)
   assert grade in by_id[code]['gradeBand'],(grade,code)
   if code not in ids:ids.append(code)
 pid=f'G{grade}-S{term}-{subject}'
 concept_ids=[]
 for name in names.split(';'):
  cid='C22-'+hashlib.sha256(f'{subject}|{name}'.encode()).hexdigest()[:12]
  if cid not in concepts:
   concepts[cid]={'id':cid,'subject':subject,'name':name,'placements':[],'reviewState':'needs_review',
                 'alignmentState':'related_standard_group_not_individually_verified'}
  concepts[cid]['placements'].append(pid);concept_ids.append(cid)
 placements.append({'id':pid,'grade':grade,'semester':term,'subject':subject,'units':units,
   'conceptIds':concept_ids,'conceptNames':names.split(';'),'relatedStandardIds':ids,
   'placementStatus':status,'placementSourceId':source_id,'reviewState':'needs_review'})
assert len(placements)==96
assert len({x['id'] for x in placements})==len(placements)
covered={code for p in placements for code in p['relatedStandardIds']}
unmapped=[s['id'] for s in standards if s['id'] not in covered]
data={'schemaVersion':'1.0','asOf':'2026-10-14','basis':'2022-33 원문 기반 초등 교과 목록; 일부개정 대조 상태는 sourceVersionNotes 참조',
 'sourceVersionNotes':['2026-1호 총론의 초1~2 변경 적용일 2028-03-01 확인. 현재 목록에 건강한 생활을 소급 적용하지 않음.',
 '사회·음악의 2024-3호 각론 전체 대조는 미완료. 기준 원장의 문장은 2022-33호 원문이며 최신 통합본 인증이 아님.',
 '교과서 목차 확인은 해당 출판사의 단원 배치 확인. 개별 개념-성취기준의 일대일 검증 및 전국 공통 학기 배치를 뜻하지 않음.',
 '원문 텍스트 추출은 표의 배열과 수식 객체를 완전히 보존하지 않음. 수식이나 상세 조건은 원본 HWP에서 재확인.'],
 'sources':sources,'placements':placements,'concepts':list(concepts.values()),'unmappedStandardIds':unmapped}
(DATA/'curriculum_registry.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'semesterSubjectRows':len(placements),'uniqueConceptCandidates':len(concepts),
 'placementStatuses':dict(collections.Counter(p['placementStatus'] for p in placements)),
 'standardsInRelatedGroups':len(covered),'unmappedStandards':unmapped},ensure_ascii=False,indent=2))
