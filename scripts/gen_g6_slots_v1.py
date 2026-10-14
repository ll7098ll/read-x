# -*- coding: utf-8 -*-
"""
Grade 6 Item Bank - Part 1: V1-1, V1-2, V1-3, V1-4 (Expository slots)
5-Option Standard (expected_opt_len = 5)
"""

from item_bank_schema_helper import build_expository_slot

slots_v1 = {}

# 1. G6-EXP-V1-1
slots_v1["V1-1"] = build_expository_slot(
    grade_num=6,
    subskill_code="V1-1",
    subject="과학(계절의 변화 6-2)",
    unit="2. 계절의 변화",
    concept="지구 자전축 기울기와 태양의 남중 고도·낮의 길이·기온 변화의 상관관계",
    text_structure="인과·과정 + 비교",
    structure_type_code="causal",
    passage_title="지구 자전축의 기울기와 사계절 기온 변화의 메커니즘",
    paragraphs=[
        "우리나라와 같은 북반구 중위도 지역에서는 계절에 따라 기온과 낮의 길이가 주기적으로 변화합니다. 이러한 사계절 변화가 일어나는 근본적인 원인은 지구가 공전 궤도면에 대하여 약 23.5도 기울어진 채 태양 주위를 공전하기 때문입니다.",
        "태양이 남쪽 하늘 가장 높은 곳에 도달했을 때의 각도를 '태양의 남중 고도'라고 합니다. 여름철(하지 무렵)에는 북반구가 태양 쪽으로 기울어져 태양의 남중 고도가 약 76.5도까지 높아집니다. 남중 고도가 높아지면 일정한 면적에 도달하는 태양 복사 에너지가 집중되고, 태양이 지표면 위에 머무는 낮의 길이도 약 14시간 30분으로 길어져 지표면이 받는 열량이 크게 증가합니다.",
        "반면 겨울철(동지 무렵)에는 북반구가 태양 반대편으로 기울어져 태양의 남중 고도가 약 29.5도로 낮아집니다. 이로 인해 태양 광선이 비스듬히 비추어 단위 면적당 도달하는 복사 에너지가 분산되고, 낮의 길이도 약 9시간 30분으로 짧아져 기온이 영하로 떨어지게 됩니다.",
        "결국 '자전축의 기울어진 공전'이라는 단 하나의 원인이 '남중 고도 변화'와 '낮의 길이 변화'를 유도하고, 이것이 복합적으로 작용하여 사계절의 뚜렷한 기온 차이를 만들어 내는 것입니다."
    ],
    vocab_notes=[
        {"word": "남중 고도", "definition": "태양이 자오선을 통과하여 하루 중 남쪽 하늘 가장 높이 떴을 때 지평선과 이루는 각도"},
        {"word": "복사 에너지", "definition": "빛이나 전자기파의 형태로 물체에서 방출되어 공간을 전달되는 열에너지"}
    ],
    visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
      <h4 class="font-bold text-blue-900 mb-2">☀️ 하지 vs 동지 태양 남중 고도 및 낮의 길이 비교</h4>
      <table class="w-full text-xs text-left border-collapse bg-white">
        <thead>
          <tr class="bg-blue-100 text-blue-900 border-b">
            <th class="p-1.5 border">구분</th><th class="p-1.5 border">태양 남중 고도</th><th class="p-1.5 border">낮의 길이</th><th class="p-1.5 border">단위 면적당 열량</th><th class="p-1.5 border">대표 기온</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="p-1.5 border font-semibold text-red-600">여름 (하지)</td><td class="p-1.5 border">약 76.5° (높음)</td><td class="p-1.5 border">약 14시간 30분</td><td class="p-1.5 border">집중 (많음)</td><td class="p-1.5 border">28~33°C (고온)</td></tr>
          <tr><td class="p-1.5 border font-semibold text-blue-600">겨울 (동지)</td><td class="p-1.5 border">약 29.5° (낮음)</td><td class="p-1.5 border">약 9시간 30분</td><td class="p-1.5 border">분산 (적음)</td><td class="p-1.5 border">-5~2°C (저온)</td></tr>
        </tbody>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v11-c1", "text": "태양이 남쪽 하늘 가장 높은 곳에 도달했을 때의 각도를 '태양의 남중 고도'라고 합니다", "role": "남중 고도 개념 정의", "para_idx": 1},
        {"cue_id": "g6-v11-c2", "text": "자전축의 기울어진 공전'이라는 단 하나의 원인이 '남중 고도 변화'와 '낮의 길이 변화'를 유도하고", "role": "사계절 기온 변화의 핵심 원인", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "인과 사슬망",
        "cause": "자전축 23.5도 기울어진 채 공전",
        "intermediates": ["계절별 태양 남중 고도 변화 (하지 76.5° vs 동지 29.5°)", "낮의 길이 변화 (14.5시간 vs 9.5시간)"],
        "result": "단위 면적당 태양 복사 에너지 차이 ➔ 사계절 기온 변화"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "세부 사실 및 한정 조건 확인",
            "stem": "위 글의 2문단과 3문단에 제시된 여름철(하지)과 겨울철(동지)의 특징을 바르게 비교한 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "여름철(하지 무렵)에는 북반구가 태양 쪽으로 기울어져 태양의 남중 고도가 약 76.5도까지 높아집니다.",
            "options": [
                {"label": "①", "text": "여름철에는 태양 남중 고도가 높아져 단위 면적당 도달하는 복사 에너지가 집중된다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 남중 고도가 약 76.5도로 높아져 에너지가 집중된다고 명시했습니다."},
                {"label": "②", "text": "겨울철에는 낮의 길이가 약 14시간 30분으로 여름철보다 길어진다.", "is_correct": False, "formula": "D3", "explanation": "낮의 길이가 14시간 30분인 것은 여름철(하지)입니다."},
                {"label": "③", "text": "여름철과 겨울철 모두 태양의 남중 고도는 45도로 일정하다.", "is_correct": False, "formula": "D1", "explanation": "하지는 76.5도, 동지는 29.5도로 크게 다릅니다."},
                {"label": "④", "text": "지구 자전축이 수직으로 서 있기 때문에 기온 차이가 발생한다.", "is_correct": False, "formula": "D5", "explanation": "자전축이 약 23.5도 기울어져 있기 때문입니다."},
                {"label": "⑤", "text": "겨울철에는 태양 광선이 수직으로 비추어 지표면 열량이 극대화된다.", "is_correct": False, "formula": "D4", "explanation": "겨울철에는 태양 광선이 비스듬히 비추어 열량이 분산됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "핵심 인과 관계 추론",
            "stem": "글쓴이가 4문단에서 강조한 사계절 기온 변화의 근본적인 원인은 무엇인가요?",
            "target_para_idx": 3,
            "spotlight_quote": "결국 '자전축의 기울어진 공전'이라는 단 하나의 원인이 '남중 고도 변화'와 '낮의 길이 변화'를 유도하고, 이것이 복합적으로 작용하여 사계절의 뚜렷한 기온 차이를 만들어 내는 것입니다.",
            "options": [
                {"label": "①", "text": "지구 자전축이 기울어진 채 공전하여 남중 고도와 낮의 길이가 복합적으로 변화하기 때문이다.", "is_correct": True, "formula": "정답", "explanation": "4문단의 결론 명제와 완벽히 일치합니다."},
                {"label": "②", "text": "지구와 태양 사이의 거리가 겨울에 10배 더 멀어지기 때문이다.", "is_correct": False, "formula": "D2", "explanation": "거리 변화가 아니라 자전축 기울기에 의한 남중 고도 변화가 핵심입니다."},
                {"label": "③", "text": "달이 지구 주위를 도는 삭망월 주기 때문만으로 결정된다.", "is_correct": False, "formula": "D4", "explanation": "달의 공전이 아닌 지구의 자전축 기울기와 공전입니다."},
                {"label": "④", "text": "북반구와 남반구의 공기 밀도가 매달 임의로 바뀌기 때문이다.", "is_correct": False, "formula": "D6", "explanation": "본문에 없는 자의적 추측입니다."},
                {"label": "⑤", "text": "태양이 스스로 빛을 내는 온도를 계절마다 인위적으로 조절하기 때문이다.", "is_correct": False, "formula": "D5", "explanation": "비과학적인 왜곡 진술입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 겨울철에 기온이 크게 떨어지는 직접적인 이유 두 가지를 가장 바르게 묶은 것은?",
            "options": [
                {"label": "①", "text": "태양 남중 고도의 하강과 낮 시간의 단축", "is_correct": True},
                {"label": "②", "text": "태양 자전 속도의 증가와 비의 증가", "is_correct": False},
                {"label": "③", "text": "지구 자전의 일시 정지와 바닷물 증발", "is_correct": False},
                {"label": "④", "text": "달의 인력 약화와 낮 시간의 증가", "is_correct": False},
                {"label": "⑤", "text": "북반구 대기의 산소 고갈과 구름 차단", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "태양 광선이 비스듬히 비추어 단위 면적당 도달하는 복사 에너지가 분산되고, 낮의 길이도 약 9시간 30분으로 짧아져 기온이 영하로 떨어지게 됩니다.", "is_correct": True},
                {"label": "②", "text": "우리나라와 같은 북반구 중위도 지역에서는 계절에 따라", "is_correct": False},
                {"label": "③", "text": "태양이 남쪽 하늘 가장 높은 곳에 도달했을 때의 각도를", "is_correct": False},
                {"label": "④", "text": "남중 고도가 높아지면 일정한 면적에 도달하는 태양 복사 에너지가 집중되고,", "is_correct": False},
                {"label": "⑤", "text": "여름철(하지 무렵)에는 북반구가 태양 쪽으로 기울어져", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "계절 변화 인과 보고서 작성",
        "guide": "지구 자전축의 기울기와 태양 남중 고도 변화를 연결하여 1문장의 원인-결과 복문으로 작성하세요.",
        "template": "지구 자전축이 약 [23.5도] 기울어진 채 공전하기 때문에, 계절별로 태양의 [남중 고도]와 낮의 길이가 달라져 사계절 기온 차이가 발생한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "복합 수치 그래프 독해 시 가로축(계절)과 세로축(고도·시간)의 대응 관계를 확인해요."},
        "step1_2_drill": {"task": "하지(76.5°, 14.5시간)와 동지(29.5°, 9.5시간) 수치 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "여름철에는 태양 남중 고도가 높아 지표면의 단위 면적당 열량이 증가한다.", "answer": "O", "reason": "본문에 명시된 인과 관계입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 여름 낮이 겨울보다 긴 과학적 이유",
        "situation": "여름 저녁 7시에도 밖이 환할 때 아이와 나눌 이야기",
        "parent_question": "여름에는 왜 저녁 7시가 넘어도 대낮처럼 밝고 더울까?",
        "expected_answer": "지구 자전축이 태양 쪽으로 기울어져서 해가 높이 뜨고 낮이 14시간 넘게 길어지기 때문이래요!",
        "coaching_tip": "계절의 변화가 단순한 날씨 변화가 아니라 지구의 우주적 운동에서 비롯됨을 칭찬해 주세요."
    }
)

# 2. G6-EXP-V1-2
slots_v1["V1-2"] = build_expository_slot(
    grade_num=6,
    subskill_code="V1-2",
    subject="과학(연소와 소화 6-2)",
    unit="3. 연소와 소화",
    concept="연소의 3요소와 화재 유형별 소화(불 끄기)의 과학적 메커니즘",
    text_structure="분석(연소 3요소) + 분류(소화 방법) + 인과",
    structure_type_code="classification",
    passage_title="불이 붙는 조건 '연소'와 불을 끄는 과학 '소화'",
    paragraphs=[
        "물질이 산소와 빠르게 반응하면서 빛과 열을 내며 타는 현상을 '연소'라고 합니다. 연소가 일어나기 위해서는 반드시 세 가지 요소가 동시에 갖추어져야 하는데, 이를 '연소의 3요소'라고 부릅니다. 첫째는 탈 수 있는 '탈 물질', 둘째는 연소를 돕는 '산소', 셋째는 물질에 불이 붙는 최저 온도인 '발화점 이상의 온도'입니다. 이 중 어느 하나라도 결핍되면 연소는 성립하지 않습니다.",
        "화재를 진압하는 '소화'는 바로 이 연소의 3요소 중 하나 이상을 과학적으로 제거하는 과정입니다. 소화 방법은 제거하는 요소에 따라 크게 세 가지로 분류됩니다. 첫째, 물을 뿌려 온도를 발화점 아래로 낮추는 '냉각 소화'입니다. 물은 비열과 증발열이 매우 커서 불타는 물질의 열을 급격히 흡수합니다.",
        "둘째, 공기의 접근을 차단하여 산소 공급을 끊는 '질식 소화'입니다. 알코올램프의 뚜껑을 덮거나 이산화 탄소 소화기를 분사하여 산소 농도를 15% 이하로 떨어뜨리는 방식이 이에 해당합니다. 셋째, 불에 탈 수 있는 물질 자체를 멀리 치우는 '제거 소화'입니다. 산불 발생 시 맞불을 놓아 중간 나무를 미리 태워 버리거나, 가스 밸브를 잠그는 것이 대표적입니다.",
        "화재 유형에 맞는 올바른 소화법을 선택하는 것은 매우 중요합니다. 예를 들어 기름 화재에 물을 뿌리면 기름이 물 위에 뜨면서 불길이 번지므로, 물을 이용한 냉각 소화 대신 모래나 전용 포말 소화기를 이용한 질식 소화를 적용해야 합니다."
    ],
    vocab_notes=[
        {"word": "발화점", "definition": "외부의 직접적인 불꽃 없이도 물질이 스스로 타기 시작하는 가장 낮은 온도"},
        {"word": "질식 소화", "definition": "산소의 유입을 물리적·화학적으로 차단하여 연소를 정지시키는 소화 방법"}
    ],
    visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
      <h4 class="font-bold text-amber-900 mb-2">🔥 연소의 3요소 vs 3대 소화 메커니즘</h4>
      <div class="grid grid-cols-3 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-red-200 text-center">
          <span class="font-bold text-red-700">1. 탈 물질 제거</span>
          <p class="mt-1 text-gray-700"><strong>제거 소화</strong><br>가스 밸브 차단, 산불 방화선 구축</p>
        </div>
        <div class="p-2 bg-white rounded border border-blue-200 text-center">
          <span class="font-bold text-blue-700">2. 산소 차단</span>
          <p class="mt-1 text-gray-700"><strong>질식 소화</strong><br>뚜껑 덮기, CO₂·모래 도포 (산소 15% 미만)</p>
        </div>
        <div class="p-2 bg-white rounded border border-green-200 text-center">
          <span class="font-bold text-green-700">3. 발화점 미만 냉각</span>
          <p class="mt-1 text-gray-700"><strong>냉각 소화</strong><br>물 분사 (단, 기름 화재는 물 금지)</p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v12-c1", "text": "연소가 일어나기 위해서는 반드시 세 가지 요소가 동시에 갖추어져야 하는데", "role": "연소의 3요소 전제", "para_idx": 0},
        {"cue_id": "g6-v12-c2", "text": "소화 방법은 제거하는 요소에 따라 크게 세 가지로 분류됩니다", "role": "소화의 3대 분류 기준", "para_idx": 1}
    ],
    graphic_organizer={
        "type": "연소 삼각형 및 소화 분류 체계도",
        "triangle": ["탈 물질", "산소", "발화점 이상의 온도"],
        "counter_actions": {
            "탈 물질": "제거 소화 (가스 밸브 차단)",
            "산소": "질식 소화 (이산화 탄소 분사)",
            "온도": "냉각 소화 (물 분사)"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "상하위 개념 및 인과 관계 파악",
            "stem": "위 글의 2문단과 3문단을 바탕으로 할 때, 소화 메커니즘의 연결이 가장 올바른 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "알코올램프의 뚜껑을 덮거나 이산화 탄소 소화기를 분사하여 산소 농도를 15% 이하로 떨어뜨리는 방식이 이에 해당합니다.",
            "options": [
                {"label": "①", "text": "알코올램프의 뚜껑을 덮는 것은 산소 공급을 차단하는 질식 소화에 해당한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에서 뚜껑을 덮어 산소를 차단하는 질식 소화의 예시로 제시되었습니다."},
                {"label": "②", "text": "물을 뿌리는 것은 탈 물질 자체를 화학적으로 분해하는 제거 소화이다.", "is_correct": False, "formula": "D3", "explanation": "물을 뿌리는 것은 온도를 낮추는 냉각 소화입니다."},
                {"label": "③", "text": "산불 발생 시 맞불을 놓는 것은 산소 농도를 100%로 높이는 과정이다.", "is_correct": False, "formula": "D5", "explanation": "주변 나무를 미리 태워 탈 물질을 없애는 제거 소화입니다."},
                {"label": "④", "text": "가스 밸브를 잠그는 것은 온도를 발화점 아래로 떨어뜨리는 냉각 소화이다.", "is_correct": False, "formula": "D2", "explanation": "탈 물질의 유입을 막는 제거 소화입니다."},
                {"label": "⑤", "text": "기름 화재에는 물을 다량으로 뿌려 냉각 소화하는 것이 가장 안전하다.", "is_correct": False, "formula": "D1", "explanation": "기름 화재에 물을 뿌리면 불길이 번지므로 금지됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "조건문 및 상황 적용 추론",
            "stem": "4문단의 내용을 고려할 때, 기름 냄비에 불이 붙었을 때 취해야 할 가장 올바른 조치는?",
            "target_para_idx": 3,
            "spotlight_quote": "기름 화재에 물을 뿌리면 기름이 물 위에 뜨면서 불길이 번지므로, 물을 이용한 냉각 소화 대신 모래나 전용 포말 소화기를 이용한 질식 소화를 적용해야 합니다.",
            "options": [
                {"label": "①", "text": "물을 붓지 말고 뚜껑을 덮거나 젖은 수건을 덮어 공기(산소)를 차단한다.", "is_correct": True, "formula": "정답", "explanation": "기름 화재에는 물을 피하고 산소를 차단하는 질식 소화를 해야 합니다."},
                {"label": "②", "text": "찬물을 한 바가지 끼얹어 온도를 급격히 낮춘다.", "is_correct": False, "formula": "D1", "explanation": "기름이 튀어 화재가 확산되는 위험한 행위입니다."},
                {"label": "③", "text": "부채질을 세게 하여 발화점 온도를 날려 버린다.", "is_correct": False, "formula": "D4", "explanation": "산소 공급을 늘려 불길을 더 키우는 행위입니다."},
                {"label": "④", "text": "기름을 냄비에 가득 더 부어서 온도를 희석한다.", "is_correct": False, "formula": "D5", "explanation": "탈 물질을 추가하여 대형 화재를 유발합니다."},
                {"label": "⑤", "text": "창문을 모두 활짝 열고 산소가 잘 들어오게 기다린다.", "is_correct": False, "formula": "D6", "explanation": "산소 유입으로 연소가 촉진됩니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 다음 중 연소의 3요소와 소화 방법의 짝이 잘못 연결된 것은?",
            "options": [
                {"label": "①", "text": "발화점 이상의 온도 차단 — 제거 소화", "is_correct": True},
                {"label": "②", "text": "산소 차단 — 질식 소화", "is_correct": False},
                {"label": "③", "text": "탈 물질 차단 — 제거 소화", "is_correct": False},
                {"label": "④", "text": "온도 하강 — 냉각 소화", "is_correct": False},
                {"label": "⑤", "text": "공기 유입 방지 — 질식 소화", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "물을 뿌려 온도를 발화점 아래로 낮추는 '냉각 소화'입니다.", "is_correct": True},
                {"label": "②", "text": "물질이 산소와 빠르게 반응하면서 빛과 열을 내며 타는 현상을", "is_correct": False},
                {"label": "③", "text": "불에 탈 수 있는 물질 자체를 멀리 치우는 '제거 소화'입니다.", "is_correct": False},
                {"label": "④", "text": "화재 유형에 맞는 올바른 소화법을 선택하는 것은 매우 중요합니다.", "is_correct": False},
                {"label": "⑤", "text": "연소가 일어나기 위해서는 반드시 세 가지 요소가 동시에 갖추어져야", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "연소-소화 과학 설명문 문장 완성",
        "guide": "연소의 3요소와 대응하는 3대 소화 원리를 포함하여 논리적인 1문장으로 정리하세요.",
        "template": "연소의 3요소인 [탈 물질], [산소], [발화점 이상의 온도] 중 하나를 차단함으로써 화재를 진압하는 원리를 [소화]라고 부른다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "연소 삼각형의 각 변과 3대 소화(냉각, 질식, 제거)를 1:1 매칭해요."},
        "step1_2_drill": {"task": "가스 밸브(제거), 뚜껑 덮기(질식), 물 분사(냉각) 연결하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "기름 화재에는 냉각을 위해 물을 뿌리는 것이 가장 안전하다.", "answer": "X", "reason": "기름이 물 위에 떠서 불길이 번지므로 질식 소화를 해야 합니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 프라이팬 불났을 때 물을 뿌리면 안 되는 이유",
        "situation": "주방에서 요리 중 안전 수칙을 함께 나눌 때",
        "parent_question": "요리하다가 기름 프라이팬에 불이 붙으면 왜 절대 물을 부으면 안 될까?",
        "expected_answer": "기름은 물보다 가벼워서 물 위에 둥둥 뜨며 불이 사방으로 튀기 때문이래요! 뚜껑을 덮어 산소를 끊어야 해요.",
        "coaching_tip": "가정 내 소화기 위치와 주방 화재 대처법을 아이와 함께 직접 점검해 보세요."
    }
)

# 3. G6-EXP-V1-3
slots_v1["V1-3"] = build_expository_slot(
    grade_num=6,
    subskill_code="V1-3",
    subject="사회(지속가능한 지구촌 6-2)",
    unit="3. 지속 가능한 지구촌",
    concept="온실효과와 기후위기의 발생 메커니즘 및 탄소중립(Net-Zero) 해결 전략",
    text_structure="복합 구조 (상위 문제·해결 + 하위 분류·인과·비교)",
    structure_type_code="problem_solution",
    passage_title="온실효과의 빛과 그림자: 기후위기 메커니즘과 탄소중립의 길",
    paragraphs=[
        "지구 대기는 태양 복사 에너지를 통과시키고 지표면이 방출하는 지구 복사 에너지의 일부를 흡수하여 지구를 따뜻하게 유지하는데, 이를 '온실효과'라고 합니다. 온실효과 자체가 없다면 지구의 평균 기온은 영하 18도까지 떨어져 생명체가 생존할 수 없습니다. 따라서 적정 수준의 온실가스는 지구의 생명 유지에 필수적입니다.",
        "문제는 산업혁명 이후 화석연료(석탄·석유)의 과도한 연소와 무분별한 삼림 벌채로 인해 대기 중 온실가스 농도가 급격히 짙어졌다는 점입니다. 온실가스는 주로 '이산화 탄소(CO₂)', '메탄(CH₄)', '아산화 질소(N₂O)' 등으로 분류됩니다. 특히 이산화 탄소는 배출량이 가장 많아 지구 온난화 기여도의 65% 이상을 차지하며, 대기 중에 수백 년 동안 머무는 특징이 있습니다.",
        "온실가스의 과다 배출은 열의 방출을 지나치게 가로막아 지구 평균 기온을 상승시켰고, 이는 해수면 상승, 슈퍼 태풍, 가뭄 등 전 지구적 기후위기를 초래했습니다. 만약 기온이 산업화 이전 대비 1.5도 이상 상승할 경우, 수많은 생물종이 멸종 위기에 처할 것으로 경고됩니다.",
        "이러한 재앙을 막기 위해 국제사회가 합의한 궁극적 해결책이 바로 '탄소중립(Net-Zero)'입니다. 탄소중립이란 인간 활동에 의한 온실가스 배출량을 최대한 감축하고, 남은 배출량은 숲 조성이나 탄소 포집·저장(CCUS) 기술을 통해 흡수하여 실질적인 순 배출량을 '0(Zero)'으로 만드는 전략입니다. 에너지 전환과 자원순환은 이제 인류 생존의 필수 조건입니다."
    ],
    vocab_notes=[
        {"word": "온실효과", "definition": "대기 중의 기체가 지구가 방출하는 적외선 복사열을 흡수하여 지표면을 보온하는 현상"},
        {"word": "탄소중립", "definition": "온실가스 배출량과 흡수량이 균형을 이루어 실질적인 배출 총량이 0이 되게 하는 상태"}
    ],
    visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
      <h4 class="font-bold text-emerald-900 mb-2">🌍 온실가스 기여도 vs 탄소중립 넷제로(Net-Zero) 공식</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-emerald-100">
          <strong class="text-emerald-800">주요 온실가스 배출 기여도</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>이산화 탄소 (CO₂): 약 65% (화석연료 연소)</li>
            <li>메탄 (CH₄): 약 16% (농축산업·폐기물)</li>
            <li>기타 (N₂O, F가스): 약 19%</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-emerald-100">
          <strong class="text-emerald-800">탄소중립 Net-Zero 메커니즘</strong>
          <p class="mt-1 text-gray-700">
            <strong>[배출 감축]</strong> 신재생에너지 전환 + 효율 향상<br>
            <strong>+ [흡수 격리]</strong> 산림 조성 + CCUS 포집 기술<br>
            <strong>= 순 배출량 0 (Net-Zero)</strong>
          </p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v13-c1", "text": "온실효과 자체가 없다면 지구의 평균 기온은 영하 18도까지 떨어져 생명체가 생존할 수 없습니다", "role": "온실효과의 본래 기능", "para_idx": 0},
        {"cue_id": "g6-v13-c2", "text": "실질적인 순 배출량을 '0(Zero)'으로 만드는 전략입니다", "role": "탄소중립의 명확한 정의", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "상위 문제-해결 복합 구조도",
        "problem_structure": {
            "origin": "온실효과는 본래 생명 유지에 필수적이었음 (영하 18도 방지)",
            "worsening": "화석연료 과다 사용 ➔ CO2 65% 기여 ➔ 열 방출 차단",
            "crisis": "평균 기온 상승 ➔ 해수면 상승, 슈퍼 태풍 등 기후위기"
        },
        "solution_structure": {
            "strategy": "탄소중립 (Net-Zero)",
            "methods": ["재생에너지 전환(배출 저감)", "산림 및 CCUS 기술(흡수·격리)"],
            "target": "순 배출량 0 달성"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "세부 개념 및 오개념 판별",
            "stem": "위 글의 1문단과 2문단을 읽고 추론할 수 있는 내용으로 가장 적절한 것은?",
            "target_para_idx": 0,
            "spotlight_quote": "온실효과 자체가 없다면 지구의 평균 기온은 영하 18도까지 떨어져 생명체가 생존할 수 없습니다.",
            "options": [
                {"label": "①", "text": "자연적인 온실효과는 지구 기온을 생명체가 살 수 있는 온도로 유지해 주는 긍정적 역할을 한다.", "is_correct": True, "formula": "정답", "explanation": "1문단에서 온실효과가 없다면 영하 18도가 되어 살 수 없다고 서술했습니다."},
                {"label": "②", "text": "온실효과는 인류에게 백해무익하므로 지구상에서 온실가스를 100% 완전히 없애야 한다.", "is_correct": False, "formula": "D5", "explanation": "온실가스가 전혀 없으면 영하 18도가 되므로 잘못된 극단적 왜곡입니다."},
                {"label": "③", "text": "이산화 탄소는 배출된 즉시 공기 중에서 1초 만에 완전 소멸된다.", "is_correct": False, "formula": "D3", "explanation": "수백 년 동안 대기에 머무는 특징이 있습니다."},
                {"label": "④", "text": "온실가스 중 메탄이 전체 온난화의 95% 이상을 유발하는 최대 원인이다.", "is_correct": False, "formula": "D1", "explanation": "이산화 탄소가 65% 이상을 차지합니다."},
                {"label": "⑤", "text": "산업혁명 이전의 지구 기온은 섭씨 100도 이상으로 끓어올랐다.", "is_correct": False, "formula": "D2", "explanation": "본문 내용과 무관한 허구입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "상위 문제-해결 구조 분석",
            "stem": "4문단에 제시된 '탄소중립(Net-Zero)'의 참된 의미를 가장 정확하게 설명한 것은?",
            "target_para_idx": 3,
            "spotlight_quote": "탄소중립이란 인간 활동에 의한 온실가스 배출량을 최대한 감축하고, 남은 배출량은 숲 조성이나 탄소 포집·저장(CCUS) 기술을 통해 흡수하여 실질적인 순 배출량을 '0(Zero)'으로 만드는 전략입니다.",
            "options": [
                {"label": "①", "text": "온실가스 배출을 최대한 줄이고 남은 양은 숲이나 기술로 흡수하여 순 배출 총량을 0으로 맞추는 것", "is_correct": True, "formula": "정답", "explanation": "4문단의 정의 문장과 완벽히 부합합니다."},
                {"label": "②", "text": "석탄 발전소만 10배로 더 짓고 나무는 모조리 벌채하는 정책", "is_correct": False, "formula": "D5", "explanation": "탄소중립에 정면으로 위배되는 행위입니다."},
                {"label": "③", "text": "모든 에너지를 탄소 배출이 가장 많은 중유 발전으로 통일하는 것", "is_correct": False, "formula": "D4", "explanation": "화석연료를 늘리는 것이 아닙니다."},
                {"label": "④", "text": "인류가 숨 쉬는 것을 완전히 금지하여 탄소를 없애는 조치", "is_correct": False, "formula": "D6", "explanation": "비현실적인 왜곡입니다."},
                {"label": "⑤", "text": "배출량을 줄이지 않고 오직 탄소세만 부과하여 돈을 걷는 것", "is_correct": False, "formula": "D2", "explanation": "실질적 감축과 흡수를 통한 넷제로가 본질입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 다음 중 기후위기 해결을 위한 탄소중립의 2대 축으로 가장 바르게 짝지어진 것은?",
            "options": [
                {"label": "①", "text": "온실가스 배출량 감축과 흡수·저장 기술의 결합", "is_correct": True},
                {"label": "②", "text": "화석연료 사용 증대와 삼림 벌채 확대", "is_correct": False},
                {"label": "③", "text": "원자재 낭비와 쓰레기 매립지 대폭 증설", "is_correct": False},
                {"label": "④", "text": "지구 자전축 변경과 달 표면 기지 건설", "is_correct": False},
                {"label": "⑤", "text": "대기 중 온실가스 전면 방출과 세금 면제", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "온실가스 배출량을 최대한 감축하고, 남은 배출량은 숲 조성이나 탄소 포집·저장(CCUS) 기술을 통해 흡수하여 실질적인 순 배출량을 '0(Zero)'으로 만드는 전략입니다.", "is_correct": True},
                {"label": "②", "text": "지구 대기는 태양 복사 에너지를 통과시키고 지표면이 방출하는", "is_correct": False},
                {"label": "③", "text": "문제는 산업혁명 이후 화석연료(석탄·석유)의 과도한 연소와", "is_correct": False},
                {"label": "④", "text": "특히 이산화 탄소는 배출량이 가장 많아 지구 온난화 기여도의", "is_correct": False},
                {"label": "⑤", "text": "만약 기온이 산업화 이전 대비 1.5도 이상 상승할 경우,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "기후위기 극복 탄소중립 요약문 작성",
        "guide": "온실효과의 과다로 인한 문제와 탄소중립의 해결 원리를 1문장의 요약문으로 완성하세요.",
        "template": "화석연료 연소로 과다해진 온실가스가 [기후위기]를 초래하므로, 배출 감축과 산림 흡수를 결합하여 순 배출량을 0으로 만드는 [탄소중립]을 실천해야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "문제-해결 복합 구조에서는 원인(과다 배출)과 대안(감축+흡수)의 대응을 확인해요."},
        "step1_2_drill": {"task": "온실효과의 긍정 기능(보온) vs 부정 기능(온난화 심화) 구분하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "탄소중립이란 배출량을 줄이고 흡수량을 늘려 순 배출량을 0으로 만드는 것이다.", "answer": "O", "reason": "본문에 제시된 정의와 일치합니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: '탄소 배출 0'은 공장을 아예 안 돌리는 걸까?",
        "situation": "뉴스에서 2050 탄소중립 뉴스를 볼 때 아이와 나눌 질문",
        "parent_question": "탄소중립(Net-Zero)은 공장이나 차를 아예 하나도 안 쓰는 걸 뜻하는 걸까?",
        "expected_answer": "아니요! 배출을 최대한 줄이고, 어쩔 수 없이 나오는 탄소는 숲을 가꾸거나 신기술로 흡수해서 뺀 값이 0이 되게 만드는 거래요!",
        "coaching_tip": "환경 보호와 산업 발전이 양립할 수 있는 탄소중립의 지혜를 함께 이야기해 보세요."
    }
)

# 4. G6-EXP-V1-4
slots_v1["V1-4"] = build_expository_slot(
    grade_num=6,
    subskill_code="V1-4",
    subject="사회(정치 발전·헌법 6-1)",
    unit="1. 우리나라의 정치 발전",
    concept="민주주의의 핵심 원리인 ‘권력분립(삼권분립)’: 국회·정부·법원의 기능과 견제·균형",
    text_structure="분석·분류 + 인과(견제와 균형)",
    structure_type_code="classification",
    passage_title="권력의 집중을 막는 민주주의의 지혜: 삼권분립의 원리와 상호 견제",
    paragraphs=[
        "과거 절대군주제 시절에는 한 사람의 왕이 법을 만들고, 집행하고, 재판까지 독점하여 백성들의 자유와 인권을 쉽게 짓밟았습니다. 민주주의는 이러한 독재와 권력 남용을 방지하기 위하여 국가의 통치 권력을 셋으로 나누어 서로 다른 기관에 맡겼는데, 이를 '삼권분립(권력분립)'이라고 부릅니다.",
        "삼권분립에 따라 국가 권력은 '입법부(국회)', '행정부(정부)', '사법부(법원)'로 분립됩니다. 첫째, 국민이 직접 뽑은 국회의원으로 구성된 '국회'는 국민의 뜻을 반영하여 법률을 제정·개정하는 입법권을 가집니다. 둘째, 대통령과 국무총리를 중심으로 한 '정부'는 국회가 만든 법을 바탕으로 국가 살림을 운영하고 정책을 펴는 행정권을 행사합니다. 셋째, 판사들로 구성된 '법원'은 법을 해석하고 적용하여 분쟁을 공정하게 판결하는 사법권을 담당합니다.",
        "이 세 기관은 단순히 나뉘어 있는 것에 그치지 않고, 서로를 끊임없이 '견제와 균형'의 원리로 감시합니다. 예를 들어 국회는 정부의 살림살이를 감시하는 '국정감사권'과 정부가 제출한 예산안을 심의·확정하는 권한으로 정부를 견제합니다. 반면 정부의 대통령은 국회가 통과시킨 법안이 부당할 때 이를 거부할 수 있는 '법률안 거부권'으로 국회를 견제합니다. 또한 법원은 국회가 만든 법이 헌법에 위배되는지 헌법재판소에 제청할 수 있고, 정부의 행정명령이 위법한지 심사하여 두 기관을 견제합니다.",
        "결국 삼권분립의 진정한 목적은 권력 기관 간의 우열을 가리는 것이 아니라, 상호 대등한 위치에서 서로를 견제하게 함으로써 어떠한 권력도 국민 위에 군림하지 못하게 하고 '국민의 기본권'을 최후까지 수호하는 데 있습니다."
    ],
    vocab_notes=[
        {"word": "삼권분립", "definition": "국가의 통치 권력을 입법, 행정, 사법의 셋으로 나누어 각각 독립된 기관에 맡기는 통치 원리"},
        {"word": "국정감사", "definition": "국회가 정부의 국정 운영 전반을 조사하고 감사하여 위법이나 부당한 점을 밝혀내는 일"}
    ],
    visual_html="""<div class="p-3 bg-indigo-50 rounded border border-indigo-200">
      <h4 class="font-bold text-indigo-900 mb-2">🏛️ 대한민국 삼권분립 상호 견제와 균형 메커니즘</h4>
      <div class="grid grid-cols-3 gap-2 text-xs text-center">
        <div class="p-2 bg-white rounded border border-indigo-200">
          <strong class="text-indigo-800">국회 (입법부)</strong>
          <p class="mt-1 text-gray-700">법률 제정, 예산 심의<br><span class="text-xs text-indigo-600">➔ 정부 견제 (국정감사)</span></p>
        </div>
        <div class="p-2 bg-white rounded border border-indigo-200">
          <strong class="text-indigo-800">정부 (행정부)</strong>
          <p class="mt-1 text-gray-700">법 집행, 국가 살림<br><span class="text-xs text-indigo-600">➔ 국회 견제 (법률안 거부권)</span></p>
        </div>
        <div class="p-2 bg-white rounded border border-indigo-200">
          <strong class="text-indigo-800">법원 (사법부)</strong>
          <p class="mt-1 text-gray-700">법 적용, 공정 재판<br><span class="text-xs text-indigo-600">➔ 행정·입법 위법 심사</span></p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v14-c1", "text": "국가의 통치 권력을 셋으로 나누어 서로 다른 기관에 맡겼는데, 이를 '삼권분립(권력분립)'이라고 부릅니다", "role": "삼권분립의 본질적 정의", "para_idx": 0},
        {"cue_id": "g6-v14-c2", "text": "서로를 견제하게 함으로써 어떠한 권력도 국민 위에 군림하지 못하게 하고 '국민의 기본권'을 최후까지 수호하는 데 있습니다", "role": "삼권분립의 궁극적 목적", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "상호 견제 삼각형 다이어그램",
        "organs": {
            "국회": "입법권 (정부에 대해 국정감사·예산심의)",
            "정부": "행정권 (국회에 대해 법률안 거부권)",
            "법원": "사법권 (정부 명령 심사 및 헌법재판 제청)"
        },
        "core_purpose": "권력 독점 방지 및 국민의 기본권 수호"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "제도적 기능 및 기관 매핑 확인",
            "stem": "위 글의 2문단과 3문단을 바탕으로 할 때, 각 기관의 권한과 견제 수단이 바르게 연결된 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "정부의 대통령은 국회가 통과시킨 법안이 부당할 때 이를 거부할 수 있는 '법률안 거부권'으로 국회를 견제합니다.",
            "options": [
                {"label": "①", "text": "정부(대통령)는 국회가 만든 부당한 법안에 대해 '법률안 거부권'을 행사하여 국회를 견제할 수 있다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 명시된 정부의 국회 견제 수단입니다."},
                {"label": "②", "text": "법원은 국회의 국정감사를 무효로 선언하고 모든 국회의원을 해산한다.", "is_correct": False, "formula": "D5", "explanation": "법원에는 국회의원 해산 권한이 없습니다."},
                {"label": "③", "text": "국회는 법원의 판결이 마음에 들지 않으면 판사를 즉각 파면한다.", "is_correct": False, "formula": "D3", "explanation": "사법권의 독립성에 위배되는 왜곡입니다."},
                {"label": "④", "text": "대통령은 법원의 재판정에 직접 들어가 판결문을 대신 작성한다.", "is_correct": False, "formula": "D1", "explanation": "삼권분립 원칙상 절대 허용되지 않습니다."},
                {"label": "⑤", "text": "삼권분립 체제에서는 국회가 왕처럼 절대적인 최고 권력을 행사한다.", "is_correct": False, "formula": "D2", "explanation": "세 기관은 대등하게 상호 견제합니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "제도의 궁극적 의도 추론",
            "stem": "글쓴이가 4문단에서 강조한 삼권분립의 가장 근본적인 존재 목적은 무엇인가요?",
            "target_para_idx": 3,
            "spotlight_quote": "결국 삼권분립의 진정한 목적은 권력 기관 간의 우열을 가리는 것이 아니라, 상호 대등한 위치에서 서로를 견제하게 함으로써 어떠한 권력도 국민 위에 군림하지 못하게 하고 '국민의 기본권'을 최후까지 수호하는 데 있습니다.",
            "options": [
                {"label": "①", "text": "어느 한 기관의 권력 독점을 막고 상호 견제함으로써 국민의 자유와 기본권을 지키기 위해", "is_correct": True, "formula": "정답", "explanation": "4문단의 결론에 명확히 제시되어 있습니다."},
                {"label": "②", "text": "세 기관 중 가장 힘센 기관을 골라 대통령 독재를 완성하기 위해", "is_correct": False, "formula": "D5", "explanation": "삼권분립의 목적과 정반대입니다."},
                {"label": "③", "text": "국가 예산을 아끼기 위해 공무원 수를 강제로 줄이기 위해", "is_correct": False, "formula": "D4", "explanation": "예산 감축 목적이 아닙니다."},
                {"label": "④", "text": "과거 군주제처럼 한 사람의 왕에게 절대권력을 돌려주기 위해", "is_correct": False, "formula": "D1", "explanation": "독재로 돌아가는 것이 아닙니다."},
                {"label": "⑤", "text": "법을 만들지 않고 국민들이 각자 마음대로 살게 하기 위해", "is_correct": False, "formula": "D6", "explanation": "무정부 상태를 뜻하지 않습니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 삼권분립을 이루는 세 기관과 주요 기능의 연결로 옳지 않은 것은?",
            "options": [
                {"label": "①", "text": "사법부(법원) — 국가 행정 집행 및 정책 수립", "is_correct": True},
                {"label": "②", "text": "입법부(국회) — 국민의 뜻을 반영한 법률 제정", "is_correct": False},
                {"label": "③", "text": "행정부(정부) — 법에 따른 국가 살림 운영", "is_correct": False},
                {"label": "④", "text": "사법부(법원) — 법을 해석하고 적용하는 재판", "is_correct": False},
                {"label": "⑤", "text": "입법부(국회) — 정부 예산안 심의 및 국정감사", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "판사들로 구성된 '법원'은 법을 해석하고 적용하여 분쟁을 공정하게 판결하는 사법권을 담당합니다.", "is_correct": True},
                {"label": "②", "text": "과거 절대군주제 시절에는 한 사람의 왕이 법을 만들고,", "is_correct": False},
                {"label": "③", "text": "국민이 직접 뽑은 국회의원으로 구성된 '국회'는 국민의 뜻을", "is_correct": False},
                {"label": "④", "text": "대통령과 국무총리를 중심으로 한 '정부'는 국회가 만든 법을", "is_correct": False},
                {"label": "⑤", "text": "이 세 기관은 단순히 나뉘어 있는 것에 그치지 않고,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "삼권분립 원리 요약문 작성",
        "guide": "국가 권력의 분립 기관과 견제·균형의 목적을 1문장의 완성된 복문으로 작성하세요.",
        "template": "국가 권력을 국회, 정부, 법원으로 분립하여 상호 [견제와 균형]을 이루게 하는 까닭은 권력 독점을 막고 [국민의 기본권]을 보호하기 위함이다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "삼권분립 구조에서는 '기관 명칭-역할(법 제정/집행/적용)-견제 수단'의 3박자를 파악해요."},
        "step1_2_drill": {"task": "국회(국정감사), 정부(법률안 거부권), 법원(위법 심사) 화살표 연결하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "삼권분립의 궁극적 목적은 어느 한 권력의 독점을 막고 국민의 기본권을 지키는 것이다.", "answer": "O", "reason": "본문에 나온 핵심 주제입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 법 만드는 사람과 벌 주는 사람이 왜 다를까?",
        "situation": "선거철이나 뉴스에서 국회와 법원 이야기가 나올 때",
        "parent_question": "만약 한 사람이 법도 만들고, 경찰도 지휘하고, 재판까지 다 하면 어떻게 될까?",
        "expected_answer": "자기 마음대로 억지 법을 만들고 사람들을 가둘 수 있어서 독재가 된대요! 그래서 세 군데로 나눠서 감시하게 만든 거예요.",
        "coaching_tip": "민주주의 권력 분립의 중요성을 학교 학급 회의나 가족 규칙 정하기에 빗대어 설명해 주세요."
    }
)
