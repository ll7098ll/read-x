# -*- coding: utf-8 -*-
"""
5단원 논설문 (Argumentative, unit5_argumentative) — Batch 4 (12~16차시: 과정중심 논설문 쓰기 5단계 W1 ~ W5)
1~11차시 읽기 전략 100% 전이 및 2층 고행간 첨삭 줄공책·교정부호 퇴고 구현
"""

BATCH4 = [
    # =========================================================================
    # 12차시: G6-ARG-W1 (계획하기)
    # 씨앗 보관함 소환 · 공동체 쟁점 발굴 · 찬반 논제 설정 · 반대 독자 분석 · 핵심 주장 확정
    # =========================================================================
    {
        "lesson_no": 12,
        "code": "G6-ARG-W1",
        "lesson_title": "[계획하기] 공동체 쟁점을 발굴하여 찬반 논제를 설정하고 예상 독자 분석하기",
        "std_badge": "[6국03-04] [6국01-05] 논제 설정 · 예상 독자 분석 · 핵심 주장 확정",
        "student_goal": "1~11차시 ‘내 글 씨앗 보관함’에서 학교·사회 공동체의 쟁점을 발굴하여 찬반 대립이 명확한 논제를 설정하고, 반대 입장 독자의 특성을 분석하여 핵심 주장 1문장을 확정할 수 있다.",
        "marking_items": [
            ["mk-double", "적격 찬반 논제", "찬반 대립이 뚜렷한 당위 평서문(~해야 한다)"],
            ["mk-line-blue", "예상 독자 특성", "독자의 관심사·배경지식·반대 우려"],
            ["mk-line-red", "핵심 가치관(관점)", "내 주장의 밑바탕이 되는 중심 가치"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>✍️ 쓰기 스튜디오 1단계 (계획하기):</strong> 1~11차시 읽기 씨앗 소환 &amp; 수사적 문제(논제·독자·관점) 설정</span>
          <span><strong>전이 연결:</strong> 1차시(논제) · 4차시(주제문) · 7차시(예상 독자) · 8차시(가치관) · 11차시(다매체 쟁점)</span>
        </div>

        <!-- 1~11차시 씨앗 보관함 총소환 대시보드 -->
        <div class="inline-segment-box" style="background:#FFFDFB; border-color:#922B21;">
          <div style="font-family:var(--font-sans); font-size:7.7pt; font-weight:800; color:#922B21; margin-bottom:4px;">
            🌱 [씨앗 보관함 총소환] 1~11차시 동안 우리가 읽고 탐구한 공동체 찬반 쟁점 꾸러미
          </div>
          <table class="std-table" style="font-size:7.2pt;">
            <thead>
              <tr>
                <th style="width:22%;">쟁점 영역</th>
                <th style="width:43%;">읽기 단원에서 만난 대표 논제</th>
                <th style="width:35%;">확장할 수 있는 내 논설문 글감 후보</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight:700;">🏫 학교·일상 안전/건강<br>(1·2·3·9차시)</td>
                <td>• 스쿨존 보행 중 스마트폰 사용 제한 의무화<br>• 청소년 고카페인 음료 규제 / 자율 선택 급식 / 9시 등교</td>
                <td>• <span class="mk-double">어린이 보호구역 내 전동 킥보드 통행 전면 금지</span><br>• 초등학생 교내 휴대전화 자율 소지 허용 여부</td>
              </tr>
              <tr>
                <td style="font-weight:700;">🌿 생태·환경·생명<br>(5·6·8차시)</td>
                <td>• 일회용 플라스틱 컵 보증금제 전국 의무화<br>• 반려동물 사전 의무 교육 / 국립공원 케이블카</td>
                <td>• <span class="mk-double">비 오는 날 교내 일회용 비닐 우산 커버 사용 금지</span><br>• 반려동물 보유세 도입 / 동물원 존폐 문제</td>
              </tr>
              <tr>
                <td style="font-weight:700;">🤖 미래 기술·인권<br>(4·11차시)</td>
                <td>• 공정 무역 제품 사용 촉구<br>• 생성형 인공지능(AI) 창작물 저작권 인정 여부</td>
                <td>• <span class="mk-double">16세 미만 청소년의 소셜미디어(SNS) 이용 제한</span><br>• 상업 시설의 ‘노키즈존(No Kids Zone)’ 규제</td>
              </tr>
            </tbody>
          </table>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📐 [논제 설정 3원칙 &amp; 예상 독자 분석 가이드]</th>
              <th class="wing-head">🧠 사고구술 &amp; 점검</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.6pt; line-height:1.5;">
                <p style="text-indent:0;"><strong>1. 좋은 논설문 논제(명제)의 3가지 조건 (SRSD STOP 전략)</strong><br>
                • ❌ <strong>단순 사실 확인 문장 탈락:</strong> “우리나라 초등학생의 스마트폰 보유율은 몇 퍼센트인가?” (찬반 토론 불가 — 설명문 주제)<br>
                • ❌ <strong>범위가 너무 넓거나 당연한 구호 탈락:</strong> “자연을 사랑하고 안전하게 생활하자.” (반대할 사람이 없어 논쟁이 되지 않음)<br>
                • ⭕ <strong>찬반 대립이 뚜렷하고 범위가 명확한 당위 평서문 채택:</strong> <span class="mk-double">“어린이 보호구역 내 개인형 이동장치(전동 킥보드)의 통행을 전면 금지해야 한다.”</span></p>
                <p style="text-indent:0; margin-top:4px;"><strong>2. 예상 독자 분석하기 (7차시 V2-3 &amp; 8차시 V2-4 연계)</strong><br>
                • 논설문의 진짜 목표는 ‘원래 나와 생각이 같은 독자’가 아니라, <span class="mk-line-blue"><strong>‘중립적이거나 내 주장에 반대하는 독자’</strong></span>의 마음을 움직이는 것입니다.<br>
                • 따라서 글쓰기를 계획할 때 <strong>① 내 글을 읽을 독자는 누구인지</strong>, <strong>② 반대 입장 독자가 왜 반대하며 무엇을 걱정하는지</strong>, <strong>③ 나는 어떤 근본 가치관(<span class="mk-line-red">생명 안전, 환경 보존, 인권과 자율성 등</span>)을 최우선으로 내세울지</strong> 미리 설계해야 합니다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>‘교통안전을 지키자’는 왜 좋은 논설문 논제가 될 수 없을까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>교통안전을 지키자는 말에 반대할 사람은 아무도 없잖아!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>‘어린이 보호구역 내 전동 킥보드 통행을 전면 금지해야 한다’처럼 <strong>찬성(안전 우선)</strong>과 <strong>반대(이동 편의 우선)</strong>가 팽팽히 맞서는 구체적 당위 문장으로 좁혀야 해!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "논제 후보 문장들의 자격을 심사하여 가장 적합한 찬반 논제 판별하기",
            "tag": "Step 1 적격 찬반 논제 판별",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:46%;">논제 후보 문장</th>
                  <th style="width:16%; text-align:center;">적격 판정 (⭕/❌)</th>
                  <th style="width:38%;">판정 이유 (쟁점성·명확성 기준)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>① 전동 킥보드는 어떤 원리로 움직이며 최고 속도는 얼마인가?</td>
                  <td style="text-align:center; font-weight:800; color:#C0392B;"><span class="blank-slot"><span class="t-ans">❌ 부적합</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">찬반 의견이 갈리는 쟁점이 아니라 단순 사실·원리를 묻는 설명문 주제이기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td>② 우리 모두 건강하고 행복한 학교생활을 만들어 나가자.</td>
                  <td style="text-align:center; font-weight:800; color:#C0392B;"><span class="blank-slot"><span class="t-ans">❌ 부적합</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">범위가 지나치게 넓고 모호하며 누구나 동의하는 당연한 말이라 찬반 논쟁이 성립하지 않는다.</span></span></td>
                </tr>
                <tr>
                  <td>③ 어린이 보호구역 내 전동 킥보드 통행을 전면 금지해야 한다.</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;"><span class="blank-slot"><span class="t-ans">⭕ 적합</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">해결이 시급한 공동체 문제이며 찬반 입장이 명확히 대립하는 구체적 당위 문장이기 때문이다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 선정한 찬반 논제에 대해 예상 독자의 입장을 분석하고 나의 최우선 가치관(관점) 세우기",
        "activity_2": {
            "title": "예상 독자(중립·반대 독자) 심리 분석 및 나의 최우선 가치관 설정 도해",
            "tag": "Step 2 예상 독자·관점 분석",
            "body_html": """
            <div class="inference-row" style="margin-bottom:0;">
              <div class="inf-card c1">
                <strong style="color:var(--mark-blue);">👥 1. 예상 독자 설정</strong><br>
                • 내가 설득할 독자: <span class="blank-slot"><span class="t-ans">전동 킥보드를 이용하는 동네 어른들과 지자체 공무원, 학교 친구들</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c2">
                <strong style="color:var(--mark-green);">💬 2. 반대 독자의 우려·관심사</strong><br>
                • 반대 이유 예상: <span class="blank-slot"><span class="t-ans">“스쿨존 통행을 막으면 출퇴근하거나 이동할 때 먼 길로 돌아가야 해서 불편하다.”</span></span>
              </div>
              <div class="inf-symbol">➔</div>
              <div class="inf-card c3">
                <strong style="color:#922B21;">💎 3. 나의 최우선 가치관(관점)</strong><br>
                • 핵심 가치: <span class="blank-slot"><span class="t-ans">어른들의 몇 분 빠른 이동 편의보다 어린이 보행자의 생명과 안전권이 최우선이다.</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 독자·관점 분석을 종합하여 내 논설문의 나침반이 될 ‘논설문 쓰기 계획서’ 확정하기",
        "activity_3": {
            "title": "나만의 논설문 쓰기 계획서 및 핵심 주장 1문장 확정하기",
            "tag": "Step 3 글쓰기 계획서 산출",
            "body_html": """
            <table class="std-table">
              <tbody>
                <tr>
                  <th style="width:24%; background:#FDEDEC; color:#922B21;">① 내가 선택한 찬반 논제</th>
                  <td><span class="blank-slot"><span class="t-ans">어린이 보호구역(스쿨존) 내 개인형 이동장치(전동 킥보드) 통행을 전면 금지해야 하는가? (또는 자유 논제)</span></span></td>
                </tr>
                <tr>
                  <th style="background:#FDEDEC; color:#922B21;">② 글을 쓰는 목적</th>
                  <td><span class="blank-slot"><span class="t-ans">등하교길 어린이 보행 사고의 위험성을 알리고 스쿨존 내 전동 킥보드 통행 금지 제도를 도입하도록 설득하기 위해</span></span></td>
                </tr>
                <tr>
                  <th style="background:#FDEDEC; color:#922B21;">③ 확정된 나의 핵심 주장<br>(명료한 당위 1문장)</th>
                  <td><span class="blank-slot"><span class="t-ans">어린이의 안전한 통학 권리와 생명을 지키기 위해 어린이 보호구역 내 전동 킥보드 통행을 법으로 전면 금지해야 한다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "13차시(W2 내용 생성하기) 직결",
            "prompt": "오늘 확정한 나의 ‘핵심 주장 1문장’을 뒷받침하기 위해 다음 시간에 어떤 통계나 사례 자료를 찾아볼지 검색 키워드를 적어 두세요.",
            "placeholder": "예: 도로교통공단 전동 킥보드 보행자 사고 통계, 해외 스쿨존 킥보드 규제 사례",
            "example_answer": "검색 키워드: 도로교통공단 개인형 이동장치(PM) 인도 보행자 사고 통계, 스쿨존 킥보드 속도 제한 및 통행 금지 사례",
        },
        "self_check": [
            "단순 사실문이나 모호한 문장이 아닌 ‘찬반 대립이 명확한 논제’를 골랐나요?",
            "내 주장에 반대할 수 있는 예상 독자의 우려와 관심사를 깊이 분석했나요?",
            "나의 입장과 핵심 가치관이 선명히 드러나는 핵심 주장 1문장을 완성했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[W1 계획하기 3단계 (Flower & Hayes 수사적 문제 설정 & SRSD STOP)] 1단계: 씨앗 소환 & 적격 논제 판별(❌사실 확인문 · ❌모호한 구호 ➔ ⭕구체적 찬반 당위 평서문) / 2단계: 예상 독자(반대·중립 독자의 우려) & 나의 최우선 가치관(8차시 V2-4 연계) 설정 / 3단계: 핵심 주장 1문장 확정",
            "intro_5min": "1~11차시 동안 교과서 오른쪽 아래 ‘내 글 씨앗 보관함’에 모아 둔 씨앗들을 펼쳐 보게 한다. 이제 독자에서 ‘설득하는 작가(논설가)’로 변신하는 첫 시간임을 선언하고, 집을 지을 때 설계도가 필요하듯 논설문 쓰기 계획서를 세워 보자고 안내한다.",
            "ido_think_aloud_script": "“논설문을 처음 쓸 때 가장 많이 하는 실수가 뭔지 알아요? 주제를 ‘환경을 보호하자’나 ‘교통안전을 지키자’처럼 너무 넓고 당연하게 잡는 거예요. 그러면 본론에서 무슨 말을 써야 할지 막막해져요. 대신 ‘비 오는 날 교내 일회용 비닐 우산 커버 사용을 금지해야 한다’ 또는 ‘어린이 보호구역 내 전동 킥보드 통행을 전면 금지해야 한다’처럼 누구에게 무엇을 어떻게 하자고 요구하는지 손에 잡힐 듯 구체적으로 좁혀야 강력한 논설문이 나온답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[활동 1]의 ①번 문장(‘전동 킥보드는 어떤 원리로 움직이며 최고 속도는 얼마인가?’)을 주제로 글을 쓰면 왜 논설문이 아니라 설명문이 될까요?",
                    "expected_ans": "글쓴이의 찬반 주장이나 의견이 들어갈 자리가 없고, 전동 킥보드의 과학적 원리와 사실 정보만 객관적으로 알려 주는 글이 되기 때문입니다.",
                    "reprompt": "①번 질문에 대해 ‘나는 찬성한다 / 반대한다’라고 대답할 수 있는지 생각해 볼까요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "글쓰기 계획서를 쓸 때 나와 생각이 같은 친구보다 ‘내 주장에 반대할 것 같은 독자’의 생각을 미리 분석해야 하는 까닭은 무엇일까요?",
                    "expected_ans": "7차시에 배운 것처럼 반대 입장 독자가 무엇을 걱정하는지 미리 알아야 본론에서 그 우려를 해결해 주는 반론·재반박 문단을 준비해 설득할 수 있기 때문입니다.",
                    "reprompt": "내가 설득해야 할 진짜 대상은 이미 찬성하는 사람일까요, 아니면 아직 망설이거나 반대하는 사람일까요?",
                },
            ],
            "youdo_and_wrapup": "학생 각자가 가장 쓰고 싶은 공동체 쟁점 1가지를 골라 [활동 2]와 [활동 3]의 계획서를 완성하도록 개별 코칭한다. 스스로 주제를 정하기 어려워하는 학생에게는 ‘스쿨존 전동 킥보드 통행 금지’, ‘교내 일회용 비닐 우산 커버 금지’, ‘학교 자율 선택 급식 도입’ 중 하나를 선택하도록 안내한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 정답:</strong> ① ❌ 부적합(찬반 쟁점이 아닌 단순 사실·원리를 묻는 설명문 주제임) / ② ❌ 부적합(범위가 지나치게 넓고 모호하며 누구나 동의하는 당연한 구호임) / ③ ⭕ 적합(찬반 입장이 명확히 대립하는 구체적 당위 문장임).<br>
              <strong>• [활동 2] 모범 답안:</strong> 1. 예상 독자(전동 킥보드를 이용하는 성인들과 지자체 공무원, 학생들) / 2. 반대 독자의 우려(스쿨존 통행을 막으면 돌아가야 해서 이동이 불편함) / 3. 나의 최우선 가치관(이동 편의보다 어린이 보행자의 생명과 안전권이 최우선임).<br>
              <strong>• [활동 3] 채점 기준:</strong> ① 찬반 대립이 분명한 논제, ② 구체적인 설득 목적, ③ 모호하지 않은 당위형 핵심 주장 1문장(‘~해야 한다’)이 일관되게 작성되었으면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "핵심 주장 문장에 찬성과 반대를 동시에 넣어 모호하게 작성함(‘전동 킥보드를 금지하되 타고 싶은 사람은 타게 해야 한다’)",
                    "diagnosis": "반론을 배려한다는 것과 자신의 핵심 주장을 흐리는 것을 혼동함",
                    "prescription": "핵심 주장 문장은 방향이 한쪽으로 명확해야 하며, 상대방에 대한 배려는 본론 3문단(반론 수용 후 대안 제시)에서 다루는 것임을 구분해 줌",
                },
                {
                    "error_case": "찬반 논제를 의문문으로만 적고 핵심 주장 칸에도 똑같이 의문문을 적음",
                    "diagnosis": "‘논제(함께 토론할 물음)’와 ‘주장(그 물음에 대한 나의 결론)’의 차이를 구별하지 못함",
                    "prescription": "논제가 ‘~해야 하는가?’라는 질문이라면, 나의 핵심 주장은 반드시 ‘~해야 한다(또는 해서는 안 된다)’라는 평서형 당위 문장으로 끝맺도록 교정함",
                },
            ],
            "scaffolding_down": "주제 선정이 막막한 학습자에게는 13차시에 풍부한 근거 자료 카드가 제공되는 추천 논제(‘어린이 보호구역 내 전동 킥보드 통행을 전면 금지해야 한다’)를 선택하여 계획서를 작성하도록 안내한다.",
            "scaffolding_up": "자신이 선택한 논제에 대해 ‘찬성 측 핵심 가치’와 ‘반대 측 핵심 가치’를 8차시처럼 양팔 저울 그림으로 비교한 뒤, 왜 자신의 가치가 더 무거운지 1문장으로 정당화하게 한다.",
            "rubric": {
                "high": "단순 사실문과 모호한 문장을 걸러 내고 찬반 대립이 명확한 논제를 설정하며, 반대 입장 독자의 우려와 자신의 핵심 가치관을 반영한 핵심 주장 1문장을 명확히 확정함.",
                "mid": "찬반 논제와 핵심 주장은 설정했으나, 반대 입장 독자가 제기할 수 있는 현실적 우려에 대한 분석이 다소 단편적임.",
                "low": "논제가 지나치게 모호하거나 사실 설명에 머물러 찬반 논설문 계획으로 구체화하는 데 도움이 필요함.",
            },
        },
    },

    # =========================================================================
    # 13차시: G6-ARG-W2 (내용 생성하기)
    # 타당한 이유 2~3개 생성 · 3점 기준 통과 근거 자료 선별·수집 · 예상 반론 및 재반박 마련
    # =========================================================================
    {
        "lesson_no": 13,
        "code": "G6-ARG-W2",
        "lesson_title": "[내용 생성하기] 타당한 이유를 생성하고 ‘3점 검증’ 통과 근거 자료와 반론·재반박 마련하기",
        "std_badge": "[6국03-04] 이유·근거 생성 · 3점 기준 자료 선별 · 반론·재반박 마련",
        "student_goal": "확정한 핵심 주장을 뒷받침할 서로 다른 차원의 이유 2가지를 생성하고, ‘3점 검증 기준(관련성·신뢰성·정확성)’으로 공신력 있는 근거 자료를 선별한 뒤 예상 반론과 재반박 논거를 마련할 수 있다.",
        "marking_items": [
            ["mk-line-red", "논리적 이유 1·2", "서로 중복되지 않는 타당한 까닭"],
            ["mk-line-blue", "🟢 적격 근거 자료", "3점 기준(관련성·신뢰성·정확성) 통과 자료"],
            ["mk-bg", "🛡️ 반론 & ⚔️ 재반박", "독자의 예상 반론과 이를 꺾는 해결 대안"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>✍️ 쓰기 스튜디오 2단계 (내용 생성하기):</strong> 다차원 이유 생성 &amp; 9차시 ‘3점 검증 신호등’으로 근거 자료 골라내기</span>
          <span><strong>전이 연결:</strong> 1차시(5요소) · 6차시(숨은 전제) · 7차시(반론·재반박) · 9차시(3점 검증) · 10차시(논리 오류 예방)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🗂️ [자료 수집실] 「어린이 보호구역 내 전동 킥보드 통행 금지」 논제를 위해 수집한 원자료 5종</th>
              <th class="wing-head">🧠 3점 검증 셀프 심사</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.45pt; line-height:1.48;">
                <p style="text-indent:0;"><span class="mk-line-blue"><strong>[수집 자료 ① — 공식 연구기관 통계]</strong> 한국도로교통공단 교통사고분석시스템(TAAS)과 삼성화재 교통안전문화연구소의 2025년 분석 결과에 따르면, 최근 5년간 개인형 이동장치(전동 킥보드)로 인한 보행자 충돌 사고가 4배 이상 급증했으며, 특히 인도와 횡단보도에서 발생한 어린이 보행자 피해 사고의 68%가 등하교 시간대 통학로 주변에서 일어났다.</span></p>
                <p style="text-indent:0; margin-top:3px;"><span class="mk-line-blue"><strong>[수집 자료 ② — 과학 실험 및 안전 기준 자료]</strong> 국립과학수사연구원과 한국소비자원의 주행 안전 실험 결과, 전동 킥보드는 소음이 거의 없어 보행자가 뒤에서 다가오는 것을 알아채기 어렵고, 바퀴가 작고 무게중심이 높아 시속 20km로 달리다 급정거할 때 제동 거리가 자전거보다 1.5배 이상 길어 눈높이가 낮은 초등학생과 부딪힐 경우 중상 위험이 매우 큰 것으로 확인되었다.</span></p>
                <p style="text-indent:0; margin-top:3px;"><strong>[수집 자료 ③ — 익명 인터넷 글]</strong> 어제 동네 인터넷 카페에 올라온 익명 게시글을 보니, “전동 킥보드를 타는 사람들은 전부 다 신호등을 한 번도 안 지키는 나쁜 사람들이라고 카더라”라는 댓글이 달려 있었다.</p>
                <p style="text-indent:0; margin-top:3px;"><strong>[수집 자료 ④ — 주제 무관 통계]</strong> 문화체육관광부가 발표한 ‘2025년 국민 여가 활동 조사’에 따르면, 주말에 등산이나 캠핑을 즐기는 인구가 지난해보다 12% 증가한 것으로 나타났다.</p>
                <p style="text-indent:0; margin-top:3px;"><span class="mk-line-blue"><strong>[수집 자료 ⑤ — 국내외 정책 사례 및 전문가 견해]</strong> 프랑스 파리와 호주 멜버른 등 해외 주요 도시는 보행자 안전을 위해 공유 전동 킥보드 운행을 금지하거나 어린이 보호구역 진입 시 전원이 자동으로 차단되는 지오펜싱(Geo-fencing, 가상 울타리) 기술을 의무화하여 보행자 사고를 40% 이상 줄였다. 교통공학 전문가 박준영 교수는 “스쿨존 외곽에 전용 주차 구역과 우회 도로를 마련하면 이용자 불편을 줄이면서 어린이 안전을 지킬 수 있다.”라고 제언했다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>수집한 5개 자료를 내 글에 전부 다 넣으면 좋을까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>잠깐! 9차시에 배운 <strong>3점 검증 기준</strong>과 10차시 <strong>논리 오류</strong>로 걸러 보자. 자료 ③은 익명 카더라 통신이자 ‘성급한 일반화 오류’이고, 자료 ④는 스쿨존 킥보드와 아무 ‘관련성’이 없는 등산 통계야!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>불량 자료 ③·④는 과감히 버리고, 3점 기준을 통과한 <strong>자료 ①·②·⑤</strong>만 내 논설문의 주춧돌로 써야 해!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "수집한 원자료 ①~⑤를 ‘3점 검증 기준’으로 심사하여 적격 자료 선별하기",
            "tag": "Step 1 수집 자료 3점 검증 선별",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">자료 번호</th>
                  <th style="width:20%; text-align:center;">선별 판정 (채택/버림)</th>
                  <th style="width:62%;">판정 이유 및 연결할 논증 기둥 (이유 1 / 이유 2 / 재반박)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700; text-align:center;">자료 ①·②</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;"><span class="blank-slot"><span class="t-ans">🟢 채택</span></span></td>
                  <td>도로교통공단·국과수의 공신력 있는 최신 통계와 실험 결과로, <span class="blank-slot"><span class="t-ans">[첫째 이유: 스쿨존 내 전동 킥보드의 높은 보행자 충돌 사고 위험성]을 증명함.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">자료 ③</td>
                  <td style="text-align:center; font-weight:800; color:#C0392B;"><span class="blank-slot"><span class="t-ans">🔴 버림(탈락)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">출처가 불분명한 익명 댓글(신뢰성 결여)이며, 이용자 전체를 비난하는 ‘성급한 일반화의 오류’가 있음.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">자료 ④</td>
                  <td style="text-align:center; font-weight:800; color:#C0392B;"><span class="blank-slot"><span class="t-ans">🔴 버림(탈락)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">주말 등산·캠핑 인구 통계는 어린이 보호구역 전동 킥보드 통행 금지 주장과 ‘관련성’이 전혀 없음.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">자료 ⑤</td>
                  <td style="text-align:center; font-weight:800; color:#196F3D;"><span class="blank-slot"><span class="t-ans">🟢 채택</span></span></td>
                  <td>해외 실제 정책 사례와 전문가 견해로, <span class="blank-slot"><span class="t-ans">[둘째 이유: 기술적·제도적 통행 제한의 실효성] 및 [반론에 대한 재반박 대안]을 뒷받침함.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 엄선한 적격 자료들을 내가 생성할 ‘이유 1·2’ 및 ‘예상 반론·재반박’과 짝지어 논증 카드 완성하기",
        "activity_2": {
            "title": "내 논설문의 [이유 1·2 + 검증된 근거] 및 [예상 반론 + 재반박] 내용 생성 매트릭스",
            "tag": "Step 2 다차원 논거·반론 생성 도해",
            "body_html": """
            <table class="std-table">
              <tbody>
                <tr>
                  <th style="width:20%; background:#FDEDEC; color:#922B21;">📣 나의 핵심 주장</th>
                  <td colspan="2">어린이의 안전한 통학 권리와 생명을 지키기 위해 <strong>어린이 보호구역 내 전동 킥보드 통행을 전면 금지해야 한다.</strong> (또는 자신이 선택한 논제의 핵심 주장)</td>
                </tr>
                <tr>
                  <th style="width:20%;">논증 기둥 구분</th>
                  <th style="width:40%;">내가 생성한 논리적 이유 (Reason)</th>
                  <th style="width:40%;">뒷받침할 3점 검증 통과 근거 자료 (Evidence)</th>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">🧱 지지 기둥 1<br>(안전·신체 차원)</td>
                  <td>첫째, 전동 킥보드는 <span class="blank-slot"><span class="t-ans">소음이 없고 제동 거리가 길어 시야가 좁은 어린이와 부딪힐 경우 치명적인 사고를 부르기</span></span> 때문이다.</td>
                  <td>• [자료 ①·② 인용]: <span class="blank-slot"><span class="t-ans">도로교통공단 통계(보행자 사고 4배 급증, 어린이 피해 68% 통학로 발생) 및 국과수 제동 거리 실험 결과</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">🧱 지지 기둥 2<br>(제도·실효성 차원)</td>
                  <td>둘째, 단순한 주의 당부만으로는 과속을 막기 어렵고 <span class="blank-slot"><span class="t-ans">진입 금지 구역 지정과 자동 감속·차단 기술이 있어야 사고를 확실히 예방할 수 있기</span></span> 때문이다.</td>
                  <td>• [자료 ⑤ 전반부 인용]: <span class="blank-slot"><span class="t-ans">해외 주요 도시의 스쿨존 진입 시 자동 전원 차단(지오펜싱) 의무화를 통한 사고 40% 감소 사례</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center; background:#EAFAF1; color:#145A32;">🛡️ 방어 기둥 3<br>(예상 반론 ⚡ 재반박)</td>
                  <td><strong>• 예상 반론:</strong> <span class="blank-slot"><span class="t-ans">스쿨존 통행을 막으면 성인 이용자들이 먼 길로 돌아가야 해서 이동이 불편하다.</span></span></td>
                  <td><strong>• 재반박 대안(자료 ⑤ 후반부):</strong> <span class="blank-slot"><span class="t-ans">박준영 교수 제언처럼 스쿨존 외곽에 우회 도로와 전용 주차 구역을 마련하면 해결 가능하며 어린이 생명이 우선이다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 생성한 이유와 주장 사이에 6차시(‘숨은 전제’)와 10차시(‘논리 오류’) 결함이 없는지 최종 점검하기",
        "activity_3": {
            "title": "내가 생성한 논거의 ‘숨은 전제(Warrant)’와 ‘무오류 타당성’ 자기 검증하기",
            "tag": "Step 3 생성 논거 타당성 검증",
            "body_html": """
            <div style="border:0.8pt solid #BDC3C7; border-radius:5px; padding:5px 8px; background:#FFFDFB;">
              <span class="pencil-line">① <strong>내 이유와 주장을 잇는 숨은 전제(6차시 연계):</strong> <span class="t-ans">어린이 보호구역에서는 이동 수단의 편리함보다 보행 약자인 어린이의 생명 안전이 언제나 최우선으로 보호되어야 한다.</span></span>
              <span class="pencil-line">② <strong>4대 논리 오류 점검(10차시 연계):</strong> 내 논거에는 성급한 일반화나 흑백논리 없이 <span class="t-ans">공식 통계(도로교통공단)와 절충 대안(외곽 우회 도로 마련)이 균형 있게 포함되었다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 내용 조직하기) 직결",
            "prompt": "오늘 생성한 [지지 기둥 1], [지지 기둥 2], [방어 기둥 3] 중 본론 맨 앞(2문단)에 배치하면 독자의 눈길을 가장 강력하게 사로잡을 기둥 1개를 골라 표시해 두세요.",
            "placeholder": "예: 보행자 사고가 4배 급증했고 어린이 피해의 68%가 통학로에서 난다는 통계가 담긴 [지지 기둥 1]을 2문단에 배치하겠다!",
            "example_answer": "가장 충격적이고 객관적인 통계(보행자 사고 4배 급증, 통학로 피해 68%)가 담긴 [지지 기둥 1]을 본론 첫머리(2문단)에 배치하겠다.",
        },
        "self_check": [
            "핵심 주장을 뒷받침할 서로 다른 차원의 이유 2가지를 생성했나요?",
            "3점 기준(관련성·신뢰성·정확성)으로 불량 자료를 버리고 적격 자료만 골랐나요?",
            "반대 독자의 예상 반론과 이를 해결할 구체적 재반박 대안을 마련했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[W2 내용 생성하기 (SRSD DARE: Develop Reasons & Evidence, Reject Arguments)] 1. 다차원 이유 생성(이유 1: 안전·신체 위험성 / 이유 2: 제도적 실효성) ➔ 2. 9차시 3점 검증 필터링(자료 ①·②·⑤ 채택 🟢 / 익명 루머 ③·무관한 등산 통계 ④ 삭제 🔴) ➔ 3. 7차시 대화적 방어 논거(반론: 우회 불편 ⚡ 재반박: 외곽 우회로·전용 주차장 + 생명 가치)",
            "intro_5min": "12차시에 세운 핵심 주장이라는 지붕 아래에 이제 튼튼한 ‘이유 기둥’과 ‘근거 주춧돌’ 재료를 모으는 시간임을 안내한다. 아무 돌이나 주춧돌로 쓰면 집이 무너지듯, 9차시에 배운 ‘3점 검증 신호등’으로 최고급 근거 재료만 골라내 보자고 독려한다.",
            "ido_think_aloud_script": "“이유를 두 개 만들 때 가장 조심해야 할 점은 ‘첫째 이유’와 ‘둘째 이유’가 똑같은 말을 반복하지 않게 하는 거예요! 예를 들어 첫째 이유를 ‘킥보드와 부딪히면 크게 다치기 때문이다(신체·안전 차원)’로 잡았다면, 둘째 이유는 다른 각도에서 ‘자율적인 주의만으로는 과속을 막을 수 없어 제도적·기술적 차단이 필요하기 때문이다(제도·실효성 차원)’처럼 서로 다른 차원의 기둥을 세워야 지붕이 평평하고 튼튼하게 받쳐진답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "수집 자료 ③번(‘전동 킥보드 타는 사람은 전부 다 신호등을 안 지키는 나쁜 사람이라고 카더라’)을 내 논설문에 쓰면 안 되는 까닭 두 가지는 무엇인가요?",
                    "expected_ans": "첫째, 익명 인터넷 카페 댓글이라 출처의 신뢰성(9차시 기준)이 없고, 둘째, 일부 사례로 전체 이용자를 나쁜 사람으로 몰아가는 성급한 일반화의 오류(10차시 기준)를 저질렀기 때문입니다.",
                    "reprompt": "9차시에 배운 ‘3점 검증 기준’과 10차시에 배운 ‘4대 논리 오류’ 두 가지 안경을 쓰고 자료 ③을 다시 봐 볼까요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "수집 자료 ⑤번은 본론의 ‘둘째 이유’뿐만 아니라 ‘예상 반론을 재반박하는 문단’에서도 아주 유용하게 쓸 수 있습니다. 어떤 부분을 재반박에 쓸 수 있나요?",
                    "expected_ans": "박준영 교수가 제언한 ‘스쿨존 외곽에 전용 주차 구역과 우회 도로를 마련하면 이용자 불편을 줄이면서 어린이 안전을 지킬 수 있다’는 부분을 이동 불편 반론을 꺾는 대안으로 쓸 수 있습니다.",
                    "reprompt": "자료 ⑤의 마지막 문장에서 킥보드 이용자들의 불편함을 덜어 줄 수 있는 해결책을 찾아보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]에서 불량 자료 ③·④를 걸러 내고, [활동 2]에서 자신의 논제에 맞는 이유 1·2, 적격 근거 1·2, 예상 반론·재반박 카드를 완성하도록 지도한다. 자유 논제를 선택한 학생도 교사가 제공하는 분야별 공식 통계 카드(자율 급식, 비닐 우산 커버, AI 저작권 등)를 활용하여 3점 검증을 거치게 한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 정답:</strong> 자료 ①·②(🟢 채택: 도로교통공단·국과수 공식 통계 및 실험으로 첫째 이유 입증) / 자료 ③(🔴 버림: 익명 루머로 신뢰성 결여 및 성급한 일반화 오류) / 자료 ④(🔴 버림: 주말 등산 통계로 논제와 관련성 없음) / 자료 ⑤(🟢 채택: 해외 사례와 전문가 견해로 둘째 이유 및 재반박 대안 입증).<br>
              <strong>• [활동 2] 모범 답안:</strong> 지지 기둥 1(소음이 없고 제동 거리가 길어 치명적 사고 위험 ⬅ 도로교통공단 보행자 사고 4배 급증·통학로 피해 68% 통계 및 국과수 실험) / 지지 기둥 2(자율 주의의 한계와 기술적·제도적 차단 필요성 ⬅ 해외 지오펜싱 도입 사고 40% 감소 사례) / 방어 기둥 3(반론: 우회 이동 불편 ⚡ 재반박: 외곽 우회 도로·전용 주차 구역 마련 대안 및 어린이 생명 최우선 가치).<br>
              <strong>• [활동 3] 채점 기준:</strong> 자신의 이유와 주장을 연결하는 숨은 전제를 명시하고, 4대 논리적 오류가 없음을 점검했으면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "첫째 이유와 둘째 이유를 단어만 조금 바꾸어 똑같은 내용(‘사고가 나서 위험하다’ / ‘다칠 수 있어서 위험하다’)으로 중복 생성함",
                    "diagnosis": "이유를 다차원(안전·건강 차원 / 제도·교육 차원 / 환경·경제 차원)으로 나누어 생성하는 범주화 전략이 부족함",
                    "prescription": "‘기둥 1은 [왜 위험한가?(신체·안전)]’, ‘기둥 2는 [왜 자율에 맡기면 안 되고 법으로 금지해야 하는가?(제도·효과)]’처럼 질문 관점을 나누어 이유를 생성하게 코칭함",
                },
                {
                    "error_case": "근거 자료 칸에 출처나 수치 없이 자기 생각(‘내 생각에도 킥보드가 아주 빠른 것 같다’)만 적음",
                    "diagnosis": "1차시·3차시에 배운 ‘이유(논리적 생각)’와 ‘근거 자료(객관적 사실 데이터)’의 구분을 쓰기 단계에서 잊어버림",
                    "prescription": "근거 자료 칸에는 반드시 ‘누가 조사한 어떤 수치/사례인가’가 들어가야 함을 강조하고 좌측 수집 자료 ①·②·⑤의 출처와 숫자를 정확히 옮겨 적게 함",
                },
            ],
            "scaffolding_down": "자유 논제 자료 수집이 어려운 학생은 좌측 페이지에 완비된 ‘스쿨존 전동 킥보드 통행 금지’ 공식 원자료 꾸러미(①·②·⑤)를 그대로 활용하여 [활동 2] 매트릭스를 완성하도록 지원한다.",
            "scaffolding_up": "자신이 선택한 자유 논제에 대해 1~11차시 본문에 등장했던 공식 통계(예: 삼성화재 교통안전문화연구소, 질병관리청, 경기도교육청, 환경부, 농림축산식품부, 문체부 등) 중 하나를 짝지어 인용 계획을 세워 보게 한다.",
            "rubric": {
                "high": "서로 중복되지 않는 타당한 이유 2가지를 생성하고, 3점 검증 기준을 적용해 불량 자료를 완벽히 걸러 낸 뒤 출처가 명확한 근거 자료와 예상 반론·재반박 논거를 빈틈없이 마련함.",
                "mid": "이유 2가지와 적격 근거 자료는 연결했으나, 예상 반론을 꺾는 재반박 대안의 구체성이 다소 부족함.",
                "low": "첫째 이유와 둘째 이유가 중복되거나, 3점 검증에서 탈락한 부적격 자료를 걸러 내지 못함.",
            },
        },
    },

    # =========================================================================
    # 14차시: G6-ARG-W3 (내용 조직하기)
    # 읽기 모델(V1-3) 미러링 서-본(이유+근거 / 반론+재반박)-결 3단 5문단 논증 개요 및 담화표지 설계
    # =========================================================================
    {
        "lesson_no": 14,
        "code": "G6-ARG-W3",
        "lesson_title": "[내용 조직하기] 읽기 모델을 미러링하여 5문단 논증 개요표와 담화표지 설계하기",
        "std_badge": "[6국03-04] [6국02-02] 3단 5문단 논증 개요 조직 · 담화표지 배치",
        "student_goal": "3차시 읽기 모델의 ‘심화 3단 논증 구조도’를 내 글의 개요 틀로 미러링하여 ‘서론 - 본론 1·2(지지 기둥) - 본론 3(반론·재반박 기둥) - 결론’의 5문단 상세 개요표와 담화표지를 설계할 수 있다.",
        "marking_items": [
            ["mk-person", "논증 담화표지", "따라서, 첫째, 실제로, 둘째, 물론, 그러나, 요약하면"],
            ["mk-double", "서론·결론 주장", "1문단 핵심 주장 제시 ↔ 5문단 요약·재강조"],
            ["mk-line-red", "본론 중심 문장", "2·3·4문단 첫머리 핵심 명제"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>✍️ 쓰기 스튜디오 3단계 (내용 조직하기):</strong> 3차시 읽기 구조도(`V1-3`) 1:1 미러링 &amp; 문단별 담화표지(`V1-2`) 배치</span>
          <span><strong>핵심 원리:</strong> 읽기에서 해부한 ‘파르테논 5문단 설계도’에 13차시 내 재료를 조립하기</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🏛️ [읽기↔쓰기 1:1 미러링 설계도] 3차시 〈자율 선택 급식〉 구조 vs 내 논설문 5문단 개요 틀</th>
              <th class="wing-head">🧠 사고구술 &amp; 조직 전략</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.45pt; line-height:1.48;">
                <table class="std-table" style="font-size:7.2pt;">
                  <thead>
                    <tr>
                      <th style="width:16%;">문단 위계</th>
                      <th style="width:24%;">필수 논증 담화표지</th>
                      <th style="width:60%;">문단 내부 문장 조립 공식 (Sentence Blueprint)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="font-weight:800; background:#FDEDEC; color:#922B21; text-align:center;">1문단<br>[서론]</td>
                      <td>• <span class="mk-person">~에 따르면</span> (실태)<br>• <span class="mk-person">따라서</span> (주장)</td>
                      <td>① [문제 상황·통계 실태 제시] ➔ ② [사회적 찬반 논제 언급] ➔ ③ <span class="mk-double">[글쓴이의 핵심 주장 천명(‘~해야 한다’)]</span></td>
                    </tr>
                    <tr>
                      <td style="font-weight:800; background:#EBF5FB; color:#1B4F72; text-align:center;">2문단<br>[본론 1]<br>지지 기둥①</td>
                      <td>• <span class="mk-person">첫째, ~기 때문이다.</span><br>• <span class="mk-person">실제로 ~에 따르면</span></td>
                      <td>① <span class="mk-line-red">[중심 문장: 첫째 이유 제시]</span> ➔ ② [뒷받침 문장: 3점 검증을 통과한 공식 통계·실험 근거 인용] ➔ ③ [소결론: 이유와 주장 연결]</td>
                    </tr>
                    <tr>
                      <td style="font-weight:800; background:#EBF5FB; color:#1B4F72; text-align:center;">3문단<br>[본론 2]<br>지지 기둥②</td>
                      <td>• <span class="mk-person">둘째, ~기 때문이다.</span><br>• <span class="mk-person">또한 ~사례를 보면</span></td>
                      <td>① <span class="mk-line-red">[중심 문장: 둘째 이유 제시]</span> ➔ ② [뒷받침 문장: 국내외 성공 사례 또는 전문가 견해 인용] ➔ ③ [소결론: 기대 효과 정리]</td>
                    </tr>
                    <tr>
                      <td style="font-weight:800; background:#EAFAF1; color:#145A32; text-align:center;">4문단<br>[본론 3]<br>방어 기둥</td>
                      <td>• <span class="mk-person">물론 ~라는 반론도 있다.</span><br>• <span class="mk-person">그러나 ~</span></td>
                      <td>① [반대 독자의 예상 반론 1문장 수용] ➔ ② <span class="mk-line-red">[재반박 1: 구체적 해결·보완 대안 제시]</span> ➔ ③ [재반박 2: 상위 공익 가치 강조]</td>
                    </tr>
                    <tr>
                      <td style="font-weight:800; background:#2C3E50; color:#fff; text-align:center;">5문단<br>[결론]</td>
                      <td>• <span class="mk-person">요약하면,</span><br>• <span class="mk-person">그러므로</span></td>
                      <td>① [본론 이유 1·2 및 핵심 논지 압축 요약(4차시 공식)] ➔ ② [긍정적 미래 전망 제시] ➔ ③ <span class="mk-double">[핵심 주장 재강조 및 실천 당부]</span></td>
                    </tr>
                  </tbody>
                </table>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>‘예상 반론과 재반박(방어 기둥)’은 왜 본론 맨 앞(2문단)이 아니라 본론 후반부(4문단)에 배치할까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>내 주장을 뒷받침하는 강력한 이유와 근거(2·3문단)를 먼저 보여 주어 독자를 설득해 놓은 뒤, 마지막 남은 의구심을 4문단에서 싹 지워 주는 것이 가장 효과적이거든!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span><strong>[지지 기둥 1·2 먼저 ➔ 방어 기둥 3 나중]</strong> 순서를 꼭 기억하자!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "순서가 뒤섞인 문단 개요와 잘못 쓰인 담화표지 바로잡기",
            "tag": "Step 1 논증 순서·담화표지 교정",
            "body_html": """
            <div style="font-size:7.3pt; margin-bottom:3px; color:#2C3E50;">
              🧩 아래 (가)~(라)는 본론과 결론 문단의 순서가 뒤섞이고 담화표지 2곳에 오류가 있는 개요입니다. 바르게 고쳐 보세요.
            </div>
            <div style="border:0.8pt solid #BDC3C7; border-radius:4px; padding:4px 7px; font-size:7.25pt; background:#F8F9F9; margin-bottom:4px;">
              • <strong>(가)</strong> <u>그러나</u>[❌ 담화표지 오류 ①] 요약하면, 전동 킥보드는 사고 위험이 크고 기술적 차단이 효과적이므로 스쿨존 통행을 금지해야 한다.<br>
              • <strong>(나)</strong> 물론 성인 이용자들이 돌아가야 해서 불편하다는 반론도 있다. <u>왜냐하면</u>[❌ 담화표지 오류 ②] 스쿨존 외곽에 우회 도로를 만들면 해결할 수 있다.<br>
              • <strong>(다)</strong> 첫째, 전동 킥보드는 소음이 없고 제동 거리가 길어 어린이 보행자 충돌 사고 위험이 매우 높기 때문이다.<br>
              • <strong>(라)</strong> 둘째, 진입 시 전원이 차단되는 지오펜싱 기술과 금지 구역 지정으로 사고를 40% 이상 확실히 줄일 수 있기 때문이다.
            </div>
            <span class="pencil-line">① <strong>올바른 문단 배열 순서:</strong> [서론] ➔ <span class="t-ans">( 다 ) ➔ ( 라 ) ➔ ( 나 ) ➔ ( 가 )</span></span>
            <span class="pencil-line">② <strong>담화표지 오류 2곳 교정:</strong> (가)의 ‘그러나’ ➔ <span class="t-ans">‘그러므로(또는 따라서)’</span> / (나)의 ‘왜냐하면’ ➔ <span class="t-ans">‘그러나(또는 하지만)’</span></span>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 논리적 질서에 맞추어 12~13차시에 준비한 내 논설문 재료를 ‘5문단 상세 논증 개요표’에 배치하기",
        "activity_2": {
            "title": "나만의 5문단 논설문 상세 개요표 및 담화표지 설계도 완성하기",
            "tag": "Step 2 5문단 상세 개요표 설계",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:15%;">문단 구분</th>
                  <th style="width:23%;">사용할 담화표지·지시어</th>
                  <th style="width:62%;">문단별 중심 내용 및 뒷받침 근거 설계</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#FDEDEC;">1문단<br>(서론)</td>
                  <td><code>~에 따르면</code>,<br><code>따라서</code></td>
                  <td>• 문제 상황: 등하교길 인도를 질주하는 전동 킥보드로 어린이 안전이 위협받음.<br>• 핵심 주장: <span class="blank-slot"><span class="t-ans">어린이의 생명을 지키기 위해 스쿨존 내 전동 킥보드 통행을 전면 금지해야 한다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#EBF5FB;">2문단<br>(본론 1)</td>
                  <td><code>첫째, ~기 때문이다</code>,<br><code>실제로 ~에 따르면</code></td>
                  <td>• 첫째 이유: <span class="blank-slot"><span class="t-ans">소음이 없고 제동 거리가 길어 치명적인 어린이 보행 사고를 부르기 때문</span></span><br>• 뒷받침 근거: <span class="blank-slot"><span class="t-ans">도로교통공단 통계(보행자 사고 4배 급증, 통학로 피해 68%) 및 국과수 실험</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#EBF5FB;">3문단<br>(본론 2)</td>
                  <td><code>둘째, ~기 때문이다</code>,<br><code>이러한 문제를 막으려면</code></td>
                  <td>• 둘째 이유: <span class="blank-slot"><span class="t-ans">자율적 주의만으로는 한계가 있어 법적 통행 금지와 자동 차단 기술이 확실한 예방책이기 때문</span></span><br>• 뒷받침 근거: <span class="blank-slot"><span class="t-ans">파리·멜버른 등 해외 스쿨존 자동 전원 차단(지오펜싱) 의무화로 사고 40% 감소 사례</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#EAFAF1;">4문단<br>(본론 3)</td>
                  <td><code>물론 ~라는 반론도 있다</code>,<br><code>그러나</code></td>
                  <td>• 예상 반론 수용: <span class="blank-slot"><span class="t-ans">성인 이용자들의 이동 경로가 길어져 불편하다는 의견</span></span><br>• 재반박 대안·가치: <span class="blank-slot"><span class="t-ans">스쿨존 외곽 우회 도로 및 전용 주차장 설치로 보완 가능하며 어린이 생명이 최우선임</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#F2F4F4;">5문단<br>(결론)</td>
                  <td><code>요약하면</code>,<br><code>그러므로</code></td>
                  <td>• 요약 및 당부: <span class="blank-slot"><span class="t-ans">사고 예방을 위해 정부와 지자체는 스쿨존 내 전동 킥보드 통행 금지를 조속히 법제화해야 한다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 완성한 5문단 개요표의 통일성·응집성과 설득적 제목을 최종 점검하기",
        "activity_3": {
            "title": "개요 조직의 통일성·응집성 점검 및 내 논설문의 설득적 제목 확정하기",
            "tag": "Step 3 개요 점검 및 제목 확정",
            "body_html": """
            <div style="border:0.8pt solid #BDC3C7; border-radius:5px; padding:5px 8px; background:#FFFDFB;">
              <span class="pencil-line">① <strong>설득적 제목 확정(4차시 기법 적용):</strong> <span class="t-ans">위험한 질주는 멈추고 안전한 등굣길은 지키는 약속, 스쿨존 내 전동 킥보드 통행을 금지하자!</span></span>
              <span class="pencil-line">② <strong>개요 조직 자기 점검:</strong> 서론(1문단)의 주장과 결론(5문단)의 주장이 일관되며, <span class="t-ans">문단 앞머리마다 알맞은 논증 담화표지(첫째, 둘째, 물론, 그러나, 요약하면)가 배치되었다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "15차시(W4 초고 집필하기) 직결",
            "prompt": "다음 시간(15차시)에는 오늘 설계한 5문단 개요표를 보며 실제 논설문 초고를 집필합니다. 내 글의 품격을 높여 줄 ‘관용표현·속담 1개’를 어느 문단에 넣을지 지정해 두세요.",
            "placeholder": "예: 3문단(또는 4문단)에 ‘소 잃고 외양간 고치기’나 ‘첫술에 배부르랴’를 넣겠다.",
            "example_answer": "3문단 마지막에 “사고가 난 뒤에 후회하는 것은 ‘소 잃고 외양간 고치기’에 불과하다.”라는 관용표현을 넣겠다.",
        },
        "self_check": [
            "‘서론 - 본론 1·2(지지) - 본론 3(반론·재반박) - 결론’ 5문단 구조를 지켰나요?",
            "각 문단 앞머리에 알맞은 논증·전환 담화표지를 정확히 배치했나요?",
            "서론의 핵심 주장과 결론의 마무리 주장이 서로 모순 없이 일관되나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[W3 내용 조직하기: 3차시 V1-3 구조도 1:1 미러링] 1문단 서론(문제 실태 ➔ 논제 ➔ 핵심 주장) / 2문단 본론1(첫째 이유 + 통계·실험 근거) / 3문단 본론2(둘째 이유 + 사례·전문가 근거) / 4문단 본론3(물론 [예상 반론] ⚡ 그러나 [재반박 대안+상위 가치]) / 5문단 결론(요약하면 [핵심 요약] ➔ 그러므로 [실천 당부])",
            "intro_5min": "13차시에 모은 훌륭한 벽돌과 기둥 재료들을 어떤 순서로 쌓아야 가장 설득력 있는 논설문 건축물이 될지 질문한다. 3차시에서 우리가 직접 그렸던 ‘파르테논 신전 5문단 구조도’를 꺼내어 내 글의 설계도로 그대로 미러링하는 방법을 안내한다.",
            "ido_think_aloud_script": "“개요표를 짤 때 문단과 문단을 단단하게 묶어 주는 접착제가 바로 2차시에 배운 ‘담화표지’예요! 2문단 문을 열 때는 ‘첫째, ~기 때문이다’, 3문단 문을 열 때는 ‘둘째, ~기 때문이다’, 그리고 4문단에서 상대방 반론을 부를 때는 ‘물론 ~라는 반론도 있다. 그러나 ~’, 마지막 5문단 문을 닫을 때는 ‘요약하면, ~ 그러므로 ~’를 미리 개요표 왼쪽 칸에 박아 두세요. 그러면 다음 시간에 초고를 쓸 때 막히지 않고 술술 문장이 풀려 나온답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "[활동 1]의 (나) 문단에서 ‘물론 불편하다는 반론도 있다. 왜냐하면 우회 도로를 만들면 해결할 수 있다’는 왜 어색한가요?",
                    "expected_ans": "앞문장의 예상 반론을 뒤집어 재반박하는 자리인데 이유를 나타내는 ‘왜냐하면’을 썼기 때문입니다. 역접 담화표지인 ‘그러나(또는 하지만)’로 고쳐야 합니다.",
                    "reprompt": "‘물론 [반대 의견]’과 짝을 이루어 흐름을 반대로 꺾어 주는 담화표지는 무엇이었는지 2차시·7차시를 떠올려 볼까요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "만약 서론(1문단)에서는 ‘스쿨존 전동 킥보드 통행을 전면 금지해야 한다’고 주장해 놓고, 결론(5문단)에서는 ‘헬멧만 쓰면 스쿨존에서 마음대로 타도 된다’라고 끝맺으면 어떤 문제가 생길까요?",
                    "expected_ans": "글의 처음과 끝 주장이 서로 어긋나 ‘일관성’이 무너지고, 독자가 글쓴이의 진짜 입장이 무엇인지 혼란스러워집니다.",
                    "reprompt": "1문단과 5문단의 빨간 겹줄(핵심 주장)은 서로 같은 방향을 가리켜야 할까요, 다른 방향을 가리켜야 할까요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 2]의 5문단 상세 개요표를 작성하며 각 문단에 들어갈 담화표지와 근거 출처를 꼼꼼히 배치하도록 순회 지도한다. 짝과 개요표를 바꾸어 문단 순서와 통일성을 상호 점검하게 한 뒤 15차시(초고 집필)를 예고한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 정답:</strong> ① 올바른 배열 순서: <code>(다) ➔ (라) ➔ (나) ➔ (가)</code> / ② 담화표지 교정: (가)의 ‘그러나’ ➔ <code>‘그러므로(또는 따라서)’</code>, (나)의 ‘왜냐하면’ ➔ <code>‘그러나(또는 하지만)’</code>.<br>
              <strong>• [활동 2] 모범 답안:</strong> 1문단(스쿨존 전동 킥보드 통행 전면 금지 주장) / 2문단(소음·제동거리 문제로 치명적 사고 위험 + 도로교통공단 보행자 사고 4배 급증·통학로 68% 통계) / 3문단(자율 주의 한계 및 기술·제도적 차단 실효성 + 해외 지오펜싱 사고 40% 감소 사례) / 4문단(성인 이동 불편 반론 수용 + 외곽 우회 도로·전용 주차장 대안 및 생명 가치 재반박) / 5문단(논거 요약 및 법제화 당부).<br>
              <strong>• [활동 3] 채점 기준:</strong> 4차시 설득적 제목 기법을 적용하여 주장이 선명한 제목을 짓고, 5문단 개요의 일관성을 점검했으면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "본론 3(4문단)에서 예상 반론만 적어 놓고 재반박 대안을 개요표에서 빠뜨림",
                    "diagnosis": "4문단의 주인공이 ‘반론’이 아니라 ‘재반박’임을 잊고 반론 소개에만 그침",
                    "prescription": "4문단 개요 칸을 반드시 <code>[물론: 예상 반론] ⚡ [그러나: 재반박 대안]</code> 두 줄로 나누어 적도록 강제하여 재반박 누락을 방지함",
                },
                {
                    "error_case": "결론(5문단) 개요에 본론에서 한 번도 말하지 않은 완전히 새로운 셋째 이유와 통계를 집어넣음",
                    "diagnosis": "결론 문단의 기능(본론 핵심 요약 + 주장 재강조 및 전망)과 본론 문단의 기능(새 논거 제시)을 혼동함",
                    "prescription": "결론은 새로운 기둥을 세우는 곳이 아니라, 이미 세운 기둥들을 한눈에 묶어 요약하고 독자의 실천을 당부하는 마무리 공간임을 안내함",
                },
            ],
            "scaffolding_down": "개요표 작성이 느린 학생에게는 13차시 [활동 2]에서 작성한 카드 내용을 화살표 번호(①➔1문단, ②➔2문단, ③➔3문단, ④➔4문단)에 따라 그대로 옮겨 적고 앞머리에 담화표지만 붙이도록 단계별로 안내한다.",
            "scaffolding_up": "문단과 문단 사이를 이어 줄 때 단순 접속어(‘첫째, 둘째’)뿐 아니라 6차시에 배운 ‘거시 지시어(이러한 위험을 막으려면, 이와 같은 대책들이 자리 잡을 때)’까지 개요표에 미리 설계해 넣도록 도전 과제를 준다.",
            "rubric": {
                "high": "‘서론 - 본론 1·2(지지 기둥) - 본론 3(반론·재반박 기둥) - 결론’의 5문단 구성과 문단별 논증 담화표지를 100% 정확하게 배치하여 완결된 논설문 상세 개요표를 작성함.",
                "mid": "5문단 개요의 기본 틀은 완성했으나, 일부 문단의 담화표지 선택이나 결론 요약 설계가 다소 소략함.",
                "low": "문단 간 순서(지지 기둥과 방어 기둥, 결론)가 뒤섞이거나 주장과 이유가 일관되지 않음.",
            },
        },
    },

    # =========================================================================
    # 15차시: G6-ARG-W4 (초고 집필하기)
    # 공식 출처 인용 틀 · 반론 재반박 틀 · 관용표현 · 정중한 당위 어조를 적용한 5문단 초고 집필
    # =========================================================================
    {
        "lesson_no": 15,
        "code": "G6-ARG-W4",
        "lesson_title": "[초고 집필하기] 공식 출처 인용 틀·관용표현·정중한 당위 어조를 적용하여 초고 쓰기",
        "std_badge": "[6국03-04] [6국04-04] 공식 인용 틀 · 관용표현 활용 · 격식 있는 당위 어조",
        "student_goal": "14차시에 완성한 5문단 개요표를 바탕으로 공식 출처 인용 문장 틀(‘~에 따르면’), 반론 수용·재반박 틀(‘물론 ~ 그러나 ~’), 관용표현, 정중하고 단호한 당위 어조(‘~해야 한다’)를 적용하여 논설문 초고를 집필할 수 있다.",
        "marking_items": [
            ["mk-line-blue", "공식 출처 인용 틀", "OO 기관의 202X년 조사에 따르면 ~"],
            ["mk-highlight", "관용표현·속담", "설득력을 높이는 비유·속담 표현"],
            ["mk-double", "당위적 설득 어조", "~해야 한다 / ~할 필요가 있다"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>✍️ 쓰기 스튜디오 4단계 (초고 집필하기):</strong> 개요표를 문단과 문장으로 풀어내는 ‘4대 고급 집필 무기’</span>
          <span><strong>전이 연결:</strong> 2차시(담화표지·호응) · 4차시(제목) · 5차시(관용표현) · 7차시(반론·재반박) · 9차시(출처 인용)</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>🛠️ [논설문 초고 집필 4대 표현 무기 &amp; 문단별 문장 스타터(Sentence Starters)]</th>
              <th class="wing-head">🧠 사고구술 &amp; 집필 팁</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col" style="font-family:var(--font-sans); font-size:7.45pt; line-height:1.5;">
                <p style="text-indent:0;"><strong>무기 ① 공식 출처 인용 문장 틀 (9차시 V3-1 연계)</strong><br>
                • ❌ 미숙한 표현: “인터넷에서 봤는데 킥보드 사고가 엄청 많이 난다고 한다.”<br>
                • ⭕ <span class="mk-line-blue"><strong>공식 인용 틀:</strong> “<strong>[공식 기관명]</strong>이 <strong>[연도]</strong>년 발표한 <strong>‘[조사·보고서 이름]’</strong>에 따르면, <strong>[구체적 수치·사실]</strong>인 것으로 나타났다.”</span></p>

                <p style="text-indent:0; margin-top:4px;"><strong>무기 ② 반론 수용 및 재반박 문장 틀 (7차시 V2-3 연계)</strong><br>
                • ⭕ <strong>대화적 논증 틀:</strong> “<strong>물론</strong> 일각에서는 <strong>[반대 독자의 예상 반론]</strong>라는 우려도 있다. <strong>그러나</strong> 이러한 불편함은 <strong>[구체적 보완 대안]</strong>을 통해 충분히 해결할 수 있다. 무엇보다 <strong>[작은 불편]</strong>보다 <strong>[상위 공익 가치]</strong>를 지키는 것이 훨씬 더 중요하다.”</p>

                <p style="text-indent:0; margin-top:4px;"><strong>무기 ③ 설득력을 높이는 관용표현·속담 1개 이상 넣기 (5차시 V2-1 연계)</strong><br>
                • <span class="mk-highlight"><code>발등에 불이 떨어지다</code></span>(서론: 시급성 강조) · <span class="mk-highlight"><code>소 잃고 외양간 고치기 / 눈 가리고 아웅</code></span>(본론: 미봉책 비판) · <span class="mk-highlight"><code>첫술에 배부르랴 / 천 리 길도 한 걸음부터</code></span>(재반박·결론: 실천 독려)</p>

                <p style="text-indent:0; margin-top:4px;"><strong>무기 ④ 격식 있고 정중한 당위 어조 유지하기</strong><br>
                • 감정적 비난(‘나쁜 어른들’)이나 무책임한 단정(‘무조건 100%’), 모호한 추측(‘~인 것 같다’)을 피하고, <span class="mk-double"><strong>‘~해야 한다’, ‘~할 필요가 있다’, ‘~이 바람직하다’</strong></span>로 정중하고 힘 있게 맺습니다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>개요표의 짧은 메모를 어떻게 매끄러운 문단으로 부풀릴 수 있을까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>본론 각 문단을 <strong>[중심 문장(이유) ➔ 뒷받침 문장 1(공식 통계 인용) ➔ 뒷받침 문장 2(관용표현·설명) ➔ 마무리 문장]</strong>의 3~4문장 블록으로 조립하면 돼!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>왼쪽의 ‘4대 표현 무기’ 문장 틀에 내 재료를 끼워 넣어 보자!</span></div>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "출처가 모호하고 구어체로 쓰인 미숙한 문단을 ‘4대 표현 무기’로 고쳐 쓰기 (워밍업)",
            "tag": "Step 1 공식 인용 틀·어조 훈련",
            "body_html": """
            <div style="border:0.8pt solid #BDC3C7; border-radius:4px; padding:4px 7px; font-size:7.25pt; background:#F8F9F9; margin-bottom:3px;">
              <strong>[미숙한 초고 조각]:</strong> “첫째, 스쿨존에서 킥보드 타면 애들이 많이 다치는 것 같다. 어디서 들었는데 요즘 사고가 옛날보다 몇 배나 늘었다고 카더라. 사고 나고 나서 후회해 봤자 아무 소용 없으니까 무조건 못 타게 막아야만 한다.”
            </div>
            <span class="pencil-line">✏️ <strong>[공식 인용 틀 + 관용표현 + 정중한 어조로 재작성]:</strong> <span class="t-ans">첫째, 전동 킥보드는 어린이 보행자와 부딪힐 경우 심각한 안전사고를 일으키기 때문이다. 한국도로교통공단이 2025년 발표한 분석에 따르면, 최근 5년간 전동 킥보드 보행자 사고가 4배 이상 급증했으며 어린이 피해의 68%가 통학로에서 발생했다. 사고가 난 뒤에 대책을 세우는 것은 ‘소 잃고 외양간 고치기’에 불과하므로 사전 통행 금지가 필수적이다.</span></span>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 문장화 기법을 적용하여 내 논설문의 [제목 · 서론(1문단) · 본론 1·2(2·3문단)] 초고 집필하기",
        "activity_2": {
            "title": "나만의 논설문 초고 집필하기 ①: [설득적 제목 · 서론(1문단) · 본론 1·2(2·3문단)]",
            "tag": "Step 2 서론·본론 지지 기둥 집필",
            "body_html": """
            <div style="border:0.9pt solid #922B21; border-radius:5px; padding:5px 8px; background:#FFFFFF; font-size:7.3pt;">
              <div style="font-weight:800; color:#922B21; border-bottom:0.7pt solid #E6B0AA; padding-bottom:2px; margin-bottom:3px;">
                🏷️ <strong>논설문 제목:</strong> <span class="blank-slot" style="min-width:260px;"><span class="t-ans">위험한 질주는 멈추고 안전한 등굣길은 지키는 약속, 스쿨존 내 전동 킥보드 통행을 금지하자!</span></span>
              </div>
              <span class="pencil-line"><strong>➊ [서론]:</strong> <span class="t-ans">최근 등하교 시간 학교 앞 인도를 빠르게 질주하는 전동 킥보드 때문에 어린이 보행 안전이 ‘발등에 불이 떨어진’ 과제가 되었다. 어린이의 소중한 생명과 안전한 통학 권리를 지키기 위해 어린이 보호구역 내 전동 킥보드 통행을 법으로 전면 금지해야 한다.</span></span>
              <span class="pencil-line"><strong>➋ [본론 1 - 첫째 이유+근거]:</strong> <span class="t-ans">첫째, 전동 킥보드는 소음이 거의 없고 제동 거리가 길어 눈높이가 낮은 어린이와 부딪힐 경우 치명적인 사고를 부르기 때문이다. 한국도로교통공단의 2025년 분석에 따르면 최근 5년간 전동 킥보드 보행자 사고가 4배 이상 급증했으며, 어린이 피해 사고의 68%가 통학로 주변에서 일어났다.</span></span>
              <span class="pencil-line"><strong>➌ [본론 2 - 둘째 이유+근거]:</strong> <span class="t-ans">둘째, 개인의 자율적인 주의만으로는 과속을 막기 어려워 제도적·기술적 통행 차단이 가장 확실한 예방책이기 때문이다. 실제로 프랑스 파리와 호주 멜버른 등은 스쿨존 진입 시 전원이 차단되는 기술을 의무화하여 보행자 사고를 40% 이상 줄였다. 사고가 난 뒤 단속하는 것은 ‘소 잃고 외양간 고치기’에 불과하다.</span></span>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에 이어 [본론 3(예상 반론 수용+재반박 4문단) · 결론(요약+당부 5문단)]을 써서 5문단 초고 완결하기",
        "activity_3": {
            "title": "나만의 논설문 초고 집필하기 ②: [본론 3(반론·재반박 4문단) · 결론(5문단)] 완결",
            "tag": "Step 3 방어 기둥·결론 집필 완결",
            "body_html": """
            <div style="border:0.9pt solid #1E8449; border-radius:5px; padding:5px 8px; background:#FFFFFF; font-size:7.3pt;">
              <span class="pencil-line"><strong>➍ [본론 3 - 예상 반론 수용+재반박]:</strong> <span class="t-ans">물론 스쿨존 내 전동 킥보드 통행을 전면 금지하면 출퇴근하거나 이동하는 성인 이용자들이 먼 길로 돌아가야 해서 불편하다는 반론도 있다. 그러나 ‘첫술에 배부르랴’라는 속담처럼 초기 불편함은 스쿨존 외곽에 우회 도로와 전용 주차 구역을 마련함으로써 충분히 해결할 수 있다. 무엇보다 어른들의 몇 분 빠른 이동 편의보다 어린이의 생명과 안전이 비교할 수 없을 만큼 더 소중한 가치이다.</span></span>
              <span class="pencil-line"><strong>➎ [결론 - 요약+실천 당부]:</strong> <span class="t-ans">요약하면, 전동 킥보드는 통학로 어린이에게 심각한 충돌 위험을 안겨 주므로 법적 통행 금지와 자동 차단 기술 도입이 시급하다. 그러므로 정부와 지자체는 스쿨존 내 전동 킥보드 통행 금지를 조속히 의무화하고, 시민 모두 안전한 통학로 만들기에 동참해야 한다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "16차시(W5 고쳐쓰기 및 공론장 발표) 직결",
            "prompt": "오늘 완성한 5문단 초고를 다시 읽으며, 다음 시간(16차시 퇴고)에 집중적으로 고쳐 보고 싶은 문장이나 아리송한 표현 1곳을 메모해 두세요.",
            "placeholder": "예: ‘이유는 ~하기 때문이다’나 ‘왜냐하면 ~기 때문이다’의 주어·부사어 호응이 맞는지 점검하겠다.",
            "example_answer": "문장이 길어진 2문단과 4문단에서 주어-서술어 호응과 ‘왜냐하면 ~기 때문이다’, ‘결코 ~아니다’ 호응이 정확한지 점검하겠다.",
        },
        "self_check": [
            "‘OO 기관이 발표한 조사에 따르면’ 공식 출처 인용 문장 틀을 사용했나요?",
            "4문단에서 ‘물론 ~ 그러나 ~’ 틀로 예상 반론을 수용하고 재반박했나요?",
            "관용표현·속담을 1개 이상 넣고 정중한 당위 어조(‘~해야 한다’)를 유지했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[W4 초고 집필하기 4대 표현 무기] ①설득적 제목(4차시) + ②공식 출처 인용 틀(‘OO 기관이 202X년 발표한 조사에 따르면 ~’) + ③반론·재반박 틀(‘물론 ~라는 반론도 있다. 그러나 [대안]으로 해결 가능하며 [상위 가치]가 더 중요하다’) + ④관용표현(‘발등에 불이 떨어지다, 소 잃고 외양간 고치기, 첫술에 배부르랴’) 및 격식 있는 당위 어조(‘~해야 한다’)",
            "intro_5min": "14차시에 설계한 5문단 개요표 위에 이제 살을 붙여 한 편의 완성된 논설문 초고를 탄생시키는 시간임을 안내한다. 초고를 쓸 때는 맞춤법이나 글씨에 너무 얽매이지 말고 좌측 페이지의 ‘4대 표현 무기’를 적극적으로 활용하여 끝까지 생각을 밀고 나가는 것이 중요함을 격려한다.",
            "ido_think_aloud_script": "“[활동 1]의 미숙한 초고 조각을 보세요. ‘어디서 들었는데 사고가 몇 배 늘었다고 카더라’라고 쓰면 독자가 코웃음을 치겠죠? 여기에 무기 ①번(공식 출처 인용 틀)을 장착해 볼게요! ‘한국도로교통공단이 2025년 발표한 분석에 따르면, 최근 5년간 전동 킥보드 보행자 사고가 4배 이상 급증했으며 어린이 피해의 68%가 통학로에서 발생했다.’ 와, 단숨에 신문 사설처럼 전문가다운 문장으로 변신했죠! 여러분의 2·3문단에도 이 공식 인용 틀을 꼭 넣어 보세요.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "초고를 쓸 때 ‘~하는 것 같다’나 ‘~라고 카더라’ 대신 어떤 종결 어미를 사용해야 논설문다운 설득력이 생길까요?",
                    "expected_ans": "근거 사실을 말할 때는 ‘~인 것으로 나타났다, ~라고 밝혔다’처럼 명확하게 쓰고, 주장을 말할 때는 ‘~해야 한다, ~할 필요가 있다’처럼 단호하고 정중한 당위 어조를 써야 합니다.",
                    "reprompt": "좌측 페이지 ‘무기 ①’과 ‘무기 ④’에서 문장 끝이 어떻게 끝나는지 밑줄 친 표현을 확인해 볼까요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "본론 2·3·4문단 사이에 관용표현(‘소 잃고 외양간 고치기’, ‘첫술에 배부르랴’)을 한두 개 넣으면 독자에게 어떤 효과가 있을까요?",
                    "expected_ans": "딱딱한 통계 숫자만 나열된 글보다 비유가 생생하게 살아나 독자가 문제의 심각성과 대안의 필요성을 훨씬 쉽고 강렬하게 공감할 수 있습니다.",
                    "reprompt": "5차시 〈일회용 컵 보증금제〉 칼럼에서 기자가 왜 ‘발등에 불이 떨어지다’와 ‘첫술에 배부르랴’를 썼었는지 떠올려 보세요.",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 2](제목·1·2·3문단)와 [활동 3](4·5문단)에 걸쳐 5문단 초고를 완주하도록 충분한 집필 시간을 부여하고 순회 코칭한다. 완성한 초고는 다음 시간(16차시 퇴고 및 시사 공론장 발표회)의 주인공이 됨을 안내하며 격려한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• [활동 1] 모범 답안:</strong> “첫째, 전동 킥보드는 어린이 보행자와 부딪힐 경우 심각한 안전사고를 일으키기 때문이다. 한국도로교통공단이 2025년 발표한 분석에 따르면, 최근 5년간 전동 킥보드 보행자 사고가 4배 이상 급증했으며 어린이 피해의 68%가 통학로에서 발생했다. 사고가 난 뒤에 대책을 세우는 것은 ‘소 잃고 외양간 고치기’에 불과하므로 사전 통행 금지가 필수적이다.”<br>
              <strong>• [활동 2] &amp; [활동 3] 5문단 초고 채점 기준:</strong> ① 설득적 제목, ② 서론(문제 실태·주장) - 본론 1·2(이유+공식 출처 인용 근거) - 본론 3(물론 반론 수용 + 그러나 재반박) - 결론(요약·당부) 5문단 완결성, ③ 관용표현·속담 1개 이상 활용, ④ 정중하고 명료한 당위 어조(‘~해야 한다’) 유지 여부를 확인하여 채점함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "본론 문단에 통계 자료만 길게 베껴 적고 정작 문단 첫머리의 중심 문장(‘첫째, ~기 때문이다’)을 빼먹음",
                    "diagnosis": "이유(중심 문장)와 근거 자료(뒷받침 문장)의 결합 순서를 놓치고 자료 나열에만 급급함",
                    "prescription": "본론 2·3문단의 첫 문장은 무조건 ‘첫째/둘째, [이유] ~기 때문이다.’로 시작하고, 그 뒤에 ‘실제로 [출처]에 따르면 ~’을 붙이도록 문단 첫 문장 공식을 점검함",
                },
                {
                    "error_case": "관용표현을 넣으려고 문맥에 맞지 않는 속담을 억지로 끼워 넣음",
                    "diagnosis": "관용표현의 정확한 문맥적 의미(위급성 강조 vs 임시방편 비판 vs 초기 어려움 극복)를 구분하지 못함",
                    "prescription": "좌측 페이지 ‘무기 ③’에 정리된 문단별 추천 관용표현 가이드를 보고 서론·본론·재반박 자리에 꼭 맞는 표현을 고르도록 지도함",
                },
            ],
            "scaffolding_down": "초고 문장 구성이 버거운 학생에게는 문단별 첫머리 담화표지와 인용 틀이 인쇄된 ‘문장 스타터 프레임(Sentence Frame)’을 제공하여 핵심 내용만 채워 넣으면 5문단이 완성되도록 돕는다.",
            "scaffolding_up": "초고를 다 쓴 학생은 2차시에 배운 ‘비록 ~일지라도’, ‘결코 ~아니다’ 같은 고급 부사어 호응 구문과 6차시에 배운 거시 지시어(‘이러한 실태는’)를 초고에 추가로 녹여 문장의 응집력을 높이게 한다.",
            "rubric": {
                "high": "설득적 제목, 5문단 논증 구조(서론-본론 1·2·3-결론), 공식 출처 인용 문장 틀, 반론 수용·재반박 문장 틀, 적절한 관용표현, 정중한 당위 어조 6가지 준거를 모두 갖추어 완성도 높은 논설문 초고를 집필함.",
                "mid": "5문단 구성과 핵심 주장·이유·근거는 갖추어 초고를 작성했으나, 공식 출처 인용 틀이나 관용표현 활용이 1곳 정도 누락됨.",
                "low": "문단 구분이 명확하지 않거나 근거 자료 인용과 반론·재반박 문단이 빠져 초고 완성을 위해 문장 틀 지원이 필요함.",
            },
        },
    },

    # =========================================================================
    # 16차시: G6-ARG-W5 (고쳐쓰기 및 학급 시사 공론장 발표회)
    # 2층 고행간 첨삭 줄공책 · 내용/조직/표현(주술·부사어 호응 [6국04-05]) 교정부호 3단계 퇴고
    # =========================================================================
    {
        "lesson_no": 16,
        "code": "G6-ARG-W5",
        "lesson_title": "[고쳐쓰기] 내용 타당성·자료 적절성·조직·문장 호응을 점검하여 교정부호로 퇴고하기",
        "std_badge": "[6국03-04] [6국04-05] 3단계 초인지 퇴고 · 주술/부사어 호응 · 교정부호",
        "student_goal": "2층 첨삭 줄공책과 표준 교정부호를 사용하여 논설문 초고의 ①내용 타당성(논리 오류·근거 3점 기준), ②조직 완결성(담화표지), ③표현 정확성(주어-서술어 및 부사어 호응 [6국04-05])을 3단계로 고쳐 쓰고 발표할 수 있다.",
        "marking_items": [
            ["mk-line-red", "주술·부사어 호응 오류", "[6국04-05] 이유는~때문이다 / 왜냐하면~때문이다 / 결코~아니다"],
            ["mk-bg", "논리·근거 오류", "성급한 일반화 및 카더라 출처 불량 근거"],
            ["mk-person", "담화표지 오류", "문단 역할과 어긋난 접속어 교정"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.4pt; color:#566573; margin-bottom:3px; display:flex; justify-content:space-between;">
          <span><strong>✍️ 쓰기 스튜디오 5단계 (고쳐쓰기):</strong> 2층 고행간 첨삭 줄공책 &amp; 3단계 초인지 퇴고(내용·조직·표현) 실연</span>
          <span><strong>핵심 문법:</strong> <code>[6국04-05]</code> 주어-서술어 및 부사어(<code>왜냐하면/결코</code>) 호응 교정 · 표준 교정부호 6종</span>
        </div>

        <!-- 2층 고행간 첨삭 줄공책 (draft-revision-grid) -->
        <div class="draft-revision-grid">
          <div class="notebook-pane">
            <!-- 제목 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">제목</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">✏️ [설득적 제목 보강]: ∨ 환경과 안전을 위협하는 (삽입)</div>
                  <div class="nb-lower-write"><strong>교내 일회용 비닐 우산 커버 사용을 금지하자</strong></div>
                </div>
              </div>
            </div>
            <!-- 1문단 서론 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">1문단<br>서론</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit"></div>
                  <div class="nb-lower-write">비 오는 날 학교 현관에는 한 번 쓰고 버려진 비닐 우산 커버가 넘쳐난다.</div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">❌① [주술 호응 교정]: 보호한다 ═➢ 보호해야 하기 때문이다. (주어 ‘이유는’과 호응)</div>
                  <div class="nb-lower-write">내가 비닐 커버 금지를 주장하는 <span class="mk-line-red">가장 큰 이유는 학교 환경을 <s>보호한다.</s></span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit"></div>
                  <div class="nb-lower-write">따라서 우리 학교는 비닐 커버 사용을 금지하고 다회용 빗물 제거기를 설치해야 한다.</div>
                </div>
              </div>
            </div>
            <!-- 2문단 본론1 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">2문단<br>본론1</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">❌② [부사어 호응 교정]: 반드시 사용을 줄여야 한다 ═➢ 토양과 바다를 오염시키기 때문이다.</div>
                  <div class="nb-lower-write">첫째, 플라스틱 쓰레기가 환경을 오염시키기 때문이다. <span class="mk-line-red">왜냐하면 비닐은 100년이 지나도 썩지 않아 <s>반드시 사용을 줄여야 한다.</s></span></div>
                </div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">❌③ [3점 검증 근거 교체]: 자원순환연대 조사에 따르면 연간 약 3억 장이 버려져 소각된다고 한다.</div>
                  <div class="nb-lower-write"><span class="mk-bg"><s>얼마 전 인터넷에서 누군가 쓴 글을 보니 버려지는 비닐 커버가 어마어마하다고 카더라.</s></span></div>
                </div>
              </div>
            </div>
            <!-- 3문단 본론2 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">3문단<br>본론2</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">❌④ [성급한 일반화·공포 호소 교정]: ═➢ 젖은 비닐이 바닥에 방치되면 미끄럼 사고 위험이 높아진다.</div>
                  <div class="nb-lower-write">둘째, 미끄러져 다칠 위험이 크기 때문이다. <span class="mk-bg"><s>어제 짝꿍이 넘어졌으니 무조건 전교생이 다 넘어져 팔다리를 다칠 것이다.</s></span></div>
                </div>
              </div>
            </div>
            <!-- 4문단 결론 블록 -->
            <div class="nb-para-block">
              <div class="nb-para-tag">4문단<br>결론</div>
              <div>
                <div class="nb-double-line">
                  <div class="nb-upper-edit">❌⑤ [담화표지 교정]: 그러나 ═➢ 요약하면, &nbsp; | &nbsp; ❌⑥ [부사어 호응]: 일이다 ═➢ 일이 아니다.</div>
                  <div class="nb-lower-write"><span class="mk-person"><s>그러나</s></span> 다회용 빗물 제거기를 쓰면 환경과 안전을 지킬 수 있다. 이 문제는 <span class="mk-line-red">결코 가벼운 <s>일이다.</s></span></div>
                </div>
              </div>
            </div>
          </div>

          <!-- 우측 교정부호 & 3단계 퇴고 가이드 패널 -->
          <div style="padding:5px 6px; background:#F8F9F9; font-size:7.1pt; line-height:1.38; display:flex; flex-direction:column; justify-content:space-between;">
            <div>
              <div style="font-weight:800; color:#922B21; border-bottom:1pt solid #E6B0AA; padding-bottom:2px; margin-bottom:4px;">
                🖍️ 표준 교정부호 &amp; 3단계 퇴고 렌즈
              </div>
              <div style="background:#fff; border:0.6pt solid #BDC3C7; border-radius:4px; padding:3.5px 5px; margin-bottom:4px;">
                <strong>[표준 교정부호 요약]</strong><br>
                • <code>═➢</code> 내용 고치기 (수정)<br>
                • <code>∨</code> 글자·어절 넣기 (삽입)<br>
                • <code><s>&nbsp;═&nbsp;</s></code> 빼기·지우기 (삭제)<br>
                • <code>┙</code> 줄 바꿈(문단 나누기)<br>
                • <code>⌒</code> 이어 쓰기 / <code>∨</code> 띄어쓰기
              </div>
              <div class="wing-box guide u5" style="margin-bottom:4px;">
                <div class="wing-box-title"><span>🎙️ 선생님 퇴고 사고구술</span><span class="role-chip">시범 I Do</span></div>
                <div class="think-row"><span class="think-tag">[표현①]</span><span>‘가장 큰 이유는 ~ 보호한다’는 주어(이유는)와 서술어가 안 맞아! <strong>‘~보호해야 하기 때문이다’</strong>로 고치자!</span></div>
                <div class="think-row"><span class="think-tag">[표현②·⑥]</span><span><strong>‘왜냐하면 ~기 때문이다’</strong>, <strong>‘결코 ~일이 아니다’</strong>로 부사어 호응을 맞춰야 해!</span></div>
                <div class="think-row"><span class="think-tag">[내용③·④]</span><span>익명 카더라 통신과 성급한 일반화를 지우고 공식 통계와 객관적 인과 문장으로 바꾸자!</span></div>
              </div>
            </div>
            <div class="wing-box question" style="margin-bottom:0;">
              <div class="wing-box-title"><span>❓ 날개 확인</span><span class="role-chip">함께 We Do</span></div>
              <div>위 줄공책의 오류 ①~⑥ 중 <strong>문장 성분 호응(<code>[6국04-05]</code>)</strong>을 어긴 번호 3개는 무엇인가요?</div>
              <span class="pencil-line">✏️ 번호: <span class="t-ans">①번(주술 호응), ②번(왜냐하면 호응), ⑥번(결코 호응)</span></span>
            </div>
          </div>
        </div>
        """,
        "activity_1": {
            "title": "2층 첨삭 줄공책 초고의 6대 오류(내용·조직·표현) 진단 및 교정 결과 정리하기",
            "tag": "Step 1 3단계 퇴고 오류 진단",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:16%;">퇴고 수준</th>
                  <th style="width:14%; text-align:center;">오류 번호</th>
                  <th style="width:32%;">오류 원인 진단</th>
                  <th style="width:38%;">바르게 고쳐 쓴 표현 (교정 결과)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="2" style="font-weight:700; text-align:center; background:#FDEDEC;">1단계: 내용<br>(3점 검증·논리)</td>
                  <td style="text-align:center; font-weight:700;">❌ ③번</td>
                  <td>익명 ‘카더라’ 인용 (<span class="blank-slot"><span class="t-ans">근거 출처 신뢰성 결여</span></span>)</td>
                  <td><span class="blank-slot"><span class="t-ans">자원순환연대 조사에 따르면 연간 약 3억 장이 버려져 소각된다고 한다.</span></span></td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:700;">❌ ④번</td>
                  <td>짝꿍 1명 사례로 전교생 단정 (<span class="blank-slot"><span class="t-ans">성급한 일반화 오류</span></span>)</td>
                  <td><span class="blank-slot"><span class="t-ans">젖은 비닐이 바닥에 방치되면 마찰력이 줄어 미끄럼 사고 위험이 높아진다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center; background:#FEF9E7;">2단계: 조직<br>(담화표지)</td>
                  <td style="text-align:center; font-weight:700;">❌ ⑤번</td>
                  <td>결론 요약 자리에 역접 표지(<code>그러나</code>) 사용</td>
                  <td><span class="blank-slot"><span class="t-ans">‘요약하면,’ 또는 ‘따라서’로 담화표지 교정</span></span></td>
                </tr>
                <tr>
                  <td rowspan="3" style="font-weight:700; text-align:center; background:#EBF5FB;">3단계: 표현<br>(문장 성분 호응<br><code>[6국04-05]</code>)</td>
                  <td style="text-align:center; font-weight:700;">❌ ①번</td>
                  <td>주어(<code>이유는</code>) ↔ 서술어(<code>보호한다</code>) 불일치</td>
                  <td><span class="blank-slot"><span class="t-ans">~ 가장 큰 이유는 학교 환경을 보호해야 하기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:700;">❌ ②번</td>
                  <td>부사어(<code>왜냐하면</code>) ↔ 서술어(<code>줄여야 한다</code>) 불일치</td>
                  <td><span class="blank-slot"><span class="t-ans">왜냐하면 비닐은 100년이 지나도 썩지 않아 환경을 오염시키기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td style="text-align:center; font-weight:700;">❌ ⑥번</td>
                  <td>부정 부사어(<code>결코</code>) ↔ 긍정 서술어(<code>일이다</code>) 불일치</td>
                  <td><span class="blank-slot"><span class="t-ans">이 문제는 결코 가벼운 일이 아니다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 3단계 퇴고 렌즈(내용·조직·표현)를 내 15차시 초고에 비추어 교정부호로 고쳐 쓰기",
        "activity_2": {
            "title": "내 논설문 초고 3단계 메타인지 퇴고 점검표 및 교정 기록",
            "tag": "Step 2 내 초고 3단계 퇴고",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">퇴고 단계</th>
                  <th style="width:52%;">초인지 퇴고 핵심 점검 질문</th>
                  <th style="width:12%; text-align:center;">점검</th>
                  <th style="width:18%;">내 초고 수정 메모</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700;">① 내용 수준<br>(타당성·근거)</td>
                  <td>• 주장과 이유가 타당하며 4대 논리 오류나 숨은 전제의 결함이 없는가?<br>• 근거 자료가 3점 기준(관련성·신뢰성·정확성)과 공식 인용 틀을 갖추었는가?</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">⭕ 완료</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">통계 출처 연도 보완</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700;">② 조직 수준<br>(구조·응집성)</td>
                  <td>• 서론-본론(지지 기둥 1·2 + 반론·재반박 기둥)-결론 5문단 구성이 완결되었는가?<br>• 문단 간 담화표지(<code>첫째, 둘째, 물론, 그러나, 요약하면</code>)가 자연스러운가?</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">⭕ 완료</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">4문단 ‘그러나’ 강조</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700;">③ 표현 수준<br>(<code>[6국04-05]</code>)</td>
                  <td>• 주어-서술어(<code>이유는 ~기 때문이다</code>) 및 부사어(<code>왜냐하면/결코/비록</code>) 호응이 바른가?<br>• 단정적·감정적 표현 없이 관용표현과 정중한 당위 어조를 사용했는가?</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">⭕ 완료</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">주술 호응 1곳 교정</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 퇴고를 마친 최종 논설문을 ‘우리 반 시사 공론장 발표회’에서 낭독하고 동료와 상호 비평하기",
        "activity_3": {
            "title": "우리 반 시사 공론장 발표회 및 대표 문장 정서(바르게 고쳐 쓰기)",
            "tag": "Step 3 최종본 완성 및 공론장 발표",
            "body_html": """
            <div style="border:0.9pt solid #922B21; border-radius:5px; padding:5px 8px; background:#FFFDFB; font-size:7.3pt;">
              <span class="pencil-line">🌟 <strong>[내가 가장 정성 들여 고쳐 쓴 핵심 문장 최종 정서]:</strong> <span class="t-ans">어린이 보호구역에서 전동 킥보드 사고를 막는 일은 결코 미룰 수 있는 문제가 아니다. 왜냐하면 어른들의 몇 분 빠른 이동 편의보다 어린이의 생명을 지키는 것이 무엇보다 소중하기 때문이다.</span></span>
              <span class="pencil-line">💬 <strong>[시사 공론장 동료 피드백 한마디]:</strong> <span class="t-ans">도로교통공단의 정확한 통계와 외곽 우회 도로라는 현실적인 재반박 대안을 함께 제시하여 반대 입장 독자까지 설득할 수 있는 훌륭한 논설문이다!</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "5단원 논설문 전 과정(1~16차시) 완주 갈무리",
            "prompt": "5단원 〈논설문〉 16차시를 모두 마친 소감과, 앞으로 뉴스나 광고·주장하는 글을 만날 때 내가 실천할 ‘비판적 문해력 다짐’을 적어 보세요.",
            "placeholder": "예: 이제 어떤 주장이나 그래프를 보더라도 숨은 전제와 출처의 3점 기준, Y축 눈금부터 꼼꼼히 따져 보겠다!",
            "example_answer": "앞으로 사회적 쟁점을 접할 때 감정에 휩쓸리지 않고 3점 검증 기준과 통계 그래프 눈금을 팩트체크하며 품격 있게 내 주장을 펼치겠다.",
        },
        "self_check": [
            "결함 초고의 6가지 오류(내용·조직·주술 및 부사어 호응)를 모두 찾아 고쳤나요?",
            "표준 교정부호를 사용하여 내 논설문 초고를 3단계로 꼼꼼히 퇴고했나요?",
            "시사 공론장 발표회에서 친구의 논설문을 경청하고 건설적인 피드백을 나누었나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[W5 고쳐쓰기 3단계 메타인지 퇴고 렌즈] 1단계 내용(3점 검증 출처 보강 · 4대 논리 오류 제거) ➔ 2단계 조직(서-본-결 문단 경계 · 담화표지 ‘그러나➔요약하면’ 교정) ➔ 3단계 표현([6국04-05] 주술 호응 ‘이유는 ~기 때문이다’ · 부사어 호응 ‘왜냐하면 ~때문이다 / 결코 ~아니다’) + [학급 시사 공론장 발표회]",
            "intro_5min": "세계적인 작가들도 초고를 쓴 뒤 수십 번 고쳐 쓰며 명작을 완성함을 이야기한다. 좌측 페이지의 ‘2층 고행간 첨삭 줄공책’에 실린 예시 초고에서 빨간 펜 편집자가 되어 6가지 숨은 오류를 찾아내는 활동을 시작한다.",
            "ido_think_aloud_script": "“좌측 2층 줄공책의 1문단 두 번째 줄을 볼까요? ‘내가 비닐 커버 금지를 주장하는 가장 큰 이유는 학교 환경을 보호한다.’ 어라, 주어는 ‘이유는’인데 서술어는 ‘보호한다’로 끝났어요! 이유가 어떻게 환경을 직접 보호하죠? 주어 ‘이유는’과 짝이 맞으려면 서술어를 ‘~보호해야 하기 때문이다’로 고쳐야 해요! 2문단의 ‘왜냐하면 ~ 줄여야 한다’도 마찬가지예요. ‘왜냐하면’이 나왔으면 끝은 반드시 ‘~오염시키기 때문이다’로 맺어야 호응이 딱 맞는답니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "책 속에 (Right There)",
                    "question": "2층 줄공책의 3문단(❌④번)과 4문단(❌⑥번)에는 각각 어떤 오류가 있었고 어떻게 고쳤나요?",
                    "expected_ans": "④번은 짝꿍 한 명이 넘어진 일로 전교생이 다 다칠 것이라고 과장한 ‘성급한 일반화 및 공포 호소 오류’여서 객관적 인과 문장으로 고쳤고, ⑥번은 부정 부사어 ‘결코’ 뒤에 긍정 서술어 ‘일이다’가 와서 ‘결코 가벼운 일이 아니다’로 고쳤습니다.",
                    "reprompt": "2층 줄공책 윗줄(nb-upper-edit)에 빨간 글씨로 적힌 첨삭 메모 ④번과 ⑥번을 함께 읽어 볼까요?",
                },
                {
                    "qar_type": "내 머릿속에 (On My Own)",
                    "question": "내가 15차시에 쓴 초고를 소리 내어 천천히 읽어 볼 때, 문장 호흡이 너무 길거나 주어와 서술어가 어색하게 느껴지는 곳은 어디인가요?",
                    "expected_ans": "(학생 개별 초고에 따라) 본론 문단에서 이유를 설명하는 문장이 너무 길어져 끝부분을 ‘~기 때문이다’로 명확히 다듬었습니다.",
                    "reprompt": "눈으로만 읽으면 놓치기 쉬운 호응 오류도 소리 내어(낭독하며) 읽으면 금방 귀에 걸린답니다. 내 초고를 작은 소리로 읽어 보세요!",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 1]을 통해 퇴고 원리를 완벽히 익힌 뒤, [활동 2] 점검표로 자신의 15차시 초고를 빨간 펜과 교정부호로 첨삭하고 [활동 3]에서 학급 시사 공론장 발표회를 연다. 5단원 논설문 16차시 대장정을 성공적으로 완주한 학생들에게 큰 박수를 보낸다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 확인 정답:</strong> <code>①번(주술 호응)</code>, <code>②번(왜냐하면 부사어 호응)</code>, <code>⑥번(결코 부사어 호응)</code>.<br>
              <strong>• [활동 1] 정답:</strong> ❌③번(근거 출처 신뢰성 결여 ➔ 자원순환연대 연간 3억 장 통계로 교체) / ❌④번(성급한 일반화 오류 ➔ 마찰력 감소로 미끄럼 사고 위험 증가로 교정) / ❌⑤번(결론 담화표지 오류 ➔ ‘요약하면,’ 또는 ‘따라서’로 교정) / ❌①번(<code>~ 가장 큰 이유는 학교 환경을 보호해야 하기 때문이다.</code>) / ❌②번(<code>왜냐하면 ~ 환경을 오염시키기 때문이다.</code>) / ❌⑥번(<code>이 문제는 결코 가벼운 일이 아니다.</code>).<br>
              <strong>• [활동 2] &amp; [활동 3] 채점 기준:</strong> 3단계 퇴고 기준(내용·조직·표현)과 표준 교정부호를 적용하여 초고의 오류를 수정하고 완결된 최종 문장을 정서했으면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "퇴고하라고 하면 글씨체나 띄어쓰기만 한두 군데 고치고 내용(논리·근거)과 조직(담화표지)은 전혀 보지 않음",
                    "diagnosis": "고쳐쓰기(Revising)를 단순 맞춤법 교정(Proofreading)으로만 좁게 인식함",
                    "prescription": "[활동 2]의 3단계 퇴고 점검표 순서대로 ‘①내용(3점 근거·논리 오류) ➔ ②조직(5문단·담화표지) ➔ ③표현(주술·부사어 호응 및 맞춤법)’을 큰 것에서 작은 것 순으로 점검하도록 안내함",
                },
                {
                    "error_case": "‘내가 주장하는 이유는 ~해야 한다’ 문장에서 왜 주술 호응이 틀렸는지 감각적으로 느끼지 못함",
                    "diagnosis": "2차시에서 배운 수식어 소거 전략을 적용하지 않아 주어(‘이유는’)와 서술어(‘~해야 한다’)의 거리가 멀어졌을 때 오류를 놓침",
                    "prescription": "문장 가운데 수식어를 손으로 가리고 ‘이유는 ~해야 한다(❌) vs 이유는 ~기 때문이다(⭕)’만 붙여 읽어 보게 하여 즉각 깨닫게 함",
                },
            ],
            "scaffolding_down": "내 초고에서 오류를 스스로 찾기 어려운 학생은 먼저 결함 초고(비닐 우산 커버 글)의 6가지 오류를 교정부호로 고쳐 본 뒤, 내 초고에서 ‘이유는 ~’, ‘왜냐하면 ~’, ‘결코 ~’가 쓰인 문장만 형광펜으로 찾아 끝맺음을 확인하게 한다.",
            "scaffolding_up": "짝과 초고를 바꾸어 ‘편집장 상호 첨삭(Peer Review)’을 실시하고, 짝의 글에서 ①가장 설득력 있는 근거 1곳 칭찬하기, ②더 보완하면 좋을 표현이나 재반박 대안 1곳 제안하기를 포스트잇에 적어 붙여 주게 한다.",
            "rubric": {
                "high": "결함 초고의 6대 오류(내용 타당성·3점 근거·담화표지·주술 및 부사어 호응 [6국04-05])를 100% 정확하게 진단·교정하고, 자신의 논설문 초고를 표준 교정부호로 3단계 퇴고하여 완결된 최종 논설문을 산출함.",
                "mid": "주술·부사어 호응 오류와 담화표지 오류는 바르게 고쳤으나, 내용 수준의 근거 출처 보강이나 논리적 세련미 다듬기가 다소 부분적임.",
                "low": "주어-서술어 및 부사어 호응 오류를 스스로 찾아내지 못하거나 교정부호 사용법을 적용하는 데 도움이 필요함.",
            },
        },
    },
]
