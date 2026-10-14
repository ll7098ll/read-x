# -*- coding: utf-8 -*-
"""
4단원: 설명문 (unit4_expository) — Batch 3 (9~11차시: V3-1 ~ V3-3 평가적 이해 및 독립적 읽기)
기출간 원문 100% 수록 (축약·생략 절대 금지), 11차시 코넬식 자율 독서 날개 및 교사용 정답(.t-ans) 완비
"""

BATCH3 = [
    # =========================================================================
    # 9차시: G6-EXP-V3-1 설명 방법·표현 및 시각 자료의 적절성 평가
    # 제재: 화제 ‘미래 식량 식용 곤충’ 2편 비교
    #       [글 가] 농촌진흥청·FAO 통계 설명문 + 단백질·온실가스 막대그래프
    #       vs [글 나] 서울시 식생활종합지원센터·어린이동아 과제 분석문 + 부적절한 도표/문장 교정
    # =========================================================================
    {
        "lesson_no": 9,
        "code": "G6-EXP-V3-1",
        "lesson_title": "설명 방법·서술 표현 및 시각 자료의 적절성 평가하기",
        "std_badge": "[6국02-03] · [6국05-02] · CCSS RI.6.5, RI.6.7",
        "student_goal": "동일한 화제를 다룬 두 설명문을 비교하며 대상의 특성과 독자 수준에 비추어 설명 방법과 시각 자료의 적절성을 평가하고, 부적절한 주관적 서술과 도표를 바르게 고칠 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "각 글에 사용된 핵심 설명 방법(정의·분류·비교·사례·문제분석)"],
            ["mk-line-blue", "파란 밑줄", "시각 자료(그래프)와 정확히 연결되는 본문 수치"],
            ["mk-line-red", "빨간 밑줄", "설명문의 객관성을 해치는 부적절한 주관적·단정적 표현"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 화제: 미래 식량 ‘식용 곤충’ — [글 가]와 [글 나]의 설명 방법·시각자료 비교 평가</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 농촌진흥청·유엔식량농업기구(FAO) &amp; 서울시 식생활종합지원센터·어린이동아</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 및 시각 자료 정독 (설명 방법·어조·도표의 적절성을 점검하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 적절성 평가 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#1A5276; margin-bottom:2px;">[글 가] 식량 위기와 환경 문제를 해결할 ‘작은 가축’, 식용 곤충</div>
                <p><span class="p-num">➊</span> 유엔식량농업기구(FAO)는 인구 증가와 기후 변화로 다가올 미래 식량 위기를 해결할 핵심 대안으로 ‘식용 곤충’을 지목하고 이를 ‘작은 가축’이라고 불렀다. <span class="mk-person">식용 곤충이란 사람이 안전하게 먹을 수 있도록 위생적인 사육 시설에서 기르고 가공한 곤충을 말한다(정의).</span> 현재 우리나라 식품의약품안전처가 식품 원료로 공식 인정한 식용 곤충에는 <span class="mk-person">메뚜기, 식용누에(백강잠·홍잠), 갈색거저리 유충(고소애), 흰점박이꽃무지 유충(꽃벵이), 쌍별귀뚜라미(쌍별이), 장수풍뎅이 유충 등 모두 10종이 속한다(분류·예시).</span></p>
                <p><span class="p-num">➋</span> 식용 곤충이 주목받는 첫째 이유는 뛰어난 영양 가치 때문이다. 농촌진흥청의 성분 분석 자료에 따르면, <span class="mk-line-blue">말린 갈색거저리 유충(고소애) 100그램 속에는 단백질이 약 53그램이나 들어 있다. 이는 같은 무게의 소고기(약 21그램)나 돼지고기(약 20그램)에 비해 단백질 함량이 두 배 이상 높은 수치이다(비교·대조 및 수치 제시).</span> 둘째 이유는 친환경적인 사육 효율이다. <span class="mk-line-blue">같은 1킬로그램의 단백질을 생산할 때 식용 곤충이 배출하는 온실가스의 양은 소를 기를 때(약 28킬로그램)의 10분의 1 이하(약 2.5킬로그램)에 불과하며,</span> 사육에 필요한 땅의 넓이와 물의 사용량도 가축보다 훨씬 적어 지구 환경을 지키는 데 크게 이바지한다.</p>
                <div style="background:#EBF5FB; border:0.75pt solid #5DADE2; border-radius:4px; padding:3.5px 6px; margin-top:3px; font-family:var(--font-sans); font-size:6.9pt;">
                  <strong>📊 [글 가의 시각자료 1] 식품 100g당 단백질 함량(g) 및 단백질 1kg 생산 시 온실가스 배출량(kg) 비교 막대그래프</strong> (출처: 농촌진흥청·유엔식량농업기구 FAO, 2022)<br>
                  • <strong>100g당 단백질 함량</strong>: 고소애(갈색거저리 유충) <strong>53g</strong> ≫ 소고기 <strong>21g</strong> &gt; 돼지고기 <strong>20g</strong><br>
                  • <strong>단백질 1kg당 온실가스 배출량</strong>: 소 <strong>28.0kg</strong> ≫ 돼지 <strong>11.2kg</strong> ≫ 식용 곤충(고소애) <strong>2.5kg</strong>
                </div>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 함께 평가하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>[글 가]가 선택한 설명 방법과 [시각자료 1]은 독자의 이해를 돕기에 적절할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>➊문단은 낯선 대상을 <strong>정의·분류</strong>해 주고, ➋문단은 소고기·돼지고기와 <strong>비교·대조</strong>하며 <strong>수치</strong>를 제시했어. 특히 [시각자료 1]은 수량의 많고 적음을 한눈에 견주는 <strong>막대그래프</strong>에 단위(g, kg)와 출처(농촌진흥청·FAO)까지 정확히 밝혔네!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>본문의 비교 수치와 막대그래프가 1:1로 일치하여 적절성이 매우 높구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#196F3D; margin-bottom:2px;">[글 나] 병원 환자식부터 과자까지 변신하는 식용 곤충, 식탁에 오르기까지의 과제</div>
                <p><span class="p-num">➌</span> 최근 고단백 영양 식품인 식용 곤충이 환자의 회복을 돕는 의료용 식품과 일상 간식으로 다양하게 활용되고 있다. <span class="mk-person">실제로 강남세브란스병원 연구진이 수술 및 항암 치료를 받는 환자들에게 갈색거저리 유충(고소애)으로 만든 환자식을 8주 동안 섭취하게 한 결과, 환자들의 단백질 섭취율이 높아지고 면역력이 빠르게 회복되는 효과가 나타났다(구체적 사례).</span> 또한 곤충 특유의 고소한 맛을 살려 분말이나 기름 형태로 가공한 쿠키, 에너지바, 국수, 어묵 등도 개발되고 있다.</p>
                <p><span class="p-num">➍</span> 하지만 이처럼 유익한 식용 곤충이 우리 일상 식탁에 널리 오르기까지는 <span class="mk-person">해결해야 할 현실적인 과제도 남아 있다(문제·해결 분석).</span> 가장 큰 걸림돌은 ‘곤충은 생김새가 징그럽다’는 소비자들의 심리적 거부감이다. <span class="mk-line-red">( ㉠ ) 곤충을 징그럽다고 먹지 않는 사람은 지구 환경을 전혀 생각하지 않는 어리석고 이기적인 사람이다.</span> 이 때문에 곤충의 원래 모습이 보이지 않도록 고운 가루로 만들어 빵이나 과자에 넣는 가공 기술이 연구되고 있다. 또 다른 문제는 비싼 가격이다. 아직은 소규모 농가에서 생산과 가공, 유통을 모두 도맡아 하는 경우가 많아 기존 단백질 식재료보다 가격이 비싸다. 전문가들은 대량 생산 체계를 갖추어 가격을 낮추고, 갑각류 알레르기 안전 표시도 강화해야 한다고 설명한다.</p>
                <div style="background:#FDEDEC; border:0.75pt solid #E74C3C; border-radius:4px; padding:3.5px 6px; margin-top:3px; font-family:var(--font-sans); font-size:6.9pt;">
                  <strong>📈 [글 나의 시각자료 2 (점검 대상)] 연도별 세계 산업용 로봇 판매 대수 전망 꺾은선그래프 (출처·단위 없음)</strong><br>
                  <span style="color:#B03A2E;">※ 비교 대안 자료 <strong>[시각자료 2-수정안]</strong>: 『소비자가 식용 곤충을 구매하지 않는 이유 설문 조사 원그래프 (출처: 농촌진흥청 소비자 인식 조사, 2023 / 단위: %) — ① 생김새 거부감(62.4%), ② 비싼 가격(18.5%), ③ 맛·안전성 우려(12.1%), ④ 기타(7.0%)』</span>
                </div>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 짝·스스로 평가하기</span><span class="role-chip">We·You Do</span></div>
                  <div>1. [글 나]의 ➍문단에 밑줄 친 <strong>문장 ( ㉠ )</strong>이 설명문의 표현으로 부적절한 까닭은 무엇인가요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">객관적 사실 전달이 아니라 필자의 주관적인 비난과 감정적 편견이 담긴 표현이기 때문이다.</span></span>
                  <div style="margin-top:3px;">2. [글 나]에 첨부된 <strong>[시각자료 2(로봇 그래프)]</strong>의 문제점 2가지는 무엇인가요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">본문 내용(식용 곤충의 과제)과 전혀 무관하며, 출처와 단위가 빠져 있다.</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "설명 방법·서술 표현·시각 자료의 적절성을 판단하는 ‘3대 평가 준거’로 단서 점검하기",
            "tag": "Step 1 설명 방법·표현·시각자료 점검",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">평가 영역 및 준거</th>
                  <th style="width:39%;">[글 가] 점검 결과</th>
                  <th style="width:39%;">[글 나] 점검 결과</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">① 설명 방법의 적절성<br>(대상 특성·독자 이해)</td>
                  <td><span class="blank-slot"><span class="t-ans">정의, 분류</span></span>로 개념을 명확히 잡고, 소고기와 <span class="blank-slot"><span class="t-ans">비교·대조 및 수치</span></span>를 제시해 영양·환경 장점을 선명히 드러냄 (적절)</td>
                  <td>강남세브란스병원 환자식 <span class="blank-slot"><span class="t-ans">구체적 사례</span></span>와 거부감·가격이라는 <span class="blank-slot"><span class="t-ans">문제·해결 과제 분석</span></span>을 사용해 현황을 잘 보여 줌 (적절)</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">② 서술 표현의 객관성<br>(모호·과장·감정 배제)</td>
                  <td>공식 통계 수치를 바탕으로 끝까지 객관적이고 명확한 설명 어조를 유지함 (적절)</td>
                  <td>➍문단의 문장 <strong>( ㉠ )</strong>에 ‘어리석고 이기적인 사람’이라는 <span class="blank-slot"><span class="t-ans">주관적 감정·비난 표현</span></span>이 섞여 객관성을 해침 (<strong>부적절</strong>)</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">③ 시각 자료의 적절성<br>(본문 부합·유형·출처)</td>
                  <td><strong>[시각자료 1]</strong>: 수량 크기를 비교하는 <span class="blank-slot"><span class="t-ans">막대그래프</span></span>가 본문 ➋문단 수치와 일치하며 출처·단위가 명확함 (적절)</td>
                  <td><strong>[시각자료 2]</strong>: 본문과 무관한 ‘산업용 로봇’ 그래프이며 <span class="blank-slot"><span class="t-ans">출처와 단위</span></span>가 누락됨 (<strong>부적절 ➔ [2-수정안]으로 교체 필요</strong>)</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 발견한 [글 나]의 표현 오류와 시각 자료 결함을 ‘왜 부적절한지 ➔ 어떻게 고쳐야 하는지’ 대조하기",
        "activity_2": {
            "title": "[글 나]의 부적절한 서술 표현(㉠)과 시각 자료([시각자료 2]) 수정 설계도 완성하기",
            "tag": "Step 2 대상 특성·독자 기준 대조 평가",
            "body_html": """
            <div class="inference-row" style="grid-template-columns:1fr 16px 1.15fr; margin-bottom:2px;">
              <div class="inf-card c1">
                <div style="font-weight:800; color:#B03A2E; margin-bottom:2px;">❌ [결함 진단: 무엇이 왜 문제인가?]</div>
                <div>• <strong>표현 결함(㉠)</strong>: 소비자의 자연스러운 심리를 ‘이기적’이라고 비난하여 설명문의 <span class="blank-slot"><span class="t-ans">객관성과 중립성</span></span>을 훼손함</div>
                <div style="margin-top:2px;">• <strong>시각자료 결함([자료 2])</strong>: ➍문단은 ‘식용 곤충 섭취 걸림돌(거부감·가격)’을 설명하는데 엉뚱한 로봇 추세선을 넣었고, <span class="blank-slot"><span class="t-ans">출처·단위</span></span>도 없음</div>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <div style="font-weight:800; color:#196F3D; margin-bottom:2px;">⭕ [수정 대안: 어떻게 고쳐야 하는가?]</div>
                <div>• <strong>표현 수정안</strong>: 문장 (㉠)을 삭제하거나, 설문 통계 수치를 인용한 <span class="blank-slot"><span class="t-ans">객관적 사실 진술 문장</span></span>으로 교체함</div>
                <div style="margin-top:2px;">• <strong>시각자료 수정안</strong>: 본문 ➍문단의 ‘거부감(62.4%)과 비싼 가격(18.5%)’ 비율을 한눈에 보여 주는 농촌진흥청의 <span class="blank-slot"><span class="t-ans">[시각자료 2-수정안] 설문 원그래프</span></span>로 교체함</div>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 수정 설계도를 바탕으로 [글 나]의 ➍문단과 시각 자료를 완벽하게 고쳐 쓴 평가·대안문 작성하기",
        "activity_3": {
            "title": "평가 준거를 밝혀 [글 나]의 문제점을 지적하고, 수정 대안 문장 산출하기",
            "tag": "Step 3 비판적 평가 및 수정 대안 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>과제</strong>: `[평가 준거 명시] ➔ [문제점 지적] ➔ [구체적 수정 문장 및 도표 대안]`의 3요소를 갖추어 [글 나]의 ➍문단(㉠ 부분 및 시각자료)을 고쳐 써 보세요.</div>
              <span class="pencil-line">✏️ <strong>1. 평가 및 문제점 지적</strong>: <span class="t-ans">설명문은 객관적 사실과 본문에 부합하는 시각 자료를 제시해야 한다. 그러나 [글 나]의 문장 (㉠)은 주관적 비난을 담고 있고, [시각자료 2]는 본문과 무관한 로봇 그래프이며 출처가 없어 부적절하다.</span></span>
              <span class="pencil-line">✏️ <strong>2. (㉠)을 대체할 객관적 설명 문장 (수정안 그래프 수치 활용)</strong>: <span class="t-ans">실제로 농촌진흥청(2023)의 설문 조사 원그래프([시각자료 2-수정안])를 보면, 소비자가 식용 곤충을 구매하지 않는 이유로 ‘생김새 거부감(62.4%)’과 ‘비싼 가격(18.5%)’이 가장 높은 비율을 차지했다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "15차시(W4 초고 집필)·16차시(W5 표현·도표 퇴고 루브릭) 직결",
            "prompt": "내가 쓸 설명문에 넣을 시각 자료의 유형(크기 비교=막대그래프 / 비율=원그래프 / 시간 추세=꺾은선그래프)을 고르고, 반드시 챙겨야 할 표기 요소 3가지를 적어 보세요.",
            "placeholder": "(예: 비율을 보여 주는 원그래프 선택 / 필수 표기: 그래프 제목, 단위(%), 정확한 출처)",
            "example_answer": "유형: 원인별 비율을 한눈에 보여 주는 원그래프 / 필수 표기 3요소: ① 그래프 제목, ② 수치 단위(%, 명), ③ 공신력 있는 조사 기관과 연도(출처)",
        },
        "self_check": [
            "대상의 특성과 독자의 이해를 돕기 위해 각 글이 선택한 설명 방법(정의·비교 vs 사례·문제분석)의 효과를 평가했나요?",
            "설명문의 객관성을 해치는 주관적·단정적 문장(㉠)을 정확히 찾아내어 객관적 진술로 고쳤나요?",
            "본문 내용과의 부합도, 그래프 유형, 단위·출처 유무를 기준으로 시각 자료의 적절성을 평가하고 대안을 제시했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 설명문 적절성 3대 평가 척도(V3-1): ① **설명 방법 적절성**(개념·수치 비교➔정의·비교·대조[글 가] vs 활용 현황·걸림돌➔사례·문제해결 분석[글 나]), ② **서술 어조 객관성**(감정·비난·과장 배제 ➔ ㉠ 삭제/교체), ③ **시각자료 적절성**(본문 정합성 + 그래프 유형[비교=막대/비율=원/추세=꺾은선] + 단위·출처 명시) / [우측 판서] 평가문 작성 3단 공식: `[평가 준거] ➔ [결함 지적] ➔ [수정 대안 제시]`.",
            "intro_5min": "이제부터는 필자가 써 놓은 설명문을 무조건 믿으며 읽는 단계를 넘어, ‘필자가 사용한 설명 방법과 그래프가 과연 적절한가?’를 매의 눈으로 심사하는 **평가적 읽기(9~11차시)** 단계입니다. 미래 식량 ‘식용 곤충’을 다룬 두 글을 심사위원이 되어 평가해 봅시다.",
            "ido_think_aloud_script": "“선생님이 심사위원이 되어 [글 가]를 먼저 평가해 볼게요. 첫째, 설명 방법을 볼까요? ‘식용 곤충’이라는 낯선 개념을 독자에게 알려 주려고 ➊문단에서 ‘정의’와 ‘분류(10종)’를 썼고, 영양과 친환경성을 설득력 있게 보여 주려고 ➋문단에서 소고기·돼지고기와 ‘비교·대조’하며 구체적 ‘수치(53g vs 21g)’를 제시했어요. 대상의 특성에 아주 잘 어울리는 방법이네요! 둘째, [시각자료 1]을 볼까요? 두 대상의 수량 크기를 견줄 때는 ‘막대그래프’가 가장 적절해요. 게다가 단위(g, kg)와 출처(농촌진흥청·FAO, 2022)까지 정확히 밝혀서 본문 ➋문단의 이해를 완벽하게 돕고 있습니다. 자, 그렇다면 [글 나]에는 어떤 훌륭한 점과 어떤 치명적인 실수가 숨어 있는지 함께 찾아볼까요?”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[글 나]의 ➌~➍문단이 식용 곤충의 활용 모습과 앞으로의 숙제를 설명하기 위해 선택한 주된 설명 방법 두 가지는 무엇이며, 어떤 효과가 있나요?",
                    "expected_ans": "➌문단에서는 강남세브란스병원 항암 환자식 임상 실험이라는 ‘구체적 사례’와 가공식품 ‘예시’를 들어 실제 활용 모습을 생생하게 보여 주었고, ➍문단에서는 심리적 거부감과 비싼 가격이라는 ‘문제·해결 과제 분석’ 방법을 써서 앞으로 보완할 점을 체계적으로 알렸습니다.",
                    "reprompt": "➌문단의 ‘실제로 강남세브란스병원~’ 부분과 ➍문단의 ‘해결해야 할 현실적인 과제~’ 부분에 쓰인 설명 방법을 확인해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "[글 나] ➍문단의 밑줄 친 문장 ( ㉠ )과 [시각자료 2]는 왜 부적절하며, 각각 어떻게 고쳐야 독자가 신뢰할 수 있는 좋은 설명문이 될까요?",
                    "expected_ans": "문장 ( ㉠ )은 곤충을 못 먹는 소비자를 ‘어리석고 이기적인 사람’이라고 비난하는 필자의 주관적 감정이 섞여 있으므로 삭제하거나 설문 통계 사실 문장으로 고쳐야 합니다. 또한 [시각자료 2]는 본문과 전혀 상관없는 로봇 그래프이고 출처·단위도 없으므로, 농촌진흥청의 ‘식용 곤충을 구매하지 않는 이유 설문 조사 원그래프([시각자료 2-수정안])’로 교체해야 합니다.",
                    "reprompt": "설명문에서 독자를 혼내거나 감정적으로 비난해도 될까요? 그리고 ‘거부감과 가격 문제의 비율’을 보여 주려면 로봇 그래프 대신 어떤 그래프를 넣어야 할지 [시각자료 2-수정안]을 살펴보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 3대 평가 준거 점검표를 채우고, [활동 2]에서 결함 진단과 수정 대안을 연결한 뒤, [활동 3]에서 문장 (㉠)과 [시각자료 2]를 결합해 수정한 객관적 설명 문장을 작성하도록 지도한다. 이 3대 준거가 15~16차시 자신의 설명문 쓰기·고쳐쓰기 채점 기준이 됨을 강조하며 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 날개 [We·You Do]</strong>: 1. <strong>객관적 사실 전달이 아니라 필자의 주관적인 비난과 감정적 편견이 담긴 표현이기 때문이다.</strong> / 2. <strong>본문 내용(식용 곤충의 과제)과 전혀 무관하며, 출처와 단위가 빠져 있다.</strong><br>
              <strong>2. [활동 1] 3대 준거 점검표</strong>: ① [글 가]: <strong>정의, 분류</strong>, <strong>비교·대조 및 수치</strong> / [글 나]: <strong>구체적 사례</strong>, <strong>문제·해결 과제 분석</strong> | ② [글 나]: <strong>주관적 감정·비난 표현</strong> | ③ [글 가]: <strong>막대그래프</strong> / [글 나]: <strong>출처와 단위</strong><br>
              <strong>3. [활동 2] 결함 진단 및 수정 설계</strong>: [결함] <strong>객관성과 중립성</strong>, <strong>출처·단위</strong> / [대안] <strong>객관적 사실 진술 문장</strong>, <strong>[시각자료 2-수정안] 설문 원그래프</strong><br>
              <strong>4. [활동 3] 평가 및 수정 대안 산출 (인정 답안 기준)</strong>: (1) 평가 준거(객관성, 본문-시각자료 부합성)와 문제점 지적 문장, (2) [시각자료 2-수정안]의 출처(농촌진흥청, 2023)와 수치(생김새 거부감 62.4%, 비싼 가격 18.5%)를 인용한 객관적 대체 문장을 모두 작성하면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "그래프가 들어 있기만 하면 본문 내용과 달라도 무조건 친절하고 좋은 설명문이라고 평가하는 오류",
                    "diagnosis": "시각 자료의 ‘존재 유무’만 확인하고 ‘본문 핵심 명제와의 내용적 정합성’ 및 ‘그래프 유형 적합성’을 따지지 않음.",
                    "prescription": "본문 문단의 중심 단어(‘소비자의 거부감과 가격 문제’)와 그래프의 제목(‘산업용 로봇 판매 대수’)이 일치하는지 반드시 1:1로 짝지어 확인하는 습관을 길러 준다.",
                },
                {
                    "error_case": "전체에서 각 항목이 차지하는 비율(거부감 62.4%, 가격 18.5%)을 보여 줄 때 ‘꺾은선그래프’가 가장 적절하다고 답하는 오류",
                    "diagnosis": "통계 그래프의 유형별 기능(크기 비교=막대 / 시간에 따른 변화 추세=꺾은선 / 전체에 대한 부분의 비율=원·띠)을 구분하지 못함.",
                    "prescription": "시간(연도·월)에 따라 변하는 값은 **꺾은선그래프**, 항목 간 수량 크기 비교는 **막대그래프**, 100% 전체 속 설문 응답 비율은 **원그래프(또는 띠그래프)**가 적합함을 명확히 정리해 준다.",
                },
            ],
            "scaffolding_down": "[활동 3]에서 대체 문장 작성을 어려워하는 학습자에게는 지시문 시작 틀(“실제로 농촌진흥청(2023)의 [시각자료 2-수정안]을 살펴보면, 소비자가 식용 곤충을 구매하지 않는 까닭은 ___이 ___%로 가장 높고, ___이 ___%로 뒤를 이었다.”)을 제공하여 수치를 넣어 완성하게 한다.",
            "scaffolding_up": "심화 학습자에게는 만약 막대그래프의 세로축 눈금 시작점을 `0`이 아니라 `18g`부터 시작하도록 왜곡해 그린다면 독자에게 어떤 착시(고소애가 소고기보다 2.5배가 아니라 10배 이상 많아 보이는 왜곡)를 일으킬지 비판적으로 분석하게 한다.",
            "rubric": {
                "high": "설명 방법, 서술 어조의 객관성, 시각 자료의 적절성 3대 준거를 정확히 적용하여 두 글을 평가하고, 부적절한 주관적 문장과 오류 도표를 대체할 객관적 설명 문장을 완벽히 산출함.",
                "mid": "[글 나]의 주관적 문장(㉠)과 엉뚱한 그래프([시각자료 2])가 부적절하다는 점은 찾아냈으나, 수정 대안 문장에서 설문 원그래프의 구체적 수치나 출처 표기가 일부 누락됨.",
                "low": "설명문의 객관적 진술과 주관적 비난 문장을 변별하지 못하거나, 본문과 시각 자료의 불일치를 찾아내는 데 어려움이 있음.",
            },
        },
    },

    # =========================================================================
    # 10차시: G6-EXP-V3-2 정보의 정확성·객관성·출처 신뢰성 및 관점 공정성 평가
    # 제재: [글 가] 공공 연구·안전 기관 보고서 (농촌진흥청·식약처 공식 통계 및 주의점 균형 서술)
    #       vs [글 나] 상업적 쇼핑몰 홍보 게시물 (출처 불명·과장 수식어·알레르기 단점 은폐 대조문)
    # =========================================================================
    {
        "lesson_no": 10,
        "code": "G6-EXP-V3-2",
        "lesson_title": "정보의 정확성·출처 신뢰성·서술 객관성·관점 공정성 평가하기",
        "std_badge": "[6국02-04] · [6국02-05] · CCSS RI.6.8 · PISA",
        "student_goal": "동일한 대상을 설명한 두 매체 자료를 ‘정확성·최신성, 출처 공신력, 서술 객관성, 관점 공정성’의 4대 준거로 비교 평가하고, 편향된 글을 객관적이고 공정한 설명문으로 고쳐 쓸 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "공신력 있는 출처·연구 기관 및 정확한 검증 수치"],
            ["mk-line-blue", "파란 밑줄", "장점뿐만 아니라 주의점·한계까지 균형 있게 다룬 공정한 서술"],
            ["mk-line-red", "빨간 밑줄", "상업적 이해관계·출처 불명·과장·단점 은폐(편향) 표현"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 정보 신뢰성·공정성 팩트체크: [글 가] 공공기관 공식 보고서 vs [글 나] 상업 홍보 블로그</span>
          <span style="font-size:6.7pt; color:#566573;">평가 기준: ① 정확성·최신성 ② 출처 공신력 ③ 서술 객관성 ④ 관점 공정성(균형성)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 비교 정독 (두 글의 출처, 통계 근거, 어조, 장단점 균형 여부를 따지며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 4대 준거 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#1A5276; margin-bottom:2px;">[글 가] 식용 곤충 ‘고소애’의 영양 성분 특성과 섭취 시 안전 관리 지침</div>
                <div style="font-family:var(--font-sans); font-size:6.8pt; color:#1B4F72; margin-bottom:2px;">• 작성 출처: <span class="mk-person">농촌진흥청 국립농업과학원 · 식품의약품안전처 『식용 곤충 영양 및 안전성 보고서』(2024년 발표)</span></div>
                <p><span class="p-num">➊</span> 식품의약품안전처가 일반 식품 원료로 인정한 갈색거저리 유충(애칭 ‘고소애’)은 단백질과 불포화 지방산이 풍부한 식재료이다. <span class="mk-person">농촌진흥청 국립농업과학원의 2024년 영양 성분 표준 분석 결과</span>에 따르면, 건조 고소애 100그램당 단백질은 평균 53그램, 지방은 약 31그램이 함유되어 있으며, 전체 지방 중 혈관 건강에 유익한 불포화 지방산의 비율이 약 75퍼센트를 차지한다. 또한 <span class="mk-person">강남세브란스병원 임상연구팀이 수술 환자 109명을 대상으로 8주간 연구한 결과</span>, 고소애 환자식을 섭취한 집단은 일반 환자식 집단에 비해 골격근량과 면역 세포 수치가 유의미하게 개선된 것으로 확인되었다.</p>
                <p><span class="p-num">➋</span> <span class="mk-line-blue">그러나 식용 곤충은 모든 사람에게 무조건 안전한 만능 식품이 아니므로 섭취 시 주의해야 할 점도 명확히 알아야 한다.</span> 곤충의 겉껍질을 이루는 ‘키틴(Chitin)’ 성분은 새우, 게, 가재 같은 갑각류의 껍질 성분과 구조가 매우 비슷하다. <span class="mk-line-blue">식품의약품안전처의 알레르기 유발 물질 관리 지침에 따르면, 평소 새우나 게에 알레르기가 있는 사람이 식용 곤충을 섭취할 경우 교차 반응으로 인해 피부 두드러기, 가려움증, 심하면 호흡 곤란 같은 알레르기 증상이 나타날 수 있다.</span> 따라서 소비자는 제품 포장지의 원재료명과 알레르기 주의 표시를 반드시 확인하고 자신의 체질에 맞게 적정량을 섭취해야 한다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님과 신뢰성 심사하기</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>[글 가]를 믿을 수 있는 좋은 설명문이라고 평가할 수 있는 근거 4가지는 무엇일까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>① <strong>출처 공신력</strong>: 농촌진흥청·식약처라는 국가 공인 연구·안전 기관(2024년 최신 자료)이야. ② <strong>정확성</strong>: 실험 대상(환자 109명, 8주)과 수치가 정확해. ③ <strong>객관성</strong>: 과장 없는 침착한 어조야. ④ <strong>공정성</strong>: ➊문단의 영양 장점뿐만 아니라 ➋문단에서 ‘갑각류 알레르기 주의점’까지 균형 있게 다루었어!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>4대 평가 준거를 모두 통과한 신뢰도 최상(★★★)의 글이구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:8pt; font-weight:800; color:#B03A2E; margin-bottom:2px;">[글 나] 먹기만 해도 모든 병이 낫는 기적의 슈퍼 푸드 고소애! 부작용은 0%!</div>
                <div style="font-family:var(--font-sans); font-size:6.8pt; color:#B03A2E; margin-bottom:2px;">• 작성 출처: <span class="mk-line-red">‘천하무적 곤충 건강원’ 인터넷 쇼핑몰 상품 홍보 게시판 (2015년 소문 인용)</span></div>
                <p><span class="p-num">➌</span> 아직도 몸에 해로운 소고기나 돼지고기를 드시나요? 이제 인류를 구원할 <span class="mk-line-red">우주 최고의 기적의 영약</span>, ‘슈퍼 고소애 분말’을 만나 보세요! <span class="mk-line-red">옛날에 어느 유명한 박사님이 말씀하시기를,</span> 고소애에는 단백질이 소고기보다 수십 배나 많이 들어 있어서 <span class="mk-line-red">하루에 한 숟가락만 먹어도 세상 모든 질병이 100퍼센트 씻은 듯이 낫는다고 합니다.</span> 실제로 지난주에 <span class="mk-line-red">저희 쇼핑몰에서 고소애 가루를 사 먹은 한 초등학생 고객은 단 일주일 만에 키가 10센티미터나 훌쩍 크고 달리기 1등을 했다는 놀라운 후기</span>를 남겨 주었습니다.</p>
                <p><span class="p-num">➍</span> 게다가 고소애는 깨끗한 자연에서 자란 곤충이기 때문에 <span class="mk-line-red">어린이나 노약자, 알레르기가 심한 환자 등 그 누구에게나 부작용이 단 0퍼센트도 없는 완벽하고 절대적으로 안전한 식품입니다.</span> 복잡한 성분 표시는 전혀 읽어 볼 필요가 없으며, 많이 먹으면 먹을수록 무조건 건강해집니다. 지금 바로 저희 쇼핑몰에서 할인가로 주문하세요!</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>🤝 짝·스스로 팩트체크</span><span class="role-chip">We·You Do</span></div>
                  <div>1. [글 나]의 작성자는 왜 고소애의 장점은 부풀리고 알레르기 부작용은 ‘0%’라고 거짓말을 했을까요? (<strong>출처의 이해관계</strong>)</div>
                  <span class="pencil-line">✏️ <span class="t-ans">자신의 쇼핑몰에서 파는 고소애 상품을 많이 팔아 이익을 얻으려는 상업적 의도가 있기 때문이다.</span></span>
                  <div style="margin-top:3px;">2. [글 가]의 사실을 근거로 [글 나]의 ‘단백질이 소고기보다 수십 배 많다’와 ‘부작용이 0%이다’를 반박해 보세요.</div>
                  <span class="pencil-line">✏️ <span class="t-ans">단백질은 수십 배가 아니라 약 2.5배(53g vs 21g)이며, 갑각류 알레르기 반응이 일어날 수 있다.</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "설명문·매체 신뢰성 평가를 위한 ‘4대 준거’로 [글 가]와 [글 나]의 단서 비교하기",
            "tag": "Step 1 정확성·공신력·객관성·공정성 단서 탐지",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:21%;">4대 평가 준거</th>
                  <th style="width:39%;">[글 가] 검증 결과 (신뢰도: ★★★)</th>
                  <th style="width:40%;">[글 나] 검증 결과 (신뢰도: ★☆☆ - 위험)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">① 정보의 정확성<br>및 최신성</td>
                  <td>2024년 최신 표준 분석 수치(단백질 53g, 불포화 지방산 75%)와 임상 조건(환자 109명, 8주)이 <span class="blank-slot"><span class="t-ans">교차 확인 가능하고 정확함</span></span></td>
                  <td>2015년 옛 소문을 인용했고, ‘단백질 수십 배, 모든 병 100% 완치, 일주일 만에 키 10cm 성장’ 등 <span class="blank-slot"><span class="t-ans">거짓·과장 수치와 성급한 일반화</span></span>를 범함</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">② 출처의 공신력<br>(전문성·이해관계)</td>
                  <td><span class="blank-slot"><span class="t-ans">농촌진흥청·식품의약품안전처</span></span> 등 상업적 이익과 무관한 국가 공인 전문 기관임</td>
                  <td>물건을 팔아 이익을 얻으려는 <span class="blank-slot"><span class="t-ans">상업적 쇼핑몰 홍보 게시판</span></span>이며 ‘어느 유명한 박사님’처럼 출처가 불분명함</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">③ 서술의 객관성<br>(감정·과장 배제)</td>
                  <td>감정적 수식어 없이 실험 결과와 안전 지침을 중립적·공식적 어조로 서술함</td>
                  <td>‘우주 최고의 기적의 영약, 100%, 절대적으로’ 등 <span class="blank-slot"><span class="t-ans">과장·단정적 수식어</span></span>를 남발함</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">④ 관점의 공정성<br>(장단점 균형 제시)</td>
                  <td>영양·면역 장점(➊문단)과 <span class="blank-slot"><span class="t-ans">갑각류 알레르기 유발 주의점(➋문단)</span></span>을 균형 있게 제시함</td>
                  <td>상품 판매에 유리한 장점만 부풀려 고르고(Cherry-picking), <span class="blank-slot"><span class="t-ans">알레르기 위험성은 ‘부작용 0%’라며 고의로 은폐·왜곡</span></span>함</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 4대 준거 분석을 바탕으로 [글 나]가 독자를 속이는 ‘왜곡·편향 메커니즘’ 진단하기",
        "activity_2": {
            "title": "[글 나]에 사용된 3대 정보 왜곡 수법(과장·성급한 일반화·단점 은폐) 진단 도해 완성하기",
            "tag": "Step 2 왜곡·편향 메커니즘 매핑",
            "body_html": """
            <div class="inference-row" style="grid-template-columns:1fr 12px 1fr 12px 1fr; margin-bottom:0;">
              <div class="inf-card c1">
                <strong style="color:#B03A2E;">[왜곡 수법 ①: 출처 불명 &amp; 수치 과장]</strong><br>
                • 본문: “어느 박사님이 소고기보다 수십 배 많고 모든 병이 100% 낫는다고 함”<br>
                • 진단: 정확한 기관명 없이 <span class="blank-slot"><span class="t-ans">약 2.5배(53g vs 21g)를 ‘수십 배’로 부풀림</span></span>
              </div>
              <div class="inf-symbol">+</div>
              <div class="inf-card c2">
                <strong style="color:#D35400;">[왜곡 수법 ②: 성급한 일반화 오류]</strong><br>
                • 본문: “고객 한 명이 일주일 만에 키가 10cm 컸음”<br>
                • 진단: 확인되지 않은 <span class="blank-slot"><span class="t-ans">극소수(1명)의 과장된 경험담을 전체의 효과인 것처럼 일반화</span></span>함
              </div>
              <div class="inf-symbol">+</div>
              <div class="inf-card c3">
                <strong style="color:#1A5276;">[왜곡 수법 ③: 불리한 정보 은폐(편향)]</strong><br>
                • 본문: “누구에게나 부작용이 0%인 완벽 식품”<br>
                • 진단: 판매에 불리한 <span class="blank-slot"><span class="t-ans">갑각류 알레르기 교차 반응 위험성</span></span>을 숨겨 소비자 안전을 위협함
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 진단한 왜곡·편향 부분들을 [글 가]의 공인 데이터를 활용해 객관적·공정한 설명문으로 다시 쓰기",
        "activity_3": {
            "title": "4대 평가 준거에 따라 [글 나]를 비판적으로 평가하고, 편향된 문단을 공정한 설명문으로 재작성하기",
            "tag": "Step 3 신뢰도 판정 및 중립적 설명문 재작성 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>1. [비판적 평가문]</strong> 4대 준거(정확성, 출처 공신력, 객관성, 공정성) 중 2가지 이상을 들어 왜 [글 나]보다 [글 가]를 신뢰해야 하는지 써 보세요.</div>
              <span class="pencil-line">✏️ <span class="t-ans">[글 나]는 상품 판매 목적의 쇼핑몰 글로 출처 공신력이 낮고 알레르기 위험을 은폐해 공정성이 떨어진다. 반면 [글 가]는 농촌진흥청과 식약처의 2024년 공식 통계를 바탕으로 영양 가치와 갑각류 알레르기 주의점을 균형 있게 설명하여 정확성과 공정성이 매우 높다.</span></span>
              <div style="margin-top:3px;"><strong>2. [객관적·공정한 재작성]</strong> [글 나]의 ➌~➍문단에서 과장·왜곡된 내용을 바로잡아 <strong>장점과 주의점이 균형을 이룬 객관적 설명문(2문장)</strong>으로 고쳐 써 보세요.</div>
              <span class="pencil-line">✏️ <span class="t-ans">농촌진흥청 분석에 따르면 말린 고소애 100g에는 소고기(21g)의 약 2.5배인 53g의 단백질과 풍부한 불포화 지방산이 들어 있어 환자의 면역 회복을 돕는다. 다만 곤충 껍질의 키틴 성분 때문에 갑각류 알레르기가 있는 사람에게는 두드러기나 호흡 곤란 같은 부작용이 나타날 수 있으므로 원재료 표시를 꼭 확인하고 섭취해야 한다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 다중 출처 신뢰성 검증)·16차시(W5 내용 공정성 퇴고) 직결",
            "prompt": "내가 쓸 설명문의 자료를 조사할 때 ‘피해야 할 출처’와 ‘찾아야 할 공신력 있는 출처’를 적고, 공정성을 위해 어떤 양면 정보를 담을지 씨앗을 남겨 보세요.",
            "placeholder": "(예: 익명 블로그·쇼핑몰 제외 ➔ 기상청·국립생태원 공식 통계 활용 / 장점과 한계점을 함께 제시)",
            "example_answer": "공신력 있는 출처: 국립환경과학원·한국소비자원 공식 보고서 (익명 인터넷 글·광고 블로그 배제) / 공정성 확보: 기술의 편리함(장점)뿐만 아니라 초기 비용이나 안전 주의점(한계)도 균형 있게 서술하기",
        },
        "self_check": [
            "정보의 사실적 정확성·최신성과 출처의 공신력(상업적 이해관계 유무)을 기준으로 두 글을 비교했나요?",
            "과장·단정적 수식어(‘100%, 기적의, 0%’)와 성급한 일반화 오류를 정확히 찾아냈나요?",
            "유리한 정보만 골라내고 불리한 주의점을 숨긴 편향된 글을 장단점이 균형을 이룬 공정한 설명문으로 고쳐 썼나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 설명 텍스트 신뢰성 평가 4대 준거(V3-2): ① **정확성·최신성**(교차 확인 가능 수치·최근 연도 vs 거짓 과장·성급한 일반화), ② **출처 공신력**(국가 연구기관·학술지 vs 상업적 이해관계 쇼핑몰·익명 블로그), ③ **서술 객관성**(중립적 어조 vs ‘기적의, 100%, 절대적’ 과장 수식어), ④ **관점 공정성**(장점+주의점 균형 제시 vs 유리한 정보만 선별[Cherry-picking]·위험 은폐) / [우측 판서] 편향문 ➔ 공정문 재작성 공식.",
            "intro_5min": "인터넷이나 유튜브에서 건강식품이나 과학 정보를 검색해 보면 “먹기만 하면 모든 병이 100% 낫는다, 부작용은 0%다!”라는 글을 흔히 볼 수 있습니다. 과연 이런 설명을 그대로 믿어도 될까요? 오늘 10차시에서는 가짜·편향 정보를 가려내는 ‘4대 평가 준거’를 배웁니다.",
            "ido_think_aloud_script": "“선생님이 [글 가]와 [글 나]를 놓고 4대 팩트체크 돋보기로 비교해 볼게요. 첫째 돋보기는 ‘출처의 공신력과 이해관계’예요! [글 가]는 농촌진흥청과 식품의약품안전처라는 국가 공인 연구·안전 기관이 2024년에 발표한 보고서예요. 물건을 팔아 돈을 벌려는 목적이 없죠. 반면 [글 나]는 어디서 쓴 글인가요? ‘천하무적 곤충 건강원 쇼핑몰 홍보 게시판’이에요! 물건을 많이 팔아야 돈을 버는 상업적 이해관계가 얽혀 있어요. 둘째 돋보기는 ‘관점의 공정성(균형성)’이에요! [글 가]는 ➊문단에서 단백질과 면역 회복 효과를 설명한 뒤, ➋문단에서 ‘그러나 새우·게 같은 갑각류 알레르기가 있는 사람은 두드러기나 호흡 곤란이 올 수 있다’고 주의점까지 솔직하고 공정하게 알려 주었어요. 반면에 [글 나]는 물건을 팔려고 알레르기 위험을 쏙 빼놓은 채 ‘부작용 0%!’라고 거짓말을 했네요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[글 가]에서는 고소애의 효과를 증명하기 위해 ‘수술 환자 109명을 대상으로 8주간 임상 연구한 결과’를 제시했는데, [글 나]는 어떤 근거를 제시했나요? 왜 [글 나]의 근거는 믿기 어려울까요?",
                    "expected_ans": "[글 나]는 ‘어느 유명한 박사님 말씀’과 ‘쇼핑몰에서 사 먹은 초등학생 1명이 일주일 만에 키가 10cm 컸다는 후기’를 제시했습니다. 박사님의 이름과 연구 출처가 불분명하고, 확인되지 않은 단 1명의 극단적 사례를 모든 사람에게 일어나는 효과인 것처럼 부풀리는 ‘성급한 일반화 오류’를 범했기 때문에 믿을 수 없습니다.",
                    "reprompt": "109명을 8주 동안 병원에서 정밀 측정한 결과와, 이름도 모르는 고객 1명이 일주일 만에 10cm 컸다는 쇼핑몰 후기 중 어느 것이 과학적으로 검증된 정확한 정보인지 비교해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "[글 나]에서 설명문의 ‘서술 객관성’을 떨어뜨리는 과장·단정적 표현들을 모두 찾아 동그라미 쳐 볼까요? 이런 말들이 들어가면 왜 오히려 신뢰도가 떨어질까요?",
                    "expected_ans": "‘우주 최고의 기적의 영약’, ‘수십 배’, ‘세상 모든 질병이 100% 씻은 듯이’, ‘부작용이 단 0%도 없는 완벽하고 절대적으로 안전한’ 등의 표현입니다. 과학적 사실에는 예외 조건과 한계가 있기 마련인데 ‘100%, 0%, 모든, 무조건’처럼 단정하고 과장하면 독자를 현혹하려는 광고성 글로 보이게 됩니다.",
                    "reprompt": "➌~➍문단에서 숫자가 극단적이거나(‘100%, 0%’) 감정을 들뜨게 만드는 화려한 꾸밈말들을 찾아보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 4대 평가 준거 비교표를 완성하고, [활동 2]에서 [글 나]의 3대 왜곡 메커니즘을 진단한 뒤, [활동 3]에서 비판적 평가문과 함께 [글 나]를 대체할 객관적·공정한 2문장 설명문을 작성하도록 지도한다. 13차시(W2 자료 수집)에서 인터넷 자료를 고를 때 이 4대 준거를 그대로 적용할 것임을 안내하며 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 날개 [We·You Do]</strong>: 1. <strong>자신의 쇼핑몰에서 파는 상품을 많이 팔아 경제적 이익을 얻으려는 상업적 이해관계가 있기 때문이다.</strong> / 2. <strong>단백질은 수십 배가 아니라 약 2.5배(53g vs 21g)이며, 키틴 성분 때문에 갑각류 알레르기 부작용이 일어날 수 있다.</strong><br>
              <strong>2. [활동 1] 4대 평가 준거 점검</strong>: ① <strong>교차 확인 가능하고 정확함</strong> vs <strong>거짓·과장 수치와 성급한 일반화</strong> / ② <strong>농촌진흥청·식품의약품안전처</strong> vs <strong>상업적 쇼핑몰 홍보 게시판</strong> / ③ <strong>과장·단정적 수식어</strong> / ④ <strong>갑각류 알레르기 유발 주의점(➋문단)</strong> vs <strong>알레르기 위험성은 ‘부작용 0%’라며 고의로 은폐·왜곡</strong><br>
              <strong>3. [활동 2] 3대 왜곡 메커니즘</strong>: ① <strong>약 2.5배(53g vs 21g)를 ‘수십 배’로 부풀림</strong> / ② <strong>극소수(1명)의 과장된 경험담을 전체의 효과인 것처럼 일반화</strong> / ③ <strong>갑각류 알레르기 교차 반응 위험성</strong><br>
              <strong>4. [활동 3] 평가문 및 공정한 재작성 (인정 답안 기준)</strong>: 1번 평가문에 4대 준거 중 2가지 이상(출처의 상업적 이해관계 vs 공인 기관, 과장 vs 정확한 수치, 알레르기 주의점 은폐 vs 균형 제시)이 포함될 것. 2번 재작성문에 (1) 정확한 영양 수치/출처, (2) 갑각류 알레르기 주의점, (3) 중립적 어조가 모두 갖추어지면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "[글 나]에 ‘100%, 0%, 10센티미터’처럼 숫자가 들어 있다는 이유만으로 “구체적 수치를 제시했으니 정확하고 객관적인 글이다”라고 잘못 평가하는 오류",
                    "diagnosis": "숫자의 ‘제시 여부’와 그 숫자의 ‘사실적 검증 가능성·출처 신뢰성’을 구분하지 못하는 표면적 수치 맹신.",
                    "prescription": "숫자가 적혀 있다고 다 진짜 통계가 아님을 강조하고, 반드시 “누가(공인 기관인가?), 어떻게(실험 표본과 방법이 있는가?), 다른 공신력 있는 자료([글 가])와 일치하는가?”를 교차 확인하게 지도한다.",
                },
                {
                    "error_case": "설명할 대상의 좋은 점만 잔뜩 써야 독자가 대상에 대해 잘 알게 된다고 생각하여 단점이나 주의점을 빼버리는 오류",
                    "diagnosis": "대상을 있는 그대로 균형 있게 설명하는 ‘설명문의 공정성’과 대상을 홍보·판매하는 ‘광고문의 설득 전략’을 혼동함.",
                    "prescription": "좋은 설명문은 독자가 올바른 판단을 내릴 수 있도록 대상의 장점(효능)과 한계·주의점(알레르기·비용 등)을 숨김없이 양면으로 보여 주는 ‘관점의 공정성’을 갖추어야 함을 주지시킨다.",
                },
            ],
            "scaffolding_down": "[활동 3]의 2번 공정한 재작성을 어려워하는 학습자에게는 ‘양면 균형 접속틀’(“농촌진흥청에 따르면 고소애는 ___이라는 장점이 있다. 그러나 식약처 지침에 따르면 ___이라는 주의점도 있으므로 ___해야 한다.”)을 제공하여 [글 가]의 핵심 사실을 채워 넣게 한다.",
            "scaffolding_up": "심화 학습자에게는 자신이 평소 유튜브나 인터넷에서 본 ‘과장되거나 출처가 의심스러운 과학·건강 정보’ 사례를 하나 떠올려 4대 준거 체크리스트로 신뢰도 별점을 매기고 팩트체크 계획을 세워 보게 한다.",
            "rubric": {
                "high": "정확성·최신성, 출처 공신력(상업적 이해관계 유무), 서술 객관성, 관점 공정성의 4대 준거를 모두 적용하여 두 글을 정밀하게 비교 평가하고, 편향된 문단을 장단점이 균형 잡힌 객관적 설명문으로 완벽히 재작성함.",
                "mid": "4대 준거 중 2~3가지를 활용해 [글 나]의 문제점을 찾아냈으나, 재작성한 설명문에서 구체적인 공인 출처 표기나 주의점 서술이 다소 간략함.",
                "low": "[글 나]의 과장된 홍보 표현에 끌리거나, 출처의 상업적 의도와 정보 은폐(불공정성)를 비판적으로 가려내는 데 어려움이 있음.",
            },
        },
    },

    # =========================================================================
    # 11차시: G6-EXP-V3-3 다중 설명 자료 교차 검증 및 지식 재구성 (GRR Level 4 You Do 독립 읽기)
    # 제재: 인공지능 미래 농업 ‘스마트 팜’ 3종 다중 매체 세트
    #       (① 사이언스올 인쇄 설명문 + ② 농식품부·농진청 통계 인포그래픽[생산량 +32.1%, 노동시간 -15.8%]
    #        + ③ 농진청 현장 영상 자막) + 코넬식 자율 독서 체크리스트 날개
    # =========================================================================
    {
        "lesson_no": 11,
        "code": "G6-EXP-V3-3",
        "lesson_title": "[독립 읽기] 다중 매체 자료를 교차 검증하여 통합 지식 보고서 쓰기",
        "std_badge": "[6국02-05] · [6국05-02] · CCSS RI.6.9 · PISA 다중문서 통합",
        "student_goal": "선생님의 도움 없이 스스로 1~10차시 읽기 전략을 총동원하여, ‘스마트 팜’을 다룬 3종 다중 매체(인쇄 설명문·통계 인포그래픽·영상 자막)의 공통 사실·고유 정보·상충 수치를 교차 검증하고 통합 지식 보고서를 작성할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "3종 매체에 공통으로 등장하는 핵심 개념·구성 요소"],
            ["mk-line-blue", "파란 밑줄", "각 매체만이 제공하는 고유한 보완 정보(원리·통계·현장 과제)"],
            ["mk-line-red", "빨간 밑줄", "매체 간 수치가 달라 교차 검증(원인 분석)이 필요한 부분"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>📖 [스스로 읽기 You Do] 인공지능 미래 농업 ‘스마트 팜’ 3종 다중 매체 세트</span>
          <span style="font-size:6.7pt; color:#566573;">출처: 한국과학창의재단 사이언스올 · 농림축산식품부 · 농촌진흥청</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>3종 다중 매체 정독 (스스로 밑줄 긋고 교차 검증하며 읽기)</th>
              <th class="wing-head">📋 코넬식 자율 독서 체크리스트 (You Do)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="font-family:var(--font-sans); font-size:7.9pt; font-weight:800; color:#1A5276; margin-bottom:1.5px;">[매체 ① 인쇄 설명문] 농업과 첨단 정보통신기술의 만남, ‘스마트 팜(지능형 농장)’ (사이언스올 과학백과사전)</div>
                <p><span class="p-num">➊</span> 오늘날 우리 농촌은 농업 인구의 <span class="mk-person">고령화(高齡化)</span>로 인한 일손 부족과 이상 기후로 인한 농작물 피해라는 이중의 문제에 놓여 있다. 이 문제를 해결하기 위해 등장한 미래형 농업 기술이 바로 ‘<span class="mk-person">스마트 팜(지능형 농장)</span>’이다. 스마트 팜이란 유리 온실이나 비닐하우스, 축사 등에 사물인터넷(IoT), 빅데이터, 인공지능(AI) 같은 정보통신기술을 결합하여 농작물이 자라는 환경을 원격·자동으로 측정하고 <span class="mk-person">최적화(最適化)</span>하여 관리하는 농장을 말한다.</p>
                <p><span class="p-num">➋</span> 스마트 팜의 시스템은 역할에 따라 크게 <span class="mk-line-blue">‘감지부’, ‘판단부’, ‘작동부’라는 세 부분으로 이루어져 있다.</span> 먼저 <span class="mk-person">감지부</span>에 속하는 온습도 센서, 토양 수분 센서, 일조량 센서는 온실 내부의 온도와 습도, 흙 속 수분량, 이산화 탄소 농도를 실시간으로 측정한다. 그다음 수집된 정보는 두뇌 역할을 하는 <span class="mk-person">판단부(인공지능 통합 제어기)</span>로 전송된다. 판단부의 인공지능은 미리 입력된 작물별 생육 빅데이터와 현재 온실 상태를 비교하여 무엇이 부족한지 스스로 분석한다. 마지막으로 판단부가 명령을 내리면 <span class="mk-person">작동부</span>의 자동 개폐기와 냉난방기, 양액(영양분) 공급 장치가 움직여 천장 창문을 열거나 물과 영양분을 알맞게 공급한다.</p>

                <div style="background:#EBF5FB; border:0.8pt solid #5DADE2; border-radius:4px; padding:4px 6px; margin:4px 0; font-family:var(--font-sans); font-size:7pt; line-height:1.38;">
                  <div style="font-weight:800; color:#1A5276;">📊 [매체 ② 공공기관 통계 인포그래픽] 스마트 팜 3단계 순환 구조 및 도입 성과 통계</div>
                  <div style="font-size:6.6pt; color:#566573; margin-bottom:2px;">• 조사·발표: 농림축산식품부 · 농촌진흥청 『전국 스마트 팜 도입 농가(1,200호) 성과 조사 보고서』(2024)</div>
                  <div>• <strong>[시각 구역 A: 작동 흐름도]</strong> <code>[1단계: 환경 감지 센서]</code> ➔ <code>[2단계: AI 통합 제어기]</code> ➔ <code>[3단계: 스마트폰 원격 제어 &amp; 자동 작동기]</code></div>
                  <div>• <strong>[시각 구역 B: 도입 전(100% 기준) 대비 도입 후 전국 평균 변화율 막대그래프]</strong><br>
                  &nbsp; ① <strong>농작물 생산량</strong>: 도입 전 100% ➔ 도입 후 <span class="mk-line-blue"><strong>132.1% (+32.1% 증가 ↑)</strong></span><br>
                  &nbsp; ② <strong>농업인 노동 시간</strong>: 도입 전 100% ➔ 도입 후 <span class="mk-line-red"><strong>84.2% (-15.8% 감소 ↓, 일평균 4.8시간➔4.0시간)</strong></span><br>
                  &nbsp; ③ <strong>물·비료 등 영농 비용</strong>: 도입 전 100% ➔ 도입 후 <span class="mk-line-blue"><strong>88.8% (-11.2% 절감 ↓)</strong></span></div>
                </div>

                <div style="font-family:var(--font-sans); font-size:7.9pt; font-weight:800; color:#196F3D; margin-bottom:1.5px;">🎬 [매체 ③ 현장 영상 자막] 〈첨단 농업의 현장, 인공지능 토마토 농장에 가다〉 (농촌진흥청 농업기술 영상)</div>
                <p><span class="p-num">➌</span> <strong>[장면 #1 / 00:15~00:40]</strong> <em>(화면: 눈보라가 치는 한겨울 바깥 풍경과 대조적으로 빨갛게 익은 방울토마토가 가득한 대형 유리 온실 내부. 벽면 디지털 온도계가 28.5℃를 가리키자, 윙 소리와 함께 천장 환기창이 자동으로 열리고 미세 물안개가 뿜어져 나온다.)</em><br>
                • <strong>해설자(자막)</strong>: “한겨울 추위 속에서도 이곳 온실의 토마토는 봄날처럼 자랍니다. 온실 안 온도가 토마토 생육 적정 기준치인 26도를 넘어서자, 인공지능 제어기가 스스로 천장 창문을 열고 물안개를 뿌려 온도를 낮추는 모습입니다.”</p>
                <p><span class="p-num">➍</span> <strong>[장면 #2 / 00:41~01:15]</strong> <em>(화면: 거실 소파에 앉아 스마트폰 앱으로 온실 내부 영상과 그래프를 확인하는 김OO 농장주 인터뷰)</em><br>
                • <strong>김OO 농장주(자막)</strong>: “예전에는 온실 온도를 맞추려고 밤새 농장을 떠나지 못했습니다. 하지만 스마트 팜을 설치한 뒤로는 집에서도 스마트폰으로 물을 줄 수 있어서 <span class="mk-line-red">제 느낌에는 온실에 매달려 일하는 시간이 예전보다 절반(약 50%) 가까이 확 줄어든 것 같습니다.</span> <span class="mk-line-blue">다만 처음 온실에 센서와 자동화 기계를 설치할 때 수천만 원에서 수억 원의 초기 비용이 들고, 나이 많은 어르신들이 복잡한 컴퓨터 프로그램을 다루기 어렵다는 점은 앞으로 꼭 해결해야 할 과제입니다.</span>”</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4" style="background:#FFFFFF; border:0.9pt solid #1A5276; border-left:3pt solid #1A5276;">
                  <div class="wing-box-title"><span>🧭 스스로 전략 점검표</span><span class="role-chip" style="background:#1A5276; color:#fff;">스스로 You Do</span></div>
                  <div style="font-size:7pt; line-height:1.38;">
                    <strong>□ 1. 구조·어휘 확인 (V1·V2)</strong><br>
                    • [매체 ①]에 쓰인 복합 설명 구조 3가지는?<br>
                    ➔ <span class="blank-slot"><span class="t-ans">문제·해결</span></span>(➊), <span class="blank-slot"><span class="t-ans">분석</span></span>(➋앞), <span class="blank-slot"><span class="t-ans">순서·인과</span></span>(➋뒤)<br>
                    • 파생 접미사 <code>-화(化)</code>가 붙은 학술어 2개는?<br>
                    ➔ <span class="blank-slot"><span class="t-ans">고령화, 최적화(자동화)</span></span>
                  </div>
                </div>
                <div class="wing-box question">
                  <div class="wing-box-title"><span>📝 코넬식 교차 검증 노트</span></div>
                  <div style="font-size:7pt; line-height:1.38;">
                    <strong>□ 2. 매체별 고유 정보 파악</strong><br>
                    • [매체 ②]에서만 알 수 있는 정량적 성과 수치는?<br>
                    <span class="pencil-line">✏️ <span class="t-ans">생산량 +32.1% 증가, 노동시간 -15.8% 감소, 영농비 -11.2% 절감</span></span>
                    <strong>□ 3. 상충 수치 팩트체크</strong><br>
                    • 노동 시간 감소폭이 [매체 ②](-15.8%)와 [매체 ③ 농장주 인터뷰](약 50% 감소)에서 다른 까닭은?<br>
                    <span class="pencil-line">✏️ <span class="t-ans">[매체 ②]는 전국 1,200호 농가의 객관적 평균 통계이고, [매체 ③]은 농장주 1명의 주관적 체감 표현이기 때문이다.</span></span>
                  </div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "3종 다중 매체(인쇄 설명문·인포그래픽·영상 자막)의 정보 깊이와 전달 특성 비교하기",
            "tag": "Step 1 다중 매체 메타데이터 및 고유 단서 추출",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">매체 구분</th>
                  <th style="width:24%;">출처 및 전달 방식</th>
                  <th style="width:32%;">이 매체가 제공하는 고유 핵심 정보</th>
                  <th style="width:26%;">매체의 강점과 한계</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">[매체 ①]<br>인쇄 설명문</td>
                  <td>사이언스올 과학백과사전<br>(문자 텍스트 중심)</td>
                  <td>스마트 팜의 등장 배경(고령화·이상기후), 개념 정의, <span class="blank-slot"><span class="t-ans">감지부·판단부·작동부</span></span>의 3대 구조와 작동 원리</td>
                  <td>• 강점: 개념과 원리를 논리적·체계적으로 깊이 설명함<br>• 한계: 구체적 성과 통계나 현장 모습은 알기 어려움</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">[매체 ②]<br>통계 인포그래픽</td>
                  <td>농림축산식품부·농촌진흥청 (2024, 도식+막대그래프)</td>
                  <td>도입 후 <span class="blank-slot"><span class="t-ans">생산량 32.1% 증가, 노동시간 15.8% 감소, 영농비 11.2% 절감</span></span>이라는 정량적 통계 수치</td>
                  <td>• 강점: 작동 흐름과 도입 효과를 한눈에 비교해 보여 줌<br>• 한계: 도입 과정의 현실적 어려움은 드러나지 않음</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">[매체 ③]<br>현장 영상 자막</td>
                  <td>농촌진흥청 농업기술 영상<br>(현장 화면+인터뷰 자막)</td>
                  <td>온실 창문 자동 개폐·물안개 분사 모습 및 <span class="blank-slot"><span class="t-ans">높은 초기 설치 비용과 고령층의 기기 조작 어려움(과제)</span></span></td>
                  <td>• 강점: 생생한 현장감과 실제 농가의 목소리를 전달함<br>• 한계: 인터뷰 대상자의 주관적 체감 수치가 섞일 수 있음</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 추출한 3종 매체의 정보를 교차 검증 매트릭스에 넣어 ‘일치 사실 · 보완 정보 · 상충 정보’ 해결하기",
        "activity_2": {
            "title": "다중 매체 교차 검증(Cross-check) 매트릭스로 정보 통합 및 수치 충돌 해결하기",
            "tag": "Step 2 교차 검증 및 상충 정보(Conflict) 규명",
            "body_html": """
            <div class="inference-row" style="grid-template-columns:1fr 12px 1fr 12px 1.15fr; margin-bottom:0;">
              <div class="inf-card c1">
                <strong style="color:#1A5276;">[1. 상호 일치 (사실 확정)]</strong><br>
                • 매체 ①·②·③ 공통 확인:<br>
                스마트 팜은 <span class="blank-slot"><span class="t-ans">감지 센서 ➔ 인공지능 제어기 ➔ 자동 작동기(원격 스마트폰)</span></span>의 3단계로 온실 환경을 자동 관리한다.
              </div>
              <div class="inf-symbol">+</div>
              <div class="inf-card c2">
                <strong style="color:#196F3D;">[2. 상호 보완 (지식 결합)]</strong><br>
                • [매체 ①·②]의 장점(원리·생산량 32.1%↑)에 [매체 ③]의 <span class="blank-slot"><span class="t-ans">현실적 한계(초기 설치비 부담, 고령 어르신의 프로그램 사용 어려움)</span></span>를 결합해야 공정한 이해가 된다.
              </div>
              <div class="inf-symbol">+</div>
              <div class="inf-card c3">
                <strong style="color:#B03A2E;">[3. 상충 정보 해결 (팩트체크)]</strong><br>
                • 충돌: 노동 시간 감소율(<strong>② -15.8%</strong> vs <strong>③ 약 50%</strong>)<br>
                • 해결: 보고서에 공식 수치로 인용할 때는 전국 1,200호 농가를 조사한 <span class="blank-slot"><span class="t-ans">[매체 ②]의 -15.8%(농식품부·농진청 통계)</span></span>를 채택해야 정확하다.
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 교차 검증된 핵심 지식을 ‘처음(정의·배경) - 가운데(구조·원리·효과) - 끝(과제·전망)’ 구조로 재구성하기",
        "activity_3": {
            "title": "3종 매체의 검증된 정보를 통합하여 1편의 완결된 ‘스마트 팜 종합 지식 보고문’ 작성하기",
            "tag": "Step 3 다중 매체 지식 재구성 산출 (You Do)",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>과제</strong>: [매체 ①·②·③]에서 교차 검증한 정보를 모두 통합하여, <strong>출처 명시</strong>와 <strong>처음-가운데-끝 구조</strong>를 갖춘 종합 요약 보고문(4~5문장)을 스스로 작성해 보세요.</div>
              <span class="pencil-line">✏️ <strong>[처음: 등장 배경과 정의]</strong> <span class="t-ans">스마트 팜은 농촌 인구의 고령화와 이상 기후 문제를 해결하기 위해 사물인터넷과 인공지능 기술로 농작물 생육 환경을 자동 최적화하는 지능형 농장이다.</span></span>
              <span class="pencil-line">✏️ <strong>[가운데: 구성 원리와 공식 통계 효과(출처 포함)]</strong> <span class="t-ans">스마트 팜은 환경 감지 센서(감지부), 인공지능 제어기(판단부), 자동 개폐기·양액기(작동부)의 3단계로 작동한다. 농림축산식품부와 농촌진흥청(2024) 통계에 따르면, 스마트 팜 도입 후 농작물 생산량은 32.1% 증가하고 노동 시간은 평균 15.8%, 영농 비용은 11.2% 감소하는 효과가 나타났다.</span></span>
              <span class="pencil-line">✏️ <strong>[끝: 해결 과제와 전망]</strong> <span class="t-ans">다만 높은 초기 설치 비용과 고령 농업인의 프로그램 조작 어려움이라는 한계가 남아 있으므로, 설치비 지원과 쉬운 사용자 교육이 함께 이루어진다면 미래 농업의 핵심 기술로 더욱 널리 확산될 것이다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "12차시(W1 계획하기)·13차시(W2 다중 출처 수집) 직접 연결",
            "prompt": "1~11차시 동안 모은 씨앗들과 오늘 읽은 다중 매체 주제 중, 다음 시간(12~16차시) ‘나만의 설명문 한 편 쓰기’에서 다룰 최종 탐구 주제를 정해 보세요.",
            "placeholder": "(예: 내가 선택한 최종 설명문 화제: 스마트 팜 / 산호초 백화 현상 / 우주 쓰레기 제거 기술 등)",
            "example_answer": "내가 선택한 최종 설명문 화제: 도시 열섬 현상의 발생 원인과 도심 속 ‘냉섬·투수성 블록’을 활용한 해결 방안 (예상 독자: 우리 학교 6학년 친구들)",
        },
        "self_check": [
            "선생님의 도움 없이 스스로 복합 구조(문제해결·분석·순서인과)와 학술 파생어(`고령화, 최적화`)를 파악했나요?",
            "3종 매체의 공통 사실과 고유 정보를 구분하고, 수치 차이(-15.8% vs 약 50%)의 원인을 출처 특성으로 규명했나요?",
            "검증된 핵심 정보와 출처를 통합하여 ‘처음-가운데-끝’ 구조를 갖춘 완결된 지식 보고문을 작성했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] GRR Level 4(You Do 독립 읽기) 다중 매체 통합 공식(Perfetti 문서 간 통합 표상): `[매체 ① 인쇄문: 정의·3대 분석 구조·작동 원리]` + `[매체 ② 인포그래픽: 농식품부·농진청 공인 통계(생산량 +32.1%, 노동시간 -15.8%, 비용 -11.2%)]` + `[매체 ③ 영상 자막: 현장 작동 사례 & 현실적 과제(초기 비용·디지털 격차)]` / [우측 판서] 상충 정보 해결 규칙: 전국 1,200호 공식 통계(-15.8%) vs 개인 인터뷰 체감 표현(약 50%) 변별.",
            "intro_5min": "오늘 11차시는 1차시부터 10차시까지 배운 설명문 읽기 전략(사실·추론·평가)을 선생님의 시범 없이 여러분 스스로 총동원해 보는 **‘독립적 읽기(You Do)’** 시간입니다. 좌측 날개의 ‘코넬식 자율 독서 체크리스트’를 나침반 삼아 ‘스마트 팜’ 3종 매체를 교차 검증해 봅시다.",
            "ido_think_aloud_script": "“(※ 11차시는 GRR Level 4 ‘You Do’ 독립 읽기 차시이므로 교사의 사전 시범 사고구술을 최소화하고, 학생의 자율적 코넬 노트 점검 과정을 촉진하는 메타인지 안내만 2분간 제공합니다.) 여러분, 오늘 좌측 페이지 날개에는 선생님의 사고구술 상자 대신 여러분이 직접 채우는 ‘🧭 스스로 전략 점검표’와 ‘📝 코넬식 교차 검증 노트’가 있습니다. 글을 읽으며 첫째, 2·3·4차시에서 배운 설명 구조(문제해결, 분석, 순서·인과)와 5차시 파생어(`-화`)를 스스로 표시해 보세요. 둘째, [매체 ②]의 공식 통계 수치와 [매체 ③] 농장주 인터뷰의 수치가 왜 다른지 10차시에서 배운 ‘출처 신뢰성·객관성’ 준거로 판정해 보세요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "(독립 읽기 후 상호 점검 발문) [매체 ①]의 ➋문단에서 설명한 ‘감지부-판단부-작동부’의 3부분은 [매체 ②]의 구조도와 [매체 ③]의 토마토 온실 장면에서 각각 어떻게 나타나나요?",
                    "expected_ans": "감지부는 [매체 ③]에서 온실 온도 28.5℃를 측정한 ‘디지털 온도 센서’이고, 판단부는 기준치(26℃)와 비교해 명령을 내린 ‘인공지능 제어기’이며, 작동부는 자동으로 열린 ‘천장 환기창과 물안개 분무기’입니다.",
                    "reprompt": "[매체 ①] ➋문단의 세 부분 이름과 [매체 ③] 장면 #1의 기계 장치들을 1:1로 짝지어 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "스마트 팜 도입 후 줄어든 노동 시간에 대해 [매체 ②]는 ‘15.8% 감소’라고 했고, [매체 ③]의 김OO 농장주는 ‘절반(약 50%) 가까이 줄어든 것 같다’고 했습니다. 내가 보고서를 쓸 때 어느 수치를 공식 근거로 삼아야 하며 그 까닭은 무엇인가요?",
                    "expected_ans": "[매체 ②]의 ‘평균 15.8% 감소(농림축산식품부·농촌진흥청, 2024)’ 수치를 공식 근거로 삼아야 합니다. [매체 ③]의 ‘약 50%’는 농장주 개인이 스마트폰 원격 제어의 편리함을 강조하며 말한 주관적 체감 표현(‘제 느낌에는 ~것 같습니다’)인 반면, [매체 ②]는 전국 1,200호 농가를 객관적으로 측정한 공인 통계이기 때문입니다.",
                    "reprompt": "[매체 ②]의 조사 대상(전국 1,200호 농가)과 [매체 ③] 농장주의 말투(‘제 느낌에는 ~것 같습니다’)를 비교해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 코넬식 자율 독서 날개와 우측 페이지 [활동 1]~[활동 3]을 독립적으로 완수하도록 시간을 충분히 부여하고 개별 피드백을 제공한다. [활동 3]의 ‘처음-가운데-끝 종합 지식 보고문’이 바로 다음 시간(12~16차시) 과정중심 설명문 쓰기의 완성 모델임을 확인하며 읽기 11차시 대장정을 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. 좌측 코넬식 자율 독서 날개</strong>: □1. 구조: <strong>문제·해결</strong>(➊), <strong>분석</strong>(➋앞), <strong>순서·인과</strong>(➋뒤) / 파생어: <strong>고령화, 최적화(자동화)</strong> | □2. <strong>생산량 +32.1% 증가, 노동시간 -15.8% 감소, 영농비 -11.2% 절감</strong> | □3. <strong>[매체 ②]는 전국 1,200호 농가의 객관적 평균 통계이고, [매체 ③]은 농장주 개인의 주관적 체감 표현이기 때문이다.</strong><br>
              <strong>2. [활동 1] 매체별 특성 비교</strong>: [매체 ①] <strong>감지부·판단부·작동부</strong> / [매체 ②] <strong>생산량 32.1% 증가, 노동시간 15.8% 감소, 영농비 11.2% 절감</strong> / [매체 ③] <strong>높은 초기 설치 비용과 고령층의 기기 조작 어려움(과제)</strong><br>
              <strong>3. [활동 2] 교차 검증 매트릭스</strong>: [1. 일치] <strong>감지 센서 ➔ 인공지능 제어기 ➔ 자동 작동기(원격 스마트폰)</strong> / [2. 보완] <strong>현실적 한계(초기 설치비 부담, 고령 어르신의 프로그램 사용 어려움)</strong> / [3. 상충 해결] <strong>[매체 ②]의 -15.8%(농식품부·농진청 통계)</strong><br>
              <strong>4. [활동 3] 종합 지식 보고문 산출 (인정 답안 기준)</strong>: (1) 처음: 등장 배경(고령화·이상기후) 및 스마트 팜 정의, (2) 가운데: 3대 구성 부분(감지·판단·작동)과 [매체 ②]의 공식 출처·통계 수치(생산량 +32.1%, 노동시간 -15.8% 등), (3) 끝: [매체 ③]의 현실적 과제(초기 비용·고령층 교육)와 전망이 객관적 어조로 모두 포함되면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "[매체 ③] 인터뷰의 ‘노동 시간 50% 감소’가 더 숫자가 크고 인상적이라는 이유로 공식 통계(-15.8%) 대신 채택하는 오류",
                    "diagnosis": "개인 인터뷰의 주관적 구술(‘제 느낌에는 ~같습니다’)과 공공기관의 대규모 표본 조사 통계의 증거 수준(Hierarchy of Evidence) 차이를 변별하지 못함.",
                    "prescription": "인터뷰 자료는 ‘현장감과 구체적 사례’를 얻는 데 유용하지만, 전체 평균 수치를 인용할 때는 반드시 표본 수(1,200호)와 조사 기관이 명시된 공식 통계([매체 ②])를 채택해야 함을 지도한다.",
                },
                {
                    "error_case": "통합 보고문을 작성할 때 [매체 ①]과 [매체 ②]의 장점만 요약하고 [매체 ③] 후반부의 ‘초기 비용·고령층 조작 어려움’ 과제를 빠뜨리는 오류",
                    "diagnosis": "다중 매체 통합 독해에서 각 매체의 고유한 보완 정보(특히 한계점·해결 과제)를 빠짐없이 아우르는 균형 감각이 부족함.",
                    "prescription": "10차시에서 배운 ‘관점의 공정성’을 상기시켜, 기술의 밝은 면(생산량 증가)과 보완할 과제(초기 비용·교육 문제)를 모두 담아야 완결된 통합 보고서가 됨을 피드백한다.",
                },
            ],
            "scaffolding_down": "독립 읽기(You Do) 과정에서 3종 매체의 정보를 한꺼번에 묶기 어려워하는 학습자에게는 매체 ①에는 ‘파란 별(★원리)’, 매체 ②에는 ‘초록 별(★통계)’, 매체 ③에는 ‘빨간 별(★과제)’ 스티커 표시를 먼저 한 뒤, [활동 3]의 처음-가운데-끝 줄에 별표 내용을 하나씩 옮겨 담게 안내한다.",
            "scaffolding_up": "심화 학습자에게는 우리 학교나 우리 동네에 스마트 팜 기술을 응용한다면 어디에 적용할 수 있을지(예: ‘학교 옥상 스마트 텃밭’, ‘교실 공기질·온습도 자동 제어 시스템’) 감지부-판단부-작동부 3단계로 창의적 설계안을 덧붙여 쓰게 한다.",
            "rubric": {
                "high": "교사의 도움 없이 스스로 3종 매체의 복합 구조·학술 어휘·고유 정보를 정확히 분석하고, 상충 수치(-15.8% vs 50%)의 원인을 규명하며, 출처와 장단점이 균형 있게 통합된 처음-가운데-끝 지식 보고문을 완벽히 작성함.",
                "mid": "3종 매체의 공통점과 고유 정보는 파악하여 보고문을 작성했으나, 수치 차이의 원인 설명이나 보고문 내 공식 출처(농식품부·농진청, 2024) 표기가 일부 생략됨.",
                "low": "3종 매체의 정보를 교차 비교하지 못하고 어느 한 매체의 내용만 단편적으로 요약하며, 상충하는 수치 정보를 변별하는 데 도움이 필요함.",
            },
        },
    },
]
