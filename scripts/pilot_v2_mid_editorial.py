"""Individual explanations and structured graph evidence for the next pilot skills."""
EXPLANATIONS={
 'G2-writing-11':[
 '날짜와 시각은 이미 있지만 만날 장소가 빠졌다. 독자가 실제로 갈 곳을 묻는 상황과 연결한다.',
 '색·그림·보관 장소는 메모에 확인된 정보다. 크기나 주인 이름은 확인하지 않아 지어 넣을 수 없다.',
 '학생은 빈 통 한 개를 준비하고 구슬은 교사가 준다. 물건과 수량, 제공자를 함께 보존한다.',
 '다음 화요일 점심시간 도서실 앞이 확인한 때와 곳이다. 종료 시각을 임의로 추가하지 않는다.',
 '이름을 적는 조건은 만들기 체험 대상이며 관람만 하는 사람은 신청하지 않는다. 보충하면서 대상 범위를 넓히지 않는다.',
 '접기 뒤 옆면을 붙이고 풀이 마른 뒤 이름을 써야 한다. 빠진 행동과 기다릴 조건을 함께 넣는다.',
 '새 친구가 모르는 별명을 지도상의 이름과 위치로 연결해야 장소를 찾을 수 있다.',
 '다섯 개 준비를 한 개로 줄이는 행동은 수량 정보가 빠졌음을 보여 준다. 날짜와 물건은 이미 알려졌다.',
 '확인한 메모는 수요일 세 시 도서실과 연필 지참이다. 글이 길어져도 틀린 시간·장소·제공자를 넣으면 정확하지 않다.',
 '모형 한 개는 확정이고 시작 시각·장소는 미정이다. 확정 사실만 보태고 미정은 후속 안내로 구별한다.',
 '지갑 지참이 기본이지만 없으면 대여하며 놀이 돈은 현장에서 준다. 기본과 예외, 제공자를 함께 남긴다.',
 '확인한 보관 장소는 도서실 대출대다. 뚜껑은 물건 특징이고 주인 이름은 아직 확인되지 않았다.'],
 'G4-media-02':[
 '범례가 별 한 개를 책 두 권으로 정했다. 종류 이름이나 기호 개수와 구별해 실제 책 수를 읽는다.',
 '세로축 단위가 학생 명수이므로 높이는 선택한 학생 수를 뜻한다. 시간·정도·재료 수로 바꾸지 않는다.',
 '나 반의 별 네 개에 한 별당 주머니 두 개를 적용하면 여덟 개다. 다른 줄이나 기호 개수만 읽지 않는다.',
 '화 막대는30개에 이른다. 한 칸5개이므로 여섯 칸을6개라고 읽으면 안 된다.',
 '첫 범례는2권, 둘째는4권이다. 월요일의4별과2별은 각각8권으로 같은 기록이다.',
 '그래프 순서는 나·다·가이므로 첫 막대의 이름 나와 값9명을 함께 읽어야 한다. 표의 행 순서를 그대로 옮기지 않는다.',
 '가12권이3별이므로 한 별은4권이다. 나5별도20권이 되어 같은 범례를 확인한다.',
 '0에서4까지 같은 간격 두 칸이므로 한 칸은2명이다. 빈 눈금은2다.',
 '실제 값은8권과10권으로 차이2권이다.6에서 시작한 그림의 보이는 길이2와4를 실제 비율로 오해하지 않는다.',
 '그림의 수량5는 맞지만 책을 센 단위가 명으로 잘못 표시됐다. 권으로 고치고 대출 인원은 별도 미확인으로 둔다.',
 '가8개와 나14개의 차이는6개다.14는8의 두 배가 아니며 장바구니 수로 참여 학생 수를 정할 수 없다.',
 '책12·18권과 참여6·9명은 다른 대상을 센 자료다. 오후18권/9명이2여도 개인별 권수가 모두 같다는 근거는 없다.']}

def pict(title,labels,values,amount,unit,**extra):
 return dict(kind='pictograph',title=title,labels=labels,values=values,symbolValue=amount,unit=unit,**extra)
