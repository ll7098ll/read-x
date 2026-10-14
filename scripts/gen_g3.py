# -*- coding: utf-8 -*-
"""
Generator for Grade 3 Item Bank (16 Expository Slots + 6 Common Foundation Slots)
Output: courseware/data/item_bank/g3_item_bank.json
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from item_bank_schema_helper import build_expository_slot, build_common_slot
import gen_item_bank_g3_g4

ITEM_BANK_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "data", "item_bank")
os.makedirs(ITEM_BANK_DIR, exist_ok=True)

# 1. Existing 8 slots and 6 common slots from gen_item_bank_g3_g4
g3_common_slots = gen_item_bank_g3_g4.build_g3_common_slots()
g3_exp_slots = gen_item_bank_g3_g4.build_g3_expository_slots_part1()

print(f"Loaded existing G3 expository slots: {len(g3_exp_slots)}")
print(f"Loaded existing G3 common slots: {len(g3_common_slots)}")

# 2. Add remaining 8 Expository slots for Grade 3: V3-1 ~ W5 (4 options per CSAT question)
g3_remaining_exp = [
    # Slot 9: V3-1
    build_expository_slot(
        grade_num=3,
        subskill_code="V3-1",
        subject="과학(동물의 생활 3-2)",
        unit="2. 동물의 생김새와 특징",
        concept="땅·물·하늘에 사는 동물들의 이동 방법과 다리 생김새",
        text_structure="분류·비교",
        structure_type_code="classification",
        passage_title="사는 곳에 따라 다른 동물의 이동 방법",
        paragraphs=[
            "동물들은 살아가는 환경에 알맞은 독특한 몸 구조와 이동 방법을 발달시켜 왔습니다. 땅에 사는 동물, 물에 사는 동물, 그리고 하늘을 날아다니는 동물은 이동하는 방식과 다리나 날개의 생김새가 서로 크게 다릅니다.",
            "먼저 땅에 사는 호랑이나 노루는 튼튼하고 긴 다리를 이용해 빠르게 뛰어다닙니다. 반면에 물에 사는 붕어나 고래는 다리 대신 물살을 가르기 쉬운 지느러미를 이용해 헤엄을 칩니다. 마지막으로 하늘을 나는 참새나 박쥐는 가볍고 넓은 날개를 퍼덕여 공중을 자유롭게 이동합니다.",
            "이처럼 동물의 이동 방법과 몸 구조는 사는 곳의 환경에 적응한 결과입니다. 글을 읽을 때는 설명하는 동물들의 특징과 제시된 관찰 삽화의 세부 모양이 정확히 일치하는지 꼼꼼하게 평가하며 읽어야 합니다."
        ],
        vocab_notes=[
            {"word": "적응", "definition": "생물이 주변 환경에 맞추어 몸의 구조나 행동 방식을 변화시키는 것"},
            {"word": "공중", "definition": "땅에서 높이 떨어진 하늘의 빈 공간"}
        ],
        visual_html="""<div class="p-3 bg-teal-50 rounded border border-teal-200">
          <h4 class="font-bold text-teal-900 mb-2">🐾 사는 환경에 따른 동물 이동 구조 분류표</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-teal-100"><th class="p-1 border border-teal-200">환경</th><th class="p-1 border border-teal-200">대표 동물</th><th class="p-1 border border-teal-200">이동 기관</th><th class="p-1 border border-teal-200">이동 방식</th></tr>
            <tr><td class="p-1 border border-teal-200 font-bold bg-white">땅</td><td class="p-1 border border-teal-200 bg-white">호랑이, 노루</td><td class="p-1 border border-teal-200 bg-white">튼튼한 다리</td><td class="p-1 border border-teal-200 bg-white">뛰어다님</td></tr>
            <tr><td class="p-1 border border-teal-200 font-bold bg-white">물</td><td class="p-1 border border-teal-200 bg-white">붕어, 고래</td><td class="p-1 border border-teal-200 bg-white">지느러미</td><td class="p-1 border border-teal-200 bg-white">헤엄침</td></tr>
            <tr><td class="p-1 border border-teal-200 font-bold bg-white">하늘</td><td class="p-1 border border-teal-200 bg-white">참새, 박쥐</td><td class="p-1 border border-teal-200 bg-white">넓은 날개</td><td class="p-1 border border-teal-200 bg-white">날아다님</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-v31-c1", "text": "물에 사는 붕어나 고래는 다리 대신 물살을 가르기 쉬운 지느러미를 이용해 헤엄을 칩니다", "role": "물속 이동 기관 특징", "para_idx": 1},
            {"cue_id": "g3-v31-c2", "text": "동물의 이동 방법과 몸 구조는 사는 곳의 환경에 적응한 결과입니다", "role": "환경 적응 핵심 결론", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "분류 매트릭스",
            "categories": ["땅에 사는 동물", "물에 사는 동물", "하늘을 나는 동물"],
            "features": {
                "땅": "튼튼한 다리 (뛰기)",
                "물": "지느러미 (헤엄치기)",
                "하늘": "넓은 날개 (날기)"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "세부 내용 확인",
                "stem": "글의 내용과 일치하지 않는 설명은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "반면에 물에 사는 붕어나 고래는 다리 대신 물살을 가르기 쉬운 지느러미를 이용해 헤엄을 칩니다.",
                "options": [
                    {"label": "①", "text": "호랑이와 노루는 긴 다리를 이용해 땅을 뛰어다닌다.", "is_correct": False, "formula": "D1", "explanation": "2문단 첫 문장에 명시된 일치 내용입니다."},
                    {"label": "②", "text": "물에 사는 고래는 네 다리로 바닷속을 걸어 다닌다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 고래는 다리 대신 지느러미를 이용해 헤엄친다고 설명했으므로 틀린 진술입니다."},
                    {"label": "③", "text": "참새와 박쥐는 날개를 퍼덕여 공중을 이동한다.", "is_correct": False, "formula": "D2", "explanation": "2문단 마지막 문장에 나오는 일치 내용입니다."},
                    {"label": "④", "text": "동물의 이동 구조는 살아가는 환경에 맞추어 적응한 결과이다.", "is_correct": False, "formula": "D4", "explanation": "3문단 중심 내용과 일치합니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "시각자료 적절성 평가",
                "stem": "글의 2문단 '물에 사는 동물' 설명 옆에 넣을 삽화로 가장 적절한 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "물에 사는 붕어나 고래는 다리 대신 물살을 가르기 쉬운 지느러미를 이용해 헤엄을 칩니다.",
                "options": [
                    {"label": "①", "text": "지느러미로 물살을 헤치며 헤엄치는 물고기의 세부 단면 그림", "is_correct": True, "formula": "정답", "explanation": "물에 사는 동물의 지느러미 기능과 이동 방식을 명확히 보여주는 가장 적절한 시각자료입니다."},
                    {"label": "②", "text": "나무 위에서 노래를 부르는 참새의 깃털 그림", "is_correct": False, "formula": "D5", "explanation": "하늘을 나는 동물에 관한 그림이므로 문단 주제와 맞지 않습니다."},
                    {"label": "③", "text": "초원을 전속력으로 달리는 얼룩말의 발굽 그림", "is_correct": False, "formula": "D3", "explanation": "땅에 사는 동물 그림이므로 물속 동물 설명과 어긋납니다."},
                    {"label": "④", "text": "실내 어항에 놓인 인공 자갈과 플라스틱 수초 장식 그림", "is_correct": False, "formula": "D6", "explanation": "동물의 몸 구조 및 이동 원리와 무관한 배경 장식물입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 동물이 서로 다른 몸 구조와 이동 방법을 갖게 된 궁극적인 원인은?",
                "options": [
                    {"label": "①", "text": "자신이 살아가는 주변 환경에 적응하기 위해", "is_correct": True},
                    {"label": "②", "text": "다른 동물보다 몸집을 더 크게 키우기 위해", "is_correct": False},
                    {"label": "③", "text": "더 많은 잠을 자기 위해", "is_correct": False},
                    {"label": "④", "text": "추운 겨울에 겨울잠을 자지 않기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답을 뒷받침하는 핵심 문장은 3문단의 어디에 있나요?",
                "options": [
                    {"label": "①", "text": "이처럼 동물의 이동 방법과 몸 구조는 사는 곳의 환경에 적응한 결과입니다.", "is_correct": True},
                    {"label": "②", "text": "글을 읽을 때는 설명하는 동물들의 특징과 제시된 관찰 삽화의 세부 모양이", "is_correct": False},
                    {"label": "③", "text": "정확히 일치하는지 꼼꼼하게 평가하며 읽어야 합니다.", "is_correct": False},
                    {"label": "④", "text": "동물들은 살아가는 환경에 알맞은 독특한 몸 구조와", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "동물 이동 방법 비교 요약문 완성하기",
            "guide": "땅, 물, 하늘에 사는 동물들의 이동 기관을 정리하여 세 문장으로 요약해 보세요.",
            "template": "땅에 사는 동물은 [       ]로 달리고, 물에 사는 동물은 [       ]로 헤엄칩니다. 그리고 하늘을 나는 동물은 [       ]로 날아다닙니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "분류 설명글을 읽을 때는 '환경'과 '이동 기관'을 표로 짝지어 읽어요."},
            "step1_2_drill": {"task": "동물 사진을 보고 알맞은 이동 기관(다리/지느러미/날개) 연결하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "고래는 다리가 아니라 지느러미를 이용해 물속을 이동합니다.", "answer": "O", "reason": "본문에 제시된 명확한 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 자연 관찰과 환경 적응",
            "situation": "동물 다큐멘터리나 동물원을 관람할 때",
            "parent_question": "오리와 독수리는 둘 다 새인데 왜 발 모양이 다르게 생겼을까?",
            "expected_answer": "오리는 물에 살아서 물갈퀴가 있고, 독수리는 하늘에서 먹이를 낚아채려고 날카로운 발톱이 있어요!",
            "coaching_tip": "환경과 생김새의 관계를 스스로 유추해 보도록 칭찬해 주세요."
        }
    ),

    # Slot 10: V3-2
    build_expository_slot(
        grade_num=3,
        subskill_code="V3-2",
        subject="사회(교통·통신 3-1)",
        unit="3. 교통과 통신의 발달",
        concept="옛날과 오늘날의 통신 수단 발달 사실 확인",
        text_structure="비교·대조 + 인과",
        structure_type_code="comparison",
        passage_title="봉수대에서 스마트폰까지 통신의 발달",
        paragraphs=[
            "통신이란 소식이나 정보를 다른 사람과 주고받는 모든 방법을 말합니다. 사람이 직접 걸어가서 소식을 전하던 먼 옛날부터 오늘날까지 통신 수단은 눈부시게 발전해 왔습니다.",
            "옛날에는 위급한 소식을 전하기 위해 산꼭대기에 봉수대를 세우고 낮에는 연기를, 밤에는 횃불을 피워 올렸습니다. 또한 중요한 소식을 편지에 적어 파발마라는 말을 타고 빠르게 달리기도 했습니다. 하지만 날씨가 흐리거나 거리가 너무 멀면 소식이 늦게 도착하는 한계가 있었습니다.",
            "오늘날에는 인터넷과 스마트폰이 발달하여 전 세계 어디든 1초 만에 글자와 사진, 영상을 주고받을 수 있습니다. 통신 수단이 발전하면서 사람들의 생활은 상상할 수 없을 만큼 편리하고 안전해졌습니다."
        ],
        vocab_notes=[
            {"word": "봉수대", "definition": "옛날에 밤에는 횃불, 낮에는 연기로 급한 군사 소식을 전하던 시설"},
            {"word": "파발마", "definition": "공문서나 중요한 소식을 신속히 전하기 위해 역마다 마련해 두었던 말"}
        ],
        visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
          <h4 class="font-bold text-amber-900 mb-2">📡 옛날 vs 오늘날 통신 수단 객관적 비교</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-amber-100"><th class="p-1 border border-amber-200">시대</th><th class="p-1 border border-amber-200">주요 통신 수단</th><th class="p-1 border border-amber-200">전달 속도</th><th class="p-1 border border-amber-200">한계 및 특징</th></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">옛날</td><td class="p-1 border border-amber-200 bg-white">봉수(연기·횃불), 파발마</td><td class="p-1 border border-amber-200 bg-white">수 시간 ~ 수일</td><td class="p-1 border border-amber-200 bg-white">날씨 영향, 먼 거리 지연</td></tr>
            <tr><td class="p-1 border border-amber-200 font-bold bg-white">오늘날</td><td class="p-1 border border-amber-200 bg-white">스마트폰, 인터넷</td><td class="p-1 border border-amber-200 bg-white">즉시 (1초 이내)</td><td class="p-1 border border-amber-200 bg-white">영상·사진 전 세계 동시 전송</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-v32-c1", "text": "산꼭대기에 봉수대를 세우고 낮에는 연기를, 밤에는 횃불을 피워 올렸습니다", "role": "봉수대 작동 원리 사실", "para_idx": 1},
            {"cue_id": "g3-v32-c2", "text": "전 세계 어디든 1초 만에 글자와 사진, 영상을 주고받을 수 있습니다", "role": "현대 통신 사실", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "시대별 비교·대조표",
            "features": {
                "옛날": ["봉수대 (낮 연기, 밤 횃불)", "파발마 (말 타고 이동)", "날씨 영향 큼"],
                "오늘날": ["스마트폰·인터넷", "1초 전송", "시공간 제약 없음"]
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "사실과 과장 변별",
                "stem": "글의 내용에 근거할 때, 옛날 통신 수단에 대한 '객관적 사실'로 바른 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "낮에는 연기를, 밤에는 횃불을 피워 올렸습니다.",
                "options": [
                    {"label": "①", "text": "옛날 사람들은 봉수대로 전 세계 사람들에게 사진을 보냈다.", "is_correct": False, "formula": "D5", "explanation": "봉수대는 사진을 보낼 수 없는 원시적 신호 수단입니다."},
                    {"label": "②", "text": "봉수대는 낮에는 연기로, 밤에는 횃불로 신호를 보냈다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 명확히 기록된 역사적 사실입니다."},
                    {"label": "③", "text": "파발마는 하늘을 날아서 1초 만에 편지를 전달했다.", "is_correct": False, "formula": "D1", "explanation": "말이 하늘을 날아다니는 것은 동화 속 허구입니다."},
                    {"label": "④", "text": "옛날 통신 수단은 날씨의 영향을 전혀 받지 않았다.", "is_correct": False, "formula": "D3", "explanation": "날씨가 흐리면 신호가 늦어지는 한계가 있었습니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "인과 관계 파악",
                "stem": "현대 통신 수단이 발전하면서 일어난 가장 큰 생활의 변화는?",
                "target_para_idx": 2,
                "spotlight_quote": "통신 수단이 발전하면서 사람들의 생활은 상상할 수 없을 만큼 편리하고 안전해졌습니다.",
                "options": [
                    {"label": "①", "text": "사람들이 더 이상 말을 타고 다닐 필요가 없게 되었다.", "is_correct": False, "formula": "D4", "explanation": "교통 수단과 통신 수단을 혼동한 오답입니다."},
                    {"label": "②", "text": "정보를 전 세계 어디서든 신속하게 주고받아 생활이 편리해졌다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 기술된 현대 통신 발전의 결과입니다."},
                    {"label": "③", "text": "산꼭대기 봉수대의 숫자가 예전보다 수백 배 늘어났다.", "is_correct": False, "formula": "D2", "explanation": "봉수대는 오늘날 통신에 사용되지 않습니다."},
                    {"label": "④", "text": "사람들이 서로 소식을 주고받는 일이 완전히 사라졌다.", "is_correct": False, "formula": "D3", "explanation": "오히려 소식을 주고받는 일이 폭발적으로 증가했습니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 옛날 봉수대 통신이 지녔던 가장 결정적인 한계는 무엇이었나요?",
                "options": [
                    {"label": "①", "text": "날씨가 흐리거나 거리가 멀면 전달이 늦어졌다.", "is_correct": True},
                    {"label": "②", "text": "연기를 피우면 산불이 나서 금지되었다.", "is_correct": False},
                    {"label": "③", "text": "봉수대를 지을 돌이 부족했다.", "is_correct": False},
                    {"label": "④", "text": "낮에는 횃불을 피우지 못해 불법이었다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 명확한 근거 문장은?",
                "options": [
                    {"label": "①", "text": "하지만 날씨가 흐리거나 거리가 너무 멀면 소식이 늦게 도착하는 한계가 있었습니다.", "is_correct": True},
                    {"label": "②", "text": "통신이란 소식이나 정보를 다른 사람과 주고받는 모든 방법을 말합니다.", "is_correct": False},
                    {"label": "③", "text": "오늘날에는 인터넷과 스마트폰이 발달하여", "is_correct": False},
                    {"label": "④", "text": "사람이 직접 걸어가서 소식을 전하던 먼 옛날부터", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "통신 수단 발달 비교 보고문 쓰기",
            "guide": "옛날의 봉수대와 오늘날 스마트폰의 차이점을 한 문단으로 대조하여 써 보세요.",
            "template": "옛날에는 [       ]를 피워 소식을 전했지만 날씨의 영향을 받았습니다. 하지만 오늘날에는 [       ]을 이용하여 전 세계에 즉시 소식을 전할 수 있습니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "시대 변화에 따른 설명글은 '과거의 한계'와 '현재의 개선점'을 짝지어 정리해요."},
            "step1_2_drill": {"task": "봉수대(과거)와 스마트폰(현재)의 속도 및 특징 카드 분류하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "봉수대는 밤에는 횃불을 피워 신호를 전달했습니다.", "answer": "O", "reason": "본문에 기록된 역사적 사실입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 소식을 전하는 방법",
            "situation": "할머니께 영상 통화를 걸어 안부를 여쭙고 난 뒤",
            "parent_question": "만약 스마트폰이 없던 조선 시대였다면 멀리 사시는 할머니께 어떻게 소식을 전했을까?",
            "expected_answer": "편지를 써서 말을 탄 사람(파발마)에게 부탁하거나 직접 걸어가서 전해야 했을 거예요!",
            "coaching_tip": "기술 발달로 편리해진 일상에 감사하고 역사적 맥락을 이해하도록 도와주세요."
        }
    ),

    # Slot 11: V3-3
    build_expository_slot(
        grade_num=3,
        subskill_code="V3-3",
        subject="과학(지표의 변화 3-2)",
        unit="3. 지표의 변화",
        concept="흙의 생성 과정과 지표의 변화 (자료 ㉮·㉯)",
        text_structure="인과 + 과정",
        structure_type_code="causal",
        passage_title="단단한 바위가 부드러운 흙이 되기까지 (자료 ㉮와 ㉯)",
        paragraphs=[
            "[자료 ㉮] 우리가 밟고 다니는 흙은 처음부터 흙이었던 것이 아닙니다. 거대한 바위와 돌이 오랜 세월 동안 비바람을 맞고 햇빛에 데워졌다 식기를 반복하면서 차츰 금이 가고 잘게 부서져 만들어졌습니다. 이렇게 바위가 부서지는 현상을 풍화 작용이라고 합니다.",
            "[자료 ㉯] 잘게 부서진 돌가루에 나뭇잎이나 죽은 곤충과 같은 생물질이 섞여 썩으면 식물이 잘 자라는 기름진 흙이 됩니다. 바위 표면의 틈 사이에 식물의 뿌리가 파고들면 바위가 더 빠르게 쪼개지기도 합니다.",
            "두 자료를 함께 살펴보면, 흙은 단순히 돌가루만 모인 것이 아니라 '풍화로 부서진 암석 가루(자료 ㉮)'에 '생물이 썩어 생긴 부식물(자료 ㉯)'이 합쳐져 만들어진 소중한 자연의 산물임을 알 수 있습니다."
        ],
        vocab_notes=[
            {"word": "풍화 작용", "definition": "바위나 돌이 공기, 물, 생물 등의 작용으로 잘게 부서지는 현상"},
            {"word": "부식물", "definition": "식물이나 동물의 유해가 미생물에 의해 분해되어 흙과 섞인 물질"}
        ],
        visual_html="""<div class="p-3 bg-stone-50 rounded border border-stone-200">
          <h4 class="font-bold text-stone-900 mb-2">⛰️ 흙 생성 4단계 과정 다이어그램</h4>
          <div class="grid grid-cols-4 gap-1 text-xs text-center">
            <div class="p-1.5 bg-white rounded border border-stone-200">1단계<br><strong>큰 바위</strong><br>단단한 암석</div>
            <div class="p-1.5 bg-white rounded border border-stone-200">2단계<br><strong>비바람·금</strong><br>바위 쪼개짐</div>
            <div class="p-1.5 bg-white rounded border border-stone-200">3단계<br><strong>돌가루</strong><br>잘게 풍화</div>
            <div class="p-1.5 bg-white rounded border border-stone-200">4단계<br><strong>생물질 혼합</strong><br>기름진 흙 완성</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-v33-c1", "text": "바위가 부서지는 현상을 풍화 작용이라고 합니다", "role": "풍화 작용 개념", "para_idx": 0},
            {"cue_id": "g3-v33-c2", "text": "잘게 부서진 돌가루에 나뭇잎이나 죽은 곤충과 같은 생물질이 섞여", "role": "기름진 흙의 성분", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "다중 자료 통합 도식",
            "source_a": "자료 ㉮: 바위의 풍화 (물리적 부서짐)",
            "source_b": "자료 ㉯: 생물질의 부식 혼합 (생물학적 작용)",
            "synthesis": "통합 결론: 암석 가루 + 썩은 생물질 = 식물이 자라는 기름진 흙"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "다중 자료 정보 통합",
                "stem": "자료 ㉮와 자료 ㉯를 바탕으로 '기름진 흙'이 만들어지는 조건을 가장 올바르게 정리한 것은?",
                "target_para_idx": 2,
                "spotlight_quote": "두 자료를 함께 살펴보면, 흙은 단순히 돌가루만 모인 것이 아니라",
                "options": [
                    {"label": "①", "text": "바위가 잘게 부서진 돌가루에 썩은 생물질이 섞여야 한다.", "is_correct": True, "formula": "정답", "explanation": "자료 ㉮의 풍화 돌가루와 자료 ㉯의 생물질 혼합을 모두 통합한 정확한 진술입니다."},
                    {"label": "②", "text": "공장에서 화학 비료를 섞어 플라스틱 가루를 부어야 한다.", "is_correct": False, "formula": "D1", "explanation": "자연 흙 생성과 무관한 왜곡입니다."},
                    {"label": "③", "text": "바위가 부서지지 않고 거대한 암석 상태를 유지해야 한다.", "is_correct": False, "formula": "D3", "explanation": "바위가 부서져야 흙이 되므로 정반대 진술입니다."},
                    {"label": "④", "text": "오직 비바람만 불고 식물이나 곤충은 절대 닿지 않아야 한다.", "is_correct": False, "formula": "D4", "explanation": "생물질이 섞여야 기름진 흙이 된다는 자료 ㉯와 모순됩니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "세부 인과 추론",
                "stem": "자료 ㉯에서 식물의 뿌리가 바위 틈에 파고들 때 일어나는 현상은?",
                "target_para_idx": 1,
                "spotlight_quote": "바위 표면의 틈 사이에 식물의 뿌리가 파고들면 바위가 더 빠르게 쪼개지기도 합니다.",
                "options": [
                    {"label": "①", "text": "바위가 쇠처럼 단단해져서 절대 부서지지 않는다.", "is_correct": False, "formula": "D3", "explanation": "바위가 더 빠르게 쪼개진다고 설명했습니다."},
                    {"label": "②", "text": "바위가 더 빠르게 쪼개져 부서진다.", "is_correct": True, "formula": "정답", "explanation": "식물 뿌리가 바위를 쪼개는 생물학적 풍화 작용의 직접적 결과입니다."},
                    {"label": "③", "text": "바위가 물에 녹아 투명한 액체로 변한다.", "is_correct": False, "formula": "D5", "explanation": "상상 속 과장된 진술입니다."},
                    {"label": "④", "text": "식물의 뿌리가 즉시 돌로 변해 굳어진다.", "is_correct": False, "formula": "D2", "explanation": "사실과 반대되는 비과학적 설명입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 바위와 돌이 오랜 세월 부서지는 자연 현상을 일컫는 과학 용어는?",
                "options": [
                    {"label": "①", "text": "풍화 작용", "is_correct": True},
                    {"label": "②", "text": "증발 현상", "is_correct": False},
                    {"label": "③", "text": "지진 활동", "is_correct": False},
                    {"label": "④", "text": "화산 폭발", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 용어가 정의된 본문 구절은?",
                "options": [
                    {"label": "①", "text": "이렇게 바위가 부서지는 현상을 풍화 작용이라고 합니다.", "is_correct": True},
                    {"label": "②", "text": "우리가 밟고 다니는 흙은 처음부터 흙이었던 것이 아닙니다.", "is_correct": False},
                    {"label": "③", "text": "잘게 부서진 돌가루에 나뭇잎이나 죽은 곤충과 같은", "is_correct": False},
                    {"label": "④", "text": "거대한 바위와 돌이 오랜 세월 동안 비바람을 맞고", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "흙의 생성 과정 인과 보고서 쓰기",
            "guide": "자료 ㉮와 ㉯의 내용을 엮어 단단한 바위가 흙이 되는 과정을 인과 접속어로 써 보세요.",
            "template": "바위가 비바람을 맞아 [       ]으로 부서집니다. 그 까닭에 생긴 돌가루에 [       ]이 섞여 비로소 기름진 흙이 완성됩니다."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "두 개 이상의 자료를 읽을 때는 각 자료의 핵심 단서를 찾아 통합 결론을 도출해요."},
            "step1_2_drill": {"task": "자료 ㉮(풍화 작용)와 자료 ㉯(부식물 혼합)의 핵심어 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "흙은 돌가루뿐만 아니라 생물질이 섞여야 비옥해집니다.", "answer": "O", "reason": "두 자료의 통합 결론입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 화분의 흙 만져보기",
            "situation": "베란다 화분에 식물을 심거나 분갈이를 할 때",
            "parent_question": "화분에 담긴 부드러운 흙은 아주 먼 옛날에 무엇이었을까?",
            "expected_answer": "커다란 바위가 비바람에 부서지고 나뭇잎이 썩어서 섞인 거래요!",
            "coaching_tip": "주변 사물의 오랜 기원을 과학적으로 상상해 볼 수 있도록 이끌어 주세요."
        }
    ),

    # Slot 12: W1
    build_expository_slot(
        grade_num=3,
        subskill_code="W1",
        subject="과학(물질의 상태 3-1)",
        unit="4. 우리 주변의 물질",
        concept="‘고체·액체·기체’ 중 한 가지 물질 상태 소개 계획하기",
        text_structure="분류 + 계획",
        structure_type_code="classification",
        passage_title="물질의 세 가지 상태와 글쓰기 계획",
        paragraphs=[
            "우리 주변에 있는 모든 물질은 단단한 고체, 흐르는 액체, 눈에 보이지 않는 기체 중 하나의 상태로 존재합니다. 물질의 상태를 설명하는 글을 쓸 때는 먼저 예상 독자를 정하고 주제를 구체적으로 좁히는 계획을 세워야 합니다.",
            "예를 들어 3학년 동생들에게 '기체'를 소개하려 한다면, 독자가 이해하기 쉬운 공기나 풍선 속 헬륨가스를 구체적 제재로 정해야 합니다. 또한 글의 목적을 '눈에 안 보이지만 공간을 차지하는 기체의 성질 알려 주기'로 명확히 설정합니다.",
            "이처럼 [예상 독자 분석 ➔ 화제 좁히기 ➔ 글의 목적과 제목 정하기]라는 3단계 깔때기 계획을 거치면 훨씬 짜임새 있는 설명글을 쓸 수 있습니다."
        ],
        vocab_notes=[
            {"word": "물질", "definition": "물체를 이루는 고유한 본바탕이나 재료"},
            {"word": "제재", "definition": "글이나 예술 작품의 바탕이 되는 구체적인 재료나 대상"}
        ],
        visual_html="""<div class="p-3 bg-cyan-50 rounded border border-cyan-200">
          <h4 class="font-bold text-cyan-900 mb-2">🎯 3단계 글쓰기 계획 깔때기 모델</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1.5 bg-white rounded border border-cyan-200"><strong>1단계 독자 분석:</strong> 3학년 친구들 (기체 개념을 어려워함)</div>
            <div class="p-1.5 bg-white rounded border border-cyan-200"><strong>2단계 화제 좁히기:</strong> 물질의 상태 ➔ 기체 ➔ 눈에 안 보이는 공기</div>
            <div class="p-1.5 bg-white rounded border border-cyan-200"><strong>3단계 목적·제목:</strong> 공간을 차지하는 공기의 성질 알리기</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-w1-c1", "text": "독자가 이해하기 쉬운 공기나 풍선 속 헬륨가스를 구체적 제재로 정해야 합니다", "role": "화제 좁히기 방법", "para_idx": 1},
            {"cue_id": "g3-w1-c2", "text": "[예상 독자 분석 ➔ 화제 좁히기 ➔ 글의 목적과 제목 정하기]", "role": "3단계 계획 공식", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "글쓰기 계획 깔때기",
            "reader": "물질을 배우는 3학년 친구들",
            "broad_topic": "물질의 상태 (고체/액체/기체)",
            "narrow_topic": "기체의 성질 (풍선과 공기)",
            "purpose": "보이지 않는 공기가 공간을 차지함을 설명하기"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "글쓰기 계획 단계 확인",
                "stem": "글에서 제시한 3단계 글쓰기 계획의 올바른 순서는?",
                "target_para_idx": 2,
                "spotlight_quote": "[예상 독자 분석 ➔ 화제 좁히기 ➔ 글의 목적과 제목 정하기]라는 3단계 깔때기 계획을 거치면",
                "options": [
                    {"label": "①", "text": "퇴고하기 ➔ 인쇄하기 ➔ 독자 찾기", "is_correct": False, "formula": "D3", "explanation": "글을 다 쓴 뒤의 출판 단계입니다."},
                    {"label": "②", "text": "예상 독자 분석 ➔ 화제 좁히기 ➔ 글의 목적과 제목 정하기", "is_correct": True, "formula": "정답", "explanation": "본문 3문단에 명시된 체계적 계획 3단계 순서입니다."},
                    {"label": "③", "text": "제목 정하기 ➔ 글 전체 쓰기 ➔ 제재 삭제하기", "is_correct": False, "formula": "D4", "explanation": "계획 없이 성급하게 쓰는 잘못된 방식입니다."},
                    {"label": "④", "text": "사진 오리기 ➔ 색칠하기 ➔ 화제 넓히기", "is_correct": False, "formula": "D1", "explanation": "글쓰기 계획과 무관한 미술 활동입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "독자 맞춤 제재 선정",
                "stem": "초등 저학년 동생들에게 '기체'의 성질을 설명할 때 가장 알맞은 친숙한 제재는?",
                "target_para_idx": 1,
                "spotlight_quote": "독자가 이해하기 쉬운 공기나 풍선 속 헬륨가스를 구체적 제재로 정해야 합니다.",
                "options": [
                    {"label": "①", "text": "우주 로켓의 복잡한 액체 수소 분자 구조식", "is_correct": False, "formula": "D5", "explanation": "독자의 눈높이에 맞지 않는 난해한 제재입니다."},
                    {"label": "②", "text": "풍선 속에 가득 찬 공기와 비눗방울", "is_correct": True, "formula": "정답", "explanation": "독자가 일상에서 쉽게 경험할 수 있는 친숙한 기체 제재입니다."},
                    {"label": "③", "text": "땅속 깊은 곳에 묻힌 단단한 화강암 바위", "is_correct": False, "formula": "D2", "explanation": "기체가 아니라 고체에 해당하는 제재입니다."},
                    {"label": "④", "text": "유리컵에 담긴 시원한 보리차 한 잔", "is_correct": False, "formula": "D2", "explanation": "액체에 해당하는 제재입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 글을 쓰기 전에 예상 독자를 분석해야 하는 가장 큰 까닭은?",
                "options": [
                    {"label": "①", "text": "독자의 이해 수준에 맞는 쉬운 낱말과 친숙한 예를 고르기 위해", "is_correct": True},
                    {"label": "②", "text": "독자에게 글짓기 시험을 보게 하기 위해", "is_correct": False},
                    {"label": "③", "text": "독자의 전화번호를 알아내기 위해", "is_correct": False},
                    {"label": "④", "text": "독자가 쓴 글을 베끼기 위해", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 문장은?",
                "options": [
                    {"label": "①", "text": "독자가 이해하기 쉬운 공기나 풍선 속 헬륨가스를 구체적 제재로 정해야 합니다.", "is_correct": True},
                    {"label": "②", "text": "우리 주변에 있는 모든 물질은 단단한 고체,", "is_correct": False},
                    {"label": "③", "text": "흐르는 액체, 눈에 보이지 않는 기체 중 하나의 상태로 존재합니다.", "is_correct": False},
                    {"label": "④", "text": "글의 목적을 '눈에 안 보이지만 공간을 차지하는", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "나만의 물질 상태 설명 계획서 작성하기",
            "guide": "내가 소개하고 싶은 물질 상태(고체/액체/기체) 중 하나를 골라 계획표를 채워 보세요.",
            "template": "1. 독자: [우리 반 친구들] / 2. 선택한 상태: [고체/액체/기체] / 3. 구체적 예시 물건: [       ] / 4. 글의 제목: [       ]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "글을 쓰기 전에 독자의 눈높이와 다룰 구체적 대상을 먼저 확정해요."},
            "step1_2_drill": {"task": "독자 대상별(유치원생 vs 초3 vs 전문가) 알맞은 설명 제재 연결하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "설명글을 쓸 때는 광범위한 주제를 구체적 제재로 좁히는 것이 좋습니다.", "answer": "O", "reason": "글의 명확성을 높이는 핵심 계획 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 누구에게 쓰는 글일까?",
            "situation": "아이가 숙제나 발표 준비를 시작할 때",
            "parent_question": "이번에 쓸 글을 읽을 사람은 누구니? 그 친구가 모르는 단어는 어떤 게 있을까?",
            "expected_answer": "친구들이 기체라는 말을 어려워할 수 있으니까 공기나 풍선 이야기로 시작할래요!",
            "coaching_tip": "독자의 입장에서 생각하는 공감적 글쓰기 태도를 칭찬해 주세요."
        }
    ),

    # Slot 13: W2
    build_expository_slot(
        grade_num=3,
        subskill_code="W2",
        subject="사회(우리 고장의 모습 3-1)",
        unit="1. 우리가 살아가는 곳",
        concept="우리 고장의 문화유산 자료 수집 및 재진술 메모",
        text_structure="열거 + 재진술",
        structure_type_code="description",
        passage_title="고장의 문화유산 조사와 똑똑한 메모 쓰기",
        paragraphs=[
            "우리 고장에는 조상들의 슬기와 숨결이 담긴 귀중한 문화유산이 곳곳에 남아 있습니다. 고장의 문화유산을 소개하는 글을 쓰려면 박물관 안내책자나 누리집에서 정확한 사실 자료를 수집해야 합니다.",
            "자료를 수집할 때 안내책자의 문장을 그대로 베껴 쓰면 표절이 되며 읽는 사람도 지루해합니다. 따라서 책자의 어려운 한자어나 전문 용어를 초등학생이 이해하기 쉬운 말로 바꾸어 요약 메모(재진술)해야 합니다.",
            "예를 들어 '성곽의 둘레는 견고하게 축조되었다'는 문장을 보았다면, '돌을 튼튼하게 쌓아 올려 성벽을 완성했다'처럼 자신의 말로 바꾸어 기록해야 훌륭한 설명글의 밑천이 됩니다."
        ],
        vocab_notes=[
            {"word": "문화유산", "definition": "조상들이 물려준 역사적·예술적 가치가 있는 유물이나 유적"},
            {"word": "재진술", "definition": "원래 글의 뜻을 해치지 않으면서 다른 알기 쉬운 말로 바꾸어 표현하는 것"}
        ],
        visual_html="""<div class="p-3 bg-emerald-50 rounded border border-emerald-200">
          <h4 class="font-bold text-emerald-900 mb-2">📝 그대로 베끼기 vs 알기 쉽게 재진술 메모</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-emerald-100"><th class="p-1 border border-emerald-200">구분</th><th class="p-1 border border-emerald-200">원문 (안내책자 전문 용어)</th><th class="p-1 border border-emerald-200">재진술 메모 (내 말로 요약)</th></tr>
            <tr><td class="p-1 border border-emerald-200 font-bold bg-white">나쁜 예</td><td class="p-1 border border-emerald-200 bg-white">성곽을 견고하게 축조하였다</td><td class="p-1 border border-emerald-200 bg-white">성곽을 견고하게 축조하였다 (베끼기)</td></tr>
            <tr><td class="p-1 border border-emerald-200 font-bold bg-white">좋은 예</td><td class="p-1 border border-emerald-200 bg-white">성곽을 견고하게 축조하였다</td><td class="p-1 border border-emerald-200 bg-white">돌을 튼튼하게 쌓아 성벽을 지었다</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-w2-c1", "text": "안내책자의 문장을 그대로 베껴 쓰면 표절이 되며", "role": "베껴 쓰기의 문제점", "para_idx": 1},
            {"cue_id": "g3-w2-c2", "text": "'돌을 튼튼하게 쌓아 올려 성벽을 완성했다'처럼 자신의 말로 바꾸어 기록해야", "role": "바람직한 재진술 예시", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "자료 수집 포트폴리오",
            "source": "고장 박물관 안내책자",
            "original_quote": "조선 시대 관아 건물로서 정교한 목조 양식을 보존함",
            "my_paraphrase": "조선 시대 나랏일을 보던 관청으로, 나무를 정성껏 끼워 맞춰 지었습니다."
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "재진술 원칙 확인",
                "stem": "자료를 수집하고 메모할 때 가장 올바른 태도는 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "따라서 책자의 어려운 한자어나 전문 용어를 초등학생이 이해하기 쉬운 말로 바꾸어 요약 메모(재진술)해야 합니다.",
                "options": [
                    {"label": "①", "text": "안내책자의 글자 토씨 하나 바꾸지 않고 전부 그대로 베낀다.", "is_correct": False, "formula": "D1", "explanation": "표절이 되며 글의 가치가 떨어지는 나쁜 태도입니다."},
                    {"label": "②", "text": "어려운 전문 용어를 자신의 쉬운 말로 바꾸어 요약 메모한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에서 강조한 올바른 재진술(Paraphrasing) 원칙입니다."},
                    {"label": "③", "text": "사실과 상관없이 거짓된 역사를 상상으로 지어낸다.", "is_correct": False, "formula": "D5", "explanation": "문화유산 설명에 거짓을 적으면 안 됩니다."},
                    {"label": "④", "text": "안내책자의 내용을 읽지 않고 사진만 오려 붙인다.", "is_correct": False, "formula": "D6", "explanation": "내용을 이해하지 못하는 부실한 자료 수집입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "어휘 재진술 적절성",
                "stem": "'성곽의 둘레는 견고하게 축조되었다'를 자신의 말로 가장 알맞게 바꾼 것은?",
                "target_para_idx": 2,
                "spotlight_quote": "'돌을 튼튼하게 쌓아 올려 성벽을 완성했다'처럼 자신의 말로 바꾸어 기록해야 훌륭한 설명글의 밑천이 됩니다.",
                "options": [
                    {"label": "①", "text": "성곽이 바람에 날려 모래처럼 사라졌다.", "is_correct": False, "formula": "D3", "explanation": "원문의 뜻과 정반대되는 왜곡입니다."},
                    {"label": "②", "text": "돌을 튼튼하게 쌓아 올려 성벽을 완성했다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 제시된 정확하고 쉬운 재진술 문장입니다."},
                    {"label": "③", "text": "성곽의 둘레는 견고하게 축조되었다.", "is_correct": False, "formula": "D1", "explanation": "어려운 한자어를 그대로 베껴 쓴 문장입니다."},
                    {"label": "④", "text": "성벽 주변에서 신나게 축구를 즐겼다.", "is_correct": False, "formula": "D2", "explanation": "원문의 의미와 무관한 내용입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 책자의 문장을 그대로 베끼지 않고 내 말로 바꾸어 쓰면 어떤 좋은 점이 있나요?",
                "options": [
                    {"label": "①", "text": "표절을 피하고 글의 내용을 깊이 이해하여 읽는 사람에게 쉽게 전달할 수 있다.", "is_correct": True},
                    {"label": "②", "text": "글의 분량을 무조건 10배 이상 늘릴 수 있다.", "is_correct": False},
                    {"label": "③", "text": "조사할 필요가 아예 없어진다.", "is_correct": False},
                    {"label": "④", "text": "책을 사지 않아도 된다.", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "자료를 수집할 때 안내책자의 문장을 그대로 베껴 쓰면 표절이 되며 읽는 사람도 지루해합니다.", "is_correct": True},
                    {"label": "②", "text": "우리 고장에는 조상들의 슬기와 숨결이 담긴", "is_correct": False},
                    {"label": "③", "text": "귀중한 문화유산이 곳곳에 남아 있습니다.", "is_correct": False},
                    {"label": "④", "text": "고장의 문화유산을 소개하는 글을 쓰려면", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "문화유산 안내문 쉬운 말로 재진술하기",
            "guide": "어려운 안내 문장을 읽고 초등학교 3학년 친구가 이해할 수 있는 쉬운 말로 바꾸어 써 보세요.",
            "template": "원문: 본 탑은 석회암 재질로 고대 장인의 섬세한 기교를 과시한다. ➔ 재진술: [이 탑은 부드러운 돌로 만들어졌으며, 옛날 장인이 정성껏 아름답게 조각했습니다.]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "자료를 읽은 뒤에는 책을 덮고 내가 이해한 쉬운 말로 공책에 메모해요."},
            "step1_2_drill": {"task": "어려운 한자어(견고하다, 축조, 유물)를 쉬운 순우리말과 짝짓기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "조사한 자료의 전문 용어는 내 말로 바꾸어 메모하는 것이 바람직합니다.", "answer": "O", "reason": "올바른 설명문 작문의 기본 수칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 내 말로 설명하기",
            "situation": "박물관이나 유적지를 다녀온 저녁 식사 자리에서",
            "parent_question": "오늘 박물관 안내판에서 본 어려운 설명 중에 기억나는 것을 네 말로 쉽게 설명해 줄래?",
            "expected_answer": "'조선 시대 도자기'는 흙을 빚어 뜨거운 불에 구워 만든 아름다운 그릇이라는 뜻이었어요!",
            "coaching_tip": "아이가 스스로의 언어로 풀어서 설명할 때 어휘력과 이해력이 급격히 성장합니다."
        }
    ),

    # Slot 14: W3
    build_expository_slot(
        grade_num=3,
        subskill_code="W3",
        subject="과학(자석의 이용 3-1)",
        unit="3. 자석의 이용",
        concept="‘자석의 성질과 이용’ 처음-가운데-끝 3단 개요 짜기",
        text_structure="순서 + 분류",
        structure_type_code="sequence",
        passage_title="자석의 신비한 성질과 3단 구성 개요 짜기",
        paragraphs=[
            "설명글은 읽는 이가 내용을 체계적으로 파악할 수 있도록 '처음-가운데-끝'의 3단 구성으로 개요를 조직하는 것이 표준적입니다. 글을 쓰기 전에 각 부분에 들어갈 중심 내용을 표로 정리하면 글의 뼈대가 튼튼해집니다.",
            "'자석의 성질과 이용'을 주제로 개요를 짠다면, [처음]에는 자석의 정의와 흥미 유발 질문을 넣습니다. [가운데]에는 자석의 두 극(N극과 S극)의 성질과 나침반의 원리를 2개 문단으로 나누어 구체적으로 설명합니다. 마지막으로 [끝]에는 자석이 우리 생활을 편리하게 해 준다는 의의와 전체 요약을 제시합니다.",
            "이렇게 중심 문장과 뒷받침 문장의 위계를 명확히 세운 개요표를 먼저 작성하면, 글을 쓰는 도중에 주제에서 벗어나는 실수를 막을 수 있습니다."
        ],
        vocab_notes=[
            {"word": "개요", "definition": "글을 쓰기 전에 전체의 줄거리나 중요한 뼈대를 간추린 것"},
            {"word": "3단 구성", "definition": "글을 '처음-가운데-끝'의 세 덩어리로 짜임새 있게 나누는 구조"}
        ],
        visual_html="""<div class="p-3 bg-violet-50 rounded border border-violet-200">
          <h4 class="font-bold text-violet-900 mb-2">📋 자석 설명문 3단 구성(처음-가운데-끝) 개요표</h4>
          <div class="space-y-1 text-xs">
            <div class="p-1.5 bg-white rounded border border-violet-200"><strong>[처음]</strong> 자석이란 무엇인가? (철을 끌어당기는 신기한 물건 소개)</div>
            <div class="p-1.5 bg-white rounded border border-violet-200"><strong>[가운데 1]</strong> 자석의 극 (N극과 S극은 서로 당기고, 같은 극은 믐)</div>
            <div class="p-1.5 bg-white rounded border border-violet-200"><strong>[가운데 2]</strong> 생활 속 자석의 쓰임 (나침반, 필통 뚜껑, 냉장고 자석)</div>
            <div class="p-1.5 bg-white rounded border border-violet-200"><strong>[끝]</strong> 자석의 가치 요약과 미래의 편리한 자석 기술</div>
          </div>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-w3-c1", "text": "'처음-가운데-끝'의 3단 구성으로 개요를 조직하는 것이 표준적입니다", "role": "3단 구성 기본 원칙", "para_idx": 0},
            {"cue_id": "g3-w3-c2", "text": "중심 문장과 뒷받침 문장의 위계를 명확히 세운 개요표를 먼저 작성하면", "role": "개요표의 효과", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "3단 구성 개요 조직도",
            "sections": {
                "처음": "자석 소개 및 호기심 유발",
                "가운데": "자석의 N극·S극 성질 + 생활 속 이용 사례",
                "끝": "내용 전체 요약 및 맺음말"
            }
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "글의 구성 요소 파악",
                "stem": "글의 2문단에 제시된 개요에서 [가운데] 부분에 들어가기에 가장 알맞은 내용은?",
                "target_para_idx": 1,
                "spotlight_quote": "[가운데]에는 자석의 두 극(N극과 S극)의 성질과 나침반의 원리를 2개 문단으로 나누어 구체적으로 설명합니다.",
                "options": [
                    {"label": "①", "text": "자석의 두 극(N극·S극)의 성질과 나침반의 원리", "is_correct": True, "formula": "정답", "explanation": "2문단에서 [가운데]에 들어갈 구체적 설명 내용으로 명시되었습니다."},
                    {"label": "②", "text": "자석의 발명가를 찾아가서 사인받은 일기", "is_correct": False, "formula": "D5", "explanation": "설명문의 본론 내용으로 적합하지 않은 사적 일화입니다."},
                    {"label": "③", "text": "자석 설명글의 원고료와 판매 가격 안내", "is_correct": False, "formula": "D1", "explanation": "글의 내용과 완전히 동떨어진 오답입니다."},
                    {"label": "④", "text": "글을 다 쓴 뒤 친구들과 나눈 축구 경기 결과", "is_correct": False, "formula": "D2", "explanation": "주제와 무관한 잡담입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "개요 작성의 효과",
                "stem": "글을 쓰기 전에 3단 구성 개요표를 작성할 때 얻을 수 있는 장점은?",
                "target_para_idx": 2,
                "spotlight_quote": "글을 쓰는 도중에 주제에서 벗어나는 실수를 막을 수 있습니다.",
                "options": [
                    {"label": "①", "text": "글씨를 예쁘게 쓰지 않아도 저절로 100점을 받는다.", "is_correct": False, "formula": "D3", "explanation": "개요 작성이 글씨 모양을 보장하지는 않습니다."},
                    {"label": "②", "text": "글을 쓰는 도중에 주제에서 벗어나는 실수를 막을 수 있다.", "is_correct": True, "formula": "정답", "explanation": "3문단에 서술된 개요표 작성의 핵심적 효과입니다."},
                    {"label": "③", "text": "글의 분량을 무조건 50쪽 이상으로 늘릴 수 있다.", "is_correct": False, "formula": "D4", "explanation": "분량을 억지로 늘리는 것이 목적이 아닙니다."},
                    {"label": "④", "text": "더 이상 글을 쓸 필요 없이 개요표만 제출하면 된다.", "is_correct": False, "formula": "D6", "explanation": "개요표는 글을 쓰기 위한 설계도입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 설명글의 [끝] 부분에 들어가야 할 필수 요소는?",
                "options": [
                    {"label": "①", "text": "글 전체 내용 요약과 중심 생각의 마무리", "is_correct": True},
                    {"label": "②", "text": "새로운 주제를 처음부터 다시 시작하기", "is_correct": False},
                    {"label": "③", "text": "다른 책의 서평을 길게 인용하기", "is_correct": False},
                    {"label": "④", "text": "자석과 상관없는 별자리 이야기 적기", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "마지막으로 [끝]에는 자석이 우리 생활을 편리하게 해 준다는 의의와 전체 요약을 제시합니다.", "is_correct": True},
                    {"label": "②", "text": "설명글은 읽는 이가 내용을 체계적으로 파악할 수 있도록", "is_correct": False},
                    {"label": "③", "text": "'자석의 성질과 이용'을 주제로 개요를 짠다면,", "is_correct": False},
                    {"label": "④", "text": "이렇게 중심 문장과 뒷받침 문장의 위계를 명확히 세운 개요표를", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "3단 구성 개요표 채우기",
            "guide": "내가 쓰고 싶은 과학 설명글의 [처음], [가운데], [끝] 개요를 한 줄씩 메모해 보세요.",
            "template": "[처음] : [자석의 정의와 질문] / [가운데] : [자석의 성질과 이용 사례] / [끝] : [요약 및 느낀 점]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "집을 짓기 전 설계도를 그리듯, 글을 쓰기 전 '처음-가운데-끝' 개요표를 짜요."},
            "step1_2_drill": {"task": "제시된 문장들을 '처음', '가운데', '끝' 상자에 알맞게 분류하기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "개요표를 작성하면 글이 주제에서 벗어나는 것을 예방할 수 있습니다.", "answer": "O", "reason": "개요표의 핵심 기능입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 처음, 가운데, 끝으로 말하기",
            "situation": "아이가 오늘 학교에서 있었던 일을 신나게 이야기할 때",
            "parent_question": "오늘 있었던 과학 실험을 '처음-가운데-끝'으로 나누어 멋지게 요약해 줄 수 있니?",
            "expected_answer": "처음엔 자석을 받았고, 가운데엔 클립을 붙여 봤고, 끝엔 나침반을 만들며 마쳤어요!",
            "coaching_tip": "두서없이 말하기보다 3단계로 간추려 말하는 논리성을 칭찬해 주세요."
        }
    ),

    # Slot 15: W4
    build_expository_slot(
        grade_num=3,
        subskill_code="W4",
        subject="사회(환경에 따라 다른 삶 3-2)",
        unit="2. 다양한 삶의 모습",
        concept="산지촌과 어촌의 생활 모습 비교 설명문 집필하기",
        text_structure="비교·대조",
        structure_type_code="comparison",
        passage_title="자연환경에 맞춘 마을, 산지촌과 어촌",
        paragraphs=[
            "우리나라 사람들은 자신이 살아가는 고장의 자연환경에 알맞게 생활 모습을 가꾸어 왔습니다. 산이 많은 높은 곳에 자리 잡은 마을을 '산지촌'이라 하고, 바다와 맞닿은 곳에 자리 잡은 마을을 '어촌'이라고 부릅니다.",
            "두 마을은 주민들이 하는 일과 집의 모습이 뚜렷하게 다릅니다. 산지촌 사람들은 경사진 밭을 일구어 옥수수나 감자를 재배하고 버섯이나 약초를 채취합니다. 반면에 어촌 사람들은 배를 타고 바다로 나가 물고기를 잡거나 미역, 김 같은 해조류를 양식합니다.",
            "또한 산지촌의 가옥은 산비탈을 따라 드문드문 흩어져 있는 경우가 많지만, 어촌의 가옥은 포구 주변에 오밀조밀 모여 있습니다. 이처럼 두 마을은 자연환경의 차이 때문에 각기 다른 독특한 삶의 방식을 발전시켰습니다."
        ],
        vocab_notes=[
            {"word": "산지촌", "definition": "산골짜기나 비탈진 산지에 형성된 마을"},
            {"word": "어촌", "definition": "바닷가에 위치하여 주로 물고기를 잡거나 양식하며 살아가는 마을"},
            {"word": "가옥", "definition": "사람이 살기 위하여 지은 집"}
        ],
        visual_html="""<div class="p-3 bg-sky-50 rounded border border-sky-200">
          <h4 class="font-bold text-sky-900 mb-2">🏔️ vs 🌊 산지촌과 어촌의 특징 비교표</h4>
          <table class="w-full text-xs text-center border-collapse">
            <tr class="bg-sky-100"><th class="p-1 border border-sky-200">구분</th><th class="p-1 border border-sky-200">산지촌 (산지 마을)</th><th class="p-1 border border-sky-200">어촌 (바닷가 마을)</th></tr>
            <tr><td class="p-1 border border-sky-200 font-bold bg-white">주민의 생업</td><td class="p-1 border border-sky-200 bg-white">밭농사(감자·옥수수), 약초 채취</td><td class="p-1 border border-sky-200 bg-white">어로 활동(어업), 해조류 양식</td></tr>
            <tr><td class="p-1 border border-sky-200 font-bold bg-white">집의 배치</td><td class="p-1 border border-sky-200 bg-white">비탈을 따라 드문드문 분포</td><td class="p-1 border border-sky-200 bg-white">포구 주변에 밀집 분포</td></tr>
          </table>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-w4-c1", "text": "산지촌 사람들은 경사진 밭을 일구어 옥수수나 감자를 재배하고", "role": "산지촌 주민의 일", "para_idx": 1},
            {"cue_id": "g3-w4-c2", "text": "반면에 어촌 사람들은 배를 타고 바다로 나가 물고기를 잡거나", "role": "어촌 주민의 일", "para_idx": 1}
        ],
        graphic_organizer={
            "diagram_type": "비교·대조 구조도",
            "contrast_items": {
                "산지촌": ["밭농사·약초 채취", "가옥이 흩어져 있음(산비탈)"],
                "어촌": ["물고기잡이·양식업", "가옥이 모여 있음(포구)"]
            },
            "common_cause": "자연환경에 적응한 주민들의 삶의 모습"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "비교·대조 세부 확인",
                "stem": "글의 내용에 나타난 '산지촌'과 '어촌'의 차이점으로 알맞은 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "산지촌 사람들은 경사진 밭을 일구어 옥수수나 감자를 재배하고 버섯이나 약초를 채취합니다. 반면에 어촌 사람들은 배를 타고 바다로 나가 물고기를 잡거나 미역, 김 같은 해조류를 양식합니다.",
                "options": [
                    {"label": "①", "text": "산지촌은 물고기를 잡고, 어촌은 감자를 재배한다.", "is_correct": False, "formula": "D3", "explanation": "두 마을의 생업을 정반대로 바꾸어 설명한 오답입니다."},
                    {"label": "②", "text": "산지촌은 밭농사와 약초를 하고, 어촌은 어업과 해조류 양식을 한다.", "is_correct": True, "formula": "정답", "explanation": "2문단에 설명된 각 마을의 올바른 생업 차이입니다."},
                    {"label": "③", "text": "두 마을 모두 배를 타고 바다로 나가야만 일할 수 있다.", "is_correct": False, "formula": "D4", "explanation": "산지촌은 산에 있으므로 바다에 나가지 않습니다."},
                    {"label": "④", "text": "두 마을의 집들은 모두 바다 한가운데 떠 있는 배 모양이다.", "is_correct": False, "formula": "D5", "explanation": "본문 내용에 전혀 없는 과장된 허구입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "중심-뒷받침 위계 파악",
                "stem": "2문단의 중심 문장으로 가장 알맞은 것은?",
                "target_para_idx": 1,
                "spotlight_quote": "두 마을은 주민들이 하는 일과 집의 모습이 뚜렷하게 다릅니다.",
                "options": [
                    {"label": "①", "text": "두 마을은 주민들이 하는 일과 집의 모습이 뚜렷하게 다릅니다.", "is_correct": True, "formula": "정답", "explanation": "2문단 전체의 구체적 설명을 이끄는 맨 앞의 중심 문장입니다."},
                    {"label": "②", "text": "산지촌 사람들은 맛있는 옥수수를 즐겨 먹습니다.", "is_correct": False, "formula": "D2", "explanation": "세부적인 1개 예시에 불과합니다."},
                    {"label": "③", "text": "미역과 김은 바다에서 자라는 해조류입니다.", "is_correct": False, "formula": "D1", "explanation": "지엽적인 단어 뜻풀이 뒷받침 문장입니다."},
                    {"label": "④", "text": "사람들은 누구나 바닷가에서 살고 싶어 합니다.", "is_correct": False, "formula": "D6", "explanation": "본문에 없는 주관적 감정입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 어촌의 가옥들이 포구 주변에 모여 있는 까닭은?",
                "options": [
                    {"label": "①", "text": "배를 타고 바다로 나가 일하기 편리한 곳이기 때문에", "is_correct": True},
                    {"label": "②", "text": "산비탈에 집을 지을 수 없어서 벌금을 내기 때문에", "is_correct": False},
                    {"label": "③", "text": "약초를 캐러 가기 위해서", "is_correct": False},
                    {"label": "④", "text": "감자를 널어놓을 마당이 없어서", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "어촌의 가옥은 포구 주변에 오밀조밀 모여 있습니다.", "is_correct": True},
                    {"label": "②", "text": "산지촌의 가옥은 산비탈을 따라 드문드문 흩어져 있는 경우가 많지만,", "is_correct": False},
                    {"label": "③", "text": "우리나라 사람들은 자신이 살아가는 고장의 자연환경에 알맞게", "is_correct": False},
                    {"label": "④", "text": "반면에 어촌 사람들은 배를 타고 바다로 나가 물고기를 잡거나", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "대조 담화표지를 살린 비교 문장 완성하기",
            "guide": "'반면에', '하지만' 같은 대조 접속어를 사용하여 산지촌과 어촌을 비교해 보세요.",
            "template": "산지촌 주민들은 밭에서 감자를 재배합니다. [반면에] 어촌 주민들은 [바다에서 물고기를 잡습니다]."
        },
        prescription_clinic={
            "step0_remedial": {"rule": "비교·대조 문단을 쓸 때는 '반면에', '이와 달리' 같은 대조 접속어를 활용해요."},
            "step1_2_drill": {"task": "산지촌과 어촌의 특징 문장 카드 짝맞춤 훈련"},
            "step3_vaccine": {"ox_quiz": [{"statement": "자연환경의 차이로 인해 두 마을의 주민들이 하는 일이 달라집니다.", "answer": "O", "reason": "본문의 핵심 인과 관계입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 산과 바다의 마을",
            "situation": "가족 여행으로 바닷가나 산골 펜션에 놀러 갔을 때",
            "parent_question": "여기 마을 사람들은 주로 어떤 일을 하시면서 살아가실까? 우리 동네와 어떻게 다를까?",
            "expected_answer": "여긴 바닷가니까 어부 아저씨들이 고기를 잡거나 김 양식을 하실 것 같아요!",
            "coaching_tip": "실제 여행지에서 주변 주민들의 생활 모습을 관찰하도록 격려해 주세요."
        }
    ),

    # Slot 16: W5
    build_expository_slot(
        grade_num=3,
        subskill_code="W5",
        subject="과학(식물의 한살이 3-1)",
        unit="2. 식물의 한살이",
        concept="강낭콩의 한살이 관찰 보고서 퇴고하기",
        text_structure="순서·과정 + 퇴고",
        structure_type_code="sequence",
        passage_title="쑥쑥 자라는 강낭콩 관찰 보고서 퇴고",
        paragraphs=[
            "강낭콩 관찰 보고서는 씨앗이 싹터서 꽃이 피고 열매를 맺기까지의 변화 과정을 날짜순으로 정확히 기록해야 합니다. 관찰 보고서 초고를 다 작성한 뒤에는 세 가지 기준에 따라 정밀하게 퇴고해야 합니다.",
            "첫째, 내용 면에서 날짜별 잎의 개수나 키의 측정 단위(cm)가 누락되지 않았는지 점검합니다. 둘째, 조직 면에서 '씨앗 ➔ 싹틈 ➔ 잎 자람 ➔ 꽃 ➔ 꼬투리' 순서가 뒤바뀌지 않았는지 확인합니다. 셋째, 표현 면에서 주어와 서술어의 호응이 바른지, 맞춤법과 띄어쓰기가 정확한지 살핍니다.",
            "초고에 있던 오류들을 표준 교정부호를 사용하여 바르게 고치면, 누구라도 한눈에 식물의 한살이를 이해할 수 있는 훌륭한 과학 보고서가 완성됩니다."
        ],
        vocab_notes=[
            {"word": "꼬투리", "definition": "콩과 식물의 열매를 싸고 있는 껍질 주머니"},
            {"word": "퇴고", "definition": "글을 다 쓴 뒤 내용을 다듬고 틀린 부분을 바로잡는 일"}
        ],
        visual_html="""<div class="p-3 bg-lime-50 rounded border border-lime-200">
          <h4 class="font-bold text-lime-900 mb-2">🔍 과학 관찰 보고서 3단계 퇴고 점검표</h4>
          <ul class="text-xs space-y-1 text-slate-700">
            <li>✔ <strong>1단계 내용 점검:</strong> 날짜, 날씨, 측정 수치(cm, 잎의 수)가 정확한가?</li>
            <li>✔ <strong>2단계 조직 점검:</strong> 시간 순서(씨앗➔싹➔꽃➔열매)가 뒤바뀌지 않았는가?</li>
            <li>✔ <strong>3단계 표현 점검:</strong> 주어와 서술어 호응, 띄어쓰기, 맞춤법이 올바른가?</li>
          </ul>
        </div>""",
        hottext_cues=[
            {"cue_id": "g3-w5-c1", "text": "측정 단위(cm)가 누락되지 않았는지 점검합니다", "role": "내용 퇴고 기준", "para_idx": 1},
            {"cue_id": "g3-w5-c2", "text": "표준 교정부호를 사용하여 바르게 고치면", "role": "퇴고 완성 효과", "para_idx": 2}
        ],
        graphic_organizer={
            "diagram_type": "3단계 퇴고 체크리스트",
            "content_check": "측정치 및 과학적 사실의 정확성",
            "organization_check": "식물 한살이 시간 순서의 일관성",
            "expression_check": "주술 호응 및 맞춤법 교정"
        },
        csat_questions=[
            {
                "q_no": 1,
                "archetype": "조직 통일성 퇴고",
                "stem": "강낭콩 관찰 보고서에서 순서가 잘못되어 고쳐야 할 부분은 무엇인가요?",
                "target_para_idx": 1,
                "spotlight_quote": "조직 면에서 '씨앗 ➔ 싹틈 ➔ 잎 자람 ➔ 꽃 ➔ 꼬투리' 순서가 뒤바뀌지 않았는지 확인합니다.",
                "options": [
                    {"label": "①", "text": "씨앗을 심기 전에 꼬투리부터 열렸다고 쓴 부분", "is_correct": True, "formula": "정답", "explanation": "꼬투리는 꽃이 진 뒤에 생기는 열매이므로, 씨앗 심기 전으로 쓰인 것은 시간 순서 오류입니다."},
                    {"label": "②", "text": "씨앗을 심고 며칠 뒤 떡잎이 나왔다고 쓴 부분", "is_correct": False, "formula": "D1", "explanation": "자연스러운 한살이 순서입니다."},
                    {"label": "③", "text": "본잎이 자라면서 키가 10cm로 자랐다고 쓴 부분", "is_correct": False, "formula": "D2", "explanation": "올바른 관찰 기록입니다."},
                    {"label": "④", "text": "꽃이 핀 뒤에 나비가 찾아왔다고 쓴 부분", "is_correct": False, "formula": "D4", "explanation": "가능한 관찰 사실입니다."}
                ]
            },
            {
                "q_no": 2,
                "archetype": "표현 호응 오류 퇴고",
                "stem": "다음 초고 문장 중 주어와 서술어의 호응이 어색하여 퇴고해야 할 문장은?",
                "target_para_idx": 1,
                "spotlight_quote": "표현 면에서 주어와 서술어의 호응이 바른지, 맞춤법과 띄어쓰기가 정확한지 살핍니다.",
                "options": [
                    {"label": "①", "text": "강낭콩의 줄기는 위를 향해 곧게 자랐습니다.", "is_correct": False, "formula": "D2", "explanation": "주어 '줄기는'과 서술어 '자랐습니다'가 잘 어울립니다."},
                    {"label": "②", "text": "내가 관찰한 강낭콩은 키가 쑥쑥 자라는 모습이었다.", "is_correct": False, "formula": "D3", "explanation": "자연스러운 문장입니다."},
                    {"label": "③", "text": "강낭콩의 잎이 날마다 크기가 점점 커졌다.", "is_correct": True, "formula": "정답", "explanation": "'잎이 날마다 크기가'처럼 주어가 어색하게 겹치므로 '강낭콩 잎의 크기가 날마다 점점 커졌다'로 다듬어야 합니다."},
                    {"label": "④", "text": "하얀 꽃이 활짝 피어 기뻤습니다.", "is_correct": False, "formula": "D1", "explanation": "자연스러운 표현입니다."}
                ]
            }
        ],
        ebsr_question={
            "part_a": {
                "stem": "[Part A] 과학 관찰 보고서 내용 점검 시 가장 중요한 수치 단위는?",
                "options": [
                    {"label": "①", "text": "키의 길이(cm)와 잎의 개수", "is_correct": True},
                    {"label": "②", "text": "씨앗의 판매 가격(원)", "is_correct": False},
                    {"label": "③", "text": "화분 가게 사장님의 나이", "is_correct": False},
                    {"label": "④", "text": "관찰을 마친 시각의 초 단위", "is_correct": False}
                ]
            },
            "part_b": {
                "stem": "[Part B] 위 정답의 근거가 되는 본문 구절은?",
                "options": [
                    {"label": "①", "text": "첫째, 내용 면에서 날짜별 잎의 개수나 키의 측정 단위(cm)가 누락되지 않았는지 점검합니다.", "is_correct": True},
                    {"label": "②", "text": "강낭콩 관찰 보고서는 씨앗이 싹터서 꽃이 피고", "is_correct": False},
                    {"label": "③", "text": "열매를 맺기까지의 변화 과정을 날짜순으로 정확히 기록해야 합니다.", "is_correct": False},
                    {"label": "④", "text": "초고에 있던 오류들을 표준 교정부호를 사용하여 바르게 고치면,", "is_correct": False}
                ]
            }
        },
        writing_workbench={
            "task_title": "관찰 일지 퇴고 교정부호 실습",
            "guide": "어색한 문장을 바르게 다듬어 보세요.",
            "template": "초고: 강낭콩 잎이 키가 커졌고 꽃이 피였다 ➔ 퇴고: [강낭콩의 키가 자랐고 예쁜 꽃이 피었다.]"
        },
        prescription_clinic={
            "step0_remedial": {"rule": "퇴고할 때는 '내용(정확성) ➔ 조직(시간 순서) ➔ 표현(맞춤법)'의 3단계로 검토해요."},
            "step1_2_drill": {"task": "잘못된 문장 호응 찾아 밑줄 긋고 바르게 고치기"},
            "step3_vaccine": {"ox_quiz": [{"statement": "보고서는 시간의 흐름 순서대로 조직되었는지 점검해야 합니다.", "answer": "O", "reason": "관찰 보고서 조직의 핵심 원칙입니다."}]}
        },
        parent_table_talk={
            "title": "밥상머리 대화: 다시 읽고 다듬는 지혜",
            "situation": "아이가 숙제 보고서를 완성하고 자랑할 때",
            "parent_question": "보고서를 다 쓴 다음에 점검표로 다시 읽어 보면 어떤 새로운 실수를 고칠 수 있을까?",
            "expected_answer": "날짜나 키 센티미터(cm)를 빠뜨린 것이나 잎의 순서가 바뀐 걸 찾아서 고칠 수 있어요!",
            "coaching_tip": "첫 번째 완성보다 다시 읽고 다듬는 퇴고의 가치를 높이 칭찬해 주세요."
        }
    )
]

g3_all_expository = g3_exp_slots + g3_remaining_exp

print(f"Total Grade 3 Expository Slots: {len(g3_all_expository)} (expected 16)")
print(f"Total Grade 3 Common Slots: {len(g3_common_slots)} (expected 6)")

out_path = os.path.join(ITEM_BANK_DIR, "g3_item_bank.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "grade_num": 3,
        "expository_slots": g3_all_expository,
        "common_slots": g3_common_slots
    }, f, ensure_ascii=False, indent=2)

print(f"✅ Successfully wrote {out_path} ({len(g3_all_expository)} Expository + {len(g3_common_slots)} Common)")
