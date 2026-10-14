import React, { useState } from 'react';
import type { EbsrQuestionData } from '../../types/courseware';

interface EBSRQuestionCardProps {
  data: EbsrQuestionData;
  onComplete?: (score: number, isFullyCorrect: boolean) => void;
}

export const EBSRQuestionCard: React.FC<EBSRQuestionCardProps> = ({
  data,
  onComplete,
}) => {
  const [partAPicked, setPartAPicked] = useState<number | null>(null);
  const [partBPicked, setPartBPicked] = useState<number | null>(null);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);

  const partACorrect = data.part_a_options.find((o) => o.is_correct)?.no;
  const partBCorrect = data.part_b_options.find((o) => o.is_correct)?.no;

  const isPartACorrect = partAPicked === partACorrect;
  const isPartBCorrect = partBPicked === partBCorrect;
  const isBothCorrect = isPartACorrect && isPartBCorrect;

  const handleSubmit = () => {
    if (partAPicked === null || partBPicked === null) return;
    setIsSubmitted(true);
    const score = isBothCorrect ? 2 : isPartACorrect ? 1 : 0;
    onComplete?.(score, isBothCorrect);
  };

  const handleReset = () => {
    setPartAPicked(null);
    setPartBPicked(null);
    setIsSubmitted(false);
  };

  return (
    <div className="ebsr-card bg-white rounded-2xl border border-indigo-200/90 shadow-sm overflow-hidden p-4 space-y-4">
      {/* Header Banner */}
      <div className="flex items-center justify-between pb-3 border-b border-indigo-100">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 bg-indigo-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-2 • EBSR
          </span>
          <h4 className="font-bold text-sm text-slate-900">
            2단계 근거 연동형 문항 (Evidence-Based Selected Response)
          </h4>
        </div>
        <span className="text-xs text-indigo-700 font-semibold bg-indigo-50 px-2 py-0.5 rounded-full border border-indigo-200">
          배점: 2점 (완전 일치 시)
        </span>
      </div>

      {/* Part A Section */}
      <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
        <div className="flex items-center gap-2 text-xs font-bold text-slate-800">
          <span className="w-5 h-5 rounded-full bg-blue-600 text-white flex items-center justify-center text-[11px] font-black">
            A
          </span>
          <span>[Part A: 중심 판단 및 추론] {data.part_a_stem}</span>
        </div>

        <div className="space-y-2">
          {data.part_a_options.map((opt) => {
            const isSelected = partAPicked === opt.no;
            let statusStyle = 'border-slate-200 hover:bg-slate-100 bg-white';
            if (isSubmitted) {
              if (opt.is_correct) {
                statusStyle = 'border-emerald-500 bg-emerald-50/80 text-emerald-950 font-bold';
              } else if (isSelected && !opt.is_correct) {
                statusStyle = 'border-rose-400 bg-rose-50 text-rose-950 line-through';
              }
            } else if (isSelected) {
              statusStyle = 'border-blue-600 bg-blue-50 text-blue-950 font-bold ring-2 ring-blue-300';
            }

            return (
              <button
                key={opt.no}
                disabled={isSubmitted}
                onClick={() => setPartAPicked(opt.no)}
                className={`w-full text-left p-2.5 rounded-lg border text-xs transition-all flex items-start gap-2 ${statusStyle}`}
              >
                <span className="w-4 h-4 rounded-full border border-slate-300 flex items-center justify-center shrink-0 text-[10px] font-bold">
                  {opt.no}
                </span>
                <span className="flex-1">{opt.text}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Part B Section (Unlocked only after Part A is picked) */}
      <div
        className={`p-3.5 rounded-xl border transition-all space-y-3 ${
          partAPicked === null
            ? 'opacity-40 bg-slate-100 border-dashed border-slate-300 pointer-events-none'
            : 'bg-indigo-50/40 border-indigo-200'
        }`}
      >
        <div className="flex items-center justify-between text-xs font-bold text-slate-800">
          <div className="flex items-center gap-2">
            <span className="w-5 h-5 rounded-full bg-indigo-600 text-white flex items-center justify-center text-[11px] font-black">
              B
            </span>
            <span>[Part B: 본문 근거 문장 매칭] {data.part_b_stem}</span>
          </div>
          {partAPicked === null && (
            <span className="text-[11px] text-slate-500 font-normal">
              🔒 Part A를 먼저 선택하세요
            </span>
          )}
        </div>

        <div className="space-y-2">
          {data.part_b_options.map((opt) => {
            const isSelected = partBPicked === opt.no;
            let statusStyle = 'border-slate-200 hover:bg-slate-100 bg-white';
            if (isSubmitted) {
              if (opt.is_correct) {
                statusStyle = 'border-emerald-500 bg-emerald-50/80 text-emerald-950 font-bold';
              } else if (isSelected && !opt.is_correct) {
                statusStyle = 'border-rose-400 bg-rose-50 text-rose-950 line-through';
              }
            } else if (isSelected) {
              statusStyle = 'border-indigo-600 bg-indigo-50 text-indigo-950 font-bold ring-2 ring-indigo-300';
            }

            return (
              <button
                key={opt.no}
                disabled={isSubmitted || partAPicked === null}
                onClick={() => setPartBPicked(opt.no)}
                className={`w-full text-left p-2.5 rounded-lg border text-xs transition-all flex items-start gap-2 ${statusStyle}`}
              >
                <span className="w-4 h-4 rounded-full border border-slate-300 flex items-center justify-center shrink-0 text-[10px] font-bold">
                  {opt.no}
                </span>
                <span className="flex-1">{opt.text}</span>
              </button>
            );
          })}
        </div>
      </div>

      {/* Action / Result Footer */}
      {!isSubmitted ? (
        <div className="flex justify-end pt-2">
          <button
            onClick={handleSubmit}
            disabled={partAPicked === null || partBPicked === null}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm ${
              partAPicked !== null && partBPicked !== null
                ? 'bg-indigo-600 hover:bg-indigo-700 text-white cursor-pointer hover:shadow-md'
                : 'bg-slate-200 text-slate-400 cursor-not-allowed'
            }`}
          >
            2단계 근거 연동 채점하기
          </button>
        </div>
      ) : (
        <div className="pt-2 space-y-3">
          <div
            className={`p-3 rounded-xl border text-xs space-y-1 ${
              isBothCorrect
                ? 'bg-emerald-50 border-emerald-300 text-emerald-900'
                : isPartACorrect
                ? 'bg-amber-50 border-amber-300 text-amber-900'
                : 'bg-rose-50 border-rose-300 text-rose-900'
            }`}
          >
            <div className="flex items-center justify-between font-bold">
              <span>
                {isBothCorrect
                  ? '🎉 완벽합니다! (Part A 판단과 Part B 본문 근거 모두 정답, 2점 획득)'
                  : isPartACorrect
                  ? '⚠️ 부분 점수 (Part A는 정답이나, Part B 근거 문장이 일치하지 않습니다, 1점 획득)'
                  : '🚨 오답 (Part A 판단부터 다시 검토해 보세요, 0점)'}
              </span>
              <button
                onClick={handleReset}
                className="text-[11px] underline text-slate-700 hover:text-slate-900"
              >
                다시 풀기 ↺
              </button>
            </div>
            <p className="text-[11.5px] leading-relaxed pt-1 text-slate-700 border-t border-slate-200/60 mt-1">
              💡 <b>정답 및 근거 해설</b>: {data.explanation}
            </p>
          </div>
        </div>
      )}
    </div>
  );
};
