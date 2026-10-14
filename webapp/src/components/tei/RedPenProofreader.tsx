import React, { useState } from 'react';
import type { ProofreadItem } from '../../types/courseware';

interface RedPenProofreaderProps {
  items: ProofreadItem[];
  onAllApplied?: () => void;
}

export const RedPenProofreader: React.FC<RedPenProofreaderProps> = ({
  items,
  onAllApplied,
}) => {
  const [appliedMarkers, setAppliedMarkers] = useState<Record<string, boolean>>({});
  const [activeItem, setActiveItem] = useState<ProofreadItem | null>(null);

  const handleApplyProofread = (marker: string) => {
    const nextMap = { ...appliedMarkers, [marker]: true };
    setAppliedMarkers(nextMap);
    setActiveItem(null);

    if (items.length > 0 && Object.keys(nextMap).length >= items.length) {
      onAllApplied?.();
    }
  };

  const appliedCount = Object.keys(appliedMarkers).length;
  const isAllApplied = items.length > 0 && appliedCount >= items.length;

  return (
    <div className="red-pen-proofreader bg-white rounded-2xl border border-rose-200 shadow-sm p-4 space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-rose-100">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 bg-rose-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-7 • 교정부호 에디터
          </span>
          <h4 className="font-bold text-sm text-slate-900">
            W5 빨간펜 교정부호 3단계 퇴고 스튜디오
          </h4>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs font-mono font-bold text-rose-800 bg-rose-50 px-2 py-0.5 rounded-full border border-rose-200">
            교정 완료: {appliedCount} / {items.length}
          </span>
        </div>
      </div>

      <div className="text-xs text-slate-600 bg-rose-50/60 p-2.5 rounded-xl border border-rose-100">
        ✏️ 밑줄 친 교정 대상 구간을 클릭하여 5대 표준 교정부호(삭제, 대체, 삽입, 자리바꿈, 띄어쓰기)를 적용해 보세요.
      </div>

      {/* Proofreading Interactive Cards List */}
      <div className="space-y-3">
        {items.map((item) => {
          const isApplied = appliedMarkers[item.marker];
          const isActive = activeItem?.marker === item.marker;

          return (
            <div
              key={item.marker}
              className={`p-3.5 rounded-xl border transition-all ${
                isApplied
                  ? 'bg-emerald-50/60 border-emerald-300'
                  : isActive
                  ? 'bg-rose-50 border-rose-400 ring-2 ring-rose-200'
                  : 'bg-slate-50 border-slate-200 hover:border-rose-300'
              }`}
            >
              <div className="flex items-start justify-between gap-2">
                <div className="space-y-1 flex-1">
                  <div className="flex items-center gap-2">
                    <span className="w-5 h-5 rounded-full bg-slate-800 text-white flex items-center justify-center text-[10px] font-bold">
                      {item.marker}
                    </span>
                    <span className="text-xs font-bold text-slate-600">
                      [{item.tier}] {item.action_label}
                    </span>
                  </div>

                  {/* Before vs After Red Pen View */}
                  <div className="text-xs leading-relaxed pt-1">
                    {isApplied ? (
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="text-rose-600 line-through bg-rose-100 px-1.5 py-0.5 rounded text-[11px]">
                          {item.original}
                        </span>
                        <span className="text-emerald-700 font-bold bg-emerald-100 px-2 py-0.5 rounded text-xs ring-1 ring-emerald-300">
                          ➔ {item.corrected}
                        </span>
                        <span className="text-[10px] bg-white border border-emerald-300 text-emerald-800 px-1.5 py-0.5 rounded-md">
                          ✓ 교정 완료
                        </span>
                      </div>
                    ) : (
                      <div className="flex items-center gap-2">
                        <span className="text-rose-950 font-bold bg-white px-2 py-1 rounded border border-rose-300 shadow-xs cursor-pointer hover:bg-rose-100">
                          {item.original}
                        </span>
                        <span className="text-[11px] text-slate-500 italic">
                          (터치하여 교정부호 적용)
                        </span>
                      </div>
                    )}
                  </div>

                  <p className="text-[11px] text-slate-500 pt-0.5">
                    💡 <b>퇴고 이유</b>: {item.status_note}
                  </p>
                </div>

                {!isApplied && (
                  <button
                    onClick={() => handleApplyProofread(item.marker)}
                    className="px-3 py-1.5 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-bold shadow-xs cursor-pointer shrink-0 transition-all"
                  >
                    빨간펜 교정 🖋️
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Completion Banner */}
      {isAllApplied && (
        <div className="p-3 bg-emerald-100 border border-emerald-300 rounded-xl text-xs text-emerald-950 font-bold flex items-center gap-2">
          <span>🎉</span>
          <span>
            모든 문장의 퇴고가 완료되었습니다! 단정하고 정확한 설명문 초고가 완성되었습니다.
          </span>
        </div>
      )}
    </div>
  );
};
