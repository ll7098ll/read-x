import React, { useState, useEffect } from 'react';
import type { HottextCueItem, HighlightColorType } from '../../types/courseware';

interface HotTextPassageProps {
  paragraphs: string[];
  hottextCues?: HottextCueItem[];
  activeHighlightColor: HighlightColorType;
  onClueFound?: (cue: HottextCueItem) => void;
  onAllCluesFound?: () => void;
  showSpotlightQuote?: string | null;
  targetParaIdx?: number | null;
}

export const HotTextPassage: React.FC<HotTextPassageProps> = ({
  paragraphs,
  hottextCues = [],
  activeHighlightColor,
  onClueFound,
  onAllCluesFound,
  showSpotlightQuote,
  targetParaIdx,
}) => {
  const [clickedCueIds, setClickedCueIds] = useState<Set<string>>(new Set());

  // Reset when cues change
  useEffect(() => {
    setClickedCueIds(new Set());
  }, [paragraphs, hottextCues]);

  const handleCueClick = (cue: HottextCueItem) => {
    if (clickedCueIds.has(cue.cue_id)) return;
    const nextSet = new Set(clickedCueIds);
    nextSet.add(cue.cue_id);
    setClickedCueIds(nextSet);
    onClueFound?.(cue);

    if (hottextCues.length > 0 && nextSet.size === hottextCues.length) {
      onAllCluesFound?.();
    }
  };

  const totalCues = hottextCues.length;
  const foundCount = clickedCueIds.size;
  const isAllFound = totalCues > 0 && foundCount >= totalCues;

  // Render paragraph with hot text cues embedded
  const renderParagraphContent = (para: string, pIdx: number) => {
    // If there are cues for this paragraph, highlight or wrap them
    const paraCues = hottextCues.filter((c) => c.para_idx === pIdx);

    if (paraCues.length === 0) {
      // Check if this paragraph contains the spotlight quote
      if (showSpotlightQuote && targetParaIdx === pIdx && para.includes(showSpotlightQuote)) {
        const parts = para.split(showSpotlightQuote);
        return (
          <>
            {parts[0]}
            <mark className="bg-amber-200/90 text-amber-950 font-bold px-1.5 py-0.5 rounded shadow-sm ring-4 ring-amber-400 animate-pulse transition-all">
              {showSpotlightQuote}
            </mark>
            {parts[1]}
          </>
        );
      }
      return para;
    }

    // Replace known cues with interactive spans
    let renderedSegments: React.ReactNode[] = [para];

    paraCues.forEach((cue) => {
      const newSegments: React.ReactNode[] = [];
      renderedSegments.forEach((seg) => {
        if (typeof seg !== 'string') {
          newSegments.push(seg);
          return;
        }

        if (!seg.includes(cue.text)) {
          newSegments.push(seg);
          return;
        }

        const splits = seg.split(cue.text);
        for (let i = 0; i < splits.length; i++) {
          newSegments.push(splits[i]);
          if (i < splits.length - 1) {
            const isClicked = clickedCueIds.has(cue.cue_id);
            const colorClass = isClicked
              ? activeHighlightColor === 'yellow'
                ? 'bg-amber-200/95 text-amber-950 ring-2 ring-amber-400 font-bold shadow-sm'
                : activeHighlightColor === 'blue'
                ? 'bg-sky-200/95 text-sky-950 ring-2 ring-sky-400 font-bold shadow-sm'
                : 'bg-rose-200/95 text-rose-950 ring-2 ring-rose-400 font-bold shadow-sm'
              : 'border-b-2 border-dashed border-amber-500 bg-amber-50/60 hover:bg-amber-100 cursor-pointer text-amber-900 transition-colors animate-pulse';

            newSegments.push(
              <span
                key={`${cue.cue_id}-${i}`}
                data-cue-id={cue.cue_id}
                onClick={() => handleCueClick(cue)}
                className={`inline-block px-1.5 py-0.5 rounded mx-0.5 select-none transition-all ${colorClass}`}
                title={isClicked ? `[포착 완료] ${cue.role}` : `클릭하여 단서 포착: ${cue.role}`}
              >
                {cue.text}
                {isClicked ? (
                  <span className="ml-1 text-[10px] bg-white/80 rounded px-1 text-slate-800 font-bold">
                    ✓
                  </span>
                ) : (
                  <span className="ml-1 text-[10px] text-amber-700 font-bold">
                    👆
                  </span>
                )}
              </span>
            );
          }
        }
      });
      renderedSegments = newSegments;
    });

    return renderedSegments;
  };

  return (
    <div className="hot-text-passage-container space-y-3">
      {/* Top Clue Progress Banner */}
      {totalCues > 0 && (
        <div
          className={`flex items-center justify-between p-2.5 rounded-xl border text-xs transition-all ${
            isAllFound
              ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
              : 'bg-amber-50/90 border-amber-300 text-amber-900'
          }`}
        >
          <div className="flex items-center gap-2">
            <span className="text-base">{isAllFound ? '🎉' : '🔍'}</span>
            <span className="font-bold">
              {isAllFound
                ? '축하합니다! 지문 속 핵심 단서를 모두 포착했습니다.'
                : '지문에서 밑줄 친 단서를 직접 클릭해 단서 보드에 수집하세요!'}
            </span>
          </div>
          <div className="flex items-center gap-2 font-mono font-black">
            <span className="px-2 py-0.5 rounded-full bg-white border border-amber-300 shadow-xs">
              {foundCount} / {totalCues}
            </span>
            {isAllFound && (
              <span className="px-2 py-0.5 bg-emerald-600 text-white rounded-full font-sans text-[11px]">
                포착 완료!
              </span>
            )}
          </div>
        </div>
      )}

      {/* Paragraphs List */}
      <div className="space-y-4">
        {paragraphs.map((para, idx) => (
          <p
            key={idx}
            className={`transition-all duration-300 ${
              targetParaIdx === idx
                ? 'p-2.5 rounded-xl bg-amber-50/60 ring-2 ring-amber-300'
                : ''
            }`}
          >
            {renderParagraphContent(para, idx)}
          </p>
        ))}
      </div>
    </div>
  );
};
