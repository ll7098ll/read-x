# -*- coding: utf-8 -*-
"""
Generator for Grade 1 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
Output: courseware/data/item_bank/g1_item_bank.json
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from item_bank_schema_helper import build_expository_slot, build_common_slot
import gen_item_bank_g1_g2

ITEM_BANK_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data", "item_bank")
os.makedirs(ITEM_BANK_DIR, exist_ok=True)

# 1. Existing 8 slots from gen_item_bank_g1_g2
g1_exp_slots = list(gen_item_bank_g1_g2.G1_EXPOSITORY_SLOTS)
g1_common_slots = list(gen_item_bank_g1_g2.G1_COMMON_SLOTS)

print(f"Loaded existing G1 expository slots: {len(g1_exp_slots)}")
print(f"Loaded existing G1 common slots: {len(g1_common_slots)}")

# 2. Add remaining 8 Expository slots for Grade 1: V3-1 ~ W5
g1_remaining_exp = [
    # Slot 9: V3-1
    build_expository_slot(
        grade_num=1,
        subskill_code="V3-1",
        subject="통합(봄/가을 1-1)",
        unit="1. 건강한 우리 몸",
        concept="우리 몸의 다섯 가지 감각 기관",
        text_structure="분석 기초 (전체-부분)",
        structure_type_code="analysis",
        passage_title="우리 몸의 다섯 가지 감각 기관",
        paragraphs=[
            "우리 몸에는 주변을 느끼는 다섯 가지 감각 기관이 있습니다. 눈은 예쁜 꽃과 글자를 보고, 귀는 아름다운 음악 소리를 듣습니다. 또 코는 향긋한 냄새를 맡고, 혀는 달콤한 맛을 느낍니다. 마지막으로 피부는 따뜻하고 차가운 느낌을 압니다.",
            "이처럼 감각 기관들이 각자 맡은 일을 잘하기 때문에 우리는 세상을 안전하고 즐겁게 경험할 수 있습니다. 감각 기관은 우리 몸을 지켜 주는 소중한 친구입니다."
        ],
        vocab_notes=[
            {"word": "감각 기관", "definition": "눈, 코, 귀, 혀, 피부처럼 보고 듣고 맛보는 몸의 부분"},
            {"word": "향긋하다", "definition": "냄새가 코에 기분 좋게 느껴지다"}
        ],
        visual_html="""<div class="p-3 bg-purple-50 rounded border border-purple-200">
          <h4 class="font-bold text-purple-900 mb-2">👂 우리 몸의 5가지 감각 기관과 역할</h4>
          <div class="grid grid-cols-5 gap-1 text-center text-xs">
            <div class="p-1.5 bg-white rounded shadow-sm border border-purple-100"><strong>👀 눈</strong><br>모양·색 보기</div>
            <div class="p-1.5 bg-white rounded shadow-sm border border-purple-100"><strong>👃 코</strong><br>냄새 맡기</div>
            <div class="p-1.5 bg-white rounded shadow-sm border border-purple-100"><strong>👂 귀</strong><br>소리 듣기</div>
            <div class="p-1.5 bg-white rounded shadow-sm border border-purple-100"><strong>👅 혀</strong><br>맛보기</div>
            <div class="p-1.5 bg-white rounded shadow-sm border border-purple-100"><strong>✋ 피부</strong><br>촉감 느끼기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-v31-c1", "text": "코는 향긋한 냄새를 맡고", "role": "코의 감각 역할", "para_idx": 0},
            {"cue_id": "g1-v31-c2", "text": "감각 기관은 우리 몸을 지켜 주는 소중한 친구입니다", "role": "중심 결론", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "전체-부분 분석도",
            "central_concept": "우리 몸의 5대 감각 기관",
            "branches": ["눈 (보기)", "코 (냄새)", "귀 (소리)", "혀 (맛)", "피부 (촉감)"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "세부 정보 확인",
                "stem": "글의 내용으로 보아, '코'가 하는 일과 가장 잘 어울리는 것은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "코는 향긋한 냄새를 맡고, 혀는 달콤한 맛을 느낍니다.",
                "options": [
                    {"label": "①", "text": "음악 소리를 맑고 또렷하게 듣는다.", "is_correct": False, "formula": "D3", "explanation": "소리를 듣는 것은 코가 아니라 '귀'의 역할입니다."},
                    {"label": "②", "text": "향긋한 꽃 냄새를 맡는다.", "is_correct": True, "formula": "정답", "explanation": "1문단에서 코는 향긋한 냄새를 맡는다고 정확히 설명했습니다."},
                    {"label": "③", "text": "달콤한 사탕의 맛을 본다.", "is_correct": False, "formula": "D4", "explanation": "맛을 보는 것은 코가 아니라 '혀'의 역할입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "시각자료 적절성 평가",
                "stem": "글의 1문단에 넣을 그림으로 어울리지 않는 엉뚱한 그림은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "마지막으로 피부는 따뜻하고 차가운 느낌을 압니다.",
                "options": [
                    {"label": "①", "text": "귀로 새소리를 즐겁게 듣고 있는 어린이 그림", "is_correct": False, "formula": "D1", "explanation": "귀로 소리를 듣는 내용은 1문단에 나오는 알맞은 그림입니다."},
                    {"label": "②", "text": "발로 축구공을 힘껏 차서 골대에 넣는 그림", "is_correct": True, "formula": "정답", "explanation": "글에는 5가지 감각 기관(눈·코·귀·혀·피부)에 대한 설명이 나오므로, 공을 차는 동작은 감각 설명 그림으로 어울리지 않습니다."},
                    {"label": "③", "text": "손으로 따뜻한 털장갑을 만져 보는 어린이 그림", "is_correct": False, "formula": "D2", "explanation": "피부로 따뜻함을 느끼는 내용은 1문단 설명과 잘 어울립니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 감각 기관이 소중한 까닭으로 알맞은 것은?",
                "options": [
                    {"label": "①", "text": "세상을 안전하고 즐겁게 경험하게 해 주기 때문에", "is_correct": True},
                    {"label": "②", "text": "키를 쑥쑥 크게 만들어 주기 때문에", "is_correct": False},
                    {"label": "③", "text": "잠을 오랫동안 자게 도와주기 때문에", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 문장을 본문에서 고르면?",
                "options": [
                    {"label": "①", "text": "우리 몸에는 주변을 느끼는 다섯 가지 감각 기관이 있습니다.", "is_correct": False},
                    {"label": "②", "text": "우리는 세상을 안전하고 즐겁게 경험할 수 있습니다.", "is_correct": True},
                    {"label": "③", "text": "마지막으로 피부는 따뜻하고 차가운 느낌을 압니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "내 감각 기관 짝꿍 카드 쓰기",
            "guide": "내가 좋아하는 감각 기관 1가지를 고르고, 그 기관이 하는 일을 한 문장으로 써 보세요.",
            "template": "나는 [눈/코/귀/혀/피부]가 좋습니다. 왜냐하면 [무엇을] 하기 때문입니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글에 나온 감각 기관의 이름과 하는 일을 1:1로 짝지어 확인해요."},
            "step1_2_drill": {"task": "눈-보기, 코-냄새, 귀-듣기, 혀-맛보기, 피부-만지기 연결선 긋기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "코는 향긋한 냄새를 맡는 감각 기관입니다.", "answer": "O", "reason": "1문단 내용과 일치합니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 우리 몸의 감각 알아보기",
            "situation": "식사 시간에 반찬을 먹으며 이야기 나눌 때",
            "parent_question": "된장찌개 냄새를 맡고 뜨거운 그릇을 느낄 때 어떤 감각 기관을 썼을까?",
            "expected_answer": "냄새는 코로 맡고, 뜨거운 것은 손 피부로 느꼈어요!",
            "coaching_tip": "일상 속 경험을 감각 기관과 연결해 표현하도록 칭찬해 주세요."
        }
    ),

    # Slot 10: V3-2
    build_expository_slot(
        grade_num=1,
        subskill_code="V3-2",
        subject="통합(여름 1-1)",
        unit="2. 여름 숲의 동물",
        concept="여름 나무에서 노래하는 매미",
        text_structure="기술·열거",
        structure_type_code="description",
        passage_title="여름 나무에서 노래하는 매미",
        paragraphs=[
            "여름이 되면 나무에서 매미가 '맴맴' 소리를 내며 웁니다. 매미는 투명한 날개가 네 개 있고, 단단한 나무껍질에 꼭 붙어 살아갑니다. 매미는 나무의 즙을 빨아먹으며 여름을 보냅니다.",
            "매미가 우는 것은 짝을 찾기 위해서입니다. 수컷 매미만 배에 있는 소리 주머니를 흔들어 소리를 낼 수 있습니다. 암컷 매미는 소리를 내지 못합니다."
        ],
        vocab_notes=[
            {"word": "투명하다", "definition": "유리처럼 맑아서 뒤가 훤히 비치다"},
            {"word": "나무껍질", "definition": "나무의 줄기를 둘러싸고 있는 바깥 부분"}
        ],
        visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">🦗 매미의 실제 모습 사실 카드</h4>
          <ul class="text-xs space-y-1 text-slate-700">
            <li>✔ 날개: 투명한 날개 4개</li>
            <li>✔ 먹이: 나무의 달콤한 즙</li>
            <li>✔ 소리: 소리 주머니가 있는 수컷 매미만 노래함</li>
          </ul>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-v32-c1", "text": "매미는 투명한 날개가 네 개 있고", "role": "사실적 외형 특징", "para_idx": 0},
            {"cue_id": "g1-v32-c2", "text": "수컷 매미만 배에 있는 소리 주머니를 흔들어 소리를 낼 수 있습니다", "role": "발성 기관의 사실", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "사실 vs 상상 구분표",
            "facts": ["투명한 날개 4개", "수컷만 소리를 냄", "나무 즙을 먹음"],
            "imaginations": ["마이크 잡고 노래함", "선글라스 쓰고 춤춤"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "사실과 상상 구별",
                "stem": "글의 내용에 나오는 '진짜 사실' 문장은 어느 것인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "매미는 투명한 날개가 네 개 있고, 단단한 나무껍질에 꼭 붙어 살아갑니다.",
                "options": [
                    {"label": "①", "text": "매미는 나무 위에서 마이크를 잡고 노래합니다.", "is_correct": False, "formula": "D5", "explanation": "마이크를 잡는 것은 상상으로 꾸며낸 이야기입니다."},
                    {"label": "②", "text": "매미는 투명한 날개가 네 개 있습니다.", "is_correct": True, "formula": "정답", "explanation": "1문단에 나오는 관찰 가능한 실제 사실입니다."},
                    {"label": "③", "text": "매미는 더위를 피해 시원한 선풍기를 켭니다.", "is_correct": False, "formula": "D1", "explanation": "선풍기를 켜는 것은 상상 속 허구입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 내용 확인",
                "stem": "글을 통해 알 수 있는 매미의 특징으로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "수컷 매미만 배에 있는 소리 주머니를 흔들어 소리를 낼 수 있습니다.",
                "options": [
                    {"label": "①", "text": "암컷 매미만 큰 소리로 노래할 수 있다.", "is_correct": False, "formula": "D3", "explanation": "암컷 매미는 소리를 내지 못한다고 했습니다."},
                    {"label": "②", "text": "수컷 매미만 소리 주머니로 소리를 낼 수 있다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 수컷 매미만 배의 소리 주머니를 흔들어 소리를 낸다고 정확히 서술했습니다."},
                    {"label": "③", "text": "매미는 물속에서 헤엄치며 물고기를 잡아먹는다.", "is_correct": False, "formula": "D4", "explanation": "매미는 나무껍질에 붙어 나무 즙을 먹습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 매미가 여름에 우는 진짜 까닭은?",
                "options": [
                    {"label": "①", "text": "짝을 찾기 위해서", "is_correct": True},
                    {"label": "②", "text": "날씨가 너무 더워 화가 나서", "is_correct": False},
                    {"label": "③", "text": "나뭇잎을 청소하기 위해서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 문장은?",
                "options": [
                    {"label": "①", "text": "여름이 되면 나무에서 매미가 '맴맴' 소리를 내며 웁니다.", "is_correct": False},
                    {"label": "②", "text": "매미가 우는 것은 짝을 찾기 위해서입니다.", "is_correct": True},
                    {"label": "③", "text": "암컷 매미는 소리를 내지 못합니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "매미의 사실 관찰 카드 쓰기",
            "guide": "매미의 날개와 소리에 대해 사실 문장 2개를 써 보세요.",
            "template": "매미는 [       ] 날개가 4개 있습니다. 그리고 [       ] 매미만 소리를 냅니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "동화책 속 꾸며낸 이야기와 과학 설명글의 진짜 사실을 구별해요."},
            "step1_2_drill": {"task": "사실 문장에는 'O', 동화 속 상상 문장에는 'X' 표시하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "수컷 매미만 배에 소리 주머니가 있습니다.", "answer": "O", "reason": "본문에 명시된 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 진짜 사실과 상상 구별하기",
            "situation": "여름 숲길이나 공원을 걸을 때 매미 소리를 들으며",
            "parent_question": "매미가 노래하는 건 왜일까? 만화처럼 신나서 부르는 걸까, 진짜 다른 까닭이 있을까?",
            "expected_answer": "짝을 찾으려고 소리 주머니를 흔들어 소리를 내는 거래요!",
            "coaching_tip": "만화적 상상과 과학적 사실을 다정하게 구분해 말할 수 있도록 이끌어 주세요."
        }
    ),

    # Slot 11: V3-3
    build_expository_slot(
        grade_num=1,
        subskill_code="V3-3",
        subject="통합(봄/가을 1-1)",
        unit="3. 귀여운 동물 친구들",
        concept="깡충깡충 토끼의 귀와 꼬리 (글 ㉮·㉯)",
        text_structure="기술·비교 기초",
        structure_type_code="comparison",
        passage_title="깡충깡충 토끼의 특징 (글 ㉮와 ㉯)",
        paragraphs=[
            "[글 ㉮] 토끼는 귀가 길고 쫑긋합니다. 토끼는 긴 귀로 작은 소리도 잘 들을 수 있습니다. 토끼는 풀과 당근을 맛있게 먹습니다.",
            "[글 ㉯] 토끼는 귀가 길고 부드럽습니다. 토끼는 뒷다리가 길어서 언덕을 깡충깡충 잘 뛰어 올라갑니다. 하지만 꼬리는 둥글고 매우 짧습니다."
        ],
        vocab_notes=[
            {"word": "쫑긋하다", "definition": "귀가 위로 곧게 서 있는 모양"},
            {"word": "언덕", "definition": "땅이 비탈지게 높이 솟은 곳"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">🐰 글 ㉮와 글 ㉯의 토끼 특징 비교표</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-amber-100"><th class="p-1 border border-amber-200">구분</th><th class="p-1 border border-amber-200">글 ㉮에 나온 내용</th><th class="p-1 border border-amber-200">글 ㉯에 나온 내용</th></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">공통점</td><td colspan="2" class="p-1 border border-amber-200 bg-white">귀가 길다</td></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">차이점</td><td class="p-1 border border-amber-200 bg-white">풀과 당근을 먹음</td><td class="p-1 border border-amber-200 bg-white">긴 뒷다리, 짧은 꼬리</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-v33-c1", "text": "토끼는 귀가 길고 쫑긋합니다", "role": "글 ㉮의 공통 특징", "para_idx": 0},
            {"cue_id": "g1-v33-c2", "text": "토끼는 뒷다리가 길어서 언덕을 깡충깡충 잘 뛰어 올라갑니다", "role": "글 ㉯의 고유 특징", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "두 글 통합 벤다이어그램",
            "common": ["귀가 길다"],
            "only_a": ["작은 소리를 잘 들음", "풀과 당근을 먹음"],
            "only_b": ["긴 뒷다리로 잘 뜀", "꼬리가 둥글고 짧음"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "다중 자료 공통점 확인",
                "stem": "글 ㉮와 글 ㉯에 '모두' 나오는 토끼의 공통된 모습은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "토끼는 귀가 길고 쫑긋합니다.",
                "options": [
                    {"label": "①", "text": "귀가 길다.", "is_correct": True, "formula": "정답", "explanation": "글 ㉮의 '귀가 길고'와 글 ㉯의 '귀가 길고' 모두에 공통으로 나옵니다."},
                    {"label": "②", "text": "당근을 맛있게 먹는다.", "is_correct": False, "formula": "D4", "explanation": "당근을 먹는 내용은 글 ㉮에만 나옵니다."},
                    {"label": "③", "text": "꼬리가 둥글고 짧다.", "is_correct": False, "formula": "D3", "explanation": "꼬리가 짧은 내용은 글 ㉯에만 나옵니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "다중 자료 정보 통합",
                "stem": "글 ㉮와 글 ㉯의 내용을 합쳐 토끼를 소개할 때, 알맞지 않은 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "하지만 꼬리는 둥글고 매우 짧습니다.",
                "options": [
                    {"label": "①", "text": "토끼는 긴 귀로 작은 소리를 잘 듣는다.", "is_correct": False, "formula": "D1", "explanation": "글 ㉮를 통해 알 수 있는 알맞은 내용입니다."},
                    {"label": "②", "text": "토끼는 꼬리가 뱀처럼 아주 길쭉하다.", "is_correct": True, "formula": "정답", "explanation": "글 ㉯에서 토끼의 꼬리는 둥글고 매우 짧다고 했습니다."},
                    {"label": "③", "text": "토끼는 긴 뒷다리로 언덕을 잘 뛴다.", "is_correct": False, "formula": "D2", "explanation": "글 ㉯에 나오는 바른 내용입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 토끼가 언덕을 깡충깡충 잘 뛰어 올라갈 수 있는 까닭은?",
                "options": [
                    {"label": "①", "text": "뒷다리가 길어서", "is_correct": True},
                    {"label": "②", "text": "귀가 길어서", "is_correct": False},
                    {"label": "③", "text": "꼬리가 둥글어서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거 문장은 글 ㉯의 어디에 있나요?",
                "options": [
                    {"label": "①", "text": "토끼는 귀가 길고 부드럽습니다.", "is_correct": False},
                    {"label": "②", "text": "토끼는 뒷다리가 길어서 언덕을 깡충깡충 잘 뛰어 올라갑니다.", "is_correct": True},
                    {"label": "③", "text": "하지만 꼬리는 둥글고 매우 짧습니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "두 글 합쳐 토끼 소개문 쓰기",
            "guide": "글 ㉮와 글 ㉯에서 알게 된 토끼의 특징을 하나씩 골라 문장을 완성해 보세요.",
            "template": "토끼는 귀가 [       ]. 그리고 [       ]가 길어서 잘 뜁니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "두 글을 읽을 때는 양쪽에 다 나온 말(공통점)과 한쪽에만 나온 말을 표로 정리해요."},
            "step1_2_drill": {"task": "글 ㉮와 글 ㉯의 내용을 선으로 연결해 비교하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "두 글 모두 토끼의 귀가 길다는 점을 설명하고 있습니다.", "answer": "O", "reason": "두 글의 공통 설명입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 두 가지 이야기 합치기",
            "situation": "동물 책이나 동물원 사진을 보며 대화할 때",
            "parent_question": "토끼에 대한 두 짧은 글을 읽고 나니 토끼에 대해 새롭게 알게 된 건 뭘까?",
            "expected_answer": "귀가 긴 것뿐만 아니라 뒷다리가 길어서 언덕을 잘 뛴다는 것도 알게 되었어요!",
            "coaching_tip": "여러 곳에서 얻은 정보를 하나로 묶어 말하는 습관을 길러 주세요."
        }
    ),

    # Slot 12: W1
    build_expository_slot(
        grade_num=1,
        subskill_code="W1",
        subject="통합(학교 1-1)",
        unit="4. 즐거운 우리 학교",
        concept="내 필통 속 학용품 소개 계획하기",
        text_structure="기술·열거",
        structure_type_code="description",
        passage_title="내 필통 속 소중한 학용품들",
        paragraphs=[
            "필통 안에는 공부할 때 쓰는 여러 학용품이 들어 있습니다. 그중 연필은 검은 심이 들어 있어 글씨를 쓸 때 사용합니다. 지우개는 말랑말랑한 고무로 되어 있어 틀린 글씨를 깨끗하게 지워 줍니다.",
            "친구에게 학용품을 소개할 때는 먼저 소개할 물건의 이름을 정하고, 그 물건의 모양과 쓰임새를 차례대로 생각하여 글을 쓸 계획을 세웁니다."
        ],
        vocab_notes=[
            {"word": "학용품", "definition": "공부할 때 필요한 연필, 공책, 지우개 등의 물건"},
            {"word": "쓰임새", "definition": "어떤 물건을 쓰는 쓰임이나 쓸모"}
        ],
        visual_html="""<div class="p-3 bg-blue-50 rounded border border-blue-200">
          <h4 class="font-bold text-blue-900 mb-2">✏️ 학용품 소개 글쓰기 3단계 계획 카드</h4>
          <div class="flex items-center justify-between text-xs text-center">
            <div class="p-2 bg-white rounded border border-blue-200 font-bold">1단계<br>소개할 물건 정하기</div>
            <div class="text-blue-500 font-bold">➔</div>
            <div class="p-2 bg-white rounded border border-blue-200 font-bold">2단계<br>읽을 사람 생각하기</div>
            <div class="text-blue-500 font-bold">➔</div>
            <div class="p-2 bg-white rounded border border-blue-200 font-bold">3단계<br>모양·쓰임새 정하기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-w1-c1", "text": "연필은 검은 심이 들어 있어 글씨를 쓸 때 사용합니다", "role": "연필의 특징과 쓰임새", "para_idx": 0},
            {"cue_id": "g1-w1-c2", "text": "먼저 소개할 물건의 이름을 정하고", "role": "계획하기 첫 단계", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "글쓰기 계획 카드",
            "subject": "학용품 소개하기",
            "reader": "우리 반 친구들",
            "topics": ["물건 이름", "생김새(모양·색)", "쓰임새(용도)"]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "글쓰기 계획 순서 확인",
                "stem": "친구에게 학용품을 소개하는 글을 쓸 때 가장 먼저 해야 할 계획은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "먼저 소개할 물건의 이름을 정하고, 그 물건의 모양과 쓰임새를 차례대로 생각하여 글을 쓸 계획을 세웁니다.",
                "options": [
                    {"label": "①", "text": "소개할 학용품 1가지의 이름을 정한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 가장 먼저 소개할 물건의 이름을 정한다고 했습니다."},
                    {"label": "②", "text": "틀린 글씨를 지우개로 깨끗이 지운다.", "is_correct": False, "formula": "D3", "explanation": "글을 쓰기도 전에 지우는 것은 계획 단계가 아닙니다."},
                    {"label": "③", "text": "친구에게 연필을 빌려 달라고 말한다.", "is_correct": False, "formula": "D1", "explanation": "글쓰기 계획과 무관한 대화입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "내용 요소 적절성",
                "stem": "'지우개'를 소개할 때 넣기에 가장 알맞은 쓰임새 내용은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "지우개는 말랑말랑한 고무로 되어 있어 틀린 글씨를 깨끗하게 지워 줍니다.",
                "options": [
                    {"label": "①", "text": "공책에 반듯한 선을 긋는 데 쓴다.", "is_correct": False, "formula": "D4", "explanation": "선을 긋는 것은 '자'의 쓰임새입니다."},
                    {"label": "②", "text": "틀린 연필 글씨를 깨끗하게 지우는 데 쓴다.", "is_correct": True, "formula": "정답", "explanation": "1문단에서 지우개는 틀린 글씨를 깨끗하게 지워 준다고 했습니다."},
                    {"label": "③", "text": "종이를 모양대로 오려 내는 데 쓴다.", "is_correct": False, "formula": "D2", "explanation": "종이를 오리는 것은 '가위'의 쓰임새입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 사물을 소개하는 글을 계획할 때 반드시 들어가야 할 두 가지는?",
                "options": [
                    {"label": "①", "text": "모양과 쓰임새", "is_correct": True},
                    {"label": "②", "text": "가격과 가게 이름", "is_correct": False},
                    {"label": "③", "text": "옛날이야기와 비밀", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "필통 안에는 공부할 때 쓰는 여러 학용품이 들어 있습니다.", "is_correct": False},
                    {"label": "②", "text": "그 물건의 모양과 쓰임새를 차례대로 생각하여 글을 쓸 계획을 세웁니다.", "is_correct": True},
                    {"label": "③", "text": "지우개는 말랑말랑한 고무로 되어 있어", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "나만의 학용품 소개 계획표 채우기",
            "guide": "소개하고 싶은 학용품 1개를 정하고 계획표의 빈칸을 채워 보세요.",
            "template": "내가 소개할 물건: [       ] / 누구에게: [       ] / 설명할 쓰임새: [       ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글을 쓰기 전에는 '누구에게', '무엇을', '어떤 특징을' 쓸지 먼저 계획해요."},
            "step1_2_drill": {"task": "학용품 이름과 알맞은 쓰임새 짝 맞추기 연습"},
            "step3_vaccine": {"ox_quiz": [{"statement": "글을 쓸 때는 먼저 소개할 대상을 정하는 것이 좋습니다.", "answer": "O", "reason": "글쓰기 계획의 첫 단계입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 글쓰기 계획 세우기",
            "situation": "아이가 숙제나 일기를 쓰기 전 이야기 나눌 때",
            "parent_question": "필통에 있는 물건 중에 친구에게 하나만 자랑하고 소개한다면 무엇을 고르고 싶니?",
            "expected_answer": "내 무지개 연필이요! 색깔도 예쁘고 글씨도 부드럽게 잘 써져요.",
            "coaching_tip": "소개할 대상의 '모양'과 '쓰임새'를 구체적으로 말해 보도록 유도해 주세요."
        }
    ),

    # Slot 13: W2
    build_expository_slot(
        grade_num=1,
        subskill_code="W2",
        subject="통합(가을 1-2)",
        unit="2. 가을의 자연",
        concept="가을 나뭇잎(은행잎·단풍잎) 특징 낱말 모으기",
        text_structure="기술·비교 기초",
        structure_type_code="comparison",
        passage_title="알록달록 가을 나뭇잎 관찰하기",
        paragraphs=[
            "가을이 되면 초록색이던 나뭇잎들이 예쁜 색으로 물듭니다. 은행잎은 맑고 노란색으로 변하고, 넓게 펼쳐진 부채 모양을 하고 있습니다. 반면에 단풍잎은 붉은 빨간색으로 물들고, 아기 손바닥처럼 여러 갈래로 갈라져 있습니다.",
            "나뭇잎을 설명하는 글을 쓸 때는 눈으로 직접 본 색깔과 모양을 나타내는 알맞은 낱말들을 먼저 모아야 합니다. 사실 낱말을 모으면 설명글을 쉽게 쓸 수 있습니다."
        ],
        vocab_notes=[
            {"word": "부채 모양", "definition": "바람을 일으키는 부채처럼 넓게 둥글게 펴진 모양"},
            {"word": "갈래", "definition": "하나의 줄기에서 여러 갈래로 갈라져 나간 가닥"}
        ],
        visual_html="""<div class="p-3 bg-orange-50 rounded border border-orange-200">
          <h4 class="font-bold text-orange-900 mb-2">🍂 가을 나뭇잎 특징 낱말 마인드맵</h4>
          <div class="grid grid-cols-2 gap-2 text-xs">
            <div class="p-2 bg-yellow-50 rounded border border-yellow-200 text-center">
              <strong class="text-yellow-800">🟡 은행잎</strong><br>노란색, 부채 모양, 매끄럽다
            </div>
            <div class="p-2 bg-red-50 rounded border border-red-200 text-center">
              <strong class="text-red-800">🔴 단풍잎</strong><br>빨간색, 아기 손 모양, 여러 갈래
            </div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-w2-c1", "text": "은행잎은 맑고 노란색으로 변하고, 넓게 펼쳐진 부채 모양을 하고 있습니다", "role": "은행잎 관찰 사실", "para_idx": 0},
            {"cue_id": "g1-w2-c2", "text": "눈으로 직접 본 색깔과 모양을 나타내는 알맞은 낱말들을 먼저 모아야 합니다", "role": "내용 생성하기 지침", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "낱말 생각 그물망",
            "topic": "가을 나뭇잎",
            "word_groups": {
                "색깔 낱말": ["노란색", "빨간색", "갈색"],
                "모양 낱말": ["부채 모양", "아기 손바닥 모양", "여러 갈래"]
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "관찰 낱말 적절성",
                "stem": "글의 1문단에서 '은행잎'을 설명할 때 모은 알맞은 특징 낱말 쌍은 무엇인가요?",
                "target_para_idx": 0,
                "spotlight_quote": "은행잎은 맑고 노란색으로 변하고, 넓게 펼쳐진 부채 모양을 하고 있습니다.",
                "options": [
                    {"label": "①", "text": "빨간색, 손바닥 모양", "is_correct": False, "formula": "D3", "explanation": "빨간색과 손바닥 모양은 단풍잎의 특징입니다."},
                    {"label": "②", "text": "노란색, 부채 모양", "is_correct": True, "formula": "정답", "explanation": "1문단에서 은행잎은 노란색, 부채 모양이라고 설명했습니다."},
                    {"label": "③", "text": "파란색, 바늘 모양", "is_correct": False, "formula": "D1", "explanation": "글에 나오지 않는 잘못된 낱말입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "내용 생성 전략",
                "stem": "가을 나뭇잎을 설명하는 글을 쓰려고 할 때 가장 알맞은 낱말 모으기 방법은?",
                "target_para_idx": 1,
                "spotlight_quote": "나뭇잎을 설명하는 글을 쓸 때는 눈으로 직접 본 색깔과 모양을 나타내는 알맞은 낱말들을 먼저 모아야 합니다.",
                "options": [
                    {"label": "①", "text": "눈으로 직접 보고 색깔과 모양 낱말을 모은다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 직접 본 색깔과 모양을 나타내는 알맞은 낱말을 모은다고 했습니다."},
                    {"label": "②", "text": "마음대로 지어낸 거짓말 낱말을 모은다.", "is_correct": False, "formula": "D5", "explanation": "설명글에는 지어낸 말이 아닌 사실 낱말을 모아야 합니다."},
                    {"label": "③", "text": "나뭇잎과 상관없는 동물 이름만 모은다.", "is_correct": False, "formula": "D2", "explanation": "주제와 관련 없는 낱말을 모으면 안 됩니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 단풍잎의 모양을 나타내는 알맞은 낱말은?",
                "options": [
                    {"label": "①", "text": "아기 손바닥처럼 여러 갈래로 갈라진 모양", "is_correct": True},
                    {"label": "②", "text": "바람에 펄럭이는 네모난 종이 모양", "is_correct": False},
                    {"label": "③", "text": "둥글둥글한 공 모양", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 문장은?",
                "options": [
                    {"label": "①", "text": "은행잎은 맑고 노란색으로 변하고", "is_correct": False},
                    {"label": "②", "text": "단풍잎은 붉은 빨간색으로 물들고, 아기 손바닥처럼 여러 갈래로 갈라져 있습니다.", "is_correct": True},
                    {"label": "③", "text": "사실 낱말을 모으면 설명글을 쉽게 쓸 수 있습니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "나뭇잎 생각 그물 채우기",
            "guide": "내가 길에서 주운 나뭇잎의 색깔과 모양을 생각하며 낱말을 써 보세요.",
            "template": "내가 본 나뭇잎: [단풍잎/은행잎] / 색깔 낱말: [       ] / 모양 낱말: [       ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "설명글을 쓸 때는 대상의 진짜 색깔과 모양을 나타내는 낱말을 골라야 해요."},
            "step1_2_drill": {"task": "나뭇잎 사진을 보고 알맞은 모양 낱말 스티커 붙이기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "은행잎은 부채 모양의 노란색 나뭇잎입니다.", "answer": "O", "reason": "본문에 나온 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 사물의 특징 낱말 찾기",
            "situation": "길가에 떨어진 낙엽을 함께 주워 관찰할 때",
            "parent_question": "이 나뭇잎은 무슨 색이고 어떤 모양을 닮았을까?",
            "expected_answer": "노란색이고 바람 부는 부채를 닮았어요!",
            "coaching_tip": "아이의 어휘력을 높이려면 감각적인 모양 흉내말을 함께 나눠 보세요."
        }
    ),

    # Slot 14: W3
    build_expository_slot(
        grade_num=1,
        subskill_code="W3",
        subject="수학(시계 보기 1-2)",
        unit="5. 시계 보기와 규칙",
        concept="째깍째깍 시계 바늘 소개 순서 정하기",
        text_structure="분석·순서 기초",
        structure_type_code="sequence",
        passage_title="째깍째깍 시계 바늘의 비밀",
        paragraphs=[
            "시계는 시간을 알려 주는 편리한 물건입니다. 시계 앞면에는 1부터 12까지 숫자가 있고, 두 개의 바늘이 움직입니다. 짧은바늘은 몇 시인지 가리키고, 긴바늘은 몇 분인지 알려 줍니다.",
            "시계를 소개하는 글을 쓸 때는 먼저 전체 시계를 소개하고, 그 다음에 짧은바늘과 긴바늘의 특징을 차례대로 쓰는 순서(① 시계 이름 ➔ ② 짧은바늘 ➔ ③ 긴바늘)로 문장을 조직해야 읽는 사람이 이해하기 쉽습니다."
        ],
        vocab_notes=[
            {"word": "짧은바늘", "definition": "시계에서 시간을 나타내는 길이가 짧은 바늘"},
            {"word": "긴바늘", "definition": "시계에서 분을 나타내는 길이가 긴 바늘"}
        ],
        visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
          <h4 class="font-bold text-teal-900 mb-2">⏰ 시계 소개 문장 배열 순서 (전체 ➔ 부분)</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1.5 bg-white rounded border border-teal-200"><strong>① 첫째 문장:</strong> 시계는 시간을 알려 줍니다. (전체 소개)</div>
            <div class="p-1.5 bg-white rounded border border-teal-200"><strong>② 둘째 문장:</strong> 짧은바늘은 시간을 가리킵니다. (부분 1)</div>
            <div class="p-1.5 bg-white rounded border border-teal-200"><strong>③ 셋째 문장:</strong> 긴바늘은 몇 분인지 알려 줍니다. (부분 2)</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-w3-c1", "text": "짧은바늘은 몇 시인지 가리키고, 긴바늘은 몇 분인지 알려 줍니다", "role": "바늘의 역할 분석", "para_idx": 0},
            {"cue_id": "g1-w3-c2", "text": "순서(① 시계 이름 ➔ ② 짧은바늘 ➔ ③ 긴바늘)로 문장을 조직해야", "role": "문장 조직 순서", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "순서 흐름도",
            "steps": [
                "1단계: 전체 시계 소개 (시간을 알려 주는 물건)",
                "2단계: 짧은바늘 소개 (몇 시)",
                "3단계: 긴바늘 소개 (몇 분)"
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "설명 순서 조직하기",
                "stem": "시계를 설명하는 글을 쓸 때 가장 알맞은 문장 순서(①·②·③)는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "순서(① 시계 이름 ➔ ② 짧은바늘 ➔ ③ 긴바늘)로 문장을 조직해야 읽는 사람이 이해하기 쉽습니다.",
                "options": [
                    {"label": "①", "text": "긴바늘 역할 ➔ 짧은바늘 역할 ➔ 시계 이름", "is_correct": False, "formula": "D3", "explanation": "전체 이름을 먼저 말하지 않고 부분부터 말하면 어색합니다."},
                    {"label": "②", "text": "시계 전체 소개 ➔ 짧은바늘 ➔ 긴바늘", "is_correct": True, "formula": "정답", "explanation": "2문단에서 전체 시계 소개 ➔ 짧은바늘 ➔ 긴바늘 순서가 가장 좋다고 했습니다."},
                    {"label": "③", "text": "짧은바늘 ➔ 시계 전체 소개 ➔ 긴바늘", "is_correct": False, "formula": "D4", "explanation": "순서가 뒤섞여 있어 읽는 사람이 혼란스럽습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 사실 확인",
                "stem": "시계의 '짧은바늘'이 하는 일로 바른 것은?",
                "target_para_idx": 0,
                "spotlight_quote": "짧은바늘은 몇 시인지 가리키고, 긴바늘은 몇 분인지 알려 줍니다.",
                "options": [
                    {"label": "①", "text": "몇 분인지 자세히 알려 준다.", "is_correct": False, "formula": "D4", "explanation": "몇 분인지 알려 주는 것은 긴바늘입니다."},
                    {"label": "②", "text": "몇 시인지 가리킨다.", "is_correct": True, "formula": "정답", "explanation": "1문단에서 짧은바늘은 몇 시인지 가리킨다고 했습니다."},
                    {"label": "③", "text": "소리를 내며 노래를 부른다.", "is_correct": False, "formula": "D1", "explanation": "바늘의 역할과 무관한 설명입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 전체에서 부분으로 사물을 설명할 때 좋은 점은?",
                "options": [
                    {"label": "①", "text": "읽는 사람이 차례대로 쉽게 이해할 수 있다.", "is_correct": True},
                    {"label": "②", "text": "글을 아주 길게 쓸 수 있다.", "is_correct": False},
                    {"label": "③", "text": "글씨를 쓰지 않아도 된다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "시계는 시간을 알려 주는 편리한 물건입니다.", "is_correct": False},
                    {"label": "②", "text": "문장을 조직해야 읽는 사람이 이해하기 쉽습니다.", "is_correct": True},
                    {"label": "③", "text": "시계 앞면에는 1부터 12까지 숫자가 있고", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "시계 바늘 문장 순서 번호 달기",
            "guide": "뒤섞인 세 문장에 알맞은 순서 번호(①, ②, ③)를 매겨 보세요.",
            "template": "(   ) 짧은바늘은 몇 시인지 가리킵니다. / (   ) 시계는 시간을 알려 주는 편리한 물건입니다. / (   ) 긴바늘은 몇 분인지 알려 줍니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "설명할 때는 '전체 이름 ➔ 세부 부분 1 ➔ 세부 부분 2' 순서로 써요."},
            "step1_2_drill": {"task": "문장 카드 3장을 순서대로 나열하여 글 완성하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "전체 대상을 먼저 소개한 뒤 바늘을 설명하는 것이 좋습니다.", "answer": "O", "reason": "이해하기 쉬운 글의 순서입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 순서대로 말하기",
            "situation": "집안 벽시계를 보며 몇 시 몇 분인지 물어볼 때",
            "parent_question": "시계를 볼 때 짧은바늘과 긴바늘 중에 어느 바늘을 먼저 보고 시간을 읽을까?",
            "expected_answer": "짧은바늘을 먼저 보고 몇 시인지 읽은 다음에, 긴바늘을 봐요!",
            "coaching_tip": "사물을 관찰하고 말할 때도 순서가 있음을 자연스럽게 격려해 주세요."
        }
    ),

    # Slot 15: W4
    build_expository_slot(
        grade_num=1,
        subskill_code="W4",
        subject="통합(우리나라 1-2)",
        unit="3. 우리나라 전통 놀이",
        concept="모양과 소리가 재미있는 전통 탈·윷 소개 쓰기",
        text_structure="기술·열거",
        structure_type_code="description",
        passage_title="우리나라 전통 놀잇감 윷가락",
        paragraphs=[
            "윷놀이는 설날에 가족들이 함께 모여 즐기는 전통 놀이입니다. 윷가락은 둥근 나무를 반으로 쪼개어 만든 네 개의 막대기입니다. 윷가락의 한쪽은 평평하고 다른 한쪽은 둥급니다.",
            "윷가락을 설명하는 글을 쓸 때는 '윷가락은', '나무가'처럼 알맞은 조사('은/는, 이/가')를 바르게 쓰고, 문장이 끝나는 곳에 마침표(.)를 꼭 찍어야 바른 글이 완성됩니다."
        ],
        vocab_notes=[
            {"word": "윷가락", "definition": "윷놀이를 할 때 던지는 네 개의 나무 막대기"},
            {"word": "조사", "definition": "'은/는, 이/가'처럼 낱말 뒤에 붙어 관계를 나타내는 말"}
        ],
        visual_html="""<div class="p-3 bg-red-50 rounded border border-red-200">
          <h4 class="font-bold text-red-900 mb-2">🪵 윷가락 소개 바른 문장 쓰기 공식</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1.5 bg-white rounded border border-red-100">✔ <strong>조사 선택:</strong> 윷가락<strong>은</strong> 나무로 만듭니다. (윷가락은 O / 윷가락를 X)</div>
            <div class="p-1.5 bg-white rounded border border-red-100">✔ <strong>마침표 확인:</strong> 문장이 끝나면 마침표(<strong>.</strong>)를 꼭 찍습니다.</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-w4-c1", "text": "윷가락은 둥근 나무를 반으로 쪼개어 만든 네 개의 막대기입니다", "role": "윷가락 모양 정의", "para_idx": 0},
            {"cue_id": "g1-w4-c2", "text": "문장이 끝나는 곳에 마침표(.)를 꼭 찍어야", "role": "문장 부호 규칙", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "문장 완성 점검표",
            "checklist": [
                "주어 뒤에 알맞은 조사('은/는', '이/가')가 있는가?",
                "설명하는 내용이 바른 사실인가?",
                "문장 끝에 마침표(.)가 정확히 찍혔는가?"
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "문장 성분과 조사 호응",
                "stem": "윷가락을 소개하는 문장으로 조사가 가장 바르게 쓰인 것은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "윷가락을 설명하는 글을 쓸 때는 '윷가락은', '나무가'처럼 알맞은 조사('은/는, 이/가')를 바르게 쓰고, 문장이 끝나는 곳에 마침표(.)를 꼭 찍어야 바른 글이 완성됩니다.",
                "options": [
                    {"label": "①", "text": "윷가락를 네 개 던집니다.", "is_correct": False, "formula": "D3", "explanation": "'윷가락를'이 아니라 '윷가락을'이라고 써야 합니다."},
                    {"label": "②", "text": "윷가락은 나무로 만듭니다.", "is_correct": True, "formula": "정답", "explanation": "받침이 있는 '윷가락' 뒤에 알맞은 조사 '은'이 바르게 쓰였습니다."},
                    {"label": "③", "text": "윷가락이 둥글 나무입니다.", "is_correct": False, "formula": "D4", "explanation": "'둥글 나무'는 어색한 표현입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "문장 부호 및 마침표 확인",
                "stem": "글의 규칙에 맞게 마침표(.)가 바르게 찍힌 완성된 문장은?",
                "target_para_idx": 1,
                "spotlight_quote": "문장이 끝나는 곳에 마침표(.)를 꼭 찍어야 바른 글이 완성됩니다.",
                "options": [
                    {"label": "①", "text": "윷가락의 한쪽은 평평합니다.", "is_correct": True, "formula": "정답", "explanation": "설명하는 문장이 끝나고 마침표(.)가 올바르게 찍혔습니다."},
                    {"label": "②", "text": "윷가락의 한쪽은 평평합니다", "is_correct": False, "formula": "D6", "explanation": "문장 끝에 마침표(.)가 빠져 있습니다."},
                    {"label": "③", "text": "윷가락의 한쪽은 평평합니다?", "is_correct": False, "formula": "D2", "explanation": "설명하는 문장에는 물음표(?)가 아닌 마침표(.)를 써야 합니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 윷가락의 겉모양 특징으로 알맞은 설명은?",
                "options": [
                    {"label": "①", "text": "한쪽은 평평하고 다른 한쪽은 둥글다.", "is_correct": True},
                    {"label": "②", "text": "양쪽 모두 날카로운 세모 모양이다.", "is_correct": False},
                    {"label": "③", "text": "쇠로 만들어 무겁고 차갑다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "윷놀이는 설날에 가족들이 함께 모여 즐기는 전통 놀이입니다.", "is_correct": False},
                    {"label": "②", "text": "윷가락의 한쪽은 평평하고 다른 한쪽은 둥급니다.", "is_correct": True},
                    {"label": "③", "text": "문장이 끝나는 곳에 마침표(.)를 꼭 찍어야", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "윷가락 소개 3문장 완성하기",
            "guide": "조사('은/는, 이/가')와 마침표(.)를 바르게 살려 문장을 완성해 보세요.",
            "template": "윷놀이[   ] 우리나라 전통 놀이입니다. 윷가락[   ] 나무로 만듭니다. 한쪽은 평평합니다[   ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "받침이 있는 낱말 뒤에는 '은/이', 받침이 없는 낱말 뒤에는 '는/가'를 써요."},
            "step1_2_drill": {"task": "알맞은 조사 고르기와 문장 끝 마침표 찍기 연습"},
            "step3_vaccine": {"ox_quiz": [{"statement": "설명하는 문장을 다 쓴 뒤에는 마침표(.)를 찍어야 합니다.", "answer": "O", "reason": "문장 부호 기본 규칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 전통 놀이와 문장 만들기",
            "situation": "명절이나 주말에 전통 놀이 이야기를 나눌 때",
            "parent_question": "윷가락을 던졌을 때 평평한 쪽이 위로 나오면 무슨 모양이 될까?",
            "expected_answer": "평평한 쪽이 1개 나오면 도, 2개 나오면 개가 돼요!",
            "coaching_tip": "아이가 문장을 말할 때 끝맺음을 분명히 하도록 칭찬해 주세요."
        }
    ),

    # Slot 16: W5
    build_expository_slot(
        grade_num=1,
        subskill_code="W5",
        subject="통합(학교·사람들 1-1)",
        unit="5. 바른 생활 습관",
        concept="학교 도서관 이용 안내글 고쳐쓰기",
        text_structure="순서·열거",
        structure_type_code="sequence",
        passage_title="다 함께 이용하는 학교 도서관",
        paragraphs=[
            "학교 도서관은 전교생이 함께 책을 읽는 조용한 공간입니다. 도서관에서는 첫째, 조용조용 발걸음으로 걸어 다녀야 합니다. 둘째, 다 읽은 책은 제자리에 바르게 꽂아 두어야 합니다.",
            "안내글을 다 쓴 뒤에는 잘못 쓴 받침이 없는지, 띄어쓰기가 잘되었는지, 문장 끝에 마침표가 빠지지 않았는지 꼼꼼하게 다시 읽고 고쳐 써야 합니다."
        ],
        vocab_notes=[
            {"word": "전교생", "definition": "학교에 다니는 모든 학생"},
            {"word": "고쳐쓰기", "definition": "글을 다 쓴 뒤 틀린 글자나 빠진 내용을 바르게 고치는 일"}
        ],
        visual_html="""<div class="p-3 bg-indigo-50 rounded border border-indigo-200">
          <h4 class="font-bold text-indigo-900 mb-2">🔍 도서관 안내문 3대 고쳐쓰기 돋보기</h4>
          <div class="grid grid-cols-3 gap-1 text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-indigo-100"><strong>1. 받침 틀림</strong><br>책읃 ➔ 책을</div>
            <div class="p-1.5 bg-white rounded border border-indigo-100"><strong>2. 띄어쓰기</strong><br>책을읽어요 ➔ 책을 읽어요</div>
            <div class="p-1.5 bg-white rounded border border-indigo-100"><strong>3. 마침표 누락</strong><br>합니다 ➔ 합니다.</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g1-w5-c1", "text": "둘째, 다 읽은 책은 제자리에 바르게 꽂아 두어야 합니다", "role": "도서관 이용 규칙", "para_idx": 0},
            {"cue_id": "g1-w5-c2", "text": "꼼꼼하게 다시 읽고 고쳐 써야 합니다", "role": "고쳐쓰기 지침", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "고쳐쓰기 점검표",
            "checkpoints": [
                "글자 받침이 틀린 곳이 없는가?",
                "낱말과 낱말 사이 띄어쓰기를 했는가?",
                "문장 끝에 마침표(.)가 있는가?"
            ]
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "글자 받침 오류 교정",
                "stem": "다음 중 받침을 잘못 써서 고쳐야 할 낱말은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "안내글을 다 쓴 뒤에는 잘못 쓴 받침이 없는지, 띄어쓰기가 잘되었는지, 문장 끝에 마침표가 빠지지 않았는지 꼼꼼하게 다시 읽고 고쳐 써야 합니다.",
                "options": [
                    {"label": "①", "text": "'책읃' ➔ '책을'로 고쳐야 한다.", "is_correct": True, "formula": "정답", "explanation": "'책읃'은 잘못된 받침이므로 '책을'로 고쳐야 합니다."},
                    {"label": "②", "text": "'조용히' ➔ '조용힏'으로 고쳐야 한다.", "is_correct": False, "formula": "D1", "explanation": "오히려 맞는 글자를 틀리게 바꾸는 잘못된 보기입니다."},
                    {"label": "③", "text": "'학교' ➔ '학굗'으로 고쳐야 한다.", "is_correct": False, "formula": "D3", "explanation": "'학교'는 올바른 글자이므로 고칠 필요가 없습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "도서관 규칙 내용 확인",
                "stem": "글을 통해 알 수 있는 올바른 도서관 이용 방법은?",
                "target_para_idx": 0,
                "spotlight_quote": "둘째, 다 읽은 책은 제자리에 바르게 꽂아 두어야 합니다.",
                "options": [
                    {"label": "①", "text": "친구들과 큰 소리로 장난치며 뛰어다닌다.", "is_correct": False, "formula": "D2", "explanation": "도서관에서는 조용조용 걸어 다녀야 합니다."},
                    {"label": "②", "text": "다 읽은 책은 제자리에 바르게 꽂아 둔다.", "is_correct": True, "formula": "정답", "explanation": "1문단에서 다 읽은 책은 제자리에 꽂아야 한다고 했습니다."},
                    {"label": "③", "text": "책을 바닥에 아무렇게나 던져 둔다.", "is_correct": False, "formula": "D4", "explanation": "바른 이용 습관에 어긋나는 행동입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 도서관 안내글을 다 쓴 뒤 꼭 해야 할 일은?",
                "options": [
                    {"label": "①", "text": "틀린 글자와 마침표를 꼼꼼히 확인하고 고쳐 쓴다.", "is_correct": True},
                    {"label": "②", "text": "다 쓴 글을 바로 찢어 버린다.", "is_correct": False},
                    {"label": "③", "text": "더 이상 글을 다시 읽어 보지 않는다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "학교 도서관은 전교생이 함께 책을 읽는 조용한 공간입니다.", "is_correct": False},
                    {"label": "②", "text": "마침표가 빠지지 않았는지 꼼꼼하게 다시 읽고 고쳐 써야 합니다.", "is_correct": True},
                    {"label": "③", "text": "둘째, 다 읽은 책은 제자리에 바르게 꽂아 두어야 합니다.", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "도서관 안내문 고쳐쓰기 실습",
            "guide": "틀린 받침과 빠진 마침표를 찾아 바르게 고쳐 써 보세요.",
            "template": "원문: 다 읽은 책읃 제자리에 꽂습니다 ➔ 바른 글: 다 읽은 [       ] 제자리에 꽂습니다[   ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글을 다 쓰고 나면 돋보기로 보듯 받침과 마침표를 한 글자씩 확인해요."},
            "step1_2_drill": {"task": "틀린 받침에 동그라미 치고 바른 글자 쓰기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "글을 쓴 뒤에는 다시 읽고 틀린 글자를 고쳐 쓰는 것이 좋습니다.", "answer": "O", "reason": "좋은 글을 완성하는 마지막 퇴고 단계입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 고쳐쓰기의 힘",
            "situation": "아이가 글짓기나 알림장을 쓰고 난 후 함께 볼 때",
            "parent_question": "글을 다 쓴 다음에 스스로 다시 읽어 보면 어떤 좋은 점이 있을까?",
            "expected_answer": "틀린 글자나 빠뜨린 마침표를 찾아서 더 멋진 글로 고칠 수 있어요!",
            "coaching_tip": "실수를 지적하기보다 스스로 찾아낸 고침을 듬뿍 칭찬해 주세요."
        }
    )
]

g1_all_expository = g1_exp_slots + g1_remaining_exp

print(f"Total Grade 1 Expository Slots: {len(g1_all_expository)} (expected 16)")
print(f"Total Grade 1 Common Slots: {len(g1_common_slots)} (expected 6)")

out_path = os.path.join(ITEM_BANK_DIR, "g1_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 1,
        "expository_slots": g1_all_expository,
        "common_slots": g1_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g1_all_expository)} Expository + {len(g1_common_slots)} Common)")
