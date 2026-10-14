# -*- coding: utf-8 -*-
"""
4단원: 설명문 (unit4_expository) — Batch 2 (5~8차시: V2-1 ~ V2-4 추론적 이해)
기출간 원문 100% 수록 (축약·생략 절대 금지) 및 교사용 정답(.t-ans) 완비
"""

BATCH2 = [
    # =========================================================================
    # 5차시: G6-EXP-V2-1 학술 어휘·형태소 및 다의어 문맥 추론
    # 제재: 〈열병 앓는 도시, ‘도시 열섬 현상’의 원인과 ‘냉섬’의 과학〉 (한국민족문화대백과사전·환경일보)
    # =========================================================================
    {
        "lesson_no": 5,
        "code": "G6-EXP-V2-1",
        "lesson_title": "형태소 분석과 문맥 단서로 학술 어휘·다의어 뜻 추론하기",
        "std_badge": "[6국04-02] · [6국04-03] · CCSS RI.6.4",
        "student_goal": "설명문에 쓰인 낯선 학술 복합어(합성어·파생어)를 어근과 접사로 분해하고 앞뒤 문맥 단서와 결합하여 정확한 뜻을 추론하며, 다의어의 문맥적 의미를 구별할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "파생 접사(불-, 초-, 재-, 폐-, -화, -성)가 붙은 학술 파생어"],
            ["mk-bg", "초록 네모", "비유적 학술 합성어(열섬, 냉섬, 인공열, 바람길)"],
            ["mk-highlight", "형광펜", "다의어(식다, 거두다, 열다)와 앞뒤 문맥 단서"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 〈열병 앓는 도시, ‘도시 열섬 현상’의 원인과 ‘냉섬’의 과학〉</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 한국학중앙연구원 『한국민족문화대백과사전(열섬)』 · 『환경일보』(2026.07.08)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (학술 복합어의 짜임과 다의어의 문맥을 살피며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 어휘 추론 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span> 여름철 한낮에 햇볕을 받아 뜨겁게 달아오른 도심은 밤이 되어도 쉽게 <span class="mk-highlight">식지(㉠)</span> 않는다. 이처럼 인구가 밀집한 도심 지역의 기온이 주변의 농촌이나 교외 지역보다 유독 높게 나타나는 현상을 ‘도시 <span class="mk-bg">열섬(熱島)</span> 현상’이라고 부른다. 기온이 같은 지점을 연결한 지도 위의 등온선을 그려 보면, 도심 지역의 등온선이 폐곡선을 이루며 주변과 구분된다. 즉, 뜨거운 공기가 도심만 둥글게 감싸고 있는 모습이 마치 바다 위에 홀로 떠 있는 ‘열기의 섬’과 같다고 하여 붙여진 이름이다.</p>
                <p><span class="p-num">➋</span> 급격한 <span class="mk-person">도시화(都市化)</span>로 인해 열섬 현상이 심해지는 까닭은 크게 세 가지이다. 첫째, 도심의 지표면 대부분이 <span class="mk-line-blue">빗물이 땅속으로 스며들지 못하는</span> <span class="mk-person">불투수성(不透水性)</span> 아스팔트와 콘크리트로 덮여 있기 때문이다. 흙과 숲, 경작지가 넓은 농촌 지역에서는 땅속 수분이 증발하거나 식물의 증산 작용이 활발하게 일어나면서 주변의 열을 빼앗아 기온을 낮춘다. 반면에 <span class="mk-line-blue">물이 통하지 않는</span> 도심의 포장도로는 열전도율과 열수용력이 커서 낮 동안 태양 복사열을 그대로 흡수하여 저장했다가, 해가 진 뒤에도 밤새도록 열을 방출하며 도시 전체를 거대한 ‘가열판’으로 만든다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 함께 추론하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>➋문단의 ‘불투수성(不透水性)’처럼 처음 보는 어려운 학술 어휘의 뜻은 어떻게 알아낼까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>1단계로 <strong>형태소(어근·접사)</strong>를 쪼개 보면 <code>불-(아니다) + 투수(물이 통과함) + -성(성질)</code>이야! 2단계로 앞뒤 <strong>문맥 단서</strong>를 보니 바로 앞에 ‘빗물이 땅속으로 스며들지 못하는’, 뒤에 ‘물이 통하지 않는’이라는 설명이 있어.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>두 단서를 합치면 ‘물이 스며들거나 통과하지 못하는 성질’이라는 뜻을 사전 없이도 100% 정확히 추론할 수 있구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➌</span> 둘째, 건물의 냉난방 시설에서 뿜어져 나오는 <span class="mk-bg">인공열(人工熱)</span>과 수많은 자동차 엔진에서 버려지는 <span class="mk-person">폐열(廢熱)</span>이 도심의 온도를 끊임없이 높인다. 셋째, 도심에 빽빽하게 들어선 <span class="mk-person">초고층(超高層)</span> 빌딩들이 바람이 드나드는 통로를 가로막아, 도시 안에 갇힌 뜨거운 공기와 대기 오염 물질이 바깥으로 빠져나가지 못하게 만든다.</p>
                <p><span class="p-num">➍</span> 이러한 도시 열섬 현상을 완화하기 위해서는 도심 곳곳에 기온이 낮은 공간, 즉 ‘<span class="mk-bg">냉섬(冷島)</span>’을 만들어야 한다. 먼저 도심 속에 숲과 공원, 하천, 호수를 넓게 조성하면 식물의 증산 작용과 물의 증발을 통해 주변 기온을 낮추는 큰 효과를 <span class="mk-highlight">거둘(㉡)</span> 수 있다. 또한 도로를 포장할 때 빗물이 땅속으로 잘 스며들고 물의 자연스러운 <span class="mk-person">재순환(再循環)</span>을 돕는 <span class="mk-person">투수성(透水性)</span> 블록을 깔거나, 건물 옥상에 식물을 심고 지붕에 햇빛 반사 페인트를 칠하는 것도 효과적이다. 더불어 높은 건물 배치 방향을 조절하여 도심 한가운데로 시원한 <span class="mk-bg">바람길</span>을 <span class="mk-highlight">열어(㉢)</span> 주면, 갇혀 있던 열기가 흩어져 쾌적한 도시 환경을 되찾을 수 있다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 짝·스스로 추론하기</span><span class="role-chip">We·You Do</span></div>
                  <div>1. ➊문단에서 ‘열섬(더울 열+섬 도)’의 조어 원리와 대조 문맥을 활용하면, ➍문단의 <strong>‘냉섬(冷島)’</strong>은 무슨 뜻일까요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">도심 속 숲이나 하천처럼 주변보다 기온이 낮게 나타나는 ‘차가운 섬’ 같은 지역</span></span>
                  <div style="margin-top:3px;">2. 접두사 <code>폐-(버릴 폐)</code>, <code>초-(뛰어넘을 초)</code>, <code>재-(다시 재)</code>의 뜻을 생각할 때 ‘폐열, 초고층, 재순환’의 뜻은?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">버려지는 열 / 보통보다 훨씬 높은 층 / 다시 돌고 듦</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "학술 파생어·합성어의 형태소(어근·접사)를 분해하고 문맥 단서와 연결하기",
            "tag": "Step 1 형태소 분해([6국04-02]) 및 문맥 단서 포착",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">학술 복합어</th>
                  <th style="width:27%;">형태소 분해 (접두사 + 어근 + 접미사)</th>
                  <th style="width:28%;">본문 속 앞뒤 문맥 단서</th>
                  <th style="width:27%;">추론한 문맥적 의미</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">도시화 (➋문단)</td>
                  <td>어근(도시) + 접미사(<span class="blank-slot"><span class="t-ans">-화[化]</span></span>: ~로 됨)</td>
                  <td>인구가 밀집하고 고층 빌딩·포장도로가 늘어남</td>
                  <td>농촌이나 자연 지역이 <span class="blank-slot"><span class="t-ans">도시의 모습으로 변해 가는 현상</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">불투수성 (➋문단)</td>
                  <td>접두사(<span class="blank-slot"><span class="t-ans">불-[不]</span></span>) + 어근(투수) + 접미사(<span class="blank-slot"><span class="t-ans">-성[性]</span></span>)</td>
                  <td>빗물이 땅속으로 스며들지 못하는 / 물이 통하지 않는</td>
                  <td>빗물이나 수분이 땅속으로 <span class="blank-slot"><span class="t-ans">통과하지 못하는 성질</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">초고층 (➌문단)</td>
                  <td>접두사(<span class="blank-slot"><span class="t-ans">초-[超]</span></span>: 뛰어넘다) + 어근(고층)</td>
                  <td>빽빽하게 들어서 바람이 드나드는 통로를 가로막음</td>
                  <td>보통의 높은 건물을 뛰어넘을 만큼 <span class="blank-slot"><span class="t-ans">매우 높은 층</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">재순환 (➍문단)</td>
                  <td>접두사(<span class="blank-slot"><span class="t-ans">재-[再]</span></span>: 다시) + 어근(순환)</td>
                  <td>투수성 블록을 깔아 빗물이 땅속으로 스며들게 함</td>
                  <td>빗물이 버려지지 않고 자연 속에서 <span class="blank-slot"><span class="t-ans">다시 돌고 도는 것</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 형태소 추론에 이어, 일상적인 고유어가 설명문에서 어떤 다의적 의미로 쓰였는지 비교하기",
        "activity_2": {
            "title": "본문 속 다의어(㉠ 식다, ㉡ 거두다, ㉢ 열다)의 문맥적 의미와 다른 쓰임 비교하기",
            "tag": "Step 2 다의어([6국04-03]) 문맥 의미 대조",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:15%;">다의어</th>
                  <th style="width:43%;">사전의 여러 가지 뜻풀이 및 예문</th>
                  <th style="width:42%;">본문 문맥에 맞는 번호 선택 &amp; 새로운 예문 만들기</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉠ 식다<br>(➊문단)</td>
                  <td>① 뜨거운 음식 따위가 찬 기운을 받아 온도가 낮아지다. (국이 식다)<br>② 달아올랐던 대기나 물체의 기온·열기가 낮아지다.<br>③ 열정이나 흥미, 사랑 따위가 줄어들어 시들해지다. (인기가 식다)</td>
                  <td>• 본문 ㉠의 뜻 번호: ( <span class="blank-slot"><span class="t-ans">②</span></span> )번<br>• ③번 뜻으로 짧은 문장 만들기: <span class="pencil-line" style="display:inline-block; width:82%;"><span class="t-ans">아무리 어려워도 과학 탐구를 향한 나의 열정은 식지 않는다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉡ 거두다<br>(➍문단)</td>
                  <td>① 논밭에서 곡식이나 열매를 수확하다. (가을에 벼를 거두다)<br>② 널어 놓은 빨래나 펴 놓은 물건을 걷어 들이다.<br>③ 바라던 좋은 결과나 성과, 효과 따위를 얻다.</td>
                  <td>• 본문 ㉡의 뜻 번호: ( <span class="blank-slot"><span class="t-ans">③</span></span> )번<br>• ①번 뜻으로 짧은 문장 만들기: <span class="pencil-line" style="display:inline-block; width:82%;"><span class="t-ans">농부들이 봄부터 가꾼 사과를 마침내 거두었다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉢ 열다<br>(➍문단)</td>
                  <td>① 닫히거나 잠긴 문, 뚜껑 따위를 젖히다. (창문을 열다)<br>② 막혔던 통로나 길 따위를 트다.<br>③ 모임이나 대회, 전람회 따위를 시작하다. (토론회를 열다)</td>
                  <td>• 본문 ㉢의 뜻 번호: ( <span class="blank-slot"><span class="t-ans">②</span></span> )번<br>• 본문 ㉢과 같은 뜻(②번) 예문: <span class="pencil-line" style="display:inline-block; width:82%;"><span class="t-ans">숲속에 생태 통로를 만들어 야생 동물의 이동 길을 열어 주었다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 1~2]에서 추론한 학술 개념어와 다의어를 활용하여 ‘도시 열섬과 냉섬’ 개념 사전 및 설명 예문 작성하기",
        "activity_3": {
            "title": "학술 개념어(‘불투수성/투수성’, ‘열섬/냉섬’) 사전 정의문과 설명 문장 산출하기",
            "tag": "Step 3 학술 어휘 정의 및 문장 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>[나만의 과학 개념 사전]</strong> 오늘 배운 형태소 결합 원리와 반의(대조) 문맥을 활용하여 두 짝꿍 학술어를 묶어 설명하는 글을 써 보세요.</div>
              <span class="pencil-line">✏️ <strong>‘불투수성’과 ‘투수성’ 비교 설명</strong>: <span class="t-ans">‘불투수성’은 아스팔트처럼 빗물이 땅속으로 통과하지 못하는 성질이고, 반대로 ‘투수성’은 빗물이 땅속으로 잘 스며들게 하는 성질이다.</span></span>
              <span class="pencil-line">✏️ <strong>‘열섬’과 ‘냉섬’을 모두 넣어 해결책 문장 쓰기</strong>: <span class="t-ans">도심의 기온이 섬처럼 높아지는 ‘열섬’ 현상을 줄이려면, 도심 속에 숲과 하천 같은 ‘냉섬’을 조성하고 바람길을 열어 주어야 한다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 어휘 생성)·15차시(W4 학술 어휘 뜻풀이 집필) 직결",
            "prompt": "내가 쓸 설명문에 꼭 넣고 싶은 ‘전문 학술 어휘(합성어·파생어)’ 2개와, 독자가 쉽게 이해할 수 있도록 덧붙일 ‘문맥 뜻풀이 표현’을 메모해 보세요.",
            "placeholder": "(예: 생분해성[생물+분해+-성] ➔ 땅속 미생물에 의해 자연스럽게 썩어 분해되는 성질)",
            "example_answer": "생분해성(生分解性: 미생물이 자연에서 스스로 분해할 수 있는 성질), 재활용(再活用: 버려지는 자원을 다시 쓸모 있게 활용하는 것)",
        },
        "self_check": [
            "낯선 학술 어휘를 어근과 접사(`불-, 초-, 재-, -화, -성`)로 쪼개어 뜻의 가설을 세웠나요?",
            "앞뒤 문장의 정의·대조 문맥 단서를 결합하여 학술 어휘의 정확한 의미를 추론했나요?",
            "다의어(`식다, 거두다, 열다`)가 일상 대화에서 쓰일 때와 학술 설명문에서 쓰일 때의 의미를 구별했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 학술 어휘 2단계 추론 공식([6국04-02]): 1단계 형태소 분해(접두사 `불-[아니다], 초-[뛰어넘다], 재-[다시], 폐-[버리다]` + 한자 어근 + 접미사 `-화[되다], -성[성질]`) ➔ 2단계 앞뒤 문맥 단서(관형절 정의·반의 대조) 결합 / [우측 판서] 다의어([6국04-03]) 중심의미(구체적 동작: 국이 식다/벼를 거두다/문을 열다) ➔ 주변의미 확장(추상적·학술적 현상: 도심 열기가 식다/효과를 거두다/바람길을 열다).",
            "intro_5min": "여름날 운동장 흙바닥과 도로 위 아스팔트 바닥 중 어디가 더 뜨거울까요? 설명문을 읽다 보면 ‘불투수성, 초고층, 재순환’처럼 한자로 된 어려운 학술 어휘를 자주 만납니다. 사전이 없을 때 단어의 블록(형태소)을 쪼개고 앞뒤 문맥을 단서로 뜻을 추론하는 5차시 목표를 제시한다.",
            "ido_think_aloud_script": "“선생님이 ➋문단을 읽다가 ‘불투수성(不透水性)’이라는 어려운 말을 만났어요. 포기하지 않고 두 단계 추론 열쇠를 써 볼게요! 첫째, 단어의 블록(형태소)을 쪼개 봅니다. 맨 앞의 ‘불(不)’은 ‘불가능, 불규칙’처럼 ‘아니다’라는 뜻의 접두사이고, 맨 뒤의 ‘성(性)’은 ‘성질’이라는 뜻의 접미사예요. 가운데 ‘투수(透水)’의 ‘수’는 물이겠네요! 둘째, 앞뒤 문맥 단서를 찾아봅니다. 바로 앞에 ‘빗물이 땅속으로 스며들지 못하는’이라는 꾸며 주는 말이 있고, 다음 문장에는 농촌의 흙과 대조하며 ‘물이 통하지 않는 도심의 포장도로’라고 다시 설명해 주었네요! 아하, ‘불투수성’은 ‘물이 스며들거나 통과하지 못하는 성질’이라는 뜻이구나! 그럼 ➍문단에 나오는 ‘투수성 블록’은 반대로 ‘불(不)’이 빠졌으니 ‘물이 잘 통과하는 성질의 블록’이겠네요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "➊문단에서는 왜 도심의 기온이 높은 현상을 ‘열섬(熱島)’이라고 불렀나요? 그리고 이를 단서로 ➍문단의 ‘냉섬(冷島)’의 뜻을 어떻게 추론할 수 있나요?",
                    "expected_ans": "도심의 등온선이 닫힌 곡선을 이루어 뜨거운 공기가 도심을 감싼 모습이 마치 바다 위의 ‘열기의 섬’ 같아서 ‘열섬’이라 불렀습니다. 이를 반대로 적용하면 ‘냉섬’은 도심 속 숲이나 하천처럼 주변보다 기온이 낮게 나타나는 ‘차가운 섬’ 같은 공간을 뜻합니다.",
                    "reprompt": "➊문단 마지막 문장의 ‘마치 바다 위에 홀로 떠 있는 ~’ 비유를 확인하고, ➍문단 첫 문장의 ‘기온이 낮은 공간, 즉 냉섬’ 부분을 연결해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "➍문단의 ‘효과를 거둘(㉡) 수 있다’와 ‘바람길을 열어(㉢) 주면’에서 ‘거두다’와 ‘열다’는 원래 어떤 뜻에서 확장된 다의어인가요?",
                    "expected_ans": "‘거두다’는 원래 농작물을 수확한다는 구체적 뜻에서 ‘좋은 성과나 효과를 얻다’라는 추상적 뜻으로 확장되었고, ‘열다’는 닫힌 문을 젖힌다는 뜻에서 ‘막힌 통로나 바람길을 트다’라는 뜻으로 확장되었습니다.",
                    "reprompt": "가을에 논에서 벼를 ‘거두는’ 모습과 숲을 만들어 온도 낮추기 효과를 ‘거두는’ 모습을 비교해 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 파생어 4종의 접사와 어근을 분해하고 문맥 단서를 찾아 뜻을 완성한 뒤, [활동 2]에서 다의어 3종의 사전적 번호 매칭과 새 예문 짓기를 수행하도록 지도한다. [활동 3]과 씨앗 보관함을 통해 내가 쓸 설명문에서 어려운 학술어를 쓸 때 어떻게 앞뒤 문맥으로 친절한 뜻풀이 단서를 넣어 줄지(15차시 W4 역전이) 연결하며 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 날개 [We·You Do]</strong>: 1. <strong>도심 속 공원·하천처럼 주변보다 기온이 낮게 나타나는 ‘차가운 섬’ 같은 지역</strong> / 2. 폐열: <strong>버려지는 열</strong>, 초고층: <strong>보통보다 훨씬 높은 층</strong>, 재순환: <strong>다시 돌고 듦</strong><br>
              <strong>2. [활동 1] 형태소 분해 및 문맥 추론</strong>: 도시화: <strong>-화[化]</strong>, <strong>도시의 모습으로 변해 가는 현상</strong> / 불투수성: <strong>불-[不]</strong>, <strong>-성[性]</strong>, <strong>통과하지 못하는 성질</strong> / 초고층: <strong>초-[超]</strong>, <strong>매우 높은 층</strong> / 재순환: <strong>재-[再]</strong>, <strong>다시 돌고 도는 것</strong><br>
              <strong>3. [활동 2] 다의어 문맥 대조</strong>: ㉠ 식다: <strong>②번</strong> / ㉡ 거두다: <strong>③번</strong> / ㉢ 열다: <strong>②번</strong> (각 지정 번호의 의미에 부합하는 예문이면 모두 정답 인정)<br>
              <strong>4. [활동 3] 개념 사전 및 문장 산출</strong>: 형태소 의미(통과 여부, 열기/냉기 섬)와 대조 관계가 명확히 드러나게 서술하면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "형태소만 기계적으로 쪼개고(예: ‘열섬 = 뜨거운 섬’) 본문 문맥을 확인하지 않아 ‘남해에 있는 진짜 화산섬’으로 오해하는 오류",
                    "diagnosis": "형태소 분석(1차 가설) 결과를 텍스트의 앞뒤 문맥 단서(2차 검증)와 결합하지 않고 글자 그대로만 해석함.",
                    "prescription": "‘형태소 가설 + 문맥 검증 2단계 법칙’ 강조: 어근·접사로 세운 뜻 가설이 본문 주제(도심의 기온 분포와 등온선)와 맞는지 반드시 앞뒤 문장으로 확인하게 한다.",
                },
                {
                    "error_case": "다의어 ‘식다(① 음식이 식다 vs ② 대기 기온이 식다)’를 구분할 때 둘 다 ‘온도가 낮아진다’는 공통점만 보고 ①번을 고르는 오류",
                    "diagnosis": "서술어가 결합하는 주어(선택 제약: ‘국/밥’ 같은 음식물 vs ‘도심/땅/공기’ 같은 자연·기상 현상)의 차이를 살피지 못함.",
                    "prescription": "밑줄 친 다의어 앞의 주어(‘뜨겁게 달아오른 도심은’, ‘큰 효과를’, ‘시원한 바람길을’)에 동그라미를 치고, 사전 뜻풀이의 짝꿍 주어·목적어와 일치하는 번호를 고르게 지도한다.",
                },
            ],
            "scaffolding_down": "한자 파생 접사가 생소한 학습자에게는 친숙한 일상 단어 짝꿍 카드(`불가능/불친절 ➔ 불-`, `초능력/초고속 ➔ 초-`, `재발견/재사용 ➔ 재-`, `과학화/정보화 ➔ -화`, `신축성/안전성 ➔ -성`)를 먼저 제시하여 접사의 뜻을 귀납적으로 발견하게 한다.",
            "scaffolding_up": "심화 학습자에게는 접두사 `비-(非)`, `범-(汎)`, 접미사 `-적(的)`이 결합된 6학년 사회·과학 학술어(예: ‘비대칭적, 범지구적, 생물다양성’)를 제시하고 형태소 분해 및 설명 예문을 만들어 보게 한다.",
            "rubric": {
                "high": "학술 복합어의 어근·접사를 정확히 분해하고 앞뒤 정의·대조 문맥 단서와 결합하여 뜻을 완벽히 추론하며, 다의어의 문맥적 의미를 변별해 정확한 새 예문을 산출함.",
                "mid": "학술 복합어의 대략적인 뜻과 다의어 번호는 찾으나, 형태소(접두사·접미사) 분해 근거 설명이나 새 예문 구성이 다소 단순함.",
                "low": "낯선 한자 학술어가 나오면 앞뒤 문맥 단서를 찾지 못하고 추측에 의존하며, 다의어의 문맥적 의미 구별에 어려움을 겪음.",
            },
        },
    },

    # =========================================================================
    # 6차시: G6-EXP-V2-2 생략된 상황·인과·숨은 전제·거시지시어 추론
    # 제재: 〈전 세계 산호초 84%가 하얗게 변한 ‘백화 현상’과 바다의 위기〉 (해양수산부·뉴스트리)
    # =========================================================================
    {
        "lesson_no": 6,
        "code": "G6-EXP-V2-2",
        "lesson_title": "거시 지시어가 압축한 내용과 생략된 인과 고리 추론하기",
        "std_badge": "[6국02-02] · CCSS RI.6.1, RI.6.3 · Kintsch 상황모형",
        "student_goal": "문단과 문단을 잇는 거시 지시어(‘이러한 공생 관계는, 이 현상이 지속되면’)가 가리키는 앞 문단 내용을 역추적하고, 글에 생략된 과학적 인과 고리를 추론할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "문단 간 응집성을 높이는 거시 지시어(이러한 ~, 이 ~, 그 때문에)"],
            ["mk-line-blue", "파란 밑줄", "지시어가 가리키는 앞 문장의 핵심 선행 내용"],
            ["mk-highlight", "형광펜", "생략된 인과 고리를 추론하기 위한 본문 속 과학 단서"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 〈전 세계 산호초 84%가 하얗게 변한 ‘백화 현상’과 바다의 위기〉</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 해양수산부 공식 자료 · 『뉴스트리』(2025.04.24, 미국 산호초감시기구 CRW 보고서 인용)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (거시 지시어가 가리키는 내용과 숨은 인과 고리를 찾으며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 인과 추론 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span> 열대 바다의 얕은 물속을 수놓는 울긋불긋한 산호초는 사실 식물이나 광물이 아니라 ‘산호충’이라는 작은 동물들이 모여 만든 <span class="mk-highlight">하얀 석회질 집(골격)</span>이다. <span class="mk-line-blue">산호의 몸속 조직에는 광합성을 하여 산호가 살아가는 데 필요한 에너지의 최대 90퍼센트를 공급해 주는 ‘황록공생조류(공생 미세조류)’가 함께 살아간다.</span> <span class="mk-highlight">이 미세조류는 산호에게 영양분을 줄 뿐만 아니라 산호초가 보라색, 노란색, 초록색 등 다채롭고 고운 빛깔을 띠게 해 준다.</span> <span class="mk-line-blue">대신 산호는 미세조류에게 천적을 피할 수 있는 안전한 보금자리와 광합성에 필요한 이산화 탄소를 제공한다.</span></p>
                <p><span class="p-num">➋</span> 그러나 최근 지구 온난화로 바닷물의 온도가 급격히 오르면서 <span class="mk-person">이러한 공생 관계는(㉠)</span> 심각한 위기를 맞고 있다. 해수 온도가 평소보다 1~2도만 높아진 상태가 이어져도, 산호 몸속의 황록공생조류는 스트레스를 받아 독성 산소를 내뿜거나 산호 밖으로 빠져나가 버린다. <span class="mk-line-blue">그 결과 산호는 고운 빛깔을 잃고 투명해진 조직 아래로 하얀 석회질 골격만 드러나게 되는데,</span> <span class="mk-person">이 현상을(㉡)</span> ‘산호초 백화(白化) 현상’이라고 부른다. 미국 산호초감시기구(CRW)의 2025년 발표에 따르면, 지난 2023년 1월 이후 최소 82개국 근해에서 백화가 진행되어 전 세계 산호초의 무려 84퍼센트에서 백화 현상이 관측되었다. <span class="mk-person">이 현상이 지속되면(㉢)</span> 산호는 질병에 취약해져 결국 집단으로 폐사하게 된다. <strong style="color:#B03A2E; font-family:var(--font-sans); font-size:7.6pt;">[🔎 추론 지점 ①: 왜 미세조류가 빠져나간 것만으로 산호가 하얗게 변하고 결국 죽게 될까?]</strong></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 함께 추론하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>➋문단 첫머리의 <strong>‘이러한 공생 관계(㉠)’</strong>는 무엇을 가리키며, 왜 조류가 떠나면 산호가 죽을까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>‘이러한 ~’은 앞 문단(➊문단) 전체를 압축하는 <strong>거시 지시어</strong>야! 또한 ➋문단에는 ‘조류가 떠나면 산호가 죽는다’고만 되어 있지만, ➊문단 형광펜 단서에 ‘조류가 에너지의 90%와 색깔을 준다’고 나와 있어.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>두 단서를 잇는 <strong>생략된 인과 고리</strong>는 ‘조류가 떠나면서 산호가 색소를 잃고, 에너지의 90%를 공급받지 못해 심각한 영양실조에 걸리기 때문’이구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➌</span> <span class="mk-line-blue">산호초는 지구 전체 바다 면적의 1퍼센트도 되지 않지만, 전체 해양 생물 종의 약 25퍼센트가 알을 낳고 먹이를 구하며 숨어 사는 ‘바다의 열대우림’이자 ‘바다의 집’이다.</span> 따라서 <span class="mk-person">이런 산호가(㉣)</span> 대규모로 폐사하면 해양 생태계는 물론 인류의 ‘식량 안보’에도 치명적인 타격을 입힌다. <strong style="color:#B03A2E; font-family:var(--font-sans); font-size:7.6pt;">[🔎 추론 지점 ②: 바닷속 산호가 죽는 일이 왜 육지에 사는 인류의 식량 안보까지 위협할까?]</strong></p>
                <p><span class="p-num">➍</span> 또한 <span class="mk-line-blue">산호초 군락은 얕은 바닷가에서 거센 파도와 태풍 해일의 에너지를 최대 90퍼센트까지 꺾어 주는 천연 방파제 역할도 겸하고 있다.</span> <span class="mk-person">그 때문에(㉤)</span> 백화 현상으로 산호초 군락이 죽어 석회질 뼈대가 부서져 내린 일부 열대 섬 지역에서는 해안가의 땅이 파도에 깎여 나가는 해안 침식이 훨씬 빨라지고 있다. 바다의 경비병이자 생명의 요람인 산호초가 보내는 하얀 경고장을 인류가 결코 가볍게 여겨서는 안 되는 까닭이 바로 여기에 있다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 짝·스스로 추론하기</span><span class="role-chip">We·You Do</span></div>
                  <div>1. ➌문단의 <strong>‘이런 산호(㉣)’</strong>와 ➍문단의 <strong>‘그 때문에(㉤)’</strong>가 각각 압축하고 있는 앞 문장의 내용은 무엇인가요?</div>
                  <span class="pencil-line">✏️ ㉣: <span class="t-ans">해양 생물 종의 25%가 알을 낳고 숨어 사는 서식처 역할을 하는 산호</span></span>
                  <span class="pencil-line">✏️ ㉤: <span class="t-ans">산호초가 거센 파도의 에너지를 최대 90%까지 꺾어 주는 천연 방파제 역할을 하기 때문에</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "문단과 문단을 촘촘하게 묶어 주는 ‘거시 지시어(㉠~㉤)’의 압축 내용 역추적하기",
            "tag": "Step 1 거시 지시어(Macro-anaphora) 선행 명제 복원",
            "body_html": """
            <div style="font-size:7.3pt; margin-bottom:3px; color:#2C3E50;">※ 학술 설명문에서는 앞 문단 전체의 설명을 <strong>‘이러한 관계는, 이 현상이, 그 때문에’</strong>와 같은 추상 지시어구로 압축하여 다음 문단의 원인으로 연결합니다.</div>
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">본문 속 거시 지시어</th>
                  <th style="width:16%;">추적 방향</th>
                  <th style="width:62%;">압축되어 있는 앞 문단·앞 문장의 구체적 내용 (완결된 명제로 복원)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉠ 이러한 공생 관계는<br>(➋문단 첫 문장)</td>
                  <td>➊문단 전체 역추적</td>
                  <td>황록공생조류는 광합성으로 산호에게 <span class="blank-slot"><span class="t-ans">에너지의 최대 90%와 고운 색깔</span></span>을 주고, 산호는 미세조류에게 <span class="blank-slot"><span class="t-ans">안전한 보금자리와 이산화 탄소</span></span>를 제공하는 상호 도움 관계</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉡ 이 현상을 / ㉢ 이 현상이<br>(➋문단 중간·끝)</td>
                  <td>➋문단 앞 문장 역추적</td>
                  <td>수온 상승으로 공생 미세조류가 빠져나가 산호의 <span class="blank-slot"><span class="t-ans">하얀 석회질 골격만 드러나는(백화)</span></span> 현상</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">㉣ 이런 산호가 (➌문단)<br>㉤ 그 때문에 (➍문단)</td>
                  <td>➌·➍문단 첫 문장 역추적</td>
                  <td>• ㉣: 전체 해양 생물 종의 약 <span class="blank-slot"><span class="t-ans">25퍼센트</span></span>에게 서식처(‘바다의 집’)가 되어 주는 산호<br>• ㉤: 산호초가 해안가에서 거센 파도를 막아 주는 <span class="blank-slot"><span class="t-ans">천연 방파제 역할</span></span>을 겸하고 있기 때문에</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 복원한 문단 간 연결 고리에 과학적 배경지식을 더해 글에 생략된 ‘중간 인과 고리’ 추론하기",
        "activity_2": {
            "title": "본문 단서와 배경지식을 결합하여 [추론 지점 ①·②]의 ‘생략된 인과 고리’ 사슬 완성하기",
            "tag": "Step 2 생략된 매개 원리(Bridging Inference) 도해",
            "body_html": """
            <!-- 추론 사슬 1 -->
            <div style="font-size:7.2pt; font-weight:800; color:#1A5276; margin-bottom:2px;">🔎 [추론 지점 ①] 수온 상승과 산호 집단 폐사 사이의 생략된 인과 고리 (➊문단 + ➋문단 결합)</div>
            <div class="inference-row" style="margin-bottom:5px;">
              <div class="inf-card c1">
                <strong>[명시된 원인 (➋문단)]</strong><br>해수 온도가 1~2℃ 상승하여 산호 몸속의 <strong>황록공생조류가 밖으로 이탈</strong>함
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#B03A2E;">[생략된 중간 인과 고리 추론]</strong><br>조류가 사라지자 색소를 잃어 하얀 골격이 드러나고, 산호 에너지의 <span class="blank-slot"><span class="t-ans">90%를 주던 광합성 영양분 공급이 끊겨 굶주림(영양실조)</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong>[명시된 결과 (➋문단)]</strong><br>산호가 하얗게 변하는 <strong>백화 현상</strong>이 나타나고 질병에 약해져 <strong>집단 폐사</strong>함
              </div>
            </div>

            <!-- 추론 사슬 2 -->
            <div style="font-size:7.2pt; font-weight:800; color:#196F3D; margin-bottom:2px;">🔎 [추론 지점 ②] 산호초 대규모 폐사와 인류 식량 안보·해안 침식 사이의 생략된 인과 고리 (➌·➍문단)</div>
            <div class="inference-row" style="margin-bottom:0;">
              <div class="inf-card c1">
                <strong>[명시된 원인 (➌·➍문단)]</strong><br>전 세계 산호초의 84% 백화 진행 및 산호초 군락의 <strong>대규모 폐사·붕괴</strong>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#B03A2E;">[생략된 중간 인과 고리 추론]</strong><br>① 해양 생물 25%가 <span class="blank-slot"><span class="t-ans">산란장·서식처를 잃어 물고기 개체 수와 어획량이 급감</span></span>함<br>② 파도 힘을 90% 꺾던 <span class="blank-slot"><span class="t-ans">천연 방파제가 사라져 거센 파도가 해안을 직접 강타</span></span>함
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong>[명시된 결과 (➌·➍문단)]</strong><br>인류의 <strong>식량 안보 위협</strong> 및 열대 섬 지역의 <strong>해안 침식 가속화</strong>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 구축한 인과 사슬을 바탕으로 조건이 변화했을 때 일어날 결과를 예측하여 완결된 글로 서술하기",
        "activity_3": {
            "title": "생략된 인과 고리를 복원하여 설명을 보충하고, 새로운 조건 변화에 따른 결과 추론하기",
            "tag": "Step 3 인과 복원 서술 및 상황 모형 예측 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>과제</strong>: 과학자들이 고온에 강한 ‘슈퍼 산호’를 심어 산호초 군락을 복원한다면 해양 생태계와 섬 해안가에 어떤 연쇄적인 변화가 일어날지, 오늘 배운 <strong>거시 지시어(`이러한 복원이 이루어지면, 그 결과`)</strong>와 <strong>인과 사슬</strong>을 활용해 2~3문장으로 추론해 써 보세요.</div>
              <span class="pencil-line">✏️ <span class="t-ans">고온에 강한 산호초 군락이 복원되면 황록공생조류와의 공생 관계가 회복되어 산호가 다시 건강하게 자라난다. 이러한 복원이 이루어지면 해양 생물 종의 25%가 살아갈 서식처가 되살아나 어류 자원이 풍부해지고 인류의 식량 안보도 안정된다. 그 결과 산호초가 다시 튼튼한 천연 방파제 역할을 수행하여 섬 지역의 해안 침식도 크게 줄어들 것이다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 문단 간 지시어 배치)·16차시(W5 논리적 비약 퇴고) 직결",
            "prompt": "내가 쓸 설명문에서 앞 문단과 뒷 문단을 매끄럽게 이어 줄 ‘거시 지시어구(`이러한 원리는, 이 문제를 해결하려면`)’를 넣어 문단 연결 씨앗을 써 보세요.",
            "placeholder": "(예: [앞 문단: 미세먼지 발생 원인] ➔ 이러한 미세먼지 발생 원인을 줄이기 위해서는...)",
            "example_answer": "[앞 문단: 스마트폰 과몰입이 수면 부족을 부르는 원리] ➔ 이러한 수면 방해 현상이 지속되면 성장기 청소년의 집중력과 면역력까지 떨어지게 된다.",
        },
        "self_check": [
            "‘이러한 공생 관계는, 이 현상이, 그 때문에’ 같은 거시 지시어가 압축한 앞 문단 내용을 정확히 찾았나요?",
            "본문에 드러난 단서(➊문단)와 배경지식을 결합해 생략된 중간 인과 고리를 논리적으로 추론했나요?",
            "인과 사슬을 바탕으로 조건이 바뀌었을 때 일어날 연쇄적 결과를 타당하게 예측하여 서술했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 거시 지시어 역추적 화살표(A4 응집성): `이러한 공생 관계는(➋)` ⬅ ➊문단 전체(조류: 에너지 90%·색소 제공 ↔ 산호: 보금자리·CO₂ 제공) / [우측 판서] Kintsch 교량 추론(Bridging Inference) 공식: `[명시된 원인: 조류 이탈]` + `[➊문단 단서: 조류=에너지 90% 공급원]` ➔ **`[생략된 인과 고리: 광합성 영양분 공급 중단으로 영양실조 발생]`** ➔ `[명시된 결과: 산호 집단 폐사]`.",
            "intro_5min": "바닷속 알록달록한 산호초가 유령처럼 새하얗게 변해 죽어 가는 사진을 본 적이 있나요? 전 세계 산호초의 84%가 겪고 있는 ‘백화 현상’ 글을 읽으며, 필자가 글의 경제성을 위해 생략해 둔 ‘숨은 과학적 인과 고리’와 ‘문단 간 지시어’를 탐정처럼 추척하는 6차시 목표를 제시한다.",
            "ido_think_aloud_script": "“선생님이 ➊문단과 ➋문단을 연결하며 읽는 시범을 보여 줄게요. ➋문단 첫 문장에 ‘그러나 최근 지구 온난화로 바닷물의 온도가 급격히 오르면서 이러한 공생 관계는 심각한 위기를 맞고 있다.’라고 했어요. 여기서 ‘이러한 공생 관계’라는 세 단어는 ➊문단 전체를 통째로 보자기에 싸서 가져온 ‘거시 지시어’예요! 무엇을 싸 왔는지 풀어 볼까요? 산호는 조류에게 집과 이산화 탄소를 주고, 조류는 광합성으로 산호 에너지의 90%와 고운 색깔을 준다는 내용이에요. 그런데 ➋문단 끝을 보니 ‘조류가 빠져나가면 산호가 하얗게 변하고 결국 죽는다’고만 되어 있어요. 왜 작은 조류가 나갔다고 산호가 죽을까요? 필자가 직접 안 써 놓았지만 ➊문단 단서를 가져와 다리를 놓아 보면(교량 추론), ‘에너지의 90%를 만들어 주던 조류가 사라졌으니 산호가 밥을 굶는 영양실조에 걸려 죽는구나!’라고 생략된 인과 고리를 완벽히 찾아낼 수 있습니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "➌문단에서 바닷속 산호초가 폐사하는 일이 왜 육지에 사는 인류의 ‘식량 안보’에까지 큰 타격을 입힌다고 했을까요? 생략된 중간 과정을 추론해 볼까요?",
                    "expected_ans": "산호초는 전체 해양 생물 종의 25%가 알을 낳고 자라는 서식처입니다. 따라서 산호초가 죽으면 어린 물고기들이 살 곳을 잃어 물고기 수가 급격히 줄어들고, 결국 사람들이 잡아먹을 수산물이 부족해져 식량 안보가 위협받게 됩니다.",
                    "reprompt": "➌문단 첫 문장에서 산호초가 해양 생물 종의 몇 퍼센트에게 어떤 역할을 해 준다고 했는지 단서를 찾아 먹이 사슬로 연결해 보세요.",
                },
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "➍문단의 ‘그 때문에(㉤)’는 앞 문장의 어떤 내용을 가리키며, 산호초가 부서지면 왜 섬 지역의 해안 침식이 빨라지나요?",
                    "expected_ans": "‘그 때문에’는 산호초 군락이 얕은 바닷가에서 거센 파도의 에너지를 최대 90%까지 꺾어 주는 천연 방파제 역할을 한다는 내용을 가리킵니다. 산호초가 죽어 부서지면 파도를 막아 줄 방파제가 사라져 거센 파도가 해안가 땅을 직접 깎아 내기 때문입니다.",
                    "reprompt": "➍문단 첫 문장의 ‘천연 방파제 역할’에 밑줄을 긋고, 방파제가 무너졌을 때 바닷가 마을에 파도가 어떻게 들이닥칠지 상상해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 거시 지시어 5개의 선행 명제를 복원하고, [활동 2]에서 추론 지점 ①·②의 생략된 중간 인과 고리 상자를 완성한 뒤, [활동 3]에서 ‘슈퍼 산호 복원 시 일어날 연쇄 결과’를 거시 지시어를 사용해 서술하도록 지도한다. 글쓰기 퇴고(16차시 W5)에서 내 글에 논리적 빈틈(비약)이 없는지 점검하는 원리와 직결됨을 안내하며 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 날개 [We·You Do]</strong>: ㉣: <strong>전체 해양 생물 종의 약 25%가 알을 낳고 숨어 사는 서식처 역할을 하는 산호</strong> / ㉤: <strong>산호초 군락이 얕은 바닷가에서 거센 파도의 에너지를 최대 90%까지 꺾어 주는 천연 방파제 역할을 하기 때문에</strong><br>
              <strong>2. [활동 1] 거시 지시어 복원</strong>: ㉠ <strong>에너지의 최대 90%와 고운 색깔</strong>, <strong>안전한 보금자리와 이산화 탄소</strong> / ㉡·㉢ <strong>하얀 석회질 골격만 드러나는(백화)</strong> / ㉣ <strong>25퍼센트</strong> / ㉤ <strong>천연 방파제 역할</strong><br>
              <strong>3. [활동 2] 생략된 인과 고리 추론</strong>: [추론 ①] <strong>90%를 주던 광합성 영양분 공급이 끊겨 굶주림(영양실조)</strong> / [추론 ②] ① <strong>산란장·서식처를 잃어 물고기 개체 수와 어획량이 급감</strong>, ② <strong>천연 방파제가 사라져 거센 파도가 해안을 직접 강타</strong><br>
              <strong>4. [활동 3] 조건 변화 추론 서술 (인정 답안 기준)</strong>: 거시 지시어(‘이러한 ~, 그 결과’)를 1개 이상 사용하고, `[공생 회복 ➔ 해양 생물 25% 서식처 회복·수산 자원 증가 ➔ 천연 방파제 기능 회복·해안 침식 감소]`의 인과 사슬이 논리적으로 서술되면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "거시 지시어 ‘이러한 공생 관계(㉠)’가 가리키는 내용을 찾을 때 바로 앞 단어 하나만 찾아 쓰는 오류",
                    "diagnosis": "단어 하나를 대신하는 대명사와 달리, ‘이러한 + 추상명사구’는 앞 문단 전체의 복합 명제를 압축한다는 텍스트 응집성 원리를 이해하지 못함.",
                    "prescription": "‘공생(함께 삶)’은 혼자 할 수 없으므로 “누가 누구에게 무엇을 주고받는지” 양방향 화살표(`산호 ⇄ 황록공생조류`)가 모두 들어가야 완전한 정답이 됨을 지도한다.",
                },
                {
                    "error_case": "생략된 인과 고리를 추론할 때 본문 단서(에너지 90% 공급, 해양 생물 25% 서식처)와 무관한 상상을 쓰는 오류",
                    "diagnosis": "문학 작품의 자유로운 상상과 설명문의 ‘텍스트 단서 기반 논리적 교량 추론’을 구분하지 못함.",
                    "prescription": "설명문의 추론은 반드시 `[앞 문장에 숨어 있는 과학 사실 단서] + [뒤 문장의 결과]`를 빈틈없이 이어 주는 징검다리여야 함을 강조하고 ➊·➌문단의 숫자 단서(90%, 25%)를 반드시 포함하게 한다.",
                },
            ],
            "scaffolding_down": "생략된 인과 고리 찾기를 어려워하는 학습자에게는 ➊문단의 ‘에너지 90% 공급’에 ①번, ➋문단의 ‘미세조류 이탈’에 ②번, ‘집단 폐사’에 ③번 번호를 매기게 한 뒤, “①번을 해 주던 친구가 ②번처럼 떠나면 왜 ③번처럼 죽을까요?”라고 징검다리 질문을 던진다.",
            "scaffolding_up": "심화 학습자에게는 3차시에서 배운 ‘북극 빙하 감소로 인한 해수 온도 상승’과 본문의 ‘산호초 백화 현상’을 연결하여, 극지방의 변화가 열대 바다 생태계에 미치는 지구적 연쇄 인과도를 그려 보게 한다.",
            "rubric": {
                "high": "문단 간 거시 지시어가 압축한 선행 명제를 정확히 복원하고, 본문 단서와 과학적 배경지식을 결합해 생략된 중간 인과 고리와 조건 변화 결과를 완벽한 인과 사슬 문장으로 서술함.",
                "mid": "거시 지시어가 가리키는 대상과 생략된 인과 고리의 핵심 의미는 파악했으나, 완결된 문장으로 복원·서술할 때 일부 수치나 매개 단서를 누락함.",
                "low": "거시 지시어의 지시 범위를 좁게 파악하며, 명시되지 않은 중간 인과 원리를 본문 단서와 연결하여 추론하는 데 어려움이 있음.",
            },
        },
    },

    # =========================================================================
    # 7차시: G6-EXP-V2-3 텍스트와 시각 매체 자료 간 통합 추론
    # 제재: 〈여름철 필수품 휴대용 선풍기, 리튬 이온 배터리 ‘열폭주’ 원리와 안전 수칙〉
    #       (한국소비자원·소방청·행정안전부 원문 + 원인별 화재 통계표 & 온도 급상승 변곡점 그래프)
    # =========================================================================
    {
        "lesson_no": 7,
        "code": "G6-EXP-V2-3",
        "lesson_title": "본문 원리와 시각 자료(통계·그래프)를 결합하여 통합 추론하기",
        "std_badge": "[6국02-03] · [6국05-01] · CCSS RI.6.7",
        "student_goal": "설명문 본문의 과학적 원리와 복합 시각 자료(화재 원인 통계표·온도 변화 그래프)를 교차 연결하여, 표면 수치 너머의 심층 경향성과 작동 원리를 통합 추론할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "배터리 핵심 구조(양극, 음극, 분리막, 보호 회로)"],
            ["mk-line-red", "빨간 밑줄", "열폭주(Thermal Runaway)가 일어나는 과학적 메커니즘"],
            ["mk-highlight", "형광펜", "시각 자료(표·그래프)의 수치 변곡점과 연결되는 본문 단서"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 〈여름철 필수품 휴대용 선풍기, 리튬 이온 배터리 ‘열폭주’ 원리와 안전 수칙〉</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 한국소비자원 · 소방청 · 행정안전부 『어린이 안전넷』</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (과학 원리와 아래 시각 자료의 수치를 교차 연결하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 텍스트-표 통합 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span> 무더운 여름철이 되면 학생들이 등하굣길에 들고 다니는 휴대용 선풍기나 스마트폰 보조 배터리 사용이 크게 늘어난다. 이 기기들 속에는 작고 가벼우면서도 많은 전기를 저장할 수 있는 ‘리튬 이온 배터리’가 들어 있다. 리튬 이온 배터리는 <span class="mk-person">양극(+)</span>과 <span class="mk-person">음극(-)</span> 사이를 리튬 이온이 오가며 충전과 방전을 반복한다. 이때 배터리 내부에서 양극과 음극이 서로 직접 맞닿아 합선(단락)되지 않도록, 미세한 구멍이 뚫린 얇은 고분자 플라스틱 막인 <span class="mk-person">분리막</span>이 두 극 사이를 안전하게 가로막고 있다.</p>
                <p><span class="p-num">➋</span> 하지만 편리한 리튬 이온 배터리도 잘못 다루면 위험한 폭발물로 변할 수 있다. <span class="mk-highlight">배터리를 바닥에 세게 떨어뜨려 물리적 충격을 주거나, 규격보다 높은 전압의 충전기로 과충전하거나, 한여름 햇볕 아래 자동차 안처럼 뜨거운 곳에 방치하면 내부의 얇은 분리막이 찢어지거나 녹아내린다(약 130℃ 부근).</span> <span class="mk-line-red">분리막이 손상되어 양극과 음극이 직접 만나면 순간적으로 엄청난 전류가 흐르면서 내부 온도가 수초 만에 800도 이상으로 수직 상승한다.</span> 이 고열 때문에 배터리 속 전해액이 가스로 변해 부풀어 오르다가 결국 불이 붙고 폭발하는 연쇄 반응을 <span class="mk-line-red">‘열폭주(Thermal Runaway)’ 현상</span>이라고 한다.</p>
                <p><span class="p-num">➌</span> 따라서 열폭주 사고를 예방하려면 세 가지 안전 수칙을 꼭 지켜야 한다. 첫째, 제품을 고를 때는 과충전 방지 <span class="mk-person">보호 회로</span>가 검증된 ‘국가통합인증마크(KC 인증)’ 제품을 선택해야 한다. 둘째, 충전할 때는 고출력 고속 충전기 대신 제품의 정격 전압에 맞는 전용 충전기를 사용하고 강한 충격을 주지 말아야 한다. 셋째, 사용 중 배터리가 부풀어 오르는 ‘스웰링 현상’이 나타나거나 유난히 뜨거워지면 즉시 사용을 멈추어야 한다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 통합 추론하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>아래 <strong>[그래프 1]</strong>에서 배터리 온도가 서서히 오르다가 왜 <strong>130℃ 지점(변곡점 A)</strong>에서 갑자기 800℃까지 수직으로 치솟을까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>그래프만 보면 이유를 알 수 없지만, 본문 ➋문단 형광펜 문장과 연결해 보면 ‘약 130℃ 부근에서 플라스틱 분리막이 녹아내려 양극과 음극이 직접 맞닿기 때문’이라는 원리가 나와!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>본문의 <strong>과학 원리</strong>와 시각 자료의 <strong>수치 변곡점</strong>을 교차 연결하면 숨은 원리를 통합 추론할 수 있구나!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>

        <!-- 복합 인포그래픽: [표 1] 원인별 통계 + [그래프 1] 열폭주 온도 변곡점 다이어그램 -->
        <div style="display:grid; grid-template-columns:1.08fr 0.92fr; gap:6px; background:#F8F9F9; border:0.85pt solid #7FB3D5; border-radius:5px; padding:5px 7px;">
          <div>
            <div style="font-size:7.2pt; font-weight:800; color:#1A5276; margin-bottom:2px;">📊 [표 1] 휴대용 배터리 기기 화재·폭발 사고 원인별 비율 및 KC 인증 여부 (한국소비자원·소방청 종합)</div>
            <table class="std-table" style="font-size:6.8pt;">
              <thead>
                <tr>
                  <th>사고 발생 원인</th>
                  <th>비율(%)</th>
                  <th>주요 발생 상황 및 보호 회로 작동 여부</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700; color:#B03A2E;">① 과충전·부적합 충전기</td>
                  <td style="font-weight:800;">48.2%</td>
                  <td>고전압 고속 충전기 연결 / <strong>KC 미인증 제품(보호 회로 미작동)이 82% 차지</strong></td>
                </tr>
                <tr>
                  <td style="font-weight:700; color:#1A5276;">② 외부 물리적 충격·압착</td>
                  <td>31.5%</td>
                  <td>바닥 낙하, 무거운 물체에 눌림 ➔ 내부 분리막 직접 파손</td>
                </tr>
                <tr>
                  <td style="font-weight:700; color:#D35400;">③ 고온 환경 방치</td>
                  <td>14.3%</td>
                  <td>여름철 직사광선·밀폐된 차량 실내(70~85℃) 장시간 방치</td>
                </tr>
                <tr>
                  <td>④ 기타(제조 결함 등)</td>
                  <td>6.0%</td>
                  <td>전극 불량 및 노후화</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div style="background:#FFFFFF; border:0.75pt solid #BDC3C7; border-radius:4px; padding:4px 6px; font-size:6.9pt; display:flex; flex-direction:column; justify-content:space-between;">
            <div style="font-weight:800; color:#B03A2E; margin-bottom:2px;">📈 [그래프 1] 배터리 내부 온도 상승 단계와 ‘열폭주’ 변곡점</div>
            <div style="background:#FDEDEC; border-left:2.5pt solid #C0392B; padding:3px 5px; line-height:1.35;">
              • <strong>1단계 (정상: 20~60℃)</strong>: 리튬 이온이 분리막의 미세 구멍을 정상 통과함<br>
              • <strong>2단계 (이상 발열: 70~120℃)</strong>: 전해액 일부 기화 시작 (배터리 부풀음 <strong>‘스웰링’</strong> 발생 구간)<br>
              • <strong style="color:#C0392B;">★ 변곡점 A (약 130℃ 도달)</strong>: 고분자 플라스틱 <strong>분리막 용융(녹아내림)</strong> 및 붕괴<br>
              • <strong>3단계 (열폭주: 130℃ ➔ 800℃↑ 수초 내 수직 폭등)</strong>: 양극(+)·음극(-) 직접 접촉 ➔ 폭발·발화
            </div>
            <div style="font-size:6.5pt; color:#566573; text-align:right;">(출처: 국립소방연구원 · 한국소비자원 시험분석 자료 재구성)</div>
          </div>
        </div>
        """,
        "activity_1": {
            "title": "본문과 복합 시각 자료([표 1], [그래프 1])에서 각각 얻을 수 있는 고유 정보 단서 추출하기",
            "tag": "Step 1 텍스트·시각 매체 고유 단서 포착",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:20%;">정보 원천</th>
                  <th style="width:80%;">각 매체에서 찾을 수 있는 핵심 정보 단서</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">본문 텍스트<br>(➊~➌문단)</td>
                  <td>리튬 이온 배터리 속 <span class="blank-slot"><span class="t-ans">분리막</span></span>은 양극과 음극이 직접 닿지 않게 막아 주며, 손상 시 두 극이 만나 온도가 800℃ 이상 치솟는 <span class="blank-slot"><span class="t-ans">열폭주</span></span> 현상이 일어난다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">[표 1]<br>원인별 사고 통계</td>
                  <td>화재 원인은 <span class="blank-slot"><span class="t-ans">과충전·부적합 충전기(48.2%)</span></span> ➔ 외부 충격(31.5%) ➔ 고온 방치(14.3%) 순으로 높으며, 과충전 사고의 82%는 <span class="blank-slot"><span class="t-ans">KC 미인증 제품(보호 회로 미작동)</span></span>에서 발생했다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">[그래프 1]<br>온도 변화 단계</td>
                  <td>70~120℃ 구간에서 배터리가 부풀어 오르는 <span class="blank-slot"><span class="t-ans">스웰링</span></span> 현상이 먼저 나타나고, <span class="blank-slot"><span class="t-ans">약 130℃(변곡점 A)</span></span>에 도달하는 순간 분리막이 녹아 수초 만에 800℃ 이상으로 폭등한다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 찾은 본문 원리와 표·그래프 데이터를 교차 결합하여 숨겨진 인과 원리와 경향성 추론하기",
        "activity_2": {
            "title": "본문 원리와 [표 1]·[그래프 1]을 교차 연결하여 심층 원리 추론하기",
            "tag": "Step 2 텍스트-시각자료 상호보완 투사(Mapping)",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:32%;">통합 추론 질문</th>
                  <th style="width:33%;">연결할 [본문 단서] + [시각자료 단서]</th>
                  <th style="width:35%;">통합 추론 결론 (표면 수치 너머의 원리)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700;">① 왜 ➌문단에서는 배터리가 볼록하게 부풀어 오르면(스웰링) 즉시 사용을 멈추라고 했을까?</td>
                  <td>• [본문 ➌]: 부풀어 오르면 내부 손상 위험<br>• [그래프 1]: <strong>70~120℃(2단계)</strong>에서 스웰링 발생 직후 <strong>130℃ 변곡점(열폭주)</strong> 도달</td>
                  <td>스웰링 현상은 온도가 열폭주 직전 단계인 <span class="blank-slot"><span class="t-ans">70~120℃까지 올라 전해액이 가스로 변했다는 마지막 경고 신호</span></span>이기 때문이다.</td>
                </tr>
                <tr>
                  <td style="font-weight:700;">② 왜 ‘KC 인증’ 마크 확인과 ‘전용 충전기’ 사용만으로도 전체 화재의 절반 가까이를 막을 수 있을까?</td>
                  <td>• [본문 ➌]: KC 인증은 과충전 <strong>보호 회로</strong> 검증, 전용 충전기는 정격 전압 유지<br>• [표 1]: <strong>과충전 사고가 48.2%(1위)</strong>이며 그중 82%가 KC 미인증 제품임</td>
                  <td>사고 원인 1위(48.2%)인 과충전 화재의 대부분이 <span class="blank-slot"><span class="t-ans">보호 회로가 없는 미인증 제품에 고전압 충전기를 꽂아 발생</span></span>하기 때문이다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 통합 추론 결과를 실생활 안전 상황에 적용하여 과학적 분석 보고문 작성하기",
        "activity_3": {
            "title": "본문 이론과 시각 자료 수치를 인용하여 ‘실생활 배터리 위험 상황 분석 보고문’ 작성하기",
            "tag": "Step 3 실생활 적용 통합 추론 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>[실생활 상황]</strong> 민수네 가족은 여름휴가 때 해수욕장에 가면서 <strong>KC 인증 마크가 없는 휴대용 선풍기</strong>를 <strong>스마트폰 초고속 충전기에 꽂은 채</strong> 햇볕이 내리쬐는 <strong>자동차 앞유리 아래에 두고</strong> 내렸습니다. 본문의 원리(`분리막, 열폭주`)와 `[표 1]·[그래프 1]`의 수치를 인용하여 왜 위험한지 분석 보고문을 써 보세요.</div>
              <span class="pencil-line">✏️ <span class="t-ans">[표 1]을 보면 과충전·부적합 충전기 사용(48.2%)과 고온 방치(14.3%)는 배터리 화재의 주요 원인이며, 특히 과충전 사고의 82%가 보호 회로가 없는 KC 미인증 제품에서 발생한다.</span></span>
              <span class="pencil-line">✏️ <span class="t-ans">민수네처럼 미인증 선풍기를 고속 충전기에 꽂아 70~85℃의 뜨거운 차 안에 두면, [그래프 1]처럼 배터리가 부풀어 오르다가 130℃ 변곡점을 넘어 분리막이 녹아내리고 양극과 음극이 맞닿아 800℃ 이상 치솟는 ‘열폭주’ 폭발이 일어날 수 있으므로 매우 위험하다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 시각자료 기획)·15차시(W4 시각자료 통합 집필) 직결",
            "prompt": "내가 쓸 설명문에서 글만으로는 설명하기 복잡하여 ‘표’나 ‘그래프’로 보여 주고 싶은 핵심 수치·원리가 무엇인지 씨앗을 적어 보세요.",
            "placeholder": "(예: 연도별 기온 상승 추세 꺾은선그래프, 원인별 비율 원그래프 등)",
            "example_answer": "청소년 스마트폰 사용 시간대별 수면의 질 변화 꺾은선그래프와 블루라이트 차단 전후 멜라토닌 분비량 비교 막대그래프",
        },
        "self_check": [
            "본문 텍스트의 과학적 원리(`분리막 파손 ➔ 단락 ➔ 열폭주`)와 표·그래프의 고유 수치를 정확히 찾았나요?",
            "[그래프 1]의 온도 변곡점(130℃)과 [표 1]의 원인별 비율(48.2%)을 본문 이론과 교차 연결하여 해석했나요?",
            "본문 명제와 시각 자료 수치를 모두 인용하여 실생활 위험 상황을 분석하는 글을 논리적으로 썼나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] Schnotz 텍스트-그림 통합 이해(ITPC) 공식: `[본문 텍스트: 분리막 구조·열폭주 원리·안전 수칙]` ⇄ `[표 1: 과충전 48.2%(KC 미인증 82%) / 충격 31.5% / 고온 14.3%]` + `[그래프 1: 70~120℃ 스웰링 ➔ ★130℃ 분리막 용융 변곡점 ➔ 800℃ 열폭주]` / [우측 판서] 실생활 적용 추론: 데이터 수치 인용 + 과학 원리 결합.",
            "intro_5min": "여름철 우리가 매일 들고 다니는 휴대용 손선풍기나 보조 배터리가 갑자기 부풀어 오르거나 불이 났다는 뉴스를 본 적이 있나요? 오늘 7차시에서는 본문의 과학 원리와 소방청·한국소비자원의 통계표·온도 그래프를 하나로 합쳐 읽는 ‘텍스트-시각자료 통합 추론’을 배웁니다.",
            "ido_think_aloud_script": "“선생님이 본문 ➋문단과 아래 [그래프 1]을 어떻게 번갈아 보며 통합 추론하는지 시범을 보일게요. [그래프 1]을 보면 배터리 온도가 20℃에서 120℃까지는 완만하게 오르다가, ‘변곡점 A(약 130℃)’에 닿는 순간 수초 만에 800℃ 이상으로 로켓처럼 수직 폭등하네요! 그래프의 숫자만 보면 ‘왜 하필 130℃에서 갑자기 폭발하지?’ 하고 궁금증이 생겨요. 이때 본문 ➋문단으로 눈을 돌려 단서를 찾아봅니다. 아하! ‘약 130℃ 부근에서 내부의 얇은 고분자 플라스틱 분리막이 녹아내린다. 분리막이 손상되어 양극과 음극이 직접 만나면 순간적으로 엄청난 전류가 흐르면서 800도 이상으로 수직 상승한다’고 설명되어 있네요! 이처럼 그래프의 ‘수치 변곡점’과 본문의 ‘과학적 작동 원리’를 연결해야만 완벽한 이해에 도달할 수 있습니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "본문 ➌문단에서는 배터리가 볼록하게 부풀어 오르는 ‘스웰링 현상’이 보이면 즉시 사용을 멈추라고 했습니다. [그래프 1]을 근거로 볼 때, 스웰링 현상은 열폭주 과정에서 어떤 단계를 뜻하나요?",
                    "expected_ans": "[그래프 1]의 2단계(70~120℃ 이상 발열 구간)를 보면 전해액이 가스로 기화하면서 배터리가 부풀어 오르는 스웰링이 일어납니다. 즉, 스웰링은 분리막이 녹아내리는 130℃ 열폭주(3단계) 직전에 배터리가 보내는 마지막 위험 경고 신호입니다.",
                    "reprompt": "[그래프 1]에서 ‘스웰링 발생 구간’이 몇 도이며, 그 바로 다음 단계(변곡점 A)가 무엇인지 확인해 보세요.",
                },
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[표 1]에서 휴대용 배터리 화재 원인 1위는 무엇이며(몇 %), 이를 예방하기 위해 본문 ➌문단이 제시한 두 가지 안전 수칙은 무엇인가요?",
                    "expected_ans": "화재 원인 1위는 ‘과충전·부적합 충전기 사용(48.2%)’이며, 특히 그중 82%가 보호 회로가 작동하지 않는 KC 미인증 제품이었습니다. 이를 막으려면 첫째 과충전 보호 회로가 검증된 ‘KC 인증 제품’을 고르고, 둘째 고속 충전기 대신 규격에 맞는 ‘전용 충전기’를 사용해야 합니다.",
                    "reprompt": "[표 1]의 첫 번째 줄(48.2%) 오른쪽 설명과 본문 ➌문단의 첫째·둘째 안전 수칙을 짝지어 읽어 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 세 정보원(본문, 표 1, 그래프 1)의 고유 단서를 추출하고, [활동 2]에서 교차 추론 표를 완성한 뒤, [활동 3]에서 민수네 가족의 위험 사례(KC 미인증 + 고속 충전기 과충전 + 여름철 차량 내 고온 방치)를 표·그래프 수치와 본문 원리를 모두 인용해 분석 보고문으로 작성하도록 지도한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 매체별 고유 단서 추출</strong>: 본문: <strong>분리막</strong>, <strong>열폭주</strong> / [표 1]: <strong>과충전·부적합 충전기(48.2%)</strong>, <strong>KC 미인증 제품(보호 회로 미작동)</strong> / [그래프 1]: <strong>스웰링</strong>, <strong>약 130℃(변곡점 A)</strong><br>
              <strong>2. [활동 2] 교차 통합 추론</strong>: ① <strong>70~120℃까지 올라 전해액이 가스로 변했다는 열폭주(130℃) 직전의 마지막 경고 신호</strong> / ② <strong>보호 회로가 없는 KC 미인증 제품에 고전압 부적합 충전기를 꽂아 발생</strong><br>
              <strong>3. [활동 3] 실생활 분석 보고문 (인정 답안 기준)</strong>: (1) [표 1]의 수치(과충전 48.2%, 고온 방치 14.3%, 미인증 82% 중 1개 이상), (2) [그래프 1]의 온도 단계(70~85℃ 스웰링 ➔ 130℃ 변곡점 ➔ 800℃), (3) 본문의 과학 원리(분리막 용융 ➔ 양극·음극 접촉 열폭주)의 3요소를 모두 결합하여 서술하면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "[활동 3] 분석 보고문을 쓸 때 본문 내용만 베껴 쓰고 [표 1]·[그래프 1]의 구체적 수치(48.2%, 130℃, 800℃)를 전혀 인용하지 않는 오류",
                    "diagnosis": "시각 자료를 본문과 독립된 장식물로 여겨, 글과 표·그래프의 정보를 하나의 논증 근거로 합성(Synthesis)하는 습관이 부족함.",
                    "prescription": "‘시각 자료 지시 표현’(“[표 1]에 따르면 ~%, [그래프 1]의 130℃ 변곡점에서 보듯이”)을 문장 첫머리에 반드시 넣어 본문 원리와 수치를 한 문장 안에서 엮도록 지도한다.",
                },
                {
                    "error_case": "[표 1]의 ‘과충전 사고 중 KC 미인증 제품이 82%’라는 수치를 ‘전체 배터리 화재 원인의 82%가 과충전’이라고 잘못 읽는 오류",
                    "diagnosis": "전체 집합(원인별 비율 48.2%)과 부분 집합 내 조건부 비율(과충전 사고 내 미인증 비율 82%)의 층위를 혼동함.",
                    "prescription": "전체 화재 원인 1위는 ‘과충전(48.2%)’이고, 그 과충전 사고 안을 들여다봤을 때 10건 중 8건 이상(82%)이 ‘KC 미인증 제품’임을 벤다이어그램이나 막대 분할로 확인시켜 준다.",
                },
            ],
            "scaffolding_down": "본문과 표·그래프를 동시에 보기 버거워하는 학습자에게는 본문 ➋문단의 ‘약 130℃’와 [그래프 1]의 ‘변곡점 A(130℃)’를 색연필 실선으로 직접 잇게 하고, 본문 ➌문단의 ‘KC 인증·전용 충전기’와 [표 1]의 ‘①번 행(48.2%)’을 실선으로 먼저 연결하게 한다.",
            "scaffolding_up": "심화 학습자에게는 비행기에 탑승할 때 왜 리튬 이온 보조 배터리를 화물칸에 부치지 못하게 하고 승객이 직접 기내에 들고 타게 하는지(화물칸 압력·충격 및 스웰링·초기 발열 즉시 감지 필요성), 오늘 배운 [표 1]·[그래프 1] 원리로 추론해 발표하게 한다.",
            "rubric": {
                "high": "본문의 과학적 원리와 [표 1]·[그래프 1]의 수치·변곡점을 정확히 교차 연결하여 숨은 경향성과 원리를 추론하고, 두 매체의 근거를 모두 인용한 분석 보고문을 논리적으로 작성함.",
                "mid": "본문과 시각 자료의 개별 정보는 찾고 추론 표의 빈칸을 채웠으나, 실생활 적용 보고문 작성 시 표나 그래프의 구체적 수치 인용이 일부 누락됨.",
                "low": "본문 텍스트와 시각 자료를 별개로 읽어 그래프의 변곡점(130℃)이 의미하는 과학적 원리를 본문에서 찾아 연결하는 데 어려움이 있음.",
            },
        },
    },

    # =========================================================================
    # 8차시: G6-EXP-V2-4 필자의 집필 목적·예상 독자·관점 추론
    # 제재: 동일 과학 소재(배터리 안전 & 우주 쓰레기 제거 기술)의
    #       [글 가] 전문가용 기술 보고서 발췌문 vs [글 나] 어린이 안전·과학 길잡이 설명문 비교
    # =========================================================================
    {
        "lesson_no": 8,
        "code": "G6-EXP-V2-4",
        "lesson_title": "어휘 수준과 설명 방식을 단서로 필자의 의도·예상 독자·관점 추론하기",
        "std_badge": "[6국02-04] · CCSS RI.6.6 · PISA 수사적 맥락",
        "student_goal": "동일한 과학 소재를 다룬 두 설명문의 어휘 수준, 비유·예시 방식, 소제목 구성을 비교하여 필자의 집필 의도와 예상 독자 수준, 내재된 관점을 추론할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "[글 가]의 전문 학술 용어·정량적 시험 규격"],
            ["mk-bg", "초록 네모", "[글 나]의 친숙한 일상 비유·독자 맞춤형 용어 풀이"],
            ["mk-highlight", "형광펜", "필자의 집필 의도와 관점이 드러나는 핵심 문장"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 동일 소재 다른 설명: [글 가] 전문 기술 보고서 vs [글 나] 어린이 과학·안전 길잡이</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 한국소비자원·한국항공우주연구원(KARI) 기술 보고서 &amp; 어린이 안전넷·카리스쿨 해설</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 비교 정독 (두 글의 어휘 난이도, 비유·예시, 강조점을 비교하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 수사적 맥락 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#1A5276; margin-bottom:2px;">[글 가] 리튬 이온 이차전지의 열폭주 제어 및 궤도 잔해물 능동 제거 기술 동향</div>
                <p><span class="p-num">➊</span> <strong>1. 분리막 열수축률 제어 및 보호회로(PCM) 설계 기준</strong><br>
                리튬 이온 이차전지의 에너지 밀도 고도화에 따라, 내부 단락(Internal Short-Circuit)에 기인한 열폭주(Thermal Runaway) 억제 기술이 핵심 안전성 지표로 대두되고 있다. <span class="mk-person">폴리올레핀(Polyolefin)계 미세 다공성 분리막</span>은 130℃ 이상의 고온 노출 시 열수축 현상으로 인해 양극(<span class="mk-person">LiCoO₂</span> 등)과 음극(흑연) 간 물리적 접촉을 유발한다. 이에 따라 세라믹 코팅 분리막(CCS)을 적용하여 내열 온도를 180℃ 이상으로 향상시키고, <span class="mk-person">과충전 차단 보호회로 모듈(PCM)의 전압 임계치를 셀당 4.25V 이하로 정밀 제어</span>하는 기술 표준 검증이 요구된다.</p>
                <p><span class="p-num">➋</span> <strong>2. 저궤도 우주 잔해물(Space Debris) 감속 및 대기권 재진입 메커니즘</strong><br>
                고도 2,000km 이하 지구 저궤도(LEO) 내 비가동 위성체의 밀도 증가는 <span class="mk-person">케슬러 신드롬(Kessler Syndrome)에 따른 궤도 포화 리스크</span>를 가중시킨다. 한국항공우주연구원(KARI)이 개발한 <span class="mk-person">25㎡급 폴리이미드 박막 태양 돛(Solar Sail) 궤도 이탈 장치</span>는 별도의 추진제 소모 없이 태양 복사압과 잔류 대기 항력(Atmospheric Drag)을 극대화하여, 임무 종료 위성체의 궤도 고도를 단기간 내 감쇠시키고 대기권 마찰열을 통한 완전 소각을 유도하는 <span class="mk-highlight">고효율·저비용 우주 교통 관리(STM) 핵심 기술로 평가된다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 비교 추론하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>[글 가]와 [글 나]는 똑같이 ‘배터리 열폭주’와 ‘우주 쓰레기 태양 돛’을 다루는데, 왜 이렇게 느낌이 다를까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>[글 가]는 ‘폴리올레핀계 다공성 분리막, 셀당 4.25V 임계치, 잔류 대기 항력’처럼 뜻풀이 없는 <strong>전문 학술 용어</strong>를 썼어. 반면 [글 나]는 ‘여러분의 가방 속 손선풍기, 창문 방충망, 거대한 돛단배’처럼 <strong>친숙한 일상 비유와 질문형 소제목</strong>을 썼네!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>필자가 염두에 둔 <strong>예상 독자의 지식 수준</strong>과 <strong>집필 의도·관점</strong>이 다르기 때문이구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#196F3D; margin-bottom:2px;">[글 나] 내 가방 속 작은 발전소와 밤하늘 청소부 위성, 어떻게 안전을 지킬까요?</div>
                <p><span class="p-num">➌</span> <strong>질문 1. 휴대용 선풍기 속 배터리는 왜 떨어뜨리면 위험할까요?</strong><br>
                여름날 <span class="mk-bg">여러분이 등하굣길 가방에 넣고 다니는 휴대용 선풍기</span> 속에는 작은 발전소 같은 ‘리튬 이온 배터리’가 들어 있습니다. 배터리 안에는 전기를 만드는 양극(+) 방과 음극(-) 방이 나란히 있는데, 두 방이 직접 부딪쳐 불꽃이 튀지 않도록 가운데에 <span class="mk-bg">창문 방충망처럼 미세한 구멍이 뚫린 얇은 플라스틱 ‘분리막’</span>이 든든한 문지기처럼 서 있답니다. 그런데 선풍기를 바닥에 쾅 떨어뜨리거나 뜨거운 차 안에 두면 이 문지기 막이 찢어져 버려요. <span class="mk-highlight">따라서 우리가 일상에서 폭발 사고를 막으려면 꼭 ‘KC 안전 인증 마크’를 확인하고, 배터리가 풍선처럼 부풀어 오르면 즉시 사용을 멈추는 안전 습관을 실천해야 합니다.</span></p>
                <p><span class="p-num">➍</span> <strong>질문 2. 수명이 끝난 인공위성은 어떻게 연료 없이 지구로 내려올까요?</strong><br>
                우주에도 우리가 쓰고 버린 일회용품처럼 위험한 ‘우주 쓰레기’가 떠돌고 있습니다. 우리나라 한국항공우주연구원 과학자들은 수명이 끝난 위성이 우주 쓰레기가 되지 않도록 <span class="mk-bg">바다 위를 달리는 ‘돛단배’의 원리</span>를 떠올렸습니다. 위성의 임무가 끝나면 <span class="mk-bg">교실 바닥 절반만 한 넓이(25제곱미터)의 얇고 커다란 ‘태양 돛’</span>을 활짝 펼치는 것이지요. 그러면 바람 대신 태양 빛이 미는 힘과 공기 저항을 받아 연료 한 방울 없이도 대기권으로 내려와 별똥별처럼 불타 사라집니다. <span class="mk-highlight">지구의 땅과 바다를 깨끗이 아끼듯, 밤하늘 우주 환경을 지키는 일에도 우리의 꾸준한 관심이 필요합니다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 짝·스스로 추론하기</span><span class="role-chip">We·You Do</span></div>
                  <div>1. 25㎡ 크기의 태양 돛을 설명할 때 [글 가]와 [글 나]는 각각 어떻게 표현했나요?</div>
                  <div>• [글 가]: <span class="blank-slot"><span class="t-ans">25㎡급 폴리이미드 박막</span></span></div>
                  <div>• [글 나]: <span class="blank-slot"><span class="t-ans">교실 바닥 절반만 한 넓이의 커다란 돛</span></span></div>
                  <div style="margin-top:3px;">2. 두 글의 어미(`~된다` vs `~합니다`)와 소제목 방식의 차이는 무엇을 보여 주나요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">예상 독자(성인 전문가 vs 초등학생·청소년)에 맞춘 필자의 배려와 설명 목적의 차이를 보여 준다.</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "동일 소재를 다룬 [글 가]와 [글 나]의 언어적·구조적 단서 비교하기",
            "tag": "Step 1 어휘·비유·소제목·선택 정보 단서 포착",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:20%;">비교 단서 항목</th>
                  <th style="width:40%;">[글 가] 기술 보고서 발췌문</th>
                  <th style="width:40%;">[글 나] 어린이 과학·안전 길잡이</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">① 어휘 수준 및<br>용어 풀이 방식</td>
                  <td>‘폴리올레핀계 분리막, <span class="blank-slot"><span class="t-ans">LiCoO₂(화학식)</span></span>, 잔류 대기 항력’ 등 전문 학술어를 별도의 뜻풀이 없이 그대로 사용함</td>
                  <td>학술어를 최소화하고, ‘분리막’이나 ‘25㎡’가 나올 때 <span class="blank-slot"><span class="t-ans">친절한 뜻풀이와 괄호 설명</span></span>을 덧붙임</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">② 비유 및 예시 소재</td>
                  <td>비유 없이 <span class="blank-slot"><span class="t-ans">180℃, 셀당 4.25V 이하</span></span> 등 정밀한 공학 수치와 기술 규격을 제시함</td>
                  <td>‘등하굣길 가방 속 손선풍기, <span class="blank-slot"><span class="t-ans">창문 방충망·문지기</span></span>, <span class="blank-slot"><span class="t-ans">돛단배·교실 바닥 절반</span></span>’ 등 친숙한 비유 사용</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">③ 소제목 및 문체</td>
                  <td>명사형 학술 소제목 / 건조하고 공식적인 어조(`~된다`)</td>
                  <td>호기심을 자극하는 <span class="blank-slot"><span class="t-ans">질문형 소제목</span></span> / 친근한 경어체(`~합니다`)</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 포착한 텍스트 단서들을 수사적 맥락(예상 독자·집필 의도·내재된 관점)과 연결하기",
        "activity_2": {
            "title": "단서를 바탕으로 [글 가]와 [글 나]의 예상 독자·집필 의도·관점 추론 도해 완성하기",
            "tag": "Step 2 수사적 맥락(독자·목적·관점) 연결",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:20%;">수사적 맥락 요소</th>
                  <th style="width:40%;">[글 가] 추론 결과</th>
                  <th style="width:40%;">[글 나] 추론 결과</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">👥 예상 독자층<br>(지식 수준·요구)</td>
                  <td>배터리·우주 공학에 대한 사전 지식이 풍부한 <span class="blank-slot"><span class="t-ans">과학 기술 연구원, 엔지니어, 안전 기준 정책 담당자</span></span></td>
                  <td>휴대용 선풍기를 직접 쓰며 과학 원리에 호기심이 많은 <span class="blank-slot"><span class="t-ans">초등학생 및 청소년 독자</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">🎯 필자의 집필 의도<br>(글을 쓴 목적)</td>
                  <td>열폭주 억제 소재(세라믹 코팅)와 태양 돛 궤도 이탈 장치의 <span class="blank-slot"><span class="t-ans">정확한 기술 메커니즘과 설계 기준(표준)을 보고</span></span>하기 위해</td>
                  <td>어린이들이 과학 원리를 쉽게 이해하고 <span class="blank-slot"><span class="t-ans">일상 속 배터리 안전 수칙 실천과 우주 환경 보호 관심</span></span>을 갖게 하기 위해</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">🔭 내재된 관점<br>(바라보는 시각)</td>
                  <td>문제를 소재 개선과 정밀 설계로 해결하려는 <span class="blank-slot"><span class="t-ans">공학·기술적 효율성 및 안전 규제 관점</span></span></td>
                  <td>과학 기술을 사용자의 <span class="blank-slot"><span class="t-ans">생활 안전 습관 및 환경 시민 의식</span></span>과 연결하여 바라보는 교육적 관점</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 배운 ‘독자 맞춤형 설명 원리’를 적용하여 예상 독자를 바꾸어 설명 문장 고쳐 쓰기",
        "activity_3": {
            "title": "예상 독자의 수준에 맞게 설명 문장을 변환하고 필자 의도·관점 분석문 작성하기",
            "tag": "Step 3 독자 맞춤형 변환 및 관점 분석 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>1. [독자 맞춤형 변환 실습]</strong> 아래 전문가용 설명 문장을 <strong>‘초등학교 3학년 동생(예상 독자)’</strong>이 쉽게 이해할 수 있도록 친숙한 비유와 쉬운 뜻풀이를 넣어 바꾸어 써 보세요.</div>
              <div style="background:#F2F4F4; padding:3px 6px; border-radius:4px; margin:2px 0; font-size:7.1pt;"><strong>[원문]</strong> “세라믹 코팅 분리막(CCS)은 고온에서의 열수축을 억제하여 양극과 음극의 내부 단락을 방지한다.”</div>
              <span class="pencil-line">✏️ 초등 3학년 맞춤형 변환: <span class="t-ans">배터리 안의 분리막에 불에 강한 도자기 가루(세라믹) 옷을 입히면, 배터리가 뜨거워져도 막이 줄어들거나 녹지 않아서 양극 방과 음극 방이 서로 부딪쳐 불이 나는 것을 안전하게 막아 준단다.</span></span>
              <div style="margin-top:3px;"><strong>2. [종합 정리]</strong> 같은 대상을 설명하는 글이라도 필자의 <span class="blank-slot"><span class="t-ans">집필 의도(목적)</span></span>와 <span class="blank-slot"><span class="t-ans">예상 독자의 수준</span></span>에 따라 어휘의 난이도와 비유·예시 방식이 달라진다.</div>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "12차시(W1 계획하기: 예상 독자·목적 설정) 1:1 직결",
            "prompt": "12차시부터 내가 직접 쓸 설명문의 ‘예상 독자(누구에게)’와 ‘집필 목적(왜)’을 정하고, 그 독자를 위해 어떤 눈높이 비유를 쓸지 씨앗을 남겨 보세요.",
            "placeholder": "(예: 예상 독자: 우리 반 6학년 친구들 / 비유: 인공지능 데이터를 ‘요리 재료’에 비유)",
            "example_answer": "예상 독자: 과학 용어를 어려워하는 5~6학년 후배와 친구들 / 집필 목적: 기후 위기 속 산호초 보호 방법 안내 / 맞춤 전략: 산호와 미세조류의 공생을 ‘집주인과 요리사 단짝 친구’에 비유하여 설명하기",
        },
        "self_check": [
            "[글 가]와 [글 나]에 쓰인 어휘 수준, 비유·예시, 소제목 방식의 차이를 정확히 찾아냈나요?",
            "텍스트 단서를 근거로 두 글의 예상 독자층과 필자의 집필 의도·관점을 타당하게 추론했나요?",
            "예상 독자의 눈높이(사전 지식 수준)에 맞추어 어려운 학술 문장을 쉬운 비유 문장으로 변환했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 수사적 맥락(Rhetorical Context) 추론 삼각형: `텍스트 단서(어휘 난이도 · 비유/수치 · 소제목 · 선택된 정보)` ➔ ① **예상 독자**(전문가 vs 초등학생), ② **집필 의도**(기술 표준 보고 vs 안전 수칙 실천·환경 교육), ③ **내재된 관점**(공학적 설계 관점 vs 생활 안전·환경 시민 관점) / [우측 판서] 12차시 쓰기(W1 계획하기) 전이 브릿지: 글을 쓰기 전에 반드시 ‘누구(독자)를 위해 왜(목적) 쓰는가’를 먼저 설계해야 한다!",
            "intro_5min": "여러분은 4차시에서 ‘우주 쓰레기 태양 돛’을, 7차시에서 ‘배터리 열폭주’를 배웠습니다. 그런데 똑같은 내용을 한국항공우주연구원 박사님들이 읽는 보고서와 어린이 과학 잡지에 실을 때 똑같이 쓸까요? 두 글을 비교하며 숨어 있는 필자의 의도와 예상 독자, 관점을 추론하는 8차시(추론적 읽기 마침표) 목표를 안내한다.",
            "ido_think_aloud_script": "“선생님이 [글 가]와 [글 나]의 첫 문단을 비교하며 필자의 머릿속 설계도를 추론해 볼게요. [글 가]를 보니 ‘폴리올레핀계 미세 다공성 분리막, LiCoO₂, 셀당 4.25V 임계치’처럼 화학 기호와 전문 공학 용어가 아무런 설명 없이 쏟아져 나와요. 만약 초등학생이 읽으라고 쓴 글이라면 이렇게 불친절하게 썼을까요? 아니겠죠! 이 단서를 보면 [글 가]의 예상 독자는 이미 이 용어들을 다 알고 있는 배터리 엔지니어나 안전 규격 담당자이고, 필자의 의도는 ‘정밀한 기술 기준을 객관적으로 보고하는 것’임을 알 수 있어요. 반면 [글 나]는 어떤가요? ‘여러분이 등하굣길 가방에 넣고 다니는 손선풍기’, ‘창문 방충망처럼 생긴 문지기 분리막’이라는 비유를 썼네요! 아하, [글 나]의 예상 독자는 초등학생·청소년이고, 필자는 학생들이 원리를 쉽게 이해해 생활 속 안전 수칙을 실천하도록 돕고 싶어 하는구나!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "우주 쓰레기를 없애는 25㎡ 태양 돛 기술을 설명할 때, [글 가]와 [글 나]가 선택한 정보와 표현 방식은 어떻게 다른가요?",
                    "expected_ans": "[글 가]는 ‘25㎡급 폴리이미드 박막, 태양 복사압과 잔류 대기 항력 극대화, 우주 교통 관리(STM) 기술’처럼 재질과 물리학적 원리를 정밀하게 서술했습니다. 반면 [글 나]는 ‘교실 바닥 절반만 한 넓이’, ‘바람을 받는 돛단배’, ‘별똥별처럼 불타 사라진다’처럼 어린이의 경험 세계에 맞춘 비유로 풀어 썼습니다.",
                    "reprompt": "➋문단과 ➍문단에서 ‘25㎡(25제곱미터)’와 ‘태양 돛’이 있는 문장을 나란히 밑줄 긋고 사용된 단어를 비교해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "두 글의 마지막 문장(형광펜 부분)을 비교해 볼 때, 우주 쓰레기 문제를 바라보는 두 필자의 ‘관점(시각)’에는 어떤 차이가 있나요?",
                    "expected_ans": "[글 가]의 필자는 태양 돛을 ‘고효율·저비용 우주 교통 관리 핵심 기술’로 평가하며 기술·경제적 효율성 관점에서 바라보고 있습니다. 반면 [글 나]의 필자는 ‘땅과 바다를 아끼듯 밤하늘 우주 환경을 지키는 관심’을 강조하며 생태·환경 보호 시민 의식의 관점에서 바라보고 있습니다.",
                    "reprompt": "➋문단 끝의 ‘고효율·저비용 기술로 평가된다’와 ➍문단 끝의 ‘우주 환경을 지키는 일에도 관심이 필요합니다’ 중 어느 쪽이 공학 기술 관점이고 어느 쪽이 환경 교육 관점인지 비교해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 어휘·비유·소제목 단서를 비교하고, [활동 2]에서 예상 독자·집필 의도·관점 추론 표를 완성한 뒤, [활동 3]에서 전문가용 문장(‘세라믹 코팅 분리막’)을 초등학교 3학년 동생 눈높이의 비유 문장으로 변환하도록 지도한다. 추론적 이해 4차시(어휘-인과-시각자료-필자의도)를 갈무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 날개 [We·You Do]</strong>: 1. [글 가]: <strong>25㎡급 폴리이미드 박막</strong> / [글 나]: <strong>교실 바닥 절반만 한 넓이의 커다란 돛</strong> / 2. <strong>예상 독자의 지식 수준에 맞춘 필자의 배려와 집필 목적의 차이</strong><br>
              <strong>2. [활동 1] 언어적·구조적 단서 비교</strong>: ① <strong>LiCoO₂(화학식)</strong>, <strong>친절한 뜻풀이와 괄호 설명</strong> / ② <strong>180℃, 셀당 4.25V 이하</strong>, <strong>창문 방충망·문지기</strong>, <strong>돛단배·교실 바닥 절반</strong> / ③ <strong>질문형 소제목</strong><br>
              <strong>3. [활동 2] 독자·의도·관점 추론</strong>: 예상 독자: <strong>과학 기술 연구원·엔지니어·정책 담당자</strong> vs <strong>초등학생 및 청소년 독자</strong> / 집필 의도: <strong>정확한 기술 메커니즘과 설계 기준(표준) 보고</strong> vs <strong>일상 속 안전 수칙 실천과 우주 환경 보호 관심 유도</strong> / 관점: <strong>공학·기술적 효율성 및 안전 규제 관점</strong> vs <strong>생활 안전 습관 및 환경 시민 의식 관점</strong><br>
              <strong>4. [활동 3] 독자 맞춤형 변환 산출</strong>: ‘세라믹 코팅(불에 강한 도자기 옷 등 비유)’과 ‘열수축 억제 및 단락 방지(뜨거워져도 줄어들지 않아 두 극이 부딪치지 않게 막음)’를 초3 눈높이의 쉬운 어휘와 비유로 풀어 쓰면 정답 인정. / 2번 빈칸: <strong>집필 의도(목적)</strong>, <strong>예상 독자의 수준</strong>
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "“설명문은 객관적인 사실만 전달하는 글이므로 필자의 관점이나 의도가 전혀 없다”고 생각하는 오개념",
                    "diagnosis": "‘주관적 주장(논설문) 배제’를 ‘필자의 집필 목적이나 대상을 바라보는 시각(관점/프레임) 부재’와 혼동함.",
                    "prescription": "설명문도 ‘어떤 독자에게 왜 설명하는가(의도)’와 ‘대상의 어떤 측면(기술적 효율 vs 환경적 가치)을 선택해 강조하는가(관점)’에 따라 글의 모습이 완전히 달라짐을 [글 가]·[글 나] 대조로 깨닫게 한다.",
                },
                {
                    "error_case": "[글 가]처럼 어려운 전문 용어를 많이 쓴 글이 무조건 더 훌륭한 설명문이라고 판단하는 오류",
                    "diagnosis": "글의 우수성을 절대적인 어휘 난이도로만 판단하고, ‘예상 독자와의 소통 적합성’이라는 수사적 준거를 고려하지 못함.",
                    "prescription": "초등학생 독자에게 [글 가]를 주면 이해할 수 없으므로 실패한 설명이 됨을 짚어 주고, “가장 좋은 설명문은 예상 독자의 눈높이에 가장 잘 맞춘 글”임을 강조한다.",
                },
            ],
            "scaffolding_down": "[활동 3]의 초등 3학년 맞춤형 문장 변환을 어려워하는 학습자에게는 1단계로 어려운 단어 3개(`세라믹 코팅`, `열수축 억제`, `내부 단락 방지`)를 각각 쉬운 말(`도자기 가루 옷 입히기`, `뜨거워져도 오그라들지 않기`, `두 방이 부딪쳐 불나는 것 막기`)로 먼저 바꾸어 적은 뒤 한 문장으로 잇게 한다.",
            "scaffolding_up": "심화 학습자에게는 6차시에서 읽은 〈산호초 백화 현상〉 글을 ‘바닷가 여행을 떠나는 관광객들에게 선크림·탄소 줄이기를 안내하는 공익 안내판 설명문’으로 바꾼다면 소제목과 첫 문장을 어떻게 바꿀지 작성해 보게 한다.",
            "rubric": {
                "high": "어휘 수준, 비유·예시, 소제목 구성을 단서로 두 설명문의 예상 독자·집필 의도·내재된 관점을 정확히 추론하여 분석하고, 독자 수준에 맞춘 설명 문장 변환을 탁월하게 수행함.",
                "mid": "두 글의 예상 독자(전문가 vs 어린이)와 어휘 수준 차이는 정확히 구분하나, 설명에 내재된 ‘관점(기술 효율 vs 안전·환경 교육)’의 차이 설명이나 문장 변환이 다소 단편적임.",
                "low": "표면적인 글의 길이만 비교할 뿐 어휘·비유 단서를 통해 필자의 집필 의도와 예상 독자 특성을 역추적하는 데 어려움이 있음.",
            },
        },
    },
]
