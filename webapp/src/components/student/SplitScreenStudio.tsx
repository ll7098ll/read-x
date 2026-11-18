import React, { useState, useEffect, useRef } from 'react';
import { BookOpen, PanelRight, Bookmark, Check, ScanLine, GitBranch, PenLine, ArrowRight, CircleHelp, SlidersHorizontal, Volume2, Square, X, StickyNote } from 'lucide-react';
import { usePracticeState, useReadingWorkspace, useReadingStorageStatus } from '../../store/useReadingWorkspace';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { ClinicDrill } from './ClinicActivities';
import { speakKoreanText, stopKoreanSpeech } from '../../utils/ttsEngine';
import type { GradeData, VocabNote, HighlightColorType, ClueNoteItem } from '../../types/courseware';
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
  const storageFailed = useReadingStorageStatus(s=>s.failed);
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
  const [rightTab, setRightTab] = usePracticeState<'evidence' | 'csat' | 'ebsr' | 'organizer' | 'cloze' | 'writing'>(gradeData.slot_id, 'tab', 'evidence');
  const [mobilePane, setMobilePane] = useState<'passage' | 'activity'>('passage');
  const [selectedParagraphs, setSelectedParagraphs] = usePracticeState<number[]>(gradeData.slot_id, 'paragraphs', []);
  const [currentClues, setCurrentClues] = usePracticeState<ClueNoteItem[]>(gradeData.slot_id, 'notes', []);
  const addClueNote = (_grade: number, text: string, color: HighlightColorType, tag: string) => {
    setCurrentClues(notes => notes.some(note => note.text === text) ? notes : [...notes, {id: crypto.randomUUID(), text, color, tag, createdAt: new Date().toISOString()}]);
  };
  const removeClueNote = (_grade: number, id: string) => setCurrentClues(notes => notes.filter(note => note.id !== id));

  // Question solving state
  const [wrongAttempts, setWrongAttempts] = usePracticeState<Record<number, number>>(gradeData.slot_id, 'wrongAttempts', {});
  const [pickedHistory, setPickedHistory] = usePracticeState<Record<number, number[]>>(gradeData.slot_id, 'pickedHistory', {});
  const [solvedMap, setSolvedMap] = usePracticeState<Record<number, boolean>>(gradeData.slot_id, 'solvedMap', {});
  const [activeQuestionIdx, setActiveQuestionIdx] = usePracticeState<number>(gradeData.slot_id, 'question', 0);

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
  const [speechMessage, setSpeechMessage] = useState('');

  // EBSR (TEI-2) state
  const [ebsrPartA, setEbsrPartA] = usePracticeState<number | null>(gradeData.slot_id, 'ebsrA', null);
  const [ebsrPartB, setEbsrPartB] = usePracticeState<number | null>(gradeData.slot_id, 'ebsrB', null);

  const paraRefs = useRef<Record<number, HTMLDivElement | null>>({});
  const passageRef = useRef<HTMLDivElement>(null);

  // Resume practice on this device; official assessment records are separate.
  useEffect(() => {
    stopKoreanSpeech();
    setIsSpeaking(false);
    useReadingWorkspace.getState().visit(gradeData.slot_id);
    const top = useReadingWorkspace.getState().sessions[gradeData.slot_id]?.scrollTop;
    if(passageRef.current && typeof top === 'number') passageRef.current.scrollTop = top;
    return () => stopKoreanSpeech();
  }, [gradeData.id, gradeData.slot_id]);

  const handleToggleTts = () => {
    if (isSpeaking) {
      stopKoreanSpeech();
      setIsSpeaking(false);
    } else {
      if (!('speechSynthesis' in window)) { setSpeechMessage('이 브라우저는 지문 듣기를 지원하지 않아요. 다른 브라우저에서 이용해 주세요.'); return; }
      setSpeechMessage('');
      setIsSpeaking(true);
      const text = `${csat.passage_title}. ${csat.paragraphs.join(' ')}`;
      speakKoreanText(text, ttsRate, () => setIsSpeaking(false), () => setSpeechMessage('지문을 재생하지 못했어요. 기기의 음성 설정을 확인하고 다시 시도해 주세요.'));
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
    if (solvedMap[qNo]) return;
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

  const currentQuestion = csat.questions[activeQuestionIdx] || csat.questions[0];

  return (
    <div className="rx-reading-workspace space-y-4 font-sans" data-pane={mobilePane} data-font={fontSize}>
      <div className="rx-reading-context"><span className="rx-eyebrow">READING STUDIO</span><span className="rx-reading-save" role="status"><Check size={15}/>{storageFailed?'저장 공간을 확인해 주세요':'이 기기의 연습 기록'}</span></div>
      {storageFailed && <p className="rx-inline-note" role="alert">기기에 연습 내용을 저장하지 못했어요. 이 창을 닫기 전에 중요한 내용은 따로 복사해 주세요.</p>}
      {/* 1. ZEN FOCUS HEADER (Minimal & Elegant) */}
      <div className="rx-reading-toolbar bg-white border border-slate-200/90 px-4 py-3 flex flex-wrap items-center justify-between gap-3">
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
                className={`rx-highlighter w-5 h-5 rounded-full ${hl.bg} transition transform hover:scale-110 cursor-pointer ${
                  activeHighlightColor === hl.id
                    ? `ring-2 ring-offset-1 ring-slate-800 scale-110`
                    : 'opacity-70 hover:opacity-100'
                }`}
                title={`${hl.label} 단서 분류 선택 (지문 드래그 시 메모 저장)`}
                aria-pressed={activeHighlightColor === hl.id}
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
            {isSpeaking ? <Square size={15}/> : <Volume2 size={15}/>}<span>{isSpeaking ? '정지' : '지문 듣기'}</span>
          </button>

          {/* Reading Display Settings Popover Toggle */}
          <div className="relative">
            <button
              onClick={() => setShowSettingsPopover(!showSettingsPopover)}
              aria-expanded={showSettingsPopover}
              className="px-2.5 py-1.5 rounded-xl text-xs font-bold bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1 cursor-pointer"
              title="글자 크기, 문단 번호, 초점 가이드 설정"
            >
              <SlidersHorizontal size={15}/><span>보기 설정</span>
            </button>

            {showSettingsPopover && (
              <div className="absolute right-0 mt-2 w-56 bg-white rounded-2xl border border-slate-200 shadow-xl p-3 z-50 space-y-3 text-xs animate-in fade-in zoom-in-95">
                <div className="font-bold text-slate-800 pb-1.5 border-b border-slate-100 flex justify-between items-center">
                  <span>독서 환경 맞춤 설정</span>
                  <button
                    onClick={() => setShowSettingsPopover(false)}
                    aria-label="보기 설정 닫기"
                    className="text-slate-400 hover:text-slate-600"
                  >
                    <X size={16}/>
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
                        aria-pressed={fontSize === fs}
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

                <fieldset className="space-y-1"><legend className="text-slate-500 font-bold">종이 색</legend><div className="grid grid-cols-3 gap-1">{(['paper','sepia','dark'] as const).map(theme=><button key={theme} aria-pressed={readerTheme===theme} onClick={()=>setReaderTheme(theme)} className={`py-1 rounded-lg border ${readerTheme===theme?'bg-blue-600 text-white border-blue-600':'bg-slate-50 text-slate-700 border-slate-200'}`}>{theme==='paper'?'종이':theme==='sepia'?'세피아':'야간'}</button>)}</div></fieldset>
                {/* Paragraph Numbers */}
                <div className="flex items-center justify-between pt-1">
                  <span className="text-slate-700 font-bold">문단 번호 (#)</span>
                  <input
                    type="checkbox"
                    checked={showParaNumbers}
                    aria-label="문단 번호 표시"
                    onChange={toggleParaNumbers}
                    className="rounded accent-blue-600 w-4 h-4 cursor-pointer"
                  />
                </div>

                {/* Focus Ruler */}
                <div className="flex items-center justify-between">
                  <span className="text-slate-700 font-bold">문단 집중 리더</span>
                  <input
                    type="checkbox"
                    checked={showFocusRuler}
                    aria-label="문단 집중 리더"
                    onChange={toggleFocusRuler}
                    className="rounded accent-blue-600 w-4 h-4 cursor-pointer"
                  />
                </div>

                {/* Two-Column Mode */}
                <div className="flex items-center justify-between">
                  <span className="text-slate-700 font-bold">본문 두 단으로 보기</span>
                  <input
                    type="checkbox"
                    checked={isTwoColumnMode}
                    aria-label="본문 두 단으로 보기"
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
            <StickyNote size={15}/><span>단서 ({currentClues.length})</span>
          </button>
        </div>
      </div>

      {speechMessage && <p role="status" className="rx-inline-note">{speechMessage}</p>}
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
              aria-label="이 수업의 단서 메모"
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
                    aria-label={`${c.text} 메모 삭제`}
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

      <div className="rx-pane-toggle" aria-label="읽기 화면 전환"><button aria-pressed={mobilePane==='passage'} onClick={()=>setMobilePane('passage')}><BookOpen size={18}/>본문 읽기</button><button aria-pressed={mobilePane==='activity'} onClick={()=>setMobilePane('activity')}><PanelRight size={18}/>생각 활동 {selectedParagraphs.length>0&&<span>{selectedParagraphs.length}개 근거</span>}</button></div>
      {/* Both panes stay mounted so draft responses and scroll survive switching. */}
      <div className="rx-reading-grid">
        {/* ================= LEFT PANE: PURE READING SANCTUARY (6 cols on lg) ================= */}
        <div ref={passageRef} onScroll={e=>useReadingWorkspace.getState().save(gradeData.slot_id,'scrollTop',e.currentTarget.scrollTop)} className={`rx-reading-paper reader-theme-${readerTheme}`}>
          {/* Passage Header */}
          <div className="rx-passage-heading">
            <div>
              <span className="text-[11px] font-bold text-stone-500 tracking-wider uppercase block">
                오늘 읽을 글
              </span>
              <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight mt-0.5 font-serif">
                {csat.passage_title}
              </h2>
            </div>
            <span className="text-xs font-medium text-stone-500 shrink-0">
              {csat.paragraphs.length}개 문단
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
            className={`rx-passage-text font-serif selection:bg-amber-200 ${
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
                  className={`rx-paragraph relative transition-all duration-200 ${selectedParagraphs.includes(idx) ? 'rx-paragraph-selected' : ''} ${
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
                  <button type="button" className="rx-evidence-toggle" aria-pressed={selectedParagraphs.includes(idx)} aria-label={`${idx+1}문단 ${selectedParagraphs.includes(idx)?'근거 해제':'근거로 담기'}`} onClick={()=>setSelectedParagraphs(prev=>prev.includes(idx)?prev.filter(p=>p!==idx):[...prev,idx])}>{selectedParagraphs.includes(idx)?<Check size={15}/>:<Bookmark size={15}/>} {selectedParagraphs.includes(idx)?'근거에 담았어요':'근거로 담기'}</button>
                </div>
              );
            })}
          </div>

          {/* Inline Vocabulary Footer Cards */}
          {csat.vocab_notes && csat.vocab_notes.length > 0 && (
            <div className="mt-8 pt-5 border-t border-stone-200 space-y-2">
              <span className="text-[11px] font-bold text-stone-500 uppercase tracking-wider block">
                글에서 만난 핵심 낱말
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
                    <button className="rx-vocab-save" aria-pressed={savedVocab.some(v=>v.word===vn.word)} onClick={()=>savedVocab.some(v=>v.word===vn.word)?removeVocabWord(vn.word):saveVocabWord(vn,gradeData.grade)}>{savedVocab.some(v=>v.word===vn.word)?<Check size={14}/>:<Bookmark size={14}/>} {savedVocab.some(v=>v.word===vn.word)?'단어장에 담았어요':'단어장에 담기'}</button>
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* ================= RIGHT PANE: FOCUS PROBLEM WORKSPACE (5 cols on lg) ================= */}
        <div className="rx-activity-pane space-y-4">
          <section className="rounded-2xl border border-blue-100 bg-blue-50 p-4 space-y-3">
            <h3 className="font-bold">오늘 연습할 생각 · {gradeData.sub_skill_name}</h3>
            <p className="text-sm leading-relaxed">글에서 단서를 찾고, 그렇게 생각한 이유를 내 말로 설명해 봐요.</p>
            <details className="text-sm"><summary className="cursor-pointer font-semibold py-2">함께 생각하는 안내 보기</summary>
              <ol className="list-decimal pl-5 space-y-3 mt-2"><li>{gradeData.prototype_step1_2.step1_mission}</li><li>{gradeData.prototype_step1_2.step2_mission}</li>
                <li>찾은 근거와 연결한 이유를 내 문장으로 설명해 보세요.</li></ol>
              <p className="mt-3 text-slate-600">안내를 보고 한 연습과 혼자 한 확인은 구분해서 살펴봐요.</p>
            </details>
          </section>
          {/* Segmented Mode Switcher */}
          <div className="rx-activity-tabs" aria-label="생각 활동 선택">
            <button aria-pressed={rightTab==='evidence'} className={rightTab==='evidence'?'is-active':''} onClick={()=>setRightTab('evidence')}><ScanLine size={16}/>근거 찾기</button>
            <button
              onClick={() => setRightTab('csat')}
              aria-pressed={rightTab === 'csat'}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'csat'
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              판단하기
            </button>
            <button
              onClick={() => setRightTab('ebsr')}
              aria-pressed={rightTab === 'ebsr'}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'ebsr'
                  ? 'bg-indigo-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              답과 근거
            </button>
            <button
              onClick={() => setRightTab('organizer')}
              aria-pressed={rightTab === 'organizer'}
              className={`flex-1 py-2 px-2 rounded-xl text-xs font-black transition cursor-pointer ${
                rightTab === 'organizer'
                  ? 'bg-emerald-600 text-white shadow-xs'
                  : 'text-slate-600 hover:text-slate-900 hover:bg-slate-50'
              }`}
            >
              관계 연결
            </button>
            <button type="button" onClick={() => setRightTab('cloze')} aria-pressed={rightTab === 'cloze'} className={`flex-1 px-3 py-3 rounded-xl text-xs font-bold ${rightTab === 'cloze' ? 'bg-blue-700 text-white' : 'bg-slate-50'}`}>생각 연습</button>
            <button type="button" onClick={() => setRightTab('writing')} aria-pressed={rightTab === 'writing'} className={`flex-1 px-3 py-3 rounded-xl text-xs font-bold ${rightTab === 'writing' ? 'bg-teal-700 text-white' : 'bg-slate-50'}`}>내 말로 쓰기</button>
          </div>

          {rightTab==='evidence'&&<section className="rx-surface rx-evidence-activity"><span className="rx-badge"><ScanLine size={15}/>첫 번째 생각</span><h2>어디에서 찾았나요?</h2><p>내 생각을 뒷받침하는 문단은 어디일까요? 글에서 단서를 찾아 보세요.</p><div className="rx-inline-note"><CircleHelp size={18}/><span>본문을 읽고 필요한 문단의 ‘근거로 담기’를 눌러보세요. 선택한 근거를 아래에서 다시 볼 수 있어요.</span></div><div className="rx-evidence-list" aria-live="polite">{selectedParagraphs.length===0?<p className="rx-muted">아직 담은 근거가 없어요.</p>:selectedParagraphs.map(idx=><blockquote key={idx}><b>{idx+1}문단</b><p>{csat.paragraphs[idx]?.replace(/<[^>]*>/g,'')}</p><button className="rx-text-link" onClick={()=>setSelectedParagraphs(prev=>prev.filter(p=>p!==idx))}>선택 해제</button></blockquote>)}</div><button className="rx-button rx-button-primary" onClick={()=>setRightTab('cloze')}>생각 연결해 보기 <ArrowRight size={17}/></button><p className="rx-fine-print">담은 문단은 연습용 근거입니다. 선택만으로 정답이나 숙련을 판정하지 않아요.</p></section>}

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

          {rightTab === 'cloze' && <ClinicDrill key={gradeData.slot_id} drill={gradeData.prescription_clinic.step1_2_drill} draftKey={`${gradeData.slot_id}:clinic`} />}
          {rightTab === 'writing' && <WritingWorkbench key={gradeData.slot_id} data={wb} draftKey={`${gradeData.slot_id}:writing`} />}
          {/* TAB 3: TEI-4 Graphic Organizer Builder */}
          {rightTab === 'organizer' && comm.graphic_organizer && (
            <div className="space-y-4">
              <GraphicOrganizerBuilder
                data={comm.graphic_organizer}
                onComplete={(allCorrect) => {
                  if (allCorrect) {
                    boostSmartScore(gradeData.grade_num, 8);

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
