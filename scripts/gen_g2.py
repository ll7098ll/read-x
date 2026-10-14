# -*- coding: utf-8 -*-
"""
Generator for Grade 2 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
Output: courseware/data/item_bank/g2_item_bank.json
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

# 1. Common Foundation Slots for Grade 2 (6 slots: G2-COM-A1 ~ G2-COM-A6)
g2_common_slots = [
    build_common_slot(
        grade_num=2,
        com_code_suffix="A1",
        title="소리 나는 대로 쓰지 않고 본모양 밝혀 적기 (연음과 된소리)",
        rule_box="[맞춤법 원칙] '꽃을[꼬츨]', '국물[궁물]'처럼 말할 때 소리가 바뀌어도 글씨는 원래 낱말의 모양을 밝혀 적어야 뜻을 분명히 알 수 있습니다.",
        passage_snippet="봄이 오면 산과 들에 예쁜 꽃이 피어납니다. 우리는 맑은 물을 마시고 산길을 걸으며 자연을 관찰합니다.",
        mini_question="'꽃이[꼬치]'처럼 소리는 나지만 글자를 바르게 적은 것은 어느 것일까요?",
        choices=["① 꼬치", "② 꽃이", "③ 꼬치이"],
        correct="②",
        feedback="소리는 [꼬치]로 나더라도, 원래 '꽃'이라는 낱말 모양을 살려 '꽃이'로 적어야 맞습니다.",
        ox_items=[
            {"statement": "낱말은 항상 들리는 소리 그대로만 적어야 뜻이 통한다.", "answer": "X", "reason": "원래 낱말의 모양을 밝혀 적어야 뜻을 쉽게 구별할 수 있습니다."},
            {"statement": "'물에[무레]'는 원래 모양 '물'을 살려 적은 바른 글자이다.", "answer": "O", "reason": "받침이 뒤로 이어져 소리 나도 '물' 모양을 밝혀 적습니다."}
        ]
    ),
    build_common_slot(
        grade_num=2,
        com_code_suffix="A2",
        title="앞뒤 문장 속 낱말의 문맥 의미 짐작하기",
        rule_box="[문맥 추론 단서] 글을 읽다가 낯선 낱말이 나오면, 그 낱말의 앞뒤 문장에 나오는 쉬운 낱말과 상황을 연결해 뜻을 짐작합니다.",
        passage_snippet="겨울이 되면 다람쥐는 굴속에 '비축'해 둔 도토리를 꺼내 먹습니다. 가을 동안 겨우내 먹을 음식을 미리 모아 두었기 때문입니다.",
        mini_question="위 글에서 '비축하다'의 뜻으로 가장 알맞은 것은 무엇인가요?",
        choices=["① 음식을 땅에 버리다", "② 앞으로 쓸 것에 대비해 미리 모아 두다", "③ 도토리를 발로 밟아 부수다"],
        correct="②",
        feedback="뒤 문장의 '겨우내 먹을 음식을 미리 모아 두었기 때문'이라는 단서에서 뜻을 알 수 있습니다.",
        ox_items=[
            {"statement": "낯선 낱말의 뜻은 앞뒤 문장의 설명 말을 통해 짐작할 수 있다.", "answer": "O", "reason": "문맥 단서를 이용한 효과적인 독해 방법입니다."},
            {"statement": "모르는 낱말이 나오면 글 전체를 읽지 않고 덮어야 한다.", "answer": "X", "reason": "앞뒤 문장을 자세히 읽으면 뜻을 유추할 수 있습니다."}
        ]
    ),
    build_common_slot(
        grade_num=2,
        com_code_suffix="A3",
        title="누가 무엇을 했는지 주어와 서술어 짝 맞추기",
        rule_box="[문장 성분 규칙] 문장은 '무엇이(누가)'에 해당하는 주어와 '어떠하다(어찌하다)'에 해당하는 서술어가 바르게 짝을 이루어야 뜻이 통합니다.",
        passage_snippet="파란 하늘에 하얀 구름이 둥실둥실 떠갑니다. 참새는 나뭇가지에 앉아 맑은 목소리로 노래합니다.",
        mini_question="'하얀 구름이'와 바르게 짝을 이루는 서술어는 무엇인가요?",
        choices=["① 둥실둥실 떠갑니다.", "② 흙탕물을 튀깁니다.", "③ 책을 조용히 읽습니다."],
        correct="①",
        feedback="하늘에 있는 구름의 행동으로는 '떠갑니다'가 자연스럽게 호응합니다.",
        ox_items=[
            {"statement": "'새가 힘차게 헤엄친다'는 주어와 서술어가 자연스럽게 어울린다.", "answer": "X", "reason": "새는 날거나 노래하는 것이 자연스럽고, 헤엄은 물고기가 칩니다."},
            {"statement": "문장을 쓸 때는 주어와 서술어의 관계를 꼭 확인해야 한다.", "answer": "O", "reason": "문장의 의미를 바르게 전달하는 기본 규칙입니다."}
        ]
    ),
    build_common_slot(
        grade_num=2,
        com_code_suffix="A4",
        title="글 속의 지시어('이것, 그곳')가 가리키는 대상 찾기",
        rule_box="[지시 대용 규칙] '이것', '그곳', '그 사람' 같은 말은 앞 문장에 이미 나온 사물이나 장소를 대신 가리키는 말입니다.",
        passage_snippet="우리 학교 운동장 옆에는 커다란 느티나무가 서 있습니다. 아이들은 더운 날씨가 되면 그곳에 모여 시원한 그늘 밑에서 쉽니다.",
        mini_question="위 글에서 밑줄 친 '그곳'이 가리키는 장소는 어디인가요?",
        choices=["① 교실 안", "② 커다란 느티나무 그늘 밑", "③ 교장선생님 방"],
        correct="②",
        feedback="앞 문장에 나온 '커다란 느티나무'를 가리킵니다.",
        ox_items=[
            {"statement": "'그것', '그곳' 같은 말은 앞 문장의 내용을 대신 가리킨다.", "answer": "O", "reason": "문장을 매끄럽게 잇는 지시어의 역할입니다."},
            {"statement": "지시어가 가리키는 대상을 몰라도 글을 정확히 이해할 수 있다.", "answer": "X", "reason": "가리키는 대상을 알아야 글의 내용이 연결됩니다."}
        ]
    ),
    build_common_slot(
        grade_num=2,
        com_code_suffix="A5",
        title="원인과 결과를 나타내는 접속어('왜냐하면, 그래서')",
        rule_box="[인과 관계 표지] 일어난 일의 까닭을 말할 때는 '왜냐하면 ~ 때문이다'를 쓰고, 까닭에 따른 결과를 말할 때는 '그래서', '따라서'를 씁니다.",
        passage_snippet="오늘 아침부터 많은 비가 내렸습니다. 그래서 놀이터에 고인 웅덩이 때문에 축구를 하지 못했습니다.",
        mini_question="축구를 하지 못한 '원인(까닭)'은 무엇인가요?",
        choices=["① 아침부터 많은 비가 내렸기 때문에", "② 축구공을 잃어버려서", "③ 친구가 집에 가 버려서"],
        correct="①",
        feedback="'그래서' 앞에 나온 '많은 비가 내렸습니다'가 원인입니다.",
        ox_items=[
            {"statement": "'그래서' 뒤에는 주로 원인이 오고 앞에는 결과가 온다.", "answer": "X", "reason": "'그래서' 앞이 원인이고 뒤가 결과입니다."},
            {"statement": "'왜냐하면' 뒤에는 일어난 일의 이유나 까닭을 쓴다.", "answer": "O", "reason": "이유를 설명할 때 쓰는 올바른 접속 표현입니다."}
        ]
    ),
    build_common_slot(
        grade_num=2,
        com_code_suffix="A6",
        title="중심 낱말을 찾아 글의 중심 생각 요약하기",
        rule_box="[요약 기초] 글에서 가장 자주 나오거나 중요한 핵심 낱말을 찾고, 그 낱말에 대해 글쓴이가 설명하려는 중심 문장을 골라 요약합니다.",
        passage_snippet="꿀벌은 꽃에서 달콤한 꿀을 모읍니다. 또 꽃가루를 몸에 묻혀 다른 꽃으로 옮겨 열매를 맺게 돕습니다. 꿀벌은 자연과 사람 모두에게 참 이로운 곤충입니다.",
        mini_question="위 글 전체의 중심 생각으로 가장 알맞은 것은 무엇인가요?",
        choices=["① 꿀벌은 쏘이면 아픈 무서운 벌레이다.", "② 꿀벌은 자연과 사람에게 참 이로운 곤충이다.", "③ 꽃가루는 바람이 불면 날아간다."],
        correct="②",
        feedback="글의 마지막 문장에 제시된 글 전체의 중심 생각입니다.",
        ox_items=[
            {"statement": "글에서 가장 중요한 핵심 내용을 한 문장으로 간추린 것을 중심 생각이라 한다.", "answer": "O", "reason": "요약의 핵심 정의입니다."},
            {"statement": "중심 생각은 글에 한 번도 안 나온 엉뚱한 상상을 적는 것이다.", "answer": "X", "reason": "글에 담긴 사실과 주장을 바탕으로 요약해야 합니다."}
        ]
    )
]

print(f"Built G2 Common Slots: {len(g2_common_slots)}")

# 2. Expository Slots for Grade 2 (16 slots: V1-1 ~ W5)
# Note: CSAT questions have 3 options (G1~2 초저 standard)
g2_expository_slots = [
    # 1. V1-1
    build_expository_slot(
        grade_num=2,
        subskill_code="V1-1",
        subject="통합(마을 2-1)",
        unit="1. 우리 마을의 여러 곳",
        concept="우리 마을을 돕는 공공장소 (우체국과 보건소)",
        text_structure="열거·분류 기초",
        structure_type_code="classification",
        passage_title="우리 마을을 돕는 고마운 공공장소",
        paragraphs=[
            "우리 마을에는 주민들의 편리한 생활을 돕는 여러 공공장소가 있습니다. 공공장소는 마을 사람들이 다 함께 이용하는 소중한 곳입니다.",
            "먼저 우체국은 편지와 소포를 안전하게 배달해 주고 저금도 할 수 있는 곳입니다. 그리고 보건소는 몸이 아픈 주민들을 치료해 주고 건강을 지키도록 예방주사를 놓아 주는 곳입니다. 이 두 곳은 마을 사람들의 안전과 생활을 지켜 주는 고마운 곳입니다."
        ],
        vocab_notes=[
            {"word": "공공장소", "definition": "마을 사람들이 다 함께 이용하는 편리한 시설"},
            {"word": "소포", "definition": "우체국을 통해 부치는 포장된 물건"}
        ],
        visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
          <h4 class="font-bold text-blue-900 mb-2">📮 우리 마을 공공장소와 하는 일</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-white rounded border border-blue-100 text-center"><strong>📬 우체국</strong><br>편지·소포 배달, 저금</div>
            <div class="p-2 bg-white rounded border border-blue-100 text-center"><strong>🏥 보건소</strong><br>주민 치료, 예방주사</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v11-c1", "text": "우체국은 편지와 소포를 안전하게 배달해 주고", "role": "우체국 역할", "para_idx": 1},
            {"cue_id": "g2-v11-c2", "text": "보건소는 몸이 아픈 주민들을 치료해 주고", "role": "보건소 역할", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "분류 카드",
            "category": "우리 마을의 공공장소",
            "items": ["우체국 (소포 배달)", "보건소 (치료·예방주사)"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "세부 내용 확인",
                "stem": "마을의 '보건소'에서 하는 일로 알맞은 것은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "보건소는 몸이 아픈 주민들을 치료해 주고 건강을 지키도록 예방주사를 놓아 주는 곳입니다.",
                "options": [
                    {"label": "①", "text": "편지와 무거운 소포를 멀리 배달한다.", "is_correct": False, "formula": "D3", "explanation": "소포 배달은 우체국의 일입니다."},
                    {"label": "②", "text": "아픈 주민을 치료하고 예방주사를 놓아 준다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 보건소의 역할입니다."},
                    {"label": "③", "text": "맛있는 빵과 음료수를 만들어 판다.", "is_correct": False, "formula": "D1", "explanation": "빵집에서 하는 일입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "중심 내용 파악",
                "stem": "글을 통해 알 수 있는 '공공장소'의 뜻으로 가장 알맞은 것은?",
                "target_para_idx": 0,
                "spotlight_quote": "공공장소는 마을 사람들이 다 함께 이용하는 소중한 곳입니다.",
                "options": [
                    {"label": "①", "text": "마을 사람들이 다 함께 이용하는 편리한 곳", "is_correct": True, "formula": "정답", "explanation": "1문단에서 공공장소의 정의로 바르게 설명했습니다."},
                    {"label": "②", "text": "한 사람만 혼자 들어가서 문을 잠그는 비밀 방", "is_correct": False, "formula": "D4", "explanation": "공공의 뜻과 반대되는 설명입니다."},
                    {"label": "③", "text": "밤에만 문을 열고 낮에는 들어갈 수 없는 곳", "is_correct": False, "formula": "D2", "explanation": "본문에 없는 잘못된 설명입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 우체국에서 편지 배달 외에 할 수 있는 일은?",
                "options": [
                    {"label": "①", "text": "저금하기", "is_correct": True},
                    {"label": "②", "text": "운동 경기하기", "is_correct": False},
                    {"label": "③", "text": "영화 관람하기", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "우체국은 편지와 소포를 안전하게 배달해 주고 저금도 할 수 있는 곳입니다.", "is_correct": True},
                    {"label": "②", "text": "우리 마을에는 주민들의 편리한 생활을 돕는", "is_correct": False},
                    {"label": "③", "text": "공공장소는 마을 사람들이 다 함께 이용하는", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "우리 마을 공공장소 안내 카드 쓰기",
            "guide": "우체국과 보건소 중 한 곳을 골라 하는 일을 한 문장으로 소개해 보세요.",
            "template": "[우체국/보건소]은(는) 우리 마을에서 [       ]을(를) 하는 고마운 곳입니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "공공장소의 이름과 그곳에서 하는 일을 1:1로 짝지어 확인해요."},
            "step1_2_drill": {"task": "장소 그림(우체국, 보건소)과 하는 일 카드 연결하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "우체국은 소포를 배달해 주는 공공장소입니다.", "answer": "O", "reason": "본문에 명시된 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 우리 동네 공공장소",
            "situation": "동네 산책을 하며 우체국이나 보건소를 지날 때",
            "parent_question": "저기 우체국 아저씨들은 어떤 일을 하실까? 만약 우체국이 없다면 어떻게 될까?",
            "expected_answer": "편지나 택배를 보낼 수 없어서 멀리 사는 친척 소식을 알기 힘들 것 같아요!",
            "coaching_tip": "공공장소의 소중함과 고마움을 함께 느껴 보도록 이야기해 주세요."
        }
    ),

    # 2. V1-2
    build_expository_slot(
        grade_num=2,
        subskill_code="V1-2",
        subject="통합(자연 2-1) / 수학(분류)",
        unit="2. 봄에 만나는 식물",
        concept="채소의 종류와 우리가 먹는 부위",
        text_structure="분류 기초",
        structure_type_code="classification",
        passage_title="채소의 종류와 우리가 먹는 부분",
        paragraphs=[
            "우리가 매일 먹는 맛있는 채소는 식물의 어느 부위를 먹느냐에 따라 여러 종류로 나눌 수 있습니다.",
            "당근과 무는 땅속 깊이 자란 뿌리를 먹는 '뿌리채소'입니다. 시금치와 배추는 초록빛 잎을 먹는 '잎채소'입니다. 그리고 오이와 토마토는 꽃이 진 뒤 열린 열매를 먹는 '열매채소'입니다. 채소마다 먹는 부위가 다르지만 모두 몸을 건강하게 해 줍니다."
        ],
        vocab_notes=[
            {"word": "부위", "definition": "몸이나 물체의 어느 한 부분"},
            {"word": "열매채소", "definition": "열매를 주로 먹는 토마토, 오이, 호박 따위의 채소"}
        ],
        visual_html="""<div class="p-3 bg-green-50 rounded border border-green-200">
          <h4 class="font-bold text-green-900 mb-2">🥕 먹는 부위에 따른 채소 3대 분류</h4>
          <div class="grid grid-cols-3 gap-1 text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-green-200"><strong>🥕 뿌리채소</strong><br>당근, 무</div>
            <div class="p-1.5 bg-white rounded border border-green-200"><strong>🥬 잎채소</strong><br>시금치, 배추</div>
            <div class="p-1.5 bg-white rounded border border-green-200"><strong>🍅 열매채소</strong><br>오이, 토마토</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v12-c1", "text": "당근과 무는 땅속 깊이 자란 뿌리를 먹는 '뿌리채소'입니다", "role": "뿌리채소 정의", "para_idx": 1},
            {"cue_id": "g2-v12-c2", "text": "시금치와 배추는 초록빛 잎을 먹는 '잎채소'입니다", "role": "잎채소 정의", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "채소 분류 나무",
            "categories": {
                "뿌리채소": ["당근", "무"],
                "잎채소": ["시금치", "배추"],
                "열매채소": ["오이", "토마토"]
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "분류 기준 확인",
                "stem": "글에서 '오이와 토마토'는 어떤 채소로 분류되나요?",
                "target_para_idx": 1,
                "spotlight_quote": "그리고 오이와 토마토는 꽃이 진 뒤 열린 열매를 먹는 '열매채소'입니다.",
                "options": [
                    {"label": "①", "text": "땅속 뿌리를 먹는 뿌리채소", "is_correct": False, "formula": "D3", "explanation": "뿌리채소는 당근과 무입니다."},
                    {"label": "②", "text": "꽃이 진 뒤 열린 열매를 먹는 열매채소", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 올바른 분류입니다."},
                    {"label": "③", "text": "바위틈에서 자라는 버섯채소", "is_correct": False, "formula": "D1", "explanation": "글에 없는 분류입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 사실 확인",
                "stem": "글의 내용으로 보아 '시금치'에 대한 설명으로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "시금치와 배추는 초록빛 잎을 먹는 '잎채소'입니다.",
                "options": [
                    {"label": "①", "text": "초록빛 잎을 주로 먹는 잎채소이다.", "is_correct": True, "formula": "정답", "explanation": "2문단 내용과 정확히 일치합니다."},
                    {"label": "②", "text": "땅속 깊은 굵은 뿌리만 골라 먹는다.", "is_correct": False, "formula": "D4", "explanation": "뿌리채소에 대한 설명입니다."},
                    {"label": "③", "text": "줄기에서 열린 빨간 열매만 먹는다.", "is_correct": False, "formula": "D2", "explanation": "토마토에 어울리는 설명입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 채소를 여러 종류로 나누는 올바른 기준은?",
                "options": [
                    {"label": "①", "text": "식물의 어느 부위를 먹느냐에 따라", "is_correct": True},
                    {"label": "②", "text": "채소의 가격이 얼마나 비싸냐에 따라", "is_correct": False},
                    {"label": "③", "text": "어느 마트에서 파느냐에 따라", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거 문장은?",
                "options": [
                    {"label": "①", "text": "식물의 어느 부위를 먹느냐에 따라 여러 종류로 나눌 수 있습니다.", "is_correct": True},
                    {"label": "②", "text": "우리가 매일 먹는 맛있는 채소는", "is_correct": False},
                    {"label": "③", "text": "채소마다 먹는 부위가 다르지만 모두 몸을 건강하게 해 줍니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "채소 분류 표 채우기",
            "guide": "내가 좋아하는 채소 1가지가 뿌리·잎·열매 중 어디에 해당하는지 적어 보세요.",
            "template": "내가 좋아하는 채소: [       ] / 먹는 부위: [뿌리/잎/열매] / 채소 종류: [       ]채소"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "분류 설명글은 '분류 기준'과 '각 무리에 속하는 예시'를 묶어 기억해요."},
            "step1_2_drill": {"task": "당근, 배추, 토마토 그림을 뿌리·잎·열매 상자에 넣기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "무와 당근은 땅속 뿌리를 먹는 뿌리채소입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 식탁 위의 식물학",
            "situation": "식사 시간에 샐러드나 나물 반찬을 먹을 때",
            "parent_question": "지금 먹는 김치와 시금치는 식물의 어느 부분일까?",
            "expected_answer": "초록색 잎을 먹는 잎채소예요!",
            "coaching_tip": "매일 먹는 반찬 속 식물의 부위를 이야기하며 분류 감각을 키워 주세요."
        }
    ),

    # 3. V1-3
    build_expository_slot(
        grade_num=2,
        subskill_code="V1-3",
        subject="통합(자연·계절 2-1)",
        unit="3. 쑥쑥 자라는 생명",
        concept="강낭콩이 씨앗에서 열매까지 자라는 과정",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="강낭콩이 쑥쑥 자라는 신기한 과정",
        paragraphs=[
            "작고 단단한 강낭콩 씨앗을 촉촉한 흙에 심으면 놀라운 변화가 시작됩니다.",
            "며칠이 지나면 단단한 껍질이 벌어지며 하얀 뿌리가 땅속으로 뻗어 나가고, 두 장의 떡잎이 땅 위로 쑥 올라옵니다. 그 후 떡잎 사이에서 본잎이 활짝 자라나고 줄기가 굵어집니다. 여름이 되면 줄기마다 연보라색 꽃이 피고, 꽃이 진 자리에 길쭉한 꼬투리가 열려 새 강낭콩이 만들어집니다."
        ],
        vocab_notes=[
            {"word": "떡잎", "definition": "씨앗에서 싹이 틀 때 가장 먼저 나오는 잎"},
            {"word": "꼬투리", "definition": "콩과 식물의 열매를 싸고 있는 주머니"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">🌱 강낭콩의 4단계 자람 순서</h4>
          <div class="flex items-center justify-between text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-amber-200">① 씨앗 싹틈</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1.5 bg-white rounded border border-amber-200">② 떡잎·본잎</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1.5 bg-white rounded border border-amber-200">③ 꽃 핌</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1.5 bg-white rounded border border-amber-200">④ 꼬투리 열림</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v13-c1", "text": "단단한 껍질이 벌어지며 하얀 뿌리가 땅속으로 뻗어 나가고", "role": "발아 단계", "para_idx": 1},
            {"cue_id": "g2-v13-c2", "text": "꽃이 진 자리에 길쭉한 꼬투리가 열려", "role": "열매 맺힘 단계", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "과정 순서도",
            "steps": ["씨앗 심기", "뿌리와 떡잎", "본잎과 줄기", "꽃 피기", "꼬투리(열매)"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "과정 순서 파악",
                "stem": "강낭콩이 자라는 순서로 가장 알맞은 것은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "두 장의 떡잎이 땅 위로 쑥 올라옵니다. 그 후 떡잎 사이에서 본잎이 활짝 자라나고 줄기가 굵어집니다. 여름이 되면 줄기마다 연보라색 꽃이 피고, 꽃이 진 자리에 길쭉한 꼬투리가 열려 새 강낭콩이 만들어집니다.",
                "options": [
                    {"label": "①", "text": "꼬투리 열림 ➔ 꽃 피기 ➔ 떡잎 나옴", "is_correct": False, "formula": "D3", "explanation": "순서가 뒤바뀐 오답입니다."},
                    {"label": "②", "text": "떡잎 나옴 ➔ 본잎 자람 ➔ 꽃 피기 ➔ 꼬투리 열림", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 정확한 성장 순서입니다."},
                    {"label": "③", "text": "꽃 피기 ➔ 씨앗 심기 ➔ 뿌리 내림", "is_correct": False, "formula": "D4", "explanation": "원인과 결과가 뒤섞인 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 내용 확인",
                "stem": "꽃이 진 자리에는 무엇이 생겨나나요?",
                "target_para_idx": 1,
                "spotlight_quote": "꽃이 진 자리에 길쭉한 꼬투리가 열려 새 강낭콩이 만들어집니다.",
                "options": [
                    {"label": "①", "text": "새 강낭콩이 든 길쭉한 꼬투리", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 사실입니다."},
                    {"label": "②", "text": "빨간 사과 열매", "is_correct": False, "formula": "D1", "explanation": "사과나무 열매이므로 엉뚱한 오답입니다."},
                    {"label": "③", "text": "커다란 호박꽃", "is_correct": False, "formula": "D2", "explanation": "꽃이 진 뒤에 꽃이 다시 필 수는 없습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 싹이 틀 때 땅속으로 먼저 뻗어 나가는 것은?",
                "options": [
                    {"label": "①", "text": "하얀 뿌리", "is_correct": True},
                    {"label": "②", "text": "연보라색 꽃", "is_correct": False},
                    {"label": "③", "text": "길쭉한 꼬투리", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "단단한 껍질이 벌어지며 하얀 뿌리가 땅속으로 뻗어 나가고", "is_correct": True},
                    {"label": "②", "text": "작고 단단한 강낭콩 씨앗을 촉촉한 흙에 심으면", "is_correct": False},
                    {"label": "③", "text": "여름이 되면 줄기마다 연보라색 꽃이 피고", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "강낭콩 한살이 순서 번호 쓰기",
            "guide": "강낭콩의 성장 과정에 맞게 순서 번호(1~4)를 매겨 보세요.",
            "template": "( ) 꽃이 핍니다. / ( ) 떡잎이 나옵니다. / ( ) 꼬투리가 열립니다. / ( ) 흙에 씨앗을 심습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "순서가 있는 설명글은 '먼저 ➔ 그 후 ➔ 마지막으로' 연결어를 따라가요."},
            "step1_2_drill": {"task": "강낭콩 4컷 만화 카드를 시간 순서대로 나열하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "꽃이 진 자리에 길쭉한 꼬투리가 열립니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 식물의 자람 과정",
            "situation": "베란다 화분의 싹이나 꽃을 함께 볼 때",
            "parent_question": "씨앗에서 싹이 틀 때 잎과 뿌리 중에 어느 것이 먼저 땅속으로 갈까?",
            "expected_answer": "뿌리가 먼저 땅속으로 뻗어 나간 다음에 떡잎이 올라와요!",
            "coaching_tip": "작은 씨앗이 자라나는 순서를 함께 떠올려 보며 과학적 호기심을 키워 주세요."
        }
    ),

    # 4. V1-4
    build_expository_slot(
        grade_num=2,
        subskill_code="V1-4",
        subject="통합(우리나라 2-2)",
        unit="1. 전통 가옥의 지혜",
        concept="겨울에는 따뜻하고 여름에는 시원한 한옥 (온돌과 마루)",
        text_structure="비교·열거 기초",
        structure_type_code="comparison",
        passage_title="여름엔 시원하고 겨울엔 따뜻한 한옥",
        paragraphs=[
            "우리나라 전통 집인 한옥에는 조상들의 놀라운 지혜가 담겨 있습니다. 한옥은 사계절이 뚜렷한 우리나라 날씨에 맞추어 지어졌습니다.",
            "한옥에는 여름을 시원하게 보내기 위한 '대청마루'가 있습니다. 마루는 바닥에 나무를 깔아 바람이 솔솔 잘 통합니다. 반면에 추운 겨울을 따뜻하게 보내기 위한 '온돌'도 있습니다. 온돌은 방바닥 밑의 구들장에 따뜻한 불기운을 통하게 하여 방 전체를 훈훈하게 데워 줍니다."
        ],
        vocab_notes=[
            {"word": "대청마루", "definition": "한옥에서 방과 방 사이에 나무로 시원하게 깐 넓은 마루"},
            {"word": "구들장", "definition": "온돌방 바닥에 얇게 깔아 불길과 열기를 전하는 납작한 돌"}
        ],
        visual_html="""<div class="p-3 bg-yellow-50 rounded border border-yellow-200">
          <h4 class="font-bold text-yellow-900 mb-2">🏠 한옥의 2대 지혜 (마루 vs 온돌)</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-yellow-100"><th class="p-1 border border-yellow-200">구분</th><th class="p-1 border border-yellow-200">대청마루 (여름)</th><th class="p-1 border border-yellow-200">온돌 (겨울)</th></tr>
            <tr><td class="p-1 border border-yellow-200 font-bold bg-white">재료·원리</td><td class="p-1 border border-yellow-200 bg-white">나무 바닥, 바람 통함</td><td class="p-1 border border-yellow-200 bg-white">돌(구들장), 불기운 통함</td></tr>
            <tr><td class="p-1 border border-yellow-200 font-bold bg-white">효과</td><td class="p-1 border border-yellow-200 bg-white">시원한 바람</td><td class="p-1 border border-yellow-200 bg-white">따뜻한 방바닥</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v14-c1", "text": "마루는 바닥에 나무를 깔아 바람이 솔솔 잘 통합니다", "role": "대청마루 원리", "para_idx": 1},
            {"cue_id": "g2-v14-c2", "text": "구들장에 따뜻한 불기운을 통하게 하여 방 전체를 훈훈하게 데워 줍니다", "role": "온돌 원리", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "대비 구조표",
            "hanok": {
                "여름 대비": "대청마루 (나무, 통풍, 시원함)",
                "겨울 대비": "온돌 (구들장, 열기 전달, 따뜻함)"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "세부 내용 확인",
                "stem": "한옥의 '온돌'이 방을 따뜻하게 데우는 원리는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "온돌은 방바닥 밑의 구들장에 따뜻한 불기운을 통하게 하여 방 전체를 훈훈하게 데워 줍니다.",
                "options": [
                    {"label": "①", "text": "방바닥 밑 구들장에 따뜻한 불기운을 통하게 한다.", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 온돌의 작동 원리입니다."},
                    {"label": "②", "text": "지붕에 큰 얼음을 얹어 차가운 물을 흘려보낸다.", "is_correct": False, "formula": "D1", "explanation": "본문에 없는 황당한 오답입니다."},
                    {"label": "③", "text": "나무 마루에 선풍기를 틀어 놓는다.", "is_correct": False, "formula": "D3", "explanation": "전통 가옥의 원리가 아닙니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "비교·대조 파악",
                "stem": "'대청마루'와 '온돌'의 차이점으로 바른 설명은?",
                "target_para_idx": 1,
                "spotlight_quote": "마루는 바닥에 나무를 깔아 바람이 솔솔 잘 통합니다. 반면에 추운 겨울을 따뜻하게 보내기 위한 '온돌'도 있습니다.",
                "options": [
                    {"label": "①", "text": "대청마루는 여름에 시원하고, 온돌은 겨울에 따뜻하다.", "is_correct": True, "formula": "정답", "explanation": "두 구조의 계절별 역할 차이를 바르게 대조했습니다."},
                    {"label": "②", "text": "대청마루는 겨울용이고, 온돌은 여름용이다.", "is_correct": False, "formula": "D4", "explanation": "역할을 반대로 뒤바꾼 오답입니다."},
                    {"label": "③", "text": "둘 다 쇠로 만들어져 바람이 전혀 통하지 않는다.", "is_correct": False, "formula": "D2", "explanation": "나무와 돌로 만들어졌습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 한옥에 마루와 온돌이 함께 만들어진 까닭은?",
                "options": [
                    {"label": "①", "text": "사계절이 뚜렷한 우리나라 날씨에 맞추기 위해", "is_correct": True},
                    {"label": "②", "text": "외국 손님들에게 자랑하기 위해", "is_correct": False},
                    {"label": "③", "text": "방을 좁게 만들기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거 문장은?",
                "options": [
                    {"label": "①", "text": "한옥은 사계절이 뚜렷한 우리나라 날씨에 맞추어 지어졌습니다.", "is_correct": True},
                    {"label": "②", "text": "우리나라 전통 집인 한옥에는 조상들의 놀라운 지혜가 담겨 있습니다.", "is_correct": False},
                    {"label": "③", "text": "한옥에는 여름을 시원하게 보내기 위한 '대청마루'가 있습니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "한옥의 지혜 소개 문장 쓰기",
            "guide": "대청마루와 온돌의 특징을 살려 한옥 소개글을 완성해 보세요.",
            "template": "한옥은 여름에는 [       ] 덕분에 시원하고, 겨울에는 [       ] 덕분에 따뜻합니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "'대청마루-여름-시원함', '온돌-겨울-따뜻함'을 짝지어 정리해요."},
            "step1_2_drill": {"task": "계절 카드(여름, 겨울)에 맞는 한옥 시설 스티커 붙이기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "온돌은 방바닥 밑의 구들장을 데워 방을 훈훈하게 만듭니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 따뜻한 방바닥의 비밀",
            "situation": "겨울철 따뜻한 방바닥에 앉아 귤을 까먹을 때",
            "parent_question": "우리나라 아파트 바닥이 따뜻한 건 옛날 한옥의 어떤 지혜 덕분일까?",
            "expected_answer": "구들장을 데우던 옛날 온돌의 지혜 덕분에 지금도 보일러로 바닥을 데운대요!",
            "coaching_tip": "전통 과학의 원리가 현대 주택에도 이어지고 있음을 알려 주세요."
        }
    ),

    # 5. V2-1
    build_expository_slot(
        grade_num=2,
        subskill_code="V2-1",
        subject="통합(자연 2-1)",
        unit="3. 식물의 특별한 줄기",
        concept="땅속에 숨은 두 가지 줄기: 비늘줄기와 덩이줄기",
        text_structure="비교·분류 기초",
        structure_type_code="classification",
        passage_title="땅속에 숨어 있는 특별한 줄기들",
        paragraphs=[
            "식물의 줄기는 보통 땅 위로 곧게 뻗어 자라지만, 어떤 식물은 영양분을 저장하기 위해 땅속에서 줄기가 자라납니다. 이렇게 땅속에 숨은 줄기를 '땅속줄기'라고 부릅니다.",
            "양파는 잎이 비늘처럼 여러 겹으로 겹쳐져 둥글게 된 '비늘줄기'입니다. 껍질을 벗기면 하얀 겹이 계속 나옵니다. 반면에 감자는 줄기 끝에 녹말 영양분이 뚱뚱하게 뭉쳐진 '덩이줄기'입니다. 둘 다 뿌리처럼 땅속에 묻혀 있지만 실제로는 줄기입니다."
        ],
        vocab_notes=[
            {"word": "비늘줄기", "definition": "양파나 마늘처럼 잎이 비늘 모양으로 겹쳐서 둥글게 된 줄기"},
            {"word": "덩이줄기", "definition": "감자처럼 줄기 끝에 녹말이 덩어리져 굵어진 줄기"}
        ],
        visual_html="""<div class="p-3 bg-purple-50 rounded border border-purple-200">
          <h4 class="font-bold text-purple-900 mb-2">🧅 땅속줄기 두 가지 모양 비교</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-white rounded border border-purple-100 text-center"><strong>🧅 비늘줄기 (양파)</strong><br>비늘잎이 여러 겹 겹침</div>
            <div class="p-2 bg-white rounded border border-purple-100 text-center"><strong>🥔 덩이줄기 (감자)</strong><br>영양분이 덩어리로 굵어짐</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v21-c1", "text": "양파는 잎이 비늘처럼 여러 겹으로 겹쳐져 둥글게 된 '비늘줄기'입니다", "role": "비늘줄기 정의", "para_idx": 1},
            {"cue_id": "g2-v21-c2", "text": "감자는 줄기 끝에 녹말 영양분이 뚱뚱하게 뭉쳐진 '덩이줄기'입니다", "role": "덩이줄기 정의", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "비교 대조표",
            "common": "땅속에 자라며 영양분을 저장하는 줄기",
            "contrast": {
                "양파 (비늘줄기)": "여러 겹의 비늘 모양 잎",
                "감자 (덩이줄기)": "녹말이 뭉쳐진 둥근 덩어리"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "문맥 어휘 의미 추론",
                "stem": "글에서 '비늘줄기'의 특징으로 알맞은 설명은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "양파는 잎이 비늘처럼 여러 겹으로 겹쳐져 둥글게 된 '비늘줄기'입니다.",
                "options": [
                    {"label": "①", "text": "잎이 물고기 비늘처럼 여러 겹 겹쳐져 있다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 양파의 비늘줄기 특징을 설명한 내용입니다."},
                    {"label": "②", "text": "돌처럼 단단해서 아무도 껍질을 깔 수 없다.", "is_correct": False, "formula": "D1", "explanation": "양파는 부드러운 껍질을 쉽게 벗길 수 있습니다."},
                    {"label": "③", "text": "땅 위에서 나무처럼 높이 자란다.", "is_correct": False, "formula": "D3", "explanation": "땅속에서 자라는 땅속줄기입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "식물 부위 확인",
                "stem": "양파와 감자의 공통점으로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "둘 다 뿌리처럼 땅속에 묻혀 있지만 실제로는 줄기입니다.",
                "options": [
                    {"label": "①", "text": "땅속에 묻혀 있지만 실제로는 식물의 '줄기'이다.", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 과학적 공통점입니다."},
                    {"label": "②", "text": "둘 다 새콤한 맛이 나는 과일이다.", "is_correct": False, "formula": "D4", "explanation": "과일이 아닌 땅속줄기 채소입니다."},
                    {"label": "③", "text": "열매가 하늘을 날아다닌다.", "is_correct": False, "formula": "D5", "explanation": "허구의 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 감자가 땅속에서 뚱뚱해진 까닭은?",
                "options": [
                    {"label": "①", "text": "녹말 영양분이 줄기 끝에 뭉쳐 저장되었기 때문에", "is_correct": True},
                    {"label": "②", "text": "돌을 많이 집어먹어서", "is_correct": False},
                    {"label": "③", "text": "비가 너무 많이 내려 부풀어서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거 문장은?",
                "options": [
                    {"label": "①", "text": "감자는 줄기 끝에 녹말 영양분이 뚱뚱하게 뭉쳐진 '덩이줄기'입니다.", "is_correct": True},
                    {"label": "②", "text": "껍질을 벗기면 하얀 겹이 계속 나옵니다.", "is_correct": False},
                    {"label": "③", "text": "식물의 줄기는 보통 땅 위로 곧게 뻗어 자라지만,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "땅속줄기 관찰 카드 작성하기",
            "guide": "양파와 감자가 땅속줄기임을 설명하는 짧은 글을 완성해 보세요.",
            "template": "양파는 겹겹이 쌓인 [비늘줄기]이고, 감자는 영양분이 뭉친 [덩이줄기]입니다. 둘 다 식물의 [       ]입니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "겉모습은 뿌리 같지만 싹과 눈이 나는 감자·양파는 줄기예요."},
            "step1_2_drill": {"task": "양파(비늘줄기)와 감자(덩이줄기) 낱말 카드 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "감자는 뿌리가 아니라 땅속에서 자란 줄기입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 감자는 뿌리일까, 줄기일까?",
            "situation": "카레나 볶음밥에 감자와 양파를 썰어 넣을 때",
            "parent_question": "땅속에서 캐내는 감자는 식물의 뿌리일까, 줄기일까?",
            "expected_answer": "뿌리처럼 보이지만 영양분을 저장한 특별한 줄기(덩이줄기)래요!",
            "coaching_tip": "식재료의 생태적 비밀을 직접 껍질을 보며 재미있게 나눠 보세요."
        }
    ),

    # 6. V2-2
    build_expository_slot(
        grade_num=2,
        subskill_code="V2-2",
        subject="통합(물건·기억 2-2)",
        unit="2. 지구를 살리는 재활용",
        concept="헌 종이가 새 종이로 태어나는 재생종이 만들기",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="헌 종이의 변신! 재생종이 만들기",
        paragraphs=[
            "다 쓴 공책이나 신문지를 버리지 않고 다시 모으면 나무를 베지 않고도 새로운 종이를 만들 수 있습니다. 이것을 '재생종이'라고 부릅니다.",
            "재생종이를 만드는 과정은 흥미롭습니다. 먼저 헌 종이를 손으로 잘게 찢어 따뜻한 물에 하루 동안 불립니다. 다음으로 믹서기에 물과 함께 넣고 곱게 갈아 종이죽을 만듭니다. 그 후 거름망 틀로 종이죽을 평평하게 건져 올려 물기를 꼭 짭니다. 마지막으로 햇볕에 바짝 말리면 환경을 살리는 튼튼한 재생종이가 완성됩니다."
        ],
        vocab_notes=[
            {"word": "재생종이", "definition": "버려진 종이를 재활용하여 다시 만든 종이"},
            {"word": "종이죽", "definition": "물에 불린 종이를 갈아서 죽처럼 만든 것"}
        ],
        visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">📜 재생종이 만드는 4단계 순서도</h4>
          <div class="grid grid-cols-4 gap-1 text-xs text-center">
            <div class="p-1 bg-white rounded border border-emerald-200">1. 잘게 찢기</div>
            <div class="p-1 bg-white rounded border border-emerald-200">2. 갈아서 종이죽</div>
            <div class="p-1 bg-white rounded border border-emerald-200">3. 틀로 건지기</div>
            <div class="p-1 bg-white rounded border border-emerald-200">4. 햇볕에 말리기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v22-c1", "text": "헌 종이를 손으로 잘게 찢어 따뜻한 물에 하루 동안 불립니다", "role": "1단계 준비", "para_idx": 1},
            {"cue_id": "g2-v22-c2", "text": "마지막으로 햇볕에 바짝 말리면", "role": "최종 완성 단계", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "제작 순서 흐름도",
            "steps": ["헌 종이 찢기", "물에 불려 갈기(종이죽)", "틀로 건져 물기 짜기", "햇볕에 말리기"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "과정 순서 확인",
                "stem": "재생종이를 만들 때 '종이죽을 만든 뒤'에 해야 할 일은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "그 후 거름망 틀로 종이죽을 평평하게 건져 올려 물기를 꼭 짭니다.",
                "options": [
                    {"label": "①", "text": "거름망 틀로 평평하게 건져 물기를 짠다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 종이죽을 만든 후 거름망 틀로 건진다고 했습니다."},
                    {"label": "②", "text": "신문지를 가위로 잘라 쓰레기통에 버린다.", "is_correct": False, "formula": "D3", "explanation": "재활용 과정과 정반대 행동입니다."},
                    {"label": "③", "text": "종이죽을 프라이팬에 넣고 기름에 볶는다.", "is_correct": False, "formula": "D1", "explanation": "요리가 아니므로 황당한 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "인과 관계 파악",
                "stem": "우리가 재생종이를 만들어 쓰면 어떤 좋은 점이 있나요?",
                "target_para_idx": 0,
                "spotlight_quote": "다 쓴 공책이나 신문지를 버리지 않고 다시 모으면 나무를 베지 않고도 새로운 종이를 만들 수 있습니다.",
                "options": [
                    {"label": "①", "text": "살아 있는 나무를 베지 않아 숲을 지킬 수 있다.", "is_correct": True, "formula": "정답", "explanation": "1문단에 제시된 재생종이의 환경적 효과입니다."},
                    {"label": "②", "text": "종이가 너무 무거워져서 가방이 찢어진다.", "is_correct": False, "formula": "D4", "explanation": "본문과 무관한 부정적 서술입니다."},
                    {"label": "③", "text": "종이에 연필 글씨를 쓸 수 없게 된다.", "is_correct": False, "formula": "D2", "explanation": "재생종이에도 글씨를 쓸 수 있습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 헌 종이를 물에 넣고 믹서기로 갈았을 때 생기는 것은?",
                "options": [
                    {"label": "①", "text": "종이죽", "is_correct": True},
                    {"label": "②", "text": "플라스틱 가루", "is_correct": False},
                    {"label": "③", "text": "쇠구슬", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "믹서기에 물과 함께 넣고 곱게 갈아 종이죽을 만듭니다.", "is_correct": True},
                    {"label": "②", "text": "재생종이를 만드는 과정은 흥미롭습니다.", "is_correct": False},
                    {"label": "③", "text": "마지막으로 햇볕에 바짝 말리면", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "재생종이 만들기 순서 정리하기",
            "guide": "재생종이 만드는 4단계 순서 말을 완성해 보세요.",
            "template": "1. 찢기 ➔ 2. 물에 불려 [       ] 만들기 ➔ 3. 거름망 틀로 건지기 ➔ 4. [       ]에 말리기"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "만드는 법 설명글은 '재료 준비 ➔ 만들기 단계 ➔ 완성'을 순서대로 읽어요."},
            "step1_2_drill": {"task": "재생종이 만들기 과정 그림 카드 순서 맞추기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "재생종이를 쓰면 나무를 베지 않아도 됩니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 종이의 재활용",
            "situation": "다 쓴 스케치북이나 종이 상자를 분리배출할 때",
            "parent_question": "우리가 모은 이 폐지들은 어디로 가서 무엇이 될까?",
            "expected_answer": "공장으로 가서 물에 갈아 종이죽을 만들고, 새 재생종이로 다시 태어난대요!",
            "coaching_tip": "환경 보호와 자원 순환의 가치를 일상에서 체감하도록 도와주세요."
        }
    ),

    # 7. V2-3
    build_expository_slot(
        grade_num=2,
        subskill_code="V2-3",
        subject="통합(자연 2-1)",
        unit="3. 곤충의 세계",
        concept="땅속 개미집의 여러 방과 개미들의 이동 길",
        text_structure="분석(전체-부분)·공간",
        structure_type_code="analysis",
        passage_title="땅속 개미집의 신기한 방들",
        paragraphs=[
            "작은 개미들은 땅속에 놀랍도록 정교한 미로 같은 큰 집을 짓고 함께 모여 살아갑니다. 땅 위에서는 작은 구멍 하나만 보이지만 땅속에는 수많은 방과 통로가 연결되어 있습니다.",
            "개미집 가장 깊숙하고 안전한 곳에는 여왕개미가 알을 낳는 '여왕개미 방'이 있습니다. 그 주변에는 알과 애벌레를 소중히 돌보는 '애벌레 방'과 겨울을 나기 위해 씨앗을 모아 두는 '먹이 창고'가 있습니다. 또한 쓰레기를 버리는 '쓰레기 방'도 따로 있어 개미집은 언제나 깨끗합니다."
        ],
        vocab_notes=[
            {"word": "통로", "definition": "이리저리 오갈 수 있게 이어진 길"},
            {"word": "먹이 창고", "definition": "구한 먹이를 상하지 않게 안전하게 모아 두는 방"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">🐜 땅속 개미집 단면 구조도</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-amber-200">👑 <strong>여왕개미 방:</strong> 가장 깊고 안전한 곳, 알 낳기</div>
            <div class="p-1 bg-white rounded border border-amber-200">🍼 <strong>애벌레 방:</strong> 알과 애벌레 보살피기</div>
            <div class="p-1 bg-white rounded border border-amber-200">🌾 <strong>먹이 창고:</strong> 모은 씨앗과 먹이 보관</div>
            <div class="p-1 bg-white rounded border border-amber-200">🗑️ <strong>쓰레기 방:</strong> 찌꺼기를 모아 두어 위생 유지</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v23-c1", "text": "가장 깊숙하고 안전한 곳에는 여왕개미가 알을 낳는 '여왕개미 방'이 있습니다", "role": "여왕개미 방 위치와 역할", "para_idx": 1},
            {"cue_id": "g2-v23-c2", "text": "쓰레기를 버리는 '쓰레기 방'도 따로 있어 개미집은 언제나 깨끗합니다", "role": "쓰레기 방 역할", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "전체-부분 공간 구조도",
            "structure": "땅속 개미집",
            "rooms": {
                "여왕개미 방": "알 낳기 (가장 깊은 곳)",
                "애벌레 방": "새끼 돌보기",
                "먹이 창고": "씨앗 보관",
                "쓰레기 방": "청결 유지"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "공간 위치와 역할 확인",
                "stem": "개미집에서 '가장 깊숙하고 안전한 곳'에 있는 방은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "개미집 가장 깊숙하고 안전한 곳에는 여왕개미가 알을 낳는 '여왕개미 방'이 있습니다.",
                "options": [
                    {"label": "①", "text": "쓰레기를 버리는 쓰레기 방", "is_correct": False, "formula": "D3", "explanation": "쓰레기 방은 따로 마련된 방입니다."},
                    {"label": "②", "text": "여왕개미가 알을 낳는 여왕개미 방", "is_correct": True, "formula": "정답", "explanation": "2문단 첫 문장에 명시된 사실입니다."},
                    {"label": "③", "text": "손님 개미가 묵는 호텔 방", "is_correct": False, "formula": "D1", "explanation": "글에 없는 상상의 방입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 내용 확인",
                "stem": "개미집이 항상 깨끗하게 유지될 수 있는 까닭은?",
                "target_para_idx": 1,
                "spotlight_quote": "또한 쓰레기를 버리는 '쓰레기 방'도 따로 있어 개미집은 언제나 깨끗합니다.",
                "options": [
                    {"label": "①", "text": "쓰레기를 따로 모아 버리는 '쓰레기 방'이 있어서", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 명확한 까닭입니다."},
                    {"label": "②", "text": "청소차 아저씨가 날마다 땅속으로 내려와서", "is_correct": False, "formula": "D5", "explanation": "자연 곤충 세계와 맞지 않는 엉뚱한 오답입니다."},
                    {"label": "③", "text": "개미들이 먹이를 전혀 먹지 않아서", "is_correct": False, "formula": "D4", "explanation": "먹이 창고에 씨앗을 모은다고 했습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 겨울을 나기 위해 씨앗을 모아 두는 방은 어디인가요?",
                "options": [
                    {"label": "①", "text": "먹이 창고", "is_correct": True},
                    {"label": "②", "text": "놀이터 방", "is_correct": False},
                    {"label": "③", "text": "목욕탕 방", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "겨울을 나기 위해 씨앗을 모아 두는 '먹이 창고'가 있습니다.", "is_correct": True},
                    {"label": "②", "text": "땅 위에서는 작은 구멍 하나만 보이지만", "is_correct": False},
                    {"label": "③", "text": "작은 개미들은 땅속에 놀랍도록 정교한 미로 같은 큰 집을 짓고", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "개미집 방 안내도 완성하기",
            "guide": "개미집의 여러 방 중 2개의 이름과 역할을 써 보세요.",
            "template": "1. [여왕개미] 방: 알을 낳는 곳 / 2. [       ] 방: [       ]을 모아 두는 곳"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "공간 구조 글은 그림을 보듯 '어디에 어떤 방이 있는지' 짝지어 읽어요."},
            "step1_2_drill": {"task": "개미집 단면 그림에서 각 방의 이름표 붙이기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "개미집에는 쓰레기만 모아 두는 방이 따로 있습니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 보이지 않는 땅속 세상",
            "situation": "길가 보도블록 틈에서 줄지어 가는 개미를 발견했을 때",
            "parent_question": "저 작은 구멍 아래에는 어떤 신기한 방들이 숨어 있을까?",
            "expected_answer": "여왕개미 방, 아기 애벌레 방, 먹이 창고, 쓰레기 방까지 있대요!",
            "coaching_tip": "작은 곤충의 지혜로운 사회적 삶을 상상해 보도록 대화를 이끌어 주세요."
        }
    ),

    # 8. V2-4
    build_expository_slot(
        grade_num=2,
        subskill_code="V2-4",
        subject="통합(나·안전 2-1)",
        unit="4. 안전하게 생활해요",
        concept="자전거를 안전하게 타는 방법과 보호 장구",
        text_structure="열거·안내",
        structure_type_code="sequence",
        passage_title="씽씽 자전거를 안전하게 타는 규칙",
        paragraphs=[
            "자전거는 재미있고 건강에도 좋은 운동이지만, 안전 규칙을 지키지 않으면 큰 사고가 날 수 있습니다. 자전거를 타기 전과 탈 때 지켜야 할 약속이 있습니다.",
            "먼저 머리를 보호하는 안전모와 무릎 보호대를 반드시 착용해야 합니다. 머리는 부딪히면 매우 위험하기 때문입니다. 그리고 자전거 도로를 이용하고, 어두운 저녁에는 앞뒤에 전조등과 반사판을 켜야 합니다. 이 글은 어린이들이 다치지 않고 안전하게 자전거를 타도록 돕기 위해 쓴 안내글입니다."
        ],
        vocab_notes=[
            {"word": "보호 장구", "definition": "몸이 다치지 않도록 보호하기 위해 착용하는 장비"},
            {"word": "전조등", "definition": "어두운 곳에서 앞을 밝히기 위해 자전거 앞부분에 다는 전등"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">🚴 자전거 안전 수칙 체크리스트</h4>
          <ul class="text-xs space-y-1 text-slate-700">
            <li>✔ <strong>보호 장구 착용:</strong> 머리 안전모(헬멧), 팔꿈치·무릎 보호대</li>
            <li>✔ <strong>길 선택:</strong> 차도가 아닌 자전거 전용 도로 이용</li>
            <li>✔ <strong>야간 장비:</strong> 어두울 때는 앞뒤 불빛(전조등, 반사판) 켜기</li>
          </ul>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v24-c1", "text": "머리를 보호하는 안전모와 무릎 보호대를 반드시 착용해야 합니다", "role": "보호 장구 규칙", "para_idx": 1},
            {"cue_id": "g2-v24-c2", "text": "이 글은 어린이들이 다치지 않고 안전하게 자전거를 타도록 돕기 위해", "role": "글쓴이의 목적", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "안내 점검표",
            "purpose": "안전한 자전거 타기 안내",
            "checklist": ["안전모 착용", "자전거 도로 이용", "저녁 전조등 켜기"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "글쓴이의 목적 추론",
                "stem": "글쓴이가 이 글을 쓴 까닭(목적)으로 가장 알맞은 것은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "이 글은 어린이들이 다치지 않고 안전하게 자전거를 타도록 돕기 위해 쓴 안내글입니다.",
                "options": [
                    {"label": "①", "text": "새로운 비싼 자전거를 사라고 광고하기 위해", "is_correct": False, "formula": "D3", "explanation": "상업 광고 글이 아닙니다."},
                    {"label": "②", "text": "어린이들이 다치지 않고 안전하게 자전거를 타도록 돕기 위해", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 글쓴이의 집필 목적입니다."},
                    {"label": "③", "text": "자전거 시합에서 무조건 1등 하는 비결을 자랑하기 위해", "is_correct": False, "formula": "D4", "explanation": "시합 1등과 무관한 안전 안내글입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 안전 수칙 확인",
                "stem": "어두운 저녁에 자전거를 탈 때 반드시 지켜야 할 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "어두운 저녁에는 앞뒤에 전조등과 반사판을 켜야 합니다.",
                "options": [
                    {"label": "①", "text": "앞뒤에 전조등과 반사판을 켠다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 야간 안전 수칙입니다."},
                    {"label": "②", "text": "눈을 감고 최고 속도로 달린다.", "is_correct": False, "formula": "D1", "explanation": "매우 위험한 행동입니다."},
                    {"label": "③", "text": "안전모를 벗어 가방에 넣는다.", "is_correct": False, "formula": "D2", "explanation": "안전모는 반드시 착용해야 합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 안전모를 반드시 써야 하는 까닭은?",
                "options": [
                    {"label": "①", "text": "부딪혔을 때 머리를 안전하게 보호하기 위해", "is_correct": True},
                    {"label": "②", "text": "머리 모양을 예쁘게 만들기 위해", "is_correct": False},
                    {"label": "③", "text": "키가 더 커 보이게 하려고", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "머리는 부딪히면 매우 위험하기 때문입니다.", "is_correct": True},
                    {"label": "②", "text": "자전거는 재미있고 건강에도 좋은 운동이지만,", "is_correct": False},
                    {"label": "③", "text": "그리고 자전거 도로를 이용하고,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "나의 자전거 안전 서약서 쓰기",
            "guide": "자전거를 탈 때 지킬 약속 1가지를 정해 서약해 보세요.",
            "template": "나는 자전거를 탈 때 꼭 [       ]을(를) 착용하고, [자전거 도로]로 다니겠습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "안내글을 읽을 때는 '글쓴이가 독자에게 무엇을 하라고 당부하는지' 찾아봐요."},
            "step1_2_drill": {"task": "자전거 안전 행동(O)과 위험한 행동(X) 구별하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "저녁에는 다른 사람 눈에 잘 띄도록 전조등을 켜야 합니다.", "answer": "O", "reason": "본문에 나온 안전 수칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 안전 장구의 중요성",
            "situation": "주말에 아이와 자전거를 타러 나가기 전",
            "parent_question": "안전모가 조금 답답해도 꼭 써야 하는 까닭은 무엇일까?",
            "expected_answer": "넘어졌을 때 우리 몸에서 가장 소중한 머리를 다치지 않게 보호해 주기 때문이에요!",
            "coaching_tip": "스스로 안전모 턱끈을 조이도록 칭찬하며 안전 의식을 심어 주세요."
        }
    ),

    # 9. V3-1
    build_expository_slot(
        grade_num=2,
        subskill_code="V3-1",
        subject="수학(여러 가지 도형 2-1)",
        unit="2. 여러 가지 도형",
        concept="색종이로 삼각형과 사각형 모양 접기 안내글",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="색종이로 삼각형과 사각형 접기",
        paragraphs=[
            "반듯한 정사각형 색종이 한 장으로 여러 가지 도형을 만들 수 있습니다. 도형 접기 안내글을 읽을 때는 글의 설명과 그림 번호가 잘 맞는지 확인해야 합니다.",
            "먼저 색종이를 마주 보는 꼭짓점끼리 대각선으로 반 접으면 곧은 선이 3개인 '삼각형'이 됩니다. 반면에 마주 보는 변끼리 반듯하게 네모로 반 접으면 곧은 선이 4개인 '직사각형'이 됩니다. 접는 방향에 따라 서로 다른 멋진 도형이 만들어집니다."
        ],
        vocab_notes=[
            {"word": "꼭짓점", "definition": "도형에서 곧은 선과 곧은 선이 만나는 뾰족한 점"},
            {"word": "대각선", "definition": "마주 보는 꼭짓점을 잇는 비스듬한 선"}
        ],
        visual_html="""<div class="p-3 bg-indigo-50 rounded border border-indigo-200">
          <h4 class="font-bold text-indigo-900 mb-2">📐 색종이 접기 도형 비교</h4>
          <div class="grid grid-cols-2 gap-2 text-xs text-center">
            <div class="p-2 bg-white rounded border border-indigo-200"><strong>🔺 삼각형 접기</strong><br>대각선 꼭짓점 맞닿게 반 접기<br>(변 3개, 꼭짓점 3개)</div>
            <div class="p-2 bg-white rounded border border-indigo-200"><strong>🟦 사각형 접기</strong><br>마주 보는 변 반듯하게 반 접기<br>(변 4개, 꼭짓점 4개)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v31-c1", "text": "마주 보는 꼭짓점끼리 대각선으로 반 접으면 곧은 선이 3개인 '삼각형'이 됩니다", "role": "삼각형 접기 방법", "para_idx": 1},
            {"cue_id": "g2-v31-c2", "text": "마주 보는 변끼리 반듯하게 네모로 반 접으면 곧은 선이 4개인 '직사각형'이 됩니다", "role": "사각형 접기 방법", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "도형 접기 분류도",
            "square_paper": "정사각형 색종이",
            "diagonal_fold": "삼각형 (변 3개)",
            "straight_fold": "직사각형 (변 4개)"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "도형의 특징 확인",
                "stem": "색종이를 마주 보는 꼭짓점끼리 대각선으로 반 접었을 때 만들어지는 도형은?",
                "target_para_idx": 1,
                "spotlight_quote": "먼저 색종이를 마주 보는 꼭짓점끼리 대각선으로 반 접으면 곧은 선이 3개인 '삼각형'이 됩니다.",
                "options": [
                    {"label": "①", "text": "곧은 선이 3개인 삼각형", "is_correct": True, "formula": "정답", "explanation": "2문단 첫 문장에 명시된 도형의 이름과 특징입니다."},
                    {"label": "②", "text": "곧은 선이 하나도 없는 동그라미", "is_correct": False, "formula": "D3", "explanation": "원은 반 접어서 바로 만들 수 없습니다."},
                    {"label": "③", "text": "별 모양 오각형", "is_correct": False, "formula": "D1", "explanation": "글의 설명과 다른 도형입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "시각 자료 일치 확인",
                "stem": "글의 2문단 '직사각형 접기' 설명 옆에 넣을 삽화로 가장 어울리는 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "반면에 마주 보는 변끼리 반듯하게 네모로 반 접으면 곧은 선이 4개인 '직사각형'이 됩니다.",
                "options": [
                    {"label": "①", "text": "색종이의 위아래 변을 나란히 맞추어 반 접는 그림", "is_correct": True, "formula": "정답", "explanation": "마주 보는 변을 반듯하게 반 접는 설명과 정확히 일치하는 삽화입니다."},
                    {"label": "②", "text": "가위로 색종이를 둥글게 오려 내는 그림", "is_correct": False, "formula": "D4", "explanation": "오리는 것은 접기 설명과 어긋납니다."},
                    {"label": "③", "text": "색종이를 구겨서 쓰레기통에 넣는 그림", "is_correct": False, "formula": "D5", "explanation": "엉뚱한 그림입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 접는 방법에 따라 삼각형과 사각형이 달라지는 까닭은?",
                "options": [
                    {"label": "①", "text": "접어서 생기는 곧은 선과 꼭짓점의 수가 달라지기 때문에", "is_correct": True},
                    {"label": "②", "text": "색종이의 색깔이 바뀌기 때문에", "is_correct": False},
                    {"label": "③", "text": "종이의 무게가 가벼워지기 때문에", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "접는 방향에 따라 서로 다른 멋진 도형이 만들어집니다.", "is_correct": True},
                    {"label": "②", "text": "반듯한 정사각형 색종이 한 장으로 여러 가지 도형을 만들 수 있습니다.", "is_correct": False},
                    {"label": "③", "text": "도형 접기 안내글을 읽을 때는", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "도형 접기 안내문 쓰기",
            "guide": "삼각형을 접는 방법을 친구에게 말하듯 한 문장으로 써 보세요.",
            "template": "색종이의 마주 보는 [꼭짓점]을 맞추어 대각선으로 접으면 [삼각형]이 됩니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "도형 설명글은 꼭짓점과 곧은 선(변)의 개수를 세며 읽어요."},
            "step1_2_drill": {"task": "삼각형(3개 변)과 사각형(4개 변) 그림 연결하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "색종이를 대각선으로 반 접으면 삼각형이 됩니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 색종이와 도형",
            "situation": "식탁에서 냅킨이나 종이를 접어 볼 때",
            "parent_question": "네모난 냅킨을 세모로 만들려면 어떻게 접어야 할까?",
            "expected_answer": "마주 보는 뾰족한 꼭짓점끼리 대각선으로 반 접으면 돼요!",
            "coaching_tip": "도형의 꼭짓점과 변의 개념을 손으로 직접 만지며 체득하게 해 주세요."
        }
    ),

    # 10. V3-2
    build_expository_slot(
        grade_num=2,
        subskill_code="V3-2",
        subject="통합(자연 2-1)",
        unit="3. 물가에 사는 동물",
        concept="올챙이가 개구리로 자라는 관찰 기록장",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="꼬물꼬물 올챙이의 자람 관찰 일기",
        paragraphs=[
            "봄이 되면 연못에 동글동글한 개구리알이 가득 생겨납니다. 알에서 깨어난 올챙이는 꼬리를 흔들며 헤엄치지만, 자라면서 몸의 모습이 크게 변합니다.",
            "올챙이는 먼저 뒷다리가 쑥 나옵니다. 그 다음에 앞다리가 쏙 나오고, 헤엄치던 긴 꼬리가 점점 짧아지며 몸속으로 흡수됩니다. 마지막으로 허파로 숨을 쉬며 물 밖으로 뛰어오르는 진짜 개구리가 됩니다. 관찰 일기는 이러한 변화 과정을 사실 그대로 정확히 기록해야 합니다."
        ],
        vocab_notes=[
            {"word": "흡수", "definition": "빨아들여져 몸 안으로 사라지거나 합쳐짐"},
            {"word": "허파", "definition": "공기 중의 산소로 숨을 쉬는 가슴속 호흡 기관"}
        ],
        visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
          <h4 class="font-bold text-teal-900 mb-2">🐸 개구리 한살이 관찰 다이어그램</h4>
          <div class="flex items-center justify-between text-xs text-center">
            <div class="p-1 bg-white rounded border border-teal-200">1. 알</div>
            <div class="text-teal-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-teal-200">2. 올챙이</div>
            <div class="text-teal-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-teal-200">3. 뒷다리 나옴</div>
            <div class="text-teal-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-teal-200">4. 앞다리 나옴</div>
            <div class="text-teal-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-teal-200">5. 꼬리 사라짐(개구리)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v32-c1", "text": "올챙이는 먼저 뒷다리가 쑥 나옵니다", "role": "다리 나오는 순서 (뒷다리 먼저)", "para_idx": 1},
            {"cue_id": "g2-v32-c2", "text": "긴 꼬리가 점점 짧아지며 몸속으로 흡수됩니다", "role": "꼬리의 변화", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "성장 단계 순서도",
            "phases": ["알", "올챙이", "뒷다리", "앞다리", "꼬리 흡수", "개구리 완성"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "관찰 사실 순서 확인",
                "stem": "올챙이에서 다리가 나올 때 올바른 순서는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "올챙이는 먼저 뒷다리가 쑥 나옵니다. 그 다음에 앞다리가 쏙 나오고,",
                "options": [
                    {"label": "①", "text": "뒷다리가 먼저 나오고, 그 다음에 앞다리가 나온다.", "is_correct": True, "formula": "정답", "explanation": "2문단 첫 문장에 서술된 실제 과학적 관찰 사실입니다."},
                    {"label": "②", "text": "앞다리가 먼저 나오고 뒷다리는 나중에 나온다.", "is_correct": False, "formula": "D3", "explanation": "순서를 반대로 뒤바꾼 대표적 함정입니다."},
                    {"label": "③", "text": "날개가 먼저 돋아나 하늘을 난다.", "is_correct": False, "formula": "D1", "explanation": "개구리에게는 날개가 없습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "사실과 과장 변별",
                "stem": "관찰 일기에 들어갈 '진짜 사실' 문장으로 알맞은 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "마지막으로 허파로 숨을 쉬며 물 밖으로 뛰어오르는 진짜 개구리가 됩니다.",
                "options": [
                    {"label": "①", "text": "개구리는 물 밖으로 나와 허파로 숨을 쉰다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 생물학적 사실입니다."},
                    {"label": "②", "text": "올챙이가 안경을 쓰고 연못에서 책을 읽는다.", "is_correct": False, "formula": "D5", "explanation": "동화 속 상상 표현입니다."},
                    {"label": "③", "text": "개구리는 겨울에 얼음 위에서 스케이트를 탄다.", "is_correct": False, "formula": "D4", "explanation": "지어낸 이야기입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 올챙이의 꼬리는 개구리가 되면서 어떻게 변하나요?",
                "options": [
                    {"label": "①", "text": "점점 짧아져 몸속으로 흡수된다.", "is_correct": True},
                    {"label": "②", "text": "가위로 자른 것처럼 뚝 떨어져 나간다.", "is_correct": False},
                    {"label": "③", "text": "뱀처럼 길어져 똬리를 튼다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 문장은?",
                "options": [
                    {"label": "①", "text": "긴 꼬리가 점점 짧아지며 몸속으로 흡수됩니다.", "is_correct": True},
                    {"label": "②", "text": "봄이 되면 연못에 동글동글한 개구리알이 가득 생겨납니다.", "is_correct": False},
                    {"label": "③", "text": "관찰 일기는 이러한 변화 과정을 사실 그대로 정확히 기록해야 합니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "올챙이 관찰 보고 문장 쓰기",
            "guide": "올챙이의 다리 나오는 순서를 사실대로 적어 보세요.",
            "template": "올챙이는 [뒷다리]가 먼저 나오고, 그 다음에 [앞다리]가 나옵니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "동물 관찰 기록은 신체 부위가 변하는 순서를 정확한 사실로 적어요."},
            "step1_2_drill": {"task": "올챙이 다리 변화 그림 순서대로 카드 맞추기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "올챙이는 뒷다리가 앞다리보다 먼저 나옵니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 개구리의 다리 순서",
            "situation": "개구리 노래('개울가에 올챙이 한 마리~')를 흥얼거릴 때",
            "parent_question": "올챙이 다리는 앞다리가 먼저 나올까, 뒷다리가 먼저 나올까?",
            "expected_answer": "노래 가사처럼 뒷다리가 쑥 나온 다음에 앞다리가 쏙 나와요!",
            "coaching_tip": "친숙한 동요와 실제 과학적 사실을 연결해 확인해 주면 기억이 오래갑니다."
        }
    ),

    # 11. V3-3
    build_expository_slot(
        grade_num=2,
        subskill_code="V3-3",
        subject="수학(표와 그래프 2-2) / 통합(마을)",
        unit="3. 세계의 다양한 집",
        concept="세계 여러 나라의 전통 집 (글 자료 ㉮와 기후 표 ㉯)",
        text_structure="열거·인과 기초",
        structure_type_code="classification",
        passage_title="기후에 맞춘 세계의 전통 집 (글 ㉮와 표 ㉯)",
        paragraphs=[
            "[글 자료 ㉮] 세계 여러 나라 사람들은 자신이 사는 곳의 날씨에 맞추어 독특한 집을 지었습니다. 눈과 얼음이 많은 추운 북극 지역 사람들은 얼음 블록을 둥글게 쌓아 올려 '이글루'를 만들었습니다. 반면에 덥고 비가 많이 오는 열대 지역 사람들은 땅의 뜨거운 열기와 습기를 피하기 위해 기둥을 높이 세운 '고상 가옥'을 지었습니다.",
            "[표 자료 ㉯] 기후별 전통 집 특징 표를 보면, 북극(매우 추움)은 얼음벽으로 찬 바람을 막고, 열대(매우 덥고 습함)는 높은 마루 기둥으로 뱀과 벌레, 빗물을 피한다고 정리되어 있습니다. 두 자료를 합쳐 보면 집의 재료와 모양은 기후를 이겨내기 위한 지혜임을 알 수 있습니다."
        ],
        vocab_notes=[
            {"word": "고상 가옥", "definition": "땅바닥에서 기둥을 높이 세워 마루를 땅 위로 띄워 지은 집"},
            {"word": "습기", "definition": "공기나 땅속에 축축하게 스며 있는 수분"}
        ],
        visual_html="""<div class="p-3 bg-orange-50 rounded border border-orange-200">
          <h4 class="font-bold text-orange-900 mb-2">🌍 기후별 세계 전통 가옥 비교표</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-orange-100"><th class="p-1 border border-orange-200">지역</th><th class="p-1 border border-orange-200">전통 집 이름</th><th class="p-1 border border-orange-200">짓는 재료</th><th class="p-1 border border-orange-200">집의 목적</th></tr>
            <tr><td class="p-1 border border-orange-200 font-bold bg-white">북극 (한대)</td><td class="p-1 border border-orange-200 bg-white">이글루</td><td class="p-1 border border-orange-200 bg-white">단단한 얼음 벽돌</td><td class="p-1 border border-orange-200 bg-white">강한 눈보라와 추위 방어</td></tr>
            <tr><td class="p-1 border border-orange-200 font-bold bg-white">열대 (밀림)</td><td class="p-1 border border-orange-200 bg-white">고상 가옥</td><td class="p-1 border border-orange-200 bg-white">긴 나무 기둥, 풀</td><td class="p-1 border border-orange-200 bg-white">땅의 열기·습기·벌레 차단</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-v33-c1", "text": "얼음 블록을 둥글게 쌓아 올려 '이글루'를 만들었습니다", "role": "북극 이글루 특징", "para_idx": 0},
            {"cue_id": "g2-v33-c2", "text": "기둥을 높이 세운 '고상 가옥'을 지었습니다", "role": "열대 고상 가옥 특징", "para_idx": 0}
        ],
        graphic_organizer={
            "diagram_type": "다중 자료 비교 매트릭스",
            "source_a": "글 ㉮: 지역별 전통 집 이야기",
            "source_b": "표 ㉯: 기후와 건축 목적 데이터",
            "integration": "이글루(얼음·보온) vs 고상 가옥(기둥·통풍)"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "다중 자료 정보 통합",
                "stem": "글 ㉮와 표 ㉯를 합쳐 보았을 때, 열대 지역에서 '기둥을 높이 세운 고상 가옥'을 지은 까닭은?",
                "target_para_idx": 0,
                "spotlight_quote": "덥고 비가 많이 오는 열대 지역 사람들은 땅의 뜨거운 열기와 습기를 피하기 위해 기둥을 높이 세운 '고상 가옥'을 지었습니다.",
                "options": [
                    {"label": "①", "text": "땅의 뜨거운 열기와 습기, 벌레를 피하기 위해", "is_correct": True, "formula": "정답", "explanation": "글 ㉮와 표 ㉯에 명시된 고상 가옥의 핵심 건축 이유입니다."},
                    {"label": "②", "text": "눈보라를 맞아 얼음 벽돌을 굳히기 위해", "is_correct": False, "formula": "D3", "explanation": "북극 이글루에 어울리는 내용입니다."},
                    {"label": "③", "text": "우주선을 타고 달나라에 가기 위해", "is_correct": False, "formula": "D1", "explanation": "글과 상관없는 황당한 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 사실 확인",
                "stem": "북극의 '이글루'에 대한 설명으로 알맞은 것은?",
                "target_para_idx": 0,
                "spotlight_quote": "눈과 얼음이 많은 추운 북극 지역 사람들은 얼음 블록을 둥글게 쌓아 올려 '이글루'를 만들었습니다.",
                "options": [
                    {"label": "①", "text": "단단한 얼음 블록을 쌓아 만들어 찬 바람을 막는다.", "is_correct": True, "formula": "정답", "explanation": "글 ㉮와 표 ㉯에 나오는 일치 내용입니다."},
                    {"label": "②", "text": "나무 기둥 위에 높이 띄워 지은 집이다.", "is_correct": False, "formula": "D4", "explanation": "고상 가옥에 대한 설명입니다."},
                    {"label": "③", "text": "흙으로 벽돌을 구워 빨갛게 칠한 집이다.", "is_correct": False, "formula": "D2", "explanation": "얼음으로 지은 집입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 세계 전통 집의 모양과 재료가 서로 다른 근본적인 까닭은?",
                "options": [
                    {"label": "①", "text": "각 지역의 기후와 자연환경을 이겨내기 위해", "is_correct": True},
                    {"label": "②", "text": "집을 짓는 도구가 모두 똑같기 때문에", "is_correct": False},
                    {"label": "③", "text": "모든 나라의 날씨가 사계절 따뜻하기 때문에", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "집의 재료와 모양은 기후를 이겨내기 위한 지혜임을 알 수 있습니다.", "is_correct": True},
                    {"label": "②", "text": "세계 여러 나라 사람들은 자신이 사는 곳의 날씨에 맞추어", "is_correct": False},
                    {"label": "③", "text": "기후별 전통 집 특징 표를 보면,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "두 자료 합쳐 세계 전통 집 소개하기",
            "guide": "글 ㉮와 표 ㉯를 보고 이글루와 고상 가옥의 차이점을 한 문장으로 써 보세요.",
            "template": "북극 사람들은 추위를 막으려 [이글루]를 지었고, 열대 사람들은 습기를 피하려 [고상 가옥]을 지었습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글과 표가 함께 나올 때는 표의 항목(지역, 재료, 목적)을 글과 1:1로 맞춰 읽어요."},
            "step1_2_drill": {"task": "기후 표와 집 사진 카드 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "이글루는 얼음 블록으로 지어 추위를 막는 북극의 집입니다.", "answer": "O", "reason": "두 자료의 공통 설명입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 얼음으로 지은 집이 따뜻할까?",
            "situation": "세계 지도나 지구본을 보며 다른 나라 이야기를 할 때",
            "parent_question": "이글루는 얼음으로 만들었는데 왜 안에서 얼어 죽지 않고 따뜻할까?",
            "expected_answer": "얼음 벽이 밖의 매서운 눈보라를 막아 주고 안에서 촛불을 켜면 열이 밖으로 안 빠져나간대요!",
            "coaching_tip": "환경에 적응한 인류의 지혜를 신기하게 느끼도록 대화해 주세요."
        }
    ),

    # 12. W1
    build_expository_slot(
        grade_num=2,
        subskill_code="W1",
        subject="수학(길이 재기 2-1)",
        unit="4. 길이 재기",
        concept="1학년 동생에게 ‘센티미터(cm) 자로 길이 재는 법’ 알려주기 계획",
        text_structure="문제·해결·순서 기초",
        structure_type_code="problem_solution",
        passage_title="1학년 동생에게 자로 길이 재는 법 알려주기 계획",
        paragraphs=[
            "1학년 동생들은 자로 물건의 길이를 잴 때 자의 맨 끝 모서리를 물건 끝에 맞추는 실수를 자주 합니다. 동생들에게 '센티미터(cm) 자로 길이를 바르게 재는 법'을 친절하게 알려 주는 글을 쓰려고 합니다.",
            "글을 쓰기 전에 [예상 독자: 1학년 동생]을 생각하고, [글의 목적: 자의 눈금 0에 맞추는 규칙 알려 주기], [제목: 0에 맞추면 길이가 쏙쏙!]을 차례대로 정하는 글쓰기 계획을 세워야 합니다. 독자의 눈높이에 맞추어 계획을 세우면 동생들이 이해하기 쉬운 훌륭한 설명글이 됩니다."
        ],
        vocab_notes=[
            {"word": "눈금 0", "definition": "길이를 잴 때 기준이 되는 자의 시작 눈금"},
            {"word": "예상 독자", "definition": "내가 쓴 글을 읽을 것으로 생각하는 대상"}
        ],
        visual_html="""<div class="p-3 bg-cyan-50 rounded border border-cyan-200">
          <h4 class="font-bold text-cyan-900 mb-2">📏 길이 재기 안내글 쓰기 계획 카드</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-cyan-200">👤 <strong>읽을 사람:</strong> 1학년 동생들 (자의 눈금 0을 헷갈려함)</div>
            <div class="p-1 bg-white rounded border border-cyan-200">🎯 <strong>글의 목적:</strong> 자의 시작 눈금 '0'에 물건 끝 맞추기 설명</div>
            <div class="p-1 bg-white rounded border border-cyan-200">📌 <strong>글의 제목:</strong> 눈금 0에 맞추면 길이가 쏙쏙!</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-w1-c1", "text": "자의 맨 끝 모서리를 물건 끝에 맞추는 실수를 자주 합니다", "role": "독자의 오개념 문제", "para_idx": 0},
            {"cue_id": "g2-w1-c2", "text": "[글의 목적: 자의 눈금 0에 맞추는 규칙 알려 주기]", "role": "글쓰기 목적 설정", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "글쓰기 계획서",
            "reader": "1학년 동생들",
            "problem": "자의 모서리에 맞추는 실수",
            "solution": "눈금 0에 맞추어 끝 눈금 읽기",
            "title": "눈금 0에 맞추면 길이가 쏙쏙!"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "독자 오개념 분석",
                "stem": "1학년 동생들이 길이를 잴 때 가장 자주 하는 실수는 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "1학년 동생들은 자로 물건의 길이를 잴 때 자의 맨 끝 모서리를 물건 끝에 맞추는 실수를 자주 합니다.",
                "options": [
                    {"label": "①", "text": "자의 눈금 0 대신 자의 맨 끝 모서리에 물건을 맞춘다.", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 1학년 독자의 대표적 실수입니다."},
                    {"label": "②", "text": "자를 반으로 부러뜨려 길이를 잰다.", "is_correct": False, "formula": "D1", "explanation": "본문에 없는 과장된 오답입니다."},
                    {"label": "③", "text": "물건의 길이를 눈을 감고 맞춘다.", "is_correct": False, "formula": "D2", "explanation": "글과 무관한 행동입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "글쓰기 목적 확인",
                "stem": "이 설명글을 쓰려는 가장 중요한 목적은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "[글의 목적: 자의 눈금 0에 맞추는 규칙 알려 주기]",
                "options": [
                    {"label": "①", "text": "자의 시작 눈금 '0'에 맞추어 길이를 바르게 재는 법을 알려 주기 위해", "is_correct": True, "formula": "정답", "explanation": "2문단에 계획된 글의 핵심 목적입니다."},
                    {"label": "②", "text": "동생들에게 비싼 자를 팔기 위해", "is_correct": False, "formula": "D3", "explanation": "상업적 목적이 아닙니다."},
                    {"label": "③", "text": "수학 시험지를 숨기기 위해", "is_correct": False, "formula": "D5", "explanation": "엉뚱한 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 동생들에게 설명할 때 가장 먼저 강조해야 할 자의 눈금은?",
                "options": [
                    {"label": "①", "text": "시작 눈금 '0'", "is_correct": True},
                    {"label": "②", "text": "가장 큰 마지막 눈금 '30'", "is_correct": False},
                    {"label": "③", "text": "자 뒷면의 제조사 상표", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "자의 눈금 0에 맞추는 규칙 알려 주기", "is_correct": True},
                    {"label": "②", "text": "1학년 동생들에게 '센티미터(cm) 자로 길이를 바르게 재는 법'을", "is_correct": False},
                    {"label": "③", "text": "독자의 눈높이에 맞추어 계획을 세우면", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "길이 재기 안내문 계획서 쓰기",
            "guide": "동생들에게 자 사용법을 알려 주는 글의 계획표를 완성해 보세요.",
            "template": "읽을 사람: [1학년 동생] / 알려 줄 핵심 규칙: 물건의 한쪽 끝을 자의 눈금 [ 0 ]에 맞추기"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "설명글 계획 단계에서는 '독자의 오개념'을 파악하고 해결책을 정해요."},
            "step1_2_drill": {"task": "물건 끝을 '눈금 0'에 바르게 맞춘 자 그림 고르기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "길이를 잴 때는 물건 끝을 자의 눈금 0에 맞추어야 합니다.", "answer": "O", "reason": "올바른 측정 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 자로 재어 보기",
            "situation": "필통에 있는 자로 연필이나 지우개 길이를 잴 때",
            "parent_question": "연필 길이를 잴 때 자의 맨 끝 플라스틱에 대야 할까, 눈금 0에 대야 할까?",
            "expected_answer": "플라스틱 끝이 아니라 숫자 0이 쓰인 눈금선에 똑바로 맞춰야 정확해요!",
            "coaching_tip": "실제 자를 대어 보며 0 눈금의 시작점을 직접 확인하도록 지도해 주세요."
        }
    ),

    # 13. W2
    build_expository_slot(
        grade_num=2,
        subskill_code="W2",
        subject="통합(물건·상상 2-2)",
        unit="3. 자연을 본뜬 발명",
        concept="도꼬마리 열매를 본떠 만든 찍찍이(벨크로) 자료 모으기",
        text_structure="비교·인과 기초",
        structure_type_code="causal",
        passage_title="옷에 착 붙는 도꼬마리와 찍찍이 테이프",
        paragraphs=[
            "풀밭을 걸을 때 바지에 달라붙어 잘 떨어지지 않는 가시 열매를 본 적이 있을 것입니다. 이 열매의 이름은 '도꼬마리'입니다. 도꼬마리 열매 끝에는 낚싯바늘처럼 갈고리 모양으로 휜 작은 가시가 빽빽하게 달려 있습니다.",
            "한 발명가는 옷에 붙은 도꼬마리를 돋보기로 자세히 관찰한 뒤, 자연의 갈고리 모양을 본떠 편리한 '찍찍이(벨크로) 테이프'를 발명했습니다. 도꼬마리를 소개하는 글을 쓸 때는 [갈고리 가시 사진]과 [신발 찍찍이 끈] 자료를 모아 두 대상을 비교하여 설명할 내용을 생성해야 합니다."
        ],
        vocab_notes=[
            {"word": "도꼬마리", "definition": "열매에 갈고리 모양 가시가 있어 동물 털이나 옷에 잘 붙는 풀"},
            {"word": "갈고리", "definition": "끝이 뾰족하고 꼬부라져 물건을 걸어 낚아채는 도구"}
        ],
        visual_html="""<div class="p-3 bg-lime-50 rounded border border-lime-200">
          <h4 class="font-bold text-lime-900 mb-2">🌿 자연을 본뜬 발명 (도꼬마리 ➔ 찍찍이)</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-white rounded border border-lime-200 text-center"><strong>🌿 도꼬마리 열매</strong><br>끝이 휜 갈고리 가시<br>동물 털·옷에 붙음</div>
            <div class="p-2 bg-white rounded border border-lime-200 text-center"><strong>👟 찍찍이(벨크로)</strong><br>플라스틱 미세 갈고리<br>신발 끈·가방에 사용</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-w2-c1", "text": "도꼬마리 열매 끝에는 낚싯바늘처럼 갈고리 모양으로 휜 작은 가시가", "role": "도꼬마리의 자연적 특징", "para_idx": 0},
            {"cue_id": "g2-w2-c2", "text": "자연의 갈고리 모양을 본떠 편리한 '찍찍이(벨크로) 테이프'를 발명했습니다", "role": "자연 모방 발명 인과", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "자연 모방 비교 도식",
            "nature": "도꼬마리 열매 (갈고리 가시)",
            "invention": "찍찍이 테이프 (벨크로 갈고리+고리)",
            "connection": "갈고리 구조가 섬유를 잡아채는 원리 모방"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "자연 모방 원리 확인",
                "stem": "찍찍이(벨크로) 테이프를 발명할 때 본뜬 도꼬마리 열매의 특징은?",
                "target_para_idx": 0,
                "spotlight_quote": "도꼬마리 열매 끝에는 낚싯바늘처럼 갈고리 모양으로 휜 작은 가시가 빽빽하게 달려 있습니다.",
                "options": [
                    {"label": "①", "text": "낚싯바늘처럼 끝이 휜 갈고리 모양 가시", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 도꼬마리의 핵심 구조 특징입니다."},
                    {"label": "②", "text": "향긋한 꽃 냄새와 달콤한 꿀", "is_correct": False, "formula": "D3", "explanation": "글에 없는 향기 설명입니다."},
                    {"label": "③", "text": "물에 뜨는 넓적한 나뭇잎", "is_correct": False, "formula": "D1", "explanation": "가시 열매에 대한 설명입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "자료 수집 적절성",
                "stem": "이 주제로 설명글을 쓰기 위해 수집할 자료로 가장 알맞은 쌍은?",
                "target_para_idx": 1,
                "spotlight_quote": "[갈고리 가시 사진]과 [신발 찍찍이 끈] 자료를 모아 두 대상을 비교하여 설명할 내용을 생성해야 합니다.",
                "options": [
                    {"label": "①", "text": "도꼬마리 갈고리 가시 사진과 운동화의 찍찍이 끈 사진", "is_correct": True, "formula": "정답", "explanation": "2문단에 제시된 두 대상의 비교 자료입니다."},
                    {"label": "②", "text": "자전거 바퀴와 자동차 타이어 사진", "is_correct": False, "formula": "D4", "explanation": "주제와 무관한 교통 자료입니다."},
                    {"label": "③", "text": "맛있는 과일 사탕과 초콜릿 포장지", "is_correct": False, "formula": "D2", "explanation": "도꼬마리 발명과 아무 관련이 없습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 도꼬마리 열매가 옷에 잘 붙는 까닭은?",
                "options": [
                    {"label": "①", "text": "끝이 갈고리처럼 휘어 있어 옷의 올을 낚아채기 때문에", "is_correct": True},
                    {"label": "②", "text": "열매에 끈적끈적한 엿기름이 묻어 있어서", "is_correct": False},
                    {"label": "③", "text": "열매 속에 자석이 들어 있어서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "도꼬마리 열매 끝에는 낚싯바늘처럼 갈고리 모양으로 휜 작은 가시가 빽빽하게 달려 있습니다.", "is_correct": True},
                    {"label": "②", "text": "풀밭을 걸을 때 바지에 달라붙어 잘 떨어지지 않는 가시 열매를", "is_correct": False},
                    {"label": "③", "text": "자연의 갈고리 모양을 본떠 편리한 '찍찍이(벨크로) 테이프'를", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "자연 본뜬 발명 메모 쓰기",
            "guide": "도꼬마리와 찍찍이의 공통된 모양을 한 문장으로 정리해 보세요.",
            "template": "도꼬마리의 [갈고리] 모양 가시를 본떠서 옷이나 신발에 착 붙는 [찍찍이 테이프]를 만들었습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "자연을 본뜬 발명 글은 '자연의 원래 모습'과 '발명품'을 짝지어 메모해요."},
            "step1_2_drill": {"task": "도꼬마리 가시 사진과 벨크로 테이프 단면도 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "찍찍이 테이프는 도꼬마리의 갈고리 모양 가시를 본떠 만든 것입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 신발의 찍찍이 끈",
            "situation": "아이가 찍찍이 운동화를 신을 때 소리를 들으며",
            "parent_question": "운동화 끈 대신 붙이는 이 찍찍이는 어떤 식물을 보고 만들었을까?",
            "expected_answer": "풀밭에 가면 옷에 달라붙는 도꼬마리 열매의 갈고리를 보고 발명했대요!",
            "coaching_tip": "생활 속 발명품들이 자연을 관찰하여 만들어졌음을 흥미롭게 알려 주세요."
        }
    ),

    # 14. W3
    build_expository_slot(
        grade_num=2,
        subskill_code="W3",
        subject="통합(나·하루 2-1)",
        unit="2. 우리 몸의 소화 여행",
        concept="우리가 먹은 음식이 소화되는 길 순서 짜기",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="음식물이 지나가는 몸속 소화 여행",
        paragraphs=[
            "우리가 꼭꼭 씹어 삼킨 음식물은 몸속 긴 소화 기관을 지나며 소화됩니다. 음식물이 지나는 길을 소개할 때는 입에서부터 항문까지 차례대로 순서를 조직해야 합니다.",
            "먼저 음식물은 '입'에서 이로 잘게 부서지고 침과 섞입니다. 다음으로 긴 미끄럼틀 같은 '식도'를 타고 내려가 주머니 모양의 '위'에 도착하여 죽처럼 부드럽게 녹습니다. 그 후 구불구불 긴 '작은창자'에서 대부분의 영양분을 흡수하고, '큰창자'에서 물기를 흡수한 뒤 찌꺼기가 몸 밖으로 나옵니다."
        ],
        vocab_notes=[
            {"word": "소화 기관", "definition": "음식물을 섭취하여 잘게 부수고 영양분을 흡수하는 몸의 장기"},
            {"word": "식도", "definition": "입에서 위까지 음식물이 내려가는 긴 통로"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">🍽️ 음식물 소화 5단계 여행길 순서도</h4>
          <div class="flex items-center justify-between text-xs text-center">
            <div class="p-1 bg-white rounded border border-amber-200">1. 입</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-amber-200">2. 식도</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-amber-200">3. 위</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-amber-200">4. 작은창자</div>
            <div class="text-amber-500 font-bold">➔</div>
            <div class="p-1 bg-white rounded border border-amber-200">5. 큰창자</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-w3-c1", "text": "음식물이 지나는 길을 소개할 때는 입에서부터 항문까지 차례대로 순서를 조직해야 합니다", "role": "순서 조직 원칙", "para_idx": 0},
            {"cue_id": "g2-w3-c2", "text": "구불구불 긴 '작은창자'에서 대부분의 영양분을 흡수하고", "role": "작은창자 역할", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "과정 흐름 순서도",
            "journey": ["입 (씹기)", "식도 (내려가기)", "위 (녹이기)", "작은창자 (영양분 흡수)", "큰창자 (물기 흡수)"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "과정 순서 조직",
                "stem": "음식물이 소화되는 올바른 이동 순서는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "입에서 이로 잘게 부서지고 침과 섞입니다. 다음으로 긴 미끄럼틀 같은 '식도'를 타고 내려가 주머니 모양의 '위'에 도착하여 죽처럼 부드럽게 녹습니다.",
                "options": [
                    {"label": "①", "text": "입 ➔ 식도 ➔ 위 ➔ 작은창자 ➔ 큰창자", "is_correct": True, "formula": "정답", "explanation": "2문단에 서술된 완벽한 소화 기관 이동 순서입니다."},
                    {"label": "②", "text": "큰창자 ➔ 입 ➔ 위 ➔ 식도", "is_correct": False, "formula": "D3", "explanation": "순서가 거꾸로 뒤바뀐 오답입니다."},
                    {"label": "③", "text": "위 ➔ 입 ➔ 코 ➔ 귀", "is_correct": False, "formula": "D1", "explanation": "소화 기관이 아닌 감각 기관이 섞인 오답입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 장기 역할 확인",
                "stem": "음식물의 '대부분의 영양분을 흡수하는 곳'은 어디인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "그 후 구불구불 긴 '작은창자'에서 대부분의 영양분을 흡수하고,",
                "options": [
                    {"label": "①", "text": "구불구불 긴 작은창자", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 작은창자의 핵심 역할입니다."},
                    {"label": "②", "text": "이로 음식을 씹는 입", "is_correct": False, "formula": "D4", "explanation": "입은 음식을 부수는 곳입니다."},
                    {"label": "③", "text": "물기를 짜내는 큰창자", "is_correct": False, "formula": "D2", "explanation": "큰창자는 물기를 흡수합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 주머니 모양의 '위'에서 일어나는 일은?",
                "options": [
                    {"label": "①", "text": "음식물이 죽처럼 부드럽게 녹는다.", "is_correct": True},
                    {"label": "②", "text": "음식물이 단단한 돌로 변한다.", "is_correct": False},
                    {"label": "③", "text": "음식물이 노래를 부른다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "주머니 모양의 '위'에 도착하여 죽처럼 부드럽게 녹습니다.", "is_correct": True},
                    {"label": "②", "text": "우리가 꼭꼭 씹어 삼킨 음식물은 몸속 긴 소화 기관을 지나며 소화됩니다.", "is_correct": False},
                    {"label": "③", "text": "음식물은 '입'에서 이로 잘게 부서지고 침과 섞입니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "소화 기관 순서 연결 문장 쓰기",
            "guide": "음식물이 입에서 위까지 가는 순서를 화살표로 정리해 보세요.",
            "template": "음식물 ➔ [입] ➔ [식도] ➔ [위] ➔ [작은창자] ➔ [큰창자]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "소화 과정처럼 단계가 있는 글은 이동 경로를 따라 번호를 매기며 읽어요."},
            "step1_2_drill": {"task": "소화 기관 인체 지도에 음식물 스티커 붙이기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "음식물은 식도를 지나 위로 내려갑니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 꼭꼭 씹어 먹는 까닭",
            "situation": "밥을 먹을 때 아이가 밥을 급하게 삼키려고 할 때",
            "parent_question": "입에서 음식을 꼭꼭 씹어 삼키면 왜 '위'가 덜 힘들고 소화가 잘될까?",
            "expected_answer": "입에서 이로 잘게 부수어 주어야 식도를 타고 내려가 위에서 편하게 녹일 수 있대요!",
            "coaching_tip": "식사 예절과 건강 습관을 과학적 소화 과정과 연결해 지도해 주세요."
        }
    ),

    # 15. W4
    build_expository_slot(
        grade_num=2,
        subskill_code="W4",
        subject="통합(자연 2-2)",
        unit="3. 가을의 식물 여행",
        concept="민들레 씨앗이 바람을 타고 여행하는 과정 쓰기",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="하얀 낙하산을 타고 날아가는 민들레 씨앗",
        paragraphs=[
            "노란 민들레꽃이 지고 나면 그 자리에 하얗고 둥근 솜뭉치 같은 갓털이 돋아납니다. 민들레 씨앗은 날개가 없지만 바람을 타고 먼 곳까지 여행할 수 있습니다.",
            "바람이 살랑 불어오면 씨앗마다 달린 하얀 갓털이 낙하산처럼 활짝 펴지며 공중에 떠오릅니다. 바람을 타고 둥실둥실 멀리 날아가다가 바람이 잦아들면 부드러운 땅 위에 살포시 내려앉습니다. 그리고 다음 해 봄에 싹을 틔웁니다. 글을 쓸 때는 '살랑, 둥실둥실, 살포시'처럼 실감 나는 흉내말을 넣으면 훨씬 생생한 설명글이 됩니다."
        ],
        vocab_notes=[
            {"word": "갓털", "definition": "민들레 씨앗 꼭대기에 낙하산처럼 달린 하얀 솜털"},
            {"word": "흉내말", "definition": "사물의 모양이나 움직임, 소리를 흉내 내어 실감 나게 표현하는 말"}
        ],
        visual_html="""<div class="p-3 bg-yellow-50 rounded border border-yellow-200">
          <h4 class="font-bold text-yellow-900 mb-2">🌼 민들레 씨앗의 3단계 비행 과정</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1 bg-white rounded border border-yellow-200">① <strong>바람 불기:</strong> 하얀 갓털이 낙하산처럼 펴짐</div>
            <div class="p-1 bg-white rounded border border-yellow-200">② <strong>공중 비행:</strong> 바람을 타고 둥실둥실 먼 곳으로 이동</div>
            <div class="p-1 bg-white rounded border border-yellow-200">③ <strong>착륙과 발아:</strong> 부드러운 흙에 내려앉아 봄에 싹틈</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-w4-c1", "text": "씨앗마다 달린 하얀 갓털이 낙하산처럼 활짝 펴지며", "role": "갓털의 비행 원리", "para_idx": 1},
            {"cue_id": "g2-w4-c2", "text": "'살랑, 둥실둥실, 살포시'처럼 실감 나는 흉내말을 넣으면", "role": "생생한 묘사 표현", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "과정 순서도",
            "steps": ["노란 꽃 지고 갓털 돋음", "바람 불어 낙하산처럼 펴짐", "공중에서 둥실 비행", "새 땅에 안착하여 싹틈"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "생태 원리 세부 확인",
                "stem": "민들레 씨앗이 바람을 타고 멀리 날아갈 수 있는 까닭은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "씨앗마다 달린 하얀 갓털이 낙하산처럼 활짝 펴지며 공중에 떠오릅니다.",
                "options": [
                    {"label": "①", "text": "씨앗 꼭대기에 낙하산 같은 하얀 갓털이 달려 있어서", "is_correct": True, "formula": "정답", "explanation": "2문단에 명시된 민들레 씨앗의 비행 비밀입니다."},
                    {"label": "②", "text": "씨앗에 무거운 쇠구슬이 달려 있어서", "is_correct": False, "formula": "D1", "explanation": "무거우면 날아갈 수 없습니다."},
                    {"label": "③", "text": "새들이 부리로 물어다 주어야만 해서", "is_correct": False, "formula": "D3", "explanation": "바람을 타고 날아간다고 했습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "표현 효과 확인",
                "stem": "글에서 '살랑, 둥실둥실, 살포시' 같은 흉내말을 넣어 쓰면 어떤 효과가 있나요?",
                "target_para_idx": 1,
                "spotlight_quote": "글을 쓸 때는 '살랑, 둥실둥실, 살포시'처럼 실감 나는 흉내말을 넣으면 훨씬 생생한 설명글이 됩니다.",
                "options": [
                    {"label": "①", "text": "씨앗이 날아가는 모습이 눈에 보이듯 생생하게 느껴진다.", "is_correct": True, "formula": "정답", "explanation": "2문단 마지막 문장에 서술된 흉내말의 효과입니다."},
                    {"label": "②", "text": "글을 읽는 사람이 깜짝 놀라 도망간다.", "is_correct": False, "formula": "D5", "explanation": "부정적 과장 오답입니다."},
                    {"label": "③", "text": "글의 글자 수가 너무 적어져 탈락한다.", "is_correct": False, "formula": "D4", "explanation": "글자 수 탈락과 무관합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 민들레 씨앗이 바람을 타고 떠나는 최종 목적은?",
                "options": [
                    {"label": "①", "text": "새로운 땅에 닿아 싹을 틔우기 위해", "is_correct": True},
                    {"label": "②", "text": "우주로 날아가 별이 되기 위해", "is_correct": False},
                    {"label": "③", "text": "바다에 빠져 물고기 밥이 되기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "부드러운 땅 위에 살포시 내려앉습니다. 그리고 다음 해 봄에 싹을 틔웁니다.", "is_correct": True},
                    {"label": "②", "text": "노란 민들레꽃이 지고 나면 그 자리에", "is_correct": False},
                    {"label": "③", "text": "바람을 타고 둥실둥실 멀리 날아가다가", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "흉내말 살려 민들레 씨앗 글쓰기",
            "guide": "흉내말('둥실둥실', '살포시')을 넣어 민들레 씨앗의 비행을 한 문장으로 써 보세요.",
            "template": "민들레 씨앗은 바람을 타고 [둥실둥실] 날아가 땅 위에 [살포시] 내려앉았습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "과정 설명글을 쓸 때는 모양 흉내말(의태어)을 알맞게 넣으면 생생해져요."},
            "step1_2_drill": {"task": "민들레 씨앗 비행 모습에 알맞은 흉내말 스티커 붙이기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "민들레 씨앗의 하얀 갓털은 낙하산 역할을 합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 후~ 불어 보는 민들레",
            "situation": "봄길에 핀 하얀 민들레 갓털을 입으로 후 불어 날릴 때",
            "parent_question": "민들레 씨앗에 달린 하얀 털은 어떤 역할을 할까?",
            "expected_answer": "낙하산처럼 바람을 타고 멀리 날아가서 새싹을 틔우게 도와줘요!",
            "coaching_tip": "식물이 씨앗을 퍼뜨리는 지혜로운 방식을 경이롭게 느끼도록 격려해 주세요."
        }
    ),

    # 16. W5
    build_expository_slot(
        grade_num=2,
        subskill_code="W5",
        subject="통합(우리나라 2-1)",
        unit="4. 자랑스러운 우리나라",
        concept="무궁화와 태극기 소개 글 고쳐쓰기",
        text_structure="열거·분석 기초",
        structure_type_code="description",
        passage_title="우리나라를 상징하는 꽃과 국기 고쳐쓰기",
        paragraphs=[
            "우리나라를 대표하는 상징에는 국화인 무궁화와 국기인 태극기가 있습니다. 무궁화는 날마다 새 꽃이 피어 영원히 피고 지지 않는 끈기 있는 꽃입니다. 태극기는 흰색 바탕에 가운데 태극 문양과 네 모서리의 4괘(건·곤·감·리)가 그려져 있습니다.",
            "초고를 쓴 뒤에는 문장의 순서가 뒤섞이지 않았는지, 태극기 4괘의 이름이나 색깔 설명이 정확한지 점검하고 퇴고해야 합니다. 오류를 찾아 바르게 고쳐 쓰면 우리나라 상징을 당당하고 정확하게 소개할 수 있습니다."
        ],
        vocab_notes=[
            {"word": "국화", "definition": "나라를 상징하는 꽃 (우리나라는 무궁화)"},
            {"word": "4괘", "definition": "태극기 네 모서리에 있는 검은색의 네 가지 막대 모양(건·곤·감·리)"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">🇰🇷 태극기와 무궁화 퇴고 체크포인트</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-white rounded border border-red-200 text-center"><strong>🌺 무궁화</strong><br>영원히 피고 또 피는 꽃<br>(끈기와 인내의 상징)</div>
            <div class="p-2 bg-white rounded border border-red-200 text-center"><strong>🇰🇷 태극기</strong><br>흰 바탕 + 태극 문양 + 4괘<br>(건·곤·감·리 4괘 위치 확인)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g2-w5-c1", "text": "무궁화는 날마다 새 꽃이 피어 영원히 피고 지지 않는 끈기 있는 꽃입니다", "role": "무궁화 상징 의미", "para_idx": 0},
            {"cue_id": "g2-w5-c2", "text": "흰색 바탕에 가운데 태극 문양과 네 모서리의 4괘(건·곤·감·리)가 그려져 있습니다", "role": "태극기 구성 사실", "para_idx": 0}
        ],
        graphic_organizer={
            "diagram_type": "퇴고 점검표",
            "items": [
                "무궁화의 뜻(영원히 피는 꽃)이 정확한가?",
                "태극기 4괘의 이름(건곤감리)이 틀리지 않았는가?",
                "문장 순서와 맞춤법이 올바른가?"
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "상징 사실 오류 퇴고",
                "stem": "태극기를 설명한 초고 중 잘못된 사실이 있어 고쳐야 할 부분은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "태극기는 흰색 바탕에 가운데 태극 문양과 네 모서리의 4괘(건·곤·감·리)가 그려져 있습니다.",
                "options": [
                    {"label": "①", "text": "태극기의 바탕이 노란색과 분홍색 줄무늬라고 쓴 부분", "is_correct": True, "formula": "정답", "explanation": "태극기 바탕은 흰색이므로 잘못된 설명입니다."},
                    {"label": "②", "text": "가운데에 둥근 태극 문양이 있다고 쓴 부분", "is_correct": False, "formula": "D1", "explanation": "올바른 설명입니다."},
                    {"label": "③", "text": "네 모서리에 4괘가 검은색으로 그려졌다고 쓴 부분", "is_correct": False, "formula": "D2", "explanation": "올바른 설명입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 내용 확인",
                "stem": "우리나라 꽃 '무궁화'의 이름에 담긴 뜻은?",
                "target_para_idx": 0,
                "spotlight_quote": "무궁화는 날마다 새 꽃이 피어 영원히 피고 지지 않는 끈기 있는 꽃입니다.",
                "options": [
                    {"label": "①", "text": "영원히 피고 또 피어 지지 않는 꽃", "is_correct": True, "formula": "정답", "explanation": "1문단에 명시된 무궁화의 의미입니다."},
                    {"label": "②", "text": "겨울에만 잠깐 피었다 사라지는 눈꽃", "is_correct": False, "formula": "D3", "explanation": "무궁화의 뜻과 반대됩니다."},
                    {"label": "③", "text": "물속에서 헤엄치며 사는 물풀꽃", "is_correct": False, "formula": "D4", "explanation": "엉뚱한 오답입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 글을 쓴 뒤 퇴고할 때 확인해야 할 핵심 기준은?",
                "options": [
                    {"label": "①", "text": "문장 순서와 설명 사실이 정확한지 꼼꼼히 점검하기", "is_correct": True},
                    {"label": "②", "text": "글씨를 쓰지 않고 백지로 제출하기", "is_correct": False},
                    {"label": "③", "text": "글의 제목을 없애 버리기", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "태극기 4괘의 이름이나 색깔 설명이 정확한지 점검하고 퇴고해야 합니다.", "is_correct": True},
                    {"label": "②", "text": "우리나라를 대표하는 상징에는 국화인 무궁화와", "is_correct": False},
                    {"label": "③", "text": "오류를 찾아 바르게 고쳐 쓰면", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "태극기 소개문 퇴고 실습",
            "guide": "틀린 내용을 바르게 고쳐 한 문장으로 써 보세요.",
            "template": "초고: 태극기는 빨간 바탕에 4괘가 있다. ➔ 바른 글: 태극기는 [흰색] 바탕에 가운데 [태극 문양]과 4괘가 있습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "국기나 상징 설명글은 색깔, 모양, 이름의 정확성을 다시 확인해요."},
            "step1_2_drill": {"task": "태극기 4괘(건곤감리) 바른 명칭 찾아 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "무궁화는 영원히 피고 지지 않는 끈기를 상징합니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 태극기 바로 알기",
            "situation": "국경일에 베란다에 태극기를 달 때",
            "parent_question": "태극기의 네 모서리에 있는 검은 막대기 4괘의 이름은 무엇일까?",
            "expected_answer": "건·곤·감·리라고 부르고 하늘, 땅, 물, 불을 뜻한대요!",
            "coaching_tip": "국기를 바르게 게양하며 나라 사랑하는 마음을 키워 주세요."
        }
    )
]

print(f"Built G2 Expository Slots: {len(g2_expository_slots)}")

out_path = os.path.join(ITEM_BANK_DIR, "g2_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 2,
        "expository_slots": g2_expository_slots,
        "common_slots": g2_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g2_expository_slots)} Expository + {len(g2_common_slots)} Common)")
