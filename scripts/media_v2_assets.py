"""Render authored media with Korean fonts; retain element bounds and source hashes."""
from pathlib import Path
import hashlib,json,math
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
FONT=Path('C:/Windows/Fonts/malgun.ttf')
BOLD=Path('C:/Windows/Fonts/malgunbd.ttf')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def font(size,bold=False):return ImageFont.truetype(str(BOLD if bold else FONT),size)
def wrap(text,f,width):
    lines=[];line=''
    for word in text.split():
        candidate=(line+' '+word) if line else word
        if f.getlength(candidate)<=width:line=candidate;continue
        if line:lines.append(line);line=''
        for ch in word:
            if line and f.getlength(line+ch)>width:lines.append(line);line=ch
            else:line+=ch
    if line:lines.append(line)
    return lines or ['']

def icon(draw,name,box):
    x,y,w=box;cx=x+w/2;cy=y+w/2
    if name=='talk':
        draw.rounded_rectangle((x+12,y+20,x+w-12,y+w-28),20,outline='#24586b',width=7)
        draw.line([(x+45,y+w-30),(x+26,y+w-4),(x+80,y+w-30)],fill='#24586b',width=7)
        for yy in (y+55,y+85):draw.line((x+42,yy,x+w-42,yy),fill='#24586b',width=7)
    elif name=='cup':
        draw.polygon([(x+38,y+24),(x+w-38,y+24),(x+w-48,y+w-18),(x+48,y+w-18)],fill='#d8edf2',outline='#24586b',width=7)
        draw.arc((x+w-65,y+42,x+w-7,y+w-38),-90,90,fill='#24586b',width=7)
        draw.line((x+45,y+78,x+w-45,y+78),fill='#297f98',width=6)
    else:
        draw.ellipse((x+16,y+16,x+w-16,y+w-16),fill='#e2efe9',outline='#24586b',width=7)
        draw.arc((x+45,y+16,x+w-45,y+w-16),90,270,fill='#24586b',width=5)
        draw.line((x+19,cy,x+w-19,cy),fill='#24586b',width=5)
        if name=='no_ball':draw.line((x+8,y+w-8,x+w-8,y+8),fill='#b73536',width=14)

def render_panel(p,path):
    width=1280;padding=54;usable=width-padding*2;layout=[];y=150
    for e in p['elements']:
        size={'large':76,'header':40,'body':36,'small':28}[e['style']];f=font(size,e['style'] in ('header','large'))
        cells=e['text'].split(' | ') if p['kind']=='table' and ' | ' in e['text'] else [e['text']]
        if e.get('icon'):y+=190
        cellwidth=usable/len(cells)
        lines=[wrap(c,f,cellwidth-40) for c in cells]
        height=max(len(ls) for ls in lines)*(size+18)+36
        layout.append(dict(id=e['id'],text=e['text'],box=[padding,y,usable,height],fontPx=size,style=e['style'],lines=lines,cells=cells,icon=e.get('icon')))
        y+=height+(8 if p['kind']=='table' else 20)
    image=Image.new('RGB',(width,y+40),'#f5f8fa');draw=ImageDraw.Draw(image)
    draw.rounded_rectangle((15,15,width-15,image.height-15),24,fill='white',outline='#a8bfca',width=3)
    draw.text((padding,32),p['title'],font=font(38,True),fill='#173d4b')
    draw.text((padding,92),'학습용 가상 자료',font=font(24),fill='#536b76')
    for row in layout:
        x,top,w,h=row['box'];e=next(e for e in p['elements'] if e['id']==row['id'])
        if row['icon']:icon(draw,row['icon'],(width/2-80,top-180,160))
        fg='#173d4b';bg='#f0f5f6'
        if row['style']=='header':fg='white';bg='#245565'
        elif row['style']=='large':fg='#70400a';bg='#fff0cf'
        elif row['style']=='small':fg='#425761';bg='#f1f3f4'
        cw=w/len(row['cells'])
        for i,ls in enumerate(row['lines']):
            left=x+i*cw
            draw.rectangle((left,top,left+cw,top+h),fill=bg,outline='#c2d3da',width=2)
            for j,line in enumerate(ls):draw.text((left+20,top+12+j*(row['fontPx']+18)),line,font=font(row['fontPx'],row['style'] in ('large','header')),fill=fg)
    path.parent.mkdir(parents=True,exist_ok=True);image.save(path,optimize=True)
    return dict(width=width,height=image.height,renderedElements=layout)

def build(source,out):
    source=Path(source);out=Path(out);sets=json.loads(source.read_text(encoding='utf-8'))['sets'];assets=[]
    for s in sets:
        for p in s.get('mediaPanels',[]):
            path=out/'media'/str(p['id']+'.png');meta=render_panel(p,path)
            assets.append(dict(id=p['id'],materialId=s['id'],png=path.relative_to(ROOT).as_posix(),pngHash=digest(path),panelDataHash=hashlib.sha256(json.dumps(p,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),**meta))
    manifest=dict(contentSnapshotHash=digest(source),assets=assets,rendering='Pillow with local Malgun Gothic. Static assets, not a browser screenshot or actual reader observation.')
    out.mkdir(parents=True,exist_ok=True);(out/'media-assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    for page in range(math.ceil(len(assets)/9)):
        group=assets[page*9:(page+1)*9];sheet=Image.new('RGB',(1500,math.ceil(len(group)/3)*660),'#e4edf1');d=ImageDraw.Draw(sheet)
        for i,a in enumerate(group):
            im=Image.open(ROOT/a['png']);im.thumbnail((480,595));x=(i%3)*500+(500-im.width)//2;y=(i//3)*660+45
            sheet.paste(im,(x,y));d.text(((i%3)*500+10,(i//3)*660+7),a['id'].replace('PV2-',''),font=font(18),fill='#173d4b')
        sheet.save(out/f'media-preview-{page+1}.png')
    return manifest
