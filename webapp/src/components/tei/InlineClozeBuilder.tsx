import React, { useState } from 'react';
import type { ClozeBlank } from '../../types/courseware';

interface InlineClozeBuilderProps {
  promptTitle: string;
  sentences: string[];
  blanks: ClozeBlank[];
  onComplete?: (allCorrect: boolean, summaryText: string) => void;
}

export const InlineClozeBuilder: React.FC<InlineClozeBuilderProps> = ({
  promptTitle,
  sentences,
  blanks,
  onComplete,
}) => {
  const [selectedValues, setSelectedValues] = useState<Record<string, string>>({});
  const [errorBlankId, setErrorBlankId] = useState<string | null>(null);
  const [isCompleted, setIsCompleted] = useState<boolean>(false);

  const handleSelectBlank = (blankId: string, value: string) => {
    const blank = blanks.find((b) => b.id === blankId);
    if (!blank) return;

    if (value === blank.correct) {
      const nextMap = { ...selectedValues, [blankId]: value };
      setSelectedValues(nextMap);
      setErrorBlankId(null);

      // Check if all blanks filled correctly
      const allFilled = blanks.every((b) => nextMap[b.id] === b.correct);
      if (allFilled) {
        setIsCompleted(true);
        const summary = sentences
          .join(' ')
          .replace(/\{(\w+)\}/g, (_, id) => nextMap[id] || `[${id}]`);
        onComplete?.(true, summary);
      }
    } else {
      setErrorBlankId(blankId);
      setTimeout(() => setErrorBlankId(null), 1200);
    }
  };

  const handleReset = () => {
    setSelectedValues({});
    setErrorBlankId(null);
    setIsCompleted(false);
  };

  return (
    <div className="inline-cloze-builder bg-white rounded-2xl border border-blue-200 shadow-sm p-4 space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-blue-100">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 bg-blue-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-3 • Think-Aloud
          </span>
          <h4 className="font-bold text-sm text-slate-900">
            사고구술(Think-Aloud) 인라인 조립 빌더
          </h4>
        </div>
        {isCompleted && (
          <span className="px-2 py-0.5 bg-emerald-100 text-emerald-800 border border-emerald-300 rounded-full text-xs font-bold">
            ✓ 조립 완료
          </span>
        )}
      </div>

      <div className="text-xs text-slate-600 bg-blue-50/60 p-2.5 rounded-xl border border-blue-100 font-semibold">
        💡 {promptTitle}
      </div>

      {/* Sentences with Inlined Blank Selectors */}
      <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 text-sm leading-loose text-slate-800 space-y-2">
        {sentences.map((sent, sIdx) => {
          const parts = sent.split(/(\{[^}]+\})/g);
          return (
            <div key={sIdx} className="flex flex-wrap items-center gap-1.5">
              {parts.map((part, pIdx) => {
                const match = part.match(/^\{([^}]+)\}$/);
                if (!match) {
                  return <span key={pIdx}>{part}</span>;
                }

                const blankId = match[1];
                const blank = blanks.find((b) => b.id === blankId);
                if (!blank) return <span key={pIdx}>{part}</span>;

                const filledValue = selectedValues[blankId];
                const isError = errorBlankId === blankId;

                return (
                  <span key={pIdx} className="inline-flex items-center">
                    {filledValue ? (
                      <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-emerald-100 border border-emerald-400 text-emerald-950 font-bold text-xs shadow-xs animate-in fade-in">
                        <span>{filledValue}</span>
                        <span className="text-[10px] text-emerald-700">✓</span>
                      </span>
                    ) : (
                      <span
                        className={`inline-flex items-center p-0.5 rounded-lg border transition-all ${
                          isError
                            ? 'border-rose-500 bg-rose-50 ring-2 ring-rose-300 animate-bounce'
                            : 'border-blue-400 bg-white ring-2 ring-blue-100'
                        }`}
                      >
                        <select
                          value=""
                          onChange={(e) => handleSelectBlank(blankId, e.target.value)}
                          className="bg-transparent text-xs font-bold text-blue-900 cursor-pointer outline-none px-2 py-1"
                        >
                          <option value="" disabled>
                            [빈칸 {blankId} 선택]
                          </option>
                          {blank.options.map((opt, oIdx) => (
                            <option key={oIdx} value={opt}>
                              {opt}
                            </option>
                          ))}
                        </select>
                      </span>
                    )}
                  </span>
                );
              })}
            </div>
          );
        })}
      </div>

      {/* Word Bank Chips Dock */}
      <div className="p-3 bg-slate-100/80 rounded-xl border border-slate-200 space-y-2">
        <div className="flex items-center justify-between text-xs font-bold text-slate-700">
          <span>🧩 단어 보관함 (Word Bank)</span>
          {isCompleted && (
            <button
              onClick={handleReset}
              className="text-[11px] text-slate-500 underline hover:text-slate-700"
            >
              다시 조립하기 ↺
            </button>
          )}
        </div>
        <div className="flex flex-wrap gap-2">
          {blanks.flatMap((b) => b.options).filter((val, idx, self) => self.indexOf(val) === idx).map((word, wIdx) => {
            const isUsed = Object.values(selectedValues).includes(word);
            return (
              <span
                key={wIdx}
                className={`px-2.5 py-1 rounded-lg text-xs font-semibold border transition-all ${
                  isUsed
                    ? 'bg-slate-200/80 text-slate-400 border-slate-300 line-through'
                    : 'bg-white text-slate-800 border-slate-300 shadow-xs hover:border-blue-400'
                }`}
              >
                {word}
              </span>
            );
          })}
        </div>
      </div>
    </div>
  );
};
