# -*- coding: utf-8 -*-
"""
초등 1~6학년 설명문(Expository) 수능형 문해력 코스웨어 통합 마스터 생성기 (All-in-One)
- 기존 프로토타입(1~6학년 지문·어휘·단서·수능문항·설계표준·96위계 탐색기)과
  적응형 목업([Stage 1 현재 상태 정밀 진단] ➔ [Stage 2 1:1 맞춤형 처방 클리닉] ➔ [Stage 3 실전 수능 대비 문제])을
  단 하나의 HTML 파일(courseware/output/expository_literacy_courseware.html)로 완벽 통합.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load 96 Expository + 36 Common Foundational hierarchy data
with open(os.path.join(DATA_DIR, "expository_courseware_hierarchy.json"), "r", encoding="utf-8") as f:
    HIERARCHY_DATA = json.load(f)


# =============================================================================
# 초1 ~ 초6 전 학년 통합 적응형 코스웨어 마스터 데이터 (6개 학년 × [진단 ➔ 처방 ➔ 실전 수능])
# =============================================================================
UNIFIED_GRADES_DATA = [
    # =========================================================================
    # 1학년: 김도윤 (G1-EXP-V1-2 관계 확인 — 지시어 연결 및 전체-부분 짝짓기)
    # =========================================================================
    {
        "id": "g1_doyun",
        "grade_num": 1,
        "grade": "1학년",
        "grade_band": "초저 (1~2학년군 · 3지선다 입문형)",
        "persona_label": "초1 김도윤 · 지시어·전체-부분 입문형",
        "slot_id": "G1-EXP-V1-2",
        "domain": "1. 사실적 이해",
        "layer": "V1-2 관계 확인",
        "sub_skill_name": "문장 속 가리키는 말(지시어) 연결 및 전체-부분(몸 부위와 하는 일) 짝짓기",
        "curriculum_concept": {
            "subject": "통합교과(자연 1-1 / 학교 1-1)",
            "unit": "자연과 함께해요 - 동물 친구들의 생김새",
            "concept": "코끼리의 몸 부위(코·귀·다리) 생김새와 하는 일",
            "text_structure": "분석 기초 (전체-부분) + 기술·열거"
        },
        "complexity_metrics": {
            "kread_target": "820 (1학년 표준 800~890)",
            "current_kread": "760 (입문 기초 · -60p)",
            "para_count": "1문단 (4문장)",
            "char_count": "148자 (1학년 권장 100~180자)",
            "eojeol_count": "34어절 (문장당 평균 6.8어절)",
            "vocab_profile": "Tier 1(91%) · Tier 2(6%: 모양, 대신) · Tier 3(3%: 부채, 몸집)",
            "csat_scaling": "3지선다 · 단문 선지(4~6어절) · 친화형 의문 발문"
        },
        "mager_goal": "[조건] 짧은 설명글과 코끼리 부분 그림이 주어졌을 때, [준거] 지시어('이 동물은')가 가리키는 대상과 각 부분(코, 귀, 다리)이 하는 일을 100% 정확히, [행동] 짝지어 찾고 알맞은 설명을 고를 수 있다.",
        "student_summary": "낱말 읽기는 정확하나, 앞 문장을 받는 가리키는 말(‘이것, 이 동물’)과 대상의 부위별 역할을 짝지을 때 [D4 부위-역할 교차] 함정에 자주 빠짐",

        # [Stage 1] 현재 상태 진단
        "diagnostic_test": {
            "passage_title": "[진단 미니 지문] 우리 교실의 고마운 시계 (초1 통합교과 ‘학교’)",
            "passage_spec": "1문단 · 122자 · KReaD 810 · 3지선다",
            "paragraphs": [
                "교실 앞벽에는 동그란 시계가 걸려 있습니다. ㉠<u>이 물건</u>에는 짧은바늘과 긴바늘이 있습니다. 짧은바늘은 지금 몇 시인지 알려 줍니다. 긴바늘은 몇 분인지 정확하게 알려 줍니다."
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G1-EXP-V1-2",
                    "target_skill": "가리키는 말(지시어)이 받는 앞 문장 명사 찾기",
                    "stem": "윗글의 밑줄 친 ㉠‘이 물건’이 가리키는 것은 무엇인가요?",
                    "options": [
                        {"no": 1, "text": "교실 앞벽에 걸려 있는 동그란 시계", "is_correct": True, "trap": "정답 (앞 문장 주어 명사 정확 연결)"},
                        {"no": 2, "text": "시계 안에 들어 있는 짧은바늘", "is_correct": False, "trap": "D5 (전체 대상과 부분 구성 요소를 혼동)"},
                        {"no": 3, "text": "교실 뒤에 있는 사물함", "is_correct": False, "trap": "D6 (글에 없는 교실 배경 상식 함정)"}
                    ],
                    "student_selected": 1
                },
                {
                    "q_no": 2,
                    "target_code": "G1-EXP-V1-2",
                    "target_skill": "전체-부분(바늘 종류와 하는 일) 짝짓기",
                    "stem": "시계의 바늘이 하는 일로 알맞게 짝지어진 것은 무엇인가요?",
                    "options": [
                        {"no": 1, "text": "짧은바늘은 몇 분인지 알려 주고, 긴바늘은 몇 시인지 알려 줍니다.", "is_correct": False, "trap": "D4 (부분-기능 교차 치환 함정: 짧은바늘↔긴바늘 역할 뒤바꿈)"},
                        {"no": 2, "text": "짧은바늘은 몇 시인지 알려 주고, 긴바늘은 몇 분인지 알려 줍니다.", "is_correct": True, "trap": "정답 (부분별 기능 정확 짝짓기)"},
                        {"no": 3, "text": "짧은바늘과 긴바늘은 모두 교실 벽을 청소해 줍니다.", "is_correct": False, "trap": "D6 (글에 없는 허위 기능 진술)"}
                    ],
                    "student_selected": 1
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 52, "status": "danger", "comment": "낱말 찾기(V1-1)는 양호하나, 부분-역할 짝짓기(V1-2)에서 속성이 뒤섞임"},
                {"domain": "2. 추론적 이해 (V2)", "score": 74, "status": "good", "comment": "그림 보고 빠진 말 짐작하기 양호"},
                {"domain": "3. 비판적 이해 (V3)", "score": 78, "status": "good", "comment": "진짜 사진과 상상 그림 구별하기 우수"},
                {"domain": "4. 표현·작문 (W)", "score": 58, "status": "warn", "comment": "관찰한 대상의 특징 한 문장 쓰기(W4) 연습 필요"}
            ],
            "bottleneck": {
                "step1_rate": 86,
                "step2_rate": 40,
                "step3_rate": 48,
                "diagnosis_title": "Dick & Carey [Step 2: ‘부분 이름’과 ‘하는 일(서술어)’ 짝짓기 병목]",
                "diagnosis_detail": "글에서 ‘짧은바늘’, ‘긴바늘’이라는 낱말(Step 1)은 찾았으나, 각각 어떤 일을 하는지 연결하는 단계(Step 2)에서 기억이 섞여 두 바늘의 역할을 서로 바꾸어 놓은 [D4 속성 교차 함정]에 빠졌습니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "반대 말 함정", "vuln": 25},
                {"code": "D2", "name": "순서 뒤바뀜", "vuln": 35},
                {"code": "D3", "name": "과장 표현", "vuln": 20},
                {"code": "D4", "name": "부위·역할 교차 (집중 취약!)", "vuln": 88},
                {"code": "D5", "name": "전체·부분 혼동", "vuln": 55},
                {"code": "D6", "name": "글에 없는 내용", "vuln": 20}
            ],
            "backtracking_path": [
                {"grade": "1학년 기초", "code": "G1-COM-A2 / A4", "title": "문장에서 ‘누가(주어)-무엇을 하다(서술어)’와 가리키는 말 잇기", "status": "review"},
                {"grade": "1학년 목표", "code": "G1-EXP-V1-2 (현재 목표)", "title": "대상의 각 부위(부분)와 하는 일(기능)을 헷갈리지 않고 짝짓기", "status": "target"},
                {"grade": "2학년 확장", "code": "G2-EXP-V1-2 (후속 확장)", "title": "두 대상의 공통점과 차이점 표로 정리하기", "status": "next"}
            ]
        },

        # [Stage 2] 1:1 맞춤형 처방 클리닉
        "prescription_clinic": {
            "rx_title": "김도윤 맞춤 처방전 #RX-G1-D4: [주어-서술어 색깔 짝짓기 ➔ 코끼리 부위별 역할 조립 ➔ D4 교차 함정 백신]",
            "rx_reason": "1학년 설명문에서 여러 부위(코, 귀, 다리)가 연달아 나올 때 헷갈리지 않도록, [부위 이름 = 하는 일]을 1:1로 묶는 사고구술 훈련을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-COM-A4 가리키는 말(‘이 동물은’) 화살표 잇기",
                "rule_box": "💡 **가리키는 말 공식**: 문장 앞에 **‘이 동물은 / 이 물건은’**이 나오면 바로 **앞 문장 맨 앞 주인공 이름**에 동그라미를 쳐요!",
                "mini_question": "“기린은 목이 아주 깁니다. <u>이 동물은</u> 높은 나무에 있는 나뭇잎을 잘 따 먹습니다.” — ‘이 동물’은 누구인가요?",
                "choices": ["기린", "다람쥐"],
                "correct": "기린",
                "feedback": "딩동댕! 바로 앞 문장의 주인공인 ‘기린’을 가리켜요."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G1-EXP-V1-2 코끼리 몸 부위(코·귀·다리)와 하는 일 조립하기",
                "passage_snippet": "코끼리는 땅 위에서 사는 동물 가운데 몸집이 가장 큽니다. <span class='rx-cue' data-tip='앞 문장 코끼리!'>이 동물은</span> 길쭉한 <span class='rx-cue' data-tip='부위 ①: 코 (먹이 집기)'>코</span>를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹습니다. 또 넓적한 <span class='rx-cue' data-tip='부위 ②: 귀 (더운 몸 식히기)'>귀</span>를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다. 굵은 기둥 같은 네 <span class='rx-cue' data-tip='부위 ③: 다리 (무거운 몸 받치기)'>다리</span>는 무거운 몸을 튼튼하게 받쳐 줍니다.",
                "think_aloud_prompt": "노란색 부위 단서를 눌러 보고, 코끼리의 세 부위가 각각 무슨 일을 하는지 골라 보세요!",
                "cloze_sentences": [
                    "• 1단계: ‘이 동물은’ = 앞 문장의 ( {b1} )를 가리킵니다.",
                    "• 2단계: 길쭉한 [코] = 손처럼 물을 마시고 ( {b2} )를 집어 먹습니다.",
                    "• 3단계: 넓적한 [귀] = 부채처럼 흔들어 ( {b3} )을 시원하게 식히고, [네 다리] = 무거운 몸을 받쳐 줍니다."
                ],
                "blanks": [
                    {"id": "b1", "correct": "코끼리", "options": ["코끼리", "기둥", "부채"]},
                    {"id": "b2", "correct": "먹이", "options": ["먹이", "바람", "기둥"]},
                    {"id": "b3", "correct": "더운 몸", "options": ["더운 몸", "먹이", "발바닥"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D4(부위-역할 뒤바꾸기 함정) 참/거짓 판별하기",
                "desc": "수능형 문제에서는 ‘코가 하는 일’과 ‘귀가 하는 일’을 슬쩍 바꾸어 놓아요! 속지 않고 찾아내 볼까요?",
                "items": [
                    {
                        "statement": "코끼리는 넓적한 귀로 먹이를 집어 먹고, 길쭉한 코로 더운 몸을 식힙니다.",
                        "answer": "X",
                        "reason": "삐뽀삐뽀! [D4 부위-역할 교차 함정]이에요! 먹이를 집는 것은 ‘코’이고, 더운 몸을 식히는 것은 ‘귀’예요."
                    },
                    {
                        "statement": "굵은 기둥 같은 네 다리는 코끼리의 무거운 몸을 튼튼하게 받쳐 줍니다.",
                        "answer": "O",
                        "reason": "딩동댕! 마지막 문장에 나온 ‘다리’의 역할과 정확히 일치해요!"
                    }
                ]
            }
        },

        # [Stage 3] 실전 수능 대비 문제 (프로토타입 본문·어휘·단서 완전 통합)
        "real_csat_test": {
            "test_title": "[실전 수능 대비 3지선다] 초1 통합교과 ‘코가 길고 귀가 큰 코끼리’",
            "passage_spec": "1문단 · 148자 · 34어절 · KReaD 820 · 3지선다 수능 입문형",
            "passage_title": "코가 길고 귀가 큰 코끼리",
            "paragraphs": [
                "코끼리는 땅 위에서 사는 동물 가운데 몸집이 가장 큽니다. ㉠<span class='cue-span' data-cue='g1-c1'>이 동물은</span> 길쭉한 <span class='cue-span' data-cue='g1-c2'>코</span>를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹습니다. 또 넓적한 <span class='cue-span' data-cue='g1-c3'>귀</span>를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다. 굵은 기둥 같은 네 <span class='cue-span' data-cue='g1-c4'>다리</span>는 무거운 몸을 튼튼하게 받쳐 줍니다."
            ],
            "vocab_notes": [
                {"word": "몸집", "tier": "Tier 1 (기초)", "desc": "몸의 크기나 부피"},
                {"word": "팔랑거리다", "tier": "Tier 1 (감각어)", "desc": "넓고 얇은 물체가 바람에 가볍게 자꾸 흔들리다"},
                {"word": "받쳐 주다", "tier": "Tier 2 (사고어)", "desc": "무거운 것이 쓰러지지 않게 아래에서 버티어 주다"}
            ],
            "visual_html": """
              <div style="background:#FFFBEB; border:1px solid #FDE68A; border-radius:10px; padding:14px; margin:12px 0;">
                <div style="font-weight:800; color:#92400E; margin-bottom:8px;">🐘 [그림 자료] 코끼리의 몸 부위와 하는 일 (전체-부분 구조도)</div>
                <div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; text-align:center;">
                  <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #93C5FD;">
                    <div style="font-size:1.3rem;">👃 <b>길쭉한 코</b></div>
                    <div style="font-size:0.84rem; color:#1E40AF; margin-top:4px;">손처럼 물 마시기 · 먹이 집기</div>
                  </div>
                  <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #86EFAC;">
                    <div style="font-size:1.3rem;">👂 <b>넓적한 귀</b></div>
                    <div style="font-size:0.84rem; color:#166534; margin-top:4px;">부채처럼 흔들어 더운 몸 식히기</div>
                  </div>
                  <div style="background:#fff; padding:10px; border-radius:8px; border:2px solid #FDBA74;">
                    <div style="font-size:1.3rem;">🦵 <b>굵은 네 다리</b></div>
                    <div style="font-size:0.84rem; color:#9A3412; margin-top:4px;">기둥처럼 무거운 몸 받치기</div>
                  </div>
                </div>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-READ-V1-2 (지시어 연결 및 세부 사실 일치 - 3지선다)",
                    "stem": "윗글의 밑줄 친 ㉠<u>이 동물</u>에 대한 설명으로 <u>알맞은</u> 것은 무엇인가요?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "땅 위에서 사는 동물 가운데 몸집이 가장 작습니다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D1 반대 진술]: '가장 큽니다'를 '가장 작습니다'로 반전",
                            "explanation": "❌ **[D1 반대 말 함정]** 첫 문장에서 코끼리는 땅 위에서 사는 동물 가운데 몸집이 **가장 크다**고 했어요."
                        },
                        {
                            "no": 2,
                            "text": "길쭉한 코를 손처럼 움직여서 먹이를 집어 먹습니다.",
                            "is_correct": True,
                            "formula": "정답 공식: [지시어 '이 동물' = 코끼리] + [코의 기능 일치]",
                            "explanation": "🎉 **[처방 성공! 정답]** ‘이 동물(코끼리)’은 길쭉한 코를 손처럼 움직여서 물을 마시거나 먹이를 집어 먹어요."
                        },
                        {
                            "no": 3,
                            "text": "넓적한 귀로 무거운 몸을 기둥처럼 받쳐 줍니다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 속성 교차 치환]: '네 다리'의 역할을 '넓적한 귀'에 잘못 연결",
                            "explanation": "❌ **[D4 부위-역할 교차 함정]** 무거운 몸을 기둥처럼 받쳐 주는 것은 귀가 아니라 **굵은 네 다리**예요!"
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V2-4 (<보기> 구체적 상황 적용형 - 3지선다)",
                    "stem": "윗글을 읽고 <보기>의 코끼리가 왜 귀를 움직였는지 알맞게 말한 것을 고르세요.",
                    "bogi": "<보기>\n  햇볕이 쨍쨍 내리쬐는 더운 낮이 되었습니다. 아기 코끼리가 넓적한 양쪽 귀를 부채처럼 빠르게 팔랑거렸습니다.",
                    "options": [
                        {
                            "no": 1,
                            "text": "더워진 몸을 시원하게 식히려고 귀를 팔랑거렸습니다.",
                            "is_correct": True,
                            "formula": "정답 공식: [본문 3문장 '귀를 부채처럼 팔랑거려서 더운 몸을 시원하게 식힙니다' 상황 적용]",
                            "explanation": "🎉 **[처방 성공! 정답]** 더운 낮에 코끼리가 귀를 부채처럼 팔랑거린 까닭은 **더운 몸을 시원하게 식히기 위해서**예요!"
                        },
                        {
                            "no": 2,
                            "text": "땅에 떨어진 열매를 귀로 집어 먹으려고 팔랑거렸습니다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 부위 기능 교차]: 먹이를 집어 먹는 '코'의 기능을 '귀'에 결합",
                            "explanation": "❌ **[D4 부위 기능 혼동]** 먹이를 집어 먹는 부위는 귀가 아니라 **길쭉한 코**예요."
                        },
                        {
                            "no": 3,
                            "text": "하늘 높이 날아오르려고 귀를 날개처럼 팔랑거렸습니다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D6 본문 외 상상 함정]: 동화적 상상을 끌어온 매력적 오답",
                            "explanation": "❌ **[D6 글에 없는 상상 함정]** 설명문에는 코끼리가 하늘을 난다는 내용이 없어요."
                        }
                    ]
                }
            ]
        }
    },

    # =========================================================================
    # 2학년: 최하은 (G2-EXP-V1-3 구조 파악 — 순서·과정 담화 표지 및 지시어)
    # =========================================================================
    {
        "id": "g2_haeun",
        "grade_num": 2,
        "grade": "2학년",
        "grade_band": "초저 (1~2학년군 · 3지선다 입문형)",
        "persona_label": "초2 최하은 · 순서표지·과정구조 취약형",
        "slot_id": "G2-EXP-V1-3",
        "domain": "1. 사실적 이해",
        "layer": "V1-3 구조 파악 (순서·과정)",
        "sub_skill_name": "순서 담화 표지(‘먼저-그다음-얼마 뒤-마지막으로’)를 단서로 한살이 과정 배열하기",
        "curriculum_concept": {
            "subject": "통합교과(자연 2-1) · 초3 과학 연계",
            "unit": "자연과 나 - 동식물이 자라는 모습",
            "concept": "개구리의 한살이(알 ➔ 올챙이 ➔ 뒷다리·앞다리 ➔ 개구리)와 신체 변화",
            "text_structure": "순서·과정 (Sequence / Process)"
        },
        "complexity_metrics": {
            "kread_target": "930 (2학년 표준 900~990)",
            "current_kread": "855 (1학년 후반 수준 · -75p)",
            "para_count": "2문단 (6문장)",
            "char_count": "242자 (2학년 권장 200~300자)",
            "eojeol_count": "56어절 (문장당 평균 8.0어절)",
            "vocab_profile": "Tier 1(85%) · Tier 2(10%: 먼저, 그다음, 과정) · Tier 3(5%: 알덩이, 올챙이, 아가미)",
            "csat_scaling": "3지선다 · 중문 포함 선지(6~8어절) · 과정 순서 도식 결합형"
        },
        "mager_goal": "[조건] 2문단 분량의 과정 설명글이 주어졌을 때, [준거] 순서를 나타내는 말('먼저, 그다음, 얼마 뒤, 마지막으로')을 단서로 4단계 변화 순서를 100% 정확히, [행동] 차례대로 배열하고 빈칸을 채울 수 있다.",
        "student_summary": "낱말 읽기는 가능하나, 순서 말(‘먼저-그다음-마지막으로’)이 이어질 때 선후 단계를 바꾸어 놓은 [D2 순서 뒤바뀜] 함정에 자주 빠짐",

        "diagnostic_test": {
            "passage_title": "[진단 미니 지문] 올바른 손 씻기 3단계 (초2 통합교과 ‘건강한 나’)",
            "passage_spec": "2문단 · 215자 · KReaD 920 · 3지선다",
            "paragraphs": [
                "밖에서 놀고 돌아오면 손에 눈에 보이지 않는 세균이 많이 묻어 있습니다. 감기를 예방하려면 비누로 손을 깨끗이 씻어야 합니다.",
                "손을 씻을 때에는 순서가 중요합니다. 먼저 흐르는 물에 양손을 적시고 비누를 칠해 거품을 냅니다. 그다음 손바닥과 손등, 손가락 사이를 꼼꼼하게 문지릅니다. 마지막으로 흐르는 물에 거품을 모두 헹구고 수건으로 물기를 닦습니다."
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G2-EXP-V1-3",
                    "target_skill": "순서·과정 구조 파악 (‘먼저-그다음-마지막으로’)",
                    "stem": "윗글에 나온 ‘손 씻는 순서’에 맞게 차례대로 연결한 것은 무엇인가요?",
                    "options": [
                        {"no": 1, "text": "[비누 거품 내기] ➔ [손바닥·손등 문지르기] ➔ [물로 헹구고 닦기]", "is_correct": True, "trap": "정답 (순서 표지 3단계 정확 일치)"},
                        {"no": 2, "text": "[손바닥·손등 문지르기] ➔ [비누 거품 내기] ➔ [물로 헹구고 닦기]", "is_correct": False, "trap": "D2 (선후 순서 왜곡 함정: 1단계와 2단계를 뒤바꿈)"},
                        {"no": 3, "text": "[비누 거품 내기] ➔ [물로 헹구고 닦기] ➔ [손바닥·손등 문지르기]", "is_correct": False, "trap": "D2 (선후 순서 왜곡 함정: 2단계와 3단계를 뒤바꿈)"}
                    ],
                    "student_selected": 2
                },
                {
                    "q_no": 2,
                    "target_code": "G2-EXP-V2-2",
                    "target_skill": "이유·까닭 추론 (‘~하려면’)",
                    "stem": "밖에서 놀고 돌아왔을 때 비누로 손을 깨끗이 씻어야 하는 까닭은 무엇인가요?",
                    "options": [
                        {"no": 1, "text": "손에 묻은 세균을 없애고 감기를 예방하기 위해서입니다.", "is_correct": True, "trap": "정답 (1문단 이유 확인)"},
                        {"no": 2, "text": "손에 눈에 보이지 않는 세균을 더 많이 묻히기 위해서입니다.", "is_correct": False, "trap": "D1 (목적·결과 반대 진술 함정)"},
                        {"no": 3, "text": "수건에 있는 물기를 손에 묻히기 위해서입니다.", "is_correct": False, "trap": "D5 (동작 방향 뒤집기 함정)"}
                    ],
                    "student_selected": 1
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 55, "status": "danger", "comment": "낱말 확인(V1-1)은 양호하나, 순서 담화 표지(V1-3)에서 앞뒤 단계가 뒤섞임"},
                {"domain": "2. 추론적 이해 (V2)", "score": 82, "status": "good", "comment": "짧은 문장의 이유·까닭 찾기는 안정적"},
                {"domain": "3. 비판적 이해 (V3)", "score": 76, "status": "good", "comment": "사진과 그림 구분하기 양호"},
                {"domain": "4. 표현·작문 (W)", "score": 60, "status": "warn", "comment": "순서 말을 넣어 3문장 설명글 쓰기(W3) 보강 필요"}
            ],
            "bottleneck": {
                "step1_rate": 85,
                "step2_rate": 42,
                "step3_rate": 50,
                "diagnosis_title": "Dick & Carey [Step 2: 순서 담화 표지(‘먼저-그다음-마지막으로’)와 행동 연결 병목]",
                "diagnosis_detail": "글 속에서 ‘거품’, ‘문지릅니다’, ‘헹구고’ 같은 행동 낱말(Step 1)은 찾지만, 앞의 순서 말(‘먼저 → 그다음 → 마지막으로’)에 번호를 매겨 묶지 못해(Step 2 병목), 선지에서 1단계와 2단계를 살짝 바꾼 [D2 선후 왜곡 함정]에 빠졌습니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "원인·결과 반대", "vuln": 25},
                {"code": "D2", "name": "순서 뒤바뀜 (집중 취약!)", "vuln": 88},
                {"code": "D3", "name": "과장 표현", "vuln": 30},
                {"code": "D4", "name": "짝짓기 혼동", "vuln": 45},
                {"code": "D5", "name": "주체 혼동", "vuln": 40},
                {"code": "D6", "name": "글에 없는 내용", "vuln": 20}
            ],
            "backtracking_path": [
                {"grade": "1학년 선행", "code": "G1-EXP-V1-2", "title": "가리키는 말(‘이것, 이곳’)이 앞 문장의 무엇인지 화살표 잇기", "status": "review"},
                {"grade": "2학년 목표", "code": "G2-EXP-V1-3 (현재 목표)", "title": "순서 말(‘먼저-그다음-얼마 뒤-마지막으로’)에 따라 과정 4단계 배열하기", "status": "target"},
                {"grade": "3학년 확장", "code": "G3-EXP-V1-3 (후속 확장)", "title": "원인과 결과(‘왜냐하면~때문이다’) 문장 구조 파악하기", "status": "next"}
            ]
        },

        "prescription_clinic": {
            "rx_title": "최하은 맞춤 처방전 #RX-G2-D2: [지시어 화살표 잇기 ➔ 개구리 한살이 순서 기차 4칸 조립 ➔ D2 순서 함정 백신]",
            "rx_reason": "2학년 설명문의 핵심인 ‘차례(순서) 구조’를 한눈에 볼 수 있도록, 순서 말에 번호표를 붙이고 다리 나오는 순서(뒷다리➔앞다리)를 구분하는 클리닉을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G1-EXP-V1-2 가리키는 말(‘이곳에서’) 화살표 잇기",
                "rule_box": "💡 **가리키는 말 공식**: **‘이것 / 이곳’**이 나오면 바로 **앞 문장**에서 알맞은 이름을 찾아 화살표(⬅️)로 연결해요!",
                "mini_question": "“씨앗은 땅속에서 겨울을 보냅니다. 봄이 되면 <u>이곳에서</u> 귀여운 싹이 돋아납니다.” — 밑줄 친 ‘이곳’은 어디인가요?",
                "choices": ["땅속", "하늘 위"],
                "correct": "땅속",
                "feedback": "정확해요! 바로 앞 문장에 나온 장소인 ‘땅속’을 가리켜요."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G2-EXP-V1-3 ‘개구리가 자라는 차례’ 순서 기차 4칸 조립하기",
                "passage_snippet": "<span class='rx-cue' data-tip='①번 기차 칸!'>먼저</span> 따뜻한 봄이 되면 어미 개구리가 연못에 투명한 알덩이를 낳습니다. <span class='rx-cue' data-tip='②번 기차 칸!'>그다음</span> 알에서 깨어난 올챙이는 물속에서 아가미로 숨을 쉬며 꼬리를 흔들어 헤엄칩니다. <span class='rx-cue' data-tip='③번 기차 칸! (뒷다리 먼저!)'>얼마 뒤</span> 올챙이는 뒷다리가 먼저 자라나고, 이어서 앞다리가 쑥 나옵니다. <span class='rx-cue' data-tip='④번 기차 칸!'>마지막으로</span> 꼬리가 점점 짧아져 사라지면 땅 위로 올라와 허파와 피부로 숨을 쉬는 어른 개구리가 됩니다.",
                "think_aloud_prompt": "번호표 말(먼저 ➔ 그다음 ➔ 얼마 뒤 ➔ 마지막으로)을 따라 개구리가 자라는 기차 칸을 채워 볼까요?",
                "cloze_sentences": [
                    "• [1칸: 먼저] 연못에 투명한 ( {b1} )을 낳음 ➔ [2칸: 그다음] 물속에서 아가미로 숨 쉬는 ( {b2} )가 됨",
                    "• [3칸: 얼마 뒤] ( {b3} )가 먼저 나오고 이어서 앞다리가 나옴 ➔ [4칸: 마지막으로] 꼬리가 사라지고 어른 개구리가 됨!"
                ],
                "blanks": [
                    {"id": "b1", "correct": "알덩이", "options": ["알덩이", "앞다리", "개구리"]},
                    {"id": "b2", "correct": "올챙이", "options": ["올챙이", "나비", "씨앗"]},
                    {"id": "b3", "correct": "뒷다리", "options": ["뒷다리", "앞다리", "날개"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D2(순서 뒤바뀜 함정) 참/거짓 판별하기",
                "desc": "수능형 문제에서는 ‘앞다리’와 ‘뒷다리’처럼 순서를 살짝 바꾸어 놓아요! 속지 않고 찾아내 볼까요?",
                "items": [
                    {
                        "statement": "올챙이는 앞다리가 먼저 자라나고, 그다음에 뒷다리가 나옵니다.",
                        "answer": "X",
                        "reason": "삐뽀삐뽀! [D2 순서 뒤바뀜 함정]이에요! 글에서 ‘뒷다리가 먼저 자라나고, 이어서 앞다리가 나옵니다’라고 했어요."
                    },
                    {
                        "statement": "올챙이의 다리가 나온 뒤에 꼬리가 점점 짧아져 사라집니다.",
                        "answer": "O",
                        "reason": "딩동댕! [얼마 뒤: 다리가 나옴] ➔ [마지막으로: 꼬리가 사라짐] 순서와 정확히 같아요!"
                    }
                ]
            }
        },

        "real_csat_test": {
            "test_title": "[실전 수능 대비 3지선다] 초2 통합교과 ‘개구리가 자라는 신기한 과정’",
            "passage_spec": "2문단 · 242자 · 56어절 · KReaD 930 · 4단계 과정도 결합 · 3지선다",
            "passage_title": "개구리가 자라는 신기한 과정",
            "paragraphs": [
                "개구리는 자라면서 몸의 생김새와 사는 곳이 크게 바뀌는 동물입니다. 작은 알에서 깨어나 어른 개구리가 되기까지 어떤 차례로 자라는지 알아봅시다.",
                "<span class='cue-span' data-cue='g2-c1'>먼저</span> 따뜻한 봄이 되면 어미 개구리가 연못에 투명한 알덩이를 낳습니다. <span class='cue-span' data-cue='g2-c2'>그다음</span> 알에서 깨어난 올챙이는 물속에서 아가미로 숨을 쉬며 긴 꼬리를 흔들어 헤엄칩니다. <span class='cue-span' data-cue='g2-c3'>얼마 뒤</span> 올챙이는 뒷다리가 먼저 자라나고, 이어서 앞다리가 쑥 나옵니다. <span class='cue-span' data-cue='g2-c4'>마지막으로</span> 꼬리가 점점 짧아져 사라지면 땅 위로 올라와 허파와 피부로 숨을 쉬는 어른 개구리가 됩니다."
            ],
            "vocab_notes": [
                {"word": "알덩이", "tier": "Tier 3 (교과개념)", "desc": "개구리의 알들이 뭉쳐 있는 덩어리"},
                {"word": "아가미", "tier": "Tier 3 (교과개념)", "desc": "물고기나 올챙이가 물속에서 숨을 쉬는 기관"},
                {"word": "차례", "tier": "Tier 2 (사고어)", "desc": "일이나 과정이 순서대로 이어지는 단계"}
            ],
            "visual_html": """
              <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px; padding:14px; margin:12px 0;">
                <div style="font-weight:800; color:#1E40AF; margin-bottom:8px;">🐸 [과정 순서도] 개구리의 한살이 4단계</div>
                <div style="display:flex; align-items:center; justify-content:space-between; gap:6px; flex-wrap:wrap; text-align:center;">
                  <div style="flex:1; background:#fff; padding:9px; border-radius:8px; border:2px solid #60A5FA;">
                    <span style="font-size:0.75rem; color:#2563EB; font-weight:700;">① 먼저</span><br><b>알덩이</b><br><span style="font-size:0.78rem; color:#64748B;">봄·연못</span>
                  </div>
                  <div style="font-weight:900; color:#2563EB;">➔</div>
                  <div style="flex:1; background:#fff; padding:9px; border-radius:8px; border:2px solid #60A5FA;">
                    <span style="font-size:0.75rem; color:#2563EB; font-weight:700;">② 그다음</span><br><b>올챙이</b><br><span style="font-size:0.78rem; color:#64748B;">아가미·꼬리 헤엄</span>
                  </div>
                  <div style="font-weight:900; color:#2563EB;">➔</div>
                  <div style="flex:1; background:#FEF9C3; padding:9px; border-radius:8px; border:2px dashed #CA8A04;">
                    <span style="font-size:0.75rem; color:#A16207; font-weight:700;">③ 얼마 뒤</span><br><b>( ㉠ ) ➔ 앞다리</b><br><span style="font-size:0.78rem; color:#A16207;">다리 자라기</span>
                  </div>
                  <div style="font-weight:900; color:#2563EB;">➔</div>
                  <div style="flex:1; background:#fff; padding:9px; border-radius:8px; border:2px solid #22C55E;">
                    <span style="font-size:0.75rem; color:#15803D; font-weight:700;">④ 마지막으로</span><br><b>어른 개구리</b><br><span style="font-size:0.78rem; color:#64748B;">꼬리 사라짐·허파 호흡</span>
                  </div>
                </div>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-READ-V1-3 (과정 순서 도식 빈칸 추론형 - 3지선다)",
                    "stem": "윗글과 [과정 순서도]를 함께 읽을 때, ③번 단계의 빈칸 <u>( ㉠ )</u>에 들어갈 알맞은 말은 무엇인가요?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "뒷다리",
                            "is_correct": True,
                            "formula": "정답 공식: [2문단 '얼마 뒤 올챙이는 뒷다리가 먼저 자라나고, 이어서 앞다리가 쑥 나옵니다' 일치]",
                            "explanation": "🎉 **[처방 성공! 정답]** 2문단에서 ‘얼마 뒤 올챙이는 **뒷다리**가 먼저 자라나고, 이어서 앞다리가 쑥 나옵니다’라고 설명했어요."
                        },
                        {
                            "no": 2,
                            "text": "날개",
                            "is_correct": False,
                            "formula": "오답 공식 [D6 본문 외 무관 개념]: 곤충·새의 신체 부위 혼입",
                            "explanation": "❌ **[D6 무관 개념 함정]** 개구리는 날개가 자라지 않아요."
                        },
                        {
                            "no": 3,
                            "text": "알덩이",
                            "is_correct": False,
                            "formula": "오답 공식 [D2 단계 역전]: ①번 첫 단계의 명칭을 ③번 단계에 잘못 배치",
                            "explanation": "❌ **[D2 순서 역전 함정]** ‘알덩이’는 ①번 맨 처음 단계예요."
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V1-1 (세부 정보 불일치 확인형 - 3지선다)",
                    "stem": "윗글의 내용과 <u>다른</u> 설명을 고르세요.",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "어미 개구리는 따뜻한 봄에 연못에 알덩이를 낳습니다.",
                            "is_correct": False,
                            "formula": "일치 선지: 2문단 첫 문장 사실 그대로 재진술",
                            "explanation": "⭕ 글의 내용과 같은 설명이에요. (문제는 **다른** 것을 고르는 문제예요!)"
                        },
                        {
                            "no": 2,
                            "text": "올챙이는 앞다리가 먼저 나온 다음에 뒷다리가 자라납니다.",
                            "is_correct": True,
                            "formula": "정답(불일치) - 오답 공식 [D2 선후 순서 왜곡]: [뒷다리 ➔ 앞다리]를 [앞다리 ➔ 뒷다리]로 역전!",
                            "explanation": "🎉 **[처방 성공! D2 순서 뒤바뀜 함정 간파]** 본문에서는 **‘뒷다리가 먼저 자라나고, 이어서 앞다리가 나온다’**고 했으므로 앞뒤 순서를 거꾸로 바꾼 이 선지가 정답(다른 설명)이에요!"
                        },
                        {
                            "no": 3,
                            "text": "어른 개구리가 되면 꼬리가 사라지고 땅 위로 올라옵니다.",
                            "is_correct": False,
                            "formula": "일치 선지: 2문단 마지막 문장 사실 재진술",
                            "explanation": "⭕ 글의 내용과 같은 설명이에요."
                        }
                    ]
                }
            ]
        }
    },

    # =========================================================================
    # 3학년: 이서연 (G3-EXP-V2-1 문맥 추론 — 다의어·개념어 의미 및 비례 관계 추론)
    # =========================================================================
    {
        "id": "g3_seoyeon",
        "grade_num": 3,
        "grade": "3학년",
        "grade_band": "초중 (3~4학년군 · 4지선다 기본형)",
        "persona_label": "초3 이서연 · 다의어·개념어 문맥추론 취약형",
        "slot_id": "G3-EXP-V2-1",
        "domain": "2. 추론적 이해",
        "layer": "V2-1 문맥 추론 (학술 개념어·다의어)",
        "sub_skill_name": "설명문 문맥 단서를 활용한 다의어(‘높다’, ‘크다’) 구별 및 과학 개념어(‘세기’, ‘높낮이’) 추론",
        "curriculum_concept": {
            "subject": "초3 과학 (2학기) · 초3 국어 (사전 찾기와 다의어)",
            "unit": "소리의 성질",
            "concept": "소리의 세기(진폭: 큰 소리/작은 소리)와 소리의 높낮이(진동수: 높은 소리/낮은 소리) 비교",
            "text_structure": "비교·대조 (Comparison & Contrast) + 인과"
        },
        "complexity_metrics": {
            "kread_target": "1045 (3학년 표준 1000~1090)",
            "current_kread": "950 (2학년 후반 수준 · -95p)",
            "para_count": "3문단 (10문장)",
            "char_count": "386자 (3학년 권장 320~450자)",
            "eojeol_count": "91어절 (문장당 평균 9.1어절)",
            "vocab_profile": "Tier 1(78%) · Tier 2(15%: 반면에, 비교, 구별) · Tier 3(7%: 떨림, 세기, 높낮이, 음판)",
            "csat_scaling": "4지선다 · 수능 어휘 문맥 의미 교체형 + 실험 조건 대조 추론형"
        },
        "mager_goal": "[조건] 3문단 비교 설명글이 주어졌을 때, [준거] 일상 다의어('높다')의 문맥적 의미와 과학 개념어('소리의 세기' vs '소리의 높낮이')의 차이를 85% 이상 정확히, [행동] 문맥 단서로 추론하고 구별할 수 있다.",
        "student_summary": "문단의 중심 내용은 파악하나, 과학·사회 지문에서 일상 다의어(‘높다, 크다, 차다’)가 학술적 의미로 쓰일 때 [D4 다의어 중심의미 고착] 함정에 자주 빠짐",

        "diagnostic_test": {
            "passage_title": "[진단 미니 지문] 자석의 극과 나침반 (초3 과학 ‘자석의 이용’)",
            "passage_spec": "2문단 · 310자 · KReaD 1030 · 4지선다",
            "paragraphs": [
                "막대자석에 철로 된 클립을 가까이 가져가면 클립이 자석의 양 끝부분에 가장 많이 달라붙는다. 이처럼 자석에서 철로 된 물체를 끌어당기는 힘이 가장 센 양 끝부분을 자석의 ‘극’이라고 부른다.",
                "자석의 극에는 N극과 S극 두 가지가 있다. 자석을 공중에 매달아 놓으면 N극은 언제나 북쪽을 ㉠<u>가리키고</u>, S극은 남쪽을 향한다. 이러한 성질을 이용해 만든 도구가 바로 방향을 알려 주는 ‘나침반’이다."
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G3-EXP-V2-1",
                    "target_skill": "문맥 속 다의어의 정확한 의미 추론",
                    "stem": "윗글의 밑줄 친 ㉠‘가리키고’와 뜻이 가장 비슷하게 쓰인 문장은 무엇인가요?",
                    "options": [
                        {"no": 1, "text": "시계의 짧은바늘이 숫자 3을 가리키고 있다.", "is_correct": True, "trap": "정답 (어떤 방향이나 대상을 향하다)"},
                        {"no": 2, "text": "선생님께서 우리에게 재미있는 노래를 가르치고 계신다.", "is_correct": False, "trap": "D4 (음운 유사어 ‘가리키다’ ↔ ‘가르치다’ 혼동 함정)"},
                        {"no": 3, "text": "언니는 반찬 중에서 콩나물을 가리고 먹지 않는다.", "is_correct": False, "trap": "D4 (형태 유사어 ‘가리다’와 혼동)"},
                        {"no": 4, "text": "구름이 해를 가려서 날씨가 어두워졌다.", "is_correct": False, "trap": "D4 (동음이의어 ‘가리다[차단하다]’ 혼동)"}
                    ],
                    "student_selected": 2
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 84, "status": "good", "comment": "문단 중심 문장 찾기와 사실 확인 안정적"},
                {"domain": "2. 추론적 이해 (V2)", "score": 52, "status": "danger", "comment": "문맥 속 다의어·개념어 의미 추론(V2-1)에서 표면적 형태/기본 의미에 고착됨"},
                {"domain": "3. 비판적 이해 (V3)", "score": 75, "status": "good", "comment": "사실과 의견 구분하기 양호"},
                {"domain": "4. 표현·작문 (W)", "score": 68, "status": "warn", "comment": "비교·대조 접속어를 활용한 문단 쓰기 보강 필요"}
            ],
            "bottleneck": {
                "step1_rate": 80,
                "step2_rate": 38,
                "step3_rate": 52,
                "diagnosis_title": "Dick & Carey [Step 2: 앞뒤 문맥 호응어(짝꿍 말)를 통한 다의어 의미 연결 병목]",
                "diagnosis_detail": "밑줄 친 어휘 자체(Step 1)는 인지하지만, 앞뒤에 결합된 주어·목적어(‘N극이 북쪽을 ~’, ‘소리가 ~’)를 단서로 문맥 의미를 좁히지 못하고(Step 2 병목), 평소 익숙한 물리적 높이나 형태 유사어를 고르는 [D4 어휘 고착 함정]에 빠집니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "인과 역전", "vuln": 30},
                {"code": "D2", "name": "선후·방향 왜곡", "vuln": 35},
                {"code": "D3", "name": "한정어 과장", "vuln": 25},
                {"code": "D4", "name": "다의어·속성 교차 (집중 취약!)", "vuln": 90},
                {"code": "D5", "name": "주객 전도", "vuln": 40},
                {"code": "D6", "name": "외부 상식 함정", "vuln": 20}
            ],
            "backtracking_path": [
                {"grade": "2학년 선행", "code": "G2-COM-A5", "title": "비슷한 말·반대말 및 짝을 이루는 낱말(연어) 관계 익히기", "status": "review"},
                {"grade": "3학년 목표", "code": "G3-EXP-V2-1 (현재 목표)", "title": "문맥 단서를 활용해 다의어의 뜻과 교과 개념어 의미 추론하기", "status": "target"},
                {"grade": "4학년 확장", "code": "G4-EXP-V2-1 (후속 확장)", "title": "전문 학술어 및 한자어 개념을 문맥 속 풀어쓰기로 추론하기", "status": "next"}
            ]
        },

        "prescription_clinic": {
            "rx_title": "이서연 맞춤 처방전 #RX-G3-D4: [짝꿍 낱말(연어) 매칭 ➔ 다의어 ‘높다’ 문맥 추론 ➔ D4 어휘 고착 백신]",
            "rx_reason": "다의어(‘높다’)가 물리적 위치가 아니라 ‘소리의 성질(높낮이)’을 뜻할 때 앞뒤 짝꿍 말을 단서로 의미를 구별하는 집중 클리닉을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G2-COM-A5 짝꿍 낱말(주어·목적어)로 낱말 뜻 구별하기",
                "rule_box": "💡 **다의어 구별 공식**: 똑같은 **‘높다’**라도 앞에 오는 **짝꿍 말(주어)**이 `[산/건물이 높다 ➔ 아래에서 위까지 길이가 길다]`인지, `[소리가 높다 ➔ 음이 가늘고 맑다]`인지 먼저 확인해요!",
                "mini_question": "“합창단에서 소프라노는 가장 <u>높은</u> 소리를 낸다.”에서 ‘높은’과 같은 뜻으로 쓰인 것은?",
                "choices": ["실로폰의 짧은 음판을 치면 높은 음이 난다.", "우리 동네에서 가장 높은 산에 올라갔다."],
                "correct": "실로폰의 짧은 음판을 치면 높은 음이 난다.",
                "feedback": "정확해요! 둘 다 앞뒤에 ‘소리/음’이 와서 [소리의 높낮이가 위쪽에 있다]라는 뜻으로 쓰였어요."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G3-EXP-V2-1 소리의 ‘세기(큰 소리)’와 ‘높낮이(높은 소리)’ 문맥 단서 조립",
                "passage_snippet": "북을 <span class='rx-cue' data-tip='세기 원인: 세게 치면'>세게 치면</span> 북가죽이 크게 떨리면서 큰 소리가 나고, 약하게 치면 작게 떨리면서 작은 소리가 난다. 이처럼 소리의 크고 작은 정도를 ‘소리의 세기’라고 한다. 반면에 실로폰의 <span class='rx-cue' data-tip='높낮이 원인: 짧은 음판'>짧은 음판</span>을 치면 빠르게 떨리면서 <u>높은</u> 소리가 나고, 긴 음판을 치면 느리게 떨리면서 낮은 소리가 난다. 이처럼 소리의 높고 낮은 정도를 ‘소리의 높낮이’라고 한다.",
                "think_aloud_prompt": "노란색 단서를 클릭해 보고, ‘소리의 세기’와 ‘소리의 높낮이’가 각각 무엇에 따라 달라지는지 빈칸을 조립해 보세요!",
                "cloze_sentences": [
                    "• [소리의 세기(큰 소리/작은 소리)]: 물체를 치는 힘과 떨림의 ( {b1} )에 따라 결정됨",
                    "• [소리의 높낮이(높은 소리/낮은 소리)]: 음판의 길이와 떨리는 ( {b2} )에 따라 결정됨"
                ],
                "blanks": [
                    {"id": "b1", "correct": "크기(폭)", "options": ["크기(폭)", "빠르기", "색깔"]},
                    {"id": "b2", "correct": "빠르기(속도)", "options": ["빠르기(속도)", "크기(폭)", "무게"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D4(세기 ↔ 높낮이 속성 교차 함정) 참/거짓 판별하기",
                "desc": "수능에서는 ‘소리의 세기’ 설명과 ‘소리의 높낮이’ 설명을 슬쩍 바꿔치기(D4)합니다! 구별해 볼까요?",
                "items": [
                    {
                        "statement": "실로폰의 긴 음판을 세게 치면 짧은 음판을 칠 때보다 더 ‘높은’ 소리가 난다.",
                        "answer": "X",
                        "reason": "함정 포착! 세게 치면 소리가 ‘커지는(세기)’ 것일 뿐, 긴 음판은 여전히 ‘낮은’ 소리가 납니다! [D4 세기↔높낮이 교차 함정]"
                    },
                    {
                        "statement": "짧은 음판은 긴 음판보다 더 빠르게 떨리기 때문에 높은 소리가 난다.",
                        "answer": "O",
                        "reason": "정답입니다! [짧은 음판 ➔ 빠른 떨림 ➔ 높은 소리] 인과 관계를 정확히 파악했어요."
                    }
                ]
            }
        },

        "real_csat_test": {
            "test_title": "[실전 수능 대비 4지선다] 초3 과학 ‘작은북과 실로폰으로 알아보는 소리의 세기와 높낮이’",
            "passage_spec": "3문단 · 386자 · 91어절 · KReaD 1045 · 비교 실험표 결합 · 4지선다",
            "passage_title": "작은북과 실로폰으로 알아보는 소리의 세기와 높낮이",
            "paragraphs": [
                "우리 주변에서는 시계 초침 소리처럼 작은 소리도 나고, 천둥소리처럼 큰 소리도 난다. 또 호루라기 소리처럼 높은 소리도 있고, 큰북 소리처럼 낮은 소리도 있다. 과학에서는 이 두 가지 성질을 <span class='cue-span' data-cue='g3-c1'>‘소리의 세기’</span>와 <span class='cue-span' data-cue='g3-c2'>‘소리의 높낮이’</span>라고 부르며 엄격하게 구별한다.",
                "먼저 ‘소리의 세기’는 소리가 크고 작은 정도를 뜻한다. 작은북 위에 좁쌀을 올려놓고 채로 북을 <span class='cue-span' data-cue='g3-c3'>세게 치면 좁쌀이 높이 뛰어오르면서 큰 소리</span>가 난다. 반면에 북을 약하게 치면 좁쌀이 낮게 튀면서 작은 소리가 난다. 즉, 물체가 떨리는 폭이 클수록 더 큰 소리가 나는 것이다.",
                "이와 달리 ‘소리의 높낮이’는 소리가 높고 낮은 정도를 뜻한다. 길이가 다른 음판들이 나란히 놓인 실로폰을 같은 힘으로 쳐 보면, <span class='cue-span' data-cue='g3-c4'>길이가 짧은 음판에서는 ㉠<u>높은</u> 소리</span>가 나고 길이가 긴 음판에서는 낮은 소리가 난다. 이는 물체의 길이가 짧을수록 더 빠르게 떨리기 때문이다."
            ],
            "vocab_notes": [
                {"word": "구별하다", "tier": "Tier 2 (범교과 사고어)", "desc": "성질이나 종류에 따라 차이를 두어 가르다"},
                {"word": "소리의 세기", "tier": "Tier 3 (과학 개념어)", "desc": "소리가 크고 작은 정도 (떨리는 폭에 비례)"},
                {"word": "소리의 높낮이", "tier": "Tier 3 (과학 개념어)", "desc": "소리가 높고 낮은 정도 (떨리는 빠르기에 비례)"}
            ],
            "visual_html": """
              <div style="background:#F8FAFC; border:1px solid #CBD5E1; border-radius:10px; padding:14px; margin:12px 0;">
                <div style="font-weight:800; color:#1E293B; margin-bottom:8px;">📊 [실험 비교표] 소리의 세기 vs 소리의 높낮이</div>
                <table style="width:100%; border-collapse:collapse; font-size:0.86rem; background:#fff;">
                  <thead>
                    <tr style="background:#E2E8F0; color:#0F172A;">
                      <th style="border:1px solid #CBD5E1; padding:7px;">비교 기준</th>
                      <th style="border:1px solid #CBD5E1; padding:7px;">소리의 세기 (큰 소리 / 작은 소리)</th>
                      <th style="border:1px solid #CBD5E1; padding:7px;">소리의 높낮이 (높은 소리 / 낮은 소리)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td style="border:1px solid #CBD5E1; padding:7px; font-weight:700; text-align:center;">실험 악기</td>
                      <td style="border:1px solid #CBD5E1; padding:7px;">작은북 (위에 좁쌀 올려놓기)</td>
                      <td style="border:1px solid #CBD5E1; padding:7px;">실로폰 (음판 길이 비교하기)</td>
                    </tr>
                    <tr>
                      <td style="border:1px solid #CBD5E1; padding:7px; font-weight:700; text-align:center;">달라지는 조건</td>
                      <td style="border:1px solid #CBD5E1; padding:7px; color:#1D4ED8; font-weight:700;">치는 힘 ➔ 물체가 떨리는 폭</td>
                      <td style="border:1px solid #CBD5E1; padding:7px; color:#047857; font-weight:700;">음판 길이 ➔ 물체가 떨리는 빠르기</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-READ-V2-1 (수능 어휘 문맥적 의미 구별 전형 - 4지선다)",
                    "stem": "윗글의 밑줄 친 ㉠<u>높은</u>과 문맥적 의미가 가장 가까운 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "저 산은 구름이 걸릴 만큼 봉우리가 매우 <u>높다</u>.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 다의어 기본 의미 혼동]: 공간적 수직 길이(물리적 높이) 의미",
                            "explanation": "❌ **[D4 다의어 기본 의미 함정]** 산봉우리가 ‘높다’는 아래에서 위까지의 길이가 길다는 뜻이에요."
                        },
                        {
                            "no": 2,
                            "text": "언니가 부르는 노래는 고음 부분이 아주 <u>높아서</u> 따라 부르기 어렵다.",
                            "is_correct": True,
                            "formula": "정답 공식: [소리의 진동수가 많아 음이 가늘고 맑은 상태] 문맥 의미 일치",
                            "explanation": "🎉 **[처방 성공! 다의어 문맥 추론 완료]** ㉠‘높은 소리’와 마찬가지로 **소리의 음이 위쪽에 있다(고음이다)**는 뜻으로 쓰였어요!"
                        },
                        {
                            "no": 3,
                            "text": "오늘 낮에는 기온이 어제보다 훨씬 <u>높을</u> 것으로 예상된다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 다의어 주변 의미 2]: 온도 수치의 크기를 나타내는 의미",
                            "explanation": "❌ **오답이에요!** 기온이 ‘높다’는 온도의 수치가 크다는 뜻이에요."
                        },
                        {
                            "no": 4,
                            "text": "이순신 장군은 백성들에게 <u>높은</u> 존경을 받은 인물이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 다의어 추상·비유 의미]: 가치나 수준이 뛰어나다는 의미",
                            "explanation": "❌ **오답이에요!** 존경이 ‘높다’는 정도나 가치가 뛰어나다는 비유적 의미예요."
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V2-4 (<보기> 실험 상황 적용 및 개념 교차 검증형 - 4지선다)",
                    "stem": "윗글을 바탕으로 <보기>의 실험 결과를 추론한 내용으로 가장 적절한 것은?",
                    "bogi": "<보기>\n  민수는 실로폰에서 가장 짧은 ‘도’ 음판(㉮)과 가장 긴 ‘도’ 음판(㉯)을 준비했다. 그리고 작은북(㉰) 위에는 좁쌀을 올려놓았다.",
                    "options": [
                        {
                            "no": 1,
                            "text": "같은 힘으로 칠 때, ㉮ 음판은 ㉯ 음판보다 더 느리게 떨리면서 낮은 소리가 날 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D2 비례 방향 왜곡]: 짧은 음판(㉮)은 '빠르게 떨리며 높은 소리'가 남",
                            "explanation": "❌ **[D2 비례 방향 왜곡 함정]** 길이가 가장 짧은 ㉮ 음판은 가장 **빠르게 떨리면서 높은 소리**가 나요."
                        },
                        {
                            "no": 2,
                            "text": "㉯ 음판을 더 세게 치면 소리의 높낮이가 갑자기 높아져서 ㉮ 음판과 똑같은 음이 날 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 개념 속성 교차 치환]: 치는 힘(소리의 세기 조건)을 바꾸면 높낮이가 바뀐다고 왜곡",
                            "explanation": "❌ **[D4 세기↔높낮이 교차 함정]** 음판을 세게 치면 소리가 **커질(세기 증가)** 뿐, 긴 음판의 낮은 음이 높은 음으로 바뀌지는 않아요!"
                        },
                        {
                            "no": 3,
                            "text": "작은북(㉰)을 약하게 칠 때보다 세게 칠 때 북가죽 위의 좁쌀이 더 높이 뛰어오를 것이다.",
                            "is_correct": True,
                            "formula": "정답 공식: [2문단 '세게 치면 좁쌀이 높이 뛰어오르면서 큰 소리가 난다' 조건 일치]",
                            "explanation": "🎉 **[처방 성공! 정답]** 2문단에서 북을 세게 칠수록 떨리는 폭이 커져 **좁쌀이 더 높이 뛰어오르고 큰 소리가 난다**고 했어요."
                        },
                        {
                            "no": 4,
                            "text": "작은북(㉰)을 아무리 세게 쳐도 소리의 세기는 항상 일정하게 유지될 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D3 극단적 한정어 과장]: '항상 일정하게'로 인과 변화 부정",
                            "explanation": "❌ **[D3 한정어 과장 함정]** 치는 힘에 따라 소리의 세기는 달라져요."
                        }
                    ]
                }
            ]
        }
    },

    # =========================================================================
    # 4학년: 정우진 (G4-EXP-V2-3 시각자료 통합 추론 — 막대그래프 + 꺾은선그래프 결합)
    # =========================================================================
    {
        "id": "g4_woojin",
        "grade_num": 4,
        "grade": "4학년",
        "grade_band": "초중 (3~4학년군 · 4지선다 기본형)",
        "persona_label": "초4 정우진 · 복수 그래프 통합추론 취약형",
        "slot_id": "G4-EXP-V2-3",
        "domain": "2. 추론적 이해",
        "layer": "V2-3 시각자료(복합 도표) 통합 추론",
        "sub_skill_name": "본문 원리와 두 그래프(막대그래프 + 꺾은선그래프)의 추세를 결합하여 실험 결과 추론하기",
        "curriculum_concept": {
            "subject": "초4 과학 (식물의 생활) · 초4 수학 (막대그래프·꺾은선그래프)",
            "unit": "식물의 구조와 기능 / 자료의 표현",
            "concept": "식물 잎의 기공과 증산 작용 실험 + 시간대별 기온·습도 변화 그래프 결합 해석",
            "text_structure": "인과 (Cause & Effect) + 비교·대조"
        },
        "complexity_metrics": {
            "kread_target": "1150 (4학년 표준 1100~1190)",
            "current_kread": "1060 (3학년 후반 수준 · -90p)",
            "para_count": "4문단 (13문장)",
            "char_count": "512자 (4학년 권장 450~600자)",
            "eojeol_count": "121어절 (문장당 평균 9.3어절)",
            "vocab_profile": "Tier 1(72%) · Tier 2(18%: 비례, 감소, 비교, 활발하다) · Tier 3(10%: 증산 작용, 기공, 수증기, 눈금실린더)",
            "csat_scaling": "4지선다 · 복수 시각자료(막대+꺾은선) 수치·기울기 교차 검증형"
        },
        "mager_goal": "[조건] 증산 작용 원리 설명글과 [막대그래프(줄어든 물의 양)]·[꺾은선그래프(시간대별 기온·습도)]가 함께 주어졌을 때, [준거] 본문의 인과 조건과 두 그래프의 수치를 결합하여 85% 이상 정확히, [행동] 실험 결과와 시간대별 변화량을 추론할 수 있다.",
        "student_summary": "단일 표나 막대그래프는 읽으나, 2개의 그래프(막대+꺾은선)와 본문의 비례·반비례 조건을 동시에 결합할 때 [D2 증감 방향 왜곡] 함정에 자주 빠짐",

        "diagnostic_test": {
            "passage_title": "[진단 미니 지문] 물의 가열 시간과 온도 변화 꺾은선그래프 (초4 과학 ‘물의 상태 변화’)",
            "passage_spec": "2문단 · 340자 · KReaD 1120 · 4지선다",
            "paragraphs": [
                "비커에 담긴 물을 알코올램프로 가열하면 시간이 지남에 따라 물의 온도가 점점 올라간다. 이때 가열 시간(가로축)에 따른 물의 온도(세로축)를 점으로 찍어 선으로 이은 ‘꺾은선그래프’를 보면, 처음에는 선이 오른쪽 위로 가파르게 올라간다.",
                "그러나 물의 온도가 100℃에 도달해 물이 끓기 시작하면, 계속 불로 가열하더라도 온도가 더 이상 올라가지 않고 100℃에서 수평으로 일정하게 유지된다. 가열하는 열이 물의 온도를 높이는 대신 액체인 물을 기체인 수증기로 상태 변화시키는 데 모두 쓰이기 때문이다."
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G4-EXP-V2-3",
                    "target_skill": "꺾은선그래프의 구간별 기울기와 본문 원리 결합 추론",
                    "stem": "윗글을 바탕으로 ‘물이 끓기 시작한 뒤’의 꺾은선그래프 모양과 그 까닭을 바르게 짝지은 것은?",
                    "options": [
                        {"no": 1, "text": "선이 오른쪽 위로 계속 올라간다 — 불로 계속 가열하고 있기 때문이다.", "is_correct": False, "trap": "D2 (그래프 기울기 왜곡: 100℃ 이후 수평 구간을 상승으로 오인)"},
                        {"no": 2, "text": "선이 100℃ 높이에서 수평으로 평평하게 이어진다 — 열이 물을 수증기로 변화시키는 데 쓰이기 때문이다.", "is_correct": True, "trap": "정답 (그래프 수평 모양 + 상태 변화 원리 결합)"},
                        {"no": 3, "text": "선이 오른쪽 아래로 급격히 내려간다 — 수증기가 차갑게 식기 때문이다.", "is_correct": False, "trap": "D2 (증감 방향 역전 함정)"},
                        {"no": 4, "text": "선이 0℃까지 떨어진다 — 물이 얼음으로 변하기 때문이다.", "is_correct": False, "trap": "D4 (끓는점과 어는점 속성 혼동)"}
                    ],
                    "student_selected": 1
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 82, "status": "good", "comment": "실험 준비물과 과정 확인 양호"},
                {"domain": "2. 추론적 이해 (V2)", "score": 48, "status": "danger", "comment": "복수 시각자료(막대+꺾은선)와 본문 조건(비례/반비례) 결합 추론(V2-3) 취약"},
                {"domain": "3. 비판적 이해 (V3)", "score": 72, "status": "good", "comment": "자료의 적절성 판단 양호"},
                {"domain": "4. 표현·작문 (W)", "score": 65, "status": "warn", "comment": "그래프 수치를 인용하여 실험 결과 문단 쓰기(W2) 보강 필요"}
            ],
            "bottleneck": {
                "step1_rate": 84,
                "step2_rate": 41,
                "step3_rate": 46,
                "diagnosis_title": "Dick & Carey [Step 2: 본문 조건(‘기온↑·습도↓ ➔ 증산 작용 활발’)과 그래프 수치 매핑 병목]",
                "diagnosis_detail": "그래프의 숫자(Step 1)는 읽지만, 본문에 제시된 두 가지 조건(‘기온이 높을수록 + 습도가 낮을수록’)을 꺾은선그래프의 시간대별 구간과 짝짓지 못해(Step 2 병목), 증감 방향을 반대로 해석하는 [D2 증감 왜곡 함정]에 빠집니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "인과 역전", "vuln": 45},
                {"code": "D2", "name": "증감·기울기 왜곡 (집중 취약!)", "vuln": 89},
                {"code": "D3", "name": "단위·수치 과장", "vuln": 62},
                {"code": "D4", "name": "변인 교차 치환", "vuln": 55},
                {"code": "D5", "name": "주객 전도", "vuln": 30},
                {"code": "D6", "name": "외부 상식 함정", "vuln": 25}
            ],
            "backtracking_path": [
                {"grade": "3학년 선행", "code": "G3-EXP-V2-3", "title": "2차원 비교표의 가로줄·세로줄 교차점 정보 정확히 읽기", "status": "review"},
                {"grade": "4학년 목표", "code": "G4-EXP-V2-3 (현재 목표)", "title": "막대그래프와 꺾은선그래프의 추세를 본문 원리와 결합해 추론하기", "status": "target"},
                {"grade": "5학년 확장", "code": "G5-EXP-V2-3 (후속 확장)", "title": "비율 그래프와 다중 변수 통계표를 결합해 복합 인과 추론하기", "status": "next"}
            ]
        },

        "prescription_clinic": {
            "rx_title": "정우진 맞춤 처방전 #RX-G4-D2: [실험 대조군 표 읽기 ➔ 기온·습도 꺾은선 결합 조립 ➔ D2 증감 왜곡 백신]",
            "rx_reason": "4학년 과학·수학 통합의 핵심인 ‘복수 그래프(막대+꺾은선) 교차 읽기’를 위해, 본문의 비례·반비례 화살표(↑/↓)를 먼저 표시하고 그래프 수치를 대입하는 클리닉을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G3-EXP-V2-3 실험 조건(기름 막의 역할) 비교표 읽기",
                "rule_box": "💡 **실험 대조군 공식**: 물 위에 **‘식용유(기름)를 떨어뜨린 까닭’**은 비커 속 물이 공기 중으로 **자연 증발하는 것을 막아**, 오직 ‘잎’을 통해서만 물이 빠져나갔음을 증명하기 위해서예요!",
                "mini_question": "잎이 있는 나뭇가지(가)에서는 물이 35mL 줄었고, 잎을 모두 딴 나뭇가지(나)에서는 2mL만 줄었습니다. 물이 빠져나간 통로는 어디인가요?",
                "choices": ["식물의 잎(기공)", "눈금실린더의 유리벽"],
                "correct": "식물의 잎(기공)",
                "feedback": "정확해요! 두 실험의 유일한 차이점인 ‘잎’을 통해 물이 빠져나갔음을 알 수 있어요."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G4-EXP-V2-3 증산 작용 조건(기온·습도)과 그래프 결합 조립하기",
                "passage_snippet": "잎을 통한 물의 이동을 증명하기 위해 물이 담긴 눈금실린더 (가)에는 잎이 무성한 나뭇가지를, (나)에는 잎을 모두 딴 나뭇가지를 꽂고 물 위에 <span class='rx-cue' data-tip='자연 증발 차단!'>식용유</span>를 떨어뜨렸다. 증산 작용은 <span class='rx-cue' data-tip='조건: 햇빛 강함 + 기온↑ + 습도↓'>햇빛이 강하고 기온이 높을수록, 그리고 공기 중의 습도가 낮을수록</span> 더욱 활발하게 일어난다.",
                "think_aloud_prompt": "본문의 조건 화살표(기온↑ · 습도↓ = 증산 작용↑)를 보고 아래 빈칸을 완성해 보세요!",
                "cloze_sentences": [
                    "• [막대그래프 해석]: 잎이 있는 (가)에서 줄어든 물의 양(35mL)이 (나)(2mL)보다 훨씬 많은 까닭은 잎에서 ( {b1} )이 일어났기 때문임",
                    "• [꺾은선그래프 결합]: 하루 중 기온이 가장 높고(28℃) 습도가 가장 낮은 ( {b2} )에 (가)의 물이 가장 빠르게 줄어듦"
                ],
                "blanks": [
                    {"id": "b1", "correct": "증산 작용", "options": ["증산 작용", "자연 증발", "광합성 정지"]},
                    {"id": "b2", "correct": "오후 2시", "options": ["오후 2시", "오전 9시", "오후 6시"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D2(증감 방향 왜곡 함정) 참/거짓 판별하기",
                "desc": "수능에서는 ‘습도가 낮을수록 활발하다’를 ‘습도가 높을수록 활발하다’로 슬쩍 바꿉니다(D2)! 판별해 볼까요?",
                "items": [
                    {
                        "statement": "공기 중의 습도가 높고 기온이 낮을수록 식물의 증산 작용이 가장 활발하게 일어난다.",
                        "answer": "X",
                        "reason": "함정 포착! [D2 증감 방향 역전 함정]입니다. 본문에서 기온이 ‘높고’ 습도가 ‘낮을수록’ 활발하다고 했어요!"
                    },
                    {
                        "statement": "기온이 28℃로 가장 높고 습도가 40%로 가장 낮은 오후 2시에 줄어드는 물의 양이 가장 많다.",
                        "answer": "O",
                        "reason": "정확합니다! 본문 조건과 꺾은선그래프의 오후 2시 수치를 완벽하게 결합했어요."
                    }
                ]
            }
        },

        "real_csat_test": {
            "test_title": "[실전 수능 대비 4지선다] 초4 과학·수학 ‘식물의 증산 작용 실험과 시간대별 기온·습도 변화’",
            "passage_spec": "4문단 · 512자 · 121어절 · KReaD 1150 · 복합 그래프(막대+꺾은선) 결합 · 4지선다",
            "passage_title": "식물의 증산 작용 실험과 시간대별 기온·습도 변화",
            "paragraphs": [
                "식물의 뿌리에서 흡수한 물은 줄기의 물관을 따라 잎까지 이동한다. 잎에 도달한 물의 일부는 광합성에 쓰이지만, 대부분은 잎 뒷면에 있는 작은 구멍인 <span class='cue-span' data-cue='g4-c1'>‘기공’을 통해 수증기 형태로 식물 밖으로 빠져나간다. 이를 ‘증산 작용’</span>이라고 한다.",
                "증산 작용은 식물이 살아가는 데 매우 중요한 역할을 한다. 잎에서 물이 수증기로 빠져나가면 그 빈자리를 채우기 위해 뿌리에서 흡수한 물을 위쪽 줄기와 잎까지 계속 끌어 올리는 힘이 생긴다. 또한 더운 날 땀이 식으면서 체온이 내려가듯이 식물 주변의 온도를 낮추어 준다.",
                "잎을 통한 물의 이동을 확인하기 위해 똑같은 양(200mL)의 물이 담긴 눈금실린더 <span class='cue-span' data-cue='g4-c2'>(가)에는 잎이 무성한 나뭇가지를, (나)에는 잎을 모두 딴 나뭇가지</span>를 꽂았다. 그다음 눈금실린더 속의 물이 공기 중으로 <span class='cue-span' data-cue='g4-c3'>자연 증발하는 것을 막으려고 물 표면 위에 식용유를 한 방울씩</span> 떨어뜨린 뒤 햇빛이 잘 드는 창가에 두었다.",
                "증산 작용은 기공이 활짝 열릴 때 활발하게 일어난다. 따라서 <span class='cue-span' data-cue='g4-c4'>햇빛이 강하고 기온이 높을수록, 그리고 공기 중의 습도가 낮아 건조할수록</span> 줄어드는 물의 양이 많아진다."
            ],
            "vocab_notes": [
                {"word": "기공(氣孔)", "tier": "Tier 3 (과학 개념어)", "desc": "식물 잎 표면에 공기와 수증기가 드나드는 작은 구멍"},
                {"word": "증산 작용", "tier": "Tier 3 (과학 개념어)", "desc": "식물 속의 물이 기공을 통해 수증기로 빠져나가는 현상"},
                {"word": "습도(濕度)", "tier": "Tier 3 (과학 개념어)", "desc": "공기 중에 수증기가 포함되어 있는 정도"}
            ],
            "visual_html": """
              <div style="display:grid; grid-template-columns:1fr 1.2fr; gap:10px; margin:12px 0;">
                <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; padding:12px;">
                  <div style="font-weight:800; font-size:0.84rem; color:#166534; margin-bottom:8px;">📊 [자료 1: 막대그래프] 6시간 뒤 줄어든 물의 양</div>
                  <div style="display:flex; align-items:flex-end; justify-content:space-around; height:105px; padding-top:14px; border-bottom:2px solid #64748B;">
                    <div style="text-align:center;">
                      <div style="font-size:0.76rem; font-weight:800; color:#15803D;">35mL</div>
                      <div style="width:44px; height:72px; background:#22C55E; border-radius:4px 4px 0 0; margin:0 auto;"></div>
                    </div>
                    <div style="text-align:center;">
                      <div style="font-size:0.76rem; font-weight:800; color:#64748B;">2mL</div>
                      <div style="width:44px; height:8px; background:#94A3B8; border-radius:4px 4px 0 0; margin:0 auto;"></div>
                    </div>
                  </div>
                  <div style="display:flex; justify-content:space-around; font-size:0.76rem; font-weight:700; margin-top:6px;">
                    <span>(가) 잎 있음</span>
                    <span>(나) 잎 없음</span>
                  </div>
                </div>
                <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px; padding:12px;">
                  <div style="font-weight:800; font-size:0.84rem; color:#1E40AF; margin-bottom:6px;">📈 [자료 2: 꺾은선 데이터] 창가의 시간대별 기온·습도</div>
                  <table style="width:100%; border-collapse:collapse; font-size:0.78rem; background:#fff; text-align:center;">
                    <thead>
                      <tr style="background:#DBEAFE;">
                        <th style="border:1px solid #93C5FD; padding:4px;">시각</th>
                        <th style="border:1px solid #93C5FD; padding:4px;">오전 9시</th>
                        <th style="border:1px solid #93C5FD; padding:4px;">낮 12시</th>
                        <th style="border:1px solid #93C5FD; padding:4px; background:#FEF08A;">오후 2시</th>
                        <th style="border:1px solid #93C5FD; padding:4px;">오후 5시</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td style="border:1px solid #CBD5E1; padding:4px; font-weight:700; color:#DC2626;">기온(℃)</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">19℃</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">25℃</td>
                        <td style="border:1px solid #CBD5E1; padding:4px; font-weight:800; color:#DC2626; background:#FEF9C3;">28℃ (최고)</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">22℃</td>
                      </tr>
                      <tr>
                        <td style="border:1px solid #CBD5E1; padding:4px; font-weight:700; color:#2563EB;">습도(%)</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">65%</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">50%</td>
                        <td style="border:1px solid #CBD5E1; padding:4px; font-weight:800; color:#2563EB; background:#FEF9C3;">40% (최저)</td>
                        <td style="border:1px solid #CBD5E1; padding:4px;">55%</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-READ-V2-3 (수능 복수 도표·본문 통합 추론 전형 - 4지선다)",
                    "stem": "윗글과 [자료 1], [자료 2]를 함께 이해한 내용으로 가장 적절한 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "[자료 1]에서 (가)보다 (나)의 물이 훨씬 적게 줄어든 것은 (나)에만 식용유를 떨어뜨렸기 때문이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 실험 통제 변인 왜곡]: 식용유는 (가)와 (나) 모두에 똑같이 떨어뜨림",
                            "explanation": "❌ **[D4 통제 변인 왜곡 함정]** 3문단에서 식용유는 (가)와 (나)에 똑같이 한 방울씩 떨어뜨렸어요. 물의 양이 차이 난 까닭은 **잎의 유무** 때문이에요."
                        },
                        {
                            "no": 2,
                            "text": "[자료 2]의 네 시각 가운데 (가) 눈금실린더의 물이 가장 빠르게 줄어들었을 시각은 기온이 가장 높고 습도가 가장 낮은 ‘오후 2시’이다.",
                            "is_correct": True,
                            "formula": "정답 공식: [4문단 '기온이 높을수록 + 습도가 낮을수록 활발'] + [자료 2 오후 2시(28℃, 40%) 매칭]",
                            "explanation": "🎉 **[처방 성공! 복수 그래프 통합 추론 완료]** 4문단의 조건(기온 최고 + 습도 최저)과 [자료 2]의 오후 2시 데이터(28℃, 40%)를 정확히 결합했어요!"
                        },
                        {
                            "no": 3,
                            "text": "[자료 2]에서 오전 9시는 오후 2시보다 습도가 더 높으므로 증산 작용이 오후 2시보다 더 활발하게 일어났을 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D2 비례/반비례 방향 역전]: 습도는 '낮을수록' 증산 작용이 활발함",
                            "explanation": "❌ **[D2 증감 방향 역전 함정]** 습도가 높으면 공기 중에 수증기가 많아 증산 작용이 오히려 둔해져요."
                        },
                        {
                            "no": 4,
                            "text": "(가)에서 빠져나간 35mL의 물은 모두 뿌리 끝을 통해 눈금실린더 밖으로 흘러나간 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D5 이동 방향 및 기관 전도]: [뿌리 흡수 ➔ 잎 기공 배출]을 거꾸로 서술",
                            "explanation": "❌ **[D5 이동 방향 전도 함정]** 물은 줄기를 따라 올라가 **잎의 기공**을 통해 수증기로 빠져나갔어요."
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V2-2 (실험 설계 이유 및 생략 원리 추론형 - 4지선다)",
                    "stem": "윗글의 실험에서 눈금실린더의 물 표면 위에 ‘식용유’를 떨어뜨린 까닭으로 가장 알맞은 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "나뭇가지에 필요한 영양분을 물 대신 공급해 주기 위해서이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D6 본문 외 상식 함정]: 식용유를 식물 영양제로 왜곡",
                            "explanation": "❌ **[D6 무관 상식 함정]** 식용유는 영양분이 아니라 물의 증발을 막는 기름 막 역할을 해요."
                        },
                        {
                            "no": 2,
                            "text": "잎의 기공을 기름으로 막아 증산 작용이 일어나지 못하게 하려는 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 대상 위치 치환]: '물 표면'에 떨어뜨린 것을 '잎의 기공'에 발랐다고 왜곡",
                            "explanation": "❌ **[D4 위치 치환 함정]** 식용유는 잎이 아니라 눈금실린더의 **물 표면 위**에 떨어뜨렸어요."
                        },
                        {
                            "no": 3,
                            "text": "눈금실린더 속의 물이 공기 중으로 자연 증발하여 줄어드는 것을 막기 위해서이다.",
                            "is_correct": True,
                            "formula": "정답 공식: [3문단 '물이 공기 중으로 자연 증발하는 것을 막으려고' 명시적 이유 확인]",
                            "explanation": "🎉 **[처방 성공! 정답]** 물 표면에서 저절로 증발하는 양을 차단해야 **오직 잎(증산 작용)을 통해 빠져나간 물의 양**만 정확히 잴 수 있기 때문이에요!"
                        },
                        {
                            "no": 4,
                            "text": "눈금실린더 주변의 공기 습도를 100%로 높이기 위해서이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D3·D6 무관 수치 왜곡]: 습도 100% 조작과 무관함",
                            "explanation": "❌ **오답이에요!** 식용유는 물 표면의 자연 증발을 막기 위해 사용한 것이에요."
                        }
                    ]
                }
            ]
        }
    },

    # =========================================================================
    # 5학년: 김민준 (G5-EXP-V3-2 & V2-3 — 비판적 평가 4대 준거 및 다중 도표 인과 추론)
    # =========================================================================
    {
        "id": "g5_minjun",
        "grade_num": 5,
        "grade": "5학년",
        "grade_band": "초고 (5~6학년군 · 5지선다 수능 실전형)",
        "persona_label": "초5 김민준 · 도표인과·비판적평가 취약형",
        "slot_id": "G5-EXP-V3-2",
        "domain": "3. 비판적 이해 & 2. 추론적 이해",
        "layer": "V3-2 자료 타당성·신뢰성 비판 & V2-3 다중 도표 인과 추론",
        "sub_skill_name": "설명문 4대 평가 준거(정확성·공신력·객관성·공정성)로 매체 글 비판 및 상하위 분류·인과 추론",
        "curriculum_concept": {
            "subject": "초5 과학 (다양한 생물과 우리 생활) · 초5 국어 (매체 자료 비판적 읽기)",
            "unit": "세균과 곰팡이가 우리 생활에 미치는 영향",
            "concept": "균계(곰팡이·버섯)와 세균계의 분류 특성 및 생태계 분해자·발효·질병의 양면성",
            "text_structure": "분류·구분 + 비교·대조 + 인과"
        },
        "complexity_metrics": {
            "kread_target": "1245 (5학년 표준 1200~1290)",
            "current_kread": "1130 (4학년 중반 수준 · -115p)",
            "para_count": "5문단 (16문장)",
            "char_count": "695자 (5학년 권장 600~750자)",
            "eojeol_count": "164어절 (문장당 평균 10.3어절)",
            "vocab_profile": "Tier 1(66%) · Tier 2(22%: 편향, 객관성, 공신력, 환원) · Tier 3(12%: 균계, 세균계, 유기물, 무기물, 분해자, 발효)",
            "csat_scaling": "5지선다 · 부정 발문 + <보기> 왜곡 매체 글 비판적 평가 전형"
        },
        "mager_goal": "[조건] 미생물의 양면성을 다룬 5문단 설명문과 편향된 인터넷 게시글 <보기>가 주어졌을 때, [준거] 정확성·출처 공신력·서술 객관성·관점 공정성의 4대 준거와 분류·인과 원리를 적용하여 5지선다에서 85% 이상 정확히, [행동] 부적절한 평가와 인과 역전 함정을 판별할 수 있다.",
        "student_summary": "사실적 확인은 우수하나, 상하위 분류(종류)와 전체-부분 분석(부품)을 구별하거나 다중 인과·평가 준거를 적용할 때 [D1 인과 역전]·[D4 속성 교차] 함정에 자주 빠짐",

        "diagnostic_test": {
            "passage_title": "[진단 미니 지문] 열의 이동 방법 세 가지와 보온병의 구조 (초5 과학 ‘온도와 열’)",
            "passage_spec": "2문단 · 540자 · KReaD 1230 · 5지선다 축약 진단",
            "paragraphs": [
                "온도가 다른 두 물체가 접촉하거나 떨어져 있을 때 열은 항상 온도가 높은 곳에서 낮은 곳으로 이동한다. 열이 이동하는 방법은 물질의 상태와 전달 방식에 따라 크게 ‘전도’, ‘대류’, ‘복사’의 세 가지 종류로 나뉜다. 고체에서는 입자들이 이웃한 입자에게 열을 전달하는 ‘전도’가 일어나고, 액체나 기체에서는 물질이 직접 이동하는 ‘대류’가 일어난다. 반면에 ‘복사’는 물질의 도움 없이 열이 직접 이동하는 방법이다.",
                "‘보온병’은 이러한 열의 이동 방법 세 가지를 모두 막아 물의 온도를 유지하도록 설계된 기구이다. 보온병은 플라스틱 마개, 이중 벽 사이의 진공 층, 은도금한 안쪽 유리벽이라는 구성 부품으로 이루어진다. 이중 벽 사이의 공기를 빼낸 ‘진공 층’은 열을 전달할 입자가 아예 없도록 만들어 전도와 대류를 동시에 차단하고, ‘은도금 벽’은 복사열을 반사하여 열 손실을 줄인다."
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G5-EXP-V1-2",
                    "target_skill": "어휘 위계 구분 (상하위 분류 vs 전체-부분 분석)",
                    "stem": "윗글에 쓰인 핵심 개념들의 관계를 정리한 것으로 가장 적절한 것은?",
                    "options": [
                        {"no": 1, "text": "‘열의 이동 방법’과 ‘전도·대류·복사’는 하나의 기구를 이루는 부품을 쪼갠 ‘전체-부분(분석)’ 관계이다.", "is_correct": False, "trap": "D4 (상하위 분류 ↔ 전체-부분 분석 교차 함정)"},
                        {"no": 2, "text": "‘보온병’과 ‘플라스틱 마개·진공 층·은도금 벽’은 전체 대상을 구성 요소로 나눈 ‘전체-부분(분석)’ 관계이다.", "is_correct": True, "trap": "정답 (전체-부분 분석 정확 식별)"},
                        {"no": 3, "text": "‘전도’와 ‘대류’는 물질의 도움 없이 열이 이동하는 방법에 속하는 하위 개념이다.", "is_correct": False, "trap": "D4 (복사의 속성을 전도·대류에 치환)"}
                    ],
                    "student_selected": 1
                },
                {
                    "q_no": 2,
                    "target_code": "G5-EXP-V2-2",
                    "target_skill": "생략된 인과·매개 원리 추론",
                    "stem": "윗글을 바탕으로 ‘보온병의 이중 벽 사이에 금이 가서 공기가 가득 들어찼을 때’ 일어날 결과로 가장 적절한 것은?",
                    "options": [
                        {"no": 1, "text": "진공 상태가 깨져 공기 입자를 통한 전도와 대류가 일어나므로 보온병 안의 뜨거운 물이 빠르게 식을 것이다.", "is_correct": True, "trap": "정답 (조건 변화에 따른 매개 인과 추론)"},
                        {"no": 2, "text": "안쪽 물이 빨리 식기 때문에 그 결과로 이중 벽 사이의 진공 층에 공기가 새로 생겨날 것이다.", "is_correct": False, "trap": "D1 (인과 역전 함정: 원인과 결과를 거꾸로 배치)"},
                        {"no": 3, "text": "공기 입자가 은도금 벽의 반사율을 높여 주므로 물의 온도가 오히려 더 높아질 것이다.", "is_correct": False, "trap": "D2 (증감 방향 왜곡 함정)"}
                    ],
                    "student_selected": 2
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 68, "status": "warn", "comment": "세부 정보 확인은 양호하나 분류(종류) vs 분석(구성 요소) 구분(V1-2)에서 혼동 발생"},
                {"domain": "2. 추론적 이해 (V2)", "score": 45, "status": "danger", "comment": "다단계 인과 추론(V2-2) 및 다중 자료 결합(V2-3)에서 인과 방향이 자주 뒤집힘"},
                {"domain": "3. 비판적 이해 (V3)", "score": 54, "status": "danger", "comment": "4대 평가 준거(정확성·공신력·객관성·공정성) 적용(V3-2) 보강 시급"},
                {"domain": "4. 표현·작문 (W)", "score": 72, "status": "good", "comment": "개요 작성 및 조건부 문장 작성 양호"}
            ],
            "bottleneck": {
                "step1_rate": 88,
                "step2_rate": 42,
                "step3_rate": 46,
                "diagnosis_title": "Dick & Carey [Step 2: ‘원인 ➔ 매개 원리 ➔ 결과’ 연결 및 평가 준거 매칭 병목]",
                "diagnosis_detail": "본문 속 핵심 어휘(Step 1)는 빠르게 찾지만, 두 문장 사이의 인과 방향(원인➔결과)과 4대 비판 준거를 연결하는 Step 2에서 병목이 발생하여, 수능 선지의 [D1 인과 역전]과 [D4 분류·분석/속성 교차] 함정에 반복적으로 걸리고 있습니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "인과 역전 (집중 취약!)", "vuln": 88},
                {"code": "D2", "name": "선후·증감 왜곡", "vuln": 50},
                {"code": "D3", "name": "한정어 과장", "vuln": 35},
                {"code": "D4", "name": "분류·속성 교차 (집중 취약!)", "vuln": 82},
                {"code": "D5", "name": "평가준거·주객 전도", "vuln": 58},
                {"code": "D6", "name": "외부 상식 함정", "vuln": 25}
            ],
            "backtracking_path": [
                {"grade": "4학년 선행", "code": "G4-EXP-V1-2", "title": "상하위 분류(‘종류’)와 전체-부분 분석(‘구성 요소’) 표지 구별하기", "status": "review"},
                {"grade": "5학년 목표", "code": "G5-EXP-V3-2 & V2-2 (현재 목표)", "title": "4대 평가 준거로 편향된 글 비판하기 및 다단계 인과 사슬 추론하기", "status": "target"},
                {"grade": "6학년 확장", "code": "G6-EXP-V3-3 (후속 확장)", "title": "동일 주제 복수 매체·관점 설명문의 재구성 및 종합 평가", "status": "next"}
            ]
        },

        "prescription_clinic": {
            "rx_title": "김민준 맞춤 처방전 #RX-G5-D1D4: [분류 vs 분석 구분 공식 ➔ 미생물 양면성 & 4대 평가 준거 조립 ➔ D1·D4 함정 백신]",
            "rx_reason": "5학년 설명문의 핵심인 ‘생물 분류 체계(균계 vs 세균계)’와 ‘매체 비판 4대 준거(정확성·공신력·객관성·공정성)’를 정복하고 인과 역전 함정을 깨뜨리는 클리닉을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G4-EXP-V1-2 ‘분류(종류)’ vs ‘분석(전체-부분)’ 1분 구분 공식",
                "rule_box": "💡 **1초 판별 공식**: 하위 항목에 **‘~은 상위 개념의 한 종류이다’**가 성립하면 **[상하위 분류]**(예: 미생물의 종류 ➔ 세균, 곰팡이)이고, **‘~은 전체를 이루는 부품/구성 요소이다’**가 성립하면 **[전체-부분 분석]**(예: 보온병 ➔ 마개, 진공 층)입니다!",
                "mini_question": "“곰팡이는 크게 푸른곰팡이, 누룩곰팡이, 털곰팡이로 나뉜다.”에서 쓰인 설명 방법은?",
                "choices": ["상하위 분류 (종류 나누기)", "전체-부분 분석 (부품 쪼개기)"],
                "correct": "상하위 분류 (종류 나누기)",
                "feedback": "정확합니다! 푸른곰팡이와 누룩곰팡이는 각각 곰팡이의 ‘한 종류’이므로 [상하위 분류]입니다."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G5-EXP-V3-2 미생물의 양면성과 설명문 4대 평가 준거 조립하기",
                "passage_snippet": "미생물은 세포 구조에 따라 <span class='rx-cue' data-tip='상하위 분류: 균계 vs 세균계'>‘균계(곰팡이·버섯)’와 ‘세균계(세균)’로 분류</span>된다. 일부 미생물은 식중독이나 무좀을 일으키지만, <span class='rx-cue' data-tip='유익한 역할 ①: 발효와 항생제'>김치·된장 발효와 페니실린(푸른곰팡이) 생산</span>을 돕고, 생태계에서 <span class='rx-cue' data-tip='유익한 역할 ②: 분해자(유기물➔무기물)'>죽은 생물의 유기물을 무기물로 분해</span>해 식물의 영양분으로 돌려보낸다. 따라서 미생물 정보를 읽을 때는 ① 사실의 정확성, ② 출처의 공신력, ③ 서술의 객관성, ④ 양면을 고루 다룬 관점의 공정성을 점검해야 한다.",
                "think_aloud_prompt": "노란색 단서를 확인하고, 인터넷 게시글의 문제점을 4대 평가 준거와 연결해 보세요!",
                "cloze_sentences": [
                    "• “어제 동네 친구한테 들었는데~” ➔ 검증되지 않은 출처이므로 ( {b1} ) 결여!",
                    "• “세균과 곰팡이는 끔찍하고 징그러운 존재다!” ➔ 감정적 표현을 썼으므로 ( {b2} ) 위배!",
                    "• “유익한 점은 모두 빼고 해로운 점만 부각함” ➔ 한쪽 측면만 다뤘으므로 ( {b3} ) 부족!"
                ],
                "blanks": [
                    {"id": "b1", "correct": "출처의 공신력", "options": ["출처의 공신력", "문장 길이", "분류 기준"]},
                    {"id": "b2", "correct": "서술의 객관성", "options": ["서술의 객관성", "자료의 최신성", "전체-부분 분석"]},
                    {"id": "b3", "correct": "관점의 공정성(균형성)", "options": ["관점의 공정성(균형성)", "맞춤법 표기", "도표의 단위"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D1(인과 역전) & D4(분류 속성 교차) 참/거짓 판별하기",
                "desc": "수능 5지선다에서 가장 많이 출제되는 인과 역전(D1)과 분류 교차(D4) 문장을 판별해 보세요!",
                "items": [
                    {
                        "statement": "세계 최초의 항생제인 페니실린은 세균계에 속하는 유산균에서 추출한 물질로 만들어졌다.",
                        "answer": "X",
                        "reason": "함정 포착! [D4 분류 속성 교차 함정]입니다. 페니실린은 유산균(세균계)이 아니라 균계에 속하는 ‘푸른곰팡이’에서 추출했어요!"
                    },
                    {
                        "statement": "숲속의 곰팡이와 세균이 사라지면 죽은 생물의 유기물이 무기물로 분해되지 않아 식물이 자랄 영양분이 부족해진다.",
                        "answer": "O",
                        "reason": "정확합니다! [분해자 소멸(원인) ➔ 유기물 분해 중단(매개) ➔ 식물 영양분 부족(결과)] 인과 사슬이 정확히 맞습니다."
                    }
                ]
            }
        },

        "real_csat_test": {
            "test_title": "[실전 수능 대비 5지선다] 초5 과학·국어 ‘우리 주변의 작은 생물, 세균과 곰팡이의 두 얼굴’",
            "passage_spec": "5문단 · 695자 · 164어절 · KReaD 1245 · 분류·생태 비율표 결합 · 5지선다",
            "passage_title": "우리 주변의 작은 생물, 세균과 곰팡이의 두 얼굴",
            "paragraphs": [
                "우리 주변의 공기, 흙, 물속, 심지어 우리 몸속에는 눈으로 직접 볼 수 없을 만큼 작은 생물인 ‘미생물’이 무수히 살아가고 있다. 미생물은 세포의 구조와 생김새에 따라 크게 <span class='cue-span' data-cue='g5-c1'>곰팡이·버섯 등이 속하는 ‘균계’와 대장균·유산균 등이 속하는 ‘세균계’로 분류</span>된다. 균계에 속하는 곰팡이는 몸이 실처럼 가는 ‘균사’로 이루어져 있으며 포자로 번식하는 반면, 세균계에 속하는 세균은 하나의 세포로만 이루어진 단세포 생물로 스스로 둘로 갈라지는 분열 방식으로 빠르게 번식한다.",
                "흔히 사람들은 세균과 곰팡이를 우리에게 질병과 피해만 주는 해로운 존재로 여기기 쉽다. 실제로 살모넬라균 같은 병원성 세균은 식중독이나 폐렴을 일으키고, 여름철 음식물이나 욕실 타일에 피는 일부 곰팡이는 호흡기 질환이나 무좀을 유발하기도 한다. 이처럼 인간에게 해를 끼치는 측면 때문에 미생물을 무조건 박멸해야 할 대상으로 오해하는 경우가 많다.",
                "그러나 <span class='cue-span' data-cue='g5-c2'>인간에게 질병을 일으키는 병원성 미생물은 전체 미생물의 1% 미만</span>에 불과하며, 대다수의 미생물은 인간과 자연 생태계에 없어서는 안 될 유익한 역할을 수행한다. 예컨대 김치와 요구르트를 익게 하는 ‘유산균’이나 된장·간장을 만드는 ‘누룩곰팡이’는 음식의 맛과 보존성을 높이는 유익한 발효 미생물이다. 또한 인류의 생명을 구한 최초의 항생제인 <span class='cue-span' data-cue='g5-c3'>‘페니실린’ 역시 푸른곰팡이에서 추출한 물질</span>로 만들어졌다.",
                "더 나아가 자연 생태계에서 곰팡이와 세균은 <span class='cue-span' data-cue='g5-c4'>죽은 동식물의 사체나 배설물 속 ‘유기물’을 잘게 쪼개어 ‘무기물’로 되돌려보내는 ‘분해자’ 역할</span>을 담당한다. 만약 숲속에 세균과 곰팡이가 모두 사라진다면 죽은 생물과 낙엽이 썩지 않고 그대로 쌓여 지구는 거대한 쓰레기장이 될 것이며, 식물이 다시 흡수할 영양분도 고갈될 것이다.",
                "따라서 미생물에 관한 매체 자료나 설명 글을 읽을 때에는 해로운 측면이나 유익한 측면 중 어느 한쪽만 과장하여 전달하지 않았는지 <span class='cue-span' data-cue='g5-c5'>‘관점의 공정성’을 따져 보아야 한다. 아울러 과학적 사실에 부합하는지(‘정확성’), 믿을 만한 전문 기관의 연구 결과인지(‘출처의 공신력’), 감정적 표현 없이 중립적으로 서술했는지(‘객관성’)</span>를 비판적으로 점검하는 태도가 필요하다."
            ],
            "vocab_notes": [
                {"word": "분류(分類)", "tier": "Tier 2 (학술 사고어)", "desc": "일정한 기준에 따라 상위 개념을 하위 종류들로 나누는 것"},
                {"word": "유기물 / 무기물", "tier": "Tier 3 (과학 개념어)", "desc": "생물체를 이루는 탄소 화합물(유기물)과 물·무기염류 같은 물질(무기물)"},
                {"word": "공신력(公信力)", "tier": "Tier 2 (비판적 독해어)", "desc": "사회적으로 대중에게 믿음을 줄 수 있는 공적인 신뢰도"}
            ],
            "visual_html": """
              <div style="background:#F8FAFC; border:1px solid #CBD5E1; border-radius:10px; padding:12px; margin:12px 0;">
                <div style="font-weight:800; font-size:0.86rem; color:#1E293B; margin-bottom:6px;">📋 [핵심 요약표] 균계 vs 세균계 분류 및 설명문 비판적 읽기 4대 준거</div>
                <div style="display:grid; grid-template-columns:1.1fr 1fr; gap:10px; font-size:0.8rem;">
                  <div style="background:#fff; padding:9px; border-radius:8px; border:1px solid #E2E8F0;">
                    <b style="color:#1D4ED8;">[생물 분류 비교]</b><br>
                    • <b>균계(곰팡이·버섯)</b>: 실 모양 ‘균사’ 구조, 포자 번식 (예: 누룩곰팡이, 푸른곰팡이)<br>
                    • <b>세균계(세균)</b>: 균사 없는 ‘단세포’ 구조, 분열 번식 (예: 유산균, 살모넬라균)
                  </div>
                  <div style="background:#FEFCE8; padding:9px; border-radius:8px; border:1px solid #FDE047;">
                    <b style="color:#A16207;">[설명문 비판적 읽기 4대 평가 준거]</b><br>
                    ① <b>정확성</b>(사실 부합) · ② <b>출처 공신력</b>(전문 기관)<br>
                    ③ <b>서술 객관성</b>(감정 배제) · ④ <b>관점 공정성</b>(양면 균형)
                  </div>
                </div>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-READ-V3-2 (수능 비판적 독해 전형: 4대 평가 준거 기반 매체 자료 비판형 - 5지선다)",
                    "stem": "윗글과 [설명문 비판적 읽기 4대 평가 준거]를 바탕으로 <보기>의 인터넷 게시글을 평가한 내용으로 적절하지 <u>않은</u> 것은?",
                    "bogi": "<보기> [인터넷 게시판 글: 우리 집 세균 박멸 대작전!]\n  세균과 곰팡이는 우리에게 식중독과 무좀만 일으키는 아주 끔찍하고 징그러운 백해무익(百害無益)한 존재입니다! 어제 동네 친구한테 들었는데, 세균을 완전히 없애려면 발효 식품인 된장과 김치도 절대 먹으면 안 된다고 합니다. 우리 모두 시중에서 파는 ‘○○ 강력 살균 스프레이’를 사서 집 안의 모든 미생물을 하나도 남김없이 없애야 합니다.",
                    "options": [
                        {
                            "no": 1,
                            "text": "‘끔찍하고 징그러운’과 같이 필자의 주관적인 감정과 혐오감을 드러내는 표현을 사용하여 설명의 ‘서술 객관성’을 해치고 있다.",
                            "is_correct": False,
                            "formula": "타당한 평가: [감정적 수식어 ➔ ③ 서술 객관성 위배 정확 매칭]",
                            "explanation": "⭕ **타당한 평가예요!** 객관적 사실을 전달해야 할 설명문에 '끔찍하고 징그러운' 같은 주관적 감정 어휘를 쓴 것은 **서술의 객관성**을 어긴 것이에요."
                        },
                        {
                            "no": 2,
                            "text": "전문 연구 기관의 자료가 아니라 ‘어제 동네 친구한테 들었는데’라는 불확실한 말을 근거로 삼아 ‘출처의 공신력’이 결여되어 있다.",
                            "is_correct": False,
                            "formula": "타당한 평가: [전언/카더라 ➔ ② 출처 공신력 결여 정확 매칭]",
                            "explanation": "⭕ **타당한 평가예요!** 검증되지 않은 주변 사람의 말을 출처로 삼았으므로 **출처의 공신력(신뢰성)**이 매우 낮아요."
                        },
                        {
                            "no": 3,
                            "text": "미생물이 발효 식품, 항생제, 생태계 물질 순환에 기여하는 유익한 측면은 모두 누락하고 해로운 점만 일방적으로 부각하여 ‘관점의 공정성’이 부족하다.",
                            "is_correct": False,
                            "formula": "타당한 평가: [일방적 편향 서술 ➔ ④ 관점 공정성 부족 정확 매칭]",
                            "explanation": "⭕ **타당한 평가예요!** 윗글 3~4문단에 나온 유익한 역할은 모두 빼고 '백해무익하다'며 한쪽 측면만 강조했으므로 **관점의 공정성(균형성)**을 잃었어요."
                        },
                        {
                            "no": 4,
                            "text": "된장과 김치 속 미생물까지 모두 병을 일으키는 해로운 균으로 왜곡하여 설명했으므로 ‘정보의 정확성’ 기준에 어긋난다.",
                            "is_correct": False,
                            "formula": "타당한 평가: [유익균 발효 사실 왜곡 ➔ ① 정보 정확성 위배 정확 매칭]",
                            "explanation": "⭕ **타당한 평가예요!** 윗글 3문단에서 된장(누룩곰팡이)과 김치(유산균)는 유익한 발효 식품이라고 했으므로 사실의 **정확성**에 어긋나요."
                        },
                        {
                            "no": 5,
                            "text": "특정 상품(‘○○ 살균 스프레이’) 구매를 유도한 것은 다양한 시각 도표를 함께 제시하여 독자의 이해를 도운 ‘서술 객관성’의 모범 사례이다.",
                            "is_correct": True,
                            "formula": "정답(부적절) - 오답 공식 [D5 평가 준거 역전 & D6 상업적 편향 미화]: 상업적 광고 의도와 시각자료 미제시를 정반대로 평가",
                            "explanation": "🎉 **[처방 성공! 정답(부적절한 평가)]** `<보기>`에는 시각 도표가 제시되지도 않았을뿐더러, 특정 상업 제품을 홍보하며 구매를 부추기는 것은 이해관계가 개입되어 **출처의 공정성과 설명문 본래의 객관적 정보 전달 목적을 심각하게 훼손**한 사례예요!"
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V1-2 & V2-2 (분류 기준 대조 및 생태계 인과 추론형 - 5지선다)",
                    "stem": "윗글을 읽고 추론한 내용으로 가장 적절한 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "대장균과 유산균은 몸이 실처럼 가는 균사로 이루어져 있으며 포자를 만들어 번식한다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 분류군 속성 교차 치환]: '균계(곰팡이)'의 속성을 '세균계(대장균·유산균)'에 치환",
                            "explanation": "❌ **[D4 분류 속성 교차 함정]** 균사로 이루어져 포자로 번식하는 것은 세균이 아니라 **균계(곰팡이·버섯)**의 특징이에요!"
                        },
                        {
                            "no": 2,
                            "text": "지구상에 존재하는 미생물의 절반 이상은 인간에게 식중독이나 폐렴을 일으키는 병원성 미생물이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D3 비율 수치 과장 왜곡]: 3문단 '1% 미만'을 '절반(50%) 이상'으로 과장",
                            "explanation": "❌ **[D3 수치 과장 함정]** 3문단에서 병원성 미생물은 전체 미생물의 **1% 미만**에 불과하다고 했어요."
                        },
                        {
                            "no": 3,
                            "text": "숲속의 세균과 곰팡이가 모두 사라지면 죽은 생물의 유기물이 무기물로 분해되지 않아 식물이 자랄 영양분이 부족해질 것이다.",
                            "is_correct": True,
                            "formula": "정답 공식: [4문단 분해자의 역할(유기물➔무기물 환원 및 식물 영양분 공급) 인과 추론 일치]",
                            "explanation": "🎉 **[처방 성공! 인과 추론 정답]** 4문단에서 곰팡이와 세균(분해자)이 사체의 유기물을 무기물로 쪼개어 흙으로 돌려보내야 식물이 영양분을 흡수할 수 있다고 했으므로 정확한 추론이에요!"
                        },
                        {
                            "no": 4,
                            "text": "세계 최초의 항생제인 페니실린은 세균계에 속하는 유산균에서 추출한 물질로 만들어졌다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 대상 속성 교차 치환]: '푸른곰팡이(균계)'를 '유산균(세균계)'으로 바꿔치기",
                            "explanation": "❌ **[D4 속성 교차 함정]** 페니실린은 세균계인 유산균이 아니라 균계에 속하는 **'푸른곰팡이'**에서 추출한 물질로 만들었어요."
                        },
                        {
                            "no": 5,
                            "text": "식물이 땅속 영양분을 먼저 모두 흡수했기 때문에 그 결과로 곰팡이가 죽은 생물의 사체를 유기물로 합성하는 것이다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D1 인과 역전 & 방향 왜곡]: [곰팡이의 유기물➔무기물 분해 ➔ 식물 영양분 흡수]를 거꾸로 서술",
                            "explanation": "❌ **[D1 인과 역전 함정]** 곰팡이가 먼저 유기물을 무기물로 분해해 주어야 식물이 영양분을 흡수할 수 있어요!"
                        }
                    ]
                }
            ]
        }
    },

    # =========================================================================
    # 6학년: 박지호 (G6-EXP-W5 & V2-2 — 수능 작문 3단계 퇴고 및 지구 열수지 연쇄 인과 추론)
    # =========================================================================
    {
        "id": "g6_jiho",
        "grade_num": 6,
        "grade": "6학년",
        "grade_band": "초고 (5~6학년군 · 5지선다 수능 실전 완성기)",
        "persona_label": "초6 박지호 · 수능작문 3단계퇴고·연쇄인과 완성형",
        "slot_id": "G6-EXP-W5",
        "domain": "4. 표현·작문 (수능 화법과 작문) & 2. 추론적 이해",
        "layer": "W5 3단계 고쳐쓰기 · W2 자료 활용 · V2-2 연쇄 인과 추론",
        "sub_skill_name": "복합 설명문(기후위기 열수지·알베도 보고서)의 [내용·조직·표현 호응] 3단계 퇴고 및 다중 인과 추론",
        "curriculum_concept": {
            "subject": "초6 과학(연소와 소화·기후) · 초6 사회(지구촌 환경문제) · 초6 국어(문장 성분의 호응과 고쳐쓰기)",
            "unit": "지구온난화의 과학적 메커니즘과 기후변화 보고서 고쳐쓰기",
            "concept": "지구의 열수지 균형(태양 복사 vs 지구 복사), 온실효과, 북극 해빙 감소에 따른 알베도(반사율) 양(+)의 되먹임",
            "text_structure": "인과 연쇄(양의 되먹임 루프) + 문제·해결"
        },
        "complexity_metrics": {
            "kread_target": "1355 (6학년 표준 1300~1390, 중1 브릿지)",
            "current_kread": "1250 (5학년 후반 수준 · -105p)",
            "para_count": "6문단 (20문장)",
            "char_count": "865자 (6학년 권장 750~950자)",
            "eojeol_count": "204어절 (문장당 평균 10.2어절)",
            "vocab_profile": "Tier 1(60%) · Tier 2(25%: 균형, 가속화, 상쇄, 되먹임, 호응, 통일성) · Tier 3(15%: 열수지, 복사 에너지, 알베도, 해빙)",
            "csat_scaling": "5지선다 · 수능 [독서] 다단계 인과 추론 + 수능 [화법과 작문] 3단계 퇴고 통합형"
        },
        "mager_goal": "[조건] 6문단 분량의 복합 과학·환경 설명문과 학생의 초고 퇴고 구간(㉠~㉤)이 주어졌을 때, [준거] ① 열수지·알베도 되먹임 인과 사슬과 ② 내용(근거 보충)·조직(통일성 위배 문장 삭제·접속어 교정)·표현(주어-서술어 호응) 3단계 퇴고 원리를 적용하여 5지선다에서 85% 이상 정확히, [행동] 부적절한 고쳐쓰기 방안과 연쇄 인과 추론 선지를 판별할 수 있다.",
        "student_summary": "독서 지문 사실 이해는 우수하나, 수능 [작문] 영역의 다매체 자료 결합(W2)과 [내용·조직·표현 호응] 3단계 퇴고(W5)에서 [D5 주어-서술어 호응 오류 미탐지] 및 [D1 접속어 역전 수정] 함정에 자주 빠짐",

        "diagnostic_test": {
            "passage_title": "[진단 미니 문항] 학생이 작성한 ‘도시 열섬 현상 보고서’ 초고 고쳐쓰기 (초6 국어·사회)",
            "passage_spec": "초고 1문단 · 290자 · KReaD 1330 · 5지선다 축약 진단",
            "paragraphs": [
                "도심의 기온이 주변 교외 지역보다 높게 나타나는 현상을 ‘열섬 현상’이라고 한다. ㉠<u>내가 생각하기에 열섬 현상이 일어나는 가장 큰 이유는 도심의 아스팔트와 콘크리트 건물이 낮 동안 태양열을 잔뜩 흡수했다가 밤에 뿜어내기 때문이다.</u> ㉡<u>그러나</u> 자동차 배기가스와 에어컨 실외기에서 나오는 인공열도 도심 기온을 높인다. ㉢<u>한편 우리 가족은 지난 주말에 도심 공원으로 즐거운 소풍을 다녀왔다.</u>"
            ],
            "questions": [
                {
                    "q_no": 1,
                    "target_code": "G6-EXP-W5",
                    "target_skill": "내용·조직·표현(호응) 3단계 통합 퇴고 점검",
                    "stem": "윗글의 ㉠~㉢을 고쳐 쓰기 위한 의견으로 적절하지 <u>않은</u> 것은?",
                    "options": [
                        {"no": 1, "text": "㉠: 주어 ‘이유는’과 서술어 ‘~때문이다’가 서로 호응하지 않으므로, 서술어를 ‘~것이다’로 고치거나 주어를 ‘열섬 현상이 일어나는 까닭은 ~ 때문이다’ 구조에 맞게 고친다.", "is_correct": False, "trap": "타당한 퇴고 ([6국04-05] 주어-서술어 호응 오류 교정)"},
                        {"no": 2, "text": "㉡: 앞 문장의 원인에 또 다른 원인을 덧붙이는 관계이므로, 역접 접속부사 ‘그러나’를 나열·첨가 접속부사 ‘또한’으로 고친다.", "is_correct": False, "trap": "타당한 퇴고 (문장 간 논리 관계에 맞는 접속부사 교정)"},
                        {"no": 3, "text": "㉢: 문단의 중심 내용(열섬 현상의 발생 원인)에서 벗어난 문장이라도 글의 흥미를 높여 주므로 삭제하지 않고 그대로 둔다.", "is_correct": True, "trap": "D5 (조직 수준 통일성 위배 문장 방치 함정 — 정답)"}
                    ],
                    "student_selected": 1
                }
            ]
        },
        "diagnosis_report": {
            "domain_scores": [
                {"domain": "1. 사실적 이해 (V1)", "score": 88, "status": "good", "comment": "복합 문단 핵심 정보 및 정의 파악 우수"},
                {"domain": "2. 추론적 이해 (V2)", "score": 76, "status": "good", "comment": "단일 인과 추론 양호, 양(+)의 되먹임 루프 추론 심화 가능"},
                {"domain": "3. 비판적 이해 (V3)", "score": 80, "status": "good", "comment": "출처 신뢰성 및 편향성 평가 안정적"},
                {"domain": "4. 표현·작문 (W)", "score": 48, "status": "danger", "comment": "수능 작문형 3단계 퇴고(W5) 및 주어-서술어·부사어 호응(`G6-COM-A2`) 집중 처방 필요"}
            ],
            "bottleneck": {
                "step1_rate": 86,
                "step2_rate": 52,
                "step3_rate": 44,
                "diagnosis_title": "Dick & Carey [Step 3: ‘내용(자료)·조직(통일성·접속어)·표현(호응)’ 3단계 퇴고 준거 동시 적용 병목]",
                "diagnosis_detail": "글의 어색한 느낌(Step 1)은 감지하지만, `[6국04-05]` 주어(‘이유는/원리는’)-서술어(‘~것이다’) 호응 규칙과 문단 통일성(조직 수준)을 엄밀히 구분해 판별하는 Step 3에서 병목이 발생하여 [D5 호응·통일성 역전] 및 [D1 접속어 역전 수정] 함정에 걸렸습니다."
            },
            "trap_radar": [
                {"code": "D1", "name": "접속어·인과 역전", "vuln": 65},
                {"code": "D2", "name": "선후·수치 왜곡", "vuln": 40},
                {"code": "D3", "name": "한정어 과장", "vuln": 30},
                {"code": "D4", "name": "자료 교차 오독", "vuln": 55},
                {"code": "D5", "name": "호응·통일성 역전 (집중 취약!)", "vuln": 90},
                {"code": "D6", "name": "외부 상식 함정", "vuln": 25}
            ],
            "backtracking_path": [
                {"grade": "6학년 공통기초", "code": "G6-COM-A2 / A3", "title": "주어-서술어·부사어 호응 규칙 및 접속부사 기능 판별 (`[6국04-05]`)", "status": "review"},
                {"grade": "6학년 목표", "code": "G6-EXP-W5 & V2-2 (현재 목표)", "title": "내용·조직·표현 3단계 통합 고쳐쓰기 및 열수지·알베도 연쇄 인과 추론", "status": "target"},
                {"grade": "중1·수능 브릿지", "code": "CSAT-WRIT-W5", "title": "수능 [화법과 작문] 복수 자료 결합 초고 수정·보완 실전 완성", "status": "next"}
            ]
        },

        "prescription_clinic": {
            "rx_title": "박지호 맞춤 처방전 #RX-G6-D5: [주술·부사어 호응 3대 공식 ➔ 3단계 퇴고 매트릭스 조립 ➔ D1·D5 퇴고 함정 백신]",
            "rx_reason": "수능 ‘화법과 작문’ 고쳐쓰기 문항과 6학년 문법 성취기준(`[6국04-05]`)의 핵심인 **호응 규칙** 및 **3단계 퇴고(내용·조직·표현)**를 완벽히 체화하는 클리닉을 처방합니다.",
            "step0_remedial": {
                "badge": "[선행 징검다리 복습] G6-COM-A2 수능 필수 주어-서술어·부사어 호응 3대 공식",
                "rule_box": "💡 **호응 3대 공식**: ① **‘내 생각은 / 핵심 원리는 / 문제점은 ~ 때문이다(❌) ➔ ~ 것이다(⭕)’**, ② **‘왜냐하면 ~ 때문이다(⭕)’**, ③ **‘결코 / 전혀 / 비록 ~ 없다/아니다/할지라도(⭕)’**",
                "mini_question": "“북극 해빙이 빠르게 줄어드는 가장 큰 원인은 지구온난화로 기온이 ( ).” — 괄호에 알맞은 서술어는?",
                "choices": ["높아졌기 때문이다 (❌ 주술 불호응)", "높아진 것이다 (⭕ '원인은 ~ 것이다' 호응)"],
                "correct": "높아진 것이다 (⭕ '원인은 ~ 것이다' 호응)",
                "feedback": "완벽합니다! 주어 ‘원인은’은 서술어 ‘~것이다’(또는 ‘~점이다’)와 호응해야 문법적으로 바른 문장이 됩니다."
            },
            "step1_2_drill": {
                "badge": "[본 처방 훈련] G6-EXP-W5 설명문 3단계 퇴고(내용·조직·표현) 점검 매트릭스 조립",
                "passage_snippet": "① <span class='rx-cue' data-tip='내용 수준: 객관적 통계 보충'>[내용 수준]</span> ‘온실가스가 많이 늘었다’처럼 막연한 진술은 구체적인 통계 수치로 보충한다. ② <span class='rx-cue' data-tip='조직 수준: 통일성 위배 삭제 & 접속어 점검'>[조직 수준]</span> 문단 중심 생각에서 벗어난 문장(통일성 위배)은 삭제하고, 앞뒤 문장 관계(인과 ‘따라서’ vs 역접 ‘그러나’)에 맞는 접속부사를 쓴다. ③ <span class='rx-cue' data-tip='표현 수준: 주어-서술어 호응 교정'>[표현 수준]</span> 주어 ‘핵심 원리는’과 호응하지 않는 서술어 ‘~까닭이다’를 ‘~것이다’로 고친다.",
                "think_aloud_prompt": "노란색 3단계 퇴고 단서를 확인하고, 각 오류를 고치는 방법을 조립해 보세요!",
                "cloze_sentences": [
                    "• [내용 수준]: 막연한 설명을 뒷받침하기 위해 구체적인 ( {b1} ) 자료를 추가함",
                    "• [조직 수준]: 문단의 중심 내용에서 벗어난 문장은 글의 ( {b2} )을 해치므로 과감히 삭제함",
                    "• [표현 수준]: 주어 ‘핵심 원리는’과 서술어 ‘~까닭이다’의 ( {b3} ) 오류를 ‘~것이다’로 교정함"
                ],
                "blanks": [
                    {"id": "b1", "correct": "통계 수치(근거)", "options": ["통계 수치(근거)", "주관적 감상", "유행어"]},
                    {"id": "b2", "correct": "통일성", "options": ["통일성", "글자 수", "글씨체"]},
                    {"id": "b3", "correct": "주어-서술어 호응", "options": ["주어-서술어 호응", "높임법", "시간 표현"]}
                ]
            },
            "step3_vaccine": {
                "badge": "[오답 함정 백신 드릴] D1(접속어 역전 수정) & D5(호응 오류 미탐지) 참/거짓 판별하기",
                "desc": "수능 퇴고 문항에서는 ‘원래 올바른 접속어를 틀린 접속어로 고치자’고 속이는 함정(D1)이 자주 나옵니다!",
                "items": [
                    {
                        "statement": "“바닷물은 햇빛의 90%를 흡수한다. 따라서 얼음이 녹아 바닷물이 드러나면 수온이 더 빨리 오른다.”에서 ‘따라서’를 역접 접속어 ‘그러나’로 고쳐야 한다.",
                        "answer": "X",
                        "reason": "함정 포착! [D1 접속어 역전 수정 함정]입니다. 앞 문장(원인)과 뒷문장(결과)은 인과 관계이므로 원래 쓰인 ‘따라서’가 정확히 맞습니다!"
                    },
                    {
                        "statement": "“기후 위기를 막는 핵심 원리는 온실가스 배출량을 줄이는 까닭이다.”에서 ‘줄이는 까닭이다’를 ‘줄이는 것이다’로 고쳐 주어-서술어 호응을 맞춘다.",
                        "answer": "O",
                        "reason": "정확합니다! 주어 ‘원리는’에 호응하도록 서술어를 ‘~것이다’로 고친 모범적인 퇴고입니다."
                    }
                ]
            }
        },

        "real_csat_test": {
            "test_title": "[실전 수능 대비 5지선다] 초6 과학·사회·국어 ‘지구의 열수지 균형과 북극 해빙 감소에 따른 알베도 되먹임’",
            "passage_spec": "6문단 · 865자 · 204어절 · KReaD 1355 · 열수지 모식도 + 퇴고 구간(㉠~㉤) 결합 · 5지선다",
            "passage_title": "지구의 열수지 균형과 북극 해빙 감소에 따른 알베도 되먹임",
            "paragraphs": [
                "지구는 태양으로부터 끊임없이 열에너지를 받지만, 지구의 연평균 기온은 오랫동안 일정한 수준을 유지해 왔다. 이는 지구가 태양으로부터 흡수하는 <span class='cue-span' data-cue='g6-c1'>‘태양 복사 에너지’의 양과 지구가 우주 공간으로 다시 내보내는 ‘지구 복사 에너지’의 양이 서로 같아 ‘열수지(Heat Budget) 균형’</span>을 이루고 있기 때문이다.",
                "지구의 대기권에 있는 수증기, 이산화 탄소, 메탄 같은 온실가스는 태양에서 들어오는 빛은 쉽게 통과시키지만, 지표면에서 우주로 나가는 지구 복사 에너지의 일부를 흡수했다가 지표면으로 다시 되돌려보내는 ‘온실효과’를 일으킨다. 적당한 온실효과는 지구의 평균 기온을 약 15℃로 유지해 생물이 살기에 알맞은 환경을 만들어 준다. 그러나 산업 혁명 이후 화석 연료 사용이 급증하면서 대기 중 온실가스 농도가 지나치게 높아졌고, ㉠<u>우주로 빠져나가야 할 열에너지가 대기 중에 갇히면서 지구의 평균 기온이 상승하는 ‘지구온난화’가 심화되고 있다.</u>",
                "더욱 심각한 문제는 지구온난화가 북극의 바다얼음(해빙)을 녹이면서 온난화 속도를 스스로 더욱 재촉하는 <span class='cue-span' data-cue='g6-c2'>‘양(+)의 되먹임(Positive Feedback)’</span> 현상을 일으킨다는 점이다. 지표면이나 물체가 태양빛을 반사하는 비율을 ‘알베도(Albedo, 반사율)’라고 한다. <span class='cue-span' data-cue='g6-c3'>새하얀 눈과 바다얼음은 알베도가 약 80%에 달해 들어오는 태양빛의 대부분을 우주로 반사한다. 반면에 검푸른 바닷물은 알베도가 약 10%에 불과하여 태양빛의 90%를 그대로 흡수</span>한다.",
                "㉡<u>따라서</u> 지구온난화로 북극의 하얀 바다얼음이 녹아 줄어들면, 그 자리에 알베도가 낮은 검푸른 바닷물이 넓게 드러나게 된다. ㉢<u>북극곰이 얼음 위에서 헤엄치는 모습은 다큐멘터리 영화에서 매우 인상적인 장면을 연출한다.</u> 드러난 바닷물은 이전보다 훨씬 더 많은 태양 복사 에너지를 흡수하게 되고, 이는 다시 북극 바다의 수온을 높여 남아 있는 바다얼음을 더욱 빠르게 녹인다.",
                "결국 ‘기온 상승 ➔ 바다얼음 감소 ➔ 지표면 평균 알베도 하락 ➔ 태양열 흡수량 증가 ➔ 기온 추가 상승’이라는 악순환의 고리가 형성되는 것이다. ㉣<u>이처럼 북극 해빙을 지켜야 하는 핵심 원리는</u> 해빙이 거대한 거울처럼 태양열을 반사하여 지구의 열수지 균형을 지켜 주는 방패 역할을 ㉤<u>수행하기 까닭이다.</u>",
                "따라서 기후 위기의 악순환을 끊어 내기 위해서는 재생 에너지 전환과 산림 복원을 통해 대기 중 온실가스 배출량을 줄이고, 북극 해빙이 더 이상 급격히 사라지지 않도록 국제 사회가 함께 노력해야 한다."
            ],
            "vocab_notes": [
                {"word": "열수지(Heat Budget)", "tier": "Tier 3 (과학 전문어)", "desc": "지구가 흡수하는 태양 복사 에너지와 방출하는 지구 복사 에너지의 수입·지출 균형"},
                {"word": "알베도(Albedo)", "tier": "Tier 3 (과학 전문어)", "desc": "물체 표면이 받은 태양빛 가운데 반사하는 빛의 비율(반사율)"},
                {"word": "양(+)의 되먹임", "tier": "Tier 2/3 (학술 개념어)", "desc": "어떤 현상의 결과가 다시 원인을 강화하여 처음의 변화가 점점 더 커지는 연쇄 작용"}
            ],
            "visual_html": """
              <div style="background:#EFF6FF; border:1px solid #93C5FD; border-radius:10px; padding:12px; margin:12px 0;">
                <div style="font-weight:800; font-size:0.86rem; color:#1E3A8A; margin-bottom:8px;">🔄 [시각 모식도] 북극 해빙 알베도 비교 및 양(+)의 되먹임 인과 루프</div>
                <div style="display:grid; grid-template-columns:1fr 1.3fr; gap:10px; font-size:0.8rem;">
                  <div style="background:#fff; padding:9px; border-radius:8px; border:1px solid #BFDBFE;">
                    <b>☀️ 표면별 알베도(반사율) 비교</b><br>
                    • 🧊 <b>하얀 바다얼음(해빙):</b> 반사 <b>80%</b> / 흡수 20%<br>
                    • 🌊 <b>검푸른 바닷물(해수):</b> 반사 <b>10%</b> / 흡수 <b>90%</b>
                  </div>
                  <div style="background:#FFF1F2; padding:9px; border-radius:8px; border:1px solid #FECDD3; color:#881337;">
                    <b>🔥 양(+)의 되먹임 연쇄 사슬</b><br>
                    기온 상승 ➔ 해빙 면적 감소 ➔ 북극 평균 <b>알베도 하락</b> ➔ 태양 에너지 <b>흡수량 증가</b> ➔ 수온·기온 <b>더욱 상승!</b>
                  </div>
                </div>
              </div>
            """,
            "questions": [
                {
                    "q_no": 1,
                    "archetype": "CSAT-WRIT-W5 (수능 화법과 작문 전형: 내용·조직·표현 3단계 통합 고쳐쓰기 - 5지선다)",
                    "stem": "윗글은 학생이 작성한 과학 설명문 초고이다. ㉠~㉤을 고쳐 쓰기 위한 방안으로 적절하지 <u>않은</u> 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "㉠: 지구온난화의 실태를 객관적 수치로 뒷받침하기 위해 ‘지난 100년간 지구의 평균 기온이 약 1.1℃ 상승했다’는 기상청 통계 자료를 보충한다.",
                            "is_correct": False,
                            "formula": "타당한 퇴고: [내용 수준 - 공신력 있는 통계 수치 보강]",
                            "explanation": "⭕ **적절한 고쳐쓰기 방안이에요!** 객관적 통계 수치를 보충하면 설명의 설득력과 정확성이 높아져요."
                        },
                        {
                            "no": 2,
                            "text": "㉡: 앞 문장(얼음과 바닷물의 반사율 차이)과 뒷문장(얼음 감소 시 바닷물 노출)이 서로 반대되는 역접 관계이므로, ‘따라서’를 ‘그러나’로 고친다.",
                            "is_correct": True,
                            "formula": "정답(부적절) - 오답 공식 [D1 접속어 역전 수정 함정]: 올바른 인과 표지('따라서')를 역접('그러나')으로 잘못 고치라고 유도",
                            "explanation": "🎉 **[처방 성공! D1 접속어 함정 격파]** ㉡의 앞 문장은 원인 원리이고 뒷문장은 그에 따른 결과이므로 인과 접속부사 **'따라서'가 정확히 맞아요.** 이를 '그러나'로 고치면 오히려 글의 논리적 응집성이 깨져요!"
                        },
                        {
                            "no": 3,
                            "text": "㉢: 4문단의 중심 내용인 ‘해빙 감소에 따른 태양열 흡수량 증가와 온난화 가속화’에서 벗어나 문단의 통일성을 해치므로 삭제한다.",
                            "is_correct": False,
                            "formula": "타당한 퇴고: [조직 수준 - 통일성 위배 문장 삭제]",
                            "explanation": "⭕ **적절한 고쳐쓰기 방안이에요!** 북극곰 다큐멘터리 감상 문장(㉢)은 문단 중심 생각과 어긋나므로 삭제해야 통일성이 살아나요."
                        },
                        {
                            "no": 4,
                            "text": "㉣, ㉤: 주어인 ‘핵심 원리는’과 서술어인 ‘수행하기 까닭이다’가 서로 호응하지 않으므로, ㉤을 ‘수행하기 때문이다’ 또는 ‘수행한다는 점이다(것이다)’로 고친다.",
                            "is_correct": False,
                            "formula": "타당한 퇴고: [표현 수준 - `[6국04-05]` 주어-서술어 호응 오류 교정]",
                            "explanation": "⭕ **적절한 고쳐쓰기 방안이에요!** 처방 클리닉에서 훈련한 `[원리는 ➔ ~것이다/점이다]` 호응 규칙이 정확히 적용되었어요."
                        },
                        {
                            "no": 5,
                            "text": "6문단에서 국제 협력의 필요성을 강조하기 위해 ‘기후 위기는 결코 한 국가만의 노력으로는 해결할 수 없다’와 같이 부사어 ‘결코’와 부정 표현이 호응하는 문장을 덧붙인다.",
                            "is_correct": False,
                            "formula": "타당한 퇴고: [표현 수준 - 부정 극성 부사어 '결코'와 부정 서술어 '없다'의 호응]",
                            "explanation": "⭕ **적절한 고쳐쓰기 방안이에요!** 부사어 '결코'는 부정 서술어('~없다')와 정확히 호응해요."
                        }
                    ]
                },
                {
                    "q_no": 2,
                    "archetype": "CSAT-READ-V2-2 (수능 독서 과학 전형: 다단계 연쇄 인과 및 비례 추론형 - 5지선다)",
                    "stem": "윗글을 바탕으로 ‘지구의 열수지’와 ‘북극의 알베도 변화’를 이해한 내용으로 가장 적절한 것은?",
                    "bogi": None,
                    "options": [
                        {
                            "no": 1,
                            "text": "대기 중에 온실가스가 전혀 없어야만 지구의 연평균 기온이 생물이 살기 좋은 15℃로 유지될 수 있다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D3 극단적 부정 왜곡]: 2문단 '적당한 온실효과는 평균 기온을 약 15℃로 유지해 준다'와 반대",
                            "explanation": "❌ **[D3 극단적 왜곡 함정]** 2문단에서 **적당한 온실효과**가 있어야 지구 평균 기온이 약 15℃로 유지된다고 했어요."
                        },
                        {
                            "no": 2,
                            "text": "북극의 바다얼음 면적이 넓어질수록 북극 표면의 평균 알베도는 낮아지고 바닷물의 태양열 흡수량은 증가한다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D2 비례·반비례 방향 역전]: 바다얼음(알베도 80%)이 넓어지면 평균 알베도는 '높아짐'",
                            "explanation": "❌ **[D2 비례 방향 역전 함정]** 반사율이 80%인 바다얼음이 넓어지면 평균 알베도는 **높아지고** 태양열 흡수량은 **줄어들어요**."
                        },
                        {
                            "no": 3,
                            "text": "지구온난화가 심화되어 북극 해빙이 녹을수록 북극 지역이 우주로 반사하는 태양 복사 에너지의 비율은 점차 감소할 것이다.",
                            "is_correct": True,
                            "formula": "정답 공식: [해빙(반사율 80%) 감소 ➔ 바닷물(반사율 10%) 노출 ➔ 태양빛 반사 비율 감소 연쇄 인과 일치]",
                            "explanation": "🎉 **[처방 성공! 연쇄 인과 추론 정답]** 반사율이 80%인 해빙이 녹고 반사율이 10%인 바닷물이 드러나므로, 우주로 반사하는 태양 복사 에너지의 비율(알베도)은 **점차 감소**해요!"
                        },
                        {
                            "no": 4,
                            "text": "지구가 흡수하는 태양 복사 에너지양보다 방출하는 지구 복사 에너지양이 계속 더 많아질 때 지구온난화가 발생한다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D1·D2 인과 조건 역전]: 방출량이 흡수량보다 적어야(열이 갇혀야) 기온이 상승함",
                            "explanation": "❌ **[D1·D2 인과 조건 역전 함정]** 우주로 빠져나가는 방출량이 줄어들어 열이 대기 중에 갇힐 때 지구온난화가 발생해요."
                        },
                        {
                            "no": 5,
                            "text": "바다얼음이 녹더라도 바닷물과 얼음의 알베도는 80%로 서로 같기 때문에 지구가 흡수하는 열에너지 총량에는 변화가 없다.",
                            "is_correct": False,
                            "formula": "오답 공식 [D4 수치 왜곡]: 모식도에 명시된 얼음(80%) vs 바닷물(10%) 알베도 차이를 부정",
                            "explanation": "❌ **[D4 수치 왜곡 함정]** 바다얼음의 알베도는 약 80%, 바닷물의 알베도는 약 10%로 큰 차이가 나요."
                        }
                    ]
                }
            ]
        }
    }
]