def bar(title,labels,values,unit,maximum,step,minimum=0,**extra):
 return dict(kind='bar',title=title,labels=labels,values=values,unit=unit,axisMin=minimum,axisMax=maximum,axisStep=step,**extra)
GRAPHS={
 'S1-A':[pict('빌린 책의 종류',['이야기책','정보책'],[6,10],2,'권')],
 'S1-B':[bar('선택한 활동',['줄넘기','공놀이'],[3,7],'명',8,1)],
 'S2-A':[pict('학급별 책 주머니',['가','나','다'],[6,8,10],2,'개')],
 'S2-B':[bar('날짜별 모은 뚜껑',['월','화','수'],[20,30,10],'개',35,5)],
 'S3-A':[pict('첫 그래프',['월','화'],[8,12],2,'권'),pict('둘째 그래프',['월','화'],[8,12],4,'권')],
 'S3-B':[bar('모둠별 선택 인원',['나','다','가'],[9,3,6],'명',12,3)],
 'S4-A':[pict('범례가 지워진 대출 기록',['가','나'],[12,20],4,'권',hiddenLegend=True)],
 'S4-B':[bar('눈금이 지워진 대여 인원',['월','화'],[6,8],'명',10,2,hiddenTicks=[2])],
 'S5-A':[bar('첫 그래프 · 축0부터',['월','화'],[8,10],'권',12,2),bar('검토할 초안 · 축6부터',['월','화'],[8,10],'권',12,2,minimum=6,intentionalPresentation='nonzero_axis_for_review')],
 'S5-B':[pict('검토할 범례 초안',['오전','오후'],[10,20],5,'권',legendOverride='별 1개 = 5명',intentionalPresentation='wrong_legend_unit_for_review')],
 'S6-A':[pict('모둠별 모은 장바구니',['가','나'],[8,14],2,'개')],
 'S6-B':[bar('대출 권수',['오전','오후'],[12,18],'권',20,2),bar('참여 인원',['오전','오후'],[6,9],'명',10,1)]}

WRITING={
 'S2-A':[('필요한 준비물','다른 물건이나 수로 바꿈','통만 쓰고 수량 없음','빈 통 한 개를 학생 준비물로 명시'),('제공 담당','구슬도 지참하라고 함','현장 제공은 쓰나 재료가 불명확','구슬은 교사가 준다고 구분')],
 'S2-B':[('때와 장소','임의 날짜·시각·곳을 넣음','날짜·때·장소 중 하나 누락','다음 화요일 점심시간 도서실 앞을 보존'),('준비와 표시','책에 직접 이름 쓰기를 요구','책만 준비하고 표시 방법 없음','책 한 권에 작은 이름표를 끼우도록 안내')],
 'S3-A':[('때와 곳','확인한 날짜·시간·장소와 모순','시간 또는 장소 누락','토요일10~12시 작은 강당을 명시'),('신청 범위','관람 모두에게 신청 요구','체험 구분은 있으나 마감 없음','관람은 무신청, 체험은 금요일까지 이름을 적음')],
 'S3-B':[('필요한 행동','없던 절차를 만들거나 반대로 씀','붙이기 또는 완성품 위치 누락','접기·옆면 붙이기·이름 쓰기·창가 상자를 포함'),('기다리는 조건','젖은 동안 이름 쓰도록 함','순서는 맞지만 마른 뒤가 없음','풀이 마른 뒤 이름을 쓰는 조건 보존')],
 'S4-A':[('독자에게 보이는 이름','모르는 별명만 반복','작은 정자만 쓰고 위치 없음','운동장 옆 작은 정자로 위치와 이름을 명료화'),('원래 정보 보존','방과 후를 다른 시각으로 만듦','장소는 고치나 언제인지 없음','원래 방과 후 약속을 유지')],
 'S4-B':[('부족한 수량 보충','다섯 개가 필요하다고 씀','한 개만 쓰고 누구 기준인지 불명확','한 사람 한 개씩 준비하도록 보충'),('수정 이유','원래 날짜가 틀렸다고 함','고쳤다고만 쓰고 독자의 행동 설명 없음','여러 개를 가져오지 않게 준비 수를 알렸다고 설명')],
 'S5-A':[('시각과 장소','네 시 교실을 유지','둘 중 한 항목만 바로잡음','수요일 세 시 도서실로 수정'),('재료 제공 구분','색종이 지참과 연필 현장 제공으로 뒤집음','한 재료의 담당만 밝힘','연필만 지참하고 색종이는 현장 제공')],
 'S5-B':[('확정 정보','모형 수까지 없다고 함','금요일 오후 또는 한 개 누락','금요일 오후와 모형 한 개를 보충'),('미확정 안내','시각과 장소를 지어냄','미정이라고만 하고 어느 정보인지 없음','정확한 시각·장소는 정해진 뒤 안내한다고 구별')],
 'S6-A':[('행사 때와 곳','새 장소나 날짜를 만듦','요일·시간·장소 중 누락','이번 토요일10~11시 강당 안내'),('준비·예외·제공','돈 지참이나 지갑 없는 학생 금지','기본 준비만 쓰고 예외 또는 제공 누락','지갑1개·없으면 대여·돈은 현장을 함께 보존')],
 'S6-B':[('물건 식별','확인한 색·그림과 다름','흰색만 써 구별 특징 부족','파란 뚜껑·나무 그림이 있는 흰 물병으로 소개'),('찾는 행동','장소나 절차를 지어냄','장소만 쓰고 확인 방법 없음','도서실 대출대에서 그림을 먼저 말하도록 안내')]}

