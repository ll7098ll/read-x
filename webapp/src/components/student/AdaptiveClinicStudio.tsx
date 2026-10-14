import React, { useState, useEffect } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';

interface AdaptiveClinicStudioProps {
  gradeData: GradeData;
}

export const AdaptiveClinicStudio: React.FC<AdaptiveClinicStudioProps> = ({ gradeData }) => {
  const { setStudentMode, boostSmartScore, unlockVaccine, markStepComplete } = useCoursewareStore();
  const rx = gradeData.prescription_clinic;
  const go = gradeData.commercial.graphic_organizer;

  // Step 0 Remedial state
  const [step0Picked, setStep0Picked] = useState<string | null>(null);

  // Step 1-2 Cloze state
  const [clozeValues, setClozeValues] = useState<Record<string, string>>({});
  const [awakenedCues, setAwakenedCues] = useState<boolean>(false);

  // Step 3 Graphic Organizer (TEI-4) state
  const [selectedSlotId, setSelectedSlotId] = useState<string | null>(go.nodes[0]?.slot_id || null);
  const [slotAnswers, setSlotAnswers] = useState<Record<string, string>>({});
  const [goFeedback, setGoFeedback] = useState<string | null>(null);

  // Step 4 Vaccine OX state
  const [vaccinePicks, setVaccinePicks] = useState<Record<number, 'O' | 'X'>>({});

  // Reset local interactive states when grade changes
  useEffect(() => {
    setStep0Picked(null);
    setClozeValues({});
    setAwakenedCues(false);
    setSelectedSlotId(gradeData.commercial.graphic_organizer.nodes[0]?.slot_id || null);
    setSlotAnswers({});
    setGoFeedback(null);
    setVaccinePicks({});
  }, [gradeData.id, gradeData.slot_id, gradeData.commercial.graphic_organizer.nodes]);

  const handlePlaceWordCard = (cardText: string) => {
    const targetSlot = selectedSlotId || go.nodes[0]?.slot_id;
    if (!targetSlot) return;

    const nodeObj = go.nodes.find((n) => n.slot_id === targetSlot);
    if (!nodeObj) return;

    const nextAnswers = { ...slotAnswers, [targetSlot]: cardText };
    setSlotAnswers(nextAnswers);

    if (cardText === nodeObj.correct) {
      setGoFeedback(`⭕ 정확해요! [${nodeObj.header}] 슬롯에 알맞은 구조 카드를 연결했어요.`);
      boostSmartScore(gradeData.grade_num, 3);
      // Advance to next empty slot automatically
      const nextEmpty = go.nodes.find((n) => !nextAnswers[n.slot_id] || nextAnswers[n.slot_id] !== n.correct);
      if (nextEmpty) {
        setSelectedSlotId(nextEmpty.slot_id);
      }
    } else {
      setGoFeedback(
        `⚠️ 잠깐! 방금 고른 카드는 [${nodeObj.header}]의 내용과 맞지 않거나 매력적 함정 카드예요. 본문 단서를 다시 확인해 보세요!`
      );
    }
  };

  const handleAutoFillOrganizer = () => {
    const filled: Record<string, string> = {};
    go.nodes.forEach((n) => {
      filled[n.slot_id] = n.correct;
    });
    setSlotAnswers(filled);
    setGoFeedback('🎉 모든 구조도 슬롯이 정답 카드로 완성되었습니다!');
  };

  const handleVaccinePick = (idx: number, choice: 'O' | 'X', correctAns: 'O' | 'X') => {
    setVaccinePicks((prev) => ({ ...prev, [idx]: choice }));
    if (choice === correctAns) {
      boostSmartScore(gradeData.grade_num, 4);
      // Unlock top vulnerable trap vaccine for this grade
      const topTrap = gradeData.diagnosis_report.trap_radar.reduce((a, b) => (a.vuln > b.vuln ? a : b));
      if (topTrap) {
        unlockVaccine(topTrap.code);
      }
      markStepComplete(gradeData.grade_num, 'clinic');
    }
  };

  return (
    <div className="space-y-4 font-sans">
      {/* Clean Prescription Header Card */}
      <div className="bg-white rounded-3xl border border-slate-200/80 p-6 shadow-xs flex flex-wrap items-center justify-between gap-4">
        <div>
          <span className="text-[11px] font-bold text-blue-600 tracking-wider uppercase block">
            1:1 ADAPTIVE PRESCRIPTION CLINIC
          </span>
          <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-0.5">
            💊 {rx.rx_title}
          </h2>
          <p className="text-xs text-slate-500 mt-1 max-w-2xl">{rx.rx_reason}</p>
        </div>

        <button
          onClick={() => {
            markStepComplete(gradeData.grade_num, 'clinic');
            setStudentMode('studio');
          }}
          className="px-4 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-xs transition flex items-center gap-1.5 cursor-pointer shrink-0"
        >
          <span>독서 스튜디오로 이동</span>
          <span>➔</span>
        </button>
      </div>

      {/* Main 2-Column Prescription Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Left Column: Step 0 Remedial + Step 1&2 Think-Aloud Cloze */}
        <div className="space-y-4">
          {/* Step 0: Prerequisite Remedial Bridge */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🪜 [처방 1단계] 역추적된 하위 학년 선행 결손 징검다리 복습
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-amber-100 text-amber-800">
                {rx.step0_remedial.badge}
              </span>
            </div>

            <div className="bg-amber-50 border border-amber-200 p-3 rounded-xl text-xs md:text-sm text-amber-950 mb-3 leading-relaxed">
              {rx.step0_remedial.rule_box}
            </div>

            <div className="font-extrabold text-sm text-slate-900 mb-2.5">
              ❓ 선행 개념 확인 퀴즈:{' '}
              <span dangerouslySetInnerHTML={{ __html: rx.step0_remedial.mini_question }} />
            </div>

            <div className="flex flex-wrap gap-2">
              {rx.step0_remedial.choices.map((ch) => {
                const isPicked = step0Picked === ch;
                const isCorrect = ch === rx.step0_remedial.correct;
                let btnCls = 'bg-white border-slate-300 text-slate-800 hover:border-blue-500';
                if (isPicked) {
                  btnCls = isCorrect
                    ? 'bg-emerald-50 border-2 border-emerald-600 text-emerald-900 font-black'
                    : 'bg-rose-50 border-2 border-rose-600 text-rose-900 font-black';
                }

                return (
                  <button
                    key={ch}
                    onClick={() => {
                      setStep0Picked(ch);
                      if (ch === rx.step0_remedial.correct) {
                        boostSmartScore(gradeData.grade_num, 3);
                      }
                    }}
                    className={`px-3.5 py-2 rounded-xl border text-xs md:text-sm font-bold transition ${btnCls}`}
                  >
                    {ch}
                  </button>
                );
              })}
            </div>

            {step0Picked && (
              <div
                className={`mt-3 p-3 rounded-xl border-l-4 text-xs md:text-sm font-bold ${
                  step0Picked === rx.step0_remedial.correct
                    ? 'bg-emerald-50 border-emerald-600 text-emerald-950'
                    : 'bg-rose-50 border-rose-600 text-rose-950'
                }`}
              >
                {step0Picked === rx.step0_remedial.correct ? '⭕ ' : '💡 다시 확인! '}
                {rx.step0_remedial.feedback}
              </div>
            )}
          </div>

          {/* Step 1 & 2: Hot-Text Cue Awakening + TEI-3 Think-Aloud Cloze */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🧠 [처방 2단계 · TEI-3] Dick & Carey 병목 돌파 (단서 포착 + 사고구술 조립)
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-blue-100 text-blue-800">
                {rx.step1_2_drill.badge}
              </span>
            </div>

            <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
              <p className="text-xs text-slate-600">
                💡 지문 속 노란색 <b>단서 칩</b>을 클릭해 깨운 뒤, 아래 사고구술(Think-Aloud) 빈칸을 드롭다운으로 조립하세요.
              </p>
              <button
                onClick={() => setAwakenedCues(!awakenedCues)}
                className="text-xs font-extrabold px-2.5 py-1 rounded-lg bg-amber-100 hover:bg-amber-200 text-amber-900 transition"
              >
                {awakenedCues ? '✨ 단서 힌트 접기' : '✨ 모든 단서 힌트 깨우기'}
              </button>
            </div>

            <div
              onClick={() => setAwakenedCues(true)}
              className="reader-theme-paper border border-slate-300 rounded-xl p-3.5 text-sm leading-relaxed mb-3"
              dangerouslySetInnerHTML={{ __html: rx.step1_2_drill.passage_snippet }}
            />

            {awakenedCues && (
              <div className="mb-3 p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-950 space-y-1">
                <div className="font-black">🔍 포착된 핵심 단서(Hot-Text Cues) 역할 해설:</div>
                {gradeData.commercial.Interactive_hottext_cues.map((c) => (
                  <div key={c.cue_id}>
                    • <b>“{c.text}”</b> ➔ {c.role}
                  </div>
                ))}
              </div>
            )}

            {/* TEI-3 Inline Cloze Dropdown Box */}
            <div className="bg-blue-50/80 border border-blue-200 rounded-xl p-3.5 space-y-2.5">
              <div className="font-extrabold text-xs md:text-sm text-blue-900">
                🗣️ 사고구술(Think-Aloud) 구조 조립: {rx.step1_2_drill.think_aloud_prompt}
              </div>

              {rx.step1_2_drill.cloze_sentences.map((line, lIdx) => {
                // Split line by {b1}, {b2}, etc.
                const parts = line.split(/(\{b\d+\})/g);
                return (
                  <div
                    key={lIdx}
                    className="text-xs md:text-sm font-bold text-slate-800 leading-loose flex flex-wrap items-center gap-1"
                  >
                    {parts.map((part, pIdx) => {
                      const match = part.match(/^\{(b\d+)\}$/);
                      if (!match) return <span key={pIdx}>{part}</span>;
                      const blankId = match[1];
                      const blankObj = rx.step1_2_drill.blanks.find((b) => b.id === blankId);
                      if (!blankObj) return <span key={pIdx}>{part}</span>;

                      const val = clozeValues[blankId] || '';
                      const isCorrect = val === blankObj.correct;
                      const selStyle = !val
                        ? 'bg-white border-blue-500 text-blue-900'
                        : isCorrect
                        ? 'bg-emerald-100 border-emerald-600 text-emerald-900'
                        : 'bg-rose-100 border-rose-600 text-rose-900';

                      return (
                        <select
                          key={pIdx}
                          value={val}
                          onChange={(e) => {
                            const nextVal = e.target.value;
                            setClozeValues((prev) => ({ ...prev, [blankId]: nextVal }));
                            if (nextVal === blankObj.correct) {
                              boostSmartScore(gradeData.grade_num, 3);
                            }
                          }}
                          className={`px-2 py-1 rounded-lg border-2 font-black text-xs md:text-sm cursor-pointer ${selStyle}`}
                        >
                          <option value="">-- 단서 선택 --</option>
                          {blankObj.options.map((o) => (
                            <option key={o} value={o}>
                              {o}
                            </option>
                          ))}
                        </select>
                      );
                    })}
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Right Column: TEI-4 Graphic Organizer Builder + Step 4 Distractor Vaccine OX */}
        <div className="space-y-4">
          {/* TEI-4 Interactive 6 Text Structures Graphic Organizer Builder */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🧩 {go.title}
              </span>
              <button
                onClick={handleAutoFillOrganizer}
                className="text-xs font-extrabold px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition"
              >
                ✨ 정답 구조 한눈에 채우기
              </button>
            </div>

            <p className="text-xs text-slate-600 mb-3">
              💡 <b>조작 방법:</b> ① 먼저 채울 구조도 빈칸 슬롯을 클릭한 뒤 ➔ ② 아래 <b>[보기 카드 뱅크]</b>에서 알맞은 카드를 탭하여 조립하세요!
            </p>

            {/* Structure Slots Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-3">
              {go.nodes.map((node) => {
                const currentAns = slotAnswers[node.slot_id];
                const isCorrect = currentAns === node.correct;
                const isSelected = selectedSlotId === node.slot_id;

                return (
                  <div
                    key={node.slot_id}
                    onClick={() => setSelectedSlotId(node.slot_id)}
                    className={`p-3 rounded-xl border-2 cursor-pointer transition-all ${
                      isSelected
                        ? 'border-blue-600 bg-blue-50/40 ring-2 ring-blue-300'
                        : isCorrect
                        ? 'border-emerald-500 bg-emerald-50/40'
                        : 'border-slate-200 bg-slate-50 hover:border-slate-300'
                    }`}
                  >
                    <div className="flex items-center justify-between text-xs font-black text-slate-900">
                      <span>{node.header}</span>
                      <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-200 text-slate-700">
                        {node.sub}
                      </span>
                    </div>

                    <div
                      className={`mt-2 p-2 rounded-lg text-xs font-bold border border-dashed min-h-[38px] flex items-center justify-between ${
                        !currentAns
                          ? 'bg-white border-slate-300 text-slate-400'
                          : isCorrect
                          ? 'bg-emerald-100 border-emerald-500 text-emerald-950'
                          : 'bg-rose-100 border-rose-500 text-rose-950'
                      }`}
                    >
                      <span>{currentAns || '여기를 선택하고 아래 카드를 탭하세요'}</span>
                      {currentAns && <span>{isCorrect ? '⭕' : '❌'}</span>}
                    </div>
                  </div>
                );
              })}
            </div>

            {/* Word Bank */}
            <div className="bg-slate-100 p-3 rounded-xl border border-slate-200">
              <div className="text-xs font-extrabold text-slate-700 mb-2">
                🗂️ [보기 카드 뱅크] (함정 카드를 피해 슬롯에 배치하세요):
              </div>
              <div className="flex flex-wrap gap-2">
                {go.word_bank.map((card, cIdx) => {
                  const isUsedCorrectly = go.nodes.some(
                    (n) => slotAnswers[n.slot_id] === card && n.correct === card
                  );
                  return (
                    <button
                      key={cIdx}
                      onClick={() => handlePlaceWordCard(card)}
                      className={`px-3 py-1.5 rounded-lg text-xs font-bold border transition text-left ${
                        isUsedCorrectly
                          ? 'bg-emerald-600 text-white border-emerald-600 opacity-75'
                          : 'bg-white hover:bg-blue-50 text-slate-800 border-slate-300 hover:border-blue-500 shadow-sm'
                      }`}
                    >
                      {isUsedCorrectly ? `✅ ${card}` : `+ ${card}`}
                    </button>
                  );
                })}
              </div>
            </div>

            {goFeedback && (
              <div
                className={`mt-2.5 p-2.5 rounded-xl text-xs font-bold ${
                  goFeedback.startsWith('⭕') || goFeedback.startsWith('🎉')
                    ? 'bg-emerald-50 text-emerald-900 border border-emerald-300'
                    : 'bg-amber-50 text-amber-900 border border-amber-300'
                }`}
              >
                {goFeedback}
              </div>
            )}
          </div>

          {/* Step 4: Distractor Trap Vaccine O/X Drill */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🛡️ [처방 3단계] 수능 매력적 오답 함정 백신 드릴 (O/X 판별)
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-rose-100 text-rose-800">
                {rx.step3_vaccine.badge}
              </span>
            </div>

            <p className="text-xs text-slate-600 mb-3">{rx.step3_vaccine.desc}</p>

            <div className="space-y-3">
              {rx.step3_vaccine.items.map((item, idx) => {
                const picked = vaccinePicks[idx];
                const isCorrect = picked === item.answer;

                return (
                  <div
                    key={idx}
                    className="p-3.5 rounded-xl border border-slate-200 bg-slate-50 space-y-2.5"
                  >
                    <div className="font-extrabold text-xs md:text-sm text-slate-900">
                      함정 검증 문장 {idx + 1}. “{item.statement}”
                    </div>
                    <div className="flex gap-2">
                      {(['O', 'X'] as const).map((choice) => {
                        const active = picked === choice;
                        let btnStyle = 'bg-white border-slate-300 text-slate-800 hover:border-blue-500';
                        if (active) {
                          btnStyle = isCorrect
                            ? 'bg-emerald-100 border-2 border-emerald-600 text-emerald-950 font-black'
                            : 'bg-rose-100 border-2 border-rose-600 text-rose-950 font-black';
                        }
                        return (
                          <button
                            key={choice}
                            onClick={() => handleVaccinePick(idx, choice, item.answer)}
                            className={`px-3.5 py-1.5 rounded-lg border text-xs font-bold transition ${btnStyle}`}
                          >
                            {choice === 'O' ? '⭕ O (본문과 일치·적절함)' : '❌ X (매력적 함정 오답!)'}
                          </button>
                        );
                      })}
                    </div>

                    {picked && (
                      <div
                        className={`p-2.5 rounded-lg border-l-4 text-xs leading-relaxed ${
                          isCorrect
                            ? 'bg-emerald-50 border-emerald-600 text-emerald-950'
                            : 'bg-rose-50 border-rose-600 text-rose-950'
                        }`}
                      >
                        <b>[정답: {item.answer}]</b> {item.reason}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            <div className="mt-4 p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 flex flex-wrap items-center justify-between gap-3">
              <div>
                <div className="font-black text-sm text-emerald-900">
                  ✅ 맞춤형 처방 훈련 & 구조도 조립 완료!
                </div>
                <div className="text-xs text-emerald-800">
                  이제 7종 읽기 도구와 3단계 점진적 스캐폴딩이 탑재된 실전 스플릿 스튜디오로 이동합니다.
                </div>
              </div>
              <button
                onClick={() => {
                  markStepComplete(gradeData.grade_num, 'clinic');
                  setStudentMode('studio');
                }}
                className="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs md:text-sm font-extrabold shadow transition"
              >
                🏆 실전 스플릿 리더 & 수능 스튜디오로 이동 ➔
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
