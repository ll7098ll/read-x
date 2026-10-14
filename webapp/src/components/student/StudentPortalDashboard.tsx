import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { speakKoreanText, stopKoreanSpeech } from '../../utils/ttsEngine';
import { VocabDuelArena } from './VocabDuelArena';
import { GalaxyExpeditionMap } from './GalaxyExpeditionMap';
import { OnboardingCatModal } from './OnboardingCatModal';
import type {
  GradeData,
  SubskillMeta,
  DistractorMeta,
  SlotLessonPackage,
  CommonRemedialSlot,
} from '../../types/courseware';

interface StudentPortalDashboardProps {
  gradeData: GradeData;
  subskillMeta: SubskillMeta[];
  distractorMeta: DistractorMeta[];
  gradeSlots16: SlotLessonPackage[];
  gradeCommon6: CommonRemedialSlot[];
}

export const StudentPortalDashboard: React.FC<StudentPortalDashboardProps> = ({
  gradeData,
  subskillMeta,
  distractorMeta,
  gradeSlots16,
  gradeCommon6,
}) => {
  const {
    activeGradeIdx,
    selectedSubskillIdx,
    setSelectedSubskillIdx,
    setActiveSlotId,
    setStudentMode,
    diagSimChoices,
    setDiagSimChoice,
    unlockedVaccines,
    completedStepsByGrade,
    completedSlots,
    smartScores,
    boostSmartScore,
    ttsRate,
  } = useCoursewareStore();

  const [showVaccineModal, setShowVaccineModal] = useState(false);
  const [showVocabDuel, setShowVocabDuel] = useState(false);
  const [showGalaxyMap, setShowGalaxyMap] = useState(false);
  const [showCatModal, setShowCatModal] = useState(false);
  const [speakingDiag, setSpeakingDiag] = useState(false);

  // Common Foundation 6-module interactive state
  const [activeCommonIdx, setActiveCommonIdx] = useState(0);
  const [commonPickedChoice, setCommonPickedChoice] = useState<Record<string, string>>({});

  const xr = gradeData.xray_overview;
  const dr = gradeData.diagnosis_report;
  const dt = gradeData.diagnostic_test;
  const activeSk = xr.subskill_matrix[selectedSubskillIdx] || xr.subskill_matrix[0];
  const activeMeta = subskillMeta.find((m) => m.code === activeSk.code) || {
    code: activeSk.code,
    name: activeSk.code,
    domain: '',
    desc: '',
  };

  const matchedSlot =
    gradeSlots16.find((s) => s.subskill_code === activeSk.code) ||
    gradeSlots16.find((s) => s.slot_id === gradeData.slot_id) ||
    gradeSlots16[0];

  const stepStatus = completedStepsByGrade[gradeData.grade_num] || {
    diag: true,
    clinic: false,
    studio: false,
  };
  const currentSmart = smartScores[gradeData.grade_num] ?? xr.overall_score;

  const handleToggleDiagTts = () => {
    if (speakingDiag) {
      stopKoreanSpeech();
      setSpeakingDiag(false);
    } else {
      setSpeakingDiag(true);
      const fullText = `${dt.passage_title}. ${dt.paragraphs.join(' ')}`;
      speakKoreanText(fullText, ttsRate, () => setSpeakingDiag(false));
    }
  };

  const handleSelectSubskillTile = (sIdx: number, code: string) => {
    setSelectedSubskillIdx(sIdx);
    const targetSlotId = `G${gradeData.grade_num}-EXP-${code}`;
    setActiveSlotId(targetSlotId);
  };

  const activeCommonSlot = gradeCommon6[activeCommonIdx] || gradeCommon6[0];

  return (
    <div className="space-y-4">
      {/* Row 0: Today's Adaptive Mission Queue & D1~D6 Vaccine Deck Bar */}
      <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
        <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3 border-b border-slate-100">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-sm font-black text-slate-900">
              🚀 오늘의 개인 맞춤형 4단계 문해력 루프 미션 ({gradeData.grade} · {gradeData.slot_id})
            </span>
            <span className="px-2 py-0.5 text-[11px] font-extrabold rounded-md bg-blue-100 text-blue-800">
              KReaD {gradeData.complexity_metrics.current_kread} ➔ 목표 {gradeData.complexity_metrics.kread_target}
            </span>
            <span className="px-2 py-0.5 text-[11px] font-extrabold rounded-md bg-emerald-100 text-emerald-800">
              수록 지문: 「{gradeData.real_csat_test.passage_title}」
            </span>
          </div>
          <div className="flex items-center gap-2 flex-wrap">
            <button
              onClick={() => setShowCatModal(true)}
              className="text-xs font-black px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white transition flex items-center gap-1.5 shadow-sm cursor-pointer"
            >
              <span>🎯 3분 CAT 적응형 진단</span>
            </button>
            <button
              onClick={() => setShowVocabDuel(true)}
              className="text-xs font-extrabold px-3 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-300 transition flex items-center gap-1.5 shadow-xs cursor-pointer"
            >
              <span>⚡ 10초 어휘 듀얼</span>
            </button>
            <button
              onClick={() => setShowGalaxyMap(true)}
              className="text-xs font-extrabold px-3 py-1.5 rounded-lg bg-indigo-50 hover:bg-indigo-100 text-indigo-900 border border-indigo-300 transition flex items-center gap-1.5 shadow-xs cursor-pointer"
            >
              <span>🌌 은하계 테라포밍 원정대</span>
            </button>
            <button
              onClick={() => setShowVaccineModal(!showVaccineModal)}
              className="text-xs font-extrabold px-3 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-300 transition flex items-center gap-1.5 cursor-pointer"
            >
              <span>🛡️ 오답 백신 도감 ({unlockedVaccines.length}/6종)</span>
              <span>{showVaccineModal ? '▲' : '▼'}</span>
            </button>
          </div>
        </div>

        {/* Collapsible D1~D6 Vaccine Collection Deck */}
        {showVaccineModal && (
          <div className="mb-4 p-3.5 rounded-xl bg-slate-900 text-white border border-slate-700">
            <div className="text-xs font-extrabold text-emerald-300 mb-2 flex items-center justify-between">
              <span>🛡️ KICE 수능 6대 매력적 오답 함정 방어 백신 도감 (클리닉 및 실전 문항 정복 시 자동 해금)</span>
              <span className="text-[11px] text-slate-400">수집 현황: {unlockedVaccines.length} / 6</span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2.5">
              {distractorMeta.map((dm) => {
                const unlocked = unlockedVaccines.includes(dm.code);
                return (
                  <div
                    key={dm.code}
                    className={`p-2.5 rounded-lg border text-xs ${
                      unlocked
                        ? 'bg-emerald-950/60 border-emerald-500/60 text-emerald-100'
                        : 'bg-slate-800/70 border-slate-700 text-slate-400 opacity-80'
                    }`}
                  >
                    <div className="flex items-center justify-between font-black mb-1">
                      <span>
                        [{dm.code}] {dm.name}
                      </span>
                      <span
                        className={`px-1.5 py-0.5 rounded text-[10px] ${
                          unlocked ? 'bg-emerald-500 text-slate-950' : 'bg-slate-700 text-slate-300'
                        }`}
                      >
                        {unlocked ? `✅ ${dm.vaccine_name}` : '🔒 미획득'}
                      </span>
                    </div>
                    <p className="text-[11px] leading-snug opacity-90">{dm.formula}</p>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* 4 Mission Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          <div className="p-3.5 rounded-xl border-2 border-blue-500 bg-blue-50/50 flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between text-xs font-extrabold text-blue-800 mb-1">
                <span>MODE 1 · 6차원 X-Ray & 코스 맵</span>
                <span className="px-2 py-0.5 rounded bg-blue-600 text-white text-[10px]">현재 화면</span>
              </div>
              <div className="font-black text-sm text-slate-900 mb-1">
                16개 하위기능 코스 선택 & 진단
              </div>
              <p className="text-xs text-slate-600">
                어디가·왜·어떻게 부족한지 6차원 지표로 투시하고 16개 전 차시 중 원하는 단원을 선택합니다.
              </p>
            </div>
            <div className="mt-3 pt-2 border-t border-blue-200/70 flex items-center justify-between text-xs font-bold text-blue-900">
              <span>진단 SmartScore: {currentSmart}점</span>
              <span>✅ 16차시 개방</span>
            </div>
          </div>

          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50 hover:border-indigo-400 transition flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between text-xs font-extrabold text-indigo-700 mb-1">
                <span>MODE 2 · 1:1 약점 처방 클리닉</span>
                <span
                  className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                    stepStatus.clinic ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'
                  }`}
                >
                  {stepStatus.clinic ? '⭕ 처방 완료' : '💊 처방 대기'}
                </span>
              </div>
              <div className="font-black text-sm text-slate-900 mb-1">
                징검다리 복습 + 사고구술 + 6대 구조도
              </div>
              <p className="text-xs text-slate-600">
                선수 학년 결손을 메우고 6대 설명 구조도와 함정 백신 O/X 드릴을 완수합니다.
              </p>
            </div>
            <button
              onClick={() => setStudentMode('clinic')}
              className="mt-3 w-full py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-extrabold transition shadow-sm"
            >
              💊 1:1 맞춤형 처방 클리닉 시작 ➔
            </button>
          </div>

          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50 hover:border-emerald-400 transition flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between text-xs font-extrabold text-emerald-700 mb-1">
                <span>MODE 3 · 스플릿 리더 스튜디오</span>
                <span
                  className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                    stepStatus.studio ? 'bg-emerald-100 text-emerald-800' : 'bg-blue-100 text-blue-800'
                  }`}
                >
                  {stepStatus.studio ? '🏆 학습 완료' : '🔥 7대 TEI 탑재'}
                </span>
              </div>
              <div className="font-black text-sm text-slate-900 mb-1 truncate">
                「{gradeData.real_csat_test.passage_title}」
              </div>
              <p className="text-xs text-slate-600">
                7종 독해 도구, 오답 시 문단 자동 스포트라이트(3단계 힌트), EBSR, 빨간펜 퇴고를 실습합니다.
              </p>
            </div>
            <button
              onClick={() => setStudentMode('studio')}
              className="mt-3 w-full py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-extrabold transition shadow-sm"
            >
              ✍️ 스플릿 리더 & 수능 스튜디오 ➔
            </button>
          </div>

          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50 hover:border-amber-400 transition flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between text-xs font-extrabold text-amber-800 mb-1">
                <span>MODE 4 · KICE CBT 모의고사</span>
                <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-slate-900 text-amber-300">
                  무보조 전이 평가
                </span>
              </div>
              <div className="font-black text-sm text-slate-900 mb-1">
                실전 타이머 · OMR · 전 선지 해부
              </div>
              <p className="text-xs text-slate-600">
                모든 힌트와 스캐폴딩을 끄고 실제 수능/성취도 평가 환경에서 실력을 검증합니다.
              </p>
            </div>
            <button
              onClick={() => setStudentMode('cbt_exam')}
              className="mt-3 w-full py-2 rounded-lg bg-slate-900 hover:bg-slate-800 text-amber-300 text-xs font-extrabold transition shadow-sm"
            >
              🏆 KICE CBT 실전 모의고사 응시 ➔
            </button>
          </div>
        </div>
      </div>

      {/* Main 2-Column 6D X-Ray Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Left Column: Dimension 1 (16 Subskills Course Map & Heatmap) + Dimension 2 (Mini Diagnostic Simulator) */}
        <div className="space-y-4">
          {/* Card 1: 16 Expository Subskills X-Ray Heatmap & Full 16-Lesson Course Launcher */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🔬 [진단 차원 ① & 정규 코스 맵] {gradeData.grade} 설명문 16대 하위기능(V1-1~W5) 전수 히트맵
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-blue-100 text-blue-800">
                셀 클릭 시 해당 차시 지문·문항 즉시 로드
              </span>
            </div>

            <div className="flex flex-wrap gap-3 text-xs font-bold text-slate-600 mb-3">
              <span>🔴 심각 결손·처방 시급 (50점↓)</span>
              <span>🟡 불안정·보강 필요 (51~69점)</span>
              <span>🟢 마스터·안정 (70점↑)</span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-3">
              {xr.subskill_matrix.map((sk, sIdx) => {
                const meta = subskillMeta.find((m) => m.code === sk.code) || { name: sk.code };
                const slotItem = gradeSlots16.find((s) => s.subskill_code === sk.code);
                const slotKey = `G${gradeData.grade_num}-EXP-${sk.code}`;
                const isDone = completedSlots[slotKey]?.studio || completedSlots[slotKey]?.clinic;
                const isSelected = sIdx === selectedSubskillIdx;
                const icon = sk.state === 'critical' ? '🔴' : sk.state === 'fragile' ? '🟡' : '🟢';
                const stateStyle =
                  sk.state === 'critical'
                    ? 'bg-rose-50 border-rose-500 text-rose-950 border-2'
                    : sk.state === 'fragile'
                    ? 'bg-amber-50 border-amber-400 text-amber-950 border'
                    : 'bg-emerald-50 border-emerald-300 text-emerald-950 border';

                return (
                  <button
                    key={sk.code}
                    onClick={() => handleSelectSubskillTile(sIdx, sk.code)}
                    className={`p-2.5 rounded-xl text-left transition-all hover:-translate-y-0.5 hover:shadow-sm ${stateStyle} ${
                      isSelected ? 'ring-2 ring-blue-600 ring-offset-1 shadow-md' : ''
                    }`}
                  >
                    <div className="flex items-center justify-between font-black text-xs">
                      <span>
                        {icon} {sk.code}
                      </span>
                      <span>{isDone ? '✅ ' : ''}{sk.score}점</span>
                    </div>
                    <div className="text-[11px] font-bold truncate mt-0.5">{meta.name}</div>
                    {slotItem && (
                      <div className="text-[10px] opacity-75 truncate mt-0.5">
                        📖 {slotItem.real_csat_test?.passage_title}
                      </div>
                    )}
                  </button>
                );
              })}
            </div>

            {/* Selected Subskill & DB Lesson Package Launcher Box */}
            <div className="bg-slate-900 text-white rounded-xl p-4 text-xs space-y-2.5 border border-slate-700">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div className="font-black text-sm text-amber-300">
                  🔎 선택된 차시 DB 패키지: [{matchedSlot?.slot_id || `G${gradeData.grade_num}-EXP-${activeSk.code}`}] {activeMeta.name}
                </div>
                <span
                  className={`px-2 py-0.5 rounded font-extrabold text-xs ${
                    activeSk.state === 'critical'
                      ? 'bg-rose-500 text-white'
                      : activeSk.state === 'fragile'
                      ? 'bg-amber-400 text-slate-950'
                      : 'bg-emerald-500 text-slate-950'
                  }`}
                >
                  현재 성취도 {activeSk.score}점 ({activeMeta.domain})
                </span>
              </div>

              {matchedSlot && (
                <div className="p-3 rounded-lg bg-slate-800/90 border border-slate-700 space-y-1">
                  <div className="font-black text-white text-xs md:text-sm">
                    📖 수록 지문: 「{matchedSlot.real_csat_test.passage_title}」
                  </div>
                  <div className="text-[11px] text-sky-300 font-bold">
                    • 연계 교과: {matchedSlot.curriculum_concept.subject} ({matchedSlot.curriculum_concept.unit}) · 구조: {matchedSlot.curriculum_concept.text_structure} · {matchedSlot.real_csat_test.passage_spec}
                  </div>
                  <div className="text-[11px] text-slate-300">
                    • Mager 수행목표: {matchedSlot.mager_goal}
                  </div>
                </div>
              )}

              <div className="text-slate-300 text-[11px]">
                👉 <b className="text-rose-300">X-Ray 진단 소견:</b> {activeSk.why}
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2 pt-1">
                <button
                  onClick={() => setStudentMode('studio')}
                  className="py-2 px-3 rounded-lg bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs transition shadow"
                >
                  📖 이 차시 본문 학습 & 수능 문항 ➔
                </button>
                <button
                  onClick={() => setStudentMode('clinic')}
                  className="py-2 px-3 rounded-lg bg-indigo-500 hover:bg-indigo-400 text-white font-black text-xs transition shadow"
                >
                  💊 이 차시 1:1 약점 처방 클리닉 ➔
                </button>
                <button
                  onClick={() => setStudentMode('cbt_exam')}
                  className="py-2 px-3 rounded-lg bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs transition shadow"
                >
                  🏆 이 차시 CBT 실전 모의고사 ➔
                </button>
              </div>
            </div>
          </div>

          {/* Card 2: Mini Diagnostic Test & Live Choice Trap Simulator */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                📝 [진단 차원 ②] 미니 진단 지문 & 실시간 오답 함정(D1~D6) 시뮬레이터
              </span>
              <div className="flex items-center gap-1.5">
                <button
                  onClick={handleToggleDiagTts}
                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold border transition ${
                    speakingDiag
                      ? 'bg-rose-600 text-white border-rose-600'
                      : 'bg-blue-50 text-blue-800 border-blue-200 hover:bg-blue-100'
                  }`}
                >
                  {speakingDiag ? '⏹️ 음성 정지' : '🔊 진단 지문 듣기'}
                </button>
                <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-blue-100 text-blue-800">
                  선지 클릭 시 오답 진단 즉시 전환
                </span>
              </div>
            </div>

            <div className="font-extrabold text-blue-900 text-sm mb-2">
              {dt.passage_title}{' '}
              <span className="text-xs font-semibold text-slate-500">({dt.passage_spec})</span>
            </div>

            <div className="reader-theme-paper border border-slate-300 rounded-xl p-3.5 text-sm leading-relaxed mb-3 space-y-2">
              {dt.paragraphs.map((para, pIdx) => (
                <p
                  key={pIdx}
                  className="indent-2"
                  dangerouslySetInnerHTML={{ __html: para }}
                />
              ))}
            </div>

            <div className="space-y-3">
              {dt.questions.map((q, qIdx) => {
                const simKey = `${activeGradeIdx}-${qIdx}`;
                const selectedNo = diagSimChoices[simKey] ?? q.student_selected;
                const pickedOpt = q.options.find((o) => o.no === selectedNo) || q.options[0];

                return (
                  <div
                    key={q.q_no}
                    className="border border-slate-200 rounded-xl p-3 bg-slate-50/80 space-y-2"
                  >
                    <div className="flex flex-wrap items-center justify-between gap-1.5">
                      <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-purple-100 text-purple-800">
                        측정 위계: {q.target_code} ({q.target_skill})
                      </span>
                      <span
                        className={`px-2 py-0.5 rounded text-xs font-extrabold ${
                          pickedOpt.is_correct
                            ? 'bg-emerald-100 text-emerald-800'
                            : 'bg-rose-100 text-rose-800'
                        }`}
                      >
                        {pickedOpt.is_correct
                          ? '⭕ 현재 선택: 정답 도달'
                          : `❌ 현재 선택(${pickedOpt.no}번): ${pickedOpt.trap}`}
                      </span>
                    </div>

                    <div className="font-extrabold text-sm text-slate-900">
                      진단 문항 {q.q_no}. {q.stem}
                    </div>

                    <div className="space-y-1.5">
                      {q.options.map((opt) => {
                        const isPicked = opt.no === selectedNo;
                        let optStyle = 'bg-white border-slate-300 text-slate-800 hover:border-blue-500';
                        let badgeEl = (
                          <span className="text-[11px] text-slate-500 shrink-0">
                            클릭 시 진단 전환: {opt.trap}
                          </span>
                        );

                        if (isPicked && !opt.is_correct) {
                          optStyle = 'bg-rose-50 border-2 border-rose-600 text-rose-950 font-bold';
                          badgeEl = (
                            <span className="px-2 py-0.5 rounded text-[11px] font-extrabold bg-rose-200 text-rose-900 shrink-0">
                              선택된 오답 · {opt.trap}
                            </span>
                          );
                        } else if (opt.is_correct) {
                          optStyle =
                            'bg-emerald-50 border-2 border-emerald-600 text-emerald-950 font-bold';
                          badgeEl = (
                            <span className="px-2 py-0.5 rounded text-[11px] font-extrabold bg-emerald-200 text-emerald-900 shrink-0">
                              {isPicked ? '선택된 정답' : '실제 정답'}
                            </span>
                          );
                        }

                        return (
                          <button
                            key={opt.no}
                            onClick={() => setDiagSimChoice(activeGradeIdx, qIdx, opt.no)}
                            className={`w-full p-2.5 rounded-lg border text-left text-xs md:text-[13px] flex flex-wrap items-center justify-between gap-2 transition ${optStyle}`}
                          >
                            <span>
                              <b>{opt.no}번.</b> {opt.text}
                            </span>
                            {badgeEl}
                          </button>
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Right Column: Dimensions 3, 4, 5, 6 */}
        <div className="space-y-4">
          {/* Card 3: Dimensions 3 & 4 (Vocab Tier 1~3 / Syntax / 6 Text Structures) */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🧬 [진단 차원 ③·④] 어휘(Tier 1·2·3) · 문장 통사 · 6대 설명 구조 정밀 진단
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-purple-100 text-purple-800">
                언어·구조 결손 해부
              </span>
            </div>

            <div className="text-xs font-extrabold text-blue-800 mb-2.5">
              • 어휘 등급(Tier 1·2·3) 및 문장·통사·담화 해독력 진단
            </div>

            <div className="space-y-2.5">
              {xr.vocab_syntax_diag.map((vs, idx) => {
                const barColor =
                  vs.status === 'danger'
                    ? 'bg-rose-600'
                    : vs.status === 'warn'
                    ? 'bg-amber-500'
                    : 'bg-emerald-600';
                const textColor =
                  vs.status === 'danger'
                    ? 'text-rose-600'
                    : vs.status === 'warn'
                    ? 'text-amber-600'
                    : 'text-emerald-600';
                const statusLabel =
                  vs.status === 'danger' ? '취약·결손' : vs.status === 'warn' ? '보통·주의' : '우수';

                return (
                  <div key={idx} className="space-y-1">
                    <div className="flex justify-between text-xs font-extrabold">
                      <span className="text-slate-800">{vs.category}</span>
                      <span className={textColor}>
                        {vs.score}점 ({statusLabel})
                      </span>
                    </div>
                    <div className="h-2.5 bg-slate-200 rounded-full overflow-hidden">
                      <div
                        className={`h-full rounded-full ${barColor}`}
                        style={{ width: `${vs.score}%` }}
                      />
                    </div>
                    <div className="text-[11px] text-slate-500">👉 {vs.detail}</div>
                  </div>
                );
              })}
            </div>

            <div className="mt-4 pt-3.5 border-t border-dashed border-slate-300">
              <div className="text-xs font-extrabold text-blue-800 mb-2.5">
                • Meyer 설명문 6대 텍스트 구조별 독해 장악력
              </div>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
                {xr.text_structure_diag.map((st, idx) => {
                  const isDanger = st.status === 'danger';
                  const barColor =
                    st.status === 'danger'
                      ? 'bg-rose-600'
                      : st.status === 'warn'
                      ? 'bg-amber-500'
                      : 'bg-emerald-600';
                  return (
                    <div
                      key={idx}
                      className={`p-2.5 rounded-xl border text-xs ${
                        isDanger
                          ? 'bg-rose-50 border-rose-300'
                          : 'bg-slate-50 border-slate-200'
                      }`}
                    >
                      <div className="flex justify-between font-extrabold">
                        <span className="truncate">{st.structure}</span>
                        <span
                          className={
                            st.status === 'danger'
                              ? 'text-rose-600'
                              : st.status === 'warn'
                              ? 'text-amber-600'
                              : 'text-emerald-600'
                          }
                        >
                          {st.score}%
                        </span>
                      </div>
                      <div className="h-1.5 bg-slate-200 rounded-full overflow-hidden mt-1.5">
                        <div
                          className={`h-full rounded-full ${barColor}`}
                          style={{ width: `${st.score}%` }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>

          {/* Card 4: Dimensions 5 & 6 (Dick & Carey Bottleneck + Trap Radar + Backtracking) */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 mb-3 border-b border-slate-100">
              <span className="font-black text-sm md:text-base text-slate-900">
                🧭 [진단 차원 ⑤·⑥] 인지 병목(Step 1·2·3) · 수능 6대 함정 취약도 · 결손 뿌리 역추적
              </span>
              <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-amber-100 text-amber-800">
                처방 알고리즘 연동
              </span>
            </div>

            <div className="font-extrabold text-xs md:text-sm text-rose-800 mb-2">
              🚨 {dr.bottleneck.diagnosis_title}
            </div>

            <div className="grid grid-cols-3 gap-2.5 my-2.5">
              {[
                { label: 'Step 1. 지문 단서 포착', rate: dr.bottleneck.step1_rate },
                { label: 'Step 2. 관계·맥락 연결', rate: dr.bottleneck.step2_rate },
                { label: 'Step 3. 구조화·선지 판별', rate: dr.bottleneck.step3_rate },
              ].map((s, idx) => {
                const isLow = s.rate < 60;
                return (
                  <div
                    key={idx}
                    className={`p-2.5 rounded-xl text-center border ${
                      isLow
                        ? 'bg-rose-50 border-2 border-rose-600'
                        : 'bg-slate-50 border-slate-200'
                    }`}
                  >
                    <div className="text-[11px] font-bold text-slate-700">{s.label}</div>
                    <div
                      className={`text-lg font-black mt-0.5 ${
                        isLow ? 'text-rose-600' : 'text-slate-900'
                      }`}
                    >
                      {s.rate}%
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="text-xs bg-rose-50 border-l-4 border-rose-600 p-2.5 rounded-md text-rose-950 mb-3.5 leading-relaxed">
              {dr.bottleneck.diagnosis_detail}
            </div>

            <div className="text-xs font-extrabold text-slate-700 mb-2">
              • 수능 6대 매력적 오답 공식(D1~D6) 취약 지수
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-3.5">
              {dr.trap_radar.map((t) => {
                const highRisk = t.vuln >= 75;
                const barColor =
                  t.vuln >= 75
                    ? 'bg-rose-600'
                    : t.vuln >= 50
                    ? 'bg-amber-500'
                    : 'bg-emerald-600';
                return (
                  <div
                    key={t.code}
                    className={`p-2 rounded-lg border text-xs ${
                      highRisk
                        ? 'bg-rose-50/80 border-rose-300'
                        : 'bg-slate-50 border-slate-200'
                    }`}
                  >
                    <div className="flex justify-between font-extrabold">
                      <span>
                        [{t.code}] {t.name}
                      </span>
                      <span className={highRisk ? 'text-rose-600' : 'text-slate-600'}>
                        취약도 {t.vuln}%
                      </span>
                    </div>
                    <div className="h-1.5 bg-slate-200 rounded-full overflow-hidden mt-1">
                      <div
                        className={`h-full rounded-full ${barColor}`}
                        style={{ width: `${t.vuln}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="text-xs font-extrabold text-slate-700 mb-2">
              • 종적 위계 결손 뿌리 역추적(Root-Cause Backtracking) 경로
            </div>
            <div className="space-y-2">
              {dr.backtracking_path.map((node, idx) => {
                const nodeStyle =
                  node.status === 'review'
                    ? 'bg-amber-50 border-2 border-amber-400'
                    : node.status === 'target'
                    ? 'bg-blue-50 border-2 border-blue-600'
                    : 'bg-slate-50 border border-slate-200';
                const badgeStyle =
                  node.status === 'review'
                    ? 'bg-amber-200 text-amber-900'
                    : node.status === 'target'
                    ? 'bg-blue-200 text-blue-900'
                    : 'bg-emerald-200 text-emerald-900';

                return (
                  <div
                    key={idx}
                    className={`flex items-center gap-3 p-2.5 rounded-xl text-xs ${nodeStyle}`}
                  >
                    <span className={`px-2 py-0.5 rounded font-extrabold shrink-0 ${badgeStyle}`}>
                      {node.grade}
                    </span>
                    <div>
                      <div className="font-black text-slate-900">{node.code}</div>
                      <div className="text-slate-600">{node.title}</div>
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="mt-4 flex flex-wrap justify-end gap-2">
              <button
                onClick={() => setStudentMode('clinic')}
                className="px-4 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs md:text-sm font-extrabold shadow transition"
              >
                💊 진단된 결손({gradeData.slot_id}) 1:1 맞춤형 처방 클리닉으로 이동 ➔
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Row 3: 6 Common Foundation (COM-A1~A6) Interactive Remedial Bridge Modules */}
      {gradeCommon6.length > 0 && activeCommonSlot && (
        <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-3">
          <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 border-b border-slate-100">
            <div>
              <span className="px-2 py-0.5 rounded text-[11px] font-extrabold bg-indigo-100 text-indigo-800">
                공통기초 36개 위계 DB 연동 ({gradeData.grade} A1~A6)
              </span>
              <h3 className="text-sm md:text-base font-black text-slate-900 mt-1">
                🪜 {gradeData.grade} 공통 언어·사고 기초 6대 징검다리 훈련실 (COM-A1 ~ COM-A6)
              </h3>
            </div>
            <div className="flex flex-wrap gap-1.5">
              {gradeCommon6.map((cm, idx) => (
                <button
                  key={cm.code}
                  onClick={() => setActiveCommonIdx(idx)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-extrabold border transition ${
                    activeCommonIdx === idx
                      ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  {cm.code} · {cm.layer.split(' ')[1] || cm.layer}
                </button>
              ))}
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start text-xs">
            <div className="lg:col-span-5 p-3.5 rounded-xl bg-amber-50/70 border border-amber-200 space-y-2">
              <div className="font-black text-amber-950 text-sm">
                📌 [{activeCommonSlot.code}] {activeCommonSlot.title}
              </div>
              <div className="text-amber-900 leading-relaxed">{activeCommonSlot.rule_box}</div>
              <div className="p-2.5 rounded-lg bg-white border border-amber-200 text-slate-700">
                <b>Mager 목표:</b> {activeCommonSlot.mager_reading}
              </div>
            </div>

            <div className="lg:col-span-7 p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-2.5">
              <div className="font-black text-slate-900">
                📖 징검다리 예문: <span className="font-normal text-slate-700">{activeCommonSlot.passage_snippet}</span>
              </div>
              <div className="font-extrabold text-indigo-900">
                Q. {activeCommonSlot.mini_question}
              </div>
              <div className="flex flex-wrap gap-2">
                {activeCommonSlot.choices.map((ch) => {
                  const picked = commonPickedChoice[activeCommonSlot.code];
                  const isThisPicked = picked === ch;
                  const isCorrect = ch === activeCommonSlot.correct;
                  return (
                    <button
                      key={ch}
                      onClick={() => {
                        setCommonPickedChoice((prev) => ({
                          ...prev,
                          [activeCommonSlot.code]: ch,
                        }));
                        if (isCorrect) {
                          boostSmartScore(gradeData.grade_num, 2, activeCommonSlot.code);
                        }
                      }}
                      className={`px-3.5 py-2 rounded-xl border font-bold transition ${
                        isThisPicked
                          ? isCorrect
                            ? 'bg-emerald-600 text-white border-emerald-600'
                            : 'bg-rose-600 text-white border-rose-600'
                          : 'bg-white text-slate-800 border-slate-300 hover:border-indigo-500'
                      }`}
                    >
                      {ch}
                    </button>
                  );
                })}
              </div>
              {commonPickedChoice[activeCommonSlot.code] && (
                <div
                  className={`p-2.5 rounded-lg border font-bold ${
                    commonPickedChoice[activeCommonSlot.code] === activeCommonSlot.correct
                      ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                      : 'bg-rose-50 border-rose-300 text-rose-900'
                  }`}
                >
                  {commonPickedChoice[activeCommonSlot.code] === activeCommonSlot.correct
                    ? `⭕ 정답입니다! ${activeCommonSlot.feedback}`
                    : `❌ 다시 생각해 볼까요? 힌트: ${activeCommonSlot.feedback}`}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Vocab Duel Modal */}
      {showVocabDuel && (
        <VocabDuelArena
          vocabList={gradeData.real_csat_test.vocab_notes || []}
          onClose={() => setShowVocabDuel(false)}
        />
      )}

      {/* Galaxy Expedition Terraforming Map Modal */}
      {showGalaxyMap && (
        <GalaxyExpeditionMap onClose={() => setShowGalaxyMap(false)} />
      )}

      {/* Mode 1: Onboarding CAT Diagnostic Modal */}
      {showCatModal && (
        <OnboardingCatModal
          gradeData={gradeData}
          onClose={() => setShowCatModal(false)}
        />
      )}
    </div>
  );
};