def enrich(sets):
 import hashlib,json
 from copy import deepcopy
 for s in sets:
  group=s['id'].removeprefix('PV2-').rsplit('-',2)[0]
  if group not in EXPLANATIONS:continue
  index=(int(s['stage'][1:])-1)*2+(s['variant']=='B')
  q=s['questions'][0];q['explanation']=EXPLANATIONS[group][index];q['options'][q['correctIndex']]['reason']=q['explanation']
  key=s['stage']+'-'+s['variant']
  if s['microSkillId']=='plan-G2-writing-11':
   for q in s['questions']:
    if q['kind']=='writing':
     q['planningPrompt']='읽는 친구가 할 일 / 글에 빠진 말 중 아는 것 / 아직 모르는 것을 먼저 나누어 적으세요.'
     q['rubric']=[dict(criterion=c,levels={'0':bad,'1':partial,'2':full}) for c,bad,partial,full in WRITING[key]]
  if s['microSkillId']=='plan-G4-media-02':
   s['graphs']=deepcopy(GRAPHS[key])
   for i,g in enumerate(s['graphs'],1):
    g['id']=s['id']+'-G'+str(i)
    g['elements']={'legend':'','axis':''}
    for j,(label,value) in enumerate(zip(g['labels'],g['values'])):
     visible=f'{label}: 별 {value//g["symbolValue"]}개' if g['kind']=='pictograph' else f'{label}: {value}{g["unit"]}'
     g['elements']['row-'+str(j)]=visible
    g['elements']['legend']=g.get('legendOverride',f'별 1개 = {"?" if g.get("hiddenLegend") else g.get("symbolValue", "해당 없음")}{g["unit"]}') if g['kind']=='pictograph' else '막대그래프의 축 단위 '+g['unit']
    g['elements']['axis']=('가로축은 항목이며 별 기호 수를 표시' if g['kind']=='pictograph' else f'세로축 단위 {g["unit"]}, 같은 간격의 눈금: '+', '.join('□' if n in g.get('hiddenTicks',[]) else str(n) for n in range(g['axisMin'],g['axisMax']+1,g['axisStep'])))
    g['accessibleDescription']=' / '.join([g['title'],g['elements']['legend'] if g['kind']=='pictograph' else g['elements']['axis']]+[g['elements']['row-'+str(j)] for j in range(len(g['labels']))])
   byid={g['id']:g for g in s['graphs']}
   for q in s['questions']:
    for e in q['evidence']:
     if e.get('evidenceKind')=='graph':e['quote']=byid[e['assetId']]['elements'][e['elementId']]
   s['graphHash']=hashlib.sha256(json.dumps(s['graphs'],ensure_ascii=False,sort_keys=True).encode()).hexdigest()
