"""Generate Read X's vector assets and a self-contained, versioned handoff kit."""
from pathlib import Path
import json
import re
import shutil
import sys
from zipfile import ZipFile, ZIP_DEFLATED
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'output/read-x-v3/.deps'))
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.subset import Subsetter

PUBLIC = ROOT / 'webapp/public/brand'
OUT = ROOT / 'output/read-x-v3'
OUT.mkdir(parents=True, exist_ok=True)
PUBLIC.mkdir(parents=True, exist_ok=True)

def symbol(mono=False, reverse=False):
    bg, first, second = ('#202D40', '#FFFFFF', '#FFFFFF') if mono else ('#DDF58A', '#202D40', '#3157D5')
    if reverse: bg, first, second = '#FFFFFF', '#202D40', '#202D40'
    return f'<rect width="64" height="64" rx="16" fill="{bg}"/><path d="M19 18L45 46" stroke="{first}" stroke-width="8" stroke-linecap="round"/><path d="M45 18L19 46" stroke="{bg}" stroke-width="14" stroke-linecap="round"/><path d="M45 18L19 46" stroke="{second}" stroke-width="8" stroke-linecap="round"/>'

def svg(contents, width=64, height=64):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Read X"><title>Read X</title>{contents}</svg>\n'

assets = {
    'readx-symbol.svg': svg(symbol()),
    'readx-symbol-mono.svg': svg(symbol(mono=True)),
    'read-x-symbol-reverse.svg': svg(symbol(reverse=True)),
}
font = TTFont(ROOT / 'webapp/public/fonts/PretendardVariable.woff2')
subset = Subsetter()
subset.populate(text='Read X')
subset.subset(font)
font = instantiateVariableFont(font, {'wght': 760}, inplace=False)
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
units = font['head'].unitsPerEm
scale = 46 / units

def wordmark(dark=False):
    cursor, parts = 0, []
    for char in 'Read X':
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        color = ('#DDF58A' if dark else '#3157D5') if char == 'X' else ('#FFFFFF' if dark else '#202D40')
        parts.append(f'<path d="{pen.getCommands()}" transform="translate({cursor:.3f} 0)" fill="{color}"/>')
        cursor += glyphs[name].width - (units * 0.035 if char != ' ' else 0)
    return f'<g transform="translate(82 49) scale({scale:.6f} {-scale:.6f})">{"".join(parts)}</g>'

assets['read-x-wordmark.svg'] = svg(symbol()+wordmark(), 250, 64)
assets['read-x-wordmark-reverse.svg'] = svg(symbol()+wordmark(True), 250, 64)
for filename, contents in assets.items():
    (PUBLIC/filename).write_text(contents, encoding='utf-8')

css = (ROOT/'webapp/src/read-x-tokens.css').read_text(encoding='utf-8')
tokens = {}
for key, value in re.findall(r'--readx-([\w-]+):\s*([^;]+);', css):
    kind = 'color' if value.startswith('#') else 'dimension' if value.endswith('px') else 'duration' if value.endswith('ms') else 'string'
    tokens[key] = {'$type': kind, '$value': value.strip()}
(PUBLIC/'read-x-tokens.json').write_text(json.dumps({'name':'Read X', 'version':'3.0', 'tokens':tokens}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
(PUBLIC/'read-x-tokens.css').write_text(css, encoding='utf-8')
for source, target in [('docs/READ_X_BRAND_UI_UX_KIT_V3.md','read-x-guidelines.md'),('docs/READ_X_COMPONENT_SPEC_V3.md','read-x-components.md')]:
    shutil.copyfile(ROOT/source, PUBLIC/target)

archive = ROOT/'docs/archive'
archive.mkdir(exist_ok=True)
for filename, target in [('CI_AND_UI_UX_THEME_KIT_MASTER.md','READ_X_BRAND_UI_UX_KIT_V3.md'),('UI_UX_COMPONENT_DEVELOPMENT_SPEC.md','READ_X_COMPONENT_SPEC_V3.md')]:
    original = ROOT/filename
    backup = archive/(original.stem+'_PRE_V3.md')
    if not backup.exists(): shutil.copyfile(original, backup)
    original.write_text(f'# Read X — 현재 디자인 기준\n\n2026-11-14부터 공식 브랜드는 **Read X / 리드엑스**입니다.\n\n**읽으라고 하기 전에, 읽는 방법부터.**\n\n현재 규격: [Read X v3](docs/{target})\n\n인터랙티브 킷: 웹앱 `#/brand`\n\n이전 규격은 [변경 이력](docs/archive/{backup.name})으로 보존했습니다. 새 화면은 v3를 따릅니다.\n',encoding='utf-8')

def luminance(hexcolor):
    vals = [int(hexcolor[i:i+2],16)/255 for i in (1,3,5)]
    vals = [v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
    return sum(a*b for a,b in zip(vals,[.2126,.7152,.0722]))

pairs = [('본문','#202D40','#F7F8F2'),('주 버튼','#FFFFFF','#3157D5'),('보조 설명','#586579','#F7F8F2'),('라임 면','#202D40','#DDF58A'),('성공','#21664B','#E9F5ED'),('도움','#785410','#FFF4D8'),('오류','#AA3548','#FFF0F2'),('입력 경계','#7D899B','#FFFFFF')]
contrast = []
for label, fg, bg in pairs:
    a,b = sorted([luminance(fg),luminance(bg)])
    ratio=(b+.05)/(a+.05)
    threshold=3 if label=='입력 경계' else 4.5
    assert ratio>=threshold, (label,ratio)
    contrast.append({'label':label,'foreground':fg,'background':bg,'ratio':round(ratio,2),'threshold':threshold,'passed':True})
(OUT/'contrast-check.json').write_text(json.dumps(contrast,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

files = list(assets) + ['read-x-tokens.json','read-x-tokens.css','read-x-guidelines.md','read-x-components.md']
with ZipFile(PUBLIC/'read-x-kit.zip','w',ZIP_DEFLATED) as z:
    for name in files: z.write(PUBLIC/name, name)
    z.write(ROOT/'webapp/public/fonts/Pretendard-LICENSE.txt','fonts/Pretendard-LICENSE.txt')
    for filename in ['ReadXBrand.tsx','readXSystem.ts','ReadingMethodDemo.tsx','BrandKit.tsx']:
        z.write(ROOT/'webapp/src/components/brand'/filename,'react/'+filename)
    z.write(ROOT/'webapp/src/read-x.css','web/read-x.css')
    z.writestr('README.txt','Read X v3 / 2026-11-14\nSee read-x-guidelines.md and read-x-components.md.\nSVG wordmarks are outlined. Pretendard license is included.\nReact examples require React, lucide-react and the existing project Dialog component.\nCSS kit includes integration selectors for the existing Read X app.\nThe app route #/brand is the interactive showcase.\n')
for name in files+['read-x-kit.zip']:
    shutil.copyfile(PUBLIC/name,OUT/name)
print(json.dumps({'output':str(OUT),'assets':len(files),'contrast_pairs':len(contrast),'zip_bytes':(PUBLIC/'read-x-kit.zip').stat().st_size},ensure_ascii=False))
