"""Create real, portable graphs from the authored source, including deliberate review drafts."""
from pathlib import Path
import os,json,hashlib,math
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pilot-v2'
os.environ['MPLCONFIGDIR']=str(OUT/'.matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from PIL import Image,ImageOps,ImageDraw,ImageFont

FONT=Path('C:/Windows/Fonts/malgun.ttf')
font_manager.fontManager.addfont(str(FONT))
plt.rcParams.update({'font.family':font_manager.FontProperties(fname=str(FONT)).get_name(),
                     'font.size':14,'axes.unicode_minus':False,'svg.fonttype':'path',
                     'svg.hashsalt':'readx-pilot-v2'})

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def render_graph(g,dest):
    fig,ax=plt.subplots(figsize=(7.2,4.4),dpi=130)
    fig.set_facecolor('white')
    fig.subplots_adjust(left=.20,right=.94,bottom=.18,top=.74)
    fig.suptitle(g['title'],x=.5,y=.95,fontsize=17,fontweight='bold',color='#193e50')
    if g['kind']=='pictograph':
        counts=[v//g['symbolValue'] for v in g['values']]
        for y,count in enumerate(counts):
            marks=ax.scatter(range(1,count+1),[y]*count,marker='*',s=520,
                             c='#297d83',edgecolors='#15565d',linewidths=.8,zorder=3)
            marks.set_gid('row-'+str(y))
        ax.set_yticks(range(len(g['labels'])),g['labels'])
        ax.set_xlim(.35,max(counts)+.8);ax.set_ylim(len(counts)-.45,-.55)
        ax.set_xticks([])
        ax.tick_params(axis='y',length=0,pad=16)
        for spine in ax.spines.values():spine.set_visible(False)
        # Missing legends intentionally expose no numerical answer, even as SVG metadata.
        legend=fig.text(.5,.81,g['elements']['legend'],ha='center',fontsize=15,
                        bbox={'boxstyle':'round,pad=.45','fc':'#eef5f6','ec':'#c6dadd'})
        legend.set_gid('legend')
        fig.text(.5,.06,'기호 하나하나를 세어 범례와 함께 읽으세요.',ha='center',fontsize=11,color='#526775')
    else:
        minimum,maximum,step=g['axisMin'],g['axisMax'],g['axisStep']
        bars=ax.bar(range(len(g['labels'])),[v-minimum for v in g['values']],bottom=minimum,
                    color='#377f91',width=.50,edgecolor='#205264',linewidth=1,zorder=3)
        for i,rect in enumerate(bars):rect.set_gid('row-'+str(i))
        ax.yaxis.set_gid('axis')
        ticks=list(range(minimum,maximum+1,step))
        ax.set_yticks(ticks,['□' if t in g.get('hiddenTicks',[]) else str(t) for t in ticks])
        ax.set_ylim(minimum,maximum)
        ax.set_xticks(range(len(g['labels'])),g['labels'])
        ax.set_xlim(-.6,len(g['labels'])-.4)
        ax.set_ylabel('단위: '+g['unit'],labelpad=13)
        ax.yaxis.grid(True,color='#dbe6eb',linewidth=.8);ax.set_axisbelow(True)
        ax.spines[['top','right']].set_visible(False)
        for i,v in enumerate(g['values']):
            ax.annotate(str(v)+g['unit'],(i,v),xytext=(0,6),textcoords='offset points',
                        ha='center',va='bottom',fontsize=14,color='#173b49')
        fig.text(.5,.81,'세로축의 수와 단위를 확인하세요.',ha='center',fontsize=12,color='#526775')
    svg=dest/(g['id']+'.svg');png=dest/(g['id']+'.png')
    fig.savefig(svg,metadata={'Date':None,'Description':g['accessibleDescription'],'Creator':'ReadX authored pilot'})
    fig.savefig(png,metadata={'Description':g['accessibleDescription']})
    plt.close(fig)
    with Image.open(png) as im:dimensions=list(im.size)
    return dict(id=g['id'],svg=str(svg.relative_to(ROOT)).replace('\\','/'),svgHash=digest(svg),
                png=str(png.relative_to(ROOT)).replace('\\','/'),pngHash=digest(png),dimensions=dimensions,
                graphDataHash=hashlib.sha256(json.dumps(g,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
                intentionalPresentation=g.get('intentionalPresentation'))

def build():
    source=ROOT/'data/content_authoring/pilot_v2/sets.json'
    sets=json.loads(source.read_text(encoding='utf-8'))['sets']
    dest=OUT/'assets';dest.mkdir(parents=True,exist_ok=True)
    assets=[render_graph(g,dest) for s in sets for g in s.get('graphs',[])]
    manifest=dict(contentSnapshotHash=digest(source),assets=assets)
    (OUT/'graph-assets.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    # A contact sheet is a local visual QA aid, not an assessment or a web preview.
    cell_w,cell_h=660,440
    gallery=Image.new('RGB',(cell_w*3,cell_h*math.ceil(len(assets)/3)),'#e4ebef')
    draw=ImageDraw.Draw(gallery);label_font=ImageFont.truetype(str(FONT),16)
    for i,a in enumerate(assets):
        x,y=(i%3)*cell_w,(i//3)*cell_h
        draw.text((x+16,y+12),a['id'],font=label_font,fill='#183b50')
        with Image.open(ROOT/a['png']) as im:
            im=ImageOps.contain(im,(cell_w-20,cell_h-48))
            gallery.paste(im,(x+(cell_w-im.width)//2,y+42))
    gallery.save(OUT/'그래프_검수_모음.png')
    print('Rendered',len(assets),'graphs and local QA sheet')
    return manifest

if __name__=='__main__':build()
