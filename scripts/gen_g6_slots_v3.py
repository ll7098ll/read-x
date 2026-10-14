# -*- coding: utf-8 -*-
"""
Grade 6 Item Bank - Part 3: V3-1, V3-2, V3-3 (Expository slots)
5-Option Standard (expected_opt_len = 5)
"""

from item_bank_schema_helper import build_expository_slot

slots_v3 = {}

# 9. G6-EXP-V3-1
slots_v3["V3-1"] = build_expository_slot(
    grade_num=6,
    subskill_code="V3-1",
    subject="국어·매체 / 실과(친환경 자동차 6-2)",
    unit="5. 친환경 미래 수송 기술",
    concept="친환경 자동차(하이브리드·전기차·수소전기차)의 작동 원리와 보급 통계 보고서 평가",
    text_structure="분류·분석 + 비교·대조",
    structure_type_code="classification",
    passage_title="미래를 달리는 바퀴: 친환경 자동차의 3대 구동 원리와 통계 그래프의 진실",
    paragraphs=[
        "기후위기 극복과 탄소 감축을 위해 내연기관(가솔린·디젤) 중심의 자동차 산업이 친환경 자동차로 급격히 전환되고 있습니다. 친환경 자동차는 동력원과 구동 메커니즘에 따라 크게 '하이브리드차(HEV)', '순수 전기차(BEV)', '수소전기차(FCEV)'의 세 가지 유형으로 분류됩니다.",
        "첫째, 하이브리드차는 기존 내연기관 엔진과 전기 모터를 함께 탑재하여 저속 주행 시에는 모터를 돌리고 고속 주행 시 엔진을 사용하는 과도기적 기술입니다. 둘째, 순수 전기차는 엔진과 기름통을 완전히 없애고 대용량 리튬 배터리의 전기로 모터를 돌려 배기가스를 전혀 배출하지 않습니다. 셋째, 수소전기차는 탱크에 저장된 수소와 공기 중의 산소를 '연료전지'에서 화학 반응시켜 전기를 생산하고 오직 순수한 물(H₂O)만을 배출하는 첨단 기술입니다.",
        "친환경 자동차의 보급 현황을 다루는 미디어 보고서를 읽을 때는 통계 시각자료의 객관성을 비판적으로 검증해야 합니다. 일부 보고서에서는 전기차 보급 대수 막대그래프의 세로축 시작점을 '0'이 아닌 '8만 대'로 잘라내어 표현하기도 합니다. 이렇게 시각자료의 세로축 눈금을 왜곡하면 실제 증가율은 10%에 불과함에도 불구하고 막대의 높이 차이가 5배 이상 극적으로 벌어져 독자에게 엄청난 폭증이라는 착시 현상을 유발합니다.",
        "따라서 훌륭한 독자는 본문의 기술 분류 원리를 정확히 이해할 뿐만 아니라, 첨부된 그래프의 기준점(0점), 단위, 축 눈금의 왜곡 여부를 교차 대조하여 통계의 객관적 진실을 판별해 낼 수 있어야 합니다."
    ],
    vocab_notes=[
        {"word": "수소연료전지", "definition": "수소와 산소의 전기화학 반응을 통해 물을 생성하면서 직접 전기를 생산하는 장치"},
        {"word": "축 눈금 왜곡", "definition": "그래프의 시작점을 0이 아닌 임의의 숫자로 설정하여 시각적 차이를 인위적으로 과장하거나 축소하는 오류"}
    ],
    visual_html="""<div class="p-3 bg-slate-50 rounded border border-slate-300">
      <h4 class="font-bold text-slate-900 mb-2">🚗 친환경차 3종 비교 및 막대그래프 세로축 눈금 왜곡 주의점</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-slate-200">
          <strong class="text-blue-800">친환경차 3대 유형</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>하이브리드:</strong> 엔진 + 모터 (연비 개선)</li>
            <li><strong>순수 전기차:</strong> 배터리 + 모터 (배출가스 0)</li>
            <li><strong>수소전기차:</strong> 수소연료전지 ➔ 모터 (물 배출)</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-slate-200">
          <strong class="text-red-800">통계 그래프 왜곡 주의보</strong>
          <p class="mt-1 text-gray-700">
            세로축 시작점을 80(만 대)으로 자르면, 80만 대에서 90만 대로의 소폭 증가(12.5%)가 시각적으로는 5배 폭증한 것처럼 왜곡됩니다. 반드시 <strong>시작점 0</strong>을 확인해야 합니다.
          </p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v31-c1", "text": "수소전기차는 탱크에 저장된 수소와 공기 중의 산소를 '연료전지'에서 화학 반응시켜 전기를 생산하고 오직 순수한 물(H₂O)만을 배출하는 첨단 기술입니다", "role": "수소전기차의 독창적 배출 메커니즘", "para_idx": 1},
        {"cue_id": "g6-v31-c2", "text": "세로축 눈금을 왜곡하면 실제 증가율은 10%에 불과함에도 불구하고 막대의 높이 차이가 5배 이상 극적으로 벌어져 독자에게 엄청난 폭증이라는 착시 현상을 유발합니다", "role": "통계 그래프 눈금 왜곡의 착시 효과", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "기술 분류 및 매체 비판 평가표",
        "car_types": {
            "하이브리드": "엔진 + 모터 (과도기)",
            "전기차": "배터리 충전 + 모터",
            "수소차": "수소연료전지 (물 배출)"
        },
        "media_critical_reading": {
            "distortion_technique": "막대그래프 세로축 눈금을 0이 아닌 높은 수치에서 시작",
            "effect": "착시 현상으로 소폭 변화를 과장",
            "reader_strategy": "축의 0점 및 실제 백분율 수치 대조 확인"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "기술 메커니즘 분류 확인",
            "stem": "위 글의 2문단에 제시된 친환경 자동차 3종의 동력원과 배출물 특성으로 가장 바른 것은?",
            "target_para_idx": 1,
            "spotlight_quote": "수소전기차는 탱크에 저장된 수소와 공기 중의 산소를 '연료전지'에서 화학 반응시켜 전기를 생산하고 오직 순수한 물(H₂O)만을 배출하는 첨단 기술입니다.",
            "options": [
                {"label": "①", "text": "수소전기차는 수소와 산소를 연료전지에서 반응시켜 전기를 만들며 순수한 물만 배출한다.", "is_correct": True, "formula": "정답", "explanation": "2문단의 수소전기차 설명과 정확히 일치합니다."},
                {"label": "②", "text": "순수 전기차는 디젤 엔진과 대용량 석탄을 태워 모터를 돌린다.", "is_correct": False, "formula": "D3", "explanation": "배터리의 전기로 모터를 돌리며 엔진이 없습니다."},
                {"label": "③", "text": "하이브리드차는 엔진과 모터를 전혀 쓰지 않고 풍력 돛단배로 움직인다.", "is_correct": False, "formula": "D5", "explanation": "본문과 무관한 허구입니다."},
                {"label": "④", "text": "수소전기차는 배기가스로 대량의 유독가스인 이산화 황을 내뿜는다.", "is_correct": False, "formula": "D1", "explanation": "순수한 물(H2O)만 배출합니다."},
                {"label": "⑤", "text": "세 차종 모두 휘발유 기름통을 똑같은 크기로 필수 장착해야 한다.", "is_correct": False, "formula": "D4", "explanation": "전기차와 수소차는 엔진과 기름통이 없습니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "매체 시각자료의 비판적 평가",
            "stem": "3문단에서 글쓴이가 지적한 통계 시각자료의 문제점과 올바른 독해 태도는?",
            "target_para_idx": 2,
            "spotlight_quote": "이렇게 시각자료의 세로축 눈금을 왜곡하면 실제 증가율은 10%에 불과함에도 불구하고 막대의 높이 차이가 5배 이상 극적으로 벌어져 독자에게 엄청난 폭증이라는 착시 현상을 유발합니다.",
            "options": [
                {"label": "①", "text": "세로축 시작점을 0으로 하지 않고 잘라내어 차이를 과장할 수 있으므로, 기준점과 실제 수치를 확인해야 한다.", "is_correct": True, "formula": "정답", "explanation": "3문단과 4문단에 명시된 시각자료 비판 준거입니다."},
                {"label": "②", "text": "신문에 실린 그래프는 무조건 100% 진실이므로 눈금은 볼 필요가 없다.", "is_correct": False, "formula": "D5", "explanation": "비판적 독해 태도와 정반대입니다."},
                {"label": "③", "text": "막대그래프 대신 모든 보고서를 오직 만화 그림으로만 그려야 한다.", "is_correct": False, "formula": "D6", "explanation": "본문과 무관한 진술입니다."},
                {"label": "④", "text": "세로축 눈금을 0에서 시작하면 그래프의 색상이 흐려져 위험하다.", "is_correct": False, "formula": "D2", "explanation": "색상과 무관한 눈금 왜곡 문제입니다."},
                {"label": "⑤", "text": "증가율이 10%일 때 막대 높이는 100배로 키우는 것이 표준 표기법이다.", "is_correct": False, "formula": "D1", "explanation": "왜곡을 부추기는 잘못된 서술입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 그래프를 통한 시각적 왜곡과 착시를 방지하기 위해 반드시 점검해야 할 요소는?",
            "options": [
                {"label": "①", "text": "세로축의 시작 기준점(0)과 실제 수치·단위의 표기", "is_correct": True},
                {"label": "②", "text": "그래프를 인쇄한 종이의 두께와 브랜드", "is_correct": False},
                {"label": "③", "text": "막대에 사용된 물감의 가격과 향기", "is_correct": False},
                {"label": "④", "text": "글쓴이가 좋아하는 자동차 회사의 로고 색상", "is_correct": False},
                {"label": "⑤", "text": "그래프 주변에 그려진 삽화 캐릭터의 표정", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "첨부된 그래프의 기준점(0점), 단위, 축 눈금의 왜곡 여부를 교차 대조하여 통계의 객관적 진실을 판별해 낼 수 있어야 합니다.", "is_correct": True},
                {"label": "②", "text": "기후위기 극복과 탄소 감축을 위해 내연기관(가솔린·디젤) 중심의", "is_correct": False},
                {"label": "③", "text": "친환경 자동차는 동력원과 구동 메커니즘에 따라 크게", "is_correct": False},
                {"label": "④", "text": "첫째, 하이브리드차는 기존 내연기관 엔진과 전기 모터를", "is_correct": False},
                {"label": "⑤", "text": "친환경 자동차의 보급 현황을 다루는 미디어 보고서를 읽을 때는", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "친환경차 기술 분류 및 시각자료 평가문 작성",
        "guide": "수소전기차의 친환경 배출 특성과 그래프 세로축 눈금 검증법을 1문장으로 정리하세요.",
        "template": "수소전기차는 순수한 [물]만을 배출하는 첨단 기술이며, 통계 보고서를 읽을 때는 그래프의 [세로축 시작점(0)]을 확인하여 착시와 과장을 걸러내야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "통계 그래프 평가 시 '세로축 시작점이 0인가? 차이가 과장되지 않았는가?'를 검증해요."},
        "step1_2_drill": {"task": "하이브리드(엔진+모터), 전기차(배터리+모터), 수소차(연료전지+물배출) 연결하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "막대그래프의 세로축을 0이 아닌 높은 수치에서 시작하면 소폭 변화가 과장되어 보일 수 있다.", "answer": "O", "reason": "본문에 설명된 통계 착시 현상입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 광고 속 그래프가 항상 진실은 아닌 이유",
        "situation": "TV 광고나 신문에서 막대그래프를 볼 때",
        "parent_question": "광고에서 어떤 상품 판매량이 5배 뛴 것처럼 보이는데 왜 실제로는 10%만 늘어난 걸까?",
        "expected_answer": "세로축 아래쪽을 0에서 시작하지 않고 잘라내서, 키 차이가 엄청나 보이는 마술(착시)을 부렸기 때문이래요!",
        "coaching_tip": "숫자와 그림을 무조건 믿지 않고 비판적으로 뜯어보는 미디어 리터러시를 북돋워 주세요."
    }
)

# 10. G6-EXP-V3-2
slots_v3["V3-2"] = build_expository_slot(
    grade_num=6,
    subskill_code="V3-2",
    subject="사회·실과(신재생에너지·환경 6-2)",
    unit="2. 지속 가능한 지구촌과 녹색 기술",
    concept="신재생에너지(태양광·풍력·수소) 발전의 원리와 현황 설명 자료의 신뢰성·공정성 평가",
    text_structure="분류 + 비교·대조 + 문제·해결",
    structure_type_code="problem_solution",
    passage_title="햇빛과 바람의 에너지: 신재생에너지의 현주소와 정보의 신뢰성 검증 4대 준거",
    paragraphs=[
        "화석연료 고갈과 기후변화에 대응하기 위해 햇빛, 바람, 물 등 자연의 에너지를 전기로 변환하는 '신재생에너지'가 주목받고 있습니다. 신재생에너지는 자연 에너지를 이용하는 '재생에너지(태양광·풍력·수력)'와 새로운 연료 기술을 이용하는 '신에너지(수소에너지·연료전지)'를 아우르는 개념입니다. 온실가스를 거의 배출하지 않는다는 점에서 지구촌의 핵심 미래 에너지로 꼽힙니다.",
        "그러나 신재생에너지는 명확한 기술적 한계도 지니고 있습니다. 날씨와 계절에 따라 발전량이 불규칙하게 요동치는 '간헐성' 문제입니다. 해가 지는 밤이나 바람이 불지 않는 날에는 전력 생산이 급감하고, 반대로 맑고 바람이 센 날에는 전기가 과도하게 넘쳐 전력망에 과부하를 줄 수 있습니다. 이를 해결하기 위해 남는 전기를 저장해 두었다가 필요할 때 꺼내 쓰는 '에너지 저장 장치(ESS)' 기술 개발이 필수적으로 요구됩니다.",
        "우리가 접하는 신재생에너지 관련 정보에는 특정 기업이나 집단의 이해관계가 얽혀 있는 경우가 많으므로 '4대 준거'를 통해 비판적으로 평가해야 합니다. 첫째 '정확성과 최신성', 둘째 출처 기관의 '공신력과 이해관계 유무', 셋째 감정적 수식어를 배제한 '서술의 객관성', 넷째 유리한 장점만 골라 쓰고 단점을 숨기는 체리피킹(Cherry-picking)이 없는지 살피는 '관점의 공정성'입니다.",
        "예를 들어 상업용 태양광 패널 시공 업체의 블로그 글은 설치 장점만 부각하고 흐린 날의 발전량 저하나 폐패널 환경오염 문제를 누락하기 쉽습니다. 독자는 공인된 국립환경과학원이나 학술 통계 보고서와 교차 검증함으로써 균형 잡힌 시각을 정립해야 합니다."
    ],
    vocab_notes=[
        {"word": "간헐성", "definition": "발전이 연속적이지 않고 기상 조건에 따라 끊기거나 불규칙하게 일어나는 성질"},
        {"word": "체리피킹", "definition": "자신에게 유리한 사례나 통계만을 선별하여 제시하고 불리한 사실은 은폐하는 비공정한 태도"}
    ],
    visual_html="""<div class="p-3 bg-lime-50 rounded border border-lime-200">
      <h4 class="font-bold text-lime-900 mb-2">⚖️ 자료 신뢰성·공정성 평가 4대 준거 매트릭스</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-lime-100">
          <strong class="text-lime-800">1. 정확성 & 공신력</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>최신 연구 데이터 기반인가?</li>
            <li>출처가 정부·국책연구원인가, 이익 기업인가?</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-lime-100">
          <strong class="text-lime-800">2. 객관성 & 공정성</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li>과장된 감정적 형용사가 없는가?</li>
            <li>단점(간헐성)을 누락한 <strong>체리피킹</strong>이 없는가?</li>
          </ul>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v32-c1", "text": "날씨와 계절에 따라 발전량이 불규칙하게 요동치는 '간헐성' 문제입니다", "role": "신재생에너지의 핵심 기술 한계", "para_idx": 1},
        {"cue_id": "g6-v32-c2", "text": "유리한 장점만 골라 쓰고 단점을 숨기는 체리피킹(Cherry-picking)이 없는지 살피는 '관점의 공정성'입니다", "role": "공정성 평가의 핵심 준거", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "자료 검증 4대 준거 다이어그램",
        "energy_facts": {
            "advantages": "청정성, 온실가스 저감",
            "challenges": "날씨에 좌우되는 간헐성 (ESS 저장 장치 필수)"
        },
        "critical_rubrics": {
            "정확성·최신성": "데이터 검증",
            "출처 공신력": "이해관계(상업 광고 여부) 확인",
            "객관성": "감정 배제",
            "공정성": "체리피킹 방지 (장단점 균형)"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "세부 한계 및 보완 기술 확인",
            "stem": "위 글의 2문단에 제시된 신재생에너지의 한계점과 필수 보완 기술은?",
            "target_para_idx": 1,
            "spotlight_quote": "이를 해결하기 위해 남는 전기를 저장해 두었다가 필요할 때 꺼내 쓰는 '에너지 저장 장치(ESS)' 기술 개발이 필수적으로 요구됩니다.",
            "options": [
                {"label": "①", "text": "날씨에 따라 발전량이 불규칙한 간헐성을 극복하기 위해 에너지 저장 장치(ESS)가 필수적이다.", "is_correct": True, "formula": "정답", "explanation": "2문단의 내용과 정확히 일치합니다."},
                {"label": "②", "text": "신재생에너지는 1년 내내 단 1초도 쉬지 않고 똑같은 양의 전기를 만든다.", "is_correct": False, "formula": "D3", "explanation": "날씨에 따라 요동치는 간헐성이 있습니다."},
                {"label": "③", "text": "비가 오고 바람이 불지 않을 때 전기 생산이 100배로 폭증한다.", "is_correct": False, "formula": "D5", "explanation": "생산이 급감합니다."},
                {"label": "④", "text": "남는 전기는 모두 바닷물에 방류하여 버리는 것이 최선이다.", "is_correct": False, "formula": "D4", "explanation": "ESS에 저장해야 합니다."},
                {"label": "⑤", "text": "신재생에너지는 석탄보다 이산화 탄소를 100배 더 많이 뿜어낸다.", "is_correct": False, "formula": "D1", "explanation": "온실가스를 거의 배출하지 않습니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "자료 신뢰성 및 공정성 평가 준거 적용",
            "stem": "3문단과 4문단을 바탕으로 할 때, 상업용 태양광 업체의 홍보 글을 비판적으로 평가하는 태도로 가장 바른 것은?",
            "target_para_idx": 3,
            "spotlight_quote": "예를 들어 상업용 태양광 패널 시공 업체의 블로그 글은 설치 장점만 부각하고 흐린 날의 발전량 저하나 폐패널 환경오염 문제를 누락하기 쉽습니다.",
            "options": [
                {"label": "①", "text": "판매 이익이라는 이해관계가 걸려 장점만 체리피킹했을 수 있으므로 공신력 있는 공공 연구 보고서와 대조한다.", "is_correct": True, "formula": "정답", "explanation": "4문단의 교차 검증 및 비판적 평가 지침과 일치합니다."},
                {"label": "②", "text": "업체 글은 돈을 버는 사람이 썼으니 무조건 100% 진실로 믿고 따른다.", "is_correct": False, "formula": "D5", "explanation": "비판적 평가 태도와 정반대입니다."},
                {"label": "③", "text": "모든 신재생에너지는 사기극이므로 당장 연구를 전면 폐기한다.", "is_correct": False, "formula": "D6", "explanation": "극단적이고 잘못된 오답입니다."},
                {"label": "④", "text": "공공기관의 보고서는 가짜이고 개인 블로그만 공신력이 높다.", "is_correct": False, "formula": "D1", "explanation": "공신력 준거에 어긋납니다."},
                {"label": "⑤", "text": "단점이 전혀 없는 완벽한 정보이므로 그대로 복사해 숙제를 낸다.", "is_correct": False, "formula": "D2", "explanation": "표절 및 비판 부재 오류입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 정보의 공정성을 해치는 대표적 오류로, 유리한 사실만 골라내고 불리한 사실은 숨기는 행위는?",
            "options": [
                {"label": "①", "text": "체리피킹 (Cherry-picking)", "is_correct": True},
                {"label": "②", "text": "형태소 분석", "is_correct": False},
                {"label": "③", "text": "항상성 유지", "is_correct": False},
                {"label": "④", "text": "에너지 저장", "is_correct": False},
                {"label": "⑤", "text": "삼권분립", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "유리한 장점만 골라 쓰고 단점을 숨기는 체리피킹(Cherry-picking)이 없는지 살피는 '관점의 공정성'입니다.", "is_correct": True},
                {"label": "②", "text": "화석연료 고갈과 기후변화에 대응하기 위해 햇빛, 바람, 물 등", "is_correct": False},
                {"label": "③", "text": "그러나 신재생에너지는 명확한 기술적 한계도 지니고 있습니다.", "is_correct": False},
                {"label": "④", "text": "우리가 접하는 신재생에너지 관련 정보에는 특정 기업이나", "is_correct": False},
                {"label": "⑤", "text": "첫째 '정확성과 최신성', 둘째 출처 기관의 '공신력과", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "신재생에너지 및 자료 평가 논술",
        "guide": "신재생에너지의 간헐성 한계와 정보 평가 시 체리피킹 검증법을 1문장으로 정리하세요.",
        "template": "신재생에너지는 날씨에 따른 [간헐성] 한계를 극복해야 하며, 관련 자료를 읽을 때는 장점만 부각하는 [체리피킹]이 없는지 4대 준거로 검증해야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "자료 평가 4대 준거(정확성, 공신력, 객관성, 공정성)를 암기해요."},
        "step1_2_drill": {"task": "상업 광고 글(체리피킹 주의) vs 국립환경과학원 보고서(공신력 높음) 구분하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "자료를 평가할 때는 글쓴이의 이해관계와 장단점 균형 서술 여부를 확인해야 한다.", "answer": "O", "reason": "비판적 독해의 핵심 준거입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 광고 블로그와 과학 보고서의 차이",
        "situation": "인터넷 포털에서 건강식품이나 제품 추천 글을 볼 때",
        "parent_question": "인터넷에 올라온 추천 글들은 왜 단점은 쏙 빼놓고 좋은 점만 잔뜩 써놓을까?",
        "expected_answer": "물건을 팔아서 돈을 벌려는 '이해관계'가 있어서 그래요! 그래서 공공기관 연구 결과와 비교해 봐야 한대요.",
        "coaching_tip": "인터넷 정보의 이면에 숨은 상업적 의도를 파악하는 디지털 비판력을 길러주세요."
    }
)

# 11. G6-EXP-V3-3
slots_v3["V3-3"] = build_expository_slot(
    grade_num=6,
    subskill_code="V3-3",
    subject="사회(한국 경제 발전 6-1) / 실과(순환경제)",
    unit="3. 자원 순환과 지속 가능한 미래 사회",
    concept="플라스틱 자원순환과 순환 경제 전환 (다중 자료 교차 검증 및 지식 재구성)",
    text_structure="비교·대조 + 문제·해결 복합 재구성",
    structure_type_code="problem_solution",
    passage_title="플라스틱의 두 얼굴: 선형 경제를 넘어 순환 경제로의 대전환",
    paragraphs=[
        "플라스틱은 가볍고 튼튼하며 부식되지 않아 현대 문명을 지탱하는 핵심 소재가 되었습니다. 그러나 한번 만들어진 플라스틱이 자연에서 분해되는 데는 500년 이상이 걸리며, 매년 수천만 톤의 미세플라스틱이 바다로 흘러들어 해양 생태계와 인류의 건강을 위협하고 있습니다. '자원 채취 ➔ 대량 생산 ➔ 소비 ➔ 폐기'로 이어지는 전통적인 '선형 경제(Linear Economy)'는 이제 지속 불가능의 한계에 봉착했습니다.",
        "이러한 한계를 돌파하기 위한 새로운 대안이 '순환 경제(Circular Economy)'입니다. 순환 경제는 제품 설계 단계부터 재활용을 고려하고, 폐기물을 다시 원자재로 투입하여 자원이 무한히 순환하도록 만듭니다. 이를 위해 플라스틱 처리는 단순히 물리적으로 잘게 부수어 녹이는 '기계적 재활용'을 넘어, 분자 단위로 분해하여 새 플라스틱과 똑같은 품질의 원유 상태로 되돌리는 '화학적 재활용' 기술로 진화하고 있습니다.",
        "그런데 플라스틱 재활용 현황 통계를 조사할 때 자료마다 수치가 심하게 충돌하는 현상이 나타납니다. 환경부 공식 자료에는 플라스틱 '재활용률이 약 70%'로 높게 기재되어 있는 반면, 환경 NGO의 심층 조사 보고서에는 '실제 물질 재활용률이 25% 미만'으로 현저히 낮게 나타납니다. 이 수치 충돌의 원인을 교차 검증해 보면, 공식 통계에는 폐플라스틱을 단순히 태워 열을 얻는 '에너지 회수(소각)'까지 재활용 범주에 포함시킨 반면, NGO 보고서는 순수하게 원자재로 다시 태어난 '물질 재활용'만을 기준으로 삼았기 때문입니다.",
        "따라서 진정한 순환 경제를 달성하기 위해서는 겉보기 통계에 안주하지 말고, 일회용 플라스틱 생산 감축, 화학적 재활용 기술 투자, 그리고 다회용기 인프라 구축이라는 종합적인 제도적 재구성이 신속히 추진되어야 합니다."
    ],
    vocab_notes=[
        {"word": "선형 경제", "definition": "자원을 채취하여 상품을 만들고 사용 후 버리는 일방통행식 전통 경제 모델"},
        {"word": "물질 재활용", "definition": "폐기물을 소각하여 열을 얻는 것이 아니라 분쇄·화학 처리를 통해 새로운 물리적 원자재로 다시 제조하는 재활용"}
    ],
    visual_html="""<div class="p-3 bg-amber-50 rounded border border-amber-200">
      <h4 class="font-bold text-amber-900 mb-2">🔄 선형 경제 vs 순환 경제 & 통계 기준 충돌 원인 분석</h4>
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="p-2 bg-white rounded border border-amber-100">
          <strong class="text-amber-800">경제 패러다임 비교</strong>
          <ul class="list-disc pl-4 space-y-0.5 mt-1 text-gray-700">
            <li><strong>선형 경제:</strong> 채취 ➔ 생산 ➔ 소비 ➔ 폐기 (쓰레기 누적)</li>
            <li><strong>순환 경제:</strong> 생산 ➔ 소비 ➔ 회수 ➔ 화학적 재생 (자원 무한 순환)</li>
          </ul>
        </div>
        <div class="p-2 bg-white rounded border border-amber-100">
          <strong class="text-red-800">재활용률 70% vs 25% 수치 충돌 원인</strong>
          <p class="mt-1 text-gray-700">
            공식 통계 70%는 소각 열회수 포함 수치이며, 실제 플라스틱 원자재로 환원된 <strong>물질 재활용률은 25% 미만</strong>임. 기준 차이 교차 검증 필요!
          </p>
        </div>
      </div>
    </div>""",
    hottext_cues=[
        {"cue_id": "g6-v33-c1", "text": "자원 채취 ➔ 대량 생산 ➔ 소비 ➔ 폐기'로 이어지는 전통적인 '선형 경제(Linear Economy)'는 이제 지속 불가능의 한계에 봉착했습니다", "role": "선형 경제의 한계 명시", "para_idx": 0},
        {"cue_id": "g6-v33-c2", "text": "공식 통계에는 폐플라스틱을 단순히 태워 열을 얻는 '에너지 회수(소각)'까지 재활용 범주에 포함시킨 반면, NGO 보고서는 순수하게 원자재로 다시 태어난 '물질 재활용'만을 기준으로 삼았기 때문입니다", "role": "통계 수치 충돌의 근본 원인 규명", "para_idx": 2}
    ],
    graphic_organizer={
        "type": "다중 자료 교차 검증 및 순환 경제 구조도",
        "paradigm_shift": {
            "선형 경제": "채취 ➔ 생산 ➔ 소비 ➔ 폐기",
            "순환 경제": "설계 ➔ 생산 ➔ 소비 ➔ 화학적 재활용 ➔ 원료 재투입"
        },
        "statistical_cross_check": {
            "자료 A (70%)": "기준: 에너지 회수(소각 발전) 포함",
            "자료 B (25%)": "기준: 순수 물질 재활용만 한정",
            "통합 결론": "소각에 의존하지 않는 고부가가치 물질 순환 인프라 필요"
        }
    },
    csat_questions=[
        {
            "q_no": 1,
            "archetype": "다중 자료 통계 충돌 원인 규명",
            "stem": "3문단에서 플라스틱 재활용률 통계(70% vs 25%)가 서로 크게 충돌하는 까닭으로 가장 적절한 것은?",
            "target_para_idx": 2,
            "spotlight_quote": "공식 통계에는 폐플라스틱을 단순히 태워 열을 얻는 '에너지 회수(소각)'까지 재활용 범주에 포함시킨 반면, NGO 보고서는 순수하게 원자재로 다시 태어난 '물질 재활용'만을 기준으로 삼았기 때문입니다.",
            "options": [
                {"label": "①", "text": "공식 통계는 소각을 통한 에너지 회수까지 포함했고, NGO는 실제 원자재 환원인 물질 재활용만 산정했기 때문에", "is_correct": True, "formula": "정답", "explanation": "3문단의 명문화된 통계 기준 차이 분석입니다."},
                {"label": "②", "text": "NGO가 계산기를 잘못 두드려 덧셈을 틀렸기 때문에", "is_correct": False, "formula": "D6", "explanation": "단순 계산 실수가 아닌 조사 기준과 범주의 차이입니다."},
                {"label": "③", "text": "플라스틱이 바다로 흘러가면 무게가 저절로 3배로 불어나기 때문에", "is_correct": False, "formula": "D5", "explanation": "비과학적 허구입니다."},
                {"label": "④", "text": "환경부가 플라스틱 공장을 모두 폐쇄하여 자료가 없기 때문에", "is_correct": False, "formula": "D3", "explanation": "본문과 무관합니다."},
                {"label": "⑤", "text": "국민들이 분리배출을 단 1건도 하지 않아 통계가 거짓이기 때문에", "is_correct": False, "formula": "D1", "explanation": "왜곡된 진술입니다."}
            ]
        },
        {
            "q_no": 2,
            "archetype": "순환 경제 개념 종합 및 대안 추론",
            "stem": "위 글의 2문단과 4문단을 바탕으로 할 때, '순환 경제'를 실현하기 위한 올바른 방향은?",
            "target_para_idx": 1,
            "spotlight_quote": "순환 경제는 제품 설계 단계부터 재활용을 고려하고, 폐기물을 다시 원자재로 투입하여 자원이 무한히 순환하도록 만듭니다.",
            "options": [
                {"label": "①", "text": "화학적 재활용 기술을 고도화하고 제품 설계부터 자원 재투입을 고려해 폐기물을 최소화한다.", "is_correct": True, "formula": "정답", "explanation": "2문단과 4문단의 순환 경제 핵심 원리와 완벽히 일치합니다."},
                {"label": "②", "text": "모든 플라스틱을 그냥 바다에 쏟아붓고 새로 원유를 시추한다.", "is_correct": False, "formula": "D5", "explanation": "선형 경제의 폐해를 극대화하는 행위입니다."},
                {"label": "③", "text": "기계적 재활용도 중단하고 오직 쓰레기를 불태워 공기 중으로 날린다.", "is_correct": False, "formula": "D4", "explanation": "진정한 물질 순환과 거리가 멉니다."},
                {"label": "④", "text": "재활용률 통계를 조작하여 100%로 거짓 발표한다.", "is_correct": False, "formula": "D6", "explanation": "윤리적·제도적 해결책이 아닙니다."},
                {"label": "⑤", "text": "일회용 플라스틱 컵 생산량을 지금보다 100배로 늘린다.", "is_correct": False, "formula": "D1", "explanation": "생산 감축 정책과 정반대입니다."}
            ]
        }
    ],
    ebsr_question={
        "part_a": {
            "stem": "[Part A] 자원을 채취하여 생산·소비하고 버리는 '선형 경제'와 대비되는, 자원을 원자재로 다시 회수하여 순환시키는 모델은?",
            "options": [
                {"label": "①", "text": "순환 경제 (Circular Economy)", "is_correct": True},
                {"label": "②", "text": "선형 경제 (Linear Economy)", "is_correct": False},
                {"label": "③", "text": "절대군주제 경제", "is_correct": False},
                {"label": "④", "text": "석탄 독점 경제", "is_correct": False},
                {"label": "⑤", "text": "일회용 투기 경제", "is_correct": False}
            ]
        },
        "part_b": {
            "stem": "[Part B] 위 판정의 근거가 되는 본문 구절은?",
            "options": [
                {"label": "①", "text": "순환 경제는 제품 설계 단계부터 재활용을 고려하고, 폐기물을 다시 원자재로 투입하여 자원이 무한히 순환하도록 만듭니다.", "is_correct": True},
                {"label": "②", "text": "플라스틱은 가볍고 튼튼하며 부식되지 않아 현대 문명을", "is_correct": False},
                {"label": "③", "text": "그러나 한번 만들어진 플라스틱이 자연에서 분해되는 데는", "is_correct": False},
                {"label": "④", "text": "그런데 플라스틱 재활용 현황 통계를 조사할 때 자료마다", "is_correct": False},
                {"label": "⑤", "text": "따라서 진정한 순환 경제를 달성하기 위해서는 겉보기 통계에", "is_correct": False}
            ]
        }
    },
    writing_workbench={
        "task_title": "순환 경제 및 통계 교차 검증 보고문",
        "guide": "통계 충돌의 원인(소각 열회수 vs 순수 물질 재활용)과 순환 경제 전환 방향을 1문장으로 정리하세요.",
        "template": "재활용률 통계는 소각 열회수 포함 여부에 따라 차이가 나므로, 단순 소각을 넘어 폐플라스틱을 원료로 되돌리는 [화학적 재활용]을 통해 [순환 경제]를 완성해야 한다."
    },
    prescription_clinic={
        "step0_remedial": {"rule": "복수 자료 비교 시 '수치가 다르면 조사 기준(소각 포함 여부)이 다른가?'를 교차 검증해요."},
        "step1_2_drill": {"task": "선형 경제(버림) vs 순환 경제(재투입) 흐름도 화살표 완성하기"},
        "step3_vaccine": {"ox_quiz": [{"statement": "재활용 통계 수치가 다를 때는 조사 기준과 분류 범위를 교차 검증해야 한다.", "answer": "O", "reason": "다중 자료 교차 검증의 핵심 방법입니다."}]}
    },
    parent_table_talk={
        "title": "밥상머리 대화: 플라스틱 분리배출 70%가 진짜 다 재활용될까?",
        "situation": "아파트 분리수거장에서 플라스틱 병을 버릴 때",
        "parent_question": "우리가 이렇게 열심히 플라스틱을 모아 버리면 전부 새 장난감이나 옷으로 만들어질까?",
        "expected_answer": "실제로 다시 플라스틱으로 태어나는 건 25%뿐이고, 나머지는 그냥 태워서 열만 내는 거래요! 그래서 아예 덜 쓰는 게 최고예요.",
        "coaching_tip": "단순 분리수거를 넘어 일회용품 줄이기 실천으로 생각을 확장해 주세요."
    }
)
