# -*- coding: utf-8 -*-
"""
Generator for Grade 4 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
Output: courseware/data/item_bank/g4_item_bank.json
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

# 1. Common Foundation Slots for Grade 4 (6 slots: G4-COM-A1 ~ G4-COM-A6)
g4_common_slots = [
    build_common_slot(
        grade_num=4,
        com_code_suffix="A1",
        title="합성어와 파생어의 어근·접사 분석하기",
        rule_box="[낱말 형성 원리] 낱말의 실질적 중심 의미를 나타내는 부분을 '어근'이라 하고, 어근의 앞뒤에 붙어 새로운 뜻을 더해 주는 말을 '접사(접두사/접미사)'라고 합니다.",
        passage_snippet="봄바람이 불어오자 들판에 파릇파릇 '풋나물'이 돋아나고, 농부들은 논밭에 나가 '맨손'으로 흙을 일굽니다.",
        mini_question="'풋나물'과 '맨손'에서 접두사 '풋-'과 '맨-'이 더해 주는 의미는 무엇인가요?",
        choices=[
            "① '풋-'은 처음 나온 덜 익은 것, '맨-'은 다른 것이 없는 상태를 뜻한다.",
            "② 둘 다 아주 크고 무겁다는 뜻을 나타낸다.",
            "③ 둘 다 차갑고 얼어붙은 상태를 나타낸다.",
            "④ 둘 다 밤하늘의 밝은 별을 가리킨다."
        ],
        correct="①",
        feedback="'풋사랑, 풋과일'의 '풋-'은 덜 익음을 뜻하고, '맨손, 맨발'의 '맨-'은 아무것도 걸치지 않은 상태를 뜻합니다.",
        ox_items=[
            {"statement": "접두사는 낱말의 앞에 붙어 특정한 뜻을 더해 준다.", "answer": "O", "reason": "파생어 형성의 기본 원칙입니다."},
            {"statement": "어근과 접사를 구별하지 않아도 낯선 낱말의 뜻을 쉽게 알 수 있다.", "answer": "X", "reason": "어근과 접사를 분석하면 모르는 낱말의 뜻을 정확히 유추할 수 있습니다."}
        ]
    ),
    build_common_slot(
        grade_num=4,
        com_code_suffix="A2",
        title="문맥 속 다의어와 관용 표현의 이면 의미 파악",
        rule_box="[관용구 원칙] 둘 이상의 낱말이 합쳐져 원래 낱말의 뜻과 다른 특별한 새로운 의미로 굳어진 표현을 '관용 표현'이라고 합니다.",
        passage_snippet="반장 선거에 출마한 민재는 온 동네를 누비며 발을 넓혔습니다. 그리고 어려운 친구들의 고민에 귀를 기울이며 진심을 다했습니다.",
        mini_question="'발을 넓히다'와 '귀를 기울이다'의 속뜻으로 가장 알맞은 것은?",
        choices=[
            "① 발의 크기를 키우고, 귀를 한쪽으로 잡아당기다.",
            "② 사귀는 사람의 범위를 넓히고, 남의 말에 주의를 집중해 듣다.",
            "③ 신발을 큰 것으로 바꾸어 신고, 귓구멍을 막다.",
            "④ 달리기 시합에서 발을 헛디뎌 넘어지다."
        ],
        correct="②",
        feedback="관용 표현의 비유적 속뜻을 문맥 속에서 파악해야 합니다.",
        ox_items=[
            {"statement": "관용 표현은 글자 그대로의 낱말 뜻만으로 해석하면 어색하다.", "answer": "O", "reason": "굳어진 비유적 의미를 파악해야 합니다."},
            {"statement": "'손이 크다'는 언제나 신체 손의 물리적 크기만을 뜻한다.", "answer": "X", "reason": "씀씀이가 너그럽다는 관용적 의미로 널리 쓰입니다."}
        ]
    ),
    build_common_slot(
        grade_num=4,
        com_code_suffix="A3",
        title="겹문장의 안은문장·이어진문장과 호응 관계 분석",
        rule_box="[문장 구조 규칙] 주어와 서술어의 관계가 두 번 이상 나타나는 문장을 겹문장이라고 하며, 앞뒤 절이 원인·조건으로 이어지거나 하나의 절이 다른 절 속에 안겨 들어갑니다.",
        passage_snippet="비가 내렸지만 우리는 우산을 쓰고 숲으로 갔다. 우리가 관찰한 식물은 줄기가 곧게 뻗어 있었다.",
        mini_question="위 글에서 '비가 내렸지만'은 어떤 방식으로 이어진 문장인가요?",
        choices=[
            "① 대조의 의미로 이어진 문장",
            "② 원인과 결과로 이어진 문장",
            "③ 시간 순서대로 나열된 문장",
            "④ 아무런 관계없이 끊어진 문장"
        ],
        correct="①",
        feedback="'~지만'은 앞 절과 뒤 절의 내용이 상반·대조됨을 나타내는 연결어미입니다.",
        ox_items=[
            {"statement": "'~지만'으로 이어진 문장은 앞뒤 내용이 서로 대조된다.", "answer": "O", "reason": "대조 연결어미의 기능입니다."},
            {"statement": "겹문장에서는 주어와 서술어가 한 번만 나온다.", "answer": "X", "reason": "주어-서술어 관계가 두 번 이상 나타납니다."}
        ]
    ),
    build_common_slot(
        grade_num=4,
        com_code_suffix="A4",
        title="문단 전환 담화표지와 거시 지시어 추적",
        rule_box="[담화 표지 기능] '이와 같이', '그럼에도 불구하고', '한편' 등은 앞 문단 전체의 내용을 가리키거나 화제를 전환하는 거시적 담화 표지입니다.",
        passage_snippet="도시에는 인구가 밀집하여 주택 부족과 교통 체증 문제가 심각합니다. 한편 촌락에서는 일손이 부족하여 농사짓기가 어렵습니다.",
        mini_question="위 글에서 '한편'이라는 담화 표지가 하는 역할은 무엇인가요?",
        choices=[
            "① 앞선 '도시 문제'에서 다른 측면인 '촌락 문제'로 화제를 전환한다.",
            "② 앞선 내용과 똑같은 사례를 반복해서 강조한다.",
            "③ 글의 전체 결론을 맺고 글을 끝낸다.",
            "④ 앞 문장의 원인을 설명한다."
        ],
        correct="①",
        feedback="'한편'은 관련된 다른 측면으로 화제를 돌릴 때 쓰는 전환 담화표지입니다.",
        ox_items=[
            {"statement": "'한편'은 새로운 화제나 다른 측면을 소개할 때 쓴다.", "answer": "O", "reason": "문단 전환 표지의 핵심 기능입니다."},
            {"statement": "담화표지는 문장의 의미 연결과 전혀 관계가 없다.", "answer": "X", "reason": "글의 응집성과 논리적 흐름을 결정하는 중요한 장치입니다."}
        ]
    ),
    build_common_slot(
        grade_num=4,
        com_code_suffix="A5",
        title="복합 인과 관계와 다중 원인 구조 분석",
        rule_box="[복합 인과] 하나의 현상이나 결과 뒤에는 여러 가지 다양한 원인이 얽혀 있을 수 있으므로, 다중 원인을 빠짐없이 찾아내야 합니다.",
        passage_snippet="지구 온난화로 극지방의 빙하가 녹고 있습니다. 이는 화석 연료의 과도한 사용뿐만 아니라 무분별한 삼림 벌채로 온실가스 흡수원이 줄어든 복합적인 원인 때문입니다.",
        mini_question="빙하가 녹는 현상의 두 가지 원인으로 올바르게 짝지어진 것은?",
        choices=[
            "① 화석 연료 과다 사용과 삼림 벌채",
            "② 플라스틱 재활용과 나무 심기",
            "③ 겨울철 폭설과 태풍 발생",
            "④ 북극곰의 사냥과 펭귄의 이동"
        ],
        correct="①",
        feedback="본문에 제시된 두 가지 복합 원인(화석 연료 사용, 삼림 벌채)을 모두 포괄한 답입니다.",
        ox_items=[
            {"statement": "어떤 결과가 일어났을 때 원인은 반드시 하나만 존재한다.", "answer": "X", "reason": "자연과 사회 현상에는 여러 원인이 복합적으로 작용합니다."},
            {"statement": "복합 인과 글에서는 여러 원인을 항목별로 나누어 파악해야 한다.", "answer": "O", "reason": "다중 원인 분석 독해의 기본 원칙입니다."}
        ]
    ),
    build_common_slot(
        grade_num=4,
        com_code_suffix="A6",
        title="3~4문단 텍스트의 중심 내용 추출 및 상위어 일반화 요약",
        rule_box="[상위어 요약 규칙] 사소하거나 반복되는 세부 내용을 삭제하고, 구체적인 사례들을 포괄하는 상위 개념어로 묶어 문단별 중심 생각을 일반화합니다.",
        passage_snippet="사과는 비타민 C가 풍부하고, 바나나는 칼륨이 많으며, 포도는 안토시아닌이 풍부합니다. 이처럼 다양한 과일은 우리 몸에 필요한 필수 영양소를 골고루 공급해 줍니다.",
        mini_question="위 문단의 세부 과일 사례들을 '상위 개념어'로 묶어 가장 잘 요약한 중심 문장은?",
        choices=[
            "① 다양한 과일은 몸에 유익한 필수 영양소를 풍부하게 공급한다.",
            "② 사과에는 비타민 C만 들어 있어 다른 과일은 먹을 필요가 없다.",
            "③ 바나나는 칼륨이 많아 운동선수만 먹어야 한다.",
            "④ 포도 껍질의 색깔은 보라색이다."
        ],
        correct="①",
        feedback="구체적인 과일 이름들을 '과일'이라는 상위어로 묶고, 공통 효과를 일반화하여 요약했습니다.",
        ox_items=[
            {"statement": "요약할 때는 구체적인 나열 사례를 상위 개념어로 묶어 일반화한다.", "answer": "O", "reason": "요약 규칙(삭제, 선택, 일반화)의 핵심 원리입니다."},
            {"statement": "요약문에는 지엽적인 사례들을 하나도 빠짐없이 다 적어야 한다.", "answer": "X", "reason": "사소한 세부 사항은 삭제하고 핵심 개념 중심으로 간추립니다."}
        ]
    )
]

print(f"Built G4 Common Slots: {len(g4_common_slots)}")

# 2. Expository Slots for Grade 4 (16 slots: V1-1 ~ W5)
# Note: CSAT questions have 4 options (G3~4 초중 standard)
g4_expository_slots = [
    # 1. V1-1
    build_expository_slot(
        grade_num=4,
        subskill_code="V1-1",
        subject="과학(물의 상태 변화 4-1)",
        unit="1. 물의 순환과 상태",
        concept="물의 세 가지 상태 변화와 지구의 물 분포",
        text_structure="과정·열거",
        structure_type_code="sequence",
        passage_title="끝없이 순환하는 물의 세 가지 모습",
        paragraphs=[
            "지구 표면의 약 70%는 물로 덮여 있지만, 우리가 마실 수 있는 담수는 전체 물의 약 2.5%에 불과합니다. 물은 고체인 얼음, 액체인 물, 기체인 수증기라는 세 가지 상태로 끊임없이 변하며 지구 전체를 순환합니다.",
            "태양열을 받은 강과 바다의 물은 수증기로 증발하여 공기 중으로 올라갑니다. 높은 하늘로 올라간 수증기는 차가운 공기를 만나 작은 물방울이나 얼음 알갱이로 응결되어 구름이 됩니다. 구름이 무거워지면 비나 눈이 되어 다시 땅으로 내립니다.",
            "땅에 내린 빗물은 지하수가 되거나 강을 거쳐 바다로 흘러 들어갑니다. 이처럼 물의 상태 변화와 순환 덕분에 지구의 생명체들은 깨끗한 물을 지속적으로 공급받으며 살아갈 수 있습니다."
        ],
        vocab_notes=[
            {"word": "담수", "definition": "염분이 거의 없어 마시거나 농사에 쓸 수 있는 민물"},
            {"word": "응결", "definition": "수증기 같은 기체가 냉각되어 액체인 물로 변하는 현상"}
        ],
        visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
          <h4 class="font-bold text-blue-900 mb-2">💧 물의 순환 3단계 다이어그램</h4>
          <div class="grid grid-cols-3 gap-1 text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-blue-200"><strong>1단계 증발</strong><br>태양열 ➔ 수증기 상승</div>
            <div class="p-1.5 bg-white rounded border border-blue-200"><strong>2단계 응결</strong><br>냉각 ➔ 구름 형성</div>
            <div class="p-1.5 bg-white rounded border border-blue-200"><strong>3단계 강수</strong><br>비·눈 ➔ 지표 및 바다</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v11-c1", "text": "우리가 마실 수 있는 담수는 전체 물의 약 2.5%에 불과합니다", "role": "지구 물 분포 사실", "para_idx": 0},
            {"cue_id": "g4-v11-c2", "text": "차가운 공기를 만나 작은 물방울이나 얼음 알갱이로 응결되어 구름이 됩니다", "role": "응결과 구름 생성 원리", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "순환 순서도",
            "cycle": ["지표수 증발(수증기)", "고공 냉각 응결(구름)", "강수(비·눈)", "하천 유입 및 지하수"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "세부 사실 확인",
                "stem": "글의 내용과 일치하지 않는 설명은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "우리가 마실 수 있는 담수는 전체 물의 약 2.5%에 불과합니다.",
                "options": [
                    {"label": "①", "text": "지구 전체 물 중에서 마실 수 있는 담수는 약 2.5%뿐이다.", "is_correct": False, "formula": "D1", "explanation": "1문단에 명시된 일치 내용입니다."},
                    {"label": "②", "text": "수증기가 차가운 공기를 만나 응결되면 구름이 형성된다.", "is_correct": False, "formula": "D2", "explanation": "2문단에 설명된 과학적 사실입니다."},
                    {"label": "③", "text": "지구의 모든 물은 한번 증발하면 우주 밖으로 사라져 버린다.", "is_correct": True, "formula": "정답", "explanation": "물은 비가 되어 다시 땅으로 순환하므로 완전히 틀린 설명입니다."},
                    {"label": "④", "text": "물의 순환 덕분에 지구 생명체가 살아갈 수 있다.", "is_correct": False, "formula": "D4", "explanation": "3문단 중심 내용과 일치합니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "과정 인과 추론",
                "stem": "하늘에 뜬 구름이 비나 눈이 되어 내리는 직접적인 원인은?",
                "target_para_idx": 1,
                "spotlight_quote": "구름이 무거워지면 비나 눈이 되어 다시 땅으로 내립니다.",
                "options": [
                    {"label": "①", "text": "구름 속 물방울과 얼음 알갱이가 뭉쳐 무거워졌기 때문에", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 강수의 직접 원인입니다."},
                    {"label": "②", "text": "바닷물이 모두 증발하여 구름을 밀어냈기 때문에", "is_correct": False, "formula": "D3", "explanation": "과학적 근거가 없는 오답입니다."},
                    {"label": "③", "text": "사람들이 인공 비행기로 구름을 터뜨렸기 때문에", "is_correct": False, "formula": "D5", "explanation": "자연 순환 과정과 무관한 설명입니다."},
                    {"label": "④", "text": "태양빛이 완전히 꺼져 얼어붙었기 때문에", "is_correct": False, "formula": "D6", "explanation": "허구의 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 공기 중의 수증기가 작은 물방울로 변하는 현상을 뜻하는 과학 용어는?",
                "options": [
                    {"label": "①", "text": "응결", "is_correct": True},
                    {"label": "②", "text": "증발", "is_correct": False},
                    {"label": "③", "text": "용해", "is_correct": False},
                    {"label": "④", "text": "연소", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 문장은?",
                "options": [
                    {"label": "①", "text": "차가운 공기를 만나 작은 물방울이나 얼음 알갱이로 응결되어 구름이 됩니다.", "is_correct": True},
                    {"label": "②", "text": "태양열을 받은 강과 바다의 물은 수증기로 증발하여", "is_correct": False},
                    {"label": "③", "text": "지구 표면의 약 70%는 물로 덮여 있지만,", "is_correct": False},
                    {"label": "④", "text": "이처럼 물의 상태 변화와 순환 덕분에", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "물의 순환 3단계 인과 요약문 쓰기",
            "guide": "증발, 응결, 강수의 과정을 인과 접속어로 정리해 보세요.",
            "template": "태양열로 물이 [증발]하여 수증기가 되고, 높은 곳에서 차가워져 구름으로 [응결]됩니다. 그 결과 무거워진 구름이 [비나 눈]으로 내립니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "물의 상태 변화(증발, 응결)와 순환 과정을 단계별로 정리해요."},
            "step1_2_drill": {"task": "물의 세 가지 상태(얼음, 물, 수증기)와 순환 과정 카드 맞추기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "수증기가 찬 공기를 만나 물방울로 변하는 것을 응결이라고 합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 냄비 뚜껑의 물방울",
            "situation": "찌개가 끓는 냄비 뚜껑 안쪽에 맺힌 물방울을 볼 때",
            "parent_question": "냄비 안에서 수증기가 뚜껑에 닿아 물방울이 되는 건 하늘의 어떤 현상과 같을까?",
            "expected_answer": "수증기가 차가운 뚜껑에 닿아 물방울이 되는 건 하늘에 구름이 맺히는 응결 현상과 같아요!",
            "coaching_tip": "일상 속 수증기 응결을 하늘의 구름 생성 원리와 연결해 주면 과학적 사고가 확장됩니다."
        }
    ),

    # 2. V1-2
    build_expository_slot(
        grade_num=4,
        subskill_code="V1-2",
        subject="과학(식물의 생활 4-1)",
        unit="2. 환경에 적응한 식물",
        concept="사막의 선인장과 물속의 부레옥잠이 환경에 적응한 모습",
        text_structure="비교·대조 + 인과",
        structure_type_code="comparison",
        passage_title="물 부족 사막과 물 위 식물의 적응 비결",
        paragraphs=[
            "식물은 자신이 살아가는 서식지의 수분 환경에 따라 독특한 몸 구조를 발달시켰습니다. 극도로 건조한 사막에 사는 '선인장'과 물 위에 둥둥 떠서 사는 '부레옥잠'은 잎과 줄기의 생김새가 완전히 다릅니다.",
            "사막의 선인장은 물 증발을 막기 위해 잎이 뾰족한 가시로 변했습니다. 또한 두껍고 초록색인 줄기 속에 스펀지처럼 많은 물을 저장할 수 있어 비가 오지 않아도 오랫동안 버팁니다. 뿌리 또한 비가 오면 즉시 물을 흡수하도록 흙 표면 가까이 넓게 퍼져 있습니다.",
            "반면에 물 위에 사는 부레옥잠은 잎자루 속에 공기주머니가 가득 들어 있어 물에 가볍게 뜹니다. 또한 깃털처럼 생긴 수염뿌리는 물속에 길게 늘어져 식물의 균형을 잡고 영양분을 흡수합니다. 이처럼 두 식물의 차이는 물이 부족한 환경과 물이 풍부한 환경에 적응한 지혜를 보여 줍니다."
        ],
        vocab_notes=[
            {"word": "서식지", "definition": "생물이 지속적으로 자리를 잡고 살아가는 자연환경"},
            {"word": "공기주머니", "definition": "식물체 내부에 공기를 채워 부력을 갖게 하는 구조"}
        ],
        visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">🌵 선인장 vs 🪷 부레옥잠 적응 대조표</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-emerald-100"><th class="p-1 border border-emerald-200">구분</th><th class="p-1 border border-emerald-200">선인장 (건조 사막)</th><th class="p-1 border border-emerald-200">부레옥잠 (수생 환경)</th></tr>
            <tr><td class="p-1 border border-emerald-200 font-bold bg-white">잎의 특징</td><td class="p-1 border border-emerald-200 bg-white">가시로 변형 (수분 손실 방지)</td><td class="p-1 border border-emerald-200 bg-white">공기주머니 잎자루 (물에 뜸)</td></tr>
            <tr><td class="p-1 border border-emerald-200 font-bold bg-white">줄기·뿌리</td><td class="p-1 border border-emerald-200 bg-white">물 저장 줄기, 넓은 뿌리</td><td class="p-1 border border-emerald-200 bg-white">물속 깃털 수염뿌리 (균형 유지)</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v12-c1", "text": "사막의 선인장은 물 증발을 막기 위해 잎이 뾰족한 가시로 변했습니다", "role": "선인장 가시 적응 원인", "para_idx": 1},
            {"cue_id": "g4-v12-c2", "text": "부레옥잠은 잎자루 속에 공기주머니가 가득 들어 있어 물에 가볍게 뜹니다", "role": "부레옥잠 부력 적응 원인", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "비교·대조 매트릭스",
            "contrast_items": {
                "선인장": ["잎: 가시 (수분 보존)", "줄기: 물 저장소", "환경: 건조 사막"],
                "부레옥잠": ["잎자루: 공기주머니 (부력)", "뿌리: 수염뿌리 (균형)", "환경: 수면 위"]
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "비교 대조 세부 확인",
                "stem": "선인장의 '가시'와 부레옥잠의 '공기주머니'에 대한 설명으로 옳은 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "사막의 선인장은 물 증발을 막기 위해 잎이 뾰족한 가시로 변했습니다.",
                "options": [
                    {"label": "①", "text": "선인장 가시는 수분 증발을 막고, 부레옥잠 공기주머니는 물에 뜨게 한다.", "is_correct": True, "formula": "정답", "explanation": "각 식물의 서식지 환경 적응 기능을 바르게 대조했습니다."},
                    {"label": "②", "text": "선인장 가시는 물에 뜨기 위한 장치이고, 부레옥잠 공기주머니는 가시 역할을 한다.", "is_correct": False, "formula": "D3", "explanation": "두 식물의 적응 기능을 뒤바꾼 오답입니다."},
                    {"label": "③", "text": "두 구조 모두 사막에서 비를 내리게 하는 마법 도구이다.", "is_correct": False, "formula": "D1", "explanation": "비과학적 허구입니다."},
                    {"label": "④", "text": "선인장 가시는 추운 겨울에 몸을 따뜻하게 덮는 털이다.", "is_correct": False, "formula": "D4", "explanation": "가시는 수분 손실을 막기 위해 변형된 잎입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "뿌리 기능 인과 추론",
                "stem": "부레옥잠의 깃털 같은 수염뿌리가 물속에서 하는 주요 역할은?",
                "target_para_idx": 2,
                "spotlight_quote": "또한 깃털처럼 생긴 수염뿌리는 물속에 길게 늘어져 식물의 균형을 잡고 영양분을 흡수합니다.",
                "options": [
                    {"label": "①", "text": "물에 뜬 식물의 균형을 잡고 영양분을 흡수한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 부레옥잠 뿌리의 명확한 기능입니다."},
                    {"label": "②", "text": "땅속 단단한 암석에 뿌리를 박아 식물을 고정한다.", "is_correct": False, "formula": "D2", "explanation": "부레옥잠은 물에 떠서 사는 식물입니다."},
                    {"label": "③", "text": "물고기를 공격하여 잡아먹는 덫 역할을 한다.", "is_correct": False, "formula": "D5", "explanation": "육식 식물이 아닙니다."},
                    {"label": "④", "text": "물 표면 위로 꽃을 쏘아 올리는 로켓 역할을 한다.", "is_correct": False, "formula": "D6", "explanation": "엉뚱한 과장입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 선인장의 두꺼운 줄기가 지닌 핵심 기능은?",
                "options": [
                    {"label": "①", "text": "많은 양의 수분을 스펀지처럼 저장하기 위해", "is_correct": True},
                    {"label": "②", "text": "바람에 날려 다른 나라로 이동하기 위해", "is_correct": False},
                    {"label": "③", "text": "곤충을 꾀어내어 가두기 위해", "is_correct": False},
                    {"label": "④", "text": "나무 열매를 맺기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "두껍고 초록색인 줄기 속에 스펀지처럼 많은 물을 저장할 수 있어", "is_correct": True},
                    {"label": "②", "text": "식물은 자신이 살아가는 서식지의 수분 환경에 따라", "is_correct": False},
                    {"label": "③", "text": "뿌리 또한 비가 오면 즉시 물을 흡수하도록", "is_correct": False},
                    {"label": "④", "text": "반면에 물 위에 사는 부레옥잠은", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "환경 적응 비교 대조문 쓰기",
            "guide": "선인장과 부레옥잠의 잎 생김새를 대조 접속어('반면에')를 사용하여 한 문장으로 써 보세요.",
            "template": "선인장은 수분을 아끼기 위해 잎이 [가시]로 변한 반면에, 부레옥잠은 물에 뜨기 위해 잎자루에 [공기주머니]를 만들었습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "환경 적응 글은 '서식지 특징(건조 vs 물)'과 '식물 부위 변형'을 대조표로 정리해요."},
            "step1_2_drill": {"task": "선인장(가시, 저장 줄기)과 부레옥잠(공기주머니, 수염뿌리) 특징 카드 분류"},
            "step3_vaccine": {"ox_quiz": [{"statement": "선인장의 가시는 원래 잎이 변한 것입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 식물의 생존 비밀",
            "situation": "거실에 놓인 선인장 화분을 볼 때",
            "parent_question": "선인장은 왜 다른 식물처럼 넓은 초록 잎 대신 뾰족한 가시를 가졌을까?",
            "expected_answer": "물이 부족한 사막에서 잎으로 물이 증발하지 않도록 가시로 변한 거래요!",
            "coaching_tip": "주변 식물의 잎 모양을 관찰하며 환경에 대한 적응의 지혜를 함께 나눠 보세요."
        }
    ),

    # 3. V1-3
    build_expository_slot(
        grade_num=4,
        subskill_code="V1-3",
        subject="과학(땅의 변화 4-2)",
        unit="3. 화산과 화성암",
        concept="화산 활동으로 만들어진 두 암석: 현무암과 화강암",
        text_structure="비교·대조 + 인과",
        structure_type_code="comparison",
        passage_title="마그마가 식어 만든 돌, 현무암과 화강암",
        paragraphs=[
            "지하 깊은 곳에서 암석이 녹아 만들어진 뜨거운 액체를 '마그마'라고 하며, 마그마가 식어서 굳어진 암석을 '화성암'이라고 부릅니다. 화성암의 대표적인 암석인 현무암과 화강암은 마그마가 식는 장소와 속도에 따라 성질이 완전히 다릅니다.",
            "현무암은 마그마가 지표면 밖으로 뿜어져 나와 용암이 된 뒤, 공기와 닿아 빠르게 식어서 만들어졌습니다. 급격히 식었기 때문에 알갱이의 크기가 매우 작고 어두운 색을 띱니다. 또한 화산가스가 빠져나간 자리에 크고 작은 구멍이 숭숭 뚫려 있는 경우가 많습니다.",
            "반면에 화강암은 마그마가 땅속 깊은 곳에서 오랜 시간에 걸쳐 천천히 식으면서 만들어졌습니다. 천천히 식었기 때문에 광물 알갱이가 굵게 자라나 육안으로도 알갱이를 볼 수 있으며, 밝은 회색이나 분홍색을 띱니다. 마그마가 식는 속도라는 원인이 두 암석의 알갱이 크기와 색깔이라는 결과를 만든 것입니다."
        ],
        vocab_notes=[
            {"word": "화성암", "definition": "마그마나 용암이 식어서 굳어진 암석"},
            {"word": "광물", "definition": "암석을 이루는 천연의 무기 결정질 고체"}
        ],
        visual_html="""<div class="p-3 bg-stone-50 rounded border border-stone-200">
          <h4 class="font-bold text-stone-900 mb-2">🪨 현무암 vs 화강암 비교 매트릭스</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-stone-100"><th class="p-1 border border-stone-200">구분</th><th class="p-1 border border-stone-200">현무암 (제주도 돌하르방)</th><th class="p-1 border border-stone-200">화강암 (북한산 바위)</th></tr>
            <tr><td class="p-1 border border-stone-200 font-bold bg-white">식은 장소·속도</td><td class="p-1 border border-stone-200 bg-white">지표면 밖, 빠르게 식음</td><td class="p-1 border border-stone-200 bg-white">땅속 깊은 곳, 천천히 식음</td></tr>
            <tr><td class="p-1 border border-stone-200 font-bold bg-white">알갱이 크기·색</td><td class="p-1 border border-stone-200 bg-white">매우 작은 알갱이, 어두운색, 구멍</td><td class="p-1 border border-stone-200 bg-white">굵은 알갱이, 밝은색</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v13-c1", "text": "공기와 닿아 빠르게 식어서 만들어졌습니다. 급격히 식었기 때문에 알갱이의 크기가 매우 작고", "role": "현무암 생성 원인과 결과", "para_idx": 1},
            {"cue_id": "g4-v13-c2", "text": "땅속 깊은 곳에서 오랜 시간에 걸쳐 천천히 식으면서 만들어졌습니다", "role": "화강암 생성 원인", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "화성암 비교 도식",
            "source": "마그마의 냉각",
            "branches": {
                "지표면(급랭)": "현무암 (미세 알갱이, 어두운색, 가스 구멍)",
                "지하 심부(완만)": "화강암 (굵은 알갱이, 밝은색, 단단함)"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "인과 관계 분석",
                "stem": "화강암의 알갱이 크기가 현무암보다 굵은 직접적인 까닭은 무엇인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "마그마가 땅속 깊은 곳에서 오랜 시간에 걸쳐 천천히 식으면서 만들어졌습니다. 천천히 식었기 때문에 광물 알갱이가 굵게 자라나",
                "options": [
                    {"label": "①", "text": "마그마가 땅속 깊은 곳에서 천천히 오랜 시간 식었기 때문에", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 알갱이가 크게 성장한 핵심 인과 이유입니다."},
                    {"label": "②", "text": "지표면에서 찬 공기를 맞아 급격히 얼어붙었기 때문에", "is_correct": False, "formula": "D3", "explanation": "현무암의 생성 조건입니다."},
                    {"label": "③", "text": "바닷속 물고기들이 암석을 갉아먹었기 때문에", "is_correct": False, "formula": "D1", "explanation": "암석 생성과 무관한 오답입니다."},
                    {"label": "④", "text": "화강암 속에 금과 은이 가득 차 있어서", "is_correct": False, "formula": "D4", "explanation": "본문에 없는 비과학적 서술입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 특징 비교",
                "stem": "'현무암'의 특징으로 알맞은 것을 고르면?",
                "target_para_idx": 1,
                "spotlight_quote": "급격히 식었기 때문에 알갱이의 크기가 매우 작고 어두운 색을 띱니다. 또한 화산가스가 빠져나간 자리에 크고 작은 구멍이 숭숭 뚫려 있는 경우가 많습니다.",
                "options": [
                    {"label": "①", "text": "어두운 색을 띠고 화산가스가 빠져나간 구멍이 뚫려 있다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 현무암의 대표 외형 특징입니다."},
                    {"label": "②", "text": "굵은 알갱이가 육안으로 보이고 전체적으로 밝은 분홍빛이다.", "is_correct": False, "formula": "D2", "explanation": "화강암의 특징입니다."},
                    {"label": "③", "text": "마그마가 아니라 물속 모래가 굳어져 생겼다.", "is_correct": False, "formula": "D5", "explanation": "퇴적암에 대한 설명입니다."},
                    {"label": "④", "text": "손으로 만지면 스펀지처럼 푹신푹신하게 들어간다.", "is_correct": False, "formula": "D6", "explanation": "암석이므로 단단합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 현무암과 화강암의 알갱이 크기를 결정하는 가장 결정적인 요인은?",
                "options": [
                    {"label": "①", "text": "마그마가 식는 속도와 장소", "is_correct": True},
                    {"label": "②", "text": "암석이 놓인 산의 높이", "is_correct": False},
                    {"label": "③", "text": "암석을 캐낸 사람의 나이", "is_correct": False},
                    {"label": "④", "text": "바람이 불어오는 방향", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "마그마가 식는 속도라는 원인이 두 암석의 알갱이 크기와 색깔이라는 결과를 만든 것입니다.", "is_correct": True},
                    {"label": "②", "text": "지하 깊은 곳에서 암석이 녹아 만들어진 뜨거운 액체를 '마그마'라고 하며,", "is_correct": False},
                    {"label": "③", "text": "현무암은 마그마가 지표면 밖으로 뿜어져 나와", "is_correct": False},
                    {"label": "④", "text": "화성암의 대표적인 암석인 현무암과 화강암은", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "화성암 비교 보고서 작성하기",
            "guide": "현무암과 화강암의 식는 속도와 알갱이 차이를 한 문장으로 대조해 보세요.",
            "template": "현무암은 마그마가 [빠르게] 식어 알갱이가 작고 구멍이 있지만, 화강암은 [천천히] 식어 알갱이가 굵고 단단합니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "암석 생성 글은 '냉각 속도(빠름 vs 느림)'와 '알갱이 크기'의 인과를 연결해요."},
            "step1_2_drill": {"task": "현무암(구멍, 어두움)과 화강암(굵은 알갱이, 밝음) 표 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "화강암은 땅속 깊은 곳에서 천천히 식어 만들어진 암석입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 제주도 돌과 북한산 돌",
            "situation": "제주도 여행 사진(돌하르방)이나 등산 사진을 볼 때",
            "parent_question": "제주도 돌하르방은 까맣고 구멍이 숭숭 뚫렸는데, 왜 서울 북한산 바위는 밝고 단단할까?",
            "expected_answer": "제주도 돌은 용암이 밖에서 빨리 식어 구멍 난 현무암이고, 북한산 바위는 땅속에서 천천히 굳은 화강암이래요!",
            "coaching_tip": "실제 주변 지형의 암석을 마그마의 냉각 원리와 연결하여 과학적 호기심을 북돋워 주세요."
        }
    )
]

# Add remaining 13 slots for Grade 4 (V1-4 ~ W5)
g4_remaining_slots = [
    # 4. V1-4
    build_expository_slot(
        grade_num=4,
        subskill_code="V1-4",
        subject="과학(땅의 변화 4-2)",
        unit="3. 지층과 퇴적암",
        concept="층층이 쌓인 지층과 퇴적암(이암·사암·역암)이 만들어지는 과정",
        text_structure="순서·과정 + 분류",
        structure_type_code="classification",
        passage_title="차곡차곡 쌓여 굳어진 지층과 퇴적암",
        paragraphs=[
            "야외에 나가 산이나 바닷가 절벽을 보면 줄무늬 시루떡처럼 줄무늬가 층층이 쌓여 있는 '지층'을 볼 수 있습니다. 지층은 자갈, 모래, 진흙 같은 퇴적물이 오랜 세월 동안 물밑에 차곡차곡 쌓여서 만들어집니다.",
            "지층이 만들어지는 과정은 물의 운반과 퇴적에서 시작됩니다. 흐르는 물이 상류의 바위를 깎아 알갱이들을 운반하여 호수나 바다 바닥에 층을 이루어 퇴적시킵니다. 위에 새로운 퇴적물이 계속 쌓이면 아래쪽 퇴적물은 엄청난 무게로 꽉 눌리고, 알갱이 사이에 녹아 있던 물질이 풀처럼 알갱이를 굳힙니다.",
            "이렇게 굳어져 생긴 돌을 '퇴적암'이라고 합니다. 퇴적암은 쌓인 알갱이의 크기에 따라 분류됩니다. 주로 진흙이 굳은 것은 '이암', 모래가 굳은 것은 '사암', 자갈 사이에 모래와 진흙이 섞여 굳은 것은 '역암'이라고 부릅니다."
        ],
        vocab_notes=[
            {"word": "퇴적물", "definition": "물이나 바람에 의해 운반되어 바닥에 가라앉아 쌓인 물질"},
            {"word": "역암", "definition": "자갈이 주성분이고 그 사이에 모래나 진흙이 채워져 굳어진 퇴적암"}
        ],
        visual_html="""<div class="p-3 bg-yellow-50 rounded border border-yellow-200">
          <h4 class="font-bold text-yellow-900 mb-2">🧱 퇴적암 3종 분류 기준 (알갱이 크기)</h4>
          <div class="grid grid-cols-3 gap-1 text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-yellow-200"><strong>이암 (진흙)</strong><br>가장 고운 알갱이<br>부드러움</div>
            <div class="p-1.5 bg-white rounded border border-yellow-200"><strong>사암 (모래)</strong><br>중간 크기 알갱이<br>까슬까슬함</div>
            <div class="p-1.5 bg-white rounded border border-yellow-200"><strong>역암 (자갈)</strong><br>굵은 자갈 섞임<br>다양한 크기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v14-c1", "text": "알갱이 사이에 녹아 있던 물질이 풀처럼 알갱이를 굳힙니다", "role": "퇴적암 교결 작용", "para_idx": 1},
            {"cue_id": "g4-v14-c2", "text": "주로 진흙이 굳은 것은 '이암', 모래가 굳은 것은 '사암', 자갈 사이에 모래와 진흙이 섞여 굳은 것은 '역암'", "role": "퇴적암 3종 분류", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "분류 매트릭스",
            "rock_type": "퇴적암",
            "sediments": {
                "이암": "진흙 (극미세 알갱이)",
                "사암": "모래 (중간 알갱이)",
                "역암": "자갈 + 모래 + 진흙 (굵은 알갱이)"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "분류 기준 세부 확인",
                "stem": "퇴적암을 '이암, 사암, 역암'으로 나누는 올바른 분류 기준은 무엇인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "퇴적암은 쌓인 알갱이의 크기에 따라 분류됩니다.",
                "options": [
                    {"label": "①", "text": "퇴적물을 이루는 알갱이의 크기", "is_correct": True, "formula": "정답", "explanation": "3문단에 명시된 퇴적암의 정확한 분류 기준입니다."},
                    {"label": "②", "text": "암석이 만들어진 나라의 이름", "is_correct": False, "formula": "D3", "explanation": "지리적 위치와 무관한 분류입니다."},
                    {"label": "③", "text": "암석을 파는 상점의 가격", "is_correct": False, "formula": "D1", "explanation": "상업적 기준입니다."},
                    {"label": "④", "text": "암석이 물에 뜨는지 가라앉는지의 여부", "is_correct": False, "formula": "D4", "explanation": "암석은 기본적으로 물에 가라앉습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "과정 순서 확인",
                "stem": "지층과 퇴적암이 만들어지는 순서로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "흐르는 물이 상류의 바위를 깎아 알갱이들을 운반하여 호수나 바다 바닥에 층을 이루어 퇴적시킵니다. 위에 새로운 퇴적물이 계속 쌓이면 아래쪽 퇴적물은 엄청난 무게로 꽉 눌리고,",
                "options": [
                    {"label": "①", "text": "운반 ➔ 퇴적(쌓임) ➔ 압축(눌림) ➔ 굳어짐", "is_correct": True, "formula": "정답", "explanation": "2문단에 서술된 지층과 퇴적암 형성의 정석적 과정입니다."},
                    {"label": "②", "text": "굳어짐 ➔ 바위 깎기 ➔ 물 증발", "is_correct": False, "formula": "D5", "explanation": "순서가 뒤죽박죽인 오답입니다."},
                    {"label": "③", "text": "화산 폭발 ➔ 용암 분출 ➔ 지층 사라짐", "is_correct": False, "formula": "D2", "explanation": "퇴적암이 아닌 화산 활동 내용입니다."},
                    {"label": "④", "text": "자갈 깨기 ➔ 공룡 발자국 지우기 ➔ 지층 완성", "is_correct": False, "formula": "D6", "explanation": "엉뚱한 허구입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 주로 '자갈'이 섞여 굳어진 퇴적암의 명칭은?",
                "options": [
                    {"label": "①", "text": "역암", "is_correct": True},
                    {"label": "②", "text": "사암", "is_correct": False},
                    {"label": "③", "text": "이암", "is_correct": False},
                    {"label": "④", "text": "현무암", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "자갈 사이에 모래와 진흙이 섞여 굳은 것은 '역암'이라고 부릅니다.", "is_correct": True},
                    {"label": "②", "text": "주로 진흙이 굳은 것은 '이암',", "is_correct": False},
                    {"label": "③", "text": "모래가 굳은 것은 '사암',", "is_correct": False},
                    {"label": "④", "text": "이렇게 굳어져 생긴 돌을 '퇴적암'이라고 합니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "퇴적암 3형제 분류 카드 쓰기",
            "guide": "이암, 사암, 역암의 퇴적물 알갱이를 짝지어 정리해 보세요.",
            "template": "진흙이 굳으면 [이암], 모래가 굳으면 [사암], 자갈이 섞여 굳으면 [역암]이 됩니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "퇴적암은 '진흙-이암', '모래-사암', '자갈-역암'을 짝지어 외워요."},
            "step1_2_drill": {"task": "퇴적물 크기별 암석 이름 카드 선 잇기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "퇴적암은 쌓인 알갱이의 크기에 따라 분류됩니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 시루떡 같은 바위 절벽",
            "situation": "고속도로 절벽이나 해안가 지층을 지나갈 때",
            "parent_question": "저 바위 절벽에 시루떡처럼 층층이 줄무늬가 생긴 까닭은 무엇일까?",
            "expected_answer": "오랜 세월 동안 바다 밑바닥에 모래와 진흙이 차곡차곡 쌓여 눌린 지층이래요!",
            "coaching_tip": "지층의 줄무늬를 지구 역사의 페이지처럼 상상해 보도록 대화해 주세요."
        }
    )
]

# We need to add remaining slots 5~16 for Grade 4 (V2-1 ~ W5)
# Let's add them systematically!
g4_remaining_slots_part2 = [
    # 5. V2-1
    build_expository_slot(
        grade_num=4,
        subskill_code="V2-1",
        subject="과학·환경 / 국어(낱말 짜임 4-2)",
        unit="3. 자원 순환과 환경",
        concept="자원을 살리는 두 가지 방법: 재활용(Recycling)과 새활용(Upcycling)",
        text_structure="비교·대조",
        structure_type_code="comparison",
        passage_title="버려지는 물건의 가치 있는 변신, 재활용과 새활용",
        paragraphs=[
            "환경 오염을 줄이고 자원을 아끼기 위해 버려진 쓰레기를 다시 활용하는 노력이 세계 곳곳에서 펼쳐지고 있습니다. 쓰레기를 다시 쓰는 방법에는 '재활용(Recycling)'과 '새활용(Upcycling)'이라는 두 가지 방식이 있습니다.",
            "재활용은 다 쓴 물건을 원래 재료 상태로 부수거나 녹여서 다시 같은 물건의 재료로 쓰는 것을 말합니다. 예를 들어 페트병을 녹여 플라스틱 칩을 만들거나, 헌 신문지를 녹여 재생종이를 만드는 것이 대표적입니다. 공정과 에너지 비용이 들지만 원자재 낭비를 막아 줍니다.",
            "반면에 새활용은 버려진 물건에 창의적인 디자인이나 기능을 더해 원래보다 훨씬 가치 높고 새로운 제품으로 재탄생시키는 방법입니다. 낡은 트럭 방수천을 멋진 가방으로 만들거나, 버려진 소방호스로 튼튼한 지갑을 만드는 것이 그 예입니다. 두 방식 모두 쓰레기를 줄이지만, 새활용은 예술성과 창의성을 더해 부가가치를 높인다는 차이가 있습니다."
        ],
        vocab_notes=[
            {"word": "부가가치", "definition": "창의력이나 기술을 더해 원래보다 높게 만들어 낸 새로운 가치"},
            {"word": "원자재", "definition": "물건을 만드는 데 바탕이 되는 원래의 재료"}
        ],
        visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
          <h4 class="font-bold text-teal-900 mb-2">♻️ 재활용(Recycling) vs ✨ 새활용(Upcycling)</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-teal-100"><th class="p-1 border border-teal-200">구분</th><th class="p-1 border border-teal-200">재활용 (리사이클링)</th><th class="p-1 border border-teal-200">새활용 (업사이클링)</th></tr>
            <tr><td class="p-1 border border-teal-200 font-bold bg-white">가공 방식</td><td class="p-1 border border-teal-200 bg-white">파쇄·용해하여 원료로 환원</td><td class="p-1 border border-teal-200 bg-white">디자인·아이디어 결합 재탄생</td></tr>
            <tr><td class="p-1 border border-teal-200 font-bold bg-white">대표 사례</td><td class="p-1 border border-teal-200 bg-white">폐지 ➔ 재생종이, 페트병 ➔ 솜</td><td class="p-1 border border-teal-200 bg-white">트럭 방수천 ➔ 명품 가방</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v21-c1", "text": "원래 재료 상태로 부수거나 녹여서 다시 같은 물건의 재료로 쓰는 것을 말합니다", "role": "재활용 개념 정의", "para_idx": 1},
            {"cue_id": "g4-v21-c2", "text": "버려진 물건에 창의적인 디자인이나 기능을 더해 원래보다 훨씬 가치 높고 새로운 제품으로 재탄생시키는", "role": "새활용 개념 정의", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "비교·대조 다이어그램",
            "common_goal": "자원 절약 및 쓰레기 감축",
            "approaches": {
                "재활용": "녹여서 원료로 되돌림 (기능 유지)",
                "새활용": "디자인을 더해 고부가가치 창출 (가치 상승)"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "개념 대조 파악",
                "stem": "'새활용(업사이클링)'이 '재활용'과 구별되는 가장 결정적인 차이점은 무엇인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "새활용은 예술성과 창의성을 더해 부가가치를 높인다는 차이가 있습니다.",
                "options": [
                    {"label": "①", "text": "창의적인 디자인과 기능을 더해 원래보다 높은 가치를 만든다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 새활용의 고유한 핵심 가치입니다."},
                    {"label": "②", "text": "물건을 무조건 땅속 깊이 파묻어 썩게 만든다.", "is_correct": False, "formula": "D3", "explanation": "매립에 대한 설명입니다."},
                    {"label": "③", "text": "모든 물건을 믹서기에 넣어 물과 함께 갈아 버린다.", "is_correct": False, "formula": "D1", "explanation": "단순 파쇄 재활용의 일부분입니다."},
                    {"label": "④", "text": "새 물건을 공장에서 대량 생산하여 싸게 판다.", "is_correct": False, "formula": "D4", "explanation": "자원 순환과 무관한 일반 생산입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 예시 연결",
                "stem": "글에서 든 '새활용'의 올바른 예시는 어느 것인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "낡은 트럭 방수천을 멋진 가방으로 만들거나, 버려진 소방호스로 튼튼한 지갑을 만드는 것이 그 예입니다.",
                "options": [
                    {"label": "①", "text": "낡은 트럭 방수천으로 멋진 가방을 만든 것", "is_correct": True, "formula": "정답", "explanation": "3문단에 제시된 명확한 새활용 사례입니다."},
                    {"label": "②", "text": "페트병을 녹여 플라스틱 칩을 만든 것", "is_correct": False, "formula": "D2", "explanation": "재활용(Recycling)의 사례입니다."},
                    {"label": "③", "text": "신문지를 녹여 재생종이를 만든 것", "is_correct": False, "formula": "D2", "explanation": "재활용의 사례입니다."},
                    {"label": "④", "text": "유리병을 깨뜨려 모래사장에 뿌린 것", "is_correct": False, "formula": "D5", "explanation": "환경 파괴 행위입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 재활용과 새활용이 공통적으로 추구하는 환경적 목표는?",
                "options": [
                    {"label": "①", "text": "쓰레기를 줄이고 지구의 소중한 자원을 절약하기 위해", "is_correct": True},
                    {"label": "②", "text": "모든 공장의 문을 닫게 만들기 위해", "is_correct": False},
                    {"label": "③", "text": "종이와 플라스틱 사용을 무한정 늘리기 위해", "is_correct": False},
                    {"label": "④", "text": "바다를 메워 육지로 만들기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "환경 오염을 줄이고 자원을 아끼기 위해 버려진 쓰레기를 다시 활용하는 노력이", "is_correct": True},
                    {"label": "②", "text": "재활용은 다 쓴 물건을 원래 재료 상태로 부수거나", "is_correct": False},
                    {"label": "③", "text": "두 방식 모두 쓰레기를 줄이지만,", "is_correct": False},
                    {"label": "④", "text": "낡은 트럭 방수천을 멋진 가방으로 만들거나,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "재활용과 새활용 비교 요약문 작성하기",
            "guide": "두 개념의 차이점을 한 문장으로 대조해 보세요.",
            "template": "재활용은 재료를 녹여 다시 쓰지만, 새활용은 [창의적인 디자인]을 더해 더 멋진 [새로운 가치]를 만들어 냅니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "재활용(원료 환원)과 새활용(가치 상승)의 차이를 구별해요."},
            "step1_2_drill": {"task": "페트병 솜(재활용) vs 소방호스 지갑(새활용) 카드 분류하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "새활용은 버려진 물건에 디자인을 더해 새로운 가치를 부여합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 버려진 물건의 재탄생",
            "situation": "집에서 분리수거를 하거나 헌 옷을 정리할 때",
            "parent_question": "안 입는 청바지로 예쁜 에코백을 만들었다면 이건 재활용일까, 새활용일까?",
            "expected_answer": "디자인과 새 아이디어를 더해 더 멋진 가방으로 바꿨으니까 '새활용'이에요!",
            "coaching_tip": "생활 속 업사이클링 아이디어를 아이와 함께 상상해 보세요."
        }
    ),

    # 6. V2-2
    build_expository_slot(
        grade_num=4,
        subskill_code="V2-2",
        subject="사회(경제·교류 4-2)",
        unit="2. 화폐와 경제 생활",
        concept="물물교환의 불편함에서 디지털 화폐까지의 발달 과정",
        text_structure="문제·해결 + 시간 순서",
        structure_type_code="problem_solution",
        passage_title="조개껍데기에서 모바일 페이까지 화폐의 발달",
        paragraphs=[
            "사람들이 필요한 물건을 얻기 위해 서로 가진 것을 바꾸던 먼 옛날의 방식을 '물물교환'이라고 합니다. 하지만 쌀과 물고기를 바꾸려 할 때 서로 원하는 시기나 가치가 맞지 않고, 무거운 물건을 멀리 들고 다니기 힘들다는 심각한 문제가 발생했습니다.",
            "사람들은 이러한 물물교환의 불편함을 해결하기 위해 누구나 귀하게 여기는 조개껍데기나 곡식, 소금을 '물품 화폐'로 정해 거래하기 시작했습니다. 이후 녹슬지 않고 보관이 편리한 금·은·구리 등의 '금속 화폐(동전)'가 등장했고, 휴대가 간편한 종이 형태의 '지폐'가 널리 쓰이게 되었습니다.",
            "오늘날에는 과학 기술의 발달로 실물 지폐 없이도 카드나 스마트폰 터치 한 번으로 결제하는 '전자 화폐와 모바일 페이'가 일상화되었습니다. 화폐의 역사는 거래의 편리성과 안전성을 높이기 위해 문제를 해결해 온 과정입니다."
        ],
        vocab_notes=[
            {"word": "물물교환", "definition": "돈을 매개로 하지 않고 물건과 물건을 직접 맞바꾸는 일"},
            {"word": "모바일 페이", "definition": "스마트폰을 이용하여 대금을 전자적으로 결제하는 방식"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">💰 화폐 발달의 4단계 진화 과정</h4>
          <div class="grid grid-cols-4 gap-1 text-xs text-center">
            <div class="p-1 bg-white rounded border border-amber-200">1. 물물교환<br>물건 직접 교환</div>
            <div class="p-1 bg-white rounded border border-amber-200">2. 물품화폐<br>조개, 곡식, 소금</div>
            <div class="p-1 bg-white rounded border border-amber-200">3. 금속·지폐<br>동전, 종이돈</div>
            <div class="p-1 bg-white rounded border border-amber-200">4. 디지털화폐<br>모바일 페이, 카드</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v22-c1", "text": "서로 원하는 시기나 가치가 맞지 않고, 무거운 물건을 멀리 들고 다니기 힘들다는 심각한 문제가 발생했습니다", "role": "물물교환의 문제점", "para_idx": 0},
            {"cue_id": "g4-v22-c2", "text": "스마트폰 터치 한 번으로 결제하는 '전자 화폐와 모바일 페이'가 일상화되었습니다", "role": "현대 디지털 화폐", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "문제-해결 발전사",
            "stages": [
                {"problem": "물물교환 불편 (운반 곤란, 가치 불일치)", "solution": "물품화폐 (조개껍데기, 소금)"},
                {"problem": "부피와 무게 한계", "solution": "금속 화폐(동전) 및 지폐 등장"},
                {"problem": "분실 위험과 휴대 불편", "solution": "전자 화폐 및 모바일 페이"}
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "문제-해결 인과 확인",
                "stem": "인류가 '화폐'를 발명하게 된 가장 근본적인 문제점은 무엇이었나요?",
                "target_para_idx": 0,
                "spotlight_quote": "서로 원하는 시기나 가치가 맞지 않고, 무거운 물건을 멀리 들고 다니기 힘들다는 심각한 문제가 발생했습니다.",
                "options": [
                    {"label": "①", "text": "물물교환 시 가치가 맞지 않고 무거운 물건을 운반하기 힘들어서", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 물물교환의 핵심 한계입니다."},
                    {"label": "②", "text": "모든 시장의 상인들이 장사를 그만두어서", "is_correct": False, "formula": "D3", "explanation": "본문과 무관한 서술입니다."},
                    {"label": "③", "text": "지구의 소금과 쌀이 전부 사라져서", "is_correct": False, "formula": "D1", "explanation": "허구의 오답입니다."},
                    {"label": "④", "text": "스마트폰을 먼저 만든 뒤 쓸 돈이 필요해서", "is_correct": False, "formula": "D4", "explanation": "시대 순서가 뒤바뀐 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "역사적 발전 순서 확인",
                "stem": "화폐의 발달 순서로 올바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "누구나 귀하게 여기는 조개껍데기나 곡식, 소금을 '물품 화폐'로 정해 거래하기 시작했습니다. 이후 녹슬지 않고 보관이 편리한 금·은·구리 등의 '금속 화폐(동전)'가 등장했고,",
                "options": [
                    {"label": "①", "text": "물물교환 ➔ 물품 화폐 ➔ 금속 화폐·지폐 ➔ 전자 화폐", "is_correct": True, "formula": "정답", "explanation": "글 전체의 시간 순서에 부합하는 정답입니다."},
                    {"label": "②", "text": "전자 화폐 ➔ 물품 화폐 ➔ 지폐 ➔ 물물교환", "is_correct": False, "formula": "D2", "explanation": "순서가 거꾸로인 오답입니다."},
                    {"label": "③", "text": "지폐 ➔ 조개껍데기 ➔ 모바일 페이 ➔ 금화", "is_correct": False, "formula": "D5", "explanation": "역사적 순서가 왜곡되었습니다."},
                    {"label": "④", "text": "물물교환 ➔ 모바일 페이 ➔ 동전 ➔ 소금 화폐", "is_correct": False, "formula": "D6", "explanation": "디지털 화폐가 먼저 올 수 없습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 금속 화폐나 지폐가 조개껍데기보다 편리했던 까닭은?",
                "options": [
                    {"label": "①", "text": "보관과 휴대가 간편하고 가치가 일정하게 보존되기 때문에", "is_correct": True},
                    {"label": "②", "text": "음식으로 끓여 먹을 수 있어서", "is_correct": False},
                    {"label": "③", "text": "물에 넣으면 녹아 사라지기 때문에", "is_correct": False},
                    {"label": "④", "text": "모양이 울퉁불퉁해서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "녹슬지 않고 보관이 편리한 금·은·구리 등의 '금속 화폐(동전)'가 등장했고, 휴대가 간편한 종이 형태의 '지폐'가", "is_correct": True},
                    {"label": "②", "text": "사람들이 필요한 물건을 얻기 위해", "is_correct": False},
                    {"label": "③", "text": "조개껍데기나 곡식, 소금을 '물품 화폐'로 정해", "is_correct": False},
                    {"label": "④", "text": "오늘날에는 과학 기술의 발달로", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "화폐 발달사 요약 타임라인 작성하기",
            "guide": "화폐가 발전해 온 과정을 순서대로 화살표로 정리해 보세요.",
            "template": "[물물교환] ➔ 조개껍데기 등 [물품 화폐] ➔ 동전과 [지폐] ➔ 스마트폰의 [전자 화폐]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "화폐 발달사는 '불편함(문제) ➔ 해결책(새 화폐)'의 흐름으로 이해해요."},
            "step1_2_drill": {"task": "화폐 종류 카드(조개, 동전, 지폐, 모바일) 시대순 나열하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "화폐는 거래의 편리함과 안전성을 높이기 위해 발전해 왔습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 보이지 않는 돈",
            "situation": "마트에서 스마트폰이나 카드로 결제할 때",
            "parent_question": "스마트폰만 띡 대도 결제가 되는 건 옛날의 돈과 어떻게 다를까?",
            "expected_answer": "옛날엔 무거운 소금이나 동전을 들고 다녔지만, 지금은 숫자가 전자로 오가는 전자 화폐예요!",
            "coaching_tip": "화폐의 본질이 '신뢰와 약속'임을 자연스럽게 대화해 보세요."
        }
    )
]

# Note: We now combine g4_expository_slots (3) + g4_remaining_slots (1) + g4_remaining_slots_part2 (2) = 6 slots.
# We still need slots 7 to 16 (10 slots) for Grade 4.
# Let's inspect the remaining concepts for Grade 4:
# 7. V2-3: 촌락과 도시의 인구 이동 추이와 미래 변화 (Flagship slot! We can import from commercialMasterData.json grades_data[3])
# 8. V2-4: 자원의 희소성과 용돈을 현명하게 쓰는 합리적 선택
# 9. V3-1: 손전등과의 거리에 따른 그림자 크기 변화와 시각별 기온 변화 (꺾은선그래프)
# 10. V3-2: 초등학생 여가 활동과 스마트폰 이용 실태 설명 자료 비교
# 11. V3-3: 조선 시대의 과학적인 빗물 측정기 ‘측우기’ (인쇄 도서 ㉮ + 웹 백과 ㉯)
# 12. W1: ‘지구’라는 넓은 주제를 ‘공룡과 산호 화석이 만들어지는 과정’으로 좁히기
# 13. W2: 도시의 쓰레기 발생량 변화와 해결 노력 설명 자료 수집·선별
# 14. W3: 지도의 ‘축척’과 ‘등고선’ 읽는 방법 3단 구성 개요 짜기
# 15. W4: 우리 몸을 움직이는 ‘뼈’와 ‘근육’의 역할과 운동 시간 그래프
# 16. W5: 염전에서 바닷물로 소금을 얻는 과정 설명문 초안 고쳐쓰기

# Let's load the flagship slot for G4 (V2-3) from commercialMasterData.json
with open(os.path.join(os.path.dirname(SCRIPT_DIR), "webapp", "src", "data", "commercialMasterData.json"), "r", encoding="utf-8") as f:
    cmd_data = json.load(f)

g4_flagship_v23 = None
for gd in cmd_data.get("grades_data", []):
    if gd.get("slot_id") == "G4-EXP-V2-3":
        g4_flagship_v23 = gd
        break

print(f"Loaded G4 Flagship slot G4-EXP-V2-3: {g4_flagship_v23 is not None}")

g4_remaining_slots_part3 = [
    # 8. V2-4
    build_expository_slot(
        grade_num=4,
        subskill_code="V2-4",
        subject="사회(생산과 소비 4-2)",
        unit="1. 현명한 경제 선택",
        concept="자원의 희소성과 용돈을 현명하게 쓰는 합리적 선택",
        text_structure="정의·인과·예시",
        structure_type_code="causal",
        passage_title="자원의 희소성과 슬기로운 소비 생활",
        paragraphs=[
            "우리가 살아가면서 갖고 싶거나 누리고 싶은 인간의 욕망은 끝이 없습니다. 하지만 이를 충족시켜 줄 돈이나 시간, 물건은 언제나 한정되어 있습니다. 이처럼 사람들의 욕구에 비해 이를 만족시켜 줄 자원이 부족한 상태를 '자원의 희소성'이라고 부릅니다.",
            "자원이 희소하기 때문에 우리는 매 순간 무엇을 선택하고 무엇을 포기해야 할지 고민해야 합니다. 한정된 용돈으로 장난감을 살지, 아니면 책을 살지 결정할 때처럼 말입니다. 이때 한 가지를 선택함으로써 포기해야 하는 다른 것의 가치를 '기회비용'이라고 합니다.",
            "따라서 우리는 적은 비용으로 가장 큰 만족을 얻을 수 있는 '합리적 선택'을 해야 합니다. 물건을 사기 전에 꼭 필요한 물건인지, 가격은 적당한지 꼼꼼하게 따져보는 용돈 기입장 쓰기는 합리적 소비의 훌륭한 첫걸음입니다."
        ],
        vocab_notes=[
            {"word": "자원의 희소성", "definition": "인간의 욕망에 비해 이를 채워 줄 자원의 양이 상대적으로 부족한 상태"},
            {"word": "기회비용", "definition": "어떤 것을 선택했을 때 포기해야 하는 대안 중 가장 가치 있는 것"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">⚖️ 합리적 선택의 경제 저울</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-amber-200"><strong>자원의 희소성:</strong> 욕구(무한) ＞ 자원(한정)</div>
            <div class="p-1 bg-white rounded border border-amber-200"><strong>기회비용:</strong> 선택 A를 위해 포기한 대안 B의 가치</div>
            <div class="p-1 bg-white rounded border border-amber-200"><strong>합리적 소비:</strong> 편익(만족) ＞ 기회비용 (용돈 기입장 활용)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v24-c1", "text": "사람들의 욕구에 비해 이를 만족시켜 줄 자원이 부족한 상태를 '자원의 희소성'이라고 부릅니다", "role": "자원의 희소성 정의", "para_idx": 0},
            {"cue_id": "g4-v24-c2", "text": "한 가지를 선택함으로써 포기해야 하는 다른 것의 가치를 '기회비용'이라고 합니다", "role": "기회비용 정의", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "경제 원리 흐름도",
            "flow": ["욕망 무한 vs 자원 한정", "자원의 희소성 발생", "선택과 기회비용 직면", "합리적 소비 실천"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "개념 정의 확인",
                "stem": "글에서 설명한 '기회비용'의 올바른 뜻은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "이때 한 가지를 선택함으로써 포기해야 하는 다른 것의 가치를 '기회비용'이라고 합니다.",
                "options": [
                    {"label": "①", "text": "어떤 것을 선택함으로써 포기해야 하는 다른 대안의 가치", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 기회비용의 정의입니다."},
                    {"label": "②", "text": "가게에서 물건을 살 때 내는 거스름돈", "is_correct": False, "formula": "D3", "explanation": "거스름돈과 무관한 경제 개념입니다."},
                    {"label": "③", "text": "은행에 돈을 저금했을 때 받는 이자", "is_correct": False, "formula": "D2", "explanation": "이자 개념입니다."},
                    {"label": "④", "text": "물건이 고장 났을 때 내는 수리비", "is_correct": False, "formula": "D1", "explanation": "단순 수리 비용입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "인과 및 행동 대안 파악",
                "stem": "자원의 희소성 때문에 일상에서 우리가 실천해야 할 가장 바람직한 행동은?",
                "target_para_idx": 2,
                "spotlight_quote": "따라서 우리는 적은 비용으로 가장 큰 만족을 얻을 수 있는 '합리적 선택'을 해야 합니다.",
                "options": [
                    {"label": "①", "text": "적은 비용으로 가장 큰 만족을 얻는 합리적 선택을 한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 제시된 합리적 소비의 지향점입니다."},
                    {"label": "②", "text": "용돈이 생기는 즉시 생각 없이 다 써 버린다.", "is_correct": False, "formula": "D4", "explanation": "낭비적이고 비합리적인 행동입니다."},
                    {"label": "③", "text": "물건의 품질이나 가격을 전혀 따지지 않고 비싼 것만 산다.", "is_correct": False, "formula": "D5", "explanation": "비합리적 과소비입니다."},
                    {"label": "④", "text": "용돈 기입장을 찢어 버린다.", "is_correct": False, "formula": "D6", "explanation": "엉뚱한 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 인간의 경제생활에서 '선택의 고민'이 발생하는 근본 원인은?",
                "options": [
                    {"label": "①", "text": "인간의 욕망에 비해 쓸 수 있는 자원이 한정되어 있기 때문에", "is_correct": True},
                    {"label": "②", "text": "가게의 물건이 너무 많아 어지럽기 때문에", "is_correct": False},
                    {"label": "③", "text": "용돈 기입장이 너무 무겁기 때문에", "is_correct": False},
                    {"label": "④", "text": "지폐의 색깔이 마음에 들지 않아서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "이처럼 사람들의 욕구에 비해 이를 만족시켜 줄 자원이 부족한 상태를 '자원의 희소성'이라고 부릅니다.", "is_correct": True},
                    {"label": "②", "text": "우리가 살아가면서 갖고 싶거나 누리고 싶은 인간의 욕망은 끝이 없습니다.", "is_correct": False},
                    {"label": "③", "text": "자원이 희소하기 때문에 우리는 매 순간", "is_correct": False},
                    {"label": "④", "text": "따라서 우리는 적은 비용으로 가장 큰 만족을 얻을 수 있는", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "나의 합리적 소비 계획 쓰기",
            "guide": "용돈을 쓸 때 기회비용을 고려하는 다짐을 한 문장으로 써 보세요.",
            "template": "나는 [자원의 희소성]을 기억하고, 포기해야 하는 [기회비용]을 신중히 따져 [합리적 선택]을 하겠습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "희소성 ➔ 선택의 문제 ➔ 기회비용의 논리적 고리를 파악해요."},
            "step1_2_drill": {"task": "합리적 선택(O)과 충동구매(X) 사례 구별하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "한정된 자원으로 최대의 만족을 얻는 것을 합리적 선택이라 합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 마트에서의 선택과 포기",
            "situation": "마트에서 아이가 두 가지 장난감을 모두 사달라고 조를 때",
            "parent_question": "두 개를 다 살 수 없을 때 하나를 고르고 다른 하나를 포기하는 걸 경제학에서 뭐라고 부를까?",
            "expected_answer": "포기한 장난감의 가치를 '기회비용'이라고 부르고, 더 만족이 큰 걸 고르는 게 '합리적 선택'이래요!",
            "coaching_tip": "현명한 경제 습관을 스스로 깨닫도록 기회비용의 개념을 따뜻하게 가르쳐 주세요."
        }
    ),

    # 9. V3-1
    build_expository_slot(
        grade_num=4,
        subskill_code="V3-1",
        subject="수학(꺾은선그래프 4-2) / 과학(빛과 그림자)",
        unit="3. 시간에 따른 변화와 그래프",
        concept="손전등과의 거리에 따른 그림자 크기 변화와 시각별 기온 변화",
        text_structure="인과·비교",
        structure_type_code="causal",
        passage_title="시간의 흐름과 연속적 변화를 보여주는 꺾은선그래프",
        paragraphs=[
            "수학에서 시간에 따라 연속적으로 변화하는 수치를 나타낼 때는 막대그래프보다 점들을 선분으로 이은 '꺾은선그래프'를 사용하는 것이 훨씬 효과적입니다. 선의 기울기를 보면 수치가 증가하는지 감소하는지 한눈에 알아볼 수 있습니다.",
            "예를 들어 맑은 날 아침 9시부터 오후 3시까지 측정한 시각별 기온 변화를 꺾은선그래프로 그리면, 정오를 지나 오후 2시 무렵에 기온이 가장 높게 치솟는 추세를 쉽게 파악할 수 있습니다. 기울기가 가파를수록 기온이 급격히 변했음을 뜻합니다.",
            "과학 실험에서도 물체와 손전등 사이의 거리가 가까워질수록 스크린에 생기는 그림자의 크기가 급격히 커지는 연속적 변화를 꺾은선그래프로 나타낼 수 있습니다. 그래프를 읽을 때는 가로축과 세로축의 눈금 단위와 선의 기울기를 정확히 분석해야 합니다."
        ],
        vocab_notes=[
            {"word": "꺾은선그래프", "definition": "수량을 점으로 찍고 그 점들을 선분으로 이어 변화를 나타낸 그래프"},
            {"word": "기울기", "definition": "그래프에서 선분이 기울어진 정도로, 변화의 빠르기를 나타냄"}
        ],
        visual_html="""<div class="p-3 bg-indigo-50 rounded border border-indigo-200">
          <h4 class="font-bold text-indigo-900 mb-2">📈 시각별 기온 변화 꺾은선그래프 분석</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-indigo-200"><strong>가로축:</strong> 시각 (9시 ➔ 11시 ➔ 13시 ➔ 15시)</div>
            <div class="p-1 bg-white rounded border border-indigo-200"><strong>세로축:</strong> 기온 (℃, 눈금 한 칸 = 1℃)</div>
            <div class="p-1 bg-white rounded border border-indigo-200"><strong>기울기:</strong> 11시~13시 급상승(가파름), 14시 최고 기온 도달</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v31-c1", "text": "시간에 따라 연속적으로 변화하는 수치를 나타낼 때는 막대그래프보다 점들을 선분으로 이은 '꺾은선그래프'를", "role": "꺾은선그래프 용도", "para_idx": 0},
            {"cue_id": "g4-v31-c2", "text": "기울기가 가파를수록 기온이 급격히 변했음을 뜻합니다", "role": "기울기 해석 원리", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "그래프 해석 프레임워크",
            "graph_components": {
                "축 확인": "가로축(시간), 세로축(측정값·단위)",
                "기울기 해석": "가파름(급변), 완만함(서서히 변화)",
                "추세 예측": "상승/하강 추세 파악"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "시각 자료 그래프 해석",
                "stem": "꺾은선그래프에서 '선의 기울기가 매우 가파르다'는 것은 무엇을 의미하나요?",
                "target_para_idx": 1,
                "spotlight_quote": "기울기가 가파를수록 기온이 급격히 변했음을 뜻합니다.",
                "options": [
                    {"label": "①", "text": "수치가 짧은 시간 동안 급격하게 변화했음을 뜻한다.", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 기울기의 수학적 의미입니다."},
                    {"label": "②", "text": "온도가 얼음점 아래로 떨어져 얼어붙었음을 뜻한다.", "is_correct": False, "formula": "D3", "explanation": "기울기와 무관한 절대 온도 수치입니다."},
                    {"label": "③", "text": "그래프를 잘못 그려서 종이를 찢어야 함을 뜻한다.", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                    {"label": "④", "text": "시간이 완전히 멈추어 변화가 없음을 뜻한다.", "is_correct": False, "formula": "D4", "explanation": "기울기가 평평할 때의 해석입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "그래프 유형 적절성 평가",
                "stem": "'시간에 따른 연속적 변화'를 나타낼 때 막대그래프보다 꺾은선그래프가 적절한 까닭은?",
                "target_para_idx": 0,
                "spotlight_quote": "선의 기울기를 보면 수치가 증가하는지 감소하는지 한눈에 알아볼 수 있습니다.",
                "options": [
                    {"label": "①", "text": "선의 기울기로 증가와 감소의 변화 추세를 한눈에 볼 수 있어서", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 꺾은선그래프의 핵심 장점입니다."},
                    {"label": "②", "text": "막대그래프보다 알록달록 색칠하기가 훨씬 쉬워서", "is_correct": False, "formula": "D2", "explanation": "단순 미술적 이유가 아닙니다."},
                    {"label": "③", "text": "숫자를 하나도 쓰지 않고 점만 찍어도 되어서", "is_correct": False, "formula": "D5", "explanation": "눈금 수치는 반드시 읽어야 합니다."},
                    {"label": "④", "text": "막대그래프는 수학책에 나오지 않아서", "is_correct": False, "formula": "D6", "explanation": "사실과 다른 거짓 진술입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 맑은 날 하루 중 기온이 가장 높게 치솟는 일반적인 시간대는?",
                "options": [
                    {"label": "①", "text": "정오를 지난 오후 2시 무렵", "is_correct": True},
                    {"label": "②", "text": "새벽 3시 한밤중", "is_correct": False},
                    {"label": "③", "text": "아침 6시 해 뜰 무렵", "is_correct": False},
                    {"label": "④", "text": "밤 11시 취침 시간", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "정오를 지나 오후 2시 무렵에 기온이 가장 높게 치솟는 추세를 쉽게 파악할 수 있습니다.", "is_correct": True},
                    {"label": "②", "text": "수학에서 시간에 따라 연속적으로 변화하는 수치를 나타낼 때는", "is_correct": False},
                    {"label": "③", "text": "과학 실험에서도 물체와 손전등 사이의 거리가", "is_correct": False},
                    {"label": "④", "text": "가로축과 세로축의 눈금 단위와 선의 기울기를", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "꺾은선그래프 분석 보고서 작성",
            "guide": "가로축, 세로축, 기울기 변화를 해석하는 한 문장을 써 보세요.",
            "template": "가로축의 [시간]이 흐름에 따라 기온이 올라가며, 기울기가 가장 가파른 구간에서 온도가 [급격히] 상승했습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "꺾은선그래프는 '가로축/세로축 눈금'과 '선의 기울기 추세'를 분석해요."},
            "step1_2_drill": {"task": "기온 꺾은선그래프에서 최고점과 최저점 찾기 훈련"},
            "step3_vaccine": {"ox_quiz": [{"statement": "꺾은선그래프의 가파른 선은 급격한 변화를 나타냅니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 일기예보의 꺾은선그래프",
            "situation": "TV 일기예보나 스마트폰 날씨 앱의 기온 그래프를 볼 때",
            "parent_question": "스마트폰 날씨 화면에서 선이 위로 솟아오르면 기온이 어떻게 변한다는 뜻일까?",
            "expected_answer": "선이 위로 가파르게 올라가면 낮에 날씨가 점점 더 따뜻해진다는 뜻이에요!",
            "coaching_tip": "실생활 속 날씨 그래프를 함께 보며 기울기와 변화의 관계를 읽게 해 주세요."
        }
    ),

    # 10. V3-2
    build_expository_slot(
        grade_num=4,
        subskill_code="V3-2",
        subject="사회(정보와 매체 4-2)",
        unit="2. 미디어와 현대 생활",
        concept="초등학생 여가 활동과 스마트폰 이용 실태 설명 자료 비교",
        text_structure="열거·비교",
        structure_type_code="comparison",
        passage_title="초등학생의 여가 활동과 스마트폰 이용의 명암",
        paragraphs=[
            "현대 초등학생들의 방과 후 여가 생활에서 스마트폰은 빼놓을 수 없는 필수 매체로 자리 잡았습니다. 교육청 조사 통계에 따르면 초등 4학년 학생 10명 중 8명 이상이 스마트폰을 보유하고 있으며, 하루 평균 2시간 이상 이용하는 것으로 나타났습니다.",
            "스마트폰은 학습에 유익한 정보를 신속히 검색하고 친구들과 편리하게 소통하며 스트레스를 해소하는 긍정적인 역할을 합니다. 교육용 앱을 활용해 외국어를 배우거나 과학 원리를 영상으로 쉽게 이해할 수도 있습니다.",
            "그러나 스마트폰 과의존으로 인해 야외 신체 활동이 급격히 줄어들고, 수면 부족이나 거북목 증후군 같은 건강 문제가 나타나기도 합니다. 설명 자료를 읽을 때는 편리한 장점만을 일방적으로 찬양한 글인지, 문제점까지 객관적으로 균형 있게 다루었는지 비판적으로 평가해야 합니다."
        ],
        vocab_notes=[
            {"word": "과의존", "definition": "특정한 물질이나 기기에 지나치게 기대어 스스로 조절하지 못하는 상태"},
            {"word": "거북목 증후군", "definition": "목을 앞으로 뺀 자세가 굳어져 통증과 피로를 유발하는 신체 증상"}
        ],
        visual_html="""<div class="p-3 bg-purple-50 rounded border border-purple-200">
          <h4 class="font-bold text-purple-900 mb-2">📱 초등학생 스마트폰 이용 명암 비교</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-purple-100"><th class="p-1 border border-purple-200">구분</th><th class="p-1 border border-purple-200">밝은 면 (긍정적 효과)</th><th class="p-1 border border-purple-200">어두운 면 (부정적 문제)</th></tr>
            <tr><td class="p-1 border border-purple-200 font-bold bg-white">생활·학습</td><td class="p-1 border border-purple-200 bg-white">신속한 정보 검색, 학습 앱 활용</td><td class="p-1 border border-purple-200 bg-white">신체 활동 부족, 학업 집중도 저하</td></tr>
            <tr><td class="p-1 border border-purple-200 font-bold bg-white">신체·건강</td><td class="p-1 border border-purple-200 bg-white">스트레스 완화, 소통</td><td class="p-1 border border-purple-200 bg-white">수면 부족, 시력 저하, 거북목 증후군</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v32-c1", "text": "학습에 유익한 정보를 신속히 검색하고 친구들과 편리하게 소통하며", "role": "스마트폰 긍정적 측면", "para_idx": 1},
            {"cue_id": "g4-v32-c2", "text": "편리한 장점만을 일방적으로 찬양한 글인지, 문제점까지 객관적으로 균형 있게 다루었는지", "role": "자료 신뢰성·객관성 비판 준거", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "양면성 비교 분석도",
            "topic": "초등 스마트폰 이용",
            "positive": ["정보 검색", "학습용 앱", "친구 소통"],
            "negative": ["야외 활동 부족", "수면 장애", "거북목 통증"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "자료의 객관성·공정성 평가",
                "stem": "스마트폰 이용에 관한 글을 비판적으로 읽을 때 가장 올바른 평가 기준은?",
                "target_para_idx": 2,
                "spotlight_quote": "편리한 장점만을 일방적으로 찬양한 글인지, 문제점까지 객관적으로 균형 있게 다루었는지 비판적으로 평가해야 합니다.",
                "options": [
                    {"label": "①", "text": "장점과 문제점을 한쪽에 치우치지 않고 균형 있게 다루었는지 확인한다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 미디어 설명 자료의 균형성 평가 준거입니다."},
                    {"label": "②", "text": "스마트폰 가격이 비싼 회사 제품만 칭찬하는지 확인한다.", "is_correct": False, "formula": "D3", "explanation": "상업적 편향을 조장하는 잘못된 태도입니다."},
                    {"label": "③", "text": "글쓴이가 스마트폰 게임 1등인지 확인한다.", "is_correct": False, "formula": "D1", "explanation": "게임 실력과 무관한 평가입니다."},
                    {"label": "④", "text": "단점이 전혀 없는 완벽한 기계라고 주장하는 글만 믿는다.", "is_correct": False, "formula": "D4", "explanation": "비판적 태도가 결여된 맹신입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 문제점 확인",
                "stem": "스마트폰 과의존으로 발생할 수 있는 신체 건강상의 문제로 글에 나온 것은?",
                "target_para_idx": 2,
                "spotlight_quote": "수면 부족이나 거북목 증후군 같은 건강 문제가 나타나기도 합니다.",
                "options": [
                    {"label": "①", "text": "수면 부족과 거북목 증후군", "is_correct": True, "formula": "정답", "explanation": "3문단에 구체적으로 언급된 신체 질환입니다."},
                    {"label": "②", "text": "치아가 갑자기 빠지는 풍치", "is_correct": False, "formula": "D2", "explanation": "글에 언급되지 않은 치과 질환입니다."},
                    {"label": "③", "text": "다리가 길어지는 성장통", "is_correct": False, "formula": "D5", "explanation": "부정적 질환과 거리가 멉니다."},
                    {"label": "④", "text": "귓바퀴가 커지는 이명 현상", "is_correct": False, "formula": "D6", "explanation": "본문에 없는 내용입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 스마트폰을 긍정적으로 활용하는 올바른 방법은?",
                "options": [
                    {"label": "①", "text": "학습 앱을 활용해 과학 원리를 이해하고 필요할 때 유익한 정보를 검색한다.", "is_correct": True},
                    {"label": "②", "text": "밤새도록 불을 끄고 자극적인 동영상만 본다.", "is_correct": False},
                    {"label": "③", "text": "공부 시간에 몰래 게임을 한다.", "is_correct": False},
                    {"label": "④", "text": "친구의 비밀 사진을 몰래 퍼뜨린다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "교육용 앱을 활용해 외국어를 배우거나 과학 원리를 영상으로 쉽게 이해할 수도 있습니다.", "is_correct": True},
                    {"label": "②", "text": "교육청 조사 통계에 따르면 초등 4학년 학생 10명 중", "is_correct": False},
                    {"label": "③", "text": "그러나 스마트폰 과의존으로 인해", "is_correct": False},
                    {"label": "④", "text": "현대 초등학생들의 방과 후 여가 생활에서", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "스마트폰 균형 시각 글쓰기",
            "guide": "스마트폰의 장점 1가지와 문제점 1가지를 균형 있게 한 문장으로 써 보세요.",
            "template": "스마트폰은 [정보 검색]에 유익하지만, 지나치게 쓰면 [거북목 증후군]이나 수면 부족을 일으킬 수 있습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "자료를 읽을 때는 장점만 쓴 편향된 글인지, 단점도 다룬 균형 잡힌 글인지 평가해요."},
            "step1_2_drill": {"task": "스마트폰 장점 카드와 부작용 카드 대조 분석하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "설명 자료는 한쪽 입장만 칭찬하기보다 객관적 사실을 균형 있게 다루어야 합니다.", "answer": "O", "reason": "비판적 독해의 핵심 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 스마트폰과의 건강한 거리",
            "situation": "식사 후 스마트폰 이용 시간에 대해 규칙을 정할 때",
            "parent_question": "스마트폰을 너무 오래 들여다보면 우리 몸과 마음에 어떤 신호가 올까?",
            "expected_answer": "목이 뻐근해지는 거북목이 오거나 밤에 잠이 안 올 수 있어서, 시간을 정해 두고 써야 해요!",
            "coaching_tip": "무조건 금지하기보다 신체적·학습적 영향을 스스로 인지하여 규칙을 정하도록 도와주세요."
        }
    ),

    # 11. V3-3
    build_expository_slot(
        grade_num=4,
        subskill_code="V3-3",
        subject="사회·과학(문화유산 4-1)",
        unit="3. 조상의 과학 유산",
        concept="조선 시대의 과학적인 빗물 측정기 ‘측우기’ (인쇄 도서 ㉮ + 웹 백과 ㉯)",
        text_structure="분석·인과 통합",
        structure_type_code="analysis",
        passage_title="하늘에서 내린 비의 양을 잰 과학 유산, 측우기",
        paragraphs=[
            "[도서 자료 ㉮] 조선 세종 대에 발명된 '측우기'는 세계 최초의 표준 강우량 측정기입니다. 측우기가 발명되기 전에는 비가 땅속 몇 치 깊이까지 스며들었는지를 흙을 파서 쟀으나, 흙의 마른 정도에 따라 깊이가 달라 정확하지 못했습니다.",
            "[웹 백과 자료 ㉯] 측우기는 원통형 구리 그릇에 빗물을 받아 '주척'이라는 자로 고인 물의 깊이를 푼(分) 단위까지 정밀하게 측정했습니다. 그릇의 지름(약 14cm)과 높이(약 42cm)를 전국적으로 통일하여 서울뿐 아니라 전국 각 고을의 강우량을 동일한 기준으로 측정해 농사와 홍수 대비에 활용했습니다.",
            "두 자료를 종합해 보면, 측우기는 '부정확했던 과거 방식(자료 ㉮)'을 극복하고, '전국 표준 규격과 자(주척)를 도입(자료 ㉯)'하여 조선의 농업 생산성을 비약적으로 높인 세계적 과학 발명품임을 알 수 있습니다."
        ],
        vocab_notes=[
            {"word": "강우량", "definition": "일정 기간 동안 일정한 장소에 내린 비의 양"},
            {"word": "주척", "definition": "조선 시대에 측우기 속 빗물의 깊이를 재던 표준 대나무 자"}
        ],
        visual_html="""<div class="p-3 bg-stone-50 rounded border border-stone-200">
          <h4 class="font-bold text-stone-900 mb-2">🌧️ 측우기 표준 규격과 측정 원리 분석</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-stone-200"><strong>측우기 본체:</strong> 원통형 청동 그릇 (지름 약 14cm, 높이 약 42cm)</div>
            <div class="p-1 bg-white rounded border border-stone-200"><strong>측정 도구:</strong> 주척 (눈금이 새겨진 표준 자로 물 깊이 측정)</div>
            <div class="p-1 bg-white rounded border border-stone-200"><strong>과거 vs 측우기:</strong> 땅 판 깊이(흙마다 다름) ➔ 전국 표준 그릇(정확)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-v33-c1", "text": "비가 땅속 몇 치 깊이까지 스며들었는지를 흙을 파서 쟀으나, 흙의 마른 정도에 따라 깊이가 달라 정확하지 못했습니다", "role": "과거 측정법의 한계", "para_idx": 0},
            {"cue_id": "g4-v33-c2", "text": "그릇의 지름(약 14cm)과 높이(약 42cm)를 전국적으로 통일하여", "role": "전국 표준화의 핵심", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "다중 자료 통합 도식",
            "source_a": "자료 ㉮: 흙 파던 방식의 문제점",
            "source_b": "자료 ㉯: 원통형 규격과 주척 측정법",
            "integrated_conclusion": "전국 표준 강우량 측정 체계로 농업과 치수 혁신 달성"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "다중 자료 정보 교차 통합",
                "stem": "자료 ㉮와 자료 ㉯를 바탕으로 '측우기가 발명되어 혁신적이었던 이유'로 가장 적절한 것은?",
                "target_para_idx": 2,
                "spotlight_quote": "두 자료를 종합해 보면, 측우기는 '부정확했던 과거 방식(자료 ㉮)'을 극복하고, '전국 표준 규격과 자(주척)를 도입(자료 ㉯)'하여",
                "options": [
                    {"label": "①", "text": "흙의 마른 정도에 좌우되던 한계를 벗어나 전국 표준 규격으로 비의 양을 정확히 측정했기 때문에", "is_correct": True, "formula": "정답", "explanation": "자료 ㉮의 문제점 극복과 자료 ㉯의 표준화 혁신을 종합한 올바른 결론입니다."},
                    {"label": "②", "text": "비가 올 때 하늘로 올라가 먹구름을 흩뜨리는 무기였기 때문에", "is_correct": False, "formula": "D5", "explanation": "측우기는 강우 측정기이지 날씨 조절 무기가 아닙니다."},
                    {"label": "③", "text": "전국의 모든 빗물을 다 모아서 마시는 물병이었기 때문에", "is_correct": False, "formula": "D3", "explanation": "빗물 측정용 작은 그릇입니다."},
                    {"label": "④", "text": "금과 다이아몬드로 만들어져 가장 비싼 보물이었기 때문에", "is_correct": False, "formula": "D1", "explanation": "구리로 만든 과학 기구입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 측정 도구 확인",
                "stem": "측우기 안에 고인 빗물의 깊이를 잴 때 사용한 표준 자의 이름은?",
                "target_para_idx": 1,
                "spotlight_quote": "원통형 구리 그릇에 빗물을 받아 '주척'이라는 자로 고인 물의 깊이를 푼(分) 단위까지 정밀하게 측정했습니다.",
                "options": [
                    {"label": "①", "text": "주척", "is_correct": True, "formula": "정답", "explanation": "자료 ㉯에 명시된 조선 시대 표준 자의 명칭입니다."},
                    {"label": "②", "text": "풍속계", "is_correct": False, "formula": "D4", "explanation": "바람 세기를 재는 현대 기구입니다."},
                    {"label": "③", "text": "온도계", "is_correct": False, "formula": "D2", "explanation": "온도 측정 도구입니다."},
                    {"label": "④", "text": "망원경", "is_correct": False, "formula": "D6", "explanation": "먼 곳을 보는 광학 기구입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 조선 시대에 전국적인 강우량을 측정해야 했던 가장 큰 목적은?",
                "options": [
                    {"label": "①", "text": "백성들의 농사를 돕고 홍수와 가뭄에 철저히 대비하기 위해", "is_correct": True},
                    {"label": "②", "text": "외국과 빗물 팔기 시합을 하기 위해", "is_correct": False},
                    {"label": "③", "text": "물놀이 축제를 매일 열기 위해", "is_correct": False},
                    {"label": "④", "text": "빗물로 궁궐 바닥을 청소하기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "전국 각 고을의 강우량을 동일한 기준으로 측정해 농사와 홍수 대비에 활용했습니다.", "is_correct": True},
                    {"label": "②", "text": "조선 세종 대에 발명된 '측우기'는 세계 최초의 표준 강우량 측정기입니다.", "is_correct": False},
                    {"label": "③", "text": "비가 땅속 몇 치 깊이까지 스며들었는지를", "is_correct": False},
                    {"label": "④", "text": "측우기는 원통형 구리 그릇에 빗물을 받아", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "측우기 과학성 다중 자료 요약문 쓰기",
            "guide": "자료 ㉮와 ㉯를 엮어 측우기의 우수성을 두 문장으로 요약해 보세요.",
            "template": "옛날에는 땅을 파서 비를 쟀으나 정확하지 않았습니다. 하지만 측우기는 [원통형 그릇]과 [주척]으로 비의 양을 전국에서 표준적으로 측정했습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "도서 자료와 웹 백과 자료의 차이점과 공통 정보를 표로 정리해요."},
            "step1_2_drill": {"task": "측우기의 구조(그릇, 주척)와 측정 목적 선으로 잇기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "측우기는 전국 각 고을에 동일한 규격으로 보급되어 측정되었습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 비의 양을 잰 조선의 지혜",
            "situation": "비 오는 날 창밖의 빗줄기를 바라볼 때",
            "parent_question": "옛날 세종대왕 때 비가 얼마나 왔는지 어떻게 알았을까?",
            "expected_answer": "세계 최초로 구리 그릇에 자를 넣어서 비의 깊이를 잰 '측우기'를 발명해서 알았대요!",
            "coaching_tip": "세종 시대의 과학적 발명이 세계사적으로 얼마나 앞섰는지 자부심을 심어 주세요."
        }
    ),

    # 12. W1
    build_expository_slot(
        grade_num=4,
        subskill_code="W1",
        subject="과학(땅의 변화 4-2)",
        unit="3. 지층과 화석",
        concept="‘지구’라는 넓은 주제를 ‘공룡과 산호 화석이 만들어지는 과정’으로 좁히기",
        text_structure="순서·과정·분류",
        structure_type_code="classification",
        passage_title="넓은 지구 이야기에서 화석의 신비로 주제 좁히기",
        paragraphs=[
            "'지구'라는 화제는 너무 넓고 방대하여 한 편의 설명글에 모든 내용을 담기 어렵습니다. 따라서 글을 계획할 때는 [상위 분야: 지구의 역사 ➔ 중위 대상: 암석 속 화석 ➔ 구체적 주제: 생물이 화석으로 변하는 과정과 옛 환경]처럼 깔때기 기법으로 주제를 좁혀야 합니다.",
            "예를 들어 4학년 독자들을 위해 주제를 좁힌다면, 공룡 뼈 화석과 바다 산호 화석을 구체적 제재로 정할 수 있습니다. 이를 통해 '생물의 유해가 어떻게 돌로 변하는지'와 '산호 화석이 발견된 산골짜기가 옛날에는 따뜻한 바다였음을 알아내는 원리'를 명확한 목표 제목으로 설정합니다.",
            "이처럼 주제를 명확하게 좁히면, 수집해야 할 자료의 범위가 뚜렷해지고 읽는 사람도 산만하지 않게 핵심 개념을 깊이 있게 이해할 수 있습니다."
        ],
        vocab_notes=[
            {"word": "깔때기 기법", "definition": "광범위한 화제를 점차 좁혀 구체적이고 명확한 주제로 압축하는 글쓰기 발상법"},
            {"word": "산호", "definition": "따뜻하고 얕은 바다에 살며 석회질 골격을 만드는 바다 동물"}
        ],
        visual_html="""<div class="p-3 bg-cyan-50 rounded border border-cyan-200">
          <h4 class="font-bold text-cyan-900 mb-2">🎯 3단계 주제 좁히기 깔때기 모델</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-cyan-200">1단계 (광범위): 지구와 지층</div>
            <div class="p-1 bg-white rounded border border-cyan-200">2단계 (중간): 지층 속에 묻힌 화석</div>
            <div class="p-1 bg-white rounded border border-cyan-200">3단계 (구체적 목표): 공룡 뼈와 산호 화석이 알려주는 과거 환경</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-w1-c1", "text": "깔때기 기법으로 주제를 좁혀야 합니다", "role": "주제 좁히기 핵심 기법", "para_idx": 0},
            {"cue_id": "g4-w1-c2", "text": "산호 화석이 발견된 산골짜기가 옛날에는 따뜻한 바다였음을 알아내는 원리", "role": "구체화된 목표 내용", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "주제 좁히기 깔때기",
            "broad": "지구의 변화",
            "intermediate": "화석",
            "focused_topic": "산호 화석으로 복원하는 고대 환경",
            "target_readers": "초등학교 4학년 학생들"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "작문 계획 전략 확인",
                "stem": "글을 쓸 때 '깔때기 기법'으로 주제를 좁혀야 하는 까닭은 무엇인가요?",
                "target_para_idx": 2,
                "spotlight_quote": "수집해야 할 자료의 범위가 뚜렷해지고 읽는 사람도 산만하지 않게 핵심 개념을 깊이 있게 이해할 수 있습니다.",
                "options": [
                    {"label": "①", "text": "자료 수집 범위가 명확해지고 독자가 핵심 개념을 깊이 이해할 수 있어서", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 주제 좁히기의 핵심 효과입니다."},
                    {"label": "②", "text": "글의 분량을 무조건 3줄 이내로 줄여 버리기 위해", "is_correct": False, "formula": "D3", "explanation": "분량을 극단적으로 줄이는 것이 목표가 아닙니다."},
                    {"label": "③", "text": "지구에 대한 책을 더 이상 읽지 않기 위해", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                    {"label": "④", "text": "글씨를 쓰지 않고 그림만 붙이기 위해", "is_correct": False, "formula": "D4", "explanation": "작문 계획과 무관합니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "제재 선정 타당성",
                "stem": "강원도 높은 산에서 '산호 화석'이 발견되었을 때 독자에게 설명할 수 있는 과학적 사실은?",
                "target_para_idx": 1,
                "spotlight_quote": "산호 화석이 발견된 산골짜기가 옛날에는 따뜻한 바다였음을 알아내는 원리",
                "options": [
                    {"label": "①", "text": "지금은 높은 산이지만 아주 먼 옛날에는 따뜻하고 얕은 바다였다.", "is_correct": True, "formula": "정답", "explanation": "산호의 생태 환경을 통해 과거 지형을 유추한 과학적 사실입니다."},
                    {"label": "②", "text": "옛날 산호들은 날개를 달고 높은 산으로 날아다녔다.", "is_correct": False, "formula": "D5", "explanation": "비과학적 허구입니다."},
                    {"label": "③", "text": "사람들이 어제 바다에서 산호를 주워 산에 묻어 두었다.", "is_correct": False, "formula": "D2", "explanation": "화석 생성 원리와 맞지 않습니다."},
                    {"label": "④", "text": "산호는 원래 눈 덮인 겨울 산에서만 자라는 풀이다.", "is_correct": False, "formula": "D6", "explanation": "산호는 바다 동물입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 넓은 화제를 좁힐 때 거치는 바람직한 3단계 순서는?",
                "options": [
                    {"label": "①", "text": "상위 광범위 분야 ➔ 중위 관심 대상 ➔ 구체적 설명 측면", "is_correct": True},
                    {"label": "②", "text": "퇴고 점검 ➔ 제목 짓기 ➔ 독자 조사", "is_correct": False},
                    {"label": "③", "text": "구체적 문장 쓰기 ➔ 넓은 주제 찾기 ➔ 인쇄하기", "is_correct": False},
                    {"label": "④", "text": "그림 그리기 ➔ 낱말 지우기 ➔ 제재 넓히기", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "[상위 분야: 지구의 역사 ➔ 중위 대상: 암석 속 화석 ➔ 구체적 주제: 생물이 화석으로 변하는 과정과 옛 환경]처럼", "is_correct": True},
                    {"label": "②", "text": "'지구'라는 화제는 너무 넓고 방대하여", "is_correct": False},
                    {"label": "③", "text": "공룡 뼈 화석과 바다 산호 화석을 구체적 제재로", "is_correct": False},
                    {"label": "④", "text": "이처럼 주제를 명확하게 좁히면,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "화제 좁히기 깔때기 연습장",
            "guide": "'동물'이라는 넓은 주제를 3단계로 좁혀 목표 제목을 정해 보세요.",
            "template": "1단계 (넓은 화제): 동물 ➔ 2단계 (중간 대상): 겨울잠 자는 동물 ➔ 3단계 (구체적 제목): [곰과 개구리의 겨울잠 비교]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글을 쓸 때는 '너무 넓은 주제'를 다루지 말고 깔때기처럼 좁혀요."},
            "step1_2_drill": {"task": "넓은 주제와 좁은 주제 카드 짝짓기 연습"},
            "step3_vaccine": {"ox_quiz": [{"statement": "주제를 좁히면 수집할 자료가 명확해집니다.", "answer": "O", "reason": "글쓰기 계획의 핵심 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 높은 산에서 나온 조개껍데기",
            "situation": "등산이나 다큐멘터리에서 태백산 조개 화석 이야기를 볼 때",
            "parent_question": "바다에 살던 조개나 산호 화석이 왜 높은 산꼭대기에서 발견될까?",
            "expected_answer": "먼 옛날에 그곳이 바다 밑바닥이었는데 땅이 솟아올라 높은 산이 되었기 때문이래요!",
            "coaching_tip": "화석을 통해 지구의 거대한 과거를 상상해 보도록 대화를 이끌어 주세요."
        }
    ),

    # 13. W2
    build_expository_slot(
        grade_num=4,
        subskill_code="W2",
        subject="사회(촌락과 도시 4-1)",
        unit="2. 도시의 문제와 해결",
        concept="도시의 쓰레기 발생량 변화와 해결 노력 설명 자료 수집·선별",
        text_structure="문제·해결",
        structure_type_code="problem_solution",
        passage_title="도시 쓰레기 문제 해결을 위한 믿을 만한 자료 모으기",
        paragraphs=[
            "도시로 많은 사람이 모여들면서 생활 쓰레기 배출량이 해마다 크게 늘어나 심각한 환경 문제가 되고 있습니다. 도시의 쓰레기 문제를 알리고 해결 방안을 제안하는 설명글을 쓰려면 공신력 있는 자료를 체계적으로 수집하고 선별해야 합니다.",
            "자료를 수집할 때는 통계청이나 환경부처럼 믿을 수 있는 공공기관의 최신 통계 수치를 수집해야 합니다. 또한 쓰레기 배출량의 연도별 변화 추이를 한눈에 보여주는 '막대그래프'나 '꺾은선그래프' 보조 시각자료를 함께 준비해야 주장에 설득력이 생깁니다.",
            "수집한 통계 자료는 출처와 연도를 명확히 기록하고, 복잡한 전문 용어를 자신의 쉬운 말로 요약 메모해야 합니다. 정확한 데이터와 시각자료가 뒷받침된 글은 읽는 사람에게 깊은 공감과 실천을 이끌어 냅니다."
        ],
        vocab_notes=[
            {"word": "공신력", "definition": "공공기관처럼 사회적으로 널리 인정받아 믿을 수 있는 능력이나 신뢰도"},
            {"word": "추이", "definition": "일이나 형세가 시간에 따라 변해 가는 모양이나 형편"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">📊 쓰레기 발생량 자료 수집 체크리스트</h4>
          <ul class="text-xs space-y-1 text-slate-700">
            <li>✔ <strong>출처 확인:</strong> 환경부·통계청 공식 보고서 (신뢰성 확보)</li>
            <li>✔ <strong>최신성 확인:</strong> 최근 3~5년 이내의 조사 데이터인가?</li>
            <li>✔ <strong>시각화 기획:</strong> 연도별 쓰레기 증가율 꺾은선그래프 첨부</li>
          </ul>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-w2-c1", "text": "통계청이나 환경부처럼 믿을 수 있는 공공기관의 최신 통계 수치를 수집해야 합니다", "role": "공신력 있는 출처 기준", "para_idx": 1},
            {"cue_id": "g4-w2-c2", "text": "수집한 통계 자료는 출처와 연도를 명확히 기록하고", "role": "출처 표기 원칙", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "자료 수집 포트폴리오",
            "topic": "도시 쓰레기 문제와 해결",
            "sources": [
                {"agency": "환경부", "data": "1인당 일일 쓰레기 배출량 추이", "visual": "꺾은선그래프"},
                {"agency": "시청 청소과", "data": "재활용 분리배출 성공 사례", "visual": "비교 사진"}
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "자료 출처 신뢰성 평가",
                "stem": "도시 쓰레기 문제 설명글을 쓸 때 수집할 자료로 가장 신뢰할 만한 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "통계청이나 환경부처럼 믿을 수 있는 공공기관의 최신 통계 수치를 수집해야 합니다.",
                "options": [
                    {"label": "①", "text": "환경부와 통계청이 발표한 최근 생활 쓰레기 통계 보고서", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 공신력 있는 공공기관의 최신 데이터입니다."},
                    {"label": "②", "text": "출처가 적혀 있지 않은 개인 블로그의 낙서", "is_correct": False, "formula": "D3", "explanation": "신뢰성이 떨어지는 개인 의견입니다."},
                    {"label": "③", "text": "100년 전 조선 시대 쓰레기 매립지 상상도", "is_correct": False, "formula": "D5", "explanation": "현대 도시 문제와 맞지 않는 옛날 자료입니다."},
                    {"label": "④", "text": "장난감 회사의 광고 전단지", "is_correct": False, "formula": "D1", "explanation": "주제와 무관한 상업 자료입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "시각 자료 기획 적절성",
                "stem": "'연도별 쓰레기 배출량의 변화 추이'를 보여주기에 가장 알맞은 시각 자료는?",
                "target_para_idx": 1,
                "spotlight_quote": "쓰레기 배출량의 연도별 변화 추이를 한눈에 보여주는 '막대그래프'나 '꺾은선그래프'",
                "options": [
                    {"label": "①", "text": "시간의 흐름에 따른 변화를 보여주는 꺾은선그래프", "is_correct": True, "formula": "정답", "explanation": "연도별 연속 변화 추이를 나타내는 최적의 시각자료입니다."},
                    {"label": "②", "text": "쓰레기통의 뚜껑 모양만 그린 동그라미 그림", "is_correct": False, "formula": "D2", "explanation": "수치 변화를 보여주지 못합니다."},
                    {"label": "③", "text": "꽃밭에 핀 장미꽃 사진", "is_correct": False, "formula": "D6", "explanation": "주제와 전혀 어긋납니다."},
                    {"label": "④", "text": "만화 영화 주인공 캐릭터 스티커", "is_correct": False, "formula": "D4", "explanation": "설명문 자료로 부적절합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 자료를 수집하고 메모할 때 반드시 기록해야 할 두 가지는?",
                "options": [
                    {"label": "①", "text": "자료의 출처와 발표 연도", "is_correct": True},
                    {"label": "②", "text": "기자의 키와 몸무게", "is_correct": False},
                    {"label": "③", "text": "종이의 두께와 냄새", "is_correct": False},
                    {"label": "④", "text": "글을 읽은 요일", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "수집한 통계 자료는 출처와 연도를 명확히 기록하고,", "is_correct": True},
                    {"label": "②", "text": "도시로 많은 사람이 모여들면서 생활 쓰레기 배출량이", "is_correct": False},
                    {"label": "③", "text": "자료를 수집할 때는 통계청이나 환경부처럼", "is_correct": False},
                    {"label": "④", "text": "정확한 데이터와 시각자료가 뒷받침된 글은", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "자료 수집 메모 카드 작성",
            "guide": "환경 문제 설명글을 쓰기 위해 수집한 통계 출처를 바르게 적어 보세요.",
            "template": "수집 기관: [환경부] / 조사 연도: [2024년] / 핵심 데이터: 1인당 하루 쓰레기 배출량 [ 1.1kg ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "자료 수집 시 '공신력 있는 기관'과 '발표 연도'를 반드시 확인해요."},
            "step1_2_drill": {"task": "믿을 수 있는 공식 자료와 믿기 힘든 헛소문 자료 변별하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "설명글에 통계 자료를 쓸 때는 출처를 밝혀야 합니다.", "answer": "O", "reason": "글의 신뢰성을 지키는 필수 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 신뢰할 수 있는 정보 찾기",
            "situation": "인터넷 뉴스를 보거나 숙제 조사를 할 때",
            "parent_question": "인터넷에 뜬 글 중 어떤 글을 믿어야 하고, 어떤 글을 조심해야 할까?",
            "expected_answer": "공공기관이나 공식 통계청처럼 출처와 조사 연도가 분명한 자료를 믿어야 해요!",
            "coaching_tip": "가짜 뉴스를 판별하고 신뢰성 있는 출처를 확인하는 디지털 리터러시를 길러 주세요."
        }
    ),

    # 14. W3
    build_expository_slot(
        grade_num=4,
        subskill_code="W3",
        subject="사회(지도 읽기 4-1)",
        unit="1. 지도로 보는 우리 고장",
        concept="지도의 ‘축척’과 ‘등고선’ 읽는 방법 3단 구성 개요 짜기",
        text_structure="정의·분석·비교",
        structure_type_code="analysis",
        passage_title="지도의 비밀 언어, 축척과 등고선 읽기 개요 짜기",
        paragraphs=[
            "지도는 지구 표면의 모습을 일정한 비율로 줄여 약속된 기호로 나타낸 그림입니다. 지도를 올바르게 읽는 방법을 설명하기 위해 '처음-가운데-끝'의 3단 구성 다층 개요를 설계합니다.",
            "[처음]에는 지도의 필요성과 흥미 유발 질문을 배치합니다. [가운데 1]에는 실제 거리를 줄인 비율인 '축척(줄인 자)'의 원리와 거리 계산법을 설명합니다. [가운데 2]에는 땅의 높낮이를 나타내는 '등고선'의 원리(선 사이가 좁으면 가파른 비탈, 넓으면 완만한 경사)를 비교 설명합니다. 마지막으로 [끝]에는 두 요소를 종합해 길을 찾는 지도의 가치로 마무리합니다.",
            "이렇게 소제목과 3단 구성을 갖춘 개요를 짜면, 자칫 딱딱하고 어려울 수 있는 지리 과학 개념을 독자가 단계별로 쉽게 이해할 수 있습니다."
        ],
        vocab_notes=[
            {"word": "축척", "definition": "지도에서 실제 거리를 일정한 비율로 줄인 정도"},
            {"word": "등고선", "definition": "지도에서 해수면을 기준으로 높이가 같은 지점을 연결한 선"}
        ],
        visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">🗺️ 지도 읽기 설명문 3단 다층 개요표</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-emerald-200"><strong>[처음]</strong> 지도의 정의: 위에서 내려다본 고장의 모습</div>
            <div class="p-1 bg-white rounded border border-emerald-200"><strong>[가운데 1]</strong> 축척: 실제 거리를 줄인 비율 (축척 막대자로 거리 재기)</div>
            <div class="p-1 bg-white rounded border border-emerald-200"><strong>[가운데 2]</strong> 등고선: 높이가 같은 곳을 이은 선 (가파름 vs 완만함)</div>
            <div class="p-1 bg-white rounded border border-emerald-200"><strong>[끝]</strong> 요약: 축척과 등고선으로 세상 넓게 바라보기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-w3-c1", "text": "실제 거리를 줄인 비율인 '축척(줄인 자)'의 원리와 거리 계산법을 설명합니다", "role": "가운데 1: 축척 설명 개요", "para_idx": 1},
            {"cue_id": "g4-w3-c2", "text": "선 사이가 좁으면 가파른 비탈, 넓으면 완만한 경사", "role": "가운데 2: 등고선 원리 개요", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "3단 구성 개요도",
            "outline": {
                "처음": "지도 소개 및 호기심 유발",
                "가운데1": "축척 (실제 거리 줄인 비율)",
                "가운데2": "등고선 (높낮이 선 간격 분석)",
                "끝": "지도 읽기의 의의 및 요약"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "개요 조직 세부 확인",
                "stem": "글의 개요에서 [가운데 2]에 들어갈 '등고선'의 핵심 원리로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "[가운데 2]에는 땅의 높낮이를 나타내는 '등고선'의 원리(선 사이가 좁으면 가파른 비탈, 넓으면 완만한 경사)를 비교 설명합니다.",
                "options": [
                    {"label": "①", "text": "선 사이의 간격이 좁을수록 가파르고, 넓을수록 완만하다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 등고선의 올바른 판독 원리입니다."},
                    {"label": "②", "text": "선이 많을수록 바다의 물고기가 많다.", "is_correct": False, "formula": "D3", "explanation": "등고선과 무관한 오답입니다."},
                    {"label": "③", "text": "등고선은 언제나 직선으로만 그린다.", "is_correct": False, "formula": "D1", "explanation": "지형에 따라 구불구불한 곡선입니다."},
                    {"label": "④", "text": "선이 하나도 없는 곳이 가장 높은 에베레스트산이다.", "is_correct": False, "formula": "D4", "explanation": "정반대 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "개요 다층 구조 파악",
                "stem": "글쓴이가 [가운데] 부분을 2개의 하위 문단으로 나눈 까닭은?",
                "target_para_idx": 1,
                "spotlight_quote": "[가운데 1]에는 실제 거리를 줄인 비율인 '축척(줄인 자)'의 원리와 거리 계산법을 설명합니다. [가운데 2]에는 땅의 높낮이를 나타내는 '등고선'의 원리",
                "options": [
                    {"label": "①", "text": "'거리(축척)'와 '높낮이(등고선)'라는 두 핵심 요소를 각각 체계적으로 설명하기 위해", "is_correct": True, "formula": "정답", "explanation": "설명 대상의 속성에 맞춘 체계적 문단 구분입니다."},
                    {"label": "②", "text": "종이가 너무 많이 남아서 아무 말이나 채우기 위해", "is_correct": False, "formula": "D2", "explanation": "엉뚱한 오답입니다."},
                    {"label": "③", "text": "독자를 헷갈리게 만들기 위해", "is_correct": False, "formula": "D5", "explanation": "글쓰기 목적과 반대됩니다."},
                    {"label": "④", "text": "선생님께 혼나지 않으려고 억지로 늘렸다.", "is_correct": False, "formula": "D6", "explanation": "사적 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 지도에서 실제 거리를 줄인 비율을 가리키는 용어는?",
                "options": [
                    {"label": "①", "text": "축척", "is_correct": True},
                    {"label": "②", "text": "방위표", "is_correct": False},
                    {"label": "③", "text": "범례", "is_correct": False},
                    {"label": "④", "text": "등고선", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "실제 거리를 줄인 비율인 '축척(줄인 자)'의 원리와 거리 계산법을 설명합니다.", "is_correct": True},
                    {"label": "②", "text": "지도는 지구 표면의 모습을 일정한 비율로 줄여", "is_correct": False},
                    {"label": "③", "text": "[처음]에는 지도의 필요성과 흥미 유발 질문을", "is_correct": False},
                    {"label": "④", "text": "마지막으로 [끝]에는 두 요소를 종합해", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "지도 읽기 3단 개요표 작성",
            "guide": "지도 설명글의 개요를 완성해 보세요.",
            "template": "[처음]: 지도 소개 ➔ [가운데 1]: 실제 거리를 줄인 [축척] ➔ [가운데 2]: 땅의 높낮이 [등고선] ➔ [끝]: 지도 읽기의 가치"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "개요를 짤 때는 주제를 2개 이상의 세부 속성으로 나누어 가운데에 배치해요."},
            "step1_2_drill": {"task": "축척(거리)과 등고선(높낮이) 개념 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "등고선 간격이 좁을수록 경사가 가파릅니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 등산 지도 읽기",
            "situation": "등산로 지도나 관광 안내도를 함께 펼쳐 볼 때",
            "parent_question": "지도에 갈색 구불구불한 선이 빽빽하게 모여 있는 곳은 어떤 길일까?",
            "expected_answer": "등고선 간격이 좁으니까 가파른 오르막길이나 비탈길이에요!",
            "coaching_tip": "실제 지도의 등고선과 축척을 손으로 짚어가며 공간 감각을 키워 주세요."
        }
    ),

    # 15. W4
    build_expository_slot(
        grade_num=4,
        subskill_code="W4",
        subject="체육·보건(우리 몸 4-1)",
        unit="2. 건강한 몸 만들기",
        concept="우리 몸을 움직이는 ‘뼈’와 ‘근육’의 역할과 운동 시간 그래프",
        text_structure="비교·인과",
        structure_type_code="causal",
        passage_title="몸을 지탱하는 뼈와 당겨주는 근육의 협동",
        paragraphs=[
            "우리가 달리고 공을 던질 수 있는 것은 몸속 200여 개의 뼈와 600여 개의 근육이 완벽한 조화를 이루며 협동하기 때문입니다. 뼈와 근육의 역할을 설명하는 보고서를 쓸 때는 중심 문장과 도표 지시문을 유기적으로 연결해 집필해야 합니다.",
            "뼈는 단단한 칼슘으로 이루어져 몸의 기둥 역할을 하며 뇌나 심장 같은 소중한 내장 기관을 안전하게 보호합니다. 하지만 뼈 스스로는 움직일 수 없습니다. 뼈에 붙어 있는 근육이 고무줄처럼 수축하고 이완하면서 뼈를 잡아당겨야 비로소 관절이 굽혀지고 몸이 움직입니다.",
            "<그림 1>의 '운동 시간에 따른 근육량 증가 그래프'에서 보듯이, 규칙적인 신체 운동을 꾸준히 지속할 때 뼈의 밀도가 높아지고 근육이 튼튼해집니다. 이처럼 뼈와 근육은 하나라도 없어서는 안 될 소중한 짝꿍입니다."
        ],
        vocab_notes=[
            {"word": "수축과 이완", "definition": "근육이 오그라들어 짧아지는 것(수축)과 늘어나 느슨해지는 것(이완)"},
            {"word": "관절", "definition": "뼈와 뼈가 서로 맞닿아 부드럽게 움직일 수 있도록 연결된 부위"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">🦴 뼈와 근육의 상호작용 및 운동 효과</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-white rounded border border-red-200 text-center"><strong>🦴 뼈의 역할</strong><br>몸 지탱, 내장 보호, 칼슘 저장</div>
            <div class="p-2 bg-white rounded border border-red-200 text-center"><strong>💪 근육의 역할</strong><br>수축·이완으로 뼈를 당김, 운동</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-w4-c1", "text": "뼈에 붙어 있는 근육이 고무줄처럼 수축하고 이완하면서 뼈를 잡아당겨야", "role": "근육 운동 메커니즘", "para_idx": 1},
            {"cue_id": "g4-w4-c2", "text": "<그림 1>의 '운동 시간에 따른 근육량 증가 그래프'에서 보듯이", "role": "도표 지시문 활용", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "협동 작용 도식",
            "components": {
                "뼈": "몸의 골격 지탱 및 내부 장기 보호",
                "근육": "수축/이완 운동으로 뼈 견인",
                "관절": "회전 및 굽힘 지점"
            },
            "synergy": "뼈와 근육의 협동을 통한 신체 운동 완성"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "인과 및 협동 메커니즘 확인",
                "stem": "우리 몸이 팔이나 다리를 구부려 움직일 수 있는 직접적인 원리는?",
                "target_para_idx": 1,
                "spotlight_quote": "뼈에 붙어 있는 근육이 고무줄처럼 수축하고 이완하면서 뼈를 잡아당겨야 비로소 관절이 굽혀지고 몸이 움직입니다.",
                "options": [
                    {"label": "①", "text": "근육이 수축하고 이완하면서 뼈를 잡아당기기 때문에", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 신체 운동의 직접적 메커니즘입니다."},
                    {"label": "②", "text": "단단한 뼈가 스스로 구부러지며 춤을 추기 때문에", "is_correct": False, "formula": "D3", "explanation": "뼈는 스스로 움직이지 못합니다."},
                    {"label": "③", "text": "피부가 바람을 불어넣어 풍선처럼 부풀기 때문에", "is_correct": False, "formula": "D1", "explanation": "비과학적 허구입니다."},
                    {"label": "④", "text": "심장이 밖으로 튀어나와 다리를 밀기 때문에", "is_correct": False, "formula": "D5", "explanation": "엉뚱한 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "도표 연계 서술 평가",
                "stem": "글쓴이가 3문단에서 '<그림 1>의 그래프에서 보듯이'라는 도표 지시문을 넣은 까닭은?",
                "target_para_idx": 2,
                "spotlight_quote": "<그림 1>의 '운동 시간에 따른 근육량 증가 그래프'에서 보듯이, 규칙적인 신체 운동을 꾸준히 지속할 때",
                "options": [
                    {"label": "①", "text": "본문의 설명 내용과 첨부된 시각 도표를 긴밀하게 연결해 신뢰성을 높이기 위해", "is_correct": True, "formula": "정답", "explanation": "도표 지시문을 활용한 학술적 작문 전략입니다."},
                    {"label": "②", "text": "글을 읽지 말고 그림만 보고 넘어가라고 알리기 위해", "is_correct": False, "formula": "D4", "explanation": "잘못된 해석입니다."},
                    {"label": "③", "text": "그림의 화가 이름을 비밀로 유지하기 위해", "is_correct": False, "formula": "D2", "explanation": "무관한 오답입니다."},
                    {"label": "④", "text": "글자 수를 억지로 채우기 위해", "is_correct": False, "formula": "D6", "explanation": "단순 분량 채우기가 아닙니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 뼈가 우리 몸에서 담당하는 핵심 역할 중 하나는?",
                "options": [
                    {"label": "①", "text": "뇌나 심장 같은 소중한 내장 기관을 안전하게 보호한다.", "is_correct": True},
                    {"label": "②", "text": "음식물을 씹어 영양분을 직접 흡수한다.", "is_correct": False},
                    {"label": "③", "text": "눈물을 흘려 눈을 적신다.", "is_correct": False},
                    {"label": "④", "text": "말을 할 때 소리를 크게 키운다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "뼈는 단단한 칼슘으로 이루어져 몸의 기둥 역할을 하며 뇌나 심장 같은 소중한 내장 기관을 안전하게 보호합니다.", "is_correct": True},
                    {"label": "②", "text": "우리가 달리고 공을 던질 수 있는 것은", "is_correct": False},
                    {"label": "③", "text": "하지만 뼈 스스로는 움직일 수 없습니다.", "is_correct": False},
                    {"label": "④", "text": "규칙적인 신체 운동을 꾸준히 지속할 때", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "도표 지시문 결합 보고서 쓰기",
            "guide": "'<그림 1>에서 보듯이' 표현을 살려 뼈와 근육의 운동 효과를 써 보세요.",
            "template": "<그림 1>에서 보듯이, 규칙적으로 운동하면 [근육]이 튼튼해지고 [뼈]의 밀도가 높아집니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "보고서 집필 시 도표를 인용할 때는 '<그림 1>에서 보듯이'처럼 지시문을 명시해요."},
            "step1_2_drill": {"task": "뼈(보호)와 근육(수축·당김)의 역할 카드 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "근육이 수축하며 뼈를 잡아당겨 몸이 움직입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 팔을 굽힐 때 불룩 솟는 알통",
            "situation": "아이가 팔을 구부려 알통을 자랑할 때",
            "parent_question": "팔을 안쪽으로 굽힐 때 왜 안쪽 알통(이두근)이 불룩 솟아오를까?",
            "expected_answer": "근육이 고무줄처럼 수축하며 짧고 굵어지면서 아래쪽 뼈를 잡아당기기 때문이래요!",
            "coaching_tip": "자신의 몸을 직접 만져보며 뼈와 근육의 수축 운동을 과학적으로 이해하게 해 주세요."
        }
    ),

    # 16. W5
    build_expository_slot(
        grade_num=4,
        subskill_code="W5",
        subject="과학(혼합물 기초 4-2)",
        unit="4. 혼합물의 분리",
        concept="염전에서 바닷물로 소금을 얻는 과정 설명문 초안 고쳐쓰기",
        text_structure="순서·과정·인과",
        structure_type_code="sequence",
        passage_title="바닷물이 하얀 소금이 되기까지 초고 퇴고하기",
        paragraphs=[
            "염전은 바닷물에 녹아 있는 소금을 햇빛과 바람으로 수분을 증발시켜 얻어내는 전통 생산 시설입니다. 염전에서 소금을 얻는 과정을 설명한 학생의 초고를 바르게 퇴고하려면 3단계 퇴고 점검 기준을 적용해야 합니다.",
            "첫째, 내용 면에서 바닷물이 증발하여 소금 결정이 석출되는 과학적 원리가 빠지지 않았는지 확인합니다. 둘째, 조직 면에서 '바닷물 유입 ➔ 저수지 보관 ➔ 증발지 증발 ➔ 결정지 소금 모으기'라는 단계적 순서가 뒤바뀌지 않았는지, '먼저-그다음에-마침내' 담화표지가 바르게 쓰였는지 살핍니다. 셋째, 표현 면에서 겹문장의 주어-서술어 호응과 맞춤법 오류를 표준 교정부호로 바로잡습니다.",
            "예를 들어 초고의 '소금이 햇빛을 말려서 바닷물이 되었다'는 인과가 뒤바뀐 비문이므로, '햇빛과 바람이 바닷물의 수분을 증발시켜 하얀 소금 결정이 남았다'로 고쳐 쓰는 것이 완벽한 퇴고입니다."
        ],
        vocab_notes=[
            {"word": "결정지", "definition": "염전에서 수분이 거의 증발하여 소금 결정이 생겨나는 마지막 판"},
            {"word": "석출", "definition": "용액 속에 녹아 있던 물질이 고체 알갱이로 분리되어 겉으로 나오는 현상"}
        ],
        visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
          <h4 class="font-bold text-blue-900 mb-2">🧂 염전 소금 생산 3단계 퇴고 점검표</h4>
          <ul class="text-xs space-y-1 text-slate-700">
            <li>✔ <strong>내용 점검:</strong> 물의 증발과 소금 결정 석출 원리가 바른가?</li>
            <li>✔ <strong>조직 점검:</strong> 저수지 ➔ 증발지 ➔ 결정지 순서가 정확한가?</li>
            <li>✔ <strong>표현 점검:</strong> 인과 전도 오류(“소금이 물을 말림” ➔ “물이 증발”) 교정</li>
          </ul>
        </div>""",
        hottext_cues=[
            {"cue_id": "g4-w5-c1", "text": "바닷물 유입 ➔ 저수지 보관 ➔ 증발지 증발 ➔ 결정지 소금 모으기", "role": "염전 4단계 공정 순서", "para_idx": 1},
            {"cue_id": "g4-w5-c2", "text": "햇빛과 바람이 바닷물의 수분을 증발시켜 하얀 소금 결정이 남았다", "role": "바른 인과 퇴고 문장", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "퇴고 체크리스트",
            "content": "물의 증발을 통한 혼합물 분리 원리 정확성",
            "organization": "저수지-증발지-결정지 공정 순서 준수",
            "expression": "주어-서술어 및 인과 관계 호응 교정"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "인과 오류 퇴고",
                "stem": "초고 문장 '소금이 햇빛을 말려서 바닷물이 되었다'가 심각한 오류인 까닭은?",
                "target_para_idx": 2,
                "spotlight_quote": "초고의 '소금이 햇빛을 말려서 바닷물이 되었다'는 인과가 뒤바뀐 비문이므로,",
                "options": [
                    {"label": "①", "text": "원인과 결과가 뒤바뀌어 소금이 햇빛을 말린다는 비과학적 문장이 되었기 때문에", "is_correct": True, "formula": "정답", "explanation": "햇빛이 바닷물의 수분을 증발시키는 것이므로 주어-목적어-인과가 완전히 전도되었습니다."},
                    {"label": "②", "text": "소금의 색깔이 검은색이라고 쓰지 않아서", "is_correct": False, "formula": "D3", "explanation": "소금은 흰색입니다."},
                    {"label": "③", "text": "염전에 비행기가 착륙하지 못해서", "is_correct": False, "formula": "D1", "explanation": "엉뚱한 오답입니다."},
                    {"label": "④", "text": "문장에 한자어가 너무 많이 들어가서", "is_correct": False, "formula": "D4", "explanation": "한자어 문제가 아닌 인과 왜곡 문제입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "과정 순서 퇴고",
                "stem": "염전에서 소금을 얻는 올바른 공간 이동 순서는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "'바닷물 유입 ➔ 저수지 보관 ➔ 증발지 증발 ➔ 결정지 소금 모으기'라는 단계적 순서",
                "options": [
                    {"label": "①", "text": "바닷물 유입 ➔ 저수지 ➔ 증발지 ➔ 결정지", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 염전의 과학적 공정 순서입니다."},
                    {"label": "②", "text": "결정지 ➔ 바다 ➔ 저수지 ➔ 증발지", "is_correct": False, "formula": "D2", "explanation": "순서가 뒤죽박죽인 오답입니다."},
                    {"label": "③", "text": "소금 모으기 ➔ 바닷물 붓기 ➔ 땅 파기", "is_correct": False, "formula": "D5", "explanation": "공정이 거꾸로 된 오답입니다."},
                    {"label": "④", "text": "증발지 ➔ 결정지 ➔ 저수지 ➔ 바다", "is_correct": False, "formula": "D6", "explanation": "순서 오류입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 염전에서 바닷물 속 소금을 분리해 내는 과학적 핵심 원리는?",
                "options": [
                    {"label": "①", "text": "햇빛과 바람을 이용한 물의 증발", "is_correct": True},
                    {"label": "②", "text": "거름종이로 바닷물을 걸러내기", "is_correct": False},
                    {"label": "③", "text": "자석으로 쇠붙이를 끌어당기기", "is_correct": False},
                    {"label": "④", "text": "냉장고에 넣어 꽁꽁 얼리기", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "염전은 바닷물에 녹아 있는 소금을 햇빛과 바람으로 수분을 증발시켜 얻어내는 전통 생산 시설입니다.", "is_correct": True},
                    {"label": "②", "text": "염전에서 소금을 얻는 과정을 설명한 학생의 초고를", "is_correct": False},
                    {"label": "③", "text": "첫째, 내용 면에서 바닷물이 증발하여", "is_correct": False},
                    {"label": "④", "text": "예를 들어 초고의 '소금이 햇빛을 말려서", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "염전 소금 설명문 퇴고 실습",
            "guide": "인과 관계가 어색한 초고를 바르게 고쳐 써 보세요.",
            "template": "초고: 소금이 햇빛을 말려서 바닷물이 되었다. ➔ 퇴고: [햇빛과 바람이 바닷물을 증발시켜 하얀 소금 결정이 남았습니다.]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "과정 설명문 퇴고는 '시간 순서(저수지-증발지-결정지)'와 '인과 호응'을 점검해요."},
            "step1_2_drill": {"task": "잘못된 인과 문장 찾아서 바른 문장으로 고쳐 쓰기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "염전은 햇빛과 바람으로 물을 증발시켜 소금을 얻는 곳입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 소금은 어디서 올까?",
            "situation": "식탁 위 소금통이나 굵은 천일염을 볼 때",
            "parent_question": "바닷물은 짠 물인데 어떻게 하얗고 네모난 소금 알갱이가 될 수 있을까?",
            "expected_answer": "염전에서 햇빛과 바람이 물만 쏙 날려 보내(증발)서 소금 알갱이만 남는 거래요!",
            "coaching_tip": "혼합물의 분리라는 과학 원리가 매일 먹는 식탁 위에 있음을 흥미롭게 알려 주세요."
        }
    )
]

# Assemble all 16 slots for Grade 4
# slots 1~3: g4_expository_slots
# slot 4: g4_remaining_slots[0]
# slots 5~6: g4_remaining_slots_part2
# slot 7: g4_flagship_v23
# slots 8~16: g4_remaining_slots_part3 (9 slots: V2-4 ~ W5)

g4_all_expository = (
    g4_expository_slots +              # V1-1, V1-2, V1-3
    g4_remaining_slots +               # V1-4
    g4_remaining_slots_part2 +         # V2-1, V2-2
    [g4_flagship_v23] +                # V2-3
    g4_remaining_slots_part3           # V2-4, V3-1, V3-2, V3-3, W1, W2, W3, W4, W5
)

print(f"Total Grade 4 Expository Slots: {len(g4_all_expository)} (expected 16)")
print(f"Total Grade 4 Common Slots: {len(g4_common_slots)} (expected 6)")

out_path = os.path.join(ITEM_BANK_DIR, "g4_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 4,
        "expository_slots": g4_all_expository,
        "common_slots": g4_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g4_all_expository)} Expository + {len(g4_common_slots)} Common)")
