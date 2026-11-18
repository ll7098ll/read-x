"""Build and verify only the declared twelve nonfiction drafts; never claims a full six-stage supply."""
import json,hashlib
from author_nonfiction_v2 import build,DEST,OUT,ROOT,SKILLS,STAGES
from validate_pilot_v2 import validate
from build_pilot_v2_workbook import build as render
from verify_pilot_v2_workbook import verify

def main():
    source=build()
    checks=validate(source,OUT,SKILLS,comparison_sources=[ROOT/'data/content_authoring/pilot_v2/sets.json',ROOT/'data/content_authoring/expansion_v2_01/sets.json'],
      expected_stage_counts={sid:{stage:2} for sid,stage in STAGES.items()})
    render(source,OUT,'expansion-v2-02');workbook=verify(source,OUT)
    sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    summary=dict(asOf='2026-11-17',contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),sets=len(sets),
      questions=sum(len(s['questions']) for s in sets),newSkills=len(SKILLS),newSkillStageCells=len(STAGES),
      factualSourceCheckedDraftSets=checks['factualSourceCheckedDraftSets'],factualAnchors=checks['factualAnchors'],
      sourcePages=len({r['id'] for s in sets for r in s['source']['factualReferences']}),passed=checks['passed'] and workbook['passed'],
      teacherApproval='pending',studentCalibration='pending',browserRuntime=workbook['browserRuntime'])
    (OUT/'build-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False))

if __name__=='__main__':main()
