# -*- coding: utf-8 -*-
"""
Master Generator for Grade 6 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
5-Option KICE Evaluation Standard (expected_opt_len = 5)
Output: courseware/data/item_bank/g6_item_bank.json
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

# 1. Common Foundation Slots for Grade 6 (6 slots: G6-COM-A1 ~ G6-COM-A6)
g6_common_slots = [
    build_common_slot(
        grade_num=6,
        com_code_suffix="A1",
        title="초등 최고 난도 학술 한자어 및 추상 개념어의 구조 분석",
        rule_box="[추상 어휘 분석] '항상성(恒常性)', '상호의존성(相互依存性)' 같은 고난도 학술 조어는 각각의 한자 형태소(恒: 항상 항, 常: 항상 상, 性: 성품/성질 성)의 의미를 결합하여 추상적 개념을 정밀하게 분해·해석합니다.",
        passage_snippet="인간의 신체는 외부 환경의 급격한 기온 변화에도 불구하고 체온을 36.5℃로 일정하게 유지하려는 생체 조절 능력인 '항상성'을 지니고 있습니다.",
        mini_question="'항상성(恒常性)'의 한자 조어 원리를 바탕으로 한 핵심 의미는 무엇인가요?",
        choices=[
            "① 언제나 변함없이 일정한 상태를 유지하려는 성질",
            "② 기온에 따라 몸의 온도가 마음대로 바뀌는 성질",
            "③ 병원균이 몸속에 무한정 증식하는 상태",
            "④ 인간이 겨울잠을 자는 동물로 변하는 성질",
            "⑤ 체온이 영하 10도까지 급격히 얼어붙는 현상"
        ],
        correct="①",
        feedback="'恒(항상 항)'과 '常(항상 상)'이 합쳐져 늘 일정한 상태를 유지한다는 생물학적 조절 성질을 뜻합니다.",
        ox_items=[
            {"statement": "학술 한자어는 개별 한자 형태소의 의미 결합을 통해 정밀하게 해석할 수 있다.", "answer": "O", "reason": "형태소 분석적 어휘 독해의 원리입니다."},
            {"statement": "'항상성'은 환경에 따라 몸 상태가 시시각각 멋대로 변함을 뜻한다.", "answer": "X", "reason": "일정한 평형을 유지하려는 성질입니다."}
        ]
    ),
    build_common_slot(
        grade_num=6,
        com_code_suffix="A2",
        title="복합 학술 텍스트 속 표면적 서술과 이면의 전제 추론",
        rule_box="[이면 전제 추론] 글쓴이가 겉으로 명시하지 않았으나 논리의 성립을 위해 바탕에 깔아 둔 숨은 가정이나 배경 이론(전제)을 논리적으로 도출합니다.",
        passage_snippet="인공지능의 자율주행 기술이 도입되면 인간 운전자의 부주의로 인한 교통사고 사망률을 획기적으로 낮출 수 있습니다. 그러나 알고리즘 오류 발생 시 법적 책임 주체를 규명하는 문제는 여전히 미완의 과제입니다.",
        mini_question="위 글에서 글쓴이가 바탕에 깔고 있는 핵심적인 '숨은 전제'는 무엇인가요?",
        choices=[
            "① 현재 발생하는 대다수 교통사고의 주요 원인은 인간 운전자의 부주의에 기인한다.",
            "② 인공지능 자율주행차는 절대로 고장 나거나 사고를 내지 않는다.",
            "③ 모든 자동차는 도로 주행을 영구히 중단해야 한다.",
            "④ 인공지능 운전자는 운전면허 시험을 볼 자격이 없다.",
            "⑤ 법적 책임은 언제나 승객 한 사람에게만 있다."
        ],
        correct="①",
        feedback="'자율주행이 인간 부주의 사고를 낮춘다'는 주장의 밑바탕에는 현재 사고의 주원인이 인간 부주의라는 전제가 깔려 있습니다.",
        ox_items=[
            {"statement": "주장의 타당성을 검증하려면 글 속에 숨은 기본 전제를 찾아내야 한다.", "answer": "O", "reason": "비판적 논증 독해의 핵심입니다."},
            {"statement": "글쓴이가 쓰지 않은 내용은 절대 생각해서는 안 된다.", "answer": "X", "reason": "논리적 전제와 함의를 추론하는 것이 고급 독해입니다."}
        ]
    ),
    build_common_slot(
        grade_num=6,
        com_code_suffix="A3",
        title="복합 비문(도치·생략·이중 피동)의 정밀 문법 교정",
        rule_box="[고난도 문법 교정] '생각되어진다(이중 피동)'는 '~로 생각한다'로 능동화하고, '내가 말하려는 것은 ~점이다'의 복합 주술 호응과 목적어-서술어 누락을 완벽히 교정합니다.",
        passage_snippet="이 연구에서 가장 중요하게 보여지는 점은 신재생에너지의 간헐성 문제를 기술적으로 극복되어져야 한다는 사실이다.",
        mini_question="위 문장의 어색한 이중 피동 표현('보여지는', '극복되어져야')을 바르게 고친 것은?",
        choices=[
            "① 가장 중요하게 드러나는 점은 ~ 극복해야 한다는 사실이다.",
            "② 가장 중요하게 보여지어지는 점은 ~ 극복당해야 한다.",
            "③ 가장 중요함을 보는 점은 ~ 극복되게 시켜야 한다.",
            "④ 중요함이 보여진 것은 ~ 극복을 당하는 것이다.",
            "⑤ 중요성이 보이게 되는 바는 ~ 극복을 받게 됨이다."
        ],
        correct="①",
        feedback="'보여지는'과 '극복되어져야' 같은 불필요한 번역투 이중 피동을 능동적이고 자연스러운 표현으로 다듬은 문장입니다.",
        ox_items=[
            {"statement": "'~되어지다'는 우리말 어법에 맞지 않는 잘못된 이중 피동 표현이다.", "answer": "O", "reason": "국립국어원 표준 문법 규정입니다."},
            {"statement": "피동 표현은 많이 쓸수록 글의 학술적 권위가 높아진다.", "answer": "X", "reason": "남용된 피동은 문장의 주체를 모호하게 만듭니다."}
        ]
    ),
    build_common_slot(
        grade_num=6,
        com_code_suffix="A4",
        title="다층 담화표지와 거시 메타 언어의 정합성 검증",
        rule_box="[메타 담화표지] '앞서 논의한 바와 같이', '결론적으로 말하자면', '이와는 대조적으로' 등의 메타 언어가 글 전체의 거시적 구조와 완벽히 정합하는지 판별합니다.",
        passage_snippet="태양광 발전은 무한한 청정 에너지를 공급한다는 장점이 있습니다. 앞서 언급한 바와 같이, 태양광 발전은 밤이나 비 오는 날에는 전기를 생산하지 못하는 간헐성 한계를 지닙니다.",
        mini_question="위 글에서 '앞서 언급한 바와 같이'라는 메타 담화표지가 어색한 까닭과 바른 교정은?",
        choices=[
            "① 장점에 이어 상반된 단점을 제시하므로 '이와는 반대로' 또는 '그러나'로 교정해야 한다.",
            "② 태양광 발전이 밤에 전기를 못 만든다는 것은 거짓말이기 때문에",
            "③ 앞선 문장과 똑같은 장점만을 반복하고 있기 때문에",
            "④ 문장을 세 줄 이상으로 더 길게 늘려야 하기 때문에",
            "⑤ 결론을 맺는 말이므로 '결론적으로'로 바꾸어야 한다."
        ],
        correct="①",
        feedback="장점에서 단점으로 논리적 역접/대조가 이루어지므로 '그러나'나 '이와는 반대로'가 적절합니다.",
        ox_items=[
            {"statement": "담화표지는 앞뒤 문맥의 논리적 관계(순접, 역접, 인과)에 맞게 쓰여야 한다.", "answer": "O", "reason": "텍스트 결속성의 필수 요건입니다."},
            {"statement": "'앞서 언급한 바와 같이'는 아무 문장에나 멋으로 붙여도 된다.", "answer": "X", "reason": "앞서 실제로 언급된 내용이 있을 때만 써야 합니다."}
        ]
    ),
    build_common_slot(
        grade_num=6,
        com_code_suffix="A5",
        title="복합 논리 구조 분석 및 논리적 비약·성급한 일반화 반박",
        rule_box="[논리 오류 판별] 제한된 몇 가지 사례만으로 전체를 단정하는 '성급한 일반화의 오류'나 원인과 결과를 자의적으로 연결하는 '논리적 비약'을 논리적으로 반박합니다.",
        passage_snippet="일부 스마트폰 사용자가 수면 부족을 겪는다는 연구 결과가 있습니다. 따라서 스마트폰은 청소년의 뇌를 파괴하는 독극물이므로 모든 스마트폰의 생산과 판매를 전면 금지해야 합니다.",
        mini_question="위 주장에 내재된 가장 치명적인 논리적 결함은 무엇인가요?",
        choices=[
            "① 일부의 부작용 사례를 바탕으로 기기 자체를 독극물로 단정하고 판매 금지를 요구하는 성급한 일반화와 논리적 비약",
            "② 스마트폰의 가격이 너무 저렴하다는 사실을 밝히지 않은 점",
            "③ 연구 조사의 대상자 이름을 공개하지 않은 점",
            "④ 스마트폰 배터리의 충전 시간을 고려하지 않은 점",
            "⑤ 청소년의 키가 자라는 이유를 설명하지 않은 점"
        ],
        correct="①",
        feedback="제한된 부정적 사례를 극단적으로 침소봉대하여 전면 금지를 주장한 전형적인 비약과 과잉 일반화입니다.",
        ox_items=[
            {"statement": "주장의 근거가 소수 사례에 국한될 때 성급한 일반화의 오류가 발생한다.", "answer": "O", "reason": "논리학적 오류 판별의 기본입니다."},
            {"statement": "모든 주장은 결론이 과격할수록 설득력이 높아진다.", "answer": "X", "reason": "합리적 근거와 비례하는 결론이어야 설득력이 있습니다."}
        ]
    ),
    build_common_slot(
        grade_num=6,
        com_code_suffix="A6",
        title="다층 융합 텍스트의 거시구조 분석 및 학술 초록(Abstract) 요약",
        rule_box="[초록 요약 규칙] 연구 목적, 핵심 이론 메커니즘, 실험·통계 결과, 그리고 결론 및 시사점을 각 1문장씩 4단위 학술 초록 구조로 압축 요약합니다.",
        passage_snippet="본 연구는 플라스틱 순환경제 전환의 경제적 타당성을 검증하고자 했습니다. 분석 결과, 화학적 재활용 기술을 적용할 때 원자재 비용을 35% 절감할 수 있었습니다. 따라서 정부의 세제 지원과 재활용 인프라 확충이 시급합니다.",
        mini_question="위 학술 텍스트를 가장 잘 압축한 한 문장 핵심 결론은?",
        choices=[
            "① 화학적 재활용은 원자재 비용을 절감하므로 정책적 인프라 확충을 통해 순환경제 전환을 가속화해야 한다.",
            "② 플라스틱을 태우는 쓰레기 소각장을 전국에 1000개 더 지어야 한다.",
            "③ 모든 플라스틱 공장은 당장 문을 닫아야 한다.",
            "④ 세금을 10배로 늘려 플라스틱 사용자에게 벌금을 물려야 한다.",
            "⑤ 재활용 기술은 비용이 너무 많이 들어 포기해야 한다."
        ],
        correct="①",
        feedback="연구 목적, 실증 데이터, 정책 시사점을 유기적으로 종합한 완벽한 학술 요약문입니다.",
        ox_items=[
            {"statement": "학술 텍스트 요약은 문제 제기, 핵심 근거, 결론을 유기적으로 엮어야 한다.", "answer": "O", "reason": "초록(Abstract) 작성의 핵심 요건입니다."},
            {"statement": "요약문에는 수치 데이터나 통계는 절대 포함해서는 안 된다.", "answer": "X", "reason": "핵심 실증 수치는 요약의 신뢰성을 높여 줍니다."}
        ]
    )
]

print(f"Built G6 Common Slots: {len(g6_common_slots)}")

# Load Grade 6 Flagship slot (G6-EXP-W5) from commercialMasterData.json
with open(os.path.join(os.path.dirname(SCRIPT_DIR), "webapp", "src", "data", "commercialMasterData.json"), "r", encoding="utf-8") as f:
    cmd_data = json.load(f)

g6_flagship_w5 = None
for gd in cmd_data.get("grades_data", []):
    if gd.get("slot_id") == "G6-EXP-W5":
        g6_flagship_w5 = gd
        break

if g6_flagship_w5:
    g6_flagship_w5["subskill_code"] = "W5"

print(f"Loaded G6 Flagship slot G6-EXP-W5: {g6_flagship_w5 is not None}")

# Import all modules
from gen_g6_slots_v1 import slots_v1
from gen_g6_slots_v2 import slots_v2
from gen_g6_slots_v3 import slots_v3
from gen_g6_slots_w import slots_w

slots_dict_g6 = {
    **slots_v1,
    **slots_v2,
    **slots_v3,
    **slots_w,
    "W5": g6_flagship_w5
}

ORDERED_SUBSKILLS = [
    "V1-1", "V1-2", "V1-3", "V1-4",
    "V2-1", "V2-2", "V2-3", "V2-4",
    "V3-1", "V3-2", "V3-3",
    "W1", "W2", "W3", "W4", "W5"
]

g6_all_expository = []
for code in ORDERED_SUBSKILLS:
    slot = slots_dict_g6.get(code)
    if slot is None:
        raise ValueError(f"Missing slot for Grade 6: {code}")
    g6_all_expository.append(slot)

print(f"Total Grade 6 Expository Slots: {len(g6_all_expository)} (expected 16)")
print(f"Total Grade 6 Common Slots: {len(g6_common_slots)} (expected 6)")

out_path = os.path.join(ITEM_BANK_DIR, "g6_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 6,
        "expository_slots": g6_all_expository,
        "common_slots": g6_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g6_all_expository)} Expository + {len(g6_common_slots)} Common)")

