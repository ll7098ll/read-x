# -*- coding: utf-8 -*-
"""
2단원: 이야기 (Narrative, unit2_narrative) — Batch 4 (12~16차시: W1 ~ W5 과정중심 이야기 쓰기 5단계)
읽기 모델 『꼴뚜기』와 100% 구조·전략 미러링 (계획 ➔ 생성 ➔ 조직 ➔ 초고 집필 ➔ 고쳐쓰기·출판)
"""

BATCH4 = [
    # =========================================================================
    # 12차시: G6-NAR-W1 계획하기 (주제·목적·독자·서술 시점 및 핵심 갈등 기획하기)
    # =========================================================================
    {
        "lesson_title": "[계획하기] 씨앗 보관함을 열어 이야기의 주제·서술 시점·핵심 갈등 기획하기",
        "std_badge": "[6국03-03] [6국05-03]",
        "student_goal": "1~11차시 읽기 과정에서 모은 ‘글쓰기 씨앗’을 소환하여, 내가 쓸 단편 이야기의 창작 목적, 예상 독자, 주제의식, 서술 시점(1인칭/3인칭)과 내·외적 핵심 갈등을 기획할 수 있다.",
        "marking_items": [
            ("mk-person", "동그라미", "중심 시점 인물"),
            ("mk-line-blue", "파란 밑줄", "외적 갈등 (인물↔인물/집단)"),
            ("mk-line-red", "빨간 밑줄", "내적 갈등 (양심↔두려움)"),
            ("mk-double", "겹밑줄", "핵심 주제 의식"),
        ],
        "left_page_body_html": """
        <div style="background:#EEF9F3; border:0.9pt solid #82E0AA; border-left:3.5pt solid #1E8449; border-radius:5px; padding:4.5px 8px; margin-bottom:5px; font-size:7.3pt;">
          <strong>🌱 [읽기➔쓰기 전이] 1~11차시 씨앗 보관함 총소환!</strong><br>
          • <strong>4차시·11차시 씨앗(주제·글감):</strong> 교실이나 일상에서 별명·오해·침묵 때문에 겪었던 갈등과 작은 용기 경험<br>
          • <strong>7차시·10차시 씨앗(갈등·선택):</strong> 양심과 두려움이 부딪히는 딜레마 상황과 용기 있는 대안 선택<br>
          • <strong>8차시 씨앗(서술 시점):</strong> 독자의 공감을 이끌어 내기에 가장 알맞은 서술자의 위치(1인칭 ‘나’ vs 3인칭 주인공)
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📐 [모델 분석] 진형민 작가의 『꼴뚜기』 창작 기획서 역추적</th>
              <th class="wing-head">🧠 작가의 기획 비법 날개</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:8.2pt; line-height:1.5;">
                <p><strong>1. 창작 목적 및 예상 독자:</strong> 교실에서 장난스러운 별명과 방관으로 상처받는 초등학교 고학년 독자들에게, 침묵을 깨는 작은 용기와 연대의 가치를 일깨워 주기 위해 쓴다.</p>
                <p><strong>2. 핵심 갈등 설계 (외적 갈등 + 내적 갈등):</strong><br>
                • <span class="mk-line-blue"><strong>[외적 갈등]:</strong> ‘꼴뚜기’라는 따돌림 꼬리표를 피하려고 서로에게 별명을 떠넘기고 고립시키는 5학년 3반 아이들의 대립</span><br>
                • <span class="mk-line-red"><strong>[내적 갈등]:</strong> 주인공 <span class="mk-person">길이찬</span>의 마음속에서 ‘나까지 꼴뚜기가 될까 봐 두려워 피하고 싶은 마음’과 ‘목구멍에 가시가 박힌 듯한 양심의 가책’이 부딪힘</span></p>
                <p><strong>3. 서술 시점 선택:</strong> <strong>[3인칭 시점 (<span class="mk-person">길이찬</span> 중심 초점화)]</strong><br>
                • <strong>선택 이유:</strong> 1대부터 5대까지 교실 전체에서 벌어지는 사건을 넓게 보여 주면서도, 가해자·방관자·피해자를 모두 겪는 길이찬의 속마음을 따라가며 독자가 자기 모습을 성찰하게 하기 위해서이다.</p>
                <p><strong>4. 주제의식:</strong> <span class="mk-double">모두가 두려워 침묵할 때 ‘어쩌다 한 번씩 용감해지는’ 작은 선택과 친구의 연대가 교실의 편견을 깨뜨린다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide">
                  <div class="wing-box-title"><span>👁️ 선생님의 기획 코칭</span><span class="role-chip">I Do 시범</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>재미있는 이야기를 기획하려면 왜 ‘외적 갈등’과 ‘내적 갈등’을 함께 설계해야 할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>친구와 다투는 겉 사건(외적 갈등)만 있으면 인물이 깊이가 없어. 주인공이 마음속으로 ‘사실을 말할까, 숨길까?’ 고민(내적 갈등)할 때 독자가 손에 땀을 쥐게 돼!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>내 이야기에도 [외적 사건]과 [마음속 두 욕구의 충돌]을 세트로 기획하자!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:8.1pt; line-height:1.48;">
                <p><strong>🔍 [서술 시점 선택 가이드: 내 이야기에 딱 맞는 카메라는?]</strong><br>
                • <strong>선택지 A — 1인칭 주인공 시점 (‘나’):</strong> 주인공인 ‘나’가 직접 겪은 사건과 떨리는 속마음을 고백하듯 서술함. ➔ <em>독자와 심리적 거리가 가까워 깊은 공감과 몰입을 유도할 때 유리!</em><br>
                • <strong>선택지 B — 3인칭 시점 (‘민준이는’, ‘수아의’):</strong> 이야기 밖의 서술자가 인물의 행동과 심리를 보여 줌. ➔ <em>교실의 여러 친구들이 얽힌 사건을 객관적이고 입체적으로 보여 줄 때 유리!</em></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 시점 결정 점검</span><span class="role-chip">We Do 함께</span></div>
                  <div>내가 쓸 이야기가 <strong>‘나의 솔직한 반성과 고백’</strong> 중심이면 [<span class="blank-slot"><span class="t-ans">1인칭 주인공</span></span>] 시점이 좋고, <strong>‘교실 여러 인물의 연쇄 사건’</strong> 중심이면 [<span class="blank-slot"><span class="t-ans">3인칭</span></span>] 시점이 좋습니다.</div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "창작 글감 선정 및 예상 독자·창작 목적·주제의식 설정하기",
            "tag": "Step 1 주제·독자 설정 ([6국03-03])",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:24%;">기획 항목</th>
                  <th style="width:76%;">나의 단편 이야기 기초 기획안</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>선정한 글감(씨앗)</strong></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">실내화 주머니가 바뀌어 생긴 오해와 ‘짝짝이’라는 놀림 별명 앞에서 방관하다가 용기 내어 진실을 밝힌 사건</span></span></td>
                </tr>
                <tr>
                  <td><strong>예상 독자 & 창작 목적</strong></td>
                  <td>• <strong>예상 독자:</strong> <span class="blank-slot"><span class="t-ans">우리 반 친구들과 6학년 학생들</span></span> / <strong>목적:</strong> <span class="blank-slot"><span class="t-ans">사소한 오해와 침묵이 친구에게 주는 상처를 깨닫고 용기의 소중함을 나누기 위해</span></span></td>
                </tr>
                <tr>
                  <td><strong>이야기의 핵심 주제문</strong></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">체면을 지키려는 비겁한 침묵보다 잘못을 바로잡는 작은 용기가 진정한 우정을 만든다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 주제를 가장 효과적으로 구현할 ‘서술 시점’과 ‘외적·내적 핵심 갈등’ 설계하기",
        "activity_2": {
            "title": "서술 시점(1인칭/3인칭) 결정 및 외적·내적 이중 갈등 구조 설계하기",
            "tag": "Step 2 시점·갈등 선정 ([6국05-03])",
            "body_html": """
            <div class="inference-row" style="grid-template-columns: 1fr 18px 1.2fr;">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">🎥 [서술 시점 결정]</strong><br>
                • <strong>선택한 시점:</strong> □ 1인칭(‘나’) / □ 3인칭(이름) ➔ [<span class="blank-slot"><span class="t-ans">1인칭 주인공 시점 (‘나’)</span></span>]<br>
                • <strong>선택한 이유:</strong> <span class="pencil-line">✏️ <span class="t-ans">내 실수를 숨기고 싶었던 두려움과 부끄러운 속마음을 독자에게 가장 솔직하고 생생하게 전달하기 위해서</span></span>
              </div>
              <div class="inf-symbol">+</div>
              <div class="inf-card c2">
                <strong style="color:var(--mark-green);">⚡ [외적 갈등 & 내적 갈등 설계]</strong><br>
                • <strong>외적 갈등(인물↔인물/집단):</strong> <span class="pencil-line">✏️ <span class="t-ans">내 실수로 짝짝이 실내화를 신게 된 전학생 지호를 반 아이들이 ‘짝짝이’라며 놀리고 따돌리는 갈등</span></span>
                • <strong>내적 갈등(양심↔두려움):</strong> <span class="pencil-line">✏️ <span class="t-ans">‘내가 바꿨다고 솔직히 고백할까?’ 하는 양심과 ‘나까지 놀림받으면 어쩌지?’ 하는 두려움의 충돌</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 1·2]의 요소를 하나로 통합하여 ‘단편 이야기 창작 마스터 기획서’ 확정하기",
        "activity_3": {
            "title": "나만의 단편 이야기 ‘창작 마스터 기획서’ 완성하기",
            "tag": "Step 3 마스터 기획서 완성",
            "body_html": """
            <div style="background:#FFFDFB; border:0.9pt solid #C85A17; border-radius:5px; padding:5px 8px; font-size:7.3pt; line-height:1.45;">
              <div style="font-weight:800; color:#C85A17; border-bottom:0.7pt dashed #F0B27A; padding-bottom:2px; margin-bottom:3px;">📋 [단편 이야기 창작 마스터 기획서]</div>
              <div>• <strong>작품 가제목:</strong> 『<span class="blank-slot"><span class="t-ans">주인을 찾은 짝짝이 실내화 (또는 네잎클로버 책갈피)</span></span>』</div>
              <div>• <strong>서술 시점 및 중심인물:</strong> [<span class="blank-slot"><span class="t-ans">1인칭 주인공 시점</span></span>] / 중심인물: [<span class="blank-slot"><span class="t-ans">나(김민준)와 전학생 박지호</span></span>]</div>
              <div>• <strong>이야기 한 줄 요약 (기획 의도):</strong></div>
              <span class="pencil-line">✏️ <span class="t-ans">아침에 급히 실내화를 신다가 전학생 지호의 실내화와 한 짝이 바뀐 ‘나’가, 아이들의 놀림이 두려워 침묵하다가 지호가 건넨 네잎클로버 책갈피를 보고 용기 내어 진실을 밝히며 화해하는 이야기이다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 내용 생성) 캐릭터 프로파일링 및 상징 소품 생성으로 직결",
            "prompt": "기획한 이야기에 등장할 주동인물과 상대 인물의 가장 큰 성격 특징을 한 단어로 메모해 두세요.",
            "placeholder": "(예: 나 — 소심하지만 마음이 약함 / 상대 친구 — 말수가 적지만 속이 깊음)",
            "example_answer": "나(민준): 남의 시선을 많이 의식하지만 양심적인 성격 / 전학생(지호): 조용하고 묵묵히 참지만 친구를 배려할 줄 아는 따뜻한 성격.",
        },
        "self_check": [
            "창작 목적과 예상 독자, 전달하고자 하는 주제의식을 명확히 설정했나요?",
            "1인칭과 3인칭 중 내 이야기에 더 효과적인 서술 시점을 고르고 이유를 밝혔나요?",
            "인물 사이의 ‘외적 갈등’과 마음속 ‘내적 갈등’을 구체적으로 기획했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[이야기 기획 4요소] ①목적·독자·주제 ➔ ②서술 시점(1인칭 ‘나’ vs 3인칭 주인공) ➔ ③이중 갈등(외적 갈등 + 내적 갈등) ➔ ④마스터 기획서 확정",
            "intro_5min": "1~11차시 동안 『꼴뚜기』를 읽으며 기록했던 ‘내 글 씨앗 보관함’을 펼쳐 보게 한다. “이제 여러분이 독자에서 ‘작가’로 변신할 시간입니다! 진형민 작가가 『꼴뚜기』를 기획했듯, 우리 반 단편집에 실릴 나만의 이야기를 기획해 볼까요?”라며 동기를 부여한다.",
            "ido_think_aloud_script": "“선생님이 어떻게 씨앗을 이야기 기획서로 발전시키는지 시범을 보여 줄게요. 선생님은 ‘실내화 한 짝이 바뀌어 생긴 오해’를 글감으로 골랐어요. 만약 단순히 ‘실내화가 바뀌었다가 다시 찾아 주었다’로 끝내면 갈등이 없어서 심심한 글이 돼요. 그래서 『꼴뚜기』처럼 [외적 갈등]으로 ‘반 아이들이 전학생을 짝짝이라며 놀리는 상황’을 넣고, [내적 갈등]으로 ‘내가 바꿨다고 말할까, 놀림받을까 봐 숨길까 고민하는 마음’을 넣을 거예요. 그리고 이 떨리는 속마음을 생생하게 전달하려고 ‘1인칭 주인공(나)’ 시점을 선택했습니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하고 찾기(Think & Search)",
                    "question": "내가 쓸 이야기에서 ‘외적 갈등’과 ‘내적 갈등’이 서로 어떻게 연결되어야 자연스러울까요?",
                    "expected_ans": "교실에서 친구들과 겪는 문제 상황(외적 갈등)이 원인이 되어, 주인공 마음속에서 ‘양심대로 행동할까, 불이익을 피할까’ 고민하는 내적 갈등이 일어나도록 연결해야 합니다.",
                    "reprompt": "『꼴뚜기』에서 오선재가 매트를 혼자 끄는 외적 상황이 길이찬의 어떤 내적 갈등을 불러일으켰는지 떠올려 보세요.",
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "여러분이 선택한 서술 시점(1인칭 또는 3인칭)은 이야기를 쓸 때 어떤 점을 가장 주의해야 할까요?",
                    "expected_ans": "1인칭(‘나’)을 선택했다면 이야기 끝까지 ‘나’로 통일해야 하고 다른 친구의 머릿속 생각을 다 아는 것처럼 쓰면 안 됩니다. 3인칭을 선택했다면 갑자기 ‘나는’이 튀어나오지 않게 주의해야 합니다.",
                    "reprompt": "8차시에서 배운 1인칭 시점과 3인칭 시점의 규칙을 떠올려 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]~[활동 3]을 차례로 작성하며 마스터 기획서를 완성하도록 개별 코칭한다. 갈등 상황이 너무 비현실적(예: 우주 전쟁, 좀비 출현 등)이어서 6학년 교실·일상 성찰 주제와 동떨어지지 않도록 현실감 있는 갈등으로 유도한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 문항:</strong> 1인칭 주인공 / 3인칭<br>
              <strong>• [활동 1] 예시 답안:</strong> (글감) 실내화 주머니가 바뀌어 생긴 오해와 ‘짝짝이’ 별명 방관 사건 / (독자·목적) 우리 반 친구들, 사소한 오해와 침묵이 주는 상처를 깨닫고 용기의 소중함을 나누기 위해 / (주제문) 체면을 지키려는 비겁한 침묵보다 잘못을 바로잡는 작은 용기가 진정한 우정을 만든다.<br>
              <strong>• [활동 2] 예시 답안:</strong> 1인칭 주인공 시점(‘나’) / 내 실수를 숨기고 싶었던 두려움과 부끄러운 속마음을 가장 솔직하게 전달하기 위해서 / (외적 갈등) 내 실수로 짝짝이 실내화를 신게 된 전학생 지호를 아이들이 놀리는 갈등 / (내적 갈등) 솔직히 고백할까 하는 양심과 나까지 놀림받으면 어쩌지 하는 두려움의 충돌.<br>
              <strong>• [활동 3] 예시 답안:</strong> 『주인을 찾은 짝짝이 실내화』 / 1인칭 주인공 시점 / 나(김민준)와 전학생 박지호 / 아침에 급히 실내화를 신다가 전학생 지호의 실내화와 한 짝이 바뀐 ‘나’가, 놀림이 두려워 침묵하다가 용기 내어 진실을 밝히며 화해하는 이야기.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "갈등 없이 ‘친구와 놀이공원에 가서 재미있게 놀고 맛있는 것을 먹었다’처럼 단순 생활문(일기)을 기획하는 경우",
                    "diagnosis": "서사(이야기) 갈래의 핵심 동력이 ‘갈등(문제 상황과 선택)’임을 인식하지 못하고 수필·생활문과 혼동함.",
                    "prescription": "‘이야기에는 반드시 주인공이 해결해야 할 문제(갈등)와 고민하는 순간이 있어야 해. 그날 친구와 사소한 오해나 다툼은 없었니?’라고 질문하여 갈등 요소를 추가하게 한다.",
                },
                {
                    "error_case": "1인칭 주인공 시점을 선택해 놓고 기획서 요약에 ‘민준이는 지호의 속마음을 모두 알고 있었다’처럼 전지적 서술을 계획하는 경우",
                    "diagnosis": "1인칭 시점의 서술 제한(상대방의 속마음은 표정·행동으로만 추측 가능함)을 이해하지 못함.",
                    "prescription": "1인칭 ‘나’는 내 마음만 직접 말할 수 있고, 친구의 마음은 친구의 떨리는 손이나 표정을 보고 짐작하도록 설계해야 함을 안내한다.",
                },
            ],
            "scaffolding_down": "글감 선정이 어려운 학생에게는 [교실 갈등 상황 뱅크 3선: ①별명 놀림 방관 사건, ②모둠 과제 실수 떠넘기기 사건, ③단톡방 오해 사건] 중 하나를 골라 자신의 경험을 조금씩 바꾸어 넣게 한다.",
            "scaffolding_up": "주인공 외에 『꼴뚜기』의 ‘구주호’나 ‘담임 선생님’처럼 갈등 해결의 실마리를 제공하는 매력적인 조력자 캐릭터의 역할까지 기획서에 함께 설계해 보게 한다.",
            "rubric": {
                "high": "창작 목적, 예상 독자, 주제의식, 서술 시점(1인칭/3인칭)의 선택 이유, 외적·내적 핵심 갈등이 유기적으로 연결된 마스터 기획서를 구체적으로 완성함.",
                "mid": "주제와 줄거리는 설정했으나, 내적 갈등이나 서술 시점 선택 이유에 대한 설명이 다소 간략함.",
                "low": "갈등 구조가 없는 단순 일기 형태이거나 필수 기획 항목이 다수 누락됨.",
            },
        },
    },

    # =========================================================================
    # 13차시: G6-NAR-W2 내용 생성하기 (입체적 인물 프로파일·시공간 배경·상징 소품 및 복선 생성하기)
    # =========================================================================
    {
        "lesson_title": "[내용 생성하기] 입체적 인물 프로파일·배경 감각어·상징 소품과 복선 만들기",
        "std_badge": "[6국05-01] [6국04-02] [6국04-04]",
        "student_goal": "기획한 이야기를 바탕으로 입체적 인물(외면·내면·습관·숨은 동기)을 프로파일링하고, 시공간 배경을 살리는 감각어·복합어·관용표현 재료와 주제를 압축하는 상징 소품 및 복선 장치를 생성할 수 있다.",
        "marking_items": [
            ("mk-person", "동그라미", "인물의 성격·행동 습관"),
            ("mk-highlight", "형광펜", "오감 감각어·복합어·관용표현"),
            ("mk-bg", "네모", "상징 소품 및 복선 장치"),
        ],
        "left_page_body_html": """
        <div style="background:#FFF8F0; border:0.8pt solid #F0B27A; border-radius:4px; padding:4px 8px; margin-bottom:5px; font-size:7.3pt;">
          <strong>🎨 이야기 재료 생성 스튜디오:</strong> 살아 숨 쉬는 이야기를 만들려면 ① <strong>입체적 인물</strong>(장점과 약점을 함께 지닌 인물), ② <strong>생생한 배경 감각어·관용표현</strong>, ③ <strong>상징 소품과 복선</strong>이라는 3가지 핵심 재료가 필요합니다.
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🗂️ [모델 분석] 『꼴뚜기』의 재료 생성 노트 & 어휘 뱅크</th>
              <th class="wing-head">🧠 재료 생성 코칭 날개</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:8.1pt; line-height:1.48;">
                <p><strong>1. 입체적 인물 프로파일 예시 (<span class="mk-person">길이찬</span>):</strong><br>
                • <strong>겉모습·습관:</strong> 긴장하면 <span class="mk-highlight">마른침</span>을 삼키고, 당황하면 안절부절못하며 눈썹을 찡그림.<br>
                • <strong>성격의 양면(입체성):</strong> 숙제를 안 해 와서 친구를 걸고넘어지고 따돌림이 무서워 몸을 사리는 <strong>[약점]</strong>이 있지만, 아픈 친구의 그림을 몰래 완성해 주고 죄책감을 느낄 줄 아는 <strong>[선한 양심]</strong>을 지님.</p>
                <p><strong>2. 상징 소품(오브제) & 복선 장치 예시:</strong><br>
                • <span class="mk-bg"><strong>[상징 소품 1 — 새끼 오징어 그림]:</strong></span> 친구를 돕는 선의였으나 누명으로 왜곡되는 갈등 매개체<br>
                • <span class="mk-bg"><strong>[상징 소품 2 — 꼴뚜기 국수]:</strong></span> 혐오와 편견을 녹이고 모두를 하나로 묶는 화해의 매개체<br>
                • <span class="mk-bg"><strong>[복선 장치]:</strong></span> 실과 시간에 선생님이 구석에서 몸을 웅크리고 국물을 만들며 히죽히죽 웃음 ➔ 나중에 그 국물이 꼴뚜기 육수임이 밝혀짐.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide">
                  <div class="wing-box-title"><span>👁️ 선생님의 캐릭터 비법</span><span class="role-chip">I Do 시범</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>인물이 진짜 사람처럼 느껴지게 하려면 무엇을 정해 두어야 할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>‘착하다/나쁘다’만 적으면 평면적 인물이 돼. ‘긴장할 때 나타나는 신체 버릇’과 ‘겉으로 한 행동 뒤에 숨은 진짜 이유(동기)’를 함께 만들어 봐!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:8pt; line-height:1.45;">
                <p><strong>💎 [내 글에 바로 쓰는 감각어·복합어·신체 관용표현 보물창고]</strong><br>
                • <strong>배경·분위기 감각어:</strong> <span class="mk-highlight">싸늘한 정적</span>, <span class="mk-highlight">수군수군</span>, <span class="mk-highlight">후끈 달아오른</span>, <span class="mk-highlight">시끌벅적한</span>, <span class="mk-highlight">차곡차곡 쌓이는 어색함</span><br>
                • <strong>합성어·파생어([6국04-02]):</strong> <span class="mk-highlight">뒷걸음질</span>, <span class="mk-highlight">눈길</span>, <span class="mk-highlight">마른침</span>, <span class="mk-highlight">아랫입술</span>, <span class="mk-highlight">식은땀</span>, <span class="mk-highlight">발걸음</span>, <span class="mk-highlight">곁눈질</span>, <span class="mk-highlight">비웃음</span><br>
                • <strong>심리·신체 관용표현([6국04-04]):</strong> <span class="mk-highlight">목구멍에 가시가 박힌 듯하다</span>(죄책감), <span class="mk-highlight">가슴이 철렁 내려앉다</span>(놀람), <span class="mk-highlight">얼굴이 홍당무가 되다 / 목덜미가 달아오르다</span>(창피함), <span class="mk-highlight">입을 꾹 다물다</span>(침묵), <span class="mk-highlight">발길이 떨어지지 않다</span>(망설임)</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 어휘 재료 고르기</span><span class="role-chip">We Do 함께</span></div>
                  <div>보물창고에서 내 이야기의 <strong>[위기·절정 장면]</strong>에 꼭 넣고 싶은 복합어 1개와 관용표현 1개를 골라 동그라미 쳐 보세요!<br>
                  ➔ <span class="blank-slot"><span class="t-ans">곁눈질 / 가슴이 철렁 내려앉다</span></span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "주동인물과 상대 인물의 ‘입체적 캐릭터 프로파일 카드’ 완성하기",
            "tag": "Step 1 인물 프로파일링 ([6국05-01])",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">구분</th>
                  <th style="width:27%;">성격의 양면 (장점 & 약점)</th>
                  <th style="width:27%;">긴장·갈등 시 신체 버릇·말버릇</th>
                  <th style="width:28%;">사건 속 숨은 행동 동기 (왜 그랬을까?)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>주동인물</strong><br><span class="blank-slot"><span class="t-ans">나 (김민준)</span></span></td>
                  <td>• 장점: 친구의 아픔에 공감할 줄 앎<br>• 약점: <span class="blank-slot"><span class="t-ans">남의 시선을 두려워해 쉽게 나서지 못함</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">당황하면 운동화 앞코로 바닥을 툭툭 차고 귓불을 만지작거림</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">아침에 지각할까 봐 급히 실내화를 신느라 지호 실내화 한 짝을 잘못 신었지만 놀림받을까 봐 숨김</span></span></td>
                </tr>
                <tr>
                  <td><strong>상대·조력 인물</strong><br><span class="blank-slot"><span class="t-ans">전학생 박지호</span></span></td>
                  <td>• 겉모습: 말수가 적고 조용함<br>• 내면: <span class="blank-slot"><span class="t-ans">관찰력이 깊고 친구의 실수를 감싸 주는 배려심</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">억울할 때도 변명 대신 입술을 꾹 다물고 조용히 스케치북에 그림을 그림</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">민준이가 자기 실내화 한 짝을 신은 걸 눈치챘지만 민준이가 민망할까 봐 먼저 말하지 않고 기다려 줌</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 인물들이 움직일 ‘시공간 배경 분위기’와 ‘감각어·복합어·관용표현’ 재료 결합하기",
        "activity_2": {
            "title": "장면별 시공간 배경 설정 및 감각어·복합어·관용표현 매칭하기",
            "tag": "Step 2 배경·표현 재료 수집 ([6국04-02/04])",
            "body_html": """
            <div class="inference-row" style="grid-template-columns: 1fr 16px 1fr;">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">📍 [갈등이 시작·심화되는 배경 & 어휘 재료]</strong><br>
                • <strong>시간·공간:</strong> <span class="blank-slot"><span class="t-ans">비 내리는 월요일 아침 신발장과 체육관 강당</span></span><br>
                • <strong>분위기 감각어·복합어:</strong> <span class="blank-slot"><span class="t-ans">축축한 냄새, 곁눈질, 식은땀, 키득키득</span></span><br>
                • <strong>사용할 관용표현:</strong> <span class="blank-slot"><span class="t-ans">가슴이 철렁 내려앉다 / 입을 꾹 다물다</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:var(--mark-green);">📍 [갈등이 해결되는 배경 & 어휘 재료]</strong><br>
                • <strong>시간·공간:</strong> <span class="blank-slot"><span class="t-ans">오후 해 질 녘 방과 후 교실 복도</span></span><br>
                • <strong>분위기 감각어·복합어:</strong> <span class="blank-slot"><span class="t-ans">따스한 노을빛, 발걸음, 맞잡은 손</span></span><br>
                • <strong>사용할 관용표현:</strong> <span class="blank-slot"><span class="t-ans">목구멍에 걸린 가시가 빠진 듯 후련하다</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 1·2]의 재료를 꿰어 줄 ‘중심 상징 소품(오브제)’ 1개와 ‘복선 장치’ 1개 고안하기",
        "activity_3": {
            "title": "주제를 압축하는 ‘상징 소품(오브제)’과 개연성을 높이는 ‘복선 장치’ 설계하기",
            "tag": "Step 3 상징·복선 고안",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:24%;">설계 항목</th>
                  <th style="width:32%;">내가 고안한 소품 / 복선 내용</th>
                  <th style="width:44%;">이야기 속 기능 및 의미 변화 (발단 ➔ 결말)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>중심 상징 소품<br>(오브제)</strong></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">초록색 별 스티커가 붙은 ‘짝짝이 실내화’</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">[발단·전개] 내 실수와 비겁한 침묵을 떠올리게 하는 부끄러운 증거물 ➔ [결말] 서로의 발에 제 짝을 찾아 주며 우정을 이어 주는 화해의 상징</span></span></td>
                </tr>
                <tr>
                  <td><strong>복선(Foreshadowing)<br>장치</strong></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">1교시 미술 시간에 지호가 내 발밑을 한 번 힐끔 보더니 말없이 웃으며 자기 발을 책상 깊숙이 넣은 장면</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">[결말 회수] 지호는 아침부터 내가 자기 실내화 한 짝을 신고 있는 걸 이미 알고도 나를 배려해 숨겨 주었다는 사실이 밝혀져 감동을 줌</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 내용 조직) 4단 플롯 아키텍처 보드에 그대로 배치 직결",
            "prompt": "오늘 만든 ‘복선’을 이야기의 어느 단계(발단/전개)에 숨겨 두고, 어느 단계(절정/결말)에서 비밀을 밝힐지 메모해 두세요.",
            "placeholder": "(예: 전개 시작 부분에 복선 배치 ➔ 절정 대화 장면에서 복선 회수)",
            "example_answer": "발단 끝부분(1교시 수업 시작)에 지호가 내 실내화를 보고도 조용히 발을 숨기는 복선을 심고, 절정에서 내가 사과할 때 지호가 미소 지으며 비밀을 밝히게 해야겠다.",
        },
        "self_check": [
            "주동인물과 상대 인물의 성격 장단점과 비언어적 행동 습관을 입체적으로 만들었나요?",
            "장면의 분위기를 살리는 감각어, 복합어(합성어·파생어), 관용표현을 3개 이상 골랐나요?",
            "주제를 압축하는 상징 소품 1개와 앞뒤 사건을 연결하는 복선 1개를 구체적으로 고안했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[이야기 재료 3종 세트] ①입체적 캐릭터 카드(장점+약점+신체 버릇+숨은 동기) + ②배경 감각어·복합어·관용표현 뱅크 + ③상징 소품(오브제 의미 변화) & 복선(심기➔거두기)",
            "intro_5min": "요리사가 최고의 국수를 만들려면 쫄깃한 면발과 구수한 육수 재료(꼴뚜기!)를 먼저 준비해야 하듯, 작가도 이야기를 쓰기 전에 인물·배경·상징·복선 재료를 풍성하게 준비해야 함을 안내한다.",
            "ido_think_aloud_script": "“선생님이 [활동 3]에서 상징 소품과 복선을 어떻게 만드는지 시범을 보여 줄게요. 『꼴뚜기』에서 ‘새끼 오징어 그림’과 ‘꼴뚜기 국수’가 이야기를 이끌어 갔던 것 기억나죠? 선생님은 ‘초록색 별 스티커가 붙은 실내화 한 짝’을 상징 소품으로 정했어요. 처음엔 내 실수를 감춘 ‘부끄러움과 침묵’을 상징하지만, 결말에서 주인을 찾아 주었을 때는 ‘정직한 용기와 우정’을 상징하게 됩니다. 그리고 복선으로는 ‘1교시에 전학생 지호가 내 발밑을 힐끔 보고도 조용히 자기 발을 책상 밑으로 숨기는 장면’을 미리 넣어 둘 거예요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하고 찾기(Think & Search)",
                    "question": "인물 프로파일 카드를 만들 때 왜 ‘긴장하거나 화날 때 나타나는 신체 버릇’을 미리 정해 두면 좋을까요?",
                    "expected_ans": "15차시에 초고를 쓸 때 ‘나는 긴장했다(Tell)’라고 설명하는 대신, 미리 정해 둔 신체 버릇(‘귓불을 만지작거렸다’, ‘아랫입술을 깨물었다’)을 써서 자연스럽게 ‘보여주기(Show)’ 묘사를 할 수 있기 때문입니다.",
                    "reprompt": "9차시에서 배운 ‘Show vs Tell’ 원리와 연결해 생각해 볼까요?",
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "여러분이 고안한 ‘상징 소품(사물)’은 이야기 처음과 끝에서 주인공에게 어떤 의미로 바뀌게 되나요?",
                    "expected_ans": "처음에는 오해나 갈등, 부끄러움을 일으키는 물건이었다가, 주인공이 용기를 낸 결말에서는 화해와 성장을 보여 주는 소중한 물건으로 의미가 바뀝니다.",
                    "reprompt": "5차시에서 분석한 ‘꼴뚜기’의 의미 변화(따돌림 폭탄 ➔ 구수한 화해)를 떠올려 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]~[활동 3]을 작성하며 자신의 이야기에 들어갈 인물·배경·어휘·상징·복선 재료를 구체화하도록 지도한다. 좌측 페이지의 ‘감각어·복합어·관용표현 보물창고’에서 최소 3개 이상의 표현을 골라 [활동 2]에 반영하도록 독려한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 문항:</strong> 곁눈질 / 가슴이 철렁 내려앉다 (학생 자율 선택 인정)<br>
              <strong>• [활동 1] 예시 답안:</strong> (주동인물 나) 남의 시선을 두려워해 쉽게 나서지 못함 / 당황하면 운동화 앞코로 바닥을 툭툭 차고 귓불을 만지작거림 / 지각할까 봐 급히 신느라 지호 실내화를 잘못 신었지만 놀림받을까 봐 숨김. (상대인물 박지호) 관찰력이 깊고 배려심 있음 / 입술을 꾹 다물고 스케치북에 그림을 그림 / 민준이가 민망할까 봐 먼저 말하지 않고 기다려 줌.<br>
              <strong>• [활동 2] 예시 답안:</strong> (갈등 배경) 비 내리는 월요일 아침 신발장과 체육관 / 축축한 냄새, 곁눈질, 식은땀, 키득키득 / 가슴이 철렁 내려앉다. (해결 배경) 오후 해 질 녘 방과 후 복도 / 따스한 노을빛, 발걸음 / 목구멍에 걸린 가시가 빠진 듯 후련하다.<br>
              <strong>• [활동 3] 예시 답안:</strong> (상징 소품) 초록색 별 스티커가 붙은 짝짝이 실내화 — 부끄러운 침묵의 증거물에서 화해의 상징으로 변화 / (복선 장치) 1교시에 지호가 내 발밑을 보고도 조용히 자기 발을 숨긴 장면 — 결말에서 지호의 깊은 배려가 밝혀짐.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "인물의 성격을 ‘착함’, ‘나쁨’ 한 단어로만 적고 신체 버릇이나 동기를 비워 두는 경우",
                    "diagnosis": "입체적 인물의 구성 요소(외면 행동 + 내면의 양면성 + 행동 이유)를 구체화하는 데 어려움을 겪음.",
                    "prescription": "‘네가 잘못을 숨겼을 때 손이나 눈은 어떻게 움직였니?’라고 구체적인 신체 부위(눈, 입술, 손가락, 발)를 짚어 질문하여 버릇을 찾게 도와준다.",
                },
                {
                    "error_case": "상징 소품을 정해 놓고 정작 주요 사건이나 결말에서는 그 소품을 전혀 사용하지 않는 경우",
                    "diagnosis": "단순한 배경 소품과 서사 전체를 관통하는 ‘상징적 오브제’의 차이를 이해하지 못함.",
                    "prescription": "상징 소품은 갈등이 시작될 때 한 번, 그리고 갈등이 풀리는 절정·결말에 다시 한 번 꼭 등장해야 함을 강조한다.",
                },
            ],
            "scaffolding_down": "상징 소품과 복선 고안이 어려운 학생에게는 [소품-복선 세트 카드: ①구겨진 쪽지, ②짝짝이 실내화, ③열쇠고리 인형] 중 하나를 골라 자신의 이야기에 맞게 이름만 바꾸어 쓰게 한다.",
            "scaffolding_up": "파생어(접두사·접미사 결합어)와 합성어를 직접 2개 이상 조합하여 인물과 배경을 묘사하는 감각적인 문장을 미리 한 줄씩 지어 보게 한다.",
            "rubric": {
                "high": "주동·상대 인물의 입체적 성격(장단점·신체 버릇·숨은 동기), 시공간 배경 감각어·복합어·관용표현, 그리고 의미가 변화하는 상징 소품 1개와 복선 1개를 모두 구체적으로 생성함.",
                "mid": "인물 프로파일과 배경 어휘는 생성했으나, 상징 소품의 의미 변화나 복선의 회수 계획이 다소 단순함.",
                "low": "인물이 단선적(‘착하다’)으로만 제시되고 상징 소품이나 복선 장치를 고안하지 못함.",
            },
        },
    },

    # =========================================================================
    # 14차시: G6-NAR-W3 내용 조직하기 (발단-전개-절정-결말 4단 인과 플롯 및 장면별 Show/Tell 배분 설계)
    # =========================================================================
    {
        "lesson_title": "[내용 조직하기] 『꼴뚜기』 이야기 산을 미러링하여 4단 플롯과 Show 묘사 설계하기",
        "std_badge": "[6국03-03] [6국05-01]",
        "student_goal": "3차시에서 분석한 『꼴뚜기』의 ‘4단 이야기 산 도해조직자’를 내 글의 개요 틀로 미러링하여, 발단-전개-절정-결말의 사건 인과와 복선 배치, 장면별 간접 묘사(Show) 및 대화문 비중을 조직할 수 있다.",
        "marking_items": [
            ("mk-bg", "네모", "장면 전환·시간 표지"),
            ("mk-dotted", "점선 밑줄", "복선 매설(심기) ➔ 회수(거두기)"),
            ("mk-line-red", "빨간 밑줄", "절정의 Show(행동·대화) 집중 구간"),
        ],
        "left_page_body_html": """
        <div style="background:#FFF8F0; border:0.8pt solid #F0B27A; border-radius:4px; padding:4px 8px; margin-bottom:5px; font-size:7.3pt;">
          <strong>🏛️ [읽기↔쓰기 1:1 구조 미러링 스튜디오]:</strong> 3차시(V1-3)에서 우리가 직접 그렸던 <strong>『꼴뚜기』의 4단 이야기 산(Story Mountain)</strong> 구조를 거울처럼 본떠서(Mirroring), 내 단편 이야기의 4단 플롯 설계도를 완성해 봅시다!
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>⛰️ [모델 구조] 『꼴뚜기』 4단 플롯 vs [내 글 미러링] 설계 비교</th>
              <th class="wing-head">🧠 플롯 조직 코칭 날개</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:8.1pt; line-height:1.48;">
                <p><strong>① 발단 (갈등의 씨앗 & 복선 매설):</strong><br>
                • <em>『꼴뚜기』:</em> 국어 속담 발표로 김소정이 1대 꼴뚜기가 됨. (반찬 소문·성격 복선 제시)<br>
                • <em>내 글 미러링:</em> <span class="mk-bg">월요일 아침 신발장</span>에서 지각할까 봐 급히 실내화를 신다 전학생 지호의 실내화 한 짝과 바뀜. <span class="mk-dotted">[복선 매설: 1교시에 지호가 내 발을 보고도 자기 발을 책상 밑으로 숨김]</span></p>
                <p><strong>② 전개 및 위기 (갈등 증폭 & 양심의 가책):</strong><br>
                • <em>『꼴뚜기』:</em> 2대➔3대➔4대➔5대로 별명이 떠넘겨지며 길이찬의 목구멍에 가시가 박힌 듯 뜨끔거림.<br>
                • <em>내 글 미러링:</em> <span class="mk-bg">3교시 체육관 이동 시간</span>, 왼쪽에 큰 내 실내화를 신은 지호를 보고 아이들이 “짝짝이 전학생!”이라며 웃음보를 터뜨림. 나는 나까지 놀림받을까 봐 입을 꾹 다물지만 마음속에 가시가 박힌 듯 괴로움.</p>
                <p><strong>③ 절정 (최고조의 갈등 & 용기 있는 Show 행동):</strong><br>
                • <em>『꼴뚜기』:</em> 실과 시간 선생님의 “용감한 사람 없니?” 질문에 길이찬·구주호가 포크로 꼴뚜기를 찍어 먹음.<br>
                • <em>내 글 미러링:</em> <span class="mk-bg">점심시간 교실</span>, 또다시 아이들이 지호의 발을 가리키며 놀리려는 순간, <span class="mk-line-red">내가 숨을 크게 들이마시고 앞으로 걸어 나가 내 오른발의 초록 별 스티커 실내화를 벗어 지호 앞에 내려놓음(Show 행동 & 대화).</span> <span class="mk-dotted">[복선 회수: 지호가 아침부터 알고도 나를 배려했음이 밝혀짐]</span></p>
                <p><strong>④ 결말 (갈등 해소 & 상징 소품의 여운):</strong><br>
                • <em>『꼴뚜기』:</em> “비로소 구수한 꼴뚜기 냄새가 코끝에 달라붙었다.” (후각적 여운)<br>
                • <em>내 글 미러링:</em> 제 짝을 찾은 하얀 실내화가 봄볕 아래 반짝이고, 내 발걸음이 날아갈 듯 가벼워짐.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide">
                  <div class="wing-box-title"><span>👁️ 선생님의 조직 비법</span><span class="role-chip">I Do 시범</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>이야기의 어느 단계에서 ‘간접 묘사(Show)’와 ‘대화문’을 가장 길고 자세하게 써야 할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>발단부터 결말까지 똑같은 길이로 쓰면 산봉우리가 없는 평평한 글이 돼.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>갈등이 최고조에 달하고 주인공이 결단을 내리는 <strong>[③ 절정]</strong> 장면에서 행동 묘사(Show)와 대화문을 슬로모션처럼 가장 자세히 쏟아부어야 해!</span></div>
                </div>
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 담화 표지 점검</span><span class="role-chip">We Do 함께</span></div>
                  <div>문단과 장면을 자연스럽게 전환하기 위해 쓸 수 있는 시간·전환 담화 표지 2개를 골라 보세요.<br>
                  ➔ <span class="blank-slot"><span class="t-ans">그러던 3교시 체육 시간이었다 / 바로 그때였다</span></span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "내 단편 이야기의 ‘4단 이야기 산(발단-전개·위기-절정-결말)’ 플롯 보드 설계하기",
            "tag": "Step 1 4단 인과 플롯 배치 ([6국03-03])",
            "body_html": """
            <div style="border:0.9pt solid #BDC3C7; border-radius:6px; padding:6px 8px; background:linear-gradient(to top, #FFFFFF 0%, #FDF5EE 100%);">
              <div style="font-size:7.2pt; font-weight:800; color:#C85A17; margin-bottom:4px; display:flex; justify-content:space-between;">
                <span>⛰️ [나의 4단 이야기 산(Story Mountain) 플롯 아키텍처]</span>
                <span>시간 구성 선택: [ <span class="blank-slot"><span class="t-ans">순행 구성 (또는 과거 회상 역순행 구성)</span></span> ]</span>
              </div>
              <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:5px; align-items:end;">
                <div style="border:0.8pt solid #5DADE2; border-top:3pt solid #2874A6; border-radius:4px; padding:4px 5px; background:#fff; min-height:78px; font-size:7.1pt;">
                  <strong style="color:#2874A6;">① 발단 (1~2문단)</strong><br>
                  • <strong>배경·사건:</strong> <span class="pencil-line">✏️ <span class="t-ans">월요일 아침 신발장에서 급히 실내화를 신다 전학생 지호의 실내화 한 짝과 바뀜</span></span>
                </div>
                <div style="border:0.8pt solid #58D68D; border-top:3pt solid #196F3D; border-radius:4px; padding:4px 5px; background:#fff; min-height:98px; font-size:7.1pt;">
                  <strong style="color:#196F3D;">② 전개·위기 (3~4문단)</strong><br>
                  • <strong>갈등 심화:</strong> <span class="pencil-line">✏️ <span class="t-ans">체육관 이동 중 아이들이 지호를 ‘짝짝이’라 놀리지만, 나는 싸잡혀 놀림받을까 봐 침묵하고 양심의 가책을 느낌</span></span>
                </div>
                <div style="border:1pt solid #E74C3C; border-top:3.5pt solid #C0392B; border-radius:4px; padding:4px 5px; background:#FFFDFB; min-height:115px; font-size:7.1pt;">
                  <strong style="color:#C0392B;">⛰️ ③ 절정 (5문단)</strong><br>
                  • <strong>결정적 선택:</strong> <span class="pencil-line">✏️ <span class="t-ans">점심시간에 다시 놀림이 시작되자, 내가 앞으로 걸어 나가 내 발의 실내화를 벗어 보이며 내 실수였다고 고백함</span></span>
                </div>
                <div style="border:0.8pt solid #F5B041; border-top:3pt solid #D35400; border-radius:4px; padding:4px 5px; background:#fff; min-height:82px; font-size:7.1pt;">
                  <strong style="color:#D35400;">④ 결말 (6문단)</strong><br>
                  • <strong>해소·여운:</strong> <span class="pencil-line">✏️ <span class="t-ans">지호가 건넨 따뜻한 미소와 함께 제 짝을 찾은 실내화를 신고 가벼운 발걸음으로 복도를 걸어감</span></span>
                </div>
              </div>
            </div>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 4단계 플롯에 ‘복선 매설➔회수’ 고리와 ‘담화 전환 표지’ 연결하기",
        "activity_2": {
            "title": "복선 매설·회수 연결 및 문단 전환 담화 표지 배치하기",
            "tag": "Step 2 복선 및 응집성 연결 ([6국02-02])",
            "body_html": """
            <div class="inference-row" style="grid-template-columns: 1fr 22px 1fr;">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">🌱 [발단·전개에 심을 복선 문장]</strong><br>
                • <strong>배치 위치:</strong> [ <span class="blank-slot"><span class="t-ans">① 발단 끝 (2문단)</span></span> ]<br>
                • <strong>복선 내용:</strong> <span class="pencil-line">✏️ <span class="t-ans">1교시 시작 종이 울렸을 때, 지호가 내 오른발을 힐끔 보더니 아무 말 없이 자기 발을 책상 깊숙이 숨겼다.</span></span>
              </div>
              <div class="inf-symbol">➔<br><span style="font-size:6.5pt;">회수</span></div>
              <div class="inf-card c3">
                <strong style="color:#D35400;">🎯 [절정·결말에서 회수할 진실 문장]</strong><br>
                • <strong>회수 위치:</strong> [ <span class="blank-slot"><span class="t-ans">③ 절정 끝 (5문단)</span></span> ]<br>
                • <strong>회수 내용:</strong> <span class="pencil-line">✏️ <span class="t-ans">“사실 아침부터 알고 있었어. 네가 당황할까 봐 기다렸는데 먼저 말해 줘서 고마워.”라는 지호의 대사로 회수함.</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 1·2]를 종합하여 15차시 초고 집필에 바로 사용할 ‘장면별 Show 묘사·대화 배분 설계표’ 완성하기",
        "activity_3": {
            "title": "문단별 중심 내용과 ‘보여주기(Show)·대화문·관용표현’ 배분 설계표",
            "tag": "Step 3 장면별 Show 설계도 완성",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:16%;">문단 (단계)</th>
                  <th style="width:24%;">문단 첫머리 담화 표지</th>
                  <th style="width:60%;">반드시 넣을 ‘간접 묘사(Show) / 핵심 대화문 / 관용표현’ 설계</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>1~2문단</strong><br>(발단)</td>
                  <td>비 내리는 월요일 아침이었다.</td>
                  <td>• <strong>배경·복선 Show:</strong> 눅눅한 신발장 공기, 지호가 조용히 발을 책상 밑으로 넣는 행동</td>
                </tr>
                <tr>
                  <td><strong>3~4문단</strong><br>(전개·위기)</td>
                  <td><span class="blank-slot"><span class="t-ans">사건이 터진 건 3교시 체육 시간이었다.</span></span></td>
                  <td>• <strong>내면 갈등 Show & 관용표현:</strong> <span class="pencil-line">✏️ <span class="t-ans">내 오른발의 초록 별 스티커를 보며 ‘가슴이 철렁 내려앉음’, ‘목구멍에 가시가 박힌 듯’ 귓불만 만지작거리며 입을 꾹 다묾</span></span></td>
                </tr>
                <tr>
                  <td><strong>5문단</strong><br>(⛰️ 절정)</td>
                  <td><span class="blank-slot"><span class="t-ans">그때였다. / 더는 숨을 수가 없었다.</span></span></td>
                  <td>• <strong>결단 Show & 대화문:</strong> <span class="pencil-line">✏️ <span class="t-ans">두 주먹을 불끈 쥐고 걸어 나가 실내화를 벗어 놓는 행동 + “잠깐만! 지호가 짝짝이로 신은 건 내 실수 때문이야!”라는 대화문</span></span></td>
                </tr>
                <tr>
                  <td><strong>6문단</strong><br>(결말)</td>
                  <td><span class="blank-slot"><span class="t-ans">방과 후, 비가 개인 복도에는</span></span></td>
                  <td>• <strong>상징·감각적 여운 Show:</strong> <span class="pencil-line">✏️ <span class="t-ans">제 짝을 찾아 나란히 놓인 하얀 실내화 위로 따뜻한 햇살이 쏟아지고 코끝에 상쾌한 비 냄새가 스침</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "15차시(W4 초고 집필하기) 문단별 초고 작성의 직접 설계도로 활용",
            "prompt": "내 이야기의 절정(5문단)에서 주인공이 갈등을 깨뜨리며 외칠 ‘가장 결정적인 대화문(큰따옴표 대사)’ 한 줄을 미리 써 보세요.",
            "placeholder": "(예: “잠깐만! 그건 지호 잘못이 아니야. 아침에 내가 실수로 바꿨어!”)",
            "example_answer": "“웃지 마! 지호가 짝짝이 실내화를 신은 건 아침에 내가 지각할까 봐 급하게 신다가 바뀐 거야. 내가 미안해, 지호야!”",
        },
        "self_check": [
            "『꼴뚜기』의 이야기 산 구조를 미러링하여 발단-전개-절정-결말의 인과를 조직했나요?",
            "앞부분에 심은 복선이 절정·결말에서 자연스럽게 회수되도록 연결했나요?",
            "절정 장면에서 직접 설명(Tell) 대신 행동과 대화로 보여 줄(Show) 계획을 세웠나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[구조 미러링] 3차시 『꼴뚜기』 이야기 산 ➔ 14차시 내 글의 4단 플롯 아키텍처 / [Show 비중 배분] 발단(배경·복선 20%) ➔ 전개·위기(외적·내적 갈등 30%) ➔ 절정(행동·대화 Show 클라이맥스 35%) ➔ 결말(상징 여운 15%)",
            "intro_5min": "3차시(교과서 38~39쪽)에서 완성했던 『꼴뚜기』의 4단 이야기 산 도해조직자를 다시 펼쳐 보게 한다. “우리가 읽으면서 분석했던 이 튼튼한 이야기 산 뼈대에, 어제(13차시) 만든 내 이야기 재료들을 차곡차곡 얹어 설계도를 완성해 볼까요?”라고 안내한다.",
            "ido_think_aloud_script": "“선생님이 좌측 페이지의 [내 글 미러링] 설계를 보며 문단 배분 비법을 알려 줄게요. 초등학생 작가들이 가장 많이 하는 실수가 발단(아침에 일어난 일)을 공책 반 바닥이나 쓰고, 정작 가장 중요한 절정(용기를 내어 사과하는 장면)은 ‘그래서 나는 사과하고 화해했다’ 한 줄로 끝내 버리는 거예요! 진짜 작가처럼 쓰려면 [③ 절정(5문단)]에서 주인공이 숨을 들이마시는 행동, 떨리는 목소리로 외치는 대화문, 친구들의 표정 변화를 슬로모션 카메라로 찍듯 가장 자세히 설계해야 합니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하고 찾기(Think & Search)",
                    "question": "문단과 문단 사이에서 시간이나 공간이 바뀔 때 독자가 헷갈리지 않게 하려면 문단 첫머리에 무엇을 넣어 주어야 할까요?",
                    "expected_ans": "‘사건이 터진 건 3교시 체육 시간이었다’, ‘점심시간이 되자’, ‘방과 후 복도에서’처럼 시간·공간 전환을 알리는 담화 표지를 넣어 주어야 합니다.",
                    "reprompt": "『꼴뚜기』에서 ‘며칠 뒤 종례 시간이었다’, ‘지난주 금요일 아침’, ‘그때였다’ 같은 표지들이 어떤 역할을 했는지 떠올려 보세요.",
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "내 이야기의 결말(6문단)을 ‘다시는 거짓말을 하지 않기로 다짐했다’ 같은 교훈 설명 대신 『꼴뚜기』처럼 감각적 여운으로 끝내려면 어떻게 설계하면 좋을까요?",
                    "expected_ans": "상징 소품(제 짝을 찾은 실내화, 네잎클로버 책갈피 등)의 모습이나 따스한 햇살, 가벼워진 발걸음, 상쾌한 바람 냄새 같은 감각적 묘사로 끝맺으면 여운이 남습니다.",
                    "reprompt": "『꼴뚜기』의 마지막 문장 ‘비로소 구수한 꼴뚜기 냄새가 코끝에 달라붙었다’를 내 소재로 바꾸어 생각해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]~[활동 3]을 통해 6문단 구성의 치밀한 이야기 설계도를 완성하도록 지도한다. 이 설계표가 다음 시간(15차시) 초고 집필의 네비게이션이 됨을 안내한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 문항:</strong> 그러던 3교시 체육 시간이었다 / 바로 그때였다<br>
              <strong>• [활동 1] 예시 답안:</strong> 순행 구성 / ①발단: 월요일 아침 신발장에서 급히 실내화를 신다 지호의 실내화와 한 짝이 바뀜 / ②전개·위기: 체육관 이동 중 아이들이 지호를 놀리지만 나는 놀림받을까 봐 침묵하고 양심의 가책을 느낌 / ③절정: 점심시간에 내가 앞으로 걸어 나가 실내화를 벗어 보이며 내 실수였다고 고백함 / ④결말: 지호의 따뜻한 미소와 함께 제 짝을 찾은 실내화를 신고 가벼운 발걸음으로 복도를 걸어감.<br>
              <strong>• [활동 2] 예시 답안:</strong> ① 발단 끝(2문단) — 1교시에 지호가 내 오른발을 힐끔 보고도 조용히 자기 발을 숨김 ➔ ③ 절정 끝(5문단) — “사실 아침부터 알고 있었어. 네가 당황할까 봐 기다렸는데 고마워.”라는 대사로 회수.<br>
              <strong>• [활동 3] 예시 답안:</strong> (3~4문단) 사건이 터진 건 3교시 체육 시간이었다 / 내 오른발의 초록 별 스티커를 보며 가슴이 철렁 내려앉음, 목구멍에 가시가 박힌 듯 입을 꾹 다묾. (5문단) 그때였다 / 두 주먹을 불끈 쥐고 걸어 나가 실내화를 벗는 행동 + “잠깐만! 지호가 짝짝이로 신은 건 내 실수 때문이야!” 대화문. (6문단) 방과 후 비가 개인 복도에는 / 제 짝을 찾은 실내화 위로 따뜻한 햇살이 쏟아지고 상쾌한 비 냄새가 스침.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "발단-전개-절정-결말의 사건이 인과 관계(‘~때문에 ~하게 되었다’)로 이어지지 않고 우연(“갑자기 선생님이 다 알게 되셨다”)으로 해결되는 경우",
                    "diagnosis": "서사 플롯에서 주인공의 주체적 선택과 인과적 필연성의 중요성을 간과함.",
                    "prescription": "우연이나 어른의 개입만으로 문제가 저절로 풀리지 않고, 주인공이 내적 갈등 끝에 스스로 용기 있는 행동(Show)을 선택하여 갈등을 해결하도록 수정하게 한다.",
                },
                {
                    "error_case": "복선을 절정 뒤에 배치하거나, 심어 둔 복선을 끝까지 회수하지 않는 경우",
                    "diagnosis": "복선의 매설(발단·전개)과 회수(절정·결말)의 구조적 짝꿍 관계를 놓침.",
                    "prescription": "[활동 2]의 화살표를 확인시켜, 앞문단에 심은 힌트가 뒷문단 대화나 사건에서 반드시 풀리도록 짝을 맞추게 한다.",
                },
            ],
            "scaffolding_down": "문단별 개요 짜기가 어려운 학생에게는 6문단 시작 문장 스티커(‘1문단: 사건이 시작된 건 ~였다’, ‘2문단: 그런데 이상한 일이 ~’, ‘3문단: 갈등이 커진 건 ~’, ‘4문단: 내 마음속에서는 ~’, ‘5문단: 마침내 나는 숨을 들이마시고 ~’, ‘6문단: 비로소 ~’)를 제공하여 이어 쓰게 한다.",
            "scaffolding_up": "순행 구성으로 짠自分の 4단 플롯을 『꼴뚜기』처럼 ‘3교시 체육관에서 아이들이 웃음보를 터뜨리는 현재 장면’부터 시작하여 아침 일을 회상하는 ‘역순행적 구성’으로 문단 번호를 재조직해 보게 한다.",
            "rubric": {
                "high": "발단-전개-절정-결말의 4단 인과 사슬과 시간 구성, 복선 매설·회수 지점, 그리고 절정 장면의 간접 묘사(Show)·대화문·관용표현 배치 계획을 빈틈없이 구조화함.",
                "mid": "4단 플롯에 따라 사건 순서는 배치했으나, 복선 회수나 절정 장면의 구체적 Show 묘사 계획이 다소 소략함.",
                "low": "사건 간의 인과 관계가 끊어져 있거나 발단-전개-절정-결말의 단계 구분이 모호함.",
            },
        },
    },

    # =========================================================================
    # 15차시: G6-NAR-W4 초고 집필하기 (행동·신체 묘사[Show], 대화문, 감각어·관용표현, 시점·시제 통일 초고 집필)
    # =========================================================================
    {
        "lesson_title": "[초고 집필하기] ‘말하지 말고 보여주기(Show)’ 전략으로 단편 이야기 초고 쓰기",
        "std_badge": "[6국03-03] [6국04-04] [6국04-05]",
        "student_goal": "14차시에 완성한 4단 플롯 설계도를 바탕으로, 서술 시점과 시제를 일관되게 유지하며 간접 묘사(Show) 3곳 이상, 큰따옴표 대화문, 감각어·관용표현 2개 이상, 상징 소품을 녹여 완결된 단편 이야기 초고를 집필할 수 있다.",
        "marking_items": [
            ("mk-line-red", "빨간 밑줄", "간접 보여주기(Show: 행동·표정 묘사)"),
            ("mk-highlight", "형광펜", "감각어·복합어·관용표현"),
            ("mk-bg", "네모", "상징 소품 & 복선 구절"),
        ],
        "left_page_body_html": """
        <div style="background:#FFF8F0; border:0.8pt solid #F0B27A; border-radius:4px; padding:3.5px 8px; margin-bottom:4px; font-size:7.2pt; display:flex; justify-content:space-between; align-items:center;">
          <span>✍️ <strong>초고 집필 모델 텍스트:</strong> 6학년 김민준 학생이 『꼴뚜기』의 표현 전략을 미러링하여 쓴 초고 <strong>『주인을 찾은 짝짝이 실내화』</strong></span>
          <span style="color:#C85A17; font-weight:800;">Show·대화·복선 완벽 적용</span>
        </div>
        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📖 모범 초고 정독하기 — 『주인을 찾은 짝짝이 실내화』 (1인칭 주인공 시점)</th>
              <th class="wing-head">🧠 초고 집필 기술 날개</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-size:8.6pt; line-height:1.52;">
                <p><span class="p-num">➊</span><strong>[발단]</strong> 비가 추적추적 내리던 월요일 아침이었다. 지각을 면하려고 헐레벌떡 현관 신발장으로 뛰어든 나는 내 신발 주머니에서 실내화를 대충 꺼내 신고 교실로 전력 질주했다. 1교시 시작 종이 울리고 숨을 고르는데, 옆 분단에 앉은 전학생 박지호가 내 발밑을 힐끔 내려다보았다. 지호는 무슨 말을 하려는 듯 입술을 달싹이더니, 이내 아무 말 없이 자기 두 발을 책상 밑 깊숙한 곳으로 쑥 집어넣었다. <strong>(복선 매설)</strong></p>
                <p><span class="p-num">➋</span><strong>[전개·위기]</strong> 사건이 터진 건 3교시 체육관 이동 시간이었다. 줄을 서던 앞자리 아이가 지호의 발을 보더니 눈을 동그랗게 뜨고 외쳤다.<br>
                “야, 박지호 실내화 좀 봐! 왼발은 엄청 큰데 오른발은 꽉 끼는 짝짝이야!”<br>
                잠깐 정적이 흐르던 복도에 <span class="mk-highlight">키득키득</span> 웃음보가 터졌다. “헤이요, 짝짝이 전학생!” 아이들이 놀려 대는 소리에 무심코 내 발을 내려다본 나는 <span class="mk-highlight">가슴이 철렁 내려앉았다</span>. 내 오른발에 신겨 있는 조금 작은 실내화 뒤축에 지호의 표시인 <span class="mk-bg">초록색 별 스티커</span>가 선명하게 붙어 있었기 때문이다. 아침에 신발장에서 지호 주머니와 섞인 게 분명했다. 하지만 나는 <span class="mk-line-red">슬그머니 오른발을 왼발 뒤로 감추며 <span class="mk-highlight">마른침</span>을 꿀꺽 삼켰다.</span> 지금 말하면 애들이 나를 비웃을 것 같아 차마 입이 떨어지지 않았다. 지호는 <span class="mk-line-red">목덜미가 벌겋게 달아오른 채 <span class="mk-highlight">입을 꾹 다물고</span> 신발 코만 내려다보았다.</span></p>
                <p><span class="p-num">➌</span><strong>[절정]</strong> 체육 시간 내내 <span class="mk-highlight">목구멍 어디쯤에 가시가 박힌 것처럼 속이 뜨끔거렸다.</span> 쉬는 시간이 되자 또다시 몇몇 아이들이 지호 주변으로 몰려들어 “짝짝이 실내화 또 신었네!” 하며 낄낄거렸다. ‘난 하루 종일 용감할 순 없지만, 지금이 바로 내가 어쩌다 한 번 용감해져야 할 때야!’ <span class="mk-line-red">나는 숨을 크게 들이마신 뒤 두 주먹을 불끈 쥐고 지호 옆으로 성큼성큼 걸어 나갔다.</span> 그리고 모두가 보는 앞에서 내 오른발의 실내화를 벗어 탁 내려놓았다.<br>
                “잠깐만! 지호가 짝짝이로 신은 건 내 실수 때문이야. 아침에 내가 급해서 지호 실내화 한 짝을 잘못 신고 왔어. 미안해, 지호야!”<br>
                떠들썩하던 교실이 오디오 플러그가 뽑힌 것처럼 조용해졌다. 놀란 눈으로 나를 보던 지호가 조용히 미소 지으며 말했다.<br>
                “괜찮아, 민준아. 사실 1교시 때 네 발에 붙은 초록 별 스티커를 보고 알고 있었어. 네가 당황할까 봐 방과 후에 말하려고 했는데, 먼저 용기 내 줘서 고마워.” <strong>(복선 회수)</strong></p>
                <p><span class="p-num">➍</span><strong>[결말]</strong> 방과 후, 비가 개인 복도 창가로 따스한 햇살이 쏟아졌다. 제 짝을 찾아 나란히 놓인 <span class="mk-bg">하얀 실내화 두 켤레</span>가 눈부시게 반짝였다. 지호와 나란히 복도를 걸어 나가는 내 <span class="mk-highlight">발걸음</span>에 비로소 상쾌한 봄바람 냄새가 코끝에 달라붙었다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide">
                  <div class="wing-box-title"><span>👁️ 초고 집필 체크포인트</span><span class="role-chip">I Do 시범</span></div>
                  <div class="think-row"><span class="think-tag">[시점·시제]</span><span>처음부터 끝까지 <strong>1인칭(‘나’)</strong>과 <strong>과거 시제(‘-았/었-’)</strong>로 일관되게 통일했어!</span></div>
                  <div class="think-row"><span class="think-tag">[Show 묘사]</span><span>‘당황했다’ 대신 ‘오른발을 왼발 뒤로 감추며 마른침을 삼켰다’고 행동으로 보여 주었어!</span></div>
                  <div class="think-row"><span class="think-tag">[대화 규칙]</span><span>인물의 대사는 <strong>줄을 바꾸어 큰따옴표(“ ”)</strong>로 묶어 현장감을 살렸어!</span></div>
                </div>
                <div class="wing-box vocab">
                  <strong>💡 큰따옴표 대화문 표기 약속</strong><br>
                  • 대화문이 시작될 때는 <strong>줄을 바꾸고 한 칸 들여쓰기</strong> 합니다.<br>
                  • 마침표(.)나 느낌표(!), 물음표(?)는 <strong>닫는 큰따옴표(”) 안쪽</strong>에 찍습니다.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "[초고 집필 1단계: 발단 & 전개] 배경 분위기·복선 제시 및 갈등의 시작 쓰기",
            "tag": "Step 1 발단·전개 집필 ([6국03-03])",
            "body_html": """
            <div style="background:#FFFDFB; border:0.85pt solid #BDC3C7; border-radius:5px; padding:5px 8px; font-size:7.3pt; line-height:1.45;">
              <div style="display:flex; justify-content:space-between; font-weight:800; color:#2874A6; margin-bottom:2px;">
                <span>🖋️ [나의 단편 이야기 초고 — ① 발단 & ② 전개·위기 (시점·시제 통일!)]</span>
                <span>제목: 『 <span class="blank-slot"><span class="t-ans">주인을 찾은 짝짝이 실내화 (학생 자율 제목)</span></span> 』</span>
              </div>
              <span class="pencil-line">✏️ <strong>[발단 — 시공간 배경 감각어 & 복선 심기]:</strong> <span class="t-ans">비가 추적추적 내리던 월요일 아침이었다. 지각할까 봐 헐레벌떡 신발장으로 뛰어든 나는 실내화를 급히 꺼내 신고 교실로 달렸다. 1교시가 시작될 때 옆자리 전학생 지호가 내 발밑을 힐끔 보더니, 아무 말 없이 자기 발을 책상 밑 깊숙이 숨겼다.</span></span>
              <span class="pencil-line">✏️ <strong>[전개·위기 — 외적 갈등 & 내적 갈등(관용표현 1개 이상 포함)]:</strong> <span class="t-ans">사건이 터진 건 3교시 체육 시간이었다. 아이들이 지호의 짝짝이 실내화를 보고 “짝짝이 전학생!”이라며 키득키득 웃어 댔다. 내 오른발 뒤축에 붙은 지호의 초록 별 스티커를 발견한 순간 나는 가슴이 철렁 내려앉았다. 하지만 나까지 놀림받을까 봐 오른발을 슬쩍 숨긴 채 입을 꾹 다물었다. 체육 시간 내내 목구멍에 가시가 박힌 것처럼 속이 뜨끔거렸다.</span></span>
            </div>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 위기를 최고조로 끌어올려 간접 묘사(Show)와 큰따옴표 대화문으로 ‘절정’ 장면 집필하기",
        "activity_2": {
            "title": "[초고 집필 2단계: 절정] 행동·표정 묘사(Show)와 대화문으로 갈등 해결 장면 쓰기",
            "tag": "Step 2 절정 Show·대화 집필 ([6국04-04])",
            "body_html": """
            <div style="background:#FFFDFB; border:0.9pt solid #E74C3C; border-radius:5px; padding:5px 8px; font-size:7.3pt; line-height:1.45;">
              <div style="font-weight:800; color:#C0392B; margin-bottom:2px;">⛰️ [나의 단편 이야기 초고 — ③ 절정 (Show 행동 묘사 2곳 이상 + 큰따옴표 대화문 필수!)]</div>
              <span class="pencil-line">✏️ <strong>[결단 행동 묘사 Show]:</strong> <span class="t-ans">쉬는 시간에 애들이 다시 지호를 에워싸고 놀리려 했다. ‘지금이 바로 내가 어쩌다 한 번 용감해져야 할 때야!’ 나는 숨을 크게 들이마신 뒤 두 주먹을 불끈 쥐고 지호 옆으로 성큼성큼 걸어 나갔다. 그리고 내 오른발 실내화를 벗어 탁 내려놓았다.</span></span>
              <span class="pencil-line">✏️ <strong>[결정적 큰따옴표 대화문 (“ ”)]:</strong> <span class="t-ans">“잠깐만! 지호가 짝짝이로 신은 건 내 실수 때문이야. 아침에 내가 급해서 지호 실내화 한 짝을 잘못 신고 왔어. 미안해, 지호야!”</span></span>
              <span class="pencil-line">✏️ <strong>[주변 반응 Show & 복선 회수]:</strong> <span class="t-ans">교실이 오디오 플러그가 뽑힌 것처럼 조용해졌다. 지호는 환하게 미소 지으며 “사실 1교시부터 알고 있었어. 네가 당황할까 봐 기다렸는데 먼저 말해 줘서 고마워.”라고 대답했다.</span></span>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 절정 이후 변화된 마음과 상징 소품의 감각적 여운을 담아 ‘결말’ 완성하기",
        "activity_3": {
            "title": "[초고 집필 3단계: 결말] 인물의 내면적 성장과 상징 소품의 감각적 여운으로 끝맺기",
            "tag": "Step 3 결말 완결 ([6국04-05])",
            "body_html": """
            <div style="background:#FFFDFB; border:0.85pt solid #D35400; border-radius:5px; padding:5px 8px; font-size:7.3pt; line-height:1.45;">
              <div style="font-weight:800; color:#D35400; margin-bottom:2px;">🌅 [나의 단편 이야기 초고 — ④ 결말 (설교 대신 상징 소품과 오감 이미지로 여운 남기기!)]</div>
              <span class="pencil-line">✏️ <strong>[결말 문단]:</strong> <span class="t-ans">방과 후, 비가 개인 복도 창가로 따스한 햇살이 쏟아졌다. 제 짝을 찾아 나란히 놓인 하얀 실내화 두 켤레가 눈부시게 반짝였다. 지호와 어깨를 나란히 하고 복도를 걸어 나가는 내 발걸음에 비로소 상쾌한 봄바람 냄새가 코끝에 달라붙었다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "16차시(W5 고쳐쓰기) 3단계 메타인지 퇴고 및 교정부호 첨삭 대상으로 직결",
            "prompt": "방금 쓴 초고를 다시 읽으며, 어색한 문장이나 직접 설명(Tell)으로 써서 다음 시간(16차시)에 더 생생하게 고치고 싶은 부분을 1곳 찾아 표시해 두세요.",
            "placeholder": "(예: 전개 부분의 ‘나는 너무 미안했다’를 행동 묘사로 바꾸고 싶음 / 시제가 현재형으로 섞인 곳 수정)",
            "example_answer": "전개 문단에서 ‘지호는 창피해 보였다’라고 설명한 부분을 ‘지호의 목덜미가 벌겋게 달아오른 채 신발 코만 내려다보았다’로 고쳐 써야겠다.",
        },
        "self_check": [
            "설정한 서술 시점(1인칭 또는 3인칭)과 과거 시제(‘-았/었-’)를 끝까지 일관되게 유지했나요?",
            "직접 감정 설명(Tell) 대신 행동·표정·비유로 보여 주는 묘사(Show)를 3곳 이상 넣었나요?",
            "큰따옴표 대화문과 감각어·관용표현, 상징 소품과 복선이 자연스럽게 어우러졌나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[초고 집필 4대 수칙] ①시점·시제 통일(1인칭 ‘나’ / 3인칭 이름, ‘-았/었-’) + ②Show 묘사 3곳 이상(행동·표정·비유) + ③큰따옴표 대화문 줄바꿈 규칙 + ④상징 소품과 감각적 결말",
            "intro_5min": "12~14차시 동안 차곡차곡 준비한 기획서, 인물·상징 카드, 4단 플롯 설계도를 책상 위에 펼쳐 놓게 한다. 좌측 페이지의 모범 초고 『주인을 찾은 짝짝이 실내화』를 함께 읽으며 『꼴뚜기』의 표현 기법이 어떻게 내 글로 재탄생했는지 감상한다.",
            "ido_think_aloud_script": "“선생님이 좌측 모범 초고의 ➋문단과 ➌문단을 보며 초고 집필 비법을 짚어 줄게요. 만약 민준이가 ‘나는 내 발에 지호 실내화가 있는 걸 보고 깜짝 놀랐고 무서워서 숨겼다’라고만 썼다면 평범한 글이 되었을 거예요. 하지만 민준이는 ‘가슴이 철렁 내려앉았다(관용표현)’, ‘슬그머니 오른발을 왼발 뒤로 감추며 마른침을 꿀꺽 삼켰다(Show 행동 묘사)’라고 썼어요! 그리고 절정에서 대사를 쓸 때는 줄을 바꾸고 큰따옴표(“ ”)를 열었죠? 여러분도 오늘 초고를 쓸 때 이 3가지 기술을 꼭 사용해 보세요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하고 찾기(Think & Search)",
                    "question": "모범 초고의 ➊문단 마지막 문장(지호가 자기 발을 책상 밑으로 집어넣은 행동)과 ➌문단 마지막 지호의 대사는 어떻게 서로 호응하고 있나요?",
                    "expected_ans": "➊문단에서 심어 둔 복선(왜 지호가 자기 발을 숨겼을까?)이 ➌문단 지호의 대사(‘1교시 때부터 알고 있었지만 네가 당황할까 봐 기다렸어’)를 통해 감동적으로 회수되고 있습니다.",
                    "reprompt": "14차시에서 우리가 설계한 ‘복선 심기 ➔ 거두기’가 실제 문장으로 어떻게 쓰였는지 비교해 보세요.",
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "초고를 쓰는 도중에 맞춤법이나 문장 호응이 조금 헷갈릴 때는 멈춰서 지우개로 계속 지워야 할까요, 아니면 일단 끝까지 흐름을 이어 써야 할까요?",
                    "expected_ans": "초고 집필 단계에서는 생각의 흐름과 장면의 생생함이 끊기지 않도록 일단 결말까지 완주하여 쓰고, 세밀한 어법·맞춤법 교정은 다음 시간(16차시 고쳐쓰기)에 교정부호로 다듬는 것이 좋습니다.",
                    "reprompt": "과정중심 쓰기에서 15차시(초고 쓰기)와 16차시(고쳐쓰기)의 역할이 왜 나뉘어 있는지 생각해 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1](발단·전개) ➔ [활동 2](절정) ➔ [활동 3](결말) 순서로 집중하여 초고를 집필하도록 20분 이상 충분한 집필 시간을 확보해 준다. 교사는 순회하며 ‘화났다, 슬펐다’ 같은 Tell 표현 밑에 작은 물결선을 그어 주며 행동 묘사(Show)로 확장하도록 격려한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 모범 초고 예시 (발단·전개):</strong> 비가 추적추적 내리던 월요일 아침이었다. 지각할까 봐 헐레벌떡 신발장으로 뛰어든 나는 실내화를 급히 꺼내 신고 교실로 달렸다. 1교시가 시작될 때 옆자리 전학생 지호가 내 발밑을 힐끔 보더니 아무 말 없이 자기 발을 책상 밑 깊숙이 숨겼다. 사건이 터진 건 3교시 체육 시간이었다. 아이들이 지호의 짝짝이 실내화를 보고 키득키득 웃어 댔다. 내 오른발 뒤축에 붙은 초록 별 스티커를 발견한 순간 가슴이 철렁 내려앉았지만, 나까지 놀림받을까 봐 오른발을 숨긴 채 입을 꾹 다물었다. 목구멍에 가시가 박힌 것처럼 속이 뜨끔거렸다.<br>
              <strong>• [활동 2] 모범 초고 예시 (절정):</strong> 쉬는 시간에 애들이 다시 지호를 놀리려 했다. 나는 숨을 크게 들이마신 뒤 두 주먹을 불끈 쥐고 지호 옆으로 성큼성큼 걸어 나가 내 오른발 실내화를 벗어 탁 내려놓았다. “잠깐만! 지호가 짝짝이로 신은 건 내 실수 때문이야. 아침에 내가 급해서 잘못 신고 왔어. 미안해, 지호야!” 교실이 오디오 플러그가 뽑힌 것처럼 조용해졌고, 지호는 미소 지으며 “사실 1교시부터 알고 있었어. 먼저 말해 줘서 고마워.”라고 대답했다.<br>
              <strong>• [활동 3] 모범 초고 예시 (결말):</strong> 방과 후 비가 개인 복도 창가로 따스한 햇살이 쏟아졌다. 제 짝을 찾아 나란히 놓인 하얀 실내화 두 켤레가 눈부시게 반짝였고, 지호와 나란히 걷는 내 발걸음에 상쾌한 봄바람 냄새가 코끝에 달라붙었다.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "대화문을 쓸 때 큰따옴표를 쓰지 않거나 ‘지호가 괜찮다고 말했고 나도 미안하다고 말했다’처럼 전부 간접화법으로만 처리하는 경우",
                    "diagnosis": "절정 장면에서 직접 인용(큰따옴표 대화문)이 주는 현장감과 극적 긴장감의 효과를 활용하지 못함.",
                    "prescription": "가장 중요한 절정 장면의 대사 최소 2개는 반드시 큰따옴표(“ ”)를 사용하여 인물의 목소리가 직접 들리도록 쓰게 지도한다.",
                },
                {
                    "error_case": "앞문단에서는 ‘나는 걸어갔다(1인칭 과거)’라고 쓰다가 뒷문단에서 ‘민준이는 걸어간다(3인칭 현재)’로 시점과 시제가 뒤섞이는 경우",
                    "diagnosis": "긴 호흡의 글을 쓰면서 처음에 설정한 서술 시점과 시제 통제력을 잃음.",
                    "prescription": "문단 끝 서술어마다 ‘-았/었-’ 과거 시제 어미가 일관되게 쓰였는지, 주어가 ‘나’로 통일되었는지 밑줄을 그어 확인하게 한다.",
                },
            ],
            "scaffolding_down": "글쓰기 분량 확장이 어려운 학생에게는 좌측 페이지 모범 초고의 문장 구조를 패러디(모방 창작)하여 소재(실내화 ➔ 우산/필통/실습 재료)와 인물 이름만 자신의 기획안으로 바꾸어 완성해 보게 한다.",
            "scaffolding_up": "절정 장면에서 주인공의 내적 독백(작은따옴표 ‘ ’ 속마음 문장)과 외적 대사(큰따옴표 “ ” 대화 문장)를 교차 배치하여 인물의 심리적 긴장감을 한층 정교하게 표현해 보게 한다.",
            "rubric": {
                "high": "설정한 서술 시점과 시제를 일관되게 유지하며, 간접 묘사(Show) 3곳 이상, 큰따옴표 대화문, 감각어·관용표현 2개 이상, 상징 소품과 복선 회수가 유기적으로 어우러진 완결된 단편 이야기 초고를 집필함.",
                "mid": "4단 플롯에 따라 완결된 이야기 초고를 작성했으나, 간접 묘사(Show)보다 직접 설명(Tell)의 비중이 다소 높거나 시제 불일치가 일부 나타남.",
                "low": "이야기가 중간에 끊겨 결말이 완결되지 않았거나 대화문과 묘사 없이 줄거리 요약처럼 짧게 작성함.",
            },
        },
    },

    # =========================================================================
    # 16차시: G6-NAR-W5 고쳐쓰기 (내용 개연성·조직 통일성·표현 어법[주술·부사어 호응, 시제, 문장부호] 3단계 교정부호 퇴고 및 출판)
    # =========================================================================
    {
        "lesson_title": "[고쳐쓰기·출판] 2층 첨삭 줄공책과 교정부호로 퇴고하여 학급 단편집 출판하기",
        "std_badge": "[6국03-06] [6국04-05] [6국05-05]",
        "student_goal": "초고를 ‘내용(개연성·주제)-조직(문단·시점 통일)-표현(Tell➔Show 변환, 주어·서술어·부사어 호응, 시제, 큰따옴표 문장부호)’의 3단계 기준으로 점검하고, 교정부호를 사용하여 고쳐 쓴 뒤 학급 단편집으로 출판할 수 있다.",
        "marking_items": [
            ("mk-line-red", "빨간 밑줄", "주술·부사어·시제 호응 오류"),
            ("mk-line-blue", "파란 밑줄", "Tell(직접 설명) ➔ Show(행동 묘사) 변환 대상"),
            ("mk-highlight", "형광펜", "큰따옴표·말줄임표 등 문장부호 교정"),
        ],
        "left_page_body_html": """
        <div style="background:#FFF8F0; border:0.8pt solid #F0B27A; border-radius:4px; padding:3.5px 8px; margin-bottom:4px; font-size:7.2pt; display:flex; justify-content:space-between; align-items:center;">
          <span>🔍 <strong>2층 고행간 첨삭 줄공책(Double-Line Revision Studio):</strong> 초고의 5대 어법·표현 결함을 교정부호로 고쳐 쓰는 시범</span>
          <span style="color:#C0392B; font-weight:800;">[6국03-06] [6국04-05]</span>
        </div>

        <!-- 2층 고행간 첨삭 줄공책 실연 그리드 -->
        <div class="draft-revision-grid" style="margin-bottom:5px;">
          <div class="notebook-pane">
            <!-- 발단 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">발단<br><span style="font-size:6pt; color:#7F8C8D;">1문단</span></div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ “야, 이 짝짝이 실내화 누구 거냐?” 하고 외쳤지만,</div>
                  <div class="nb-lower-write">월요일 아침 복도에서 준서가 <span class="mk-highlight">야 이 짝짝이 실내화 누구 거냐 하고 외쳤지만</span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">───(삭제: 결코)─── &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ───(시제 교정: 숨겼다.)</div>
                  <div class="nb-lower-write">나는 <span class="mk-line-red">결코</span> 놀림받을까 봐 오른발을 책상 밑으로 <span class="mk-line-red">숨긴다.</span></div>
                </div>
              </div>
            </div>
            <!-- 전개·위기 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">전개<br>위기<br><span style="font-size:6pt; color:#7F8C8D;">2문단</span></div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">───(Tell➔Show 교체: 아랫입술을 꽉 깨물며 신발 코만 내려다보았다.)───</div>
                  <div class="nb-lower-write">억울한 누명을 쓴 지호는 <span class="mk-line-blue">너무나 창피하고 속상하고 화가 많이 났다.</span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">───(주술 호응 교정: 못 본 척했다는 점 때문에 마음이 무거웠다.)───</div>
                  <div class="nb-lower-write"><span class="mk-line-red">내가 가장 부끄러웠던 까닭은</span> 지호의 아픔을 <span class="mk-line-red">못 본 척했다.</span></div>
                </div>
              </div>
            </div>
            <!-- 절정·결말 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">절정<br>결말<br><span style="font-size:6pt; color:#7F8C8D;">3문단</span></div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">¶(줄바꿈) &nbsp; ∨ 마치 오디오 플러그가 뽑힌 것처럼</div>
                  <div class="nb-lower-write">나는 앞으로 나가 “내 실수야!”라고 외쳤다. 교실은 <span class="mk-line-red">오디오 플러그가 뽑혔다.</span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">───(시점 통일: 나는)─── &nbsp; &nbsp; &nbsp; ───(여운 결말: 구수한 봄바람이 코끝을 스쳤다.)</div>
                  <div class="nb-lower-write">지호가 웃어 주자 <span class="mk-line-red">민준이는</span> 기분이 좋아져서 <span class="mk-line-blue">착하게 살기로 다짐했다.</span></div>
                </div>
              </div>
            </div>
          </div>

          <!-- 우측 첨삭 해설 & 교정부호 가이드 패널 -->
          <div style="background:#F8F9F9; padding:5px 6px; font-size:7pt; line-height:1.38; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-weight:800; color:#C0392B; border-bottom:0.8pt solid #BDC3C7; padding-bottom:2px; margin-bottom:3px;">🩺 5대 퇴고 클리닉 진단</div>
              <div style="margin-bottom:2.5px;"><strong>① 문장부호:</strong> 직접 대사에는 <strong>큰따옴표(“ ”)</strong>와 쉼표(,)를 정확히 표기함.</div>
              <div style="margin-bottom:2.5px;"><strong>② 부사어·시제 호응:</strong> 부사어 ‘결코’는 부정어(‘않았다’)와 호응하므로 삭제! 현재형 ‘숨긴다’를 과거 시제 <strong>‘숨겼다’</strong>로 통일함.</div>
              <div style="margin-bottom:2.5px;"><strong>③ Tell➔Show 변환:</strong> ‘창피하고 화가 났다’를 <strong>‘아랫입술을 꽉 깨물며 신발 코만 내려다보았다’</strong>로 생생하게 교체!</div>
              <div style="margin-bottom:2.5px;"><strong>④ 주어-서술어 호응:</strong> ‘~까닭은’과 ‘~척했다’가 안 맞으므로 <strong>‘~까닭은 ~척했다는 점이다’</strong>로 교정!</div>
              <div><strong>⑤ 시점 통일 & 여운 결말:</strong> 1인칭 글에서 갑자기 나온 ‘민준이는’을 <strong>‘나는’</strong>으로 고치고 설교 결말을 감각적 여운으로 교체!</div>
            </div>
            <div style="background:#FFFFFF; border:0.7pt solid #BDC3C7; border-radius:4px; padding:3px 5px; font-size:6.7pt;">
              <strong>✏️ 필수 교정부호 5종:</strong><br>
              • <strong>─── (교정):</strong> 내용 바꾸기 &nbsp; • <strong>∨ (삽입):</strong> 글자 넣기<br>
              • <strong>═ (삭제):</strong> 지우기 &nbsp; • <strong>¶ (줄바꿈):</strong> 문단 나누기<br>
              • <strong>⏝ (이어쓰기):</strong> 줄 잇기
            </div>
          </div>
        </div>
        """,
        "activity_1": {
            "title": "어법·문장 호응(주술·부사어·시제·문장부호) 및 Tell➔Show 오류 찾아 바르게 고치기",
            "tag": "Step 1·2 오류 진단 및 교정 ([6국04-05])",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">퇴고 점검 영역</th>
                  <th style="width:38%;">오류가 있는 초고 문장 (Before)</th>
                  <th style="width:40%;">어법과 표현 전략에 맞게 고쳐 쓴 문장 (After)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>주어-서술어 호응</strong><br>([6국04-05])</td>
                  <td>내 마음이 가장 괴로웠던 이유는 친구의 고통을 모른 척하고 지나쳤다.</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">내 마음이 가장 괴로웠던 이유는 친구의 고통을 모른 척하고 지나쳤기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td><strong>부사어 호응 & 시제</strong><br>([6국04-05])</td>
                  <td>아이들의 노랫소리는 <strong>마치</strong> 오디오 플러그가 뽑혔다. 그래서 교실이 조용해진다.</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">아이들의 노랫소리는 마치 오디오 플러그가 뽑힌 것처럼 끊겼다. 그래서 교실이 조용해졌다.</span></span></td>
                </tr>
                <tr>
                  <td><strong>Tell ➔ Show 변환<br>& 큰따옴표 부호</strong></td>
                  <td>나는 너무 무서웠지만 용기를 내어 잠깐만 그건 내 실수야 라고 말했다.</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">나는 다리가 후들거렸지만 두 주먹을 불끈 쥐고 “잠깐만! 그건 내 실수야!”라고 외쳤다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 교정 원리를 적용하여 15차시에 쓴 내 초고를 [내용-조직-표현] 3단계 루브릭으로 상호·자기 점검하기",
        "activity_2": {
            "title": "내용·조직·표현 3단계 메타인지 퇴고 체크리스트 및 짝 상호 피드백",
            "tag": "Step 2 3단계 퇴고 점검 ([6국03-06])",
            "body_html": """
            <div class="inference-row" style="grid-template-columns: 1fr 1fr 1fr; gap:5px;">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">① 내용 수준 (개연성·주제)</strong><br>
                □ 갈등이 우연이 아니라 주인공의 용기 있는 선택으로 해결되었는가?<br>
                □ 앞부분에 심은 복선이 절정에서 자연스럽게 회수되었는가?
              </div>
              <div class="inf-card c2">
                <strong style="color:var(--mark-green);">② 조직 수준 (시점·문단)</strong><br>
                □ 발단-전개-절정-결말 및 대화문마다 줄바꿈(¶)을 바르게 했는가?<br>
                □ 1인칭(‘나’) 또는 3인칭 시점이 끝까지 흔들리지 않았는가?
              </div>
              <div class="inf-card c3">
                <strong style="color:#D35400;">③ 표현 수준 (Show·어법)</strong><br>
                □ 추상적 감정(Tell)을 행동·표정(Show)과 관용표현으로 바꾸었는가?<br>
                □ 주어-서술어·부사어 호응과 과거 시제, 큰따옴표가 정확한가?
              </div>
            </div>
            <div style="background:#F8F9F9; border:0.75pt solid #BDC3C7; border-radius:4px; padding:3.5px 7px; font-size:7.2pt;">
              <strong>🤝 짝 작가의 한 줄 칭찬 & 퇴고 제안:</strong> <span class="pencil-line" style="display:inline-block; width:72%; min-height:4.5mm; line-height:4.5mm;">✏️ <span class="t-ans">초록 별 스티커 복선이 정말 멋져! 절정 부분의 감정 설명 한 문장만 행동 묘사(Show)로 바꾸면 완벽하겠어.</span></span>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 퇴고를 거쳐 최종 완성본 핵심 장면을 정서(깨끗이 고쳐 쓰기)하고 학급 단편집 ‘작가의 말’ 남기기",
        "activity_3": {
            "title": "최종 퇴고 완성본 하이라이트 정서 및 학급 단편집 『어쩌다 용감해지는 날』 출판 쇼케이스",
            "tag": "Step 3 최종 작품 완성 및 출판",
            "body_html": """
            <div style="background:#FFFDFB; border:1pt solid #C85A17; border-radius:5px; padding:5px 8px; font-size:7.3pt; line-height:1.45;">
              <div style="display:flex; justify-content:space-between; border-bottom:0.8pt solid #F0B27A; padding-bottom:2px; margin-bottom:3px; font-weight:800; color:#C85A17;">
                <span>📖 [우리 반 창작 단편집 수록 최종본 — 내가 가장 공들여 고쳐 쓴 절정·결말 명장면]</span>
                <span>작가: ( &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; )</span>
              </div>
              <span class="pencil-line">✏️ <span class="t-ans">나는 마른침을 꿀꺽 삼키고 두 주먹을 불끈 쥔 채 지호 옆으로 성큼성큼 걸어 나갔다. “잠깐만! 지호가 짝짝이로 신은 건 아침에 내가 급해서 지호 실내화 한 짝을 잘못 신고 왔기 때문이야. 미안해, 지호야!” 교실은 마치 오디오 플러그가 뽑힌 것처럼 조용해졌다. 지호가 따스하게 웃어 주던 그 순간, 내 목구멍에 박혀 있던 가시가 스르르 녹아내리며 상쾌한 봄바람 냄새가 코끝에 달라붙었다.</span></span>
              <div style="margin-top:3px;"><strong>🎙️ [단편집 뒤표지에 실을 ‘작가의 말’ 한 줄]:</strong></div>
              <span class="pencil-line">✏️ <span class="t-ans">장난스러운 별명 뒤에 숨어 침묵했던 모든 친구들에게, ‘어쩌다 한 번씩 용감해지는’ 따뜻한 포크 하나를 건네고 싶어 이 이야기를 썼습니다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "2단원(이야기) 대단원 갈무리 및 3단원(수필: 삶의 성찰)로의 종적·횡적 확장",
            "prompt": "2단원 『꼴뚜기』 읽기와 나만의 단편 이야기 창작을 모두 마치며, ‘이야기를 읽고 쓰는 힘’이 나를 어떻게 성장시켰는지 한 줄로 적어 보세요.",
            "placeholder": "(예: 인물의 침묵 뒤에 숨은 아픔을 읽을 수 있게 되었고, 내 마음을 생생한 행동으로 표현하는 법을 배웠다.)",
            "example_answer": "겉으로 드러난 행동 너머에 있는 친구의 속마음을 깊이 추론할 줄 알게 되었고, 직접 설명하기보다 행동과 비유로 보여 주는 글쓰기의 즐거움을 깨달았다.",
        },
        "self_check": [
            "내용(개연성·복선), 조직(시점·문단 줄바꿈), 표현(Show 묘사·어법)의 3단계로 꼼꼼히 퇴고했나요?",
            "주어-서술어·부사어 호응 오류와 시제 불일치, 큰따옴표 문장부호를 교정부호로 바르게 고쳤나요?",
            "완성된 단편 이야기를 친구들과 나누어 읽으며 서로의 성장을 축하했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[3단계 메타인지 퇴고] ①내용(개연성·복선 회수) ➔ ②조직(시점 통일·대화문 줄바꿈 ¶) ➔ ③표현(Tell➔Show 교체 + 주술/부사어 호응 + 과거 시제 + 큰따옴표) / [출판] 학급 단편집 『어쩌다 용감해지는 날』 낭독회",
            "intro_5min": "유명한 동화 작가들도 초고를 쓴 뒤 수십 번 고쳐 쓰며(퇴고) 문장을 보석처럼 다듬는다는 사실을 알려 준다. 좌측 페이지의 ‘2층 고행간 첨삭 줄공책’을 함께 보며 윗줄(빨간 교정부호)이 아랫줄(초고)을 어떻게 명문장으로 바꾸었는지 탐색한다.",
            "ido_think_aloud_script": "“선생님이 좌측 2층 줄공책의 2문단과 3문단을 어떻게 고쳤는지 사고구술해 볼게요. 첫째, 어법 호응을 볼까요? ‘내가 가장 부끄러웠던 까닭은 지호의 아픔을 못 본 척했다’라고 쓰면 주어(‘까닭은’)와 서술어(‘척했다’)가 짝이 안 맞아요! 그래서 ‘~못 본 척했다는 점이다(또는 척했기 때문이다)’로 고쳤어요. 둘째, 부사어 ‘마치’가 나오면 뒤에는 반드시 ‘~처럼 / ~듯’이 호응해야 해요. 셋째, 문학적 표현을 볼까요? ‘지호는 너무나 창피하고 속상하고 화가 났다(Tell)’에 교정줄(───)을 긋고 ‘아랫입술을 꽉 깨물며 신발 코만 내려다보았다(Show)’로 바꾸니 문장이 단숨에 살아났죠!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하고 찾기(Think & Search)",
                    "question": "좌측 2층 줄공책의 1문단에서 ‘나는 결코 놀림받을까 봐 오른발을 책상 밑으로 숨긴다’에는 어떤 두 가지 어법 오류가 숨어 있었나요?",
                    "expected_ans": "첫째, ‘결코’는 뒤에 부정 표현(‘~하지 않는다’)이 와야 하는 부사어인데 긍정 서술어(‘숨긴다’)와 쓰여 호응 오류가 났고, 둘째, 이야기 전체가 과거 시제인데 갑자기 현재 시제(‘숨긴다’)가 쓰여 시제가 어긋났습니다.",
                    "reprompt": "‘결코’와 어울리는 서술어가 무엇인지, 그리고 앞문장의 시제(‘외쳤지만’)와 뒷문장의 시제(‘숨긴다’)가 맞는지 확인해 보세요.",
                },
                {
                    "qar_type": "내 생각(On My Own)",
                    "question": "짝과 바꾸어 초고를 읽고 피드백해 줄 때(상호 퇴고), 친구의 기분을 존중하면서도 실질적인 도움을 주려면 어떻게 말해야 할까요?",
                    "expected_ans": "먼저 친구의 글에서 복선이나 비유가 잘 쓰인 멋진 구절을 찾아 구체적으로 칭찬한 뒤, ‘절정 부분의 이 감정 설명을 행동 묘사로 바꾸면 훨씬 더 실감 날 것 같아!’처럼 대안을 함께 제안해야 합니다.",
                    "reprompt": "[활동 2] 하단의 ‘짝 작가의 한 줄 칭찬 & 퇴고 제안’ 예시를 참고해 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]의 어법 교정 연습을 마친 뒤, [활동 2] 체크리스트로 자신의 15차시 초고를 첨삭하고 [활동 3]에 최종 명장면과 ‘작가의 말’을 정서하게 한다. 완성된 작품들을 모아 학급 문집으로 제본하거나 교실 뒤편 ‘우리 반 작가 갤러리’에 전시하며 2단원(이야기) 전 16차시 대장정을 감동적으로 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 모범 답안:</strong> ① 내 마음이 가장 괴로웠던 이유는 친구의 고통을 모른 척하고 지나쳤기 때문이다(지나쳤다는 점이다). / ② 아이들의 노랫소리는 마치 오디오 플러그가 뽑힌 것처럼 끊겼다. 그래서 교실이 조용해졌다. / ③ 나는 다리가 후들거렸지만 두 주먹을 불끈 쥐고 “잠깐만! 그건 내 실수야!”라고 외쳤다.<br>
              <strong>• [활동 2] 예시 답안:</strong> 초록 별 스티커 복선이 정말 멋져! 절정 부분의 감정 설명 한 문장만 행동 묘사(Show)로 바꾸면 완벽하겠어.<br>
              <strong>• [활동 3] 예시 답안:</strong> (최종 정서) 나는 마른침을 꿀꺽 삼키고 두 주먹을 불끈 쥔 채 지호 옆으로 성큼성큼 걸어 나갔다. “잠깐만! 지호가 짝짝이로 신은 건 아침에 내가 급해서 잘못 신고 왔기 때문이야. 미안해, 지호야!” 교실은 마치 오디오 플러그가 뽑힌 것처럼 조용해졌다. 지호가 따스하게 웃어 주던 그 순간, 내 목구멍에 박혀 있던 가시가 스르르 녹아내리며 상쾌한 봄바람 냄새가 코끝에 달라붙었다. / (작가의 말) 장난스러운 별명 뒤에 숨어 침묵했던 모든 친구들에게 따뜻한 포크 하나를 건네고 싶어 이 이야기를 썼습니다.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "퇴고 단계에서 맞춤법이나 띄어쓰기 한두 개만 고치고, 정작 중요한 ‘내용 개연성’이나 ‘Tell➔Show 표현 변환’은 전혀 건드리지 않는 경우",
                    "diagnosis": "고쳐쓰기(퇴고)를 단순한 철자 교정으로만 좁게 인식함.",
                    "prescription": "[활동 2]의 3단계(①내용 ➔ ②조직 ➔ ③표현) 순서를 짚어 주며, 최소 1곳 이상의 감정 설명 문장(Tell)을 행동 묘사(Show)로 바꾸는 것을 필수 미션으로 부여한다.",
                },
                {
                    "error_case": "부사어 ‘마치’, ‘결코’, ‘비록’을 쓰고도 뒤에 호응하는 어미(‘~처럼’, ‘~않다’, ‘~일지라도’)를 빠뜨리는 경우",
                    "diagnosis": "짝을 이루는 부사어-서술어 호응 규칙([6국04-05])에 대한 문법적 민감도가 부족함.",
                    "prescription": "칠판에 [짝꿍 부사어 공식: 결코/절대로 ~ 않다, 마치 ~ 처럼/듯, 비록 ~ 일지라도, 왜냐하면 ~ 때문이다]를 게시하여 자신의 초고와 대조 점검하게 한다.",
                },
            ],
            "scaffolding_down": "스스로 오류를 찾기 어려운 학생에게는 교사가 학생 초고에서 ①주술 호응 오류 1곳, ②Tell 문장 1곳, ③문장부호 누락 1곳에 연필로 작은 별표(☆)를 표시해 주어 그 3곳을 집중적으로 고치게 안내한다.",
            "scaffolding_up": "완성된 단편 이야기를 4컷 북트레일러(책 소개 카드뉴스) 또는 낭독 극본으로 재구성하여 학급 출판 기념회에서 발표해 보게 한다.",
            "rubric": {
                "high": "내용(개연성·복선), 조직(문단 줄바꿈·시점 통일), 표현(Tell➔Show 변환, 주술·부사어 호응, 과거 시제, 큰따옴표 부호)에서 5곳 이상을 교정부호로 정확히 첨삭하고 완성도 높은 최종 작품을 출판함.",
                "mid": "주술·부사어 호응 오류와 문장부호는 바르게 교정했으나, Tell 문장을 Show 묘사로 확장하는 표현 퇴고가 다소 소극적임.",
                "low": "초고의 문법적 호응 오류나 시점·시제 불일치를 찾지 못하고 초고를 그대로 베껴 씀.",
            },
        },
    },
]
