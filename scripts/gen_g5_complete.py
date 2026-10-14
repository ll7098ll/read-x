# -*- coding: utf-8 -*-
"""
Master Generator for Grade 5 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
5-Option Standard (수능 평가원 표준형, expected_opt_len = 5)
Output: courseware/data/item_bank/g5_item_bank.json
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from item_bank_schema_helper import build_expository_slot, build_common_slot
import gen_g5

ITEM_BANK_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data", "item_bank")
os.makedirs(ITEM_BANK_DIR, exist_ok=True)

# 1. Common Foundation Slots for Grade 5 (6 slots from gen_g5)
g5_common_slots = gen_g5.g5_common_slots

# 2. Expository Slots already defined in gen_g5
# - gen_g5.g5_slot_v11 (V1-1)
# - gen_g5.g5_slots_part2[0] (V1-2)
# - gen_g5.g5_slots_part2[1] (V1-3)
# - gen_g5.g5_flagship_v32 (V3-2)
g5_flagship_v32 = gen_g5.g5_flagship_v32
if g5_flagship_v32:
    g5_flagship_v32["subskill_code"] = "V3-2"

slots_dict = {
    "V1-1": gen_g5.g5_slot_v11,
    "V1-2": gen_g5.g5_slots_part2[0],
    "V1-3": gen_g5.g5_slots_part2[1],
    "V3-2": g5_flagship_v32,
}

# 3. Define the remaining 12 slots for Grade 5:
# V1-4, V2-1, V2-2, V2-3, V2-4, V3-1, V3-3, W1, W2, W3, W4, W5

# Slot 4: V1-4
slots_dict["V1-4"] = build_expository_slot(
    grade_num=5,
    subskill_code="V1-4",
    subject="사회(인권과 헌법 5-1)",
    unit="1. 국민의 권리와 의무",
    concept="대한민국 헌법이 보장하는 국민의 5대 기본권과 4대 의무",
    text_structure="분류·열거 + 정의·예시",
    structure_type_code="classification",
    passage_title="헌법이 지켜주는 국민의 기본권과 시민의 의무",
    paragraphs=[
        "대한민국 최고의 법인 헌법은 모든 국민이 인간으로서의 존엄과 가치를 누리며 살아갈 수 있도록 다섯 가지 핵심 '기본권'을 보장하고 있습니다. 기본권이란 사람이 태어나면서부터 당연히 가지는 기본적 자유와 권리를 법으로 확정한 것입니다.",
        "5대 기본권에는 차별받지 않을 '평등권', 부당하게 간섭받지 않고 행동할 '자유권', 나랏일에 참여할 수 있는 '참정권', 기본권이 침해되었을 때 국가에 구제를 요구하는 '청구권', 그리고 인간다운 생활을 보장받을 '사회권'이 있습니다. 이 권리들은 서로 긴밀히 연결되어 민주 시민의 삶을 지탱합니다.",
        "권리를 누리기 위해서는 그에 상응하는 책임인 '4대 의무'도 성실히 다해야 합니다. 국민의 의무에는 '교육의 의무', '근로의 의무', 세금을 내는 '납세의 의무', 그리고 나라를 지키는 '국방의 의무'가 있습니다. 권리와 의무가 조화를 이룰 때 비로소 정의롭고 평화로운 민주 사회가 유지됩니다."
    ],
    vocab_notes=[
        {"word": "기본권", "definition": "헌법에 의해 보장되는 국민의 기본적인 자유와 권리"},
        {"word": "참정권", "definition": "선거권 등 국민이 국가의 정치에 직접 또는 간접으로 참여할 수 있는 권리"}
    ],
    visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
      <h4 class="font-bold text-blue-900 mb-2">⚖️ 대한민국 헌법의 5대 기본권 vs 4대 의무</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-blue-100">
          <strong class="text-blue-800">5대 기본권</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1">
            <li>평등권 (차별 금지)</li><li>자유권 (신체·표현 자유)</li>
            <li>참정권 (선거 참여)</li><li>청구권 (재판 요구)</li>
            <li>사회권 (인간다운 생활)</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-blue-100">
          <strong class="text-blue-800">4대 의무</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1">
            <li>교육의 의무</li><li>근로의 의무</li>
            <li>납세의 의무</li><li>국방의 의무</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v14-c1", "text": "기본권이 침해되었을 때 국가에 구제를 요구하는 '청구권'", "role": "청구권 정의", "para_idx": 1},
        {"cue_id": "g5-v14-c2", "text": "권리와 의무가 조화를 이룰 때 비로소 정의롭고 평화로운 민주 사회가 유지됩니다", "role": "권리와 의무의 조화", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "헌법 체계도",
        "constitution": "대한민국 헌법",
        "rights_5": ["평등권", "자유권", "참정권", "청구권", "사회권"],
        "duties_4": ["교육", "근로", "납세", "국방"]
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "개념 분류 세부 확인",
            "stem": "자신의 권리가 부당하게 침해당했을 때 법원에 재판을 요구할 수 있는 기본권은?",
            "target_para_idx": 1,
            "spotlight_quote": "기본권이 침해되었을 때 국가에 구제를 요구하는 '청구권',",
            "options": [
                {"label": "①", "text": "청구권", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 기본권 침해 시 구제를 요구하는 권리입니다."},
                {"label": "②", "text": "평등권", "is_correct": False, "formula": "D3", "explanation": "차별받지 않을 권리입니다."},
                {"label": "③", "text": "국방의 의무", "is_correct": False, "formula": "D4", "explanation": "권리가 아니라 국민의 의무입니다."},
                {"label": "④", "text": "참정권", "is_correct": False, "formula": "D2", "explanation": "선거 등 정치에 참여할 권리입니다."},
                {"label": "⑤", "text": "자유권", "is_correct": False, "formula": "D1", "explanation": "간섭받지 않고 행동할 권리입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "인과 및 조화 관계 파악",
            "stem": "글쓴이가 3문단에서 4대 의무를 강조하며 전달하려는 핵심 교훈은 무엇인가요?",
            "target_para_idx": 2,
            "spotlight_quote": "권리와 의무가 조화를 이룰 때 비로소 정의롭고 평화로운 민주 사회가 유지됩니다.",
            "options": [
                {"label": "①", "text": "국민의 기본권을 보장받기 위해서는 상응하는 의무를 성실히 다해야 한다.", "is_correct": True, "formula": "정답", "explanation": "3문단 마지막 결론 문장에 나타난 권리와 의무의 조화입니다."},
                {"label": "②", "text": "의무만 중요하므로 모든 기본권은 당장 포기해야 한다.", "is_correct": False, "formula": "D5", "explanation": "기본권과 대립되는 극단적 왜곡입니다."},
                {"label": "③", "text": "세금을 내지 않는 사람만 선거에 출마할 수 있다.", "is_correct": False, "formula": "D3", "explanation": "납세의 의무에 위배됩니다."},
                {"label": "④", "text": "헌법은 대통령 혼자 마음대로 바꿀 수 있는 법이다.", "is_correct": False, "formula": "D1", "explanation": "민주주의 헌법 원리와 어긋납니다."},
                {"label": "⑤", "text": "교육은 개인이 알아서 하고 국가는 상관하지 않는다.", "is_correct": False, "formula": "D2", "explanation": "교육은 헌법상 의무이자 권리입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 다음 중 국민의 4대 의무에 해당하지 않는 것은?",
            "options": [
                {"label": "①", "text": "해외여행의 의무", "is_correct": True},
                {"label": "②", "text": "교육의 의무", "is_correct": False},
                {"label": "③", "text": "근로의 의무", "is_correct": False},
                {"label": "④", "text": "납세의 의무", "is_correct": False},
                {"label": "⑤", "text": "국방의 의무", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "국민의 의무에는 '교육의 의무', '근로의 의무', 세금을 내는 '납세의 의무', 그리고 나라를 지키는 '국방의 의무'가 있습니다.", "is_correct": True},
                {"label": "②", "text": "5대 기본권에는 차별받지 않을 '평등권',", "is_correct": False},
                {"label": "③", "text": "대한민국 최고의 법인 헌법은 모든 국민이 인간으로서의", "is_correct": False},
                {"label": "④", "text": "기본권이란 사람이 태어나면서부터 당연히 가지는", "is_correct": False},
                {"label": "⑤", "text": "권리를 누리기 위해서는 그에 상응하는 책임인", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "기본권과 의무 조화 논술문 쓰기",
        "guide": "내가 가장 소중하게 생각하는 기본권 1가지와 그에 따르는 의무를 한 문장으로 써 보세요.",
        "template": "나는 [자유권]을 소중히 누리는 동시에, 타인의 권리를 지키기 위해 [국민의 의무]를 성실히 다하겠습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "5대 기본권(평등, 자유, 참정, 청구, 사회)과 4대 의무를 구분해요."},
        "step1_2_drill": {"task": "기본권 상황 카드와 헌법 조항 짝맞춤 훈련"},
        "step3_vaccine": {"ox_quiz": [{"statement": "청구권은 기본권이 침해되었을 때 국가에 구제를 요구하는 권리입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 나의 권리와 책임",
        "situation": "선거일 투표 뉴스를 보거나 가족 회의를 할 때",
        "parent_question": "어른들이 투표소에 가서 투표하는 것은 헌법의 어떤 권리를 행사하는 걸까?",
        "expected_answer": "나랏일에 주권자로서 참여하는 '참정권'을 행사하는 거래요!",
        "coaching_tip": "민주주의 국가의 주권자로서 권리와 책임의 소중함을 함께 나눠 주세요."
    }
)

print("Constructed G5 slot V1-4 successfully.")

# Slot 5: V2-1
slots_dict["V2-1"] = build_expository_slot(
    grade_num=5,
    subskill_code="V2-1",
    subject="과학(산과 염기 5-2) / 실과(발효식품)",
    unit="2. 용액의 성질과 이용",
    concept="산성·염기성 용액의 ‘수용성·지시약·중화’와 발효식품의 ‘유기산’",
    text_structure="비교·대조·인과",
    structure_type_code="comparison",
    passage_title="산과 염기의 만남, 지시약의 색 변화와 중화 반응",
    paragraphs=[
        "주변의 다양한 수용액은 성질에 따라 신맛을 내고 금속을 녹이는 '산성 용액'과 미끈미끈하고 단백질을 녹이는 '염기성 용액'으로 구분됩니다. 용액의 성질을 구별하기 위해 특정한 물질과 반응하여 색깔이 변하는 '지시약'을 사용합니다.",
        "대표적인 지시약인 붉은 양배추 지시약을 넣으면, 묽은 염산이나 식초 같은 산성 용액에서는 붉은색 계열로 변하고, 유리 세정제나 비눗물 같은 염기성 용액에서는 푸른색이나 노란색 계열로 변합니다. 김치가 알맞게 익었을 때 새콤한 맛이 나는 것은 유산균이 젖산 같은 유기산을 생성하여 김치 국물이 약한 산성을 띠기 때문입니다.",
        "산성 용액과 염기성 용액을 적절한 비율로 섞으면 서로의 성질을 약화시키는 '중화 반응'이 일어납니다. 위산이 과다하게 나와 속이 쓰릴 때 염기성 제산제를 먹거나, 생선의 비린내(염기성)를 잡기 위해 레몬즙(산성)을 뿌리는 생활의 지혜가 모두 중화 반응을 이용한 것입니다."
    ],
    vocab_notes=[
        {"word": "지시약", "definition": "용액이 산성인지 염기성인지에 따라 색깔이 변하여 성질을 알려 주는 물질"},
        {"word": "중화 반응", "definition": "산과 염기가 반응하여 각각의 성질을 잃고 물과 염을 생성하는 반응"}
    ],
    visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
      <h4 class="font-bold text-red-900 mb-2">🧪 산성과 염기성의 특성 및 중화 반응 비교</h4>
      <table class="w-full text-xs text-center border-collapse">
        <tr class="bg-red-100"><th class="p-1 border border-red-200">구분</th><th class="p-1 border border-red-200">산성 용액 (식초·레몬즙)</th><th class="p-1 border border-red-200">염기성 용액 (비눗물·세정제)</th></tr>
        <tr><td class="p-1 border border-red-200 font-bold bg-white">맛과 촉감</td><td class="p-1 border border-red-200 bg-white">신맛, 금속 반응(기포)</td><td class="p-1 border border-red-200 bg-white">쓴맛, 미끈거림 (단백질 용해)</td></tr>
        <tr><td class="p-1 border border-red-200 font-bold bg-white">붉은양배추 지시약</td><td class="p-1 border border-red-200 bg-white">붉은색 계열</td><td class="p-1 border border-red-200 bg-white">푸른색·노란색 계열</td></tr>
        <tr><td class="p-1 border border-red-200 font-bold bg-white">중화 사례</td><td colspan="2" class="p-1 border border-red-200 bg-white">위산 과다에 제산제 복용, 생선 비린내에 레몬즙 뿌리기</td></tr>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v21-c1", "text": "붉은 양배추 지시약을 넣으면, 묽은 염산이나 식초 같은 산성 용액에서는 붉은색 계열로 변하고", "role": "산성 지시약 반응", "para_idx": 1},
        {"cue_id": "g5-v21-c2", "text": "산성 용액과 염기성 용액을 적절한 비율로 섞으면 서로의 성질을 약화시키는 '중화 반응'이 일어납니다", "role": "중화 반응 원리", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "화학 반응 대조도",
        "acid": "산성 (신맛, 붉은색 지시약, 금속 반응)",
        "base": "염기성 (미끈거림, 푸른색 지시약, 단백질 용해)",
        "neutralization": "중화 반응 (산 + 염기 ➔ 물 + 염, 성질 약화)"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "개념 적용 세부 확인",
            "stem": "생선회에 레몬즙을 뿌려 비린내를 없애는 조리법의 과학적 원리는?",
            "target_para_idx": 2,
            "spotlight_quote": "생선의 비린내(염기성)를 잡기 위해 레몬즙(산성)을 뿌리는 생활의 지혜가 모두 중화 반응을 이용한 것입니다.",
            "options": [
                {"label": "①", "text": "염기성인 생선 비린내 물질을 산성인 레몬즙으로 중화시켜 없앤다.", "is_correct": True, "formula": "정답", "explanation": "3문단 마지막 문장에 서술된 중화 반응의 실생활 활용 사례입니다."},
                {"label": "②", "text": "레몬즙이 생선의 온도를 영하로 급랭시켜 얼린다.", "is_correct": False, "formula": "D3", "explanation": "온도 변화와 무관합니다."},
                {"label": "③", "text": "생선 살을 완전히 녹여 국물로 만들기 위해", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                {"label": "④", "text": "비린내가 레몬 껍질 속으로 숨어 들어가게 하려고", "is_correct": False, "formula": "D5", "explanation": "비과학적 허구입니다."},
                {"label": "⑤", "text": "생선 뼈를 금으로 바꾸기 위해", "is_correct": False, "formula": "D6", "explanation": "연금술적 거짓말입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "지시약 반응 비교",
            "stem": "붉은 양배추 지시약을 넣었을 때 나타나는 색깔 변화로 옳은 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "산성 용액에서는 붉은색 계열로 변하고, 유리 세정제나 비눗물 같은 염기성 용액에서는 푸른색이나 노란색 계열로 변합니다.",
            "options": [
                {"label": "①", "text": "식초(산성)에서는 붉은색, 비눗물(염기성)에서는 푸른색이나 노란색으로 변한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 지시약의 정확한 변색 결과입니다."},
                {"label": "②", "text": "모든 용액에서 언제나 검은색으로만 변한다.", "is_correct": False, "formula": "D4", "explanation": "성질에 따라 색이 달라집니다."},
                {"label": "③", "text": "산성 용액에서는 보라색 꽃이 피어난다.", "is_correct": False, "formula": "D6", "explanation": "꽃이 피는 것이 아닙니다."},
                {"label": "④", "text": "염기성 용액에서는 아무런 색깔 변화가 전혀 없다.", "is_correct": False, "formula": "D2", "explanation": "푸른색·노란색 계열로 변합니다."},
                {"label": "⑤", "text": "식초에서는 푸른색, 비눗물에서는 붉은색으로 정반대로 변한다.", "is_correct": False, "formula": "D3", "explanation": "색깔을 반대로 뒤바꾼 함정입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 알맞게 익은 김치에서 새콤한 신맛이 나는 과학적 원인은?",
            "options": [
                {"label": "①", "text": "유산균이 젖산 같은 유기산을 생성하여 산성을 띠기 때문에", "is_correct": True},
                {"label": "②", "text": "배추가 햇빛을 받아 소금을 만들어 냈기 때문에", "is_correct": False},
                {"label": "③", "text": "김치통의 플라스틱이 녹아 흘러내려서", "is_correct": False},
                {"label": "④", "text": "고춧가루가 얼어붙어 설탕으로 변해서", "is_correct": False},
                {"label": "⑤", "text": "냉장고가 전기를 많이 먹어서", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "유산균이 젖산 같은 유기산을 생성하여 김치 국물이 약한 산성을 띠기 때문입니다.", "is_correct": True},
                {"label": "②", "text": "주변의 다양한 수용액은 성질에 따라", "is_correct": False},
                {"label": "③", "text": "산성 용액과 염기성 용액을 적절한 비율로 섞으면", "is_correct": False},
                {"label": "④", "text": "대표적인 지시약인 붉은 양배추 지시약을 넣으면,", "is_correct": False},
                {"label": "⑤", "text": "위산이 과다하게 나와 속이 쓰릴 때 염기성 제산제를", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "중화 반응 생활 보고서 쓰기",
        "guide": "속 쓰림에 제산제를 먹는 원리를 산·염기 중화 개념으로 한 문장 써 보세요.",
        "template": "위산(산성)이 과다할 때 제산제(염기성)를 복용하면 [중화 반응]이 일어나 위벽을 보호하고 속 쓰림을 완화합니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "산성(신맛, 붉은색)과 염기성(미끈거림, 푸른색), 그리고 중화 반응을 정리해요."},
        "step1_2_drill": {"task": "산성 물질과 염기성 물질 및 지시약 변색 카드 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "산과 염기가 반응하여 서로의 성질을 잃는 것을 중화 반응이라 합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 생선에 레몬을 뿌리는 까닭",
        "situation": "생선구이나 회를 먹을 때 레몬 조각을 짤 때",
        "parent_question": "생선에 레몬즙을 뿌리는 건 상큼한 맛뿐만 아니라 어떤 과학 반응 때문일까?",
        "expected_answer": "생선 비린내(염기성)를 레몬의 산성 성분이 만나 서로 약화시키는 '중화 반응' 때문이래요!",
        "coaching_tip": "식탁 위 요리 비결 속에 숨은 산과 염기의 화학 반응을 이야기해 보세요."
    }
)

# Slot 6: V2-2
slots_dict["V2-2"] = build_expository_slot(
    grade_num=5,
    subskill_code="V2-2",
    subject="과학(생물과 환경 5-2)",
    unit="2. 생태계와 상호작용",
    concept="생태계 먹이그물의 평형과 외래종(큰입배스) 유입의 연쇄 영향",
    text_structure="인과·과정 + 문제·해결",
    structure_type_code="causal",
    passage_title="생태계 평형의 파괴와 외래 생물의 연쇄 영향",
    paragraphs=[
        "생태계 내에서 생산자(식물), 소비자(동물), 분해자(균류)는 서로 먹고 먹히는 복잡한 '먹이그물'을 형성하며 살아갑니다. 먹이그물이 복잡하게 얽혀 있을수록 특정 생물종이 일시적으로 줄어도 다른 먹이로 대체할 수 있어 생태계의 '평형(균형)'이 안정적으로 유지됩니다.",
        "그러나 번식력이 강하고 천적이 없는 '외래 생물'이 무분별하게 유입되면 이러한 평형은 급격히 무너집니다. 대표적인 생태계 교란종인 '큰입배스'와 '파랑볼우럭(블루길)'은 토종 참붕어와 피라미 치어, 토종 새우를 닥치는 대로 잡아먹어 토종 어류의 개체 수를 급감시켰습니다.",
        "토종 작은 물고기가 사라지자 이들이 먹던 장구벌레와 물속 플랑크톤이 폭발적으로 증식하여 녹조 현상이 심화되는 등 연쇄적인 생태계 파괴가 일어났습니다. 생태계의 한 고리가 끊어지면 전체 환경에 치명적인 영향을 미치므로, 외래종 퇴치와 토종 서식지 복원이 시급합니다."
    ],
    vocab_notes=[
        {"word": "생태계 평형", "definition": "생태계를 이루는 생물의 종류와 개체 수가 안정적으로 유지되는 상태"},
        {"word": "생태계 교란종", "definition": "외래 생물 중 번식력이 강해 고유 생태계의 균형을 깨뜨리는 생물"}
    ],
    visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">🐟 외래종 유입에 따른 연쇄적 생태 파괴 사슬</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-emerald-200">1. 큰입배스(외래 포식자) 유입 ➔ 토종 피라미·치어 남획</div>
            <div class="p-1 bg-white rounded border border-emerald-200">2. 토종 어류 급감 ➔ 플랑크톤·유충 천적 소멸</div>
            <div class="p-1 bg-white rounded border border-emerald-200">3. 조류 과다 번식 ➔ 하천 녹조 심화 및 수질 오염 (생태계 파괴)</div>
          </div>
        </div>""",
    hottext_cues=[
        {"cue_id": "g5-v22-c1", "text": "먹이그물이 복잡하게 얽혀 있을수록 특정 생물종이 일시적으로 줄어도 다른 먹이로 대체할 수 있어", "role": "복잡한 먹이그물의 안정성", "para_idx": 0},
        {"cue_id": "g5-v22-c2", "text": "토종 작은 물고기가 사라지자 이들이 먹던 장구벌레와 물속 플랑크톤이 폭발적으로 증식하여", "role": "연쇄적 인과 파괴", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "연쇄 인과 사슬망",
        "trigger": "외래종(큰입배스) 유입",
        "step1": "토종 소형 어류 포식 급감",
        "step2": "중간 포식자 실종 및 플랑크톤 급증",
        "final_result": "녹조 현상 심화 및 생태계 평형 파괴"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "생태계 평형 원리 확인",
            "stem": "먹이그물이 복잡하게 얽혀 있을 때 생태계 평형이 안정적으로 유지되는 까닭은?",
            "target_para_idx": 0,
            "spotlight_quote": "먹이그물이 복잡하게 얽혀 있을수록 특정 생물종이 일시적으로 줄어도 다른 먹이로 대체할 수 있어 생태계의 '평형(균형)'이 안정적으로 유지됩니다.",
            "options": [
                {"label": "①", "text": "어떤 생물종이 줄어도 다른 먹이로 대체할 수 있는 통로가 다양하기 때문에", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 생물다양성과 먹이그물 안정성의 핵심 원리입니다."},
                {"label": "②", "text": "모든 동물이 풀만 먹고 살기 때문에", "is_correct": False, "formula": "D3", "explanation": "초식과 육식이 공존합니다."},
                {"label": "③", "text": "외래종이 들어오면 동물들이 친구가 되기 때문에", "is_correct": False, "formula": "D5", "explanation": "외래종은 생태계를 교란합니다."},
                {"label": "④", "text": "물속 산소가 100배로 증가하기 때문에", "is_correct": False, "formula": "D1", "explanation": "근거 없는 진술입니다."},
                {"label": "⑤", "text": "생산자인 식물이 완전히 사라지기 때문에", "is_correct": False, "formula": "D4", "explanation": "식물이 사라지면 생태계가 붕괴합니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "연쇄 인과 결과 분석",
            "stem": "외래 어종인 큰입배스의 유입이 초래한 최종적인 환경 피해는 무엇인가요?",
            "target_para_idx": 2,
            "spotlight_quote": "토종 작은 물고기가 사라지자 이들이 먹던 장구벌레와 물속 플랑크톤이 폭발적으로 증식하여 녹조 현상이 심화되는 등 연쇄적인 생태계 파괴가 일어났습니다.",
            "options": [
                {"label": "①", "text": "토종 어류 감소로 플랑크톤이 폭증하여 녹조 현상과 수질 오염이 심화되었다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 먹이사슬 붕괴에 따른 연쇄적 피해입니다."},
                {"label": "②", "text": "강물이 꽁꽁 얼어붙어 북극곰이 찾아왔다.", "is_correct": False, "formula": "D6", "explanation": "기후와 무관한 허구입니다."},
                {"label": "③", "text": "토종 붕어의 몸집이 고래만큼 커졌다.", "is_correct": False, "formula": "D2", "explanation": "과장된 오답입니다."},
                {"label": "④", "text": "바닷물이 증발하여 사막이 되었다.", "is_correct": False, "formula": "D4", "explanation": "하천 생태계와 동떨어진 진술입니다."},
                {"label": "⑤", "text": "모든 모기와 파리가 지구상에서 박멸되었다.", "is_correct": False, "formula": "D5", "explanation": "오히려 장구벌레가 증식했습니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 천적이 없는 외래종이 토종 생태계에 치명적인 이유는?",
            "options": [
                {"label": "①", "text": "개체 수를 조절할 자연 천적이 없어 무제한 번식하며 토종 생물을 남획하기 때문에", "is_correct": True},
                {"label": "②", "text": "물속에서 전기를 방출하여 감전시키기 때문에", "is_correct": False},
                {"label": "③", "text": "외래종이 말을 타고 다니기 때문에", "is_correct": False},
                {"label": "④", "text": "식물만 골라서 불태우기 때문에", "is_correct": False},
                {"label": "⑤", "text": "강바닥의 돌을 전부 깨뜨리기 때문에", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "번식력이 강하고 천적이 없는 '외래 생물'이 무분별하게 유입되면 이러한 평형은 급격히 무너집니다.", "is_correct": True},
                {"label": "②", "text": "생태계 내에서 생산자(식물), 소비자(동물),", "is_correct": False},
                {"label": "③", "text": "토종 참붕어와 피라미 치어, 토종 새우를 닥치는 대로", "is_correct": False},
                {"label": "④", "text": "생태계의 한 고리가 끊어지면 전체 환경에 치명적인 영향을 미치므로,", "is_correct": False},
                {"label": "⑤", "text": "장구벌레와 물속 플랑크톤이 폭발적으로 증식하여", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "생태계 연쇄 파괴 인과 보고서 작성",
        "guide": "외래종 유입에서 녹조 심화까지의 연쇄 과정을 인과 접속어로 써 보세요.",
        "template": "큰입배스가 유입되어 [토종 어류]가 급감하자, 천적이 없어진 [플랑크톤]이 폭발적으로 증식하여 녹조 현상을 초래했습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "생태계 파괴는 단일 사건이 아닌 연쇄적 도미노 인과 사슬로 분석해요."},
        "step1_2_drill": {"task": "생태계 교란종 유입 도미노 사슬 번호 매기기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "먹이그물이 복잡할수록 생태계 평형은 안정적으로 유지됩니다.", "answer": "O", "reason": "생물다양성의 기본 원리입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 강가에 사는 외래 물고기",
        "situation": "한강이나 저수지에서 낚시 금지 표지판이나 생태계 교란종 안내를 볼 때",
        "parent_question": "배스나 붉은귀거북 같은 외래종을 강에 함부로 방생하면 왜 큰일이 날까?",
        "expected_answer": "천적이 없어서 토종 물고기를 다 잡아먹고 먹이사슬을 무너뜨려 강 전체가 오염된대요!",
        "coaching_tip": "외래종 무단 방생의 위험성과 생태계 보전의 중요성을 함께 일깨워 주세요."
    }
)

print("Constructed G5 slots V2-1 and V2-2.")

# Slot 7: V2-3
slots_dict["V2-3"] = build_expository_slot(
    grade_num=5,
    subskill_code="V2-3",
    subject="사회(국토와 인구 5-1) / 수학(꺾은선그래프)",
    unit="2. 인구 변화와 우리 국토",
    concept="우리나라의 지형·산업 발달에 따른 인구 분포와 고령화 추이",
    text_structure="인과·비교",
    structure_type_code="causal",
    passage_title="산업화에 따른 인구 이동과 초고령 사회의 도래",
    paragraphs=[
        "우리나라의 인구 분포는 과거 농경 중심 사회에서 1960년대 이후 급격한 산업화와 도시화를 겪으며 획기적인 변화를 맞이했습니다. 일자리와 교육 시설이 풍부한 수도권과 대도시로 인구가 집중되는 '이촌향도' 현상이 일어났습니다.",
        "그 결과 서울과 경기도를 포함한 수도권에 전체 인구의 50% 이상이 거주하게 되었으며, 반면에 농산어촌 지역은 청장년층 인구의 유출로 급격한 인구 감소를 겪게 되었습니다. 통계청의 '연도별 연령별 인구 구성 꺾은선그래프'를 보면 14세 이하 유소년 인구는 급감하고 65세 이상 고령 인구는 가파르게 증가하고 있습니다.",
        "우리나라는 이미 65세 이상 인구 비율이 20%를 넘어서는 '초고령 사회'에 진입하고 있습니다. 이러한 인구 구조의 변화는 노동력 부족과 지방 소멸 위기라는 새로운 사회적 과제를 던져주고 있어, 균형 있는 국토 발전과 출산·양육 지원 정책이 절실합니다."
    ],
    vocab_notes=[
        {"word": "이촌향도", "definition": "농촌을 떠나 일자리와 편의시설이 많은 도시로 인구가 이동하는 현상"},
        {"word": "초고령 사회", "definition": "전체 인구 중 65세 이상 고령자 비율이 20% 이상인 사회"}
    ],
    visual_html="""<div class="p-3 bg-indigo-50 rounded border border-indigo-200">
      <h4 class="font-bold text-indigo-900 mb-2">📈 연령별 인구 구성비 추이 (통계청 데이터)</h4>
      <div class="space-y-1 text-xs">
        <div class="p-1 bg-white rounded border border-indigo-200"><strong>유소년 인구(0~14세):</strong> 1970년 42.5% ➔ 2024년 10.6% (지속 급감)</div>
        <div class="p-1 bg-white rounded border border-indigo-200"><strong>고령 인구(65세 이상):</strong> 1970년 3.1% ➔ 2024년 19.8% (가파른 급상승)</div>
        <div class="p-1 bg-white rounded border border-indigo-200"><strong>핵심 과제:</strong> 청년 유출에 따른 농산어촌 지방 소멸 방지</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v23-c1", "text": "일자리와 교육 시설이 풍부한 수도권과 대도시로 인구가 집중되는 '이촌향도' 현상이 일어났습니다", "role": "인구 이동 인과 원인", "para_idx": 0},
        {"cue_id": "g5-v23-c2", "text": "우리나라는 이미 65세 이상 인구 비율이 20%를 넘어서는 '초고령 사회'에 진입하고 있습니다", "role": "초고령 사회 현주소", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "인구 구조 인과도",
        "industrialization": "산업화 및 이촌향도",
        "consequences": ["수도권 과밀 (전체 인구 50% 초과)", "농산어촌 고령화 및 지방 소멸"],
        "future_challenges": "저출생·초고령 사회 극복 대책"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "통계 및 개념 세부 확인",
            "stem": "'초고령 사회'를 정의하는 통계적 기준으로 올바른 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "우리나라는 이미 65세 이상 인구 비율이 20%를 넘어서는 '초고령 사회'에 진입하고 있습니다.",
            "options": [
                {"label": "①", "text": "전체 인구 중 65세 이상 고령자 비율이 20% 이상인 사회", "is_correct": True, "formula": "정답", "explanation": "3문단 첫 문장에 명시된 사회학적 기준입니다."},
                {"label": "②", "text": "유소년 인구 비율이 50%를 넘는 젊은 사회", "is_correct": False, "formula": "D3", "explanation": "유소년 인구는 급감하고 있습니다."},
                {"label": "③", "text": "수도권에만 사람이 살고 지방에는 아무도 안 사는 사회", "is_correct": False, "formula": "D4", "explanation": "극단적 과장입니다."},
                {"label": "④", "text": "모든 국민이 100세 이상인 사회", "is_correct": False, "formula": "D1", "explanation": "허구적 오답입니다."},
                {"label": "⑤", "text": "농사를 짓는 사람만 투표할 수 있는 사회", "is_correct": False, "formula": "D5", "explanation": "엉뚱한 오답입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "인구 이동 인과 분석",
            "stem": "1960년대 이후 농촌 인구가 대도시로 대거 이동한(이촌향도) 가장 큰 까닭은?",
            "target_para_idx": 0,
            "spotlight_quote": "일자리와 교육 시설이 풍부한 수도권과 대도시로 인구가 집중되는 '이촌향도' 현상이 일어났습니다.",
            "options": [
                {"label": "①", "text": "산업화로 인해 일자리와 교육 시설이 도시에 풍부해졌기 때문에", "is_correct": True, "formula": "정답", "explanation": "1문단 마지막 문장에 서술된 명확한 인과 요인입니다."},
                {"label": "②", "text": "농촌에 큰 지진이 매일 일어나서", "is_correct": False, "formula": "D6", "explanation": "지진과 무관합니다."},
                {"label": "③", "text": "정부에서 농촌 거주를 전면 금지했기 때문에", "is_correct": False, "formula": "D2", "explanation": "거짓 진술입니다."},
                {"label": "④", "text": "도시에는 세금이 전혀 없었기 때문에", "is_correct": False, "formula": "D5", "explanation": "세금 면제와 무관합니다."},
                {"label": "⑤", "text": "모든 농작물이 하루 만에 썩어버려서", "is_correct": False, "formula": "D1", "explanation": "비과학적 허구입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 인구 구성 꺾은선그래프에서 나타나는 우리나라의 인구 변화 추이는?",
            "options": [
                {"label": "①", "text": "유소년 인구는 급감하고, 고령 인구는 가파르게 증가하고 있다.", "is_correct": True},
                {"label": "②", "text": "유소년 인구와 고령 인구 모두 똑같이 증가하고 있다.", "is_correct": False},
                {"label": "③", "text": "청장년층만 100%로 늘어나고 있다.", "is_correct": False},
                {"label": "④", "text": "시간이 지나도 인구 변화가 전혀 없다.", "is_correct": False},
                {"label": "⑤", "text": "고령 인구만 줄어들고 있다.", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "14세 이하 유소년 인구는 급감하고 65세 이상 고령 인구는 가파르게 증가하고 있습니다.", "is_correct": True},
                {"label": "②", "text": "우리나라의 인구 분포는 과거 농경 중심 사회에서", "is_correct": False},
                {"label": "③", "text": "서울과 경기도를 포함한 수도권에 전체 인구의 50% 이상이 거주하게 되었으며,", "is_correct": False},
                {"label": "④", "text": "이러한 인구 구조의 변화는 노동력 부족과 지방 소멸 위기라는", "is_correct": False},
                {"label": "⑤", "text": "농산어촌 지역은 청장년층 인구의 유출로", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "인구 변화 통계 분석문 작성",
        "guide": "이촌향도와 초고령화 현상을 엮어 한 문장으로 요약해 보세요.",
        "template": "산업화로 인한 [이촌향도]로 수도권 과밀이 심화된 가운데, 저출생과 수명 연장으로 [초고령 사회]에 진입하고 있습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "인구 통계 글은 '공간적 이동(이촌향도)'과 '연령별 구조(고령화)'를 나누어 분석해요."},
        "step1_2_drill": {"task": "유소년 인구 감소 vs 고령 인구 증가 꺾은선그래프 읽기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "우리나라는 65세 이상 인구가 20%를 넘는 초고령 사회에 진입했습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 시골 할머니 댁의 인구 변화",
        "situation": "명절에 시골 친척 댁에 방문하거나 폐교 뉴스를 볼 때",
        "parent_question": "시골 마을에 젊은 사람과 아이들이 점점 줄어드는 까닭은 무엇일까?",
        "expected_answer": "일자리와 학교를 찾아 도시로 떠나는 이촌향도와 저출생·고령화 현상 때문이래요!",
        "coaching_tip": "사회적 통계와 일상의 경험을 연결하여 국토 균형 발전의 필요성을 함께 생각해 보세요."
    }
)

# Slot 8: V2-4
slots_dict["V2-4"] = build_expository_slot(
    grade_num=5,
    subskill_code="V2-4",
    subject="실과(스마트팜 5-2)",
    unit="3. 첨단 기술과 미래 농업",
    concept="정보통신기술(ICT)이 바꾸는 미래 농업: 스마트팜의 작동 원리",
    text_structure="과정 + 비교·대조",
    structure_type_code="sequence",
    passage_title="센서와 데이터로 작물을 키우는 스마트팜",
    paragraphs=[
        "전통적인 농업은 계절과 날씨의 변화, 가뭄이나 폭우 같은 자연환경에 절대적으로 의존했습니다. 그러나 첨단 정보통신기술(ICT)과 사물인터넷(IoT)이 결합된 '스마트팜(지능형 농장)'은 실내에서 작물 재배 환경을 과학적으로 통제합니다.",
        "스마트팜의 작동은 3단계 순환 과정으로 이루어집니다. 1단계 '수집': 온습도, 이산화탄소, 일조량을 측정하는 센서가 온실 내부 환경을 실시간 측정합니다. 2단계 '분석': 수집된 빅데이터를 컴퓨터 인공지능이 분석하여 최적의 생육 조건을 계산합니다. 3단계 '제어': 분석 결과에 따라 자동으로 창문을 열거나 냉난방기를 켜고, 뿌리에 필요한 영양액을 방울방울 공급합니다.",
        "스마트팜은 기후 위기와 농촌의 일손 부족 문제를 해결하고, 1년 내내 일정한 품질의 농산물을 생산할 수 있는 지속 가능한 미래 농업의 핵심 대안으로 주목받고 있습니다."
    ],
    vocab_notes=[
        {"word": "스마트팜", "definition": "정보통신기술을 농업에 접목하여 작물의 생육 환경을 자동으로 원격 제어하는 농장"},
        {"word": "사물인터넷(IoT)", "definition": "사물에 센서와 통신 기능을 내장하여 인터넷을 통해 데이터를 주고받는 기술"}
    ],
    visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
      <h4 class="font-bold text-teal-900 mb-2">🌱 스마트팜 3단계 자동화 프로세스</h4>
      <div class="grid grid-cols-3 gap-1 text-xs text-center">
        <div class="p-1.5 bg-white rounded border border-teal-200"><strong>1. 센서 수집</strong><br>온도·습도·빛 데이터 실시간 측정</div>
        <div class="p-1.5 bg-white rounded border border-teal-200"><strong>2. AI 분석</strong><br>생육 최적 조건 계산 및 판단</div>
        <div class="p-1.5 bg-white rounded border border-teal-200"><strong>3. 자동 제어</strong><br>양액 공급, 환기, 조명 자동 조절</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v24-c1", "text": "첨단 정보통신기술(ICT)과 사물인터넷(IoT)이 결합된 '스마트팜(지능형 농장)'", "role": "스마트팜 개념", "para_idx": 0},
        {"cue_id": "g5-v24-c2", "text": "스마트팜의 작동은 3단계 순환 과정으로 이루어집니다", "role": "3단계 작동 프로세스", "para_idx": 1}
    ],
    graphic_organizer={
        "diagram_type": "자동 제어 루프",
        "steps": ["환경 센서 데이터 수집", "클라우드 AI 분석", "구동기 자동 제어(환기·양액)", "피드백 모니터링"]
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "과정 단계 세부 확인",
            "stem": "스마트팜의 작동 과정에서 '2단계(분석)'가 수행하는 구체적 역할은?",
            "target_para_idx": 1,
            "spotlight_quote": "2단계 '분석': 수집된 빅데이터를 컴퓨터 인공지능이 분석하여 최적의 생육 조건을 계산합니다.",
            "options": [
                {"label": "①", "text": "수집된 빅데이터를 인공지능이 분석하여 작물의 최적 생육 조건을 계산한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 2단계 분석의 명확한 역할입니다."},
                {"label": "②", "text": "농부가 낫을 들고 풀을 직접 벤다.", "is_correct": False, "formula": "D3", "explanation": "전통 수작업 농업입니다."},
                {"label": "③", "text": "창문을 손으로 열어 비를 맞힌다.", "is_correct": False, "formula": "D2", "explanation": "자동 제어 방식과 어긋납니다."},
                {"label": "④", "text": "작물을 모두 뽑아 시장에 내다 판다.", "is_correct": False, "formula": "D5", "explanation": "수확 후 유통 단계입니다."},
                {"label": "⑤", "text": "센서의 전원을 모두 끄고 컴퓨터를 버린다.", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "기술 도입 효과 파악",
            "stem": "전통 농업과 비교할 때 스마트팜이 지닌 가장 큰 장점은?",
            "target_para_idx": 2,
            "spotlight_quote": "스마트팜은 기후 위기와 농촌의 일손 부족 문제를 해결하고, 1년 내내 일정한 품질의 농산물을 생산할 수 있는",
            "options": [
                {"label": "①", "text": "날씨에 구애받지 않고 일손 부족을 극복하며 연중 고품질 작물을 생산할 수 있다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 스마트팜의 핵심 혁신 가치입니다."},
                {"label": "②", "text": "작물이 하룻밤 사이에 100미터 높이로 자란다.", "is_correct": False, "formula": "D6", "explanation": "동화 속 허구입니다."},
                {"label": "③", "text": "전기나 물을 전혀 쓰지 않는다.", "is_correct": False, "formula": "D4", "explanation": "전기와 용수를 정밀하게 사용합니다."},
                {"label": "④", "text": "모든 농산물이 고기 맛으로 변한다.", "is_correct": False, "formula": "D5", "explanation": "황당한 오답입니다."},
                {"label": "⑤", "text": "겨울에는 농장 문을 닫고 일하지 않는다.", "is_correct": False, "formula": "D3", "explanation": "1년 내내 생산 가능합니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 스마트팜에서 실시간으로 환경 데이터를 측정하는 핵심 장비는?",
            "options": [
                {"label": "①", "text": "온습도·이산화탄소 센서", "is_correct": True},
                {"label": "②", "text": "나무 빗자루", "is_correct": False},
                {"label": "③", "text": "재래식 물레방아", "is_correct": False},
                {"label": "④", "text": "종이 바람개비", "is_correct": False},
                {"label": "⑤", "text": "쇠스랑", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "온습도, 이산화탄소, 일조량을 측정하는 센서가 온실 내부 환경을 실시간 측정합니다.", "is_correct": True},
                {"label": "②", "text": "전통적인 농업은 계절과 날씨의 변화,", "is_correct": False},
                {"label": "③", "text": "스마트팜의 작동은 3단계 순환 과정으로", "is_correct": False},
                {"label": "④", "text": "지속 가능한 미래 농업의 핵심 대안으로", "is_correct": False},
                {"label": "⑤", "text": "분석 결과에 따라 자동으로 창문을 열거나", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "스마트팜 기술 요약문 쓰기",
        "guide": "스마트팜의 [센서 수집] ➔ [AI 분석] ➔ [자동 제어] 3단계를 연결해 보세요.",
        "template": "스마트팜은 [센서]로 환경을 측정하고, [인공지능]으로 분석하여, 영양액과 온도를 [자동으로 제어]합니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "ICT 기술 설명글은 '수집 ➔ 분석 ➔ 제어'의 3단계 흐름을 따라 읽어요."},
        "step1_2_drill": {"task": "스마트팜 3단계 장비와 기능 카드 연결하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "스마트팜은 기후 위기에 구애받지 않고 연중 작물을 생산할 수 있습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 인공지능이 농사짓는 세상",
        "situation": "마트에서 '스마트팜 딸기'나 실내 채소 재배기를 볼 때",
        "parent_question": "흙과 햇빛이 없는 건물 안에서도 딸기가 빨갛게 잘 자라는 비결은 뭘까?",
        "expected_answer": "온도와 습도를 센서로 재고 LED 빛과 영양분을 컴퓨터가 딱 맞춰 주는 스마트팜 기술 덕분이래요!",
        "coaching_tip": "전통 농업이 첨단 ICT와 만나 어떻게 미래 기술로 진화하는지 대화해 보세요."
    }
)

# Slot 9: V3-1
slots_dict["V3-1"] = build_expository_slot(
    grade_num=5,
    subskill_code="V3-1",
    subject="사회(한국사·인쇄술 5-2)",
    unit="1. 찬란한 고려의 문화",
    concept="고려의 목판 인쇄술(팔만대장경)과 금속 활자(직지) 설명문 비교",
    text_structure="비교·대조 + 분류",
    structure_type_code="comparison",
    passage_title="세계 최고의 인쇄 문화유산, 팔만대장경과 직지심체요절",
    paragraphs=[
        "고려는 세계 인쇄술의 역사를 새로 쓴 뛰어난 문화유산을 꽃피웠습니다. 하나의 나무판에 글자를 전부 새긴 '목판 인쇄술'의 정수인 '팔만대장경'과, 금속으로 글자 알갱이를 하나씩 만들어 조판한 '금속 활자 인쇄술'의 정수인 '직지심체요절(직지)'이 그 대표작입니다.",
        "팔만대장경은 몽골의 침략을 부처님의 힘으로 막아내고자 16년에 걸쳐 완성한 8만여 장의 목판입니다. 나무를 소금물에 삶고 말려 뒤틀림과 썩음을 방지한 과학적 가공 기술이 돋보입니다. 목판 인쇄는 동일한 책을 수천 권씩 대량 인쇄하기에 매우 유리하지만, 판목을 새기는 데 엄청난 시간과 노동이 들고 다른 책을 인쇄할 수 없다는 한계가 있었습니다.",
        "이를 극복한 것이 1377년 청주 흥덕사에서 인쇄된 세계 최고(最古)의 금속 활자본 '직지'입니다. 서양의 구텐베르크보다 무려 78년이나 앞선 것으로, 글자 알갱이를 자유롭게 재배열하여 여러 종류의 책을 소량 다품종으로 신속히 찍어낼 수 있는 혁신적인 정보 기술이었습니다."
    ],
    vocab_notes=[
        {"word": "팔만대장경", "definition": "고려 고종 때 몽골의 침입을 물리치기 위해 제작한 불교 경전 목판"},
        {"word": "직지심체요절", "definition": "1377년 고려에서 간행된 현존하는 세계에서 가장 오래된 금속 활자본"}
    ],
    visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">📜 목판(팔만대장경) vs 금속활자(직지) 기술 비교</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-amber-100"><th class="p-1 border border-amber-200">구분</th><th class="p-1 border border-amber-200">목판 인쇄 (팔만대장경)</th><th class="p-1 border border-amber-200">금속 활자 (직지심체요절)</th></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">제작 방식</td><td class="p-1 border border-amber-200 bg-white">판목 전체에 글자 조각</td><td class="p-1 border border-amber-200 bg-white">낱개 금속 글자 주조 후 조판</td></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">인쇄 특성</td><td class="p-1 border border-amber-200 bg-white">동일 도서 대량 인쇄에 적합</td><td class="p-1 border border-amber-200 bg-white">다양한 도서 소량 다품종 인쇄에 혁신</td></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">세계적 의의</td><td class="p-1 border border-amber-200 bg-white">완벽한 보존 과학(장경판전)</td><td class="p-1 border border-amber-200 bg-white">구텐베르크보다 78년 앞선 최고(最古) 활자</td></tr>
          </table>
        </div>""",
    hottext_cues=[
        {"cue_id": "g5-v31-c1", "text": "나무를 소금물에 삶고 말려 뒤틀림과 썩음을 방지한 과학적 가공 기술", "role": "목판 제작 과학성", "para_idx": 1},
        {"cue_id": "g5-v31-c2", "text": "서양의 구텐베르크보다 무려 78년이나 앞선 것으로, 글자 알갱이를 자유롭게 재배열하여", "role": "직지의 세계사적 위상", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "인쇄술 비교 매트릭스",
        "woodblock": "목판(팔만대장경) ➔ 동일 책 대량 인쇄 최적",
        "metal_type": "금속 활자(직지) ➔ 활자 재배치, 다품종 인쇄 혁신",
        "historical_impact": "고려 인쇄 과학의 세계적 독창성 증명"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "기술 특성 비교 대조",
            "stem": "'금속 활자 인쇄술(직지)'이 '목판 인쇄술(팔만대장경)'에 비해 가졌던 가장 혁신적인 장점은?",
            "target_para_idx": 2,
            "spotlight_quote": "글자 알갱이를 자유롭게 재배열하여 여러 종류의 책을 소량 다품종으로 신속히 찍어낼 수 있는 혁신적인 정보 기술이었습니다.",
            "options": [
                {"label": "①", "text": "글자 알갱이를 자유롭게 재배열하여 다양한 종류의 책을 신속히 인쇄할 수 있었다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 금속 활자의 핵심 혁신성입니다."},
                {"label": "②", "text": "나무를 소금물에 삶을 필요 없이 종이를 안 쓰고 쇠판에 바로 읽을 수 있었다.", "is_correct": False, "formula": "D3", "explanation": "금속 활자도 한지에 먹물로 인쇄합니다."},
                {"label": "③", "text": "서양의 구텐베르크보다 1000년 늦게 만들어져 서양 기술을 베꼈다.", "is_correct": False, "formula": "D5", "explanation": "구텐베르크보다 78년 앞섰습니다."},
                {"label": "④", "text": "한 번 찍고 나면 글자가 모두 녹아 사라졌다.", "is_correct": False, "formula": "D1", "explanation": "금속 활자는 재사용이 가능합니다."},
                {"label": "⑤", "text": "오직 부처님 불경 한 가지만 찍을 수 있었다.", "is_correct": False, "formula": "D4", "explanation": "다양한 서적을 인쇄할 수 있었습니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "역사적 사실 및 과학성 확인",
            "stem": "팔만대장경판이 700년이 넘도록 뒤틀리거나 썩지 않고 보존된 과학적 비결은?",
            "target_para_idx": 1,
            "spotlight_quote": "나무를 소금물에 삶고 말려 뒤틀림과 썩음을 방지한 과학적 가공 기술이 돋보입니다.",
            "options": [
                {"label": "①", "text": "나무를 소금물에 삶고 오랜 시간 그늘에 말려 가공했기 때문에", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 팔만대장경판 가공의 과학적 비결입니다."},
                {"label": "②", "text": "유리 상자에 넣어 냉동고에 보관했기 때문에", "is_correct": False, "formula": "D6", "explanation": "현대 냉동 기술이 아닙니다."},
                {"label": "③", "text": "나무가 아니라 100% 순금으로 만들었기 때문에", "is_correct": False, "formula": "D2", "explanation": "나무로 만든 목판입니다."},
                {"label": "④", "text": "몽골군이 대장경판을 보호해 주었기 때문에", "is_correct": False, "formula": "D4", "explanation": "몽골 침입을 막으려 만든 것입니다."},
                {"label": "⑤", "text": "바닷속 깊은 갯벌에 묻어 두었기 때문에", "is_correct": False, "formula": "D5", "explanation": "해인사 장경판전에 보관했습니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 세계 최초의 금속 활자본 '직지심체요절'이 간행된 시기와 장소는?",
            "options": [
                {"label": "①", "text": "1377년 청주 흥덕사", "is_correct": True},
                {"label": "②", "text": "1443년 한양 경복궁", "is_correct": False},
                {"label": "③", "text": "1592년 한산도 바다", "is_correct": False},
                {"label": "④", "text": "1234년 강화도 마니산", "is_correct": False},
                {"label": "⑤", "text": "1919년 탑골공원", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "이를 극복한 것이 1377년 청주 흥덕사에서 인쇄된 세계 최고(最古)의 금속 활자본 '직지'입니다.", "is_correct": True},
                {"label": "②", "text": "고려는 세계 인쇄술의 역사를 새로 쓴", "is_correct": False},
                {"label": "③", "text": "팔만대장경은 몽골의 침략을 부처님의 힘으로", "is_correct": False},
                {"label": "④", "text": "서양의 구텐베르크보다 무려 78년이나 앞선 것으로,", "is_correct": False},
                {"label": "⑤", "text": "목판 인쇄는 동일한 책을 수천 권씩 대량 인쇄하기에", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "고려 2대 인쇄술 비교문 작성",
        "guide": "팔만대장경과 직지의 기술적 차이를 한 문장으로 대조해 보세요.",
        "template": "팔만대장경은 동일한 책을 대량 인쇄하는 [목판 인쇄술]이고, 직지는 활자를 재배열하여 다양한 책을 찍어내는 [금속 활자 인쇄술]입니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "목판(동일 책 대량)과 금속활자(활자 재배치, 다품종)의 특성을 비교해요."},
        "step1_2_drill": {"task": "팔만대장경과 직지심체요절 역사적 카드 짝맞추기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "직지는 서양 구텐베르크보다 78년 앞선 현존 최고 금속활자본입니다.", "answer": "O", "reason": "유네스코 세계기록유산 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 구텐베르크보다 앞선 고려의 활자",
        "situation": "인쇄물이나 교과서를 보며 역사 이야기를 나눌 때",
        "parent_question": "서양에서는 구텐베르크가 활자를 발명했다고 자랑하는데, 우리 조상들은 어땠을까?",
        "expected_answer": "고려 시대 '직지'가 구텐베르크보다 무려 78년이나 먼저 금속 활자로 인쇄되었대요!",
        "coaching_tip": "우리 인쇄 문화유산의 세계사적 우수성에 자긍심을 가질 수 있도록 이야기해 주세요."
    }
)

print("Constructed G5 slots V2-3, V2-4, V3-1.")

# Slots 11 to 16 for Grade 5 (5 options each)

# Slot 11: V3-3
slots_dict["V3-3"] = build_expository_slot(
    grade_num=5,
    subskill_code="V3-3",
    subject="사회(국토와 자연환경 5-1)",
    unit="1. 기후 변화와 우리 생활",
    concept="우리나라의 기후 변화와 아열대화 현상 (백과사전 글 ㉮ + 기상청 인포그래픽 ㉯)",
    text_structure="인과 + 다중 문서 통합",
    structure_type_code="causal",
    passage_title="한반도의 기후 변화와 아열대화의 징후 (글 ㉮와 자료 ㉯)",
    paragraphs=[
        "[백과사전 글 ㉮] 지난 100년간 지구 온난화의 가속화로 한반도의 평균 기온은 전 지구 평균(약 1.0℃)보다 훨씬 높은 약 1.8℃나 상승했습니다. 기온 상승으로 인해 겨울철은 짧아지고 여름철은 길어졌으며, 남부 지방을 중심으로 사과와 감귤 같은 대표 농작물의 재배 가능 지역이 점차 북쪽으로 이동하고 있습니다.",
        "[기상청 인포그래픽 ㉯] 한반도 해수면 온도 변화 지도와 어획량 통계 그래프를 보면, 동해안의 수온이 2℃ 이상 상승함에 따라 한류성 어종인 명태는 거의 자취를 감추고 난류성 어종인 방어와 오징어, 아열대성 참다랑어가 대량 어획되고 있다고 수치로 입증하고 있습니다.",
        "두 자료를 교차 검증하여 종합하면, 한반도는 온난화로 인해 '육상 생태계의 농작물 북방 한계선 이동(자료 ㉮)'과 '해양 생태계의 난류성 어종 대체(자료 ㉯)'가 동시에 진행되는 '아열대 기후화'라는 거대한 환경 변화에 직면해 있음을 명확히 알 수 있습니다."
    ],
    vocab_notes=[
        {"word": "아열대화", "definition": "온대 기후 지역의 기온이 상승하여 열대 기후에 가까워지는 현상"},
        {"word": "북방 한계선", "definition": "특정한 농작물이나 식물이 정상적으로 자랄 수 있는 북쪽의 한계선"}
    ],
    visual_html="""<div class="p-3 bg-orange-50 rounded border border-orange-200">
      <h4 class="font-bold text-orange-900 mb-2">🌏 한반도 아열대화 교차 검증 매트릭스</h4>
      <table class="w-full text-xs text-center border-collapse">
        <tr class="bg-orange-100"><th class="p-1 border border-orange-200">구분</th><th class="p-1 border border-orange-200">육상 생태계 (자료 ㉮ 백과사전)</th><th class="p-1 border border-orange-200">해양 생태계 (자료 ㉯ 기상청 통계)</th></tr>
        <tr><td class="p-1 border border-orange-200 font-bold bg-white">온도 변화</td><td class="p-1 border border-orange-200 bg-white">100년간 평균 기온 약 1.8℃ 상승</td><td class="p-1 border border-orange-200 bg-white">동해안 수온 2℃ 이상 급상승</td></tr>
        <tr><td class="p-1 border border-orange-200 font-bold bg-white">생태계 변화</td><td class="p-1 border border-orange-200 bg-white">사과·감귤 재배지 북상 (강원도 사과)</td><td class="p-1 border border-orange-200 bg-white">한류성 명태 실종, 참다랑어·방어 급증</td></tr>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v33-c1", "text": "남부 지방을 중심으로 사과와 감귤 같은 대표 농작물의 재배 가능 지역이 점차 북쪽으로 이동하고 있습니다", "role": "육상 농작물 재배지 북상", "para_idx": 0},
        {"cue_id": "g5-v33-c2", "text": "한류성 어종인 명태는 거의 자취를 감추고 난류성 어종인 방어와 오징어, 아열대성 참다랑어가", "role": "해양 어종 변화 통계", "para_idx": 1}
    ],
    graphic_organizer={
        "diagram_type": "다중 문서 통합 도식",
        "source_a": "글 ㉮: 한반도 기온 1.8℃ 상승 및 농작물 재배지 북상",
        "source_b": "자료 ㉯: 동해 수온 2℃ 상승 및 명태 실종·난류 어종 급증",
        "synthesis": "육지와 바다 전역에 걸친 아열대화 현상 종합 입증"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "다중 자료 정보 통합",
            "stem": "자료 ㉮와 자료 ㉯를 종합하여 도출한 '한반도 기후 변화의 특징'으로 가장 적절한 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "두 자료를 교차 검증하여 종합하면, 한반도는 온난화로 인해 '육상 생태계의 농작물 북방 한계선 이동(자료 ㉮)'과 '해양 생태계의 난류성 어종 대체(자료 ㉯)'가",
            "options": [
                {"label": "①", "text": "육상에서는 농작물 재배지가 북상하고 해양에서는 난류성 어종이 급증하는 아열대화가 진행 중이다.", "is_correct": True, "formula": "정답", "explanation": "두 자료의 육상과 해양 데이터를 완벽하게 융합한 핵심 결론입니다."},
                {"label": "②", "text": "동해안이 얼어붙어 북극곰이 명태를 사냥하고 있다.", "is_correct": False, "formula": "D5", "explanation": "수온이 상승하여 명태가 사라졌습니다."},
                {"label": "③", "text": "사과 재배가 전면 금지되어 과일 가게가 문을 닫았다.", "is_correct": False, "formula": "D3", "explanation": "재배지가 북쪽으로 이동한 것입니다."},
                {"label": "④", "text": "기온이 내려가 겨울철이 6개월로 길어졌다.", "is_correct": False, "formula": "D4", "explanation": "겨울이 짧아졌습니다."},
                {"label": "⑤", "text": "한반도는 지구 온난화의 영향을 전혀 받지 않는 청정 지역이다.", "is_correct": False, "formula": "D1", "explanation": "지구 평균보다 1.8배 빠르게 상승했습니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "해양 생태계 인과 분석",
            "stem": "자료 ㉯에서 과거 대표 어종이었던 '명태'가 동해안에서 거의 사라진 직접적인 원인은?",
            "target_para_idx": 1,
            "spotlight_quote": "동해안의 수온이 2℃ 이상 상승함에 따라 한류성 어종인 명태는 거의 자취를 감추고",
            "options": [
                {"label": "①", "text": "동해안의 수온이 2℃ 이상 상승하여 차가운 물을 좋아하는 한류성 어종이 살 수 없어서", "is_correct": True, "formula": "정답", "explanation": "2문단에 제시된 명확한 수온 상승의 생태학적 결과입니다."},
                {"label": "②", "text": "외계인이 명태를 전부 우주로 가져가서", "is_correct": False, "formula": "D6", "explanation": "비과학적 허구입니다."},
                {"label": "③", "text": "명태가 모두 사과나무 열매로 변했기 때문에", "is_correct": False, "formula": "D2", "explanation": "황당한 오답입니다."},
                {"label": "④", "text": "어부들이 그물을 전혀 던지지 않아서", "is_correct": False, "formula": "D4", "explanation": "조업과 무관한 수온 문제입니다."},
                {"label": "⑤", "text": "동해의 물이 모두 말라붙어서", "is_correct": False, "formula": "D1", "explanation": "허위 진술입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 지난 100년간 한반도 평균 기온 상승 폭이 지닌 세계사적 특징은?",
            "options": [
                {"label": "①", "text": "약 1.8℃ 상승하여 전 지구 평균(약 1.0℃)보다 훨씬 가파르게 상승했다.", "is_correct": True},
                {"label": "②", "text": "전 지구 평균보다 10배 낮게 상승했다.", "is_correct": False},
                {"label": "③", "text": "온도가 오히려 20℃ 떨어졌다.", "is_correct": False},
                {"label": "④", "text": "세계 기상청의 측정이 불가능했다.", "is_correct": False},
                {"label": "⑤", "text": "남극의 얼음 두께와 동일했다.", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "한반도의 평균 기온은 전 지구 평균(약 1.0℃)보다 훨씬 높은 약 1.8℃나 상승했습니다.", "is_correct": True},
                {"label": "②", "text": "지난 100년간 지구 온난화의 가속화로", "is_correct": False},
                {"label": "③", "text": "기온 상승으로 인해 겨울철은 짧아지고", "is_correct": False},
                {"label": "④", "text": "기상청 인포그래픽 ㉯ 한반도 해수면 온도 변화 지도와", "is_correct": False},
                {"label": "⑤", "text": "두 자료를 교차 검증하여 종합하면,", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "기후 변화 다중 자료 통합 보고서 작성",
        "guide": "육상(자료 ㉮)과 해양(자료 ㉯)의 변화를 엮어 한반도 아열대화 보고문을 작성해 보세요.",
        "template": "기온과 수온이 상승함에 따라 육지에서는 [농작물 재배지]가 북상하고, 바다에서는 [난류성 어종]이 증가하는 아열대화가 나타나고 있습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "다중 문서 독해는 서로 다른 출처의 통계 데이터를 '공통 주제(아열대화)'로 묶어 읽어요."},
        "step1_2_drill": {"task": "육상 변화(사과 북상)와 해양 변화(명태 실종) 매트릭스 완성하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "한반도의 평균 기온 상승 속도는 전 지구 평균보다 빠릅니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 대구 사과가 강원도 양구 사과로?",
        "situation": "마트 과일 코너에서 강원도산 사과를 볼 때",
        "parent_question": "옛날엔 대구 사과가 유명했는데, 왜 요즘엔 강원도 사과가 맛있고 유명해졌을까?",
        "expected_answer": "기후 온난화로 남쪽 날씨가 너무 더워져서 사과가 잘 자라는 시원한 곳이 북쪽 강원도로 올라갔기 때문이래요!",
        "coaching_tip": "식탁 위 과일 원산지의 변화를 통해 한반도 기후 온난화를 실감 나게 체감하도록 이끌어 주세요."
    }
)

# Slot 12: W1
slots_dict["W1"] = build_expository_slot(
    grade_num=5,
    subskill_code="W1",
    subject="사회(한국사·조선 과학 5-2) / 국어",
    unit="2. 조선의 과학 문화",
    concept="독자 수준에 맞춘 ‘훈민정음(한글) 자음·모음의 과학적 창제 원리’ 3단계 계획",
    text_structure="분석 + 분류",
    structure_type_code="analysis",
    passage_title="발음 기관을 본뜬 한글의 과학적 창제 원리 계획하기",
    paragraphs=[
        "'훈민정음'을 소개하는 설명글을 쓸 때 광범위한 세종대왕의 업적 전체를 다루면 글이 산만해집니다. 따라서 [상위 분야: 조선의 문화 ➔ 중위 대상: 훈민정음 ➔ 구체적 주제: 발음 기관을 본뜬 자음의 상형과 가획 원리]라는 3단계 깔때기 모델로 주제를 정밀하게 좁혀야 합니다.",
        "독자가 초등학교 5학년 학생임을 고려하여, 기본 자음(ㄱ, ㄴ, ㅁ, ㅅ, ㅇ)이 각각 혀, 입술, 이, 목구멍의 모양을 본떠 만들어진 '상형의 원리'와, 소리가 세어짐에 따라 획을 더한 '가획의 원리(ㄱ➔ㅋ, ㄴ➔ㄷ➔ㅌ)'를 시각 단면도와 함께 설명하는 목표를 명확히 세웁니다.",
        "이처럼 독자의 사전 지식을 분석하고 핵심 원리에 집중하여 작문 계획을 세우면, 한글이 왜 세계에서 유일하게 만든 원리가 밝혀진 과학적 문자인지 독자에게 깊은 감동과 깨달음을 줄 수 있습니다."
    ],
    vocab_notes=[
        {"word": "상형의 원리", "definition": "구체적인 사물이나 발음 기관의 모양을 본떠 글자를 만든 원리"},
        {"word": "가획의 원리", "definition": "기본 글자에 획을 더하여 소리의 세기를 나타낸 원리"}
    ],
    visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
      <h4 class="font-bold text-blue-900 mb-2">🎯 훈민정음 과학성 설명글 3단계 작문 계획서</h4>
      <div class="space-y-1 text-xs">
        <div class="p-1 bg-white rounded border border-blue-200">1단계 독자 분석: 5학년 (한글의 자모 원리를 처음 체계적으로 배움)</div>
        <div class="p-1 bg-white rounded border border-blue-200">2단계 주제 좁히기: 세종 업적 ➔ 훈민정음 ➔ 발음 기관 상형과 가획 원리</div>
        <div class="p-1 bg-white rounded border border-blue-200">3단계 목표 제목: 혀와 입술을 본뜬 한글 자음의 과학적 비밀</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-w1-c1", "text": "발음 기관을 본뜬 자음의 상형과 가획 원리", "role": "구체화된 핵심 화제", "para_idx": 0},
        {"cue_id": "g5-w1-c2", "text": "소리가 세어짐에 따라 획을 더한 '가획의 원리(ㄱ➔ㅋ, ㄴ➔ㄷ➔ㅌ)'", "role": "가획의 원리 규칙", "para_idx": 1}
    ],
    graphic_organizer={
        "diagram_type": "작문 계획 깔때기",
        "audience": "초등학교 5학년 학생",
        "focus": "발음 기관 상형(ㄱ,ㄴ,ㅁ,ㅅ,ㅇ) 및 가획 원리",
        "visual_aid": "입안 발음 기관 단면 삽화 기획"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "작문 계획 전략 파악",
            "stem": "글쓴이가 '훈민정음 설명글'을 계획할 때 세종대왕의 모든 업적이 아닌 '상형과 가획 원리'로 주제를 좁힌 까닭은?",
            "target_para_idx": 0,
            "spotlight_quote": "광범위한 세종대왕의 업적 전체를 다루면 글이 산만해집니다. 따라서 [상위 분야: 조선의 문화 ➔ 중위 대상: 훈민정음 ➔ 구체적 주제: 발음 기관을 본뜬 자음의 상형과 가획 원리]라는 3단계 깔때기 모델로",
            "options": [
                {"label": "①", "text": "글이 산만해지는 것을 막고 한글 자음의 과학적 창제 원리에 집중하여 깊이 있게 전달하기 위해", "is_correct": True, "formula": "정답", "explanation": "1문단에 서술된 주제 좁히기의 명확한 작문 목적입니다."},
                {"label": "②", "text": "세종대왕의 다른 업적을 전부 깎아내리기 위해", "is_correct": False, "formula": "D3", "explanation": "부정적 왜곡입니다."},
                {"label": "③", "text": "한글을 쓰지 말고 한자를 쓰자고 주장하기 위해", "is_correct": False, "formula": "D5", "explanation": "글의 취지와 정반대입니다."},
                {"label": "④", "text": "독자가 글을 읽지 못하게 암호로 감추기 위해", "is_correct": False, "formula": "D1", "explanation": "소통 목적과 어긋납니다."},
                {"label": "⑤", "text": "글자 수를 줄여 1분 만에 끝내기 위해", "is_correct": False, "formula": "D4", "explanation": "질적 목적이 아닌 단순 성급함입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "창제 원리 세부 확인",
            "stem": "글에서 소개한 훈민정음 자음의 '가획의 원리'에 대한 설명으로 바른 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "소리가 세어짐에 따라 획을 더한 '가획의 원리(ㄱ➔ㅋ, ㄴ➔ㄷ➔ㅌ)'를",
            "options": [
                {"label": "①", "text": "기본 글자에 소리가 세어짐에 따라 획을 더하여 거센소리를 나타냈다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 가획 원리의 과학적 규칙입니다."},
                {"label": "②", "text": "외국 글자의 획을 가위로 오려 붙였다.", "is_correct": False, "formula": "D2", "explanation": "독창적 창제 원리와 모순됩니다."},
                {"label": "③", "text": "모양을 예쁘게 만들기 위해 아무렇게나 줄을 그었다.", "is_correct": False, "formula": "D6", "explanation": "음성학적 체계성을 무시한 오답입니다."},
                {"label": "④", "text": "획을 뺄수록 소리가 더 커진다.", "is_correct": False, "formula": "D4", "explanation": "획을 더할수록 소리가 거세집니다."},
                {"label": "⑤", "text": "모음 글자에만 적용되는 규칙이다.", "is_correct": False, "formula": "D3", "explanation": "자음 창제 원리입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 한글 기본 자음(ㄱ, ㄴ, ㅁ, ㅅ, ㅇ)의 모양을 본뜬 대상은?",
            "options": [
                {"label": "①", "text": "발음할 때 움직이는 사람의 입안 발음 기관(혀, 입술, 이, 목구멍)", "is_correct": True},
                {"label": "②", "text": "산과 바다, 강의 자연 풍경", "is_correct": False},
                {"label": "③", "text": "궁궐 건물의 지붕 처마", "is_correct": False},
                {"label": "④", "text": "고대 동물의 뼈 모양", "is_correct": False},
                {"label": "⑤", "text": "칼과 활 같은 무기", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "기본 자음(ㄱ, ㄴ, ㅁ, ㅅ, ㅇ)이 각각 혀, 입술, 이, 목구멍의 모양을 본떠 만들어진 '상형의 원리'와,", "is_correct": True},
                {"label": "②", "text": "'훈민정음'을 소개하는 설명글을 쓸 때", "is_correct": False},
                {"label": "③", "text": "한글이 왜 세계에서 유일하게 만든 원리가 밝혀진", "is_correct": False},
                {"label": "④", "text": "소리가 세어짐에 따라 획을 더한 '가획의 원리'", "is_correct": False},
                {"label": "⑤", "text": "독자의 사전 지식을 분석하고 핵심 원리에 집중하여", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "훈민정음 자음 창제 계획서 작성",
        "guide": "상형과 가획의 원리를 연결하는 한글 설명 계획을 한 문장으로 써 보세요.",
        "template": "한글 자음은 발음 기관을 본뜬 [상형의 원리]로 기본자를 만들고, 소리가 세어짐에 따라 획을 더하는 [가획의 원리]로 체계화했습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "작문 계획 시 '독자 분석'과 '주제 좁히기(상형·가획)'의 연결을 확인해요."},
        "step1_2_drill": {"task": "기본 자음(상형)과 가획자(ㅋ, ㄷ, ㅌ, ㅂ, ㅍ) 짝짓기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "한글 자음은 발음 기관의 모양을 본떠 만든 상형의 원리가 적용되었습니다.", "answer": "O", "reason": "훈민정음 해례본의 명확한 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 발음 기관이 만든 글자, 한글",
        "situation": "한글날 즈음이나 아이가 글씨를 쓸 때",
        "parent_question": "'ㄱ'을 소리 낼 때 혀뿌리가 어디에 닿을까? 그 모양이 'ㄱ'과 닮았을까?",
        "expected_answer": "'그' 소리를 낼 때 혀뿌리가 목구멍을 막는 모양을 본떠서 만든 게 'ㄱ'이래요!",
        "coaching_tip": "실제 입을 벌리고 혀의 위치를 느껴보며 한글의 과학적 우수성을 감탄하게 해 주세요."
    }
)

# Slot 13: W2
slots_dict["W2"] = build_expository_slot(
    grade_num=5,
    subskill_code="W2",
    subject="실과·도덕(저작권 5-2)",
    unit="3. 정보 윤리와 창작",
    concept="창작자의 권리 ‘저작권’과 자유이용허락표시(CCL) 설명 자료 수집·선별",
    text_structure="분류·분석",
    structure_type_code="classification",
    passage_title="창작자를 보호하고 공유를 넓히는 저작권과 CCL",
    paragraphs=[
        "인터넷에서 글, 사진, 음악, 영상 콘텐츠를 손쉽게 복사하고 공유할 수 있는 디지털 시대에 타인의 창작물을 올바르게 존중하는 '저작권(Copyright)' 보호는 매우 중요한 시민 윤리입니다. 저작권이란 인간의 사상이나 감정을 표현한 창작물에 대해 창작자가 가지는 독점적 권리를 말합니다.",
        "출처를 밝히지 않고 인터넷 이미지나 글을 무단 복제하여 게시하는 것은 엄연한 저작권 침해이자 표절에 해당합니다. 하지만 모든 자료 이용을 금지하면 지식의 발전이 저해될 수 있으므로, 창작자가 일정한 조건 아래 자유로운 이용을 허락하는 '자유이용허락표시(CCL: Creative Commons License)'가 널리 쓰이고 있습니다.",
        "CCL 마크에는 '저작자 표시(BY)', '비영리(NC)', '변경 금지(ND)', '동일조건변경허락(SA)'의 네 가지 핵심 조건 기호가 있습니다. 설명글을 집필하기 위해 자료를 수집할 때는 무료 이미지 검색 누리집에서 이러한 CCL 마크의 조건을 정확히 확인하고 선별하는 능력이 필수적입니다."
    ],
    vocab_notes=[
        {"word": "저작권", "definition": "문학, 학술, 예술 등 저작물에 대해 저작자가 가지는 배타적 권리"},
        {"word": "자유이용허락표시(CCL)", "definition": "저작권자가 자신의 저작물에 대해 일정한 이용 조건을 명시하여 공유를 허락하는 표준 표시"}
    ],
    visual_html="""<div class="p-3 bg-purple-50 rounded border border-purple-200">
      <h4 class="font-bold text-purple-900 mb-2">🏷️ CCL 4대 조건 기호와 이용 수칙</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-1.5 bg-white rounded border border-purple-100">👤 <strong>BY (저작자 표시):</strong> 저작자의 이름과 출처를 반드시 표기</div>
        <div class="p-1.5 bg-white rounded border border-purple-100">💲 <strong>NC (비영리):</strong> 영리적(상업적) 목적으로 이용 불가</div>
        <div class="p-1.5 bg-white rounded border border-purple-100">🚫 <strong>ND (변경 금지):</strong> 저작물을 바꾸거나 편집하지 않고 원본대로 이용</div>
        <div class="p-1.5 bg-white rounded border border-purple-100">🔄 <strong>SA (동일조건 변경허락):</strong> 2차 저작물 작성 시 동일한 CCL 조건 적용</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-w2-c1", "text": "출처를 밝히지 않고 인터넷 이미지나 글을 무단 복제하여 게시하는 것은 엄연한 저작권 침해이자 표절", "role": "저작권 침해의 위험성", "para_idx": 1},
        {"cue_id": "g5-w2-c2", "text": "CCL 마크에는 '저작자 표시(BY)', '비영리(NC)', '변경 금지(ND)', '동일조건변경허락(SA)'의 네 가지 핵심 조건", "role": "CCL 4대 기호 분석", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "저작권 활용 매트릭스",
        "copyright_law": "저작권법 기본 원칙 (무단 복제 금지)",
        "ccl_solution": {
            "BY": "출처 표기",
            "NC": "비상업적 이용",
            "ND": "원본 유지",
            "SA": "동일 라이선스 배포"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "조건 기호 세부 확인",
            "stem": "CCL 조건 기호 중 '저작물을 상업적·영리적 목적으로 판매하여 돈을 버는 데 쓸 수 없음'을 나타내는 기호는?",
            "target_para_idx": 2,
            "spotlight_quote": "'저작자 표시(BY)', '비영리(NC)', '변경 금지(ND)', '동일조건변경허락(SA)'",
            "options": [
                {"label": "①", "text": "비영리 (NC)", "is_correct": True, "formula": "정답", "explanation": "2문단과 3문단에 명시된 비영리 조건(NC: Non-Commercial)입니다."},
                {"label": "②", "text": "저작자 표시 (BY)", "is_correct": False, "formula": "D3", "explanation": "출처 표기 조건입니다."},
                {"label": "③", "text": "변경 금지 (ND)", "is_correct": False, "formula": "D2", "explanation": "편집 금지 조건입니다."},
                {"label": "④", "text": "무조건 삭제 (DL)", "is_correct": False, "formula": "D1", "explanation": "존재하지 않는 기호입니다."},
                {"label": "⑤", "text": "동일조건변경허락 (SA)", "is_correct": False, "formula": "D4", "explanation": "동일 라이선스 적용 조건입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "자료 수집 윤리 평가",
            "stem": "설명글 작성을 위해 인터넷 자료를 수집할 때 가장 올바른 윤리적 태도는?",
            "target_para_idx": 2,
            "spotlight_quote": "무료 이미지 검색 누리집에서 이러한 CCL 마크의 조건을 정확히 확인하고 선별하는 능력이 필수적입니다.",
            "options": [
                {"label": "①", "text": "CCL 마크의 조건을 꼼꼼히 확인하고 출처와 저작자를 정확히 밝혀 인용한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 제시된 올바른 저작권 준수 및 자료 수집 수칙입니다."},
                {"label": "②", "text": "남의 글을 복사한 뒤 자기가 직접 쓴 글인 것처럼 이름을 바꾼다.", "is_correct": False, "formula": "D5", "explanation": "심각한 표절 범죄입니다."},
                {"label": "③", "text": "워터마크가 박힌 유료 사진을 포토샵으로 지워 몰래 쓴다.", "is_correct": False, "formula": "D6", "explanation": "명백한 저작권 침해입니다."},
                {"label": "④", "text": "인터넷에 있는 모든 자료는 누구든 마음대로 팔아도 된다고 생각한다.", "is_correct": False, "formula": "D3", "explanation": "비영리 조건 등에 위배됩니다."},
                {"label": "⑤", "text": "출처를 밝히면 창피하므로 일부러 감춘다.", "is_correct": False, "formula": "D4", "explanation": "비윤리적 행위입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 저작자가 자신의 창작물에 CCL을 표시하여 공개하는 궁극적인 이유는?",
            "options": [
                {"label": "①", "text": "자신의 권리를 지키면서도 지식과 문화가 자유롭게 공유되도록 돕기 위해", "is_correct": True},
                {"label": "②", "text": "모든 책의 출판을 중단시키기 위해", "is_correct": False},
                {"label": "③", "text": "컴퓨터 바이러스를 퍼뜨리기 위해", "is_correct": False},
                {"label": "④", "text": "인터넷 사용료를 비싸게 청구하기 위해", "is_correct": False},
                {"label": "⑤", "text": "스마트폰을 고장 내기 위해", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "창작자가 일정한 조건 아래 자유로운 이용을 허락하는 '자유이용허락표시(CCL)'가 널리 쓰이고 있습니다.", "is_correct": True},
                {"label": "②", "text": "인터넷에서 글, 사진, 음악, 영상 콘텐츠를", "is_correct": False},
                {"label": "③", "text": "출처를 밝히지 않고 인터넷 이미지나 글을 무단 복제하여", "is_correct": False},
                {"label": "④", "text": "CCL 마크에는 '저작자 표시(BY)', '비영리(NC)',", "is_correct": False},
                {"label": "⑤", "text": "설명글을 집필하기 위해 자료를 수집할 때는", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "저작권 및 CCL 활용 메모 작성",
        "guide": "자료를 수집할 때 지켜야 할 CCL 이용 수칙을 한 문장으로 써 보세요.",
        "template": "타인의 창작물을 이용할 때는 [CCL 조건]을 확인하여 [출처]를 명확히 밝히고 저작자의 권리를 존중해야 합니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "저작권(무단복제 금지)과 CCL 4대 기호(BY, NC, ND, SA)를 분석해요."},
        "step1_2_drill": {"task": "CCL 기호(BY, NC, ND, SA) 의미 짝맞춤 훈련"},
        "step3_vaccine": {"ox_quiz": [{"statement": "인터넷 자료를 인용할 때는 반드시 출처와 저작자를 밝혀야 합니다.", "answer": "O", "reason": "정보 윤리의 필수 원칙입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 숙제할 때 사진 가져오기",
        "situation": "아이가 학교 발표 숙제로 인터넷 사진을 복사할 때",
        "parent_question": "인터넷에 뜬 멋진 사진을 숙제에 넣을 때 그냥 가져와도 될까, 출처를 밝혀야 할까?",
        "expected_answer": "다른 사람이 정성껏 찍은 저작물이니까, 무료 공유(CCL)인지 확인하고 출처를 꼭 써야 해요!",
        "coaching_tip": "어릴 때부터 타인의 저작권을 존중하고 출처를 표기하는 정직한 디지털 윤리를 길러 주세요."
    }
)

# Slot 14: W3
slots_dict["W3"] = build_expository_slot(
    grade_num=5,
    subskill_code="W3",
    subject="과학(식물의 구조와 기능 5-1)",
    unit="2. 식물의 세계와 작용",
    concept="식물의 기관별(뿌리·줄기·잎·꽃) 구조와 광합성·증산작용 과정 다층 개요 짜기",
    text_structure="분석(기관 구조) + 과정(광합성·증산작용)",
    structure_type_code="analysis",
    passage_title="식물의 각 기관이 펼치는 놀라운 생명 공학 개요 설계",
    paragraphs=[
        "식물은 이동할 수 없지만 뿌리, 줄기, 잎, 꽃과 열매라는 고도로 분업화된 기관들을 유기적으로 결합하여 생명을 유지합니다. 식물의 생명 활동을 설명하는 4문단 보고서를 집필하기 위해 '다층 개요(Multi-level Outline)'를 정밀하게 설계합니다.",
        "[처음]에는 햇빛과 흙의 양분으로 스스로 양분을 만드는 식물의 위대함을 소개합니다. [가운데 1: 흡수와 운반]에는 뿌리의 물 흡수(삼투 현상)와 줄기의 관다발(물관과 체관) 구조를 분석합니다. [가운데 2: 생산과 조절]에는 잎의 엽록체에서 일어나는 '광합성'과 기공을 통해 수분을 배출해 물 상승을 이끄는 '증산작용'의 과정을 연계 설명합니다. [끝]에는 식물이 지구 산소를 공급하는 생태적 가치로 결론을 맺습니다.",
        "이처럼 기관의 구조적 분석(상위)과 생리적 과정(하위)을 결합한 다층 개요를 작성하면, 복잡한 생명 과학 메커니즘을 흐트러짐 없이 논리정연하게 서술할 수 있습니다."
    ],
    vocab_notes=[
        {"word": "광합성", "definition": "식물이 빛에너지를 이용하여 이산화탄소와 물로부터 포도당과 산소를 만드는 작용"},
        {"word": "증산작용", "definition": "잎의 기공을 통해 식물체 내부의 수분이 수증기 형태로 공기 중에 배출되는 현상"}
    ],
    visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
      <h4 class="font-bold text-emerald-900 mb-2">🌿 식물 생명 활동 다층 개요 설계도</h4>
      <div class="space-y-1 text-xs">
        <div class="p-1 bg-white rounded border border-emerald-200"><strong>[처음]</strong> 식물의 독립영양 생활과 생태적 중요성</div>
        <div class="p-1 bg-white rounded border border-emerald-200"><strong>[가운데 1]</strong> 뿌리털의 수분 흡수 ➔ 줄기 물관을 통한 상승 (구조 분석)</div>
        <div class="p-1 bg-white rounded border border-emerald-200"><strong>[가운데 2]</strong> 잎의 광합성(양분 생산) + 기공의 증산작용(수분 견인력) (과정)</div>
        <div class="p-1 bg-white rounded border border-emerald-200"><strong>[끝]</strong> 지구 산소 공급원으로서 식물의 가치 요약</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-w3-c1", "text": "줄기의 관다발(물관과 체관) 구조를 분석합니다", "role": "가운데 1 개요 요소", "para_idx": 1},
        {"cue_id": "g5-w3-c2", "text": "잎의 엽록체에서 일어나는 '광합성'과 기공을 통해 수분을 배출해 물 상승을 이끄는 '증산작용'", "role": "가운데 2 핵심 과정", "para_idx": 1}
    ],
    graphic_organizer={
        "diagram_type": "다층 개요 구조도",
        "level1": "식물의 구조와 기능",
        "subsections": {
            "처음": "식물의 독립영양 소개",
            "가운데1 (흡수·운반)": "뿌리(물 흡수) + 줄기(물관·체관)",
            "가운데2 (생산·조절)": "잎(광합성 양분 합성) + 기공(증산작용)",
            "끝": "생태계 산소 공급 기여 및 맺음말"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "개요 다층 구조 분석",
            "stem": "글쓴이가 설계한 개요에서 [가운데 2]에 배치할 핵심 설명 내용은?",
            "target_para_idx": 1,
            "spotlight_quote": "[가운데 2: 생산과 조절]에는 잎의 엽록체에서 일어나는 '광합성'과 기공을 통해 수분을 배출해 물 상승을 이끄는 '증산작용'의 과정을 연계 설명합니다.",
            "options": [
                {"label": "①", "text": "잎의 엽록체 광합성(양분 생산)과 기공의 증산작용(수분 상승)", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 [가운데 2]의 핵심 내용입니다."},
                {"label": "②", "text": "뿌리의 삼투 현상과 줄기의 관다발 구조 분석", "is_correct": False, "formula": "D3", "explanation": "[가운데 1]에 배치된 내용입니다."},
                {"label": "③", "text": "꽃집에서 화초를 저렴하게 구입하는 방법", "is_correct": False, "formula": "D5", "explanation": "과학적 개요와 동떨어진 오답입니다."},
                {"label": "④", "text": "지구 온난화로 사막이 늘어나는 현상", "is_correct": False, "formula": "D4", "explanation": "주제와 무관합니다."},
                {"label": "⑤", "text": "공룡이 식물을 먹고 멸종한 사건", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "생태 원리 세부 확인",
            "stem": "잎의 '증산작용'이 식물 전체에 미치는 가장 중요한 기능은?",
            "target_para_idx": 1,
            "spotlight_quote": "기공을 통해 수분을 배출해 물 상승을 이끄는 '증산작용'",
            "options": [
                {"label": "①", "text": "잎에서 물을 증발시켜 뿌리로부터 물이 높이 끌어올려지도록 돕는다.", "is_correct": True, "formula": "정답", "explanation": "증산작용의 수분 견인력 기능입니다."},
                {"label": "②", "text": "뿌리를 썩게 만들어 식물을 쓰러뜨린다.", "is_correct": False, "formula": "D2", "explanation": "부정적 왜곡입니다."},
                {"label": "③", "text": "빛을 차단하여 식물을 잠재운다.", "is_correct": False, "formula": "D4", "explanation": "기능과 무관합니다."},
                {"label": "④", "text": "줄기를 금으로 바꾼다.", "is_correct": False, "formula": "D6", "explanation": "허구적 오답입니다."},
                {"label": "⑤", "text": "흙 속의 돌을 부순다.", "is_correct": False, "formula": "D1", "explanation": "뿌리의 역할이 아닙니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 줄기 속에서 물과 무기양분이 이동하는 통로의 이름은?",
            "options": [
                {"label": "①", "text": "물관", "is_correct": True},
                {"label": "②", "text": "체관", "is_correct": False},
                {"label": "③", "text": "숨관", "is_correct": False},
                {"label": "④", "text": "혈관", "is_correct": False},
                {"label": "⑤", "text": "기공", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "줄기의 관다발(물관과 체관) 구조를 분석합니다.", "is_correct": True},
                {"label": "②", "text": "식물은 이동할 수 없지만 뿌리, 줄기, 잎, 꽃과 열매라는", "is_correct": False},
                {"label": "③", "text": "잎의 엽록체에서 일어나는 '광합성'과", "is_correct": False},
                {"label": "④", "text": "지구 산소를 공급하는 생태적 가치로", "is_correct": False},
                {"label": "⑤", "text": "식물의 생명 활동을 설명하는 4문단 보고서를", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "식물 생명 활동 다층 개요 작성",
        "guide": "흡수와 생산의 두 축을 살려 가운데 문단의 다층 개요를 작성해 보세요.",
        "template": "[가운데 1]: 뿌리의 흡수와 줄기의 [물관·체관] / [가운데 2]: 잎의 [광합성]과 기공의 [증산작용]"
    },
    prescription_clinic={
        "step0_remedial": {"rule": "다층 개요는 상위 범주(구조 분석 vs 과정)와 하위 내용을 위계적으로 배치해요."},
        "step1_2_drill": {"task": "식물 기관별 역할(뿌리, 줄기, 잎) 다층 개요 카드 배열하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "증산작용은 식물체 내의 물을 끌어올리는 원동력이 됩니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 높은 나무 꼭대기까지 물이 올라가는 힘",
        "situation": "키가 큰 가로수나 화분의 잎을 바라볼 때",
        "parent_question": "아파트 5층 높이의 큰 나무는 펌프도 없는데 어떻게 뿌리의 물을 꼭대기 잎까지 올릴까?",
        "expected_answer": "잎에서 물을 수증기로 뿜어내는 '증산작용'이 빨대처럼 물을 위로 쭉쭉 잡아당기기 때문이래요!",
        "coaching_tip": "식물의 놀라운 생명 공학 메커니즘을 일상 속 호기심으로 연결해 주세요."
    }
)

# Slot 15: W4
slots_dict["W4"] = build_expository_slot(
    grade_num=5,
    subskill_code="W4",
    subject="과학(물체의 운동 5-2)",
    unit="3. 물체의 속력과 안전",
    concept="물체의 속력 비교와 빗길에서 자동차 제동거리가 길어지는 과학적 원리",
    text_structure="정의·비교 + 인과",
    structure_type_code="causal",
    passage_title="물체의 속력과 빗길 제동거리가 증가하는 물리 법칙",
    paragraphs=[
        "물체가 일정한 시간 동안 이동한 거리를 '속력'이라고 하며, 단위로는 m/s나 km/h를 사용합니다. 같은 거리를 이동할 때 걸린 시간이 짧을수록, 또는 같은 시간 동안 이동한 거리가 길수록 속력이 빠릅니다. 자동차의 속력과 제동거리에 관한 안전 보고서를 집필할 때는 도표 지시문과 객관적 인과 관계를 명확히 제시해야 합니다.",
        "달리는 자동차가 브레이크를 밟았을 때 완전히 멈출 때까지 이동한 거리를 '제동거리'라고 합니다. 제동거리는 자동차의 속력의 제곱에 비례하여 증가하므로, 속력이 2배 빨라지면 제동거리는 약 4배나 급증합니다.",
        "<표 1>의 '노면 상태별 제동거리 비교표'에서 확인할 수 있듯이, 비가 내리는 젖은 도로에서는 타이어와 도로 사이의 마찰력이 크게 감소하여 마른 도로보다 제동거리가 1.5배 이상 길어집니다. 따라서 빗길에서는 반드시 20% 이상 감속 운행해야 사고를 예방할 수 있습니다."
    ],
    vocab_notes=[
        {"word": "속력", "definition": "물체의 빠르기를 나타내는 양으로, 이동 거리를 걸린 시간으로 나눈 값"},
        {"word": "제동거리", "definition": "자동차가 브레이크를 작동한 순간부터 완전히 정지할 때까지 진행한 거리"},
        {"word": "마찰력", "definition": "두 물체의 접촉면에서 물체의 운동을 방해하는 힘"}
    ],
    visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
      <h4 class="font-bold text-red-900 mb-2">🚗 <표 1> 속력 및 노면 상태별 자동차 제동거리 비교표</h4>
      <table class="w-full text-xs text-center border-collapse">
        <tr class="bg-red-100"><th class="p-1 border border-red-200">주행 속력</th><th class="p-1 border border-red-200">마른 도로 제동거리</th><th class="p-1 border border-red-200">젖은 도로(빗길) 제동거리</th><th class="p-1 border border-red-200">위험도</th></tr>
        <tr><td class="p-1 border border-red-200 font-bold bg-white">시속 50km</td><td class="p-1 border border-red-200 bg-white">약 12m</td><td class="p-1 border border-red-200 bg-white">약 19m (+58%)</td><td class="p-1 border border-red-200 bg-white">주의</td></tr>
        <tr><td class="p-1 border border-red-200 font-bold bg-white">시속 100km</td><td class="p-1 border border-red-200 bg-white">약 42m</td><td class="p-1 border border-red-200 bg-white">약 67m (+60%)</td><td class="p-1 border border-red-200 bg-white">매우 위험</td></tr>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-w4-c1", "text": "제동거리는 자동차의 속력의 제곱에 비례하여 증가하므로, 속력이 2배 빨라지면 제동거리는 약 4배나 급증합니다", "role": "속력과 제동거리 물리 법칙", "para_idx": 1},
        {"cue_id": "g5-w4-c2", "text": "<표 1>의 '노면 상태별 제동거리 비교표'에서 확인할 수 있듯이", "role": "도표 지시문 활용", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "물리 인과 분석도",
        "speed_factor": "속력 2배 ➔ 제동거리 4배 급증 (제곱 비례)",
        "weather_factor": "빗길 수막 현상 ➔ 마찰력 감소 ➔ 제동거리 1.5배 연장",
        "action": "빗길 20% 이상 감속 운전 필수"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "물리 법칙 세부 확인",
            "stem": "자동차의 주행 속력이 2배로 빨라졌을 때 제동거리에 일어나는 물리적 변화는?",
            "target_para_idx": 1,
            "spotlight_quote": "제동거리는 자동차의 속력의 제곱에 비례하여 증가하므로, 속력이 2배 빨라지면 제동거리는 약 4배나 급증합니다.",
            "options": [
                {"label": "①", "text": "속력의 제곱에 비례하여 제동거리가 약 4배로 급증한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 속력과 제동거리의 물리적 법칙입니다."},
                {"label": "②", "text": "제동거리가 절반으로 줄어들어 즉시 멈춘다.", "is_correct": False, "formula": "D3", "explanation": "정반대 위험한 오답입니다."},
                {"label": "③", "text": "속력과 상관없이 언제나 정확히 1미터만 이동한다.", "is_correct": False, "formula": "D1", "explanation": "허구적 오답입니다."},
                {"label": "④", "text": "자동차가 하늘로 날아오른다.", "is_correct": False, "formula": "D5", "explanation": "비과학적 허구입니다."},
                {"label": "⑤", "text": "타이어의 바퀴가 사각형으로 변한다.", "is_correct": False, "formula": "D6", "explanation": "엉뚱한 오답입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "도표 인용 및 안전 원리",
            "stem": "비 오는 날 도로에서 자동차의 제동거리가 마른 도로보다 길어지는 직접적 원인은?",
            "target_para_idx": 2,
            "spotlight_quote": "비가 내리는 젖은 도로에서는 타이어와 도로 사이의 마찰력이 크게 감소하여",
            "options": [
                {"label": "①", "text": "물기로 인해 타이어와 도로 표면 사이의 마찰력이 크게 감소했기 때문에", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 마찰력 저하의 직접적 인과 요인입니다."},
                {"label": "②", "text": "빗물이 자동차의 엔진을 얼려버렸기 때문에", "is_correct": False, "formula": "D4", "explanation": "엔진 동력과 무관한 제동 마찰 문제입니다."},
                {"label": "③", "text": "운전자가 앞을 보지 않고 눈을 감아서", "is_correct": False, "formula": "D2", "explanation": "물리적 마찰력 원인입니다."},
                {"label": "④", "text": "비가 올 때는 도로의 신호등이 모두 꺼지기 때문에", "is_correct": False, "formula": "D5", "explanation": "신호등과 무관합니다."},
                {"label": "⑤", "text": "자동차가 물에 떠서 배로 변했기 때문에", "is_correct": False, "formula": "D6", "explanation": "수막현상의 과장된 오답입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 빗길에서 교통사고를 예방하기 위해 지켜야 할 가장 중요한 운전 수칙은?",
            "options": [
                {"label": "①", "text": "마른 도로보다 속력을 20% 이상 감속하여 안전거리를 확보한다.", "is_correct": True},
                {"label": "②", "text": "비가 올수록 최고 속도로 가속하여 빨리 벗어난다.", "is_correct": False},
                {"label": "③", "text": "브레이크 페달을 발로 차지 않고 손으로 당긴다.", "is_correct": False},
                {"label": "④", "text": "자동차의 와이퍼를 떼어낸다.", "is_correct": False},
                {"label": "⑤", "text": "타이어에 기름을 칠한다.", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "따라서 빗길에서는 반드시 20% 이상 감속 운행해야 사고를 예방할 수 있습니다.", "is_correct": True},
                {"label": "②", "text": "물체가 일정한 시간 동안 이동한 거리를 '속력'이라고 하며,", "is_correct": False},
                {"label": "③", "text": "달리는 자동차가 브레이크를 밟았을 때", "is_correct": False},
                {"label": "④", "text": "<표 1>의 '노면 상태별 제동거리 비교표'에서 확인할 수 있듯이,", "is_correct": False},
                {"label": "⑤", "text": "제동거리는 자동차의 속력의 제곱에 비례하여", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "제동거리 안전 보고서 집필",
        "guide": "도표 지시문('<표 1>에서 보듯이')과 감속 원리를 결합하여 한 문장으로 써 보세요.",
        "template": "<표 1>에서 보듯이 빗길에서는 [마찰력 감소]로 제동거리가 급증하므로, 반드시 [20% 이상 감속] 운행해야 합니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "보고서 집필 시 객관적 데이터 표(<표 1>)를 명시적으로 인용해 서술해요."},
        "step1_2_drill": {"task": "속력 2배 ➔ 제동거리 4배, 빗길 마찰력 감소 인과 도식 완성"},
        "step3_vaccine": {"ox_quiz": [{"statement": "빗길에서는 마찰력이 감소하여 제동거리가 길어집니다.", "answer": "O", "reason": "교통안전 물리 법칙입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 비 오는 날 자동차 감속의 비밀",
        "situation": "비 오는 날 가족과 함께 차를 타고 이동할 때",
        "parent_question": "비 오는 날에는 왜 아빠가 평소보다 속도를 줄이고 차간 거리를 넓힐까?",
        "expected_answer": "빗물 때문에 타이어 마찰력이 떨어져서 브레이크를 밟아도 미끄러지는 제동거리가 훨씬 길어지기 때문이래요!",
        "coaching_tip": "실제 주행 상황에서 물리학의 마찰력과 안전거리 원리를 체감하도록 대화해 주세요."
    }
)

# Slot 16: W5
slots_dict["W5"] = build_expository_slot(
    grade_num=5,
    subskill_code="W5",
    subject="사회(한국사·문화유산 5-1)",
    unit="2. 삼국과 통일신라의 문화",
    concept="신라의 과학 유산 ‘석굴암’과 ‘첨성대’의 건축 원리 설명문 3단계 정밀 퇴고",
    text_structure="분석·인과",
    structure_type_code="analysis",
    passage_title="천 년의 신비를 간직한 석굴암의 건축 과학 퇴고하기",
    paragraphs=[
        "통일 신라 경덕왕 때 창건된 토함산의 '석굴암'은 돌을 짜 맞춘 돔 형태의 인공 석굴로, 정밀한 수학과 천문학, 습도 조절 과학이 결합된 세계 유일의 석조 사원입니다. 학생이 작성한 석굴암 설명문 초고를 3단계 점검 기준에 맞추어 퇴고해야 합니다.",
        "첫째, 내용 면에서 지하수가 차가운 바닥 암반을 흐르며 결로 현상을 유도해 본존불에 이슬이 맺히지 않게 한 '자연 습도 조절 원리'가 바르게 기술되었는지 점검합니다. 둘째, 조직 면에서 '외부 전실 ➔ 통로(비도) ➔ 둥근 본실(원형 주실)'이라는 공간적 진입 순서와 수학적 비례(1:√2)가 통일성 있게 전개되었는지 확인합니다.",
        "셋째, 표현 면에서 '비록 신라인들의 기술이 뛰어났지만 결코 결로 현상이 일어나지 않았다'처럼 부사어 '결코'와 호응하지 않는 문맥 비문을 표준 교정부호로 바로잡습니다. 편견 없는 객관적 어조와 정확한 용어로 퇴고할 때 조상의 과학적 지혜가 생생히 살아납니다."
    ],
    vocab_notes=[
        {"word": "결로 현상", "definition": "공기 중의 수증기가 차가운 물체 표면에 닿아 물방울로 맺히는 현상"},
        {"word": "원형 주실", "definition": "석굴암에서 본존불이 모셔져 있는 돔 형태의 둥근 방"}
    ],
    visual_html="""<div class="p-3 bg-stone-50 rounded border border-stone-200">
      <h4 class="font-bold text-stone-900 mb-2">🏛️ 석굴암 자연 환기·제습 과학 구조도</h4>
      <div class="space-y-1 text-xs">
        <div class="p-1 bg-white rounded border border-stone-200"><strong>차가운 바닥 암반수:</strong> 바닥 온도를 낮춰 수증기가 바닥에만 응결되게 유도</div>
        <div class="p-1 bg-white rounded border border-stone-200"><strong>본존불 보호:</strong> 본존불 표면에는 결로(이슬)가 맺히지 않고 뽀송하게 유지</div>
        <div class="p-1 bg-white rounded border border-stone-200"><strong>자연 통풍 돔:</strong> 틈새 환기구로 공기가 순환하여 천 년간 보존</div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-w5-c1", "text": "지하수가 차가운 바닥 암반을 흐르며 결로 현상을 유도해 본존불에 이슬이 맺히지 않게 한 '자연 습도 조절 원리'", "role": "석굴암 핵심 제습 과학", "para_idx": 1},
        {"cue_id": "g5-w5-c2", "text": "'외부 전실 ➔ 통로(비도) ➔ 둥근 본실(원형 주실)'이라는 공간적 진입 순서", "role": "공간 조직 순서", "para_idx": 1}
    ],
    graphic_organizer={
        "diagram_type": "3단계 정밀 퇴고표",
        "content_eval": "자연 암반수 결로 제습 과학 원리 확인",
        "structure_eval": "전실-비도-주실 공간적 진입 동선 일치",
        "expression_eval": "부사어 호응 및 객관적 어조 표준 교정"
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "문화유산 과학 원리 확인",
            "stem": "천 년 동안 석굴암 본존불에 이슬(결로)이 맺혀 훼손되지 않았던 과학적 비결은?",
            "target_para_idx": 1,
            "spotlight_quote": "지하수가 차가운 바닥 암반을 흐르며 결로 현상을 유도해 본존불에 이슬이 맺히지 않게 한 '자연 습도 조절 원리'가 바르게 기술되었는지",
            "options": [
                {"label": "①", "text": "차가운 암반수가 바닥을 흐르며 수증기를 바닥에만 결로시켜 본존불을 보송하게 유지했기 때문에", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 석굴암의 놀라운 자연 제습 과학입니다."},
                {"label": "②", "text": "전기 에어컨과 제습기를 하루 종일 틀어 두었기 때문에", "is_correct": False, "formula": "D6", "explanation": "신라 시대에 전기가 없었습니다."},
                {"label": "③", "text": "불상 표면에 플라스틱 랩을 씌워 두었기 때문에", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                {"label": "④", "text": "비가 올 때마다 스님들이 동굴을 들고 이동했기 때문에", "is_correct": False, "formula": "D5", "explanation": "불가능한 허구입니다."},
                {"label": "⑤", "text": "본존불에 기름을 발라 불을 붙였기 때문에", "is_correct": False, "formula": "D4", "explanation": "문화재 훼손 행위입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "표현 호응 오류 퇴고",
            "stem": "글쓴이가 3문단에서 지적한 초고의 표현상 결함과 올바른 교정 방향은?",
            "target_para_idx": 2,
            "spotlight_quote": "'비록 신라인들의 기술이 뛰어났지만 결코 결로 현상이 일어나지 않았다'처럼 부사어 '결코'와 호응하지 않는 문맥 비문을 표준 교정부호로 바로잡습니다.",
            "options": [
                {"label": "①", "text": "어색한 접속어와 부사어 호응 오류를 바로잡고 주어와 서술어를 매끄럽게 연결한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 표현 차원의 정확한 퇴고 목표입니다."},
                {"label": "②", "text": "모든 문장에 느낌표를 10개씩 붙여 흥분된 어조로 바꾼다.", "is_correct": False, "formula": "D3", "explanation": "객관적 설명문 어조에 어긋납니다."},
                {"label": "③", "text": "석굴암 대신 외국 사원 이야기로 전부 교체한다.", "is_correct": False, "formula": "D2", "explanation": "주제 통일성 위반입니다."},
                {"label": "④", "text": "글씨를 한자로만 번역하여 아무도 못 읽게 한다.", "is_correct": False, "formula": "D4", "explanation": "독자 배려에 위배됩니다."},
                {"label": "⑤", "text": "마침표를 전부 쉼표로 바꾼다.", "is_correct": False, "formula": "D5", "explanation": "비문 유발입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 석굴암의 공간적 진입 순서로 올바른 것은?",
            "options": [
                {"label": "①", "text": "외부 전실 ➔ 통로(비도) ➔ 둥근 본실(원형 주실)", "is_correct": True},
                {"label": "②", "text": "원형 주실 ➔ 외부 전실 ➔ 토함산 꼭대기", "is_correct": False},
                {"label": "③", "text": "지하 감옥 ➔ 종각 ➔ 비도", "is_correct": False},
                {"label": "④", "text": "비도 ➔ 외부 전실 ➔ 첨성대", "is_correct": False},
                {"label": "⑤", "text": "바다 ➔ 갯벌 ➔ 원형 주실", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "'외부 전실 ➔ 통로(비도) ➔ 둥근 본실(원형 주실)'이라는 공간적 진입 순서와 수학적 비례(1:√2)가", "is_correct": True},
                {"label": "②", "text": "통일 신라 경덕왕 때 창건된 토함산의 '석굴암'은", "is_correct": False},
                {"label": "③", "text": "첫째, 내용 면에서 지하수가 차가운 바닥 암반을 흐르며", "is_correct": False},
                {"label": "④", "text": "셋째, 표현 면에서 '비록 신라인들의 기술이", "is_correct": False},
                {"label": "⑤", "text": "편견 없는 객관적 어조와 정확한 용어로 퇴고할 때", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "석굴암 과학 퇴고 교정문 작성",
        "guide": "석굴암의 자연 제습 원리를 매끄러운 주술 호응 문장으로 퇴고해 보세요.",
        "template": "석굴암은 차가운 암반수를 바닥으로 흘려 수증기를 바닥에 [결로]시킴으로써 본존불의 습기를 제거하는 [자연 제습 과학]을 완성했습니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "퇴고 시 '내용(제습 원리) ➔ 조직(공간 진입) ➔ 표현(호응)' 3단계를 점검해요."},
        "step1_2_drill": {"task": "석굴암 공간 진입 동선(전실-비도-주실) 순서 맞추기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "석굴암은 바닥 암반수를 이용해 본존불의 결로를 방지했습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 석굴암의 숨겨진 에어컨",
        "situation": "경주 여행을 다녀오거나 석굴암 사진을 볼 때",
        "parent_question": "돌로 만든 동굴은 습기가 차서 곰팡이가 피기 쉬운데, 석굴암은 어떻게 천 년 동안 멀쩡했을까?",
        "expected_answer": "차가운 지하수를 바닥에만 흐르게 해서 습기를 바닥으로 끌어당긴 신라인의 과학 덕분이래요!",
        "coaching_tip": "신라인들의 놀라운 건축 물리학과 제습 기술에 대해 긍지와 감탄을 나누어 보세요."
    }
)

# Assemble all 16 slots for Grade 5 in order
ORDERED_SUBSKILLS = [
    "V1-1", "V1-2", "V1-3", "V1-4",
    "V2-1", "V2-2", "V2-3", "V2-4",
    "V3-1", "V3-2", "V3-3",
    "W1", "W2", "W3", "W4", "W5"
]

g5_all_expository = [slots_dict[code] for code in ORDERED_SUBSKILLS]

print(f"Total Grade 5 Expository Slots: {len(g5_all_expository)} (expected 16)")
print(f"Total Grade 5 Common Slots: {len(g5_common_slots)} (expected 6)")

out_path = os.path.join(ITEM_BANK_DIR, "g5_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 5,
        "expository_slots": g5_all_expository,
        "common_slots": g5_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g5_all_expository)} Expository + {len(g5_common_slots)} Common)")
