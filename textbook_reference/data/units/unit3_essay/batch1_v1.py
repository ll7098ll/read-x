# -*- coding: utf-8 -*-
"""
3단원: 수필 (unit3_essay) — Batch 1 (1~4차시: 사실적 이해 V1-1 ~ V1-4)
제재: 법정, 〈무소유〉 (『현대문학』 1971 / 수필집 『무소유』, 범우사, 1976 / 중·고등 국어 교과서 수록 원문 100%)
"""

BATCH1 = [
    # =========================================================================
    # 1차시: G6-ESS-V1-1 (내용 확인)
    # 체험 사실·관찰 묘사와 내면 성찰의 층위 분리 및 갈래 특성 확인
    # =========================================================================
    {
        "lesson_no": 1,
        "code": "G6-ESS-V1-1",
        "lesson_title": "겪은 일과 마음의 깨달음 구분하며 수필 읽기",
        "std_badge": "[6국05-01] [6국04-02] 복합어·감각어·갈래특성",
        "student_goal": "글쓴이가 직접 겪은 체험 사실·관찰 묘사(감각어·복합어 포함)와 내면의 성찰 문장을 구분하고 수필 갈래의 특성을 설명할 수 있다.",
        "marking_items": [
            ("mk-line-blue", "파란 밑줄", "글쓴이가 직접 겪은 일(외적 체험·사실)"),
            ("mk-bg", "초록 □", "대상을 생생히 나타낸 감각어·복합어"),
            ("mk-line-red", "빨간 밑줄", "마음속 생각과 삶의 깨달음(내면 성찰)"),
        ],
        "left_page_body_html": """
        <div style="background:#EEF9F3; border:0.8pt solid #82E0AA; border-radius:5px; padding:4px 8px; margin-bottom:5px; display:flex; justify-content:space-between; align-items:center; font-size:7.4pt;">
          <span>📖 <strong>본문 제재: 〈무소유(無所有)〉</strong> — 법정(法頂, 1932~2010) | 출처: 수필집 『무소유』(범우사, 1976)</span>
          <span style="color:#1E8449; font-weight:800;">갈래: 경수필(성찰적 수필)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📜 본문 정독 — 겪은 일(🔵)과 깨달음(🔴)의 층위를 나누며 읽기</th>
              <th class="wing-head">🧠 사고구술 &amp; 어휘 날개</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span> 나는 지난해 여름까지 <span class="mk-person">난초 두 분(盆)</span>을 <span class="mk-bg">정성스레</span>, 정말 정성을 다해 길렀었다. <span class="mk-line-blue">3년 전 거처를 지금의 다래헌(茶來軒)으로 옮겨 왔을 때 어떤 스님이 우리 방으로 보내 준 것이다.</span> 혼자 사는 거처라 살아 있는 생물이라고는 나하고 그 애들뿐이었다. <span class="mk-line-blue">그 애들을 위해 관계 서적을 구해다 읽었고, 그 애들의 건강을 위해 하이포넥슨가 하는 비료를 바다 건너가는 친지들에게 부탁하여 구해 오기도 했었다. 여름철이면 서늘한 그늘을 찾아 자리를 옮겨 주어야 했고, 겨울에는 필요 이상으로 실내 온도를 높이곤 했었다.</span> 이런 정성을 일찍이 부모에게 바쳤더라면 아마 효자 소리를 듣고도 남았을 것이다. 이렇듯 애지중지 가꾼 보람으로 이른 봄이면 <span class="mk-bg">은은한 향기</span>와 함께 <span class="mk-bg">연둣빛</span> 꽃을 피워 방 안을 채워 주었고, 잎은 늘 <span class="mk-bg">청청했었다</span>.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u3">
                  <div class="wing-box-title"><span>👁️ 시범 (I Do)</span><span class="role-chip">교사 사고구술</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>이 글의 '나'는 소설처럼 꾸며 낸 인물일까, 실제 글쓴이일까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>'3년 전 다래헌', '어떤 스님이 보내 준 난초 두 분'처럼 글쓴이(법정 스님)가 실제로 겪은 사실(🔵)을 고백하고 있어.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>수필의 '나'는 <strong>글쓴이 자신</strong>이며, 감각어(<span class="mk-bg">은은한 향기</span>, <span class="mk-bg">연둣빛</span>)로 난초를 생생히 묘사했구나!</span></div>
                </div>
                <div class="wing-box vocab">
                  <strong>📘 어휘 돋보기</strong><br>
                  • <strong>분(盆)</strong>: 화분을 세는 단위.<br>
                  • <strong>다래헌(茶來軒)</strong>: 법정 스님이 머물던 서울 봉은사의 작은 처소.<br>
                  • <strong>애지중지(愛之重之)</strong>: 매우 사랑하고 소중히 여김.
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➋</span> <span class="mk-line-blue">지난해 여름 장마가 갠 어느 날 봉선사로 운허 노사를 뵈러 간 일이 있었다.</span> 한낮이 되자 장마에 갇혔던 햇볕이 <span class="mk-bg">눈부시게</span> 쏟아져 내리고 <span class="mk-bg">앞개울물</span> 소리에 어울려 <span class="mk-bg">숲속</span>에서는 매미들이 있는 대로 목청을 돋우었다. 아차! 이때에야 문득 생각이 난 것이다. <span class="mk-line-blue">난초를 뜰에 내놓은 채 온 것이다.</span> 모처럼 보인 찬란한 햇볕이 돌연 원망스러워졌다. 뜨거운 햇볕에 늘어져 있을 난초 잎이 눈에 아른거려 더 지체할 수가 없었다. <span class="mk-line-blue">허둥지둥 그 길로 돌아왔다. 아니나 다를까, 잎은 축 늘어져 있었다. 안타까워하며 <span class="mk-bg">샘물</span>을 길어다 축여 주고 했더니 겨우 고개를 들었다.</span> 하지만 어딘지 생생한 기운이 빠져나간 것 같았다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 함께 (We Do)</span><span class="role-chip">짝과 확인</span></div>
                  <div><strong>Q1.</strong> ➋문단에서 글쓴이가 봉선사에 갔다가 허둥지둥 돌아온 까닭(겪은 일 🔵)은 무엇인가요?</div>
                  <div style="margin-top:2px;">➔ 난초를 <span class="blank-slot"><span class="t-ans">뜰에 내놓은 채</span></span> 외출했는데 한낮에 뜨거운 <span class="blank-slot"><span class="t-ans">햇볕</span></span>이 쏟아졌기 때문이다.</div>
                  <div style="margin-top:3px;"><strong>Q2.</strong> ➋문단의 복합어 <span class="mk-bg">앞개울물</span>과 <span class="mk-bg">샘물</span>은 어떤 어근들이 결합된 말일까요?</div>
                  <div>➔ 앞+개울+물 / <span class="blank-slot"><span class="t-ans">샘 + 물 (합성어)</span></span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➌</span> <span class="mk-line-red">나는 이때 <span class="mk-bg">온몸</span>으로 그리고 <span class="mk-bg">마음속</span>으로 절절히 느끼게 되었다. 집착이 괴로움인 것을. 그렇다, 나는 난초에게 너무 집념(執念)한 것이다. 이 하나의 집착에 조금도 여유가 없이 매달려 있었던 것이다. 더구나 출가한 몸으로 별것도 아닌 한두 분의 식물에 마음을 빼앗겨 허둥대다니, 스스로 생각해 보아도 부끄러운 노릇이었다.</span> <span class="mk-line-blue">며칠 후 난초를 나처럼 아끼는 친구가 놀러 왔기에 선뜻 그의 품에 안겨 주었다.</span> <span class="mk-line-red">비로소 나는 얽매임에서 벗어난 것이다. 날아갈 듯이 홀가분한 해방감을 맛보았다. 이후부터 나는 하루 한 가지씩 버려야겠다고 스스로 다짐을 했다.</span></p>
                <p><span class="p-num">➍</span> <span class="mk-line-red">우리의 일상생활에서 꼭 필요한 물건이 과연 얼마나 될까. 그러니까 무엇인가를 갖는다는 것은 다른 한편 무엇인가에 얽매이게 된다는 뜻이다. 필요에 따라 가졌던 것이 도리어 우리를 부자유하게 얽어맨다고 할 때 주객이 전도되어 우리는 가짐을 당하게 된다. 흔히들 무엇인가를 더 많이 가지려고 아등바등하지만, 가만히 돌이켜 보면 가진 것 때문에 마음이 상하고 무거운 짐을 지고 있는 경우가 얼마나 많은가. 크게 버리는 사람만이 크게 얻을 수 있다는 말이 있다. 물건으로 인해 마음을 상하고 있는 사람들에게는 한 번쯤 생각해 볼 말이다. 아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다는 것은 무소유(無所有)의 역리(逆理)이니까.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🚀 스스로 (You Do)</span><span class="role-chip">혼자 해보기</span></div>
                  <div><strong>Q3.</strong> ➌~➍문단에서 파란 밑줄(겪은 일)과 빨간 밑줄(깨달음)의 비중이 어떻게 달라졌나요?</div>
                  <div>➔ 난초를 친구에게 준 사실(🔵) 뒤로, <strong>집착과 소유에서 벗어나는 깨달음(🔴 <span class="blank-slot"><span class="t-ans">내면 성찰</span></span>)</strong>이 글의 중심을 이룬다.</div>
                </div>
                <div class="wing-box vocab">
                  <strong>📘 어휘 돋보기</strong><br>
                  • <strong>집착(執着)</strong>: 어떤 것에 마음이 쏠려 잊지 못하고 매달림.<br>
                  • <strong>주객전도(主客顚倒)</strong>: 주인과 손님의 위치가 뒤바뀜.<br>
                  • <strong>역리(逆理)</strong>: 언뜻 보면 이치에 어긋나는 것 같으나 실제로는 깊은 진리가 담긴 역설적 이치.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "수필의 갈래 특성과 본문 속 감각어·복합어 단서 찾기",
            "tag": "Step 1 단서 포착 (A1·A2 결합)",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:4px;">1. 2단원에서 배운 <strong>이야기(소설)</strong>와 이 글 <strong>〈무소유〉(수필)</strong>를 비교하고, 본문의 어휘 단서를 분석해 봅시다.</div>
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">비교·분석 항목</th>
                  <th style="width:38%;">이야기(소설) vs 수필 갈래 비교</th>
                  <th style="width:40%;">본문 속 감각어 및 복합어([6국04-02]) 분해</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th>글 속의 '나'와 내용</th>
                  <td>
                    • 소설: 작가가 꾸며 낸 <strong>허구적 대리인(서술자)</strong><br>
                    • 수필: <span class="blank-slot"><span class="t-ans">글쓴이 자신(법정 스님)</span></span>이 직접 겪은 <span class="blank-slot"><span class="t-ans">실제 체험 사실</span></span>
                  </td>
                  <td>
                    • <strong>감각적 묘사어</strong>: 후각(<span class="blank-slot"><span class="t-ans">은은한 향기</span></span>), 시각(<span class="blank-slot"><span class="t-ans">연둣빛, 눈부시게, 축 늘어져</span></span>), 청각(<span class="blank-slot"><span class="t-ans">앞개울물 소리</span></span>)
                  </td>
                </tr>
                <tr>
                  <th>복합어 형태소 분석<br>(어근·접사 결합)</th>
                  <td colspan="2">
                    • <strong>합성어(어근+어근)</strong>: <code>연둣빛</code>(연두+ㅅ+빛), <code>앞개울물</code>(<span class="blank-slot"><span class="t-ans">앞 + 개울 + 물</span></span>), <code>숲속</code>(<span class="blank-slot"><span class="t-ans">숲 + 속</span></span>), <code>샘물</code>(<span class="blank-slot"><span class="t-ans">샘 + 물</span></span>), <code>온몸</code>(<span class="blank-slot"><span class="t-ans">온 + 몸</span></span>), <code>마음속</code>(<span class="blank-slot"><span class="t-ans">마음 + 속</span></span>), <code>눈부시게</code>(<span class="blank-slot"><span class="t-ans">눈 + 부시다</span></span>)<br>
                    • <strong>파생어(어근+접사)</strong>: <code>정성스레</code>(어근 '정성' + 접미사 <span class="blank-slot"><span class="t-ans">'-스레'</span></span>), <code>맨손</code>(접두사 '맨-' + 어근 '손')
                  </td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 확인한 실제 체험 단서와 어휘를 바탕으로 문단별 [경험 사실 ↔ 내면 성찰] 짝짓기",
        "activity_2": {
            "title": "문단별 [겪은 일·관찰 사실(🔵) ↔ 마음속 생각·성찰(🔴)] 2원 분석표 완성하기",
            "tag": "Step 2 층위 분리·연결",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:12%;">문단</th>
                  <th style="width:44%;">🔵 글쓴이가 직접 겪은 일과 관찰 묘사 (외적 사실)</th>
                  <th style="width:44%;">🔴 그때의 마음과 삶에 대한 깨달음 (내면 성찰)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="text-align:center; font-weight:800;">➊문단</td>
                  <td>3년 전 다래헌으로 거처를 옮겼을 때 스님에게 받은 <strong>난초 두 분</strong>을 서늘한 그늘과 비료를 챙기며 애지중지 길러 연둣빛 꽃을 피움.</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">이런 정성을 부모님께 바쳤다면 효자 소리를 들었을 것이라 생각하며 난초 가꾸는 보람을 느낌.</span></span></td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:800;">➋문단</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">장마가 갠 여름날 봉선사에 갔다가 뜰에 내놓은 난초가 생각나 허둥지둥 돌아와 축 늘어진 난초에 샘물을 축여 줌.</span></span></td>
                  <td>모처럼 내리쬔 찬란한 햇볕이 돌연 원망스러워지고, 시든 난초가 눈에 아른거려 무척 안타까워함.</td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:800;">➌문단</td>
                  <td>며칠 후 난초를 나처럼 아끼는 친구가 놀러 왔을 때 <strong>선뜻 그의 품에 난초를 안겨 줌.</strong></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">집착이 곧 괴로움임을 절절히 깨닫고, 난초를 준 뒤 날아갈 듯이 홀가분한 해방감을 맛보며 하루 한 가지씩 버리기로 다짐함.</span></span></td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:800;">➍문단</td>
                  <td>사람들이 일상생활에서 무엇인가를 더 많이 가지려고 아등바등하며 살아가는 모습을 돌아봄.</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">무엇인가를 갖는 것은 도리어 그것에 얽매이는 것임을 깨닫고, 아무것도 갖지 않을 때 온 세상을 얻는다는 '무소유'의 이치를 성찰함.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 2원 분석표를 종합하여 수필이 단순한 일기나 소설과 다른 점 정리하기",
        "activity_3": {
            "title": "체험에서 성찰로 나아가는 수필의 매력 정리하기",
            "tag": "Step 3 개념 구조화·산출",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:3px;">• 만약 〈무소유〉에 🔵<strong>겪은 일(난초를 기르고 물을 준 사실)</strong>만 적혀 있고 🔴<strong>마음속 성찰(3~4문단의 깨달음)</strong>이 빠졌다면 어떤 글이 되었을지 비교하며 수필의 특성을 한 문장으로 정리해 보세요.</div>
            <span class="pencil-line">✏️ 수필이란: <span class="t-ans">글쓴이가 일상에서 직접 겪은 실제 경험(사실)을 생생하게 그린 뒤, 그 속에서 얻은 깊은 삶의 깨달음(성찰)을 솔직하게 표현하는 글이다.</span></span>
            """,
        },
        "writing_seed": {
            "transfer_tag": "➔ 12~13차시(W1·W2) 글감·감각어 생성으로 전이",
            "prompt": "내가 아끼던 물건이나 동식물 때문에 마음이 조마조마했거나, 반대로 무언가를 양보하고 마음이 홀가분했던 실제 경험을 한 줄로 메모해 두세요.",
            "placeholder": "(내가 아꼈던 대상과 그때 겪은 일)",
            "example_answer": "한정판 축구화에 흙이 묻을까 봐 운동장에서 제대로 뛰지도 못하고 전전긍긍하다가, 동생에게 물려주고 나서야 마음껏 축구를 즐기게 된 경험",
        },
        "self_check": [
            "수필 속 '나'가 실제 글쓴이임을 알고 겪은 일(🔵)과 깨달음(🔴)을 구분했나요?",
            "본문 속 감각어와 합성어·파생어의 짜임을 정확히 분석했나요?",
            "문단별 2원 분석표를 빈칸 없이 완성했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측] 소설(허구 대리인·사건 중심) vs 수필(실제 글쓴이 '법정'·체험+성찰 중심) 대비 ➔ [중앙] 〈무소유〉 1~4문단 🔵외적 체험(난초 선물➔봉선사 소낙비 후 햇볕➔친구에게 줌) ↔ 🔴내면 성찰(집착은 괴로움➔해방감➔무소유의 역리) 2단 층위도 ➔ [우측] 복합어 분해(앞+개울+물, 숲+속, 정성+-스레).",
            "intro_5min": "단원 핵심 질문('작은 경험이나 사물 하나가 어떻게 우리의 삶을 바꾸는 깊은 깨달음이 될 수 있을까요?')을 함께 읽습니다. 2단원 이야기(소설)의 '나'가 작가가 만든 가상의 인물이었다면, 오늘부터 읽을 수필의 '나'는 누구인지 칠판에 '법정 스님과 난초 두 화분' 일러스트 카드를 붙이며 호기심을 유발합니다.",
            "ido_think_aloud_script": "“선생님이 ➊문단을 읽으며 머릿속 생각을 소리 내어 볼게요. '나는 지난해 여름까지 난초 두 분을 정성스레 길렀었다. 3년 전 거처를 다래헌으로 옮겨 왔을 때 어떤 스님이 보내 준 것이다.' 어? 여기 나오는 '다래헌'은 실제 법정 스님이 머물던 방 이름이에요. 그러니까 수필에서 '나'는 소설처럼 꾸며 낸 인물이 아니라 글쓴이 자신이네요! 스님이 직접 겪은 사실인 '3년 전 난초를 선물 받아 그늘을 옮겨 주고 비료를 구해 온 일'에는 파란 밑줄(🔵)을 긋겠습니다. 그리고 난초를 묘사한 '은은한 향기', '연둣빛' 같은 감각어와 '정성+-스레(파생어)'에는 초록 네모(□)를 칠게요. 이제 여러분이 ➋~➍문단에서 겪은 일(🔵)과 깨달음(🔴)을 구분해 볼까요?”",
            "wedo_qa_list": [
                {
                    "qar_type": "해독·어휘(A1)",
                    "question": "➋문단과 ➌문단에 나오는 '앞개울물', '숲속', '샘물', '온몸', '마음속'은 낱말이 어떻게 만들어진 복합어인가요?",
                    "expected_ans": "모두 실질적인 뜻을 가진 어근과 어근이 합쳐진 합성어입니다. 예를 들어 '앞개울물'은 '앞+개울+물', '마음속'은 '마음+속'으로 나뉩니다.",
                    "reprompt": "혼자서도 뜻을 가지는 말(어근)끼리 만났는지, 아니면 '정성스레(-스레)'처럼 뜻을 더하는 꼬리(접사)가 붙었는지 쪼개 볼까요?",
                },
                {
                    "qar_type": "텍스트 내(Right There)",
                    "question": "➋문단에서 글쓴이가 봉선사로 운허 노사를 뵈러 갔다가 허둥지둥 돌아온 까닭은 무엇인가요?",
                    "expected_ans": "장마가 개고 한낮에 뜨거운 햇볕이 눈부시게 쏟아지자, 아침에 난초 화분을 마당(뜰)에 내놓은 채 나온 것이 문득 생각났기 때문입니다.",
                    "reprompt": "한낮에 날씨가 어떻게 변했는지, 그리고 글쓴이가 '아차!' 하며 떠올린 장면이 무엇인지 ➋문단에서 찾아보세요.",
                },
                {
                    "qar_type": "검색·통합(Think & Search)",
                    "question": "➊~➋문단과 비교할 때 ➌~➍문단에서는 파란 밑줄(겪은 일)과 빨간 밑줄(성찰)의 비중이 어떻게 달라지나요?",
                    "expected_ans": "➊~➋문단은 난초를 기르고 햇볕에 시든 난초를 살려 낸 '겪은 일(파란 밑줄)'이 중심이지만, ➌~➍문단은 난초를 친구에게 준 뒤 깨달은 '집착의 괴로움과 무소유의 철학(빨간 밑줄)'이 중심을 이룹니다.",
                    "reprompt": "만약 1~2문단만 있고 3~4문단이 없다면 이 글은 단순한 '식물 기르기 일기'와 무엇이 다를지 생각해 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 스스로 ➌~➍문단에 빨간 밑줄을 긋고 우측 페이지 [활동 2]의 2원 분석표를 완성하도록 순회 지도합니다. 정리 단계에서는 '체험(사실) + 성찰(깨달음) = 수필' 공식을 합창하고, 내 삶에서 물건에 집착했던 경험을 씨앗 보관함에 한 줄로 적게 합니다.",
            "answer_key_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <strong>1. 본문 날개 문항 정답:</strong> Q1. 뜰에 내놓은 채 / 햇볕 | Q2. 샘 + 물 (합성어) | Q3. 내면 성찰<br>
              <strong>2. [활동 1] 정답:</strong> • 수필의 '나': 글쓴이 자신(법정 스님), 실제 체험 사실 • 감각어: 후각(은은한 향기), 시각(연둣빛, 눈부시게, 축 늘어져), 청각(앞개울물 소리) • 합성어: 앞+개울+물, 숲+속, 샘+물, 온+몸, 마음+속, 눈+부시다 / 파생어: '-스레'<br>
              <strong>3. [활동 2] 2원 분석표 모범 답안:</strong><br>
              • <strong>➊문단(성찰)</strong>: 이런 정성을 부모님께 바쳤다면 효자 소리를 들었을 것이라 생각하며 애지중지 가꾼 보람을 느낌.<br>
              • <strong>➋문단(체험)</strong>: 장마가 갠 여름날 봉선사에 갔다가 뜰에 내놓은 난초가 생각나 허둥지둥 돌아와 축 늘어진 난초에 샘물을 길어다 축여 줌.<br>
              • <strong>➌문단(성찰)</strong>: 집착이 곧 괴로움임을 절절히 깨닫고 출가한 몸으로 식물에 마음 빼앗긴 것을 부끄러워함. 난초를 준 뒤 날아갈 듯한 해방감을 맛보며 하루 한 가지씩 버리기로 다짐함.<br>
              • <strong>➍문단(성찰)</strong>: 무엇인가를 갖는 것은 도리어 그것에 얽매여 가짐을 당하는 것임을 깨닫고, 아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다는 무소유의 이치를 성찰함.<br>
              <strong>4. [활동 3] 모범 답안:</strong> 수필은 글쓴이가 일상에서 직접 겪은 실제 경험(사실)을 바탕으로 그 속에서 얻은 삶의 깨달음(내면 성찰)을 솔직하게 표현하는 비허구 문학 갈래이다.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "➋문단의 '찬란한 햇볕이 돌연 원망스러워졌다'를 외적 사실(🔵)로 분류함",
                    "diagnosis": "'햇볕이 쏟아졌다'는 외적 날씨 사실과 '원망스러워졌다'는 주관적 감정을 한 문장 안에서 분리하지 못함",
                    "prescription": "'햇볕이 쏟아진 것'은 누구나 볼 수 있는 사실(🔵)이지만, 그 햇볕을 보고 '원망스럽다'고 느낀 것은 글쓴이 마음속 감정(🔴)임을 구분해 주세요.",
                },
                {
                    "error_case": "'정성스레'를 합성어로, '마음속'을 파생어로 혼동함",
                    "diagnosis": "홀로 쓰일 수 있는 실질 형태소(어근: '속')와 홀로 쓰이지 못하는 형식 형태소(접사: '-스레')의 차이를 헷갈림",
                    "prescription": "'속'은 '속이 깊다'처럼 혼자 단어로 쓰이므로 어근(마음+속=합성어)이고, '-스레'는 혼자 쓰이지 못하고 어근 뒤에 붙어 부사를 만드는 접미사(파생어)임을 예시로 확인시킵니다.",
                },
            ],
            "scaffolding_down": "외적 사실(🔵)과 내면 성찰(🔴) 구분이 어려운 학생에게는 '카메라로 찍을 수 있는 행동·장면인가요(🔵), 아니면 머리와 가슴속에서 일어난 생각인가요(🔴)?'라는 판별 질문 카드를 제공합니다.",
            "scaffolding_up": "➍문단에서 '우리가 물건을 가지는 것(소유)'과 '물건에 우리가 가짐을 당하는 것(주객전도)'의 차이를 자신의 일상 속 스마트폰·게임기 사용 경험에 비추어 2문장으로 설명해 보게 합니다.",
            "rubric": {
                "high": "본문에서 외적 체험 사실(🔵), 감각어·복합어(□), 내면 성찰(🔴)을 정확히 구분하고, 문단별 2원 분석표와 수필의 갈래 특성을 근거 있게 서술한다.",
                "mid": "체험 사실과 내면 성찰의 큰 흐름은 구분하나, 일부 복합어 형태소 분해나 4문단의 보편적 성찰 정리가 다소 소략하다.",
                "low": "외적 사건과 내면의 생각·성찰을 구분하지 못하고 본문 문장을 그대로 옮겨 적는 데 그친다.",
            },
        },
    },

    # =========================================================================
    # 2차시: G6-ESS-V1-2 (관계 확인)
    # 담화 지시어 역추적 및 '과거 경험 ➔ 그때의 감정 ➔ 지금의 성찰' 이중 인과 확인
    # =========================================================================
    {
        "lesson_no": 2,
        "code": "G6-ESS-V1-2",
        "lesson_title": "지시어를 추적하고 '경험 ➔ 감정 ➔ 성찰'의 인과 관계 파악하기",
        "std_badge": "[6국02-02] [6국04-05] 지시어·시제·이중인과·문장골격",
        "student_goal": "문단과 일화를 이어 주는 지시어의 대상을 찾고, '과거의 경험 ➔ 그때의 감정 ➔ 지금의 성찰'로 이어지는 이중 인과 관계를 주·목·서 골격으로 정리할 수 있다.",
        "marking_items": [
            ("mk-person", "파란 ○", "앞 문장·일화를 가리키는 지시어"),
            ("mk-line-blue", "파란 밑줄", "과거의 경험·그때의 감정(과거 시제 -았/었-)"),
            ("mk-line-red", "빨간 밑줄", "지금의 성찰·깨달음(현재 시제 -ㄴ다/는다)"),
        ],
        "left_page_body_html": """
        <div style="font-size:7.4pt; color:#1E8449; font-weight:700; margin-bottom:4px;">🔍 〈무소유〉 원문에서 문단을 이어 주는 <strong>지시어(파란 ○)</strong>와 <strong>시간 표현(과거 -았/었- ↔ 현재 -ㄴ다)</strong>의 변화에 주목하며 인과 사슬을 따라가 봅시다.</div>

        <!-- 구간 1 -->
        <div class="inline-segment-box">
          <p><span class="p-num">➊</span> 나는 지난해 여름까지 난초 두 분(盆)을 정성스레, 정말 정성을 다해 <span class="mk-line-blue">길렀었다</span>. 3년 전 거처를 지금의 다래헌(茶來軒)으로 옮겨 왔을 때 어떤 스님이 우리 방으로 보내 준 것이다. 혼자 사는 거처라 살아 있는 생물이라고는 나하고 <span class="mk-person">㉠ 그 애들</span>뿐이었다. <span class="mk-person">그 애들</span>을 위해 관계 서적을 구해다 읽었고, <span class="mk-person">그 애들</span>의 건강을 위해 하이포넥슨가 하는 비료를 바다 건너가는 친지들에게 부탁하여 구해 오기도 <span class="mk-line-blue">했었다</span>. 여름철이면 서늘한 그늘을 찾아 자리를 옮겨 주어야 했고, 겨울에는 필요 이상으로 실내 온도를 높이곤 <span class="mk-line-blue">했었다</span>. <span class="mk-person">㉡ 이런 정성</span>을 일찍이 부모에게 바쳤더라면 아마 효자 소리를 듣고도 남았을 것이다. 이렇듯 애지중지 가꾼 보람으로 이른 봄이면 은은한 향기와 함께 연둣빛 꽃을 피워 방 안을 채워 주었고, 잎은 늘 청청했었다.</p>
        </div>
        <div class="inline-bridge-box model">
          <div style="font-weight:800; color:#1E8449;">👁️ 시범 (I Do)<br><span style="font-size:6.6pt; font-weight:600; color:#566573;">지시어 역추적</span></div>
          <div>
            • <strong>[단서 포착]</strong> <span class="mk-person">㉠ 그 애들</span>은 앞 문장의 <strong>'난초 두 분(화분)'</strong>을 의인화하여 가리키고, <span class="mk-person">㉡ 이런 정성</span>은 앞서 말한 <strong>'책을 구해 읽고, 외국 비료를 구해 오고, 여름·겨울마다 자리와 온도를 맞춰 준 행동 전체'</strong>를 묶어 가리키는구나!
          </div>
        </div>

        <!-- 구간 2 -->
        <div class="inline-segment-box">
          <p><span class="p-num">➋</span> 지난해 여름 장마가 갠 어느 날 봉선사로 운허 노사를 뵈러 간 일이 <span class="mk-line-blue">있었다</span>. 한낮이 되자 장마에 갇혔던 햇볕이 눈부시게 쏟아져 내리고 앞개울물 소리에 어울려 숲속에서는 매미들이 있는 대로 목청을 돋우었다. 아차! <span class="mk-person">㉢ 이때</span>에야 문득 생각이 난 것이다. 난초를 뜰에 내놓은 채 온 것이다. <span class="mk-line-blue">모처럼 보인 찬란한 햇볕이 돌연 원망스러워졌다.</span> 뜨거운 햇볕에 늘어져 있을 난초 잎이 눈에 아른거려 더 지체할 수가 없었다. 허둥지둥 <span class="mk-person">㉣ 그 길로</span> 돌아왔다. 아니나 다를까, 잎은 축 늘어져 있었다. 안타까워하며 샘물을 길어다 축여 주고 했더니 겨우 고개를 들었다. 하지만 어딘지 생생한 기운이 빠져나간 것 같았다.</p>
          <p><span class="p-num">➌</span> 나는 <span class="mk-person">㉤ 이때</span> 온몸으로 그리고 마음속으로 절절히 느끼게 되었다. 집착이 괴로움인 것을. 그렇다, 나는 난초에게 너무 집념(執念)한 것이다. <span class="mk-person">㉥ 이 하나의 집착</span>에 조금도 여유가 없이 매달려 있었던 것이다. 더구나 출가한 몸으로 별것도 아닌 한두 분의 식물에 마음을 빼앗겨 허둥대다니, 스스로 생각해 보아도 <span class="mk-line-blue">부끄러운 노릇이었다</span>. 며칠 후 난초를 나처럼 아끼는 친구가 놀러 왔기에 선뜻 <span class="mk-person">㉦ 그의 품</span>에 안겨 주었다. 비로소 나는 얽매임에서 벗어난 것이다. <span class="mk-line-blue">날아갈 듯이 홀가분한 해방감을 맛보았다.</span> 이후부터 나는 하루 한 가지씩 버려야겠다고 스스로 다짐을 했다.</p>
        </div>
        <div class="inline-bridge-box practice">
          <div style="font-weight:800; color:#2874A6;">🤝 함께 (We Do)<br><span style="font-size:6.6pt; font-weight:600; color:#566573;">지시어 &amp; 감정 전환</span></div>
          <div>
            • <span class="mk-person">㉢ 이때</span>는 <strong>'봉선사에서 한낮의 눈부신 햇볕과 매미 소리를 들은 때'</strong>이고, <span class="mk-person">㉤ 이때</span>는 <span class="blank-slot"><span class="t-ans">집으로 돌아와 축 늘어진 난초를 살려 낸 직후</span></span>를 가리킵니다.<br>
            • <span class="mk-person">㉥ 이 하나의 집착</span>은 <span class="blank-slot"><span class="t-ans">난초 두 분을 지나치게 아끼며 마음을 빼앗긴 것</span></span>을 가리킵니다.
          </div>
        </div>

        <!-- 구간 3 -->
        <div class="inline-segment-box" style="margin-bottom:0;">
          <p><span class="p-num">➍</span> 우리의 일상생활에서 꼭 필요한 물건이 과연 얼마나 될까. 그러니까 <span class="mk-line-red">무엇인가를 갖는다는 것은 다른 한편 무엇인가에 얽매이게 된다는 뜻이다.</span> 필요에 따라 가졌던 것이 도리어 우리를 부자유하게 얽어맨다고 할 때 주객이 전도되어 <span class="mk-line-red">우리는 가짐을 당하게 된다.</span> 흔히들 무엇인가를 더 많이 가지려고 아등바등하지만, 가만히 돌이켜 보면 가진 것 때문에 마음이 상하고 무거운 짐을 지고 있는 경우가 얼마나 많은가. 크게 버리는 사람만이 크게 얻을 수 있다는 말이 <span class="mk-line-red">있다.</span> 물건으로 인해 마음을 상하고 있는 사람들에게는 한 번쯤 생각해 볼 말이다. <span class="mk-line-red">아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다는 것은 무소유(無所有)의 역리(逆理)이니까.</span></p>
        </div>
        """,
        "activity_1": {
            "title": "문단 간 지시어 역추적 및 시제(과거 경험 ↔ 현재 성찰) 표지 확인하기",
            "tag": "Step 1 지시·시제 단서 (A4·A3 결합)",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">지시어·시제 표지</th>
                  <th style="width:42%;">가리키는 대상 (앞 문장·일화 역추적)</th>
                  <th style="width:40%;">시제 변화와 담화 기능 ([6국04-05])</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700;">㉡ 이런 정성 (➊)</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">난초 재배 서적을 읽고, 외국 비료를 구해 오며, 여름·겨울마다 그늘과 실내 온도를 맞춰 준 일</span></span></td>
                  <td rowspan="2" style="vertical-align:middle;">
                    • <strong>➊~➌문단 시제</strong>: <code>-았/었-</code>, <code>-더-</code> (<span class="blank-slot"><span class="t-ans">과거 시제</span></span>)<br>
                    ➔ 이미 겪은 구체적 일화와 그때의 감정을 생생히 회상함.
                  </td>
                </tr>
                <tr>
                  <td style="font-weight:700;">㉣ 그 길로 (➋)<br>㉦ 그의 품 (➌)</td>
                  <td>
                    • ㉣ 그 길로: <span class="blank-slot"><span class="t-ans">봉선사에서 지체하지 않고 곧바로 돌아온 길</span></span><br>
                    • ㉦ 그의 품: <span class="blank-slot"><span class="t-ans">난초를 나처럼 아끼는 친구의 품</span></span>
                  </td>
                </tr>
                <tr>
                  <td style="font-weight:700;">➍문단 서술어<br>(~뜻이다, ~된다)</td>
                  <td>개인의 난초 일화를 넘어 <strong>'우리 모두의 일상생활 속 소유와 집착'</strong>으로 화제를 일반화함.</td>
                  <td>
                    • <strong>➍문단 시제</strong>: <code>-ㄴ다/는다</code>, <code>~이다</code> (<span class="blank-slot"><span class="t-ans">현재 시제</span></span>)<br>
                    ➔ 시대를 초월한 보편적 삶의 진리·성찰을 전달함.
                  </td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 지시어와 시간 흐름을 따라 [과거의 경험 ➔ 그때의 감정 ➔ 지금의 성찰] 이중 인과 사슬 연결하기",
        "activity_2": {
            "title": "'과거의 경험 ➔ 그때의 감정 ➔ 지금의 성찰' 이중 인과 도해 완성하기",
            "tag": "Step 2 이중 인과 연결 (A5 결합)",
            "body_html": """
            <div class="inference-row">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">① 과거의 경험 사건 (원인 1)</strong>
                <div style="margin-top:3px;">
                  • <strong>사건 A</strong>: 난초를 뜰에 내놓은 채 봉선사에 갔는데 한낮에 뜨거운 햇볕이 쏟아져 난초가 축 늘어짐.<br>
                  • <strong>사건 B</strong>: <span class="blank-slot"><span class="t-ans">난초를 아끼는 친구에게 선뜻 난초를 줌.</span></span>
                </div>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:var(--mark-green);">② 그때의 일차적 감정 (매개 원인 2)</strong>
                <div style="margin-top:3px;">
                  • <strong>감정 A</strong>: 찬란한 햇볕이 <span class="blank-slot"><span class="t-ans">원망스럽고</span></span>, 식물에 마음을 빼앗겨 허둥댄 자신이 <span class="blank-slot"><span class="t-ans">부끄러움</span></span>.<br>
                  • <strong>감정 B</strong>: 얽매임에서 벗어나 날아갈 듯이 홀가분한 <span class="blank-slot"><span class="t-ans">해방감</span></span>을 맛봄.
                </div>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#1E8449;">③ 지금의 철학적 성찰 (최종 결과)</strong>
                <div style="margin-top:3px;">
                  • <strong>깨달음 1</strong>: 무엇을 갖는다는 것은 도리어 그것에 <span class="blank-slot"><span class="t-ans">얽매이게 된다</span></span>는 뜻이다.<br>
                  • <strong>깨달음 2</strong>: 크게 버리는 사람만이 크게 얻을 수 있으며, 아무것도 갖지 않을 때 <span class="blank-slot"><span class="t-ans">온 세상을 갖게 된다(무소유)</span></span>.
                </div>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 인과 사슬에서 꾸미는 말을 덜어내고 [주어 + 목적어/부사어 + 서술어] 핵심 골격 문장으로 압축하기",
        "activity_3": {
            "title": "주·목·서 문장 골격으로 3단 인과 브릿지 완성하기",
            "tag": "Step 3 문장 골격 산출 (A3 결합)",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">인과 단계</th>
                  <th style="width:22%;">주어 (누가/무엇은)</th>
                  <th style="width:35%;">목적어·부사어 (무엇을 / 어떻게)</th>
                  <th style="width:25%;">서술어 (어찌했다/어떠하다)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700; color:var(--mark-blue);">1. 과거 경험</td>
                  <td>나는 (글쓴이는)</td>
                  <td>정성껏 기르던 <span class="blank-slot"><span class="t-ans">난초 두 분을</span></span> 친구에게</td>
                  <td><span class="blank-slot"><span class="t-ans">안겨 주었다(선물했다).</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; color:var(--mark-green);">2. 그때의 감정</td>
                  <td>나는 (글쓴이는)</td>
                  <td>집착의 괴로움과 얽매임에서 벗어나 <span class="blank-slot"><span class="t-ans">홀가분한 해방감을</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">맛보았다(느꼈다).</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; color:#1E8449;">3. 지금의 성찰</td>
                  <td>우리는 (사람들은)</td>
                  <td>아무것도 갖지 않을 때 비로소 <span class="blank-slot"><span class="t-ans">참된 자유(온 세상)를</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">얻게 된다(갖게 된다).</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "➔ 13~14차시(W2·W3) 과거 감정 ↔ 현재 성찰 연결로 전이",
            "prompt": "1차시 씨앗 경험에서 '그때 느꼈던 솔직한 감정(과거)'과 시간이 흐른 '지금 돌아보며 깨달은 점(현재)'을 화살표(➔)로 이어 적어 보세요.",
            "placeholder": "(그때의 감정 ➔ 지금의 깨달음)",
            "example_answer": "[그때의 감정] 새 축구화가 더러워질까 봐 조마조마하고 친구가 원망스러웠다 ➔ [지금의 성찰] 물건을 아끼느라 친구와 뛰노는 즐거움을 놓치는 것은 주객이 뒤바뀐 일임을 깨닫는다.",
        },
        "self_check": [
            "지시어('그 애들', '이런 정성', '이때')가 가리키는 앞 내용을 정확히 찾았나요?",
            "과거 경험(-았/었-)과 현재 성찰(-ㄴ다)의 시제 차이를 이해했나요?",
            "'경험 ➔ 감정 ➔ 성찰'을 주·목·서 문장 골격에 맞게 정리했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측] 지시어 역추적 화살표(그 애들=난초 두 분, 이런 정성=비료·그늘·온도 조절, 이때=봉선사 한낮 / 난초 살려낸 직후) ➔ [중앙] 이중 인과 도미노: [햇볕에 시든 난초 사건(원인1) ➔ 원망·부끄러움·해방감(매개 감정) ➔ 무소유의 성찰(결과)] ➔ [우측] 시제 전환 공식: 과거 경험(-았/었-) ↔ 현재 성찰(-ㄴ다/는다).",
            "intro_5min": "지난 시간에 나눈 '겪은 일(🔵)'과 '깨달음(🔴)'이 서로 따로 놀지 않고 하나의 끈으로 촘촘히 묶여 있는 비결이 무엇인지 질문합니다. 문단과 문단을 이어 주는 '지시어 접착제'와 '경험➔감정➔성찰 도미노'를 찾아보자고 안내합니다.",
            "ido_think_aloud_script": "“➊문단에서 '나하고 그 애들뿐이었다'를 볼까요? 스님이 혼자 사신다는데 갑자기 웬 '그 애들'일까요? 앞 문장으로 거슬러 올라가 보니 '난초 두 분'이 있네요! 난초를 사람처럼 아껴서 '그 애들'이라는 지시어로 받은 거예요. 또 '이런 정성'은 바로 앞 문장의 '책을 읽고, 비료를 구해 오고, 여름·겨울마다 자리와 온도를 맞춰 준 일 전체'를 하나로 묶어 가리킵니다. 이렇게 지시어는 앞 문장의 긴 일화를 압축해 뒤 문장의 감정·생각과 이어 주는 다리 역할을 한답니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "담화 응집성(A4)",
                    "question": "➋문단의 '㉢ 이때'와 ➌문단의 '㉤ 이때'는 글자 모양은 똑같지만 가리키는 시점이 다릅니다. 각각 언제인가요?",
                    "expected_ans": "➋문단의 '이때'는 봉선사에서 눈부신 햇볕과 매미 소리를 들으며 마당에 내놓은 난초가 떠오른 순간이고, ➌문단의 '이때'는 집으로 달려와 시든 난초에 샘물을 주어 겨우 살려 낸 직후의 순간입니다.",
                    "reprompt": "각각의 '이때' 바로 앞 문장에서 글쓴이가 어디에 있었고 무슨 행동을 했는지 확인해 볼까요?",
                },
                {
                    "qar_type": "인과·논리(A5)",
                    "question": "평소 같으면 장마가 개고 비친 '찬란한 햇볕'이 반가웠을 텐데, 왜 글쓴이에게는 돌연 '원망스러워졌을까요'?",
                    "expected_ans": "난초를 뜰에 내놓고 왔기 때문에, 그 찬란한 햇볕이 난초 잎을 타들어 가게 만들 것이라 걱정되었기 때문입니다. 즉 난초에 대한 집착이 자연의 햇볕마저 원망하게 만든 것입니다.",
                    "reprompt": "글쓴이가 마당에 두고 온 것이 무엇인지, 햇볕이 난초에게 어떤 영향을 줄지 연결해 보세요.",
                },
                {
                    "qar_type": "문법·시제(A3)",
                    "question": "➊~➌문단 끝의 서술어('길렀었다', '있었다', '맛보았다')와 ➍문단 끝의 서술어('된다는 뜻이다', '당하게 된다')는 시제가 어떻게 다르며 왜 바뀌었을까요?",
                    "expected_ans": "➊~➌문단은 과거 시제(-았/었-)를 써서 이미 겪은 일화를 이야기하고, ➍문단은 현재 시제(-ㄴ다)를 써서 지금도 변함없는 삶의 보편적 진리(무소유)를 전달하기 위해서입니다.",
                    "reprompt": "옛날 일기처럼 그때만 그랬던 일인지, 아니면 지금 우리 모두에게도 해당되는 삶의 이치인지 비교해 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 2]의 이중 인과 카드를 채운 뒤, [활동 3]에서 수식어를 걷어내고 '주어-목적어-서술어' 골격 문장으로 압축하도록 지도합니다. 이 시제 전환(`과거 경험 -았/었-` ↔ `현재 성찰 -ㄴ다`)이 15차시(W4) 수필 초고 쓰기의 핵심 규칙임을 강조하며 마무리합니다.",
            "answer_key_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <strong>1. 본문 브릿지 정답:</strong> • ㉤ 이때: 집으로 돌아와 축 늘어진 난초를 살려 낸 직후 • ㉥ 이 하나의 집착: 난초 두 분을 지나치게 아끼며 마음을 빼앗긴 것<br>
              <strong>2. [활동 1] 정답:</strong> • ㉡ 이런 정성: 난초 서적을 읽고 외국 비료를 구해 오며 여름·겨울마다 자리와 실내 온도를 맞춰 준 일 • ㉣ 그 길로: 봉선사에서 지체하지 않고 곧장 집으로 돌아온 길 • ㉦ 그의 품: 난초를 아끼는 친구의 품 • 시제: 과거 시제 / 현재 시제<br>
              <strong>3. [활동 2] 이중 인과 도해 정답:</strong> ① 사건 B: 난초를 아끼는 친구에게 선뜻 난초를 줌 ② 감정 A: 원망스럽고 / 부끄러움, 감정 B: 해방감 ③ 깨달음 1: 얽매이게 된다, 깨달음 2: 온 세상을 갖게 된다(무소유)<br>
              <strong>4. [활동 3] 주·목·서 골격 정답:</strong><br>
              • 1. 과거 경험: 나는 / 정성껏 기르던 <strong>난초 두 분을</strong> 친구에게 / <strong>안겨 주었다.</strong><br>
              • 2. 그때의 감정: 나는 / 집착에서 벗어나 <strong>홀가분한 해방감을</strong> / <strong>맛보았다.</strong><br>
              • 3. 지금의 성찰: 우리는 / 아무것도 갖지 않을 때 비로소 <strong>참된 자유(온 세상)를</strong> / <strong>얻게 된다.</strong>
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "'그 애들'을 실제 어린아이들이나 제자 스님으로 오해함",
                    "diagnosis": "사물(식물)을 인격화하여 대명사로 지칭하는 수필의 의인화·대용 표현에 익숙하지 않음",
                    "prescription": "바로 앞 문장의 '살아 있는 생물이라고는 나하고 그 애들뿐'과 1문단 첫 줄의 '난초 두 분'을 연결하여 난초를 사랑스럽게 부른 표현임을 확인시킵니다.",
                },
                {
                    "error_case": "[활동 3] 문장 골격 요약에서 주어('나는')와 서술어('해방감이었다')의 호응을 어색하게 작성함",
                    "diagnosis": "주어 '나는'에 호응하는 동작·상태 동사('맛보았다/느꼈다') 대신 명사구 서술어를 연결하는 주술 호응 오류([6국04-05])",
                    "prescription": "'내가 해방감이다'는 어색하므로, '나는(주어) + 해방감을(목적어) + 맛보았다/느꼈다(서술어)'로 주술·목서 호응을 맞추도록 교정합니다.",
                },
            ],
            "scaffolding_down": "지시어 찾기가 막히는 학생에게는 지시어 바로 앞 1~2문장에 형광펜으로 후보 명사구 2개를 칠해 주고 알맞은 것을 고르게 합니다.",
            "scaffolding_up": "본문 4문단에서 '주어(내가) + 목적어(난초를) + 능동 서술어(가졌다)'가 어떻게 '주어(우리는) + 피동 표현(가짐을 당하게 된다)'으로 뒤집히는지 문장 성분의 자리바꿈(주객전도) 원리를 설명해 보게 합니다.",
            "rubric": {
                "high": "문단 간 지시어의 선행 일화를 100% 정확히 찾고, '과거 경험 ➔ 그때의 감정 ➔ 지금의 성찰'의 이중 인과를 주·목·서 호응에 맞는 문장 골격으로 완성한다.",
                "mid": "지시어의 대상과 인과 흐름은 파악했으나, 주·목·서 문장 골격 요약에서 수식어가 과다하거나 호응이 다소 어색하다.",
                "low": "지시어가 가리키는 범위를 찾지 못하거나 경험과 성찰의 인과 순서를 혼동한다.",
            },
        },
    },

    # =========================================================================
    # 3차시: G6-ESS-V1-3 (구조 확인)
    # 수필의 시작[화제·계기] - 중간[일화·관찰·감정 전환] - 끝[성찰·인생관 확장] 구조 도해
    # =========================================================================
    {
        "lesson_no": 3,
        "code": "G6-ESS-V1-3",
        "lesson_title": "수필의 '시작 - 중간 - 끝' 3단 성찰 구조 도해하기",
        "std_badge": "[6국02-02] [6국03-03] 3단 성찰 구조·의미 확장 도해",
        "student_goal": "작은 일상 소재(난초)에서 시작해 구체적 일화와 전환점을 거쳐 보편적 삶의 이치(무소유)로 확장되는 수필의 3단 구조를 도해할 수 있다.",
        "marking_items": [
            ("mk-highlight", "노란 형광펜", "각 단계(시작·중간·끝)의 중심 문장"),
            ("mk-double", "빨간 두줄", "내면의 태도가 바뀐 결정적 전환점(Turning Point)"),
        ],
        "left_page_body_html": """
        <div style="font-size:7.4pt; color:#1E8449; font-weight:700; margin-bottom:4px;">📐 수필이 <strong>[시작(계기·소재) ➔ 중간(일화·전환점·결단) ➔ 끝(보편적 성찰 확장)]</strong>의 3단 짜임으로 어떻게 생각을 넓혀 가는지 중심 문장(노란 형광펜)을 찾으며 읽어 봅시다.</div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📜 〈무소유〉 3단 구조 정독 — 작은 소재(점)에서 삶의 철학(면)으로</th>
              <th class="wing-head">🧭 구조 코칭 &amp; 의미 확장</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:7.3pt; font-weight:800; color:#1E8449; margin-bottom:2px;">[시작 — ➊문단: 중심 소재 제시와 난초를 기르게 된 계기]</div>
                <p><span class="p-num">➊</span> <span class="mk-highlight">나는 지난해 여름까지 난초 두 분(盆)을 정성스레, 정말 정성을 다해 길렀었다.</span> 3년 전 거처를 지금의 다래헌(茶來軒)으로 옮겨 왔을 때 어떤 스님이 우리 방으로 보내 준 것이다. 혼자 사는 거처라 살아 있는 생물이라고는 나하고 그 애들뿐이었다. 그 애들을 위해 관계 서적을 구해다 읽었고, 그 애들의 건강을 위해 하이포넥슨가 하는 비료를 바다 건너가는 친지들에게 부탁하여 구해 오기도 했었다. 여름철이면 서늘한 그늘을 찾아 자리를 옮겨 주어야 했고, 겨울에는 필요 이상으로 실내 온도를 높이곤 했었다. 이런 정성을 일찍이 부모에게 바쳤더라면 아마 효자 소리를 듣고도 남았을 것이다. 이렇듯 애지중지 가꾼 보람으로 이른 봄이면 은은한 향기와 함께 연둣빛 꽃을 피워 방 안을 채워 주었고, 잎은 늘 청청했었다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u3">
                  <div class="wing-box-title"><span>👁️ 시범 (I Do): 시작</span><span class="role-chip">점(소재)</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>첫 문장에서 '난초 두 분을 정성을 다해 길렀었다'라고 중심 소재와 경험을 바로 제시했어.</span></div>
                  <div class="think-row"><span class="think-tag">[역할]</span><span><strong>[시작]</strong>은 독자의 호기심을 끌고 회상의 실마리가 되는 <strong>작은 소재(난초)와 계기</strong>를 여는 단계야!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:7.3pt; font-weight:800; color:#D35400; margin-bottom:2px;">[중간 — ➋~➌문단: 봉선사 외출 사건과 내면의 전환점 및 결단]</div>
                <p><span class="p-num">➋</span> 지난해 여름 장마가 갠 어느 날 봉선사로 운허 노사를 뵈러 간 일이 있었다. 한낮이 되자 장마에 갇혔던 햇볕이 눈부시게 쏟아져 내리고 앞개울물 소리에 어울려 숲속에서는 매미들이 있는 대로 목청을 돋우었다. 아차! 이때에야 문득 생각이 난 것이다. 난초를 뜰에 내놓은 채 온 것이다. 모처럼 보인 찬란한 햇볕이 돌연 원망스러워졌다. 뜨거운 햇볕에 늘어져 있을 난초 잎이 눈에 아른거려 더 지체할 수가 없었다. <span class="mk-highlight">허둥지둥 그 길로 돌아왔다. 아니나 다를까, 잎은 축 늘어져 있었다.</span> 안타까워하며 샘물을 길어다 축여 주고 했더니 겨우 고개를 들었다. 하지만 어딘지 생생한 기운이 빠져나간 것 같았다.</p>
                <p><span class="p-num">➌</span> <span class="mk-double">나는 이때 온몸으로 그리고 마음속으로 절절히 느끼게 되었다. 집착이 괴로움인 것을.</span> 그렇다, 나는 난초에게 너무 집념(執念)한 것이다. 이 하나의 집착에 조금도 여유가 없이 매달려 있었던 것이다. 더구나 출가한 몸으로 별것도 아닌 한두 분의 식물에 마음을 빼앗겨 허둥대다니, 스스로 생각해 보아도 부끄러운 노릇이었다. <span class="mk-highlight">며칠 후 난초를 나처럼 아끼는 친구가 놀러 왔기에 선뜻 그의 품에 안겨 주었다. 비로소 나는 얽매임에서 벗어난 것이다.</span> 날아갈 듯이 홀가분한 해방감을 맛보았다. 이후부터 나는 하루 한 가지씩 버려야겠다고 스스로 다짐을 했다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 함께 (We Do): 중간</span><span class="role-chip">선(일화·전환)</span></div>
                  <div><strong>Q1.</strong> <strong>[중간]</strong> 단계에서 글쓴이의 생각이 확 바뀌게 만든 <strong>전환점(빨간 두줄)</strong>은 무엇인가요?</div>
                  <div>➔ 햇볕에 시든 난초 때문에 허둥대다가 <strong>'<span class="blank-slot"><span class="t-ans">집착이 괴로움</span></span>인 것'</strong>을 절절히 깨달은 순간!</div>
                  <div style="margin-top:3px;"><strong>Q2.</strong> 그 깨달음 뒤에 글쓴이는 어떤 행동(결단)을 했나요?</div>
                  <div>➔ 친구에게 <span class="blank-slot"><span class="t-ans">난초를 선뜻 안겨 주고</span></span> 얽매임에서 벗어났다.</div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:7.3pt; font-weight:800; color:#1B4F72; margin-bottom:2px;">[끝 — ➍문단: 개인의 일화에서 보편적 삶의 철학(무소유)으로 확장]</div>
                <p><span class="p-num">➍</span> 우리의 일상생활에서 꼭 필요한 물건이 과연 얼마나 될까. 그러니까 <span class="mk-highlight">무엇인가를 갖는다는 것은 다른 한편 무엇인가에 얽매이게 된다는 뜻이다.</span> 필요에 따라 가졌던 것이 도리어 우리를 부자유하게 얽어맨다고 할 때 주객이 전도되어 우리는 가짐을 당하게 된다. 흔히들 무엇인가를 더 많이 가지려고 아등바등하지만, 가만히 돌이켜 보면 가진 것 때문에 마음이 상하고 무거운 짐을 지고 있는 경우가 얼마나 많은가. 크게 버리는 사람만이 크게 얻을 수 있다는 말이 있다. 물건으로 인해 마음을 상하고 있는 사람들에게는 한 번쯤 생각해 볼 말이다. <span class="mk-highlight">아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다는 것은 무소유(無所有)의 역리(逆理)이니까.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🚀 스스로 (You Do): 끝</span><span class="role-chip">면(삶의 철학)</span></div>
                  <div><strong>Q3.</strong> <strong>[끝]</strong> 문단에서는 주어가 '나는'에서 누구로 넓어졌나요?</div>
                  <div>➔ '<span class="blank-slot"><span class="t-ans">우리(사람들)</span></span>'로 넓어지며, 난초 이야기를 넘어 <strong>인간 삶 전체의 소유와 자유</strong>에 대한 성찰로 확장되었다.</div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "시작 - 중간 - 끝 각 단계의 역할과 문단별 중심 문장 찾기",
            "tag": "Step 1 구조 표지·중심문장 (A6 결합)",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:15%;">구조 단계</th>
                  <th style="width:28%;">수필에서의 역할</th>
                  <th style="width:57%;">문단별 중심 문장 간추리기</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1E8449;">시작 (➊문단)</td>
                  <td>중심 소재(오브제) 제시 및 회상 계기 열기</td>
                  <td><span class="pencil-line">✏️ ➊: <span class="t-ans">나는 3년 전 선물 받은 난초 두 분을 온갖 정성을 다해 애지중지 길렀었다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#D35400;">중간 (➋~➌문단)</td>
                  <td>결정적 사건(일화) 발생 ➔ 내면의 반성(전환점) ➔ 행동의 결단</td>
                  <td>
                    • ➋: <span class="blank-slot"><span class="t-ans">봉선사 외출 중 쏟아진 햇볕에 난초가 걱정되어 허둥지둥 돌아오니 난초가 축 늘어져 있었다.</span></span><br>
                    • ➌: <span class="blank-slot"><span class="t-ans">집착이 괴로움임을 깨닫고 친구에게 난초를 준 뒤 홀가분한 해방감을 맛보았다.</span></span>
                  </td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1B4F72;">끝 (➍문단)</td>
                  <td>개인의 경험을 보편적 삶의 철학·가치관으로 확장</td>
                  <td><span class="pencil-line">✏️ ➍: <span class="t-ans">무엇인가를 갖는 것은 도리어 그것에 얽매이는 것이며, 아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 중심 문장을 바탕으로 [점(작은 사물) ➔ 선(개인의 일화) ➔ 면(보편적 삶의 이치)] 의미 확장 구조도 완성하기",
        "activity_2": {
            "title": "수필의 3단 의미 확장 구조 도해조직자 완성하기 (➔ 14차시 W3 개요 틀 직결)",
            "tag": "Step 2 거시 구조 도해",
            "body_html": """
            <div class="inference-row">
              <div class="inf-card c1">
                <strong style="color:#1E8449;">🟢 [시작] 점(Point): 일상 소재와 계기</strong>
                <div style="margin-top:3px;">
                  • <strong>중심 사물</strong>: <span class="blank-slot"><span class="t-ans">난초 두 분(화분)</span></span><br>
                  • <strong>초기 태도</strong>: 비료를 구해 오고 온도를 맞춰 주며 <span class="blank-slot"><span class="t-ans">애지중지 정성을 쏟음</span></span>
                </div>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:#D35400;">🟠 [중간] 선(Line): 일화와 전환점</strong>
                <div style="margin-top:3px;">
                  • <strong>갈등 일화</strong>: 뜰에 두고 간 난초가 햇볕에 시들자 허둥지둥 돌아옴.<br>
                  • <strong>전환점 &amp; 결단</strong>: <span class="blank-slot"><span class="t-ans">집착이 괴로움</span></span>임을 반성하고 친구에게 난초를 줌(해방감).
                </div>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#1B4F72;">🔵 [끝] 면(Plane): 보편적 삶의 철학</strong>
                <div style="margin-top:3px;">
                  • <strong>화제 확장</strong>: '나의 난초' ➔ <strong>'우리 모두의 <span class="blank-slot"><span class="t-ans">소유와 집착</span></span>'</strong><br>
                  • <strong>보편적 주제</strong>: 크게 버릴 때 크게 얻으며, 비움을 통해 참된 <span class="blank-slot"><span class="t-ans">마음의 자유(무소유)</span></span>에 이른다.
                </div>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 의미 확장 원리를 바탕으로 개인의 경험이 어떻게 독자 모두의 공감을 얻는지 설명하기",
        "activity_3": {
            "title": "'나만의 경험'을 '우리 모두의 지혜'로 넓히는 수필의 힘 서술하기",
            "tag": "Step 3 구조 원리 산출",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:3px;">• 글쓴이는 스님이고 독자인 우리는 학생인데도, 마지막 ➍문단을 읽을 때 고개가 끄덕여지는 까닭을 <strong>'시작-중간-끝의 의미 확장'</strong>과 관련지어 써 보세요.</div>
            <span class="pencil-line">✏️ <span class="t-ans">시작과 중간에서는 스님 개인이 겪은 '난초 일화'를 들려주었지만, 끝 문단에서 이를 '물건을 가지려다 도리어 물건에 얽매이는 우리 모두의 일상'으로 넓혀 보편적인 삶의 지혜를 일깨워 주었기 때문이다.</span></span>
            """,
        },
        "writing_seed": {
            "transfer_tag": "➔ 14차시(W3) 내 수필 '시작-중간-끝' 3단 개요 짜기로 1:1 미러링",
            "prompt": "내가 쓸 수필의 [시작(소재·계기) - 중간(결정적 사건과 깨달음의 순간) - 끝(친구들과 나누고 싶은 삶의 다짐)]을 한 단어로 스케치해 보세요.",
            "placeholder": "(시작 소재 ➔ 중간 전환점 사건 ➔ 끝 삶의 다짐)",
            "example_answer": "[시작] 한정판 축구화 ➔ [중간] 비 오는 날 공을 피하다 넘어져 부끄러웠던 순간과 동생에게 축구화를 준 일 ➔ [끝] 물건의 주인이 되어 자유롭게 즐기자는 다짐",
        },
        "self_check": [
            "수필의 '시작 - 중간 - 끝' 3단 구성과 문단별 중심 문장을 찾았나요?",
            "글쓴이의 생각이 바뀐 전환점(Turning Point)을 정확히 짚었나요?",
            "개인의 일화(점·선)가 보편적 삶의 철학(면)으로 확장되는 구조를 도해했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측] 수필의 동심원 확장 모형: 점(➊ 난초 두 화분) ➔ 선(➋~➌ 봉선사 햇볕 사건 & 집착 반성·양보) ➔ 면(➍ 인간 삶의 소유와 자유·무소유) ➔ [우측] 14차시(W3) 내 수필 개요 틀로의 미러링 예고.",
            "intro_5min": "물에 작은 조약돌 하나를 던지면 물결이 동그랗게 퍼져 나가듯, 좋은 수필은 작은 일상 사물 하나에서 시작해 세상 전체의 이치로 넓어진다는 점을 시각 자료(동심원 그림)로 보여 줍니다.",
            "ido_think_aloud_script": "“선생님이 〈무소유〉 전체의 설계도를 그려 볼게요. ➊문단은 [시작]이에요. '난초 두 분'이라는 작은 점(소재)에서 이야기를 시작하죠. ➋~➌문단은 [중간]이에요. 봉선사에 갔다가 햇볕에 시든 난초 때문에 허둥대고, '아, 집착이 괴로움이구나!'라고 깨닫는 전환점을 지나 친구에게 난초를 주는 선(일화)이 펼쳐집니다. 그리고 ➍문단 [끝]을 보세요. 더 이상 난초 이야기만 하지 않고 '우리의 일상생활에서 꼭 필요한 물건이 얼마나 될까'라며 모든 사람의 삶(면)으로 생각을 확 넓히고 있어요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "구조·전환(A6)",
                    "question": "[중간] 부분(➋~➌문단)에서 글쓴이의 태도가 '애지중지 매달림'에서 '홀가분한 버림'으로 바뀌게 된 결정적 전환점 문장은 어디인가요?",
                    "expected_ans": "➌문단 첫 문장인 '나는 이때 온몸으로 그리고 마음속으로 절절히 느끼게 되었다. 집착이 괴로움인 것을.'입니다.",
                    "reprompt": "시든 난초에게 물을 준 직후, 글쓴이가 마음속으로 무엇을 절절히 깨달았는지 ➌문단 첫째 줄을 찾아보세요.",
                },
                {
                    "qar_type": "담화 확장(A4·A6)",
                    "question": "➍문단 첫 문장에서 글쓴이는 왜 '나의 방에 필요한 물건'이라고 하지 않고 '우리의 일상생활에서 꼭 필요한 물건'이라고 표현했을까요?",
                    "expected_ans": "자신만의 특별한 경험에 머물지 않고, 글을 읽는 독자 모두가 자신의 삶을 되돌아보며 공감할 수 있도록 보편적인 삶의 문제로 확장하기 위해서입니다.",
                    "reprompt": "'나'만 겪는 문제와 '우리 모두'가 겪는 문제 중 어느 쪽이 독자에게 더 큰 울림과 교훈을 줄지 생각해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]과 [활동 2]의 3단 구조 도해조직자를 완성하도록 돕습니다. 특히 이 '시작(점) - 중간(선·전환점) - 끝(면)' 도해조직자가 14차시(W3)에 자신이 직접 수필 개요를 짤 때 그대로 쓰이는 설계도임을 알려 주고 씨앗을 적게 합니다.",
            "answer_key_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <strong>1. 본문 날개 정답:</strong> Q1. 집착이 괴로움 | Q2. 난초를 선뜻 안겨 주고 | Q3. 우리(사람들)<br>
              <strong>2. [활동 1] 중심 문장 모범 답안:</strong><br>
              • ➊: 나는 3년 전 선물 받은 난초 두 분을 온갖 정성을 다해 애지중지 길렀었다.<br>
              • ➋: 봉선사 외출 중 쏟아진 햇볕에 난초가 걱정되어 허둥지둥 돌아오니 난초가 축 늘어져 있었다.<br>
              • ➌: 집착이 괴로움임을 깨닫고 친구에게 난초를 준 뒤 홀가분한 해방감을 맛보았다.<br>
              • ➍: 무엇인가를 갖는 것은 도리어 그것에 얽매이는 것이며, 아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다.<br>
              <strong>3. [활동 2] 구조 도해 정답:</strong> [시작] 난초 두 분(화분) / 애지중지 정성을 쏟음 ➔ [중간] 집착이 괴로움 ➔ [끝] 소유와 집착 / 마음의 자유(무소유)<br>
              <strong>4. [활동 3] 모범 답안:</strong> 시작과 중간에서는 스님 개인의 '난초 일화'를 다루었지만, 끝 문단에서 이를 '가진 물건 때문에 도리어 얽매이는 우리 모두의 일상'으로 확장하여 보편적인 삶의 진리를 일깨워 주었기 때문이다.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "➌문단(난초를 친구에게 준 일)을 [끝] 단계로 분류함",
                    "diagnosis": "사건이 해결된 시점(난초 양보)과 보편적 삶의 철학으로 확장된 시점(4문단)을 구분하지 못함",
                    "prescription": "➌문단은 여전히 '난초 일화'의 마무리(결단)에 해당하며, 난초 이야기를 넘어 '인간의 소유와 자유' 전체를 성찰하는 ➍문단이 수필의 진정한 [끝(성찰 확장)]임을 짚어 줍니다.",
                },
                {
                    "error_case": "중심 문장을 찾을 때 세부 예시('하이포넥슨가 하는 비료를 구해 오기도 했었다')를 골라 적음",
                    "diagnosis": "중심 문장(정성을 다해 길렀다)과 이를 뒷받침하는 세부 사례(비료, 온도 조절)의 위계를 혼동함",
                    "prescription": "비료 이야기와 온도 이야기를 모두 포괄할 수 있는 대표 문장이 ➊문단 첫째 줄('정성을 다해 길렀었다')임을 상위·하위 포함 관계로 안내합니다.",
                },
            ],
            "scaffolding_down": "중심 문장 추출이 어려운 학생에게는 각 문단의 첫 문장과 마지막 문장에 밑줄을 긋게 한 뒤, 문단 전체 내용을 대표하는 문장을 고르게 합니다.",
            "scaffolding_up": "만약 이 수필에서 ➍문단([끝])을 아예 삭제하고 ➌문단으로 글을 끝낸다면 주제의 깊이가 어떻게 달라질지 비교하여 발표하게 합니다.",
            "rubric": {
                "high": "수필의 '시작-중간-끝' 3단 구조와 문단별 중심 문장을 정확히 추출하고, '점(소재)➔선(일화·전환)➔면(보편적 성찰)'의 의미 확장 원리를 도해하고 서술한다.",
                "mid": "시작-중간-끝의 단계 구분과 도해 빈칸은 채웠으나, 개인의 경험이 보편적 성찰로 확장되는 원리 설명이 다소 부족하다.",
                "low": "문단별 중심 문장과 세부 문장을 구분하지 못하거나 3단 구조 도해를 완성하지 못한다.",
            },
        },
    },

    # =========================================================================
    # 4차시: G6-ESS-V1-4 (요약 및 주제 확인)
    # 주·목·서 골격 압축 1문장 요약 및 은유·성찰적 제목 리브랜딩
    # =========================================================================
    {
        "lesson_no": 4,
        "code": "G6-ESS-V1-4",
        "lesson_title": "핵심 골격으로 한 문장 요약하고 은유적 새 제목 붙이기",
        "std_badge": "[6국02-02] [6국04-05] 거시요약·문장골격·제목리브랜딩",
        "student_goal": "수식어를 덜어낸 주·목·서 문장 골격으로 [경험]과 [성찰]을 결합해 한 문장으로 요약하고, 중심 소재와 깨달음을 담은 새 제목을 붙일 수 있다.",
        "marking_items": [
            ("mk-dotted", "점선 밑줄", "요약할 때 삭제할 세부 수식어·예시"),
            ("mk-highlight", "노란 형광펜", "요약문에 꼭 넣을 [핵심 경험] 골격"),
            ("mk-double", "빨간 두줄", "요약문에 꼭 넣을 [핵심 성찰(주제)] 골격"),
        ],
        "left_page_body_html": """
        <div style="font-size:7.4pt; color:#1E8449; font-weight:700; margin-bottom:4px;">✂️ <strong>수필 요약의 황금 공식:</strong> 세부 수식어·예시(점선)는 덜어 내고, <strong>[핵심 경험(노란 형광펜)] + [핵심 성찰(빨간 두줄)]</strong>을 주·목·서 골격으로 결합합니다!</div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📜 〈무소유〉 요약 스튜디오 — 덜어 내기와 골격 세우기</th>
              <th class="wing-head">🧠 요약 4원칙 코칭</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span> 나는 지난해 여름까지 <span class="mk-highlight">난초 두 분(盆)을 정성스레, 정말 정성을 다해 길렀었다.</span> <span class="mk-dotted">3년 전 거처를 지금의 다래헌(茶來軒)으로 옮겨 왔을 때 어떤 스님이 우리 방으로 보내 준 것이다. 혼자 사는 거처라 살아 있는 생물이라고는 나하고 그 애들뿐이었다. 그 애들을 위해 관계 서적을 구해다 읽었고, 그 애들의 건강을 위해 하이포넥슨가 하는 비료를 바다 건너가는 친지들에게 부탁하여 구해 오기도 했었다. 여름철이면 서늘한 그늘을 찾아 자리를 옮겨 주어야 했고, 겨울에는 필요 이상으로 실내 온도를 높이곤 했었다. 이런 정성을 일찍이 부모에게 바쳤더라면 아마 효자 소리를 듣고도 남았을 것이다. 이렇듯 애지중지 가꾼 보람으로 이른 봄이면 은은한 향기와 함께 연둣빛 꽃을 피워 방 안을 채워 주었고, 잎은 늘 청청했었다.</span></p>
                <p><span class="p-num">➋</span> 지난해 여름 장마가 갠 어느 날 봉선사로 운허 노사를 뵈러 간 일이 있었다. <span class="mk-dotted">한낮이 되자 장마에 갇혔던 햇볕이 눈부시게 쏟아져 내리고 앞개울물 소리에 어울려 숲속에서는 매미들이 있는 대로 목청을 돋우었다. 아차! 이때에야 문득 생각이 난 것이다.</span> <span class="mk-highlight">난초를 뜰에 내놓은 채 온 것이다.</span> 모처럼 보인 찬란한 햇볕이 돌연 원망스러워졌다. 뜨거운 햇볕에 늘어져 있을 난초 잎이 눈에 아른거려 더 지체할 수가 없었다. <span class="mk-highlight">허둥지둥 그 길로 돌아왔다. 아니나 다를까, 잎은 축 늘어져 있었다.</span> <span class="mk-dotted">안타까워하며 샘물을 길어다 축여 주고 했더니 겨우 고개를 들었다. 하지만 어딘지 생생한 기운이 빠져나간 것 같았다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u3">
                  <div class="wing-box-title"><span>👁️ 시범 (I Do): 삭제·일반화</span><span class="role-chip">교사 시범</span></div>
                  <div class="think-row"><span class="think-tag">[삭제]</span><span>'하이포넥스 비료', '실내 온도' 같은 세부 예시는 점선(⋯)으로 지워도 뜻이 통해.</span></div>
                  <div class="think-row"><span class="think-tag">[선택]</span><span>대신 이 모든 예를 아우르는 <strong>'난초 두 분을 정성을 다해 길렀으나 외출 중 햇볕에 시들까 봐 허둥대며 괴로워했다'</strong>는 핵심 경험만 남기자!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➌</span> <span class="mk-double">나는 이때 온몸으로 그리고 마음속으로 절절히 느끼게 되었다. 집착이 괴로움인 것을.</span> <span class="mk-dotted">그렇다, 나는 난초에게 너무 집념(執念)한 것이다. 이 하나의 집착에 조금도 여유가 없이 매달려 있었던 것이다. 더구나 출가한 몸으로 별것도 아닌 한두 분의 식물에 마음을 빼앗겨 허둥대다니, 스스로 생각해 보아도 부끄러운 노릇이었다.</span> <span class="mk-highlight">며칠 후 난초를 나처럼 아끼는 친구가 놀러 왔기에 선뜻 그의 품에 안겨 주었다. 비로소 나는 얽매임에서 벗어난 것이다.</span> 날아갈 듯이 홀가분한 해방감을 맛보았다. 이후부터 나는 하루 한 가지씩 버려야겠다고 스스로 다짐을 했다.</p>
                <p><span class="p-num">➍</span> <span class="mk-dotted">우리의 일상생활에서 꼭 필요한 물건이 과연 얼마나 될까.</span> 그러니까 <span class="mk-double">무엇인가를 갖는다는 것은 다른 한편 무엇인가에 얽매이게 된다는 뜻이다.</span> 필요에 따라 가졌던 것이 도리어 우리를 부자유하게 얽어맨다고 할 때 주객이 전도되어 우리는 가짐을 당하게 된다. <span class="mk-dotted">흔히들 무엇인가를 더 많이 가지려고 아등바등하지만, 가만히 돌이켜 보면 가진 것 때문에 마음이 상하고 무거운 짐을 지고 있는 경우가 얼마나 많은가.</span> <span class="mk-double">크게 버리는 사람만이 크게 얻을 수 있다는 말이 있다.</span> 물건으로 인해 마음을 상하고 있는 사람들에게는 한 번쯤 생각해 볼 말이다. <span class="mk-double">아무것도 갖지 않을 때 비로소 온 세상을 갖게 된다는 것은 무소유(無所有)의 역리(逆理)이니까.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 함께 &amp; 🚀 스스로</span><span class="role-chip">성찰 압축</span></div>
                  <div><strong>Q1.</strong> ➌~➍문단에서 두 줄(🔴) 친 문장들이 공통으로 말하는 핵심 성찰 키워드 2개는 무엇인가요?</div>
                  <div>➔ <span class="blank-slot"><span class="t-ans">집착(얽매임)</span></span>에서 벗어나기, <span class="blank-slot"><span class="t-ans">무소유(크게 버림)</span></span>의 참된 자유!</div>
                  <div style="margin-top:3px;"><strong>Q2.</strong> 수필 제목을 지을 때 '소재(난초)'와 '주제(자유/비움)'를 결합하면 어떤 효과가 있을까요?</div>
                  <div>➔ 글의 구체적 글감과 깊은 철학이 한눈에 드러난다.</div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "요약 규칙(삭제·선택·일반화)으로 단계별 필수 핵심어 추출하기",
            "tag": "Step 1 수식어 삭제·핵심어 추출 (A3·A6)",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:16%;">단계</th>
                  <th style="width:42%;">삭제·일반화한 세부 내용 (점선 부분)</th>
                  <th style="width:42%;">남겨야 할 필수 핵심어 (주어·목적어·서술어 재료)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800;">시작·중간<br>(경험)</td>
                  <td>서적 읽기, 하이포넥스 비료 구하기, 그늘·실내 온도 조절, 봉선사 앞개울물·매미 소리 등</td>
                  <td>• 핵심 경험 재료: <span class="blank-slot"><span class="t-ans">애지중지 기르던 난초</span></span>에 마음이 얽매여 괴로워하다가, 친구에게 <span class="blank-slot"><span class="t-ans">난초를 선뜻 준 경험</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800;">중간·끝<br>(성찰)</td>
                  <td>출가한 몸으로서의 부끄러움, 일상생활에서 필요한 물건에 대한 질문 등</td>
                  <td>• 핵심 성찰 재료: 소유에 대한 <span class="blank-slot"><span class="t-ans">집착이 곧 괴로움</span></span>이며, 가진 것을 비울 때 참된 자유를 얻는다는 <span class="blank-slot"><span class="t-ans">무소유의 진리</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 추출한 [핵심 경험]과 [핵심 성찰] 재료를 주·목·서 요약 슬롯에 넣어 3문장 및 1문장으로 압축하기",
        "activity_2": {
            "title": "주·목·서 요약 빌더로 3문장 ➔ 1문장 압축 요약 완성하기",
            "tag": "Step 2 골격 결합·호응 검증",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:3px;"><strong>[1단계: 시작-중간-끝 3문장 요약]</strong></div>
            <div style="background:#F8F9F9; border:0.75pt solid #BDC3C7; border-radius:4px; padding:4px 7px; font-size:7.3pt; margin-bottom:4px;">
              ① <strong>(시작)</strong> 글쓴이는 선물 받은 난초 두 분을 온갖 정성을 다해 애지중지 길렀다.<br>
              ② <strong>(중간)</strong> 외출 중 햇볕에 시든 난초 때문에 허둥대다가 <span class="blank-slot"><span class="t-ans">집착이 괴로움</span></span>임을 깨닫고 친구에게 난초를 주며 해방감을 맛보았다.<br>
              ③ <strong>(끝)</strong> 이를 통해 무엇을 갖는 것은 그것에 얽매이는 것이며, <span class="blank-slot"><span class="t-ans">아무것도 갖지 않을 때 온 세상을 얻는다는 무소유의 이치</span></span>를 깨달았다.
            </div>
            <div style="font-size:7.4pt; margin-bottom:2px;"><strong>[2단계: 주·목·서 호응 슬롯을 결합한 1문장 압축 요약]</strong></div>
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:14%;">주어 (누가는)</th>
                  <th style="width:36%;">부사어 ([핵심 경험]을 통해)</th>
                  <th style="width:36%;">목적어 ([핵심 성찰·주제]를)</th>
                  <th style="width:14%;">서술어 (어찌했다)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="text-align:center; font-weight:700;">글쓴이는</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">애지중지하던 난초에 얽매여 괴로워하다가 친구에게 난초를 떠나보낸 경험을 통해,</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">집착을 버리고 비울 때 비로소 참된 마음의 자유를 얻는다는 '무소유'의 삶의 가치를</span></span></td>
                  <td style="text-align:center; font-weight:700;"><span class="blank-slot"><span class="t-ans">깨달았다(성찰했다).</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 1문장 요약문(소재 + 주제)을 바탕으로 독자의 마음을 사로잡는 은유적 새 제목 리브랜딩하기",
        "activity_3": {
            "title": "중심 사물(난초)과 깨달음(자유·비움)을 결합한 새 제목 리브랜딩",
            "tag": "Step 3 제목 창안·산출",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:28%;">제목 짓기 유형</th>
                  <th style="width:34%;">내가 붙인 새로운 제목</th>
                  <th style="width:38%;">그렇게 제목을 붙인 까닭 (소재·주제 연결)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700;">① [중심 소재 + 깨달음] 결합형</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">난초를 떠나보내고 얻은 마음의 자유</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">중심 소재인 '난초'를 양보한 경험과 그 결과 얻은 '마음의 자유'가 한눈에 드러나기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700;">② [비유·역설적 성찰] 강조형</td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">두 손은 비우고 온 세상을 품다</span></span></td>
                  <td><span class="pencil-line">✏️ <span class="t-ans">'아무것도 갖지 않을 때 온 세상을 갖게 된다'는 4문단의 역설적 주제를 비유적으로 압축했기 때문이다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "➔ 12·15차시(W1·W4) 내 수필의 주제문 및 제목 설정으로 전이",
            "prompt": "내가 쓸 수필의 [1문장 핵심 주제문]과 [소재+깨달음을 담은 멋진 가제목]을 지어 보세요.",
            "placeholder": "(내 수필 가제목 / 1문장 주제문)",
            "example_answer": "[가제목] 흙 묻은 축구화가 선물한 진짜 자유 / [주제문] 나는 아끼던 축구화를 동생에게 물려준 경험을 통해, 물건에 대한 집착을 내려놓을 때 더 큰 기쁨을 얻을 수 있음을 깨달았다.",
        },
        "self_check": [
            "세부 예시를 덜어 내고 [핵심 경험]과 [핵심 성찰]만 골라냈나요?",
            "주어·부사어·목적어·서술어 호응에 맞게 한 문장으로 요약했나요?",
            "중심 소재와 주제가 잘 드러나는 창의적인 새 제목을 붙였나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측] 요약 4원칙(삭제: 비료·온도 세부예시 ➔ 일반화: 애지중지 기름 ➔ 선택: 집착 반성·무소유) ➔ [중앙] 수필 1문장 요약 공식: [글쓴이는(주) + ~한 경험을 통해(부) + ~라는 삶의 가치를(목) + 깨달았다(서)] ➔ [우측] 제목 리브랜딩 2가지 전략(소재+깨달음형 / 은유·역설형).",
            "intro_5min": "수필을 요약할 때 흔히 저지르는 실수 두 가지('난초를 길렀다'처럼 경험만 쓰는 것 vs '욕심을 버리자'처럼 교훈만 쓰는 것)를 칠판에 보여 주고, 좋은 수필 요약문에는 반드시 [경험]과 [성찰] 두 바퀴가 함께 들어가야 함을 안내합니다.",
            "ido_think_aloud_script": "“선생님이 ➊~➋문단을 어떻게 줄이는지 보세요. '하이포넥스 비료를 구해 오고, 여름에는 그늘로 옮기고, 겨울에는 온도를 높이고...' 이건 모두 '난초를 애지중지 길렀다'는 한마디를 뒷받침하는 세부 예시니까 점선으로 지울게요(삭제·일반화). 그리고 ➌~➍문단에서는 '집착이 괴로움임을 깨닫고 난초를 친구에게 준 뒤, 비울 때 참된 자유를 얻는다는 무소유의 이치를 깨달았다'를 골라냅니다(선택). 이제 이 둘을 [글쓴이는 ~한 경험을 통해 ~라는 가치를 깨달았다] 틀에 끼우면 완벽한 한 문장 요약이 완성돼요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "요약·위계(A6)",
                    "question": "만약 이 글을 '글쓴이는 난초 두 분을 키우다가 여름 햇볕에 시들자 친구에게 주었다.'라고만 요약했다면 왜 부족한 요약일까요?",
                    "expected_ans": "글쓴이가 겪은 외적 사건(경험)만 적혀 있고, 그 일을 통해 얻은 가장 중요한 주제인 '집착에서 벗어난 해방감과 무소유의 성찰'이 통째로 빠졌기 때문입니다.",
                    "reprompt": "수필의 진짜 목적이 '난초 자랑'인지, 아니면 '소유와 집착에 대한 깨달음 전달'인지 4문단을 보며 생각해 볼까요?",
                },
                {
                    "qar_type": "통사·호응(A3)",
                    "question": "[활동 2]의 1문장 요약 슬롯에서 '글쓴이는 ~한 경험을 통해 ~라는 가치를' 뒤에 어울리는 서술어는 무엇인가요?",
                    "expected_ans": "목적어 '~가치를/이치를'과 주어 '글쓴이는'에 호응하는 타동사 서술어인 '깨달았다(성찰했다, 발견했다)'가 와야 문장 호응이 정확합니다.",
                    "reprompt": "'글쓴이는 가치를 중요하다'라고 하면 어색하죠? '가치를'이라는 목적어와 짝을 이루는 움직임 말을 찾아보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 2]의 1문장 요약 빌더를 완성하고 [활동 3]에서 자신만의 새 제목을 리브랜딩해 발표하도록 합니다. 사실적 이해 4차시(V1-1~V1-4) 동안 〈무소유〉의 내용·관계·구조·주제를 완벽히 파악했음을 칭찬하고, 다음 차시(V2-1)부터는 행간의 숨은 뜻과 상징을 추론할 것임을 예고합니다.",
            "answer_key_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <strong>1. 본문 날개 정답:</strong> Q1. 집착(얽매임), 무소유(크게 버림)<br>
              <strong>2. [활동 1] 정답:</strong> • 경험 재료: 애지중지 기르던 난초 / 난초를 선뜻 준 경험 • 성찰 재료: 집착이 곧 괴로움 / 무소유의 진리<br>
              <strong>3. [활동 2] 3문장 &amp; 1문장 요약 모범 답안:</strong><br>
              • <strong>3문장 요약</strong>: 빈칸 — 집착이 괴로움 / 아무것도 갖지 않을 때 온 세상을 얻는다는 무소유의 이치<br>
              • <strong>1문장 요약</strong>: 글쓴이는 <strong>애지중지하던 난초에 얽매여 괴로워하다가 친구에게 난초를 떠나보낸 경험을 통해,</strong> <strong>집착을 버리고 비울 때 비로소 참된 마음의 자유를 얻는다는 '무소유'의 삶의 가치를</strong> <strong>깨달았다.</strong><br>
              <strong>4. [활동 3] 제목 리브랜딩 예시 답안:</strong><br>
              • ① 소재+깨달음형: 〈난초 두 화분이 가르쳐 준 비움의 지혜〉, 〈난초를 떠나보내고 얻은 마음의 자유〉<br>
              • ② 비유·역설형: 〈두 손은 비우고 온 세상을 품다〉, 〈가짐을 당하던 마음에서 날아오른 자유〉
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "1문장 요약문을 쓸 때 '우리는 물건을 버려야 한다'처럼 주장하는 글(논설문) 형태로 요약함",
                    "diagnosis": "성찰적 수필의 요약(경험을 통한 깨달음)과 논설문의 주장 요약(~해야 한다)을 혼동함",
                    "prescription": "수필 요약문은 남을 설득하는 명령조가 아니라, '[글쓴이는 ~한 경험을 통해 ~을 깨달았다]'는 성찰 구조로 써야 갈래 특성이 살아남을 안내합니다.",
                },
                {
                    "error_case": "새 제목을 '난초 키우기 힘들었던 날'처럼 단순 일기 제목으로 붙임",
                    "diagnosis": "중심 소재(난초)만 반영하고 3~4문단의 핵심 주제(집착 내려놓기, 마음의 자유)를 제목에 담지 못함",
                    "prescription": "제목에 '난초(소재)'와 함께 '비움, 자유, 내려놓음(주제어)'이 함께 들어가도록 단어를 조합해 보게 합니다.",
                },
            ],
            "scaffolding_down": "1문장 요약이 어려운 학생에게는 [활동 2]의 3문장 요약문 중 ②번(중간)과 ③번(끝)을 연결 어미('~한 경험을 통해')로 이어 붙이는 단계별 가이드를 제공합니다.",
            "scaffolding_up": "원제목인 〈무소유(無所有)〉라는 한자어 제목이 주는 묵직한 철학적 울림과, 자신이 새로 붙인 우리말 은유적 제목이 독자에게 주는 친근함의 차이를 비교해 발표하게 합니다.",
            "rubric": {
                "high": "세부 수식어를 덜어 내고 [핵심 경험]과 [핵심 성찰]을 주·목·서 호응에 맞게 1문장으로 정확히 압축하며, 소재와 주제를 결합한 창의적 제목을 짓는다.",
                "mid": "1문장 요약문에 경험과 성찰이 모두 포함되었으나 문장 호응이 다소 길거나 새 제목이 평면적이다.",
                "low": "경험이나 성찰 중 한쪽만 요약문에 쓰거나 주술 호응이 맞지 않는 비문을 작성한다.",
            },
        },
    },
]
