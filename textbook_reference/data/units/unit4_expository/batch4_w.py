# -*- coding: utf-8 -*-
"""
4단원: 설명문 (unit4_expository) — Batch 4 (12~16차시: W1 ~ W5 과정중심 쓰기 5단계)
읽기-쓰기 1:1 미러링 스튜디오, 2층 고행간 첨삭 줄공책(W5), 교사용 정답(.t-ans) 및 지도서 6대 모듈 완비
"""

BATCH4 = [
    # =========================================================================
    # 12차시: G6-EXP-W1 계획하기 (설명 목적·독자 분석·대상 및 주제 좁히기)
    # =========================================================================
    {
        "lesson_no": 12,
        "code": "G6-EXP-W1",
        "lesson_title": "[계획하기] 씨앗 보관함 소환 및 예상 독자·설명 주제 좁히기",
        "std_badge": "[6국03-01] · [6국03-02] · CCSS W.6.2, W.6.4",
        "student_goal": "1~11차시 읽기 씨앗 보관함에서 탐구 화제를 고르고, 예상 독자의 지식 수준과 설명 목적을 분석하여 ‘3단계 깔때기 기법’으로 주제를 좁히며 포괄적인 가제목을 세울 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "내가 선택한 핵심 설명 대상"],
            ["mk-bg", "초록 네모", "예상 독자의 특성(사전 지식 수준·궁금증)"],
            ["mk-highlight", "형광펜", "[핵심 대상] + [설명 측면 A·B]로 좁혀진 최종 주제·제목"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>🛠️ [쓰기 스튜디오 1단계: 계획하기] 1~11차시 읽기 씨앗 소환 &amp; 3단계 깔때기 주제 좁히기</span>
          <span style="font-size:6.7pt; color:#566573;">연계: 4차시(V1-4 제목 공식) · 8차시(V2-4 예상 독자·목적) · 11차시(V3-3 다매체 주제)</span>
        </div>

        <!-- 1. 읽기 씨앗 보관함 소환 뱅크 -->
        <div style="background:#EBF5FB; border:0.85pt solid #5DADE2; border-radius:5px; padding:5px 8px; margin-bottom:5px; font-size:7.2pt; line-height:1.4;">
          <div style="font-weight:800; color:#1A5276; margin-bottom:2px;">🌱 1단계: 1~11차시 [내 글 씨앗 보관함]에서 설명할 화제(글감) 소환하기</div>
          <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:5px;">
            <div style="background:#fff; border:0.6pt solid #BDC3C7; border-radius:4px; padding:3.5px 5px;">
              <strong style="color:#196F3D;">[클러스터 A: 생태계와 기후·환경]</strong><br>
              • 토양 분해자와 생태계 물질 순환(1~2차시)<br>
              • 도시 열섬 현상과 도심 속 냉섬(5차시)<br>
              • 산호초 백화 현상과 바다 생태계(6차시)<br>
              • 학교 급식실 잔반·미세 플라스틱 문제
            </div>
            <div style="background:#fff; border:0.6pt solid #BDC3C7; border-radius:4px; padding:3.5px 5px;">
              <strong style="color:#1A5276;">[클러스터 B: 인체·극지·일상 과학]</strong><br>
              • 사람의 눈 구조와 사진기 원리(2차시)<br>
              • 북극과 남극의 환경 비교(3차시)<br>
              • 물의 순환과 이상 기후 연쇄 반응(3차시)<br>
              • 자전거·악기·한옥의 과학적 구조
            </div>
            <div style="background:#fff; border:0.6pt solid #BDC3C7; border-radius:4px; padding:3.5px 5px;">
              <strong style="color:#B03A2E;">[클러스터 C: 우주·안전·미래 기술]</strong><br>
              • 우주 쓰레기와 청소 위성·태양 돛(4차시)<br>
              • 배터리 열폭주 원리와 안전 수칙(7~8차시)<br>
              • 미래 식량 식용 곤충의 명암(9~10차시)<br>
              • 인공지능 미래 농업 스마트 팜(11차시)
            </div>
          </div>
        </div>

        <!-- 2. 3단계 깔때기 기법(Funneling) 시범 모델 & 사고구술 -->
        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🔎 2단계: 포괄적인 화제를 ‘3단계 깔때기(Funneling)’로 좁히는 법</th>
              <th class="wing-head">🧠 사고구술 &amp; 계획 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.6pt; line-height:1.48;">
                <div style="background:#F8F9F9; border-left:3pt solid #B03A2E; padding:4px 7px; margin-bottom:4px;">
                  <strong>❌ 나쁜 주제 설정의 예 (너무 넓거나 모호함)</strong>: “나는 <strong>환경 오염</strong>에 대해 설명문을 쓸 거야.” 또는 “나는 <strong>인공지능</strong>의 모든 것을 다 설명할 거야.”<br>
                  ➔ <em>문제점: 범위가 책 한 권 분량만큼 너무 넓어서 5~6문단 안에 깊이 있고 정확한 정보를 담을 수 없음!</em>
                </div>
                <div style="background:#EAFAF1; border:0.8pt solid #58D68D; border-radius:5px; padding:5px 8px;">
                  <strong style="color:#145A32;">⭕ 3단계 깔때기(Funneling) 주제 좁히기 모델 예시</strong><br>
                  • <strong>[Lv.1 상위 대분류 분야]</strong>: 기후 변화와 도시 환경 문제 (너무 넓음)<br>
                  &nbsp; &nbsp; ⬇ <em>(구체적인 현상이나 대상으로 초점 좁히기)</em><br>
                  • <strong>[Lv.2 중위 핵심 설명 대상]</strong>: 여름철 도심 기온이 치솟는 <span class="mk-person">‘도시 열섬 현상’</span>과 학교·교실의 열기 문제<br>
                  &nbsp; &nbsp; ⬇ <em>(독자가 가장 궁금해하는 설명 측면 2가지 결합하기)</em><br>
                  • <strong>[Lv.3 최종 좁혀진 주제 &amp; 목표 제목]</strong>: <span class="mk-highlight">〈도시 열섬 현상이 발생하는 3가지 원인과 도심 속 ‘냉섬’·투수성 블록을 활용한 해결 방안〉</span>
                </div>
                <div style="margin-top:4px; background:#FFFDF9; border:0.75pt solid #F5B041; border-radius:4px; padding:4px 7px;">
                  <strong style="color:#D35400;">👥 3단계: 예상 독자 프로파일(Profile) 분석 (8차시 V2-4 역적용)</strong><br>
                  • <strong>예상 독자</strong>: <span class="mk-bg">우리 학교 5~6학년 친구들</span><br>
                  • <strong>독자의 사전 지식 &amp; 오개념</strong>: 여름에 도시가 덥다는 것은 알지만, 왜 아스팔트(‘불투수성 포장’) 때문에 밤에도 기온이 안 내려가는지 과학적 원리는 잘 모름.<br>
                  • <strong>독자 맞춤형 설명 전략</strong>: 한자 학술어(‘불투수성, 증산 작용, 냉섬’)가 나올 때 쉬운 뜻풀이와 일상 비유(‘거대한 가열판’)를 덧붙여 설명한다.
                </div>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님의 계획 시범</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>설명문을 쓰기 전에 왜 ‘예상 독자’를 먼저 분석하고 ‘주제’를 좁혀야 할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>8차시에서 보았듯 독자가 초등학생인지 전문가인지에 따라 단어 수준과 비유가 달라져. 또 주제를 ‘환경’처럼 넓게 잡으면 겉핥기 글이 돼 버려!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span><strong>[핵심 대상] + [설명 측면 A(원인/구조) · B(해결/효과)]</strong>까지 깔때기로 좁혀야 탄탄한 설명문을 쓸 수 있구나!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "잘된 작문 계획서와 보완이 필요한 작문 계획서 판별하기",
            "tag": "Step 1 독자·목적·주제 범위 진단",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:48%;">학생들의 설명문 작문 계획서 초안</th>
                  <th style="width:14%; text-align:center;">적절성</th>
                  <th style="width:38%;">진단 근거 및 수정 방향 (목적·독자·주제 범위)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>[지훈]</strong> • 주제: 우주의 모든 별과 행성의 역사<br>• 목적: 우주 쓰레기가 얼마나 무서운지 내 감상을 일기로 쓰기 위해</td>
                  <td style="text-align:center; font-weight:800; color:#B03A2E;">( <span class="blank-slot"><span class="t-ans">부적절</span></span> )</td>
                  <td>주제 범위가 지나치게 <span class="blank-slot"><span class="t-ans">넓고(광범위하고)</span></span>, 설명문의 목적은 개인 감상이 아니라 <span class="blank-slot"><span class="t-ans">객관적 정보·원리 전달</span></span>이어야 한다.</td>
                </tr>
                <tr>
                  <td><strong>[서연]</strong> • 주제: 우리 학교 급식실 음식물 쓰레기 발생 원인과 자율 배식대 해결 방안<br>• 예상 독자: 급식을 먹는 6학년 친구들 (설문 원그래프와 쉬운 용어 사용)</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;">( <span class="blank-slot"><span class="t-ans">적절</span></span> )</td>
                  <td>주제가 <strong>[핵심 대상]+[원인과 해결 방안]</strong>으로 명확히 <span class="blank-slot"><span class="t-ans">좁혀졌고</span></span>, 예상 독자 수준에 맞는 설명 전략이 구체적이다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 기준을 적용하여 내가 설명할 화제를 ‘3단계 깔때기 기법’으로 좁히기",
        "activity_2": {
            "title": "‘3단계 깔때기(Funneling)’ 도해조직자로 내 설명문의 주제 좁히기",
            "tag": "Step 2 3단계 깔때기 주제 구체화",
            "body_html": """
            <div class="inference-row" style="grid-template-columns:1fr 14px 1fr 14px 1.25fr; margin-bottom:0;">
              <div class="inf-card c1">
                <strong style="color:#1A5276;">[1단계: 상위 관심 분야]</strong><br>
                내가 관심 있는 큰 분야:<br>
                <span class="pencil-line">✏️ <span class="t-ans">학교 환경 보호와 자원 순환 (또는 해양 생태계와 기후 변화)</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:#196F3D;">[2단계: 중위 핵심 대상]</strong><br>
                그중 집중해서 설명할 구체적 대상:<br>
                <span class="pencil-line">✏️ <span class="t-ans">우리 학교 급식실의 음식물 쓰레기(잔반) 문제 (또는 산호초 백화 현상)</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#B03A2E;">[3단계: 최종 설명 측면 2~3가지]</strong><br>
                대상의 어떤 점(정의·원인·구조·해결)을 설명할 것인가:<br>
                <span class="pencil-line">✏️ <span class="t-ans">음식물 쓰레기의 정의, 발생 원인 2가지(과다 배식·편식), 해결 방안 2가지(자율 배식대·조리법 개선)</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 좁힌 주제와 예상 독자 분석을 결합하여 ‘나만의 설명문 작문 계획서’ 완성하기",
        "activity_3": {
            "title": "예상 독자 프로파일과 목표 제목을 갖춘 ‘복합 설명문 작문 계획서’ 산출하기",
            "tag": "Step 3 정밀 작문 계획서 산출",
            "body_html": """
            <table class="std-table">
              <tbody>
                <tr>
                  <th style="width:24%;">① 예상 독자 및 사전 지식</th>
                  <td style="width:76%;"><span class="pencil-line">✏️ 누구에게 쓰며, 독자는 무엇을 궁금해하나요?: <span class="t-ans">우리 학교 5~6학년 학생들 / 잔반이 왜 많이 나오는지 정확한 통계와 우리 스스로 실천할 수 있는 해결 방법을 궁금해한다.</span></span></td>
                </tr>
                <tr>
                  <th>② 집필 목적 및 어조</th>
                  <td><span class="pencil-line">✏️ 왜 이 설명문을 쓰며, 어떤 말투를 쓸 것인가요?: <span class="t-ans">급식실 음식물 쓰레기 발생 원인과 해결 방안을 객관적인 정보로 알리기 위해 / 명확하고 공식적인 설명 어조(~이다, ~한다) 사용</span></span></td>
                </tr>
                <tr>
                  <th>③ 목표 가제목<br>(`[핵심 대상]+[설명 측면]`)</th>
                  <td><span class="pencil-line">✏️ 글 전체를 포괄하는 제목: <span class="t-ans">우리 학교 급식실의 음식물 쓰레기 발생 원인과 줄이기 방안 (또는 도시 열섬 현상의 원인과 냉섬 해결책)</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 다중 출처 자료 수집) 직결",
            "prompt": "오늘 확정한 내 설명문 주제를 뒷받침하기 위해 다음 시간(13차시)에 어떤 통계 자료나 백과사전 정의를 찾아야 할지 질문 2개를 적어 보세요.",
            "placeholder": "(예: 1. 음식물 쓰레기가 처리될 때 온실가스가 얼마나 나올까? 2. 우리 학교 잔반 이유 1위는 무엇일까?)",
            "example_answer": "1. 환경부 통계에서 하루 평균 버려지는 음식물 쓰레기양과 온실가스 배출량은 얼마일까? 2. 우리 학교 학생들이 반찬을 남기는 가장 큰 이유(비율 %)는 무엇일까?",
        },
        "self_check": [
            "예상 독자의 사전 지식 수준과 궁금해할 점을 구체적으로 분석했나요?",
            "포괄적인 화제를 ‘3단계 깔때기 기법’으로 좁혀 5~6문단으로 깊이 있게 설명할 수 있는 주제를 정했나요?",
            "개인 감상이나 주장이 아닌 ‘객관적 정보 전달’ 목적에 맞게 `[핵심 대상]+[설명 측면]` 형식의 가제목을 지었나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] Flower & Hayes 수사적 문제 표상(W1 계획하기): ① **누구에게(예상 독자 프로파일: 사전 지식·오개념·정보 요구)** + ② **왜(설명 목적: 객관적 원리·해결책 안내)** / [우측 판서] 3단계 깔때기(Funneling) 공식: `Lv.1 대분류(환경/기술)` ➔ `Lv.2 중위 대상(학교 급식 잔반 / 도시 열섬 / 스마트 팜)` ➔ `Lv.3 설명 측면 결합([핵심 대상] + [원인·구조와 해결 방안])`.",
            "intro_5min": "1차시부터 11차시까지 여러분은 생태계, 극지, 우주 쓰레기, 도시 열섬, 산호초 백화, 배터리 열폭주, 식용 곤충, 스마트 팜까지 최고의 과학·환경 설명문들을 읽으며 11개의 ‘글쓰기 씨앗’을 모았습니다. 오늘 12차시부터 16차시까지는 여러분이 직접 과학·시사 백과사전의 작가가 되어 나만의 설명문 한 편을 완성합니다!",
            "ido_think_aloud_script": "“선생님이 설명문 작문 계획을 세울 때 가장 먼저 피해야 할 함정을 보여 줄게요. 만약 주제를 ‘지구 환경 오염’이나 ‘우주의 신비’처럼 넓게 잡으면 어떻게 될까요? 할 말이 너무 많아서 결국 아무것도 깊게 설명하지 못하는 겉핥기 글이 되고 맙니다. 그래서 선생님은 ‘3단계 깔때기 기법’을 씁니다! 1단계 큰 깔때기에 ‘도시 환경 문제’를 넣고, 2단계에서 ‘여름철 도시 열섬 현상’으로 대상을 좁힌 뒤, 3단계 좁은 깔때기 끝에서 ‘발생 원인 3가지와 냉섬·투수성 블록 해결 방안’까지 날카롭게 좁히는 거예요. 그리고 예상 독자를 ‘우리 반 6학년 친구들’로 정하면, ‘불투수성’ 같은 한자어를 쓸 때 ‘물이 통하지 않는 성질’이라고 친절한 뜻풀이를 넣어 주어야겠다는 계획까지 자동으로 세워진답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[활동 1]에서 지훈이의 계획서(‘우주의 모든 별과 행성의 역사 / 무서웠던 내 감상을 일기로 쓰기’)는 왜 설명문 계획으로 적절하지 않을까요?",
                    "expected_ans": "첫째, ‘우주의 모든 별과 행성의 역사’는 범위가 너무 넓어 한 편의 글로 설명하기 어렵습니다. 둘째, ‘무서웠던 내 감상을 일기로 쓰는 것’은 객관적 정보를 전달하는 설명문의 집필 목적에 맞지 않습니다.",
                    "reprompt": "4차시에서 배운 좋은 제목의 조건(너무 넓거나 좁지 않을 것)과 설명문의 목적(객관적 사실·원리 전달)을 떠올려 보세요.",
                },
                {
                    "qar_type": "내 생각 말하기 (On My Own)",
                    "question": "여러분이 1~11차시 씨앗 보관함에서 고른 설명 대상은 무엇이며, 예상 독자인 친구들이 그 대상에 대해 가장 궁금해하거나 잘못 알고 있는 점(오개념)은 무엇일까요?",
                    "expected_ans": "(학생 발표 예시) 저는 ‘학교 급식실 음식물 쓰레기’를 골랐습니다. 친구들은 내가 남긴 반찬 조금은 괜찮다고 생각하지만, 실제로는 학교 전체 잔반량과 온실가스 배출량이 엄청나다는 사실을 잘 모릅니다.",
                    "reprompt": "내가 설명할 대상에 대해 친구들에게 질문한다면 어떤 질문을 가장 많이 할지 생각해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]을 통해 좋은 계획서의 준거를 확인하고, [활동 2]의 3단계 깔때기 상자에 자신의 주제를 단계별로 좁혀 적은 뒤, [활동 3]에서 예상 독자·집필 목적·목표 가제목을 갖춘 작문 계획서를 완성하도록 개별 지도한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 계획서 판별</strong>: [지훈] <strong>부적절</strong> — 근거: <strong>넓고(광범위하고)</strong>, <strong>객관적 정보·원리 전달</strong> / [서연] <strong>적절</strong> — 근거: <strong>좁혀졌고</strong><br>
              <strong>2. [활동 2] 3단계 깔때기 주제 좁히기 (예시 답안 및 인정 기준)</strong>: 학생이 선택한 주제(학교 급식 잔반, 도시 열섬, 산호초 백화, 우주 쓰레기, 스마트 팜 등 자유 선택 가능)가 `Lv.1(상위 분야) ➔ Lv.2(구체적 대상) ➔ Lv.3(세부 설명 측면 2~3가지)`의 위계로 좁혀졌으면 모두 정답으로 인정함.<br>
              <strong>3. [활동 3] 작문 계획서 산출 (인정 답안 기준)</strong>: ① 예상 독자의 수준·궁금증 분석, ② 객관적 정보 전달 목적 및 어조 설정, ③ `[핵심 대상]+[설명 측면]` 형식의 포괄적 가제목 3요소를 모두 충족하면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "집필 목적란에 “친구들에게 일회용품을 절대 쓰지 말라고 강력히 주장하고 설득하기 위해서”라고 쓰는 오류",
                    "diagnosis": "대상의 원리·원인·해결 방법을 객관적으로 해설하는 ‘설명문(Expository)’과 자신의 주장을 관철하는 ‘논설문(Argumentative, 5단원)’의 목적을 혼동함.",
                    "prescription": "논설문이 “~해야 한다!”라고 설득하는 글이라면, 설명문은 독자가 스스로 이해할 수 있도록 “~란 무엇이며, 어떤 원리·원인으로 일어나고, 어떤 해결 기술·방법이 있는지”를 객관적으로 알려 주는 글임을 명확히 구분해 준다.",
                },
                {
                    "error_case": "3단계 깔때기에서 1단계(환경)와 3단계(지구 환경 보호)가 사실상 똑같아 주제가 전혀 좁혀지지 않는 오류",
                    "diagnosis": "상위 범주어를 유의어로만 바꾸었을 뿐 하위 대상과 구체적 설명 측면(정의·구조·원인·해결책)으로 한정한 경험이 부족함.",
                    "prescription": "2단계에는 반드시 ‘눈에 보이거나 특정할 수 있는 구체적 현상·사물 하나’를 넣고, 3단계에는 ‘원인과 해결책’ 또는 ‘구조와 원리’라는 단어를 직접 넣어 합치도록 코칭한다.",
                },
            ],
            "scaffolding_down": "주제 선정 자체를 막막해하는 학습자에게는 교과서 1~11차시 제재 중 가장 흥미로웠던 주제 3가지(① 우리 학교 급식 잔반 문제와 해결법, ② 도시 열섬 현상과 냉섬 만들기, ③ 휴대용 배터리 열폭주 원리와 안전 수칙)를 ‘추천 주제 카드’로 제공하여 하나를 골라 자신의 학교·동네 상황에 맞게 변형하도록 돕는다.",
            "scaffolding_up": "심화 학습자에게는 동일한 주제(예: 스마트 팜)에 대해 예상 독자를 ① ‘초등 2학년 동생들’로 했을 때와 ② ‘지역 농촌 마을 이장님들’로 했을 때 제목과 중점 설명 내용이 어떻게 달라져야 하는지 이중 계획서를 설계해 보게 한다.",
            "rubric": {
                "high": "예상 독자의 사전 지식과 정보 요구를 구체적으로 분석하고, 3단계 깔때기 기법으로 주제를 정교하게 좁히며, [핵심 대상]+[설명 측면]을 갖춘 목표 제목과 객관적 설명 목적을 완벽히 수립함.",
                "mid": "설명할 대상과 예상 독자는 설정했으나, 주제가 다소 넓거나 가제목에 구체적인 설명 측면(원인·구조·해결 등)이 선명하게 드러나지 않음.",
                "low": "주제가 지나치게 광범위하거나 설명문의 목적을 감상문·논설문의 목적과 혼동하여 계획서 보완이 필요함.",
            },
        },
    },

    # =========================================================================
    # 13차시: G6-EXP-W2 내용 생성하기 (다중 출처 자료 수집·신뢰성 검증·시각자료 기획)
    # =========================================================================
    {
        "lesson_no": 13,
        "code": "G6-EXP-W2",
        "lesson_title": "[내용 생성하기] 다중 출처 자료 교차 검증 및 보조 시각 자료 기획하기",
        "std_badge": "[6국03-02] · [6국05-02] · CCSS W.6.7, W.6.8",
        "student_goal": "설명할 주제에 맞게 3종 이상의 다중 출처(백과사전·공공기관 통계·조사 자료)에서 정보를 수집하여 정확성과 신뢰성을 검증하고, 자신의 말로 요약 메모하며 본문을 도울 시각 자료(표·그래프)를 기획할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "공신력 있는 출처(국가 연구기관·백과사전·공식 통계)"],
            ["mk-line-blue", "파란 밑줄", "교차 검증으로 확정된 정확한 수치·사실 정보"],
            ["mk-line-red", "빨간 밑줄", "출처가 불분명하거나 과장·편향되어 걸러 내야 할 자료"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>🛠️ [쓰기 스튜디오 2단계: 내용 생성하기] 다중 출처 자료 수집·필터링 &amp; 시각자료 설계</span>
          <span style="font-size:6.7pt; color:#566573;">연계: 7차시(V2-3 텍스트+표) · 9~10차시(V3-1·2 도표·신뢰성 평가) · 11차시(V3-3 다매체 검증)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🔎 수집된 4종 자료 꾸러미 (신뢰성·정확성을 검증하여 내 글감으로 선별하기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 자료 선별 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.4pt; line-height:1.42;">
                <div style="margin-bottom:3px;"><strong>[자료 A: 표준 백과사전·법령 정의]</strong> (<span class="mk-person">출처: 환경부 『전국 폐기물 통계 조사』 및 『자원순환기본법』 해설, 2024</span>)<br>
                • <strong>내용</strong>: ‘음식물류 폐기물(음식물 쓰레기)’이란 식품의 생산·유통·조리 과정이나 식사 후에 먹고 남겨 버려지는 음식물 찌꺼기를 말한다. <span class="mk-line-blue">우리나라에서 하루 평균 발생하는 음식물 쓰레기는 약 1만 4,000톤으로 전체 생활 폐기물의 약 27%를 차지한다.</span></div>

                <div style="margin-bottom:3px;"><strong>[자료 B: 공공기관 과학·환경 통계]</strong> (<span class="mk-person">출처: 한국환경공단 · 국립환경과학원 『음식물 쓰레기와 온실가스 보고서』, 2024</span>)<br>
                • <strong>내용</strong>: 음식물 쓰레기는 수분 함량이 80% 이상이어서 땅에 묻거나 태울 때 많은 에너지가 소모된다. <span class="mk-line-blue">특히 음식물 쓰레기 1킬로그램(kg)을 처리하는 과정에서 이산화 탄소 환산량으로 약 1.65kg의 온실가스가 배출되어 지구 온난화를 가속한다.</span> 반면 학교 급식실에 학생 스스로 먹을 만큼만 덜어 먹는 ‘자율 배식대’와 ‘선호도 맞춤 조리법’을 도입한 시범 학교(150개교)에서는 <span class="mk-line-blue">1인당 잔반량이 평균 28.4% 감소했다.</span></div>

                <div style="margin-bottom:3px;"><strong>[자료 C: 우리 학교 학생회 실태 설문 조사]</strong> (<span class="mk-person">출처: 한빛초등학교 6학년 학생회 자치부, 2026년 5월 전교생 420명 설문</span>)<br>
                • <strong>내용</strong>: <span class="mk-line-blue">급식실에서 음식을 남기는 가장 큰 이유를 조사한 결과, ① ‘배식받은 양이 내가 먹을 수 있는 양보다 너무 많아서’가 52.0%(218명)로 1위였고, ② ‘채소·생선 등 좋아하지 않는 반찬이어서(편식)’가 35.0%(147명), ③ ‘국이나 반찬의 간이 맞지 않아서’가 9.0%(38명), ④ ‘기타’가 4.0%(17명)로 나타났다.</span></div>

                <div style="background:#FDEDEC; border:0.7pt solid #E74C3C; border-radius:4px; padding:3px 6px;">
                  <strong>[자료 D: 인터넷 익명 게시판 글]</strong> (<span class="mk-line-red">출처: ‘급식 싫어’ 개인 익명 블로그, 2016년 작성 / 근거 출처 없음</span>)<br>
                  • <strong>내용</strong>: <span class="mk-line-red">“내가 어제 급식실에서 봤는데 초등학생들은 원래 채소를 100% 다 싫어한다. 음식물 쓰레기는 바다에 그냥 버리면 물고기 밥이 되어서 환경에 아주 좋다. 그리고 마법의 소금만 뿌리면 쓰레기가 1초 만에 사라진다고 누가 그랬다.”</span>
                </div>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님의 자료 검증</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>수집한 [자료 A~D] 중 내 설명문에 쓰면 안 되는 가짜·불량 자료는 어느 것일까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>10차시에서 배운 <strong>4대 평가 준거</strong>로 보면, <strong>[자료 D]</strong>는 익명 블로그(공신력 없음)에 2016년 옛날 글이고, ‘100% 싫어한다(성급한 일반화)’, ‘바다에 버리면 좋다([자료 B]의 온실가스 사실과 충돌)’라는 거짓 정보야!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>[자료 D]는 과감히 버리고, 공신력 있는 <strong>[자료 A·B·C]</strong>만 골라 내 말로 요약 메모해야 해!</span></div>
                </div>
                <div class="wing-box vocab">
                  <strong>💡 표절 없이 내 말로 바꾸어 적기(재진술)</strong><br>
                  남의 자료를 글자 그대로 베껴 쓰지 말고, <strong>핵심 키워드와 수치·출처</strong>만 뽑아 내 문장 뼈대로 다시 정리합니다.
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "다중 출처 자료([자료 A~D])의 신뢰성을 검증하고 내 말로 바꾸어(재진술) 메모하기",
            "tag": "Step 1 다중 출처 필터링 및 재진술 메모",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:16%;">자료 번호</th>
                  <th style="width:16%; text-align:center;">채택 여부</th>
                  <th style="width:68%;">판정 이유 또는 내 설명문에 활용할 핵심 메모 (출처 + 핵심 사실 재진술)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">[자료 A]<br>환경부 통계</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;">( <span class="blank-slot"><span class="t-ans">채택 O</span></span> )</td>
                  <td>• 활용 문단: <strong>[처음]</strong> (개념 정의 및 문제 제기)<br>• 내 말 메모: 음식물 쓰레기란 조리·식사 후 버려지는 남은 음식물이며, 우리나라 하루 발생량은 약 <span class="blank-slot"><span class="t-ans">1만 4,000톤(생활 폐기물의 27%)</span></span>에 달한다(환경부, 2024).</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">[자료 B]<br>한국환경공단</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;">( <span class="blank-slot"><span class="t-ans">채택 O</span></span> )</td>
                  <td>• 활용 문단: <strong>[가운데-심각성 및 해결 효과]</strong><br>• 내 말 메모: 음식물 쓰레기 1kg 처리 시 온실가스 <span class="blank-slot"><span class="t-ans">약 1.65kg</span></span>이 배출된다. ‘자율 배식대’와 ‘맞춤 조리법’ 도입 시 1인당 잔반량이 <span class="blank-slot"><span class="t-ans">평균 28.4% 감소</span></span>했다(한국환경공단, 2024).</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">[자료 C]<br>학생회 설문</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;">( <span class="blank-slot"><span class="t-ans">채택 O</span></span> )</td>
                  <td>• 활용 문단: <strong>[가운데-발생 원인 및 시각자료]</strong><br>• 내 말 메모: 전교생 420명 설문 결과, 잔반 원인 1위는 <span class="blank-slot"><span class="t-ans">양이 너무 많아서(52.0%)</span></span>, 2위는 <span class="blank-slot"><span class="t-ans">좋아하지 않는 반찬이어서(35.0%)</span></span>이다(6학년 학생회, 2026).</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">[자료 D]<br>익명 블로그</td>
                  <td style="text-align:center; font-weight:800; color:#B03A2E;">( <span class="blank-slot"><span class="t-ans">제외 X</span></span> )</td>
                  <td>• 제외 이유: 익명 블로그라 <span class="blank-slot"><span class="t-ans">출처 공신력이 없고</span></span>, ‘바다에 버리면 좋다’ 등 과학적 사실([자료 B])과 충돌하는 <span class="blank-slot"><span class="t-ans">거짓·과장 정보</span></span>이기 때문이다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 선별한 수치 데이터([자료 B·C])를 독자가 한눈에 이해할 수 있도록 ‘보조 시각 자료’로 기획하기",
        "activity_2": {
            "title": "데이터의 성격(비율 vs 전후 크기 비교)에 맞는 ‘보조 시각 자료’ 기획·설계하기",
            "tag": "Step 2 시각 자료 유형 선택 및 4대 요소(제목·단위·범례·출처) 설계",
            "body_html": """
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px;">
              <div style="border:0.8pt solid #2980B9; border-radius:5px; padding:5px 7px; background:#F8FBFE; font-size:7.1pt;">
                <div style="font-weight:800; color:#1A5276; margin-bottom:2px;">📊 [시각자료 기획 ①] [자료 C] 잔반 발생 이유 (비율 데이터)</div>
                <div>• <strong>적절한 그래프 유형</strong>: 전체 100% 속 항목별 비율을 보여 주는 <span class="blank-slot"><span class="t-ans">원그래프(또는 띠그래프)</span></span></div>
                <div>• <strong>그래프 제목</strong>: <span class="blank-slot"><span class="t-ans">우리 학교 학생들의 급식 잔반 발생 이유 비율</span></span></div>
                <div>• <strong>수치 및 단위(%)</strong>: ① 양이 많아서(<span class="blank-slot"><span class="t-ans">52.0%</span></span>) / ② 안 좋아하는 반찬(<span class="blank-slot"><span class="t-ans">35.0%</span></span>) / ③ 간이 안 맞아서(9.0%) / ④ 기타(4.0%)</div>
                <div>• <strong>출처 표기</strong>: <span class="blank-slot"><span class="t-ans">한빛초 6학년 학생회 자치부(2026, 전교생 420명 설문)</span></span></div>
              </div>
              <div style="border:0.8pt solid #196F3D; border-radius:5px; padding:5px 7px; background:#F9FBF9; font-size:7.1pt;">
                <div style="font-weight:800; color:#196F3D; margin-bottom:2px;">📈 [시각자료 기획 ②] [자료 B] 자율 배식대 도입 전후 비교</div>
                <div>• <strong>적절한 그래프 유형</strong>: 도입 전후 수량 크기를 비교하는 <span class="blank-slot"><span class="t-ans">막대그래프</span></span></div>
                <div>• <strong>그래프 제목</strong>: <span class="blank-slot"><span class="t-ans">자율 배식대 및 맞춤 조리법 도입 전후 1인당 잔반량 비교</span></span></div>
                <div>• <strong>핵심 수치 변화</strong>: 도입 전(100% 기준) ➔ 도입 후 <span class="blank-slot"><span class="t-ans">71.6% (-28.4% 감소 ↓)</span></span></div>
                <div>• <strong>출처 표기</strong>: <span class="blank-slot"><span class="t-ans">한국환경공단·국립환경과학원(2024, 시범 학교 150개교 조사)</span></span></div>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 1~2]에서 검증한 자료 메모와 시각 자료 기획안을 내가 쓸 설명문 주제에 맞게 종합 포트폴리오로 정리하기",
        "activity_3": {
            "title": "내 설명문에 넣을 ‘검증된 핵심 자료 메모 & 시각 자료 지시 문장’ 산출하기",
            "tag": "Step 3 내용 생성 포트폴리오 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>과제</strong>: [활동 2]에서 기획한 시각 자료를 본문 문단 속에 자연스럽게 소개하는 <strong>‘시각 자료 지시 문장 + 핵심 수치 해석 문장’</strong>을 미리 작성해 보세요. (7차시·9차시 전략 적용)</div>
              <span class="pencil-line">✏️ <strong>[시각자료 ① 연동 문장]</strong>: <span class="t-ans">6학년 학생회가 전교생 420명을 대상으로 조사한 [원그래프 1]을 살펴보면, 음식을 남기는 이유로 ‘배식받은 양이 너무 많아서(52.0%)’와 ‘좋아하지 않는 반찬이어서(35.0%)’가 전체의 87%를 차지했다.</span></span>
              <span class="pencil-line">✏️ <strong>[시각자료 ② 연동 문장]</strong>: <span class="t-ans">한국환경공단(2024)의 [막대그래프 2]에서 확인할 수 있듯이, 자율 배식대와 맞춤 조리법을 도입한 학교에서는 1인당 잔반량이 평균 28.4%나 감소하는 뚜렷한 효과가 나타났다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 내용 조직: 다층 개요표 설계) 직결",
            "prompt": "오늘 모은 자료(정의, 발생 원인 2가지, 해결 방안 2가지, 그래프 2개)를 다음 시간 ‘처음-가운데-끝’ 개요표의 어느 문단에 배치할지 순서를 메모해 보세요.",
            "placeholder": "(예: 1문단[처음]: 음식물 쓰레기 정의와 발생량 ➔ 2문단[가운데1]: 원인 2가지와 설문 원그래프...)",
            "example_answer": "➊문단(처음): 음식물 쓰레기 정의와 온실가스 문제 제기 ➔ ➋문단(가운데1): 발생 원인 2가지(과다 배식 52%, 편식 35%) + [원그래프 1] ➔ ➌문단(가운데2): 맞춤형 해결 방안 2가지(자율 배식대, 조리법 개선) + [막대그래프 2] ➔ ➍문단(끝): 요약 및 기대 효과",
        },
        "self_check": [
            "10~11차시에서 배운 신뢰성 기준(공신력·정확성·최신성)을 적용해 불량 자료([자료 D])를 걸러 냈나요?",
            "선별한 자료의 핵심 내용을 그대로 베끼지 않고 출처(기관·연도)와 함께 내 말로 바꾸어 메모했나요?",
            "데이터의 성격(비율=원그래프, 크기 비교=막대그래프)에 맞게 제목·단위·출처를 갖춘 시각 자료를 기획했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 다중 출처 필터링 & 패러프레이징(W2 내용 생성): `[자료 A·B·C: 환경부·환경공단·학생회 설문 ➔ 채택(O)]` vs `[자료 D: 익명 블로그·거짓 과장 ➔ 폐기(X)]` / [우측 판서] 보조 시각 자료 설계 4대 필수 요소: ① 데이터 맞춤형 그래프 유형(비율=원 / 비교=막대 / 추세=꺾은선), ② 명확한 제목, ③ 측정 단위(%, 톤, kg), ④ 공인 출처(기관·연도).",
            "intro_5min": "12차시에서 설명할 주제와 예상 독자를 정했다면, 이제 빈 바구니에 정확하고 믿을 수 있는 재료(정보와 통계)를 담을 차례입니다. 9~11차시 평가적 읽기에서 배운 팩트체크 기준을 총동원해 자료를 고르고, 독자의 눈을 사로잡을 그래프를 직접 기획하는 13차시 목표를 안내한다.",
            "ido_think_aloud_script": "“선생님이 ‘학교 급식실 음식물 쓰레기’ 설명문을 쓰기 위해 자료 4개를 모아 왔어요. 다 쓰면 좋을까요? 아니죠! [자료 D]를 보세요. 2016년 익명 블로그 글인데 ‘초등학생은 채소를 100% 싫어한다’, ‘바다에 버리면 물고기 밥이 되어 환경에 좋다’고 쓰여 있네요. [자료 B](한국환경공단, 2024)에서 음식물 쓰레기 1kg당 온실가스 1.65kg이 나온다는 과학적 사실과 정면으로 충돌하는 거짓 정보이므로 즉시 휴지통에 버립니다! 대신 공신력 있는 [자료 A·B·C]를 채택하되, 남의 문장을 그대로 베껴 쓰면 ‘표절’이 되므로 핵심 숫자와 출처만 뽑아 내 말로 바꾸어(재진술) 메모카드를 만듭니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[자료 C]의 ‘우리 학교 잔반 발생 이유 설문 결과(52%, 35%, 9%, 4%)’와 [자료 B]의 ‘자율 배식대 도입 전후 잔반량 변화(100% ➔ 71.6%)’를 시각화할 때 각각 어떤 그래프를 선택하는 것이 가장 적절할까요?",
                    "expected_ans": "[자료 C]는 전체 응답자(100%) 중에서 각 이유가 차지하는 ‘비율’을 보여 주므로 원그래프(또는 띠그래프)가 가장 적절하고, [자료 B]는 도입 전과 도입 후의 잔반량 ‘크기 차이’를 비교하므로 막대그래프가 가장 적절합니다.",
                    "reprompt": "9차시에서 배웠던 그래프 유형 선택 기준(비율=원그래프 vs 크기 비교=막대그래프)을 떠올려 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "그래프를 그릴 때 그림만 그리고 ‘단위(%)’나 ‘출처(조사 기관·연도)’를 빼먹으면 독자가 읽을 때 어떤 문제가 생길까요?",
                    "expected_ans": "숫자가 몇 명인지 몇 퍼센트(%)인지 정확히 알 수 없고, 누가 언제 조사한 자료인지 알 수 없어 글 전체의 신뢰성이 떨어집니다.",
                    "reprompt": "9차시 [글 나]에서 출처와 단위가 없던 그래프를 평가했던 기억을 떠올려 볼까요?",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 자료 A~D의 채택 여부를 판정하고 재진술 메모를 완성한 뒤, [활동 2]에서 원그래프와 막대그래프 기획안을 설계하고, [활동 3]에서 본문에 삽입할 ‘시각 자료 지시 문장’을 미리 작성하도록 지도한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 다중 출처 필터링 및 메모</strong>: [자료 A] <strong>채택 O</strong> — <strong>1만 4,000톤(생활 폐기물의 27%)</strong> / [자료 B] <strong>채택 O</strong> — <strong>약 1.65kg</strong>, <strong>평균 28.4% 감소</strong> / [자료 C] <strong>채택 O</strong> — <strong>양이 너무 많아서(52.0%)</strong>, <strong>좋아하지 않는 반찬이어서(35.0%)</strong> / [자료 D] <strong>제외 X</strong> — <strong>출처 공신력이 없고</strong>, <strong>거짓·과장 정보</strong><br>
              <strong>2. [활동 2] 보조 시각 자료 설계</strong>: [기획 ①] 유형: <strong>원그래프(띠그래프)</strong>, 제목: <strong>우리 학교 학생들의 급식 잔반 발생 이유 비율</strong>, 수치: <strong>52.0% / 35.0%</strong>, 출처: <strong>한빛초 6학년 학생회 자치부(2026)</strong> | [기획 ②] 유형: <strong>막대그래프</strong>, 제목: <strong>자율 배식대 및 맞춤 조리법 도입 전후 1인당 잔반량 비교</strong>, 수치: <strong>71.6% (-28.4% 감소)</strong>, 출처: <strong>한국환경공단·국립환경과학원(2024)</strong><br>
              <strong>3. [활동 3] 시각 자료 지시 문장 산출 (인정 답안 기준)</strong>: 문장 안에 (1) 시각 자료 지시어(`[원그래프 1]을 살펴보면`, `[막대그래프 2]에서 보듯이`), (2) 조사 출처, (3) 핵심 수치 해석이 모두 포함되면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "자료를 메모할 때 원문 문장을 조사 하나 바꾸지 않고 토씨까지 그대로 베껴 적는 오류",
                    "diagnosis": "자료 인용·재진술(Paraphrasing)과 단순 베껴 쓰기(표절)의 차이를 인식하지 못함.",
                    "prescription": "원문을 덮고 핵심 명사(키워드)와 숫자, 출처만 메모 칸에 적은 뒤, 자신의 주어-목적어-서술어 호흡으로 문장을 새로 조립하게 지도한다.",
                },
                {
                    "error_case": "시각 자료를 기획할 때 본문에는 한마디 언급도 없이 그래프만 덩그러니 그려 넣는 오류",
                    "diagnosis": "본문 텍스트와 시각 자료를 유기적으로 연결하는 ‘지시 문장(Cross-reference sentence)’의 필요성을 모름.",
                    "prescription": "[활동 3]처럼 반드시 본문 속에 “~가 조사한 [그림 1]을 살펴보면”이라는 안내판 문장을 넣어야 독자가 그래프와 글을 연결해 읽을 수 있음을 강조한다.",
                },
            ],
            "scaffolding_down": "다른 개인 주제(예: 도시 열섬, 스마트 팜, 산호초 백화)로 글을 쓰는 학습자에게도 교과서 1~11차시 지문과 표에 수록된 공인 통계(KISTI, 극지연구소, 항우연, 소비자원, 농촌진흥청 등)를 ‘공식 자료 뱅크’로 그대로 활용하여 메모 카드를 작성할 수 있게 허용·지원한다.",
            "scaffolding_up": "심화 학습자에게는 두 가지 변인(예: 연도별 잔반량 막대그래프 + 처리 비용 꺾은선그래프)이 결합된 ‘복합 축 인포그래픽’을 직접 간단히 스케치하여 설계해 보게 한다.",
            "rubric": {
                "high": "4대 평가 준거로 불량 자료를 정확히 걸러 내고, 공신력 있는 3종 자료를 출처와 함께 자신의 말로 요약 메모하며, 제목·단위·범례·출처와 본문 지시문을 완비한 시각 자료를 기획함.",
                "mid": "신뢰할 수 있는 자료 선별과 시각 자료 유형 선택은 적절하나, 재진술 메모가 원문과 너무 비슷하거나 그래프의 단위·출처 표기 일부가 빠짐.",
                "low": "자료의 신뢰성을 변별하지 못하거나 데이터의 성격에 맞지 않는 그래프 유형을 선택함.",
            },
        },
    },

    # =========================================================================
    # 14차시: G6-EXP-W3 내용 조직하기 (6대 설명 구조 선택·처음-가운데-끝 개요·담화표지 배치)
    # =========================================================================
    {
        "lesson_no": 14,
        "code": "G6-EXP-W3",
        "lesson_title": "[내용 조직하기] 읽기 구조 도해조직자를 미러링하여 다층 개요표 짜기",
        "std_badge": "[6국03-01] · [6국03-02] · CCSS W.6.2a, W.6.2c",
        "student_goal": "설명할 대상과 자료의 성격에 맞게 6대 설명 구조(분류·분석·비교대조·과정·인과·문제해결)를 복합 선택하고, 소제목과 담화 표지·거시 지시어가 포함된 ‘처음-가운데-끝’ 다층 개요표를 작성할 수 있다.",
        "marking_items": [
            ["mk-person", "파란 동그라미", "글 전체 상위 거시 구조 및 문단별 하위 설명 구조"],
            ["mk-bg", "초록 네모", "문단군을 대표하는 명쾌한 소제목"],
            ["mk-highlight", "형광펜", "문단과 문장 사이를 잇는 담화 표지 및 거시 지시어"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>🛠️ [쓰기 스튜디오 3단계: 내용 조직하기] 6대 설명 구조 선택 &amp; 다층 개요 설계도</span>
          <span style="font-size:6.7pt; color:#566573;">연계: 2~4차시(V1-2·3·4 6대 설명 구조 도해) · 6차시(V2-2 거시 지시어) 1:1 미러링</span>
        </div>

        <!-- 1. 6대 설명 구조 & 담화 표지 선택 툴박스 -->
        <div style="background:#F8F9F9; border:0.85pt solid #7FB3D5; border-radius:5px; padding:4.5px 7px; margin-bottom:5px; font-size:7pt;">
          <div style="font-weight:800; color:#1A5276; margin-bottom:2px;">🧰 1단계: 내 설명문의 뼈대가 될 ‘6대 설명 구조 &amp; 짝꿍 담화 표지’ 고르기 (2종 이상 복합 선택!)</div>
          <table class="std-table" style="font-size:6.8pt;">
            <thead>
              <tr>
                <th style="width:16%;">설명 구조</th>
                <th style="width:34%;">언제 사용하면 좋을까? (읽기 모델)</th>
                <th style="width:50%;">반드시 함께 배치할 짝꿍 담화 표지 (Signal Words)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight:800; color:#1A5276;">① 분류 / ② 분석</td>
                <td>종류를 나누거나(2차시 생물), 구성 부분을 쪼갤 때(2차시 눈)</td>
                <td><code>~기준에 따라 크게 ~로 나뉜다, ~에는 ~이 속한다 / ~은 ~부분들로 이루어져 있다</code></td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#1A5276;">③ 비교·대조</td>
                <td>두 대상의 공통점과 차이점을 견줄 때(3차시 북극과 남극)</td>
                <td><code>모두, 마찬가지로, 공통적으로 / 반면에, 이와 달리, ~에 비해</code></td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#196F3D;">④ 순서 / ⑤ 인과</td>
                <td>절차를 설명하거나 원인과 결과를 연결할 때(3차시 물·기후)</td>
                <td><code>먼저, 그다음, 이어서, 마지막으로 / ~이기 때문이다, ~한 탓에, 그 결과, 이로 인해</code></td>
              </tr>
              <tr>
                <td style="font-weight:800; color:#B03A2E;">⑥ 문제·해결</td>
                <td>문제의 원인을 밝히고 해결책을 제시할 때(4차시 우주 쓰레기)</td>
                <td><code>~문제에 직면해 있다, 원인은 ~이다 / 이 문제를 해결하기 위해, 첫째 방안은 ~이다</code></td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- 2. 읽기 모델을 미러링한 ‘처음-가운데-끝’ 다층 개요 시범 모델 -->
        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📐 2단계: 복합 설명문 ‘처음-가운데-끝’ 다층 개요표 시범 모델</th>
              <th class="wing-head">🧠 사고구술 &amp; 조직 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.3pt; line-height:1.42;">
                <div><strong>• 본제목</strong>: 〈우리 학교 급식실의 음식물 쓰레기 발생 원인과 줄이기 방안〉</div>
                <div><strong>• 상위 거시 구조</strong>: <span class="mk-person">문제·해결 구조</span> (하위 결합: 정의 + 인과 분석 + 원인-해결 1:1 대응)</div>
                <div style="margin-top:3px; border-left:2.5pt solid #1A5276; padding-left:6px;">
                  <strong>[처음 (1문단)] 화제 도입 및 개념 정의</strong><br>
                  • 중심 내용: 학교 급식실 잔반 문제 제기 및 ‘음식물 쓰레기’의 개념 정의<br>
                  • 뒷받침 자료: 하루 1만 4,000톤 발생 및 1kg당 온실가스 1.65kg 배출 통계(환경부·한국환경공단, 2024)
                </div>
                <div style="margin-top:3px; border-left:2.5pt solid #196F3D; padding-left:6px;">
                  <strong>[가운데 1 (2문단)]</strong> <span class="mk-bg">소제목 1: 급식실 음식물 쓰레기가 발생하는 두 가지 원인</span> (<span class="mk-person">인과·나열 구조</span>)<br>
                  • 담화 표지: <span class="mk-highlight">발생하는 원인은 크게 두 가지이다. 첫째 ~기 때문이다. 둘째 ~탓에</span><br>
                  • 중심·뒷받침: [원인 ①] 먹을 양을 고려하지 않은 과다 배식(52.0%) / [원인 ②] 채소·생선 기피 편식 습관(35.0%) + <strong>📊 [원그래프 1] 삽입 (학생회 설문 출처 명시)</strong>
                </div>
                <div style="margin-top:3px; border-left:2.5pt solid #D35400; padding-left:6px;">
                  <strong>[가운데 2 (3문단)]</strong> <span class="mk-bg">소제목 2: 음식물 쓰레기를 줄이는 맞춤형 해결 방안</span> (<span class="mk-person">문제·해결 구조</span>)<br>
                  • 거시 지시어 &amp; 표지: <span class="mk-highlight">이러한 음식물 쓰레기 문제를 해결하기 위해서는 / 먼저 ~ 방법이 있다. 다음으로 ~ 대안이 효과적이다.</span><br>
                  • 중심·뒷받침: [해결 ①(원인① 대응)] 자율 배식대 운영 / [해결 ②(원인② 대응)] 선호도 조사 기반 조리법 개선 + <strong>📈 [막대그래프 2] 삽입 (잔반 28.4% 감소 통계)</strong>
                </div>
                <div style="margin-top:3px; border-left:2.5pt solid #2C3E50; padding-left:6px;">
                  <strong>[끝 (4문단)] 전체 요약 및 전망</strong>: <span class="mk-highlight">이처럼</span> 원인을 알고 자율 배식과 조리법 개선을 실천하면 급식실 잔반을 줄이고 지구 환경도 지킬 수 있음.
                </div>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님의 조직 비법</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>개요를 짤 때 왜 [가운데 1]의 원인과 [가운데 2]의 해결책을 짝맞추어 배치해야 할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>4차시 ‘우주 쓰레기’ 글에서 원인①(이미 떠도는 쓰레기)↔해결①(청소 위성), 원인②(임무 종료 위성)↔해결②(태양 돛)가 1:1로 짝을 이루었지!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>내 글도 <strong>원인①(과다 배식)↔해결①(자율 배식대)</strong>, <strong>원인②(편식)↔해결②(조리법 개선)</strong>으로 1:1 대응시키고, 문단 첫머리에 <strong>거시 지시어(‘이러한 문제를 해결하기 위해서는’)</strong>를 넣으면 응집성이 완벽해져!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "개요 초안의 구조적 결함(통일성 위배·분류 기준 혼란·담화 표지 오용) 진단하기",
            "tag": "Step 1 개요의 구조적 정합성 점검",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:52%;">문제가 있는 개요 초안 사례</th>
                  <th style="width:48%;">구조적 결함 진단 및 수정 방안</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>[사례 1]</strong> ‘도시 열섬 현상의 원인’ 문단에 <em>“내가 지난여름 수영장에서 먹은 수박이 정말 시원하고 맛있었다.”</em>를 뒷받침 내용으로 넣음.</td>
                  <td>주제와 관련 없는 개인적 일화로 문단의 <span class="blank-slot"><span class="t-ans">통일성</span></span>을 해치므로 과감히 <span class="blank-slot"><span class="t-ans">삭제</span></span>해야 한다.</td>
                </tr>
                <tr>
                  <td><strong>[사례 2]</strong> ‘원인 1: 과다 배식, 원인 2: 편식’을 설명한 뒤, 해결책 문단 첫머리를 <em>“반면에(또는 그러므로) 이것을 해결하려면”</em>으로 시작함.</td>
                  <td>대조 표지(`반면에`)와 모호한 대명사(`이것`) 대신, 앞 문단 전체를 받는 거시 지시어 <span class="blank-slot"><span class="t-ans">이러한 음식물 쓰레기 문제를 해결하기 위해서는</span></span>으로 고쳐야 응집성이 높아진다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 점검 원리를 바탕으로 내 설명문의 ‘상위 거시 구조’와 ‘문단별 하위 구조·담화 표지’ 연결하기",
        "activity_2": {
            "title": "내 설명문의 복합 구조(상위 거시 틀 + 문단별 하위 설명 방법 + 담화 표지) 설계하기",
            "tag": "Step 2 복합 설명 구조 및 거시 지시어 배치",
            "body_html": """
            <div class="inference-row" style="grid-template-columns:1fr 12px 1fr 12px 1fr; margin-bottom:0;">
              <div class="inf-card c1">
                <strong style="color:#1A5276;">[처음 (1문단) 설계]</strong><br>
                • 설명 방법: <span class="blank-slot"><span class="t-ans">정의 + 수치 제시</span></span><br>
                • 핵심 표지: <code>~란 ~을 말한다, ~통계에 따르면</code>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:#196F3D;">[가운데 1 (2문단) 설계]</strong><br>
                • 설명 구조: <span class="blank-slot"><span class="t-ans">인과 + 분류·나열</span></span><br>
                • 핵심 표지: <code>원인은 크게 두 가지이다, 첫째 ~기 때문이다, 둘째 ~탓에</code>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#B03A2E;">[가운데 2 (3문단) &amp; 끝(4문단)]</strong><br>
                • 설명 구조: <span class="blank-slot"><span class="t-ans">문제·해결 + 요약</span></span><br>
                • 거시 지시어: <span class="blank-slot"><span class="t-ans">이러한 문제를 해결하기 위해서는</span></span>, <code>먼저, 다음으로, 이처럼</code>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 구조 설계를 바탕으로 소제목·중심문장·뒷받침 자료·시각자료 위치가 모두 담긴 다층 개요표 완성하기",
        "activity_3": {
            "title": "나만의 복합 설명문 ‘처음-가운데-끝 다층 개요표(Multi-level Outline)’ 완성하기",
            "tag": "Step 3 다층 개요서 산출",
            "body_html": """
            <table class="std-table" style="font-size:7.1pt;">
              <thead>
                <tr>
                  <th style="width:14%;">구성 단계</th>
                  <th style="width:28%;">소제목 및 문단 중심문장 골격</th>
                  <th style="width:36%;">뒷받침 세부 내용 및 시각 자료 삽입 위치</th>
                  <th style="width:22%;">담화 표지·거시 지시어</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">처음<br>(➊문단)</td>
                  <td>• 중심 내용: <span class="blank-slot"><span class="t-ans">음식물 쓰레기의 정의와 환경적 심각성</span></span></td>
                  <td>• 정의 풀이 + 하루 1만 4,000톤 발생 및 1kg당 온실가스 1.65kg 배출 통계(환경부, 2024)</td>
                  <td><code>~문제에 직면해 있다, ~란 ~을 말한다</code></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">가운데 1<br>(➋문단)</td>
                  <td>• <strong>소제목 1</strong>: <span class="blank-slot"><span class="t-ans">급식실 음식물 쓰레기가 발생하는 두 가지 원인</span></span></td>
                  <td>• 원인① 과다 배식(52%) + 원인② 편식 습관(35%)<br>• 삽입할 시각자료: <span class="blank-slot"><span class="t-ans">📊 [원그래프 1] 학생회 설문 결과</span></span></td>
                  <td><code>원인은 크게 두 가지이다, 첫째 ~기 때문이다, 둘째 ~탓에</code></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#D35400;">가운데 2<br>(➌문단)</td>
                  <td>• <strong>소제목 2</strong>: <span class="blank-slot"><span class="t-ans">음식물 쓰레기를 줄이는 맞춤형 해결 방안</span></span></td>
                  <td>• 해결① 자율 배식대 운영 + 해결② 선호도 조사 및 조리법 개선<br>• 삽입할 시각자료: <span class="blank-slot"><span class="t-ans">📈 [막대그래프 2] 잔반 28.4% 감소 통계</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">이러한 문제를 해결하기 위해서는</span></span>, <code>먼저, 다음으로</code></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#2C3E50;">끝<br>(➍문단)</td>
                  <td>• 중심 내용: <span class="blank-slot"><span class="t-ans">핵심 요약 및 친환경 급식실 전망</span></span></td>
                  <td>• 원인에 맞는 해결 방안 실천을 통한 잔반 감소 및 지구 환경 보호 효과 정리</td>
                  <td><code>이처럼, 따라서</code></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "15차시(W4 초고 집필하기) 1:1 직결",
            "prompt": "오늘 완성한 개요표의 [가운데 1] 또는 [가운데 2] 문단에서 가장 먼저 쓸 ‘두괄식 중심문장’ 1개를 미리 완성해 보세요.",
            "placeholder": "(예: 우리 학교 급식실에서 음식물 쓰레기가 발생하는 원인은 크게 두 가지이다.)",
            "example_answer": "우리 학교 급식실에서 음식물 쓰레기가 발생하는 원인은 크게 먹을 양을 고려하지 않은 과다 배식과 채소·생선을 기피하는 편식 습관 두 가지이다.",
        },
        "self_check": [
            "설명 대상의 특성에 맞게 6대 설명 구조 중 2종 이상을 복합적으로 선택했나요?",
            "‘처음-가운데(소제목 포함)-끝’의 각 문단에 중심 내용과 뒷받침 자료, 시각 자료 삽입 위치를 빈틈없이 배치했나요?",
            "문단과 문단을 자연스럽게 이어 주는 거시 지시어(‘이러한 문제를~’)와 담화 표지를 알맞게 설계했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 읽기 도해조직자 ➔ 쓰기 개요표 1:1 미러링(Meyer 상위구조 전이): `처음(정의+문제 제기)` ➔ `가운데 1(소제목1 + 원인①·② 인과 분석 + [원그래프 1])` ➔ `가운데 2(소제목2 + 거시 지시어 + 해결①·② 대안 제시 + [막대그래프 2])` ➔ `끝(요약 및 전망)` / [우측 판서] 원인-해결책 1:1 대칭 법칙: 원인①(과다 배식)↔해결①(자율 배식대), 원인②(편식)↔해결②(조리법 개선).",
            "intro_5min": "집을 지을 때 벽돌(13차시 자료)만 쌓아 놓는다고 튼튼한 집이 될까요? 기둥과 방의 위치를 정하는 ‘설계도(개요표)’가 있어야 합니다. 2~4차시 읽기 시간에 그렸던 텍스트 구조 도해조직자를 거울처럼 그대로 뒤집어 내 설명문의 다층 개요표를 짜는 14차시 목표를 제시한다.",
            "ido_think_aloud_script": "“선생님이 어떻게 읽기 시간에 배운 구조도를 내 글의 개요표로 바꾸는지 보여 줄게요. 우리는 4차시 ‘우주 쓰레기’ 글에서 [문제 제기 ➔ 원인·심각성 ➔ 해결 방안 ①·②] 구조를 배웠어요. 내 글도 똑같이 거시 구조를 ‘문제·해결’로 잡습니다! 그리고 본론 문단 위에는 독자가 길을 잃지 않도록 ‘소제목’이라는 안내판을 달아 줄 거예요. 가장 중요한 비법은 문단과 문단이 만나는 이음매예요! ➋문단에서 잔반 발생 원인 두 가지를 설명한 뒤, ➌문단 첫머리를 그냥 시작하지 않고 6차시에서 배운 거시 지시어 ‘이러한 음식물 쓰레기 문제를 해결하기 위해서는’으로 시작하면 두 문단이 자석처럼 착 달라붙는답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "시범 모델 개요표에서 [가운데 1]의 원인 두 가지와 [가운데 2]의 해결 방안 두 가지는 어떻게 짝을 이루고 있나요? 왜 이렇게 순서를 맞추어 조직해야 할까요?",
                    "expected_ans": "원인①(과다 배식 52%)은 해결①(먹을 만큼 덜어 먹는 자율 배식대)과 짝을 이루고, 원인②(편식 35%)는 해결②(선호도 조사 및 조리법 개선)와 1:1로 짝을 이룹니다. 이렇게 순서를 맞추어야 독자가 ‘어떤 원인을 어떤 방법으로 해결하는지’ 논리적으로 명쾌하게 이해할 수 있습니다.",
                    "reprompt": "4차시 우주 쓰레기 글에서 원인 두 가지와 해결책 두 가지가 어떻게 짝지어졌는지 떠올려 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "13차시에서 기획한 [원그래프 1(잔반 이유 설문)]과 [막대그래프 2(자율 배식대 도입 효과)]는 개요표의 몇 문단에 각각 넣어야 본문 내용과 가장 잘 어울릴까요?",
                    "expected_ans": "잔반 발생 이유 비율을 보여 주는 [원그래프 1]은 원인을 분석하는 ➋문단(가운데 1)에 넣고, 자율 배식대 도입 후 잔반 감소 효과를 보여 주는 [막대그래프 2]는 해결 방안을 설명하는 ➌문단(가운데 2)에 넣어야 본문과 시각 자료가 100% 일치합니다.",
                    "reprompt": "각 그래프의 제목이 ➋문단 소제목(원인)과 ➌문단 소제목(해결 방안) 중 어디와 짝꿍인지 확인해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 통일성·응집성 오류를 진단하고, [활동 2]에서 문단별 설명 구조와 담화 표지를 선택한 뒤, [활동 3]에서 소제목·중심문장·뒷받침 자료·시각자료 위치·담화표지가 모두 포함된 다층 개요표를 완성하도록 지도한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 개요 결함 진단</strong>: [사례 1] <strong>통일성</strong>, <strong>삭제</strong> / [사례 2] <strong>이러한 음식물 쓰레기 문제를 해결하기 위해서는</strong><br>
              <strong>2. [활동 2] 복합 구조 및 표지 설계</strong>: [처음] <strong>정의 + 수치 제시</strong> / [가운데 1] <strong>인과 + 분류·나열</strong> / [가운데 2 &amp; 끝] <strong>문제·해결 + 요약</strong>, 거시 지시어: <strong>이러한 문제를 해결하기 위해서는</strong><br>
              <strong>3. [활동 3] 다층 개요표 완성 (인정 답안 기준)</strong>: 학생이 선택한 주제(학교 잔반 또는 개별 선택 주제)에 대해 (1) 처음-가운데1·2-끝 위계와 소제목 2개 이상, (2) 2종 이상의 복합 설명 구조, (3) 문단 간 거시 지시어 및 담화 표지, (4) 시각 자료 삽입 위치가 논리적으로 일치하게 작성되면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "개요표에 키워드나 줄거리만 나열하고 문단과 문단을 이어 줄 ‘담화 표지’와 ‘거시 지시어’를 비워 두는 오류",
                    "diagnosis": "개요 짜기를 단순한 ‘소재 나열’로만 생각하고, 문단 간 논리적 결속 장치(Cohesive devices)까지 설계해야 초고 집필이 매끄러워진다는 점을 간과함.",
                    "prescription": "개요표의 오른쪽 열(‘담화 표지·거시 지시어’)을 먼저 채우게 하여, 각 문단의 첫 문장과 문장 연결 고리를 미리 설계하도록 지도한다.",
                },
                {
                    "error_case": "원인 문단에서는 ‘과다 배식’을 말하고 해결책 문단에서는 엉뚱하게 ‘분리수거함 색깔 바꾸기’를 제시하여 원인과 해결책이 겉도는 오류",
                    "diagnosis": "문제·해결 구조에서 해결 방안은 반드시 앞서 제기한 발생 원인을 직접 제거하거나 완화하는 대안이어야 한다는 인과적 대응 원리를 놓침.",
                    "prescription": "개요표의 [가운데 1] 원인① 옆에서 [가운데 2] 해결①로 화살표(➔)를 직접 그어 보게 하여, 그 해결책이 정말 그 원인을 해결할 수 있는지 자가 점검하게 한다.",
                },
            ],
            "scaffolding_down": "개요표의 소제목 짓기를 어려워하는 학습자에게는 ‘소제목 공식 카드’(`소제목 1: [대상]이 발생하는 [숫자]가지 원인 / [대상]을 이루는 구성 요소`, `소제목 2: [대상] 문제를 해결하는 [숫자]가지 방안`)를 제공하여 빈칸만 채워 소제목을 완성하게 돕는다.",
            "scaffolding_up": "심화 학습자에게는 본론을 3문단(가운데 1: 국내외 음식물 쓰레기 처리 방식 비교·대조 문단 추가)으로 확장하여 ‘정의 + 인과 + 비교·대조 + 문제·해결’의 4중 복합 구조 개요표를 설계해 보게 한다.",
            "rubric": {
                "high": "6대 설명 구조 중 2종 이상을 대상의 특성에 맞게 결합하고, 소제목·중심-뒷받침 위계·거시 지시어·담화 표지·시각 자료 삽입 위치를 완벽히 갖춘 다층 개요표를 작성함.",
                "mid": "처음-가운데-끝의 기본 개요와 소제목은 갖추었으나, 문단 간 거시 지시어 배치나 원인-해결책의 1:1 대칭성이 일부 미흡함.",
                "low": "문단 구분 없이 내용을 나열하거나 주제에서 벗어난 내용이 포함되어 개요의 통일성과 응집성 보완이 필요함.",
            },
        },
    },

    # =========================================================================
    # 15차시: G6-EXP-W4 초고 집필하기 (중심-뒷받침 위계·학술어 뜻풀이·객관적 어조·시각자료 통합 집필)
    # =========================================================================
    {
        "lesson_no": 15,
        "code": "G6-EXP-W4",
        "lesson_title": "[초고 집필하기] 학술 어휘 뜻풀이와 시각 자료 지시문을 통합하여 초고 쓰기",
        "std_badge": "[6국03-01] · [6국03-02] · [6국04-02] · CCSS W.6.2a-f",
        "student_goal": "완성한 다층 개요표를 바탕으로 문단별 중심-뒷받침 위계를 세우고, 학술 어휘 뜻풀이·시각 자료 지시문·출처 표기·객관적 설명 어조를 통합하여 한 편의 완결된 복합 설명문 초고를 집필할 수 있다.",
        "marking_items": [
            ["mk-highlight", "형광펜", "각 문단의 두괄식 중심문장"],
            ["mk-person", "파란 동그라미", "전문 학술 어휘와 독자 맞춤형 뜻풀이 단서"],
            ["mk-line-blue", "파란 밑줄", "시각 자료 지시 문장(‘[표/그래프]에서 보듯이’) 및 출처 표기"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>🛠️ [쓰기 스튜디오 4단계: 초고 집필하기] 설명문 집필 5대 핵심 표현 전략 &amp; 모범 문단</span>
          <span style="font-size:6.7pt; color:#566573;">연계: 1차시(중심-뒷받침) · 5차시(학술어 뜻풀이) · 7·9차시(도표 지시문) · 10차시(객관적 어조)</span>
        </div>

        <!-- 1. 설명문 초고 집필 5대 표현 전략 가이드 -->
        <div style="background:#EBF5FB; border:0.85pt solid #5DADE2; border-radius:5px; padding:4.5px 8px; margin-bottom:5px; font-size:7.1pt; line-height:1.4;">
          <div style="font-weight:800; color:#1A5276; margin-bottom:2px;">✍️ 1단계: 개요표를 살아 있는 문장으로 바꾸는 ‘설명문 집필 5대 법칙’</div>
          <div>① <strong>[중심-뒷받침 다층 위계]</strong> 각 문단 첫머리에 <strong>중심문장(일반적 진술)</strong>을 세우고, 뒤에 <strong>설명·수치·예시 뒷받침문장</strong>을 연결한다.</div>
          <div>② <strong>[학술 어휘 친절한 뜻풀이]</strong> 어려운 한자 학술어(예: <code>폐기물, 온실가스, 자율 배식, 불투수성</code>)가 나오면 <strong>괄호 설명이나 ‘즉, 다시 말해’ 재진술</strong>로 뜻을 풀어 준다.</div>
          <div>③ <strong>[시각 자료 지시문 &amp; 출처 통합]</strong> 본문 안에 <code>“[원그래프 1]의 조사 결과에서 확인할 수 있듯이”</code>처럼 지시문과 공식 출처(기관·연도)를 함께 밝힌다.</div>
          <div>④ <strong>[담화 표지 &amp; 거시 지시어 연결]</strong> <code>첫째~둘째, 반면에, 이러한 문제를 해결하기 위해서는</code>으로 문장과 문단을 촘촘히 잇는다.</div>
          <div>⑤ <strong>[객관적·공식적 어조 일관성]</strong> 개인 감정(‘너무 슬프다’)을 빼고 <code>~이다, ~한다</code>(또는 일관된 <code>~입니다</code>)의 객관적 어조를 끝까지 유지한다.</div>
        </div>

        <!-- 2. 개요가 실제 문단으로 변환되는 시범 모델 (I Do) -->
        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📖 2단계: 개요 메모를 완결된 설명 문단으로 확장한 시범 모델</th>
              <th class="wing-head">🧠 사고구술 &amp; 문장화 길잡이</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-size:8.6pt; line-height:1.55;">
                <div style="font-family:var(--font-sans); font-size:8.2pt; font-weight:800; color:#1A5276; text-align:center; margin-bottom:3px; background:#F2F4F4; padding:2px; border-radius:3px;">제목: 우리 학교 급식실의 음식물 쓰레기 발생 원인과 줄이기 방안</div>
                <p><span class="p-num">➊</span> <strong>[처음]</strong> 오늘날 많은 학교 급식실은 매일 버려지는 음식물 쓰레기가 늘어나는 문제에 직면해 있다. <span class="mk-person">음식물 쓰레기(음식물류 폐기물)란 식품을 조리하는 과정이나 식사 후에 먹지 않고 남겨 버려지는 음식물 찌꺼기를 말한다.</span> <span class="mk-line-blue">환경부의 2024년 전국 폐기물 통계에 따르면</span> 우리나라에서 하루 평균 발생하는 음식물 쓰레기는 약 1만 4,000톤으로 전체 생활 쓰레기의 27퍼센트를 차지한다. 특히 음식물 쓰레기 1킬로그램을 처리할 때마다 약 1.65킬로그램의 <span class="mk-person">온실가스(지구의 기온을 높이는 기체)</span>가 배출되어 지구 온난화를 가속하므로, 급식실 잔반이 발생하는 원인을 정확히 알고 해결 방안을 마련해야 한다.</p>
                <p><span class="p-num">➋</span> <strong>[가운데 1] 소제목 1: 급식실 음식물 쓰레기가 발생하는 두 가지 원인</strong><br>
                <span class="mk-highlight">우리 학교 급식실에서 음식물 쓰레기가 발생하는 원인은 크게 두 가지이다.</span> <span class="mk-line-blue">한빛초등학교 6학년 학생회가 2026년 5월 전교생 420명을 대상으로 조사한 [원그래프 1]을 살펴보면,</span> 첫째 원인은 학생들이 자신이 먹을 수 있는 양을 고려하지 않고 음식을 지나치게 많이 배식받기 때문이다(52.0%). 둘째 원인은 채소나 생선처럼 익숙하지 않은 식재료를 기피하는 <span class="mk-person">편식(음식을 골고루 먹지 않고 가려 먹는 습관)</span> 탓에 반찬을 입에 대지도 않고 그대로 남기는 경우가 많기 때문이다(35.0%).</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u4">
                  <div class="wing-box-title"><span>🎙️ 선생님의 집필 시범</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>개요표의 짧은 메모를 어떻게 읽는 이가 이해하기 쉬운 문단으로 살을 붙일까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>➊문단에서 ‘음식물류 폐기물’은 정의 문장으로 풀었고, ‘온실가스’와 ‘편식’ 뒤에는 괄호로 예상 독자(친구들)를 위한 <strong>뜻풀이</strong>를 넣었어! 또 ➋문단에서는 <strong>[원그래프 1]을 살펴보면</strong>이라는 지시문으로 그래프와 본문을 하나로 엮었지.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>이제 여러분이 이어서 <strong>➌문단(가운데 2)</strong>과 <strong>➍문단(끝)</strong>을 완성해 볼 차례야!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "초고 집필에 사용할 ‘학술 어휘 뜻풀이 문장’과 ‘시각 자료 지시 문장’ 조립하기",
            "tag": "Step 1 핵심 문장 부품(정의·뜻풀이·도표 지시문) 조립",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:24%;">집필 전략 요소</th>
                  <th style="width:76%;">내 설명문 초고에 넣을 문장 부품 완성하기</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">① 학술 복합어 뜻풀이<br>(5차시·8차시 전략)</td>
                  <td>• 설명할 용어: <strong>자율 배식(自律配食)</strong><br>• 뜻풀이 문장: ‘자율 배식대’란 <span class="blank-slot"><span class="t-ans">학생 스스로(자율) 자신이 먹을 수 있는 알맞은 양만큼만 음식을 덜어 가는 배식 공간</span></span>을 말한다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">② 거시 지시어 + 중심문장<br>(6차시·14차시 전략)</td>
                  <td>• ➌문단(가운데 2) 첫 문장: <span class="blank-slot"><span class="t-ans">이러한 음식물 쓰레기 문제를 해결하기 위해서는</span></span> 발생 원인에 맞춘 두 가지 방안이 시행되어야 한다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">③ 시각자료 지시문 + 출처<br>(7차시·9차시 전략)</td>
                  <td>• [막대그래프 2] 연결 문장: 실제로 <span class="blank-slot"><span class="t-ans">한국환경공단(2024)의 [막대그래프 2]에서 확인할 수 있듯이</span></span>, 시범 학교의 1인당 잔반량이 평균 <span class="blank-slot"><span class="t-ans">28.4% 감소</span></span>했다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 조립한 문장 부품들과 보조 시각 자료 도표를 결합하여 본론·결론 문단 구성하기",
        "activity_2": {
            "title": "본문 초고 옆에 배치할 ‘보조 시각 자료 2종([원그래프 1], [막대그래프 2])’ 완성하기",
            "tag": "Step 2 텍스트-시각자료 멀티모달 통합 배치",
            "body_html": """
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:6px; font-size:7pt;">
              <div style="background:#F8FBFE; border:0.8pt solid #5DADE2; border-radius:4px; padding:4px 6px;">
                <div style="font-weight:800; color:#1A5276;">📊 [원그래프 1] 우리 학교 급식 잔반 발생 이유 (단위: %)</div>
                <div style="margin-top:2px;">• 1위: 배식받은 양이 너무 많아서 — <span class="blank-slot"><span class="t-ans">52.0%</span></span> (218명)</div>
                <div>• 2위: 좋아하지 않는 반찬이어서(편식) — <span class="blank-slot"><span class="t-ans">35.0%</span></span> (147명)</div>
                <div>• 3위: 간이 맞지 않아서(9.0%) / 기타(4.0%)</div>
                <div style="font-size:6.5pt; color:#566573; margin-top:2px;">* 출처: <span class="blank-slot"><span class="t-ans">한빛초 6학년 학생회 자치부(2026. 5., 420명 조사)</span></span></div>
              </div>
              <div style="background:#F9FBF9; border:0.8pt solid #58D68D; border-radius:4px; padding:4px 6px;">
                <div style="font-weight:800; color:#196F3D;">📈 [막대그래프 2] 자율 배식·맞춤 조리 도입 전후 잔반량 (단위: %)</div>
                <div style="margin-top:2px;">• 도입 전 1인당 잔반량 기준: <strong>100.0%</strong></div>
                <div>• 도입 후 1인당 잔반량: <span class="blank-slot"><span class="t-ans">71.6% (-28.4% 감소 ↓)</span></span></div>
                <div style="font-size:6.5pt; color:#566573; margin-top:4px;">* 출처: <span class="blank-slot"><span class="t-ans">한국환경공단·국립환경과학원(2024, 150개교 조사)</span></span></div>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "좌측의 ➊~➋문단에 이어, [활동 1~2]를 모두 통합하여 ➌문단(가운데 2)과 ➍문단(끝) 초고를 완성하기",
        "activity_3": {
            "title": "소제목, 거시 지시어, 학술어 뜻풀이, 시각자료 지시문을 넣어 복합 설명문 초고 완성하기",
            "tag": "Step 3 완결된 복합 설명문 초고 산출",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>과제</strong>: 좌측 페이지의 ➊~➋문단에 이어지는 <strong>➌문단(가운데 2: 소제목 2 포함)</strong>과 <strong>➍문단(끝: 요약 및 전망)</strong>을 객관적인 설명 어조(`~이다, ~한다`)로 집필하여 한 편의 설명문을 완성해 보세요. *(자신이 선택한 다른 주제로 전체 초고를 써도 좋습니다.)*</div>
              <span class="pencil-line">✏️ <strong>[소제목 2]</strong>: <span class="t-ans">음식물 쓰레기를 줄이는 맞춤형 해결 방안</span></span>
              <span class="pencil-line">✏️ <strong>[➌문단: 거시 지시어 + 해결 방안 ①·② + 학술어 뜻풀이 + 막대그래프 2 지시문]</strong>: <span class="t-ans">이러한 음식물 쓰레기 문제를 해결하기 위해서는 발생 원인에 맞춘 두 가지 방안이 시행되어야 한다. 먼저 양 조절 문제를 해결하기 위해 학생 스스로 먹을 만큼만 음식을 덜어 가는 ‘자율 배식대’를 운영하는 방법이 있다. 다음으로 편식 문제를 줄이기 위해 매달 급식 선호도 조사를 실시하여 채소를 잘게 다져 넣는 등 조리법을 개선하는 대안이 효과적이다. 실제로 한국환경공단(2024)의 [막대그래프 2]에서 확인할 수 있듯이, 자율 배식대와 맞춤 조리법을 도입한 시범 학교에서는 1인당 잔반량이 평균 28.4퍼센트나 감소했다.</span></span>
              <span class="pencil-line">✏️ <strong>[➍문단: 끝 — 복합 구조 요약 및 전망]</strong>: <span class="t-ans">이처럼 급식실 음식물 쓰레기는 과다 배식과 편식 습관 때문에 발생하지만, 자율 배식대 운영과 선호도 맞춤 조리법 개선을 통해 효과적으로 줄일 수 있다. 학교 구성원 모두가 알맞은 양을 덜어 먹는 습관을 실천한다면 소중한 식자원을 아끼고 온실가스 배출도 크게 줄여 건강한 지구 환경을 지켜 나갈 수 있을 것이다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "16차시(W5 고쳐쓰기: 내용·조직·표현 3단계 퇴고) 직결",
            "prompt": "오늘 쓴 내 초고를 다시 읽어 보며, 혹시 ‘주어와 서술어의 호응’이 어색하거나 ‘내 개인 감정’이 섞인 문장은 없는지 퇴고 메모를 남겨 보세요.",
            "placeholder": "(예: ‘원인은 ~ 배식받는다’라고 쓴 문장을 다음 시간에 ‘원인은 ~ 배식받기 때문이다’로 고쳐야겠다.)",
            "example_answer": "점검 메모: 1. ‘원인은 ~ 때문이다’ 주어-서술어 호응 확인하기, 2. [원그래프 1]과 [막대그래프 2]의 출처 표기 누락 없는지 확인하기, 3. 주관적 주장 표현 삭제하기",
        },
        "self_check": [
            "본제목과 소제목을 갖추고 각 문단을 ‘중심문장 - 뒷받침 설명·수치 문장’의 위계로 썼나요?",
            "어려운 학술 어휘에 예상 독자를 배려한 친절한 뜻풀이를 덧붙이고, 시각 자료 지시문과 출처를 본문에 통합했나요?",
            "개인적인 감정이나 편견을 빼고 끝까지 객관적이고 공식적인 설명 어조(`~이다, ~한다`)를 유지했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 복합 설명문 초고 집필 5대 체크포인트(W4): ① `[핵심 대상]+[설명 측면]` 본제목 & 소제목, ② 문단별 `[두괄식 중심문장 ➔ 설명·수치·예시 뒷받침문장]` 위계, ③ 학술 어휘 독자 맞춤형 뜻풀이(괄호·재진술), ④ 시각 자료 지시문(`“[그래프 2]에서 보듯이”`) + 출처 통합, ⑤ 공식적·객관적 설명 어조(`~이다, ~한다`) 일관성.",
            "intro_5min": "12차시(계획), 13차시(자료 수집·도표 기획), 14차시(다층 개요)를 거쳐 드디어 나만의 설명문 초고를 완성하는 **15차시 집필하기** 시간입니다! 개요표의 뼈대에 살을 붙여 독자가 고개를 끄덕이며 읽을 수 있는 명품 설명문을 집필해 봅시다.",
            "ido_think_aloud_script": "“선생님이 좌측 페이지의 ➊~➋문단을 어떻게 집필했는지 비법을 공개할게요. 첫째, ➊문단에서 ‘음식물 쓰레기’와 ‘온실가스’, ➋문단에서 ‘편식’이라는 한자 학술어가 나올 때마다 바로 뒤에 ‘~란 ~을 말한다’ 또는 괄호 `(지구의 기온을 높이는 기체)`를 넣어 예상 독자인 친구들이 막힘없이 읽도록 배려했어요(5·8차시 전략). 둘째, 그래프를 그냥 옆에 두지 않고 ➋문단 가운데에 ‘6학년 학생회가 2026년 5월 전교생 420명을 대상으로 조사한 [원그래프 1]을 살펴보면’이라는 다리 문장(지시문)을 놓아 본문과 그래프를 하나로 엮었답니다(7·9차시 전략). 자, 이제 여러분이 이 배턴을 이어받아 ➌문단(해결 방안)과 ➍문단(맺음말)을 완성해 볼까요?”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "➌문단(가운데 2)을 시작할 때 ➋문단의 원인 두 가지를 자연스럽게 이어받으면서 해결 방안을 제시하는 ‘두괄식 중심문장’은 어떻게 쓰면 좋을까요?",
                    "expected_ans": "거시 지시어를 맨 앞에 넣어 “이러한 음식물 쓰레기 문제를 해결하기 위해서는 발생 원인에 맞춘 두 가지 방안이 시행되어야 한다.”라고 쓰면 앞 문단과의 응집성도 높아지고 문단의 중심 생각도 또렷해집니다.",
                    "reprompt": "[활동 1]의 ②번 칸에 있는 거시 지시어구(‘이러한 ~ 문제를 해결하기 위해서는’)로 문장을 시작해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "초고를 쓰다가 “반찬을 남기는 친구들은 정말 얄밉고 나쁘다”라거나 “우리 모두 무조건 반찬을 다 먹자!”라고 쓰면 왜 안 될까요?",
                    "expected_ans": "설명문은 독자에게 객관적인 원리와 해결 방법을 알려 주는 글이므로, 감정적인 비난이나 논설문 같은 명령·청유형 문장(‘~자!’) 대신 ‘~하는 방법이 있다, ~효과가 나타난다’ 같은 객관적 설명 어조를 유지해야 합니다.",
                    "reprompt": "설명문의 끝맺음 어미(`~이다, ~한다`)와 주장·감상문의 어미를 비교해 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 학술어 뜻풀이·거시 지시어·도표 지시문 부품을 조립하고, [활동 2]에서 시각 자료 2종을 완성한 뒤, [활동 3]에서 ➌~➍문단(또는 개인 주제의 전체 초고)을 집필하도록 순회 지도한다. 다음 시간(16차시 W5)에 오늘 쓴 초고를 교정부호로 다듬어 학급 백과사전으로 출판할 것임을 안내한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 핵심 문장 부품 조립</strong>: ① <strong>학생 스스로(자율) 자신이 먹을 수 있는 알맞은 양만큼만 음식을 덜어 가는 배식 공간</strong> / ② <strong>이러한 음식물 쓰레기 문제를 해결하기 위해서는</strong> / ③ <strong>한국환경공단(2024)의 [막대그래프 2]에서 확인할 수 있듯이</strong>, <strong>28.4% 감소</strong><br>
              <strong>2. [활동 2] 보조 시각 자료 완성</strong>: [원그래프 1] <strong>52.0%</strong>, <strong>35.0%</strong>, 출처: <strong>한빛초 6학년 학생회 자치부(2026. 5., 420명 조사)</strong> / [막대그래프 2] <strong>71.6% (-28.4% 감소 ↓)</strong>, 출처: <strong>한국환경공단·국립환경과학원(2024, 150개교 조사)</strong><br>
              <strong>3. [활동 3] 초고 집필 산출 (인정 답안 기준)</strong>: (1) 소제목 제시, (2) 거시 지시어 및 담화 표지(`먼저, 다음으로, 이처럼`) 사용, (3) 학술어 뜻풀이 1개 이상 포함, (4) `[막대그래프 2]` 지시문 및 출처·수치(28.4% 감소) 통합, (5) 객관적 설명 어조(`~이다, ~한다`) 일관성 유지의 5대 준거를 충족하면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "한 문단은 `~합니다`로 쓰고 다음 문단은 `~한다`로 써서 문체(어조)의 일관성이 깨지는 오류",
                    "diagnosis": "글 전체에서 종결 어미의 높임 등급(해라체 vs 하십시오체)을 통일해야 한다는 공식적 문체 규칙을 놓침.",
                    "prescription": "예상 독자와 글의 성격에 맞추어 `~이다, ~한다`(백과사전·보고서체) 또는 `~입니다, ~합니다`(친절한 안내서체) 중 하나를 정하면 첫 문단부터 끝 문단까지 하나로 통일하도록 지도한다.",
                },
                {
                    "error_case": "개요표의 메모 조각들을 접속어나 지시어 없이 마침표로만 뚝뚝 끊어 나열하는 오류",
                    "diagnosis": "개요의 명사구 메모를 문장 간 응집 장치(담화 표지)로 엮어 내는 문장화 기술이 부족함.",
                    "prescription": "중심문장 뒤에 `첫째 ~기 때문이다. 둘째 ~탓에`, 해결 방안 앞에 `먼저 ~ 방법이 있다. 다음으로 ~ 대안이 효과적이다.`라는 접속 틀을 넣어 문장들을 매끄럽게 이어 주게 한다.",
                },
            ],
            "scaffolding_down": "긴 문단 집필에 부담을 느끼는 학습자에게는 [활동 1]에서 완성한 세 문장 부품을 순서대로 이어 붙인 뒤 가운데에 해결 방안 두 번째 문장만 추가하면 ➌문단이 완성되도록 ‘문장 블록 조립 가이드’를 제공한다.",
            "scaffolding_up": "심화 학습자에게는 자신이 개별적으로 선택한 과학·환경 주제(예: 산호초 백화 현상, 스마트 팜, 도시 열섬)로 5문단 이상의 전체 설명문 초고를 독립적으로 집필하게 하고, 전문 학술어 3개 이상에 형태소 분석 뜻풀이를 넣도록 도전 과제를 부여한다.",
            "rubric": {
                "high": "본제목과 소제목, 문단별 중심-뒷받침 위계, 학술 어휘 뜻풀이, 시각 자료 지시문 및 출처 표기, 객관적 설명 어조의 5대 준거를 모두 충족하여 완결된 복합 설명문 초고를 집필함.",
                "mid": "개요에 따라 초고를 완성하고 시각 자료를 언급했으나, 학술 어휘에 대한 친절한 뜻풀이가 부족하거나 어조(`~이다/~입니다`)가 일부 혼용됨.",
                "low": "중심문장과 뒷받침문장의 구분이 모호하고 시각 자료 지시문이나 출처 표기가 누락되어 초고 보완이 필요함.",
            },
        },
    },

    # =========================================================================
    # 16차시: G6-EXP-W5 고쳐쓰기 (내용·조직·표현[주술/부사어 호응·교정부호] 3단계 퇴고 및 출판)
    # =========================================================================
    {
        "lesson_no": 16,
        "code": "G6-EXP-W5",
        "lesson_title": "[고쳐쓰기] 내용·조직·표현(문장 호응·교정부호) 3단계로 퇴고하여 출판하기",
        "std_badge": "[6국03-05] · [6국04-05] · CCSS W.6.5, L.6.1",
        "student_goal": "초고에서 주관적 표현과 출처 누락(내용), 담화 표지·도표 지시문 오류(조직), 주어-서술어 및 부사어-서술어 호응 오류(`[6국04-05]`, 표현)를 찾아 표준 교정부호로 고쳐 쓰고 학급 백과사전으로 출판할 수 있다.",
        "marking_items": [
            ["mk-line-red", "빨간 밑줄", "주어-서술어·부사어 호응 오류([6국04-05]) 및 비문"],
            ["mk-dotted", "점선 밑줄", "삭제해야 할 주관적 일화·설득 주장·잉여 표현"],
            ["mk-line-blue", "파란 밑줄", "교정부호로 추가·수정한 정확한 설명 표현·담화 표지"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.8pt; font-weight:800; color:#1A5276; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span>🛠️ [쓰기 스튜디오 5단계: 고쳐쓰기] 2층 고행간 첨삭 줄공책 &amp; 3단계 교정부호 퇴고</span>
          <span style="font-size:6.7pt; color:#566573;">핵심 문법: [6국04-05] 주어-서술어 호응(`원인은 ~ 때문이다`) · 부사어-서술어 호응(`결코 ~ 않다`)</span>
        </div>

        <!-- 2층 고행간 첨삭 줄공책 (.draft-revision-grid) -->
        <div class="draft-revision-grid" style="margin-bottom:5px;">
          <div class="notebook-pane">
            <!-- 제목 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">제목<br>점검</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ 우리 학교 급식실의 음식물 [교정: 포괄적 제목으로 구체화] ∨ 발생 원인과 줄이기 방안</div>
                  <div class="nb-lower-write">제목: <span class="mk-line-red">쓰레기 문제</span></div>
                </div>
              </div>
            </div>

            <!-- 1문단 블록 (내용: 주관적 일화 삭제 & 개념 정의 추가) -->
            <div class="nb-para-block">
              <div class="nb-para-tag">➊문단<br>(처음)</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ 버려지는 음식물 쓰레기가 급격히 늘어나는 문제에 직면해 있다. [교정: 객관적 어조]</div>
                  <div class="nb-lower-write">최근 우리 학교 급식실에서는 <span class="mk-line-red">음식물 쓰레기가 너무 많이 나와서 큰일이다.</span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">─── [교정부호: 삭제(돼지꼬리)] ➔ ∨ 음식물 쓰레기란 식사 후 버려지는 남은 음식물을 말한다.(정의 추가)</div>
                  <div class="nb-lower-write"><span class="mk-dotted">어제도 나는 급식실에서 시금치 반찬이 맛없어서 남겼다.</span></div>
                </div>
              </div>
            </div>

            <!-- 2문단 블록 (표현: 주술 호응 [6국04-05] & 조직: 담화표지·당위주장 삭제) -->
            <div class="nb-para-block">
              <div class="nb-para-tag">➋문단<br>(원인)</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ 원인은 크게 두 가지이다. 첫째, [교정: 주어 ‘이유는/원인은’ ↔ 서술어 ‘~기 때문이다’ 호응!]</div>
                  <div class="nb-lower-write">음식물 쓰레기가 생기는 <span class="mk-line-red">이유는</span> 학생들이 먹을 양보다 음식을 너무 많이</div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ 배식받기 때문이다(52%). 둘째, [교정: 접속어 ‘그리고’ ➔ 나열·인과 표지 ‘둘째, ~탓에’]</div>
                  <div class="nb-lower-write"><span class="mk-line-red">배식받는다. 그리고</span> 편식 때문에 채소 반찬을 먹지 않고 버린다(35%).</div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">─── [교정부호: 삭제] (설득문식 주관적 주장 배제!)</div>
                  <div class="nb-lower-write"><span class="mk-dotted">내 생각에는 채소를 남기는 학생들에게 무조건 벌점을 주어야만 한다.</span></div>
                </div>
              </div>
            </div>

            <!-- 3문단 블록 (조직: 시각자료 지시문·출처 추가 & 거시지시어·부사어 호응 교정) -->
            <div class="nb-para-block">
              <div class="nb-para-tag">➌문단<br>(해결)</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ [막대그래프 2](한국환경공단, 2024)에서 보듯이, 이러한 음식물 쓰레기 문제를 [거시지시어 구체화]</div>
                  <div class="nb-lower-write"><span class="mk-line-red">이것을</span> 해결하려면 스스로 먹을 만큼 덜어 먹는 ‘자율 배식대’를 운영하고,</div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">∨ 결코 줄어들지 않을 것이다.(또는 ‘반드시 줄어들 것이다’) [교정: 부사어 ‘결코’ ↔ 부정 서술어 호응!]</div>
                  <div class="nb-lower-write">선호도 조사를 거쳐 조리법을 바꾸어야 한다. 노력하지 않으면 잔반은 <span class="mk-line-red">결코 줄어들 것이다.</span></div>
                </div>
              </div>
            </div>
          </div>

          <!-- 우측 날개: 3단계 퇴고 & 표준 교정부호 가이드 -->
          <div style="padding:5px 6px; background:#F8F9F9; font-size:7pt; line-height:1.36; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-weight:800; color:#1A5276; margin-bottom:3px; border-bottom:1pt solid #BDC3C7; padding-bottom:2px;">🔍 설명문 3단계 퇴고 돋보기</div>
              <div style="margin-bottom:3px;"><strong style="color:#B03A2E;">1단계 [내용 수준]</strong><br>• 개인적 일화·감상·설득 주장 삭제<br>• 핵심 개념 정의·출처·단위 보충</div>
              <div style="margin-bottom:3px;"><strong style="color:#196F3D;">2단계 [조직 수준]</strong><br>• 포괄적 제목·소제목 점검<br>• 모호한 지시어(`이것`) ➔ 거시 지시어(`이러한 문제를`)로 교체<br>• 도표 본문 지시문 추가</div>
              <div><strong style="color:#1A5276;">3단계 [표현 수준 (`[6국04-05]`)]</strong><br>• <strong>주술 호응</strong>: <code>원인은 ~ 때문이다</code><br>• <strong>부사어 호응</strong>: <code>결코/절대로 ~ 않다</code>, <code>비록 ~하더라도</code></div>
            </div>
            <div style="background:#FFFFFF; border:0.7pt solid #BDC3C7; border-radius:4px; padding:3.5px 5px; font-size:6.7pt;">
              <strong>✏️ 주요 교정부호</strong><br>
              • <code>───(돼지꼬리)</code>: <strong>삭제(빼기)</strong><br>
              • <code>∨</code>: <strong>추가(넣기)</strong><br>
              • <code>═(두 줄) + ∨</code>: <strong>고치기(대체)</strong><br>
              • <code>[~](물결)</code>: <strong>자리 바꾸기</strong><br>
              • <code>¶</code>: <strong>줄 바꿈(문단 나누기)</strong>
            </div>
          </div>
        </div>
        """,
        "activity_1": {
            "title": "3단계 퇴고 기준(내용·조직·표현)으로 초고의 결함과 교정부호 연결하기",
            "tag": "Step 1 내용·조직·표현 오류 진단",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">퇴고 층위</th>
                  <th style="width:42%;">좌측 줄공책 초고에서 발견한 문제점</th>
                  <th style="width:40%;">적용할 교정부호 및 퇴고 방법</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">① 내용 수준<br>(객관성·정확성)</td>
                  <td>• ➊문단: “어제도 시금치 반찬을 남겼다” (개인 일화)<br>• ➋문단: “벌점을 주어야만 한다” (주관적 주장)</td>
                  <td>• 적용 부호: <span class="blank-slot"><span class="t-ans">삭제(빼기) 부호</span></span> 및 <span class="blank-slot"><span class="t-ans">추가(넣기: ∨)</span></span><br>• 방법: 일화·주장을 빼고 ‘음식물 쓰레기’의 <strong>개념 정의</strong>와 <strong>통계 출처</strong>를 넣는다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">② 조직 수준<br>(제목·응집성·도표)</td>
                  <td>• 제목: ‘쓰레기 문제’ (너무 넓음)<br>• ➌문단: ‘이것을 해결하려면’ (지시 대상 모호, 도표 언급 누락)</td>
                  <td>• 적용 부호: <span class="blank-slot"><span class="t-ans">고치기 및 넣기(∨) 부호</span></span><br>• 방법: 포괄적 제목으로 고치고, `이것을`을 <span class="blank-slot"><span class="t-ans">이러한 음식물 쓰레기 문제를</span></span>로 바꾸며 도표 지시문을 넣는다.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">③ 표현 수준<br>(`[6국04-05]` 호응)</td>
                  <td>• ➋문단: “생기는 <strong>이유는</strong> ~ 많이 <strong>배식받는다.</strong>”<br>• ➌문단: “잔반은 <strong>결코 줄어들 것이다.</strong>”</td>
                  <td>• 적용 부호: <span class="blank-slot"><span class="t-ans">고치기(대체) 부호</span></span><br>• 방법: 주어-서술어 호응과 부사어-서술어 호응이 맞도록 서술어를 고친다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 찾은 ‘표현 수준(`[6국04-05]` 문장 성분 호응)’ 오류를 정밀하게 교정하는 연습하기",
        "activity_2": {
            "title": "설명문에서 자주 틀리는 ‘주어-서술어 호응’과 ‘부사어-서술어 호응(`[6국04-05]`)’ 바르게 고치기",
            "tag": "Step 2 문장 성분 호응([6국04-05]) 정밀 교정",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">호응 오류 유형</th>
                  <th style="width:39%;">호응이 어긋난 문장 (비문 ❌)</th>
                  <th style="width:39%;">바르게 고쳐 쓴 문장 (정문 ⭕)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1A5276;">① 주어 - 서술어<br>호응 오류</td>
                  <td>급식실 음식물 쓰레기가 발생하는 <strong>원인은(이유는)</strong> 학생들이 음식을 너무 많이 <strong>배식받는다.</strong></td>
                  <td>급식실 음식물 쓰레기가 발생하는 <strong>원인은</strong> 학생들이 음식을 지나치게 많이 <span class="blank-slot"><span class="t-ans">배식받기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">② 부사어 - 서술어<br>호응 오류 (부정)</td>
                  <td>우리가 노력하지 않으면 환경 오염 문제는 <strong>결코(절대로)</strong> 해결될 <strong>것이다.</strong></td>
                  <td>우리가 노력하지 않으면 환경 오염 문제는 <strong>결코</strong> <span class="blank-slot"><span class="t-ans">해결되지 않을 것이다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">③ 부사어 - 서술어<br>호응 오류 (비유·양보)</td>
                  <td>• 도심의 뜨거운 공기는 <strong>마치</strong> 열기의 <strong>섬이다.</strong><br>• <strong>비록</strong> 크기가 작은 파편이지만 위성을 파괴한다.</td>
                  <td>• 도심의 뜨거운 공기는 <strong>마치</strong> 열기의 <span class="blank-slot"><span class="t-ans">섬과 같다(섬처럼 보인다).</span></span><br>• <strong>비록</strong> 크기가 작은 <span class="blank-slot"><span class="t-ans">파편일지라도(파편이라 하더라도)</span></span> 위성을 파괴한다.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 1~2]의 3단계 퇴고를 모두 반영하여 ‘학급 과학·시사 백과사전’에 실을 최종 완성본 출판하기",
        "activity_3": {
            "title": "3단계 퇴고를 마친 ‘나의 복합 설명문 최종 완성본’ 작성 및 출판하기",
            "tag": "Step 3 최종 수정본 산출 및 출판",
            "body_html": """
            <div style="font-size:7.3pt; line-height:1.45;">
              <div><strong>📘 [학급 과학·시사 백과사전 최종 원고]</strong> 좌측 줄공책의 교정 내역(또는 15차시 내 초고의 퇴고 내역)을 모두 반영하여, 제목·정의·원인·해결 방안·시각자료 지시문·문장 호응이 완벽한 최종 설명문을 완성해 보세요.</div>
              <span class="pencil-line">✏️ <strong>[최종 제목]</strong>: <span class="t-ans">우리 학교 급식실의 음식물 쓰레기 발생 원인과 줄이기 방안</span></span>
              <span class="pencil-line">✏️ <strong>[➊~➋문단 (정의·원인·원그래프 1 연동)]</strong>: <span class="t-ans">최근 우리 학교 급식실은 버려지는 음식물 쓰레기가 늘어나는 문제에 직면해 있다. 음식물 쓰레기란 조리 과정이나 식사 후에 먹지 않고 버려지는 남은 음식물을 말한다. 6학년 학생회 설문 결과([원그래프 1], 2026)를 살펴보면, 음식물 쓰레기가 발생하는 원인은 크게 두 가지이다. 첫째, 학생들이 먹을 수 있는 양을 고려하지 않고 음식을 지나치게 많이 배식받기 때문이다(52.0%). 둘째, 채소나 생선을 기피하는 편식 습관 탓에 반찬을 그대로 남기는 경우가 많다(35.0%).</span></span>
              <span class="pencil-line">✏️ <strong>[➌~➍문단 (거시 지시어·해결 방안·막대그래프 2 연동·맺음말)]</strong>: <span class="t-ans">이러한 음식물 쓰레기 문제를 해결하기 위해서는 원인에 맞는 두 가지 방안이 시행되어야 한다. 먼저 양 조절 문제를 해결하기 위해 스스로 먹을 만큼만 덜어 먹는 ‘자율 배식대’를 운영하는 방법이 있다. 다음으로 편식 문제를 줄이기 위해 선호도 조사를 거쳐 조리법을 개선하는 대안이 효과적이다. 한국환경공단(2024)의 [막대그래프 2]에서 보듯이 두 방안을 도입한 학교에서는 잔반량이 28.4% 감소했다. 우리가 알맞게 덜어 먹는 습관을 실천하지 않으면 잔반은 결코 줄어들지 않을 것이므로 모두의 꾸준한 노력이 필요하다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "4단원(설명문) 총괄 갈무리 ➔ 5단원(논설문) 연결",
            "prompt": "4단원 ‘설명문’ 16차시를 모두 마쳤습니다! 복잡한 과학·사회 현상을 설명하는 글을 읽고 쓸 때 가장 중요하다고 느낀 나만의 핵심 원칙 한 문장을 남겨 보세요.",
            "placeholder": "(예: 정확한 출처와 통계, 탄탄한 설명 구조, 그리고 독자를 배려한 친절하고 객관적인 표현이 핵심이다!)",
            "example_answer": "좋은 설명문은 공신력 있는 출처의 사실과 시각 자료를 교차 검증하고, 독자의 눈높이에 맞는 설명 구조와 정확한 문장 호응으로 객관적 지식을 전달하는 글이다.",
        },
        "self_check": [
            "내용 수준에서 주관적 일화·감상·설득 주장을 삭제하고 개념 정의와 정확한 출처를 보충했나요?",
            "조직 수준에서 포괄적 제목, 문단 간 거시 지시어(‘이러한 문제를~’), 시각 자료 본문 지시문을 바르게 고쳤나요?",
            "표현 수준(`[6국04-05]`)에서 주어-서술어 호응(‘원인은 ~ 때문이다’)과 부사어-서술어 호응(‘결코 ~ 않다’) 오류를 100% 교정했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[좌측 판서] 설명문 3단계 메타인지 퇴고 사다리(W5): **1단계 내용**(주관적 일화·당위 주장 삭제 + 정의·출처 추가) ➔ **2단계 조직**(포괄적 제목 + 거시 지시어 `이러한 문제를` + 도표 지시문 추가) ➔ **3단계 표현(`[6국04-05]`)**(주술 호응 `원인은 ~ 때문이다` + 부사어 호응 `결코 ~ 않다, 마치 ~ 같다, 비록 ~일지라도`) / [우측 판서] 표준 교정부호 5종 실연 및 학급 백과사전 출판회.",
            "intro_5min": "훌륭한 작가들은 초고를 쓴 뒤 반드시 ‘고쳐쓰기(퇴고)’ 과정을 거쳐 글을 보석처럼 다듬습니다. 오늘 4단원 대장정의 마지막 16차시에서는 2층 첨삭 줄공책을 활용해 **내용·조직·표현(문장 성분 호응 `[6국04-05]`) 3단계 퇴고**를 완수하고 학급 백과사전을 출판합니다!",
            "ido_think_aloud_script": "“선생님이 좌측 페이지의 ‘2층 고행간 첨삭 줄공책’을 보며 어떻게 3단계로 고쳐 쓰는지 시범을 보일게요. 먼저 1단계 ‘내용’을 볼까요? ➊문단에 ‘어제도 나는 시금치 반찬을 남겼다’라는 개인 일화와 ➋문단에 ‘무조건 벌점을 주어야만 한다’라는 설득문식 주장이 들어 있네요. 설명문의 객관성을 해치므로 돼지꼬리 삭제 부호(───)로 과감히 지우고, 대신 ∨(넣기 부호)로 ‘음식물 쓰레기의 개념 정의’를 넣습니다! 다음 2단계 ‘조직’을 볼까요? 제목 ‘쓰레기 문제’는 너무 넓으니 구체화하고, ➌문단 첫머리의 모호한 ‘이것을’은 거시 지시어 ‘이러한 음식물 쓰레기 문제를’로 고칩니다. 마지막 3단계 ‘표현(`[6국04-05]`)’이 가장 중요해요! ➋문단에 ‘쓰레기가 생기는 이유는 ~ 음식을 너무 많이 배식받는다’라고 되어 있죠? 주어가 ‘이유는(원인은)’이면 서술어는 반드시 ‘~기 때문이다’로 호응해야 바른 문장이 됩니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "좌측 줄공책 ➌문단 마지막 줄의 “노력하지 않으면 잔반은 결코 줄어들 것이다.”라는 문장은 왜 어색하며 어떻게 고쳐야 할까요? (`[6국04-05]` 부사어-서술어 호응)",
                    "expected_ans": "‘결코(또는 절대로, 전혀)’라는 부정 부사어는 반드시 뒤에 ‘~지 않다, ~지 못하다’ 같은 부정 서술어와 짝을 이루어야 합니다. 따라서 “잔반은 결코 줄어들지 않을 것이다.”라고 고치거나, 긍정 서술어를 살리려면 부사어를 바꾸어 “노력한다면 잔반은 반드시 줄어들 것이다.”라고 고쳐야 합니다.",
                    "reprompt": "‘결코, 절대로, 비록, 마치’처럼 뒤에 오는 서술어 짝꿍이 정해져 있는 부사어들의 호응 규칙([활동 2] ②·③번)을 확인해 보세요.",
                },
                {
                    "qar_type": "글쓴이와 나 (Author & You)",
                    "question": "➋문단에서 첫 번째 원인과 두 번째 원인을 연결할 때 초고의 ‘그리고’보다 ‘첫째 ~기 때문이다. 둘째 ~탓에’로 고치면 독자에게 어떤 점이 더 좋을까요?",
                    "expected_ans": "‘그리고’는 단순 나열이라 문장 관계가 흐릿하지만, ‘첫째 ~ 둘째’와 ‘~기 때문이다 / ~탓에’라는 담화 표지를 쓰면 독자가 두 가지 발생 원인을 번호순으로 명확히 구분하며 인과 관계를 쉽게 파악할 수 있습니다.",
                    "reprompt": "3차시와 14차시에서 배운 ‘담화 표지(나침반)’의 효과를 떠올려 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생 스스로 [활동 1]에서 3단계 퇴고 내역을 정리하고, [활동 2]에서 주술 호응·부사어 호응(`[6국04-05]`) 문장 교정 연습을 완수한 뒤, [활동 3]에서 최종 수정본을 작성하도록 지도한다. 완성된 글들을 모아 ‘6학년 우리 반 과학·시사 백과사전’으로 묶어 전시하고, 다음 5단원(논설문)과의 차이점을 환기하며 4단원 전체 수업을 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.42;">
              <strong>1. [활동 1] 3단계 퇴고 진단</strong>: ① 내용: <strong>삭제(빼기) 부호</strong>, <strong>추가(넣기: ∨)</strong> / ② 조직: <strong>고치기 및 넣기(∨) 부호</strong>, <strong>이러한 음식물 쓰레기 문제를</strong> / ③ 표현: <strong>고치기(대체) 부호</strong><br>
              <strong>2. [활동 2] 문장 성분 호응([6국04-05]) 교정</strong>: ① 주어-서술어: <strong>배식받기 때문이다.</strong> / ② 부사어(결코): <strong>해결되지 않을 것이다.</strong> / ③ 부사어(마치/비록): <strong>섬과 같다(섬처럼 보인다).</strong>, <strong>파편일지라도(파편이라 하더라도)</strong><br>
              <strong>3. [활동 3] 최종 완성본 산출 (인정 답안 기준)</strong>: (1) 내용: 개인 일화·당위 주장 삭제 및 정의·출처 포함, (2) 조직: 포괄적 제목, 담화 표지(`첫째~둘째, 먼저~다음으로`), 거시 지시어(`이러한 문제를`), 도표 지시문(`[원그래프 1], [막대그래프 2]`) 완비, (3) 표현: 주술 호응(`원인은 ~ 때문이다`) 및 부사어 호응(`결코 ~ 않을 것이다`)이 100% 정확한 문장으로 작성되면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "고쳐쓰기(퇴고)를 ‘글씨를 지우개로 지워 깨끗하게 다시 베껴 쓰는 것’이나 ‘맞춤법·띄어쓰기만 고치는 것’으로 좁게 생각하는 오개념",
                    "diagnosis": "표면적인 철자 교정(Proofreading)과 글의 내용·조직·문장 호응을 재구조화하는 과정중심 퇴고(Revising)를 혼동함.",
                    "prescription": "맞춤법은 가장 마지막(3단계 끝)에 보는 것이며, 진짜 퇴고는 **1단계 내용(객관성·출처)** ➔ **2단계 조직(통일성·거시 지시어·도표 연결)** ➔ **3단계 표현(주술·부사어 호응)**의 순서로 위에서 아래로 점검하는 것임을 강조한다.",
                },
                {
                    "error_case": "“내가 설명하려는 핵심은 ~라는 점이다 / 원인은 ~기 때문이다”에서 앞의 주어(‘핵심은 / 원인은’)를 잊어버리고 문장 끝을 ‘~한다’로 끝내는 오류",
                    "diagnosis": "안긴문장이 길어질수록 문장 맨 앞의 주어와 맨 끝의 서술어 사이의 통사적 거리가 멀어져 호응 감각을 잃어버림.",
                    "prescription": "문장이 길 때는 맨 앞의 주어(`원인은`)와 맨 끝의 서술어(`때문이다`)만 먼저 밑줄 그어 둘만 붙여 읽어 보게 하는 ‘주어-서술어 직결 점검법’을 훈련시킨다.",
                },
            ],
            "scaffolding_down": "주어-서술어 및 부사어-서술어 호응 찾기를 어려워하는 학습자에게는 ‘호응 짝꿍 스티커 카드’(`원인은/이유는 ↔ ~기 때문이다`, `결코/절대로 ↔ ~지 않다`, `비록 ↔ ~하더라도`, `마치 ↔ ~처럼/같다`, `왜냐하면 ↔ ~때문이다`)를 책상 옆에 두고 대조하며 고치게 돕는다.",
            "scaffolding_up": "심화 학습자에게는 짝과 서로의 초고를 바꾸어 읽고, 2층 줄공책의 윗줄(`nb-upper-edit`)에 빨간색 펜으로 표준 교정부호를 사용해 ‘동료 첨삭 피드백(내용 1개 + 조직 1개 + 표현 1개)’을 직접 달아 주는 상호 편집장 활동을 수행하게 한다.",
            "rubric": {
                "high": "표준 교정부호를 사용하여 내용(주관적 표현 삭제·정의/출처 보충), 조직(통일성·거시 지시어·도표 지시문), 표현(주술 호응·부사어 호응 [6국04-05])의 3단계 퇴고를 완벽히 수행하여 정확하고 응집성 높은 최종 설명문을 완성함.",
                "mid": "내용 및 조직 수준의 주요 오류와 주술 호응 오류는 바르게 고쳤으나, 부사어 호응이나 세부 교정부호 사용에서 1~2개의 미비점이 있음.",
                "low": "단순 맞춤법 수정에만 머물러 주어-서술어 호응 오류나 주관적 문장을 스스로 진단·교정하는 데 교사의 도움이 필요함.",
            },
        },
    },
]
