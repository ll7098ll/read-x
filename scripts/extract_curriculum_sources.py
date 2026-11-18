"""Extract paragraph text from downloaded MOE HWP annexes without changing sources."""
from pathlib import Path
import hashlib, json, re, struct, sys, zipfile, zlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'output/curriculum_2022/.python_deps'))
import olefile

BASE = ROOT / 'research/curriculum_2022/sources'
OUT = ROOT / 'research/curriculum_2022/extracted'
OUT.mkdir(parents=True, exist_ok=True)
subjects = {5:'국어',6:'도덕',7:'사회',8:'수학',9:'과학',10:'실과',11:'체육',12:'음악',13:'미술',14:'영어',15:'통합교과'}
manifest = []
for archive in ['subjects_05_14.zip', 'subjects_15_22.zip']:
    with zipfile.ZipFile(BASE / archive) as z:
        for info in z.infolist():
            name = info.filename
            if not info.flag_bits & 0x800:
                name = name.encode('cp437').decode('cp949')
            match = re.search(r'별책(\d+)', name)
            if not match or int(match[1]) not in subjects or not name.endswith('.hwp'):
                continue
            annex = int(match[1]); raw = z.read(info)
            local = BASE / f'annex_{annex:02}.hwp'; local.write_bytes(raw)
            paragraphs = []
            with olefile.OleFileIO(raw) as doc:
                header = doc.openstream('FileHeader').read()
                compressed = bool(struct.unpack_from('<I', header, 36)[0] & 1)
                sections = sorted([s for s in doc.listdir() if len(s)==2 and s[0]=='BodyText'], key=lambda s:int(s[1][7:]))
                for section in sections:
                    data = doc.openstream(section).read()
                    if compressed: data = zlib.decompress(data, -15)
                    offset = 0
                    while offset + 4 <= len(data):
                        record = struct.unpack_from('<I', data, offset)[0]; offset += 4
                        tag = record & 0x3ff; size = record >> 20
                        if size == 0xfff:
                            size = struct.unpack_from('<I', data, offset)[0]; offset += 4
                        payload = data[offset:offset+size]; offset += size
                        if tag != 67: continue
                        units = list(struct.unpack('<'+'H'*(len(payload)//2), payload[:len(payload)//2*2]))
                        cleaned = []; i = 0
                        while i < len(units):
                            code = units[i]
                            if code in (1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,22,23):
                                if code == 9: cleaned.append(' ')
                                i += 8
                            else:
                                if code >= 32: cleaned.append(chr(code))
                                i += 1
                        decoded = ''.join(cleaned).encode('utf-16-le', errors='surrogatepass').decode('utf-16-le', errors='replace')
                        text = re.sub(r'\s+', ' ', decoded).strip()
                        if text: paragraphs.append(text)
            (OUT / f'annex_{annex:02}.txt').write_text('\n'.join(paragraphs), encoding='utf-8')
            manifest.append({'sourceId':f'MOE2022-33-A{annex:02}', 'subject':subjects[annex], 'annex':annex,
                'officialFilename':name,'sha256':hashlib.sha256(raw).hexdigest(),'paragraphCount':len(paragraphs),
                'url':'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=141&boardSeq=93458&lev=0',
                'noticeVersion':'2022-33','retrievedOn':'2026-10-14','localFile':str(local.relative_to(ROOT)).replace('\\','/')})
(OUT / 'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False, indent=2))
