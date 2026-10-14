# -*- coding: utf-8 -*-
"""
1단원: 시 (Poetry, unit1_poetry) — Batch 4 (12~16차시: 과정중심 시 쓰기 5단계 W1 ~ W5)
구성:
- 12차시(W1 계획하기): 1~11차시 씨앗 보관함 소환, 일상 대상의 재발견 주제·화자(페르소나)·독자·목적·어조 설정
- 13차시(W2 생성하기): 오감·공감각 심상 팔레트, 형태소 결합 복합 시어(합성어·파생어), 비유 브릿지(원관념⟷공통점⟷보조관념)
- 14차시(W3 조직하기): 읽기 모델(〈구부러진 길〉·〈봄길〉·〈새로운 길〉) 미러링 4연 시상 전개(기-승-전-결/수미상관) 및 운율 설계도
- 15차시(W4 집필하기): 시어·운율·비유 뱅크 활용 및 행간 걸침·연 구분을 살린 현대시 초고 집필 스튜디오
- 16차시(W5 고쳐쓰기): 2층 고행간 시어 조탁 노트(상투적 어휘 교체, 행간 주술·부사어 호응 교정, 교정부호 첨삭) 및 시화 출판·성찰
"""

BATCH4 = [
    # =========================================================================
    # 12차시: G6-POE-W1 계획하기 (목적·독자·주제·갈래 설정)
    # =========================================================================
    {
        "lesson_title": "[시 쓰기 ① 계획하기] 씨앗 보관함을 열어 시적 대상과 화자·주제 기획하기",
        "std_badge": "[6국03-02] [6국05-03]",
        "student_goal": "1~11차시 읽기에서 모은 씨앗을 바탕으로 일상 속 시적 대상(원관념)을 재발견하고, 주제를 효과적으로 드러낼 시적 화자(페르소나)와 어조, 예상 독자를 설정하여 시 창작 설계서를 작성할 수 있다.",
        "marking_items": [
            ["mk-person", "동그라미", "내가 선택한 시적 대상과 설정한 화자(페르소나)"],
            ["mk-highlight", "형광펜", "대상을 통해 전하고 싶은 핵심 주제와 성찰"],
            ["mk-line-blue", "파란 밑줄", "예상 독자에게 줄 위로·울림과 어울리는 어조"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.9pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px;">
              <div style="font-size:7.6pt; font-weight:800; color:#6C3483; margin-bottom:3px;">🌱 [1~11차시 읽기 씨앗 총소환 아카이브] 우리가 읽은 시인들은 어떻게 시를 계획했을까?</div>
              <table class="std-table" style="font-size:7.2pt;">
                <thead>
                  <tr>
                    <th style="width:22%;">읽기 모델 작품</th>
                    <th style="width:26%;">재발견한 시적 대상</th>
                    <th style="width:26%;">화자 설정 및 어조</th>
                    <th style="width:26%;">구현한 주제 의식</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>〈구부러진 길〉</strong> (1~4차시)</td>
                    <td>시골의 구불구불한 길 ➔ 어머니·이웃의 주름살</td>
                    <td>‘나’ / 다정하고 예찬적인 고백 어조 (‘~이 좋다’)</td>
                    <td>가족과 이웃을 품고 정직하게 살아온 삶의 아름다움</td>
                  </tr>
                  <tr>
                    <td><strong>〈봄길〉</strong> (5~7차시)</td>
                    <td>막다른 길 ➔ 스스로 봄길이 되는 사람</td>
                    <td>숨은 관찰자 / 단정적 확신과 환기 어조 (‘~있다, 보라’)</td>
                    <td>절망 끝에서도 타인을 위해 헌신하는 사랑의 위대함</td>
                  </tr>
                  <tr>
                    <td><strong>〈담쟁이〉·〈새로운 길〉</strong> (8~10차시)</td>
                    <td>벽을 오르는 담쟁이 / 시내와 고개 너머의 길</td>
                    <td>‘우리·나’ / 의지적이고 힘찬 어조 (‘~오른다, ~갈’)</td>
                    <td>시련의 벽을 넘는 끈기 있는 전진과 함께 손잡는 연대</td>
                  </tr>
                  <tr>
                    <td><strong>〈우리가 눈발이라면〉</strong> (11차시)</td>
                    <td>진눈깨비 vs 따뜻한 함박눈·편지·새 살</td>
                    <td>‘우리’ / 따뜻한 권유·다짐의 청유형 어조 (‘~되자’)</td>
                    <td>소외되고 상처 입은 이웃에게 위로와 치유를 건네는 삶</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- 시 창작 기획 코칭 스튜디오 -->
            <div class="inline-segment-box" style="background:#FFFDF9; border-color:#F5B041; margin-bottom:4px;">
              <div style="font-family:var(--font-sans); font-size:7.4pt; font-weight:800; color:#D35400; margin-bottom:3px;">🎨 [시 창작 기획 스튜디오] 평범한 일상 사물에서 ‘보물 같은 삶의 의미’ 건져 올리기</div>
              <div style="font-size:7.4pt; line-height:1.45; font-family:var(--font-sans);">
                • <strong>글감 후보 1 [흙 묻은 운동화]</strong>: 밑창이 다 닳도록 내 발을 지켜 준 운동화 ➔ 실패해도 다시 뛰게 해 주는 친구·부모님의 응원<br>
                • <strong>글감 후보 2 [몽당 지우개]</strong>: 네모난 몸이 둥글게 닳아 작아진 지우개 ➔ 남의 실수를 지워 주느라 자신을 희생하는 따뜻한 용서<br>
                • <strong>글감 후보 3 [골목길 가로등]</strong>: 밤새 고개를 숙인 채 깜깜한 길을 비추는 가로등 ➔ 늦은 밤 가족의 귀가를 묵묵히 기다리는 사랑
              </div>
            </div>

            <div class="inline-bridge-box model" style="background:#F6F0F9; border-color:#C39BD3; border-left-color:#6C3483; margin-bottom:0;">
              <div style="font-weight:800; color:#6C3483;">🎙️ 기획 사고구술<br><span class="role-chip">시범 I Do</span></div>
              <div>“선생님은 필통 속 <strong>‘몽당 지우개’</strong>를 시적 대상으로 골랐어. 지우개가 까만 연필 자국을 지우며 제 몸이 닳아 가는 모습이 꼭 우리들의 실수를 감싸 주시는 부모님이나 친구 같거든! 화자는 <strong>‘나’</strong>로 설정하고, 지우개에게 고마움을 전하는 <strong>따뜻하고 성찰적인 어조(‘~한다, ~되자’)</strong>로 써서 친구들에게 ‘용서와 배려’의 울림을 주고 싶어!”</div>
            </div>
        """,
        "activity_1": {
            "title": "내 주변의 시적 대상(글감) 탐색 및 새로운 가치 발견하기",
            "tag": "Step 1 성찰적 경험·대상 탐색 (W1)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:22%;">탐색 영역</th>
                      <th style="width:36%;">내가 발견한 일상 사물·자연물 후보</th>
                      <th style="width:42%;">그 대상에서 발견한 삶의 모습이나 따뜻한 가치</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 교실·내 방 사물</strong></td>
                      <td>예: 몽당 지우개, 낡은 운동화, <span class="blank-slot"><span class="t-ans">우산 (또는 연필깎이)</span></span></td>
                      <td>제 몸은 젖거나 닳아 가면서도 다른 사람을 지켜 주고 실수를 감싸 안아 주는 헌신</td>
                    </tr>
                    <tr>
                      <td><strong>② 등굣길·마을 풍경</strong></td>
                      <td>예: 골목길 가로등, 아파트 계단, <span class="blank-slot"><span class="t-ans">보도블록 틈 민들레</span></span></td>
                      <td>아무도 알아주지 않는 자리에서도 묵묵히 길을 밝히거나 시련을 딛고 피어나는 생명력</td>
                    </tr>
                    <tr>
                      <td><strong>★ 나의 최종 선택</strong></td>
                      <td colspan="2">내가 시로 가장 쓰고 싶은 중심 대상(원관념/소재): <strong><span class="blank-slot"><span class="t-ans">비 오는 날 함께 쓰는 우산 (또는 몽당 지우개)</span></span></strong></td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]에서 고른 시적 대상에 어울리는 화자(페르소나)·거리·어조와 예상 독자 설정하기",
        "activity_2": {
            "title": "화자(Persona)·어조·독자·주제 일관성 검증 매트릭스",
            "tag": "Step 2 화자 페르소나·어조 설정 (W1 + V2-3·V2-4 전이)",
            "body_html": """
                <div class="inference-row">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">🗣️ [시적 화자(페르소나) &amp; 거리]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 화자: <span class="blank-slot"><span class="t-ans">‘나’ 또는 ‘우리’</span></span><br>
                      • 대상과의 거리: 대상을 가까이서 다정하게 바라보며 삶을 되돌아보는 친밀한 거리
                    </div>
                  </div>
                  <div class="inf-symbol">+</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">🎵 [화자의 목소리(어조) 선택]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 선택한 어조: <span class="blank-slot"><span class="t-ans">따뜻한 고백·다짐의 어조</span></span><br>
                      • 종결 표현 예: ‘~좋다’, ‘~있다’, ‘~되자’ 중 주제의 정서와 어울리는 말투
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#6C3483;">🎯 [예상 독자 &amp; 창작 목적]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 예상 독자: <span class="blank-slot"><span class="t-ans">우리 반 친구들과 가족</span></span><br>
                      • 전달할 울림: 작은 배려와 헌신이 세상을 따뜻하게 만든다는 공감과 위로 전달
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 1·2]의 기획 요소를 하나로 통합하여 나만의 '시 창작 마스터 설계서' 확정하기",
        "activity_3": {
            "title": "나만의 시 창작 마스터 설계서 완성하기",
            "tag": "Step 3 시 창작 설계도 수립 (W1)",
            "body_html": """
                <div style="font-size:7.3pt; margin-bottom:3px;"><strong>[조건]</strong> <code>[시적 대상 + 화자 설정 및 어조 + 중심 주제 및 성찰 + 예상 독자 효과]</code>의 4요소를 갖추어 나의 시 창작 계획을 완성하세요.</div>
                <div style="background:#F8F9F9; border:0.8pt solid #BDC3C7; border-radius:4px; padding:5px 8px; font-size:7.5pt; line-height:1.58;">
                  • <strong>가제(임시 제목)</strong>: <span class="blank-slot"><span class="t-ans">〈한쪽 어깨가 젖은 우산〉 (또는 〈둥글어진 지우개의 마음〉)</span></span><br>
                  • <strong>창작 기획서 요약</strong>: 나는 <span class="blank-slot"><span class="t-ans">비 오는 날 친구와 함께 썼던 우산</span></span>을 시적 대상으로 삼아, 화자인 <span class="blank-slot"><span class="t-ans">‘나(우리)’</span></span>가 <span class="blank-slot"><span class="t-ans">따뜻하고 다정한 다짐의 어조(‘~되자’)</span></span>로 노래할 것이다. 이를 통해 독자인 <span class="blank-slot"><span class="t-ans">반 친구들</span></span>에게 ‘내 어깨가 조금 젖더라도 친구의 비를 막아 주는 배려와 연대의 아름다움’이라는 주제를 감동적으로 전하고 싶다.
                </div>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 13차시(W2 내용 생성) 오감 심상·복합 시어·비유 생성으로 직결",
            "prompt": "방금 확정할 시적 대상(예: 우산, 지우개, 운동화, 가로등)의 생김새, 소리, 촉감을 떠올리며 다음 시간에 쓸 핵심 단어 3개를 미리 메모해 두세요.",
            "placeholder": "예: 토독토독(빗소리), 젖은 어깨, 푸른 지붕",
            "example_answer": "토독토독(청각), 차가운 빗방울(촉각), 두 사람을 품은 작은 지붕(은유)"
        },
        "self_check": [
            "선택한 일상 대상이 내가 전하고 싶은 추상적 주제(사랑·배려·연대·성찰)를 나타내기에 적합한가요?",
            "설정한 시적 화자(페르소나)의 어조가 시의 전체 정서 및 주제와 일관되나요?",
            "시적 대상, 화자·어조, 중심 주제, 예상 독자 효과를 모두 갖추어 시 창작 설계서를 완성했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[시 창작 기획 4대 기둥] ① 무엇을(시적 대상 재발견: 낡은 사물·자연물) + ② 누가 어떤 목소리로(화자 페르소나 & 어조: '~좋다 / ~있다 / ~되자') + ③ 왜(중심 주제·성찰) + ④ 누구에게(예상 독자와 기대 효과)",
            "intro_5min": "1~11차시 동안 차곡차곡 모은 ‘내 글 씨앗 보관함’을 펼쳐 보게 한다. 이준관, 정호승, 윤동주, 도종환, 안도현 시인처럼 이제 우리도 평범한 사물에서 빛나는 의미를 찾아 시인이 되어 보는 첫 단계(계획하기)임을 안내한다.",
            "ido_think_aloud_script": "“시를 쓰려고 연필을 들었을 때 ‘무엇을 쓰지?’ 하고 막막할 때가 있죠. 그때는 내 책상 위나 신발장을 가만히 들여다보세요. 선생님은 닳아서 작아진 ‘몽당 지우개’를 골랐어요. 왜냐하면 처음엔 네모나고 각졌던 지우개가 친구의 틀린 글씨를 지워 주면서 자기 몸은 깎이고 둥글어졌거든요. 이 모습을 ‘실수를 감싸 주는 따뜻한 용서’라는 주제와 연결하면 훌륭한 시가 될 수 있겠죠!”",
            "wedo_qa_list": [
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "만약 ‘비 오는 날 친구와 함께 쓰는 우산’을 주제로 시를 쓴다면, 장난스럽고 웃긴 어조와 다정하고 따뜻한 어조 중 어떤 목소리가 주제와 더 잘 어울릴까요?",
                    "expected_ans": "친구를 배려해 우산을 기울여 주는 따뜻한 마음을 전해야 하므로, 다정하고 포근한 어조나 ‘~되자’ 같은 청유형 어조가 더 잘 어울려요.",
                    "reprompt": "시에서 전달하려는 중심 감정(배려, 고마움)과 말하는 이의 목소리 톤(어조)이 서로 어울려야 독자가 감동을 받을 수 있어요."
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "여러분이 고른 사물(운동화, 가로등, 지우개, 자전거 등)은 누구를 닮았나요? 그 사물에서 어떤 삶의 가치를 발견했나요?",
                    "expected_ans": "저는 ‘현관문 앞 신발장’을 골랐어요. 온 가족의 지친 신발들을 매일 저녁 말없이 품어 주는 모습이 우리 할머니의 품을 닮았어요.",
                    "reprompt": "1~4차시에 읽은 〈구부러진 길〉에서 시인이 길과 사람의 주름살을 연결했던 것처럼, 사물의 특징과 사람의 마음을 이어 보세요."
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]에서 글감 후보를 탐색하여 최종 대상을 고르고, [활동 2]에서 화자·어조·독자 일관성을 점검한 뒤 [활동 3] 시 창작 마스터 설계서를 완성하도록 지도한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [활동 1 모범 답안]</strong> 일상 사물·자연물(우산, 지우개, 운동화, 가로등, 민들레 등) 중 구체적 대상 1가지를 선정하고 그에 담긴 삶의 가치를 연결하면 정답 인정.<br>
                  <strong>• [활동 2 모범 답안]</strong> 화자(‘나’ 또는 ‘우리’), 주제 정서와 일관되는 어조(고백적·단정적·청유형 등), 예상 독자(친구·가족 등) 설정.<br>
                  <strong>• [활동 3 모범 답안]</strong> [시적 대상 + 화자·어조 + 중심 주제 + 예상 독자 효과] 4요소가 모두 구체적으로 기술되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "시적 대상 없이 ‘우정’, ‘평화’, ‘효도’처럼 추상적인 관념어만 주제로 적어 시가 웅변이나 표어처럼 계획되는 경우",
                    "diagnosis": "시는 추상적 주제를 ‘구체적 사물(객관적 상관물·보조관념)’을 통해 형상화하는 갈래임을 간과함.",
                    "prescription": "‘우정’이라는 추상어 대신 우정을 보여 줄 수 있는 구체적 사물(‘함께 쓴 우산’, ‘짝꿍과 나눈 지우개’)을 반드시 먼저 선정하도록 코칭한다."
                },
                {
                    "error_case": "선택한 주제(예: 부모님의 헌신에 대한 감사)와 설정한 어조(예: 공격적이거나 차가운 명령조)가 서로 어울리지 않는 경우",
                    "diagnosis": "화자의 어조(Tone)와 주제의 정서적 일관성 기준을 고려하지 못함.",
                    "prescription": "[활동 2]에서 주제의 감정 색깔과 어조의 말투가 서로 조화를 이루는지 소리 내어 확인하게 한다."
                }
            ],
            "scaffolding_down": "글감 선정이 어려운 학생을 위해 ‘교실 사물 베스트 5(지우개, 분필/보드마카, 시계, 걸레, 창문)’ 사진과 특징 힌트 카드를 제공하여 하나를 고르게 한다.",
            "scaffolding_up": "사물 자체를 화자(의인화된 페르소나: 예컨대 내가 ‘낡은 운동화’ 자신이 되어 주인에게 말을 거는 시점)로 설정하는 창의적인 시점 전환 기획도 시도해 보게 한다.",
            "rubric": {
                "high": "추상적 주제를 형상화하기에 적합한 구체적 시적 대상을 선정하고, 화자의 페르소나·어조·중심 주제·예상 독자 효과의 4요소가 완벽히 일관된 시 창작 설계서를 수립함.",
                "mid": "시적 대상과 주제는 설정했으나 화자의 어조나 예상 독자 효과에 대한 설정이 다소 일반적임.",
                "low": "구체적 시적 대상 없이 추상적인 다짐만 적거나 설계서의 필수 요소가 누락됨."
            }
        }
    },

    # =========================================================================
    # 13차시: G6-POE-W2 내용 생성하기 (글감·감각/비유·사실/근거 자료 수집)
    # =========================================================================
    {
        "lesson_title": "[시 쓰기 ② 생성하기] 오감 심상 팔레트와 복합 시어·비유 브릿지 만들기",
        "std_badge": "[6국04-02] [6국05-01]",
        "student_goal": "12차시에 계획한 시적 대상에서 다각적인 오감·공감각 심상을 추출하고, 형태소 결합 원리를 활용한 복합 시어(합성어·파생어) 3개 이상과 참신한 비유·상징 표현 3개 이상을 생성할 수 있다.",
        "marking_items": [
            ["mk-highlight", "형광펜", "시각·청각·촉각·후각 등 생생한 감각적 심상 어휘"],
            ["mk-line-blue", "파란 밑줄", "어근+어근(합성어), 어근+접사(파생어)로 만든 복합 시어"],
            ["mk-line-red", "빨간 밑줄", "공통 속성을 바탕으로 연결한 참신한 직유·은유·의인 표현"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.9pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px;">
              <div style="font-size:7.6pt; font-weight:800; color:#6C3483; margin-bottom:3px;">🎨 [시어·비유 생성 워크숍] 상투적인 표현을 넘어 참신한 시어 빚어내기</div>
              <table class="std-table" style="font-size:7.2pt;">
                <thead>
                  <tr>
                    <th style="width:20%;">생성 전략</th>
                    <th style="width:36%;">❌ 흔하고 상투적인 표현 (피할 것)</th>
                    <th style="width:44%;">⭕ 참신하게 생성한 시적 표현 (읽기 모델 원리 적용)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>① 오감·공감각 심상</strong><br>(V1-1 원리)</td>
                    <td>• 비가 많이 내린다.<br>• 지우개가 작아졌다.</td>
                    <td>• 차가운 빗방울이 우산 지붕을 <span class="mk-highlight">토독토독</span> 두드린다. (청각·촉각)<br>• 까만 실수를 지우며 <span class="mk-highlight">하얀 눈가루</span>를 털어 내는 지우개 (시각)</td>
                  </tr>
                  <tr>
                    <td><strong>② 복합 시어 조어</strong><br>(COM-A1 원리)</td>
                    <td>• 먼지가 많은 신발<br>• 비가 오는 길</td>
                    <td>• <span class="mk-line-blue">흙먼지투성이</span>(파생어)가 된 <span class="mk-line-blue">발걸음</span>(합성어)<br>• <span class="mk-line-blue">빗물방울</span>(합성어) 맺힌 <span class="mk-line-blue">어깨너머</span>(합성어)</td>
                  </tr>
                  <tr>
                    <td><strong>③ 확장 은유·의인</strong><br>(V1-2·V2-1 원리)</td>
                    <td>• 호수처럼 맑은 눈<br>• 천사처럼 착한 친구</td>
                    <td>• <span class="mk-line-red">두 사람을 품어 주는 둥근 하늘 같은 우산</span> (직유·의인)<br>• <span class="mk-line-red">친구의 아픈 실수 위에 새 종이를 깔아 주는 지우개</span> (은유)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- 비유 브릿지(원관념 ⟷ 공통 속성 ⟷ 보조관념) 모델 -->
            <div class="inline-segment-box" style="background:#FFFDF9; border-color:#F5B041; margin-bottom:4px; font-family:var(--font-sans);">
              <div style="font-size:7.4pt; font-weight:800; color:#D35400; margin-bottom:2px;">🌉 [비유 브릿지 3단계 공식] 원관념과 보조관념 사이에 ‘참신한 공통점 다리’ 놓기</div>
              <div style="font-size:7.3pt; line-height:1.45;">
                1단계 <strong>[원관념 관찰]</strong>: 비 오는 날 친구 쪽으로 기울어진 우산 (또는 닳아빠진 몽당 지우개)<br>
                2단계 <strong>[핵심 공통 속성 추출]</strong>: 자기 한쪽은 비에 젖으면서도(희생) 옆 사람의 머리 위에 마른 길을 만들어 줌(보호·사랑)<br>
                3단계 <strong>[보조관념 결합 문장화]</strong>: “우산은 <strong>젖은 어깨로 친구의 머리 위에 띄워 놓은 작은 봄하늘</strong>이다.”
              </div>
            </div>

            <div class="inline-bridge-box practice" style="margin-bottom:0;">
              <div style="font-weight:800; color:#2874A6;">🙋 상투적 비유 판별<br><span class="role-chip">함께 We Do</span></div>
              <div>
                “그 친구는 천사처럼 착하다.”보다 “그 친구는 내 구겨진 마음을 펴 주는 따뜻한 다리미 같다.”가 더 좋은 시적 비유인 까닭은 무엇일까요?<br>
                <span class="pencil-line">✏️ 판별 이유: <span class="t-ans">‘천사처럼’은 누구나 쓰는 상투적 비유이지만, ‘구겨진 마음을 펴 주는 따뜻한 다리미’는 구체적인 사물의 공통 속성을 참신하게 연결했기 때문이다.</span></span>
              </div>
            </div>
        """,
        "activity_1": {
            "title": "내 시적 대상의 오감·공감각 심상 팔레트 채우기",
            "tag": "Step 1 다각적 감각 심상 추출 (W2 + V1-1)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:22%;">감각 종류</th>
                      <th style="width:38%;">대상에서 관찰·상상한 모습과 특징</th>
                      <th style="width:40%;">생생한 감각 시어·의성어·의태어 표현</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>👁️ 시각 (모양·색깔)</strong></td>
                      <td>대상의 겉모습, 색채 대비, 움직이는 모양</td>
                      <td><span class="blank-slot"><span class="t-ans">활짝 펴진 파란 지붕, 비스듬히 기울어진 모습 (또는 네모난 모서리가 둥글어진 모습)</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>👂 청각 (소리)</strong></td>
                      <td>대상이 내는 소리나 주변에서 들리는 소리</td>
                      <td><span class="blank-slot"><span class="t-ans">토독토독 빗방울이 노크하는 소리 (또는 사각사각 연필 자국 지우는 소리)</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>✋ 촉각·기타 (온도·질감)</strong></td>
                      <td>손끝에 닿는 느낌, 차갑거나 따뜻한 온도 대비</td>
                      <td><span class="blank-slot"><span class="t-ans">축축하고 차가운 빗물 vs 맞닿은 어깨의 따뜻한 온기</span></span></td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 감각 재료에 형태소 결합 원리(합성어·파생어)를 적용하여 정밀한 복합 시어 만들기",
        "activity_2": {
            "title": "형태소 결합 원리(어근+어근, 어근+접사)를 활용한 복합 시어 3개 이상 만들기",
            "tag": "Step 2 복합 시어 조어 (W2 + COM-A1)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:22%;">조어 방식</th>
                      <th style="width:36%;">형태소 결합 과정 ([어근] + [어근/접사])</th>
                      <th style="width:42%;">완성한 복합 시어와 시 속 활용 구절</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 합성어 1<br>(어근 + 어근)</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">비(어근) + 바람(어근)</span></span> (또는 <span class="blank-slot"><span class="t-ans">발+걸음</span></span>)</td>
                      <td>• 시어: <strong><span class="blank-slot"><span class="t-ans">비바람 (발걸음)</span></span></strong><br>• 구절: 세찬 비바람 속에서도 나란히 맞추어 걷는 발걸음</td>
                    </tr>
                    <tr>
                      <td><strong>② 합성어 2<br>(어근 + 어근)</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">손(어근) + 잡다(어근)</span></span> (또는 <span class="blank-slot"><span class="t-ans">마음+길</span></span>)</td>
                      <td>• 시어: <strong><span class="blank-slot"><span class="t-ans">손잡고 (마음길)</span></span></strong><br>• 구절: 우산 손잡이를 꼭 손잡고 걸어가는 따뜻한 마음길</td>
                    </tr>
                    <tr>
                      <td><strong>③ 파생어<br>(어근 + 접사)</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">물기(어근) + -투성이(접사)</span></span> (또는 <span class="blank-slot"><span class="t-ans">새-(접사)+하얀</span></span>)</td>
                      <td>• 시어: <strong><span class="blank-slot"><span class="t-ans">물기투성이 (새하얀)</span></span></strong><br>• 구절: 내 한쪽 어깨가 물기투성이가 되어도 좋은 날</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_2_to_3": "[활동 1·2]의 시어들을 '비유 브릿지(원관념⟷공통점⟷보조관념)'로 연결하여 참신한 비유·상징 3개 산출하기",
        "activity_3": {
            "title": "원관념-보조관념 비유 브릿지를 통한 확장 은유·의인·역설 표현 3개 생성하기",
            "tag": "Step 3 참신한 비유·상징 산출 (W2 + V1-2·V2-1)",
            "body_html": """
                <div style="font-size:7.3pt; margin-bottom:3px;"><strong>[조건]</strong> 상투적 비유를 피하고, 원관념과 보조관념의 <strong>공통 속성</strong>이 잘 드러나는 직유·은유·의인·역설 표현을 3개 이상 만드세요.</div>
                <span class="pencil-line">✏️ 비유·상징 표현 1 (직유/은유): <span class="t-ans">[원관념: 기울어진 우산 ⟷ 보조관념: 작은 지붕/봄하늘] 친구 쪽으로 기울어진 우산은 비 오는 날 머리 위에 띄운 작은 봄하늘이다.</span></span>
                <span class="pencil-line">✏️ 비유·상징 표현 2 (의인화): <span class="t-ans">[의인법] 우산은 세찬 빗방울을 온몸으로 받아 내며 두 친구의 어깨를 다정하게 안아 준다.</span></span>
                <span class="pencil-line">✏️ 비유·상징 표현 3 (역설/대조): <span class="t-ans">[역설적 감각] 내 한쪽 어깨는 차가운 비에 젖어 가지만, 우산 속 우리 마음은 햇살처럼 가장 따뜻하다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 14차시(W3 내용 조직) 연별 시상 전개 배치 재료로 직결",
            "prompt": "오늘 만든 감각 시어, 복합 시어, 비유 표현 중 내 시의 ‘가장 빛나는 핵심 구절(하이라이트 행)’로 쓰고 싶은 문장 하나를 별표(★)와 함께 적어 두세요.",
            "placeholder": "예: ★ 내 한쪽 어깨가 젖는 만큼 친구의 마음에는 뽀송한 봄길이 열린다.",
            "example_answer": "★ 내 한쪽 어깨가 차갑게 젖는 만큼, 친구의 발걸음에는 뽀송하고 따뜻한 봄길이 열린다."
        },
        "self_check": [
            "시각·청각·촉각 등 2가지 이상의 감각적 심상을 구체적으로 추출했나요?",
            "어근+어근(합성어)과 어근+접사(파생어) 원리를 활용해 복합 시어를 3개 이상 만들었나요?",
            "상투적 비유를 배제하고 원관념-보조관념의 공통 속성이 참신한 비유·상징 표현을 3개 이상 생성했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[시어 생성 3대 팔레트] ① 오감·공감각 심상(시각+청각+촉각 온도 대비) + ② 형태소 조어소(합성어: 비+바람, 발+걸음 / 파생어: 물기+-투성이, 새-+하얀) + ③ 비유 브릿지(원관념 ──[참신한 공통 속성]──> 보조관념: 직유·은유·의인·역설)",
            "intro_5min": "요리사가 최고의 요리를 만들려면 신선하고 특별한 재료가 필요하듯, 시인에게는 ‘참신한 시어와 비유’가 요리 재료임을 안내한다. ‘천사 같은, 보석 같은’처럼 이미 굳어진 상투적 비유를 깨뜨리는 워밍업 퀴즈를 진행한다.",
            "ido_think_aloud_script": "“선생님이 ‘비 오는 날 친구와 함께 쓰는 우산’이라는 대상으로 비유 브릿지를 만들어 볼게요. 우산(원관념)의 특징은 머리 위에서 비를 막아 주는 거죠? 여기에 ‘작은 봄하늘’이나 ‘걸어가는 초록 지붕’(보조관념)을 연결해 볼까요? 더 나아가 우산을 친구 쪽으로 기울이면 내 한쪽 어깨는 차갑게 젖지만 마음은 따뜻해지죠! 이걸 5차시 〈봄길〉과 11차시 〈우리가 눈발이라면〉에서 배운 역설적 표현으로 바꾸면 ‘내 어깨는 차갑게 젖어도 우리 마음은 가장 따뜻하다’라는 멋진 시행이 탄생합니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "1차시 〈구부러진 길〉에서 배운 파생어 ‘흙투성이’처럼, 접미사 ‘-투성이’나 접두사 ‘새-’, ‘맨-’을 붙여서 내 시에 쓸 파생어를 만들어 볼까요?",
                    "expected_ans": "운동화 시에는 ‘상처투성이, 먼지투성이, 맨발’을 쓸 수 있고, 지우개 시에는 ‘연필자국투성이, 새하얀’을 쓸 수 있어요.",
                    "reprompt": "어근 앞이나 뒤에 붙어 뜻을 더 선명하게 해 주는 접사(‘새-, 시-, 맨-, 풋-’ / ‘-투성이, -꾼, -질’)를 떠올려 보세요."
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "내가 고른 사물이 만약 사람처럼 행동한다면(의인법), 어떤 동작을 하고 있을까요?",
                    "expected_ans": "가로등은 밤새 졸음을 참으며 골목길을 지켜보고 있고, 낡은 운동화는 내 발을 꽉 껴안으며 넘어지지 않게 땅을 버티고 있어요.",
                    "reprompt": "2차시에서 ‘산을 품고 마을을 품고’나 9차시에서 ‘여럿이 함께 손을 잡고 올라간다’처럼 사물에게 사람의 따뜻한 행동을 선물해 보세요."
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1] 오감 팔레트, [활동 2] 복합 시어 3개, [활동 3] 비유·상징 3개를 차례대로 생성하도록 순회 지도한다. 생성한 표현 중 상투적인 표현이 있으면 구체적 감각과 공통 속성을 찾도록 피드백한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 브릿지 질문 정답]</strong> ‘천사처럼’은 누구나 쓰는 상투적 비유이지만, ‘구겨진 마음을 펴 주는 따뜻한 다리미’는 구체적인 사물의 공통 속성을 참신하게 연결했기 때문이다.<br>
                  <strong>• [활동 1 모범 답안]</strong> 자신이 선택한 대상의 시각·청각·촉각 심상이 구체적 의성어·의태어·감각어로 작성되면 정답 인정.<br>
                  <strong>• [활동 2 모범 답안]</strong> 합성어(어근+어근) 2개 이상 + 파생어(어근+접사) 1개 이상 총 3개 이상의 복합 시어 산출.<br>
                  <strong>• [활동 3 모범 답안]</strong> 원관념-보조관념의 공통 속성에 기반한 직유·은유·의인·역설 표현 3개 이상 산출 시 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "합성어·파생어를 만들 때 단순히 조사가 붙은 어절(예: ‘우산을’, ‘지우개가’)을 파생어로 착각하여 적는 경우",
                    "diagnosis": "새로운 단어를 만드는 파생 접사(예: -투성이, 새-)와 문장 성분의 관계만 나타내는 굴절 조사(은/는/이/가/을/를)를 혼동함.",
                    "prescription": "조사는 단어를 새로 만드는 것이 아니라 단어 뒤에 잠시 붙는 꼬리표임을 설명하고, 사전에 한 단어로 실리거나 새로운 뜻을 더하는 어근+어근/어근+접사 결합을 안내한다."
                },
                {
                    "error_case": "원관념과 보조관념 사이에 공통점이 전혀 없는 억지 비유(예: ‘우산은 축구공처럼 둥글게 나를 지켜 준다’)를 만드는 경우",
                    "diagnosis": "비유의 핵심 준거인 ‘의미적·기능적 공통 속성(유추)’을 확인하지 않고 아무 사물이나 결합함.",
                    "prescription": "비유 브릿지의 가운데 칸인 ‘공통 속성(왜 그 사물에 빗대었는가?)’을 먼저 말로 설명해 보게 하여 주제를 뒷받침하는 보조관념으로 교체하게 한다."
                }
            ],
            "scaffolding_down": "어근·접사 조합 퍼즐 카드(예: [빗물/발/어깨/마음/흙먼지] + [길/걸음/동무/-투성이])와 비유 연결어 카드(‘~처럼 품어 주는’, ‘스스로 ~이 되어’)를 제공하여 조합을 돕는다.",
            "scaffolding_up": "하나의 감각을 다른 감각으로 옮겨 표현하는 ‘공감각적 심상’(예: ‘토독토독 동그랗게 피어나는 빗소리’, ‘노란 웃음소리’)을 1개 이상 창작해 보게 한다.",
            "rubric": {
                "high": "복수의 감각 심상과 형태소 결합 원리를 활용한 복합 시어 3개 이상, 원관념-보조관념의 공통 속성이 참신한 확장 은유·의인·역설 표현 3개 이상을 완벽히 산출함.",
                "mid": "감각 심상과 복합 시어, 비유 표현을 생성했으나 일부 비유가 다소 상투적이거나 복합어 형태소 분석이 부정확함.",
                "low": "단순한 일상어 나열에 그치며 복합 시어나 비유 표현을 1개 이하로만 작성함."
            }
        }
    },

    # =========================================================================
    # 14차시: G6-POE-W3 내용 조직하기 (읽기 구조 미러링 개요·도해 설계)
    # =========================================================================
    {
        "lesson_title": "[시 쓰기 ③ 조직하기] 읽기 모델의 시상 구조를 미러링하여 4연 설계도 짜기",
        "std_badge": "[6국03-02] [6국05-02]",
        "student_goal": "13차시에서 생성한 시어와 비유 재료들을 의미 군집별로 묶고, 읽기 모델(〈구부러진 길〉·〈봄길〉·〈새로운 길〉)의 시상 전개 구조를 미러링하여 3~4연의 시상 전개 설계도를 작성할 수 있다.",
        "marking_items": [
            ["mk-person", "동그라미", "각 연의 중심 이미지와 소재 배치"],
            ["mk-bg", "네모", "시상을 전환하거나 심화시키는 3연(전·轉)의 전환 표지"],
            ["mk-double", "두줄 밑줄", "1연과 마지막 연을 맞물리게 하는 수미상관·반복 운율 계획"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.9pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px;">
              <div style="font-size:7.6pt; font-weight:800; color:#6C3483; margin-bottom:3px;">📐 [읽기 ➔ 쓰기 구조 미러링 스튜디오] 명작 시의 뼈대를 내 시의 설계도로!</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:7.2pt; line-height:1.4;">
                <div style="background:#FFFFFF; border:0.8pt solid #C39BD3; border-radius:4px; padding:4px 6px;">
                  <strong style="color:#6C3483;">🏛️ 모델 A: [자연/사물 관찰 ➔ 인간 삶으로 확장형]</strong><br>
                  <span style="color:#566573;">(미러링 원본: 3차시 이준관 〈구부러진 길〉)</span><br>
                  • <strong>1연(기)</strong>: 내가 좋아하는 사물의 모습과 첫인상 제시<br>
                  • <strong>2연(승)</strong>: 사물이 겪는 일과 주변을 품어 주는 특징 확대<br>
                  • <strong>3연(전)</strong>: <code>‘그 [사물]처럼 살아가는 [사람]’</code>으로 시상 전환<br>
                  • <strong>4연(결)</strong>: 1연과 호응(변주된 수미상관)하며 주제·다짐 완결
                </div>
                <div style="background:#FFFFFF; border:0.8pt solid #82E0AA; border-radius:4px; padding:4px 6px;">
                  <strong style="color:#196F3D;">🏛️ 모델 B: [시련/대조 제시 ➔ 스스로 희망 되기형]</strong><br>
                  <span style="color:#566573;">(미러링 원본: 6차시 〈봄길〉 &amp; 11차시 〈우리가 눈발이라면〉)</span><br>
                  • <strong>1연(기)</strong>: 힘들거나 차가운 상황 및 부정적 모습 지양<br>
                  • <strong>2연(승)</strong>: 시련 속에서도 묵묵히 견디는 사물의 모습 묘사<br>
                  • <strong>3연(전)</strong>: <code>‘보라 / 만약 우리가 [사물]이라면’</code> 인식 전환<br>
                  • <strong>4연(결)</strong>: 스스로 따뜻한 위로(은유)가 되자는 다짐으로 완결
                </div>
              </div>
            </div>

            <!-- 모범 시상 조직 설계도 예시 -->
            <div class="inline-segment-box" style="background:#FFFDF9; border-color:#F5B041; margin-bottom:4px; font-family:var(--font-sans);">
              <div style="font-size:7.4pt; font-weight:800; color:#D35400; margin-bottom:2px;">📋 [학생 모범 시상 조직도 예시] 〈한쪽 어깨가 젖은 우산〉 (모델 A+B 결합 4연 구성)</div>
              <div style="font-size:7.2pt; line-height:1.45;">
                • <strong>1연 [기 · 외적 풍경 제시]</strong>: 비 내리는 하굣길, 친구와 머리 맞대고 펼치는 작은 우산 (수미상관 첫 행: <em>“나는 비스듬히 기울어진 우산이 좋다.”</em>)<br>
                • <strong>2연 [승 · 감각·비유 심화]</strong>: 토독토독 차가운 빗방울을 온몸으로 막아 주며 두 사람의 발걸음을 품고 가는 푸른 지붕<br>
                • <strong>3연 [전 · 시상 전환(삶으로 확장)]</strong>: <span class="mk-bg">“그 우산처럼 걸어가는 사람이 나는 또한 좋다.”</span> — 내 한쪽 어깨가 물기투성이로 젖어도 친구의 어깨를 먼저 감싸 주는 마음<br>
                • <strong>4연 [결 · 주제 완결(수미상관)]</strong>: 비바람 부는 날 누군가의 머리 위에 따뜻한 봄하늘을 띄우는 <span class="mk-double">“비스듬히 기울어진 우산 같은 사람이 좋다.”</span>
              </div>
            </div>

            <div class="inline-bridge-box practice" style="margin-bottom:0;">
              <div style="font-weight:800; color:#2874A6;">🙋 3연(전·轉)의 역할<br><span class="role-chip">함께 We Do</span></div>
              <div>
                4연으로 시를 조직할 때, 왜 <strong>3연(전·轉)</strong>에서 시상의 전환이나 확장이 일어나는 것이 중요할까요?<br>
                <span class="pencil-line">✏️ 중요성: <span class="t-ans">1~2연에서 묘사한 구체적 사물의 특징을 3연에서 ‘사람의 삶과 마음’으로 전환해야 시의 주제가 깊어지고 감동이 고조되기 때문이다.</span></span>
              </div>
            </div>
        """,
        "activity_1": {
            "title": "13차시에 생성한 시어·비유 재료를 연별 의미 군집으로 분류하기",
            "tag": "Step 1 시적 재료 군집 분류 (W3)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:24%;">연별 의미 군집</th>
                      <th style="width:38%;">배치할 핵심 시어·감각어·복합어</th>
                      <th style="width:38%;">배치할 핵심 비유(직유·은유·의인·역설)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 사물의 첫인상과 풍경<br>(1~2연 배치용)</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">토독토독, 비바람, 발걸음, 활짝 펴진</span></span></td>
                      <td><span class="blank-slot"><span class="t-ans">두 사람을 품고 가는 작은 푸른 지붕 (의인·은유)</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>② 삶의 가치와 내면 성찰<br>(3~4연 배치용)</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">물기투성이, 손잡고, 젖은 어깨, 마음길</span></span></td>
                      <td><span class="blank-slot"><span class="t-ans">내 어깨는 차갑게 젖어도 마음은 따뜻한 봄하늘 (역설·은유)</span></span></td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]에서 분류한 재료들을 선택한 시상 전개 모델(기-승-전-결)에 배치하기",
        "activity_2": {
            "title": "나만의 4연 시상 전개 구조도(기-승-전-결) 및 정서 변화 설계하기",
            "tag": "Step 2 시상 전개 방식 배치 (W3 + V1-3 미러링)",
            "body_html": """
                <div class="inference-row" style="grid-template-columns:1fr 12px 1fr 12px 1fr 12px 1fr;">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">[1연: 기(起)]<br>대상 제시</strong>
                    <div style="margin-top:2px; font-size:7pt; line-height:1.38;">
                      • 중심 이미지: <span class="blank-slot"><span class="t-ans">비 오는 날 펼친 우산</span></span><br>
                      • 정서: 반가움, 다정함
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">[2연: 승(承)]<br>특징·행동 심화</strong>
                    <div style="margin-top:2px; font-size:7pt; line-height:1.38;">
                      • 중심 이미지: <span class="blank-slot"><span class="t-ans">비바람을 막고 품어 주는 우산</span></span><br>
                      • 정서: 든든함, 고마움
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#D35400;">[3연: 전(轉)]<br>시상 전환·확장</strong>
                    <div style="margin-top:2px; font-size:7pt; line-height:1.38;">
                      • 전환 표지: <span class="blank-slot"><span class="t-ans">그 우산처럼</span></span><br>
                      • 확장: <span class="blank-slot"><span class="t-ans">친구를 위해 어깨가 젖는 사람</span></span>
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3" style="border-top-color:#6C3483;">
                    <strong style="color:#6C3483;">[4연: 결(結)]<br>주제·여운 완결</strong>
                    <div style="margin-top:2px; font-size:7pt; line-height:1.38;">
                      • 마무리: <span class="blank-slot"><span class="t-ans">1연과 수미상관 호응</span></span><br>
                      • 정서: 따뜻한 다짐과 예찬
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 2]의 4연 구조도에 반복 운율(통사 구조 반복·수미상관)과 행 분할 계획을 더해 설계 완성하기",
        "activity_3": {
            "title": "운율 형성(수미상관·통사 반복) 및 의도적 행바꿈 설계표 완성하기",
            "tag": "Step 3 연·행 위계와 운율 설계 (W3)",
            "body_html": """
                <div style="font-size:7.3pt; margin-bottom:3px;"><strong>[조건]</strong> 내 시에 리듬감과 구조적 안정감을 줄 수 있도록 ① 수미상관(1연과 4연 호응), ② 반복할 문장 구조, ③ 호흡을 조절할 행바꿈(행간 걸침) 계획을 구체적으로 적으세요.</div>
                <span class="pencil-line">✏️ ① 수미상관 설계 (1연 첫 행 ↔ 4연 끝 행): <span class="t-ans">1연 첫 행 “나는 비스듬히 기울어진 우산이 좋다.” ↔ 4연 끝 행 “비스듬히 기울어진 우산 같은 사람이 좋다.”</span></span>
                <span class="pencil-line">✏️ ② 반복할 문장 구조 (내재율 형성): <span class="t-ans">‘~을 막아 주고 ~을 품어 주는’, ‘~가 젖어도 ~는 따뜻한’ 구절을 대칭으로 반복한다.</span></span>
                <span class="pencil-line">✏️ ③ 의도적 행바꿈·시상 전환 계획: <span class="t-ans">3연 첫 행에서 ‘그 우산처럼’으로 시상을 전환하고, 마지막 연에서 여운을 남기도록 3~4행으로 나누어 배열한다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 15차시(W4 초고 집필하기) 4연 시 원고 집필로 1:1 직결",
            "prompt": "설계한 4연 구조도 중 독자의 마음을 가장 뭉클하게 만들 ‘3연(전환 연)’의 첫 문장을 미리 써 보세요.",
            "placeholder": "예: 그 지우개처럼 조용히 자기를 깎아 내는 사람이 나는 또한 좋다.",
            "example_answer": "그 우산처럼 자기 한쪽 어깨가 젖는 줄도 모르고 걸어가는 사람이 나는 또한 좋다."
        },
        "self_check": [
            "13차시에 만든 시어와 비유들을 1~4연의 흐름에 맞게 체계적으로 분류했나요?",
            "기-승-전-결의 4연 구조 속에서 3연(전·轉)의 시상 전환과 의미 확장이 자연스럽게 설계되었나요?",
            "수미상관과 통사 구조 반복, 행 분할 계획을 구체적으로 세워 시의 리듬감을 준비했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[시상 조직 4단 아키텍처] 1연 기(사물 첫인상 제시 ★수미상관 시작) ➔ 2연 승(감각·비유로 사물 속성 확대) ➔ 3연 전(전환 표지 '그 ~처럼 / 만약 우리가 ~이라면'으로 인간 삶·가치로 확장) ➔ 4연 결(주제 응축 ★변주된 수미상관 마무리)",
            "intro_5min": "아무리 좋은 벽돌(시어·비유)이 많아도 설계도 없이 쌓으면 집이 무너지듯, 시에서도 감동을 차곡차곡 쌓아 올리는 ‘시상 전개 설계도(조직하기)’가 핵심임을 안내한다. 3차시 〈구부러진 길〉과 6차시 〈봄길〉의 구조도를 칠판에 소환한다.",
            "ido_think_aloud_script": "“선생님은 3차시에서 배운 이준관 시인의 〈구부러진 길〉 구조를 미러링해서 〈한쪽 어깨가 젖은 우산〉의 4연 설계도를 짜 보았어요. 1연에서는 비 오는 날 펼친 우산을 제시하고, 2연에서는 비바람을 막아 주는 우산의 고마운 행동을 깊게 묘사해요. 그리고 대망의 3연(전)! 여기서 ‘그 우산처럼 걸어가는 사람이 나는 또한 좋다’라는 전환 표지를 써서 사물 이야기를 ‘배려하는 사람의 이야기’로 확 넓혔어요. 마지막 4연에서는 1연 첫 줄과 호응하게 끝맺어 완벽한 균형을 잡았답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "모델 A(〈구부러진 길〉형)와 모델 B(〈봄길〉·〈우리가 눈발이라면〉형) 중 내 시적 대상과 주제를 표현하기에 어느 쪽이 더 효과적일까요?",
                    "expected_ans": "사물의 따뜻한 특징을 사람과 닮았다고 예찬할 때는 모델 A가 좋고, ‘차가운 모습은 되지 말고 따뜻한 존재가 되자’라고 다짐할 때는 모델 B가 더 효과적이에요.",
                    "reprompt": "12차시에서 내가 정한 어조가 ‘~이 좋다(예찬형)’인지, ‘~되자(청유·다짐형)’인지에 따라 모델을 골라 보세요."
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "1연의 첫 행과 4연의 마지막 행을 똑같이 반복하는 것보다 조금 바꾸어(변주하여) 반복하면 어떤 점이 더 좋을까요?",
                    "expected_ans": "1연의 ‘사물(우산/지우개)’이 4연에서는 ‘그 사물 같은 사람(삶)’으로 깊어졌다는 것을 한눈에 보여 주면서 리듬감까지 살릴 수 있어요.",
                    "reprompt": "3차시에서 배운 ‘나는 구부러진 길이 좋다’ ➔ ‘구부러진 길 같은 사람이 좋다’의 변주 효과를 떠올려 보세요!"
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1] 재료 분류, [활동 2] 기-승-전-결 4연 구조도, [활동 3] 운율·행바꿈 설계표를 완성하도록 지도한다. 이 설계도가 다음 15차시 초고 집필의 네비게이션이 됨을 안내한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 브릿지 질문 정답]</strong> 1~2연에서 묘사한 구체적 사물의 특징을 3연에서 ‘사람의 삶과 마음’으로 전환해야 시의 주제가 깊어지고 감동이 고조되기 때문이다.<br>
                  <strong>• [활동 1 모범 답안]</strong> 1~2연용(외적 모습·감각 시어·사물 비유)과 3~4연용(내면 성찰·인생 확장 비유)이 적절히 구분되면 정답 인정.<br>
                  <strong>• [활동 2·3 모범 답안]</strong> 기-승-전-결 4연의 연별 중심 이미지, 3연의 시상 전환 표지, 수미상관 및 통사 구조 반복 계획이 구체적으로 작성되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "1연부터 4연까지 시상의 발전이나 전환 없이 똑같은 사물 묘사만 나열식으로 배치하는 경우",
                    "diagnosis": "연(Stanza) 구분의 기능과 ‘기-승-전-결’의 위계적 심화 원리를 이해하지 못함.",
                    "prescription": "1~2연은 ‘눈으로 본 사물 이야기’, 3~4연은 ‘마음으로 깨달은 사람 이야기’로 층위를 나누도록 [활동 2]의 3연(전·轉) 전환 표지 칸을 집중 점검한다."
                },
                {
                    "error_case": "운율 계획을 세울 때 글자 수(3·4조, 4·4조)만 기계적으로 맞추려고 하여 문장이 부자연스러워지는 경우",
                    "diagnosis": "현대 자유시의 내재율이 글자 수 제한보다 ‘통사 구조(문장 틀)의 반복과 변주, 시어의 대칭’에서 비롯됨을 모름.",
                    "prescription": "‘~을 품고 ~을 품고’, ‘~할 때 ~한다’처럼 문장 구조를 나란히 반복하는 것이 자연스러운 현대시 운율 형성법임을 안내한다."
                }
            ],
            "scaffolding_down": "모델 A와 모델 B의 4연 빈칸 템플릿 중 하나를 선택하게 하고, 13차시에 만든 시어 카드를 각 연 상자 위에 올려놓으며 순서를 배열하게 한다.",
            "scaffolding_up": "연과 연 사이의 시간 변화(낮➔밤, 겨울➔봄)나 공간 이동(근경➔원경)까지 고려하여 입체적인 시상 전개도를 설계해 보게 한다.",
            "rubric": {
                "high": "생성한 시적 재료들을 군집별로 분류하고, 4연(기-승-전-결)의 연별 중심 이미지·3연의 시상 전환·수미상관 운율·행 분할 계획을 유기적으로 완벽히 구조화함.",
                "mid": "4연의 연별 중심 내용은 배치했으나, 3연의 시상 전환 표지나 수미상관·반복 운율 설계가 다소 단순함.",
                "low": "연 구분의 기준이 모호하고 1~4연의 내용이 평면적으로 중복됨."
            }
        }
    },

    # =========================================================================
    # 15차시: G6-POE-W4 초고 집필하기 (갈래별 핵심 표현 전략·문장화)
    # =========================================================================
    {
        "lesson_title": "[시 쓰기 ④ 집필하기] 운율과 행간 걸침·호흡을 살려 4연 현대시 초고 쓰기",
        "std_badge": "[6국05-01] [6국05-03]",
        "student_goal": "14차시 시상 설계도에 따라 설정한 화자의 어조, 복합 시어, 참신한 비유·상징, 내재율, 의도적 행·연 배열과 주술 호응을 갖추어 3~4연 이상의 완결된 현대시 초고를 집필할 수 있다.",
        "marking_items": [
            ["mk-highlight", "형광펜", "내가 초고에 사용한 핵심 비유(직유·은유·의인·역설) 구절"],
            ["mk-line-blue", "파란 밑줄", "형태소 결합으로 만든 복합 시어(합성어·파생어)와 감각어"],
            ["mk-line-red", "빨간 밑줄", "호흡과 여운을 조절하기 위해 의도적으로 행을 바꾼 지점"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.9pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px;">
              <div style="font-size:7.6pt; font-weight:800; color:#6C3483; margin-bottom:3px;">✒️ [현대시 초고 집필 코칭 스튜디오] 줄글(산문)을 시(운문)로 바꾸는 ‘행바꿈(행간 걸침)’의 마법</div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:7.2pt; line-height:1.42;">
                <div style="background:#FDEDEC; border:0.7pt solid #E6B0AA; border-radius:4px; padding:4px 6px;">
                  <strong style="color:#B03A2E;">❌ 줄글처럼 길게 늘어뜨린 배열 (호흡 단조로움)</strong><br>
                  나는 비스듬히 기울어진 우산이 좋다. 비 오는 날 우산을 쓰면 토독토독 빗방울이 노크하는 소리를 들을 수 있고 친구와 발걸음을 맞추어 걸을 수 있다.
                </div>
                <div style="background:#EAFAF1; border:0.7pt solid #82E0AA; border-radius:4px; padding:4px 6px;">
                  <strong style="color:#196F3D;">⭕ 시적 호흡과 여운을 살린 행바꿈 (Enjambment)</strong><br>
                  나는 비스듬히 기울어진 우산이 좋다. <strong>(단정·여운)</strong><br>
                  비 내리는 하굣길 우산을 펼치면 <strong>(배경 제시 후 행바꿈)</strong><br>
                  토독토독 푸른 지붕을 두드리는 빗소리를 만날 수 있고<br>
                  친구와 나란히 맞추어 걷는 발걸음을 만날 수 있다.
                </div>
              </div>
            </div>

            <!-- 모범 초고 전문 예시 -->
            <div class="inline-segment-box" style="padding:6px 10px; margin-bottom:4px;">
              <div style="font-family:var(--font-sans); font-size:7.3pt; font-weight:800; color:#6C3483; border-bottom:0.7pt solid #C39BD3; padding-bottom:2px; margin-bottom:4px; display:flex; justify-content:space-between;">
                <span>📜 [학생 모범 초고 예시] 비스듬히 기울어진 우산 (4연 16행)</span>
                <span style="color:#196F3D;">비유·복합어·수미상관·행바꿈 적용본</span>
              </div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:8.2pt; line-height:1.5;">
                <div style="border-right:0.7pt dashed #BDC3C7; padding-right:6px;">
                  <span class="p-num">➊</span> 나는 비스듬히 기울어진 우산이 좋다.<br>
                  비 내리는 하굣길 우산을 펼치면<br>
                  <span class="mk-line-blue">토독토독</span> <span class="mk-highlight">작은 지붕을 두드리는 빗소리</span>를 만날 수 있고<br>
                  친구와 나란히 맞추는 <span class="mk-line-blue">발걸음</span>을 만날 수 있다.<br><br>
                  <span class="p-num">➋</span> 둥근 나뭇잎 아래 작은 새들이 모여 쉬듯이<br>
                  웃음소리도 피어나고 이야기도 피어나는 우산.<br>
                  우산은 세찬 <span class="mk-line-blue">비바람</span>을 막아 주며 <span class="mk-highlight">두 어깨를 품고 간다.</span>
                </div>
                <div>
                  <span class="p-num">➌</span> <span class="mk-line-red">그 우산처럼 걸어가는 사람이 나는 또한 좋다.</span><br>
                  혼자서만 마른 길 편하게 걷는 사람보다<br>
                  내 한쪽 어깨가 <span class="mk-line-blue">물기투성이</span>로 차갑게 젖어도<br>
                  <span class="mk-highlight">친구의 머리 위에 봄하늘을 띄워 주는 사람</span>이 좋다.<br><br>
                  <span class="p-num">➍</span> 젖은 어깨에 친구를 품고 이웃을 품고 가는<br>
                  <span class="mk-line-red">비스듬히 기울어진 우산 같은 사람이 좋다.</span>
                </div>
              </div>
            </div>

            <div class="inline-bridge-box practice" style="margin-bottom:0;">
              <div style="font-weight:800; color:#2874A6;">🙋 행바꿈과 호응 점검<br><span class="role-chip">함께 We Do</span></div>
              <div>
                시를 여러 행으로 나누어 쓸 때(행간 걸침), 문장의 <strong>주어(‘나는 / 우산은’)와 서술어(‘좋다 / 품고 간다’)</strong>가 서로 어긋나지 않게 하려면 무엇을 주의해야 할까요?<br>
                <span class="pencil-line">✏️ 주의할 점: <span class="t-ans">행이 바뀌더라도 한 문장으로 이어 읽었을 때 주어와 서술어, 목적어와 서술어의 짝(문장 성분 호응)이 정확히 맞는지 확인해야 한다.</span></span>
              </div>
            </div>
        """,
        "activity_1": {
            "title": "초고 집필 전 나의 ‘핵심 시어·비유·운율 체크뱅크’ 최종 점검하기",
            "tag": "Step 1 조직도 및 시어 목록 확인 (W4)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:25%;">점검 항목</th>
                      <th style="width:75%;">내 초고에 반드시 넣을 핵심 재료 확인</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 시 제목 &amp; 화자 어조</strong></td>
                      <td>• 제목: <span class="blank-slot"><span class="t-ans">〈비스듬히 기울어진 우산〉 (또는 나만의 창작 시 제목)</span></span> / 어조: <span class="blank-slot"><span class="t-ans">따뜻한 고백·예찬 어조 (‘~좋다 / ~되자’)</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>② 필수 복합어 &amp; 감각어</strong></td>
                      <td>• 합성어·파생어 3개: <span class="blank-slot"><span class="t-ans">비바람, 발걸음, 물기투성이</span></span> / 감각어: <span class="blank-slot"><span class="t-ans">토독토독, 차갑게 젖어도, 따뜻한</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>③ 핵심 비유 &amp; 수미상관</strong></td>
                      <td>• 비유: <span class="blank-slot"><span class="t-ans">작은 지붕, 두 어깨를 품고 간다, 봄하늘을 띄워 주는 사람</span></span> / 수미상관: 1연 첫 행 ↔ 4연 끝 행 호응</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 체크뱅크 재료를 활용하여 통사 구조 반복과 행바꿈 호흡을 조절하며 시행 다듬기",
        "activity_2": {
            "title": "운율 형성(통사 반복)과 행간 걸침(행바꿈) 호흡 조절 연습하기",
            "tag": "Step 2 운율 및 호흡·여운 통제 (W4 + COM-A3)",
            "body_html": """
                <div class="inference-row" style="grid-template-columns:1fr 18px 1fr;">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">🎵 [내재율 만들기] 나란히 반복할 문장 구조</strong>
                    <div style="margin-top:3px; font-size:7.2pt;">
                      내 시에서 리듬감을 주기 위해 2회 이상 반복·변주할 구절:<br>
                      <span class="pencil-line">✏️ <span class="t-ans">‘~을 만날 수 있고 / ~을 만날 수 있다’, ‘친구를 품고 이웃을 품고 가는’</span></span>
                    </div>
                  </div>
                  <div class="inf-symbol">+</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">✂️ [행바꿈 &amp; 주술 호응] 강조를 위한 행 나눔</strong>
                    <div style="margin-top:3px; font-size:7.2pt;">
                      시상을 전환하는 3연의 주어-서술어 호응 문장:<br>
                      <span class="pencil-line">✏️ <span class="t-ans">그 우산처럼 걸어가는 사람이(보어) / 나는(주어) 또한 좋다(서술어).</span></span>
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 1·2]를 통합하여 3~4연 이상의 완결된 나만의 현대시 초고 집필하기",
        "activity_3": {
            "title": "나만의 현대시 초고 집필 스튜디오 (3~4연 완결본 작성)",
            "tag": "Step 3 완결된 현대시 초고 집필 (W4)",
            "body_html": """
                <div style="font-size:7.3pt; margin-bottom:3px;"><strong>[조건]</strong> ① 3~4연 이상의 연 구분, ② 복합 시어와 감각어 3개 이상, ③ 참신한 비유·상징 3개 이상, ④ 반복 운율과 정확한 주술 호응을 갖추어 시 초고를 완성하세요.</div>
                <div style="background:#FFFDF9; border:0.9pt solid #6C3483; border-radius:5px; padding:6px 9px; font-size:7.4pt; line-height:1.52;">
                  <div style="text-align:center; font-weight:800; color:#6C3483; margin-bottom:3px;">시 제목: <span class="blank-slot" style="min-width:160px;"><span class="t-ans">〈비스듬히 기울어진 우산〉 (또는 〈둥글어진 지우개〉)</span></span></div>
                  <span class="pencil-line">✏️ <strong>[1연]</strong> <span class="t-ans">나는 비스듬히 기울어진 우산이 좋다. / 비 내리는 하굣길 우산을 펼치면 / 토독토독 작은 지붕을 두드리는 빗소리를 만날 수 있고 / 친구와 나란히 맞추는 발걸음을 만날 수 있다.</span></span>
                  <span class="pencil-line">✏️ <strong>[2연]</strong> <span class="t-ans">둥근 나뭇잎 아래 작은 새들이 모여 쉬듯이 / 웃음소리도 피어나고 이야기도 피어나는 우산. / 우산은 세찬 비바람을 막아 주며 두 어깨를 품고 간다.</span></span>
                  <span class="pencil-line">✏️ <strong>[3연]</strong> <span class="t-ans">그 우산처럼 걸어가는 사람이 나는 또한 좋다. / 혼자서만 마른 길 편하게 걷는 사람보다 / 내 한쪽 어깨가 물기투성이로 차갑게 젖어도 / 친구의 머리 위에 봄하늘을 띄워 주는 사람이 좋다.</span></span>
                  <span class="pencil-line">✏️ <strong>[4연]</strong> <span class="t-ans">젖은 어깨에 친구를 품고 이웃을 품고 가는 / 비스듬히 기울어진 우산 같은 사람이 좋다.</span></span>
                </div>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 16차시(W5 고쳐쓰기) 2층 시어 조탁 및 문법 호응 퇴고 대상으로 직결",
            "prompt": "방금 쓴 초고를 소리 내어 읽어 보고, 다음 시간(고쳐쓰기)에 더 참신한 시어로 바꾸거나 다듬고 싶은 부분 1곳에 밑줄을 그어 메모해 두세요.",
            "placeholder": "예: 2연의 ‘이야기도 피어나는’을 더 감각적인 시어로 바꾸고 싶다.",
            "example_answer": "3연의 ‘편하게 걷는 사람보다’를 ‘빗방울 하나 맞지 않고 반듯하게 걷는 사람보다’로 더 선명하게 대조시키고 싶다."
        },
        "self_check": [
            "14차시에서 계획한 3~4연의 시상 전개 구조와 일관된 화자의 어조를 살려 초고를 썼나요?",
            "복합 시어(합성어·파생어)와 감각 심상, 참신한 비유·상징 표현을 3개 이상 자연스럽게 녹여 냈나요?",
            "행바꿈(행간 걸침)을 할 때 호흡과 리듬감을 살리면서 주어-서술어 호응이 맞도록 작성했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[초고 집필 3대 컨트롤 타워] ① 호흡 통제(행바꿈·연바꿈으로 시선의 멈춤과 여운 만들기) + ② 리듬 통제(통사 구조 반복 '~을 만날 수 있고', 수미상관 호응) + ③ 문법 통제(행간 걸침 시 주어-목적어-서술어 호응 유지)",
            "intro_5min": "설계도와 재료가 모두 준비되었으니 이제 나만의 시집에 실릴 초고를 완성하는 시간임을 안내한다. 줄글(산문)과 시(운문)의 가장 큰 형태적 차이인 ‘행바꿈(행간 걸침)’이 어떻게 음악적 호흡과 여운을 만드는지 칠판 예시로 비교해 보여 준다.",
            "ido_think_aloud_script": "“초고를 쓸 때 가장 중요한 비결은 ‘소리 내어 읽으며 행을 바꾸는 것’이에요. ‘나는 비스듬히 기울어진 우산이 좋다.’를 쓰고 나서 바로 이어 쓰지 않고 줄을 딱 바꾸면(행바꿈), 읽는 사람이 잠시 숨을 멈추며 기울어진 우산의 모습을 머릿속에 그리게 돼요. 또 3연에서 여러 줄에 걸쳐 길게 수식하더라도, ‘내 한쪽 어깨가 젖어도(부사절) + 친구의 머리 위에 봄하늘을 띄워 주는 사람이(주어/보어) + 좋다(서술어)’처럼 문장 성분의 짝이 정확히 맞도록 호응을 챙겨야 합니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "2연 2행 ‘웃음소리도 피어나고 이야기도 피어나는 우산.’처럼 서술어를 생략하고 명사(‘우산’)로 행을 끝맺으면 어떤 효과가 있나요?",
                    "expected_ans": "4차시 〈구부러진 길〉의 2연 2행에서 배운 것처럼, 독자의 시선을 ‘우산’에 딱 집중시키면서 여운을 남기는 효과가 있어요.",
                    "reprompt": "4차시(V1-4)에서 읽었던 ‘들꽃도 많이 피고 별도 많이 뜨는 구부러진 길.’이라는 명사형 종결 시행의 효과를 떠올려 보세요."
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "내 초고에서 독자의 눈과 귀를 가장 사로잡을 ‘하이라이트 비유 구절’은 몇 연 몇 행에 배치했나요?",
                    "expected_ans": "저는 3연 마지막 행에 ‘내 몸이 하얀 가루로 부서져도 친구의 실수 위에 새 길을 내어 주는 지우개 같은 사람이 좋다’를 배치했어요.",
                    "reprompt": "시상이 가장 고조되는 3연(전)이나 주제를 마무리하는 4연(결)에 가장 참신한 비유를 배치하면 감동이 배가됩니다."
                }
            ],
            "youdo_and_wrapup": "조용하고 잔잔한 배경 음악을 틀어 주고 학생들이 [활동 1]·[활동 2] 점검 후 [활동 3] 원고 노트에 3~4연 초고를 몰입하여 집필하도록 순회 지도한다. 첫 행을 시작하기 어려워하는 학생에게 1연 첫 행 물꼬를 터 준다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 브릿지 질문 정답]</strong> 행이 바뀌더라도 한 문장으로 이어 읽었을 때 주어와 서술어, 목적어와 서술어의 짝(문장 성분 호응)이 정확히 맞는지 확인해야 한다.<br>
                  <strong>• [활동 1·2·3 모범 답안]</strong> 학생이 선정한 시적 대상을 바탕으로 ① 3~4연 이상의 연 구분, ② 복합 시어 및 감각어 3개 이상, ③ 참신한 비유·상징 3개 이상, ④ 통사 구조 반복(내재율) 및 주술 호응을 갖춘 초고를 작성하면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "행바꿈을 어절마다 무조건 끊어 쓰거나(예: ‘나는 / 비스듬히 / 기울어진 / 우산이 / 좋다’), 반대로 한 행에 두세 문장을 길게 몰아 쓰는 경우",
                    "diagnosis": "행바꿈이 의미 단위(음보·호흡 단위)와 시적 여운을 조절하는 장치임을 체득하지 못함.",
                    "prescription": "자신이 쓴 시를 천천히 낭송해 보게 하여 자연스럽게 숨을 쉬는 호흡 단위와 강조하고 싶은 이미지 단위로 행을 나누도록 코칭한다."
                },
                {
                    "error_case": "행간 걸침(수식어가 다음 행으로 이어짐) 과정에서 앞 행의 주어(‘나는’)와 뒷 행의 서술어(‘되어 내리자’)가 호응하지 않는 비문을 쓰는 경우",
                    "diagnosis": "여러 행에 걸쳐 문장이 길어질 때 앞 행에 쓴 주어·부사어를 잊어버리고 종결 어미를 바꿈.",
                    "prescription": "연 전체를 줄글처럼 한 줄로 이어 읽어 보게 하여 주어(‘나는/우리는’)와 서술어(‘좋다/되자’)의 호응을 점검하게 한다."
                }
            ],
            "scaffolding_down": "모범 초고 예시의 구조 틀(1연: 나는 ___이 좋다 / 2연: ___하듯이 ___하는 ___ / 3연: 그 ___처럼 살아온 사람이 나는 또한 좋다 / 4연: ___을 품고 가는 ___ 같은 사람이 좋다)을 제공하여 자신의 시어로 채워 완성하게 한다.",
            "scaffolding_up": "도치법(3연 1행), 명사형 종결(2연 2행), 말줄임표나 명령형 환기어(‘보라’) 등 단원에서 배운 고급 통사·수사 기법을 3가지 이상 의도적으로 결합하여 초고를 작성하게 한다.",
            "rubric": {
                "high": "설정한 화자의 어조, 복합 시어·감각어 3개 이상, 참신한 비유·상징 3개 이상, 내재율과 의도적 행·연 배열 및 정확한 주술 호응을 모두 갖추어 3~4연 이상의 완성도 높은 시 초고를 집필함.",
                "mid": "3~4연의 시 초고를 완성하고 비유와 감각어를 사용했으나, 행바꿈 호흡이나 일부 문장 성분 호응이 다소 어색함.",
                "low": "연 구분 없이 짧은 산문처럼 작성하거나 필수 표현 요소(복합어·비유·운율)가 대부분 누락됨."
            }
        }
    },

    # =========================================================================
    # 16차시: G6-POE-W5 고쳐쓰기 (내용·조직·표현[주술호응·교정부호] 3단계 퇴고)
    # =========================================================================
    {
        "lesson_title": "[시 쓰기 ⑤ 고쳐쓰기] 2층 노트로 시어를 조탁하고 호응·교정부호로 퇴고해 시화 완성하기",
        "std_badge": "[6국03-06] [6국04-05]",
        "student_goal": "초고의 내용·조직·표현(상투적 어휘, 행간 걸침 시 주술·부사어·시제 호응 오류)을 정밀 진단하고, 교정부호를 사용하여 시어를 참신하게 조탁(퇴고)한 뒤 최종 시화(詩畫) 작품을 완성할 수 있다.",
        "marking_items": [
            ["mk-line-red", "빨간 교정부호", "상투적·추상적 어휘를 참신한 감각·비유·복합 시어로 조탁(교체)"],
            ["mk-line-blue", "파란 교정부호", "행간 걸침 시 어긋난 주어·부사어·서술어 호응 교정"],
            ["mk-highlight", "형광펜", "시적 허용과 구별하여 반드시 고쳐야 할 문법적 비문 진단"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.8pt solid #C39BD3; border-radius:5px; padding:4px 9px; margin-bottom:4px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:7.3pt; font-weight:800; color:#6C3483;">🛠️ [2층 고행간 시어 조탁 &amp; 호응 교정 스튜디오]</span>
                <strong style="font-size:9.2pt; color:#17202A; margin-left:5px;">초고 진찰부터 교정부호 첨삭까지</strong>
              </div>
              <span style="font-size:7.1pt; color:#C0392B; font-weight:700;">윗줄(교정부호·조탁안) / 아랫줄(원래 초고)</span>
            </div>

            <!-- 2층 줄공책 (.draft-revision-grid + .nb-para-block + .nb-double-line) -->
            <div class="draft-revision-grid" style="margin-bottom:4px;">
              <div class="notebook-pane">
                <!-- 1연 블록 -->
                <div class="nb-para-block">
                  <div class="nb-para-tag">1연<br><span style="font-size:6.2pt; color:#6C3483;">[기]</span></div>
                  <div>
                    <div class="nb-double-line">
                      <div class="nb-upper-edit">↳ [표현 조탁] ‘엄청 큰 소리’ ➔ <strong>‘토독토독 작은 지붕을 두드리는 빗소리’</strong> (감각·은유)</div>
                      <div class="nb-lower-write">비 내리는 하굣길 우산을 펼치면 <del style="color:#C0392B;">엄청 큰 비 오는 소리</del>를 만날 수 있고</div>
                    </div>
                    <div class="nb-double-line">
                      <div class="nb-upper-edit">↳ [복합 시어 교체] ‘걸어가는 발’ ➔ <strong>‘나란히 맞추는 발걸음(합성어)’</strong></div>
                      <div class="nb-lower-write">친구와 <del style="color:#C0392B;">걸어가는 발</del>을 만날 수 있다.</div>
                    </div>
                  </div>
                </div>
                <!-- 2연 블록 -->
                <div class="nb-para-block">
                  <div class="nb-para-tag">2연<br><span style="font-size:6.2pt; color:#196F3D;">[승]</span></div>
                  <div>
                    <div class="nb-double-line">
                      <div class="nb-upper-edit">↳ [부사어·서술어 호응 교정] ‘결코’는 부정 서술어와 호응! ➔ <strong>‘세찬 비바람을 끝내 막아 주며’</strong></div>
                      <div class="nb-lower-write">우산은 <del style="color:#C0392B;">결코</del> 비바람을 막아 주며 두 어깨를 품고 간다.</div>
                    </div>
                  </div>
                </div>
                <!-- 3~4연 블록 -->
                <div class="nb-para-block">
                  <div class="nb-para-tag">3·4연<br><span style="font-size:6.2pt; color:#B03A2E;">[전·결]</span></div>
                  <div>
                    <div class="nb-double-line">
                      <div class="nb-upper-edit">↳ [주술·시제 호응 교정] 주어 ‘나는’과 호응하도록 ➔ <strong>‘봄하늘을 띄워 주는 사람이 좋다.’</strong></div>
                      <div class="nb-lower-write">그 우산처럼 <span style="color:#1F618D; font-weight:700;">나는</span> 내 어깨가 물기투성이로 젖어도 친구 머리 위에 봄하늘을 <del style="color:#C0392B;">띄워 주자.</del></div>
                    </div>
                    <div class="nb-double-line">
                      <div class="nb-upper-edit">↳ [조직 퇴고: 수미상관 추가] ¶ 행 추가: <strong>‘비스듬히 기울어진 우산 같은 사람이 좋다.’</strong></div>
                      <div class="nb-lower-write">젖은 어깨에 친구를 품고 이웃을 품고 가는 <strong>[ ∨ 마지막 행 추가 ]</strong></div>
                    </div>
                  </div>
                </div>
              </div>

              <!-- 우측 퇴고 진단 메모란 -->
              <div style="background:#FFFDF9; padding:5px 7px; font-size:7.1pt; line-height:1.38; display:flex; flex-direction:column; justify-content:space-between;">
                <div>
                  <strong style="color:#C0392B; font-size:7.4pt;">🩺 3차원 메타인지 퇴고 진단</strong>
                  <div style="margin-top:3px; border-top:0.6pt dashed #BDC3C7; padding-top:3px;">
                    <strong>1. [표현·어휘 조탁]</strong><br>
                    • ‘엄청 큰 소리’ 같은 일상적·상투적 어휘를 의성어(<strong>토독토독</strong>)와 은유(<strong>작은 지붕</strong>), 합성어(<strong>발걸음</strong>)로 조탁함.
                  </div>
                  <div style="margin-top:3px; border-top:0.6pt dashed #BDC3C7; padding-top:3px;">
                    <strong>2. [문법·호응 교정 (COM-A3)]</strong><br>
                    • 2연: 부사어 ‘결코’는 ‘~않는다’와 호응하므로 긍정 서술어(‘막아 주며’) 앞에서는 <strong>‘끝내/묵묵히’</strong>로 고침.<br>
                    • 3연: 앞 행의 주어가 <strong>‘나는’</strong>인데 끝이 청유형(‘띄워 주자’)으로 끝나 주술 호응이 깨짐 ➔ <strong>‘사람이 좋다’</strong>로 교정!
                  </div>
                  <div style="margin-top:3px; border-top:0.6pt dashed #BDC3C7; padding-top:3px;">
                    <strong>3. [조직·수미상관 완결]</strong><br>
                    • 4연 끝에 1연 첫 행과 호응하는 문장을 삽입(∨)하여 수미상관 완성.
                  </div>
                </div>
                <div style="background:#F2F4F4; border-radius:4px; padding:3px 5px; font-size:6.8pt; color:#2C3E50;">
                  <strong>📌 핵심 교정부호</strong>: <span style="color:#C0392B; font-weight:800;">═○</span>(삭제), <span style="color:#C0392B; font-weight:800;">∨</span>(삽입), <span style="color:#C0392B; font-weight:800;">─□</span>(내용 바꿈), <span style="color:#C0392B; font-weight:800;">¶</span>(줄 바꿈)
                </div>
              </div>
            </div>

            <div class="inline-bridge-box practice" style="margin-bottom:0;">
              <div style="font-weight:800; color:#2874A6;">🙋 시적 허용 vs 비문<br><span class="role-chip">함께 We Do</span></div>
              <div>
                시에서 여운을 주려고 서술어를 생략하는 것(‘~구부러진 길.’)은 <strong>시적 허용(기법)</strong>이지만, 3연처럼 <strong>“나는 ~ 띄워 주자.”</strong>라고 쓴 것은 왜 반드시 고쳐야 할까요?<br>
                <span class="pencil-line">✏️ 진단 이유: <span class="t-ans">의도적인 여운 효과가 아니라 주어(‘나는’)와 서술어(‘~자’)의 짝이 맞지 않아 문장의 뜻이 흐려지는 문법적 호응 오류(비문)이기 때문이다.</span></span>
              </div>
            </div>
        """,
        "activity_1": {
            "title": "내용·조직·표현(어휘 조탁 및 문장 성분 호응) 3단계 오류 정밀 진단하기",
            "tag": "Step 1 3차원 정밀 진단 (W5 + COM-A3·A4)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:20%;">퇴고 차원</th>
                      <th style="width:42%;">초고의 문제점 진단 (점검 질문)</th>
                      <th style="width:38%;">진단 결과 및 교정부호 처방</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 내용·표현 차원<br>(시어 조탁)</strong></td>
                      <td>‘엄청 큰 비 오는 소리’, ‘걸어가는 발’처럼 시적 울림이 부족하고 상투적·추상적인 일상어가 쓰였는가?</td>
                      <td><strong>[내용 바꿈 ─□]</strong> 청각 심상(<span class="blank-slot"><span class="t-ans">토독토독</span></span>)과 비유(<span class="blank-slot"><span class="t-ans">작은 지붕</span></span>), 합성어(<span class="blank-slot"><span class="t-ans">발걸음</span></span>)로 교체 처방</td>
                    </tr>
                    <tr>
                      <td><strong>② 문법 호응 차원<br>(부사어·주술 호응)</strong></td>
                      <td>• 2연: ‘결코 ~ 막아 주며’ (부사어 호응 오류)<br>• 3연: ‘<strong>나는</strong> ~ 봄하늘을 <strong>띄워 주자</strong>’ (주술 호응 오류)</td>
                      <td>• ‘결코’ ➔ 긍정문과 어울리는 <span class="blank-slot"><span class="t-ans">‘끝내/묵묵히’</span></span>로 수정<br>• ‘띄워 주자’ ➔ 주어 ‘나는’과 호응하는 <span class="blank-slot"><span class="t-ans">‘사람이 좋다’</span></span>로 수정</td>
                    </tr>
                    <tr>
                      <td><strong>③ 조직 차원<br>(연·행 배열)</strong></td>
                      <td>4연 마지막 행이 1연 첫 행과 호응하지 못한 채 갑자기 끝났는가?</td>
                      <td><strong>[삽입 ∨]</strong> 1연 첫 행과 변주된 수미상관을 이루도록 마지막 행 추가 처방</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 진단 결과를 내 초고에도 적용하여 퇴고 전후(Before & After) 표현 효과 비교하기",
        "activity_2": {
            "title": "내 초고의 시어 조탁 및 문장 호응 교정 전후(Before ➔ After) 비교표",
            "tag": "Step 2 시어 교체 및 통사 수정안 도출 (W5)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:18%;">수정 지점</th>
                      <th style="width:36%;">고치기 전 초고 구절 (Before)</th>
                      <th style="width:46%;">조탁·교정한 최종 구절 (After) &amp; 개선 효과</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 상투적 어휘<br>➔ 감각·비유 조탁</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">편하게 걷는 사람보다 (또는 엄청 큰 비 오는 소리)</span></span></td>
                      <td>➔ <strong><span class="blank-slot"><span class="t-ans">빗방울 하나 맞지 않고 반듯하게 걷는 사람보다</span></span></strong><br>(효과: ‘물기투성이로 젖은 어깨’와의 시각적·촉각적 대비가 훨씬 선명해짐)</td>
                    </tr>
                    <tr>
                      <td><strong>② 행간 걸침 시<br>호응·운율 교정</strong></td>
                      <td><span class="blank-slot"><span class="t-ans">나는 ~ 봄하늘을 띄워 주자.</span></span></td>
                      <td>➔ <strong><span class="blank-slot"><span class="t-ans">나는 ~ 봄하늘을 띄워 주는 사람이 좋다.</span></span></strong><br>(효과: 주어 ‘나는’과 서술어 ‘좋다’의 호응이 정확해지고 1연과 어조가 통일됨)</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_2_to_3": "[활동 2]의 퇴고를 거쳐 완성한 최종 시와 시각 이미지를 결합하여 시화(詩畫)로 출판하기",
        "activity_3": {
            "title": "최종 완성 시화(詩畫) 출판 및 퇴고 효과 설명하기",
            "tag": "Step 3 최종 작품 완성 및 메타인지 성찰 (W5)",
            "body_html": """
                <div style="font-size:7.3pt; margin-bottom:3px;"><strong>[최종 출판]</strong> 교정부호로 고쳐 쓴 최종 시의 하이라이트 연(3~4연)을 정서(正書)하고, 퇴고를 통해 내 시가 어떻게 더 좋아졌는지 설명하세요.</div>
                <div style="background:#F6F0F9; border:1pt solid #6C3483; border-radius:5px; padding:5px 9px; font-size:7.5pt; line-height:1.55; margin-bottom:3px;">
                  <strong>🎨 [나의 최종 완성 시화 작품 (하이라이트 연)]</strong><br>
                  <span class="pencil-line">✏️ <span class="t-ans">그 우산처럼 걸어가는 사람이 나는 또한 좋다. / 빗방울 하나 맞지 않고 반듯하게 걷는 사람보다 / 내 한쪽 어깨가 물기투성이로 차갑게 젖어도 / 친구의 머리 위에 봄하늘을 띄워 주는 사람이 좋다. // 젖은 어깨에 친구를 품고 이웃을 품고 가는 / 비스듬히 기울어진 우산 같은 사람이 좋다.</span></span>
                </div>
                <span class="pencil-line">✏️ 퇴고 전후 표현 효과 개선점 설명: <span class="t-ans">상투적인 일상어를 ‘물기투성이(파생어)’, ‘작은 지붕·봄하늘(은유)’로 조탁하여 심상이 생생해졌고, 행간에 어긋났던 주술·부사어 호응을 바로잡고 수미상관을 더해 시적 완성도와 여운이 깊어졌다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "🏆 1단원(시) 전 과정 완주! ➔ 2단원(이야기)으로 문해력 날개 펼치기",
            "prompt": "1단원 「시어의 결을 따라 마음의 길을 걷다」 16차시를 모두 마친 소감과, 단원 핵심 질문(“시인은 왜 평범한 일상과 자연의 모습에 마음을 담아 노래할까요?”)에 대한 나만의 답을 적어 보세요.",
            "placeholder": "예: 평범한 사물 속에서도 가족과 친구를 사랑하는 따뜻한 삶의 길을 발견할 수 있기 때문이다.",
            "example_answer": "무심코 지나치는 구부러진 길, 봄길, 담쟁이, 눈발, 우산 속에도 시련을 이겨 내고 이웃을 품어 주는 따뜻한 삶의 지혜가 숨어 있기 때문이다."
        },
        "self_check": [
            "시적 허용과 문법적 비문(주술·부사어 호응 불일치)을 정확히 구별하여 수정 지점을 진단했나요?",
            "2층 시어 조탁 노트와 교정부호를 사용해 상투적 어휘를 참신한 감각·비유·복합 시어로 고쳐 썼나요?",
            "퇴고 전후의 표현 효과 개선점을 설명하고 나만의 완결된 시화(詩畫) 작품을 완성했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[3차원 메타인지 시 퇴고 클리닉] ① 내용·표현 조탁(상투적 어휘 ➔ 감각어·복합어·참신한 비유로 교체 `─□`) + ② 통사 호응 교정(행간 걸침 시 주어 ‘나는’ ↔ 서술어 ‘좋다’, 부사어 ‘결코’ ↔ 부정어 호응 점검) + ③ 조직 완결(수미상관 행 삽입 `∨` 및 행바꿈 `¶` 조절)",
            "intro_5min": "보석 원석을 정교하게 깎고 다듬어야 다이아몬드가 되듯, 시인이 초고를 쓰고 난 뒤 단어를 갈고닦는 과정을 ‘조탁(彫琢·퇴고)’이라고 부름을 소개한다. 좌측 페이지의 2층 고행간 시어 조탁 노트를 함께 살펴본다.",
            "ido_think_aloud_script": "“2층 조탁 노트의 2연과 3연을 볼까요? 2연 초고에 ‘우산은 결코 비바람을 막아 주며’라고 썼어요. 어라? ‘결코’라는 부사어는 뒤에 ‘포기하지 않는다’ 같은 부정 서술어가 와야 호응이 맞죠! 긍정 서술어 ‘막아 주며’ 앞에서는 ‘끝내’나 ‘묵묵히’로 고쳐야 해요. 또 3연을 보세요. 첫 줄에 ‘나는’이라는 주어로 시작했는데, 행이 여러 번 바뀌다 보니 마지막 줄을 ‘봄하늘을 띄워 주자.’라고 끝냈어요. ‘나는 ~ 띄워 주자’는 주어와 서술어가 맞지 않는 비문이에요! 시에서도 이런 문법 호응 오류는 시적 허용이 아니므로 반드시 ‘띄워 주는 사람이 좋다.’로 고쳐야 시의 울림이 살아납니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "1연 초고의 ‘엄청 큰 비 오는 소리’를 ‘토독토독 작은 지붕을 두드리는 빗소리’로 고쳤을 때 어떤 점이 더 좋아졌나요?",
                    "expected_ans": "‘엄청 큰’이라는 막연한 말 대신 ‘토독토독’이라는 청각 의성어와 우산을 ‘작은 지붕’에 빗댄 은유가 들어가서 빗소리가 훨씬 정겹고 생생하게 들려요.",
                    "reprompt": "9차시(V3-1)에서 평이한 산문과 시적 표현을 비교했던 기준(감각적 심상, 비유의 생동감)을 떠올려 보세요."
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "시에서 문법 규칙을 일부러 어기는 ‘시적 허용’과 반드시 고쳐야 하는 ‘문법 호응 오류(비문)’는 어떻게 구별할 수 있을까요?",
                    "expected_ans": "여운을 남기기 위해 서술어를 생략하거나 강조를 위해 순서를 바꾸는(도치) 것은 독자에게 특별한 느낌을 주는 시적 기법이지만, 주어와 서술어·부사어의 짝이 안 맞는 것은 실수로 뜻이 어색해진 비문이므로 꼭 고쳐야 해요.",
                    "reprompt": "독자가 읽었을 때 ‘여운이 남고 멋지다’고 느끼는지, 아니면 ‘앞뒤 말이 안 맞아서 이상하다’고 느끼는지 비교해 보세요."
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]~[활동 3]을 통해 자신의 15차시 초고를 3차원(내용·조직·표현 및 호응)으로 퇴고하고 최종 시화를 완성하도록 지도한다. 학급 ‘우리 반 마음의 길 시화전’을 열어 작품을 감상하며 1단원 대장정을 마무리한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 브릿지 질문 정답]</strong> 의도적인 여운 효과가 아니라 주어(‘나는’)와 서술어(‘~자’)의 짝이 맞지 않아 문장의 뜻이 흐려지는 문법적 호응 오류(비문)이기 때문이다.<br>
                  <strong>• [활동 1 모범 답안]</strong> ① 토독토독, 작은 지붕, 발걸음 ② 끝내/묵묵히, 사람이 좋다<br>
                  <strong>• [활동 2·3 모범 답안]</strong> 교정부호를 활용하여 상투적 어휘를 감각·비유·복합 시어로 조탁하고, 행간 문장 성분 호응을 바로잡아 퇴고 전후 개선점을 구체적으로 서술하면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "모든 문법적 호응 오류(예: ‘나는 ~ 가자’, ‘결코 ~ 좋았다’)를 “시니까 시적 허용이다”라고 합리화하며 고치지 않는 경우",
                    "diagnosis": "음운·어순 변용을 통한 미학적 장치인 ‘시적 허용’과 단순 통사 통제 실패인 ‘호응 비문’의 개념 경계를 혼동함.",
                    "prescription": "시적 허용은 원래 문법을 아는 상태에서 리듬·강조를 위해 쓰는 제한적 장치이며, 주술·부사어 호응 불일치는 시의 의미를 훼손하는 오류임을 명확히 구분해 준다."
                },
                {
                    "error_case": "고쳐쓰기를 맞춤법·띄어쓰기 고치기로만 좁게 생각하여 시어 조탁(비유·감각어 개선)이나 연·행 조직 수정을 하지 않는 경우",
                    "diagnosis": "표면적인 철자 교정에만 머무르는 초보 필자의 퇴고 습관을 지님.",
                    "prescription": "[활동 1]의 3차원(내용·표현 시어 조탁 ➔ 문법 호응 ➔ 조직·수미상관) 체크리스트를 순서대로 밟아 나가도록 안내한다."
                }
            ],
            "scaffolding_down": "자신의 초고에서 스스로 오류를 찾기 어려운 학생에게는 ‘짝꿍 상호 퇴고 점검표(① 주어-서술어 짝이 맞는가? ② 일반 단어를 감각어·합성어로 바꿀 곳은 어디인가?)’를 활용해 짝과 함께 찾아보게 한다.",
            "scaffolding_up": "완성된 시화 작품 뒤에 ‘시인의 말(창작 노트)’을 덧붙여, 내가 어떤 시어를 어떻게 조탁했고 어떤 삶의 가치를 담았는지 한 문단의 비평적 작가 노트로 작성해 보게 한다.",
            "rubric": {
                "high": "시적 허용과 문법적 비문(주술·부사어 호응 오류)을 100% 정확히 구별하여 진단하고, 교정부호를 사용해 내용·조직·표현 3차원을 전면 조탁·수정한 뒤 퇴고 전후의 개선점을 논리적으로 설명하여 최종 시화를 완성함.",
                "mid": "상투적 시어 교체와 주술 호응 오류 수정은 수행했으나, 퇴고 전후의 표현 효과 개선점에 대한 설명이 다소 간단함.",
                "low": "단순 맞춤법 수정에만 머무르며 행간 주술·부사어 호응 오류나 상투적 어휘를 진단·교정하는 데 교사의 직접적인 도움이 필요함."
            }
        }
    }
]
