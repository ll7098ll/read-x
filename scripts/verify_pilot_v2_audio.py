"""Inspect actual synthesized WAV files; do not imply pronunciation or student calibration."""
from pathlib import Path
import json,wave,array,math,hashlib,sys,argparse
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pilot-v2/audio'

def verify(report_name='synthesis-result.json',output_name='verification.json',out=None):
 OUT=Path(out).resolve() if out else ROOT/'output/pilot-v2/audio'
 assert OUT.is_relative_to((ROOT/'output').resolve()),'Audio directory outside workspace output'
 assert Path(report_name).name==report_name and Path(output_name).name==output_name
 report=json.loads((OUT/report_name).read_text(encoding='utf-8-sig'))
 request_path=Path(report['requestFile'])
 request=json.loads(request_path.read_text(encoding='utf-8'))
 assert report['requestHash']==hashlib.sha256(request_path.read_bytes()).hexdigest(),'Synthesis used a different request version'
 expected={r['id']:r for r in request['requests']};assets=[]
 assert len(expected)==len(request['requests']) and report['assets']
 if request.get('sourceSnapshotHash'):
  source=(ROOT/request.get('sourcePath','data/content_authoring/pilot_v2/sets.json')).resolve()
  assert source.is_relative_to(ROOT),'Audio source outside workspace'
  assert request['sourceSnapshotHash']==hashlib.sha256(source.read_bytes()).hexdigest(),'Stale listening request'
 assert set(expected)=={a['id'] for a in report['assets']}
 for a in report['assets']:
  path=Path(a['path']).resolve();assert path.parent==OUT.resolve()
  assert a['textHash']==hashlib.sha256(expected[a['id']]['text'].encode()).hexdigest(),'Speech input changed'
  assert a['fileHash']==hashlib.sha256(path.read_bytes()).hexdigest(),'Synthesized WAV changed'
  with wave.open(str(path),'rb') as wav:
   rate,channels,width,frames=wav.getframerate(),wav.getnchannels(),wav.getsampwidth(),wav.getnframes()
   assert wav.getcomptype()=='NONE' and width==2 and rate>=16000 and channels in (1,2)
   samples=array.array('h',wav.readframes(frames))
   if sys.byteorder!='little':samples.byteswap()
  assert len(samples)==frames*channels and frames>rate*.3
  rms=math.sqrt(sum(v*v for v in samples)/len(samples))/32768
  peak=max(abs(v) for v in samples)/32768
  assert rms>.0001,'Silent or nearly silent synthesized audio'
  assert a['language']=='ko-KR' and a['contentType']=='audio/wav'
  assets.append(dict(id=a['id'],path=str(path.relative_to(ROOT)).replace('\\','/'),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
   intendedTextHash=hashlib.sha256(expected[a['id']]['text'].encode()).hexdigest(),voice=a['voice'],language=a['language'],
   durationSeconds=round(frames/rate,3),sampleRate=rate,channels=channels,pcmBits=width*8,rmsDbFS=round(20*math.log10(rms),2),peakFraction=round(peak,5),
   clippingFraction=round(sum(abs(v)>=32767 for v in samples)/len(samples),6),listeningReview='pending',materialId=expected[a['id']].get('materialId'),usage=expected[a['id']].get('usage','listening_material' if expected[a['id']].get('materialId') else 'technical_probe')))
 result=dict(passed=True,requestFile=str(request_path.relative_to(ROOT)).replace('\\','/'),requestHash=hashlib.sha256(request_path.read_bytes()).hexdigest(),
  assets=assets,purpose=request.get('purpose'),countedLearningSets=0,countingNote='음성 파일 수를 자료 묶음 수에 추가 합산하지 않는다. 집필 수는 진행 원장으로 관리한다.',approvedLearningSets=0,authoredAudioSets=len({a['materialId'] for a in assets if a['materialId']}),authoredListeningSets=sum(a['usage']=='listening_material' for a in assets),authoredReadingModelSets=sum(a['usage']=='reading_model_after_first_read' for a in assets),contentSnapshotHash=request.get('sourceSnapshotHash'),
  limits=['WAV 구조·길이·무음 여부를 확인했다. 발음·쉼·속도의 청취 확인과 수업 적합성은 검토 대기다.'])
 (OUT/output_name).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps(dict(passed=True,assets=len(assets),durationSeconds=round(sum(a['durationSeconds'] for a in assets),3),maximumClippingFraction=max(a['clippingFraction'] for a in assets),authoredListeningSets=result['authoredListeningSets'],authoredReadingModelSets=result['authoredReadingModelSets'],listeningReview='pending'),ensure_ascii=False))
 return result

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--report',default='synthesis-result.json');parser.add_argument('--output',default='verification.json');parser.add_argument('--directory');args=parser.parse_args()
 verify(args.report,args.output,args.directory)
