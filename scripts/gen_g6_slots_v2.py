# -*- coding: utf-8 -*-
"""
Grade 6 Item Bank - Part 2: V2-1, V2-2, V2-3, V2-4 (Expository slots)
5-Option Standard (expected_opt_len = 5)
"""

from item_bank_schema_helper import build_expository_slot

slots_v2 = {}

# 5. G6-EXP-V2-1
slots_v2["V2-1"] = build_expository_slot(
    grade_num=6,
    subskill_code="V2-1",
    subject="과학(인체·생물 6-1)",
    unit="4. 우리 몸의 구조와 기능",
    concept="우리 몸의 ‘항상성(恒常性)’ 유지 메커니즘과 세균·바이러스에 대한 ‘면역·비특이적 방어’",
    text_structure="비교·대조 + 과정·인과",
    structure_type_code="comparison",
    passage_title="생명의 정밀 조절기 '항상성'과 질병을 막는 다층 '면역 방어선'",
    paragraphs=[
        "인간의 신체는 외부 환경이 한파나 폭염으로 극심하게 요동치더라도 체온, 혈당량, 삼투압(수분량)을 일정한 범위로 유지하는 능력을 지니고 있습니다. 이를 한자어로 '항상성(恒常性)'이라고 부르는데, 늘(恒) 변함없는(常) 상태의 성질(性)을 뜻합니다. 만약 체온이 42도를 넘거나 32도 이하로 떨어지면 체내 효소가 파괴되어 생명이 위태로워지므로, 항상성은 생명 유지의 절대적 전제 조건입니다.",
        "우리 몸이 병원체(세균과 바이러스)의 침입에 맞서 항상성을 지키는 방어 작용을 '면역(免疫)'이라고 합니다. 면역 체계는 크게 '비특이적 방어(선천 면역)'와 '특이적 방어(후천 면역)'의 두 단계로 구분됩니다. 비특이적 방어는 병원체의 종류를 가리지 않고 즉각 작동하는 1차 방어선입니다. 피부와 점막이 물리적 장벽을 형성하여 침입을 막고, 침이나 눈물 속의 라이소자임 효소가 세균의 세포벽을 분해합니다. 만약 피부가 뚫려 병원체가 침입하면 백혈구가 출동하여 식균 작용을 벌입니다.",
        "반면 특이적 방어는 병원체의 독특한 표면 물질(항원)을 정밀하게 인식하여 공격하는 고도화된 2차 방어선입니다. 림프구가 침입한 항원에 딱 들어맞는 맞춤형 무기인 '항체'를 생성하여 무력화합니다. 이 과정에서 면역계는 해당 항원의 특징을 기억하는 '기억 세포'를 만들어 내는데, 이는 백신의 기본 원리가 됩니다.",
        "백신은 인체에 해가 없도록 약화하거나 죽인 병원체(항원)를 미리 주입하여 기억 세포를 형성하게 만드는 의학 기술입니다. 훗날 진짜 병원체가 침입했을 때 기억 세포가 즉각 다량의 항체를 쏟아내어 질병에 걸리지 않도록 항상성을 완벽히 수호합니다."
    ],
    vocab_notes=[
        {"word": "항상성", "definition": "외부 환경의 변화에도 불구하고 체온, 삼투압 등 체내 상태를 일정하게 유지하려는 성질"},
        {"word": "비특이적 방어", "definition": "병원체의 종류를 구별하지 않고 침입을 물리적·화학적으로 즉각 차단하는 선천적 면역 반응"}
    ],
    visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
      <h4 class="font-bold text-teal-900 mb-2">🛡️ 인체 2단계 면역 방어 체계 비교</h4>
      <table class="w-full text-xs text-left border-collapse bg-white">
        <thead>
          <tr class="bg-teal-100 text-teal-900 border-b">
            <th class="p-1.5 border">구분</th><th class="p-1.5 border">1차 비특이적 방어 (선천)</th><th class="p-1.5 border">2차 특이적 방어 (후천)</th>
          </tr>
        </thead>
        <tbody>
          <tr><td class="p-1.5 border font-semibold">특징</td><td class="p-1.5 border">병원체 종류 불문 즉각 작용</td><td class="p-1.5 border">특정 항원 정밀 식별·맞춤 공격</td></tr>
          <tr><td class="p-1.5 border font-semibold">핵심 요소</td><td class="p-1.5 border">피부 장벽, 점막, 침, 백혈구 식균</td><td class="p-1.5 border">림프구, 항체 생성, 기억 세포</td></tr>
          <tr><td class="p-1.5 border font-semibold">의학 응용</td><td class="p-1.5 border">소독 및 상처 보호 밴드</td><td class="p-1.5 border">백신 예방 접종</td></tr>
        </tbody>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v21-c1", "text": "외부 환경이 한파나 폭염으로 극심하게 요동치더라도 체온, 혈당량, 삼투압(수분량)을 일정한 범위로 유지하는 능력을 지니고 있습니다", "role": "항상성 개념 정의", "para_idx": 0},
        {"cue_id": "g6-v21-c2", "text": "비특이적 방어는 병원체의 종류를 가리지 않고 즉각 작동하는 1차 방어선입니다", "role": "비특이적 방어의 특징", "para_idx": 1}
    ],
    graphic_organizer={
        "type": "2단계 면역 방어 구조도",
        "homeostasis": "항상성 (체온·혈당·수분 일정 유지)",
        "immunity": {
            "1차 비특이적": ["피부·점막 장벽", "라이소자임 효소", "백혈구 식균 작용"],
            "2차 특이적": ["항원 인식", "항체 생성 (림프구)", "기억 세포 형성 (백신 원리)"]
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "어휘 형태소 및 개념 분석",
            "stem": "1문단의 '항상성(恒常性)'의 한자 형태소와 2~3문단의 면역 개념에 대한 설명으로 가장 바른 것은?",
            "target_para_idx": 0,
            "spotlight_quote": "이를 한자어로 '항상성(恒常性)'이라고 부르는데, 늘(恒) 변함없는(常) 상태의 성질(性)을 뜻합니다.",
            "options": [
                {"label": "①", "text": "'항상성'은 늘(恒) 변함없이(常) 일정한 상태를 유지하려는 성질(性)로 인체 생존의 기초이다.", "is_correct": True, "formula": "정답", "explanation": "1문단의 한자 풀이 및 개념 정의와 정확히 일치합니다."},
                {"label": "②", "text": "'항상성'은 기온에 따라 몸 상태가 매 시간 급변해야 한다는 뜻이다.", "is_correct": False, "formula": "D3", "explanation": "일정하게 유지한다는 의미와 정반대입니다."},
                {"label": "③", "text": "비특이적 방어는 병원체의 종류를 몇 달 동안 분석한 뒤에만 작동한다.", "is_correct": False, "formula": "D2", "explanation": "종류를 가리지 않고 즉각 작동하는 1차 방어선입니다."},
                {"label": "④", "text": "피부와 점막은 병원체가 자유롭게 드나들도록 돕는 통로이다.", "is_correct": False, "formula": "D5", "explanation": "병원체의 침입을 막는 물리적 장벽입니다."},
                {"label": "⑤", "text": "항체는 모든 병원체를 구별 없이 똑같은 방식으로 분해한다.", "is_correct": False, "formula": "D4", "explanation": "항원에 딱 들어맞는 맞춤형 무기입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "원리 적용 및 인과 추론",
            "stem": "4문단에 나타난 백신의 작동 원리를 바탕으로 할 때, 예방 접종을 맞는 과학적 까닭은?",
            "target_para_idx": 3,
            "spotlight_quote": "백신은 인체에 해가 없도록 약화하거나 죽인 병원체(항원)를 미리 주입하여 기억 세포를 형성하게 만드는 의학 기술입니다.",
            "options": [
                {"label": "①", "text": "무해한 항원을 미리 주입하여 기억 세포를 만듦으로써 향후 진짜 병원체 침입 시 신속히 항체를 만들기 위해", "is_correct": True, "formula": "정답", "explanation": "4문단의 백신 작동 메커니즘을 온전히 설명하고 있습니다."},
                {"label": "②", "text": "몸속의 모든 면역 세포를 파괴하여 체온을 영하로 낮추기 위해", "is_correct": False, "formula": "D5", "explanation": "생명을 위협하는 왜곡입니다."},
                {"label": "③", "text": "피부를 영구히 돌처럼 단단하게 굳히기 위해", "is_correct": False, "formula": "D6", "explanation": "본문과 무관한 허구입니다."},
                {"label": "④", "text": "병원체가 평생 동안 몸속에서 마음대로 증식하도록 돕기 위해", "is_correct": False, "formula": "D1", "explanation": "질병 예방 목적에 정면 배치됩니다."},
                {"label": "⑤", "text": "비특이적 방어선인 피부의 땀구멍을 완전히 밀폐하기 위해", "is_correct": False, "formula": "D3", "explanation": "백신은 특이적 방어(기억 세포)의 원리입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 다음 중 '특이적 방어(후천 면역)'에만 해당하는 핵심 요소를 고른 것은?",
            "options": [
                {"label": "①", "text": "항체 생성 및 기억 세포 형성", "is_correct": True},
                {"label": "②", "text": "피부의 물리적 장벽 형성", "is_correct": False},
                {"label": "③", "text": "눈물 속 라이소자임 효소 분비", "is_correct": False},
                {"label": "④", "text": "백혈구의 무차별 식균 작용", "is_correct": False},
                {"label": "⑤", "text": "기관지 점막의 이물질 배출", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "림프구가 침입한 항원에 딱 들어맞는 맞춤형 무기인 '항체'를 생성하여 무력화합니다. 이 과정에서 면역계는 해당 항원의 특징을 기억하는 '기억 세포'를 만들어 내는데,", "is_correct": True},
                {"label": "②", "text": "인간의 신체는 외부 환경이 한파나 폭염으로 극심하게 요동치더라도", "is_correct": False},
                {"label": "③", "text": "비특이적 방어는 병원체의 종류를 가리지 않고 즉각 작동하는", "is_correct": False},
                {"label": "④", "text": "피부와 점막이 물리적 장벽을 형성하여 침입을 막고,", "is_correct": False},
                {"label": "⑤", "text": "체온이 42도를 넘거나 32도 이하로 떨어지면 체내 효소가 파괴되어", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "항상성과 면역 과학 설명문 작성",
        "guide": "항상성의 개념과 백신의 기억 세포 원리를 연결하여 1문장의 요약문으로 작성하세요.",
        "template": "우리 몸은 체내 환경을 일정하게 유지하는 [항상성]을 지니며, 백신을 통해 형성된 [기억 세포]는 병원체 침입 시 신속히 항체를 분비하여 몸을 방어한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "면역의 2단계(1차 비특이적 vs 2차 특이적) 차이점을 표로 정리해요."},
        "step1_2_drill": {"task": "피부·눈물(비특이적)과 항체·백신(특이적) 분류하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "백신은 기억 세포를 형성하여 훗날 침입할 병원체에 빠르게 대항하게 한다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 아프지도 않은데 왜 백신 주사를 맞을까?",
        "situation": "예방 주사를 맞으러 병원에 갈 때 아이와 나눌 이야기",
        "parent_question": "지금 아프지도 않은데 왜 따끔한 예방 주사를 미리 맞아야 할까?",
        "expected_answer": "몸속 면역 세포들에게 병원체 몽타주를 미리 보여주어 '기억 세포' 훈련을 시켜놓는 거래요!",
        "coaching_tip": "백신이 인체의 자가 치유 및 방어 능력을 길러주는 과학적 훈련임을 안심시켜 주세요."
    }
)

# 6. G6-EXP-V2-2
slots_v2["V2-2"] = build_expository_slot(
    grade_num=6,
    subskill_code="V2-2",
    subject="과학(전기의 이용·기체 6-1/6-2)",
    unit="4. 기체의 성질",
    concept="기체의 온도와 압력에 따른 부피 변화 원리와 열기구·잠수함의 부력 조절 메커니즘",
    text_structure="인과·과정 + 원리 적용",
    structure_type_code="causal",
    passage_title="기체 입자의 춤: 온도·압력에 따른 부피 변화와 거대 비행·잠수 원리",
    paragraphs=[
        "기체는 눈에 보이지 않는 수많은 미세한 입자들로 이루어져 있으며, 이 입자들은 끊임없이 모든 방향으로 자유롭게 운동하고 있습니다. 기체의 부피는 고정되어 있지 않고 외부의 '온도'와 '압력'이라는 두 가지 변인에 따라 극적으로 변화합니다.",
        "먼저 온도와 기체 부피의 관계(샤를 법칙)를 살펴보면, 압력이 일정할 때 온도가 높아지면 기체 입자들의 운동이 활발해져 서로 밀어내는 거리가 멀어집니다. 그 결과 기체의 부피가 팽창하고 밀도는 작아집니다. 열기구는 바로 이 원리를 이용합니다. 버너로 열기구 내부의 공기를 가열하면 공기 부피가 팽창하여 바깥 찬 공기보다 가벼워지므로(밀도 감소), 위로 떠오르는 힘인 '부력'이 중력보다 커져 하늘로 솟아오릅니다.",
        "반대로 압력과 기체 부피의 관계(보일 법칙)를 보면, 온도가 일정할 때 외부에서 가해지는 압력이 커지면 기체 입자 사이의 빈 공간이 좁아져 부피가 줄어듭니다. 바닷속을 운항하는 잠수함은 압축 공기와 물을 저장하는 탱크인 '밸러스트 탱크'를 조절하여 부력을 다룹니다. 잠수함이 잠수할 때는 탱크에 바닷물을 채워 무게를 늘리고, 떠오를 때는 고압으로 압축해 둔 공기를 탱크에 밀어 넣어 바닷물을 배출함으로써 부력을 회복합니다.",
        "이처럼 열기구와 잠수함은 인간이 눈에 보이지 않는 기체 입자의 열역학적 성질과 유체의 부력 원리를 정밀하게 공학적으로 응용한 대표적인 과학적 성취입니다."
    ],
    vocab_notes=[
        {"word": "부력", "definition": "물이나 공기 같은 유체 속에 잠긴 물체를 위쪽으로 밀어 올리는 힘"},
        {"word": "밀도", "definition": "물질의 질량을 부피로 나눈 값으로, 물질의 빽빽한 정도를 나타내는 물리량"}
    ],
    visual_html="""<div class="p-3 bg-cyan-50 rounded border border-cyan-200">
      <h4 class="font-bold text-cyan-900 mb-2">🎈 열기구 vs 잠수함 부력 조절 메커니즘 비교</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-cyan-100">
          <strong class="text-red-700">열기구 (온도 ➔ 부피·밀도 조절)</strong>
          <p class="mt-1 text-gray-700">공기 가열 ➔ 입자 운동 활발 ➔ 부피 팽창 ➔ 공기 밀도 감소 (주변 공기보다 가벼움) ➔ <strong>상승</strong></p>
        </div>
        <div class="p-2 bg-white rounded border border-cyan-100">
          <strong class="text-blue-700">잠수함 (압축 공기 ➔ 바닷물 조절)</strong>
          <p class="mt-1 text-gray-700">압축 공기로 밸러스트 탱크의 해수 배출 ➔ 전체 무게 감소 ➔ <strong>부력 회복하여 부상</strong></p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v22-c1", "text": "온도가 높아지면 기체 입자들의 운동이 활발해져 서로 밀어내는 거리가 멀어집니다", "role": "샤를 법칙의 입자 운동 원리", "para_idx": 1},
        {"cue_id": "g6-v22-c2", "text": "고압으로 압축해 둔 공기를 탱크에 밀어 넣어 바닷물을 배출함으로써 부력을 회복합니다", "role": "잠수함의 압축 공기 활용 원리", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "기체 성질의 기술 응용 매트릭스",
        "variables": {
            "온도 상승 (가열)": "기체 입자 운동 활발 ➔ 부피 팽창 ➔ 밀도 감소 ➔ 열기구 상승",
            "압력 증가 (압축)": "기체 입자 거리 감소 ➔ 부피 수축 ➔ 잠수함 탱크 압축 공기 저장"
        },
        "principle": "유체의 부력 조절을 통한 비행 및 잠수"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "원인과 결과 입자 운동 추론",
            "stem": "2문단을 바탕으로 할 때, 열기구가 하늘 위로 떠오르는 과정을 바르게 나열한 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "버너로 열기구 내부의 공기를 가열하면 공기 부피가 팽창하여 바깥 찬 공기보다 가벼워지므로(밀도 감소), 위로 떠오르는 힘인 '부력'이 중력보다 커져 하늘로 솟아오릅니다.",
            "options": [
                {"label": "①", "text": "공기 가열 ➔ 기체 부피 팽창 ➔ 밀도 감소 ➔ 부력이 중력보다 커짐 ➔ 상승", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 인과 과정과 정확히 일치합니다."},
                {"label": "②", "text": "공기 냉각 ➔ 기체 수축 ➔ 무거워짐 ➔ 아래로 추락", "is_correct": False, "formula": "D3", "explanation": "가열하여 상승하는 원리와 반대입니다."},
                {"label": "③", "text": "열기구 표면에 모래를 얹음 ➔ 중력 극대화 ➔ 수직 상승", "is_correct": False, "formula": "D5", "explanation": "중력이 커지면 하강합니다."},
                {"label": "④", "text": "열기구 안의 공기를 모두 빼서 진공 상태로 만듦 ➔ 무게 증가", "is_correct": False, "formula": "D4", "explanation": "공기를 가열하는 것입니다."},
                {"label": "⑤", "text": "바깥 공기의 온도를 버너로 전부 가열 ➔ 열기구 압축", "is_correct": False, "formula": "D2", "explanation": "열기구 내부 공기를 가열합니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "응용 기술 및 조건 변화 추론",
            "stem": "3문단을 바탕으로 할 때, 잠수함이 바닷속 깊이 잠수하고자 할 때 취해야 할 조치는?",
            "target_para_idx": 2,
            "spotlight_quote": "잠수함이 잠수할 때는 탱크에 바닷물을 채워 무게를 늘리고, 떠오를 때는 고압으로 압축해 둔 공기를 탱크에 밀어 넣어 바닷물을 배출함으로써 부력을 회복합니다.",
            "options": [
                {"label": "①", "text": "밸러스트 탱크에 바닷물을 채워 잠수함 전체의 무게를 늘린다.", "is_correct": True, "formula": "정답", "explanation": "3문단에서 잠수할 때는 바닷물을 채워 무게를 늘린다고 명시했습니다."},
                {"label": "②", "text": "탱크의 바닷물을 모두 빼내어 부력을 극대화한다.", "is_correct": False, "formula": "D1", "explanation": "바닷물을 빼면 떠오르게 됩니다."},
                {"label": "③", "text": "잠수함 표면의 철판을 모두 떼어내어 가볍게 만든다.", "is_correct": False, "formula": "D6", "explanation": "본문과 무관한 위험한 오답입니다."},
                {"label": "④", "text": "엔진을 끄고 바닷물을 얼려 얼음 덩어리로 만든다.", "is_correct": False, "formula": "D5", "explanation": "기체의 압축 및 해수 주입 원리와 다릅니다."},
                {"label": "⑤", "text": "공기 탱크에 뜨거운 열기를 불어넣어 부피를 100배 키운다.", "is_correct": False, "formula": "D2", "explanation": "잠수함은 고압 압축 공기와 해수 출납으로 조절합니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 기체 입자의 운동과 온도·압력의 관계에 대한 설명으로 옳은 것은?",
            "options": [
                {"label": "①", "text": "온도가 올라가면 기체 입자 운동이 활발해져 부피가 팽창한다.", "is_correct": True},
                {"label": "②", "text": "압력이 높아지면 기체 입자 거리가 멀어져 부피가 팽창한다.", "is_correct": False},
                {"label": "③", "text": "온도가 내려가면 기체 입자가 사라져 무게가 0이 된다.", "is_correct": False},
                {"label": "④", "text": "기체는 어떤 조건에서도 부피가 절대 변하지 않는다.", "is_correct": False},
                {"label": "⑤", "text": "압력이 낮아지면 기체 입자들이 뭉쳐서 고체로 굳어진다.", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "온도가 높아지면 기체 입자들의 운동이 활발해져 서로 밀어내는 거리가 멀어집니다. 그 결과 기체의 부피가 팽창하고 밀도는 작아집니다.", "is_correct": True},
                {"label": "②", "text": "기체는 눈에 보이지 않는 수많은 미세한 입자들로 이루어져 있으며,", "is_correct": False},
                {"label": "③", "text": "바닷속을 운항하는 잠수함은 압축 공기와 물을 저장하는", "is_correct": False},
                {"label": "④", "text": "이처럼 열기구와 잠수함은 인간이 눈에 보이지 않는", "is_correct": False},
                {"label": "⑤", "text": "기체의 부피는 고정되어 있지 않고 외부의 '온도'와 '압력'", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "기체 열역학과 부력 원리 요약",
        "guide": "온도에 따른 기체 부피 팽창과 열기구의 부력 원리를 1문장으로 요약하세요.",
        "template": "공기를 가열하면 입자 운동이 활발해져 부피가 팽창하고 [밀도]가 감소하므로, [부력]이 중력보다 커져 열기구가 하늘로 떠오른다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "온도 증가 ➔ 부피 증가(샤를), 압력 증가 ➔ 부피 감소(보일) 규칙을 암기해요."},
        "step1_2_drill": {"task": "열기구(온도 조절)와 잠수함(압축 공기/해수 조절) 작동 원리 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "열기구는 내부 공기를 데워 밀도를 주변보다 낮춤으로써 떠오른다.", "answer": "O", "reason": "샤를 법칙과 부력 원리에 부합합니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 거대한 쇠뭉치 잠수함이 물 위로 뜨는 비결",
        "situation": "잠수함 다큐멘터리나 그림책을 함께 볼 때",
        "parent_question": "쇠로 만든 무거운 잠수함이 어떻게 깊은 바닷속에 들어갔다 다시 수면 위로 뜰 수 있을까?",
        "expected_answer": "탱크 안에 압축 공기를 쏴서 바닷물을 밖으로 쫓아내면 가벼워져서 물 위로 둥둥 뜨는 거래요!",
        "coaching_tip": "공기의 힘이 무거운 쇠를 띄울 만큼 강력함을 재미있게 대화해 보세요."
    }
)

# 7. G6-EXP-V2-3
slots_v2["V2-3"] = build_expository_slot(
    grade_num=6,
    subskill_code="V2-3",
    subject="과학(전기의 이용·에너지 6-2)",
    unit="1. 전기의 이용",
    concept="전구의 직렬·병렬연결 원리와 에너지 전환 효율 인포그래픽 통합 분석",
    text_structure="비교·대조 + 과정(에너지 전환)",
    structure_type_code="comparison",
    passage_title="회로 연결의 비밀과 스마트한 빛: 직렬·병렬연결과 에너지 전환 효율",
    paragraphs=[
        "전기 회로에서 전구를 연결하는 방식은 크게 '직렬연결'과 '병렬연결'로 나뉩니다. 직렬연결은 전구 여러 개를 한 줄로 이어 연결하는 방식입니다. 이 방식은 회로가 단순하지만, 전구의 수가 늘어날수록 전체 전기 저항이 커져 각 전구의 밝기가 어두워집니다. 또한 전구 하나가 끊어지면 회로 전체에 전류가 흐르지 않아 모든 전구가 꺼지는 치명적인 단점이 있습니다.",
        "반면 병렬연결은 전선이 여러 갈래로 갈라져 전구를 각각 연결하는 방식입니다. 병렬연결에서는 전구를 여러 개 추가하더라도 각 전구에 걸리는 전압이 유지되므로 전구의 밝기가 변함없이 밝습니다. 게다가 한 전구가 고장 나더라도 다른 갈래 전선의 전류는 정상적으로 흐르므로 나머지 전구는 그대로 켜져 있습니다. 이러한 이유로 우리가 사는 가정집의 콘센트와 방 조명은 모두 병렬연결 방식을 채택하고 있습니다.",
        "한편 조명 기구의 진화는 '에너지 전환 효율'의 역사이기도 합니다. 전구는 공급받은 전기 에너지를 '빛에너지'와 '열에너지'로 변환합니다. 과거의 백열등은 투입된 전력의 겨우 5%만 빛으로 바꾸고 나머지 95%를 쓸모없는 열로 낭비했습니다. 이에 비해 발광 다이오드(LED)는 투입된 전력의 40~50% 이상을 유효한 빛으로 전환하여 백열등보다 약 8배 이상의 높은 에너지 효율을 자랑합니다.",
        "가정에서 병렬 회로 시스템을 기반으로 LED 조명을 사용할 경우, 개별 제어의 편리함은 물론 국가적인 전력 낭비를 획기적으로 줄일 수 있습니다."
    ],
    vocab_notes=[
        {"word": "병렬연결", "definition": "전기 회로에서 두 개 이상의 부품이 각각 다른 갈래의 도선에 연결된 방식"},
        {"word": "에너지 전환 효율", "definition": "공급된 총에너지 중 우리가 목적으로 하는 유용한 에너지 형태로 전환된 비율"}
    ],
    visual_html="""<div class="p-3 bg-yellow-50 rounded border border-yellow-200">
      <h4 class="font-bold text-yellow-900 mb-2">💡 직렬 vs 병렬 회로 및 조명별 에너지 효율 비교</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-yellow-100">
          <strong class="text-gray-800">회로 연결 방식 비교</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>직렬:</strong> 전구 추가 시 어두워짐, 1개 단선 시 전체 소등</li>
            <li><strong>병렬:</strong> 전구 추가해도 밝기 유지, 1개 고장 나도 정상 작동 (가정용 콘센트)</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-yellow-100">
          <strong class="text-gray-800">조명 기구별 빛 에너지 전환 비율</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>백열등: 빛 5% (열 손실 95%) ❌</li>
            <li>형광등: 빛 약 20% (열 손실 80%) ⚠️</li>
            <li><strong>LED 조명:</strong> 빛 45~50% (고효율 친환경) ✅</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v23-c1", "text": "한 전구가 고장 나더라도 다른 갈래 전선의 전류는 정상적으로 흐르므로 나머지 전구는 그대로 켜져 있습니다", "role": "병렬연결의 핵심 장점", "para_idx": 1},
        {"cue_id": "g6-v23-c2", "text": "발광 다이오드(LED)는 투입된 전력의 40~50% 이상을 유효한 빛으로 전환하여 백열등보다 약 8배 이상의 높은 에너지 효율을 자랑합니다", "role": "LED 조명의 고효율 수치", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "회로 및 조명 효율 비교 매트릭스",
        "circuit_types": {
            "직렬연결": "한 줄 연결 / 개수 늘면 어두워짐 / 하나 꺼지면 전체 소등",
            "병렬연결": "갈래 연결 / 밝기 유지 / 하나 꺼져도 유지 (가정용 적용)"
        },
        "energy_efficiency": {
            "백열등": "빛 5% (열 95% 낭비)",
            "LED": "빛 45~50% (백열등 대비 8배 고효율)"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "원리 비교 및 생활 적용 파악",
            "stem": "위 글의 1문단과 2문단을 바탕으로, 가정용 콘센트에 병렬연결 방식을 사용하는 까닭으로 가장 적절한 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "게다가 한 전구가 고장 나더라도 다른 갈래 전선의 전류는 정상적으로 흐르므로 나머지 전구는 그대로 켜져 있습니다.",
            "options": [
                {"label": "①", "text": "가전제품 하나가 꺼져도 다른 제품의 작동에 영향을 주지 않고 동일한 전압이 유지되기 때문에", "is_correct": True, "formula": "정답", "explanation": "2문단에서 병렬연결의 독립성과 밝기 유지 장점을 명시했습니다."},
                {"label": "②", "text": "가전제품을 켤 때마다 집안 전체 전기가 한꺼번에 꺼지게 만들기 위해", "is_correct": False, "formula": "D5", "explanation": "직렬연결의 단점과 관련된 정반대 진술입니다."},
                {"label": "③", "text": "전기 저항을 100배로 높여 집안을 난로처럼 덥히기 위해", "is_correct": False, "formula": "D4", "explanation": "에너지 낭비 목적이 아닙니다."},
                {"label": "④", "text": "전선을 오직 한 가닥만 써서 공사 비용을 0원으로 만들기 위해", "is_correct": False, "formula": "D2", "explanation": "병렬연결은 갈래 전선이 필요합니다."},
                {"label": "⑤", "text": "전구 밝기를 최대한 어둡게 만들어 잠을 잘 오게 하기 위해", "is_correct": False, "formula": "D6", "explanation": "본문과 무관한 자의적 추측입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "도표 연계 수치 및 에너지 효율 추론",
            "stem": "3문단과 시각자료를 연계할 때, 백열등을 LED 조명으로 교체했을 때 얻을 수 있는 효과는?",
            "target_para_idx": 2,
            "spotlight_quote": "발광 다이오드(LED)는 투입된 전력의 40~50% 이상을 유효한 빛으로 전환하여 백열등보다 약 8배 이상의 높은 에너지 효율을 자랑합니다.",
            "options": [
                {"label": "①", "text": "열로 낭비되는 전력을 대폭 줄이고 투입 전력의 약 절반을 유용한 빛으로 전환하여 전력을 절감한다.", "is_correct": True, "formula": "정답", "explanation": "3문단의 에너지 전환 효율 설명과 일치합니다."},
                {"label": "②", "text": "빛은 전혀 안 나오고 오직 100% 뜨거운 열기만 발생한다.", "is_correct": False, "formula": "D3", "explanation": "LED는 빛 효율이 40~50%로 매우 높습니다."},
                {"label": "③", "text": "백열등보다 전기를 10배 더 많이 소모하여 전기 요금이 급증한다.", "is_correct": False, "formula": "D1", "explanation": "에너지 고효율이므로 전력 소모가 적습니다."},
                {"label": "④", "text": "스위치를 켜는 즉시 회로 전체가 폭발하여 타버린다.", "is_correct": False, "formula": "D5", "explanation": "황당한 왜곡입니다."},
                {"label": "⑤", "text": "가정집의 병렬 회로를 강제로 직렬 회로로 변경해야만 한다.", "is_correct": False, "formula": "D4", "explanation": "기존 병렬 소켓에 그대로 체결하여 사용합니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 다음 중 직렬연결과 병렬연결의 차이점을 바르게 설명한 것은?",
            "options": [
                {"label": "①", "text": "직렬은 하나가 끊어지면 전체가 꺼지지만, 병렬은 다른 갈래가 유지된다.", "is_correct": True},
                {"label": "②", "text": "직렬은 전구를 더 달수록 밝아지고, 병렬은 어두워진다.", "is_correct": False},
                {"label": "③", "text": "병렬연결은 전선이 단 한 줄로만 이어져 있다.", "is_correct": False},
                {"label": "④", "text": "가정용 콘센트는 모두 직렬연결로 되어 있다.", "is_correct": False},
                {"label": "⑤", "text": "직렬연결은 각 전구에 걸리는 전압이 독립적으로 보장된다.", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "또한 전구 하나가 끊어지면 회로 전체에 전류가 흐르지 않아 모든 전구가 꺼지는 치명적인 단점이 있습니다.", "is_correct": True},
                {"label": "②", "text": "전기 회로에서 전구를 연결하는 방식은 크게 '직렬연결'과", "is_correct": False},
                {"label": "③", "text": "한편 조명 기구의 진화는 '에너지 전환 효율'의 역사이기도", "is_correct": False},
                {"label": "④", "text": "과거의 백열등은 투입된 전력의 겨우 5%만 빛으로 바꾸고", "is_correct": False},
                {"label": "⑤", "text": "가정에서 병렬 회로 시스템을 기반으로 LED 조명을 사용할 경우,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "회로 및 에너지 전환 설명문 완성",
        "guide": "병렬 회로의 편의성과 LED 조명의 에너지 절감 효과를 1문장으로 정리하세요.",
        "template": "가정에서는 독립적 작동이 가능한 [병렬연결] 회로에 에너지 효율이 높은 [LED 조명]을 사용함으로써 편리함과 전력 절감을 동시에 달성한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "회로 독해 시 '전류의 길(한 갈래 vs 여러 갈래)'을 머릿속에 그려보세요."},
        "step1_2_drill": {"task": "직렬(크리스마스 트리 옛날 전구) vs 병렬(집안 방 조명) 실생활 예시 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "LED 조명은 백열등보다 빛 에너지 전환 효율이 훨씬 높다.", "answer": "O", "reason": "백열등 5% 대비 LED 40~50%로 고효율입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 방 불을 꺼도 거실 TV가 계속 나오는 이유",
        "situation": "방에서 불을 끄고 거실로 나올 때 아이와 나눌 질문",
        "parent_question": "내 방 전등을 껐는데 왜 거실 TV나 냉장고는 안 꺼지고 계속 켜져 있을까?",
        "expected_answer": "집 안의 전선들이 '병렬연결'로 각각 갈라져 있어서, 하나를 꺼도 다른 기기에는 전기가 계속 흐르기 때문이래요!",
        "coaching_tip": "일상 속 집안 전기 설비에 숨겨진 과학 원리를 칭찬해 주세요."
    }
)

# 8. G6-EXP-V2-4
slots_v2["V2-4"] = build_expository_slot(
    grade_num=6,
    subskill_code="V2-4",
    subject="사회(경제 발전·무역 6-1)",
    unit="2. 우리나라의 경제 발전",
    concept="국제 분업과 자유무역협정(FTA)이 국가 경제에 미치는 영향",
    text_structure="인과 + 비교·대조",
    structure_type_code="comparison",
    passage_title="국경을 넘는 경제 협력: 국제 분업의 원리와 자유무역협정(FTA)의 명암",
    paragraphs=[
        "오늘날 세계 각국은 자신이 상대적으로 더 잘 만들 수 있는 제품 생산에 특화하고, 부족한 것은 다른 나라와 거래하는 '국제 분업'과 무역을 활발히 펼치고 있습니다. 각 나라마다 자연환경, 기술 수준, 노동력 등의 생산 조건이 다르기 때문에, 특화된 물품을 교역하면 모든 참여국이 경제적 이익을 얻을 수 있다는 '비교우위' 원리가 그 이론적 토대입니다.",
        "이러한 무역을 극대화하기 위해 국가 간에 상품 이동 시 부과하는 세금인 '관세'를 낮추거나 없애기로 약속하는 조약이 바로 '자유무역협정(FTA)'입니다. 자유무역협정이 체결되면 수출 기업은 상대국 시장에서 가격 경쟁력을 확보하여 수출을 크게 늘릴 수 있고, 소비자들은 질 좋은 외제 과일이나 공산품을 훨씬 저렴한 가격에 구매할 수 있다는 분명한 혜택이 있습니다.",
        "그러나 자유무역협정이 모든 산업에 축복인 것만은 아닙니다. 가격 경쟁력이 취약한 국내 산업, 특히 값싼 외국산 농축산물이 대량 유입될 경우 국내 농가와 축산업은 심각한 타격을 입게 됩니다. 농업 기반이 무너지면 국가의 식량 안보가 위협받을 수 있으며, 취약 계층의 일자리가 감소하는 양극화 문제가 발생하기도 합니다.",
        "따라서 성공적인 무역 강국이 되기 위해서는 FTA를 통해 반도체·자동차 등 첨단 수출 산업을 적극 육성하는 한편, 무역 이익의 일부를 취약 농어촌에 재투자하여 피해 산업의 경쟁력을 높이고 상생을 도모하는 균형 잡힌 정책적 보완이 반드시 병행되어야 합니다."
    ],
    vocab_notes=[
        {"word": "국제 분업", "definition": "각 나라가 비교우위에 있는 산업에 집중하고 서로 무역을 통해 교환하는 생산 방식"},
        {"word": "자유무역협정(FTA)", "definition": "협정을 맺은 국가 간에 관세 및 무역 장벽을 철폐하여 자유로운 상품 이동을 보장하는 특혜 무역 협정"}
    ],
    visual_html="""<div class="p-3 bg-violet-50 rounded border border-violet-200">
      <h4 class="font-bold text-violet-900 mb-2">🌐 자유무역협정(FTA)의 혜택 vs 극복 과제</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-green-200">
          <strong class="text-green-800">긍정적 효과 (수출 및 소비자)</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>관세 철폐로 첨단 제조업(반도체·차) 수출 경쟁력 강화</li>
            <li>소비자 후생 증가 (수입 소비재 가격 인하)</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-red-200">
          <strong class="text-red-800">극복 과제 (취약 산업 보호)</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>외국산 저가 농축산물 유입으로 국내 농가 피해</li>
            <li>식량 안보 약화 우려 ➔ 정부의 피해 보전 지원금 필요</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v24-c1", "text": "자유무역협정이 체결되면 수출 기업은 상대국 시장에서 가격 경쟁력을 확보하여 수출을 크게 늘릴 수 있고", "role": "FTA의 주요 기대 효과", "para_idx": 1},
        {"cue_id": "g6-v24-c2", "text": "무역 이익의 일부를 취약 농어촌에 재투자하여 피해 산업의 경쟁력을 높이고 상생을 도모하는 균형 잡힌 정책적 보완", "role": "국가의 상생 보완책", "para_idx": 3}
    ],
    graphic_organizer={
        "type": "FTA 이해관계 비교 매트릭스",
        "beneficiaries": {
            "수출 기업": "관세 철폐 ➔ 가격 경쟁력 ➔ 해외 판매 급증",
            "일반 소비자": "수입품 가격 하락 ➔ 선택의 폭 확대"
        },
        "vulnerabilities": {
            "국내 농축산업": "저가 농산물 수입 ➔ 농가 소득 감소 ➔ 식량 안보 위협"
        },
        "solution": "무역 이익의 농어촌 재투자 및 고부가가치 농업 육성"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "관점 및 이해관계 분석",
            "stem": "위 글의 2문단과 3문단을 바탕으로 할 때, 자유무역협정(FTA)에 대한 설명으로 가장 적절한 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "가격 경쟁력이 취약한 국내 산업, 특히 값싼 외국산 농축산물이 대량 유입될 경우 국내 농가와 축산업은 심각한 타격을 입게 됩니다.",
            "options": [
                {"label": "①", "text": "수출 기업과 소비자에게 이익을 주지만 국내 취약 농가에는 타격을 줄 수 있어 양면성을 지닌다.", "is_correct": True, "formula": "정답", "explanation": "2문단의 혜택과 3문단의 피해 우려를 균형 있게 종합한 진술입니다."},
                {"label": "②", "text": "모든 산업이 100% 무조건 이익만 보므로 아무런 지원 대책도 필요 없다.", "is_correct": False, "formula": "D5", "explanation": "3문단에서 농가 피해를 명시했습니다."},
                {"label": "③", "text": "국제 분업은 다른 나라와 절대 대화나 무역을 하지 않는 쇄국 정책이다.", "is_correct": False, "formula": "D3", "explanation": "비교우위에 따른 국가 간 특화 및 교역입니다."},
                {"label": "④", "text": "FTA가 체결되면 모든 외국 물건에 1000%의 세금을 새로 매긴다.", "is_correct": False, "formula": "D1", "explanation": "관세를 낮추거나 없애는 협정입니다."},
                {"label": "⑤", "text": "농업은 식량 안보와 아무 관련이 없으므로 모조리 폐업시켜야 한다.", "is_correct": False, "formula": "D4", "explanation": "본문의 식량 안보 중요성 강조와 반대됩니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "필자의 주장 및 정책 대안 추론",
            "stem": "4문단에서 필자가 제시한 성공적인 무역 강국의 해법으로 가장 적절한 것은?",
            "target_para_idx": 3,
            "spotlight_quote": "따라서 성공적인 무역 강국이 되기 위해서는 FTA를 통해 반도체·자동차 등 첨단 수출 산업을 적극 육성하는 한편, 무역 이익의 일부를 취약 농어촌에 재투자하여 피해 산업의 경쟁력을 높이고 상생을 도모하는 균형 잡힌 정책적 보완이 반드시 병행되어야 합니다.",
            "options": [
                {"label": "①", "text": "첨단 제조업의 수출을 육성하면서도 무역 이익을 취약 농어촌에 재투자하는 상생 정책을 펴야 한다.", "is_correct": True, "formula": "정답", "explanation": "4문단의 결론에 명확히 제시되어 있습니다."},
                {"label": "②", "text": "외국과의 모든 무역을 오늘부로 영구 중단하고 문을 걸어 잠근다.", "is_correct": False, "formula": "D1", "explanation": "무역 중단은 해법이 아닙니다."},
                {"label": "③", "text": "농민들에게 세금을 10배로 거두어 수출 대기업에 전액 몰아준다.", "is_correct": False, "formula": "D5", "explanation": "상생 취지에 정면으로 위배됩니다."},
                {"label": "④", "text": "모든 물건을 한국 안에서만 만들고 해외 판매는 금지한다.", "is_correct": False, "formula": "D2", "explanation": "수출 주도형 경제와 모순됩니다."},
                {"label": "⑤", "text": "소비자들이 수입 과일을 사 먹으면 전원 처벌하는 법을 만든다.", "is_correct": False, "formula": "D6", "explanation": "황당한 왜곡 오답입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 자유무역협정(FTA) 체결 시 관세를 철폐함으로써 얻는 직접적인 경제 효과는?",
            "options": [
                {"label": "①", "text": "수출 상품의 가격 경쟁력 강화 및 수입품 가격 인하", "is_correct": True},
                {"label": "②", "text": "전 세계 모든 은행의 폐쇄 및 화폐 통일", "is_correct": False},
                {"label": "③", "text": "국내 모든 공장의 가동 전면 중단", "is_correct": False},
                {"label": "④", "text": "농산물 가격의 전 세계적 100배 폭등", "is_correct": False},
                {"label": "⑤", "text": "국경 간 이동 시 여권 검사 전면 금지", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "수출 기업은 상대국 시장에서 가격 경쟁력을 확보하여 수출을 크게 늘릴 수 있고, 소비자들은 질 좋은 외제 과일이나 공산품을 훨씬 저렴한 가격에 구매할 수 있다는", "is_correct": True},
                {"label": "②", "text": "오늘날 세계 각국은 자신이 상대적으로 더 잘 만들 수 있는", "is_correct": False},
                {"label": "③", "text": "가격 경쟁력이 취약한 국내 산업, 특히 값싼 외국산 농축산물이", "is_correct": False},
                {"label": "④", "text": "농업 기반이 무너지면 국가의 식량 안보가 위협받을 수 있으며,", "is_correct": False},
                {"label": "⑤", "text": "이러한 무역을 극대화하기 위해 국가 간에 상품 이동 시", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "FTA의 명암과 상생 방안 논술",
        "guide": "자유무역협정의 수출 기회와 취약 산업 보호를 위한 상생 대책을 1문장으로 정리하세요.",
        "template": "자유무역협정은 [수출 경쟁력]을 높여 경제 성장을 이끌지만, 취약 농업 부문의 피해를 보전하는 [상생 정책]이 반드시 뒷받침되어야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "경제 설명문에서는 혜택을 받는 집단(수출기업)과 피해를 입는 집단(취약농가)의 입장을 대조해요."},
        "step1_2_drill": {"task": "관세 철폐(가격 경쟁력 강화) vs 농가 피해(지원 대책 필요) 인과 연결하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "FTA는 수출 기업에 유리하지만 국내 취약 농가에는 지원 대책이 필요하다.", "answer": "O", "reason": "본문에 제시된 균형 잡힌 논지입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 마트에 바나나와 망고가 흔해진 경제적 이유",
        "situation": "마트 과일 코너에서 수입 과일을 장바구니에 담을 때",
        "parent_question": "우리나라에서는 망고나 바나나가 안 자라는데 왜 이렇게 싸게 많이 팔고 있을까?",
        "expected_answer": "다른 나라와 'FTA'를 맺어서 세금(관세)을 없애고 자유롭게 무역하기 때문이래요! 대신 우리 쌀과 과일 농가도 지켜줘야 해요.",
        "coaching_tip": "식탁 위의 세계화와 우리 농축산물 애용의 가치를 함께 나누어 보세요."
    }
)
