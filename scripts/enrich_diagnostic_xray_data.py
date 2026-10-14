# -*- coding: utf-8 -*-
"""
통합 코스웨어 데이터 고도화 스크립트 (enrich_diagnostic_xray_data.py)
- 기존 프로토타입의 모든 요소(Step 1 단서 포착 미션, Step 2 사고구술, Step 3 실전 수능 문항, 2개 이상의 풍부한 지문 세트) 보존
- 학습자가 '어디가, 왜, 어떻게 부족한지' 전 영역에 걸쳐 낱낱이 진단되는 정밀 X-Ray 진단 데이터(16개 설명문 하위기능 V1-1~W5 + 6개 공통기초 A1~A6 + 6대 텍스트 구조 + 어휘 Tier 1~3·통사 복잡도 + Dick & Carey 병목 + D1~D6 오답 메커니즘 + 종적 결손 뿌리 역추적) 추가
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

with open(os.path.join(DATA_DIR, "unified_courseware_master_data.json"), "r", encoding="utf-8") as f:
    GRADES_DATA = json.load(f)

# 16개 설명문 하위기능 마스터 정의
SUBSKILL_16_META = [
    {"code": "V1-1", "domain": "1. 사실적 이해", "name": "세부 정보 확인", "desc": "명시적 사실·정의·수치·명칭의 정확한 위치 포착"},
    {"code": "V1-2", "domain": "1. 사실적 이해", "name": "관계 확인 (지시어·분류/분석)", "desc": "지시어 연결, 상하위(분류) vs 전체-부분(분석) 위계 파악"},
    {"code": "V1-3", "domain": "1. 사실적 이해", "name": "구조 파악 (6대 설명 구조)", "desc": "담화 표지를 단서로 순서·인과·비교·문제해결 구조 파악"},
    {"code": "V1-4", "domain": "1. 사실적 이해", "name": "중심 내용·요약", "desc": "문단 중심 문장 식별 및 글 전체 핵심 요약"},
    {"code": "V2-1", "domain": "2. 추론적 이해", "name": "문맥·다의어·개념어 추론", "desc": "문맥 호응어를 단서로 다의어 의미 구별 및 신출 개념어 추론"},
    {"code": "V2-2", "domain": "2. 추론적 이해", "name": "생략된 인과·전제 추론", "desc": "명시되지 않은 매개 원리, 이유, 조건 변화 시 결과 추론"},
    {"code": "V2-3", "domain": "2. 추론적 이해", "name": "시각자료(표·그래프) 통합 추론", "desc": "본문 원리와 표·막대·꺾은선·비율그래프·모식도 교차 해석"},
    {"code": "V2-4", "domain": "2. 추론적 이해", "name": "<보기> 구체 사례 적용 추론", "desc": "본문의 추상적 원리를 <보기>의 새로운 실험·일상 상황에 전이"},
    {"code": "V3-1", "domain": "3. 비판적 이해", "name": "사실과 의견·주관 구분", "desc": "객관적 사실 진술과 필자의 주관적 감상·의견 판별"},
    {"code": "V3-2", "domain": "3. 비판적 이해", "name": "4대 준거 타당성·신뢰성 비판", "desc": "정확성·출처 공신력·서술 객관성·관점 공정성 기준 평가"},
    {"code": "V3-3", "domain": "3. 비판적 이해", "name": "다매체·복수 관점 비교 평가", "desc": "동일 주제 서로 다른 매체·관점 글의 설명 방식 비교"},
    {"code": "W1", "domain": "4. 표현·작문", "name": "설명문 작문 계획 세우기", "desc": "예상 독자·목적·주제에 맞는 설명 방법 및 계획 점검"},
    {"code": "W2", "domain": "4. 표현·작문", "name": "자료 선별 및 통합 활용", "desc": "통계표·전문가 인터뷰·신문기사를 초고 맥락에 맞게 결합"},
    {"code": "W3", "domain": "4. 표현·작문", "name": "개요 조직 및 구조 수정", "desc": "글의 처음-중간-끝 개요 배열 및 하위 항목 이동·추가"},
    {"code": "W4", "domain": "4. 표현·작문", "name": "조건에 맞는 설명 문단 쓰기", "desc": "제시된 담화 표지·구조·어휘 조건을 모두 충족하는 문장 산출"},
    {"code": "W5", "domain": "4. 표현·작문", "name": "내용·조직·표현 3단계 퇴고", "desc": "근거 보충(내용), 통일성·접속어(조직), 주술 호응(표현) 교정"}
]

# 학년별 정밀 X-Ray 진단 프로파일 & 기존 프로토타입 Step 1·2·3 미션 보강 데이터
ENRICHMENTS = {
    1: {
        "xray_overview": {
            "overall_score": 64,
            "percentile": "하위 32% (주의·처방 필요군)",
            "where_summary": "① [사실적 이해 V1-2] 지시어(‘이 동물, 이 물건’) 연결 및 전체-부분(부위↔기능) 짝짓기 결손(42점) / ② [공통기초 A2·A4] 한 문장 내 주어-서술어 짝짓기 흔들림",
            "how_summary": "낱말 자체(코, 귀, 다리, 짧은바늘, 긴바늘)는 눈으로 찾지만(Step 1 정상 86%), 부위 이름과 뒤따르는 서술어를 1:1로 묶어 기억하지 못해(Step 2 병목 40%), 선지에서 두 부위의 역할을 서로 크로스해 놓은 [D4 부위-역할 교차 함정]에 88% 확률로 걸려듭니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 기초 어휘 (김광해 1등급)", "score": 92, "status": "good", "detail": "몸집, 부채, 기둥 등 일상 기초 명사·형용사 이해 안정적"},
                {"category": "Tier 2 범교과 사고·기능어", "score": 48, "status": "danger", "detail": "‘각각, 대신, 역할을 하다, 가리키다’ 등 관계 설정 어휘 취약"},
                {"category": "Tier 3 교과 개념어 (통합교과)", "score": 70, "status": "warn", "detail": "시계 바늘, 동물 부위 명칭은 아나 기능 서술어와 결합 시 혼동"},
                {"category": "문장·통사 해독력 (홑문장 ➔ 이어진문장)", "score": 45, "status": "danger", "detail": "‘~해서 ~합니다’ 형태의 이어진문장에서 앞 절과 뒷절의 주어를 놓침"},
                {"category": "담화 표지·지시어 추적력 (A4)", "score": 40, "status": "danger", "detail": "‘이것, 이 동물’이 바로 앞 문장 주어를 가리킨다는 응집 규칙 미형성"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거 (특징 나열)", "score": 78, "status": "good"},
                {"structure": "분석 (전체-부분·부위별 기능)", "score": 38, "status": "danger"},
                {"structure": "분류·구분 (종류 묶기)", "score": 55, "status": "warn"},
                {"structure": "순서·과정 (차례)", "score": 62, "status": "warn"},
                {"structure": "비교·대조 (공통점·차이점)", "score": 60, "status": "warn"},
                {"structure": "인과 (이유·까닭)", "score": 65, "status": "warn"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 85, "state": "mastered", "why": "단일 낱말·이름 위치 찾기는 정확함"},
                {"code": "V1-2", "score": 38, "state": "critical", "why": "지시어 연결 및 [부위↔역할] 짝짓기에서 D4 교차 오답 발생 (핵심 처방 타깃)"},
                {"code": "V1-3", "score": 60, "state": "fragile", "why": "전체-부분 설명 구조도에서 빈칸 위치 파악 불안정"},
                {"code": "V1-4", "score": 75, "state": "mastered", "why": "글이 무엇을 설명하는지(코끼리/시계) 화제 찾기는 양호"},
                {"code": "V2-1", "score": 68, "state": "fragile", "why": "비유적 표현(‘부채처럼’, ‘기둥 같은’)의 문맥 의미 추론 보강 필요"},
                {"code": "V2-2", "score": 58, "state": "fragile", "why": "‘~하려고(목적·이유)’와 행동 연결이 긴 문장에서 흔들림"},
                {"code": "V2-3", "score": 52, "state": "fragile", "why": "부분 명칭 그림과 본문 문장을 동시에 대조하는 시각 통합 미숙"},
                {"code": "V2-4", "score": 55, "state": "fragile", "why": "<보기>의 구체적 상황(더운 낮)에 본문 원리(귀 팔랑거림) 적용 연습 필요"},
                {"code": "V3-1", "score": 82, "state": "mastered", "why": "실제 코끼리 설명과 동화 속 상상 구별 양호"},
                {"code": "V3-2", "score": 76, "state": "mastered", "why": "대상의 특징을 바르게 말한 친구 찾기 양호"},
                {"code": "V3-3", "score": 72, "state": "mastered", "why": "사진과 그림 자료의 차이 이해 양호"},
                {"code": "W1", "score": 70, "state": "mastered", "why": "설명할 동물 고르고 특징 질문 만들기 양호"},
                {"code": "W2", "score": 64, "state": "fragile", "why": "관찰 카드에서 알맞은 특징 고르기 보강 필요"},
                {"code": "W3", "score": 58, "state": "fragile", "why": "전체 소개 문장 뒤에 부분 설명 문장 이어 쓰기 연습 필요"},
                {"code": "W4", "score": 50, "state": "critical", "why": "‘[부위]는 [모양]이고 [하는 일]을 합니다’ 조건 문장 완성 미숙"},
                {"code": "W5", "score": 62, "state": "fragile", "why": "문장 끝 알맞은 마침표 및 어색한 짝꿍 말 고치기 보강 필요"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 ㉠‘이 동물은’이 가리키는 말과 코끼리의 세 부분(코, 귀, 다리) 단서를 찾아 하이라이팅하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: 코끼리의 각 부위(코·귀·다리)와 하는 일을 바르게 연결해 보세요."
        }
    },
    2: {
        "xray_overview": {
            "overall_score": 66,
            "percentile": "하위 35% (순서·과정 구조 집중 처방군)",
            "where_summary": "① [사실적 이해 V1-3] 순서·과정 담화 표지(‘먼저-그다음-얼마 뒤-마지막으로’) 기반 단계 배열 심각 결손(40점) / ② [관계 확인 V1-2] 문단 간 장소·사물 지시어(‘이곳에서, 이것을’) 추적 미숙",
            "how_summary": "개별 사건(‘알을 낳다’, ‘뒷다리가 나오다’, ‘모심기’)은 기억하지만(Step 1 85%), 시간·순서 담화 표지에 번호를 매겨 순차 사슬을 만드는 과정(Step 2 42%)이 생략되어, 선지에서 앞뒤 순서를 살짝 뒤바꾼 [D2 선후 순서 왜곡 함정]에 88% 확률로 오답을 고릅니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 기초 어휘 (김광해 1~2등급)", "score": 88, "status": "good", "detail": "연못, 거품, 수건, 봄·여름·가을 등 일상 어휘 안정적"},
                {"category": "Tier 2 담화·순서 표지 어휘", "score": 42, "status": "danger", "detail": "‘먼저, 그다음, 이어서, 얼마 뒤, 마지막으로’의 순차 위계 감각 취약"},
                {"category": "Tier 3 교과 개념어 (통합·과학)", "score": 68, "status": "warn", "detail": "알덩이, 아가미, 겉껍질 등 생물·농업 기초 개념어 보강 필요"},
                {"category": "문장·통사 해독력 (시간 부사절·연결어미)", "score": 48, "status": "danger", "detail": "‘~한 뒤에’, ‘~고 나서’, ‘~면’ 등 선후 관계 연결어미 처리 미숙"},
                {"category": "지시어·대용어 응집 추적 (A4)", "score": 50, "status": "danger", "detail": "앞 구절의 결과물(‘하얀 쌀’)을 받는 ‘이것’을 첫 문장 단어와 혼동"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거", "score": 82, "status": "good"},
                {"structure": "분석 (전체-부분)", "score": 74, "status": "good"},
                {"structure": "분류·구분", "score": 70, "status": "good"},
                {"structure": "순서·과정 (시계열 단계)", "score": 38, "status": "danger"},
                {"structure": "비교·대조", "score": 65, "status": "warn"},
                {"structure": "인과 (이유·까닭)", "score": 78, "status": "good"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 84, "state": "mastered", "why": "단일 문장 내 명시적 사실 찾기는 우수함"},
                {"code": "V1-2", "score": 52, "state": "fragile", "why": "문장 너머 지시어(‘이것, 이곳’) 연결 시 원거리 명사와 혼동"},
                {"code": "V1-3", "score": 38, "state": "critical", "why": "4단계 과정(알➔올챙이➔뒷다리·앞다리➔개구리) 순서 배열 결손 (핵심 처방 타깃)"},
                {"code": "V1-4", "score": 76, "state": "mastered", "why": "글 전체 화제(개구리가 자라는 과정) 파악 양호"},
                {"code": "V2-1", "score": 72, "state": "mastered", "why": "문맥 속 기초 낱말 뜻 짐작하기 양호"},
                {"code": "V2-2", "score": 80, "state": "mastered", "why": "‘~하려면’, ‘~기 때문에’ 이유 찾기는 안정적"},
                {"code": "V2-3", "score": 48, "state": "critical", "why": "과정 화살표 그림의 빈칸(③번 단계)과 본문 매칭 취약"},
                {"code": "V2-4", "score": 64, "state": "fragile", "why": "다른 동물(나비·벼)의 성장 과정에 순서 원리 적용 보강 필요"},
                {"code": "V3-1", "score": 78, "state": "mastered", "why": "관찰 사실과 느낌 구분 양호"},
                {"code": "V3-2", "score": 74, "state": "mastered", "why": "설명이 맞는지 점검하기 양호"},
                {"code": "V3-3", "score": 70, "state": "mastered", "why": "순서 그림의 도움 효과 이해 양호"},
                {"code": "W1", "score": 72, "state": "mastered", "why": "관찰한 과정 글쓰기 계획 양호"},
                {"code": "W2", "score": 66, "state": "fragile", "why": "순서 사진 자료 고르기 보강 필요"},
                {"code": "W3", "score": 46, "state": "critical", "why": "순서 말을 넣어 4단계 문장 차례대로 배열하기 미숙"},
                {"code": "W4", "score": 58, "state": "fragile", "why": "‘먼저 ~ 그다음 ~ 마지막으로’ 조건 문장 쓰기 연습 필요"},
                {"code": "W5", "score": 64, "state": "fragile", "why": "뒤바뀐 순서 문장 찾아 고치기 보강 필요"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 순서를 나타내는 담화 표지 4개(‘먼저, 그다음, 얼마 뒤, 마지막으로’)를 찾아 하이라이팅하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: 개구리가 자라는 4단계 기차 칸과 호흡 기관(아가미➔허파·피부) 변화를 연결하세요."
        }
    },
    3: {
        "xray_overview": {
            "overall_score": 65,
            "percentile": "하위 34% (다의어·학술개념어 문맥 추론 처방군)",
            "where_summary": "① [추론적 이해 V2-1] 일상 다의어(‘높다, 크다, 가리키다’)의 학술 문맥 의미 구별 및 개념어(‘소리의 세기 vs 높낮이’) 추론 결손(44점) / ② [공통기초 A5] 연어(짝꿍 말) 호응 관계 파악 부족",
            "how_summary": "어휘의 표면적 글자만 보고 앞뒤에 결합된 주어·목적어(‘소리가 높다’ vs ‘산이 높다’, ‘북을 세게 치다’ vs ‘짧은 음판을 치다’)를 연결하지 못해(Step 2 병목 38%), 다의어의 기본 의미나 비교 대상의 속성을 교차 치환한 [D4 다의어·속성 교차 함정]에 90% 확률로 빠집니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 일상 어휘 (기본 의미)", "score": 88, "status": "good", "detail": "산이 높다, 소리가 크다 등 1차적·물리적 기본 의미는 잘 앎"},
                {"category": "Tier 1/2 다의어 문맥 확장 의미 (A5)", "score": 38, "status": "danger", "detail": "‘높다(위치/음역/온도/존경)’, ‘가리키다 vs 가르치다’ 문맥 변별 심각 취약"},
                {"category": "Tier 2 범교과 비교·대조 표지", "score": 64, "status": "warn", "detail": "‘반면에, 이와 달리, ~할수록’ 대조·비례 표지 주의 깊게 읽기 필요"},
                {"category": "Tier 3 교과 개념어 (초3 과학)", "score": 46, "status": "danger", "detail": "‘소리의 세기(떨림 폭)’와 ‘소리의 높낮이(떨림 빠르기)’ 개념 속성 혼동"},
                {"category": "문장·통사 해독력 (‘~할수록 ~하다’ 비례 구문)", "score": 54, "status": "warn", "detail": "조건 비례 구문에서 원인 변인과 결과 변인을 크로스하여 오독함"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거", "score": 85, "status": "good"},
                {"structure": "분석 (전체-부분)", "score": 80, "status": "good"},
                {"structure": "분류·구분", "score": 72, "status": "good"},
                {"structure": "순서·과정", "score": 78, "status": "good"},
                {"structure": "비교·대조 (두 개념 속성 대조)", "score": 42, "status": "danger"},
                {"structure": "인과 (실험 조건 ➔ 결과)", "score": 55, "status": "warn"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 86, "state": "mastered", "why": "실험 준비물(작은북, 좁쌀, 실로폰) 명시적 확인 우수"},
                {"code": "V1-2", "score": 60, "state": "fragile", "why": "두 비교 대상(세기 vs 높낮이)의 속성 짝짓기에서 혼동 발생"},
                {"code": "V1-3", "score": 74, "state": "mastered", "why": "‘먼저 ~ 반면에/이와 달리’ 대조 문단 구성 파악 양호"},
                {"code": "V1-4", "score": 82, "state": "mastered", "why": "문단별 중심 문장 찾기 안정적"},
                {"code": "V2-1", "score": 38, "state": "critical", "why": "다의어 ‘높다’의 문맥 의미 추론 및 유사 어휘 변별 결손 (핵심 처방 타깃)"},
                {"code": "V2-2", "score": 56, "state": "fragile", "why": "음판 길이 ➔ 떨림 빠르기 ➔ 소리 높낮이 비례 인과 추론 보강 필요"},
                {"code": "V2-3", "score": 64, "state": "fragile", "why": "실험 비교표의 비교 기준 열(치는 힘 vs 음판 길이) 교차 읽기 보강 필요"},
                {"code": "V2-4", "score": 46, "state": "critical", "why": "<보기> 실험에서 ‘긴 음판을 세게 칠 때’ 세기와 높낮이 변화 구분 실패"},
                {"code": "V3-1", "score": 80, "state": "mastered", "why": "실험 관찰 사실과 개인적 느낌 구분 우수"},
                {"code": "V3-2", "score": 72, "state": "mastered", "why": "실험 조건이 공정한지 판단하기 양호"},
                {"code": "V3-3", "score": 70, "state": "mastered", "why": "표와 글의 설명 효과 비교 양호"},
                {"code": "W1", "score": 74, "state": "mastered", "why": "비교 설명문 계획하기 양호"},
                {"code": "W2", "score": 68, "state": "fragile", "why": "실험 결과 표를 활용해 문장 쓰기 연습 필요"},
                {"code": "W3", "score": 70, "state": "mastered", "why": "대조 구조 문단 배열 양호"},
                {"code": "W4", "score": 58, "state": "fragile", "why": "‘반면에’를 넣어 두 개념의 차이를 설명하는 문장 쓰기 보강 필요"},
                {"code": "W5", "score": 62, "state": "fragile", "why": "문맥에 맞지 않는 다의어·유사어 교정하기 연습 필요"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 ‘소리의 세기’ 조건과 ‘소리의 높낮이’ 조건을 나타내는 단어를 하이라이팅하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: 다의어 ‘높다’의 문맥 의미와 [음판 길이 ➔ 떨림 속도 ➔ 소리 높낮이] 관계를 조립하세요."
        }
    },
    4: {
        "xray_overview": {
            "overall_score": 63,
            "percentile": "하위 30% (복수 시각자료·그래프 추론 집중 처방군)",
            "where_summary": "① [추론적 이해 V2-3] 복수 시각자료(막대그래프 + 꺾은선그래프)와 본문 비례·반비례 조건 통합 추론 심각 결손(40점) / ② [인과 추론 V2-2] 실험 통제 변인(식용유 낙하 이유) 추론 미숙",
            "how_summary": "단일 그래프의 숫자(Step 1 84%)는 읽지만, 본문의 복합 조건(‘기온이 높을수록↑ + 습도가 낮을수록↓ ➔ 증산 작용 활발↑’)을 꺾은선그래프의 시간대별 데이터와 결합하는 Step 2(41%)에서 역방향으로 해석하여 [D2 비례·증감 방향 왜곡 함정]에 89% 확률로 빠집니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 기초 어휘", "score": 90, "status": "good", "detail": "일상 어휘 해독 완전 정착"},
                {"category": "Tier 2 수량·비례·추세 학술어", "score": 44, "status": "danger", "detail": "‘비례, 반비례, 급격히, 일정하게 유지, 최고/최저’ 추세 어휘 오독"},
                {"category": "Tier 3 교과 개념어 (초4 과학·수학)", "score": 56, "status": "warn", "detail": "증산 작용, 기공, 자연 증발, 통제 변인의 실험적 의미 보강 필요"},
                {"category": "문장·통사 해독력 (다중 조건 복합문)", "score": 46, "status": "danger", "detail": "‘A가 높고 B가 낮을수록 C가 많아진다’처럼 방향이 반대인 두 조건 동시 처리 미숙"},
                {"category": "시각 매체(축·단위·범례) 문해력", "score": 42, "status": "danger", "detail": "막대그래프(누적 감소량)와 꺾은선그래프(시간대별 기온·습도) 교차 매핑 취약"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거", "score": 86, "status": "good"},
                {"structure": "분석 (전체-부분)", "score": 82, "status": "good"},
                {"structure": "분류·구분", "score": 78, "status": "good"},
                {"structure": "순서·과정 (실험 절차)", "score": 72, "status": "good"},
                {"structure": "비교·대조 (실험군 vs 대조군)", "score": 50, "status": "warn"},
                {"structure": "인과 + 도표 수리 통합", "score": 38, "status": "danger"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 86, "state": "mastered", "why": "기공의 위치와 증산 작용의 정의 확인 우수"},
                {"code": "V1-2", "score": 68, "state": "fragile", "why": "실험군(가: 잎 있음)과 대조군(나: 잎 없음)의 비교 변인 연결 보강 필요"},
                {"code": "V1-3", "score": 75, "state": "mastered", "why": "정의 ➔ 역할 ➔ 실험 ➔ 조건의 문단 구조 파악 양호"},
                {"code": "V1-4", "score": 80, "state": "mastered", "why": "글 전체 핵심 주제 요약 안정적"},
                {"code": "V2-1", "score": 74, "state": "mastered", "why": "기공·증발 문맥 의미 파악 양호"},
                {"code": "V2-2", "score": 50, "state": "critical", "why": "실험에서 물 표면에 ‘식용유’를 떨어뜨린 숨은 이유(통제 변인) 추론 미숙"},
                {"code": "V2-3", "score": 38, "state": "critical", "why": "[막대그래프] + [꺾은선그래프(기온·습도)] + [본문 조건] 3중 통합 추론 결손 (핵심 타깃)"},
                {"code": "V2-4", "score": 54, "state": "fragile", "why": "장마철(습도 높음) vs 맑고 건조한 날 증산량 비교 적용 연습 필요"},
                {"code": "V3-1", "score": 82, "state": "mastered", "why": "실험 측정값과 추측 구분 양호"},
                {"code": "V3-2", "score": 68, "state": "fragile", "why": "실험 설계의 공정성(변인 통제) 평가 보강 필요"},
                {"code": "V3-3", "score": 65, "state": "fragile", "why": "막대그래프와 꺾은선그래프 중 목적에 맞는 자료 선택 연습 필요"},
                {"code": "W1", "score": 76, "state": "mastered", "why": "실험 보고서 계획하기 양호"},
                {"code": "W2", "score": 52, "state": "critical", "why": "두 그래프의 수치를 근거로 인용해 설명 문단 쓰기 미숙"},
                {"code": "W3", "score": 72, "state": "mastered", "why": "실험 과정-결과 개요 조직 양호"},
                {"code": "W4", "score": 60, "state": "fragile", "why": "비례·반비례 조건 문장 서술 연습 필요"},
                {"code": "W5", "score": 68, "state": "fragile", "why": "그래프 수치와 어긋나는 설명 문장 고쳐쓰기 보강 필요"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 실험 대조 조건(가 vs 나), 식용유의 역할, 증산 작용이 활발해지는 기온·습도 조건을 하이라이팅하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: [자료 1 막대그래프]와 [자료 2 시간대별 기온·습도 표]를 본문 원리와 결합해 빈칸을 완성하세요."
        }
    },
    5: {
        "xray_overview": {
            "overall_score": 61,
            "percentile": "하위 28% (수능형 다단계 인과·비판적 평가 집중 처방군)",
            "where_summary": "① [비판적 이해 V3-2] 설명문 4대 평가 준거(정확성·공신력·객관성·공정성) 적용 결손(45점) / ② [추론 V2-2·V2-3] 다단계 인과 역전 취약(42점) / ③ [사실 V1-2] 상하위 분류(종류) vs 전체-부분 분석(부품) 혼동",
            "how_summary": "어휘·문장 표면 해독(Step 1 88%)은 빠르나, ‘원인 ➔ 매개 원리 ➔ 결과’ 화살표 방향과 ‘분류(균계/세균계) vs 분석(보온병 부품)’ 위계를 구조화하는 Step 2(42%)가 취약해, 수능 5지선다의 [D1 인과 역전]·[D4 분류·속성 교차]·[D5 평가준거 왜곡] 함정에 반복해서 걸립니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 기초 어휘", "score": 94, "status": "good", "detail": "일상 어휘 해독 완성"},
                {"category": "Tier 2 학술·비판 사고 도구어 (김광해 3등급)", "score": 46, "status": "danger", "detail": "‘공신력, 객관성, 공정성, 편향, 상하위 분류, 매개, 환원’ 개념 경계 모호"},
                {"category": "Tier 3 교과 개념어 (초5 과학 생물·열)", "score": 52, "status": "warn", "detail": "균계(균사·포자) vs 세균계(단세포·분열), 유기물 vs 무기물 속성 혼동"},
                {"category": "문장·통사 해독력 (다중 내포문·이중 피동/부정)", "score": 50, "status": "danger", "detail": "긴 관형절이 안긴 문장에서 주절의 원인과 종속절의 결과를 거꾸로 파악함"},
                {"category": "비판적 매체 문해력 (출처·의도·균형성)", "score": 44, "status": "danger", "detail": "상업적 홍보 의도나 일방적 편향 서술을 ‘객관적 설명’으로 오판함"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거", "score": 88, "status": "good"},
                {"structure": "분석 (전체-부분 구성 요소)", "score": 48, "status": "danger"},
                {"structure": "분류·구분 (상하위 종류 체계)", "score": 45, "status": "danger"},
                {"structure": "순서·과정", "score": 80, "status": "good"},
                {"structure": "비교·대조 (양면성 대조)", "score": 58, "status": "warn"},
                {"structure": "다단계 연쇄 인과 (생태계·열 이동)", "score": 42, "status": "danger"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 88, "state": "mastered", "why": "본문 내 명시적 사실·수치(1% 미만 등) 확인 우수"},
                {"code": "V1-2", "score": 45, "state": "critical", "why": "상하위 분류(종류)와 전체-부분 분석(구성 요소) 구분 실패 및 균계↔세균계 속성 혼동"},
                {"code": "V1-3", "score": 74, "state": "mastered", "why": "통념 반박형(‘흔히 ~ 그러나’) 문단 전개 파악 양호"},
                {"code": "V1-4", "score": 82, "state": "mastered", "why": "미생물의 양면성과 비판적 읽기 태도 요약 우수"},
                {"code": "V2-1", "score": 72, "state": "mastered", "why": "발효·박멸·고갈 등 한자어 문맥 추론 양호"},
                {"code": "V2-2", "score": 42, "state": "critical", "why": "[분해자 소멸 ➔ 유기물 분해 중단 ➔ 식물 영양분 고갈] 인과 사슬 역전 오답 발생"},
                {"code": "V2-3", "score": 48, "state": "critical", "why": "산호초 백화 현상 등 다중 변수 통계표(수온·백화율·어류 종 수) 결합 추론 취약"},
                {"code": "V2-4", "score": 56, "state": "fragile", "why": "<보기> 실험·실생활 사례에 본문 원리 전이 시 D1 인과 역전 주의 필요"},
                {"code": "V3-1", "score": 76, "state": "mastered", "why": "단순 사실과 의견 구분은 가능함"},
                {"code": "V3-2", "score": 40, "state": "critical", "why": "4대 평가 준거(정확성·공신력·객관성·공정성)로 편향된 매체 글 비판하기 결손 (핵심 타깃)"},
                {"code": "V3-3", "score": 54, "state": "fragile", "why": "서로 다른 관점의 두 설명문 비교 평가 보강 필요"},
                {"code": "W1", "score": 78, "state": "mastered", "why": "설명문 작문 계획 수립 안정적"},
                {"code": "W2", "score": 62, "state": "fragile", "why": "공신력 있는 통계 자료 선별하기 보강 필요"},
                {"code": "W3", "score": 70, "state": "mastered", "why": "분류·대조 구조 개요 작성 양호"},
                {"code": "W4", "score": 66, "state": "fragile", "why": "양면성을 균형 있게 서술하는 문단 쓰기 연습 필요"},
                {"code": "W5", "score": 60, "state": "fragile", "why": "편향적·감정적 표현을 객관적 표현으로 고쳐쓰기 보강 필요"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 균계·세균계 분류 단서, 유익한 역할(발효·페니실린·분해자), 4대 평가 준거 단서를 하이라이팅하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: 인터넷 게시글의 문장들을 [정확성·공신력·객관성·공정성] 4대 준거와 매칭하세요."
        }
    },
    6: {
        "xray_overview": {
            "overall_score": 68,
            "percentile": "하위 36% (수능 화법과 작문 3단계 퇴고 & 연쇄 인과 완성 처방군)",
            "where_summary": "① [표현·작문 W5] 내용·조직(통일성·접속어)·표현(주어-서술어·부사어 호응) 3단계 통합 퇴고 심각 결손(44점) / ② [공통기초 A2·A3] `[6국04-05]` 주술 호응(‘원리는 ~ 까닭이다’ 오류) 미탐지 / ③ [추론 V2-2] 양(+)의 되먹임(알베도 루프) 비례·반비례 추론 보강 필요",
            "how_summary": "독서 지문의 개별 문장(Step 1 86%)은 잘 읽으나, 학생 초고의 문법적 호응 오류(`이유는/원리는 ~ 때문이다/까닭이다`)와 논리적 접속부사(`따라서` vs `그러나`)를 검증하는 Step 3(44%)에서 병목이 발생해, [D5 주술 호응·통일성 역전] 및 [D1 올바른 접속어를 틀리게 고치라는 함정]에 90% 확률로 빠집니다.",
            "vocab_syntax_diag": [
                {"category": "Tier 1 기초 어휘", "score": 96, "status": "good", "detail": "기초 어휘 완전 마스터"},
                {"category": "Tier 2 학술·논리·작문 메타 어휘", "score": 52, "status": "warn", "detail": "‘통일성, 응집성, 호응, 상쇄, 가속화, 양(+)의 되먹임’ 정밀 개념 보강 필요"},
                {"category": "Tier 3 교과 전문 개념어 (초6 과학·사회)", "score": 64, "status": "warn", "detail": "열수지 균형, 태양/지구 복사 에너지, 알베도(반사율) 반비례 관계 주의"},
                {"category": "문장 성분 호응 감각 (`[6국04-05]` A2)", "score": 38, "status": "danger", "detail": "‘핵심 원리는 ~ 까닭이다(❌)’, ‘결코 ~ 할 수 있다(❌)’ 등 호응 오류 불감증"},
                {"category": "문단 간·문장 간 담화 응집성 (A3)", "score": 45, "status": "danger", "detail": "인과 관계(‘따라서’)를 역접(‘그러나’)으로 바꾸라는 선지 함정에 취약"}
            ],
            "text_structure_diag": [
                {"structure": "기술·열거", "score": 92, "status": "good"},
                {"structure": "분석 (전체-부분)", "score": 88, "status": "good"},
                {"structure": "분류·구분", "score": 85, "status": "good"},
                {"structure": "순서·과정", "score": 84, "status": "good"},
                {"structure": "인과 연쇄 (양의 되먹임 루프)", "score": 54, "status": "warn"},
                {"structure": "문제·해결 & 3단계 작문 퇴고 구조", "score": 42, "status": "danger"}
            ],
            "subskill_matrix": [
                {"code": "V1-1", "score": 90, "state": "mastered", "why": "열수지·온실효과·알베도 정의 및 수치(80% vs 10%) 파악 우수"},
                {"code": "V1-2", "score": 84, "state": "mastered", "why": "해빙과 바닷물의 반사율·흡수율 대조 관계 파악 안정적"},
                {"code": "V1-3", "score": 80, "state": "mastered", "why": "원리 ➔ 문제 심화(되먹임) ➔ 해결 방안 구조 파악 우수"},
                {"code": "V1-4", "score": 86, "state": "mastered", "why": "문단별 중심 내용 및 주제 요약 우수"},
                {"code": "V2-1", "score": 82, "state": "mastered", "why": "되먹임·악순환·방패 역할 등 문맥적 의미 추론 양호"},
                {"code": "V2-2", "score": 56, "state": "fragile", "why": "[해빙 감소 ➔ 알베도 하락 ➔ 흡수량 증가 ➔ 수온 상승] 4단계 연쇄 비례 추론 보강 필요"},
                {"code": "V2-3", "score": 68, "state": "fragile", "why": "열수지·알베도 모식도와 복수 통계 자료 결합 해석 연습 필요"},
                {"code": "V2-4", "score": 72, "state": "mastered", "why": "다른 기후 피드백 사례 적용 양호"},
                {"code": "V3-1", "score": 88, "state": "mastered", "why": "과학적 사실과 주장 구분 우수"},
                {"code": "V3-2", "score": 80, "state": "mastered", "why": "근거 자료의 신뢰성 평가 안정적"},
                {"code": "V3-3", "score": 76, "state": "mastered", "why": "매체별 설명 방식 비교 양호"},
                {"code": "W1", "score": 80, "state": "mastered", "why": "보고서 작성 계획 점검 양호"},
                {"code": "W2", "score": 52, "state": "critical", "why": "통계 그래프·전문가 인터뷰·신문기사를 삼각 결합해 초고 보완하기 미숙"},
                {"code": "W3", "score": 64, "state": "fragile", "why": "개요의 하위 항목 누락·순서 수정 보강 필요"},
                {"code": "W4", "score": 60, "state": "fragile", "why": "인과 표지와 비유를 결합한 조건부 결론 문단 작성 연습 필요"},
                {"code": "W5", "score": 40, "state": "critical", "why": "[내용·조직(통일성/접속어)·표현(주술 호응)] 3단계 통합 고쳐쓰기 결손 (핵심 타깃)"}
            ]
        },
        "prototype_step1_2": {
            "step1_mission": "Step 1 [단서 포착 미션]: 본문에서 열수지 균형, 양(+)의 되먹임, 해빙(80%) vs 바닷물(10%) 알베도 단서와 퇴고 구간(㉠~㉤)을 확인하세요!",
            "step2_mission": "Step 2 [관계 연결 사고구술]: [내용·조직·표현 3단계 퇴고 매트릭스]와 [북극 해빙 알베도 양(+)의 되먹임 사슬]을 조립하세요."
        }
    }
}

# 5학년 김민준에게 프로토타입에 있던 산호초 백화 현상 실전 문항도 추가하여 기존 지문·문항 100% 보존!
CORAL_EXTRA_QUESTION = {
    "q_no": 3,
    "archetype": "CSAT-READ-V2-3 (<보기> 해수 온도·산호초 백화율 다중 도표 결합 추론형 - 5지선다)",
    "stem": "윗글의 ‘생태계 상호작용 및 인과 추론 원리’를 바탕으로 <보기>의 산호초 백화 현상 조사 자료를 이해한 내용으로 적절하지 <u>않은</u> 것은?",
    "bogi": "<보기> [A 해역의 산호초 백화 현상과 어류 종 수 변화]\n  산호는 몸속에 사는 ‘공생 조류(식물성 플랑크톤)’에게 서식처와 이산화 탄소를 제공하고, 공생 조류는 광합성으로 만든 영양분을 산호에게 공급한다. 그러나 바닷물 수온이 평년보다 +1.5℃ 이상 높아지는 고수온 현상이 지속되면 공생 조류가 독성 물질을 내뿜게 되고, 산호는 공생 조류를 몸 밖으로 내보내 하얀 석회질 골격만 남는 ‘백화 현상’을 겪다 사멸한다.\n  • 2019년(수온 편차 +0.3℃): 건강한 산호 82% / 백화 산호 8% / 서식 어류 145종\n  • 2022년(수온 편차 +2.1℃): 건강한 산호 35% / 백화 산호 52% / 서식 어류 88종\n  • 2023년(수온 편차 +2.4℃): 건강한 산호 18% / 백화 산호 68% / 서식 어류 54종",
    "options": [
        {
            "no": 1,
            "text": "2019년에는 수온 편차가 +0.3℃로 임계치(+1.5℃)보다 낮아 산호와 공생 조류의 상리 공생이 안정적으로 유지되었겠군.",
            "is_correct": False,
            "formula": "적절한 추론: [2019년 +0.3℃ < +1.5℃] ➔ 건강한 산호 82% 유지",
            "explanation": "⭕ **적절한 이해예요!** 수온 편차가 +1.5℃ 미만일 때는 공생 관계가 잘 유지됩니다."
        },
        {
            "no": 2,
            "text": "2022년과 2023년에 백화 산호 비율이 50%를 넘어선 것은 고수온 현상으로 인해 산호가 공생 조류를 몸 밖으로 배출했기 때문이겠군.",
            "is_correct": False,
            "formula": "적절한 추론: [고수온(+2.1℃, +2.4℃) ➔ 공생 조류 배출 ➔ 백화 비율 급증]",
            "explanation": "⭕ **적절한 이해예요!** +1.5℃ 이상 고수온이 나타나 산호가 공생 조류를 내보낸 결과입니다."
        },
        {
            "no": 3,
            "text": "2022년에서 2023년 사이에 서식 어류 종 수가 54종으로 급감한 까닭은, 어류와 산호가 먼저 사라졌기 때문에 그 결과로 바닷물의 수온 편차가 +2.4℃까지 올라갔기 때문이겠군.",
            "is_correct": True,
            "formula": "정답(부적절) - 오답 공식 [D1 인과 역전 함정]: [수온 상승(원인) ➔ 산호 백화·어류 급감(결과)]을 정반대로 뒤집음!",
            "explanation": "🎉 **[처방 성공! D1 인과 역전 함정 완벽 간파]** 산호와 어류가 사라져서 수온이 올라간 것이 아니라, **수온이 +2.4℃까지 올라갔기 때문에(원인) 산호가 백화 현상을 겪고 서식처를 잃은 어류 종 수가 급감(결과)**한 것입니다!"
        },
        {
            "no": 4,
            "text": "평상시에 산호에게 광합성으로 만든 영양분을 공급하는 주체는 산호 자신이 아니라 몸속의 ‘공생 조류’이겠군.",
            "is_correct": False,
            "formula": "적절한 추론: [D5 주객 전도 방어 확인 - 광합성 주체 = 공생 조류]",
            "explanation": "⭕ **적절한 이해예요!** 광합성으로 영양분을 만드는 주체는 공생 조류입니다."
        },
        {
            "no": 5,
            "text": "A 해역의 어류 다양성을 보전하려면 지구온난화로 인한 여름철 고수온 현상을 완화해야겠군.",
            "is_correct": False,
            "formula": "적절한 추론: [근본 원인(고수온) 해결 방안 도출]",
            "explanation": "⭕ **적절한 이해예요!** 근본 원인인 고수온 현상을 줄여야 산호초 생태계를 지킬 수 있습니다."
        }
    ]
}

for g in GRADES_DATA:
    gnum = g["grade_num"]
    if gnum in ENRICHMENTS:
        g["xray_overview"] = ENRICHMENTS[gnum]["xray_overview"]
        g["prototype_step1_2"] = ENRICHMENTS[gnum]["prototype_step1_2"]
    if gnum == 5:
        # Ensure question 3 (Coral Bleaching from adaptive mockup) is included alongside Microorganisms questions 1 & 2
        if len(g["real_csat_test"]["questions"]) == 2:
            g["real_csat_test"]["questions"].append(CORAL_EXTRA_QUESTION)

with open(os.path.join(DATA_DIR, "unified_courseware_master_data.json"), "w", encoding="utf-8") as f:
    json.dump({
        "subskill_16_meta": SUBSKILL_16_META,
        "grades_data": GRADES_DATA
    }, f, ensure_ascii=False, indent=2)

print("Enriched unified_courseware_master_data.json with full X-Ray diagnostics and all prototype/mockup items!")
