# -*- coding: utf-8 -*-
"""
5단원 논설문 (Argumentative, unit5_argumentative) — Batch 1 (1~4차시: 사실적 이해 V1-1 ~ V1-4)
기출간 원문 및 공공기관 공식 통계 100% 수록 (축약·생략 없음)
"""

BATCH1 = [
    # =========================================================================
    # 1차시: G6-ARG-V1-1 (내용 확인)
    # 〈어린이 보호구역 보행 중 스마트폰 사용 제한, 법으로 의무화해야 할까?〉
    # =========================================================================
    {
        "lesson_no": 1,
        "code": "G6-ARG-V1-1",
        "lesson_title": "사회적 쟁점과 논증의 5요소(주장·이유·근거·반론·재반박) 찾기",
        "std_badge": "[6국02-03] [6국01-05] 사실과 의견 구분 · 논증 요소 식별",
        "student_goal": "사회적 찬반 논제를 다룬 논설문을 읽고 사실 진술과 주장 진술을 구분하며, 핵심 주장·이유·근거 자료·예상 반론·재반박 요소를 정확히 찾아 정리할 수 있다.",
        "marking_items": [
            ["mk-double", "핵심 주장", "글쓴이의 당위적 주장(~해야 한다)"],
            ["mk-line-red", "이유", "주장을 뒷받침하는 논리적 까닭"],
            ["mk-line-blue", "근거 자료(사실)", "통계·실험·사례 등 객관적 사실"],
            ["mk-bg", "예상 반론·재반박", "반대 측 우려와 이를 꺾는 논거"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>📖 정독 지문:</strong> 〈어린이 보호구역 내 보행 중 스마트폰 사용 제한, 법과 기술로 의무화해야 할까?〉</span>
          <span><strong>출처:</strong> 『동아일보』·『어린이동아』 시사논설 및 삼성화재 교통안전문화연구소(2025) 공식 통계</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (사실 <span class="mk-line-blue">파란 밑줄</span> · 이유 <span class="mk-line-red">빨간 밑줄</span> · 주장 <span class="mk-double">겹줄</span> 표시하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 날개 질문</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span>등하교 시간 학교 앞 횡단보도를 살펴보면 스마트폰 화면에 고개를 파묻은 채 길을 건너는 어린이들을 쉽게 볼 수 있다. 이처럼 스마트폰에 빠져 주변을 살피지 않고 좀비처럼 걸어 다니는 사람을 ‘스몸비(스마트폰+좀비)’라고 부른다. <span class="mk-line-blue">삼성화재 교통안전문화연구소가 2025년에 발표한 어린이 보행안전 조사에 따르면, 우리나라 초등학생의 54%가 길을 걸으면서 스마트폰을 사용한 경험이 있다고 응답했다.</span> 이 때문에 <span class="mk-highlight">어린이 보호구역 안에서 보행 중 스마트폰 사용을 법과 기술로 제한해야 하는지</span>를 두고 찬반 논란이 일고 있다. <span class="mk-double">어린이의 소중한 생명을 지키기 위해서는 어린이 보호구역과 횡단보도 내 보행 중 스마트폰 사용 제한을 반드시 법과 제도로 의무화해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>1문단에서 사실과 글쓴이의 주장은 어떻게 다를까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>‘~조사에 따르면 54%가 응답했다’는 참·거짓을 확인할 수 있는 <strong>사실(Fact)</strong>이고, ‘~의무화해야 한다’는 글쓴이의 <strong>주장(Claim)</strong>이야.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>찬반이 갈리는 문제(논제)에 대한 글쓴이의 결론이 핵심 주장이구나!</span></div>
                </div>
                <div class="wing-box vocab">
                  <strong>📘 어휘 풀이</strong><br>
                  • <strong>스몸비(Smombie)</strong>: 스마트폰(Smartphone)과 좀비(Zombie)의 합성어.<br>
                  • <strong>의무화(義務化)</strong>: 반드시 따라야 할 의무로 만듦.
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➋</span><span class="mk-line-red">첫째, 걸으면서 스마트폰을 사용하면 시야와 청각 인지 능력이 크게 떨어져 교통사고 위험이 급격히 높아지기 때문이다.</span> <span class="mk-line-blue">실제로 삼성화재 교통안전문화연구소의 실험 결과, 보행 중 스마트폰 화면을 바라보면 평소 120도이던 사람의 시야각이 56%나 좁아지고 전방 주시율도 15%까지 급감하는 것으로 나타났다.</span> <span class="mk-line-blue">또한 이어폰을 끼고 스마트폰을 볼 때 다가오는 자동차 소리를 알아채는 인지 거리는 평소보다 50% 이상 짧아진다.</span> 특히 초등학생은 성인보다 눈높이가 낮아 주차된 차량 사이에서 시야가 더욱 좁아지므로, 보행 중에는 스마트폰 화면 대신 신호등과 자동차를 살피도록 강제할 안전장치를 마련해야 한다.</p>
                <p><span class="p-num">➌</span><span class="mk-line-red">둘째, 어린이의 자율적인 다짐만으로는 스마트폰의 강한 유혹을 이겨 내기 어렵기 때문이다.</span> 많은 어린이가 보행 중 스마트폰 사용이 위험하다는 사실을 머리로는 알고 있지만, 친구의 메시지나 게임 알림이 울리면 무의식중에 화면을 들여다보곤 한다. <span class="mk-line-blue">최근 일부 지방자치단체와 교육청이 일곱 걸음 이상 걸으면 스마트폰 화면이 자동으로 잠기는 보행 안전 앱과 바닥 신호등을 시범 도입한 결과, 어린이들의 보행 중 스마트폰 사용률이 크게 줄어드는 효과를 거두었다.</span> 따라서 개인의 주의에만 맡기지 말고 통학로 내 스마트폰 화면 자동 차단 기술과 사용 제한 규정을 제도적으로 확대해야 한다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 1</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">①</span> 2문단에서 첫째 이유를 증명하기 위해 제시한 <strong>실험 통계 수치</strong> 세 가지를 찾아 빈칸을 채워 보세요.</div>
                  <div style="margin-top:3px;">
                    • 시야각: <span class="blank-slot"><span class="t-ans">56%</span></span> 축소<br>
                    • 전방 주시율: <span class="blank-slot"><span class="t-ans">15%</span></span> 급감<br>
                    • 소리 인지 거리: <span class="blank-slot"><span class="t-ans">50% 이상</span></span> 단축
                  </div>
                </div>
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 2</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">②</span> 3문단에서 글쓴이가 내세운 <strong>둘째 이유</strong>는 무엇인가요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">어린이의 자율적인 다짐만으로는 스마트폰의 유혹을 이겨 내기 어렵기 때문이다.</span></span>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➍</span><span class="mk-bg">물론 보행 중 스마트폰 사용까지 법이나 앱으로 막는 것은 개인의 행동 자유를 지나치게 침해하며, 위급할 때 부모님께 연락하기 어렵다는 반론도 있다.</span> <span class="mk-line-red">그러나 어린이 보행 안전 앱은 걸을 때만 화면을 잠시 잠글 뿐 걸음을 멈추면 즉시 사용할 수 있고, 긴급 통화 기능은 언제나 열려 있으므로 안전과 편의를 모두 지킬 수 있다.</span> 무엇보다 도로 위에서의 작은 자유보다 어린이의 생명과 안전이 비교할 수 없을 만큼 더 소중한 가치이다.</p>
                <p><span class="p-num">➎</span>요약하면, 보행 중 스마트폰 사용은 어린이의 시야와 대처 능력을 빼앗아 심각한 교통사고를 부르는 위험한 습관이다. 잠깐의 편리함이나 재미보다 어린이의 안전과 생명이 무엇보다 우선시되어야 하는 것은 당연하다. <span class="mk-double">그러므로 정부와 학교는 어린이 보호구역 내 보행 중 스마트폰 사용 제한을 의무화하고, 어린이 스스로도 걸을 때 스마트폰을 가방에 넣는 안전한 보행 문화를 실천해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 3</span><span class="role-chip">스스로 You Do</span></div>
                  <div><span class="q-num">③</span> 4문단의 ‘물론 ~ 반론도 있다’는 누구의 의견인가요? 글쓴이는 이를 어떻게 <strong>재반박</strong>했나요?</div>
                  <span class="pencil-line">✏️ 반대 측 의견: <span class="t-ans">개인의 행동 자유 침해 및 위급 시 연락 곤란</span></span>
                  <span class="pencil-line">✏️ 글쓴이의 재반박: <span class="t-ans">멈추면 즉시 사용 가능하고 긴급 통화가 열려 있으며 생명이 우선이다.</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "사실(Fact) 진술과 의견·주장(Claim) 진술 구분하기",
            "tag": "Step 1 사실 vs 주장 식별",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:4px; color:#2C3E50;">
              💡 객관적 자료로 참·거짓을 검증할 수 있는 문장은 <strong>[사실]</strong>, 글쓴이의 생각이나 당위적 요구(<code>~해야 한다</code>)가 담긴 문장은 <strong>[주장/의견]</strong>입니다. 본문 문장을 분류해 봅시다.
            </div>
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:52%;">본문 속 문장</th>
                  <th style="width:18%; text-align:center;">구분 (사실 / 주장)</th>
                  <th style="width:30%;">판단 단서 (서술어·출처 표현)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>① 조사에 따르면 우리나라 초등학생의 54%가 걸으면서 스마트폰을 사용한 경험이 있다고 응답했다.</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">사실 (Fact)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">~조사에 따르면, 54%가 응답했다</span></span></td>
                </tr>
                <tr>
                  <td>② 어린이 보호구역과 횡단보도 내 보행 중 스마트폰 사용 제한을 반드시 의무화해야 한다.</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">주장 (Claim)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">반드시 ~의무화해야 한다</span></span></td>
                </tr>
                <tr>
                  <td>③ 보행 중 스마트폰 화면을 바라보면 시야각이 56%나 좁아지고 전방 주시율도 15%까지 급감한다.</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">사실 (Fact)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">실험 결과, 수치(56%, 15%) 제시</span></span></td>
                </tr>
                <tr>
                  <td>④ 통학로 내 스마트폰 화면 자동 차단 기술과 사용 제한 규정을 제도적으로 확대해야 한다.</td>
                  <td style="text-align:center;"><span class="blank-slot"><span class="t-ans">주장 (Claim)</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">제도적으로 ~확대해야 한다</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 구분한 사실(근거)과 의견(주장·이유·반론·재반박)을 논설문의 5요소 매트릭스로 구조화하기",
        "activity_2": {
            "title": "논설문의 5대 핵심 요소(주장·이유·근거·예상 반론·재반박) 추출 매트릭스",
            "tag": "Step 2 논증 5요소 분류·연결",
            "body_html": """
            <table class="std-table">
              <tbody>
                <tr>
                  <th style="width:22%; background:#FDEDEC; color:#922B21;">⚖️ 사회적 찬반 논제</th>
                  <td colspan="2">어린이 보호구역 내 <span class="blank-slot"><span class="t-ans">보행 중 스마트폰 사용 제한을 법과 기술로 의무화해야 하는가?</span></span></td>
                </tr>
                <tr>
                  <th style="background:#FDEDEC; color:#922B21;">📣 글쓴이의 핵심 주장</th>
                  <td colspan="2"><span class="blank-slot"><span class="t-ans">어린이의 생명을 지키기 위해 어린이 보호구역과 횡단보도 내 보행 중 스마트폰 사용 제한을 의무화해야 한다.</span></span></td>
                </tr>
                <tr>
                  <th style="width:22%;">지지 기둥 구분</th>
                  <th style="width:39%;">논리적 이유 (Reason: 왜냐하면 ~기 때문이다)</th>
                  <th style="width:39%;">객관적 근거 자료 (Evidence: 통계·실험·사례)</th>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">본론 1 (2문단)</td>
                  <td>첫째, 보행 중 스마트폰을 쓰면 <span class="blank-slot"><span class="t-ans">시야와 청각 인지 능력이 떨어져 교통사고 위험이 급격히 높아지기</span></span> 때문이다.</td>
                  <td>[실험 통계] 삼성화재 교통안전문화연구소 실험 결과, 시야각 <span class="blank-slot"><span class="t-ans">56% 축소</span></span>, 전방 주시율 <span class="blank-slot"><span class="t-ans">15% 급감</span></span>, 소리 인지 거리 절반 이하 단축.</td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">본론 2 (3문단)</td>
                  <td>둘째, <span class="blank-slot"><span class="t-ans">어린이의 자율적인 다짐만으로는 스마트폰의 강한 유혹을 이겨 내기 어렵기</span></span> 때문이다.</td>
                  <td>[적용 사례] 지자체·교육청이 <span class="blank-slot"><span class="t-ans">일곱 걸음 화면 자동 잠금 앱과 바닥 신호등</span></span>을 시범 도입하자 사용률이 크게 감소함.</td>
                </tr>
                <tr>
                  <th style="background:#EAFAF1; color:#196F3D;">🛡️ 반대 측 예상 반론<br>(4문단 ‘물론 ~’)</th>
                  <td>개인의 <span class="blank-slot"><span class="t-ans">행동 자유를 침해</span></span>하고 위급할 때 부모님께 연락하기 어렵다.</td>
                  <td><strong>⚔️ 글쓴이의 재반박 (‘그러나 ~’):</strong> <span class="blank-slot"><span class="t-ans">걸음을 멈추면 즉시 사용 가능하고 긴급 통화가 열려 있으며, 작은 자유보다 생명이 더 소중하다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 익힌 5요소 틀을 적용하여 새로운 학교 논제에 대한 나만의 5요소 논증 카드 작성하기",
        "activity_3": {
            "title": "나만의 5요소 논증 카드 작성하기 (전이 실습)",
            "tag": "Step 3 논증 요소 산출",
            "body_html": """
            <div style="font-size:7.4pt; margin-bottom:3px;">
              🎯 <strong>실습 논제:</strong> 「초등학생의 수업 시간 중 스마트 기기(휴대전화) 자율 소지를 제한해야 하는가?」 — 내 입장(찬성 또는 반대)을 정하고 5요소 문장을 완성해 보세요.
            </div>
            <div style="border:0.8pt solid #E6B0AA; background:#FFFDFB; border-radius:5px; padding:5px 8px; font-size:7.4pt;">
              <span class="pencil-line">① 나의 핵심 주장: <span class="t-ans">수업 집중도를 높이고 사이버 폭력을 예방하기 위해 수업 시간 중 휴대전화 소지를 제한해야 한다.</span></span>
              <span class="pencil-line">② 이유와 근거 자료: <span class="t-ans">알림 소리가 학습 흐름을 끊기 때문이다. 실제로 휴대전화를 수거한 학급의 수업 몰입도가 크게 향상되었다는 조사 결과가 있다.</span></span>
              <span class="pencil-line">③ 예상 반론과 재반박: <span class="t-ans">물론 통신의 자유 침해라는 반론도 있으나, 쉬는 시간과 방과 후에 자율 사용을 보장하면 권리와 학습권을 모두 지킬 수 있다.</span></span>
            </div>
            """,
        },
        "writing_seed": {
            "transfer_tag": "12차시(W1 계획)·13차시(W2 생성) 직결",
            "prompt": "오늘 읽은 ‘스몸비 통학로 안전’ 글처럼 우리 학교나 동네에서 찬반 의견이 나뉘는 시급한 문제(쟁점) 1가지를 적어 두세요.",
            "placeholder": "예: 교내 복도 통행 규칙, 어린이 보호구역 전동 킥보드 단속 등",
            "example_answer": "어린이 보호구역 내 개인형 이동장치(전동 킥보드) 통행을 전면 금지해야 한다.",
        },
        "self_check": [
            "통계 수치로 검증 가능한 ‘사실’과 당위적 ‘주장’을 구분했나요?",
            "예상 반론을 글쓴이의 주장과 혼동하지 않고 가려냈나요?",
            "논증 5요소(주장·이유·근거·반론·재반박)를 모두 찾았나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[논제: 스쿨존 보행 중 스마트폰 제한 의무화?] ➔ [핵심 주장(지붕): 법·제도로 의무화해야 한다] ⬅ [기둥1: 시야 56% 축소·전방주시율 15% 급감(삼성화재 교통안전문화연구소 통계)] + [기둥2: 자율 통제 한계·7걸음 잠금 앱 사례] + [방어 기둥: 반론(자유 침해·비상연락) ⚡ 재반박(멈추면 해제·긴급통화 가능·생명 최우선)]",
            "intro_5min": "등하교길에 스마트폰을 보며 걷다가 아찔했던 경험을 나누며 ‘스몸비(Smombie)’ 개념을 도입한다. 단원 관통 질문(EQ)을 함께 읽고, 설득하는 글에서 왜 사실(Fact)과 주장(Claim)을 구분하며 읽어야 하는지 질문을 던진다.",
            "ido_think_aloud_script": "“선생님이 1문단을 읽으며 머릿속 생각을 소리 내어 볼게요. ‘삼성화재 교통안전문화연구소가 2025년에 발표한 조사에 따르면 초등학생의 54%가 걸으면서 스마트폰을 사용한 경험이 있다고 응답했다.’ 이 문장은 실제로 연구소 보고서를 찾아보면 참인지 거짓인지 확인할 수 있죠? 이런 문장을 ‘사실(Fact)’이라고 하고 파란 밑줄을 긋습니다. 반면 마지막 문장 ‘보행 중 스마트폰 사용 제한을 반드시 법과 제도로 의무화해야 한다’는 ‘~해야 한다’라는 당위 표현이 쓰인 글쓴이의 ‘핵심 주장(Claim)’이에요. 여기는 빨간 겹줄을 그어 볼게요!”",
            "wedo_qa_list": [
                {
                    "qar_type": "책 속에 (Right There)",
                    "question": "2문단에서 보행 중 스마트폰을 볼 때 시야각과 전방 주시율이 어떻게 변한다고 했나요?",
                    "expected_ans": "평소 120도이던 시야각이 56% 좁아지고, 전방 주시율도 15%까지 급감한다고 했습니다.",
                    "reprompt": "2문단 두 번째 문장에서 ‘삼성화재 교통안전문화연구소의 실험 결과’ 뒤에 나오는 퍼센트(%) 숫자를 손가락으로 짚어 볼까요?",
                },
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "4문단 첫 문장 ‘개인의 행동 자유를 지나치게 침해한다’는 글쓴이의 주장인가요, 반대 측의 예상 반론인가요?",
                    "expected_ans": "글쓴이의 주장이 아니라, 반대하는 사람들이 내세울 수 있는 ‘예상 반론’입니다.",
                    "reprompt": "문장 맨 앞에 있는 ‘물론 ~라는 반론도 있다’와 그다음 문장의 ‘그러나’에 동그라미를 쳐 보세요. 글쓴이는 ‘물론’ 뒤의 의견에 찬성하고 있나요, ‘그러나’ 뒤에서 반박하고 있나요?",
                },
            ],
            "youdo_and_wrapup": "우측 페이지 [활동 1]~[활동 3]을 스스로 해결하게 하며, 특히 4문단의 예상 반론을 글쓴이의 이유로 잘못 적는 학생이 없는지 순회 점검한다. ‘내 글 씨앗 보관함’에 우리 주변의 찬반 쟁점을 1개 이상 기록하며 마무리한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 물음 정답:</strong> ① 시야각 <code>56%</code> 축소, 전방 주시율 <code>15%</code> 급감, 소리 인지 거리 <code>50% 이상</code> 단축 / ② 어린이의 자율적인 다짐만으로는 스마트폰의 강한 유혹을 이겨 내기 어렵기 때문이다. / ③ 반대 측 예상 반론(행동 자유 침해 및 위급 시 연락 곤란)이며, 걸음을 멈추면 즉시 쓸 수 있고 긴급 통화가 열려 있으며 생명이 우선이라는 점으로 재반박함.<br>
              <strong>• [활동 1] 정답:</strong> ① 사실(<code>~에 따르면, 54% 응답</code>) / ② 주장(<code>~의무화해야 한다</code>) / ③ 사실(<code>실험 결과, 56%·15% 수치</code>) / ④ 주장(<code>~확대해야 한다</code>).<br>
              <strong>• [활동 2] 정답:</strong> 논제(보행 중 스마트폰 사용 제한 의무화 여부), 핵심 주장(스쿨존·횡단보도 보행 중 스마트폰 사용 제한 의무화), 본론1 이유(시야·청각 인지 저하로 교통사고 위험 증가) &amp; 근거(시야각 56% 축소, 전방주시율 15% 급감), 본론2 이유(어린이 자율 다짐의 한계) &amp; 근거(7걸음 화면 자동 잠금 앱 시범 도입 효과), 예상 반론(개인 행동 자유 침해) &amp; 재반박(멈추면 사용 가능·긴급통화 보장·생명 최우선).<br>
              <strong>• [활동 3] 채점 기준:</strong> 핵심 주장, 이유, 근거 자료, 예상 반론, 재반박 5요소가 서로 구별되게 작성되었으면 정답으로 인정함.
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "4문단의 예상 반론(‘개인의 행동 자유를 침해한다’)을 글쓴이의 주장으로 오인함",
                    "diagnosis": "대화적 논증 구조(‘물론 [반론] ~ 그러나 [재반박]’)의 양보·역접 표지 기능을 파악하지 못함",
                    "prescription": "‘물론 ~라는 반론도 있다’를 회색 괄호로 묶어 ‘상대방 목소리’로 표시하게 하고, ‘그러나’ 뒤의 문장이 글쓴이의 진짜 목소리(재반박)임을 대조 지도함",
                },
                {
                    "error_case": "‘이유(Reason)’와 ‘근거 자료(Evidence)’를 구분하지 못하고 섞어 씀",
                    "diagnosis": "논리적 까닭(‘~기 때문이다’)과 이를 입증하는 객관적 데이터(통계·사례)의 위계 차이를 혼동함",
                    "prescription": "‘왜냐하면 ~기 때문이다’로 끝나는 중심 문장은 [이유], ‘실제로 ~조사 결과 ~%로 나타났다’처럼 출처와 수치가 있는 뒷받침 문장은 [근거 자료]로 분리하는 색깔 펜 전략을 적용함",
                },
            ],
            "scaffolding_down": "사실과 주장 구분이 어려운 학습자에게는 문장 끝 서술어 카드(<code>~%로 나타났다[사실]</code> vs <code>~해야 한다[주장]</code>)를 제공하여 서술어 밑줄 긋기부터 시작하도록 안내한다.",
            "scaffolding_up": "본문의 2문단(통계 근거)과 3문단(사례 근거) 중 자신을 더 강하게 설득한 근거가 무엇인지 고르고, 왜 그렇게 생각했는지 2문장으로 비평문을 써 보게 한다.",
            "rubric": {
                "high": "사실과 주장을 100% 구분하고, 논설문의 5대 요소(논제·주장·이유·근거·반론 및 재반박)를 혼동 없이 정확히 추출하여 나만의 5요소 논증 카드까지 완결성 있게 작성함.",
                "mid": "주장과 이유·근거는 찾아내었으나, 본론 4문단의 예상 반론과 재반박 요소를 구분하는 데 부분적인 혼동이 있음.",
                "low": "사실 진술과 주장 진술을 구분하지 못하거나, 이유와 근거 자료를 찾지 못해 교사의 단서 표시 도움이 필요함.",
            },
        },
    },

    # =========================================================================
    # 2차시: G6-ARG-V1-2 (관계 확인)
    # 〈청소년 고카페인 음료 판매와 광고를 규제해야 한다〉
    # =========================================================================
    {
        "lesson_no": 2,
        "code": "G6-ARG-V1-2",
        "lesson_title": "논증·반박 담화표지와 긴 문장의 필수 성분(주·목·서) 골격 관계 확인하기",
        "std_badge": "[6국02-03] [6국04-05] 담화표지 · 문장 성분과 호응 관계",
        "student_goal": "논설문 속 담화표지(‘첫째, 왜냐하면, ~에 따르면, 물론, 그러나’)가 잇는 논증 관계를 파악하고, 긴 겹문장에서 수식어를 덜어내어 필수 문장 성분(주어·목적어·서술어)과 호응 관계를 확인할 수 있다.",
        "marking_items": [
            ["mk-person", "담화표지", "첫째, ~에 따르면, 물론, 그러나, 따라서"],
            ["mk-highlight", "주어·목적어·서술어", "문장의 핵심 뼈대 성분"],
            ["mk-dotted", "(수식어 괄호)", "꾸며 주는 말 덜어내기"],
            ["mk-line-red", "부사어 호응", "왜냐하면~때문이다 / 결코~아니다"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>📖 정독 지문:</strong> 〈청소년 고카페인 음료 판매와 무분별한 광고를 규제해야 한다〉</span>
          <span><strong>출처:</strong> 질병관리청 『2025년 청소년건강행태조사』 · 식품의약품안전처 권고 기준 및 『어린이동아』 시사논설</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (담화표지 <span class="mk-person">파란 테두리</span> · 문장 골격 <span class="mk-highlight">형광펜</span> · 수식어 <span class="mk-dotted">점선</span> 표시하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 날개 질문</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span>요즘 학교 주변 편의점에 가 보면 공부할 때 잠을 쫓아 준다는 이른바 ‘에너지 음료’와 고카페인 커피 우유를 사는 학생들을 흔히 볼 수 있다. <span class="mk-person">질병관리청이 발표한 2025년 청소년건강행태조사에 따르면,</span> 일주일에 3번 이상 고카페인 음료를 마시는 청소년의 비율은 남학생 21.9%, 여학생 21.2%로 10년 전인 2015년의 3.3%에 비해 무려 7배 가까이 급증했다. 현재 법으로 학교 매점 안에서는 고카페인 음료를 팔 수 없지만, 학교 문밖 편의점과 온라인에서는 아무런 제한 없이 판매되고 있다. <span class="mk-person">따라서</span> <span class="mk-highlight">정부와 사회는</span> <span class="mk-dotted">(성장기 어린이와 청소년의 건강을 위협하는)</span> <span class="mk-highlight">고카페인 음료의 판매와 광고를</span> <span class="mk-dotted">(더욱 엄격하게)</span> <span class="mk-highlight">규제해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>1문단 마지막 문장이 길고 복잡한데 핵심 뼈대는 무엇일까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>꾸며 주는 말인 ‘(성장기 ~ 위협하는)’과 ‘(더욱 엄격하게)’를 괄호로 묶어 덜어내 보자.</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span><strong>[주어: 정부와 사회는] + [목적어: 고카페인 음료의 판매와 광고를] + [서술어: 규제해야 한다]</strong>라는 뼈대가 한눈에 보이네!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➋</span><span class="mk-person">첫째,</span> <span class="mk-dotted">(시험 기간에 잠을 깨려고 마시는)</span> <span class="mk-highlight">고카페인 음료의 과도한 섭취는</span> <span class="mk-dotted">(성장기 청소년의 심장 박동을 비정상적으로 빠르게 만들고 극심한 수면 장애를 일으켜)</span> <span class="mk-highlight">청소년의 신체적·정신적 건강을</span> <span class="mk-dotted">(심각하게)</span> <span class="mk-highlight">해치기 때문이다.</span> 식품의약품안전처가 정한 청소년의 하루 카페인 최대 섭취 권고량은 몸무게 1kg당 2.5mg 이하로, 몸무게가 50kg인 학생의 경우 하루 125mg 수준이다. 그러나 시중 편의점에서 파는 고카페인 음료나 대용량 커피는 한 캔에 60mg에서 많게는 150mg이 넘는 카페인이 들어 있어, 하루에 한두 캔만 마셔도 일일 권고량을 훌쩍 넘기게 된다. 카페인을 지나치게 섭취하면 가슴 두근거림과 어지럼증, 불면증이 나타날 뿐 아니라 뼈 성장을 돕는 칼슘과 철분이 몸에 흡수되는 것을 방해하여 키 성장에도 나쁜 영향을 미친다.</p>
                <p><span class="p-num">➌</span><span class="mk-person">둘째,</span> <span class="mk-dotted">(유명 연예인이나 인기 게임 캐릭터를 내세워 집중력을 높여 준다고 유혹하는)</span> <span class="mk-highlight">음료 회사의 과장된 상업 광고는</span> <span class="mk-dotted">(카페인 부작용에 대한 정확한 지식이 부족한)</span> <span class="mk-highlight">어린이들의 올바른 판단력을</span> <span class="mk-dotted">(쉽게)</span> <span class="mk-highlight">흐리게 하기 때문이다.</span> 많은 음료 회사가 고카페인 음료에 ‘에너지’나 ‘집중력 향상’ 같은 그럴듯한 이름을 붙여 마치 성적을 올려 주는 건강음료인 것처럼 홍보하고 있다. <span class="mk-person">왜냐하면</span> <span class="mk-line-red">고카페인 음료는 피로를 진짜로 없애 주는 것이 아니라 뇌의 신경을 일시적으로 각성시켜 피로를 느끼지 못하게 속일 뿐이기 때문이다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 1</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">①</span> 2문단 첫 문장에서 괄호 친 수식어를 덜어내고 <strong>주어·목적어·서술어</strong> 골격을 찾아 적으세요.</div>
                  <span class="pencil-line">• 주어: <span class="t-ans">고카페인 음료의 과도한 섭취는</span></span>
                  <span class="pencil-line">• 목적어: <span class="t-ans">청소년의 신체적·정신적 건강을</span></span>
                  <span class="pencil-line">• 서술어: <span class="t-ans">해치기 때문이다.</span></span>
                </div>
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 2</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">②</span> 3문단 마지막 문장의 부사어 <strong>‘왜냐하면’</strong>은 문장 끝의 어떤 표현과 짝을 이루어 호응하나요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">‘~이기 때문이다’와 짝을 이루어 호응한다.</span></span>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➍</span><span class="mk-person">물론</span> 어떤 음료를 마실지는 학생 개인이 자율적으로 선택할 문제이며 판매까지 막는 것은 지나치다는 반론도 있다. <span class="mk-person">그러나</span> <span class="mk-line-red">중독성이 강하고 건강을 해치는 고카페인 음료로부터 어린이를 보호하는 일은 결코 개인의 책임에만 떠넘길 문제가 아니다.</span> <span class="mk-person">비록</span> <span class="mk-line-red">당장은 음료 회사의 매출이 조금 줄어들지라도,</span> 미래 세대의 건강을 지키는 것이 훨씬 더 중요한 사회적 가치이다.</p>
                <p><span class="p-num">➎</span><span class="mk-person">요약하면,</span> 고카페인 음료 섭취는 청소년의 건강을 해치고, 과장된 상업 광고는 어린이의 판단력을 흐리게 하므로, 정부와 사회는 고카페인 음료의 판매와 광고를 규제해야 한다. 청소년들이 카페인에 의존하지 않고 충분한 수면과 건강한 식습관으로 활력을 찾을 수 있도록, 학교 주변 판매점의 고카페인 주의 문구 표시를 강화하고 청소년 대상 판촉 광고를 제한하는 제도를 조속히 마련해야 한다.</p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 3</span><span class="role-chip">스스로 You Do</span></div>
                  <div><span class="q-num">③</span> 4문단에서 부사어 <strong>‘결코’</strong>와 <strong>‘비록’</strong>은 각각 어떤 서술어 표현과 호응하고 있나요?</div>
                  <span class="pencil-line">• 결코 ➔ <span class="t-ans">~문제가 아니다 (부정 표현)</span></span>
                  <span class="pencil-line">• 비록 ➔ <span class="t-ans">~줄어들지라도 (양보 표현)</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "논증·반박 담화표지가 이어 주는 문장 관계 연결하기",
            "tag": "Step 1 담화표지 관계 추적",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:22%;">본문 속 담화표지</th>
                  <th style="width:33%;">논증 속 역할과 기능</th>
                  <th style="width:45%;">이어 주는 앞뒤 내용 관계</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; color:#1F618D;">① ~에 따르면 (1문단)</td>
                  <td>공신력 있는 <span class="blank-slot"><span class="t-ans">근거 자료 출처</span></span> 제시</td>
                  <td>질병관리청 2025 통계(주 3회 이상 섭취율 21.9%, 7배 급증) 인용</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#1F618D;">② 첫째, / 둘째, (2·3문단)</td>
                  <td>주장을 뒷받침하는 <span class="blank-slot"><span class="t-ans">이유(까닭)</span></span> 나열</td>
                  <td>[이유 1: 청소년 건강 침해] + [이유 2: 과장 광고의 판단력 저해]</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#196F3D;">③ 물론 ~ (4문단)</td>
                  <td>반대 측의 <span class="blank-slot"><span class="t-ans">예상 반론 수용(언급)</span></span></td>
                  <td>“음료 선택은 개인의 자율이며 판매 규제는 지나치다”는 반론 제시</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#B03A2E;">④ 그러나 (4문단)</td>
                  <td>예상 반론을 꺾는 <span class="blank-slot"><span class="t-ans">재반박 전환</span></span></td>
                  <td>중독성 있는 고카페인으로부터 어린이를 보호하는 것은 사회적 책임임</td>
                </tr>
                <tr>
                  <td style="font-weight:800; color:#922B21;">⑤ 따라서 / 요약하면</td>
                  <td>본론 논거 종합 및 <span class="blank-slot"><span class="t-ans">핵심 주장 결론</span></span> 도출</td>
                  <td>정부와 사회는 고카페인 음료 판매와 광고를 엄격히 규제해야 함</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 담화표지 뒤에 오는 긴 겹문장에서 수식어를 덜어내고 필수 문장 성분(주어·목적어·서술어) 골격 뽑아내기",
        "activity_2": {
            "title": "긴 논증 문장의 수식어 소거 및 필수 성분(주어·목적어·서술어) 골격 도해",
            "tag": "Step 2 문장 성분 골격 추출 [6국04-05]",
            "body_html": """
            <div style="font-size:7.3pt; margin-bottom:3px; color:#2C3E50;">
              🔍 꾸며 주는 말(관형어절·부사어절)을 덜어내고 <strong>[누가/무엇이(주어) + 무엇을(목적어) + 어찌하다(서술어)]</strong>의 핵심 골격만 추출하여 5문단 요약문과 연결해 보세요.
            </div>
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:14%;">구분</th>
                  <th style="width:28%;">무엇이/누가 (주어)</th>
                  <th style="width:30%;">무엇을 (목적어)</th>
                  <th style="width:28%;">어찌하다/어떠하다 (서술어)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700; text-align:center;">이유 1 골격<br>(2문단)</td>
                  <td><span class="blank-slot"><span class="t-ans">고카페인 음료의 과도한 섭취는</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">청소년의 신체적·정신적 건강을</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">해치기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">이유 2 골격<br>(3문단)</td>
                  <td><span class="blank-slot"><span class="t-ans">음료 회사의 과장된 상업 광고는</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">어린이들의 올바른 판단력을</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">흐리게 하기 때문이다.</span></span></td>
                </tr>
                <tr style="background:#FDEDEC;">
                  <td style="font-weight:800; text-align:center; color:#922B21;">주장 골격<br>(1·5문단)</td>
                  <td><span class="blank-slot"><span class="t-ans">정부와 사회는</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">고카페인 음료의 판매와 광고를</span></span></td>
                  <td><span class="blank-slot"><span class="t-ans">규제해야 한다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 익힌 문장 성분·부사어 호응 원리([6국04-05])를 적용하여 호응이 어긋난 논증 문장 고쳐 쓰기",
        "activity_3": {
            "title": "문장 성분(주어·서술어, 부사어·서술어) 호응 오류 클리닉",
            "tag": "Step 3 바른 문장 교정 산출 [6국04-05]",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:42%;">❌ 호응이 어긋난 논증 문장</th>
                  <th style="width:20%;">호응 오류 진단</th>
                  <th style="width:38%;">⭕ 바르게 고쳐 쓴 문장</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>① 내가 고카페인 음료 규제를 찬성하는 까닭은 청소년의 수면 장애를 <u>일으킨다.</u></td>
                  <td>주어(<code>까닭은</code>) ↔ 서술어 불일치</td>
                  <td><span class="blank-slot"><span class="t-ans">내가 고카페인 음료 규제를 찬성하는 까닭은 그것이 청소년의 수면 장애를 일으키기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td>② <u>왜냐하면</u> 카페인을 과다 섭취하면 칼슘 흡수를 방해하므로 <u>주의해야 한다.</u></td>
                  <td>부사어(<code>왜냐하면</code>) ↔ 서술어 불일치</td>
                  <td><span class="blank-slot"><span class="t-ans">왜냐하면 카페인을 과다 섭취하면 칼슘 흡수를 방해하기 때문이다.</span></span></td>
                </tr>
                <tr>
                  <td>③ 어린이의 건강을 지키는 일은 <u>결코</u> 가볍게 여길 <u>문제이다.</u></td>
                  <td>부사어(<code>결코</code>) ↔ 부정 서술어 누락</td>
                  <td><span class="blank-slot"><span class="t-ans">어린이의 건강을 지키는 일은 결코 가볍게 여길 문제가 아니다.</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 조직)·16차시(W5 퇴고) 직결",
            "prompt": "내 논설문에서 꼭 사용해 보고 싶은 ‘담화표지 + 부사어 호응 문장 틀’ 1가지를 골라 문장으로 연습해 보세요.",
            "placeholder": "예: 물론 ~라는 반론도 있다. 그러나 이는 결코 ~할 문제가 아니다. 왜냐하면 ~기 때문이다.",
            "example_answer": "물론 전동 킥보드가 편리하다는 의견도 있다. 그러나 어린이의 보행 안전은 결코 편리함과 맞바꿀 수 있는 문제가 아니다.",
        },
        "self_check": [
            "논증·반박 담화표지가 이어 주는 문단 간 관계를 정확히 파악했나요?",
            "긴 문장에서 수식어를 덜어내고 ‘주어+목적어+서술어’ 뼈대를 찾았나요?",
            "‘왜냐하면 ~때문이다’, ‘결코 ~아니다’의 호응 오류를 바르게 고쳤나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[담화표지 이정표: ~에 따르면(출처) ➔ 첫째/둘째(이유) ➔ 물론(반론 수용) ⚡ 그러나(재반박) ➔ 요약하면/따라서(결론)] + [겹문장 뼈대 발골법: (관형어절/부사어절 소거) ➔ 주어 + 목적어 + 서술어] + [6국04-05 필수 호응: 까닭은 ~기 때문이다 / 왜냐하면 ~때문이다 / 결코 ~아니다 / 비록 ~일지라도]",
            "intro_5min": "편의점 에너지 음료나 고카페인 커피 우유를 마셔 본 경험을 이야기 나누며 질병관리청 통계(10년 새 7배 급증)의 심각성을 환기한다. 논설문의 문장이 길고 복잡할 때 어떻게 핵심 의미를 한눈에 파악할 수 있을지 ‘문장 뼈대 찾기’ 전략을 소개한다.",
            "ido_think_aloud_script": "“2문단 첫 문장을 보세요. 무려 세 줄이나 되는 긴 문장이에요! 이럴 때 길을 잃지 않으려면 꾸며 주는 말(수식어)을 괄호로 묶어 덜어내야 해요. ‘(시험 기간에 잠을 깨려고 마시는)’ 괄호! ‘(성장기 청소년의 심장 박동을 ~ 일으켜)’ 괄호! ‘(심각하게)’ 괄호! 자, 이제 남은 뼈대만 읽어 볼까요? ‘고카페인 음료의 과도한 섭취는[주어] 청소년의 신체적·정신적 건강을[목적어] 해치기 때문이다[서술어].’ 어때요? 복잡한 문장의 핵심 뜻이 단번에 드러나죠!”",
            "wedo_qa_list": [
                {
                    "qar_type": "책 속에 (Right There)",
                    "question": "3문단 첫 문장에서 수식어를 모두 덜어내면 남는 주어·목적어·서술어는 무엇인가요?",
                    "expected_ans": "‘음료 회사의 과장된 상업 광고는(주어) 어린이들의 올바른 판단력을(목적어) 흐리게 하기 때문이다(서술어)’입니다.",
                    "reprompt": "‘~유혹하는’과 ‘~지식이 부족한’처럼 뒤에 오는 명사를 꾸며 주는 말을 먼저 괄호로 묶어 볼까요? 그 뒤에 남는 ‘~는’, ‘~을’, ‘~기 때문이다’를 찾아보세요.",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "5문단 첫 문장(‘요약하면 ~’)은 1, 2, 3문단과 어떤 관계가 있나요?",
                    "expected_ans": "2문단의 이유 1 골격, 3문단의 이유 2 골격, 1문단의 주장 골격 세 가지를 하나로 합쳐 놓은 문장입니다!",
                    "reprompt": "[활동 2] 표에 적은 세 줄의 골격 문장과 5문단 첫 문장을 나란히 비교해 보세요. 어떤 놀라운 공통점이 보이나요?",
                },
            ],
            "youdo_and_wrapup": "[활동 2]에서 추출한 주·목·서 골격이 5문단 결론 요약문으로 어떻게 직결되는지 확인하게 한 뒤, [활동 3]의 주술·부사어 호응 오류 3문장을 스스로 교정하도록 지도한다. 이 호응 규칙이 16차시 퇴고의 핵심 기준임을 예고한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 물음 정답:</strong> ① 주어: <code>고카페인 음료의 과도한 섭취는</code> / 목적어: <code>청소년의 신체적·정신적 건강을</code> / 서술어: <code>해치기 때문이다.</code> / ② <code>~이기 때문이다</code>와 호응함. / ③ 결코 ➔ <code>~문제가 아니다</code>, 비록 ➔ <code>~줄어들지라도</code>.<br>
              <strong>• [활동 1] 정답:</strong> ① 근거 자료 출처 / ② 이유(까닭) / ③ 예상 반론 수용 / ④ 재반박 전환 / ⑤ 핵심 주장 결론.<br>
              <strong>• [활동 2] 정답:</strong> 이유 1 골격(<code>고카페인 음료의 과도한 섭취는</code> + <code>청소년의 신체적·정신적 건강을</code> + <code>해치기 때문이다</code>) / 이유 2 골격(<code>음료 회사의 과장된 상업 광고는</code> + <code>어린이들의 올바른 판단력을</code> + <code>흐리게 하기 때문이다</code>) / 주장 골격(<code>정부와 사회는</code> + <code>고카페인 음료의 판매와 광고를</code> + <code>규제해야 한다</code>).<br>
              <strong>• [활동 3] 정답:</strong> ① <code>~찬성하는 까닭은 그것이 청소년의 수면 장애를 일으키기 때문이다.</code> / ② <code>왜냐하면 ~ 칼슘 흡수를 방해하기 때문이다.</code>(또는 ‘왜냐하면’을 삭제) / ③ <code>~ 결코 가볍게 여길 문제가 아니다.</code>
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "안긴문장(관형절) 속의 주어나 목적어를 문장 전체의 주어나 목적어로 잘못 찾음",
                    "diagnosis": "‘(성장기 청소년의 심장 박동을 빠르게 만들고)’ 속의 ‘심장 박동을’을 전체 문장의 목적어로 착각함",
                    "prescription": "문장 맨 끝 서술어(‘해치기 때문이다’)를 먼저 찾고, ‘무엇이 해치는가?(섭취는)’, ‘무엇을 해치는가?(건강을)’라고 서술어 중심 역질문법을 적용하게 함",
                },
                {
                    "error_case": "‘왜냐하면 ~하므로 ~해야 한다’ 문장을 자연스러운 문장으로 여김",
                    "diagnosis": "구어 담화에서 부사어 ‘왜냐하면’을 쓰고 끝을 당위형으로 맺는 습관이 굳어져 있음",
                    "prescription": "‘왜냐하면’과 ‘~기 때문이다’를 자석의 N극과 S극처럼 짝지어 외우게 하고, 문장 끝에 ‘~해야 한다’를 쓰고 싶다면 앞의 ‘왜냐하면’을 지우도록 지도함",
                },
            ],
            "scaffolding_down": "긴 문장 골격 추출이 어려운 학생에게는 서술어(‘해치기 때문이다’, ‘흐리게 하기 때문이다’)를 먼저 찾게 한 뒤, ‘누가/무엇이?’, ‘무엇을?’ 질문 스티커를 붙이며 주어와 목적어를 찾도록 돕는다.",
            "scaffolding_up": "본문 4문단의 ‘물론 ~ 그러나 ~ 비록 ~일지라도’ 구조를 그대로 본떠, 고카페인 음료 규제에 대한 자기만의 재반박 복문 1문장을 새로 지어 보게 한다.",
            "rubric": {
                "high": "담화표지의 논증 기능을 정확히 연결하고, 긴 복문에서 필수 문장 성분(주·목·서) 골격을 100% 추출하며 주술·부사어 호응 오류 3문장을 모두 바르게 교정함.",
                "mid": "담화표지 관계와 문장 골격은 대부분 찾았으나, 부사어 호응 오류 문장을 고쳐 쓸 때 1문장 정도의 어색함이 남음.",
                "low": "긴 문장에서 수식어와 필수 성분을 구분하지 못하거나 주술·부사어 호응 오류 지점을 찾지 못함.",
            },
        },
    },

    # =========================================================================
    # 3차시: G6-ARG-V1-3 (구조 확인)
    # 〈학교 급식 잔반 줄이기, ‘자율 선택 급식’ 도입으로 해결하자〉
    # =========================================================================
    {
        "lesson_no": 3,
        "code": "G6-ARG-V1-3",
        "lesson_title": "서론-본론(지지 기둥 & 반론·재반박 기둥)-결론 심화 3단 논증 구조 도해하기",
        "std_badge": "[6국02-03] [6국03-04] 논설문 거시·미시 구조 도해",
        "student_goal": "예상 반론과 재반박이 포함된 5문단 논설문을 읽고, ‘서론(문제 제기·주장) - 본론(이유+근거 지지 기둥 & 반론+재반박 방어 기둥) - 결론(요약·전망)’의 심화 3단 논증 피라미드 구조도를 완성할 수 있다.",
        "marking_items": [
            ["mk-double", "서론·결론 주장", "핵심 주장 천명 및 재강조"],
            ["mk-line-red", "본론 지지 기둥", "이유 1·2와 중심 문장"],
            ["mk-line-blue", "근거 주춧돌", "통계·학교 사례·전문가 인용"],
            ["mk-bg", "대화적 방어 기둥", "예상 반론 수용 + 재반박 논거"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>📖 정독 지문:</strong> 〈학교 급식 잔반 줄이기, ‘자율 선택 급식’ 도입으로 해결하자〉</span>
          <span><strong>출처:</strong> 경기도교육청 『자율선택급식 성과 분석 보고서』(2023~2025) 및 『대한급식신문』</span>
        </div>

        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>본문 정독 (서론-본론-결론 3단 경계를 나누고 각 기둥의 역할 표시하며 읽기)</th>
              <th class="wing-head">🧠 사고구술 &amp; 날개 질문</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➊</span><strong>[서론]</strong> 매일 점심시간이 끝날 무렵이면 학교 급식실 퇴식구 앞에는 먹지 않고 버려지는 반찬과 밥이 산더미처럼 쌓인다. 환경부와 교육 당국의 조사에 따르면, 전국 학교 급식실에서 발생하는 음식물 쓰레기는 한 해 수십만 톤에 이르며 이를 처리하는 데에만 매년 천문학적인 비용이 쓰이고 있다. 그동안 많은 학교에서 ‘수요일은 다 먹는 날(수다날)’이나 칭찬 스티커 제도를 운영해 왔지만, 일률적으로 똑같은 양을 퍼 주는 배식 방식에서는 잔반을 근본적으로 줄이기 어려웠다. <span class="mk-double">따라서 학교 급식의 음식물 쓰레기 문제를 해결하고 학생들의 올바른 식습관을 기르기 위해, 학생이 자신의 식사량과 기호에 맞게 음식을 덜어 먹는 ‘자율 선택 급식’을 전면 도입해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box guide u5">
                  <div class="wing-box-title"><span>🎙️ 선생님 사고구술</span><span class="role-chip">시범 I Do</span></div>
                  <div class="think-row"><span class="think-tag">[질문]</span><span>서론(1문단)은 어떤 순서로 독자의 관심을 끌고 주장을 펼칠까?</span></div>
                  <div class="think-row"><span class="think-tag">[단서]</span><span>①급식실 잔반이 쌓이는 <strong>문제 상황</strong> 제시 ➔ ②기존 정량 배식의 <strong>한계</strong> 지적 ➔ ③‘자율 선택 급식을 도입해야 한다’는 <strong>핵심 주장</strong> 천명!</span></div>
                  <div class="think-row"><span class="think-tag">[정리]</span><span>서론의 3단계 공식(문제 제기 ➔ 논제·한계 ➔ 주장)이 뚜렷하구나!</span></div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➋</span><strong>[본론 1]</strong> <span class="mk-line-red">첫째, 자율 선택 급식을 시행하면 학생들이 자신이 먹을 수 있는 만큼만 음식을 덜어 가므로 버려지는 음식물 쓰레기와 환경오염을 크게 줄일 수 있기 때문이다.</span> 기존의 정량 배식에서는 평소 양이 적거나 특정 음식을 먹지 못하는 학생에게도 똑같은 양을 나누어 주어 먹기도 전에 버려지는 음식이 많았다. <span class="mk-line-blue">실제로 경기도교육청이 자율 선택 급식을 도입한 학교들을 분석한 성과 보고서에 따르면, 자율 배식을 시행한 학교는 일반 배식 학교보다 학생 1인당 잔반 발생량이 평균 27%에서 최대 82%까지 감소한 것으로 나타났다.</span> 잔반이 줄어들면 처리 비용을 아낄 수 있을 뿐만 아니라, 쓰레기를 처리할 때 발생하는 온실가스까지 줄여 지구 환경을 보호할 수 있다.</p>
                <p><span class="p-num">➌</span><strong>[본론 2]</strong> <span class="mk-line-red">둘째, 학생 스스로 음식을 선택하고 책임지는 과정을 통해 자기주도적인 식습관을 기르고 민주적인 학교 문화를 만들 수 있기 때문이다.</span> <span class="mk-line-blue">실제로 자율 선택 급식과 샐러드바를 도입한 경기도의 한 시범 초등학교 사례를 보면, 학생 스스로 먹을 양을 결정하게 한 뒤로 ‘내가 담은 음식은 끝까지 다 먹는다’는 책임감이 생겨 급식 만족도가 94%로 높아졌고 채소 섭취량도 이전보다 뚜렷하게 늘어났다.</span> <span class="mk-line-blue">식품영양학 전문가인 김정현 교수 또한 “자율 선택 급식은 단순히 밥을 퍼 주는 방식을 바꾸는 것을 넘어, 학생이 자신의 몸 상태와 영양 균형을 스스로 생각하며 식생활의 주체로 성장하게 돕는 살아 있는 교육 과정이다.”라고 강조하였다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 1</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">①</span> 본론 1(2문단)과 본론 2(3문단)의 주춧돌 역할을 하는 <strong>근거 자료의 종류</strong>를 연결해 보세요.</div>
                  <div style="margin-top:3px;">
                    • 2문단 근거: <span class="blank-slot"><span class="t-ans">공식 통계 자료 (잔반 27~82% 감소)</span></span><br>
                    • 3문단 근거: <span class="blank-slot"><span class="t-ans">시범 학교 사례(만족도 94%) 및 전문가 견해</span></span>
                  </div>
                </div>
              </td>
            </tr>
            <tr>
              <td class="text-col">
                <p><span class="p-num">➍</span><strong>[본론 3]</strong> <span class="mk-bg">물론 자율 선택 급식을 도입하면 학생들이 좋아하는 고기 반찬만 골라 담아 영양 불균형이 생기고, 배식 시간이 길어져 조리 종사자분들의 업무 부담이 커진다는 우려도 있다.</span> <span class="mk-line-red">그러나 이러한 문제는 사전 영양 교육과 배식대 환경 개선으로 충분히 해결할 수 있다.</span> 시범 운영 학교들처럼 필수 영양군 반찬은 기본 최소량을 담도록 안내하고 자율 배식대를 두 곳으로 늘리면, 영양 균형을 지키면서도 배식 시간을 오히려 단축할 수 있기 때문이다.</p>
                <p><span class="p-num">➎</span><strong>[결론]</strong> 요약하면, 자율 선택 급식은 음식물 쓰레기를 획기적으로 줄여 환경을 살리고, 학생들의 건강한 식습관과 자율적인 책임감을 키워 주는 일석이조의 제도이다. 이제 학교 급식실은 단순히 배를 채우는 곳이 아니라 환경 사랑과 자율성을 배우는 교육의 장이 되어야 한다. <span class="mk-double">그러므로 교육청과 일선 학교는 급식실 인력과 시설을 적극적으로 지원하여 ‘자율 선택 급식’을 하루빨리 확대 시행해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 2</span><span class="role-chip">스스로 You Do</span></div>
                  <div><span class="q-num">②</span> 본론 3(4문단)은 앞선 2·3문단과 달리 어떤 특별한 역할을 하는 기둥인가요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">반대 측의 예상 반론(영양 불균형·배식 시간 지연)을 먼저 수용한 뒤 해결 대안으로 재반박하여 주장을 방어하는 기둥이다.</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "문단별 중심 내용과 논증 기능 파악하기",
            "tag": "Step 1 문단별 기능 식별",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:16%;">3단 구성</th>
                  <th style="width:14%;">문단</th>
                  <th style="width:32%;">문단의 논증 기능</th>
                  <th style="width:38%;">문단 중심 내용 간추리기</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#FDEDEC;">서론</td>
                  <td style="text-align:center;">1문단</td>
                  <td>문제 상황 제기 ➔ <span class="blank-slot"><span class="t-ans">핵심 주장 제시</span></span></td>
                  <td>학교 급식 잔반 문제를 해결하기 위해 ‘자율 선택 급식’을 도입해야 함.</td>
                </tr>
                <tr>
                  <td rowspan="3" style="font-weight:800; text-align:center; background:#FEF9E7;">본론</td>
                  <td style="text-align:center;">2문단</td>
                  <td>지지 기둥 1 (<span class="blank-slot"><span class="t-ans">첫째 이유 + 통계 근거</span></span>)</td>
                  <td>먹을 만큼만 덜어 가므로 잔반(27~82% 감소)과 환경오염을 줄일 수 있음.</td>
                </tr>
                <tr>
                  <td style="text-align:center;">3문단</td>
                  <td>지지 기둥 2 (<span class="blank-slot"><span class="t-ans">둘째 이유 + 사례·전문가 근거</span></span>)</td>
                  <td>자기주도적 식습관과 책임감을 기르고 급식 만족도(94%)를 높일 수 있음.</td>
                </tr>
                <tr>
                  <td style="text-align:center;">4문단</td>
                  <td>방어 기둥 (<span class="blank-slot"><span class="t-ans">예상 반론 수용 + 재반박</span></span>)</td>
                  <td>영양 불균형과 배식 시간 우려는 영양 교육과 배식대 확충으로 해결 가능함.</td>
                </tr>
                <tr>
                  <td style="font-weight:800; text-align:center; background:#EAFAF1;">결론</td>
                  <td style="text-align:center;">5문단</td>
                  <td>핵심 논거 요약 ➔ <span class="blank-slot"><span class="t-ans">전망 제시 및 실천 당부</span></span></td>
                  <td>환경과 자율성을 살리는 자율 선택 급식을 적극 지원하여 확대 시행해야 함.</td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]의 문단별 기능을 조립하여 ‘지붕(주장) - 기둥(이유·반론·재반박) - 주춧돌(근거)’ 심화 논증 구조도 완성하기",
        "activity_2": {
            "title": "6학년 심화 3단 논증 피라미드(파르테논 신전) 구조 도해조직자",
            "tag": "Step 2 거시·미시 논증 구조 도해",
            "body_html": """
            <div style="border:1pt solid #922B21; border-radius:6px; padding:6px; background:#FFFDFB; font-size:7.3pt;">
              <!-- 지붕: 서론 & 핵심 주장 -->
              <div style="background:#922B21; color:#fff; padding:4px 8px; border-radius:4px; text-align:center; font-weight:800; margin-bottom:5px;">
                🏛️ [서론 · 지붕 (핵심 주장)] 학교 급식 잔반 문제를 해결하고 올바른 식습관을 기르기 위해 <span class="blank-slot" style="background:#fff;"><span class="t-ans">‘자율 선택 급식’을 전면 도입해야 한다.</span></span>
              </div>
              <!-- 3대 기둥: 지지 기둥 1, 지지 기둥 2, 방어 기둥 3 -->
              <div style="display:grid; grid-template-columns:1fr 1fr 1.1fr; gap:5px; margin-bottom:5px;">
                <div style="border:0.9pt solid #2980B9; border-radius:4px; padding:4px 6px; background:#EBF5FB;">
                  <div style="font-weight:800; color:#1B4F72; border-bottom:0.6pt solid #7FB3D5; margin-bottom:2px;">🧱 [본론 1 · 지지 기둥 ①]</div>
                  <div><strong>• 첫째 이유:</strong> <span class="blank-slot"><span class="t-ans">음식물 쓰레기와 환경오염 감소</span></span></div>
                  <div style="margin-top:2px;"><strong>• 주춧돌 근거(통계):</strong> 경기도교육청 보고서 결과 1인당 잔반량 <span class="blank-slot"><span class="t-ans">평균 27%~최대 82% 감소</span></span></div>
                </div>
                <div style="border:0.9pt solid #2980B9; border-radius:4px; padding:4px 6px; background:#EBF5FB;">
                  <div style="font-weight:800; color:#1B4F72; border-bottom:0.6pt solid #7FB3D5; margin-bottom:2px;">🧱 [본론 2 · 지지 기둥 ②]</div>
                  <div><strong>• 둘째 이유:</strong> <span class="blank-slot"><span class="t-ans">자기주도적 식습관 및 민주적 문화 형성</span></span></div>
                  <div style="margin-top:2px;"><strong>• 주춧돌 근거(사례·전문가):</strong> 시범 초교 급식 만족도 <span class="blank-slot"><span class="t-ans">94%</span></span> 및 김정현 교수 인터뷰 인용</div>
                </div>
                <div style="border:0.9pt solid #1E8449; border-radius:4px; padding:4px 6px; background:#EAFAF1;">
                  <div style="font-weight:800; color:#145A32; border-bottom:0.6pt solid #82E0AA; margin-bottom:2px;">🛡️ [본론 3 · 대화적 방어 기둥]</div>
                  <div><strong>• 예상 반론:</strong> <span class="blank-slot"><span class="t-ans">영양 불균형 및 배식 시간·업무 부담 증가</span></span></div>
                  <div style="margin-top:2px;"><strong>• 재반박 대안:</strong> <span class="blank-slot"><span class="t-ans">필수 영양군 최소량 안내(영양 교육) 및 자율 배식대 확충으로 해결 가능</span></span></div>
                </div>
              </div>
              <!-- 주춧돌 바닥: 결론 -->
              <div style="background:#2C3E50; color:#fff; padding:4px 8px; border-radius:4px; text-align:center; font-weight:700;">
                🏁 [결론 · 토대 (요약 및 당부)] 일석이조의 교육 과정인 자율 선택 급식이 확대되도록 <span class="blank-slot" style="background:#fff;"><span class="t-ans">교육청과 학교가 인력과 시설을 적극 지원해야 한다.</span></span>
              </div>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]의 파르테논 신전 구조도를 내 글의 개요 설계 틀로 미러링하여 3단 논증 기둥 세우기",
        "activity_3": {
            "title": "내 논설문 주제에 맞춰 3대 기둥(지지 기둥 2개 + 방어 기둥 1개) 미니 설계하기",
            "tag": "Step 3 논증 구조 설계 전이",
            "body_html": """
            <div style="font-size:7.3pt; margin-bottom:2px;">
              🏗️ <strong>논제 예시:</strong> 「우리 학교에 ‘책가방 없는 날(자율 체험 학습의 날)’을 매달 운영해야 한다」 (또는 자유 논제)
            </div>
            <span class="pencil-line">• [지지 기둥 1 &amp; 2]: <span class="t-ans">첫째, 학업 스트레스를 줄이고 창의적 협동심을 기를 수 있다. 둘째, 교실 밖 살아 있는 진로·생태 체험이 가능하다.</span></span>
            <span class="pencil-line">• [방어 기둥 (반론 ⚡ 재반박)]: <span class="t-ans">물론 수업 진도가 늦어진다는 우려도 있으나, 교과 연계 프로젝트 활동으로 구성하면 학습 결손 없이 깊이 있는 배움이 가능하다.</span></span>
            """,
        },
        "writing_seed": {
            "transfer_tag": "14차시(W3 내용 조직하기) 1:1 미러링",
            "prompt": "오늘 완성한 ‘지붕(주장) - 지지 기둥 1·2 - 방어 기둥(반론·재반박) - 토대(결론)’ 구조도는 14차시 내 논설문 개요표가 됩니다. 가장 설득력 있었던 근거 유형(통계/사례/전문가)을 메모하세요.",
            "placeholder": "예: 구체적인 퍼센트(%) 통계와 실제 시범 학교 사례를 함께 쓰니 설득력이 2배가 되었다.",
            "example_answer": "경기도교육청의 잔반 27~82% 감소 통계와 시범 초등학교 만족도 94% 사례처럼 통계와 사례를 결합하는 전략을 쓰겠다.",
        },
        "self_check": [
            "서론-본론-결론 3단 구성의 문단 경계와 역할을 정확히 나누었나요?",
            "본론의 지지 기둥(이유+근거)과 방어 기둥(반론+재반박)을 구조도로 완성했나요?",
            "통계·사례·전문가 견해 근거가 각각 어떤 이유를 떠받치는지 연결했나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[파르테논 신전 논증 구조도] 🏛️ 지붕(서론 1문단: 문제 제기 ➔ 자율 선택 급식 도입 주장) / 🧱 기둥 1(2문단: 잔반·환경오염 감소 ⬅ 경기도교육청 잔반 27~82% 감소 통계) / 🧱 기둥 2(3문단: 자기주도 식습관·만족도 ⬅ 시범초 만족도 94% 사례 + 김정현 교수 인용) / 🛡️ 방어 기둥 3(4문단: 영양 불균형·배식 지연 반론 ⚡ 필수 영양군 안내·배식대 확충 재반박) / 🏁 토대(결론 5문단: 요약 및 인력·시설 지원 당부)",
            "intro_5min": "오늘 점심 급식에서 반찬을 남긴 적이 있는지 이야기 나누며 학교 급식 잔반 문제를 떠올리게 한다. 5학년 때 배운 기본 3단 구성(서론-본론-결론)에서 한 걸음 더 나아가, 6학년 논설문에는 왜 ‘반론·재반박 방어 기둥’이 추가되는지 파르테논 신전 비유로 안내한다.",
            "ido_think_aloud_script": "“논설문은 지붕을 떠받치는 신전 건축물과 같아요. 지붕이 ‘핵심 주장’이라면, 그 지붕이 무너지지 않게 받쳐 주는 기둥들이 바로 본론의 ‘이유와 근거’예요. 그런데 만약 반대하는 사람이 와서 기둥을 흔들면 어떡하죠? 그래서 4문단처럼 상대방의 반론(‘영양 불균형이 생기고 배식 시간이 길어진다’)을 미리 받아들인 뒤, 해결 대안으로 튼튼하게 막아 내는 ‘방어 기둥(대화적 논증 기둥)’을 세워 주는 거랍니다!”",
            "wedo_qa_list": [
                {
                    "qar_type": "책 속에 (Right There)",
                    "question": "3문단에서는 둘째 이유를 뒷받침하기 위해 어떤 두 가지 종류의 근거 자료를 사용했나요?",
                    "expected_ans": "경기도 시범 초등학교의 실제 사례(급식 만족도 94%)와 식품영양학 전문가 김정현 교수의 인터뷰 견해를 함께 사용했습니다.",
                    "reprompt": "3문단에서 ‘실제로 ~ 초등학교 사례를 보면’이 시작하는 문장과, ‘식품영양학 전문가인 김정현 교수 또한’이 시작하는 문장을 각각 찾아볼까요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "서론(1문단)의 핵심 주장과 결론(5문단)의 마지막 문장은 어떻게 닮았고 어떻게 다른가요?",
                    "expected_ans": "둘 다 ‘자율 선택 급식을 도입(확대)해야 한다’는 같은 주장을 담고 있지만, 결론에서는 교육청과 학교가 ‘조리 인력과 시설을 적극 지원하라’는 구체적인 실천 당부까지 덧붙였습니다.",
                    "reprompt": "1문단 마지막 문장과 5문단 마지막 문장의 밑줄 친 겹줄 부분을 나란히 읽어 보세요. 5문단에 새로 추가된 실천 방법이 무엇인가요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 우측 페이지 [활동 2]의 파르테논 신전 구조 도해조직자를 빈틈없이 완성하도록 순회 지도한다. 이 도해조직자가 14차시(W3 내용 조직하기)의 개요 틀과 1:1로 똑같음을 강조하며 씨앗 보관함을 작성하게 한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 물음 정답:</strong> ① 2문단: 공식 통계 자료(잔반 27~82% 감소), 3문단: 시범 학교 사례(만족도 94%) 및 전문가 견해(김정현 교수) / ② 반대 측 예상 반론을 먼저 수용하고 대안으로 재반박하여 주장을 방어하는 기둥.<br>
              <strong>• [활동 1] 정답:</strong> 1문단(핵심 주장 제시) / 2문단(첫째 이유 + 통계 근거) / 3문단(둘째 이유 + 사례·전문가 근거) / 4문단(예상 반론 수용 + 재반박) / 5문단(전망 제시 및 실천 당부).<br>
              <strong>• [활동 2] 정답:</strong> 지붕(<code>‘자율 선택 급식’을 전면 도입해야 한다</code>) / 기둥① 이유(<code>음식물 쓰레기와 환경오염 감소</code>), 근거(<code>평균 27%~최대 82% 감소</code>) / 기둥② 이유(<code>자기주도적 식습관 및 민주적 문화 형성</code>), 근거(<code>94%</code>) / 방어 기둥 예상 반론(<code>영양 불균형 및 배식 시간·업무 부담 증가</code>), 재반박(<code>필수 영양군 최소량 안내 및 자율 배식대 확충</code>) / 결론 토대(<code>교육청과 학교가 인력과 시설을 적극 지원해야 한다</code>).
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "본론 3(4문단)을 ‘셋째 이유’로 잘못 분류함",
                    "diagnosis": "지지 기둥(이유 1·2)과 대화적 방어 기둥(예상 반론+재반박)의 구조적 차이를 구별하지 못함",
                    "prescription": "4문단 첫머리가 ‘셋째,’가 아니라 ‘물론 ~라는 우려도 있다. 그러나 ~’로 시작함을 확인시켜 ‘공격(지지) 기둥’과 ‘방패(방어) 기둥’의 역할 차이를 시각적으로 구분하게 함",
                },
                {
                    "error_case": "서론의 ‘문제 상황’을 글쓴이의 ‘이유’ 칸에 적음",
                    "diagnosis": "서론에서 화제를 꺼내기 위해 제시한 급식 잔반 실태와 본론의 논리적 이유를 혼동함",
                    "prescription": "서론의 실태는 ‘왜 지금 이 문제를 이야기하는가(배경)’이고, 본론의 이유는 ‘왜 자율 선택 급식이 해답인가(효과)’임을 대비하여 설명함",
                },
            ],
            "scaffolding_down": "구조도 작성이 막막한 학생에게는 본문에서 이미 밑줄 친 빨간 줄(이유), 파란 줄(근거), 초록 상자(반론)를 구조도 같은 색깔 칸에 그대로 옮겨 적는 색깔 매칭법을 안내한다.",
            "scaffolding_up": "본문 3문단처럼 하나의 이유 뒤에 ‘실제 사례’와 ‘전문가 인용’ 두 가지 근거를 연속으로 배치했을 때 독자에게 주는 설득 효과가 무엇인지 분석해 보게 한다.",
            "rubric": {
                "high": "5문단 논설문의 서론-본론(지지 기둥 1·2 + 방어 기둥)-결론 구조를 100% 정확하게 도해조직자로 시각화하고, 자신의 논제에 맞는 3대 기둥을 체계적으로 설계함.",
                "mid": "서론-본론-결론의 큰 틀과 이유·근거는 도해했으나, 방어 기둥의 예상 반론과 재반박 대안을 요약하는 데 일부 누락이 있음.",
                "low": "문단별 중심 내용과 서론-본론-결론의 구조적 위계를 연결하지 못해 도해조직자 완성에 도움이 필요함.",
            },
        },
    },

    # =========================================================================
    # 4차시: G6-ARG-V1-4 (요약 및 주제 확인)
    # 3차시 〈자율 선택 급식〉 심화 + 〈공정 무역 제품을 사용합시다〉 비교 요약 및 설득적 제목 붙이기
    # =========================================================================
    {
        "lesson_no": 4,
        "code": "G6-ARG-V1-4",
        "lesson_title": "세부 통계·사례를 덜어내어 압축 요약하고 설득적 제목 붙이기",
        "std_badge": "[6국02-02] [6국02-03] 논설문 거시 요약 · 설득적 제목 생성",
        "student_goal": "논설문에서 세부 통계 수치와 사례 수식어를 덜어내고 ‘핵심 주장 + 이유 1·2 + 반론 재반박 골격’을 결합하여 1~2문장으로 압축 요약한 뒤, 독자의 행동을 촉구하는 설득적 제목을 붙일 수 있다.",
        "marking_items": [
            ["mk-dotted", "(삭제할 세부 사례·수치)", "요약할 때 덜어낼 뒷받침 자료"],
            ["mk-double", "핵심 주장 골격", "요약문에 꼭 넣을 결론 명제"],
            ["mk-line-red", "이유·재반박 골격", "요약문에 결합할 핵심 논거"],
        ],
        "left_page_body_html": """
        <div style="font-size:7.5pt; color:#566573; margin-bottom:4px; display:flex; justify-content:space-between;">
          <span><strong>📖 부분 자세히 읽기 &amp; 비교 정독:</strong> (가) 〈자율 선택 급식〉 핵심 요약 훈련 + (나) 〈공정 무역 제품을 사용합시다〉</span>
          <span><strong>출처:</strong> 경기도교육청 보고서 &amp; 2015 개정 초등 『국어 6-2』 수록 논설문 원문</span>
        </div>

        <!-- (가) 3차시 글의 세부 삭제 & 골격 추출 시범 박스 -->
        <div class="inline-segment-box">
          <div style="font-family:var(--font-sans); font-size:7.6pt; font-weight:800; color:#922B21; margin-bottom:3px;">
            🔎 [글 (가) 요약 시범] 3차시 〈학교 급식 잔반 줄이기, ‘자율 선택 급식’ 도입으로 해결하자〉에서 세부 사례·수치 덜어내기
          </div>
          <p>• <strong>[서론 골격]</strong> <span class="mk-dotted">(매일 점심시간 퇴식구에 반찬이 쌓이고 한 해 수십만 톤의 쓰레기 처리 비용이 드는데,)</span> <span class="mk-double">학교 급식 잔반 문제를 해결하기 위해 ‘자율 선택 급식’을 도입해야 한다.</span></p>
          <p>• <strong>[본론 1·2 골격]</strong> 첫째, <span class="mk-line-red">먹을 만큼만 덜어 가므로 음식물 쓰레기와 환경오염을 줄일 수 있고</span> <span class="mk-dotted">(경기도교육청 통계 잔반 27~82% 감소 삭제)</span>, 둘째, <span class="mk-line-red">스스로 선택하며 자기주도적인 식습관을 기를 수 있기 때문이다.</span> <span class="mk-dotted">(시범 초교 만족도 94%, 김정현 교수 인터뷰 삭제)</span></p>
          <p>• <strong>[본론 3 골격]</strong> <span class="mk-line-red">물론 영양 불균형과 배식 지연 우려도 있으나, 영양 교육과 배식대 확충으로 해결할 수 있다.</span></p>
        </div>

        <div class="inline-bridge-box model">
          <div style="font-weight:800; color:#C85A17;">🎙️ 선생님 요약 시범<br><span class="role-chip">I Do 압축 공식</span></div>
          <div>
            <strong>[논설문 1~2문장 압축 요약 공식]:</strong> <code>[반론 수용] + [재반박] + [이유 1·2 골격] + [핵심 주장]</code><br>
            ➔ “자율 선택 급식은 영양 불균형 등의 우려도 있으나 영양 교육과 시설 보완으로 해결할 수 있으며, 음식물 쓰레기를 줄이고 자기주도적 식습관을 길러 주므로 적극 도입해야 한다.”
          </div>
        </div>

        <!-- (나) 2015 개정 초6-2 국어 교과서 『공정 무역 제품을 사용합시다』 원문 -->
        <table class="wing-reading-table">
          <thead>
            <tr>
              <th>📖 [글 (나) 스스로 요약하고 제목 붙이기] (제목을 가린 논설문 전문)</th>
              <th class="wing-head">🧠 날개 질문 &amp; 제목 짓기</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="text-col">
                <div style="background:#F2F4F4; border:1pt dashed #922B21; padding:3px 7px; border-radius:4px; font-family:var(--font-sans); font-size:8pt; font-weight:800; margin-bottom:4px;">
                  🏷️ 내가 붙인 설득적 제목: <span class="blank-slot" style="min-width:210px;"><span class="t-ans">정당한 땀의 대가를 지키는 약속, 공정 무역 제품을 사용합시다</span></span>
                </div>
                <p><span class="p-num">➊</span><span class="mk-dotted">(우리가 즐겨 먹는 달콤한 초콜릿의 원료인 카카오는 주로 서아프리카나 라틴아메리카 등 개발 도상국에서 생산된다. 그러나 정작 카카오 농장에서 일하는 어린이와 농부들은 하루 종일 일하고도 초콜릿 한 개 값에도 못 미치는 적은 임금을 받으며 가난에서 벗어나지 못하고 있다.)</span> 이처럼 불공정한 무역 구조로 고통받는 생산자들에게 정당한 대가를 지불하자는 운동이 바로 ‘공정 무역’이다. <span class="mk-double">지구촌 이웃의 인권을 보호하고 지속 가능한 세상을 만들기 위해 우리는 공정 무역 제품을 적극적으로 사용해야 한다.</span></p>
                <p><span class="p-num">➋</span><span class="mk-line-red">첫째, 공정 무역 제품을 사용하면 개발 도상국 생산자들이 정당한 노동의 대가를 받아 경제적으로 자립할 수 있기 때문이다.</span> <span class="mk-dotted">(일반 무역에서는 거대 다국적 기업과 중간 상인이 이익의 90% 이상을 가져가고 농부에게는 판매 가격의 5% 남짓만 돌아간다. 반면)</span> 공정 무역은 생산자에게 최저 가격을 보장해 주고 지역 사회 발전 기금까지 지원하여 농부들이 빈곤에서 벗어나 자립하도록 돕는다.</p>
                <p><span class="p-num">➌</span><span class="mk-line-red">둘째, 공정 무역은 아동 노동 착취를 막고 지구 생태 환경을 보호하기 때문이다.</span> 공정 무역 인증을 받으려면 어린이를 강제로 일하게 해서는 안 되며, 위험한 농약 대신 친환경 농법을 사용해야 한다. <span class="mk-dotted">(실제로 공정 무역 커피 농장 마을에서는 아이들이 농장 대신 학교에 다니게 되었고, 농약 중독 사고도 크게 줄어들었다.)</span></p>
                <p><span class="p-num">➍</span><span class="mk-line-red">물론 공정 무역 제품은 일반 제품보다 가격이 조금 더 비싸고 판매하는 곳이 많지 않아 소비자가 구매하기 불편하다는 의견도 있다. 그러나 우리의 작은 소비 선택이 누군가의 삶과 학교를 지키는 가장 확실한 방법이라는 점에서 그 가치는 가격 이상으로 크다.</span> <span class="mk-double">따라서 우리는 물건을 살 때 공정 무역 인증 마크를 확인하고 공정 무역 제품을 사용하는 착한 소비를 실천해야 한다.</span></p>
              </td>
              <td class="wing-col">
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 1</span><span class="role-chip">함께 We Do</span></div>
                  <div><span class="q-num">①</span> 글 (나)의 1·2·3문단에서 점선 괄호 <code>( )</code>로 묶인 문장들은 요약할 때 왜 덜어내야 할까요?</div>
                  <span class="pencil-line">✏️ <span class="t-ans">중심 주장을 꾸며 주는 구체적인 예시(초콜릿·커피 농장 사례)와 세부 수치여서 덜어내도 핵심 논지가 유지되기 때문이다.</span></span>
                </div>
                <div class="wing-box question">
                  <div class="wing-box-title"><span>❓ 날개 물음 2</span><span class="role-chip">스스로 You Do</span></div>
                  <div><span class="q-num">②</span> 글 (나)에서 글쓴이가 내세운 <strong>두 가지 이유 골격</strong>은 무엇인가요?</div>
                  <span class="pencil-line">• 첫째: <span class="t-ans">생산자의 경제적 자립 지원</span></span>
                  <span class="pencil-line">• 둘째: <span class="t-ans">아동 노동 방지 및 환경 보호</span></span>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        """,
        "activity_1": {
            "title": "요약 규칙(삭제·선택·일반화)에 따라 남길 핵심 골격과 덜어낼 세부 자료 가려내기",
            "tag": "Step 1 중심 골격 vs 세부 수식 분리",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:18%;">구분</th>
                  <th style="width:42%;">✂️ 덜어낼 세부 통계·사례 수식어 (삭제 대상)</th>
                  <th style="width:40%;">💎 남겨야 할 핵심 명제 골격 (선택 대상)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700; text-align:center;">글 (가)<br>자율 선택 급식</td>
                  <td>경기도교육청 통계(잔반 27~82% 감소), 시범 초교 만족도 94%, 김정현 교수 인터뷰 인용구</td>
                  <td>• 주장: <span class="blank-slot"><span class="t-ans">자율 선택 급식을 도입해야 한다.</span></span><br>• 이유 1·2: <span class="blank-slot"><span class="t-ans">잔반·환경오염 감소 및 자기주도적 식습관 형성</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700; text-align:center;">글 (나)<br>공정 무역 제품</td>
                  <td>초콜릿 카카오 농장 일화, 중간 상인 이익 90% vs 농부 5% 수치, 커피 농장 마을 사례</td>
                  <td>• 주장: <span class="blank-slot"><span class="t-ans">공정 무역 제품을 적극 사용해야 한다.</span></span><br>• 이유 1·2: <span class="blank-slot"><span class="t-ans">생산자의 경제적 자립 지원 및 아동 노동 방지·환경 보호</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "arrow_1_to_2": "[활동 1]에서 남긴 핵심 골격(반론·재반박 + 이유 1·2 + 주장)을 결합하여 1~2문장 압축 요약문 완성하기",
        "activity_2": {
            "title": "논설문 압축 요약 공식에 넣어 글 (나)를 2문장으로 요약하기",
            "tag": "Step 2 구조적 통합 요약문 구성",
            "body_html": """
            <div style="border:0.9pt solid #2980B9; background:#EBF5FB; border-radius:5px; padding:5px 8px; font-size:7.4pt; margin-bottom:4px;">
              📐 <strong>[6학년 논설문 압축 요약 틀]:</strong><br>
              “<strong>[논제/대상]</strong>은 비록 <strong>[예상 반론]</strong>이라는 의견도 있으나 <strong>[재반박 핵심]</strong>라는 점에서 가치가 크다. 특히 <strong>[첫째 이유 골격]</strong>하고 <strong>[둘째 이유 골격]</strong>하므로, 우리는 <strong>[핵심 주장 골격]</strong>해야 한다.”
            </div>
            <div style="border:0.8pt solid #BDC3C7; border-radius:5px; padding:5px 8px; background:#FFFFFF;">
              <span class="pencil-line">✏️ <strong>글 (나) 압축 요약문 (1문장):</strong> 공정 무역 제품은 비록 <span class="t-ans">일반 제품보다 가격이 조금 비싸고 구매하기 불편하다는 의견도 있으나 누군가의 삶을 지키는 가치 있는 소비이다.</span></span>
              <span class="pencil-line">✏️ <strong>(2문장):</strong> 특히 <span class="t-ans">개발 도상국 생산자의 경제적 자립을 돕고 아동 노동 착취 방지와 환경 보호에 기여하므로, 우리는 공정 무역 제품을 적극적으로 사용해야 한다.</span></span>
            </div>
            """,
        },
        "arrow_2_to_3": "[활동 2]에서 요약한 핵심 주제와 글쓴이의 입장이 한눈에 드러나도록 3가지 기법으로 설득적 제목 붙이기",
        "activity_3": {
            "title": "독자의 마음을 움직이는 ‘설득적 제목 짓기 3대 기법’ 실습",
            "tag": "Step 3 설득적 제목·부제 산출",
            "body_html": """
            <table class="std-table">
              <thead>
                <tr>
                  <th style="width:24%;">설득적 제목 기법</th>
                  <th style="width:38%;">글 (가) 〈자율 선택 급식〉 제목 예시</th>
                  <th style="width:38%;">글 (나) 〈공정 무역〉 나만의 제목 짓기</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:700;">① 당위·행동 촉구형<br>(<code>~하자 / ~해야 한다</code>)</td>
                  <td>학교 급식 잔반 줄이기, ‘자율 선택 급식’ 도입으로 해결하자</td>
                  <td><span class="blank-slot"><span class="t-ans">지구촌 이웃의 인권을 지키는 ‘공정 무역 제품’을 사용합시다</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700;">② 대구·대조 강조형<br>(<code>A는 줄이고, B는 높이고!</code>)</td>
                  <td>버려지는 잔반은 확 줄이고, 식습관 자율성은 쑥 높이는 자율 선택 급식!</td>
                  <td><span class="blank-slot"><span class="t-ans">불공정한 착취는 멈추고, 정당한 땀의 가치는 살리는 공정 무역!</span></span></td>
                </tr>
                <tr>
                  <td style="font-weight:700;">③ 수사적 의문문형<br>(<code>~할 것인가?</code>)</td>
                  <td>산더미 같은 급식 잔반, 언제까지 정량 배식만 고집할 것인가?</td>
                  <td><span class="blank-slot"><span class="t-ans">달콤한 초콜릿 뒤의 눈물, 공정 무역으로 닦아 주어야 하지 않을까?</span></span></td>
                </tr>
              </tbody>
            </table>
            """,
        },
        "writing_seed": {
            "transfer_tag": "12차시(W1 주제문)·15차시(W4 제목 짓기) 직결",
            "prompt": "1차시에 적어 둔 나의 관심 쟁점에 어울리는 ‘설득적 제목’ 1개를 위 3대 기법 중 하나로 미리 지어 보세요.",
            "placeholder": "예: [대구형] 위험한 질주는 멈추고, 안전한 등굣길은 지키는 스쿨존 킥보드 금지!",
            "example_answer": "위험한 질주는 멈추고 안전한 통학로는 지키는 약속, 스쿨존 내 전동 킥보드 통행을 금지하자!",
        },
        "self_check": [
            "세부 통계 수치와 개별 사례를 덜어내고 핵심 골격만 남겼나요?",
            "주장, 이유 1·2, 반론·재반박이 모두 담긴 2문장 요약문을 완성했나요?",
            "쟁점과 글쓴이의 입장이 선명하게 드러나는 설득적 제목을 지었나요?",
        ],
        "teacher_guide": {
            "board_plan_summary": "[논설문 요약 3원칙: ①삭제(세부 통계·개별 사례 일화 괄호 소거) ➔ ②선택(핵심 주장 + 이유 1·2 골격 + 반론·재반박 골격 추출) ➔ ③통합 재구성(2문장 압축 요약 틀)] + [설득적 제목 3대 기법: ①당위·촉구형 / ②대구·대조형 / ③수사적 의문문형]",
            "intro_5min": "긴 논설문을 친구에게 단 두 문장으로 소개해야 한다면 무엇을 빼고 무엇을 남겨야 할지 질문한다. 2차시에 배운 ‘문장 골격 추출’과 3차시에 배운 ‘3단 논증 구조도’를 합치면 어떤 논설문이든 완벽하게 요약할 수 있음을 안내한다.",
            "ido_think_aloud_script": "“글 (가)를 요약할 때 많은 친구가 ‘경기도교육청 조사에서 27%에서 82%까지 잔반이 줄었다’는 숫자가 멋져 보여서 요약문에 그대로 베껴 써요. 하지만 통계 숫자와 인터뷰는 이유를 증명하는 ‘주춧돌(세부 근거)’일 뿐이에요! 요약문에는 기둥인 ‘이유(음식물 쓰레기를 줄이고 자기주도적 식습관을 기른다)’와 ‘반론·재반박’, 그리고 지붕인 ‘주장(자율 선택 급식을 도입해야 한다)’만 남겨야 진짜 뼈대 요약문이 된답니다.”",
            "wedo_qa_list": [
                {
                    "qar_type": "생각하며 찾기 (Think & Search)",
                    "question": "글 (나)의 2문단에서 ‘일반 무역에서는 중간 상인이 90%를 가져가고 농부에게는 5%만 돌아간다’는 문장을 요약문에서 뺀 까닭은 무엇인가요?",
                    "expected_ans": "첫째 이유인 ‘생산자가 정당한 대가를 받아 경제적으로 자립할 수 있다’를 뒷받침하기 위한 세부 수치 비교 자료이기 때문입니다.",
                    "reprompt": "2문단의 첫 문장(중심 문장)과 두 번째 문장(90% vs 5% 비교) 중 어느 문장이 글쓴이의 첫째 이유를 직접 말하고 있나요?",
                },
                {
                    "qar_type": "작가와 내가 함께 (Author & You)",
                    "question": "논설문의 제목을 그냥 〈공정 무역에 대하여〉라고 짓는 것과 〈정당한 땀의 대가를 지키는 약속, 공정 무역 제품을 사용합시다〉라고 짓는 것은 어떤 차이가 있나요?",
                    "expected_ans": "〈공정 무역에 대하여〉는 설명문 제목처럼 입장이 드러나지 않지만, 두 번째 제목은 글쓴이의 찬성 주장과 핵심 이유가 한눈에 드러나 독자를 설득하는 힘이 강합니다.",
                    "reprompt": "독자가 제목만 보고도 ‘아, 이 글은 나에게 어떤 행동을 하자고 설득하는 글이구나!’라고 바로 알 수 있는 제목은 어느 쪽인가요?",
                },
            ],
            "youdo_and_wrapup": "학생들이 [활동 2]의 2문장 압축 요약 틀에 맞추어 글 (나)를 요약하고, [활동 3]에서 3가지 수사 기법으로 설득적 제목을 창작하도록 지도한다. 1~4차시(사실적 이해) 학습을 갈무리하며 다음 차시부터는 글 속에 숨겨진 뜻과 전제를 추론하는 ‘추론적 이해’로 나아감을 안내한다.",
            "answer_key_html": """
            <div style="font-size:7.2pt; line-height:1.45;">
              <strong>• 날개 물음 정답:</strong> ① 중심 주장을 뒷받침하는 세부 예시(초콜릿·커피 농장)와 구체적 수치여서 덜어내도 핵심 논지가 유지되기 때문. / ② 첫째: 생산자의 경제적 자립 지원, 둘째: 아동 노동 착취 방지 및 생태 환경 보호.<br>
              <strong>• [활동 1] 정답:</strong> 글 (가) 주장(자율 선택 급식 도입), 이유 1·2(잔반·환경오염 감소 및 자기주도적 식습관 형성) / 글 (나) 주장(공정 무역 제품 적극 사용), 이유 1·2(생산자 경제적 자립 지원 및 아동 노동 방지·환경 보호).<br>
              <strong>• [활동 2] 모범 답안:</strong> “공정 무역 제품은 비록 일반 제품보다 가격이 조금 비싸고 구매하기 불편하다는 의견도 있으나 누군가의 삶을 지키는 가치 있는 소비이다. 특히 개발 도상국 생산자의 경제적 자립을 돕고 아동 노동 착취 방지와 환경 보호에 기여하므로, 우리는 공정 무역 제품을 적극적으로 사용해야 한다.”<br>
              <strong>• [활동 3] 모범 답안:</strong> ① 당위형: <code>지구촌 이웃의 인권을 지키는 ‘공정 무역 제품’을 사용합시다</code> / ② 대구형: <code>불공정한 착취는 멈추고, 정당한 땀의 가치는 살리는 공정 무역!</code> / ③ 의문문형: <code>달콤한 초콜릿 뒤의 눈물, 공정 무역으로 닦아 주어야 하지 않을까?</code>
            </div>
            """,
            "misconceptions": [
                {
                    "error_case": "요약문에 서론의 흥미 유발 일화(초콜릿 카카오 농장 이야기)를 길게 포함시킴",
                    "diagnosis": "독자의 관심을 끌기 위한 도입부 예시를 글 전체의 중심 명제로 오인함",
                    "prescription": "1문단에서 ‘이처럼 ~’ 뒤의 핵심 주장 문장만 남기고 앞부분의 도입 일화는 과감히 괄호로 묶어 지우는 삭제 규칙을 시연함",
                },
                {
                    "error_case": "설득적 제목을 지을 때 설명문처럼 중립적 명사구(‘공정 무역의 뜻과 특징’)로 작성함",
                    "diagnosis": "설명문 제목(정보 제시)과 논설문 제목(입장·주장 천명)의 갈래적 차이를 인식하지 못함",
                    "prescription": "논설문 제목에는 반드시 ‘찬성/반대 입장’이나 ‘~하자, ~해야 한다’라는 당위적 방향성이 들어가야 함을 3대 기법 예시와 대조해 지도함",
                },
            ],
            "scaffolding_down": "2문장 요약문 작성이 어려운 학생에게는 [활동 2]의 요약 문장 틀에서 빈칸 4곳(반론, 이유1, 이유2, 주장)만 채워 넣으면 문장이 완성되도록 구조화된 문장 프레임을 제공한다.",
            "scaffolding_up": "자신이 지은 3가지 설득적 제목 중 ‘공정 무역에 전혀 관심이 없던 친구’의 마음을 가장 잘 움직일 수 있는 제목 1개를 고르고, 그 제목이 가진 표현 효과를 발표하게 한다.",
            "rubric": {
                "high": "세부 통계·사례 수식어를 정확히 덜어내고 핵심 주장·이유 1·2·반론 재반박 골격이 모두 포함된 2문장 요약문을 완성하며, 3가지 기법으로 참신하고 설득력 있는 제목을 작성함.",
                "mid": "핵심 주장과 이유 1·2를 포함하여 요약문을 작성했으나, 반론·재반박 골격이 빠지거나 세부 사례 일부가 요약문에 남아 있음.",
                "low": "중심 문장과 세부 뒷받침 문장을 구분하지 못해 특정 문단만 그대로 베껴 적거나 논지가 드러나지 않는 제목을 지음.",
            },
        },
    },
]