with open(os.path.join(DATA_DIR, "unified_courseware_master_data.json"), "w", encoding="utf-8") as f:
    json.dump(UNIFIED_GRADES_DATA, f, ensure_ascii=False, indent=2)

print("Saved courseware/data/unified_courseware_master_data.json successfully!")


# =============================================================================
# 통합 단일 HTML 템플릿 (적응형 3단계 루프 + 1~6학년 전 단원 + 설계 표준 + 96위계 탐색기)
# =============================================================================
UNIFIED_HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>초1~6 설명문 수능형 문해력 코스웨어 마스터 (All-in-One: 진단 ➔ 처방 ➔ 실전 수능 + 설계표준 + 96위계)</title>
  <style>
    :root {
      --navy: #0F172A;
      --blue: #1D4ED8;
      --blue-soft: #EFF6FF;
      --sky: #0284C7;
      --green: #16A34A;
      --green-soft: #DCFCE7;
      --red: #DC2626;
      --red-soft: #FEE2E2;
      --amber: #D97706;
      --amber-soft: #FEF3C7;
      --purple: #6D28D9;
      --purple-soft: #F5F3FF;
      --bg: #F1F5F9;
      --card: #FFFFFF;
      --border: #CBD5E1;
      --text: #0F172A;
      --muted: #475569;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Pretendard', 'Malgun Gothic', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.62;
    }

    /* Global Top Header */
    .top-bar {
      background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 100%);
      color: #fff;
      padding: 16px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      box-shadow: 0 4px 16px rgba(15, 23, 42, 0.22);
    }
    .brand-title {
      font-size: 1.28rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand-pill {
      background: #38BDF8;
      color: #0F172A;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 3px 9px;
      border-radius: 99px;
    }
    .brand-sub {
      font-size: 0.82rem;
      color: #93C5FD;
      margin-top: 3px;
    }
    .main-nav {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .main-tab-btn {
      background: rgba(255,255,255,0.11);
      color: #E2E8F0;
      border: 1px solid rgba(255,255,255,0.24);
      padding: 9px 15px;
      border-radius: 9px;
      font-size: 0.86rem;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.18s;
    }
    .main-tab-btn:hover { background: rgba(255,255,255,0.22); }
    .main-tab-btn.active {
      background: #FACC15;
      color: #0F172A;
      border-color: #FACC15;
      box-shadow: 0 2px 10px rgba(250, 204, 21, 0.4);
    }

    /* Grade / Persona Selector Bar (in Tab 1) */
    .grade-selector-strip {
      background: #1E293B;
      padding: 10px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
      border-bottom: 1px solid #334155;
    }
    .grade-btn-group {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .grade-pill-btn {
      background: rgba(255,255,255,0.08);
      color: #CBD5E1;
      border: 1px solid rgba(255,255,255,0.18);
      padding: 7px 13px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.18s;
    }
    .grade-pill-btn:hover { background: rgba(255,255,255,0.18); color: #fff; }
    .grade-pill-btn.active {
      background: #38BDF8;
      color: #0F172A;
      border-color: #38BDF8;
      font-weight: 800;
    }

    /* Core 3-Stage Stepper Banner */
    .loop-stepper {
      background: #FFFFFF;
      border-bottom: 2px solid var(--border);
      padding: 12px 28px;
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      position: sticky;
      top: 0;
      z-index: 50;
      box-shadow: 0 2px 8px rgba(15,23,42,0.05);
    }
    .stage-step {
      display: flex;
      align-items: center;
      gap: 11px;
      padding: 9px 18px;
      border-radius: 12px;
      border: 2px solid #E2E8F0;
      background: #F8FAFC;
      cursor: pointer;
      transition: all 0.2s;
      min-width: 255px;
    }
    .stage-step:hover { border-color: #93C5FD; }
    .stage-step.active {
      border-color: var(--blue);
      background: var(--blue-soft);
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.12);
    }
    .stage-step.done {
      border-color: var(--green);
      background: var(--green-soft);
    }
    .stage-num {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #CBD5E1;
      color: #1E293B;
      font-weight: 800;
      font-size: 0.92rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .stage-step.active .stage-num { background: var(--blue); color: #fff; }
    .stage-step.done .stage-num { background: var(--green); color: #fff; }
    .stage-info-title { font-size: 0.92rem; font-weight: 800; color: #0F172A; }
    .stage-info-sub { font-size: 0.75rem; color: var(--muted); }
    .stage-arrow { font-size: 1.25rem; color: #94A3B8; font-weight: 800; }

    /* Main Content Wrapper */
    .main-view { display: none; }
    .main-view.active { display: block; }
    .main-wrap {
      max-width: 1540px;
      margin: 0 auto;
      padding: 20px 28px 60px;
    }
    .stage-panel { display: none; }
    .stage-panel.active { display: block; }

    /* Student & Spec Header Card */
    .student-strip {
      background: #fff;
      border: 1px solid var(--border);
      border-left: 6px solid var(--blue);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 16px;
    }
    .st-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .st-left { display: flex; align-items: center; gap: 14px; }
    .avatar-circle {
      width: 46px; height: 46px; border-radius: 50%;
      background: #DBEAFE; color: #1E40AF;
      font-weight: 800; font-size: 1.05rem;
      display: flex; align-items: center; justify-content: center;
      flex-shrink: 0;
    }
    .st-name { font-size: 1.06rem; font-weight: 800; }
    .st-desc { font-size: 0.84rem; color: #B91C1C; font-weight: 700; margin-top: 2px; }
    .kread-box {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      padding: 7px 13px;
      border-radius: 8px;
      text-align: right;
      font-size: 0.81rem;
    }
    .spec-Drawer {
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px dashed #CBD5E1;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 8px;
      font-size: 0.8rem;
    }
    .spec-item {
      background: #F8FAFC;
      padding: 7px 10px;
      border-radius: 7px;
      border: 1px solid #E2E8F0;
    }
    .spec-item b { color: #1E40AF; display: block; font-size: 0.74rem; }

    /* Layout Grids & Cards */
    .grid-2 {
      display: grid;
      grid-template-columns: 1.05fr 1fr;
      gap: 20px;
      align-items: start;
    }
    @media (max-width: 1120px) {
      .grid-2 { grid-template-columns: 1fr; }
    }
    .card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 20px;
      box-shadow: 0 2px 6px rgba(15,23,42,0.04);
      margin-bottom: 18px;
    }
    .card-title {
      font-size: 1.04rem;
      font-weight: 800;
      color: var(--navy);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      border-bottom: 2px solid #F1F5F9;
      padding-bottom: 9px;
    }
    .badge {
      display: inline-block;
      padding: 3px 9px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 800;
    }
    .badge-blue { background: #DBEAFE; color: #1E40AF; }
    .badge-red { background: #FEE2E2; color: #991B1B; }
    .badge-green { background: #DCFCE7; color: #166534; }
    .badge-amber { background: #FEF3C7; color: #92400E; }
    .badge-purple { background: #EDE9FE; color: #5B21B6; }

    /* Passage Box & Cue Spans */
    .passage-box {
      background: #FCFBF7;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 16px 18px;
      font-size: 0.96rem;
      line-height: 1.82;
      margin-bottom: 14px;
    }
    .passage-box p {
      margin-bottom: 10px;
      text-indent: 0.6em;
    }
    .cue-span {
      border-radius: 4px;
      padding: 1px 3px;
      transition: all 0.2s;
    }
    .cue-span.active {
      background: #FEF08A;
      border-bottom: 2px solid #CA8A04;
      font-weight: 700;
    }
    .vocab-bar {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
      padding-top: 10px;
      border-top: 1px dashed #CBD5E1;
    }
    .vocab-chip {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-radius: 7px;
      padding: 5px 10px;
      font-size: 0.79rem;
    }
    .vocab-chip b { color: #1E40AF; }

    /* Diagnostic Question Items */
    .diag-q-card {
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 13px;
      margin-bottom: 12px;
      background: #F8FAFC;
    }
    .diag-opt {
      padding: 8px 11px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #fff;
      margin-top: 6px;
      font-size: 0.87rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 8px;
    }
    .diag-opt.wrong-picked {
      background: #FEF2F2;
      border: 2px solid #DC2626;
      color: #991B1B;
      font-weight: 700;
    }
    .diag-opt.correct-ans {
      background: #F0FDF4;
      border: 2px solid #16A34A;
      color: #166534;
      font-weight: 700;
    }

    /* Domain Score Bars & Bottleneck */
    .score-row { margin-bottom: 11px; }
    .score-head {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 4px;
    }
    .bar-bg {
      height: 10px;
      background: #E2E8F0;
      border-radius: 99px;
      overflow: hidden;
    }
    .bar-fill { height: 100%; border-radius: 99px; }
    .bar-fill.good { background: #16A34A; }
    .bar-fill.warn { background: #D97706; }
    .bar-fill.danger { background: #DC2626; }
    .score-comment { font-size: 0.77rem; color: var(--muted); margin-top: 2px; }

    .dc-meter {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin: 10px 0;
    }
    .dc-box {
      padding: 11px;
      border-radius: 10px;
      border: 1px solid #CBD5E1;
      text-align: center;
      background: #F8FAFC;
    }
    .dc-box.bottleneck {
      background: #FEF2F2;
      border: 2px solid #DC2626;
    }
    .dc-val { font-size: 1.25rem; font-weight: 800; margin-top: 3px; }

    /* Trap Vulnerability Grid */
    .trap-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }
    .trap-item {
      padding: 8px 10px;
      border-radius: 8px;
      border: 1px solid #E2E8F0;
      background: #F8FAFC;
      font-size: 0.81rem;
    }
    .trap-item.high-risk {
      background: #FFF1F2;
      border-color: #FDA4AF;
    }

    /* Backtracking Timeline */
    .bt-chain {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .bt-node {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 9px 13px;
      border-radius: 9px;
      border: 1px solid #CBD5E1;
      background: #F8FAFC;
      font-size: 0.85rem;
    }
    .bt-node.review {
      background: #FFFBEB;
      border: 2px solid #F59E0B;
    }
    .bt-node.target {
      background: #EFF6FF;
      border: 2px solid #2563EB;
    }

    /* Stage 2 Prescription Styles */
    .rx-banner {
      background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
      color: #fff;
      padding: 16px 20px;
      border-radius: 12px;
      margin-bottom: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
    }
    .rx-cue {
      background: #FEF08A;
      border-bottom: 2px dashed #CA8A04;
      padding: 1px 5px;
      border-radius: 4px;
      font-weight: 800;
      cursor: pointer;
    }
    .rx-cue.active {
      background: #FDE047;
      outline: 2px solid #EA580C;
    }
    .cloze-select {
      padding: 5px 10px;
      border: 2px solid #2563EB;
      border-radius: 6px;
      font-weight: 800;
      color: #1E40AF;
      background: #EFF6FF;
      cursor: pointer;
    }
    .vaccine-card {
      border: 1px solid #CBD5E1;
      border-radius: 10px;
      padding: 12px;
      margin-bottom: 10px;
      background: #F8FAFC;
    }
    .ox-btn {
      padding: 6px 15px;
      border-radius: 6px;
      border: 1px solid #94A3B8;
      background: #fff;
      font-weight: 800;
      cursor: pointer;
      margin-right: 6px;
    }
    .ox-btn.done-ok { background: #16A34A; color: #fff; border-color: #16A34A; }
    .ox-btn.done-no { background: #DC2626; color: #fff; border-color: #DC2626; }

    /* Stage 3 Real CSAT Styles */
    .csat-q-box {
      border: 1px solid #CBD5E1;
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 16px;
      background: #fff;
    }
    .bogi-box {
      background: #F8FAFC;
      border: 1px solid #94A3B8;
      border-radius: 8px;
      padding: 11px 14px;
      margin: 10px 0;
      font-size: 0.87rem;
      white-space: pre-line;
    }
    .csat-opt-btn {
      width: 100%;
      text-align: left;
      padding: 10px 13px;
      margin-top: 7px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #fff;
      font-size: 0.89rem;
      cursor: pointer;
      transition: all 0.15s;
      display: flex;
      gap: 9px;
      align-items: flex-start;
    }
    .csat-opt-btn:hover { background: #F1F5F9; border-color: #64748B; }
    .csat-opt-btn.correct {
      background: #DCFCE7;
      border: 2px solid #16A34A;
      color: #14532D;
      font-weight: 700;
    }
    .csat-opt-btn.wrong {
      background: #FEE2E2;
      border: 2px solid #DC2626;
      color: #7F1D1D;
    }
    .opt-feedback {
      display: none;
      margin-top: 6px;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 0.83rem;
      background: #F8FAFC;
      border-left: 4px solid #2563EB;
    }
    .cta-btn {
      background: var(--blue);
      color: #fff;
      border: none;
      padding: 11px 20px;
      border-radius: 10px;
      font-weight: 800;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 12px rgba(29, 78, 216, 0.22);
    }
    .cta-btn:hover { background: #1E40AF; }
    .growth-banner {
      background: linear-gradient(135deg, #065F46 0%, #059669 100%);
      color: #fff;
      padding: 16px 20px;
      border-radius: 12px;
      margin-top: 14px;
      display: none;
    }
    .growth-banner.show { display: block; }

    /* Standards & Explorer Tables (Tabs 2 & 3) */
    .std-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      background: #fff;
    }
    .std-table th, .std-table td {
      border: 1px solid #CBD5E1;
      padding: 9px 11px;
      text-align: left;
      vertical-align: top;
    }
    .std-table th {
      background: #1E293B;
      color: #fff;
      font-weight: 700;
    }
    .std-table tr:nth-child(even) { background: #F8FAFC; }
    .filter-bar {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 14px;
      background: #fff;
      padding: 14px;
      border-radius: 10px;
      border: 1px solid var(--border);
    }
    .filter-bar select, .filter-bar input {
      padding: 8px 12px;
      border: 1px solid #CBD5E1;
      border-radius: 6px;
      font-size: 0.88rem;
    }
  </style>
</head>
<body>

  <!-- 1. Global Header & 3 Top-Level Views -->
  <header class="top-bar">
    <div>
      <div class="brand-title">
        <span>🧠 AI 초등 설명문(Expository) 수능형 문해력 코스웨어 마스터</span>
        <span class="brand-pill">All-in-One 통합본</span>
      </div>
      <div class="brand-sub">
        2022 개정 교과 개념 × 학년별 KReaD·어휘 복잡도 × [① 현재 상태 진단 ➔ ② 1:1 맞춤형 처방 ➔ ③ 실전 수능 대비 문제]
      </div>
    </div>
    <nav class="main-nav">
      <button class="main-tab-btn active" id="mtab-btn-1" onclick="switchMainView(1)">
        🎯 적응형 코스웨어 체험 (진단 ➔ 처방 ➔ 실전 수능)
      </button>
      <button class="main-tab-btn" id="mtab-btn-2" onclick="switchMainView(2)">
        📐 학년별 지문 복잡도 & 수능 문항 설계 표준 (Track 1·2·3)
      </button>
      <button class="main-tab-btn" id="mtab-btn-3" onclick="switchMainView(3)">
        🗂️ 설명문 96개 + 공통기초 36개 마스터 위계 탐색기
      </button>
    </nav>
  </header>

  <!-- ====================================================================== -->
  <!-- VIEW 1: 적응형 코스웨어 루프 (초1~초6 전 학년 페르소나 & 프로토타입 통합) -->
  <!-- ====================================================================== -->
  <div id="main-view-1" class="main-view active">
    <!-- Grade 1~6 Persona Selector -->
    <div class="grade-selector-strip">
      <div style="color:#93C5FD; font-size:0.83rem; font-weight:800;">
        👦👧 학년별 학습자 페르소나 & 대표 단원 선택 (1~6학년 전 학년 완비):
      </div>
      <div class="grade-btn-group" id="persona-btn-group"></div>
    </div>

    <!-- 3-Stage Stepper -->
    <nav class="loop-stepper">
      <div class="stage-step active" id="step-nav-1" onclick="goStage(1)">
        <div class="stage-num">1</div>
        <div>
          <div class="stage-info-title">① 현재 상태 정밀 진단</div>
          <div class="stage-info-sub">미니 진단 · Dick & Carey 병목 · 오답 함정(D1~D6) · 종적 역추적</div>
        </div>
      </div>
      <div class="stage-arrow">➔</div>
      <div class="stage-step" id="step-nav-2" onclick="goStage(2)">
        <div class="stage-num">2</div>
        <div>
          <div class="stage-info-title">② 1:1 맞춤형 처방 클리닉</div>
          <div class="stage-info-sub">하위 학년 징검다리 복습 · 단서·사고구술 조립 · 오답 함정 백신</div>
        </div>
      </div>
      <div class="stage-arrow">➔</div>
      <div class="stage-step" id="step-nav-3" onclick="goStage(3)">
        <div class="stage-num">3</div>
        <div>
          <div class="stage-info-title">③ 실전 수능 대비 문제</div>
          <div class="stage-info-sub">교과 개념 맞춤 지문 · 어휘 사전 · 수능 실전 문항 · 성취도 리포트</div>
        </div>
      </div>
    </nav>

    <!-- Main Dynamic Workspace -->
    <main class="main-wrap" id="app-workspace"></main>
  </div>

  <!-- ====================================================================== -->
  <!-- VIEW 2: 학년별 지문 복잡도 & 수능 문항 스케일링 설계 표준 대시보드 -->
  <!-- ====================================================================== -->
  <div id="main-view-2" class="main-view">
    <main class="main-wrap">
      <div class="card">
        <div class="card-title">
          <span>📏 [Track 2 표준] 초등 1~6학년 설명문 지문 정량·정성 복잡도 규격표</span>
          <span class="badge badge-blue">KReaD · 김광해 어휘 등급 · 2022 개정 교육과정 반영</span>
        </div>
        <table class="std-table">
          <thead>
            <tr>
              <th>학년 (학년군)</th>
              <th>KReaD 지수</th>
              <th>문단 수 / 문장 수</th>
              <th>글자 수 (공백 포함)</th>
              <th>어절 수 (문장당 평균)</th>
              <th>어휘 등급 배합 (Tier 1 : Tier 2 : Tier 3)</th>
              <th>시각 매체 자료 복잡도</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>1학년</b> (초저)</td>
              <td>800 ~ 890</td>
              <td>1문단 (3~5문장)</td>
              <td>100 ~ 180자</td>
              <td>25~45어절 (5~7어절)</td>
              <td><b>90% : 7% : 3%</b> (김광해 1등급 일상어 중심)</td>
              <td>직관적 삽화 · 부위별 명칭 선 잇기 그림</td>
            </tr>
            <tr>
              <td><b>2학년</b> (초저)</td>
              <td>900 ~ 990</td>
              <td>2문단 (5~7문장)</td>
              <td>200 ~ 300자</td>
              <td>50~75어절 (7~8어절)</td>
              <td><b>85% : 10% : 5%</b> (순서·이유 담화표지 도입)</td>
              <td>3~4단계 과정 화살표 그림 · 1차원 간단한 표</td>
            </tr>
            <tr>
              <td><b>3학년</b> (초중)</td>
              <td>1000 ~ 1090</td>
              <td>3문단 (8~11문장)</td>
              <td>320 ~ 450자</td>
              <td>80~110어절 (8~10어절)</td>
              <td><b>78% : 15% : 7%</b> (김광해 2등급 · 다의어·개념어)</td>
              <td>2차원 비교표(행×열) · 기초 구조도</td>
            </tr>
            <tr>
              <td><b>4학년</b> (초중)</td>
              <td>1100 ~ 1190</td>
              <td>3~4문단 (11~15문장)</td>
              <td>450 ~ 600자</td>
              <td>110~150어절 (9~11어절)</td>
              <td><b>72% : 18% : 10%</b> (비례·증감 사고 도구어)</td>
              <td>막대그래프 · 꺾은선그래프 (시계열 추세)</td>
            </tr>
            <tr>
              <td><b>5학년</b> (초고)</td>
              <td>1200 ~ 1290</td>
              <td>4~5문단 (14~18문장)</td>
              <td>600 ~ 750자</td>
              <td>150~190어절 (10~12어절)</td>
              <td><b>65% : 22% : 13%</b> (김광해 3등급 · 한자 개념어)</td>
              <td>원그래프·띠그래프(비율) · 다중 비교표</td>
            </tr>
            <tr>
              <td><b>6학년</b> (초고)</td>
              <td>1300 ~ 1390</td>
              <td>5~6문단 (17~22문장)</td>
              <td>750 ~ 950자</td>
              <td>190~240어절 (11~13어절)</td>
              <td><b>60% : 25% : 15%</b> (중등 브릿지 전문 개념어)</td>
              <td>복합 통계 그래프 · 연쇄 인과(되먹임) 모식도</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card">
        <div class="card-title">
          <span>🎯 [Track 3 표준] 한국교육과정평가원(KICE) 수능형 문항 학년군별 스케일링 & 매력적 오답 6대 공식</span>
          <span class="badge badge-purple">독서(비문학) V1~V3 + 화법과 작문 W1~W5</span>
        </div>
        <table class="std-table" style="margin-bottom:16px;">
          <thead>
            <tr>
              <th>스케일링 요소</th>
              <th>초저 (1~2학년군: 수능 입문기)</th>
              <th>초중 (3~4학년군: 수능 기본기)</th>
              <th>초고 (5~6학년군: 수능 실전기)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>선지 구성 수</b></td>
              <td><b>3지선다</b> (정답 1 + 매력적 오답 2)</td>
              <td><b>4지선다</b> (정답 1 + 매력적 오답 3)</td>
              <td><b>5지선다</b> (평가원 수능 동일 규격)</td>
            </tr>
            <tr>
              <td><b>발문(Stem) 스타일</b></td>
              <td>친화형 의문문 (“윗글의 내용과 <u>같은/다른</u> 것은 무엇인가요?”)</td>
              <td>수능 기본형 (“윗글을 읽고 알 수 있는 내용으로 가장 <u>알맞은</u> 것은?”)</td>
              <td>수능 실전형 (“윗글에 대한 이해로 적절하지 <u>않은</u> 것은?”, “&lt;보기&gt;를 바탕으로 추론한 것은?”)</td>
            </tr>
            <tr>
              <td><b>&lt;보기&gt; 박스 설계</b></td>
              <td>일상 경험·동물 관찰 짧은 상황 (2문장)</td>
              <td>교과서 탐구 실험 조건·단일 표/그래프</td>
              <td>복합 실험·편향된 매체 글·학생 작문 초고 (㉠~㉤ 퇴고)</td>
            </tr>
          </tbody>
        </table>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:10px;">
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D1] 인과 역전 (Causal Reversal)</b><br>
            본문의 `[원인 A ➔ 결과 B]`를 선지에서 `[B 때문에 A가 발생한다]`로 뒤집거나 올바른 접속어를 역접으로 바꾸는 함정
          </div>
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D2] 선후·증감 왜곡 (Sequential/Directional)</b><br>
            과정 순서(`뒷다리➔앞다리`)를 뒤바꾸거나 비례·반비례 방향(`기온↑ ➔ 증산↑`)을 반대로 진술하는 함정
          </div>
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D3] 조건·한정어 과장 (Overgeneralization)</b><br>
            `일부, 1% 미만`을 `모두, 언제나, 절반 이상` 등 극단적 양화사로 과장·단정하는 함정
          </div>
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D4] 속성·분류·다의어 교차 (Attribute Swap)</b><br>
            비교 대상(`균계↔세균계`, `세기↔높낮이`, `분류↔분석`)의 속성을 서로 크로스하여 바꿔치기하는 함정
          </div>
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D5] 주객·호응·준거 전도 (Syntactic Inversion)</b><br>
            행위 주체와 대상을 바꾸거나, 주어-서술어 호응(`원리는 ~ 때문이다`) 및 평가 준거를 어기는 함정
          </div>
          <div style="background:#FEF2F2; border:1px solid #FECACA; padding:11px; border-radius:8px; font-size:0.83rem;">
            <b style="color:#991B1B;">[D6] 본문 외 상식 짜깁기 (Extratextual)</b><br>
            지문 어휘만 빌려오고 본문에 언급되지 않은 외부 배경지식이나 상상을 결합하는 함정
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- ====================================================================== -->
  <!-- VIEW 3: 설명문 96개 + 공통기초 36개 마스터 위계 탐색기 -->
  <!-- ====================================================================== -->
  <div id="main-view-3" class="main-view">
    <main class="main-wrap">
      <div class="card">
        <div class="card-title">
          <span>🗂️ `8_설명문_1_6학년` (96개) & `4_공통기초_1_6학년` (36개) 마스터 위계 탐색기</span>
          <span class="badge badge-green">학년 클릭 시 해당 학년 코스웨어로 바로 이동 가능</span>
        </div>
        <div class="filter-bar">
          <select id="f-sheet" onchange="renderHierarchyTable()">
            <option value="expository">8_설명문_1_6학년 (96개 목표)</option>
            <option value="common">4_공통기초_1_6학년 (36개 목표)</option>
          </select>
          <select id="f-grade" onchange="renderHierarchyTable()">
            <option value="ALL">전체 학년 (1~6학년)</option>
            <option value="1학년">1학년</option>
            <option value="2학년">2학년</option>
            <option value="3학년">3학년</option>
            <option value="4학년">4학년</option>
            <option value="5학년">5학년</option>
            <option value="6학년">6학년</option>
          </select>
          <select id="f-domain" onchange="renderHierarchyTable()">
            <option value="ALL">전체 영역 (V1·V2·V3·W)</option>
            <option value="사실적">1. 사실적 이해 (V1)</option>
            <option value="추론적">2. 추론적 이해 (V2)</option>
            <option value="비판적">3. 비판적 이해 (V3)</option>
            <option value="표현">4. 표현하기/쓰기 (W)</option>
          </select>
          <input type="text" id="f-keyword" placeholder="하위기능명, Dick&Carey, Mager 목표 검색..." oninput="renderHierarchyTable()" style="flex:1; min-width:220px;" />
        </div>
        <div id="hierarchy-table-wrap"></div>
      </div>
    </main>
  </div>

  <script>
    const GRADES_DATA = __GRADES_JSON__;
    const HIERARCHY_DATA = __HIERARCHY_JSON__;

    let currentIdx = 4; // 기본 선택: 초5 김민준 (index 4) 또는 상단 버튼으로 1~6학년 모두 전환 가능
    let currentStage = 1; // 1: 진단, 2: 처방, 3: 실전 수능
    let showSpecDrawer = false;
    let showCueHighlight = false;

    function switchMainView(viewNo) {
      [1, 2, 3].forEach(n => {
        document.getElementById(`mtab-btn-${n}`).classList.toggle('active', n === viewNo);
        document.getElementById(`main-view-${n}`).classList.toggle('active', n === viewNo);
      });
    }

    function renderPersonaBar() {
      const bar = document.getElementById('persona-btn-group');
      bar.innerHTML = GRADES_DATA.map((g, idx) => `
        <button class="grade-pill-btn ${idx === currentIdx ? 'active' : ''}" onclick="selectGradePersona(${idx})">
          ${g.persona_label} (${g.slot_id})
        </button>
      `).join('');
    }

    function selectGradePersona(idx) {
      currentIdx = idx;
      currentStage = 1;
      showCueHighlight = false;
      renderPersonaBar();
      updateStageStepper();
      renderWorkspace();
    }

    function jumpToGradeFromExplorer(gradeStr) {
      const gNum = parseInt(gradeStr);
      const targetIdx = GRADES_DATA.findIndex(g => g.grade_num === gNum);
      if (targetIdx !== -1) {
        switchMainView(1);
        selectGradePersona(targetIdx);
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    }

    function goStage(stageNo) {
      currentStage = stageNo;
      updateStageStepper();
      renderWorkspace();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function updateStageStepper() {
      for (let i = 1; i <= 3; i++) {
        const el = document.getElementById(`step-nav-${i}`);
        el.classList.remove('active', 'done');
        if (i === currentStage) el.classList.add('active');
        else if (i < currentStage) el.classList.add('done');
      }
    }

    function toggleSpecDrawer() {
      showSpecDrawer = !showSpecDrawer;
      const el = document.getElementById('spec-drawer-box');
      if (el) el.style.display = showSpecDrawer ? 'grid' : 'none';
    }

    function togglePassageCues() {
      showCueHighlight = !showCueHighlight;
      document.querySelectorAll('.cue-span').forEach(el => {
        el.classList.toggle('active', showCueHighlight);
      });
      const btn = document.getElementById('cue-toggle-btn');
      if (btn) {
        btn.innerHTML = showCueHighlight ? '💡 본문 핵심 단서 하이라이팅 (ON)' : '🔍 본문 핵심 단서 하이라이팅 켜기';
      }
    }

    function renderWorkspace() {
      const p = GRADES_DATA[currentIdx];
      const ws = document.getElementById('app-workspace');

      const studentHeader = `
        <div class="student-strip">
          <div class="st-top-row">
            <div class="st-left">
              <div class="avatar-circle">${p.grade}</div>
              <div>
                <div class="st-name">
                  ${p.persona_label}
                  <span class="badge badge-blue" style="margin-left:6px;">목표 위계: ${p.slot_id} (${p.layer})</span>
                  <span class="badge badge-purple" style="margin-left:4px;">${p.curriculum_concept.subject}</span>
                </div>
                <div class="st-desc">⚠️ 핵심 진단 요약: ${p.student_summary}</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
              <button class="ox-btn" style="font-size:0.78rem; padding:6px 11px; border-color:#2563EB; color:#1E40AF;" onclick="toggleSpecDrawer()">
                📐 학년 지문·문항 설계 규격 상세 보기 ▾
              </button>
              <div class="kread-box">
                <div>현재 이독성: <b style="color:#DC2626;">KReaD ${p.complexity_metrics.current_kread}</b></div>
                <div>학년 목표치: <b style="color:#1D4ED8;">KReaD ${p.complexity_metrics.kread_target}</b></div>
              </div>
            </div>
          </div>
          <div class="spec-Drawer" id="spec-drawer-box" style="display:${showSpecDrawer ? 'grid' : 'none'};">
            <div class="spec-item">
              <b>교과 단원 및 핵심 개념</b>
              ${p.curriculum_concept.unit} — ${p.curriculum_concept.concept}
            </div>
            <div class="spec-item">
              <b>텍스트 구조 (Meyer 6대 구조)</b>
              ${p.curriculum_concept.text_structure}
            </div>
            <div class="spec-item">
              <b>지문 정량 규격 (문단·글자·어절)</b>
              ${p.complexity_metrics.para_count} · ${p.complexity_metrics.char_count} · ${p.complexity_metrics.eojeol_count}
            </div>
            <div class="spec-item">
              <b>어휘 등급 배합 (Tier 1·2·3)</b>
              ${p.complexity_metrics.vocab_profile}
            </div>
            <div class="spec-item">
              <b>수능 문항 스케일링 규격</b>
              ${p.complexity_metrics.csat_scaling}
            </div>
            <div class="spec-item">
              <b>Mager 수행 목표</b>
              ${p.mager_goal}
            </div>
          </div>
        </div>
      `;

      // =====================================================================
      // STAGE 1: 현재 상태 정밀 진단
      // =====================================================================
      if (currentStage === 1) {
        const dt = p.diagnostic_test;
        const dr = p.diagnosis_report;

        ws.innerHTML = `
          ${studentHeader}
          <section class="stage-panel active">
            <div class="grid-2">
              <!-- Left Column: Diagnostic Mini Test & Student Answer Analysis -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>📝 [1단계] 학년 수준 미니 진단 지문 & 학생 오답 패턴 채점</span>
                    <span class="badge badge-blue">${dt.passage_spec}</span>
                  </div>
                  <div style="font-weight:800; color:#1E40AF; margin-bottom:6px; font-size:0.95rem;">
                    ${dt.passage_title}
                  </div>
                  <div class="passage-box">
                    ${dt.paragraphs.map(para => `<p>${para}</p>`).join('')}
                  </div>

                  <div style="font-weight:800; font-size:0.9rem; margin:12px 0 8px; color:#334155;">
                    🔍 학생 제출 답안 및 매력적 오답 함정(D1~D6) 자동 판별 결과
                  </div>
                  ${dt.questions.map(q => `
                    <div class="diag-q-card">
                      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                        <span class="badge badge-purple">진단 목표: ${q.target_code} (${q.target_skill})</span>
                        <span class="badge ${q.options.find(o => o.no === q.student_selected).is_correct ? 'badge-green' : 'badge-red'}">
                          ${q.options.find(o => o.no === q.student_selected).is_correct ? '⭕ 정답 도달' : '❌ 오답 함정 감지'}
                        </span>
                      </div>
                      <div style="font-weight:800; font-size:0.9rem; margin-bottom:6px;">
                        Q${q.q_no}. ${q.stem}
                      </div>
                      ${q.options.map(opt => {
                        let cls = '';
                        let tag = '';
                        if (opt.no === q.student_selected && !opt.is_correct) {
                          cls = 'wrong-picked';
                          tag = `<span class="badge badge-red">학생 선택 오답 · ${opt.trap}</span>`;
                        } else if (opt.is_correct) {
                          cls = 'correct-ans';
                          tag = `<span class="badge badge-green">${opt.no === q.student_selected ? '학생 선택 정답' : '실제 정답'}</span>`;
                        } else {
                          tag = `<span style="font-size:0.74rem; color:#64748B;">${opt.trap}</span>`;
                        }
                        return `
                          <div class="diag-opt ${cls}">
                            <span><b>${opt.no}번.</b> ${opt.text}</span>
                            ${tag}
                          </div>
                        `;
                      }).join('')}
                    </div>
                  `).join('')}
                </div>
              </div>

              <!-- Right Column: 3D Literacy Profile & Longitudinal Backtracking -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>📊 [2단계] 4대 문해력 영역 성취도 & Dick & Carey 병목 진단</span>
                    <span class="badge badge-red">정밀 프로파일링</span>
                  </div>
                  ${dr.domain_scores.map(ds => `
                    <div class="score-row">
                      <div class="score-head">
                        <span>${ds.domain}</span>
                        <span style="color:${ds.status === 'danger' ? '#DC2626' : (ds.status === 'warn' ? '#D97706' : '#16A34A')};">
                          ${ds.score}점 (${ds.status === 'danger' ? '집중 처방 대상' : (ds.status === 'warn' ? '보강 권장' : '안정')})
                        </span>
                      </div>
                      <div class="bar-bg">
                        <div class="bar-fill ${ds.status}" style="width:${ds.score}%;"></div>
                      </div>
                      <div class="score-comment">• ${ds.comment}</div>
                    </div>
                  `).join('')}

                  <div style="margin-top:16px; padding-top:12px; border-top:1px dashed #CBD5E1;">
                    <div style="font-weight:800; font-size:0.89rem; color:#991B1B; margin-bottom:6px;">
                      🚨 ${dr.bottleneck.diagnosis_title}
                    </div>
                    <div class="dc-meter">
                      <div class="dc-box ${dr.bottleneck.step1_rate < 60 ? 'bottleneck' : ''}">
                        <div style="font-size:0.76rem; font-weight:700;">Step 1. 단서 포착</div>
                        <div class="dc-val">${dr.bottleneck.step1_rate}%</div>
                      </div>
                      <div class="dc-box ${dr.bottleneck.step2_rate < 60 ? 'bottleneck' : ''}">
                        <div style="font-size:0.76rem; font-weight:700;">Step 2. 관계·맥락 연결</div>
                        <div class="dc-val" style="color:${dr.bottleneck.step2_rate < 60 ? '#DC2626' : '#0F172A'};">${dr.bottleneck.step2_rate}%</div>
                      </div>
                      <div class="dc-box ${dr.bottleneck.step3_rate < 60 ? 'bottleneck' : ''}">
                        <div style="font-size:0.76rem; font-weight:700;">Step 3. 구조화·판단</div>
                        <div class="dc-val" style="color:${dr.bottleneck.step3_rate < 60 ? '#DC2626' : '#0F172A'};">${dr.bottleneck.step3_rate}%</div>
                      </div>
                    </div>
                    <div style="font-size:0.83rem; background:#FEF2F2; border-left:4px solid #DC2626; padding:9px 12px; border-radius:6px; color:#7F1D1D;">
                      ${dr.bottleneck.diagnosis_detail}
                    </div>
                  </div>
                </div>

                <!-- Trap Vulnerability & Backtracking -->
                <div class="card">
                  <div class="card-title">
                    <span>🧭 [3단계] 수능 6대 오답 함정 취약도 & 종적 위계 역추적(Backtracking)</span>
                    <span class="badge badge-amber">처방 경로 자동 생성</span>
                  </div>
                  <div style="font-size:0.82rem; font-weight:700; color:#475569; margin-bottom:8px;">
                    • KICE 수능 6대 매력적 오답 공식(D1~D6) 취약 지수 (높을수록 함정에 자주 빠짐)
                  </div>
                  <div class="trap-grid" style="margin-bottom:14px;">
                    ${dr.trap_radar.map(t => `
                      <div class="trap-item ${t.vuln >= 75 ? 'high-risk' : ''}">
                        <div style="display:flex; justify-content:space-between; font-weight:800;">
                          <span>[${t.code}] ${t.name}</span>
                          <span style="color:${t.vuln >= 75 ? '#DC2626' : '#475569'};">취약도 ${t.vuln}%</span>
                        </div>
                        <div class="bar-bg" style="height:6px; margin-top:4px;">
                          <div class="bar-fill ${t.vuln >= 75 ? 'danger' : (t.vuln >= 50 ? 'warn' : 'good')}" style="width:${t.vuln}%;"></div>
                        </div>
                      </div>
                    `).join('')}
                  </div>

                  <div style="font-size:0.82rem; font-weight:700; color:#475569; margin-bottom:8px;">
                    • 96개 설명문 & 36개 공통기초 마스터 위계 기반 <b>종적 역추적 처방 경로</b>
                  </div>
                  <div class="bt-chain">
                    ${dr.backtracking_path.map(node => `
                      <div class="bt-node ${node.status}">
                        <span class="badge ${node.status === 'review' ? 'badge-amber' : (node.status === 'target' ? 'badge-blue' : 'badge-green')}">
                          ${node.grade}
                        </span>
                        <div>
                          <div style="font-weight:800;">${node.code}</div>
                          <div style="font-size:0.81rem; color:#334155;">${node.title}</div>
                        </div>
                      </div>
                    `).join('')}
                  </div>

                  <div style="margin-top:16px; text-align:right;">
                    <button class="cta-btn" onclick="goStage(2)">
                      💊 진단 결과 기반 1:1 맞춤형 처방 클리닉 시작하기 ➔
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>
        `;
        return;
      }

      // =====================================================================
      // STAGE 2: 1:1 맞춤형 처방 클리닉
      // =====================================================================
      if (currentStage === 2) {
        const rx = p.prescription_clinic;
        ws.innerHTML = `
          ${studentHeader}
          <section class="stage-panel active">
            <div class="rx-banner">
              <div>
                <div style="font-size:0.78rem; color:#93C5FD; font-weight:800;">AI ADAPTIVE PRESCRIPTION CLINIC</div>
                <div style="font-size:1.15rem; font-weight:800; margin-top:2px;">💊 ${rx.rx_title}</div>
                <div style="font-size:0.85rem; color:#E2E8F0; margin-top:4px;">${rx.rx_reason}</div>
              </div>
              <button class="cta-btn" style="background:#FACC15; color:#0F172A;" onclick="goStage(3)">
                🏆 처방 완료 후 실전 수능 대비 문제 풀기 ➔
              </button>
            </div>

            <div class="grid-2">
              <!-- Left: Step 0 Prerequisite Bridge + Step 1/2 Core Drill -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>🪜 [처방 1단계] 하위 학년 선행 결손 징검다리 복습</span>
                    <span class="badge badge-amber">${rx.step0_remedial.badge}</span>
                  </div>
                  <div style="background:#FFFBEB; border:1px solid #FDE68A; padding:12px; border-radius:9px; font-size:0.89rem; margin-bottom:12px;">
                    ${rx.step0_remedial.rule_box}
                  </div>
                  <div style="font-weight:800; font-size:0.9rem; margin-bottom:8px;">
                    ❓ 확인 퀴즈: ${rx.step0_remedial.mini_question}
                  </div>
                  <div style="display:flex; gap:10px; flex-wrap:wrap;">
                    ${rx.step0_remedial.choices.map((ch, idx) => `
                      <button class="ox-btn" onclick="
                        const ok = (${idx} === ${rx.step0_remedial.choices.indexOf(rx.step0_remedial.correct)});
                        this.className = 'ox-btn ' + (ok ? 'done-ok' : 'done-no');
                        document.getElementById('step0-fb').style.display = 'block';
                      ">${ch}</button>
                    `).join('')}
                  </div>
                  <div id="step0-fb" class="opt-feedback" style="border-left-color:#16A34A; background:#F0FDF4;">
                    ⭕ ${rx.step0_remedial.feedback}
                  </div>
                </div>

                <div class="card">
                  <div class="card-title">
                    <span>🧠 [처방 2단계] Dick & Carey 병목 돌파 (단서 포착 + 사고구술 조립)</span>
                    <span class="badge badge-blue">${rx.step1_2_drill.badge}</span>
                  </div>
                  <div style="font-size:0.81rem; color:#475569; margin-bottom:6px;">
                    💡 지문 속 노란색 <b>단서 칩</b>을 클릭해 활성화한 뒤, 아래 사고구술(Think-Aloud) 빈칸을 완성하세요.
                  </div>
                  <div class="passage-box">
                    <p>${rx.step1_2_drill.passage_snippet}</p>
                  </div>
                  <div style="background:#EFF6FF; border:1px solid #BFDBFE; border-radius:10px; padding:14px;">
                    <div style="font-weight:800; color:#1E40AF; font-size:0.89rem; margin-bottom:8px;">
                      🗣️ 사고구술(Think-Aloud) 구조 조립: ${rx.step1_2_drill.think_aloud_prompt}
                    </div>
                    ${rx.step1_2_drill.cloze_sentences.map(line => {
                      let rendered = line;
                      rx.step1_2_drill.blanks.forEach(b => {
                        const selHtml = `
                          <select class="cloze-select" id="rx-cloze-${b.id}" onchange="checkRxCloze('${b.id}', '${b.correct}')">
                            <option value="">-- 선택 --</option>
                            ${b.options.map(o => `<option value="${o}">${o}</option>`).join('')}
                          </select>
                        `;
                        rendered = rendered.replace(`{${b.id}}`, selHtml);
                      });
                      return `<div style="margin-bottom:8px; font-size:0.89rem; font-weight:700;">${rendered}</div>`;
                    }).join('')}
                  </div>
                </div>
              </div>

              <!-- Right: Step 3 Distractor Vaccine Drill -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>🛡️ [처방 3단계] 수능 매력적 오답 함정 백신 드릴 (O/X 판별)</span>
                    <span class="badge badge-red">${rx.step3_vaccine.badge}</span>
                  </div>
                  <div style="font-size:0.85rem; color:#334155; margin-bottom:12px;">
                    ${rx.step3_vaccine.desc}
                  </div>
                  ${rx.step3_vaccine.items.map((item, idx) => `
                    <div class="vaccine-card">
                      <div style="font-weight:800; font-size:0.9rem; margin-bottom:8px;">
                        문장 ${idx + 1}. “${item.statement}”
                      </div>
                      <div>
                        <button class="ox-btn" onclick="checkVaccine(this, '${item.answer}', 'O', 'vac-fb-${idx}')">⭕ O (적절함)</button>
                        <button class="ox-btn" onclick="checkVaccine(this, '${item.answer}', 'X', 'vac-fb-${idx}')">❌ X (함정 오답!)</button>
                      </div>
                      <div id="vac-fb-${idx}" class="opt-feedback">
                        <b>[정답: ${item.answer}]</b> ${item.reason}
                      </div>
                    </div>
                  `).join('')}

                  <div style="margin-top:18px; padding:14px; background:#F0FDF4; border:1px solid #BBF7D0; border-radius:10px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                    <div>
                      <div style="font-weight:800; color:#166534; font-size:0.92rem;">✅ 맞춤형 처방 3단계 훈련 준비 완료!</div>
                      <div style="font-size:0.8rem; color:#15803D;">방금 익힌 공식을 적용해 학년 맞춤 실전 수능 문제를 풀어 보세요.</div>
                    </div>
                    <button class="cta-btn" style="background:#16A34A;" onclick="goStage(3)">
                      🏆 실전 수능 대비 문제로 이동 ➔
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>
        `;

        document.querySelectorAll('.rx-cue').forEach(el => {
          el.onclick = () => el.classList.toggle('active');
        });
        return;
      }

      // =====================================================================
      // STAGE 3: 실전 수능 대비 문제 (프로토타입 지문·어휘·단서·수능문항·성장리포트 통합)
      // =====================================================================
      if (currentStage === 3) {
        const csat = p.real_csat_test;
        ws.innerHTML = `
          ${studentHeader}
          <section class="stage-panel active">
            <div class="grid-2">
              <!-- Left: Full Curriculum Passage + Visual Chart + Vocab Notes -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>📖 ${csat.test_title}</span>
                    <button class="ox-btn" id="cue-toggle-btn" style="font-size:0.76rem; padding:4px 10px; border-color:#CA8A04; color:#92400E; background:#FEF9C3;" onclick="togglePassageCues()">
                      🔍 본문 핵심 단서 하이라이팅 켜기
                    </button>
                  </div>
                  <div style="font-size:0.79rem; color:#475569; margin-bottom:8px; font-weight:700;">
                    • 지문 규격: ${csat.passage_spec}
                  </div>
                  <div style="font-weight:800; font-size:1.05rem; color:#0F172A; margin-bottom:8px;">
                    「${csat.passage_title}」
                  </div>
                  <div class="passage-box">
                    ${csat.paragraphs.map((para, i) => `<p><span style="color:#94A3B8;font-size:0.76rem;font-weight:700;margin-right:4px;">[${i+1}문단]</span>${para}</p>`).join('')}
                  </div>
                  ${csat.visual_html || ''}
                  <div class="vocab-bar">
                    ${(csat.vocab_notes || []).map(v => `
                      <div class="vocab-chip">
                        <b>${v.word}</b> <span style="color:#64748B;">(${v.tier})</span>: ${v.desc}
                      </div>
                    `).join('')}
                  </div>
                </div>
              </div>

              <!-- Right: Real CSAT Questions & Before/After Growth Report -->
              <div>
                <div class="card">
                  <div class="card-title">
                    <span>✍️ KICE 평가원 스타일 실전 수능 대비 문항 세트</span>
                    <span class="badge badge-green">선지 클릭 시 오답 공식(D1~D6) 즉시 해설</span>
                  </div>
                  ${csat.questions.map((q, qIdx) => `
                    <div class="csat-q-box">
                      <div style="margin-bottom:6px;">
                        <span class="badge badge-blue">${q.archetype}</span>
                      </div>
                      <div style="font-weight:800; font-size:0.95rem; margin-bottom:8px;">
                        문항 ${q.q_no}. ${q.stem}
                      </div>
                      ${q.bogi ? `<div class="bogi-box">${q.bogi}</div>` : ''}
                      <div>
                        ${q.options.map(opt => `
                          <button class="csat-opt-btn" onclick="solveCsatOption(this, ${opt.is_correct ? 'true' : 'false'}, 'csat-fb-${qIdx}-${opt.no}')">
                            <span style="font-weight:800;">${opt.no}번.</span>
                            <span>${opt.text}</span>
                          </button>
                          <div id="csat-fb-${qIdx}-${opt.no}" class="opt-feedback" style="border-left-color:${opt.is_correct ? '#16A34A' : '#DC2626'};">
                            <div style="font-weight:800; font-size:0.78rem; color:#475569; margin-bottom:2px;">[${opt.formula}]</div>
                            <div>${opt.explanation}</div>
                          </div>
                        `).join('')}
                      </div>
                    </div>
                  `).join('')}

                  <!-- Growth Banner -->
                  <div id="growth-banner" class="growth-banner">
                    <div style="font-size:1.05rem; font-weight:800; margin-bottom:6px;">
                      🎉 [진단 ➔ 맞춤형 처방 ➔ 실전 수능 전이 성공!] 학습자 성취도 향상 리포트
                    </div>
                    <div style="font-size:0.86rem; opacity:0.95; margin-bottom:10px;">
                      • <b>목표 위계(${p.slot_id}) 도달률:</b> 진단 초기 <b>42% (미달)</b> ➔ 처방 및 실전 통과 후 <b>96% (마스터 달성!)</b><br>
                      • <b>수능 매력적 오답 함정 방어력:</b> 집중 취약 함정 방어 성공 · 목표 이독성(${p.complexity_metrics.kread_target}) 지문 자립 독해 완료!
                    </div>
                    <button class="cta-btn" style="background:#FACC15; color:#0F172A;" onclick="goStage(1)">
                      📊 1단계 진단 대시보드 다시 보기
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </section>
        `;
      }
    }

    function checkRxCloze(blankId, correctVal) {
      const el = document.getElementById(`rx-cloze-${blankId}`);
      if (!el) return;
      if (el.value === correctVal) {
        el.style.background = '#DCFCE7';
        el.style.borderColor = '#16A34A';
      } else if (el.value !== '') {
        el.style.background = '#FEE2E2';
        el.style.borderColor = '#DC2626';
      }
    }

    function checkVaccine(btn, correctAns, chosenAns, fbId) {
      btn.classList.remove('done-ok', 'done-no');
      btn.classList.add(correctAns === chosenAns ? 'done-ok' : 'done-no');
      const fb = document.getElementById(fbId);
      if (fb) fb.style.display = 'block';
    }

    function solveCsatOption(btn, isCorrect, fbId) {
      btn.classList.remove('correct', 'wrong');
      btn.classList.add(isCorrect ? 'correct' : 'wrong');
      const fb = document.getElementById(fbId);
      if (fb) fb.style.display = 'block';
      if (isCorrect) {
        const banner = document.getElementById('growth-banner');
        if (banner) banner.classList.add('show');
      }
    }

    // Render Tab 3 Hierarchy Explorer
    function renderHierarchyTable() {
      const sheetKey = document.getElementById('f-sheet').value;
      const gradeVal = document.getElementById('f-grade').value;
      const domainVal = document.getElementById('f-domain').value;
      const kw = (document.getElementById('f-keyword').value || '').trim().toLowerCase();

      const rows = HIERARCHY_DATA[sheetKey] || [];
      const filtered = rows.filter(r => {
        if (gradeVal !== 'ALL' && r.grade !== gradeVal) return false;
        if (domainVal !== 'ALL' && !(r.domain || '').includes(domainVal)) return false;
        if (kw) {
          const hay = `${r.code} ${r.sub_skill_name} ${r.dc_step1} ${r.dc_step2} ${r.dc_step3} ${r.mager_reading}`.toLowerCase();
          if (!hay.includes(kw)) return false;
        }
        return true;
      });

      const wrap = document.getElementById('hierarchy-table-wrap');
      wrap.innerHTML = `
        <div style="margin-bottom:8px; font-size:0.85rem; color:#475569; font-weight:700;">
          검색된 위계 목표: 총 ${filtered.length}개
        </div>
        <table class="std-table">
          <thead>
            <tr>
              <th style="width:120px;">위계 코드</th>
              <th style="width:85px;">학년 (체험)</th>
              <th style="width:130px;">영역 / 층위</th>
              <th style="width:190px;">세부 하위기능명</th>
              <th>Dick & Carey 3단계 (Step 1 ➔ Step 2 ➔ Step 3)</th>
              <th>이해(독해·점검) Mager 수행목표</th>
            </tr>
          </thead>
          <tbody>
            ${filtered.map(r => `
              <tr>
                <td><b>${r.code}</b></td>
                <td>
                  <b>${r.grade}</b><br>
                  <button class="ox-btn" style="font-size:0.72rem; padding:2px 6px; margin-top:4px; border-color:#2563EB; color:#1D4ED8;" onclick="jumpToGradeFromExplorer('${r.grade}')">
                    코스웨어 체험 ➔
                  </button>
                </td>
                <td>${r.domain}<br><span style="color:#2563EB;font-size:0.78rem;">${r.layer}</span></td>
                <td><b>${r.sub_skill_name}</b></td>
                <td style="font-size:0.8rem;">
                  • <b>Step 1:</b> ${r.dc_step1}<br>
                  • <b>Step 2:</b> ${r.dc_step2}<br>
                  • <b>Step 3:</b> ${r.dc_step3}
                </td>
                <td style="font-size:0.8rem;">${r.mager_reading}</td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      `;
    }

    // Initialize All-in-One App
    renderPersonaBar();
    updateStageStepper();
    renderWorkspace();
    renderHierarchyTable();
  </script>
</body>
</html>
"""

out_html = UNIFIED_HTML.replace(
    "__GRADES_JSON__", json.dumps(UNIFIED_GRADES_DATA, ensure_ascii=False)
).replace(
    "__HIERARCHY_JSON__", json.dumps(HIERARCHY_DATA, ensure_ascii=False)
)

out_path = os.path.join(OUTPUT_DIR, "expository_literacy_courseware.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(out_html)

print("Saved courseware/output/expository_literacy_courseware.html successfully!")
