"""Reject stale request/input/WAV provenance without changing real audio or authoring data."""
from pathlib import Path
import copy,json,hashlib,argparse
from verify_pilot_v2_audio import verify
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'output/pilot-v2/audio'

def check(folder=None,report_name='listening-synthesis-result.json'):
    FOLDER=Path(folder).resolve() if folder else ROOT/'output/pilot-v2/audio'
    assert FOLDER.is_relative_to((ROOT/'output').resolve()) and Path(report_name).name==report_name
    original=json.loads((FOLDER/report_name).read_text(encoding='utf-8-sig'))
    request=json.loads(Path(original['requestFile']).read_text(encoding='utf-8'))
    source=(ROOT/request.get('sourcePath','data/content_authoring/pilot_v2/sets.json')).resolve()
    assert source.is_relative_to(ROOT)
    temporary=FOLDER/'_freshness_test_report.json'
    unexpected=FOLDER/'_unexpected_test_success.json'
    assert not temporary.exists() and not unexpected.exists(),'Remove no files implicitly; test paths must be unused'
    cases={}
    try:
        for field,message in [('requestHash','different request version'),('textHash','Speech input changed'),('fileHash','Synthesized WAV changed')]:
            invalid=copy.deepcopy(original)
            if field=='requestHash':invalid[field]='0'*64
            else:invalid['assets'][0][field]='0'*64
            temporary.write_text(json.dumps(invalid,ensure_ascii=False),encoding='utf-8')
            try:verify(temporary.name,unexpected.name,FOLDER)
            except AssertionError as error:
                assert message in str(error),(field,str(error))
                cases[field]='rejected_as_expected'
            else:raise RuntimeError('Freshness check unexpectedly accepted '+field)
    finally:
        temporary.unlink(missing_ok=True)
        unexpected.unlink(missing_ok=True)
    report=dict(passed=True,cases=cases,contentSnapshotHash=hashlib.sha256(source.read_bytes()).hexdigest(),scope='메타데이터만 바꾼 잘못된 보고서를 거부하는지 확인. 실제 대본·WAV는 수정하지 않음.')
    (FOLDER/'freshness-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--directory');parser.add_argument('--report',default='listening-synthesis-result.json');args=parser.parse_args()
    check(args.directory,args.report)
