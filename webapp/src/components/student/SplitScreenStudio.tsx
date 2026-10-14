import React, { useState, useEffect, useRef } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { speakKoreanText, stopKoreanSpeech } from '../../utils/ttsEngine';
import type { GradeData, VocabNote, HighlightColorType } from '../../types/courseware';
import {
  EyeBeaconGuide,
  GraphicOrganizerBuilder,
  InlineClozeBuilder,
  WritingWorkbench,
} from '../tei';

interface SplitScreenStudioProps {
  gradeData: GradeData;
}

// Helper to inject syntactic slash (/) chunking for Korean expository sentences
function applySyntacticChunking(html: string): string {
  return html
    .split(/(<[^>]+>)/g)
    .map((segment) => {
      if (segment.startsWith('<')) return segment;
      return segment
        .replace(/(은|는|이|가|에서|에게|으로|로|에는|에도)\s+/g, '$1 <span class="text-blue-500 font-bold select-none">/</span> ')
        .replace(/(고,|며,|지만,|거나,|아서|어서|므로|면)\s+/g, '$1 <span class="text-indigo-500 font-bold select-none">//</span> ');
    })
    .join('');
}

export const SplitScreenStudio: React.FC<SplitScreenStudioProps> = ({ gradeData }) => {
  const {
    readerTheme,
    setReaderTheme,
    fontSize,
    setFontSize,
    showParaNumbers,
    toggleParaNumbers,
    showSlashChunking,
    toggleSlashChunking,
    showFocusRuler,
    toggleFocusRuler,
    activeHighlightColor,
    setActiveHighlightColor,
    ttsRate,
    setTtsRate,
    isTwoColumnMode,
    toggleTwoColumnMode,
    savedVocab,
    saveVocabWord,
    removeVocabWord,
    clueNotesByGrade,
    addClueNote,
    removeClueNote,
    boostSmartScore,
    unlockVaccine,
    markStepComplete,
    setStudentMode,
  } = useCoursewareStore();

  const csat = gradeData.real_csat_test;
  const comm = gradeData.commercial;
  const ebsr = comm.ebsr_question;
  const wb = comm.writing_workbench;

  // Active right-pane tab: 'csat' | 'ebsr' | 'organizer' | 'cloze' | 'writing'
  const [rightTab, setRightTab] = useState<'csat' | 'ebsr' | 'organizer' | 'cloze' | 'writing'>('csat');

  // Question solving state
  const [wrongAttempts, setWrongAttempts] = useState<Record<number, number>>({});
  const [pickedHistory, setPickedHistory] = useState<Record<number, number[]>>({});
  const [solvedMap, setSolvedMap] = useState<Record<number, boolean>>({});
  const [activeQuestionIdx, setActiveQuestionIdx] = useState<number>(0);

  // Spotlight paragraph index triggered by scaffolding
  const [spotlightState, setSpotlightState] = useState<{
    paraIdx: number;
    quote: string;
    qNo: number;
  } | null>(null);

  // Active Focused Paragraph (for Focus Line Ruler mode)
  const [focusedParaIdx, setFocusedParaIdx] = useState<number>(0);

  // Active Vocab Popover
  const [activeVocab, setActiveVocab] = useState<VocabNote | null>(null);

  // Drawer & Popover UI toggles
  const [showClueDrawer, setShowClueDrawer] = useState<boolean>(false);
  const [showSettingsPopover, setShowSettingsPopover] = useState<boolean>(false);
  const [customClueInput, setCustomClueInput] = useState<string>('');

  // TTS state
  const [isSpeaking, setIsSpeaking] = useState<boolean>(false);

  // EBSR (TEI-2) state
  const [ebsrPartA, setEbsrPartA] = useState<number | null>(null);
  const [ebsrPartB, setEbsrPartB] = useState<number | null>(null);

  const paraRefs = useRef<Record<number, HTMLParagraphElement | null>>({});

  // Reset state on slot change
  useEffect(() => {
    stopKoreanSpeech();
    setIsSpeaking(false);
    setWrongAttempts({});
    setPickedHistory({});
    setSolvedMap({});
    setSpotlightState(null);
    setFocusedParaIdx(0);
    setActiveQuestionIdx(0);
    setActiveVocab(null);
    setEbsrPartA(null);
    setEbsrPartB(null);
  }, [gradeData.id, gradeData.slot_id]);

  const handleToggleTts = () => {
    if (isSpeaking) {
      stopKoreanSpeech();
      setIsSpeaking(false);
    } else {
      setIsSpeaking(true);
      const text = `${csat.passage_title}. ${csat.paragraphs.join(' ')}`;
      speakKoreanText(text, ttsRate, () => setIsSpeaking(false));
    }
  };

  // Drag text selection handler to save clue note
  const handlePassageMouseUp = () => {
    if (typeof window === 'undefined') return;
    const sel = window.getSelection()?.toString().trim();
    if (sel && sel.length >= 2 && sel.length <= 120) {
      const tagLabel =
        activeHighlightColor === 'yellow'
          ? '중심 문장'
          : activeHighlightColor === 'blue'
          ? '구조 표지'
          : '핵심 어휘';
      addClueNote(gradeData.grade_num, sel, activeHighlightColor, tagLabel);
    }
  };

  // Option selection handler
  const handleSelectCsatOption = (qNo: number, optNo: number, isCorrect: boolean, formula: string) => {
    const prevPicks = pickedHistory[qNo] || [];
    if (!prevPicks.includes(optNo)) {
      setPickedHistory((prev) => ({ ...prev, [qNo]: [...prevPicks, optNo] }));
    }

    const scaff = comm.question_scaffolding.find((s) => s.q_no === qNo);

    if (isCorrect) {
      setSolvedMap((prev) => ({ ...prev, [qNo]: true }));
      const prevWrong = wrongAttempts[qNo] || 0;
      const delta = prevWrong === 0 ? 8 : prevWrong === 1 ? 5 : 3;
      boostSmartScore(gradeData.grade_num, delta);
      markStepComplete(gradeData.grade_num, 'studio');

      const qObj = csat.questions.find((q) => q.q_no === qNo);
      qObj?.options.forEach((o) => {
        const m = o.formula.match(/D[1-6]/);
        if (m) unlockVaccine(m[0]);
      });
    } else {
      const nextWrong = (wrongAttempts[qNo] || 0) + 1;
      setWrongAttempts((prev) => ({ ...prev, [qNo]: nextWrong }));

      const m = formula.match(/D[1-6]/);
      if (m) unlockVaccine(m[0]);

      if (scaff) {
        setSpotlightState({
          paraIdx: scaff.target_para_idx,
          quote: scaff.spotlight_quote,
          qNo,
        });
        setFocusedParaIdx(scaff.target_para_idx);
        const el = paraRefs.current[scaff.target_para_idx];
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    }
  };

  const currentClues = clueNotesByGrade[gradeData.grade_num] || [];
  const currentQuestion = csat.questions[activeQuestionIdx] || csat.questions[0];

  return (
    <div className="space-y-4 font-sans selection:bg-amber-200 selection:text-slate-900">
      {/* 1. ZEN FOCUS HEADER (Minimal & Elegant) */}
      <div className="bg-white rounded-2xl border border-slate-200/90 px-4 py-3 shadow-xs flex flex-wrap items-center justify-between gap-3">
        {/* Left: Passage Title & Breadcrumb */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setStudentMode('portal')}
            className="p-1.5 rounded-lg text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition text-xs font-bold flex items-center gap-1 cursor-pointer"
            title="과제함 목록으로 돌아가기"
          >
            <span>←</span>
            <span className="hidden sm:inline">과제함</span>
          </button>
          <div className="h-4 w-px bg-slate-200" />
          <div className="flex items-center gap-2 flex-wrap">
            <span className="px-2 py-0.5 rounded-md text-[11px] font-bold bg-blue-50 text-blue-700 border border-blue-200">
              {gradeData.curriculum_concept.subject}
            </span>
            <h1 className="font-black text-sm sm:text-base text-slate-900 tracking-tight">
              {csat.passage_title}
            </h1>
          </div>
        </div>

        {/* Center/Right: Ergonomic Reading Controls */}
        <div className="flex items-center gap-2 flex-wrap">
          {/* 3-Color Highlighter Dots */}
          <div className="flex items-center gap-1.5 bg-slate-50 border border-slate-200 rounded-xl px-2.5 py-1">
            <span className="text-[11px] font-bold text-slate-500 mr-1 hidden md:inline">형광펜:</span>
            {(
              [
                { id: 'yellow', label: '중심', bg: 'bg-amber-400', border: 'border-amber-500' },
                { id: 'blue', label: '구조', bg: 'bg-sky-400', border: 'border-sky-500' },
                { id: 'pink', label: '어휘', bg: 'bg-pink-400', border: 'border-pink-500' },
              ] as const
            ).map((hl) => (
              <button
                key={hl.id}
                onClick={() => setActiveHighlightColor(hl.id)}
                className={`w-5 h-5 rounded-full ${hl.bg} transition transform hover:scale-110 cursor-pointer ${
                  activeHighlightColor === hl.id
                    ? `ring-2 ring-offset-1 ring-slate-800 scale-110`
                    : 'opacity-70 hover:opacity-100'
                }`}
                title={`${hl.label} 형광펜 선택 (지문 드래그 시 자동 칠하기)`}
              />
            ))}
          </div>

          {/* Syntactic Slash Chunking Toggle */}
          <button
            onClick={toggleSlashChunking}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1 cursor-pointer ${
              showSlashChunking
                ? 'bg-indigo-600 text-white shadow-xs'
                : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200'
            }`}
            title="문장의 주어·조사 단위로 슬래시(/)를 자동 삽입하여 독해 속도를 높입니다"
          >
            <span>/</span>
            <span>끊어읽기</span>
          </button>

          {/* Korean TTS Listen */}
          <button
            onClick={handleToggleTts}
            className={`px-3 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer ${
              isSpeaking
                ? 'bg-rose-600 text-white animate-pulse'
                : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200'
            }`}
          >
            <span>{isSpeaking ? '⏹️ 정지' : '🔊 지문 듣기'}</span>
          </button>

          {/* Reading Display Settings Popover Toggle */}
          <div className="relative">
            <button
              onClick={() => setShowSettingsPopover(!showSettingsPopover)}
              className="px-2.5 py-1.5 rounded-xl text-xs font-bold bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1 cursor-pointer"
              title="글자 크기, 문단 번호, 초점 가이드 설정"
            >
              <span>⚙️ 보기 설정</span>
            </button>

            {showSettingsPopover && (
              <div className="absolute right-0 mt-2 w-56 bg-white rounded-2xl border border-slate-200 shadow-xl p-3 z-50 space-y-3 text-xs animate-in fade-in zoom-in-95">
                <div className="font-bold text-slate-800 pb-1.5 border-b border-slate-100 flex justify-between items-center">
                  <span>독서 환경 맞춤 설정</span>
                  <button
                    onClick={() => setShowSettingsPopover(false)}
                    className="text-slate-400 hover:text-slate-600"
                  >
                    ✕
                  </button>
                </div>

                {/* Font Size */}
                <div className="space-y-1">
                  <span className="text-[11px] text-slate-500 font-bold">글자 크기:</span>
                  <div className="grid grid-cols-3 gap-1">
                    {(['sm', 'md', 'lg'] as const).map((fs) => (
                      <button
                        key={fs}
                        onClick={() => setFontSize(fs)}
                        className={`py-1 rounded-lg font-bold text-center border ${
                          fontSize === fs
                            ? 'bg-blue-600 text-white border-blue-600'
                            : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                        }`}
                      >
                        {fs === 'sm' ? '작게' : fs === 'md' ? '보통' : '크게'}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Paragraph Numbers */}
                <div className="flex items-center justify-between pt-1">
                  <span className="text-slate-700 font-bold">문단 번호 (#)</span>
                  <input
                    type="checkbox"
                    checked={showParaNumbers}
                    onChange={toggleParaNumbers}
                    className="rounded accent-blue-600 w-4 h-4 cursor-pointer"
                  />
                </div>

                {/* Focus Ruler */}
                <div className="flex items-center justify-between">
                  <span className="text-slate-700 font-bold">🎯 문단 집중 리더</span>
                  <input
                    type="checkbox"
                    checked={showFocusRuler}
                    onChange={toggleFocusRuler}
                    className="rounded accent-blue-600 w-4 h-4 cursor-pointer"
                  />
                </div>

                {/* Two-Column Mode */}
                <div className="flex items-center justify-between">
                  <span className="text-slate-700 font-bold">📰 수능 2단 시험지 뷰</span>
                  <input
                    type="checkbox"
                    checked={isTwoColumnMode}
                    onChange={toggleTwoColumnMode}
                    className="rounded accent-blue-600 w-4 h-4 cursor-pointer"
                  />
                </div>
              </div>
            )}
          </div>

          {/* Clues & Vocab Drawer Button */}
          <button
            onClick={() => setShowClueDrawer(!showClueDrawer)}
            className="px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-300 transition flex items-center gap-1 cursor-pointer"
          >
            <span>📌 단서 ({currentClues.length})</span>
          </button>
        </div>
      </div>

      {/* Collapsible Clue Notes Drawer */}
      {showClueDrawer && (
        <div className="bg-amber-50/50 rounded-2xl border border-amber-200 p-4 shadow-sm space-y-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="font-black text-xs text-amber-950">📌 내가 수집한 독서 단서 및 메모</span>
              <span className="text-[11px] text-amber-800">
                (본문 문장을 드래그하면 자동으로 저장됩니다)
              </span>
            </div>
            <button
              onClick={() => setShowClueDrawer(false)}
              className="text-xs text-amber-700 hover:text-amber-950 font-bold"
            >
              닫기 ✕
            </button>
          </div>

          {/* Quick Memo Input */}
          <div className="flex gap-2">
            <input
              type="text"
              value={customClueInput}
              onChange={(e) => setCustomClueInput(e.target.value)}
              placeholder="기억할 핵심 단서나 내 생각을 직접 적어보세요..."
              className="flex-1 px-3 py-1.5 rounded-xl border border-amber-300/80 bg-white text-xs outline-none focus:ring-2 focus:ring-amber-500"
              onKeyDown={(e) => {
                if (e.key === 'Enter' && customClueInput.trim()) {
                  addClueNote(gradeData.grade_num, customClueInput.trim(), activeHighlightColor, '직접 메모');
                  setCustomClueInput('');
                }
              }}
            />
            <button
              onClick={() => {
                if (customClueInput.trim()) {
                  addClueNote(gradeData.grade_num, customClueInput.trim(), activeHighlightColor, '직접 메모');
                  setCustomClueInput('');
                }
              }}
              className="px-3 py-1.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold cursor-pointer"
            >
              저장
            </button>
          </div>

          {/* Saved Clues List */}
          {currentClues.length === 0 ? (
            <p className="text-xs text-amber-800/70 italic py-1">
              아직 저장된 단서가 없습니다. 본문 텍스트를 드래그하거나 위 입력창에 적어보세요.
            </p>
          ) : (
            <div className="flex flex-wrap gap-2 max-h-32 overflow-y-auto pt-1">
              {currentClues.map((c) => (
                <div
                  key={c.id}
                  className="bg-white border border-amber-200/90 rounded-lg px-2.5 py-1 text-xs text-slate-800 flex items-center gap-2 shadow-2xs"
                >
                  <span className="font-bold text-amber-800 text-[10px]">[{c.tag}]</span>
                  <span>{c.text}</span>
                  <button
                    onClick={() => removeClueNote(gradeData.grade_num, c.id)}
                    className="text-slate-400 hover:text-rose-600 font-bold text-[11px]"
                  >
                    ×
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {/* 2. SPLIT-SCREEN WORKSPACE: LEFT PASSAGE (55%) : RIGHT QUESTIONS (45%) */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
        {/* ================= LEFT PANE: PURE READING SANCTUARY (6 cols on lg) ================= */}
        <div className="lg:col-span-7 bg-[#FCFBF7] rounded-3xl border border-stone-200/90 p-6 sm:p-8 shadow-sm lg:sticky lg:top-20 max-h-[calc(100vh-100px)] overflow-y-auto">
          {/* Passage Header */}
          <div className="pb-4 mb-6 border-b border-stone-200 flex items-baseline justify-between gap-3">
            <div>
              <span className="text-[11px] font-bold text-stone-500 tracking-wider uppercase block">
                EXPOSITORY PASSAGE
              </span>
              <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight mt-0.5 font-serif">
                {csat.passage_title}
              </h2>
            </div>
            <span className="text-xs font-medium text-stone-500 shrink-0">
              {csat.paragraphs.length}개 문단 · {csat.passage_spec}
            </span>
          </div>

          {/* Scaffolding Spotlight Alert Banner (Appears only when wrong) */}
          {spotlightState && (
            <div className="mb-6 p-3.5 rounded-2xl bg-amber-50 border border-amber-300 text-xs text-amber-950 flex items-center justify-between gap-3 animate-fade-in">
              <div className="flex items-center gap-2">
                <span className="text-base">💡</span>
                <div>
                  <span className="font-black">
                    {spotlightState.qNo}번 문제의 정답 단서가 있는 [{spotlightState.paraIdx + 1}문단]을 강조했습니다.
                  </span>
                  <p className="text-amber-800 text-[11px] mt-0.5">
                    해당 문단을 다시 천천히 정독하고 우측 문제를 풀어보세요.
                  </p>
                </div>
              </div>
              <button
                onClick={() => setSpotlightState(null)}
                className="text-amber-700 hover:text-amber-950 font-bold px-2 py-1 rounded-lg hover:bg-amber-100 text-[11px]"
              >
                닫기 ✕
              </button>
            </div>
          )}

          {/* Pure Reading Text Area */}
          <div
            onMouseUp={handlePassageMouseUp}
            className={`font-serif text-slate-850 selection:bg-amber-200 ${
              fontSize === 'sm'
                ? 'text-[15px] leading-[2.0]'
                : fontSize === 'lg'
                ? 'text-[18px] sm:text-[19px] leading-[2.3]'
                : 'text-[16.5px] sm:text-[17.5px] leading-[2.15]'
            } ${isTwoColumnMode ? 'columns-1 sm:columns-2 gap-8' : 'space-y-6'}`}
          >
            {csat.paragraphs.map((paraText, idx) => {
              const isSpotlighted = spotlightState?.paraIdx === idx;
              const isFocused = focusedParaIdx === idx;
              const isDimmed = showFocusRuler && !isFocused;

              // Apply syntactic slash chunking if toggled
              const renderedContent = showSlashChunking
                ? applySyntacticChunking(paraText)
                : paraText;

              return (
                <div
                  key={idx}
                  ref={(el) => {
                    paraRefs.current[idx] = el;
                  }}
                  onClick={() => setFocusedParaIdx(idx)}
                  className={`relative p-3.5 rounded-2xl transition-all duration-200 ${
                    isSpotlighted
                      ? 'bg-amber-100/70 ring-2 ring-amber-400 shadow-xs'
                      : isFocused && showFocusRuler
                      ? 'bg-white shadow-xs ring-1 ring-slate-300'
                      : isDimmed
                      ? 'opacity-35 hover:opacity-80'
                      : 'hover:bg-stone-100/50'
                  }`}
                >
                  {/* Paragraph Number Index Marker */}
                  {showParaNumbers && (
                    <span className="inline-block font-mono text-[11px] font-bold text-stone-500 mr-2 select-none px-1.5 py-0.5 rounded bg-stone-200/60">
                      {String(idx + 1).padStart(2, '0')}
                    </span>
                  )}

                  {/* Paragraph Text with Line Height */}
                  <span
                    className="text-slate-800 tracking-normal break-keep"
                    dangerouslySetInnerHTML={{ __html: renderedContent }}
                  />
                </div>
              );
            })}
          </div>

          {/* Inline Vocabulary Footer Cards */}
          {csat.vocab_notes && csat.vocab_notes.length > 0 && (
            <div className="mt-8 pt-5 border-t border-stone-200 space-y-2">
              <span className="text-[11px] font-bold text-stone-500 uppercase tracking-wider block">
                KEY CONCEPTS & VOCABULARY
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                {csat.vocab_notes.map((vn) => (
                  <div
                    key={vn.word}
                    className="bg-white rounded-xl border border-stone-200/80 p-2.5 text-xs space-y-0.5"
                  >
                    <div className="flex items-center justify-between">
                      <b className="text-slate-900 font-bold">{vn.word}</b>
                      <span className="text-[10px] text-stone-500 font-mono">{vn.tier}</span>
                    </div>
                    <p className="text-slate-600 text-[11px] leading-snug">{vn.desc}</p>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* ================= RIGHT PANE: FOCUS PROBLEM WORKSPACE (5 cols on lg) ================= */}
        <div className="lg:col-span-5 space-y-4">
          {/* Segmented Mode Switcher */}
          <div className="bg-white rounded-2xl border border-slate-200/90 p-1.5 shadow-xs flex gap-1">
            <button
              onClick={() => setRightTab('csat')}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'csat'
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              ✍️ 수능 실전 문제
            </button>
            <button
              onClick={() => setRightTab('ebsr')}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'ebsr'
                  ? 'bg-indigo-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              🔗 근거 연동(EBSR)
            </button>
            <button
              onClick={() => setRightTab('organizer')}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'organizer'
                  ? 'bg-emerald-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              🧩 구조도
            </button>
          </div>

          {/* TAB 1: Real CSAT Questions Focus Card */}
          {rightTab === 'csat' && (
            <div className="space-y-4">
              {/* Question Pagination Selector Bar */}
              <div className="bg-white rounded-2xl border border-slate-200/90 p-2.5 shadow-xs flex items-center justify-between gap-2">
                <div className="flex items-center gap-1.5">
                  <span className="text-xs font-bold text-slate-500 mr-1">문항:</span>
                  {csat.questions.map((q, idx) => {
                    const isSolved = solvedMap[q.q_no];
                    const isCurrent = activeQuestionIdx === idx;
                    return (
                      <button
                        key={q.q_no}
                        onClick={() => setActiveQuestionIdx(idx)}
                        className={`w-8 h-8 rounded-xl text-xs font-black transition flex items-center justify-center cursor-pointer ${
                          isCurrent
                            ? 'bg-blue-600 text-white shadow-xs'
                            : isSolved
                            ? 'bg-emerald-100 text-emerald-800'
                            : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                        }`}
                      >
                        {q.q_no}
                        {isSolved && <span className="text-[9px] absolute -top-1 -right-1">✓</span>}
                      </button>
                    );
                  })}
                </div>

                <span className="text-xs font-bold text-slate-500">
                  {Object.keys(solvedMap).length} / {csat.questions.length} 완료
                </span>
              </div>

              {/* Active Single Question Presentation Card */}
              {currentQuestion && (() => {
                const q = currentQuestion;
                const attempts = wrongAttempts[q.q_no] || 0;
                const pickedList = pickedHistory[q.q_no] || [];
                const isSolved = solvedMap[q.q_no] || false;
                const scaff = comm.question_scaffolding.find((s) => s.q_no === q.q_no);

                return (
                  <div className="bg-white rounded-3xl border border-slate-200/90 p-5 sm:p-6 shadow-sm space-y-4">
                    {/* Question Header & Stem */}
                    <div className="space-y-2">
                      <div className="flex items-center justify-between gap-2">
                        <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-50 text-blue-700 border border-blue-200">
                          {q.archetype}
                        </span>
                        {isSolved ? (
                          <span className="text-xs font-black text-emerald-600 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200 flex items-center gap-1">
                            <span>✓</span> 정답 완료
                          </span>
                        ) : attempts > 0 ? (
                          <span className="text-xs font-bold text-amber-700 bg-amber-50 px-2.5 py-0.5 rounded-full border border-amber-200">
                            힌트 가동 중 ({attempts}회 시도)
                          </span>
                        ) : (
                          <span className="text-xs text-slate-400">배점 3점</span>
                        )}
                      </div>

                      <h3
                        className="text-base sm:text-lg font-black text-slate-900 leading-snug tracking-tight"
                        dangerouslySetInnerHTML={{ __html: `[${q.q_no}번] ${q.stem}` }}
                      />
                    </div>

                    {/* <보기> Box if present */}
                    {q.bogi && (
                      <div
                        className="bg-stone-50 border border-stone-200 rounded-2xl p-4 text-xs sm:text-[13px] text-slate-800 whitespace-pre-line leading-relaxed font-serif"
                        dangerouslySetInnerHTML={{ __html: q.bogi }}
                      />
                    )}

                    {/* Progressive Scaffolding Hint (Clean Accordion) */}
                    {!isSolved && attempts >= 1 && scaff && (
                      <div className="p-3.5 rounded-2xl bg-amber-50 border border-amber-200 text-xs text-amber-950 space-y-1.5 animate-fade-in">
                        <div className="font-bold flex items-center justify-between">
                          <span>💡 1단계 힌트: 지문 {scaff.target_para_idx + 1}문단과 연계됩니다</span>
                          <button
                            onClick={() => {
                              setSpotlightState({
                                paraIdx: scaff.target_para_idx,
                                quote: scaff.spotlight_quote,
                                qNo: q.q_no,
                              });
                              paraRefs.current[scaff.target_para_idx]?.scrollIntoView({
                                behavior: 'smooth',
                                block: 'center',
                              });
                            }}
                            className="underline font-black text-amber-800 hover:text-amber-950 cursor-pointer"
                          >
                            좌측 단서 보기 ➔
                          </button>
                        </div>
                        <p className="text-amber-900 leading-relaxed">{scaff.step1_hint}</p>
                      </div>
                    )}

                    {/* 5-Choice Options List */}
                    <div className="space-y-2 pt-1">
                      {q.options.map((opt) => {
                        const wasPicked = pickedList.includes(opt.no);
                        const isThisCorrect = opt.is_correct;

                        let cardStyle =
                          'bg-white border-slate-200/90 text-slate-800 hover:border-blue-400 hover:bg-blue-50/20';

                        if (wasPicked && isThisCorrect) {
                          cardStyle =
                            'bg-emerald-50 border-emerald-500 text-emerald-950 font-bold ring-1 ring-emerald-500';
                        } else if (wasPicked && !isThisCorrect) {
                          cardStyle =
                            'bg-rose-50/80 border-rose-300 text-rose-900 line-through opacity-75';
                        } else if (isSolved && isThisCorrect) {
                          cardStyle =
                            'bg-emerald-50/60 border-emerald-400 text-emerald-950 font-semibold';
                        }

                        return (
                          <div key={opt.no} className="space-y-1">
                            <button
                              onClick={() =>
                                handleSelectCsatOption(q.q_no, opt.no, opt.is_correct, opt.formula)
                              }
                              className={`w-full p-3.5 rounded-2xl border text-left text-xs sm:text-[13.5px] transition flex items-start gap-3 cursor-pointer ${cardStyle}`}
                            >
                              <span className="w-5 h-5 rounded-full border border-current flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
                                {opt.no}
                              </span>
                              <span className="flex-1 leading-snug">{opt.text}</span>
                            </button>

                            {/* Detailed Explanation on Pick or Solved */}
                            {(wasPicked || isSolved) && (
                              <div
                                className={`px-3 py-2 rounded-xl text-xs leading-relaxed ${
                                  opt.is_correct
                                    ? 'bg-emerald-50 text-emerald-900 border border-emerald-200'
                                    : 'bg-slate-50 text-slate-600 border border-slate-200'
                                }`}
                              >
                                <span className="font-bold mr-1">[{opt.formula}]</span>
                                <span dangerouslySetInnerHTML={{ __html: opt.explanation }} />
                              </div>
                            )}
                          </div>
                        );
                      })}
                    </div>

                    {/* Question Bottom Next/Prev Navigation */}
                    <div className="pt-2 flex items-center justify-between border-t border-slate-100">
                      <button
                        onClick={() =>
                          setActiveQuestionIdx(Math.max(0, activeQuestionIdx - 1))
                        }
                        disabled={activeQuestionIdx === 0}
                        className="px-3 py-1.5 rounded-xl text-xs font-bold text-slate-600 hover:bg-slate-100 disabled:opacity-30 cursor-pointer"
                      >
                        ← 이전 문항
                      </button>

                      {activeQuestionIdx < csat.questions.length - 1 ? (
                        <button
                          onClick={() => setActiveQuestionIdx(activeQuestionIdx + 1)}
                          className="px-4 py-1.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-xs transition cursor-pointer"
                        >
                          다음 문항 ➔
                        </button>
                      ) : (
                        <button
                          onClick={() => setRightTab('ebsr')}
                          className="px-4 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-xs transition cursor-pointer"
                        >
                          2단계 심화(EBSR)로 이동 ➔
                        </button>
                      )}
                    </div>
                  </div>
                );
              })()}
            </div>
          )}

          {/* TAB 2: TEI-2 EBSR (Evidence-Based Selected Response) */}
          {rightTab === 'ebsr' && (
            <div className="bg-white rounded-3xl border border-slate-200/90 p-5 sm:p-6 shadow-sm space-y-4">
              <div className="pb-3 border-b border-slate-100">
                <span className="text-[11px] font-bold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md border border-indigo-200">
                  TEI-2 PISA 근거 연동형
                </span>
                <h3 className="font-black text-base text-slate-900 mt-1">
                  {ebsr.archetype}
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  [Part A] 추론 결론과 [Part B] 본문 근거를 함께 매핑해야 합니다.
                </p>
              </div>

              {/* Part A */}
              <div className="p-4 rounded-2xl border border-slate-200 bg-slate-50/70 space-y-2">
                <div className="font-bold text-xs sm:text-sm text-slate-900">
                  {ebsr.part_a_stem}
                </div>
                <div className="space-y-1.5">
                  {ebsr.part_a_options.map((opt) => {
                    const picked = ebsrPartA === opt.no;
                    const cls = picked
                      ? opt.is_correct
                        ? 'bg-emerald-50 border-emerald-600 text-emerald-950 font-bold'
                        : 'bg-rose-50 border-rose-500 text-rose-900'
                      : 'bg-white border-slate-200 text-slate-800 hover:border-indigo-400';
                    return (
                      <button
                        key={opt.no}
                        onClick={() => setEbsrPartA(opt.no)}
                        className={`w-full p-2.5 rounded-xl border text-left text-xs transition cursor-pointer ${cls}`}
                      >
                        <b>{opt.no}.</b> {opt.text}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Part B */}
              <div className="p-4 rounded-2xl border border-slate-200 bg-slate-50/70 space-y-2">
                <div className="font-bold text-xs sm:text-sm text-slate-900">
                  {ebsr.part_b_stem}
                </div>
                <div className="space-y-1.5">
                  {ebsr.part_b_options.map((opt) => {
                    const picked = ebsrPartB === opt.no;
                    const cls = picked
                      ? opt.is_correct
                        ? 'bg-emerald-50 border-emerald-600 text-emerald-950 font-bold'
                        : 'bg-rose-50 border-rose-500 text-rose-900'
                      : 'bg-white border-slate-200 text-slate-800 hover:border-indigo-400';
                    return (
                      <button
                        key={opt.no}
                        onClick={() => {
                          setEbsrPartB(opt.no);
                          const aOk = ebsr.part_a_options.find((a) => a.no === ebsrPartA)?.is_correct;
                          if (aOk && opt.is_correct) {
                            boostSmartScore(gradeData.grade_num, 5);
                          }
                        }}
                        className={`w-full p-2.5 rounded-xl border text-left text-xs transition cursor-pointer ${cls}`}
                      >
                        <b>{opt.no}.</b> {opt.text}
                      </button>
                    );
                  })}
                </div>
              </div>

              {/* Feedback */}
              {ebsrPartA !== null && ebsrPartB !== null && (
                <div
                  className={`p-3.5 rounded-2xl text-xs leading-relaxed ${
                    ebsr.part_a_options.find((a) => a.no === ebsrPartA)?.is_correct &&
                    ebsr.part_b_options.find((b) => b.no === ebsrPartB)?.is_correct
                      ? 'bg-emerald-50 border border-emerald-300 text-emerald-950 font-semibold'
                      : 'bg-amber-50 border border-amber-300 text-amber-950'
                  }`}
                >
                  <div dangerouslySetInnerHTML={{ __html: ebsr.explanation }} />
                </div>
              )}
            </div>
          )}

          {/* TAB 3: TEI-4 Graphic Organizer Builder */}
          {rightTab === 'organizer' && comm.graphic_organizer && (
            <div className="space-y-4">
              <GraphicOrganizerBuilder
                data={comm.graphic_organizer}
                onComplete={(allCorrect) => {
                  if (allCorrect) {
                    boostSmartScore(gradeData.grade_num, 8);
                    markStepComplete(gradeData.grade_num, 'studio');
                  }
                }}
              />
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default SplitScreenStudio;
