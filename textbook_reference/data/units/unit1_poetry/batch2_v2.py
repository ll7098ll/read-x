# -*- coding: utf-8 -*-
"""
1단원: 시 (Poetry, unit1_poetry) — Batch 2 (5~8차시: 추론적 이해 V2-1 ~ V2-4)
수록 작품:
- 5~7차시: 정호승, 〈봄길〉 (시집 『사랑하다가 죽어버려라』, 창작과비평사, 1997 — 14행 전문 수록)
- 8차시: 윤동주, 〈새로운 길〉 (10행 전문) + 도종환, 〈담쟁이〉 (13행 전문)
"""

BATCH2 = [
    # =========================================================================
    # 5차시: G6-POE-V2-1 시어·상징·역설 추론
    # =========================================================================
    {
        "lesson_title": "다의어와 은유·역설 표현의 숨은 뜻 추론하기",
        "std_badge": "[6국05-02] [6국04-04]",
        "student_goal": "시 〈봄길〉에 쓰인 다의어(‘길, 끝나다, 봄’)의 사전적 의미와 시적 함축 의미를 대조하고, 역설과 은유 표현에 담긴 깊은 뜻을 문맥 단서로 추론할 수 있다.",
        "marking_items": [
            ["mk-person", "동그라미", "문맥에 따라 뜻이 달라지는 다의어(‘길, 끝나다, 봄’)"],
            ["mk-double", "두줄 밑줄", "겉으로는 모순되지만 깊은 진실을 담은 역설 구절"],
            ["mk-highlight", "형광펜", "‘A가 B가 되다’ 형태의 은유와 상실의 상징 구절"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.8pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:7.3pt; font-weight:800; color:#6C3483;">📜 [제재 시 전문 읽기]</span>
                <strong style="font-size:9.5pt; color:#17202A; margin-left:5px;">봄길</strong>
              </div>
              <span style="font-size:7.4pt; color:#566573; font-weight:600;">정호승 (시집 『사랑하다가 죽어버려라』, 1997)</span>
            </div>

            <table class="wing-reading-table">
              <thead>
                <tr>
                  <th>시 본문 정독 (14행 전문 · 표시하며 읽기)</th>
                  <th class="wing-head">🧠 다의어·역설·은유 추론</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➊</span> <span class="q-num">①</span><span class="mk-double"><span class="mk-person">길</span>이 <span class="mk-person">끝나는</span> 곳에서도</span><br>
                    <span class="q-num">②</span><span class="mk-double"><span class="mk-person">길</span>이 있다</span><br>
                    길이 끝나는 곳에서도<br>
                    길이 되는 사람이 있다<br>
                    <span class="q-num">③</span><span class="mk-highlight">스스로 <span class="mk-person">봄</span>길이 되어</span><br>
                    끝없이 걸어가는 사람이 있다</p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box guide u2">
                      <div class="wing-box-title"><span>🎙️ 선생님과 함께 생각 읽기</span><span class="role-chip">시범 I Do</span></div>
                      <div class="think-row"><span class="think-tag">[질문]</span><span>“길이 끝나는 곳에서도 길이 있다”는 말은 겉보기에 말이 안 되는 모순(역설)인데 무슨 뜻일까?</span></div>
                      <div class="think-row"><span class="think-tag">[단서]</span><span>앞의 <span class="q-num">①</span>‘길’은 걸어가는 땅이나 희망이 막힌 절망적 한계를 뜻하지만, 뒤의 <span class="q-num">②</span>‘길’은 누군가 스스로 ‘봄길이 되어’ 만들어 내는 새로운 가능성을 뜻해!</span></div>
                      <div class="think-row"><span class="think-tag">[정리]</span><span>다의어 ‘길’의 뜻을 달리 써서, 절망의 끝에서도 새로운 희망의 길이 열린다는 진실을 강조했구나!</span></div>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➋</span> <span class="q-num">④</span><span class="mk-highlight">강물은 흐르다가 멈추고</span><br>
                    <span class="mk-highlight">새들은 날아가 돌아오지 않고</span><br>
                    <span class="mk-highlight">하늘과 땅 사이의 모든 꽃잎은 흩어져도</span><br>
                    보라<br>
                    <span class="q-num">⑤</span><span class="mk-double">사랑이 끝난 곳에서도</span><br>
                    <span class="mk-double">사랑으로 남아 있는 사람이 있다</span><br>
                    <span class="mk-highlight">스스로 사랑이 되어</span><br>
                    한없이 <span class="mk-person">봄길</span>을 걸어가는 사람이 있다</p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 1 (상징 추론)</span><span class="role-chip">함께 We Do</span></div>
                      <div>2연 1~3행(<span class="q-num">④</span>)에서 강물이 멈추고, 새들이 돌아오지 않고, 꽃잎이 모두 흩어지는 모습은 우리 삶의 어떤 상황을 상징할까요?</div>
                      <span class="pencil-line">✏️ 상징 의미: <span class="t-ans">소중한 것들을 모두 잃어버린 극한의 상실과 절망의 상황</span></span>
                    </div>
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 2 (은유·역설)</span><span class="role-chip">스스로 You Do</span></div>
                      <div><span class="q-num">③</span>‘스스로 봄길이 되어’와 <span class="q-num">⑤</span>‘사랑이 끝난 곳에서도 사랑으로 남아 있는 사람’은 어떤 사람을 뜻할까요?</div>
                      <span class="pencil-line">✏️ 추론: <span class="t-ans">모두가 포기한 절망 속에서도 남을 위해 먼저 따뜻한 희망과 사랑을 베푸는 사람</span></span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
        """,
        "activity_1": {
            "title": "다의어(‘길, 끝나다, 봄’)의 사전적 기본 의미와 시적 함축 의미 비교하기",
            "tag": "Step 1 다의적 시어 식별 (V2-1 + COM-A2)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:16%;">다의어</th>
                      <th style="width:38%;">사전적 중심 의미 (표면적 의미)</th>
                      <th style="width:46%;">시 〈봄길〉 속 문맥적·함축적 의미 (확장 의미)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="text-align:center; font-weight:800; color:#6C3483;">길</td>
                      <td>사람이나 차가 지나다니도록 땅 위에 낸 일정한 공간</td>
                      <td>• 1행(길이 끝나는 곳): 지금까지 의지해 온 삶의 <span class="blank-slot"><span class="t-ans">희망이나 가능성</span></span><br>• 2행(길이 있다): 절망을 넘어 새로 개척하는 <span class="blank-slot"><span class="t-ans">살아갈 방법·구원</span></span></td>
                    </tr>
                    <tr>
                      <td style="text-align:center; font-weight:800; color:#6C3483;">끝나다</td>
                      <td>이어지던 공간이나 시간이 마지막에 이르러 끊어지다</td>
                      <td>더 이상 나아갈 수 없는 <span class="blank-slot"><span class="t-ans">절망적 한계와 단절</span></span>에 부딪히다</td>
                    </tr>
                    <tr>
                      <td style="text-align:center; font-weight:800; color:#6C3483;">봄(길)</td>
                      <td>겨울 다음에 오는 따뜻한 계절</td>
                      <td>얼어붙은 절망을 녹이고 생명을 살리는 <span class="blank-slot"><span class="t-ans">따뜻한 사랑과 희망의 길</span></span></td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 다의어 분석을 바탕으로 시 속 '상징·은유·역설' 표현을 문맥 단서와 연결하기",
        "activity_2": {
            "title": "상징·은유·역설 표현의 문맥 단서와 심층 의미 추론 매트릭스",
            "tag": "Step 2 문맥·대조 구도 연결 (V2-1)",
            "body_html": """
                <div class="inference-row">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">🔍 [시 속 표현 (표면적 모순·비유)]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      ① “길이 끝나는 곳에서도 길이 있다”<br>
                      ② “강물은 멈추고 … 꽃잎은 흩어져도”<br>
                      ③ “스스로 봄길이 되어 / 스스로 사랑이 되어”
                    </div>
                  </div>
                  <div class="inf-symbol">+</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">🧩 [텍스트 내적 문맥 단서]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      • 뒤이어 나오는 ‘길이 <span class="blank-slot"><span class="t-ans">되는 사람</span></span>이 있다’<br>
                      • 역접 어미 ‘~흩어<strong>져도</strong>’와 환기어 ‘<span class="blank-slot"><span class="t-ans">보라</span></span>’<br>
                      • 1연의 ‘봄길’과 2연의 ‘<span class="blank-slot"><span class="t-ans">사랑</span></span>’이 같은 위치에 대응됨
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#6C3483;">💡 [추론한 심층 함축 의미]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      • <strong>역설의 진실</strong>: 모든 희망이 끊어진 극한의 절망 속에서도, 누군가의 <span class="blank-slot"><span class="t-ans">희생과 사랑</span></span>이 있다면 새로운 희망의 길이 시작된다.
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 2]에서 추론한 결과를 종합하여 핵심 시어·역설 해설문 작성하기",
        "activity_3": {
            "title": "‘봄길’의 상징적 의미와 역설 구절을 풀이하는 시어 해설문 쓰기",
            "tag": "Step 3 심층 함축 의미 산출 (V2-1)",
            "body_html": """
                <div style="font-size:7.4pt; margin-bottom:3px;"><strong>[조건]</strong> ① 표면적 모순, ② 문맥적 단서(‘길이 되는 사람’, ‘스스로 사랑이 되어’), ③ 심층 함축 의미의 3단계를 갖추어 “길이 끝나는 곳에서도 길이 있다”와 ‘봄길’의 의미를 해설해 보세요.</div>
                <span class="pencil-line">✏️ 1단계(표면적 의미와 모순): <span class="t-ans">‘길이 끝나는 곳에 길이 있다’는 말은 길이 끊어졌는데 다시 길이 있다고 하여 겉으로는 모순되는 역설적 표현이다.</span></span>
                <span class="pencil-line">✏️ 2·3단계(문맥 단서와 심층 의미): <span class="t-ans">하지만 4~5행의 ‘길이 되는 사람’, ‘스스로 봄길이 되어’라는 단서를 보면, 절망 속에서도 타인을 위해 스스로 따뜻한 사랑과 희망(봄길)이 되어 주는 사람 덕분에 새로운 삶의 길이 열린다는 깊은 진실을 담고 있다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 13차시(W2 내용 생성) 다의어·은유·역설 표현 씨앗",
            "prompt": "일상에서 흔히 쓰는 낱말(예: 길, 빛, 그늘, 문, 다리) 중 하나를 골라, 사전적 의미를 넘어선 ‘시적 함축 의미’와 은유 표현(‘스스로 ~이 되어’)을 만들어 보세요.",
            "placeholder": "예: 다리 — 강을 건너는 다리(사전) ➔ 멀어진 친구의 마음을 이어 주는 화해의 손길(함축)",
            "example_answer": "그늘 — 빛이 가려진 어두운 곳(사전) ➔ 지친 친구가 쉬어 가도록 스스로 나무 그늘이 되어 주는 따뜻한 위로(함축)"
        },
        "self_check": [
            "다의어(‘길, 끝나다, 봄’)의 사전적 기본 의미와 시 속 문맥적 함축 의미를 정확히 비교했나요?",
            "1연의 ‘봄길’과 2연의 ‘사랑’이 맺는 은유·상징 관계를 텍스트 단서로 연결했나요?",
            "역설적 표현 이면에 담긴 진실을 3단계(표면 의미-문맥 단서-심층 의미)로 명료하게 해설했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측: 다의어 의미 확장] 길①(땅·기존 희망의 끝) vs 길②(새로 여는 삶의 방법·봄길) / [중앙: 1연↔2연 대칭 매핑] 길이 끝나는 곳(강물 멈춤·새 떠남·꽃잎 흩어짐) ⟷ 사랑이 끝난 곳 / 스스로 봄길이 되어 ⟷ 스스로 사랑이 되어 / [우측] 역설(Paradox)의 공식: 표면적 모순 + 문맥 단서 = 절망을 이기는 헌신의 진실",
            "intro_5min": "막다른 골목길 표지판 사진을 보여 주며 “길이 끝났을 때 우리는 보통 어떻게 하나요? 그런데 시인은 왜 ‘길이 끝나는 곳에서도 길이 있다’고 말했을까요?”라는 질문으로 호기심을 자극하며 역설과 다의어의 세계로 안내한다.",
            "ido_think_aloud_script": "“1연 1~2행을 읽을 때 선생님은 처음에 고개를 갸우뚱했어요. ‘길이 끝나는 곳에서도 길이 있다’니, 길이 끝났으면 없는 거지 어떻게 길이 있을까요? 겉으로 보면 앞뒤가 맞지 않는 모순(역설)이에요. 그런데 바로 다음 줄을 읽어 보니 단서가 나왔어요! ‘길이 끝나는 곳에서도 길이 되는 사람이 있다 / 스스로 봄길이 되어’. 아하! 첫 줄의 ‘길’은 지금까지 걸어온 땅이나 희망이 끊어진 절망을 뜻하고, 둘째 줄의 ‘길’은 누군가 자기 자신을 내어 주어 새로 만들어 낸 ‘희망의 봄길’을 뜻하는 거였어요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "2연에서 ‘강물은 흐르다가 멈추고 / 새들은 날아가 돌아오지 않고 / 모든 꽃잎은 흩어져도’는 1연의 어떤 구절과 뜻이 통하나요?",
                    "expected_ans": "1연의 ‘길이 끝나는 곳’과 뜻이 통해요. 흐르던 강물이 멈추고 꽃잎이 다 흩어지는 것은 모든 희망과 사랑이 끝난 절망적인 상황을 뜻해요.",
                    "reprompt": "강물, 새, 꽃잎이 모두 사라지고 멈추어 버린 풍경은 희망찬 상황일까요, 아니면 ‘길이 끝나는 곳’처럼 절망적인 상황일까요?"
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "1연의 ‘스스로 봄길이 되어’와 2연의 ‘스스로 사랑이 되어’를 나란히 놓아 보면, 결국 시인이 말하는 ‘봄길’의 진짜 의미는 무엇일까요?",
                    "expected_ans": "‘봄길’은 단순한 봄철의 길이 아니라, 절망에 빠진 이웃이 다시 걸어갈 수 있도록 자신을 바쳐 베푸는 ‘따뜻한 사랑과 헌신’을 뜻해요.",
                    "reprompt": "1연 5행과 2연 7행의 문장 구조를 겹쳐 보세요. ‘봄길’ 자리에 2연에서는 어떤 단어가 들어갔나요?"
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]에서 국어사전적 의미와 시적 함축 의미를 대조하고, [활동 2]~[활동 3]을 통해 역설과 은유를 해설하도록 지도한다. ‘내 글 씨앗 보관함’에 다의어를 활용한 은유 구절을 적으며 마무리한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 날개 질문 정답]</strong> ① 소중한 것들을 모두 잃어버린 극한의 상실과 절망의 상황 ② 모두가 포기한 절망 속에서도 남을 위해 먼저 따뜻한 희망과 사랑을 베푸는 사람<br>
                  <strong>• [활동 1 모범 답안]</strong> 길: 희망이나 가능성 / 살아갈 방법·구원 | 끝나다: 절망적 한계와 단절 | 봄(길): 따뜻한 사랑과 희망의 길<br>
                  <strong>• [활동 2 모범 답안]</strong> 문맥 단서: 되는 사람, 보라, 사랑 | 심층 의미: 희생과 사랑<br>
                  <strong>• [활동 3 모범 답안]</strong> 표면적 모순(끝난 곳에 길이 있음), 문맥 단서(‘길이 되는 사람’, ‘봄길=사랑’), 심층 의미(절망 속에서도 타인을 위해 헌신하는 사랑을 통해 새 희망이 열림) 3요소가 포함되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "역설법(“길이 끝나는 곳에서도 길이 있다”)을 시인이 말을 잘못 쓴 문법 오류나 거짓말로 판단하는 경우",
                    "diagnosis": "문학의 역설(Paradox)이 표면적 모순을 통해 독자의 주의를 환기하고 더 깊은 진리를 전달하는 수사법임을 이해하지 못함.",
                    "prescription": "앞의 ‘길(물리적 길·기존의 희망)’과 뒤의 ‘길(사람이 스스로 만들어 내는 사랑의 봄길)’의 의미 층위가 다름을 보여 주어 모순이 해소되는 과정을 시각화한다."
                },
                {
                    "error_case": "‘봄길’을 단순히 ‘봄에 꽃이 예쁘게 핀 산책로’라는 사전적·표면적 의미로만 해석하는 경우",
                    "diagnosis": "2연의 ‘스스로 사랑이 되어 한없이 봄길을 걸어가는 사람’과의 대응 관계를 연결하지 못함.",
                    "prescription": "1연의 ‘스스로 봄길이 되어’와 2연의 ‘스스로 사랑이 되어’를 위아래로 포개어 보게 하여 ‘봄길 = 절망을 녹이는 따뜻한 사랑’임을 추론하게 한다."
                }
            ],
            "scaffolding_down": "다의어 ‘길’의 사전 뜻풀이 카드(① 땅 위에 낸 공간, ② 방법이나 수단, ③ 앞으로 나아갈 희망)를 제시하고, 시의 각 행에 어울리는 번호를 먼저 골라 보게 한다.",
            "scaffolding_up": "일상 속 역설적 표현(예: ‘작은 거인’, ‘소리 없는 아우성’, ‘지는 것이 이기는 것이다’)을 찾아보고, 〈봄길〉의 역설과 어떤 공통 원리가 있는지 비교해 보게 한다.",
            "rubric": {
                "high": "다의어의 사전적·함축적 의미를 정확히 대조하고, 텍스트 내적 단서 2가지 이상을 들어 역설과 은유(‘봄길’)의 심층 의미를 3단계 해설문으로 완벽히 작성함.",
                "mid": "다의어의 함축 의미와 ‘봄길’이 사랑을 뜻한다는 점은 추론했으나, 역설 표현의 표면적 모순과 문맥 단서 연결 설명이 다소 소략함.",
                "low": "시어를 사전적 의미로만 해석하거나 역설적 표현의 이면에 담긴 의미를 추론하는 데 교사의 안내가 필요함."
            }
        }
    },

    # =========================================================================
    # 6차시: G6-POE-V2-2 시적 상황·내적 인과 추론
    # =========================================================================
    {
        "lesson_title": "행간에 생략된 시적 상황과 내적 인과 과정 추론하기",
        "std_badge": "[6국02-03] [6국05-02]",
        "student_goal": "시 〈봄길〉에서 화자가 마주한 절망적 상황(원인)이 어떤 내면적 계기(매개)를 거쳐 희망과 헌신의 태도(결과)로 이어졌는지 생략된 행간의 내적 인과를 추론할 수 있다.",
        "marking_items": [
            ["mk-line-blue", "파란 밑줄", "화자가 마주한 시련·상실·절망의 상황 (원인)"],
            ["mk-bg", "네모", "시선과 인식을 바꾸는 전환점·매개 단서"],
            ["mk-line-red", "빨간 밑줄", "극복 의지와 헌신적 행동으로 나아가는 결과"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.8pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:7.3pt; font-weight:800; color:#6C3483;">🔎 [행간 추론 · 부분 자세히 읽기]</span>
                <strong style="font-size:9.5pt; color:#17202A; margin-left:5px;">봄길 (정호승) — 생략된 행간의 인과 고리 찾기</strong>
              </div>
              <span style="font-size:7.2pt; color:#6C3483; font-weight:700;">상황(원인) ➔ 매개(발견·성찰) ➔ 태도(결과)</span>
            </div>

            <table class="wing-reading-table">
              <thead>
                <tr>
                  <th>시 본문 (행간 [ ㉠ · ㉡ ]의 생략된 맥락 추론하며 읽기)</th>
                  <th class="wing-head">🧠 행간 인과 추론 가이드</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➊</span> <span class="mk-line-blue">길이 끝나는 곳에서도</span><br>
                    길이 있다<br>
                    <span class="mk-line-blue">길이 끝나는 곳에서도</span><br>
                    <span style="background:#FEF9E7; border:1pt dashed #D35400; padding:0 4px; font-size:8pt; font-weight:700; color:#D35400;">[ ㉠ 생략된 행간 1 ]</span><br>
                    <span class="mk-bg">길이 되는 사람이 있다</span><br>
                    <span class="mk-line-red">스스로 봄길이 되어</span><br>
                    <span class="mk-line-red">끝없이 걸어가는 사람이 있다</span></p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box guide u2">
                      <div class="wing-box-title"><span>🎙️ 행간 [㉠] 인과 추론</span><span class="role-chip">시범 I Do</span></div>
                      <div class="think-row"><span class="think-tag">[질문]</span><span>길이 끝난 절망적인 곳에서 어떻게 갑자기 ‘길이 있다’는 결과로 넘어갈 수 있었을까?</span></div>
                      <div class="think-row"><span class="think-tag">[단서]</span><span>4~5행의 ‘길이 되는 사람’, ‘스스로 봄길이 되어’가 바로 숨은 원인(매개)이야!</span></div>
                      <div class="think-row"><span class="think-tag">[정리]</span><span>누군가 주저앉지 않고 <strong>‘뒤따라올 사람들을 위해 자기 자신이 길이 되어 주기로 결심했기 때문에’</strong> 다시 길이 생긴 거구나!</span></div>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➋</span> <span class="mk-line-blue">강물은 흐르다가 멈추고</span><br>
                    <span class="mk-line-blue">새들은 날아가 돌아오지 않고</span><br>
                    <span class="mk-line-blue">하늘과 땅 사이의 모든 꽃잎은 흩어져도</span><br>
                    <span class="mk-bg">보라</span> &nbsp; <span style="background:#FEF9E7; border:1pt dashed #D35400; padding:0 4px; font-size:8pt; font-weight:700; color:#D35400;">[ ㉡ 생략된 행간 2 ]</span><br>
                    <span class="mk-line-blue">사랑이 끝난 곳에서도</span><br>
                    <span class="mk-line-red">사랑으로 남아 있는 사람이 있다</span><br>
                    <span class="mk-line-red">스스로 사랑이 되어</span><br>
                    <span class="mk-line-red">한없이 봄길을 걸어가는 사람이 있다</span></p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 1 (양보 구문)</span><span class="role-chip">함께 We Do</span></div>
                      <div>2연 3행의 연결 어미 <strong>‘흩어<u>져도</u>’(-아도/어도)</strong>는 앞의 절망적 상황과 뒤의 결과를 어떤 논리 관계로 이어 주나요?</div>
                      <span class="pencil-line">✏️ 논리 관계: <span class="t-ans">비록 모든 것이 사라지는 절망적인 조건이라도 결코 굴복하지 않는다는 양보·역접 관계</span></span>
                    </div>
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 2 (행간 [㉡])</span><span class="role-chip">스스로 You Do</span></div>
                      <div>화자가 “보라”라고 외친 순간([㉡]), 화자는 무엇을 발견했기에 절망에서 희망으로 시선이 바뀌었을까요?</div>
                      <span class="pencil-line">✏️ 발견한 것: <span class="t-ans">사랑이 끝난 자리에서도 끝까지 사랑으로 남아 헌신하는 사람을 발견함</span></span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
        """,
        "activity_1": {
            "title": "시적 화자가 마주한 외적 상황(원인)과 최종 태도(결과) 단서 찾기",
            "tag": "Step 1 원인·결과 상황 식별 (V2-2 + COM-A4·A5)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:24%;">구분</th>
                      <th style="width:42%;">시 속 명시적 구절 찾기</th>
                      <th style="width:34%;">시적 상황의 의미</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 위기·결핍 상황<br>(외적 원인)</strong></td>
                      <td>• 1연: 길이 <span class="blank-slot"><span class="t-ans">끝나는 곳</span></span><br>• 2연: 강물은 <span class="blank-slot"><span class="t-ans">멈추고</span></span>, 새들은 돌아오지 않고, 꽃잎은 <span class="blank-slot"><span class="t-ans">흩어져도</span></span>, 사랑이 끝난 곳</td>
                      <td>삶의 희망이 끊어지고 소중한 존재들과 이별·단절된 극한의 상실 상태</td>
                    </tr>
                    <tr>
                      <td><strong>② 전환 표지 (환기)</strong></td>
                      <td>• 양보 연결 어미: ‘~흩어<span class="blank-slot"><span class="t-ans">져도</span></span>’<br>• 명령형 감탄 시어: “<span class="blank-slot"><span class="t-ans">보라</span></span>” (2연 4행)</td>
                      <td>절망에 빠진 독자와 화자 자신의 시선을 새로운 희망의 주체에게로 돌리는 전환점</td>
                    </tr>
                    <tr>
                      <td><strong>③ 인식 전환과 극복<br>(내적 결과)</strong></td>
                      <td>• 1연: 스스로 <span class="blank-slot"><span class="t-ans">봄길이 되어</span></span> 끝없이 걸어가는 사람<br>• 2연: 스스로 <span class="blank-slot"><span class="t-ans">사랑이 되어</span></span> 한없이 봄길을 걸어가는 사람</td>
                      <td>누군가 길이나 사랑을 주기를 기다리지 않고, 자기 자신이 직접 희망과 사랑의 주체가 됨</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 원인(절망)과 결과(희망) 사이에 생략된 '내면의 성찰과 매개 과정'을 3단 도미노로 연결하기",
        "activity_2": {
            "title": "생략된 행간([㉠]·[㉡])을 메우는 3단계 내적 인과 도해조직자",
            "tag": "Step 2 생략된 매개 인과 연결 (V2-2 + COM-A5)",
            "body_html": """
                <div class="inference-row">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">[원인] 극한의 절망과 상실</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 길이 끝나고 강물이 멈춤<br>
                      • 새가 떠나고 꽃잎이 흩어짐<br>
                      • 믿었던 <span class="blank-slot"><span class="t-ans">사랑</span></span>마저 끝난 한계 상황 직면
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">[매개: 생략된 내면 성찰 ㉠·㉡]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • <strong>깨달음 1</strong>: 길이 없다고 주저앉으면 영원히 끝이지만, 내가 직접 <span class="blank-slot"><span class="t-ans">길이 되어 주면</span></span> 새 길이 열림.<br>
                      • <strong>깨달음 2 (“보라”)</strong>: 상실 속에서도 끝까지 <span class="blank-slot"><span class="t-ans">사랑으로 남아 있는 사람</span></span>의 숭고함을 목격함.
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#6C3483;">[결과] 주체적 헌신과 희망</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 스스로 따뜻한 <span class="blank-slot"><span class="t-ans">봄길</span></span>과 <span class="blank-slot"><span class="t-ans">사랑</span></span>이 됨<br>
                      • ‘끝없이 / 한없이’ 걸어가는 강인한 생명력과 구원의 태도 확립
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 2]에서 복원한 다단계 내적 인과 고리를 바탕으로 한 문단 분석 글 쓰기",
        "activity_3": {
            "title": "시에 압축·생략된 상황과 심리 변화의 인과 과정을 한 문단으로 재구성하기",
            "tag": "Step 3 다단계 내적 인과 산출 (V2-2)",
            "body_html": """
                <div style="font-size:7.4pt; margin-bottom:3px;"><strong>[조건]</strong> <code>[원인 상황] ➔ [‘보라’에 담긴 내면적 깨달음(매개)] ➔ [최종 태도 변화(결과)]</code>의 인과 연결어(‘비록 ~하지만, 왜냐하면 ~이기 때문에, 그 결과 ~한다’)를 사용하여 한 문단으로 서술하세요.</div>
                <span class="pencil-line">✏️ 인과 재구성 문장 1: <span class="t-ans">비록 길이 끊어지고 강물이 멈추며 꽃잎이 흩어지는 절망적인 상실의 상황(원인)에 부딪혔지만, 화자는 결코 좌절하지 않는다.</span></span>
                <span class="pencil-line">✏️ 인과 재구성 문장 2: <span class="t-ans">왜냐하면 사랑이 끝난 자리에서도 포기하지 않고 스스로 봄길과 사랑이 되어 타인을 위해 헌신하는 사람을 발견하고 깊은 깨달음(매개)을 얻었기 때문이다. 그 결과 화자는 절망의 끝에서 다시 시작되는 영원한 희망과 사랑을 확신하게 된다(결과).</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 14차시(W3 내용 조직) 시련 ➔ 깨달음(전환) ➔ 다짐의 인과 구조 씨앗",
            "prompt": "내가 겪었던 어려움이나 속상했던 상황(원인)이 어떤 계기나 생각(매개)을 통해 새로운 다짐(결과)으로 바뀌었는지 인과 화살표로 메모해 보세요.",
            "placeholder": "예: 달리기에서 넘어져 꼴찌를 함(원인) ➔ 손을 잡아 준 친구의 따뜻한 손길(매개) ➔ 나도 넘어진 친구를 일으켜 주는 사람이 되기로 함(결과)",
            "example_answer": "비 오는 날 우산이 없어 막막함(원인) ➔ 자기 어깨가 젖으면서도 우산을 씌워 준 친구의 배려(매개) ➔ 나도 누군가의 비를 가려 주는 따뜻한 우산이 되겠다고 다짐함(결과)"
        },
        "self_check": [
            "화자가 처한 절망적 상황(원인)과 극복 의지(결과)를 나타내는 시 구절을 정확히 찾았나요?",
            "시행 사이에 생략된 내면의 성찰 과정(‘보라’, ‘스스로 ~이 되어’)을 논리적으로 추론했나요?",
            "원인-매개-결과의 인과 고리가 잘 드러나도록 한 문단의 분석 글로 재구성했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[행간 인과 다리 놓기] [원인: 길·강물·새·꽃잎·사랑이 끝난 절망] ──(양보 '-어도' + 환기 '보라!' + 숨은 매개: 누군가 받기를 기다리지 않고 스스로 봄길·사랑이 되는 사람의 존재 발견)──> [결과: 끝없이/한없이 봄길을 걸어가는 희망과 헌신]",
            "intro_5min": "시는 소설이나 설명문과 달리 ‘왜냐하면’, ‘그래서’ 같은 접속어를 생략하고 압축해서 쓴다는 점을 환기한다. 〈봄길〉의 시행과 시행 사이(행간)에 숨겨진 시인의 마음속 징검다리를 찾아보는 탐정 활동을 안내한다.",
            "ido_think_aloud_script": "“1연을 다시 볼까요? ‘길이 끝나는 곳’은 절망(원인)인데, 바로 다음 줄에 ‘길이 있다’는 희망(결과)이 나와요. 이 두 줄 사이[㉠]에는 무슨 일이 있었던 걸까요? 4~5행을 보니 ‘길이 되는 사람이 있다 / 스스로 봄길이 되어’라고 했어요. 즉, ‘길이 없네, 어떡하지?’ 하고 주저앉는 대신 ‘내가 직접 얼어붙은 땅을 녹이는 봄길이 되어 걸어가자!’라고 마음을 바꾼 내면의 결단(매개)이 있었기 때문에 길이 새로 열린 거랍니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "2연 1~3행에서 강물이 멈추고 새가 떠나고 꽃잎이 흩어진다는 세 가지 절망적 문장 끝에 어떤 글자(어미)가 붙어 있나요?",
                    "expected_ans": "‘흩어져도’의 ‘-어도’라는 어미가 붙어 있어요. 아무리 나쁜 상황이 닥쳐도 뒤에 나오는 희망을 막을 수 없다는 뜻을 나타내요.",
                    "reprompt": "‘꽃잎이 흩어져서 슬프다’라고 끝났나요, 아니면 ‘꽃잎은 흩어져도’라고 이어졌나요? ‘비록 ~하더라도’의 뜻을 가진 연결 어미를 주목해 보세요."
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "2연 4행에는 단 두 글자, ‘보라’만 단독 행으로 놓여 있어요. 시인은 왜 이 자리에 ‘보라’를 넣었을까요?",
                    "expected_ans": "1~3행의 슬프고 절망적인 풍경에만 빠져 있지 말고, 고개를 들어 사랑이 끝난 곳에서도 사랑으로 남아 있는 위대한 사람을 바라보라고 시선을 전환시키기 위해서예요.",
                    "reprompt": "절망에 빠져 땅만 쳐다보고 있는 사람에게 “자, 고개를 들고 저기를 보라!” 하고 외치면 마음과 시선이 어떻게 바뀔까요?"
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]에서 원인·전환·결과 단서를 찾고, [활동 2]의 3단 인과 도해조직자를 거쳐 [활동 3] 한 문단 인과 분석 글을 완성하도록 지도한다. ‘내 글 씨앗 보관함’에 자신의 경험 속 인과 전환을 기록하게 한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 날개 질문 정답]</strong> ① 비록 모든 것이 사라지는 절망적 조건이라도 굴복하지 않는다는 양보·역접 관계 ② 사랑이 끝난 자리에서도 끝까지 사랑으로 남아 헌신하는 사람을 발견함<br>
                  <strong>• [활동 1 모범 답안]</strong> ① 끝나는 곳 / 멈추고, 흩어져도 ② 져도 / 보라 ③ 봄길이 되어 / 사랑이 되어<br>
                  <strong>• [활동 2 모범 답안]</strong> [원인] 사랑 [매개] 길이 되어 주면 / 사랑으로 남아 있는 사람 [결과] 봄길, 사랑<br>
                  <strong>• [활동 3 모범 답안]</strong> 원인(절망·상실 상황), 매개(스스로 봄길·사랑이 되는 사람의 발견과 내면적 성찰), 결과(영원한 희망과 헌신적 태도)가 인과 표지와 함께 연결되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "2연 1~3행(강물 멈춤·새 떠남·꽃잎 흩어짐)을 ‘길이 다시 열리는 원인’으로 잘못 연결하는 경우",
                    "diagnosis": "‘~흩어져도’의 양보(-아도/어도) 구문을 순접 인과(-아서/어서)로 혼동함.",
                    "prescription": "‘비가 와서 소풍을 못 갔다(원인)’와 ‘비가 와도 소풍을 갔다(양보·극복 조건)’를 비교하여, 1~3행은 극복해야 할 극한의 시련 조건임을 명확히 구분해 준다."
                },
                {
                    "error_case": "누가 봄길을 만들어 주었는지에 대해 ‘시간이 지나서 저절로 봄이 왔다’고 추론하는 경우",
                    "diagnosis": "시 속 핵심 부사어인 ‘스스로(자기 자신이 직접)’의 의미를 간과함.",
                    "prescription": "1연 5행과 2연 7행에 반복된 ‘스스로’에 형광펜을 칠하게 하여, 자연의 계절 변화가 아니라 인간의 주체적인 결단과 희생이 매개였음을 확인시킨다."
                }
            ],
            "scaffolding_down": "‘비록 [절망 상황]이지만 ➔ 왜냐하면 [누군가 스스로 ~이 되었기] 때문이다 ➔ 그래서 [희망의 결과]가 열린다’ 문장 틀 카드를 제공하여 빈칸을 먼저 채워 보게 한다.",
            "scaffolding_up": "만약 2연 4행의 ‘보라’ 앞뒤에 생략된 시적 화자의 속마음 독백 2행을 추가로 써 넣는다면 어떤 시행이 어울릴지 창작해 보게 한다.",
            "rubric": {
                "high": "시적 화자가 처한 절망적 상황(원인)과 내면적 전환 계기(매개: ‘보라’, ‘스스로 ~이 되어’), 태도 변화(결과)의 다단계 내적 인과를 90% 이상 정확히 추론하여 완결된 분석 문단으로 작성함.",
                "mid": "원인 상황과 결과 태도는 찾았으나, 행간에 생략된 내면적 성찰(매개 과정)에 대한 서술이 다소 간단함.",
                "low": "양보 구문(‘~흩어져도’)의 논리 관계를 파악하지 못하거나 인과 순서를 반대로 연결함."
            }
        }
    },

    # =========================================================================
    # 7차시: G6-POE-V2-3 화자 정서·태도·가치관 추론
    # =========================================================================
    {
        "lesson_title": "어조와 시어 선택을 단서로 화자의 정서 전환과 가치관 추론하기",
        "std_badge": "[6국05-02] [6국05-04]",
        "student_goal": "시 〈봄길〉의 어조 변화와 반복 시어(‘스스로, 끝없이, 한없이’)를 단서로 절망에서 희망·헌신으로 나아가는 화자의 정서 전환과 삶의 가치관을 추론하고 시 구절을 인용해 논술할 수 있다.",
        "marking_items": [
            ["mk-line-red", "빨간 밑줄", "화자의 확신에 찬 단정적·감탄적 어조(‘~있다’, ‘보라’)"],
            ["mk-highlight", "형광펜", "화자가 가장 소중하게 여기는 삶의 태도를 보여 주는 부사어"],
            ["mk-person", "동그라미", "화자가 예찬하고 닮고자 하는 이상적인 인간상"],
        ],
        "left_page_body_html": """
            <div style="background:#F6F0F9; border:0.8pt solid #C39BD3; border-radius:5px; padding:5px 9px; margin-bottom:5px; display:flex; justify-content:space-between; align-items:center;">
              <div>
                <span style="font-size:7.3pt; font-weight:800; color:#6C3483;">🧭 [화자의 정서·태도·가치관 심층 추론]</span>
                <strong style="font-size:9.5pt; color:#17202A; margin-left:5px;">봄길 (정호승) — 어조·시선·가치관 분석</strong>
              </div>
              <span style="font-size:7.2pt; color:#6C3483; font-weight:700;">어조·부사어 단서 ➔ 삶의 가치관 도출</span>
            </div>

            <table class="wing-reading-table">
              <thead>
                <tr>
                  <th>시 본문 (어조·부사어·종결 표현에 주목하며 읽기)</th>
                  <th class="wing-head">🧠 어조·가치관 추론 가이드</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➊</span> 길이 끝나는 곳에서도<br>
                    길이 <span class="mk-line-red">있다</span><br>
                    길이 끝나는 곳에서도<br>
                    <span class="mk-person">길이 되는 사람</span>이 <span class="mk-line-red">있다</span><br>
                    <span class="q-num">①</span><span class="mk-highlight">스스로</span> 봄길이 되어<br>
                    <span class="q-num">②</span><span class="mk-highlight">끝없이</span> 걸어가는 <span class="mk-person">사람</span>이 <span class="mk-line-red">있다</span></p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box guide u2">
                      <div class="wing-box-title"><span>🎙️ 어조·태도 생각 읽기</span><span class="role-chip">시범 I Do</span></div>
                      <div class="think-row"><span class="think-tag">[질문]</span><span>1연에서는 왜 문장 끝마다 ‘~있다, ~있다, ~있다’를 세 번이나 반복했을까?</span></div>
                      <div class="think-row"><span class="think-tag">[단서]</span><span>‘~일지도 모른다’ 같은 추측이 아니라 <strong>‘~있다’라는 현재형 단정 어조</strong>를 반복했어.</span></div>
                      <div class="think-row"><span class="think-tag">[정리]</span><span>절망 속에서도 반드시 희망의 사람이 존재한다는 화자의 <strong>굳건한 믿음과 확신</strong>을 드러내는구나!</span></div>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="text-col">
                    <p style="text-indent:0;"><span class="p-num">➋</span> 강물은 흐르다가 멈추고<br>
                    새들은 날아가 돌아오지 않고<br>
                    하늘과 땅 사이의 모든 꽃잎은 흩어져도<br>
                    <span class="q-num">③</span><span class="mk-line-red">보라</span><br>
                    사랑이 끝난 곳에서도<br>
                    <span class="mk-person">사랑으로 남아 있는 사람</span>이 <span class="mk-line-red">있다</span><br>
                    <span class="mk-highlight">스스로</span> 사랑이 되어<br>
                    <span class="q-num">④</span><span class="mk-highlight">한없이</span> 봄길을 걸어가는 <span class="mk-person">사람</span>이 <span class="mk-line-red">있다</span></p>
                  </td>
                  <td class="wing-col">
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 1 (부사어의 힘)</span><span class="role-chip">함께 We Do</span></div>
                      <div>시인이 선택한 부사어 <span class="q-num">①</span>‘스스로’와 <span class="q-num">②</span>‘끝없이’·<span class="q-num">④</span>‘한없이’는 봄길을 걷는 사람의 어떤 태도를 보여 주나요?</div>
                      <span class="pencil-line">✏️ 태도: <span class="t-ans">누가 시켜서가 아니라 자발적으로(스스로), 포기하지 않고 영원히(끝없이·한없이) 헌신하는 태도</span></span>
                    </div>
                    <div class="wing-box question">
                      <div class="wing-box-title"><span>🙋 날개 질문 2 (가치관 추론)</span><span class="role-chip">스스로 You Do</span></div>
                      <div>이 시의 화자가 가장 아름답고 가치 있다고 여기는 삶의 모습은 무엇인가요?</div>
                      <span class="pencil-line">✏️ 가치관: <span class="t-ans">시련 속에서도 남을 위해 자신을 내어 주는 이타적 사랑과 헌신의 삶</span></span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
        """,
        "activity_1": {
            "title": "화자의 어조 변화와 핵심 시어(부사어·서술어) 선택 단서 분석하기",
            "tag": "Step 1 어조·시선·시어 식별 (V2-3 + COM-A2)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:24%;">분석 기준</th>
                      <th style="width:36%;">시 속 언어적 단서</th>
                      <th style="width:40%;">화자의 정서 및 태도 효과</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 종결 어미의 반복</strong></td>
                      <td>1~2연에서 <strong>‘~ <span class="blank-slot"><span class="t-ans">있다</span></span>’</strong>를 총 5회 반복함</td>
                      <td>차분하면서도 흔들림 없는 <strong>단정적·확신적 어조</strong>로 절망을 이기는 힘에 대한 믿음을 전달함.</td>
                    </tr>
                    <tr>
                      <td><strong>② 어조의 고조(환기)</strong></td>
                      <td>2연 4행의 명령형 단독 시행: <strong>“<span class="blank-slot"><span class="t-ans">보라</span></span>”</strong></td>
                      <td>상실의 슬픔을 단숨에 끊어 내고, 숭고한 사랑의 존재를 향해 독자의 주의를 강렬하게 환기함.</td>
                    </tr>
                    <tr>
                      <td><strong>③ 핵심 부사어 선택</strong></td>
                      <td>• 주체성: <span class="blank-slot"><span class="t-ans">스스로</span></span> (2회 반복)<br>• 지속성: <span class="blank-slot"><span class="t-ans">끝없이, 한없이</span></span></td>
                      <td>대가를 바라거나 남이 해 주기를 기다리지 않는 <strong>자발적 헌신</strong>과 <strong>끈기 있는 사랑</strong>을 강조함.</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]에서 분석한 어조·시어 단서를 연결하여 화자의 정서 전환과 삶의 가치관 도해하기",
        "activity_2": {
            "title": "화자의 정서 전환 과정과 지향하는 삶의 가치관 구조도",
            "tag": "Step 2 태도·가치관 연결 (V2-3)",
            "body_html": """
                <div class="inference-row" style="grid-template-columns:1fr 18px 1fr 18px 1.15fr;">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">😢 [출발점: 세상의 통념]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 길이 끝나고 사랑이 끝나면 모든 것이 끝났다고 여기는 <strong>절망과 체념</strong>의 정서
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">🔥 [정서·태도의 전환]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • “보라!” — 절망을 딛고 일어서는 사람에 대한 <strong>경외감·예찬·희망</strong>으로 정서 전환
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#6C3483;">💎 [화자의 삶의 가치관]</strong>
                    <div style="margin-top:3px; font-size:7.2pt; line-height:1.42;">
                      • 진정한 사랑과 희망은 조건이 좋을 때가 아니라, <strong><span class="blank-slot"><span class="t-ans">모두가 떠나고 끝난 자리</span></span>에서 스스로를 내어 줄 때</strong> 완성된다는 <strong><span class="blank-slot"><span class="t-ans">이타적 헌신</span></span></strong>의 가치관
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 2]에서 추론한 화자의 가치관을 시 구절 3곳 이상을 인용하여 논술하기",
        "activity_3": {
            "title": "시 구절 3곳 이상을 인용하여 화자가 지향하는 삶의 가치관 논술하기",
            "tag": "Step 3 가치관 인용 논술 (V2-3)",
            "body_html": """
                <div style="font-size:7.4pt; margin-bottom:3px;"><strong>[조건]</strong> 이 시의 화자가 가장 소중하게 여기는 <strong>삶의 가치관</strong>을 한 문장으로 정의하고, 이를 뒷받침하는 <strong>시 구절을 작은따옴표(‘ ’)로 3곳 이상 직접 인용</strong>하여 서술하세요.</div>
                <span class="pencil-line">✏️ 화자의 가치관 정의: <span class="t-ans">이 시의 화자는 절망의 순간에도 타인을 위해 기꺼이 자신을 바치는 ‘자발적 헌신과 조건 없는 사랑’을 최고의 가치로 여긴다.</span></span>
                <span class="pencil-line">✏️ 시 구절 3곳 인용 근거: <span class="t-ans">왜냐하면 화자는 ‘길이 끝나는 곳에서도 길이 되는 사람’과 ‘사랑이 끝난 곳에서도 사랑으로 남아 있는 사람’을 예찬하며, 누구의 강요도 없이 ‘스스로 봄길이 되어 끝없이 걸어가는’ 이타적인 삶의 태도를 힘주어 노래하고 있기 때문이다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 12차시(W1 계획하기) & 15차시(W4 집필하기) 내 시의 어조와 가치관 설정 씨앗",
            "prompt": "내가 쓸 시에서는 어떤 목소리(어조: 다정한 말투, 확신에 찬 말투, 조용히 다짐하는 말투 등)로 어떤 삶의 가치를 노래하고 싶은지 적어 보세요.",
            "placeholder": "예: 어조(‘~하자’ 청유형 어조) / 가치관(작고 느린 친구를 기다려 주는 배려의 가치)",
            "example_answer": "어조: 조용하지만 단단한 확신의 어조(‘~이다, ~있다’) / 가치관: 눈에 띄지 않는 자리에서도 묵묵히 남을 받쳐 주는 성실함과 배려의 가치"
        },
        "self_check": [
            "반복되는 종결 어미(‘~있다’)와 감탄어(‘보라’), 부사어(‘스스로, 끝없이’)의 효과를 파악했나요?",
            "절망에서 희망과 예찬으로 나아가는 화자의 정서 전환 과정을 정확히 추론했나요?",
            "시 구절 3곳 이상을 정확히 인용하여 화자가 지향하는 삶의 가치관을 논리적으로 서술했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[어조 온도계] 1~3행(차분한 단정 '~있다') ➔ 2연 1~3행(상실의 고조) ➔ 2연 4행('보라!' 강렬한 환기·전환) ➔ 2연 5~8행(숭고한 예찬과 확신 '한없이 ~ 있다') / [가치관 3대 키워드] '스스로'(자발성) + '봄길·사랑이 되어'(자기희생·헌신) + '끝없이·한없이'(영원성)",
            "intro_5min": "같은 문장이라도 끝말을 ‘~있을까?’, ‘~있겠지.’, ‘~있다!’, ‘보라!’로 바꿀 때 말하는 사람의 태도와 마음의 힘이 어떻게 달라지는지 직접 소리 내어 읽어 보며 시의 ‘어조(Tone)’ 개념을 도입한다.",
            "ido_think_aloud_script": "“선생님은 이 시를 읽을 때 ‘스스로’라는 부사어가 가슴에 깊이 박혔어요. ‘누군가 만들어 준 봄길을 걸어가는 사람’이 아니라 ‘스스로 봄길이 되어’ 걸어간다고 했잖아요. 내가 꽃길 위를 편하게 걷는 사람이 아니라, 내 몸을 낮추어 다른 사람이 걸어갈 따뜻한 봄길 자체가 되어 준다는 뜻이에요. 여기서 화자가 얼마나 이타적이고 헌신적인 삶의 가치관을 지니고 있는지 추론할 수 있답니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "1연 6행의 ‘끝없이’와 2연 8행의 ‘한없이’는 화자가 생각하는 사랑의 어떤 특징을 보여 주나요?",
                    "expected_ans": "잠깐 도와주고 멈추는 것이 아니라, 공간적으로나 시간적으로나 한계를 두지 않고 영원히 이어지는 끈기 있고 무조건적인 사랑을 보여 줘요.",
                    "reprompt": "‘조금만 걸어가는 사람’과 ‘끝없이, 한없이 걸어가는 사람’의 마음가짐은 어떻게 다를까요?"
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "우리가 1~4차시에서 읽은 〈구부러진 길〉의 화자와 〈봄길〉의 화자는 어떤 공통된 삶의 가치관을 가지고 있나요?",
                    "expected_ans": "두 화자 모두 자기 혼자만 쉽고 편하게 살아가는 것보다, 시련 속에서도 가족과 이웃을 품고 남을 위해 따뜻한 길이 되어 주는 더불어 사는 삶을 소중하게 여겨요.",
                    "reprompt": "〈구부러진 길〉의 ‘가족을 품고 이웃을 품고 가는 사람’과 〈봄길〉의 ‘스스로 봄길이 되어 걸어가는 사람’의 닮은 점을 찾아보세요!"
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]·[활동 2]를 통해 어조와 가치관을 정리한 뒤, [활동 3]에서 작은따옴표로 시 구절 3곳 이상을 직접 인용하여 가치관 논술문을 작성하도록 지도한다. 텍스트 근거 인용법을 꼼꼼히 피드백한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 날개 질문 정답]</strong> ① 누가 시켜서가 아니라 자발적으로(스스로), 포기하지 않고 영원히(끝없이·한없이) 헌신하는 태도 ② 시련 속에서도 남을 위해 자신을 내어 주는 이타적 사랑과 헌신의 삶<br>
                  <strong>• [활동 1 모범 답안]</strong> ① 있다 ② 보라 ③ 스스로 / 끝없이, 한없이<br>
                  <strong>• [활동 2 모범 답안]</strong> 모두가 떠나고 끝난 자리 / 이타적 헌신<br>
                  <strong>• [활동 3 모범 답안]</strong> 화자의 가치관(이타적 헌신·자발적 사랑·희망) 정의 + 시 구절 3곳 이상 직접 인용(‘길이 끝나는 곳에서도 길이 되는 사람’, ‘스스로 봄길이 되어’, ‘사랑이 끝난 곳에서도 사랑으로 남아 있는 사람’, ‘스스로 사랑이 되어’ 등)이 모두 충족되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "화자의 정서를 2연 1~3행(‘강물은 멈추고…’)만 보고 ‘슬픔과 절망, 체념’이라고 답하는 경우",
                    "diagnosis": "대비를 위해 제시된 배경 상황(절망적 조건)과 화자의 중심 정서(극복 의지·예찬·희망)를 혼동함.",
                    "prescription": "2연 1~3행은 화자가 ‘보라!’를 외치며 뛰어넘고자 하는 디딤돌(배경 상황)이며, 진짜 정서는 5~8행의 확신과 예찬에 있음을 구분해 준다."
                },
                {
                    "error_case": "[활동 3] 논술문에서 시 구절을 직접 인용하지 않고 자기 생각만 막연하게 적는 경우",
                    "diagnosis": "문학 논술에서 ‘텍스트 내적 근거 인용’의 중요성과 작은따옴표 인용 형식을 숙지하지 못함.",
                    "prescription": "교과서 본문에서 형광펜 친 구절 3개를 먼저 골라 번호를 매긴 뒤, 작은따옴표(‘ ’) 안에 넣어 문장에 자연스럽게 결합하는 시범을 보여 준다."
                }
            ],
            "scaffolding_down": "인용할 수 있는 핵심 시 구절 4개를 보기로 제시하고, 그중 3개를 골라 ‘화자는 ‘___’, ‘___’, ‘___’라고 노래하며 ~한 가치관을 보여 준다.’ 틀에 넣어 완성하게 한다.",
            "scaffolding_up": "〈구부러진 길〉의 화자와 〈봄길〉의 화자가 만나 대화를 나눈다면 서로 어떤 말을 건넬지 4줄의 가상 대화문으로 작성해 보게 한다.",
            "rubric": {
                "high": "어조 변화(‘~있다’, ‘보라’)와 핵심 부사어를 단서로 화자의 정서 전환과 삶의 가치관을 심층 추론하고, 시 구절 3곳 이상을 정확히 인용하여 논술문을 완성함.",
                "mid": "화자의 정서 전환과 가치관은 파악했으나, 논술문에서 직접 인용한 시 구절이 1~2곳에 그침.",
                "low": "화자의 정서를 단순한 슬픔으로 오인하거나 시 구절 근거 없이 단편적인 감상만 적음."
            }
        }
    },

    # =========================================================================
    # 8차시: G6-POE-V2-4 작가(필자) 의도·관점·시점·맥락 추론
    # =========================================================================
    {
        "lesson_title": "시인의 삶과 시대 맥락을 연결하여 창작 의도와 주제 추론하기",
        "std_badge": "[6국05-02] [6국05-04]",
        "student_goal": "윤동주의 〈새로운 길〉과 도종환의 〈담쟁이〉 전문을 읽고, 시인의 삶·시대적 배경 맥락과 시의 핵심 상징을 연결하여 창작 의도를 추론하고 함축적인 새 제목을 붙일 수 있다.",
        "marking_items": [
            ["mk-person", "동그라미", "각 시에서 시련을 넘어 앞으로 나아가는 주체(‘나’, ‘담쟁이’)"],
            ["mk-bg", "네모", "극복해야 할 장애물·한계 공간(‘내, 고개’, ‘절망의 벽’)"],
            ["mk-highlight", "형광펜", "시인의 창작 의도와 주제가 응축된 핵심 시행"],
        ],
        "left_page_body_html": """
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-bottom:4px;">
              <!-- (가) 윤동주, 새로운 길 (전문 5연 10행) -->
              <div class="inline-segment-box" style="margin-bottom:0; padding:6px 8px;">
                <div style="font-family:var(--font-sans); font-size:7.4pt; font-weight:800; color:#6C3483; border-bottom:0.7pt solid #C39BD3; padding-bottom:2px; margin-bottom:4px; display:flex; justify-content:space-between;">
                  <span>(가) 새로운 길 (5연 10행 전문)</span>
                  <span style="color:#566573;">윤동주 (1938)</span>
                </div>
                <div style="font-size:8.4pt; line-height:1.52;">
                  <span class="p-num">➊</span> <span class="mk-bg">내</span>를 건너서 숲으로<br>
                  <span class="mk-bg">고개</span>를 넘어서 마을로<br><br>
                  <span class="p-num">➋</span> 어제도 가고 오늘도 갈<br>
                  <span class="mk-person">나의</span> 길 <span class="mk-highlight">새로운 길</span><br><br>
                  <span class="p-num">➌</span> 민들레가 피고 까치가 날고<br>
                  아가씨가 지나고 바람이 일고<br><br>
                  <span class="p-num">➍</span> <span class="mk-highlight">나의 길은 언제나 새로운 길</span><br>
                  <span class="mk-highlight">오늘도…… 내일도……</span><br><br>
                  <span class="p-num">➎</span> 내를 건너서 숲으로<br>
                  고개를 넘어서 마을로
                </div>
              </div>

              <!-- (나) 도종환, 담쟁이 (전문 13행) -->
              <div class="inline-segment-box" style="margin-bottom:0; padding:6px 8px;">
                <div style="font-family:var(--font-sans); font-size:7.4pt; font-weight:800; color:#196F3D; border-bottom:0.7pt solid #82E0AA; padding-bottom:2px; margin-bottom:4px; display:flex; justify-content:space-between;">
                  <span>(나) 담쟁이 (13행 전문)</span>
                  <span style="color:#566573;">도종환 (1993)</span>
                </div>
                <div style="font-size:8.3pt; line-height:1.48;">
                  저것은 <span class="mk-bg">벽</span><br>
                  어쩔 수 없는 벽이라고 우리가 느낄 때<br>
                  그때<br>
                  <span class="mk-person">담쟁이는</span> 말없이 그 벽을 오른다<br>
                  물 한 방울 없고 씨앗 한 톨 살아남을 수 없는<br>
                  저것은 <span class="mk-bg">절망의 벽</span>이라고 말할 때<br>
                  담쟁이는 서두르지 않고 앞으로 나아간다<br>
                  <span class="mk-highlight">한 뼘이라도 꼭 여럿이 함께 손을 잡고 올라간다</span><br>
                  푸르게 절망을 다 덮을 때까지<br>
                  바로 그 절망을 잡고 놓지 않는다<br>
                  저것은 넘을 수 없는 벽이라고 고개를 떨구고 있을 때<br>
                  <span class="mk-highlight">담쟁이 잎 하나는 담쟁이 잎 수천 개를 이끌고</span><br>
                  <span class="mk-highlight">결국 그 벽을 넘는다</span>
                </div>
              </div>
            </div>

            <!-- 작가·시대 맥락 아카이브 카드 -->
            <div style="background:#F8F9F9; border:0.8pt solid #BDC3C7; border-left:3.5pt solid #6C3483; border-radius:5px; padding:4.5px 8px; margin-bottom:4px; font-size:7.2pt; line-height:1.38;">
              <div style="font-weight:800; color:#6C3483; margin-bottom:2px;">📚 [작가·시대 배경 맥락 자료실] 시인은 왜 이 시를 썼을까?</div>
              <div>• <strong>(가) 윤동주(1917~1945)와 〈새로운 길〉 창작 맥락</strong>: 일제강점기인 1938년 5월, 윤동주 시인이 고향 북간도를 떠나 서울 연희전문학교에 입학한 직후 쓴 시입니다. 민족의 자유를 빼앗긴 어두운 시대(내, 고개) 속에서도 좌절하지 않고, 배움과 성찰을 통해 민족과 이웃이 사는 ‘마을’로 나아가는 희망찬 소명의 길을 날마다 새롭게 걸어가겠다는 다짐을 담았습니다.</div>
              <div style="margin-top:2px;">• <strong>(나) 도종환(1954~)과 〈담쟁이〉 창작 맥락</strong>: 교사이자 시인이었던 작가가 학교 현장에서 해직되는 아픔과 사회적 시련을 겪던 시기(1993년 시집 『당신은 누구십니까』)에 발표한 시입니다. 혼자만의 힘으로는 도저히 넘을 수 없을 것 같은 현실의 높은 한계(‘절망의 벽’) 앞에서도, 작은 존재들이 서로 손을 잡고 연대하면 마침내 벽을 넘어 푸른 희망을 일굴 수 있다는 믿음을 노래했습니다.</div>
            </div>

            <div class="inline-bridge-box practice" style="margin-bottom:0;">
              <div style="font-weight:800; color:#2874A6;">🎙️ 맥락 연결 질문<br><span class="role-chip">함께 We Do</span></div>
              <div>
                시대·작가 맥락 자료를 참고할 때, (가)의 <strong>‘내·고개를 넘어가는 새로운 길’</strong>과 (나)의 <strong>‘절망의 벽을 오르는 담쟁이’</strong>는 각각 어떤 시대적·사회적 태도를 상징하나요?<br>
                <span class="pencil-line">✏️ 맥락 추론: <span class="t-ans">(가)는 일제강점기 시련을 넘어 날마다 새롭게 희망을 개척하는 태도, (나)는 현실의 높은 한계를 연대와 끈기로 함께 넘어서는 태도를 상징함.</span></span>
              </div>
            </div>
        """,
        "activity_1": {
            "title": "두 시의 시적 대상·상징과 시인의 삶·시대 맥락 단서 짝짓기",
            "tag": "Step 1 맥락·상징 식별 (V2-4)",
            "body_html": """
                <table class="std-table">
                  <thead>
                    <tr>
                      <th style="width:18%;">구분</th>
                      <th style="width:41%;">(가) 윤동주, 〈새로운 길〉 (1938)</th>
                      <th style="width:41%;">(나) 도종환, 〈담쟁이〉 (1993)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>① 시련·한계 상징</strong></td>
                      <td>건너야 할 <span class="blank-slot"><span class="t-ans">내(시내)</span></span>와 넘어야 할 <span class="blank-slot"><span class="t-ans">고개</span></span></td>
                      <td>물 한 방울, 씨앗 한 톨 살 수 없는 <span class="blank-slot"><span class="t-ans">절망의 벽</span></span></td>
                    </tr>
                    <tr>
                      <td><strong>② 극복 방식과 태도</strong></td>
                      <td>어제도 오늘도 내일도 날마다 <span class="blank-slot"><span class="t-ans">새로운 마음</span></span>으로 길을 걸어감</td>
                      <td>말없이 서두르지 않고 <span class="blank-slot"><span class="t-ans">여럿이 함께 손을 잡고</span></span> 올라감</td>
                    </tr>
                    <tr>
                      <td><strong>③ 시대·작가 맥락</strong></td>
                      <td>일제강점기의 암울한 현실 속에서도 배움과 양심의 길을 포기하지 않으려는 청년 윤동주의 다짐</td>
                      <td>사회적 시련과 거대한 장벽 앞에서도 작은 사람들의 <span class="blank-slot"><span class="t-ans">연대와 인내</span></span>로 희망을 만들려는 믿음</td>
                    </tr>
                  </tbody>
                </table>
            """
        },
        "arrow_1_to_2": "[활동 1]의 내적 상징과 외적 맥락(시대·작가)을 결합하여 창작 의도와 주제 의식 추론하기",
        "activity_2": {
            "title": "텍스트 내적 구조와 외적 맥락을 결합한 창작 의도 추론 도해",
            "tag": "Step 2 내적 구조 ↔ 외적 맥락 연결 (V2-4 + COM-A6)",
            "body_html": """
                <div class="inference-row">
                  <div class="inf-card c1">
                    <strong style="color:var(--mark-blue);">📜 [텍스트 내적 단서]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      • (가) 1연과 5연의 수미상관(‘내를 건너서 숲으로 / 고개를 넘어서 마을로’), ‘오늘도…… 내일도……’<br>
                      • (나) ‘우리(체념)’ vs ‘담쟁이(연대·도전)’ 대조
                    </div>
                  </div>
                  <div class="inf-symbol">+</div>
                  <div class="inf-card c2">
                    <strong style="color:var(--mark-green);">🌏 [작가·시대 외적 맥락]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      • (가) 1938년 식민지 시대의 어둠 속에서도 <span class="blank-slot"><span class="t-ans">공동체(마을)</span></span>와 미래를 향한 소명 의식<br>
                      • (나) 개인의 힘만으로는 넘기 힘든 사회적 시련과 <span class="blank-slot"><span class="t-ans">함께하는 힘</span></span>의 발견
                    </div>
                  </div>
                  <div class="inf-symbol">➔</div>
                  <div class="inf-card c3">
                    <strong style="color:#6C3483;">🎯 [시인의 창작 의도 추론]</strong>
                    <div style="margin-top:2px; font-size:7.2pt;">
                      • 두 시인 모두 시대의 시련 앞에 좌절하는 독자들에게 <strong><span class="blank-slot"><span class="t-ans">끊임없는 전진과 연대</span></span>를 통해 한계를 넘어설 수 있다는 용기와 희망</strong>을 전하고자 했다.
                    </div>
                  </div>
                </div>
            """
        },
        "arrow_2_to_3": "[활동 2]에서 추론한 주제 의식을 상징·비유적으로 압축하여 새 제목을 짓고 정당화하기",
        "activity_3": {
            "title": "주제 의식을 압축한 함축적 새 제목 창안 및 타당성 정당화하기",
            "tag": "Step 3 새 제목 창안·논술 (V2-4)",
            "body_html": """
                <div style="font-size:7.4pt; margin-bottom:3px;"><strong>[과제]</strong> (가) 〈새로운 길〉 또는 (나) 〈담쟁이〉 중 한 편(또는 두 편 통합)의 주제를 비유·상징적으로 압축한 <strong>새 제목</strong>을 짓고, <strong>[시대·작가 맥락] + [시 속 근거]</strong>를 결합해 그 타당성을 한 문단으로 정당화하세요.</div>
                <span class="pencil-line">✏️ 내가 창안한 새 제목: <span class="t-ans">〈손잡고 절망의 벽을 푸르게 넘는 기적〉 (또는 〈어둠의 고개를 넘어 마을로 가는 희망의 발걸음〉)</span></span>
                <span class="pencil-line">✏️ 타당성 정당화 논술: <span class="t-ans">도종환 시인이 사회적 시련 속에서 작은 존재들의 연대로 위기를 극복하고자 했던 창작 맥락과, 시 속에서 ‘여럿이 함께 손을 잡고’ 올라가 ‘푸르게 절망을 다 덮’고 결국 벽을 넘는 담쟁이의 모습을 결합하여 주제를 가장 상징적으로 압축했기 때문이다.</span></span>
            """
        },
        "writing_seed": {
            "transfer_tag": "➔ 12차시(W1 계획하기) 내 시의 창작 의도·목적 및 시점 수립 씨앗",
            "prompt": "오늘 두 시인이 시대와 삶의 아픔 속에서 희망을 건네려 시를 쓴 것처럼, 내가 시를 쓰는 ‘목적(독자에게 주고 싶은 위로·용기)’을 적어 보세요.",
            "placeholder": "예: 시험이나 친구 문제로 풀이 죽은 반 친구들에게 ‘천천히 함께 가자’는 위로를 건네기 위해",
            "example_answer": "초등학교 졸업을 앞두고 새로운 출발이 두려운 6학년 친구들에게, 우리가 함께 손을 잡으면 어떤 벽도 넘을 수 있다는 용기를 주기 위해 시를 쓰고 싶다."
        },
        "self_check": [
            "윤동주·도종환 시인의 삶과 시대적 배경이 시 속 상징(‘새로운 길’, ‘벽’, ‘담쟁이’)에 어떻게 투영되었는지 찾았나요?",
            "텍스트 내적 단서와 외적 맥락(시대·작가)을 결합하여 시인의 창작 의도를 깊이 있게 추론했나요?",
            "추론한 주제를 상징적으로 압축한 새 제목을 짓고 맥락과 시 구절 근거를 들어 타당성을 설명했나요?"
        ],
        "teacher_guide": {
            "board_plan_summary": "[상호텍스트 비교 매트릭스] (가) 윤동주 〈새로운 길〉(1938 일제강점기: 내·고개 ➔ 어제도 오늘도 내일도 걷는 새로운 길 ➔ 마을/공동체 지향) vs (나) 도종환 〈담쟁이〉(1993 사회적 시련기: 절망의 벽 ➔ 여럿이 손을 잡고 수천 개를 이끌고 넘음 ➔ 연대와 인내의 승리)",
            "intro_5min": "시 한 편을 읽을 때 시의 글자만 읽는 것보다 ‘그 시인이 어떤 시대에 어떤 아픔을 겪으며 이 시를 썼을까?’를 알면 시의 감동이 몇 배로 커진다는 점을 안내하며 윤동주 시인과 도종환 시인의 사진을 제시한다.",
            "ido_think_aloud_script": "“(가) 〈새로운 길〉을 그냥 읽으면 ‘민들레가 피고 까치가 날고’ 하는 밝은 산책 시처럼 보여요. 하지만 창작 연도인 ‘1938년 일제강점기’라는 시대 맥락을 겹쳐서 읽어 볼까요? 나라를 빼앗긴 답답한 시대에 시인은 ‘내(시내)’와 ‘고개’라는 시련을 넘어 사람들이 모여 사는 ‘마을’로 간다고 했어요. 그리고 4연에서 ‘나의 길은 언제나 새로운 길 / 오늘도…… 내일도……’라며 말줄임표 속에 어떤 고난이 와도 날마다 양심과 희망의 길을 걸어가겠다는 굳은 다짐을 숨겨 놓았답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "모아 생각(Think & Search)",
                    "question": "(나) 〈담쟁이〉에서 ‘우리(사람들)’와 ‘담쟁이’는 똑같은 ‘벽’을 보고 어떻게 서로 다른 태도를 보이나요?",
                    "expected_ans": "‘우리’는 어쩔 수 없는 벽, 절망의 벽이라고 말하며 고개를 떨구고 포기하지만, ‘담쟁이’는 말없이 서두르지 않고 여럿이 함께 손을 잡아 결국 그 벽을 넘어요.",
                    "reprompt": "2행, 6행, 11행에서 ‘우리가 느낄 때/말할 때/고개를 떨구고 있을 때’와 4행, 7~8행, 12~13행의 ‘담쟁이’의 행동을 대조해 보세요."
                },
                {
                    "qar_type": "작가와 나(Author & You)",
                    "question": "도종환 시인이 겪었던 시련의 맥락을 생각할 때, ‘한 뼘이라도 꼭 여럿이 함께 손을 잡고 올라간다’는 구절을 통해 독자에게 전하고 싶었던 진짜 의도는 무엇일까요?",
                    "expected_ans": "혼자서는 도저히 이겨 낼 수 없을 것 같은 큰 시련이나 사회의 벽도, 주변 이웃·동료들과 서로 손을 잡고 힘을 합치면(연대하면) 반드시 넘어설 수 있다는 용기를 주고자 했어요.",
                    "reprompt": "담쟁이 줄기에 달린 수많은 잎과 흡반이 벽을 오르는 모습을 사람 사는 세상에 비추어 생각해 보세요."
                }
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]·[활동 2]에서 내적 단서와 외적 맥락을 결합한 뒤, [활동 3]에서 함축적 새 제목을 짓고 정당화 글을 작성하도록 지도한다. ‘내 글 씨앗 보관함’에서 내 시의 창작 의도를 설정하며 추론적 이해 4차시(V2-1~V2-4)를 마무리한다.",
            "answer_key_html": """
                <div style="font-size:7.2pt; line-height:1.42;">
                  <strong>• [본문 브릿지 질문 정답]</strong> (가)는 일제강점기 시련을 넘어 날마다 새롭게 희망을 개척하는 태도, (나)는 현실의 높은 한계를 연대와 끈기로 함께 넘어서는 태도를 상징함<br>
                  <strong>• [활동 1 모범 답안]</strong> ① 내(시내), 고개 / 절망의 벽 ② 새로운 마음 / 여럿이 함께 손을 잡고 ③ 연대와 인내<br>
                  <strong>• [활동 2 모범 답안]</strong> 외적 맥락: 공동체(마을) / 함께하는 힘 | 창작 의도: 끊임없는 전진과 연대<br>
                  <strong>• [활동 3 모범 답안]</strong> 주제를 비유·상징적으로 압축한 새 제목과 함께 [시대·작가 맥락] + [시 속 구체적 구절 근거]가 모두 결합되어 서술되면 정답 인정.
                </div>
            """,
            "misconceptions": [
                {
                    "error_case": "시대적 맥락 자료만 그대로 베껴 적고 시 본문의 시어·상징(‘내, 고개, 마을’, ‘벽, 담쟁이’)과 연결하지 않는 경우",
                    "diagnosis": "외적 맥락(작가·시대)과 텍스트 내적 요소를 상호 텍스트적으로 결합하는 방법을 모르고 배경지식만 나열함.",
                    "prescription": "‘시대 맥락의 [시련/연대]가 시 속에서는 [고개·벽 / 손을 잡고 올라감]이라는 시어로 표현되었다’는 양방향 연결 화살표를 반드시 확인하게 한다."
                },
                {
                    "error_case": "새 제목을 지을 때 〈담쟁이의 특징〉, 〈윤동주의 일기〉처럼 설명문이나 단순 사실 제목으로 짓는 경우",
                    "diagnosis": "시의 제목이 지닌 ‘상징적·비유적 함축성’의 원리를 고려하지 못함.",
                    "prescription": "4차시(V1-4)에서 배운 새 제목 짓기를 떠올려, 시의 중심 이미지(‘푸른 손길’, ‘절망의 벽’, ‘희망의 고개’)와 주제가 함께 빛나는 문학적 제목으로 다듬게 한다."
                }
            ],
            "scaffolding_down": "시 속 시어 카드(‘내와 고개’, ‘마을’, ‘절망의 벽’, ‘여럿이 함께 손잡음’)와 시대 맥락 뜻풀이 카드를 선으로 먼저 이어 보게 한 뒤 빈칸을 작성하게 한다.",
            "scaffolding_up": "1~7차시에 배운 〈구부러진 길〉, 〈봄길〉과 오늘 배운 〈새로운 길〉, 〈담쟁이〉 네 편에 공통으로 흐르는 ‘길과 벽을 대하는 시인들의 태도’를 비교하여 한 문단으로 종합해 보게 한다.",
            "rubric": {
                "high": "시인의 삶·시대 맥락이 시어와 주제에 어떻게 투영되었는지 심층 추론하고, 주제를 상징·비유적으로 압축한 새 제목을 창안하여 맥락+텍스트 근거로 완벽히 정당화함.",
                "mid": "시대 맥락과 시어의 상징적 의미는 연결했으나, 새 제목의 정당화 서술에서 외적 맥락이나 내적 근거 중 한 가지가 부족함.",
                "low": "시 본문과 작가·시대 배경 자료를 별개로 파악하여 창작 의도를 추론하는 데 어려움이 있음."
            }
        }
    }
]
