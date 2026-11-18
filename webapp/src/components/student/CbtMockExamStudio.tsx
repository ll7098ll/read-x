import React, { useState, useEffect } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData, SlotLessonPackage } from '../../types/courseware';

interface CbtMockExamStudioProps {
  gradeData: GradeData;
  gradeSlots16: SlotLessonPackage[];
}

export const CbtMockExamStudio: React.FC<CbtMockExamStudioProps> = ({
  gradeData,
  gradeSlots16,
}) => {
  const {
    activeSlotId,
    selectGradeAndSlot,
    boostSmartScore,
    updateSubskillScore,
    markSlotCompleted,
    recordAttemptLog,
    unlockVaccine,
  } = useCoursewareStore();

  // Select up to 3 passages (current slot + 2 adjacent slots in the grade) for a comprehensive CBT Mock Exam,
  // or allow single-passage focused CBT mode
  const [examScope, setExamScope] = useState<'single' | 'comprehensive'>('single');
  const currentSlot =
    gradeSlots16.find((s) => s.slot_id === (activeSlotId || gradeData.slot_id)) ||
    gradeSlots16[0];

  const examPassages: SlotLessonPackage[] =
    examScope === 'single' || gradeSlots16.length <= 1
      ? currentSlot
        ? [currentSlot]
        : []
      : (() => {
          const curIdx = Math.max(
            0,
            gradeSlots16.findIndex((s) => s.slot_id === currentSlot?.slot_id)
          );
          const picked: SlotLessonPackage[] = [];
          for (let i = 0; i < Math.min(3, gradeSlots16.length); i++) {
            picked.push(gradeSlots16[(curIdx + i) % gradeSlots16.length]);
          }
          return picked;
        })();

  const [activePassageIdx, setActivePassageIdx] = useState(0);
  const [omrAnswers, setOmrAnswers] = useState<Record<string, number>>({});
  const [flaggedKeys, setFlaggedKeys] = useState<Record<string, boolean>>({});
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [elapsedSec, setElapsedSec] = useState(0);
  const [hideTimer, setHideTimer] = useState(false);

  useEffect(() => {
    setActivePassageIdx(0);
    setOmrAnswers({});
    setFlaggedKeys({});
    setIsSubmitted(false);
    setElapsedSec(0);
  }, [gradeData.grade_num, activeSlotId, examScope]);

  useEffect(() => {
    if (isSubmitted) return;
    const timer = setInterval(() => {
      setElapsedSec((s) => s + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [isSubmitted]);

  // Flatten all questions across examPassages for the OMR sheet
  const allExamItems = examPassages.flatMap((slot, pIdx) =>
    (slot.real_csat_test?.questions || []).map((q, qIdx) => ({
      key: `${slot.slot_id}-Q${q.q_no}`,
      globalNo: examPassages.slice(0, pIdx).reduce((n, s) => n + s.real_csat_test.questions.length, 0) + qIdx + 1,
      passageIdx: pIdx,
      slot,
      question: q,
    }))
  );

  const activePassageSlot = examPassages[activePassageIdx] || currentSlot;
  const totalQuestions = allExamItems.length;
  const answeredCount = Object.keys(omrAnswers).length;

  const formatTime = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  };

  const handleSelectOption = (itemKey: string, optNo: number) => {
    if (isSubmitted) return;
    setOmrAnswers((prev) => ({ ...prev, [itemKey]: optNo }));
  };

  const toggleFlag = (itemKey: string) => {
    if (isSubmitted) return;
    setFlaggedKeys((prev) => ({ ...prev, [itemKey]: !prev[itemKey] }));
  };

  const handleSubmitExam = () => {
    if (totalQuestions === 0 || isSubmitted) return;
    setIsSubmitted(true);

    let correctCnt = 0;
    allExamItems.forEach((item) => {
      const pickedNo = omrAnswers[item.key] || 0;
      const pickedOpt = item.question.options.find((o) => o.no === pickedNo);
      const isCorrect = Boolean(pickedOpt?.is_correct);
      if (isCorrect) correctCnt += 1;

      const trapMatch = pickedOpt?.formula?.match(/D[1-6]/);
      const trapCode = isCorrect ? 'NONE' : trapMatch ? trapMatch[0] : 'D6';

      recordAttemptLog({
        slot_id: item.slot.slot_id,
        grade_num: item.slot.grade_num,
        subskill_code: item.slot.subskill_code,
        q_no: item.question.q_no,
        selected_option: pickedNo,
        is_correct: isCorrect,
        trap_code: trapCode,
        reading_time_sec: Math.round(elapsedSec / Math.max(1, totalQuestions)),
        scaffolding_used: 0,
      });

      if (isCorrect) {
        unlockVaccine('D1');
      }
    });

    // This screen reports only responses to this practice set.
    // A practice score is not a completed assignment or a subskill mastery update.

  };

  const correctTotal = allExamItems.filter((item) => {
    const picked = omrAnswers[item.key];
    return item.question.options.find((o) => o.no === picked)?.is_correct;
  }).length;
  const finalScore = totalQuestions > 0 ? Math.round((correctTotal / totalQuestions) * 100) : 0;

  return (
    <div className="space-y-4 font-sans">
      {/* Clean CBT Exam Control & OMR Bar */}
      <div className="bg-white rounded-3xl border border-slate-200/90 p-5 sm:p-6 shadow-xs text-slate-800">
        <div className="flex flex-wrap items-center justify-between gap-4 pb-4 border-b border-slate-100">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-md text-[11px] font-bold bg-blue-50 text-blue-700 border border-blue-200">
                KICE CBT 수능 실전 모의평가
              </span>
              <span className="text-xs text-slate-400 font-medium hidden md:inline">
                단서 및 힌트 무보조 실전 전이 검증
              </span>
            </div>
            <h2 className="text-lg sm:text-xl font-black text-slate-900 mt-1 tracking-tight">
              {gradeData.grade} 실전 모의고사 · {activePassageSlot?.real_csat_test.passage_title}
            </h2>
          </div>

          {/* Scope Switcher + Timer + Submit CTA */}
          <div className="flex flex-wrap items-center gap-2">
            <div className="bg-slate-100 p-1 rounded-xl border border-slate-200 flex items-center gap-1">
              <button
                onClick={() => setExamScope('single')}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                  examScope === 'single'
                    ? 'bg-white text-blue-600 shadow-xs'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                단일 지문 (2문항)
              </button>
              <button
                onClick={() => setExamScope('comprehensive')}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                  examScope === 'comprehensive'
                    ? 'bg-white text-blue-600 shadow-xs'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                3개 지문 종합 (6문항)
              </button>
            </div>

            <div className="bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 flex items-center gap-2 text-xs">
              <span className="text-slate-500 font-bold">⏱️ 응시 시간:</span>
              {!hideTimer ? (
                <span className="font-mono font-black text-slate-800 text-sm">
                  {formatTime(elapsedSec)}
                </span>
              ) : (
                <span className="text-slate-400">숨김</span>
              )}
              <button
                onClick={() => setHideTimer(!hideTimer)}
                className="text-[10px] text-slate-500 hover:text-slate-800 underline cursor-pointer"
              >
                {hideTimer ? '표시' : '숨김'}
              </button>
            </div>

            {!isSubmitted ? (
              <button
                onClick={handleSubmitExam}
                className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-xs transition cursor-pointer"
              >
                답안 제출 및 채점 ({answeredCount}/{totalQuestions})
              </button>
            ) : (
              <button
                onClick={() => {
                  setOmrAnswers({});
                  setFlaggedKeys({});
                  setIsSubmitted(false);
                  setElapsedSec(0);
                }}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs shadow-xs transition cursor-pointer"
              >
                🔄 재응시
              </button>
            )}
          </div>
        </div>

        {/* OMR Palette Row */}
        <div className="pt-3 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-bold text-slate-500">📋 OMR 마킹:</span>
            {allExamItems.map((item) => {
              const picked = omrAnswers[item.key];
              const flagged = flaggedKeys[item.key];
              const isCorrect =
                isSubmitted &&
                item.question.options.find((o) => o.no === picked)?.is_correct;

              return (
                <button
                  key={item.key}
                  onClick={() => setActivePassageIdx(item.passageIdx)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold border flex items-center gap-1 transition cursor-pointer ${
                    isSubmitted
                      ? isCorrect
                        ? 'bg-emerald-50 border-emerald-400 text-emerald-800'
                        : 'bg-rose-50 border-rose-400 text-rose-800'
                      : picked
                      ? 'bg-blue-600 border-blue-600 text-white shadow-xs'
                      : 'bg-white border-slate-200 text-slate-700 hover:border-slate-300'
                  }`}
                >
                  <span>문항 {item.globalNo}</span>
                  {picked && <span className="text-amber-300">({picked}번)</span>}
                  {flagged && <span>🚩</span>}
                  {isSubmitted && <span>{isCorrect ? '⭕' : '❌'}</span>}
                </button>
              );
            })}
          </div>

          {examPassages.length > 1 && (
            <div className="flex items-center gap-1.5">
              {examPassages.map((p, idx) => (
                <button
                  key={p.slot_id}
                  onClick={() => setActivePassageIdx(idx)}
                  className={`px-3 py-1 rounded-lg text-xs font-extrabold border transition ${
                    activePassageIdx === idx
                      ? 'bg-amber-400 text-slate-950 border-amber-300'
                      : 'bg-slate-800 text-slate-300 border-slate-700 hover:text-white'
                  }`}
                >
                  지문 {idx + 1}: {p.slot_id}
                </button>
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Post-Submission Score & Telemetry Summary Banner */}
      {isSubmitted && (
        <div className="bg-white rounded-2xl border-2 border-indigo-600 p-5 shadow-md">
          <div className="flex flex-wrap items-center justify-between gap-4">
            <div>
              <span className="px-2.5 py-0.5 rounded-full text-xs font-black bg-indigo-100 text-indigo-800">
                KICE 평가원 기준 CBT 채점 리포트
              </span>
              <h3 className="text-lg font-black text-slate-900 mt-1">
                총점 <span className="text-indigo-600">{finalScore}점</span> ({correctTotal} / {totalQuestions}문항 정답) · 총 소요시간 {formatTime(elapsedSec)}
              </h3>
              <p className="text-xs text-slate-600 mt-0.5">
                {finalScore >= 80
                  ? '🎉 스캐폴딩 없이도 핵심 명제와 오답 함정을 정확히 변별하여 목표 위계 전이(Transfer)에 성공했습니다!'
                  : '💊 일부 매력적 오답 함정(D1~D6)에 흔들린 문항이 있습니다. 아래 전 선지 해부 해설을 확인하고 1:1 약점 처방 클리닉으로 즉시 보강하세요.'}
              </p>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={() =>
                  selectGradeAndSlot(
                    gradeData.grade_num,
                    activePassageSlot.slot_id,
                    'clinic'
                  )
                }
                className="px-4 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-black text-xs shadow transition"
              >
                💊 이 차시 1:1 처방 클리닉으로 보강하기 ➔
              </button>
              <button
                onClick={() =>
                  selectGradeAndSlot(
                    gradeData.grade_num,
                    activePassageSlot.slot_id,
                    'portal'
                  )
                }
                className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-900 text-white font-black text-xs shadow transition"
              >
                📊 6차원 X-Ray 대시보드로 돌아가기
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Split-Screen CBT Layout: Left Unassisted Passage + Right OMR Questions */}
      {activePassageSlot && (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
          {/* Left: Clean KICE Exam Paper Style Passage */}
          <div className="lg:col-span-6 bg-[#FCFBF7] rounded-2xl border border-slate-300 p-5 shadow-sm lg:sticky lg:top-20 max-h-[82vh] overflow-y-auto">
            <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-200">
              <div>
                <span className="text-[11px] font-black px-2 py-0.5 rounded bg-slate-800 text-white">
                  {activePassageSlot.slot_id} · {activePassageSlot.curriculum_concept.subject}
                </span>
                <h3 className="text-base md:text-lg font-black text-slate-900 mt-1">
                  {activePassageSlot.real_csat_test.passage_title}
                </h3>
              </div>
              <span className="text-[11px] text-slate-500 font-bold">
                {activePassageSlot.real_csat_test.passage_spec}
              </span>
            </div>

            <div className="space-y-3.5 text-slate-900 leading-[1.95] text-[15.5px] font-serif">
              {activePassageSlot.real_csat_test.paragraphs.map((para, pIdx) => (
                <p key={pIdx} className="indent-3">
                  <span className="inline-block font-sans text-[11px] font-black text-slate-400 mr-1.5 select-none">
                    [{pIdx + 1}문단]
                  </span>
                  <span dangerouslySetInnerHTML={{ __html: para }} />
                </p>
              ))}
            </div>

            {activePassageSlot.real_csat_test.visual_html && (
              <div className="mt-4 pt-4 border-t border-slate-200">
                <div className="text-xs font-black text-slate-700 mb-2">
                  📊 [참고 시각·도표 자료]
                </div>
                <div
                  className="text-xs bg-white p-3 rounded-xl border border-slate-200"
                  dangerouslySetInnerHTML={{
                    __html: activePassageSlot.real_csat_test.visual_html,
                  }}
                />
              </div>
            )}
          </div>

          {/* Right: Unassisted CBT Questions + Post-Submit Full D1~D6 Anatomy */}
          <div className="lg:col-span-6 space-y-4">
            {allExamItems
              .filter((it) => it.passageIdx === activePassageIdx)
              .map((item) => {
                const q = item.question;
                const pickedNo = omrAnswers[item.key];
                const isFlagged = flaggedKeys[item.key];

                return (
                  <div
                    key={item.key}
                    className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-3"
                  >
                    <div className="flex items-center justify-between gap-2 pb-2 border-b border-slate-100">
                      <span className="text-xs font-extrabold text-indigo-700 bg-indigo-50 px-2.5 py-1 rounded-lg">
                        문항 {item.globalNo} · {q.archetype}
                      </span>
                      <button
                        onClick={() => toggleFlag(item.key)}
                        className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition ${
                          isFlagged
                            ? 'bg-amber-100 border-amber-400 text-amber-900'
                            : 'bg-slate-50 border-slate-200 text-slate-500 hover:bg-slate-100'
                        }`}
                      >
                        🚩 {isFlagged ? '별표 체크됨' : '헷갈리는 문항 체크'}
                      </button>
                    </div>

                    <div
                      className="font-black text-sm md:text-base text-slate-900 leading-snug"
                      dangerouslySetInnerHTML={{
                        __html: `${item.globalNo}. ${q.stem}`,
                      }}
                    />

                    {q.bogi && (
                      <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-300 text-xs text-slate-800 leading-relaxed">
                        <div className="font-black text-slate-900 mb-1 text-center">
                          &lt;보 기&gt;
                        </div>
                        <div dangerouslySetInnerHTML={{ __html: q.bogi }} />
                      </div>
                    )}

                    <div className="space-y-2 pt-1">
                      {q.options.map((opt) => {
                        const isPicked = pickedNo === opt.no;
                        let btnStyle =
                          'bg-white border-slate-200 hover:border-blue-400 text-slate-800';
                        if (!isSubmitted && isPicked) {
                          btnStyle =
                            'bg-blue-50 border-blue-600 ring-1 ring-blue-600 text-blue-950 font-bold';
                        } else if (isSubmitted) {
                          if (opt.is_correct) {
                            btnStyle =
                              'bg-emerald-50 border-emerald-500 ring-1 ring-emerald-500 text-emerald-950 font-bold';
                          } else if (isPicked && !opt.is_correct) {
                            btnStyle =
                              'bg-rose-50 border-rose-500 ring-1 ring-rose-500 text-rose-950';
                          }
                        }

                        return (
                          <div key={opt.no} className="space-y-1.5">
                            <button
                              onClick={() => handleSelectOption(item.key, opt.no)}
                              className={`w-full text-left p-3 rounded-xl border text-xs md:text-sm transition flex items-start gap-2.5 ${btnStyle}`}
                            >
                              <span
                                className={`w-5 h-5 rounded-full flex items-center justify-center text-xs font-black shrink-0 mt-0.5 ${
                                  isPicked
                                    ? 'bg-blue-600 text-white'
                                    : 'bg-slate-200 text-slate-700'
                                }`}
                              >
                                {opt.no}
                              </span>
                              <span className="flex-1 leading-relaxed">{opt.text}</span>
                              {isSubmitted && opt.is_correct && (
                                <span className="px-2 py-0.5 rounded bg-emerald-600 text-white text-[10px] font-black shrink-0">
                                  정답
                                </span>
                              )}
                              {isSubmitted && isPicked && !opt.is_correct && (
                                <span className="px-2 py-0.5 rounded bg-rose-600 text-white text-[10px] font-black shrink-0">
                                  내 오답
                                </span>
                              )}
                            </button>

                            {/* Post-Submission Full Distractor Anatomy */}
                            {isSubmitted && (
                              <div
                                className={`ml-6 p-2.5 rounded-lg text-xs border ${
                                  opt.is_correct
                                    ? 'bg-emerald-50/70 border-emerald-200 text-emerald-900'
                                    : 'bg-slate-50 border-slate-200 text-slate-700'
                                }`}
                              >
                                <div className="font-black mb-0.5">
                                  [{opt.formula}]
                                </div>
                                <div className="leading-relaxed">{opt.explanation}</div>
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
          </div>
        </div>
      )}
    </div>
  );
};
