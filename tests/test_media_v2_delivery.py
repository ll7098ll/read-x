"""Reject mismatched visual evidence and corrupted delivered assets."""
from contextlib import contextmanager,redirect_stdout
from pathlib import Path
import base64,io,json,re,shutil,sys,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from author_media_v2 import CELLS,SKILLS
from validate_pilot_v2 import validate
from verify_pilot_v2_workbook import verify
SOURCE=ROOT/'data/content_authoring/expansion_v2_06/sets.json'
OUT=ROOT/'output/expansion-v2-06'

@contextmanager
def scratch():
    temp=tempfile.TemporaryDirectory(prefix='media-negative-',dir=ROOT/'output')
    path=Path(temp.name).resolve();assert path.is_relative_to((ROOT/'output').resolve())
    try:yield path
    finally:
        assert Path(temp.name).resolve().is_relative_to((ROOT/'output').resolve())
        temp.cleanup()

def delivery_copy(path):
    for name in ['verification.json','media-assets.json','workbook-script.js','학생용_문제집.html','교사용_해설집.html','학생용_원고.txt']:
        if (OUT/name).exists():shutil.copyfile(OUT/name,path/name)

class MediaDeliveryTests(unittest.TestCase):
    def test_wrong_element_quote_is_rejected(self):
        with scratch() as temp:
            data=json.loads(SOURCE.read_text(encoding='utf-8'))
            data['sets'][0]['questions'][0]['evidence'][0]['quote']='원본 요소와 다른 문장'
            source=temp/'sets.json';source.write_text(json.dumps(data,ensure_ascii=False),encoding='utf-8')
            with redirect_stdout(io.StringIO()),self.assertRaises(SystemExit):
                validate(source,temp/'report',SKILLS,expected_stage_counts={sid:{stage:1 for stage in stages} for sid,stages in CELLS.items()})
            result=json.loads((temp/'report/verification.json').read_text(encoding='utf-8'))
            self.assertTrue(any('media element reference' in e for e in result['errors']))

    def test_changed_image_bytes_are_rejected(self):
        with scratch() as temp:
            delivery_copy(temp);file=temp/'학생용_문제집.html';text=file.read_text(encoding='utf-8')
            match=re.search(r'(data:image/png;base64,)([A-Za-z0-9+/=]+)',text);self.assertIsNotNone(match)
            payload=bytearray(base64.b64decode(match.group(2)));payload[-1]^=1
            text=text[:match.start(2)]+base64.b64encode(payload).decode()+text[match.end(2):];file.write_text(text,encoding='utf-8')
            with redirect_stdout(io.StringIO()),self.assertRaisesRegex(AssertionError,'embedded media bytes changed'):verify(SOURCE,temp)

    def test_changed_image_alternative_is_rejected(self):
        with scratch() as temp:
            delivery_copy(temp);file=temp/'학생용_문제집.html';text=file.read_text(encoding='utf-8')
            text,n=re.subn(r'(<img data-media="[^"]+"[^>]+ alt=")[^"]*(")',r'\1다른 그림의 설명\2',text,count=1)
            self.assertEqual(n,1);file.write_text(text,encoding='utf-8')
            with redirect_stdout(io.StringIO()),self.assertRaisesRegex(AssertionError,'media alternative changed'):verify(SOURCE,temp)

if __name__=='__main__':unittest.main()
