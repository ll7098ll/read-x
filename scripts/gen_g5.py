# -*- coding: utf-8 -*-
"""
Generator for Grade 5 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
Output: courseware/data/item_bank/g5_item_bank.json
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from item_bank_schema_helper import build_expository_slot, build_common_slot

ITEM_BANK_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data", "item_bank")
os.makedirs(ITEM_BANK_DIR, exist_ok=True)

# 1. Common Foundation Slots for Grade 5 (6 slots: G5-COM-A1 ~ G5-COM-A6)
g5_common_slots = [
    build_common_slot(
        grade_num=5,
        com_code_suffix="A1",
        title="공통 형태소를 공유하는 어휘군과 고난도 유의어 분석",
        rule_box="[어휘 형성 규칙] '생산, 출산, 재산'처럼 공통의 형태소나 한자 어근(産: 낳을 산)을 공유하는 어휘군을 묶어 파악하면, 낯선 학술 어휘의 의미를 체계적으로 확장할 수 있습니다.",
        passage_snippet="현대 사회에서는 공장에서 공산품을 대량 '생산'할 뿐만 아니라, 지식과 정보를 가공하여 고부가가치 콘텐츠를 '창산(창조적 생산)'하는 산업이 급성장하고 있습니다.",
        mini_question="'생산(生産)'과 '창산(創産)'에서 공통으로 쓰인 형태소 '산(産)'의 핵심 의미는 무엇인가요?",
        choices=[
            "① 물건이나 가치를 새롭게 만들어 냄",
            "② 낡은 것을 부수어 없앰",
            "③ 높은 산으로 올라감",
            "④ 돈을 은행에 저금함",
            "⑤ 차가운 얼음이 녹아내림"
        ],
        correct="①",
        feedback="'産(낳을 산)'은 무언가를 낳거나 새로운 물건·가치를 만들어 낸다는 뜻을 공통으로 담고 있습니다.",
        ox_items=[
            {"statement": "공통 형태소를 알면 새로운 복합어의 의미를 쉽게 추론할 수 있다.", "answer": "O", "reason": "형태소 기반 어휘 학습의 핵심 효과입니다."},
            {"statement": "한자 어근 '産'은 언제나 '높은 산'만을 의미한다.", "answer": "X", "reason": "뫼 산(山)과 낳을 산(産)은 서로 다른 형태소입니다."}
        ]
    ),
    build_common_slot(
        grade_num=5,
        com_code_suffix="A2",
        title="학술 텍스트 속 비유적 표현과 다의어 문맥 판별",
        rule_box="[학술 비유 규칙] 학술 설명문에서 '생태계의 그물', '사회의 윤활유' 같은 비유적 표현은 추상적인 상호작용과 기능적 관계를 구체화하여 설명하기 위한 표현 기법입니다.",
        passage_snippet="법과 도덕은 복잡한 사회 구성원 간의 갈등을 부드럽게 해결해 주는 '사회의 윤활유' 역할을 합니다. 기계 부품 사이에 기름을 치듯 인간관계를 원활하게 만듭니다.",
        mini_question="위 글에서 '사회의 윤활유'라는 비유적 표현이 뜻하는 바는 무엇인가요?",
        choices=[
            "① 기계에 바르는 미끄러운 기름",
            "② 사회적 갈등과 마찰을 줄여 관계를 원활하게 해 주는 역할",
            "③ 주유소에서 파는 자동차 휘발유",
            "④ 사람들이 싸우도록 불을 지르는 위험한 물질",
            "⑤ 법을 어긴 사람에게 내리는 벌금"
        ],
        correct="②",
        feedback="문맥에서 기계 부품의 마찰을 줄이는 윤활유처럼 사회 갈등을 완화한다는 비유적 속뜻입니다.",
        ox_items=[
            {"statement": "학술문 속 비유적 표현은 추상적 개념을 쉽게 설명하기 위해 쓰인다.", "answer": "O", "reason": "비유적 개념화의 기능입니다."},
            {"statement": "'윤활유'는 언제나 공업용 기름만을 뜻하므로 사회에 쓸 수 없다.", "answer": "X", "reason": "문맥에 따라 비유적·추상적 의미로 확장됩니다."}
        ]
    ),
    build_common_slot(
        grade_num=5,
        com_code_suffix="A3",
        title="겹문장의 복합 주술 호응 및 부사어-서술어 호응 오류 교정",
        rule_box="[호응 규칙] '비록 ~하더라도', '결코 ~않다', '왜냐하면 ~때문이다'처럼 특정한 부사어는 정해진 서술어 형태와 엄격히 호응해야 하며, 주어와 서술어의 거리가 멀어도 주술 관계가 일치해야 합니다.",
        passage_snippet="내가 이번 실험을 통해 증명하고자 하는 핵심은 빛의 굴절 현상이 매질의 밀도 차이에 따라 나타난다는 점이다. 결코 우리는 안전 수칙을 소홀히 해서는 안 된다.",
        mini_question="'결코'라는 부사어와 가장 자연스럽게 호응하는 서술어 형태는?",
        choices=[
            "① ~해서는 안 된다 (부정 서술)",
            "② ~하기를 바란다 (기원)",
            "③ ~할 수도 있다 (추측)",
            "④ ~해서 기쁘다 (감정)",
            "⑤ ~했기 때문이다 (이유)"
        ],
        correct="①",
        feedback="'결코'는 '결코 ~않다/안 된다'처럼 강한 부정 서술어와 호응하는 필수 부사어입니다.",
        ox_items=[
            {"statement": "'결코' 뒤에는 긍정의 서술어가 와야 자연스럽다.", "answer": "X", "reason": "'결코'는 부정어와 호응합니다."},
            {"statement": "'내가 강조하고 싶은 점은 ~라는 사실이다'는 주술 호응이 바르다.", "answer": "O", "reason": "주어 '점은'과 서술어 '사실이다'가 잘 호응합니다."}
        ]
    ),
    build_common_slot(
        grade_num=5,
        com_code_suffix="A4",
        title="거시 지시어('이러한 현상', '이 문제')의 전방 조응 추적",
        rule_box="[거시 조응] '이러한 현상', '이 문제점' 같은 거시적 지시 표현은 단일 단어가 아니라 앞 문단 전체에서 서술된 복합적 상황이나 원인-결과 관계를 가리킵니다.",
        passage_snippet="도시의 인구 과밀로 인해 출퇴근 시간의 극심한 교통 체증과 대기오염이 심화되고 있습니다. 정부는 '이러한 문제'를 해결하기 위해 대중교통망을 확충하고 있습니다.",
        mini_question="위 글에서 밑줄 친 '이러한 문제'가 가리키는 구체적 내용은?",
        choices=[
            "① 도시 인구 과밀로 인한 교통 체증과 대기오염 심화",
            "② 대중교통망의 무리한 공사 지연",
            "③ 농촌 지역의 일손 부족 현상",
            "④ 정부의 예산 낭비 문제",
            "⑤ 새로운 자동차의 출시 지연"
        ],
        correct="①",
        feedback="앞 문장에 서술된 도시 과밀에 따른 교통 체증과 대기오염 전체를 가리킵니다.",
        ox_items=[
            {"statement": "거시 지시어는 앞선 문장이나 문단 전체의 내용을 집약하여 가리킨다.", "answer": "O", "reason": "담화 응집성을 높이는 거시 지시어의 기능입니다."},
            {"statement": "지시어가 가리키는 대상은 항상 바로 앞의 한 단어에 국한된다.", "answer": "X", "reason": "문단 전체의 사태를 포괄하기도 합니다."}
        ]
    ),
    build_common_slot(
        grade_num=5,
        com_code_suffix="A5",
        title="연쇄적 인과 고리 추적 및 생략된 전제 복원",
        rule_box="[연쇄 인과] A(원인) ➔ B(결과/새 원인) ➔ C(최종 결과)처럼 이어지는 연쇄적 논리 구조에서, 글에 직접 언급되지 않고 생략된 중간 전제를 논리적으로 복원해야 합니다.",
        passage_snippet="가뭄이 지속되면 흙 속 수분이 줄어듭니다. 이는 농작물의 광합성을 방해하여 수확량 감소로 이어지고, 결국 식료품 가격이 급등하는 물가 불안을 초래합니다.",
        mini_question="가뭄에서 식료품 가격 급등으로 이어지는 연쇄 인과 고리의 중간 단계는?",
        choices=[
            "① 토양 수분 감소 ➔ 농작물 광합성 저해 ➔ 수확량 감소",
            "② 농가 소득 증가 ➔ 농기계 대량 구매",
            "③ 비가 많이 내려 ➔ 홍수 피해 발생",
            "④ 태풍 발생 ➔ 바다 양식장 파괴",
            "⑤ 도시 인구 증가 ➔ 아파트 가격 상승"
        ],
        correct="①",
        feedback="가뭄이 토양 수분을 줄이고 광합성을 방해해 수확량이 감소하는 중간 인과 사슬입니다.",
        ox_items=[
            {"statement": "원인과 최종 결과 사이에는 여러 중간 단계가 연쇄적으로 연결될 수 있다.", "answer": "O", "reason": "연쇄적 인과 구조의 본질입니다."},
            {"statement": "가뭄이 들면 농작물 수확량이 저절로 두 배 늘어난다.", "answer": "X", "reason": "수확량이 감소하여 가격이 급등합니다."}
        ]
    ),
    build_common_slot(
        grade_num=5,
        com_code_suffix="A6",
        title="명시적 중심문장이 결여된 문단의 거시구조 일반화 요약",
        rule_box="[거시구조 규칙] 문단에 중심문장이 명시적으로 드러나지 않을 때는, 나열된 세부 사례들의 공통 속성을 추출하여 독자 스스로 포괄적인 상위 중심문장을 구성(생성 규칙)해야 합니다.",
        passage_snippet="태양광 패널은 햇빛을 전기로 바꾸고, 풍력 발전기는 바람의 힘으로 터빈을 돌립니다. 수력 발전소는 댐에서 떨어지는 물의 낙차를 이용합니다.",
        mini_question="위 문단의 세부 사례들을 종합하여 독자가 생성할 수 있는 가장 적절한 상위 중심문장은?",
        choices=[
            "① 인류는 자연의 청정 에너지를 활용하여 다양한 방식으로 친환경 전기를 생산한다.",
            "② 태양광 발전기만 전기를 만들 수 있고 나머지는 불가능하다.",
            "③ 댐을 짓는 데는 너무 많은 시멘트가 들어간다.",
            "④ 바람이 불지 않는 날에는 모든 전기가 끊어진다.",
            "⑤ 석탄과 석유는 땅속 깊은 곳에 묻혀 있다."
        ],
        correct="①",
        feedback="태양, 바람, 물이라는 자연 에너지를 이용한 친환경 발전 방식을 포괄적으로 일반화한 요약입니다.",
        ox_items=[
            {"statement": "중심문장이 없는 문단은 세부 사실들의 공통점을 묶어 스스로 요약문을 구성해야 한다.", "answer": "O", "reason": "고난도 독해의 일반화·생성 규칙입니다."},
            {"statement": "중심문장이 없으면 그 문단은 아무 의미가 없는 엉터리 글이다.", "answer": "X", "reason": "사례 나열형 문단도 내재된 거시적 중심 생각을 지닙니다."}
        ]
    )
]

print(f"Built G5 Common Slots: {len(g5_common_slots)}")

# Load Grade 5 Flagship slot (G5-EXP-V3-2) from commercialMasterData.json
with open(os.path.join(os.path.dirname(SCRIPT_DIR), "webapp", "src", "data", "commercialMasterData.json"), "r", encoding="utf-8") as f:
    cmd_data = json.load(f)

g5_flagship_v32 = None
for gd in cmd_data.get("grades_data", []):
    if gd.get("slot_id") == "G5-EXP-V3-2":
        g5_flagship_v32 = gd
        break

print(f"Loaded G5 Flagship slot G5-EXP-V3-2: {g5_flagship_v32 is not None}")

# Now build the other 15 Expository slots for Grade 5 (5 options per question!)
# 1. V1-1
g5_slot_v11 = build_expository_slot(
    grade_num=5,
    subskill_code="V1-1",
    subject="과학(용해와 용액 5-1)",
    unit="1. 물질의 혼합과 분리",
    concept="물질이 물에 녹는 ‘용해’의 원리와 온도에 따른 용해도 변화",
    text_structure="정의·비교·인과",
    structure_type_code="causal",
    passage_title="물질이 골고루 섞이는 용해 현상과 온도의 영향",
    paragraphs=[
        "어떤 물질이 다른 물질에 골고루 녹아 들어가는 현상을 '용해'라고 하며, 녹는 물질을 '용질', 녹이는 물질을 '용매', 그리고 이들이 골고루 섞인 액체를 '용액'이라고 정의합니다. 소금을 물에 넣으면 소금 입자가 눈에 보이지 않을 만큼 미세하게 쪼개져 물 분자 사이에 균일하게 흩어지므로 용액은 어느 부분을 맛보아도 짠맛의 농도가 일정합니다.",
        "일정한 양의 용매에 최대로 녹을 수 있는 용질의 양을 '용해도'라고 합니다. 고체 물질의 용해도는 일반적으로 온도가 높아질수록 증가합니다. 따뜻한 물에서는 물 분자들의 운동이 활발해져 용질 입자를 둘러싸고 분리시키는 힘이 강해지기 때문입니다. 예를 들어 20℃의 물보다 80℃의 물에 백당(설탕)이 훨씬 더 많은 양 녹아들어 갑니다.",
        "반면에 기체 물질의 용해도는 온도가 높아질수록 오히려 감소합니다. 온도가 올라가면 기체 분자의 운동이 지나치게 활발해져 용매 밖으로 빠져나가기 때문입니다. 여름철 수온이 오르면 물속 산소(용존산소)가 줄어들어 물고기들이 수면 위로 입을 뻐끔거리는 현상이 바로 이러한 기체 용해도의 원리를 보여 줍니다."
    ],
    vocab_notes=[
        {"word": "용해도", "definition": "어떤 온도에서 용매 100g에 최대로 녹을 수 있는 용질의 g 수"},
        {"word": "용존산소", "definition": "물속에 분자 상태로 녹아 있는 산소의 양"}
    ],
    visual_html="""<div class="p-3 bg-cyan-50 rounded border border-cyan-200">
      <h4 class="font-bold text-cyan-900 mb-2">🧪 온도에 따른 물질 상태별 용해도 변화 비교</h4>
      <table class="w-full text-xs text-center border-collapse">
        <tr class="bg-cyan-100"><th class="p-1 border border-cyan-200">구분</th><th class="p-1 border border-cyan-200">고체 용질 (설탕·소금)</th><th class="p-1 border border-cyan-200">기체 용질 (산소·이산화탄소)</th></tr>
        <tr><td class="p-1 border border-cyan-200 font-bold bg-white">온도 상승 시</td><td class="p-1 border border-cyan-200 bg-white">용해도 <strong>증가</strong> (분자 운동 활발)</td><td class="p-1 border border-cyan-200 bg-white">용해도 <strong>감소</strong> (기체 기화 탈출)</td></tr>
        <tr><td class="p-1 border border-cyan-200 font-bold bg-white">대표 사례</td><td class="p-1 border border-cyan-200 bg-white">따뜻한 차에 설탕이 더 잘 녹음</td><td class="p-1 border border-cyan-200 bg-white">여름철 강물의 용존산소 부족</td></tr>
      </table>
    </div>""",
    hottext_cues=[
        {"cue_id": "g5-v11-c1", "text": "소금 입자가 눈에 보이지 않을 만큼 미세하게 쪼개져 물 분자 사이에 균일하게 흩어지므로", "role": "용해의 미시적 원리", "para_idx": 0},
        {"cue_id": "g5-v11-c2", "text": "반면에 기체 물질의 용해도는 온도가 높아질수록 오히려 감소합니다", "role": "기체 용해도 역상관성", "para_idx": 2}
    ],
    graphic_organizer={
        "diagram_type": "비교·대조 매트릭스",
        "factor": "온도 상승",
        "solubility": {
            "고체 용질": "용해도 상승 (물 분자 운동 촉진)",
            "기체 용질": "용해도 하강 (기체 분자의 탈출 가속)"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "개념 대조 추론",
            "stem": "글을 통해 알 수 있는 '고체 용질'과 '기체 용질'의 용해도 특성 차이로 가장 적절한 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "반면에 기체 물질의 용해도는 온도가 높아질수록 오히려 감소합니다. 온도가 올라가면 기체 분자의 운동이 지나치게 활발해져 용매 밖으로 빠져나가기 때문입니다.",
            "options": [
                {"label": "①", "text": "온도가 올라갈 때 고체는 용해도가 증가하지만, 기체는 용해도가 감소한다.", "is_correct": True, "formula": "정답", "explanation": "2문단과 3문단에 서술된 온도에 따른 고체와 기체 용해도의 명확한 대비입니다."},
                {"label": "②", "text": "온도가 올라가면 고체와 기체 모두 용해도가 무한정 증가한다.", "is_correct": False, "formula": "D3", "explanation": "기체의 용해도는 감소하므로 오답입니다."},
                {"label": "③", "text": "고체는 물에 절대 녹지 않고 기체만 녹을 수 있다.", "is_correct": False, "formula": "D1", "explanation": "소금이나 설탕 등 고체도 물에 잘 녹습니다."},
                {"label": "④", "text": "온도 변화는 물질의 용해도에 아무런 영향을 주지 않는다.", "is_correct": False, "formula": "D4", "explanation": "온도는 용해도에 결정적 영향을 미칩니다."},
                {"label": "⑤", "text": "여름철 수온이 오르면 물속 산소량이 겨울철보다 훨씬 풍부해진다.", "is_correct": False, "formula": "D5", "explanation": "수온이 오르면 용존산소가 줄어듭니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "생태 현상 인과 적용",
            "stem": "여름철 수온이 높아졌을 때 물고기들이 수면 위로 입을 내밀고 뻐끔거리는 과학적 원인은?",
            "target_para_idx": 2,
            "spotlight_quote": "여름철 수온이 오르면 물속 산소(용존산소)가 줄어들어 물고기들이 수면 위로 입을 뻐끔거리는 현상이",
            "options": [
                {"label": "①", "text": "수온 상승으로 기체인 산소의 용해도가 감소하여 물속 산소가 부족해졌기 때문에", "is_correct": True, "formula": "정답", "explanation": "3문단 마지막 문장에 서술된 생태학적 인과 관계입니다."},
                {"label": "②", "text": "물속 소금기가 너무 많아져 물고기가 목이 말랐기 때문에", "is_correct": False, "formula": "D2", "explanation": "염분과 무관한 산소 문제입니다."},
                {"label": "③", "text": "햇빛을 쬐며 일광욕을 즐기기 위해", "is_correct": False, "formula": "D6", "explanation": "의인화된 비과학적 오답입니다."},
                {"label": "④", "text": "물속 모래 알갱이가 너무 커져서", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                {"label": "⑤", "text": "물고기의 시력이 좋아져 하늘을 구경하기 위해", "is_correct": False, "formula": "D5", "explanation": "허구적 오답입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 따뜻한 물에서 고체 설탕이 더 빨리, 더 많이 녹는 분자 수준의 까닭은?",
            "options": [
                {"label": "①", "text": "물 분자의 운동이 활발해져 용질 입자를 둘러싸고 분리시키는 힘이 강해지기 때문에", "is_correct": True},
                {"label": "②", "text": "설탕 알갱이가 스스로 녹아 액체 기름으로 변하기 때문에", "is_correct": False},
                {"label": "③", "text": "물컵의 크기가 저절로 커지기 때문에", "is_correct": False},
                {"label": "④", "text": "공기 중의 질소가 물속으로 침투하기 때문에", "is_correct": False},
                {"label": "⑤", "text": "설탕의 질량이 사라지기 때문에", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "따뜻한 물에서는 물 분자들의 운동이 활발해져 용질 입자를 둘러싸고 분리시키는 힘이 강해지기 때문입니다.", "is_correct": True},
                {"label": "②", "text": "어떤 물질이 다른 물질에 골고루 녹아 들어가는 현상을 '용해'라고 하며,", "is_correct": False},
                {"label": "③", "text": "일정한 양의 용매에 최대로 녹을 수 있는 용질의 양을 '용해도'라고 합니다.", "is_correct": False},
                {"label": "④", "text": "반면에 기체 물질의 용해도는 온도가 높아질수록", "is_correct": False},
                {"label": "⑤", "text": "소금을 물에 넣으면 소금 입자가 눈에 보이지 않을 만큼", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "온도에 따른 용해도 과학 보고문 작성",
        "guide": "온도 상승에 따른 고체와 기체의 상반된 용해도 변화를 대조 접속어로 서술해 보세요.",
        "template": "온도가 올라가면 고체 용질은 분자 운동 촉진으로 용해도가 [증가]하지만, 기체 용질은 기화 탈출로 인해 용해도가 [감소]합니다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "용질의 상태(고체 vs 기체)에 따른 온도의 상반된 효과를 도표로 정리해요."},
        "step1_2_drill": {"task": "설탕(온도↑ 용해도↑) vs 탄산음료 기포(온도↑ 용해도↓) 인과 매핑"},
        "step3_vaccine": {"ox_quiz": [{"statement": "기체의 용해도는 온도가 높아질수록 감소합니다.", "answer": "O", "reason": "본문에 나온 핵심 과학 사실입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 따뜻한 콜라와 김빠짐",
        "situation": "냉장고에서 꺼낸 시원한 탄산음료와 미지근해진 탄산음료를 마실 때",
        "parent_question": "미지근해진 탄산음료는 왜 톡 쏘는 맛이 사라지고 김이 푹 빠졌을까?",
        "expected_answer": "온도가 올라가면 기체인 이산화탄소가 물에 녹아 있지 못하고 공기 중으로 날아가기 때문이래요!",
        "coaching_tip": "일상 속 탄산음료의 김빠짐을 기체 용해도 원리와 연결해 주면 과학이 친숙해집니다."
    }
)

print("Constructed G5 slot V1-1 successfully.")

# Slots 2 to 9 for Grade 5 (5 options each)
g5_slots_part2 = [
    # 2. V1-2
    build_expository_slot(
        grade_num=5,
        subskill_code="V1-2",
        subject="과학(온도와 열 5-1)",
        unit="2. 열의 전달과 보온",
        concept="열의 이동 방법 세 가지(전도·대류·복사)와 보온병의 구조",
        text_structure="분류(종류) + 분석(구조)",
        structure_type_code="classification",
        passage_title="열이 전달되는 세 가지 길과 보온병의 원리",
        paragraphs=[
            "열은 온도가 높은 곳에서 온도가 낮은 곳으로 세 가지 독특한 방식을 통해 끊임없이 이동합니다. 고체 물질에서 이웃한 물질 입자들의 충돌을 통해 열이 직접 전해지는 '전도', 액체나 기체에서 데워진 물질이 직접 위로 올라가고 찬 물질이 내려오면서 순환하는 '대류', 그리고 물질의 도움 없이 빛처럼 열에너지가 직접 사방으로 퍼져 나가는 '복사'가 그것입니다.",
            "예를 들어 쇠숟가락을 뜨거운 국에 담갔을 때 손잡이까지 뜨거워지는 것은 전도이며, 방바닥에 보일러를 틀었을 때 방 전체의 공기가 훈훈해지는 것은 대류입니다. 또한 모닥불이나 햇볕 아래 서 있을 때 피부로 온기를 느끼는 것은 열이 복사 형태로 전달되기 때문입니다.",
            "우리가 일상에서 쓰는 '보온병'은 이 세 가지 열의 이동을 완벽하게 차단하도록 설계된 첨단 과학 제품입니다. 내부를 이중 유리벽으로 만들고 그 사이를 진공 상태로 만들어 전도와 대류를 막았으며, 유리벽 안쪽에 은도금을 하여 열이 밖으로 빠져나가지 못하도록 복사열을 반사시킵니다."
        ],
        vocab_notes=[
            {"word": "전도", "definition": "고체 물질을 따라 열이 이웃한 분자로 차례차례 전달되는 현상"},
            {"word": "대류", "definition": "액체나 기체가 가열되어 밀도가 작아진 부분이 위로 올라가며 열을 전달하는 순환 현상"},
            {"word": "복사", "definition": "열이 다른 매개 물질 없이 전자기파(열선) 형태로 직접 전달되는 현상"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">🔥 열의 3대 전달 방식과 보온병 차단 설계</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-red-100"><th class="p-1 border border-red-200">열 전달 방식</th><th class="p-1 border border-red-200">주요 매질 및 메커니즘</th><th class="p-1 border border-red-200">보온병의 차단 설계</th></tr>
            <tr><td class="p-1 border border-red-200 font-bold bg-white">전도</td><td class="p-1 border border-red-200 bg-white">고체 (입자 간 충돌)</td><td class="p-1 border border-red-200 bg-white">이중벽 사이 <strong>진공 상태</strong>로 차단</td></tr>
            <tr><td class="p-1 border border-red-200 font-bold bg-white">대류</td><td class="p-1 border border-red-200 bg-white">액체·기체 (물질의 순환 이동)</td><td class="p-1 border border-red-200 bg-white">진공 공간 및 밀폐 뚜껑으로 차단</td></tr>
            <tr><td class="p-1 border border-red-200 font-bold bg-white">복사</td><td class="p-1 border border-red-200 bg-white">매질 없음 (빛처럼 직접 전달)</td><td class="p-1 border border-red-200 bg-white">내부 벽면 <strong>은도금(반사판)</strong>으로 차단</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g5-v12-c1", "text": "고체 물질에서 이웃한 물질 입자들의 충돌을 통해 열이 직접 전해지는 '전도'", "role": "전도 개념", "para_idx": 0},
            {"cue_id": "g5-v12-c2", "text": "유리벽 안쪽에 은도금을 하여 열이 밖으로 빠져나가지 못하도록 복사열을 반사시킵니다", "role": "보온병 복사열 차단 원리", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "구조-기능 매핑도",
            "thermos_flask": "보온병의 열 차단 구조",
            "insulation_parts": {
                "진공층": "전도와 대류 차단 (매질 제거)",
                "은도금 벽": "복사열 반사 (열 방출 방지)",
                "플라스틱 마개": "입구 쪽 전도 및 대류 차단"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "개념 분류 세부 확인",
                "stem": "글의 내용에 근거할 때 열의 이동 방식과 일상 사례의 연결이 올바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "쇠숟가락을 뜨거운 국에 담갔을 때 손잡이까지 뜨거워지는 것은 전도이며, 방바닥에 보일러를 틀었을 때 방 전체의 공기가 훈훈해지는 것은 대류입니다. 또한 모닥불이나 햇볕 아래 서 있을 때 피부로 온기를 느끼는 것은 열이 복사",
                "options": [
                    {"label": "①", "text": "뜨거운 국에 담긴 쇠숟가락 손잡이가 뜨거워지는 것 ➔ 전도", "is_correct": True, "formula": "정답", "explanation": "2문단 첫 문장에 명시된 고체에서의 열 전도 사례입니다."},
                    {"label": "②", "text": "햇볕을 쬘 때 온몸이 따뜻해지는 것 ➔ 대류", "is_correct": False, "formula": "D3", "explanation": "햇볕은 매질 없는 복사입니다."},
                    {"label": "③", "text": "방바닥의 온기로 방 전체 공기가 순환하는 것 ➔ 복사", "is_correct": False, "formula": "D2", "explanation": "공기 순환은 대류 현상입니다."},
                    {"label": "④", "text": "진공 공간을 통해 열이 입자 충돌로 전달되는 것 ➔ 전도", "is_correct": False, "formula": "D4", "explanation": "진공에는 입자가 없어 전도가 일어나지 않습니다."},
                    {"label": "⑤", "text": "보온병의 은도금 벽이 바람을 일으키는 것 ➔ 대류", "is_correct": False, "formula": "D5", "explanation": "은도금은 복사열을 반사합니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "구조-원리 인과 분석",
                "stem": "보온병 내부 유리벽 안쪽에 '은도금'을 처리한 과학적 이유는 무엇인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "유리벽 안쪽에 은도금을 하여 열이 밖으로 빠져나가지 못하도록 복사열을 반사시킵니다.",
                "options": [
                    {"label": "①", "text": "빠져나가려는 복사열을 안쪽으로 다시 반사시켜 보온을 유지하기 위해", "is_correct": True, "formula": "정답", "explanation": "3문단 마지막 문장에 서술된 은도금의 기능입니다."},
                    {"label": "②", "text": "보온병을 더 무겁게 만들어 쉽게 넘어지지 않게 하려고", "is_correct": False, "formula": "D1", "explanation": "무게와 무관한 열차단 장치입니다."},
                    {"label": "③", "text": "유리벽을 녹여서 투명하게 만들기 위해", "is_correct": False, "formula": "D6", "explanation": "유리를 녹이는 것이 아닙니다."},
                    {"label": "④", "text": "물속에 은 성분을 녹여 살균하기 위해", "is_correct": False, "formula": "D4", "explanation": "살균이 아닌 열반사 목적입니다."},
                    {"label": "⑤", "text": "진공 공간에 공기를 가득 채우기 위해", "is_correct": False, "formula": "D3", "explanation": "진공은 공기가 없는 상태입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 보온병의 이중벽 사이를 '진공 상태'로 만든 핵심 까닭은?",
                "options": [
                    {"label": "①", "text": "열을 전달할 매질(물질)을 없애 전도와 대류를 동시에 차단하기 위해", "is_correct": True},
                    {"label": "②", "text": "보온병 속 물을 얼음으로 급랭시키기 위해", "is_correct": False},
                    {"label": "③", "text": "소리가 밖으로 새어 나가지 않게 하려고", "is_correct": False},
                    {"label": "④", "text": "보온병을 비싼 가격에 팔기 위해", "is_correct": False},
                    {"label": "⑤", "text": "공기 방울을 모으기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "내부를 이중 유리벽으로 만들고 그 사이를 진공 상태로 만들어 전도와 대류를 막았으며,", "is_correct": True},
                    {"label": "②", "text": "열은 온도가 높은 곳에서 온도가 낮은 곳으로", "is_correct": False},
                    {"label": "③", "text": "우리가 일상에서 쓰는 '보온병'은 이 세 가지 열의 이동을 완벽하게 차단하도록", "is_correct": False},
                    {"label": "④", "text": "고체 물질에서 이웃한 물질 입자들의 충돌을 통해", "is_correct": False},
                    {"label": "⑤", "text": "방바닥에 보일러를 틀었을 때 방 전체의 공기가 훈훈해지는 것은", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "보온병의 열 차단 원리 분석문 작성",
            "guide": "보온병의 이중벽 진공층과 은도금 벽이 각각 어떤 열 이동을 차단하는지 서술해 보세요.",
            "template": "보온병의 진공층은 물질이 없어 [전도와 대류]를 차단하고, 은도금 벽면은 열선을 튕겨내어 [복사]를 차단합니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "열의 3대 이동(전도-고체, 대류-유체, 복사-빛)과 차단 기법을 연결해요."},
            "step1_2_drill": {"task": "전도, 대류, 복사 현상 매핑 및 보온병 차단 요소 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "진공 상태에서는 열의 전도와 대류가 일어나지 않습니다.", "answer": "O", "reason": "열을 전달할 매개 입자가 없기 때문입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 따뜻한 보온병의 비밀",
            "situation": "소풍이나 캠핑 갈 때 보온병에 담긴 따뜻한 물을 마실 때",
            "parent_question": "보온병 안의 따뜻한 물은 왜 차가운 바깥 날씨에도 식지 않고 오래갈까?",
            "expected_answer": "이중벽 사이를 공기 없는 진공으로 만들어 전도와 대류를 막고, 은도금으로 복사열을 반사하기 때문이래요!",
            "coaching_tip": "매일 쓰는 생활 용품에 숨겨진 물리 과학 원리를 신기하게 체감하도록 격려해 주세요."
        }
    ),

    # 3. V1-3
    build_expository_slot(
        grade_num=5,
        subskill_code="V1-3",
        subject="과학(태양계와 별 5-1)",
        unit="3. 태양계와 우주",
        concept="태양계를 이루는 8개 행성의 분류와 특징 비교",
        text_structure="분류(분류 기준 명시) + 비교",
        structure_type_code="classification",
        passage_title="태양계를 도는 행성들의 두 얼굴, 지구형과 목성형",
        paragraphs=[
            "태양 주위를 공전하는 8개의 행성은 구성 물질과 물리적 특성에 따라 '지구형 행성'과 '목성형 행성'이라는 두 개의 커다란 무리로 분류할 수 있습니다. 분류 기준을 명확히 설정하면 수많은 천체 데이터의 규칙성을 체계적으로 이해할 수 있습니다.",
            "수성, 금성, 지구, 화성은 '지구형 행성'에 속합니다. 이 행성들은 단단한 암석과 금속으로 이루어져 있어 밀도가 크고 표면에 발을 디딜 수 있는 고체 지각이 존재합니다. 하지만 크기와 질량은 상대적으로 작으며, 고리가 없고 위성의 수가 매우 적거나 없습니다.",
            "반면에 목성, 토성, 천왕성, 해왕성은 '목성형 행성'으로 분류됩니다. 이들은 주로 수소나 헬륨 같은 가벼운 기체로 구성되어 있어 덩치는 거대하지만 밀도가 작습니다. 표면이 기체로 덮여 있어 단단한 지각이 없으며, 아름다운 고리를 거느리고 수십 개의 위성을 가지고 있습니다."
        ],
        vocab_notes=[
            {"word": "지구형 행성", "definition": "암석과 금속으로 이루어져 단단한 표면과 큰 밀도를 가진 행성군"},
            {"word": "목성형 행성", "definition": "기체 성분으로 이루어져 크기는 거대하나 밀도가 작고 고리가 있는 행성군"}
        ],
        visual_html="""<div class="p-3 bg-violet-50 rounded border border-violet-200">
          <h4 class="font-bold text-violet-900 mb-2">🪐 태양계 행성 양대 분류 (지구형 vs 목성형)</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-violet-100"><th class="p-1 border border-violet-200">구분 기준</th><th class="p-1 border border-violet-200">지구형 행성 (수·금·지·화)</th><th class="p-1 border border-violet-200">목성형 행성 (목·토·천·해)</th></tr>
            <tr><td class="p-1 border border-violet-200 font-bold bg-white">주성분·표면</td><td class="p-1 border border-violet-200 bg-white">암석·금속 (단단한 표면 지각)</td><td class="p-1 border border-violet-200 bg-white">수소·헬륨 기체 (고체 표면 없음)</td></tr>
            <tr><td class="p-1 border border-violet-200 font-bold bg-white">크기·밀도</td><td class="p-1 border border-violet-200 bg-white">크기 작음, 밀도 큼</td><td class="p-1 border border-violet-200 bg-white">크기 거대함, 밀도 작음</td></tr>
            <tr><td class="p-1 border border-violet-200 font-bold bg-white">고리·위성</td><td class="p-1 border border-violet-200 bg-white">고리 없음, 위성 적음</td><td class="p-1 border border-violet-200 bg-white">고리 있음, 위성 매우 많음</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g5-v13-c1", "text": "단단한 암석과 금속으로 이루어져 있어 밀도가 크고 표면에 발을 디딜 수 있는 고체 지각이 존재합니다", "role": "지구형 행성 특성", "para_idx": 1},
            {"cue_id": "g5-v13-c2", "text": "주로 수소나 헬륨 같은 가벼운 기체로 구성되어 있어 덩치는 거대하지만 밀도가 작습니다", "role": "목성형 행성 특성", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "분류 매트릭스",
            "solar_system": "태양계 8개 행성",
            "classes": {
                "지구형": ["수성", "금성", "지구", "화성"],
                "목성형": ["목성", "토성", "천왕성", "해왕성"]
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "분류 기준 적용 세부 확인",
                "stem": "글의 내용에 근거할 때 '목성형 행성'에 속하는 행성들의 공통적 특징으로 알맞은 것은?",
                "target_para_idx": 2,
                "spotlight_quote": "주로 수소나 헬륨 같은 가벼운 기체로 구성되어 있어 덩치는 거대하지만 밀도가 작습니다. 표면이 기체로 덮여 있어 단단한 지각이 없으며, 아름다운 고리를 거느리고 수십 개의 위성을",
                "options": [
                    {"label": "①", "text": "기체 성분으로 이루어져 덩치는 거대하지만 밀도가 작고 고리가 있다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 목성형 행성의 핵심 물리적 특징입니다."},
                    {"label": "②", "text": "단단한 암석 지각이 있어 우주선이 표면에 착륙할 수 있다.", "is_correct": False, "formula": "D3", "explanation": "지구형 행성의 특징입니다."},
                    {"label": "③", "text": "위성이 단 하나도 존재하지 않는다.", "is_correct": False, "formula": "D2", "explanation": "수십 개의 위성을 거느리고 있습니다."},
                    {"label": "④", "text": "밀도가 철덩어리처럼 매우 크다.", "is_correct": False, "formula": "D4", "explanation": "가벼운 기체이므로 밀도가 작습니다."},
                    {"label": "⑤", "text": "수성과 금성, 화성이 대표적인 목성형 행성이다.", "is_correct": False, "formula": "D1", "explanation": "지구형 행성의 이름들입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "비교 대조 분석",
                "stem": "지구형 행성과 목성형 행성을 가르는 가장 핵심적인 분류 기준은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "태양 주위를 공전하는 8개의 행성은 구성 물질과 물리적 특성에 따라 '지구형 행성'과 '목성형 행성'이라는 두 개의 커다란 무리로 분류할 수 있습니다.",
                "options": [
                    {"label": "①", "text": "행성을 이루는 구성 물질(암석 vs 기체)과 밀도·고리 유무", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 행성 분류의 과학적 기준입니다."},
                    {"label": "②", "text": "행성의 이름이 한글인지 영어인지의 여부", "is_correct": False, "formula": "D5", "explanation": "과학적 기준이 아닙니다."},
                    {"label": "③", "text": "행성이 태양 주변을 도는지 다른 은하를 도는지", "is_correct": False, "formula": "D3", "explanation": "8개 행성 모두 태양을 돕니다."},
                    {"label": "④", "text": "인류가 이주하여 집을 지었는지의 여부", "is_correct": False, "formula": "D4", "explanation": "아직 지구 외에 인류가 집을 짓지 못했습니다."},
                    {"label": "⑤", "text": "망원경으로 보았을 때 초록색으로 보이는지 여부", "is_correct": False, "formula": "D6", "explanation": "단순 색깔 구분이 아닙니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 목성형 행성에 사람이 발을 딛고 서 있을 수 없는 물리적 이유는?",
                "options": [
                    {"label": "①", "text": "표면이 고체 암석이 아닌 기체로 덮여 있어 단단한 지각이 없기 때문에", "is_correct": True},
                    {"label": "②", "text": "외계인이 땅을 전부 파헤쳐 놓아서", "is_correct": False},
                    {"label": "③", "text": "행성의 중력이 전혀 없기 때문에", "is_correct": False},
                    {"label": "④", "text": "표면이 온통 끈적끈적한 엿기름이라서", "is_correct": False},
                    {"label": "⑤", "text": "행성이 너무 작아 발바닥만 해서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "표면이 기체로 덮여 있어 단단한 지각이 없으며,", "is_correct": True},
                    {"label": "②", "text": "수성, 금성, 지구, 화성은 '지구형 행성'에 속합니다.", "is_correct": False},
                    {"label": "③", "text": "고체 물질에서 이웃한 물질 입자들의 충돌을 통해", "is_correct": False},
                    {"label": "④", "text": "아름다운 고리를 거느리고 수십 개의 위성을 가지고 있습니다.", "is_correct": False},
                    {"label": "⑤", "text": "태양 주위를 공전하는 8개의 행성은 구성 물질과", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "행성 양대 분류 비교표 작성",
            "guide": "지구형 행성과 목성형 행성의 주성분과 표면 특징을 한 문장으로 대조해 보세요.",
            "template": "지구형 행성은 [암석과 금속]으로 이루어져 단단한 지각이 있는 반면에, 목성형 행성은 [수소와 헬륨 기체]로 이루어져 고체 표면이 없고 고리가 있습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "행성 분류는 '구성 물질(암석 vs 가스)'과 '크기/밀도'를 대조표로 묶어 외워요."},
            "step1_2_drill": {"task": "8개 행성을 지구형(4개)과 목성형(4개) 상자에 분류하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "목성형 행성은 기체로 이루어져 있어 단단한 지각이 없습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 목성에 우주선이 착륙할 수 있을까?",
            "situation": "밤하늘의 밝은 목성이나 토성을 관측하거나 사진을 볼 때",
            "parent_question": "토성이나 목성 표면에 우주선이 달 표면처럼 쿵 하고 착륙할 수 있을까?",
            "expected_answer": "목성형 행성은 돌로 된 땅이 없고 온통 가스(기체) 덩어리라서 발을 디딜 바닥이 없대요!",
            "coaching_tip": "행성의 본질적 구성 차이를 상상해 보도록 우주적 대화를 이끌어 주세요."
        }
    )
]

print("Constructed G5 slots V1-2 and V1-3.")
