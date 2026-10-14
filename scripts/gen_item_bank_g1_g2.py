# -*- coding: utf-8 -*-
"""
초등 1~2학년 설명문(Expository 32슬롯) 및 공통기초(Common 12슬롯) 문항 은행 생성기
- 산출물:
  1) courseware/data/item_bank/g1_item_bank.json (1학년 설명문 16슬롯 + 공통기초 6슬롯)
  2) courseware/data/item_bank/g2_item_bank.json (2학년 설명문 16슬롯 + 공통기초 6슬롯)
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from item_bank_schema_helper import (
    ITEM_BANK_DIR,
    build_common_slot,
    build_expository_slot,
    strip_html,
)


# =============================================================================
# 1학년 공통기초 슬롯 (G1-COM-A1 ~ G1-COM-A6)
# =============================================================================
G1_COMMON_SLOTS = [
    build_common_slot(
        grade_num=1,
        com_code_suffix="A1",
        title="받침이 있는 글자와 친숙한 사물 낱말 바르게 읽고 짝짓기",
        rule_box="💡 **해독·낱말 공식**: 글자 아래에 있는 **받침(ㄱ, ㄴ, ㄹ, ㅁ, ㅂ, ㅇ)** 소리를 정확히 내어 읽고, 같은 종류의 사물끼리 묶어 보아요!",
        passage_snippet="우리 교실 책상 위에는 연필, 지우개, 공책이 나란히 놓여 있습니다. 가방 안에는 알록달록한 색연필과 필통도 들어 있습니다.",
        mini_question="윗글에 나온 낱말 가운데 ‘글씨를 쓰거나 지울 때 쓰는 학용품’끼리 바르게 묶인 것은 무엇인가요?",
        choices=[
            "연필, 지우개, 색연필",
            "연필, 강아지, 구름",
            "가방, 비행기, 냉장고",
        ],
        correct="연필, 지우개, 색연필",
        feedback="딩동댕! ‘연필, 지우개, 색연필’은 모두 교실에서 글씨를 쓰거나 그림을 그릴 때 사용하는 ‘학용품’ 가족이에요!",
        ox_items=[
            {
                "statement": "‘책상’과 ‘가방’에는 모두 동그라미 모양의 ‘ㅇ’ 받침이 들어 있습니다.",
                "answer": "O",
                "reason": "맞아요! ‘책상(상)’과 ‘가방(방)’의 마지막 글자 아래에는 모두 ‘ㅇ’ 받침이 들어 있어요.",
            },
            {
                "statement": "‘연필’과 ‘지우개’는 하늘을 나는 탈것을 나타내는 낱말입니다.",
                "answer": "X",
                "reason": "삐뽀! 연필과 지우개는 탈것이 아니라 공부할 때 쓰는 ‘학용품’이에요.",
            },
        ],
    ),
    build_common_slot(
        grade_num=1,
        com_code_suffix="A2",
        title="소리와 모양을 흉내 내는 말(의성어·의태어)의 생생한 느낌 찾기",
        rule_box="💡 **감각 낱말 공식**: **소리를 흉내 내는 말(개골개골, 칙칙폭폭)**과 **모양을 흉내 내는 말(깡충깡충, 엉금엉금)**을 찾으면 대상의 모습이 눈앞에 생생하게 그려져요!",
        passage_snippet="비 오는 날 연못가에서 청개구리가 개골개골 큰 소리로 노래를 부릅니다. 아기 토끼는 풀밭 위를 깡충깡충 힘차게 뛰어갑니다.",
        mini_question="윗글에서 아기 토끼가 뛰어가는 ‘모양’을 흉내 낸 말은 무엇인가요?",
        choices=[
            "깡충깡충",
            "개골개골",
            "연못가에서",
        ],
        correct="깡충깡충",
        feedback="정답이에요! ‘개골개골’은 개구리의 울음소리를 흉내 낸 말이고, ‘깡충깡충’은 토끼가 긴 뒷다리로 뛰어가는 모양을 흉내 낸 말이에요.",
        ox_items=[
            {
                "statement": "‘개골개골’은 청개구리가 우는 소리를 흉내 낸 말입니다.",
                "answer": "O",
                "reason": "딩동댕! 귀로 들리는 소리를 그대로 흉내 낸 말이에요.",
            },
            {
                "statement": "거북이가 느리게 걸어가는 모양은 ‘깡충깡충’이라고 표현합니다.",
                "answer": "X",
                "reason": "거북이가 느리게 기어가는 모양은 ‘깡충깡충’이 아니라 ‘엉금엉금’이라고 표현해요!",
            },
        ],
    ),
    build_common_slot(
        grade_num=1,
        com_code_suffix="A3",
        title="‘누가/무엇이 - 어찌하다/어떠하다’ 문장 짝짓기와 마침표 찍기",
        rule_box="💡 **문장 뼈대 공식**: 문장은 **‘무엇이(주인공)’**와 **‘어떠하다/어찌하다(설명)’**가 알맞게 짝을 이루어야 하고, 설명하는 문장 끝에는 꼭 **마침표(`.`)**를 찍어요!",
        passage_snippet="노란 개나리가 활짝 피었습니다. 아기 참새가 나뭇가지에 앉아 지저귑니다. 봄바람이 살랑살랑 불어옵니다.",
        mini_question="다음 중 ‘무엇이 - 어찌하다’ 짝이 자연스럽고 문장부호가 바르게 쓰인 문장은 무엇인가요?",
        choices=[
            "아기 참새가 나뭇가지에서 노래를 부릅니다.",
            "책상이 하늘 높이 날아갑니다?",
            "노란 개나리가 맛있게 밥을 먹습니다",
        ],
        correct="아기 참새가 나뭇가지에서 노래를 부릅니다.",
        feedback="참 잘했어요! ‘아기 참새가(누가) + 노래를 부릅니다(어찌하다)’가 자연스럽게 연결되었고, 설명하는 문장 끝에 마침표(`.`)도 정확히 찍혔어요.",
        ox_items=[
            {
                "statement": "무엇을 물어보는 질문 문장 끝에는 물음표(?)를 쓰고, 사실을 알려 주는 문장 끝에는 마침표(.)를 씁니다.",
                "answer": "O",
                "reason": "맞아요! 설명하는 문장 끝에는 마침표(.), 물어보는 문장 끝에는 물음표(?)를 써요.",
            },
            {
                "statement": "“노란 개나리가”만 써도 완전한 한 문장이 됩니다.",
                "answer": "X",
                "reason": "뒤에 ‘피었습니다’나 ‘예쁩니다’처럼 ‘어찌하다/어떠하다’ 말이 와야 온전한 문장이 돼요!",
            },
        ],
    ),
    build_common_slot(
        grade_num=1,
        com_code_suffix="A4",
        title="가리키는 말(‘이것, 이 동물, 여기’)이 받는 앞 문장 낱말 찾기",
        rule_box="💡 **지시어 화살표 공식**: 문장에 **‘이것은, 이 동물은, 여기는’**이 나오면 바로 **앞 문장 맨 앞의 주인공 낱말**로 화살표를 연결해 보세요!",
        passage_snippet="도서관에는 재미있는 그림책이 아주 많습니다. 여기는 친구들과 함께 조용히 책을 읽는 곳입니다. 다 읽은 책은 제자리에 꽂아 둡니다.",
        mini_question="윗글의 둘째 문장에 나오는 ‘여기’가 가리키는 장소는 어디인가요?",
        choices=[
            "도서관",
            "운동장",
            "그림책",
        ],
        correct="도서관",
        feedback="정답! 바로 앞 문장에서 소개한 장소인 ‘도서관’을 다시 부를 때 ‘여기는’이라는 가리키는 말을 썼어요.",
        ox_items=[
            {
                "statement": "“기린은 목이 깁니다. 이 동물은 나뭇잎을 좋아합니다.”에서 ‘이 동물’은 ‘기린’을 가리킵니다.",
                "answer": "O",
                "reason": "딩동댕! 바로 앞 문장의 주인공인 ‘기린’을 가리키는 말이에요.",
            },
            {
                "statement": "‘여기는’은 사람의 이름을 가리킬 때 쓰는 말입니다.",
                "answer": "X",
                "reason": "‘여기, 거기, 저기’는 사람이 아니라 ‘장소(곳)’를 가리킬 때 쓰는 말이에요!",
            },
        ],
    ),
    build_common_slot(
        grade_num=1,
        com_code_suffix="A5",
        title="‘~해서, 그래서’로 이어진 까닭(원인)과 결과 짝짓기",
        rule_box="💡 **까닭-결과 공식**: **‘~해서 / 왜냐하면’** 앞에는 일이 일어난 **까닭(이유)**이 오고, **‘그래서’** 뒤에는 **결과**가 따라와요!",
        passage_snippet="아침부터 하늘에서 비가 주룩주룩 내렸습니다. 그래서 민수는 노란 우산을 활짝 펴고 학교에 갔습니다. 장화도 신어서 발이 젖지 않았습니다.",
        mini_question="민수가 노란 우산을 펴고 학교에 간 ‘까닭(이유)’은 무엇인가요?",
        choices=[
            "아침부터 하늘에서 비가 내렸기 때문입니다.",
            "운동장에서 축구를 하고 싶었기 때문입니다.",
            "날씨가 아주 맑고 더웠기 때문입니다.",
        ],
        correct="아침부터 하늘에서 비가 내렸기 때문입니다.",
        feedback="딩동댕! ‘그래서’ 앞 문장인 “아침부터 하늘에서 비가 주룩주룩 내렸습니다”가 우산을 쓴 까닭(원인)이에요.",
        ox_items=[
            {
                "statement": "“장화를 신어서 발이 젖지 않았습니다.”에서 까닭은 ‘장화를 신은 것’입니다.",
                "answer": "O",
                "reason": "맞아요! ‘~어서’ 앞에 있는 ‘장화를 신은 것’이 까닭이고, ‘발이 젖지 않은 것’이 결과예요.",
            },
            {
                "statement": "비가 내린 것은 민수가 우산을 폈기 때문에 일어난 결과입니다.",
                "answer": "X",
                "reason": "까닭과 결과가 뒤바뀌었어요! 비가 내렸기 때문에(까닭) 우산을 편 것(결과)이에요.",
            },
        ],
    ),
    build_common_slot(
        grade_num=1,
        com_code_suffix="A6",
        title="짧은 글에서 가장 많이 나오는 핵심 낱말(주인공) 찾기",
        rule_box="💡 **핵심 낱말 공식**: 짧은 설명글에서 **여러 번 반복**되거나 모든 문장이 설명하고 있는 **주인공 낱말 1개**가 바로 그 글의 ‘중심 낱말’이에요!",
        passage_snippet="해바라기는 여름에 피는 노란 꽃입니다. 해바라기는 줄기가 어른 키만큼 길쭉하게 자랍니다. 또 해바라기 씨앗은 고소해서 간식으로도 먹습니다.",
        mini_question="윗글의 모든 문장이 공통으로 설명하고 있는 ‘중심 낱말(주인공)’은 무엇인가요?",
        choices=[
            "해바라기",
            "여름 방학",
            "어른 키",
        ],
        correct="해바라기",
        feedback="정답이에요! 세 문장 모두 ‘해바라기’의 꽃 색깔, 줄기 크기, 씨앗의 쓰임새를 설명하고 있으므로 중심 낱말은 ‘해바라기’입니다.",
        ox_items=[
            {
                "statement": "윗글에 가장 잘 어울리는 제목은 ‘노랗고 키가 큰 해바라기’입니다.",
                "answer": "O",
                "reason": "중심 낱말인 ‘해바라기’와 주요 특징이 잘 들어가 있는 멋진 제목이에요!",
            },
            {
                "statement": "윗글은 여름 방학 물놀이 안전 수칙을 알려 주는 글입니다.",
                "answer": "X",
                "reason": "물놀이 이야기는 전혀 없고 ‘해바라기’의 특징을 설명하는 글이에요.",
            },
        ],
    ),
]


# =============================================================================
# 1학년 설명문 슬롯 (G1-EXP-V1-1 ~ G1-EXP-W5, 총 16슬롯)
# =============================================================================
G1_EXPOSITORY_SLOTS = [
    # -------------------------------------------------------------------------
    # 1차시: G1-EXP-V1-1 (봄을 알리는 노란 개나리)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V1-1",
        subject="통합교과(자연·계절 1-1)",
        unit="봄이 왔어요 - 봄꽃 관찰하기",
        concept="개나리의 노란 꽃잎 모양과 피는 시기",
        text_structure="기술·열거",
        structure_type_code="analysis",
        passage_title="봄을 알리는 노란 개나리",
        paragraphs=[
            "따뜻한 봄이 오면 길가에 개나리가 활짝 핍니다. 개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있습니다. 작은 나팔처럼 생긴 꽃들이 긴 줄기에 나란히 매달려 피어납니다. 개나리는 초록 잎보다 노란 꽃이 먼저 피어서 봄이 온 것을 가장 먼저 알려 줍니다."
        ],
        vocab_notes=[
            {"word": "갈래", "tier": "Tier 1 (기초)", "desc": "하나에서 여러 개로 갈라진 줄기나 부분"},
            {"word": "나팔", "tier": "Tier 1 (기초)", "desc": "입으로 불어서 소리를 내는 끝이 퍼진 악기"},
            {"word": "매달리다", "tier": "Tier 2 (사고어)", "desc": "어떤 곳에 붙어서 아래로 드리워지다"},
        ],
        visual_html="""
        <div style="background:#FEFCE8; border:2px solid #FDE047; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#854D0E; margin-bottom:10px;">🌼 [실물 관찰 카드] 봄을 알리는 개나리 생김새 살펴보기</div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
            <div style="background:#fff; padding:10px; border-radius:8px; border:1px solid #FACC15;">
              <div style="font-size:1.3rem;">🌸 <b>꽃 색깔</b></div>
              <div style="font-size:0.86rem; color:#713F12; margin-top:4px;">병아리처럼 <b>샛노란 색</b></div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:1px solid #FACC15;">
              <div style="font-size:1.3rem;">🎺 <b>꽃잎 모양</b></div>
              <div style="font-size:0.86rem; color:#713F12; margin-top:4px;">작은 나팔 모양 · <b>네 갈래</b></div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:1px solid #FACC15;">
              <div style="font-size:1.3rem;">🌱 <b>피는 차례</b></div>
              <div style="font-size:0.86rem; color:#713F12; margin-top:4px;">초록 잎보다 <b>꽃이 먼저 핌</b></div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v1-1-c1", "text": "개나리", "role": "설명 대상 이름: 봄을 알리는 꽃", "para_idx": 0},
            {"cue_id": "g1-v1-1-c2", "text": "샛노란 꽃잎이 네 갈래", "role": "겉모습 특징 ①: 색깔과 꽃잎 수", "para_idx": 0},
            {"cue_id": "g1-v1-1-c3", "text": "초록 잎보다 노란 꽃이 먼저", "role": "피는 시기 특징 ②: 꽃이 잎보다 먼저 핌", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 대상·특징 도해] 개나리의 이름과 겉모습 특징 짝짓기",
            "instruction": "개나리의 특징을 나타내는 알맞은 낱말 카드를 골라 빈칸에 넣으세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "🌼 꽃 이름과 계절", "sub": "따뜻한 봄에 피는 꽃", "correct": "개나리"},
                {"slot_id": "slot-2", "header": "🎨 꽃잎 색깔과 갈래", "sub": "작은 나팔 모양 꽃잎", "correct": "샛노란 색 · 네 갈래"},
                {"slot_id": "slot-3", "header": "🌿 피어나는 순서", "sub": "잎과 꽃 가운데 먼저!", "correct": "초록 잎보다 노란 꽃이 먼저 핌"},
            ],
            "word_bank": [
                "개나리",
                "샛노란 색 · 네 갈래",
                "초록 잎보다 노란 꽃이 먼저 핌",
                "추운 겨울에 하얀 꽃이 핌 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V1-1 (명시적 대상·겉모습 사실 확인 - 3지선다)",
                "stem": "윗글에서 설명하는 ‘개나리’의 꽃잎 모습으로 <u>알맞은</u> 것은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있습니다.",
                "step1_hint": "잠깐! 본문 두 번째 문장에서 개나리 꽃잎의 색깔과 몇 갈래인지 적힌 노란색 문장을 다시 읽어 보세요!",
                "step2_hint": "‘샛노란 꽃잎’이 ‘네 갈래’로 갈라져 있다고 그대로 적혀 있는 선지를 고르면 정답이에요!",
                "options": [
                    {
                        "no": 1,
                        "text": "샛노란 꽃잎이 네 갈래로 갈라져 있습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [대상 '개나리' + 명시적 특징 '샛노란 꽃잎', '네 갈래' 1:1 일치]",
                        "explanation": "🎉 **[정답]** 둘째 문장에 “개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있습니다.”라고 정확히 나와 있어요!",
                    },
                    {
                        "no": 2,
                        "text": "새하얀 꽃잎이 열 갈래로 갈라져 있습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 속성 수치·색깔 변형]: '샛노란/네 갈래'를 '새하얀/열 갈래'로 왜곡",
                        "explanation": "❌ **[D1 반대·변형 말 함정]** 개나리는 하얀색 열 갈래가 아니라 **샛노란 색 네 갈래**예요.",
                    },
                    {
                        "no": 3,
                        "text": "추운 겨울에 눈을 맞으며 피어납니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 계절 정보 반전]: '따뜻한 봄'을 '추운 겨울'로 반전",
                        "explanation": "❌ **[D1 계절 반대 함정]** 첫 문장에서 개나리는 추운 겨울이 아니라 **따뜻한 봄**이 오면 핀다고 했어요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V1-1 (<보기> 관찰 카드 빈칸 확인형 - 3지선다)",
                "stem": "윗글을 읽고 <보기>의 관찰 기록 카드를 완성할 때 빈칸에 들어갈 알맞은 말을 고르세요.",
                "bogi": "<보기>\n  [봄꽃 관찰 카드]\n  • 꽃 모양: 작은 나팔처럼 생겼습니다.\n  • 피는 특징: (                    )",
                "target_para_idx": 0,
                "spotlight_quote": "개나리는 초록 잎보다 노란 꽃이 먼저 피어서 봄이 온 것을 가장 먼저 알려 줍니다.",
                "step1_hint": "잠깐! 마지막 네 번째 문장에서 초록 잎과 노란 꽃 가운데 무엇이 먼저 핀다고 했는지 확인해 보세요!",
                "step2_hint": "‘초록 잎보다 노란 꽃이 먼저 피어서’라고 적힌 부분을 그대로 찾으면 돼요!",
                "options": [
                    {
                        "no": 1,
                        "text": "노란 꽃보다 초록 잎이 먼저 자라납니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D2 선후 관계 역전]: '초록 잎보다 노란 꽃이 먼저'의 순서를 반대로 뒤집음",
                        "explanation": "❌ **[D2 순서 뒤바뀜 함정]** 초록 잎이 먼저 나는 것이 아니라 **초록 잎보다 노란 꽃이 먼저** 피어나요!",
                    },
                    {
                        "no": 2,
                        "text": "초록 잎보다 노란 꽃이 먼저 피어납니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [본문 마지막 문장 '초록 잎보다 노란 꽃이 먼저 피어서' 정확 일치]",
                        "explanation": "🎉 **[정답]** 개나리는 초록 잎보다 노란 꽃이 먼저 피어서 봄이 온 것을 알려 줍니다!",
                    },
                    {
                        "no": 3,
                        "text": "꽃이 지고 난 뒤에 커다란 사과가 열립니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 글에 없는 내용]: 본문에 언급되지 않은 사과 열매 정보 삽입",
                        "explanation": "❌ **[D6 글에 없는 내용 함정]** 개나리에 사과가 열린다는 이야기는 글에 전혀 없어요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 대상 특징 확인 + 근거 문장 찾기)",
            "part_a_stem": "[Part A] 개나리 꽃들이 긴 줄기에 피어 있는 모양은 무엇과 비슷하다고 했나요?",
            "part_a_options": [
                {"no": 1, "text": "작은 나팔처럼 생긴 꽃들이 긴 줄기에 나란히 매달려 있습니다.", "is_correct": True},
                {"no": 2, "text": "커다란 축구공처럼 둥근 꽃이 땅바닥에 굴러다닙니다.", "is_correct": False},
                {"no": 3, "text": "뾰족한 바늘처럼 생긴 꽃이 하늘 위로 솟아 있습니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 알려 주는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “따뜻한 봄이 오면 길가에 개나리가 활짝 핍니다.”", "is_correct": False},
                {"no": 2, "text": "셋째 문장: “작은 나팔처럼 생긴 꽃들이 긴 줄기에 나란히 매달려 피어납니다.”", "is_correct": True},
                {"no": 3, "text": "넷째 문장: “개나리는 초록 잎보다 노란 꽃이 먼저 피어서 봄이 온 것을 가장 먼저 알려 줍니다.”", "is_correct": False},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 개나리 꽃 모양이 ‘작은 나팔’(Part A) 같다는 사실은 본문 셋째 문장(Part B)에 정확히 적혀 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W4",
            "title": "[TEI-6 작문 워크벤치] ‘개나리의 이름과 특징’ 소개 문장 완성하기",
            "conditions": [
                "조건 ①: 꽃의 이름(‘개나리는’)을 문장 맨 앞에 넣을 것",
                "조건 ②: 본문에 나온 꽃잎 색깔과 갈래 수(‘샛노란 꽃잎이 네 갈래’)를 바르게 쓸 것",
            ],
            "draft_prefix": "봄이 오면 길가에 예쁜 꽃이 핍니다.",
            "choices": [
                {
                    "id": "w-1",
                    "text": "개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있습니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 완벽해요! 꽃 이름(‘개나리는’)과 겉모습 특징(‘샛노란 꽃잎이 네 갈래’)을 모두 바르게 썼어요.",
                },
                {
                    "id": "w-2",
                    "text": "샛노란 꽃잎이 다섯 갈래로 갈라져 있습니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 꽃 이름(‘개나리는’)이 빠졌고, 꽃잎도 다섯 갈래가 아니라 네 갈래예요.",
                },
                {
                    "id": "w-3",
                    "text": "개나리는 내가 세상에서 제일 좋아하는 꽃이라서 기분이 날아갈 것 같습니다.",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ 꽃잎의 색깔과 모양 특징 대신 내 기분을 적었어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V1-1 맞춤 처방전: [대상 이름 동그라미 ➔ 색깔·모양 낱말 밑줄 ➔ D1·D2 함정 백신]",
            "rx_reason": "사물이나 식물을 소개하는 글에서 대상 이름과 겉모습 낱말(색깔, 개수, 순서)을 1:1로 짝지어 정확히 확인하는 훈련을 진행합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A1 꽃 이름과 색깔·모양 낱말 짝짓기",
                "rule_box": "💡 **대상-특징 짝짓기 공식**: 첫 문장에서 **‘무엇(이름)’**에 동그라미를 치고, 뒤에 나오는 **‘색깔·모양 낱말’**에 밑줄을 그어요!",
                "mini_question": "“민들레는 노란 꽃이 활짝 핍니다.”에서 설명하는 꽃의 ‘이름’은 무엇인가요?",
                "choices": ["민들레", "소나무"],
                "correct": "민들레",
                "feedback": "딩동댕! 문장 맨 앞에 나온 ‘민들레’가 설명 대상의 이름이에요.",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V1-1 개나리 이름과 겉모습 낱말 빈칸 조립",
                "passage_snippet": "따뜻한 봄이 오면 길가에 <span class='rx-cue'>개나리</span>가 활짝 핍니다. 개나리는 <span class='rx-cue'>샛노란 꽃잎이 네 갈래</span>로 갈라져 있습니다. 개나리는 <span class='rx-cue'>초록 잎보다 노란 꽃이 먼저</span> 피어납니다.",
                "think_aloud_prompt": "본문의 노란색 단서를 보고 개나리의 3가지 특징 빈칸을 완성해 보세요!",
                "cloze_sentences": [
                    "• 1단계(대상 이름): 따뜻한 봄에 길가에 피는 꽃의 이름은 ( {b1} )입니다.",
                    "• 2단계(꽃잎 모양): 샛노란 꽃잎이 작은 나팔처럼 ( {b2} )로 갈라져 있습니다.",
                    "• 3단계(피는 순서): 초록 잎보다 ( {b3} )이 먼저 피어 봄을 알려 줍니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "개나리", "options": ["개나리", "해바라기", "단풍잎"]},
                    {"id": "b2", "correct": "네 갈래", "options": ["네 갈래", "열 갈래", "한 갈래"]},
                    {"id": "b3", "correct": "노란 꽃", "options": ["노란 꽃", "빨간 열매", "굵은 뿌리"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D1(숫자·색깔 바꾸기) & D2(순서 바꾸기) OX 판별",
                "desc": "수능형 문제에서는 꽃잎 갈래 수나 피는 순서를 슬쩍 바꾸어 놓아요! 눈을 크게 뜨고 판별해 볼까요?",
                "items": [
                    {
                        "statement": "개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있습니다.",
                        "answer": "O",
                        "reason": "딩동댕! 본문 둘째 문장과 글자 그대로 정확히 일치해요.",
                    },
                    {
                        "statement": "개나리는 초록 잎이 먼저 자라난 뒤에 노란 꽃이 핍니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D2 순서 뒤바뀜 함정]이에요! 개나리는 초록 잎보다 노란 꽃이 먼저 피어나요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 사물·식물 이름과 겉모습 말하기)",
            "situation": "아이와 함께 산책길에 본 꽃이나 식탁 위 과일(바나나, 딸기, 귤)을 살펴볼 때",
            "parent_question": "“오늘 읽은 개나리는 꽃잎이 무슨 색이고 몇 갈래로 갈라져 있었지? 그리고 초록 잎이랑 노란 꽃 중에 누가 먼저 핀다고 했을까?”",
            "expected_answer": "“개나리는 샛노란 꽃잎이 네 갈래로 갈라져 있어! 그리고 초록 잎보다 노란 꽃이 먼저 피어서 봄이 온 걸 알려 줘!”",
            "coaching_tip": "아이가 대상의 이름(‘개나리는’)을 먼저 말하고 색깔과 모양 특징을 두 가지 이상 정확히 말하면 엄지를 척 들어 칭찬해 주세요.",
        },
    ),

    # -------------------------------------------------------------------------
    # 2차시: G1-EXP-V1-2 (코가 길고 귀가 큰 코끼리)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V1-2",
        subject="통합교과(자연 1-1)",
        unit="자연과 함께해요 - 동물 친구들의 생김새",
        concept="코끼리의 코·귀·다리의 생김새와 하는 일",
        text_structure="분석 기초 (전체-부분)",
        structure_type_code="analysis",
        passage_title="코가 길고 귀가 큰 코끼리",
        paragraphs=[
            "코끼리는 땅 위에서 사는 동물 가운데 몸집이 가장 큽니다. 이 동물은 길쭉한 코를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹습니다. 또 넓적한 귀를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다. 굵은 기둥 같은 네 다리는 무거운 몸을 튼튼하게 받쳐 줍니다."
        ],
        vocab_notes=[
            {"word": "몸집", "tier": "Tier 1 (기초)", "desc": "몸의 크기나 부피"},
            {"word": "팔랑거리다", "tier": "Tier 1 (감각어)", "desc": "넓고 얇은 물체가 바람에 가볍게 자꾸 흔들리다"},
            {"word": "받쳐 주다", "tier": "Tier 2 (사고어)", "desc": "무거운 것이 쓰러지지 않게 아래에서 버티어 주다"},
        ],
        visual_html="""
        <div style="background:#FFFBEB; border:2px solid #FDE68A; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#92400E; margin-bottom:10px;">🐘 [그림 지시선 자료] 코끼리의 몸 부위와 하는 일 (전체-부분 구조도)</div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #93C5FD;">
              <div style="font-size:1.3rem;">👃 <b>길쭉한 코</b></div>
              <div style="font-size:0.85rem; color:#1E40AF; margin-top:4px;">손처럼 물 마시기 · 먹이 집기</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #86EFAC;">
              <div style="font-size:1.3rem;">👂 <b>넓적한 귀</b></div>
              <div style="font-size:0.85rem; color:#166534; margin-top:4px;">부채처럼 흔들어 더운 몸 식히기</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #FDBA74;">
              <div style="font-size:1.3rem;">🦵 <b>굵은 네 다리</b></div>
              <div style="font-size:0.85rem; color:#9A3412; margin-top:4px;">기둥처럼 무거운 몸 받치기</div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v1-2-c1", "text": "이 동물은", "role": "앞 문장 주인공(‘코끼리’)을 가리키는 지시어", "para_idx": 0},
            {"cue_id": "g1-v1-2-c2", "text": "길쭉한 코", "role": "부위 ①: 손처럼 물을 마시거나 먹이를 집는 부분", "para_idx": 0},
            {"cue_id": "g1-v1-2-c3", "text": "넓적한 귀", "role": "부위 ②: 부채처럼 팔랑거려 더운 몸을 식히는 부분", "para_idx": 0},
            {"cue_id": "g1-v1-2-c4", "text": "네 다리", "role": "부위 ③: 기둥처럼 무거운 몸을 받쳐 주는 부분", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 전체-부분 분석 구조도] 코끼리의 몸 부위와 하는 일 짝짓기",
            "instruction": "아래 보기 카드를 탭하여 코끼리의 각 몸 부위가 하는 일 빈칸을 완성하세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "👃 길쭉한 코", "sub": "모양: 긴 호스 모양", "correct": "손처럼 물 마시기 · 먹이 집기"},
                {"slot_id": "slot-2", "header": "👂 넓적한 귀", "sub": "모양: 큰 부채 모양", "correct": "팔랑거려 더운 몸 식히기"},
                {"slot_id": "slot-3", "header": "🦵 굵은 네 다리", "sub": "모양: 튼튼한 기둥 모양", "correct": "무거운 몸 튼튼하게 받치기"},
            ],
            "word_bank": [
                "손처럼 물 마시기 · 먹이 집기",
                "팔랑거려 더운 몸 식히기",
                "무거운 몸 튼튼하게 받치기",
                "하늘 높이 날아오르기 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V1-2 (지시어 연결 및 전체-부분 관계 확인 - 3지선다)",
                "stem": "윗글의 둘째 문장에 나오는 ‘이 동물’에 대한 설명으로 <u>알맞은</u> 것은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "이 동물은 길쭉한 코를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹습니다.",
                "step1_hint": "잠깐! 1문단 두 번째 문장에서 ‘이 동물은’ 뒤에 어떤 부위로 무엇을 한다고 적혀 있는지 노란색 하이라이트 문장을 다시 읽어 볼까요?",
                "step2_hint": "‘길쭉한 코 = 먹이 집어 먹기’, ‘굵은 네 다리 = 무거운 몸 받치기’예요! 부위와 역할을 바르게 짝지어 보세요.",
                "options": [
                    {
                        "no": 1,
                        "text": "땅 위에서 사는 동물 가운데 몸집이 가장 작습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 반대 진술]: '가장 큽니다'를 '가장 작습니다'로 반전",
                        "explanation": "❌ **[D1 반대 말 함정]** 첫 문장에서 코끼리는 땅 위에서 사는 동물 가운데 몸집이 **가장 크다**고 했어요.",
                    },
                    {
                        "no": 2,
                        "text": "길쭉한 코를 손처럼 움직여서 먹이를 집어 먹습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [지시어 '이 동물' = 코끼리] + [코의 기능 일치]",
                        "explanation": "🎉 **[정답]** ‘이 동물(코끼리)’은 길쭉한 코를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹어요.",
                    },
                    {
                        "no": 3,
                        "text": "넓적한 귀로 무거운 몸을 기둥처럼 받쳐 줍니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 속성 교차 치환]: '네 다리'의 역할을 '넓적한 귀'에 잘못 연결",
                        "explanation": "❌ **[D4 부위-역할 교차 함정]** 무거운 몸을 기둥처럼 받쳐 주는 것은 귀가 아니라 **굵은 네 다리**예요!",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V1-2 (<보기> 상황 적용 및 부위별 역할 연결 - 3지선다)",
                "stem": "윗글을 읽고 <보기>의 아기 코끼리가 왜 귀를 움직였는지 알맞게 말한 것을 고르세요.",
                "bogi": "<보기>\n  햇볕이 쨍쨍 내리쬐는 더운 낮이 되었습니다. 아기 코끼리가 넓적한 양쪽 귀를 부채처럼 빠르게 팔랑거렸습니다.",
                "target_para_idx": 0,
                "spotlight_quote": "또 넓적한 귀를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다.",
                "step1_hint": "잠깐! 본문 세 번째 문장에서 ‘넓적한 귀를 부채처럼 팔랑거려서’ 무엇을 한다고 했는지 노란색 문장을 확인해 보세요!",
                "step2_hint": "<보기>는 ‘햇볕이 쨍쨍 내리쬐는 더운 낮’이에요. 더운 날 부채처럼 귀를 흔드는 까닭을 연결해 보세요!",
                "options": [
                    {
                        "no": 1,
                        "text": "더워진 몸을 시원하게 식히려고 귀를 팔랑거렸습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [본문 3문장 '귀를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다' 상황 적용]",
                        "explanation": "🎉 **[정답]** 더운 낮에 코끼리가 귀를 부채처럼 팔랑거린 까닭은 **더운 몸을 시원하게 식히기 위해서**예요!",
                    },
                    {
                        "no": 2,
                        "text": "땅에 떨어진 열매를 귀로 집어 먹으려고 팔랑거렸습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 부위 기능 교차]: 먹이를 집어 먹는 '코'의 기능을 '귀'에 결합",
                        "explanation": "❌ **[D4 부위 기능 혼동]** 먹이를 집어 먹는 부위는 귀가 아니라 **길쭉한 코**예요.",
                    },
                    {
                        "no": 3,
                        "text": "새처럼 하늘 높이 날아오르려고 귀를 팔랑거렸습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 본문 외 상상]: '팔랑거리다'라는 단어만 보고 하늘을 난다는 허위 상식 결합",
                        "explanation": "❌ **[D6 글에 없는 상상 함정]** 코끼리는 몸집이 아주 큰 땅 위 동물이라서 귀를 흔들어 하늘을 날 수 없어요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 추론 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 코끼리가 무거운 몸으로 쓰러지지 않고 서 있을 수 있는 까닭은 무엇인가요?",
            "part_a_options": [
                {"no": 1, "text": "굵은 기둥 같은 네 다리가 몸을 튼튼하게 받쳐 주기 때문입니다.", "is_correct": True},
                {"no": 2, "text": "넓적한 귀로 바람을 일으켜 몸을 띄워 주기 때문입니다.", "is_correct": False},
                {"no": 3, "text": "길쭉한 코로 땅바닥을 짚고 서 있기 때문입니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 고른 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “코끼리는 땅 위에서 사는 동물 가운데 몸집이 가장 큽니다.”", "is_correct": False},
                {"no": 2, "text": "셋째 문장: “또 넓적한 귀를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다.”", "is_correct": False},
                {"no": 3, "text": "넷째 문장: “굵은 기둥 같은 네 다리는 무거운 몸을 튼튼하게 받쳐 줍니다.”", "is_correct": True},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 무거운 몸을 받쳐 주는 것은 ‘굵은 네 다리’(Part A)이며, 그 근거는 본문 마지막 넷째 문장(Part B)에 정확히 나와 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W4",
            "title": "[TEI-6 작문 워크벤치] ‘기린의 몸 부위와 하는 일’ 조건 문장 조립하기",
            "conditions": [
                "조건 ①: 앞 문장 ‘기린’을 받는 가리키는 말(‘이 동물은’)을 넣을 것",
                "조건 ②: 몸 부위(‘긴 목’)와 하는 일(‘높은 나뭇잎 따 먹기’)을 바르게 연결할 것",
            ],
            "draft_prefix": "기린은 동물원에서 키가 가장 큰 동물입니다.",
            "choices": [
                {
                    "id": "w-1",
                    "text": "이 동물은 긴 목을 뻗어 높은 나무에 있는 나뭇잎을 잘 따 먹습니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 두 가지 조건(지시어 ‘이 동물은’ + 긴 목의 역할)을 모두 완벽하게 지켰어요!",
                },
                {
                    "id": "w-2",
                    "text": "긴 목을 뻗어 땅속에 숨은 두더지를 잡습니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 가리키는 말(‘이 동물은’)이 빠졌고, 기린의 실제 특징과도 맞지 않아요.",
                },
                {
                    "id": "w-3",
                    "text": "이 동물은 너무 귀여워서 내가 제일 좋아하는 최고 동물입니다!",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ 설명하는 글인데 몸 부위가 하는 일 대신 내 기분(감상)을 적었어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V1-2 맞춤 처방전: [지시어 화살표 잇기 ➔ 코끼리 부위별 역할 조립 ➔ D4 교차 함정 백신]",
            "rx_reason": "1학년 설명문에서 여러 부위(코, 귀, 다리)가 연달아 나올 때 헷갈리지 않도록, [부위 이름 = 하는 일]을 1:1로 묶는 사고구술 훈련을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A4 가리키는 말(‘이 동물은’) 화살표 잇기",
                "rule_box": "💡 **가리키는 말 공식**: 문장 앞에 **‘이 동물은 / 이 물건은’**이 나오면 바로 **앞 문장 맨 앞 주인공 이름**에 동그라미를 쳐요!",
                "mini_question": "“기린은 목이 아주 깁니다. 이 동물은 높은 나무에 있는 나뭇잎을 잘 따 먹습니다.” — ‘이 동물’은 누구인가요?",
                "choices": ["기린", "다람쥐"],
                "correct": "기린",
                "feedback": "딩동댕! 바로 앞 문장의 주인공인 ‘기린’을 가리켜요.",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V1-2 코끼리 몸 부위(코·귀·다리)와 하는 일 조립하기",
                "passage_snippet": "코끼리는 땅 위에서 사는 동물 가운데 몸집이 가장 큽니다. <span class='rx-cue'>이 동물은</span> 길쭉한 <span class='rx-cue'>코</span>를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹습니다. 또 넓적한 <span class='rx-cue'>귀</span>를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다. 굵은 기둥 같은 네 <span class='rx-cue'>다리</span>는 무거운 몸을 튼튼하게 받쳐 줍니다.",
                "think_aloud_prompt": "노란색 부위 단서를 눌러 보고, 코끼리의 세 부위가 각각 무슨 일을 하는지 골라 보세요!",
                "cloze_sentences": [
                    "• 1단계: ‘이 동물은’ = 앞 문장의 ( {b1} )를 가리킵니다.",
                    "• 2단계: 길쭉한 [코] = 손처럼 물을 마시고 ( {b2} )를 집어 먹습니다.",
                    "• 3단계: 넓적한 [귀] = 부채처럼 흔들어 ( {b3} )을 시원하게 식히고, [네 다리] = 무거운 몸을 받쳐 줍니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "코끼리", "options": ["코끼리", "기둥", "부채"]},
                    {"id": "b2", "correct": "먹이", "options": ["먹이", "바람", "기둥"]},
                    {"id": "b3", "correct": "더운 몸", "options": ["더운 몸", "먹이", "발바닥"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D4(부위-역할 뒤바꾸기 함정) 참/거짓 판별하기",
                "desc": "수능형 문제에서는 ‘코가 하는 일’과 ‘귀가 하는 일’을 슬쩍 바꾸어 놓아요! 속지 않고 찾아내 볼까요?",
                "items": [
                    {
                        "statement": "코끼리는 넓적한 귀로 먹이를 집어 먹고, 길쭉한 코로 더운 몸을 식힙니다.",
                        "answer": "X",
                        "reason": "삐뽀삐뽀! [D4 부위-역할 교차 함정]이에요! 먹이를 집는 것은 ‘코’이고, 더운 몸을 식히는 것은 ‘귀’예요.",
                    },
                    {
                        "statement": "굵은 기둥 같은 네 다리는 코끼리의 무거운 몸을 튼튼하게 받쳐 줍니다.",
                        "answer": "O",
                        "reason": "딩동댕! 마지막 문장에 나온 ‘다리’의 역할과 정확히 일치해요!",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 지시어 & 부분-역할 연결)",
            "situation": "아이와 함께 식탁 위 도구(숟가락, 젓가락, 포크)나 동물 그림책을 볼 때",
            "parent_question": "“도윤아, 코끼리는 귀가 아주 넓적하대. 이 동물은 왜 큰 귀를 부채처럼 팔랑거릴까? 코가 하는 일이랑 어떻게 다를까?”",
            "expected_answer": "“이 동물은 코끼리야! 코로는 물이랑 먹이를 집어 먹고, 넓적한 귀는 부채처럼 흔들어서 더운 몸을 시원하게 식혀 줘!”",
            "coaching_tip": "아이가 ‘코’와 ‘귀’의 역할을 섞지 않고 [무엇은 ~을 합니다]로 주어를 붙여 한 문장으로 끝까지 말하면 크게 칭찬해 주세요.",
        },
    ),

    # -------------------------------------------------------------------------
    # 3차시: G1-EXP-V1-3 (보글보글 깨끗하게 손 씻는 순서)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V1-3",
        subject="통합교과(하루·안전 1-1)",
        unit="건강하고 안전한 하루 - 올바른 손 씻기",
        concept="손바닥➔손등➔손가락 사이 씻기 3~4단계 순서",
        text_structure="순서·과정",
        structure_type_code="sequence",
        passage_title="보글보글 깨끗하게 손 씻는 순서",
        paragraphs=[
            "밖에서 놀고 돌아오면 비누로 손을 깨끗하게 씻어야 합니다. 먼저 흐르는 물에 손을 적시고 비누 거품을 보글보글 냅니다. 다음에 손바닥과 손등을 마주 대고 골고루 문지릅니다. 마지막으로 손가락 사이까지 닦은 뒤 맑은 물로 깨끗이 헹구어 냅니다."
        ],
        vocab_notes=[
            {"word": "적시다", "tier": "Tier 1 (기초)", "desc": "물기가 스며들게 하여 축축하게 만들다"},
            {"word": "골고루", "tier": "Tier 1 (기초)", "desc": "빠진 곳이 없이 한결같이 고르게"},
            {"word": "헹구다", "tier": "Tier 2 (사고어)", "desc": "비누 거품이나 더러운 것을 맑은 물에 씻어 내다"},
        ],
        visual_html="""
        <div style="background:#EFF6FF; border:2px solid #93C5FD; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#1E3A8A; margin-bottom:10px;">🧼 [단계 그림 자료] 보글보글 손 씻기 3단계 순서 기차</div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #60A5FA;">
              <div style="font-size:1.2rem;">① <b>먼저</b></div>
              <div style="font-size:0.85rem; color:#1E40AF; margin-top:4px;">물에 손 적시고<br><b>비누 거품</b> 내기</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #3B82F6;">
              <div style="font-size:1.2rem;">② <b>다음에</b></div>
              <div style="font-size:0.85rem; color:#1E40AF; margin-top:4px;"><b>손바닥과 손등</b><br>골고루 문지르기</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #2563EB;">
              <div style="font-size:1.2rem;">③ <b>마지막으로</b></div>
              <div style="font-size:0.85rem; color:#1E40AF; margin-top:4px;"><b>손가락 사이</b> 닦고<br>맑은 물로 헹구기</div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v1-3-c1", "text": "먼저", "role": "1단계 순서 표지: 물 적시고 비누 거품 내기", "para_idx": 0},
            {"cue_id": "g1-v1-3-c2", "text": "다음에", "role": "2단계 순서 표지: 손바닥과 손등 문지르기", "para_idx": 0},
            {"cue_id": "g1-v1-3-c3", "text": "마지막으로", "role": "3단계 순서 표지: 손가락 사이 닦고 물로 헹구기", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 순서·과정 구조도] 깨끗하게 손 씻는 3단계 차례 배열하기",
            "instruction": "순서 신호등(먼저 ➔ 다음에 ➔ 마지막으로)에 맞게 손 씻는 과정 카드를 배치하세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "① 먼저", "sub": "첫 번째 단계", "correct": "물에 손을 적시고 비누 거품을 보글보글 냄"},
                {"slot_id": "slot-2", "header": "② 다음에", "sub": "두 번째 단계", "correct": "손바닥과 손등을 마주 대고 골고루 문지름"},
                {"slot_id": "slot-3", "header": "③ 마지막으로", "sub": "세 번째 단계", "correct": "손가락 사이까지 닦은 뒤 맑은 물로 헹구어 냄"},
            ],
            "word_bank": [
                "물에 손을 적시고 비누 거품을 보글보글 냄",
                "손바닥과 손등을 마주 대고 골고루 문지름",
                "손가락 사이까지 닦은 뒤 맑은 물로 헹구어 냄",
                "비누를 묻힌 채로 수건에 바로 닦음 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V1-3 (순서·과정 텍스트 구조 확인 - 3지선다)",
                "stem": "윗글에 나온 ‘손을 씻는 순서’로 <u>알맞게</u> 연결된 것은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "먼저 흐르는 물에 손을 적시고 비누 거품을 보글보글 냅니다.",
                "step1_hint": "잠깐! 본문에서 ‘먼저’, ‘다음에’, ‘마지막으로’ 뒤에 나오는 행동을 차례대로 찾아보세요!",
                "step2_hint": "①비누 거품 내기 ➔ ②손바닥·손등 문지르기 ➔ ③손가락 사이 닦고 헹구기 순서인 것을 고르세요!",
                "options": [
                    {
                        "no": 1,
                        "text": "비누 거품 내기 ➔ 손바닥과 손등 문지르기 ➔ 손가락 사이 닦고 물로 헹구기",
                        "is_correct": True,
                        "formula": "정답 공식: [먼저(거품 내기) ➔ 다음에(손바닥·손등) ➔ 마지막으로(손가락 사이·헹구기) 순서 일치]",
                        "explanation": "🎉 **[정답]** ‘먼저 - 다음에 - 마지막으로’ 순서에 따라 손 씻는 3단계가 정확하게 배열되었어요!",
                    },
                    {
                        "no": 2,
                        "text": "손바닥과 손등 문지르기 ➔ 맑은 물로 헹구기 ➔ 비누 거품 내기",
                        "is_correct": False,
                        "formula": "오답 공식 [D2 단계 순서 뒤섞기]: 1단계인 '비누 거품 내기'를 맨 뒤로 배치",
                        "explanation": "❌ **[D2 순서 뒤바뀜 함정]** 비누 거품을 내는 것은 맨 마지막이 아니라 **제일 먼저** 해야 하는 일이에요!",
                    },
                    {
                        "no": 3,
                        "text": "맑은 물로 헹구기 ➔ 비누 거품 내기 ➔ 손가락 사이 닦기",
                        "is_correct": False,
                        "formula": "오답 공식 [D2 역순 배열]: 마지막 단계인 '맑은 물로 헹구기'를 맨 앞에 배치",
                        "explanation": "❌ **[D2 순서 뒤바뀜 함정]** 맑은 물로 거품을 헹구어 내는 것은 **마지막** 단계예요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V1-3 (<보기> 단계 그림 배열 확인형 - 3지선다)",
                "stem": "윗글을 읽고 <보기>의 ‘다음에’ 단계에서 해야 할 행동을 고르세요.",
                "bogi": "<보기>\n  [손 씻기 안내판]\n  • 먼저: 흐르는 물에 손을 적시고 비누 거품을 냅니다.\n  • 다음에: (                                        )\n  • 마지막으로: 손가락 사이까지 닦고 맑은 물로 헹굽니다.",
                "target_para_idx": 0,
                "spotlight_quote": "다음에 손바닥과 손등을 마주 대고 골고루 문지릅니다.",
                "step1_hint": "잠깐! 본문 세 번째 문장에서 ‘다음에’ 바로 뒤에 무엇을 문지른다고 했는지 확인해 보세요!",
                "step2_hint": "‘손바닥과 손등을 마주 대고 골고루 문지릅니다’와 똑같은 내용을 찾으면 정답이에요!",
                "options": [
                    {
                        "no": 1,
                        "text": "밖으로 나가서 모래놀이를 시작합니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 무관한 행동]: 손 씻기 과정과 관련 없는 놀이 행동 삽입",
                        "explanation": "❌ **[D6 글에 없는 내용 함정]** 손을 씻는 도중에 모래놀이를 나간다는 내용은 없어요.",
                    },
                    {
                        "no": 2,
                        "text": "손바닥과 손등을 마주 대고 골고루 문지릅니다.",
                        "is_correct": True,
                        "formula": "정답 공식: ['다음에' 표지 뒤의 2단계 행동 정확 일치]",
                        "explanation": "🎉 **[정답]** 비누 거품을 낸 ‘다음에’ 할 일은 손바닥과 손등을 마주 대고 골고루 문지르는 것이에요!",
                    },
                    {
                        "no": 3,
                        "text": "비누 거품을 헹구지 않고 그대로 말립니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 사실 반대]: 맑은 물로 헹구어 낸다는 본문 내용과 반대",
                        "explanation": "❌ **[D1 반대 말 함정]** 비누 거품은 마지막에 맑은 물로 깨끗이 헹구어 내야 해요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 단계 확인 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 비누 거품을 맑은 물로 헹구어 내기 바로 직전에 어느 부위까지 꼼꼼히 닦아야 하나요?",
            "part_a_options": [
                {"no": 1, "text": "손가락 사이까지 꼼꼼히 닦아야 합니다.", "is_correct": True},
                {"no": 2, "text": "발가락 사이까지 비누로 닦아야 합니다.", "is_correct": False},
                {"no": 3, "text": "머리카락 끝까지 비누로 닦아야 합니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 알려 주는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “밖에서 놀고 돌아오면 비누로 손을 깨끗하게 씻어야 합니다.”", "is_correct": False},
                {"no": 2, "text": "둘째 문장: “먼저 흐르는 물에 손을 적시고 비누 거품을 보글보글 냅니다.”", "is_correct": False},
                {"no": 3, "text": "넷째 문장: “마지막으로 손가락 사이까지 닦은 뒤 맑은 물로 깨끗이 헹구어 냅니다.”", "is_correct": True},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 마지막 단계에서 ‘손가락 사이’(Part A)까지 닦은 뒤 물로 헹군다는 사실이 넷째 문장(Part B)에 나와 있어요!",
        },
        writing_workbench={
            "mode": "outline_order",
            "code": "G1-EXP-W3",
            "title": "[TEI-6 작문 워크벤치] ‘양치질하는 순서’ 3단계 문장 배열하기",
            "conditions": [
                "조건 ①: ‘먼저 ➔ 다음에 ➔ 마지막으로’ 순서 말이 차례대로 이어질 것",
                "조건 ②: [치약 짜기 ➔ 이 닦기 ➔ 물로 입 헹구기] 순서에 맞을 것",
            ],
            "draft_prefix": "밥을 먹고 난 뒤에 바르게 양치질하는 순서를 알아봅시다.",
            "choices": [
                {
                    "id": "w-1",
                    "text": "① 먼저 칫솔에 치약을 알맞게 짭니다. ➔ ② 다음에 치아와 잇몸을 구석구석 닦습니다. ➔ ③ 마지막으로 맑은 물로 입안을 깨끗이 헹굽니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 참 잘했어요! ‘먼저-다음에-마지막으로’ 순서에 맞게 양치질 과정이 차례대로 연결되었어요.",
                },
                {
                    "id": "w-2",
                    "text": "① 먼저 물로 입안을 헹굽니다. ➔ ② 다음에 치약을 짭니다. ➔ ③ 마지막으로 이를 닦고 그냥 잡니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 이를 닦기도 전에 입을 먼저 헹구고, 마지막에 거품을 헹구지 않아서 순서가 뒤섞였어요.",
                },
                {
                    "id": "w-3",
                    "text": "칫솔은 색깔이 예뻐서 내가 정말 좋아하는 물건입니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 순서를 알려 주는 말이 없고, 양치질하는 차례도 설명하지 않았어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V1-3 맞춤 처방전: [순서 신호등(먼저·다음에·마지막으로) 네모 치기 ➔ 단계 기차 연결 ➔ D2 순서 백신]",
            "rx_reason": "일을 하는 차례가 담긴 안내글에서 순서를 나타내는 표지어를 찾아 번호(①·②·③)를 매기며 읽는 습관을 길러 줍니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A4 순서를 나타내는 말 찾기",
                "rule_box": "💡 **순서 신호등 공식**: 문장 맨 앞의 **‘먼저(①) - 다음에(②) - 마지막으로(③)’**에 네모 표시를 하면 순서가 절대 헷갈리지 않아요!",
                "mini_question": "세 가지 순서 말 ‘먼저, 다음에, 마지막으로’ 가운데 **맨 처음(①번)**에 오는 말은 무엇인가요?",
                "choices": ["먼저", "마지막으로"],
                "correct": "먼저",
                "feedback": "딩동댕! ‘먼저’가 1번, ‘다음에’가 2번, ‘마지막으로’가 3번이에요.",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V1-3 손 씻기 3단계 순서 빈칸 채우기",
                "passage_snippet": "<span class='rx-cue'>먼저</span> 흐르는 물에 손을 적시고 비누 거품을 보글보글 냅니다. <span class='rx-cue'>다음에</span> 손바닥과 손등을 마주 대고 골고루 문지릅니다. <span class='rx-cue'>마지막으로</span> 손가락 사이까지 닦은 뒤 맑은 물로 깨끗이 헹구어 냅니다.",
                "think_aloud_prompt": "순서 신호등 낱말 뒤의 행동을 보고 빈칸을 차례대로 채워 보세요!",
                "cloze_sentences": [
                    "• ① 먼저: 물에 손을 적시고 ( {b1} )을 보글보글 냅니다.",
                    "• ② 다음에: ( {b2} )을 마주 대고 골고루 문지릅니다.",
                    "• ③ 마지막으로: 손가락 사이까지 닦고 ( {b3} )로 깨끗이 헹구어 냅니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "비누 거품", "options": ["비누 거품", "흙먼지", "물감"]},
                    {"id": "b2", "correct": "손바닥과 손등", "options": ["손바닥과 손등", "이마와 코", "무릎과 발등"]},
                    {"id": "b3", "correct": "맑은 물", "options": ["맑은 물", "비누 거품", "뜨거운 바람"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D2(단계 순서 뒤바꾸기) OX 판별",
                "desc": "수능형 문제에서는 1단계와 3단계 순서를 슬쩍 바꾸어 놓아요! 바른 순서인지 확인해 보세요.",
                "items": [
                    {
                        "statement": "손을 씻을 때는 먼저 비누 거품을 내고, 다음에 손바닥과 손등을 문지릅니다.",
                        "answer": "O",
                        "reason": "딩동댕! 1단계(비누 거품 내기) ➔ 2단계(손바닥·손등 문지르기) 순서가 정확해요!",
                    },
                    {
                        "statement": "맑은 물로 먼저 손을 다 헹구고 난 뒤, 마지막으로 비누 거품을 냅니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D2 순서 역전 함정]이에요! 비누 거품을 먼저 내고, 맑은 물로 헹구는 것은 마지막에 해야 해요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 순서 말 ‘먼저·다음에·마지막으로’ 쓰기)",
            "situation": "외출 후 돌아와 아이와 함께 화장실에서 손을 씻거나 양치질을 할 때",
            "parent_question": "“우리 오늘 배운 ‘먼저 - 다음에 - 마지막으로’ 세 단어를 넣어서 손 씻는 순서를 엄마한테 선생님처럼 알려 줄래?”",
            "expected_answer": "“먼저 물에 손을 적셔서 비누 거품을 내고, 다음에 손바닥이랑 손등을 문질러! 마지막으로 손가락 사이까지 닦고 맑은 물로 헹구면 끝!”",
            "coaching_tip": "아이가 세 단계를 말할 때 손가락으로 ①, ②, ③을 표시해 주면 글의 구조(순서 짜임) 감각이 쑥쑥 자라납니다.",
        },
    ),

    # -------------------------------------------------------------------------
    # 4차시: G1-EXP-V1-4 (우리를 도와주는 세 가지 소방차)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V1-4",
        subject="통합교과(동네·안전 1-2)",
        unit="우리 동네 안전 지킴이 - 소방서와 소방차",
        concept="펌프차·사다리차·구급차의 역할과 중심 내용 간추리기",
        text_structure="열거·분류 기초",
        structure_type_code="classification",
        passage_title="우리를 도와주는 세 가지 소방차",
        paragraphs=[
            "소방서에는 위험에 빠진 사람들을 도와주는 여러 가지 소방차가 있습니다. 펌프차는 긴 호스로 시원한 물줄기를 뿜어내어 불을 끕니다. 사다리차는 아주 긴 사다리를 높이 뻗어 높은 건물에 갇힌 사람을 구합니다. 구급차는 다치거나 아픈 사람을 병원까지 빠르게 데려다줍니다."
        ],
        vocab_notes=[
            {"word": "뿜어내다", "tier": "Tier 1 (기초)", "desc": "물이나 김 따위를 안쪽에서 밖으로 세차게 밀어내다"},
            {"word": "사다리", "tier": "Tier 1 (기초)", "desc": "높은 곳에 오르내릴 때 발을 디딜 수 있게 만든 도구"},
            {"word": "구급차", "tier": "Tier 3 (교과어)", "desc": "갑자기 아프거나 다친 환자를 병원으로 급히 옮기는 차"},
        ],
        visual_html="""
        <div style="background:#FEF2F2; border:2px solid #FCA5A5; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#991B1B; margin-bottom:10px;">🚒 [분류 사진 카드] 우리를 도와주는 소방차 3총사</div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #EF4444;">
              <div style="font-size:1.25rem;">🚒 <b>펌프차</b></div>
              <div style="font-size:0.85rem; color:#991B1B; margin-top:4px;">긴 호스로 물줄기를 뿜어<br><b>불을 끔</b></div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #F97316;">
              <div style="font-size:1.25rem;">🪜 <b>사다리차</b></div>
              <div style="font-size:0.85rem; color:#9A3412; margin-top:4px;">긴 사다리를 높이 뻗어<br><b>높은 곳 사람 구조</b></div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #10B981;">
              <div style="font-size:1.25rem;">🚑 <b>구급차</b></div>
              <div style="font-size:0.85rem; color:#065F46; margin-top:4px;">다치거나 아픈 사람을<br><b>병원으로 옮김</b></div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v1-4-c1", "text": "여러 가지 소방차", "role": "글 전체의 중심 낱말(대표 상위어)", "para_idx": 0},
            {"cue_id": "g1-v1-4-c2", "text": "펌프차", "role": "세부 종류 ①: 물줄기로 불을 끄는 소방차", "para_idx": 0},
            {"cue_id": "g1-v1-4-c3", "text": "사다리차", "role": "세부 종류 ②: 높은 건물 사람을 구하는 소방차", "para_idx": 0},
            {"cue_id": "g1-v1-4-c4", "text": "구급차", "role": "세부 종류 ③: 아픈 사람을 병원으로 옮기는 소방차", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 중심-세부 분류 구조도] 세 가지 소방차와 하는 일 정리하기",
            "instruction": "글 전체를 대표하는 중심 문장과 각 소방차가 하는 일을 빈칸에 알맞게 넣으세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "🌟 글의 중심 생각", "sub": "첫째 문장(대표 문장)", "correct": "위험에 빠진 사람을 돕는 여러 가지 소방차"},
                {"slot_id": "slot-2", "header": "🚒 펌프차", "sub": "불이 났을 때", "correct": "긴 호스로 물줄기를 뿜어 불을 끔"},
                {"slot_id": "slot-3", "header": "🪜 사다리차 & 🚑 구급차", "sub": "구조와 병원 이동", "correct": "높은 곳 사람을 구하고 아픈 사람을 병원에 데려다줌"},
            ],
            "word_bank": [
                "위험에 빠진 사람을 돕는 여러 가지 소방차",
                "긴 호스로 물줄기를 뿜어 불을 끔",
                "높은 곳 사람을 구하고 아픈 사람을 병원에 데려다줌",
                "편지와 소포를 집으로 배달해 줌 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V1-4 (글 전체의 대표 중심 문장 찾기 - 3지선다)",
                "stem": "윗글 전체의 중심 내용을 가장 잘 나타내 주는 ‘대표 문장’은 어느 것인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "소방서에는 위험에 빠진 사람들을 도와주는 여러 가지 소방차가 있습니다.",
                "step1_hint": "잠깐! 펌프차, 사다리차, 구급차 세 가지를 모두 아우르는 문장이 몇 번째 문장인지 살펴보세요!",
                "step2_hint": "한 가지 차만 말한 문장(D5 함정)을 빼고, ‘여러 가지 소방차’를 모두 감싸는 첫째 문장을 고르세요!",
                "options": [
                    {
                        "no": 1,
                        "text": "소방서에는 위험에 빠진 사람들을 도와주는 여러 가지 소방차가 있습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [펌프차·사다리차·구급차를 모두 포괄하는 첫 문장(중심문장) 선택]",
                        "explanation": "🎉 **[정답]** 첫째 문장이 펌프차, 사다리차, 구급차 세 가지 이야기를 모두 묶어 주는 **대표 중심 문장**이에요!",
                    },
                    {
                        "no": 2,
                        "text": "펌프차는 긴 호스로 시원한 물줄기를 뿜어내어 불을 끕니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D5 지엽적 세부사항을 전체 주제로 과장]: 펌프차 1종만 설명한 뒷받침 문장",
                        "explanation": "❌ **[D5 부분·전체 혼동 함정]** 이 문장은 ‘펌프차’ 한 가지만 설명하고 있어서 사다리차와 구급차 내용을 담지 못해요.",
                    },
                    {
                        "no": 3,
                        "text": "구급차는 다치거나 아픈 사람을 병원까지 빠르게 데려다줍니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D5 지엽적 세부사항]: 구급차 1종만 설명한 뒷받침 문장",
                        "explanation": "❌ **[D5 부분·전체 혼동 함정]** 이 문장도 ‘구급차’ 한 가지만 설명하는 세부 문장이에요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V1-4 (중심 낱말 기반 제목 붙이기 - 3지선다)",
                "stem": "윗글의 중심 낱말을 넣어 글의 제목을 지을 때 <보기>의 빈칸에 가장 알맞은 것은 무엇인가요?",
                "bogi": "<보기>\n  [내가 지은 제목]: 불을 끄고 사람을 구하는 고마운 (          )",
                "target_para_idx": 0,
                "spotlight_quote": "소방서에는 위험에 빠진 사람들을 도와주는 여러 가지 소방차가 있습니다.",
                "step1_hint": "잠깐! 펌프차, 사다리차, 구급차를 하나로 묶어 부르는 중심 낱말이 무엇인지 첫 문장에서 찾아보세요!",
                "step2_hint": "세 가지 차를 모두 포함하는 낱말인 ‘소방차’를 넣으면 멋진 제목이 완성돼요!",
                "options": [
                    {
                        "no": 1,
                        "text": "경찰차",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 글에 없는 대상]: 본문에 등장하지 않는 경찰차 제시",
                        "explanation": "❌ **[D6 글에 없는 내용 함정]** 이 글은 경찰차가 아니라 소방서에서 일하는 차들을 설명하고 있어요.",
                    },
                    {
                        "no": 2,
                        "text": "소방차",
                        "is_correct": True,
                        "formula": "정답 공식: [글 전체의 상위 중심 낱말 '소방차' 정확 도출]",
                        "explanation": "🎉 **[정답]** 펌프차, 사다리차, 구급차를 모두 포함하는 중심 낱말은 **소방차**예요!",
                    },
                    {
                        "no": 3,
                        "text": "사다리",
                        "is_correct": False,
                        "formula": "오답 공식 [D5 부분 어휘 선택]: 사다리차의 일부 도구만 제목으로 선택",
                        "explanation": "❌ **[D5 부분·전체 혼동 함정]** ‘사다리’만 넣으면 물로 불을 끄는 펌프차와 구급차를 나타낼 수 없어요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 종류별 역할 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 높은 건물에 갇힌 사람을 구출할 때 출동하는 소방차는 무엇인가요?",
            "part_a_options": [
                {"no": 1, "text": "긴 사다리를 높이 뻗는 ‘사다리차’입니다.", "is_correct": True},
                {"no": 2, "text": "물줄기를 뿜어내는 ‘펌프차’입니다.", "is_correct": False},
                {"no": 3, "text": "아픈 사람을 병원으로 옮기는 ‘구급차’입니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 뒷받침하는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "둘째 문장: “펌프차는 긴 호스로 시원한 물줄기를 뿜어내어 불을 끕니다.”", "is_correct": False},
                {"no": 2, "text": "셋째 문장: “사다리차는 아주 긴 사다리를 높이 뻗어 높은 건물에 갇힌 사람을 구합니다.”", "is_correct": True},
                {"no": 3, "text": "넷째 문장: “구급차는 다치거나 아픈 사람을 병원까지 빠르게 데려다줍니다.”", "is_correct": False},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 높은 건물에 갇힌 사람을 구하는 차는 ‘사다리차’(Part A)이며, 셋째 문장(Part B)에 정확히 설명되어 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W1",
            "title": "[TEI-6 작문 워크벤치] 글 전체를 대표하는 ‘제목’과 ‘첫 문장’ 만들기",
            "conditions": [
                "조건 ①: 중심 낱말인 ‘소방차’가 반드시 들어갈 것",
                "조건 ②: 세 가지 차(펌프차·사다리차·구급차)를 모두 감싸는 대표 문장일 것",
            ],
            "draft_prefix": "[글의 시작 문장 고르기]",
            "choices": [
                {
                    "id": "w-1",
                    "text": "우리를 도와주는 고마운 소방차에는 여러 가지 종류가 있습니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 최고예요! 중심 낱말 ‘소방차’가 들어 있고, 뒤에 이어질 세 가지 소방차 이야기를 멋지게 대표해요.",
                },
                {
                    "id": "w-2",
                    "text": "구급차는 삐뽀삐뽀 소리를 내며 달립니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ ‘소방차’라는 중심 낱말이 빠졌고, 구급차 한 가지만 설명하고 있어요.",
                },
                {
                    "id": "w-3",
                    "text": "나는 장난감 자동차를 가지고 노는 것이 제일 재미있습니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 소방차의 종류를 설명하는 글인데 장난감 놀이 이야기를 썼어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V1-4 맞춤 처방전: [중심 낱말 찾기 ➔ 대표 문장 골라내기 ➔ D5 부분·전체 함정 백신]",
            "rx_reason": "여러 대상을 나열한 설명글에서 한 가지 세부 대상만 보고 제목을 짓는 실수(D5)를 막고, 모두를 감싸는 대표 낱말을 찾는 힘을 기릅니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A6 세 낱말을 하나로 묶어 부르는 대표 낱말 찾기",
                "rule_box": "💡 **큰 우산 공식**: ‘펌프차, 사다리차, 구급차’를 한 우산 아래 모두 넣을 수 있는 **큰 이름(소방차)**이 바로 중심 낱말이에요!",
                "mini_question": "‘사과, 바나나, 포도’를 하나로 묶어 부르는 대표 낱말은 무엇인가요?",
                "choices": ["과일", "장난감"],
                "correct": "과일",
                "feedback": "딩동댕! 사과, 바나나, 포도는 모두 ‘과일’이라는 큰 우산 안에 들어가요!",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V1-4 소방차 3총사의 대표 문장과 역할 간추리기",
                "passage_snippet": "소방서에는 위험에 빠진 사람들을 도와주는 <span class='rx-cue'>여러 가지 소방차</span>가 있습니다. <span class='rx-cue'>펌프차</span>는 물줄기로 불을 끕니다. <span class='rx-cue'>사다리차</span>는 높은 곳의 사람을 구하고, <span class='rx-cue'>구급차</span>는 아픈 사람을 병원으로 데려다줍니다.",
                "think_aloud_prompt": "큰 우산(대표 문장)과 작은 우산(세부 소방차)을 구별하여 빈칸을 채워 보세요!",
                "cloze_sentences": [
                    "• 1단계(대표 중심 낱말): 이 글 전체가 설명하는 중심 대상은 여러 가지 ( {b1} )입니다.",
                    "• 2단계(세부 1·2): 불을 끄는 ( {b2} )와 높은 곳 사람을 구하는 사다리차가 있습니다.",
                    "• 3단계(세부 3): 다치거나 아픈 사람을 병원으로 옮기는 ( {b3} )도 있습니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "소방차", "options": ["소방차", "비행기", "자전거"]},
                    {"id": "b2", "correct": "펌프차", "options": ["펌프차", "구급차", "기차"]},
                    {"id": "b3", "correct": "구급차", "options": ["구급차", "펌프차", "사다리차"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D5(부분을 전체 제목으로 착각) OX 판별",
                "desc": "수능형 제목 문제에서는 한 문장에만 나온 작은 낱말을 제목처럼 꾸며 놓아요! 속지 않고 가려내 볼까요?",
                "items": [
                    {
                        "statement": "윗글 전체에 가장 잘 어울리는 제목은 ‘우리를 도와주는 여러 가지 소방차’입니다.",
                        "answer": "O",
                        "reason": "딩동댕! 펌프차, 사다리차, 구급차를 모두 감싸는 완벽한 제목이에요!",
                    },
                    {
                        "statement": "윗글은 구급차에 대해서만 설명하고 있으므로 제목을 ‘빠르게 달리는 구급차’로 지어야 합니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D5 부분·전체 혼동 함정]이에요! 펌프차와 사다리차 이야기도 있으므로 ‘구급차’만 제목으로 쓰면 안 돼요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 중심 낱말 찾기와 제목 짓기)",
            "situation": "길에서 소방차나 구급차를 보거나 장난감 자동차 놀이를 할 때",
            "parent_question": "“소방서에는 불을 끄는 펌프차, 높은 곳 사람을 구하는 사다리차, 아픈 사람을 옮기는 구급차가 있대! 이 세 가지 차를 하나로 묶어서 부르면 무슨 차라고 할까?”",
            "expected_answer": "“세 가지 모두 우리를 도와주는 ‘소방차’야! 그래서 글의 제목도 ‘우리를 도와주는 세 가지 소방차’라고 지으면 돼!”",
            "coaching_tip": "아이가 세부 이름(펌프차, 구급차)과 전체 대표 이름(소방차)을 구분해 말하면 ‘중심 생각 찾기 박사님!’이라고 칭찬해 주세요.",
        },
    ),

    # -------------------------------------------------------------------------
    # 5차시: G1-EXP-V2-1 (몸 색깔을 숨기는 카멜레온의 ‘보호색’)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V2-1",
        subject="통합교과(자연 1-2)",
        unit="자연의 신비 - 몸을 숨기는 동물들",
        concept="나뭇잎 색과 비슷하게 변하는 보호색의 뜻 추론",
        text_structure="기술·예시",
        structure_type_code="analysis",
        passage_title="몸 색깔을 숨기는 카멜레온의 ‘보호색’",
        paragraphs=[
            "카멜레온은 주변 색깔에 맞추어 몸 색깔을 감쪽같이 바꾸는 동물입니다. 초록색 나뭇잎 위에 있을 때는 몸을 초록색으로 바꾸고, 갈색 나무줄기 위에서는 갈색으로 바꿉니다. 이처럼 주변 색깔과 비슷하게 변해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색을 ‘보호색’이라고 부릅니다. 카멜레온은 보호색 덕분에 무서운 새나 뱀에게 들키지 않고 안전하게 숨을 수 있습니다."
        ],
        vocab_notes=[
            {"word": "감쪽같이", "tier": "Tier 2 (사고어)", "desc": "전혀 눈치채지 못할 만큼 아주 깜쪽같이"},
            {"word": "보호색", "tier": "Tier 3 (교과어)", "desc": "주변 색깔과 비슷해서 적의 눈에 띄지 않게 몸을 지켜 주는 색"},
            {"word": "들키다", "tier": "Tier 1 (기초)", "desc": "숨기거나 몰래 하던 일이 남의 눈에 띄다"},
        ],
        visual_html="""
        <div style="background:#F0FDF4; border:2px solid #86EFAC; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#166534; margin-bottom:10px;">🦎 [그림 단서 카드] 카멜레온의 ‘보호색’ 변신 모습</div>
          <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px; text-align:center;">
            <div style="background:#DCFCE7; padding:10px; border-radius:8px; border:2px solid #22C55E;">
              <div style="font-size:1.2rem;">🍃 <b>초록 나뭇잎 위</b></div>
              <div style="font-size:0.85rem; color:#14532D; margin-top:4px;">몸을 <b>초록색</b>으로 변신!<br>(나뭇잎과 똑같아 안 보여요)</div>
            </div>
            <div style="background:#FEF3C7; padding:10px; border-radius:8px; border:2px solid #D97706;">
              <div style="font-size:1.2rem;">🪵 <b>갈색 나무줄기 위</b></div>
              <div style="font-size:0.85rem; color:#78350F; margin-top:4px;">몸을 <b>갈색</b>으로 변신!<br>(나무줄기와 똑같아 안 보여요)</div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v2-1-c1", "text": "주변 색깔에 맞추어 몸 색깔을 감쪽같이 바꾸는", "role": "앞 문맥 단서: 카멜레온의 변신 능력", "para_idx": 0},
            {"cue_id": "g1-v2-1-c2", "text": "주변 색깔과 비슷하게 변해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색", "role": "‘보호색’의 뜻풀이 단서 문장", "para_idx": 0},
            {"cue_id": "g1-v2-1-c3", "text": "보호색", "role": "목표 추론 어휘: 몸을 보호하는 색깔", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 어휘 문맥 추론 도해] 앞뒤 설명과 그림으로 ‘보호색’ 뜻 짐작하기",
            "instruction": "본문의 예시와 설명 단서를 연결하여 ‘보호색’의 뜻과 효과를 완성하세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "🍃 예시 단서", "sub": "나뭇잎·나무줄기 위에서", "correct": "초록 나뭇잎에서는 초록색, 갈색 줄기에서는 갈색으로 변함"},
                {"slot_id": "slot-2", "header": "💡 ‘보호색’의 뜻", "sub": "셋째 문장 뜻풀이 단서", "correct": "주변 색깔과 비슷해 적의 눈에 띄지 않게 몸을 지켜 주는 색"},
                {"slot_id": "slot-3", "header": "🛡️ 보호색의 효과", "sub": "넷째 문장 결과", "correct": "무서운 새나 뱀에게 들키지 않고 안전하게 숨음"},
            ],
            "word_bank": [
                "초록 나뭇잎에서는 초록색, 갈색 줄기에서는 갈색으로 변함",
                "주변 색깔과 비슷해 적의 눈에 띄지 않게 몸을 지켜 주는 색",
                "무서운 새나 뱀에게 들키지 않고 안전하게 숨음",
                "적의 눈에 잘 띄도록 반짝반짝 빛나는 색 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V2-1 (문맥 단서를 활용한 어휘 의미 추론 - 3지선다)",
                "stem": "윗글과 그림을 보고 짐작한 ‘보호색’의 뜻으로 가장 <u>알맞은</u> 것은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "이처럼 주변 색깔과 비슷하게 변해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색을 ‘보호색’이라고 부릅니다.",
                "step1_hint": "잠깐! 세 번째 문장에서 ‘보호색이라고 부릅니다’ 바로 앞에 어떤 설명이 적혀 있는지 노란색 문장을 읽어 보세요!",
                "step2_hint": "‘주변 색깔과 비슷하게 변해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색’과 뜻이 같은 선지를 고르세요!",
                "options": [
                    {
                        "no": 1,
                        "text": "주변 색깔과 비슷해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색",
                        "is_correct": True,
                        "formula": "정답 공식: [3문장 앞쪽 문맥 정의 단서와 1:1 일치]",
                        "explanation": "🎉 **[정답]** 바로 앞 설명 단서(“주변 색깔과 비슷하게 변해서 적의 눈에 잘 띄지 않게 몸을 지켜 주는 색”)를 연결해 ‘보호색’의 뜻을 정확히 찾았어요!",
                    },
                    {
                        "no": 2,
                        "text": "멀리 있는 친구의 눈에 아주 잘 띄도록 알록달록하게 빛나는 색",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 반대 의미 함정]: '눈에 잘 띄지 않게'를 '눈에 아주 잘 띄도록'으로 반전",
                        "explanation": "❌ **[D1 반대 말 함정]** 보호색은 눈에 잘 띄게 하는 색이 아니라 **적의 눈에 잘 띄지 않게 숨겨 주는 색**이에요.",
                    },
                    {
                        "no": 3,
                        "text": "도화지에 예쁜 그림을 그릴 때 쓰는 물감과 크레파스의 색",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 무관한 일상 상식]: '색'이라는 글자만 보고 미술 도구로 오해",
                        "explanation": "❌ **[D6 글에 없는 상식 함정]** 본문은 미술 시간이 아니라 동물이 몸을 지키는 자연의 색깔을 설명하고 있어요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V2-1 (<보기> 다른 동물의 보호색 사례 적용형 - 3지선다)",
                "stem": "윗글에서 배운 ‘보호색’의 뜻에 맞게 <보기>의 빈칸에 들어갈 알맞은 말을 고르세요.",
                "bogi": "<보기>\n  하얀 눈이 가득 쌓인 북극에 사는 북극곰은 털 색깔이 새하얗습니다. 그래서 하얀 눈밭에 숨으면 (                              ).",
                "target_para_idx": 0,
                "spotlight_quote": "카멜레온은 보호색 덕분에 무서운 새나 뱀에게 들키지 않고 안전하게 숨을 수 있습니다.",
                "step1_hint": "잠깐! 하얀 눈밭과 북극곰의 하얀 털 색깔이 서로 비슷할 때 어떤 일이 일어날지 네 번째 문장을 참고해 보세요!",
                "step2_hint": "주변 색깔(하얀 눈)과 몸 색깔(하얀 털)이 비슷하면 다른 동물의 눈에 잘 띄지 않아요!",
                "options": [
                    {
                        "no": 1,
                        "text": "털 색깔이 갑자기 빨간색과 파란색으로 바뀝니다",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 허위 추론]: 북극곰의 털이 빨갛고 파랗게 변한다는 거짓 진술",
                        "explanation": "❌ **[D6 사실 왜곡 함정]** 하얀 눈밭에서 빨간색이 되면 오히려 눈에 확 띄어요!",
                    },
                    {
                        "no": 2,
                        "text": "주변 눈 색깔과 비슷해서 다른 동물의 눈에 잘 띄지 않습니다",
                        "is_correct": True,
                        "formula": "정답 공식: [보호색의 핵심 원리(주변 색과 비슷해 눈에 띄지 않음)를 북극곰 사례에 적용]",
                        "explanation": "🎉 **[정답]** 하얀 눈밭과 하얀 털이 서로 비슷해서 눈에 잘 띄지 않는 것도 바로 ‘보호색’이에요!",
                    },
                    {
                        "no": 3,
                        "text": "추운 겨울이 사라지고 갑자기 더운 여름이 찾아옵니다",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 무관한 계절 변화]: 털 색깔과 계절 변화를 엉뚱하게 연결",
                        "explanation": "❌ **[D6 엉뚱한 추론 함정]** 북극곰이 눈밭에 숨는다고 계절이 여름으로 바뀌지는 않아요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 문맥 추론 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 카멜레온이 갈색 나무줄기 위로 올라가면 몸 색깔을 무슨 색으로 바꾸나요?",
            "part_a_options": [
                {"no": 1, "text": "나무줄기 색깔과 비슷한 ‘갈색’으로 바꿉니다.", "is_correct": True},
                {"no": 2, "text": "나뭇잎 색깔과 비슷한 ‘초록색’으로 바꿉니다.", "is_correct": False},
                {"no": 3, "text": "하늘 색깔과 비슷한 ‘파란색’으로 바꿉니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 알려 주는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “카멜레온은 주변 색깔에 맞추어 몸 색깔을 감쪽같이 바꾸는 동물입니다.”", "is_correct": False},
                {"no": 2, "text": "둘째 문장: “초록색 나뭇잎 위에 있을 때는 몸을 초록색으로 바꾸고, 갈색 나무줄기 위에서는 갈색으로 바꿉니다.”", "is_correct": True},
                {"no": 3, "text": "넷째 문장: “카멜레온은 보호색 덕분에 무서운 새나 뱀에게 들키지 않고 안전하게 숨을 수 있습니다.”", "is_correct": False},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 갈색 나무줄기 위에서는 ‘갈색’(Part A)으로 바꾼다는 내용이 본문 둘째 문장(Part B)에 정확히 나와 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W2",
            "title": "[TEI-6 작문 워크벤치] ‘보호색’ 낱말을 넣어 청개구리 소개 문장 쓰기",
            "conditions": [
                "조건 ①: 배운 낱말 ‘보호색’을 반드시 넣을 것",
                "조건 ②: 초록색 풀잎과 청개구리의 몸 색깔이 비슷하다는 사실이 드러날 것",
            ],
            "draft_prefix": "청개구리는 초록색 풀잎 위에 앉아 있습니다.",
            "choices": [
                {
                    "id": "w-1",
                    "text": "풀잎과 비슷한 초록색 보호색 덕분에 적의 눈에 잘 띄지 않습니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 대단해요! ‘보호색’ 낱말과 초록 풀잎에 숨는 원리를 모두 정확하게 사용했어요!",
                },
                {
                    "id": "w-2",
                    "text": "청개구리는 비가 오면 개골개골 큰 소리로 노래를 부릅니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ ‘보호색’ 낱말이 빠졌고, 몸 색깔에 대한 설명도 없어요.",
                },
                {
                    "id": "w-3",
                    "text": "보호색은 눈에 제일 잘 띄게 해 주는 반짝이는 색깔입니다.",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ ‘보호색’의 뜻을 정반대(눈에 잘 띄게 해 주는 색)로 잘못 썼어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V2-1 맞춤 처방전: [모르는 낱말 동그라미 ➔ 앞 문장 쉬운 설명 연결 ➔ D1 반대 뜻 백신]",
            "rx_reason": "처음 보는 낱말(‘보호색’)이 나와도 당황하지 않고, 바로 앞 문장의 쉬운 설명 말과 그림을 힌트로 삼아 뜻을 짐작하는 법을 익힙니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A2 앞뒤 말로 낱말 뜻 짐작하기",
                "rule_box": "💡 **문맥 탐정 공식**: 어려운 낱말 앞에는 항상 **‘이처럼 ~하는 것을 ○○이라고 부릅니다’**라는 친절한 설명 힌트가 숨어 있어요!",
                "mini_question": "“추운 겨울 동안 땅속에서 내내 잠을 자는 것을 ‘겨울잠’이라고 합니다.” — ‘겨울잠’은 언제 자는 잠인가요?",
                "choices": ["추운 겨울", "더운 여름"],
                "correct": "추운 겨울",
                "feedback": "딩동댕! 바로 앞 설명에 ‘추운 겨울 동안’이라고 힌트가 나와 있어요!",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V2-1 카멜레온의 ‘보호색’ 뜻 단서 조립하기",
                "passage_snippet": "초록색 나뭇잎 위에 있을 때는 몸을 <span class='rx-cue'>초록색</span>으로 바꾸고, 갈색 나무줄기 위에서는 <span class='rx-cue'>갈색</span>으로 바꿉니다. 이처럼 주변 색깔과 비슷하게 변해서 <span class='rx-cue'>적의 눈에 잘 띄지 않게</span> 몸을 지켜 주는 색을 ‘<span class='rx-cue'>보호색</span>’이라고 부릅니다.",
                "think_aloud_prompt": "‘보호색’ 앞에 있는 힌트 낱말들을 모아 뜻을 완성해 보세요!",
                "cloze_sentences": [
                    "• 1단계(예시 단서): 초록 나뭇잎 위에서는 ( {b1} )으로, 갈색 줄기 위에서는 갈색으로 바꿉니다.",
                    "• 2단계(뜻 단서): 주변 색깔과 비슷해서 적의 눈에 ( {b2} ) 몸을 지켜 줍니다.",
                    "• 3단계(어휘 확인): 이렇게 몸을 지켜 주는 색을 ( {b3} )이라고 부릅니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "초록색", "options": ["초록색", "보라색", "무지개색"]},
                    {"id": "b2", "correct": "잘 띄지 않게", "options": ["잘 띄지 않게", "제일 잘 띄게", "반짝거리게"]},
                    {"id": "b3", "correct": "보호색", "options": ["보호색", "물감색", "신호등색"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D1(뜻 반대 바꾸기) & D4(색깔 교차) OX 판별",
                "desc": "카멜레온이 변하는 색깔과 보호색의 뜻을 정확히 알고 있는지 확인해 볼까요?",
                "items": [
                    {
                        "statement": "보호색은 주변 색깔과 비슷하게 변해서 무서운 적에게 들키지 않게 도와줍니다.",
                        "answer": "O",
                        "reason": "딩동댕! 본문 셋째·넷째 문장의 설명과 정확히 일치해요!",
                    },
                    {
                        "statement": "카멜레온은 초록색 나뭇잎 위에서 갈색으로 변하고, 갈색 나무줄기 위에서 초록색으로 변합니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D4 장소-색깔 교차 함정]이에요! 초록 나뭇잎에서는 초록색, 갈색 줄기에서는 갈색으로 변해요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 ‘보호색’ 문맥 추론 놀이)",
            "situation": "아이와 숨바꼭질을 하거나 옷 색깔과 이불 색깔을 비교해 볼 때",
            "parent_question": "“카멜레온이 초록 나뭇잎 위에서 초록색으로 변하는 걸 ‘보호색’이라고 한대! 왜 이름을 ‘보호색’이라고 지었을까?”",
            "expected_answer": "“주변 색깔이랑 비슷하게 변해서 무서운 새나 뱀 눈에 안 띄게 몸을 ‘보호해 주는 색’이라서 보호색이야!”",
            "coaching_tip": "‘보호(지켜 줌) + 색(색깔)’처럼 글자 조각의 뜻을 풀어서 생각하도록 도와주시면 초등 어휘력이 몰라보게 탄탄해집니다.",
        },
    ),

    # -------------------------------------------------------------------------
    # 6차시: G1-EXP-V2-2 (횡단보도에서 손을 들고 건너는 까닭)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V2-2",
        subject="통합교과(사람들·안전 1-1)",
        unit="안전한 등굣길 - 횡단보도 바르게 건너기",
        concept="초록 불에 좌우를 살피고 손을 드는 이유 추론",
        text_structure="순서·인과 기초",
        structure_type_code="causal",
        passage_title="횡단보도에서 손을 들고 건너는 까닭",
        paragraphs=[
            "길을 건널 때는 반드시 횡단보도로 건너야 안전합니다. 신호등에 초록 불이 켜져도 바로 뛰어들지 않고 멈추어서 왼쪽과 오른쪽을 먼저 살핍니다. 아직 멈추지 못한 자동차가 달려올 수도 있기 때문입니다. 차가 완전히 멈춘 것을 확인한 뒤에는 손을 번쩍 들고 운전하는 사람과 눈을 맞추며 천천히 걸어서 건넙니다."
        ],
        vocab_notes=[
            {"word": "횡단보도", "tier": "Tier 2 (사고어)", "desc": "사람이 차도를 안전하게 건널 수 있도록 흰 줄을 그어 놓은 길"},
            {"word": "살피다", "tier": "Tier 1 (기초)", "desc": "이곳저곳을 주의 깊게 자세히 보다"},
            {"word": "번쩍", "tier": "Tier 1 (감각어)", "desc": "가볍고 힘차게 높이 들어 올리는 모양"},
        ],
        visual_html="""
        <div style="background:#ECFDF5; border:2px solid #6EE7B7; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#065F46; margin-bottom:10px;">🚦 [안전 수칙 그림] 횡단보도를 안전하게 건너는 3가지 약속</div>
          <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #34D399;">
              <div style="font-size:1.25rem;">🛑 <b>1. 멈추어 살피기</b></div>
              <div style="font-size:0.84rem; color:#065F46; margin-top:4px;">초록 불이 켜져도<br><b>왼쪽·오른쪽</b> 차 확인</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #10B981;">
              <div style="font-size:1.25rem;">🙋 <b>2. 손 번쩍 들기</b></div>
              <div style="font-size:0.84rem; color:#065F46; margin-top:4px;">운전하는 사람 눈에<br><b>내가 잘 보이게</b> 하기</div>
            </div>
            <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #059669;">
              <div style="font-size:1.25rem;">🚶 <b>3. 걸어서 건너기</b></div>
              <div style="font-size:0.84rem; color:#065F46; margin-top:4px;">운전자와 눈 맞추며<br><b>천천히 걸어서</b> 이동</div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v2-2-c1", "text": "왼쪽과 오른쪽을 먼저 살핍니다", "role": "안전 행동 ①: 좌우 살피기", "para_idx": 0},
            {"cue_id": "g1-v2-2-c2", "text": "아직 멈추지 못한 자동차가 달려올 수도 있기 때문입니다", "role": "명시된 까닭 ①: 좌우를 살피는 이유", "para_idx": 0},
            {"cue_id": "g1-v2-2-c3", "text": "손을 번쩍 들고 운전하는 사람과 눈을 맞추며", "role": "생략된 까닭 추론 단서: 운전자가 어린이를 잘 볼 수 있게 함", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 인과 추론 구조도] 횡단보도 안전 행동과 그 까닭 연결하기",
            "instruction": "각 안전 행동을 왜 해야 하는지 알맞은 까닭(이유) 카드를 찾아 연결하세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "👀 초록 불에도 좌우 살피기", "sub": "왜 바로 뛰어들지 않을까요?", "correct": "아직 멈추지 못한 자동차가 달려올 수도 있기 때문"},
                {"slot_id": "slot-2", "header": "🙋 손을 번쩍 들고 눈 맞추기", "sub": "왜 손을 높이 들까요? (추론)", "correct": "운전하는 사람 눈에 어린이가 잘 띄게 하려고"},
                {"slot_id": "slot-3", "header": "🚶 뛰지 않고 걸어서 건너기", "sub": "안전한 이동 방법", "correct": "넘어지지 않고 안전하게 길을 건너기 위해서"},
            ],
            "word_bank": [
                "아직 멈추지 못한 자동차가 달려올 수도 있기 때문",
                "운전하는 사람 눈에 어린이가 잘 띄게 하려고",
                "넘어지지 않고 안전하게 길을 건너기 위해서",
                "자동차보다 더 빨리 달리기 시합을 하려고 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V2-2 (명시적 인과 관계 확인 - 3지선다)",
                "stem": "신호등에 초록 불이 켜졌는데도 바로 뛰어들지 않고 왼쪽과 오른쪽을 먼저 살피는 까닭은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "아직 멈추지 못한 자동차가 달려올 수도 있기 때문입니다.",
                "step1_hint": "잠깐! 세 번째 문장 끝에 있는 ‘~기 때문입니다’ 앞부분을 노란색 하이라이트 문장에서 읽어 보세요!",
                "step2_hint": "초록 불이 켜진 직후에도 ‘아직 멈추지 못한 자동차’가 있을 수 있어서 살피는 것이에요!",
                "options": [
                    {
                        "no": 1,
                        "text": "아직 멈추지 못한 자동차가 달려올 수도 있기 때문입니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [2문장 행동 + 3문장 '~기 때문입니다' 이유 진술 정확 연결]",
                        "explanation": "🎉 **[정답]** 초록 불이 켜져도 아직 멈추지 못한 자동차가 달려올 수 있어서 왼쪽과 오른쪽을 먼저 살펴야 해요!",
                    },
                    {
                        "no": 2,
                        "text": "초록 불이 켜지면 자동차들이 더 빨리 달려야 하기 때문입니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 규칙 반전]: 보행자 초록 불에 자동차가 더 빨리 달려야 한다는 반대 진술",
                        "explanation": "❌ **[D1 반대 사실 함정]** 횡단보도에 초록 불이 켜지면 자동차는 멈추어야 해요.",
                    },
                    {
                        "no": 3,
                        "text": "길가에 피어 있는 꽃을 구경하고 싶기 때문입니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 무관한 이유]: 안전 수칙과 무관한 꽃 구경 이유 제시",
                        "explanation": "❌ **[D6 엉뚱한 이유 함정]** 꽃 구경 때문이 아니라 달려오는 자동차가 있는지 확인하려고 좌우를 살피는 것이에요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V2-2 (생략된 행동 이유 추론형 - 3지선다)",
                "stem": "윗글과 그림을 참고할 때, 어린이가 횡단보도에서 ‘손을 번쩍 들고’ 건너는 까닭으로 가장 알맞은 것을 고르세요.",
                "bogi": "<보기>\n  키가 작은 어린이는 큰 자동차에 가려져 운전하는 사람 눈에 잘 보이지 않을 수 있습니다.",
                "target_para_idx": 0,
                "spotlight_quote": "차가 완전히 멈춘 것을 확인한 뒤에는 손을 번쩍 들고 운전하는 사람과 눈을 맞추며 천천히 걸어서 건넙니다.",
                "step1_hint": "잠깐! 마지막 문장에서 ‘손을 번쩍 들고 운전하는 사람과 눈을 맞추며’ 건넌다고 했어요. <보기>의 힌트와 합쳐 생각해 볼까요?",
                "step2_hint": "키가 작은 어린이가 손을 높이 들면 운전하는 사람 눈에 잘 보여서 안전해요!",
                "options": [
                    {
                        "no": 1,
                        "text": "팔 운동을 해서 근육을 튼튼하게 만들려고 손을 듭니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 배경지식 오용]: 손 들기 행동을 체조·운동으로 잘못 추론",
                        "explanation": "❌ **[D6 엉뚱한 추론 함정]** 횡단보도는 운동을 하는 곳이 아니에요!",
                    },
                    {
                        "no": 2,
                        "text": "운전하는 사람 눈에 내가 건너는 모습이 잘 보이게 하려고 손을 듭니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [본문 '손을 번쩍 들고 운전하는 사람과 눈을 맞추며' + <보기> 키 작은 어린이 단서 결합 추론]",
                        "explanation": "🎉 **[정답]** 손을 번쩍 들면 운전하는 사람이 길을 건너는 어린이를 멀리서도 잘 볼 수 있어서 안전해요!",
                    },
                    {
                        "no": 3,
                        "text": "신호등의 초록 불을 빨간 불로 빨리 바꾸려고 손을 듭니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D5 인과 오류]: 손을 드는 행동이 신호등을 바꾼다는 잘못된 인과",
                        "explanation": "❌ **[D5 잘못된 인과 함정]** 손을 든다고 신호등 불빛이 바뀌지는 않아요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 인과 추론 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 횡단보도에 초록 불이 켜진 뒤 길을 건너 출발하기 전에 무엇이 완전히 멈춘 것을 확인해야 하나요?",
            "part_a_options": [
                {"no": 1, "text": "자동차가 완전히 멈춘 것을 확인해야 합니다.", "is_correct": True},
                {"no": 2, "text": "하늘의 구름이 완전히 멈춘 것을 확인해야 합니다.", "is_correct": False},
                {"no": 3, "text": "시계 바늘이 완전히 멈춘 것을 확인해야 합니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 뒷받침하는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “길을 건널 때는 반드시 횡단보도로 건너야 안전합니다.”", "is_correct": False},
                {"no": 2, "text": "둘째 문장: “신호등에 초록 불이 켜져도 바로 뛰어들지 않고 멈추어서 왼쪽과 오른쪽을 먼저 살핍니다.”", "is_correct": False},
                {"no": 3, "text": "넷째 문장: “차가 완전히 멈춘 것을 확인한 뒤에는 손을 번쩍 들고 운전하는 사람과 눈을 맞추며 천천히 걸어서 건넙니다.”", "is_correct": True},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 길을 건너기 전 ‘차가 완전히 멈춘 것’(Part A)을 확인해야 한다는 내용이 넷째 문장(Part B)에 정확히 나와 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W4",
            "title": "[TEI-6 작문 워크벤치] ‘비 오는 날 밝은색 우산을 쓰는 까닭’ 문장 완성하기",
            "conditions": [
                "조건 ①: 까닭을 나타내는 말(‘~기 때문입니다’)로 문장을 끝맺을 것",
                "조건 ②: 운전하는 사람 눈에 잘 띈다는 안전한 이유가 들어갈 것",
            ],
            "draft_prefix": "비 오는 날 길을 걸을 때는 노란색처럼 밝은색 우산을 쓰면 좋습니다. 왜냐하면",
            "choices": [
                {
                    "id": "w-1",
                    "text": "어두운 빗속에서도 운전하는 사람 눈에 잘 띄어 안전하기 때문입니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 완벽해요! ‘~기 때문입니다’ 표현과 밝은색 우산이 안전한 까닭을 아주 잘 연결했어요!",
                },
                {
                    "id": "w-2",
                    "text": "비가 아예 내리지 않게 마법을 부릴 수 있기 때문입니다.",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ 우산 색깔이 비를 멈추게 한다는 것은 실제 사실이 아니에요.",
                },
                {
                    "id": "w-3",
                    "text": "노란색 우산이 제일 비싸다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ ‘~기 때문입니다’로 끝맺지 않았고, 안전과 관련 없는 내용이에요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V2-2 맞춤 처방전: [‘~기 때문입니다’ 밑줄 긋기 ➔ 숨은 까닭 추론 ➔ D5 인과 오류 백신]",
            "rx_reason": "글에 직접 쓰인 까닭(‘~기 때문입니다’)을 먼저 찾고, 일상 안전 경험을 더해 글에 생략된 까닭까지 추론하는 힘을 기릅니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A5 까닭을 알려 주는 말 찾기",
                "rule_box": "💡 **까닭 탐정 공식**: **‘왜 그럴까요?’**라는 질문이 나오면 본문에서 **‘~기 때문입니다 / ~해서’**가 붙은 문장을 먼저 찾아요!",
                "mini_question": "“복도에서는 뛰지 않고 걸어야 합니다. 뛰다가 친구와 부딪혀 다칠 수 있기 때문입니다.” — 복도에서 걸어야 하는 까닭은 무엇인가요?",
                "choices": ["뛰다가 친구와 부딪혀 다칠 수 있어서", "복도가 너무 짧아서"],
                "correct": "뛰다가 친구와 부딪혀 다칠 수 있어서",
                "feedback": "딩동댕! ‘~기 때문입니다’ 앞에 있는 ‘뛰다가 친구와 부딪혀 다칠 수 있다’는 점이 까닭이에요.",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V2-2 횡단보도 안전 수칙과 까닭 연결하기",
                "passage_snippet": "신호등에 초록 불이 켜져도 멈추어서 <span class='rx-cue'>왼쪽과 오른쪽</span>을 먼저 살핍니다. 아직 <span class='rx-cue'>멈추지 못한 자동차</span>가 달려올 수도 있기 때문입니다. 차가 완전히 멈춘 뒤에는 <span class='rx-cue'>손을 번쩍 들고</span> 운전하는 사람과 눈을 맞추며 건넙니다.",
                "think_aloud_prompt": "안전 행동과 그 까닭이 바르게 이어지도록 빈칸을 채워 보세요!",
                "cloze_sentences": [
                    "• 1단계(행동 1): 초록 불이 켜져도 먼저 ( {b1} )을 살핍니다.",
                    "• 2단계(까닭 1): 아직 멈추지 못한 ( {b2} )가 달려올 수도 있기 때문입니다.",
                    "• 3단계(까닭 2 추론): ( {b3} )을 번쩍 들면 운전하는 사람 눈에 내가 잘 보여서 안전합니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "왼쪽과 오른쪽", "options": ["왼쪽과 오른쪽", "하늘과 땅", "가방 안쪽"]},
                    {"id": "b2", "correct": "자동차", "options": ["자동차", "구름", "나무"]},
                    {"id": "b3", "correct": "손", "options": ["손", "발가락", "귀"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D1(행동 반전) & D5(잘못된 까닭 연결) OX 판별",
                "desc": "횡단보도를 건널 때의 바른 행동과 까닭을 정확히 구별해 보세요!",
                "items": [
                    {
                        "statement": "신호등에 초록 불이 켜지자마자 좌우를 보지 않고 달리기 시합하듯 뛰어가야 합니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D1 반대 행동 함정]이에요! 바로 뛰어들지 않고 멈추어 왼쪽과 오른쪽을 먼저 살펴야 해요.",
                    },
                    {
                        "statement": "차가 완전히 멈춘 것을 확인한 뒤 운전하는 사람과 눈을 맞추며 걸어서 건넙니다.",
                        "answer": "O",
                        "reason": "딩동댕! 본문 마지막 문장의 안전 수칙과 정확히 일치해요!",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 ‘왜 그럴까?’ 까닭 추론하기)",
            "situation": "아이와 등하굣길 횡단보도를 건너거나 교통안전 이야기를 나눌 때",
            "parent_question": "“초록 불이 켜졌는데도 왜 바로 뛰지 않고 왼쪽·오른쪽을 먼저 살펴야 할까? 그리고 왜 손을 번쩍 들고 건널까?”",
            "expected_answer": "“아직 못 멈춘 자동차가 달려올 수도 있어서 먼저 살펴야 해! 그리고 손을 번쩍 들면 운전하는 아저씨 눈에 내가 잘 보여서 안전해!”",
            "coaching_tip": "아이가 대답할 때 끝말을 ‘~기 때문이야!’라고 또박또박 마무리하도록 격려해 주시면 인과적 사고력이 크게 자랍니다.",
        },
    ),

    # -------------------------------------------------------------------------
    # 7차시: G1-EXP-V2-3 (굴러가는 모양과 쌓이는 모양)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V2-3",
        subject="수학(여러 가지 모양 1-1)",
        unit="여러 가지 모양 - 상자 모양·둥근기둥 모양·공 모양",
        concept="블록 모양별 평평한 부분과 둥근 부분에 따른 굴러가기·쌓기 특징 통합 추론",
        text_structure="비교·분류 기초",
        structure_type_code="comparison",
        passage_title="굴러가는 모양과 쌓이는 모양",
        paragraphs=[
            "우리 주변의 물건들은 모양에 따라 잘 쌓이기도 하고 잘 굴러가기도 합니다. 상자 모양은 반듯하고 평평한 부분만 있어서 위로 높이 쌓기에 아주 좋습니다. 반면에 공 모양은 어느 쪽으로 보아도 둥글어서 모든 방향으로 데구루루 잘 굴러가지만 위로 쌓기는 어렵습니다. 둥근기둥 모양은 위아래에 평평한 부분도 있고 옆에 둥근 부분도 있어서 세우면 잘 쌓이고 눕히면 잘 굴러갑니다."
        ],
        vocab_notes=[
            {"word": "평평하다", "tier": "Tier 1 (기초)", "desc": "바닥이나 겉면이 높고 낮음이 없이 고르고 반듯하다"},
            {"word": "방향", "tier": "Tier 2 (사고어)", "desc": "앞, 뒤, 왼쪽, 오른쪽처럼 어떤 쪽을 가리키는 곳"},
            {"word": "둥근기둥", "tier": "Tier 3 (교과어)", "desc": "위아래는 동그랗고 평평하며 옆면은 둥근 기둥 모양"},
        ],
        visual_html="""
        <div style="background:#EFF6FF; border:2px solid #93C5FD; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#1E3A8A; margin-bottom:10px;">🧊 [실험 그림 표] 모양 블록 쌓기와 굴리기 실험 결과</div>
          <table style="width:100%; border-collapse:collapse; background:#fff; font-size:0.86rem; text-align:center;">
            <thead>
              <tr style="background:#DBEAFE; color:#1E3A8A;">
                <th style="padding:8px; border:1px solid #93C5FD;">모양 이름</th>
                <th style="padding:8px; border:1px solid #93C5FD;">겉모습 특징</th>
                <th style="padding:8px; border:1px solid #93C5FD;">위로 쌓기</th>
                <th style="padding:8px; border:1px solid #93C5FD;">바닥에 굴리기</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding:8px; border:1px solid #BFDBFE; font-weight:700;">📦 상자 모양</td>
                <td style="padding:8px; border:1px solid #BFDBFE;">평평한 부분만 있음</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#15803D; font-weight:700;">⭕ 아주 잘 쌓임</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#B91C1C;">❌ 안 굴러감</td>
              </tr>
              <tr>
                <td style="padding:8px; border:1px solid #BFDBFE; font-weight:700;">⚽ 공 모양</td>
                <td style="padding:8px; border:1px solid #BFDBFE;">둥근 부분만 있음</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#B91C1C;">❌ 쌓기 어려움</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#15803D; font-weight:700;">⭕ 모든 방향 굴러감</td>
              </tr>
              <tr>
                <td style="padding:8px; border:1px solid #BFDBFE; font-weight:700;">🥫 둥근기둥 모양</td>
                <td style="padding:8px; border:1px solid #BFDBFE;">평평한 곳 + 둥근 곳</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#1D4ED8; font-weight:700;">⭕ 세우면 잘 쌓임</td>
                <td style="padding:8px; border:1px solid #BFDBFE; color:#1D4ED8; font-weight:700;">⭕ 눕히면 잘 굴러감</td>
              </tr>
            </tbody>
          </table>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v2-3-c1", "text": "상자 모양은 반듯하고 평평한 부분만 있어서", "role": "상자 모양 특징: 위로 잘 쌓임", "para_idx": 0},
            {"cue_id": "g1-v2-3-c2", "text": "공 모양은 어느 쪽으로 보아도 둥글어서", "role": "공 모양 특징: 모든 방향으로 잘 굴러감", "para_idx": 0},
            {"cue_id": "g1-v2-3-c3", "text": "세우면 잘 쌓이고 눕히면 잘 굴러갑니다", "role": "둥근기둥 모양 특징: 세울 때와 눕힐 때의 차이", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 비교·분류 구조도] 세 가지 모양 블록의 특징 비교하기",
            "instruction": "글과 실험 표를 함께 보고 각 모양 블록의 알맞은 특징 카드를 빈칸에 넣으세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "📦 상자 모양", "sub": "평평한 부분만 있음", "correct": "위로 높이 쌓기에 아주 좋음"},
                {"slot_id": "slot-2", "header": "⚽ 공 모양", "sub": "둥근 부분만 있음", "correct": "모든 방향으로 잘 굴러가지만 쌓기 어려움"},
                {"slot_id": "slot-3", "header": "🥫 둥근기둥 모양", "sub": "평평한 부분 + 둥근 부분", "correct": "세우면 잘 쌓이고 눕히면 잘 굴러감"},
            ],
            "word_bank": [
                "위로 높이 쌓기에 아주 좋음",
                "모든 방향으로 잘 굴러가지만 쌓기 어려움",
                "세우면 잘 쌓이고 눕히면 잘 굴러감",
                "세워 놓아도 저절로 굴러감 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V2-3 (텍스트와 실험 표 통합 추론 - 3지선다)",
                "stem": "윗글과 [실험 그림 표]를 함께 보았을 때, ‘둥근기둥 모양’ 블록을 바닥에 데구루루 굴리려면 어떻게 놓아야 하나요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "둥근기둥 모양은 위아래에 평평한 부분도 있고 옆에 둥근 부분도 있어서 세우면 잘 쌓이고 눕히면 잘 굴러갑니다.",
                "step1_hint": "잠깐! 마지막 문장과 표의 맨 아랫줄에서 ‘둥근기둥 모양’이 언제 잘 굴러간다고 했는지 찾아보세요!",
                "step2_hint": "평평한 바닥으로 ‘세우면’ 쌓이고, 둥근 옆면이 바닥에 닿게 ‘눕히면’ 잘 굴러가요!",
                "options": [
                    {
                        "no": 1,
                        "text": "둥근 옆부분이 바닥에 닿도록 옆으로 눕혀 놓아야 합니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [본문 '옆에 둥근 부분도 있어서... 눕히면 잘 굴러갑니다' + 표 '눕히면 잘 굴러감' 통합]",
                        "explanation": "🎉 **[정답]** 둥근기둥 모양은 옆에 둥근 부분이 있어서 옆으로 **눕히면** 데구루루 잘 굴러가요!",
                    },
                    {
                        "no": 2,
                        "text": "평평한 위아래 부분이 바닥에 닿도록 똑바로 세워 놓아야 합니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 조건-결과 교차]: '세우면 잘 쌓이고'와 '눕히면 잘 굴러갑니다'를 서로 뒤바꿈",
                        "explanation": "❌ **[D4 조건 교차 함정]** 똑바로 **세워** 놓으면 굴러가지 않고 위로 잘 쌓여요!",
                    },
                    {
                        "no": 3,
                        "text": "상자 모양 블록 속에 넣어서 묶어 놓아야 합니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 무관한 조작]: 상자 모양은 굴러가지 않는데 상자에 넣어야 한다는 오류",
                        "explanation": "❌ **[D6 잘못된 추론 함정]** 상자 모양은 평평한 부분만 있어서 바닥에 굴러가지 않아요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V2-3 (<보기> 블록 탑 쌓기 상황 추론형 - 3지선다)",
                "stem": "윗글과 표를 참고할 때, <보기>의 지민이가 무너지지 않는 높은 탑을 쌓으려면 맨 아래에 어떤 모양을 놓는 것이 가장 좋을까요?",
                "bogi": "<보기>\n  지민이는 블록들을 위로 층층이 높이 쌓아서 튼튼한 성을 만들려고 합니다.",
                "target_para_idx": 0,
                "spotlight_quote": "상자 모양은 반듯하고 평평한 부분만 있어서 위로 높이 쌓기에 아주 좋습니다.",
                "step1_hint": "잠깐! 표의 ‘위로 쌓기’ 칸에서 ‘⭕ 아주 잘 쌓임’이라고 적힌 모양과 둘째 문장을 확인해 보세요!",
                "step2_hint": "공 모양은 굴러가서 쌓기 어렵고, 평평한 부분만 있는 ‘상자 모양’이 높이 쌓기에 가장 좋아요!",
                "options": [
                    {
                        "no": 1,
                        "text": "어느 쪽으로 보아도 둥근 공 모양 블록을 맨 아래에 놓습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D1 특징 반전]: 위로 쌓기 어려운 '공 모양'을 탑 맨 아래에 놓는다는 오류",
                        "explanation": "❌ **[D1 특징 반대 함정]** 공 모양은 둥글어서 굴러가기 때문에 위로 블록을 쌓기가 어려워요.",
                    },
                    {
                        "no": 2,
                        "text": "반듯하고 평평한 부분만 있는 상자 모양 블록을 놓습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [본문 2문장 '상자 모양은 반듯하고 평평한 부분만 있어서 위로 높이 쌓기에 아주 좋습니다' 적용]",
                        "explanation": "🎉 **[정답]** 반듯하고 평평한 부분만 있는 **상자 모양**이 위로 높이 쌓기에 아주 좋아요!",
                    },
                    {
                        "no": 3,
                        "text": "둥근기둥 모양 블록을 옆으로 눕혀서 맨 아래에 놓습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 세우기/눕히기 혼동]: 둥근기둥을 눕히면 굴러가서 쌓을 수 없음",
                        "explanation": "❌ **[D4 세우기·눕히기 혼동 함정]** 둥근기둥을 옆으로 눕히면 데구루루 굴러가서 탑이 무너져요!",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 모양 비교 추론 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 공 모양 블록이 모든 방향으로 잘 굴러가지만 위로 쌓기 어려운 까닭은 무엇인가요?",
            "part_a_options": [
                {"no": 1, "text": "평평한 부분이 없고 어느 쪽으로 보아도 둥글기 때문입니다.", "is_correct": True},
                {"no": 2, "text": "반듯하고 평평한 부분만 있기 때문입니다.", "is_correct": False},
                {"no": 3, "text": "위아래는 평평하고 옆면만 둥글기 때문입니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 뒷받침하는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "둘째 문장: “상자 모양은 반듯하고 평평한 부분만 있어서 위로 높이 쌓기에 아주 좋습니다.”", "is_correct": False},
                {"no": 2, "text": "셋째 문장: “반면에 공 모양은 어느 쪽으로 보아도 둥글어서 모든 방향으로 데구루루 잘 굴러가지만 위로 쌓기는 어렵습니다.”", "is_correct": True},
                {"no": 3, "text": "넷째 문장: “둥근기둥 모양은 위아래에 평평한 부분도 있고 옆에 둥근 부분도 있어서 세우면 잘 쌓이고 눕히면 잘 굴러갑니다.”", "is_correct": False},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 공 모양은 ‘어느 쪽으로 보아도 둥글어서’(Part A) 잘 굴러가고 쌓기 어렵다는 사실이 셋째 문장(Part B)에 나와 있어요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W4",
            "title": "[TEI-6 작문 워크벤치] 그림과 글을 합쳐 ‘둥근기둥 모양’ 특징 한 문장 쓰기",
            "conditions": [
                "조건 ①: ‘둥근기둥 모양은’으로 문장을 시작할 것",
                "조건 ②: ‘세울 때’와 ‘눕힐 때’의 특징이 모두 바르게 들어갈 것",
            ],
            "draft_prefix": "실험 그림과 글을 함께 살펴보았습니다.",
            "choices": [
                {
                    "id": "w-1",
                    "text": "둥근기둥 모양은 똑바로 세우면 잘 쌓이고 옆으로 눕히면 잘 굴러갑니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 완벽해요! 둥근기둥 모양을 세울 때와 눕힐 때의 특징을 정확하게 비교해 썼어요.",
                },
                {
                    "id": "w-2",
                    "text": "둥근기둥 모양은 똑바로 세우면 잘 굴러가고 옆으로 눕히면 잘 쌓입니다.",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ 세울 때와 눕힐 때의 결과가 거꾸로 바뀌었어요!",
                },
                {
                    "id": "w-3",
                    "text": "공 모양은 축구할 때 쓰면 참 재미있습니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ ‘둥근기둥 모양’에 대한 설명이 아니에요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V2-3 맞춤 처방전: [글의 모양 이름과 표의 ⭕·❌ 포개기 ➔ 세우기/눕히기 구분 ➔ D4 교차 백신]",
            "rx_reason": "글만 읽거나 그림표만 따로 보지 않고, 본문의 이유 설명(‘평평해서/둥글어서’)과 표의 결과(⭕/❌)를 하나로 합쳐 생각하는 훈련을 진행합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A2 ‘평평하다’와 ‘둥글다’ 감각 낱말 구별",
                "rule_box": "💡 **모양 공식**: 책상 위처럼 반듯한 것은 **‘평평한 부분(잘 쌓임)’**, 공처럼 모서리가 없는 것은 **‘둥근 부분(잘 굴러감)’**이에요!",
                "mini_question": "바닥에 놓았을 때 데구루루 잘 굴러가는 부분은 어떤 모양일까요?",
                "choices": ["둥근 부분", "평평한 부분"],
                "correct": "둥근 부분",
                "feedback": "딩동댕! 둥근 부분이 바닥에 닿아야 데구루루 잘 굴러가요!",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V2-3 모양 블록 3종의 특징과 표 통합 조립",
                "passage_snippet": "<span class='rx-cue'>상자 모양</span>은 평평한 부분만 있어서 위로 높이 쌓기에 좋습니다. <span class='rx-cue'>공 모양</span>은 어느 쪽으로 보아도 둥글어서 잘 굴러갑니다. <span class='rx-cue'>둥근기둥 모양</span>은 <span class='rx-cue'>세우면 잘 쌓이고 눕히면 잘 굴러갑니다</span>.",
                "think_aloud_prompt": "본문과 실험 표를 비교하며 빈칸에 알맞은 말을 골라 보세요!",
                "cloze_sentences": [
                    "• 1단계: 평평한 부분만 있어서 잘 쌓이지만 안 굴러가는 것은 ( {b1} )입니다.",
                    "• 2단계: 둥근 부분만 있어서 모든 방향으로 잘 굴러가는 것은 ( {b2} )입니다.",
                    "• 3단계: 둥근기둥 모양은 세우면 잘 쌓이고 옆으로 ( {b3} ) 잘 굴러갑니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "상자 모양", "options": ["상자 모양", "공 모양", "바람 모양"]},
                    {"id": "b2", "correct": "공 모양", "options": ["공 모양", "상자 모양", "네모 모양"]},
                    {"id": "b3", "correct": "눕히면", "options": ["눕히면", "세우면", "숨기면"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D4(세울 때와 눕힐 때 바꾸기) OX 판별",
                "desc": "둥근기둥 모양의 특징을 바르게 설명한 문장인지 판별해 보세요!",
                "items": [
                    {
                        "statement": "둥근기둥 모양은 평평한 부분도 있고 둥근 부분도 있어서 세우면 잘 쌓입니다.",
                        "answer": "O",
                        "reason": "딩동댕! 위아래 평평한 부분으로 세우면 위로 잘 쌓여요!",
                    },
                    {
                        "statement": "상자 모양은 둥근 부분이 많아서 공 모양보다 더 잘 굴러갑니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D4 대상 특징 교차 함정]이에요! 상자 모양은 평평한 부분만 있어서 굴러가지 않아요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 글+그림 통합 관찰: 모양 찾기)",
            "situation": "집에 있는 과자 상자(상자 모양), 통조림 캔·물컵(둥근기둥 모양), 귤·공(공 모양)을 식탁에 놓았을 때",
            "parent_question": "“이 통조림 캔은 ‘둥근기둥 모양’이네! 이걸 위로 쌓고 싶을 때랑 바닥에 굴리고 싶을 때 각각 어떻게 놓아야 할까?”",
            "expected_answer": "“위아래 평평한 쪽으로 똑바로 세우면 위로 잘 쌓이고, 둥근 옆면이 닿게 옆으로 눕히면 데구루루 잘 굴러가!”",
            "coaching_tip": "직접 캔이나 휴지심을 세워 보고 눕혀 보며 글에서 읽은 문장 그대로 말해보게 하면 수학·국어 통합 사고력이 자라납니다.",
        },
    ),

    # -------------------------------------------------------------------------
    # 8차시: G1-EXP-V2-4 (겨울잠을 자는 동물들 - 곰과 개구리)
    # -------------------------------------------------------------------------
    build_expository_slot(
        grade_num=1,
        subskill_code="V2-4",
        subject="통합교과(계절 1-2)",
        unit="겨울이 왔어요 - 동물의 겨울나기",
        concept="추운 겨울에 겨울잠을 자는 동물 소개 및 설명글을 쓴 목적 추론",
        text_structure="열거·인과 기초",
        structure_type_code="causal",
        passage_title="겨울잠을 자는 동물들 (곰과 개구리)",
        paragraphs=[
            "찬 바람이 쌩쌩 부는 겨울이 오면 날씨가 아주 추워지고 동물들의 먹이도 줄어듭니다. 그래서 곰과 개구리는 따뜻한 봄이 올 때까지 긴 겨울잠을 잡니다. 곰은 가을 동안 열매를 많이 먹어 몸속에 영양분을 모아 둔 뒤 동굴 속에서 잠을 잡니다. 개구리는 얼지 않는 따뜻한 땅속으로 깊이 들어가 겨울잠을 잡니다."
        ],
        vocab_notes=[
            {"word": "겨울잠", "tier": "Tier 2 (사고어)", "desc": "일부 동물들이 추운 겨울 동안 굴이나 땅속에서 활동을 멈추고 자는 긴 잠"},
            {"word": "영양분", "tier": "Tier 3 (교과어)", "desc": "몸이 자라고 힘을 내는 데 필요한 좋은 성분"},
            {"word": "동굴", "tier": "Tier 1 (기초)", "desc": "산이나 바위 속에 자연적으로 넓게 뚫린 굴"},
        ],
        visual_html="""
        <div style="background:#F8FAFC; border:2px solid #94A3B8; border-radius:12px; padding:14px; margin:12px 0;">
          <div style="font-weight:800; color:#1E293B; margin-bottom:10px;">❄️ [단면 그림 자료] 추운 겨울, 곰과 개구리는 어디서 겨울잠을 잘까요?</div>
          <div style="display:grid; grid-template-columns:repeat(2, 1fr); gap:10px; text-align:center;">
            <div style="background:#FEF3C7; padding:10px; border-radius:8px; border:2px solid #F59E0B;">
              <div style="font-size:1.25rem;">🐻 <b>곰의 겨울잠</b></div>
              <div style="font-size:0.85rem; color:#78350F; margin-top:4px;">가을에 열매를 많이 먹고<br><b>바위 동굴 속</b>에서 잠을 잠</div>
            </div>
            <div style="background:#ECFDF5; padding:10px; border-radius:8px; border:2px solid #10B981;">
              <div style="font-size:1.25rem;">🐸 <b>개구리의 겨울잠</b></div>
              <div style="font-size:0.85rem; color:#065F46; margin-top:4px;">얼지 않는 따뜻한<br><b>깊은 땅속</b>에서 잠을 잠</div>
            </div>
          </div>
        </div>
        """,
        hottext_cues=[
            {"cue_id": "g1-v2-4-c1", "text": "날씨가 아주 추워지고 동물들의 먹이도 줄어듭니다", "role": "겨울잠을 자는 까닭(원인)", "para_idx": 0},
            {"cue_id": "g1-v2-4-c2", "text": "곰과 개구리는 따뜻한 봄이 올 때까지 긴 겨울잠을 잡니다", "role": "핵심 설명 정보: 겨울잠을 자는 동물 소개", "para_idx": 0},
            {"cue_id": "g1-v2-4-c3", "text": "동굴 속에서 잠을 잡니다", "role": "곰이 겨울잠을 자는 장소", "para_idx": 0},
            {"cue_id": "g1-v2-4-c4", "text": "따뜻한 땅속으로 깊이 들어가 겨울잠을 잡니다", "role": "개구리가 겨울잠을 자는 장소", "para_idx": 0},
        ],
        graphic_organizer={
            "title": "[TEI-4 필자 목적 및 인과·열거 도해] 겨울잠을 자는 동물과 글을 쓴 목적",
            "instruction": "곰과 개구리가 겨울잠을 자는 까닭·장소와 글쓴이가 이 글을 쓴 목적을 완성하세요!",
            "nodes": [
                {"slot_id": "slot-1", "header": "❄️ 겨울잠을 자는 까닭", "sub": "첫째 문장 원인", "correct": "날씨가 추워지고 먹이가 줄어들기 때문"},
                {"slot_id": "slot-2", "header": "🐻 곰 vs 🐸 개구리 장소", "sub": "어디서 잘까요?", "correct": "곰은 동굴 속, 개구리는 따뜻한 땅속에서 잠"},
                {"slot_id": "slot-3", "header": "✍️ 글을 쓴 목적", "sub": "왜 이 글을 썼을까요?", "correct": "겨울잠을 자는 동물의 실제 사실을 알려 주려고"},
            ],
            "word_bank": [
                "날씨가 추워지고 먹이가 줄어들기 때문",
                "곰은 동굴 속, 개구리는 따뜻한 땅속에서 잠",
                "겨울잠을 자는 동물의 실제 사실을 알려 주려고",
                "곰이 사람으로 변한 옛날이야기를 들려주려고 (함정!)",
            ],
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "CSAT-READ-V2-4 (글쓴이의 집필 목적 추론 - 3지선다)",
                "stem": "글쓴이가 윗글을 쓴 까닭(목적)으로 가장 <u>알맞은</u> 것은 무엇인가요?",
                "bogi": None,
                "target_para_idx": 0,
                "spotlight_quote": "그래서 곰과 개구리는 따뜻한 봄이 올 때까지 긴 겨울잠을 잡니다.",
                "step1_hint": "잠깐! 이 글이 꾸며낸 옛날이야기인지, 아니면 동물들의 진짜 사실을 알려 주는 설명글인지 생각해 보세요!",
                "step2_hint": "문장 끝이 ‘~잡니다’로 끝나며, 곰과 개구리가 겨울잠을 자는 까닭과 장소를 ‘알려 주려고’ 쓴 글이에요!",
                "options": [
                    {
                        "no": 1,
                        "text": "곰과 개구리가 겨울잠을 자는 까닭과 모습을 알려 주려고 썼습니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [설명문의 집필 목적 '새로운 사실·정보 전달' 정확 추론]",
                        "explanation": "🎉 **[정답]** 이 글은 겨울에 잠을 자는 동물(곰과 개구리)의 실제 사실을 독자에게 **알려 주려고** 쓴 설명글이에요!",
                    },
                    {
                        "no": 2,
                        "text": "동굴에서 쑥과 마늘을 먹고 사람이 된 곰의 옛날이야기를 들려주려고 썼습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 이야기 글(서사) 목적과 혼동]: 단군신화 옛날이야기 목적을 제시",
                        "explanation": "❌ **[D6 갈래 목적 혼동 함정]** 곰이 사람이 되었다는 옛날이야기가 아니라, 실제 자연 속 동물의 생태를 알려 주는 설명글이에요.",
                    },
                    {
                        "no": 3,
                        "text": "추운 겨울에도 잠을 자지 말고 밖에서 뛰어놀자고 설득하려고 썼습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D6 주장하는 글(설득) 목적과 혼동]: 독자의 행동을 촉구하는 설득 목적 제시",
                        "explanation": "❌ **[D6 설득 목적 혼동 함정]** 사람들에게 잠을 자지 말자고 주장하는 글이 아니에요.",
                    },
                ],
            },
            {
                "q_no": 2,
                "archetype": "CSAT-READ-V2-4 (<보기> 옛날이야기와 설명글 비교 추론형 - 3지선다)",
                "stem": "윗글과 <보기>의 글을 비교했을 때, 윗글만의 특징으로 알맞은 것을 고르세요.",
                "bogi": "<보기>\n  옛날 옛적에 아기 곰이 개구리와 함께 눈사람을 만들며 신나게 노래를 불렀습니다. 눈사람도 함께 춤을 추었습니다.",
                "target_para_idx": 0,
                "spotlight_quote": "곰은 가을 동안 열매를 많이 먹어 몸속에 영양분을 모아 둔 뒤 동굴 속에서 잠을 잡니다.",
                "step1_hint": "잠깐! <보기>는 눈사람이 춤을 추는 상상의 이야기예요. 반면에 윗글은 어떤 내용을 담고 있나요?",
                "step2_hint": "윗글은 상상이 아니라 실제로 동물들이 어떻게 겨울을 나는지 ‘진짜 사실’을 알려 주고 있어요!",
                "options": [
                    {
                        "no": 1,
                        "text": "실제로는 일어날 수 없는 마법 이야기를 재미있게 꾸며 썼습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 <보기>와 특징 교차]: <보기>(옛날이야기)의 특징을 윗글(설명문)의 특징으로 서술",
                        "explanation": "❌ **[D4 대상 특징 교차 함정]** 꾸며낸 이야기는 윗글이 아니라 <보기>의 특징이에요!",
                    },
                    {
                        "no": 2,
                        "text": "곰과 개구리가 실제로 어떻게 겨울잠을 자는지 정확한 사실을 알려 줍니다.",
                        "is_correct": True,
                        "formula": "정답 공식: [이야기 글(<보기>)과 대비되는 설명문(윗글)의 사실 전달 목적 변별]",
                        "explanation": "🎉 **[정답]** <보기>는 재미있게 꾸며낸 이야기이고, 윗글은 동물의 겨울잠에 대한 **정확한 사실**을 알려 주는 설명글이에요!",
                    },
                    {
                        "no": 3,
                        "text": "곰은 땅속에서 자고 개구리는 나무 위에서 잔다고 거꾸로 설명했습니다.",
                        "is_correct": False,
                        "formula": "오답 공식 [D4 장소 교차 왜곡]: 곰(동굴)과 개구리(땅속)의 장소를 왜곡",
                        "explanation": "❌ **[D4 장소 교차 함정]** 윗글은 곰은 동굴 속에서, 개구리는 땅속에서 잔다고 바르게 설명했어요.",
                    },
                ],
            },
        ],
        ebsr_question={
            "archetype": "TEI-2 EBSR (2단계 근거 연동형 문항 — 이유 추론 + 본문 근거 문장 선택)",
            "part_a_stem": "[Part A] 곰과 개구리가 겨울에 활동을 멈추고 긴 겨울잠을 자는 까닭은 무엇인가요?",
            "part_a_options": [
                {"no": 1, "text": "겨울이 오면 날씨가 아주 추워지고 먹을 수 있는 먹이도 줄어들기 때문입니다.", "is_correct": True},
                {"no": 2, "text": "겨울이 오면 날씨가 너무 더워지고 먹이가 너무 많아지기 때문입니다.", "is_correct": False},
                {"no": 3, "text": "봄에 친구들과 달리기 시합을 하기로 약속했기 때문입니다.", "is_correct": False},
            ],
            "part_b_stem": "[Part B] 위 Part A의 답을 알려 주는 ‘근거 문장’을 윗글에서 찾아 고르세요.",
            "part_b_options": [
                {"no": 1, "text": "첫째 문장: “찬 바람이 쌩쌩 부는 겨울이 오면 날씨가 아주 추워지고 동물들의 먹이도 줄어듭니다.”", "is_correct": True},
                {"no": 2, "text": "셋째 문장: “곰은 가을 동안 열매를 많이 먹어 몸속에 영양분을 모아 둔 뒤 동굴 속에서 잠을 잡니다.”", "is_correct": False},
                {"no": 3, "text": "넷째 문장: “개구리는 얼지 않는 따뜻한 땅속으로 깊이 들어가 겨울잠을 잡니다.”", "is_correct": False},
            ],
            "explanation": "🔗 **[EBSR 근거 연결 성공]** 겨울에 날씨가 추워지고 먹이가 줄어들어서(Part A, 첫째 문장 Part B) 긴 겨울잠을 자는 것이에요!",
        },
        writing_workbench={
            "mode": "sentence_builder",
            "code": "G1-EXP-W1",
            "title": "[TEI-6 작문 워크벤치] 글쓴이가 이 글을 쓴 까닭(목적) 한 문장으로 쓰기",
            "conditions": [
                "조건 ①: 설명 대상인 ‘겨울잠을 자는 동물’이 들어갈 것",
                "조건 ②: 설명글의 목적을 나타내는 ‘~에 대해 알려 주려고 썼습니다’로 끝맺을 것",
            ],
            "draft_prefix": "[질문: 글쓴이는 왜 이 글을 썼을까요?]",
            "choices": [
                {
                    "id": "w-1",
                    "text": "추운 겨울에 겨울잠을 자는 동물들에 대해 알려 주려고 썼습니다.",
                    "is_correct": True,
                    "cond_check": [True, True],
                    "feedback": "🎉 완벽해요! 설명 대상(‘겨울잠을 자는 동물들’)과 설명글의 목적(‘알려 주려고 썼습니다’)이 정확히 들어갔어요!",
                },
                {
                    "id": "w-2",
                    "text": "곰이랑 개구리가 나오는 웃긴 만화를 그리려고 썼습니다.",
                    "is_correct": False,
                    "cond_check": [False, False],
                    "feedback": "❌ 만화를 그리려는 것이 아니라 실제 사실을 알려 주려고 쓴 글이에요.",
                },
                {
                    "id": "w-3",
                    "text": "겨울잠을 자는 동물이 불쌍해서 눈물이 났습니다.",
                    "is_correct": False,
                    "cond_check": [True, False],
                    "feedback": "❌ ‘~에 대해 알려 주려고 썼습니다’라는 목적 표현이 빠졌어요.",
                },
            ],
        },
        prescription_clinic={
            "rx_title": "1학년 V2-4 맞춤 처방전: [설명글 끝맺음 확인 ➔ 이야기 글과 구별하기 ➔ 집필 목적 백신]",
            "rx_reason": "재미있는 이야기를 꾸며 쓴 동화책과 새로운 사실을 알려 주는 설명글의 차이점을 알고, 글쓴이가 왜 이 글을 썼는지 추론합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A6 이야기 글과 설명하는 글 구별하기",
                "rule_box": "💡 **설명글 목적 공식**: **‘옛날 옛적에~’**는 재미있는 이야기를 들려주려는 글이고, **‘~은 ~합니다’**로 진짜 사실을 적은 글은 **‘새로운 사실을 알려 주려는 글’**이에요!",
                "mini_question": "새로운 사실이나 방법을 친구에게 ‘알려 주려고’ 쓰는 글을 무엇이라고 하나요?",
                "choices": ["설명하는 글", "옛날이야기"],
                "correct": "설명하는 글",
                "feedback": "딩동댕! 정확한 사실과 정보를 알려 주려고 쓴 글이 바로 ‘설명하는 글’이에요.",
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V2-4 겨울잠 동물 정보와 글쓴이 목적 조립",
                "passage_snippet": "겨울이 오면 날씨가 아주 추워지고 동물들의 <span class='rx-cue'>먹이도 줄어듭니다</span>. 그래서 곰과 개구리는 긴 <span class='rx-cue'>겨울잠</span>을 잡니다. 곰은 <span class='rx-cue'>동굴 속</span>에서 자고, 개구리는 따뜻한 <span class='rx-cue'>땅속</span>에서 잡니다.",
                "think_aloud_prompt": "본문에서 알려 주는 사실과 글쓴이의 목적을 빈칸에 넣어 보세요!",
                "cloze_sentences": [
                    "• 1단계: 겨울에는 날씨가 춥고 ( {b1} )가 줄어들어 곰과 개구리가 겨울잠을 잡니다.",
                    "• 2단계: 곰은 ( {b2} )에서 자고, 개구리는 따뜻한 땅속에서 잡니다.",
                    "• 3단계: 글쓴이는 겨울잠을 자는 동물의 사실을 ( {b3} ) 이 글을 썼습니다.",
                ],
                "blanks": [
                    {"id": "b1", "correct": "먹이", "options": ["먹이", "눈사람", "장난감"]},
                    {"id": "b2", "correct": "동굴 속", "options": ["동굴 속", "구름 위", "바다 위"]},
                    {"id": "b3", "correct": "알려 주려고", "options": ["알려 주려고", "숨기려고", "놀리려고"]},
                ],
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D4(장소 뒤바꾸기) & D6(갈래 목적 혼동) OX 판별",
                "desc": "곰과 개구리가 겨울잠을 자는 곳과 글의 목적을 바르게 말했는지 판별해 보세요!",
                "items": [
                    {
                        "statement": "윗글은 곰과 개구리가 겨울잠을 자는 실제 사실을 알려 주려고 쓴 글입니다.",
                        "answer": "O",
                        "reason": "딩동댕! 설명글을 쓴 목적을 정확하게 찾았어요!",
                    },
                    {
                        "statement": "곰은 땅속 깊이 들어가 자고, 개구리는 바위 동굴 속에서 겨울잠을 잡니다.",
                        "answer": "X",
                        "reason": "삐뽀! [D4 장소 교차 함정]이에요! 곰이 동굴 속, 개구리가 땅속에서 겨울잠을 자요.",
                    },
                ],
            },
        },
        parent_table_talk={
            "title": "오늘 저녁 5분 식탁 대화 가이드 (초1 옛날이야기 vs 설명글 구별하기)",
            "situation": "아이와 잠자리에서 동화책과 자연관찰 책을 함께 볼 때",
            "parent_question": "“곰이 쑥이랑 마늘 먹고 사람이 됐다는 이야기책이랑, 오늘 읽은 ‘겨울잠을 자는 곰과 개구리’ 글은 쓴 이유가 어떻게 다를까?”",
            "expected_answer": "“옛날이야기는 재미있게 꾸며낸 이야기고, 오늘 읽은 글은 곰이랑 개구리가 추운 겨울에 어떻게 겨울잠을 자는지 진짜 사실을 알려 주려고 쓴 글이야!”",
            "coaching_tip": "책을 읽기 전 ‘이 책은 재미있는 이야기책일까, 진짜 사실을 알려 주는 설명책일까?’를 물어보시면 필자 의도 추론 능력이 쑥쑥 자랍니다.",
        },
    ),
]
