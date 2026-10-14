# -*- coding: utf-8 -*-
"""
Grade 6 Item Bank - Part 4: W1, W2, W3, W4 (Writing slots)
5-Option Standard (expected_opt_len = 5)
"""

from item_bank_schema_helper import build_expository_slot

slots_w = {}

# 12. G6-EXP-W1
slots_w["W1"] = build_expository_slot(
    grade_num=6,
    subskill_code="W1",
    subject="실과(인공지능 6-2) / 국어",
    unit="4. 인공지능과 미래 사회",
    concept="‘인공지능’ 화제를 ‘생성형 인공지능의 기계학습 작동 원리와 알고리즘 편향성 해결 방안’으로 좁히는 정밀 작문 계획",
    text_structure="과정·비교 + 문제·해결",
    structure_type_code="problem_solution",
    passage_title="글쓰기의 나침반 '계획하기': 생성형 인공지능과 알고리즘 편향성 작문 설계",
    paragraphs=[
        "글을 쓰기 전에 무엇을, 누구에게, 왜 쓸 것인지를 체계적으로 구상하는 단계를 '계획하기'라고 합니다. 많은 학생들이 글을 쓸 때 주제를 너무 넓게 잡아 내용이 산만해지는 실수를 범합니다. 성공적인 글을 쓰기 위해서는 광범위한 화제를 구체화하는 '3단계 깔때기 기법(Funneling)'을 적용해야 합니다.",
        "예를 들어 '첨단 과학 기술'이라는 거대한 상위 분야에서 시작하여, 1단계로 '인공지능(AI)'이라는 중위 화제로 좁히고, 2단계로 '생성형 인공지능의 기계학습'으로 범위를 좁힌 뒤, 마지막 3단계에서 '생성형 AI의 학습 원리와 알고리즘 편향성 해결 방안'이라는 `[핵심 대상]+[설명 측면 A·B]` 구조의 정밀한 목표 제목을 도출하는 것입니다.",
        "계획하기의 또 다른 핵심은 '예상 독자 프로파일 분석'입니다. 만약 독자가 초등학교 고학년 친구들이라면 어려운 수식이나 복잡한 신경망 코드를 나열하기보다, '사람이 쓴 글과 그림을 대량으로 읽고 다음 단어를 확률적으로 예측하는 챗봇 원리'처럼 친숙한 비유로 설명해야 합니다. 또한 'AI는 사람처럼 완벽한 판단을 내린다'는 독자의 흔한 오개념을 포착하고, 학습 데이터에 인간의 고정관념이 섞여 발생하는 '알고리즘 편향성'의 위험과 이를 교정하는 윤리적 정렬(Alignment) 기술을 대조적으로 제시하기로 계획해야 합니다.",
        "이처럼 목적, 독자, 주제의 3요소를 사전에 치밀하게 분석하고 설계도를 그릴 때, 비로소 독자의 지적 호기심을 충족시키는 강력한 설명문이 탄생할 수 있습니다."
    ],
    vocab_notes=[
        {"word": "깔때기 기법", "definition": "광범위하고 막연한 화제를 점진적으로 좁혀 구체적이고 명확한 작문 제목으로 이끌어내는 발상법"},
        {"word": "알고리즘 편향성", "definition": "인공지능이 학습한 데이터에 포함된 인간의 편견이나 왜곡이 결과물에 그대로 반영되는 오류"}
    ],
    visual_html="""<div class="p-3 bg-fuchsia-50 rounded border border-fuchsia-200">
      <h4 class="font-bold text-fuchsia-900 mb-2">🎯 3단계 주제 좁히기 깔때기 기법 (Funneling)</h4>
      <div class="space-y-1.5 text-xs">
        <div class="p-1.5 bg-white rounded border border-fuchsia-200 text-center font-semibold text-gray-700">
          [상위 분야] 첨단 정보통신 과학 기술
        </div>
        <div class="text-center text-fuchsia-600 font-bold">▼ 1단계 좁히기</div>
        <div class="p-1.5 bg-fuchsia-100 rounded border border-fuchsia-300 text-center font-semibold text-fuchsia-900">
          [중위 화제] 인공지능(AI)과 챗봇 기술
        </div>
        <div class="text-center text-fuchsia-600 font-bold">▼ 2단계 좁히기</div>
        <div class="p-1.5 bg-fuchsia-200 rounded border border-fuchsia-400 text-center font-bold text-fuchsia-950">
          [최종 목표 제목] 생성형 인공지능의 기계학습 작동 원리와 알고리즘 편향성 해결 방안
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-w1-c1", "text": "생성형 AI의 학습 원리와 알고리즘 편향성 해결 방안'이라는 `[핵심 대상]+[설명 측면 A·B]` 구조의 정밀한 목표 제목을 도출하는 것입니다", "role": "3단계 깔때기 목표 제목 명세", "para_idx": 1},
        {"cue_id": "g6-w1-c2", "text": "목적, 독자, 주제의 3요소를 사전에 치밀하게 분석하고 설계도를 그릴 때, 비로소 독자의 지적 호기심을 충족시키는 강력한 설명문이 탄생할 수 있습니다", "role": "계획하기 3대 요소 요약", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "작문 계획 3요소 매트릭스",
        "elements": {
            "주제 좁히기": "첨단기술 ➔ AI ➔ 생성형 AI 원리 및 편향성 해결",
            "독자 분석": "초등 고학년 대상 (수식 배제, 친숙한 비유, 오개념 해소)",
            "목적 및 측면": "원리 이해(측면 A) + 편향성 극복 대안 제시(측면 B)"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "작문 계획 및 주제 좁히기 원리 파악",
            "stem": "위 글의 1문단과 2문단을 바탕으로 할 때, '3단계 깔때기 기법'에 대한 설명으로 가장 바른 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "마지막 3단계에서 '생성형 AI의 학습 원리와 알고리즘 편향성 해결 방안'이라는 `[핵심 대상]+[설명 측면 A·B]` 구조의 정밀한 목표 제목을 도출하는 것입니다.",
            "options": [
                {"label": "①", "text": "광범위한 상위 화제에서 시작하여 설명할 구체적 대상과 측면 A·B로 좁혀 명확한 제목을 정하는 기법이다.", "is_correct": True, "formula": "정답", "explanation": "2문단의 깔때기 기법 원리와 일치합니다."},
                {"label": "②", "text": "글을 쓸 때 처음부터 끝까지 무조건 '우주'라는 단어 하나만 반복하는 기법이다.", "is_correct": False, "formula": "D5", "explanation": "주제 좁히기와 무관한 엉뚱한 진술입니다."},
                {"label": "③", "text": "계획하기 단계는 시간 낭비이므로 아무 생각 없이 즉흥적으로 쓰는 것이 원칙이다.", "is_correct": False, "formula": "D3", "explanation": "1문단의 계획하기 중요성과 정면 배치됩니다."},
                {"label": "④", "text": "화제를 가능한 한 무한대로 넓혀 백과사전 전체를 베껴 쓰는 기법이다.", "is_correct": False, "formula": "D1", "explanation": "산만해지는 오류를 유발합니다."},
                {"label": "⑤", "text": "예상 독자의 수준은 무시하고 글쓴이 혼자만 아는 암호로 쓰는 기법이다.", "is_correct": False, "formula": "D4", "explanation": "독자 분석 원리에 위배됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "독자 분석 및 내용 선정 추론",
            "stem": "3문단을 바탕으로 할 때, 초등학생 독자를 고려한 바람직한 글쓰기 전략으로 가장 적절한 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "어려운 수식이나 복잡한 신경망 코드를 나열하기보다, '사람이 쓴 글과 그림을 대량으로 읽고 다음 단어를 확률적으로 예측하는 챗봇 원리'처럼 친숙한 비유로 설명해야 합니다.",
            "options": [
                {"label": "①", "text": "어려운 수학 공식 대신 친숙한 비유를 활용하고 흔한 오개념을 바로잡아 준다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 제시된 초등 독자 맞춤 전략입니다."},
                {"label": "②", "text": "영어로 된 대학원 수준의 논문 코드를 그대로 복사해 넣는다.", "is_correct": False, "formula": "D5", "explanation": "독자 수준에 전혀 맞지 않습니다."},
                {"label": "③", "text": "인공지능은 신(神)이므로 절대 오류를 범하지 않는다고 거짓말을 쓴다.", "is_correct": False, "formula": "D4", "explanation": "오개념을 조장하는 왜곡입니다."},
                {"label": "④", "text": "모든 글자를 한자로만 표기하여 독자를 시험에 들게 한다.", "is_correct": False, "formula": "D6", "explanation": "부적절한 전달 방식입니다."},
                {"label": "⑤", "text": "독자가 이미 다 알고 있는 1더하기 1의 산수만 계속 설명한다.", "is_correct": False, "formula": "D2", "explanation": "새로운 지식 요구를 충족하지 못합니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 글쓰기 계획 단계에서 반드시 점검해야 할 핵심 3요소는?",
            "options": [
                {"label": "①", "text": "목적, 독자, 주제", "is_correct": True},
                {"label": "②", "text": "원고지, 만년필, 잉크", "is_correct": False},
                {"label": "③", "text": "인쇄소, 배달원, 트럭", "is_correct": False},
                {"label": "④", "text": "성적표, 등수, 시험지", "is_correct": False},
                {"label": "⑤", "text": "형용사, 부사, 감탄사", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "이처럼 목적, 독자, 주제의 3요소를 사전에 치밀하게 분석하고 설계도를 그릴 때, 비로소 독자의 지적 호기심을 충족시키는 강력한 설명문이 탄생할 수 있습니다.", "is_correct": True},
                {"label": "②", "text": "글을 쓰기 전에 무엇을, 누구에게, 왜 쓸 것인지를 체계적으로", "is_correct": False},
                {"label": "③", "text": "많은 학생들이 글을 쓸 때 주제를 너무 넓게 잡아", "is_correct": False},
                {"label": "④", "text": "계획하기의 또 다른 핵심은 '예상 독자 프로파일 분석'입니다.", "is_correct": False},
                {"label": "⑤", "text": "예를 들어 '첨단 과학 기술'이라는 거대한 상위 분야에서 시작하여,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "AI 설명문 작문 계획서 작성",
        "guide": "3단계 깔때기 기법을 적용하여 도출한 목표 제목과 예상 독자 맞춤 전략을 1문장으로 정리하세요.",
        "template": "본 글은 초등 독자의 눈높이에 맞추어, 생성형 인공지능의 [학습 원리]와 데이터 편견을 극복하는 [알고리즘 편향성 해결 방안]을 쉬운 비유로 설명하기로 계획한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "계획하기에서는 '상위 분야 ➔ 중위 화제 ➔ 구체적 대상+측면'으로 좁혀요."},
        "step1_2_drill": {"task": "첨단 기술(상위) ➔ AI(중위) ➔ 생성형 AI 원리와 편향성(구체적 제목) 순서 배열하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "좋은 글을 쓰려면 주제를 무작정 넓히기보다 설명할 대상을 구체적으로 좁혀야 한다.", "answer": "O", "reason": "3단계 깔때기 기법의 핵심입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 인공지능이 거짓말이나 편견을 말하는 이유",
        "situation": "아이와 함께 생성형 AI 챗봇을 써보았을 때",
        "parent_question": "인공지능 컴퓨터는 엄청 똑똑한데 왜 가끔 엉뚱한 거짓말이나 편견 섞인 대답을 할까?",
        "expected_answer": "인터넷에 사람들이 올려놓은 글을 그대로 배웠기 때문에, 사람들의 편견까지 닮아버리는 '알고리즘 편향성' 때문이래요!",
        "coaching_tip": "인공지능의 편리함과 함께 비판적 사고의 필요성을 함께 나누어 보세요."
    }
)

# 13. G6-EXP-W2
slots_w["W2"] = build_expository_slot(
    grade_num=6,
    subskill_code="W2",
    subject="과학·환경(생물다양성 6-1)",
    unit="3. 생물과 환경",
    concept="생물다양성의 3가지 수준과 서식지 단편화 해결(생태통로) 보고서 자료 수집·검증 및 시각자료 기획",
    text_structure="분류·분석 + 인과·문제해결",
    structure_type_code="classification",
    passage_title="생명의 그물망 '생물다양성'과 단절된 숲을 잇는 '생태통로' 조사 기획",
    paragraphs=[
        "지구상에 존재하는 생명체의 풍요로움을 뜻하는 '생물다양성'은 크게 세 가지 위계 수준으로 분류됩니다. 첫째 같은 종 안에서 다양한 형질이 나타나는 '유전적 다양성', 둘째 한 생태계 내에 서식하는 종의 풍부함을 뜻하는 '종 다양성', 셋째 숲, 습지, 사막 등 다양한 서식 환경이 존재하는 '생태계 다양성'입니다. 이 세 층위가 톱니바퀴처럼 맞물려야 생태계의 회복력이 건강하게 유지됩니다.",
        "그러나 도로 개설과 도시 개발로 인해 거대한 숲이 조각조각 쪼개지는 '서식지 단편화(Habitat Fragmentation)'가 심각한 위협으로 대두되었습니다. 서식지가 고립되면 야생동물이 짝짓기를 하지 못해 유전적 다양성이 급감하고, 먹이를 찾아 도로를 건너다 차에 치여 목숨을 잃는 '로드킬(Roadkill)' 사고가 빈발하게 됩니다.",
        "이에 대한 과학적 해결책으로 단절된 서식지를 육교나 터널 형태로 연결해 주는 '생태통로(Eco-corridor)'가 설치되고 있습니다. 성공적인 조사 보고서를 집필하기 위해서는 다양한 출처에서 자료를 수집하고 교차 검증해야 합니다. 환경부 국립생태원의 '생태통로 설치 전후 로드킬 발생 건수 추이 꺾은선그래프'와 야생동물 전문가의 현장 인터뷰를 함께 수집하여 데이터의 공신력을 확보해야 합니다.",
        "또한 수집된 통계의 성격에 맞게 시각자료를 기획해야 합니다. 시간에 따른 로드킬 감소 추세는 꺾은선그래프로, 통로를 이용하는 주요 동물 종별 비율은 원그래프로 배치할 때 독자에게 조사 결과의 설득력을 극대화할 수 있습니다."
    ],
    vocab_notes=[
        {"word": "생물다양성", "definition": "지구상의 모든 생물종, 생물이 가진 유전자, 그리고 생물들이 살아가는 생태계의 다양성을 포괄하는 개념"},
        {"word": "서식지 단편화", "definition": "도로나 댐 건설 등으로 연속적이던 서식지가 좁고 고립된 여러 조각으로 분할되는 현상"}
    ],
    visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
      <h4 class="font-bold text-emerald-900 mb-2">🌿 생물다양성 3층위 및 생태통로 시각자료 기획표</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-emerald-100">
          <strong class="text-emerald-800">생물다양성 3가지 수준</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>유전적 다양성:</strong> 종 내 개체 간 유전자 차이</li>
            <li><strong>종 다양성:</strong> 한 군집 내 종의 풍부도</li>
            <li><strong>생태계 다양성:</strong> 서식지 환경의 다양성</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-emerald-100">
          <strong class="text-emerald-800">보고서 시각자료 매칭 기획</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>로드킬 감소 변화:</strong> 꺾은선그래프 (시계열)</li>
            <li><strong>이용 동물 종 비율:</strong> 원그래프 (노루·고라니 등)</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-w2-c1", "text": "도로 개설과 도시 개발로 인해 거대한 숲이 조각조각 쪼개지는 '서식지 단편화(Habitat Fragmentation)'가 심각한 위협으로 대두되었습니다", "role": "서식지 단편화의 개념 및 문제", "para_idx": 1},
        {"cue_id": "g6-w2-c2", "text": "시간에 따른 로드킬 감소 추세는 꺾은선그래프로, 통로를 이용하는 주요 동물 종별 비율은 원그래프로 배치할 때", "role": "데이터 성격에 따른 시각자료 기획 원칙", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "생태 보고서 내용 생성 및 시각화 기획서",
        "biodiversity_levels": ["유전적 다양성", "종 다양성", "생태계 다양성"],
        "problem_solution": {
            "문제": "서식지 단편화 ➔ 유전적 고립 및 로드킬 발생",
            "해결": "생태통로 설치 (서식지 재연결)"
        },
        "visualization_plan": {
            "시계열 변화 (로드킬 수)": "꺾은선그래프",
            "동물 종별 비율": "원그래프"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "개념 분류 및 원인 분석",
            "stem": "위 글의 1문단과 2문단을 바탕으로 할 때, '서식지 단편화'가 생태계에 미치는 영향으로 옳은 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "서식지가 고립되면 야생동물이 짝짓기를 하지 못해 유전적 다양성이 급감하고, 먹이를 찾아 도로를 건너다 차에 치여 목숨을 잃는 '로드킬(Roadkill)' 사고가 빈발하게 됩니다.",
            "options": [
                {"label": "①", "text": "숲이 고립되어 야생동물의 짝짓기가 제한되어 유전적 다양성이 떨어지고 로드킬이 증가한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 서식지 단편화의 악영향입니다."},
                {"label": "②", "text": "모든 야생동물이 슈퍼맨처럼 날아다녀 로드킬이 완전히 0이 된다.", "is_correct": False, "formula": "D5", "explanation": "비과학적 허구입니다."},
                {"label": "③", "text": "도로가 생기면 유전적 다양성이 100배로 급증하여 생태계가 번영한다.", "is_correct": False, "formula": "D1", "explanation": "본문 내용과 정반대입니다."},
                {"label": "④", "text": "생물다양성은 오직 숲의 면적만 뜻하며 유전자와는 전혀 무관하다.", "is_correct": False, "formula": "D3", "explanation": "1문단의 3층위 정의(유전적 다양성 포함)와 위배됩니다."},
                {"label": "⑤", "text": "도로 주변에 동물들이 스스로 아파트를 짓고 정착한다.", "is_correct": False, "formula": "D6", "explanation": "황당한 왜곡입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "자료 성격에 따른 시각자료 기획 원칙",
            "stem": "3문단과 4문단을 바탕으로, 수집된 데이터에 최적화된 시각자료를 기획한 것으로 가장 바른 것은?",
            "target_para_idx": 3,
            "spotlight_quote": "시간에 따른 로드킬 감소 추세는 꺾은선그래프로, 통로를 이용하는 주요 동물 종별 비율은 원그래프로 배치할 때 독자에게 조사 결과의 설득력을 극대화할 수 있습니다.",
            "options": [
                {"label": "①", "text": "연도별 로드킬 건수의 감소 추세는 꺾은선그래프로, 동물 종별 구성 비율은 원그래프로 표현한다.", "is_correct": True, "formula": "정답", "explanation": "4문단의 시각자료 매칭 기획과 정확히 일치합니다."},
                {"label": "②", "text": "모든 데이터를 오직 소리 파일로만 녹음하고 글자는 한 자도 쓰지 않는다.", "is_correct": False, "formula": "D6", "explanation": "보고서 양식에 부합하지 않습니다."},
                {"label": "③", "text": "동물들의 비율을 볼 때 시간의 흐름을 나타내는 꺾은선그래프만 쓴다.", "is_correct": False, "formula": "D4", "explanation": "비율은 원그래프나 띠그래프가 적합합니다."},
                {"label": "④", "text": "공신력 있는 국립생태원 자료는 버리고 개인 블로그 헛소문만 도표로 만든다.", "is_correct": False, "formula": "D2", "explanation": "공신력 확보에 어긋납니다."},
                {"label": "⑤", "text": "시각자료는 독자를 혼란스럽게 하므로 무조건 삭제하는 것이 원칙이다.", "is_correct": False, "formula": "D5", "explanation": "시각자료의 설득력 극대화 기능과 반대됩니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 생물다양성을 구성하는 3대 층위에 속하지 않는 것은?",
            "options": [
                {"label": "①", "text": "화석연료 매장 다양성", "is_correct": True},
                {"label": "②", "text": "유전적 다양성", "is_correct": False},
                {"label": "③", "text": "종 다양성", "is_correct": False},
                {"label": "④", "text": "생태계 다양성", "is_correct": False},
                {"label": "⑤", "text": "서식지 환경의 다양성", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "첫째 같은 종 안에서 다양한 형질이 나타나는 '유전적 다양성', 둘째 한 생태계 내에 서식하는 종의 풍부함을 뜻하는 '종 다양성', 셋째 숲, 습지, 사막 등 다양한 서식 환경이 존재하는 '생태계 다양성'입니다.", "is_correct": True},
                {"label": "②", "text": "지구상에 존재하는 생명체의 풍요로움을 뜻하는 '생물다양성'은", "is_correct": False},
                {"label": "③", "text": "이 세 층위가 톱니바퀴처럼 맞물려야 생태계의 회복력이", "is_correct": False},
                {"label": "④", "text": "그러나 도로 개설과 도시 개발로 인해 거대한 숲이", "is_correct": False},
                {"label": "⑤", "text": "이에 대한 과학적 해결책으로 단절된 서식지를 육교나 터널", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "생태통로 보고서 내용 생성 및 시각화 메모",
        "guide": "서식지 단편화의 문제점과 생태통로 시각자료 기획 원리를 1문장으로 요약하세요.",
        "template": "도로 건설로 인한 [서식지 단편화]는 로드킬과 유전적 고립을 부르므로, [생태통로] 설치 효과를 로드킬 감소 꺾은선그래프와 동물 비율 원그래프로 입증해야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "통계 시각화 기획 시 '추세는 꺾은선, 비율은 원그래프, 비교는 막대'를 연결해요."},
        "step1_2_drill": {"task": "생물다양성 3층위(유전자, 종, 생태계) 카드 분류하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "생태통로는 서식지 단편화로 고립된 야생동물의 이동과 짝짓기를 돕는다.", "answer": "O", "reason": "본문에 설명된 생태통로의 설치 목적입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 고속도로 위 육교에 나무가 심어져 있는 이유",
        "situation": "고속도로를 달리다 산과 산을 잇는 초록색 육교를 보았을 때",
        "parent_question": "사람도 안 다니는 고속도로 위에 왜 흙을 깔고 나무를 심은 육교를 만들었을까?",
        "expected_answer": "고라니나 다람쥐 같은 동물들이 차에 치이지 않고 안전하게 숲을 건너다니는 '생태통로'래요!",
        "coaching_tip": "인간의 개발과 야생동물의 공존을 위한 과학적 노력에 대해 이야기를 나누어 보세요."
    }
)

# 14. G6-EXP-W3
slots_w["W3"] = build_expository_slot(
    grade_num=6,
    subskill_code="W3",
    subject="과학(지구와 달·우주항공 6-1)",
    unit="3. 지구와 달의 운동 및 우주 탐사",
    concept="로켓 추진의 작용·반작용 원리와 인공위성의 궤도별 분류(저궤도 vs 정지궤도) 복합 설명문 다층 개요 짜기",
    text_structure="복합 구조 (과정·인과 + 분류·비교·대조)",
    structure_type_code="comparison",
    passage_title="중력을 뚫고 우주로: 로켓의 추진 원리와 인공위성 궤도의 다층 개요 설계",
    paragraphs=[
        "복합적인 과학 원리를 설명할 때는 글 전체를 '처음-가운데-끝'의 3단계로 나누고, 가운데 부분을 소제목을 활용한 다층 개요(Multi-level Outline)로 정밀하게 설계해야 합니다. 로켓 공학과 인공위성 시스템을 다루는 설명문은 '과정·인과 구조'와 '분류·비교 구조'라는 두 가지 설명 방식을 유기적으로 결합해야 합니다.",
        "먼저 '처음' 단계에서는 지구 중력을 극복하고 우주로 나아가려는 인류의 도전과 글의 집필 목적을 명시합니다. 이어 '가운데 1(소제목: 가스를 내뿜어 솟구치는 뉴턴의 법칙)'에서는 로켓 엔진의 연료 연소 과정을 다룹니다. 고온·고압의 가스를 아래로 강하게 분사할 때(작용), 그 반발력으로 로켓 본체가 반대 방향인 하늘로 밀려 올라가는(반작용) 뉴턴의 '작용·반작용 원리'를 인과적 과정으로 서술합니다.",
        "다음으로 '가운데 2(소제목: 고도에 따라 임무가 다른 인공위성 궤도)'에서는 궤도별 특성을 비교·분류합니다. 고도 200~2000km를 돌며 지구를 하루에 14바퀴 이상 빠르게 회전하여 정밀 지구 관측을 수행하는 '저궤도 위성'과, 약 36,000km 상공에서 지구 자전 속도와 똑같이 돌아 지구에서 볼 때 항상 한자리에 멈춰 있는 것처럼 보이는 '정지궤도 위성(기상·통신 위성)'의 기능과 속도를 대조표로 배치하도록 설계합니다.",
        "마지막 '끝' 단계에서는 로켓 추진 기술과 위성 궤도 운용이 결합되어 우주 탐사의 새 시대를 열고 있음을 요약하며 미래 시사점을 제시합니다. 이처럼 각 문단의 하위 구조와 담화표지를 사전에 개요로 확정할 때, 복잡한 항공우주 과학도 독자에게 일목요연하게 전달됩니다."
    ],
    vocab_notes=[
        {"word": "작용·반작용 원리", "definition": "한 물체가 다른 물체에 힘을 가하면(작용), 다른 물체도 동시에 크기가 같고 방향이 반대인 힘을 가한다(반작용)는 물리 법칙"},
        {"word": "정지궤도 위성", "definition": "공전 주기가 지구 자전 주기(24시간)와 같아 지표면의 관측자에게 항상 같은 위치에 정지해 있는 것처럼 보이는 인공위성"}
    ],
    visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
      <h4 class="font-bold text-blue-900 mb-2">🚀 로켓과 인공위성 다층 개요 설계도 (Multi-level Outline)</h4>
      <div class="space-y-1.5 text-xs">
        <div class="p-1.5 bg-white rounded border border-blue-100 font-semibold text-gray-800">
          [처음] 중력 극복과 우주 진출의 목표 제시
        </div>
        <div class="p-1.5 bg-blue-100 rounded border border-blue-200 font-semibold text-blue-900">
          [가운데 1] 소제목: 로켓 추진 메커니즘 (가스 하향 분사 ➔ 작용·반작용 ➔ 상승)
        </div>
        <div class="p-1.5 bg-blue-100 rounded border border-blue-200 font-semibold text-blue-900">
          [가운데 2] 소제목: 위성 궤도 분류 (저궤도 관측위성 vs 36,000km 정지궤도 기상위성)
        </div>
        <div class="p-1.5 bg-white rounded border border-blue-100 font-semibold text-gray-800">
          [끝] 우주 과학 기술의 융합과 미래 가치 요약
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-w3-c1", "text": "고온·고압의 가스를 아래로 강하게 분사할 때(작용), 그 반발력으로 로켓 본체가 반대 방향인 하늘로 밀려 올라가는(반작용) 뉴턴의 '작용·반작용 원리'", "role": "로켓 추진 원리 명세", "para_idx": 1},
        {"cue_id": "g6-w3-c2", "text": "지구 자전 속도와 똑같이 돌아 지구에서 볼 때 항상 한자리에 멈춰 있는 것처럼 보이는 '정지궤도 위성(기상·통신 위성)'", "role": "정지궤도 위성의 핵심 원리", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "처음-가운데-끝 다층 개요표",
        "outline": {
            "처음": "우주 진출의 서막과 글의 목적",
            "가운데 1 (과정·인과)": "연소 가스 하향 분사 ➔ 작용·반작용 추진력 발생",
            "가운데 2 (비교·대조)": "저궤도(200~2000km, 정밀관측) vs 정지궤도(36,000km, 기상·통신)",
            "끝": "기술 종합 및 우주 탐사 시사점"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "물리 원리 및 추진 과정 파악",
            "stem": "위 글의 2문단에 제시된 로켓 엔진의 추진 원리로 가장 적절한 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "고온·고압의 가스를 아래로 강하게 분사할 때(작용), 그 반발력으로 로켓 본체가 반대 방향인 하늘로 밀려 올라가는(반작용) 뉴턴의 '작용·반작용 원리'를 인과적 과정으로 서술합니다.",
            "options": [
                {"label": "①", "text": "가스를 아래로 분사하는 작용에 대해 반대 방향으로 밀어 올리는 반작용 힘으로 추진된다.", "is_correct": True, "formula": "정답", "explanation": "2문단의 뉴턴 작용·반작용 원리 설명과 정확히 일치합니다."},
                {"label": "②", "text": "우주 허공에 걸려 있는 거대한 밧줄을 당겨 올라간다.", "is_correct": False, "formula": "D6", "explanation": "비과학적인 상상입니다."},
                {"label": "③", "text": "로켓 스스로 숨을 들이마셔 중력을 완전히 지워버린다.", "is_correct": False, "formula": "D5", "explanation": "황당한 왜곡입니다."},
                {"label": "④", "text": "가스를 위쪽으로 뿜어 아래로 곤두박질치는 힘을 쓴다.", "is_correct": False, "formula": "D3", "explanation": "반대 방향으로 비행하게 됩니다."},
                {"label": "⑤", "text": "연료를 전혀 쓰지 않고 오직 자석의 힘으로만 뜬다.", "is_correct": False, "formula": "D1", "explanation": "가스 분사 연소 과정에 위배됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "개요 조직 및 궤도 비교 분석",
            "stem": "3문단을 바탕으로 할 때, '가운데 2'에 배치할 저궤도 위성과 정지궤도 위성의 비교로 옳은 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "약 36,000km 상공에서 지구 자전 속도와 똑같이 돌아 지구에서 볼 때 항상 한자리에 멈춰 있는 것처럼 보이는 '정지궤도 위성(기상·통신 위성)'의 기능과 속도를 대조표로 배치하도록 설계합니다.",
            "options": [
                {"label": "①", "text": "저궤도 위성은 지구를 빠르게 돌며 정밀 관측하고, 정지궤도 위성은 36,000km 상공에서 지구 자전과 같은 속도로 돈다.", "is_correct": True, "formula": "정답", "explanation": "3문단의 대조 내용과 온전히 일치합니다."},
                {"label": "②", "text": "정지궤도 위성은 공전을 멈추고 땅바닥에 텐트를 치고 산다.", "is_correct": False, "formula": "D5", "explanation": "우주 상공에서 자전과 같은 속도로 도는 것입니다."},
                {"label": "③", "text": "저궤도 위성은 100년에 한 번만 지구를 돈다.", "is_correct": False, "formula": "D2", "explanation": "하루에 14바퀴 이상 빠르게 돕니다."},
                {"label": "④", "text": "두 위성 모두 고도 10m 높이에서 날아다닌다.", "is_correct": False, "formula": "D4", "explanation": "수백 km 및 36,000km 상공입니다."},
                {"label": "⑤", "text": "기상 위성은 반드시 저궤도에만 배치해야 한다.", "is_correct": False, "formula": "D3", "explanation": "기상·통신 위성은 한 지역을 지속 관측하는 정지궤도가 적합합니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 지구 자전 주기와 똑같은 속도로 공전하여 지표면에서 볼 때 항상 한자리에 머무는 것처럼 보이는 위성은?",
            "options": [
                {"label": "①", "text": "정지궤도 위성", "is_correct": True},
                {"label": "②", "text": "저궤도 관측 위성", "is_correct": False},
                {"label": "③", "text": "달 탐사선", "is_correct": False},
                {"label": "④", "text": "태양 궤도선", "is_correct": False},
                {"label": "⑤", "text": "소행성 충돌선", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "약 36,000km 상공에서 지구 자전 속도와 똑같이 돌아 지구에서 볼 때 항상 한자리에 멈춰 있는 것처럼 보이는 '정지궤도 위성(기상·통신 위성)'", "is_correct": True},
                {"label": "②", "text": "복합적인 과학 원리를 설명할 때는 글 전체를 '처음-가운데-끝'", "is_correct": False},
                {"label": "③", "text": "고도 200~2000km를 돌며 지구를 하루에 14바퀴 이상", "is_correct": False},
                {"label": "④", "text": "로켓 엔진의 연료 연소 과정을 다룹니다.", "is_correct": False},
                {"label": "⑤", "text": "마지막 '끝' 단계에서는 로켓 추진 기술과 위성 궤도 운용이", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "우주 로켓 및 위성 다층 개요 작성",
        "guide": "로켓의 작용·반작용 추진 원리와 정지궤도 위성의 특성을 1문장으로 정리하세요.",
        "template": "로켓은 가스를 뿜는 [작용·반작용]의 힘으로 중력을 벗어나며, 약 36,000km 상공의 [정지궤도 위성]은 지구 자전 속도와 일치하여 통신과 기상 관측을 수행한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "다층 개요 작성 시 '처음(목적) ➔ 가운데1(과정) ➔ 가운데2(비교) ➔ 끝(요약)' 틀을 지켜요."},
        "step1_2_drill": {"task": "저궤도(지구 관측) vs 정지궤도(통신·기상) 위성 용도 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "정지궤도 위성은 지구 자전 속도와 같아서 멈춰 있는 것처럼 보인다.", "answer": "O", "reason": "본문에 설명된 정지궤도의 원리입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 공기가 없는 우주에서 로켓이 앞으로 나가는 비결",
        "situation": "누리호 발사 뉴스나 우주 영화를 볼 때",
        "parent_question": "우주에는 밀어낼 공기가 없는데 로켓이 어떻게 쌩쌩 날아갈 수 있을까?",
        "expected_answer": "로켓 스스로 불타는 가스를 뒤로 뿜어내면, 그 반동(반작용)으로 앞으로 튕겨져 나가는 거래요! 풍선 바람 빠질 때 날아가는 것처럼요.",
        "coaching_tip": "풍선을 불어 손을 놓았을 때 날아가는 놀이로 작용·반작용을 체감하게 해 주세요."
    }
)

# 15. G6-EXP-W4
slots_w["W4"] = build_expository_slot(
    grade_num=6,
    subskill_code="W4",
    subject="사회(지구촌 갈등과 협력 6-2)",
    unit="3. 지속 가능한 지구촌의 평화와 발전",
    concept="지구촌 열대우림 파괴의 다각적 원인과 국제기구(UN)·비정부기구(NGO)의 해결 노력 복합 보고서 집필",
    text_structure="인과 + 비교·대조 + 문제·해결",
    structure_type_code="problem_solution",
    passage_title="지구의 허파가 불타고 있다: 열대우림 파괴의 다각적 원인과 국제사회의 복합 해법",
    paragraphs=[
        "남아메리카 아마존을 비롯한 열대우림은 지구상 산소의 상당 부분을 생산하고 막대한 양의 이산화 탄소를 흡수하여 흔히 '지구의 허파'이자 거대한 '탄소흡수원(Carbon Sink)'으로 불립니다. 또한 전 세계 생물종의 절반 이상이 서식하는 생물다양성의 보고이기도 합니다. 그러나 최근 수십 년 동안 무분별한 벌채와 개간으로 인해 매년 한반도 면적에 달하는 열대우림이 지구상에서 사라지고 있습니다.",
        "열대우림 파괴의 원인은 단일하지 않고 복합적인 경제적 요인이 얽혀 있습니다. <그림 1>의 아마존 산림 벌채 원인별 비율 원그래프에서 확인할 수 있듯이, 파괴의 약 65%는 대규모 기업형 소 방목을 위한 목초지 조성 때문입니다. 여기에 글로벌 곡물 기업들의 대두(콩) 대량 경작이 약 15%, 상업적 원목 채벌이 10%를 차지합니다. 즉, 선진국의 값싼 소고기와 사료 수요를 충족시키기 위해 지구의 허파를 불태우고 있는 것입니다.",
        "열대우림의 파괴는 단순한 나무의 소멸에 그치지 않고 가속화된 기후변화라는 부메랑으로 돌아옵니다. 나무가 불타면서 흡수되어 있던 수십억 톤의 탄소가 한꺼번에 대기 중으로 방출되고, 지표면의 수분 증발 능력이 상실되어 극심한 가뭄과 사막화가 촉발됩니다.",
        "이러한 지구촌 위기를 해결하기 위해 국제기구(UN)와 비정부기구(NGO)가 다각적인 공조를 펼치고 있습니다. UN은 열대우림을 보존하는 개발도상국에 탄소배출권 판매 대금으로 경제적 보상을 지급하는 '레드플러스(REDD+)' 정책을 추진하고 있습니다. 한편 그린피스와 같은 국제 NGO는 산림을 파괴하여 생산된 소고기나 콩의 국제 유통을 거부하는 소비자 불매 운동과 현장 감시 활동을 전개하고 있습니다.",
        "결국 열대우림을 지키는 일은 현지 국가만의 책임이 아니라, 육류 소비를 줄이고 지속 가능한 인증 목재를 소비하려는 전 세계 시민 모두의 연대와 책임 있는 실천에 달려 있습니다."
    ],
    vocab_notes=[
        {"word": "탄소흡수원", "definition": "광합성을 통해 대기 중의 이산화 탄소를 흡수하여 유기물 형태로 고정·저장하는 산림이나 바다 생태계"},
        {"word": "레드플러스(REDD+)", "definition": "개발도상국의 산림 파괴를 방지하고 온실가스 배출을 줄인 노력에 대해 경제적 인센티브를 제공하는 UN 기후 메커니즘"}
    ],
    visual_html="""<div class="p-3 bg-green-50 rounded border border-green-200">
      <h4 class="font-bold text-green-900 mb-2">🌴 아마존 열대우림 벌채 원인 및 국제 협력 솔루션</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-green-100">
          <strong class="text-red-700">&lt;그림 1&gt; 벌채 주요 원인 비율</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>소 방목 목초지 조성: 약 65%</li>
            <li>대두(사료용 콩) 경작: 약 15%</li>
            <li>상업적 원목 채벌: 약 10%</li>
            <li>기타 인프라: 약 10%</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-green-100">
          <strong class="text-blue-700">국제사회 해결 공조</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>UN REDD+:</strong> 산림 보존 개도국에 탄소배출권 경제 보상</li>
            <li><strong>국제 NGO:</strong> 파괴 기업 불매 운동 및 현장 감시</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-w4-c1", "text": "파괴의 약 65%는 대규모 기업형 소 방목을 위한 목초지 조성 때문입니다", "role": "열대우림 파괴의 최대 원인", "para_idx": 1},
        {"cue_id": "g6-w4-c2", "text": "UN은 열대우림을 보존하는 개발도상국에 탄소배출권 판매 대금으로 경제적 보상을 지급하는 '레드플러스(REDD+)' 정책을 추진하고 있습니다", "role": "UN의 제도적 경제 보상 정책", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "열대우림 복합 보고서 구조도",
        "causes": {
            "소 방목 (65%)": "선진국 육류 소비",
            "대두 경작 (15%)": "사료용 콩 수출",
            "목재 채벌 (10%)": "상업 원목"
        },
        "consequences": "탄소 대량 방출 ➔ 온난화 가속 및 사막화",
        "global_solutions": {
            "UN 기구": "REDD+ (탄소배출권 보상)",
            "환경 NGO": "파괴 생산품 유통 거부 및 감시",
            "세계 시민": "지속가능 인증 소비 및 연대"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "복합 원인 및 시각자료 지시문 확인",
            "stem": "위 글의 2문단과 <그림 1>을 바탕으로 할 때, 열대우림 파괴의 최대 원인으로 옳은 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "<그림 1>의 아마존 산림 벌채 원인별 비율 원그래프에서 확인할 수 있듯이, 파괴의 약 65%는 대규모 기업형 소 방목을 위한 목초지 조성 때문입니다.",
            "options": [
                {"label": "①", "text": "기업형 소 방목을 위한 목초지 조성이 약 65%로 가장 큰 비중을 차지한다.", "is_correct": True, "formula": "정답", "explanation": "2문단과 시각자료에 명시된 사실입니다."},
                {"label": "②", "text": "원주민들이 모닥불을 피우는 행위가 99%를 차지한다.", "is_correct": False, "formula": "D5", "explanation": "기업형 방목과 농업이 주원인입니다."},
                {"label": "③", "text": "우주선 착륙장 건설이 유일한 원인이다.", "is_correct": False, "formula": "D6", "explanation": "허구의 오답입니다."},
                {"label": "④", "text": "나무가 스스로 걸어가서 바다에 빠지는 자연 현상이다.", "is_correct": False, "formula": "D5", "explanation": "인위적 벌채를 왜곡한 오답입니다."},
                {"label": "⑤", "text": "소고기 소비와 산림 벌채는 아무 관련이 없다.", "is_correct": False, "formula": "D1", "explanation": "목초지 조성이 65%로 직결됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "국제 협력 대안 및 시민 실천 추론",
            "stem": "4문단과 5문단에 제시된 국제사회의 해결 노력에 대한 설명으로 가장 적절한 것은?",
            "target_para_idx": 3,
            "spotlight_quote": "UN은 열대우림을 보존하는 개발도상국에 탄소배출권 판매 대금으로 경제적 보상을 지급하는 '레드플러스(REDD+)' 정책을 추진하고 있습니다.",
            "options": [
                {"label": "①", "text": "UN은 보존 개도국에 경제적 보상(REDD+)을 제공하고, NGO는 불매 운동과 감시를 통해 협력한다.", "is_correct": True, "formula": "정답", "explanation": "4문단의 기구별 역할 분담과 완벽히 일치합니다."},
                {"label": "②", "text": "UN은 남아있는 아마존 나무를 모조리 불태우라고 명령했다.", "is_correct": False, "formula": "D1", "explanation": "보존 정책과 정반대입니다."},
                {"label": "③", "text": "NGO는 산림 파괴 기업에 상금을 주고 훈장을 수여한다.", "is_correct": False, "formula": "D5", "explanation": "불매 운동 및 감시를 전개합니다."},
                {"label": "④", "text": "선진국 시민들은 고기를 지금보다 10배 더 많이 먹어야 산림이 살아난다.", "is_correct": False, "formula": "D3", "explanation": "육류 소비 감소가 권장됩니다."},
                {"label": "⑤", "text": "모든 열대우림 문제를 브라질 혼자서만 책임지게 방치한다.", "is_correct": False, "formula": "D4", "explanation": "전 세계 시민의 연대 책임입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 개발도상국이 산림을 보존하여 온실가스를 감축했을 때 경제적 인센티브를 제공하는 UN 기후 프로그램은?",
            "options": [
                {"label": "①", "text": "레드플러스 (REDD+)", "is_correct": True},
                {"label": "②", "text": "화석연료 보조금", "is_correct": False},
                {"label": "③", "text": "자유무역협정 (FTA)", "is_correct": False},
                {"label": "④", "text": "삼권분립 헌법", "is_correct": False},
                {"label": "⑤", "text": "원목 무제한 벌채권", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "UN은 열대우림을 보존하는 개발도상국에 탄소배출권 판매 대금으로 경제적 보상을 지급하는 '레드플러스(REDD+)' 정책을 추진하고 있습니다.", "is_correct": True},
                {"label": "②", "text": "남아메리카 아마존을 비롯한 열대우림은 지구상 산소의", "is_correct": False},
                {"label": "③", "text": "열대우림 파괴의 원인은 단일하지 않고 복합적인 경제적 요인이", "is_correct": False},
                {"label": "④", "text": "열대우림의 파괴는 단순한 나무의 소멸에 그치지 않고", "is_correct": False},
                {"label": "⑤", "text": "결국 열대우림을 지키는 일은 현지 국가만의 책임이 아니라,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "열대우림 보존 복합 보고서 작성",
        "guide": "소 방목으로 인한 열대우림 파괴 원인과 UN REDD+ 정책을 1문장으로 정리하세요.",
        "template": "열대우림은 [소 방목 목초지] 조성으로 파괴되고 있으므로, 산림 보존 개도국에 경제적 혜택을 주는 [UN REDD+] 정책과 글로벌 시민 연대로 지켜내야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "복합 보고서 작성 시 '원인(육류 수요) ➔ 영향(탄소 방출) ➔ 대책(UN REDD+)' 흐름을 구성해요."},
        "step1_2_drill": {"task": "UN(REDD+ 경제 보상) vs NGO(불매·감시) 역할 분담 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "열대우림 보존은 현지 국가뿐 아니라 전 세계 소비자와 국제기구의 협력이 필요하다.", "answer": "O", "reason": "본문에 제시된 결론입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 소고기 햄버거와 아마존 정글의 안타까운 연결고리",
        "situation": "햄버거 가게에서 점심을 먹을 때 아이와 나눌 질문",
        "parent_question": "우리가 맛있는 소고기를 먹는 것과 저 멀리 아마존 밀림이 불타는 게 어떻게 연결되어 있을까?",
        "expected_answer": "소를 많이 키우려고 풀밭(목초지)을 만드느라 아마존 나무들을 베어내기 때문이래요! 고기를 남기지 않고 감사히 먹어야겠어요.",
        "coaching_tip": "우리의 일상적 소비가 지구 반대편 생태계와 어떻게 연결되어 있는지 글로벌 생태 감수성을 나누어 보세요."
    }
)
