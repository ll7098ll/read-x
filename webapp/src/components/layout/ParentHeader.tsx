import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';

interface ParentHeaderProps {
  gradeData: GradeData;
  onOpenRoleGateway: () => void;
}

export const ParentHeader: React.FC<ParentHeaderProps> = ({
  gradeData,
  onOpenRoleGateway,
}) => {
  const { setActiveRole } = useCoursewareStore();
  const xr = gradeData.xray_overview;

  const handlePrint = () => {
    window.print();
  };

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 text-slate-800 shadow-2xs no-print">
      <div className="max-w-[1500px] mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Left: Brand & Child Info */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-emerald-600 text-white flex items-center justify-center font-black text-sm shadow-xs">
            RX
          </div>
          <div className="flex items-center gap-2">
            <span className="font-black text-sm sm:text-base text-slate-900 tracking-tight">
              학부모 리포트
            </span>
            <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200">
              자녀: 김도윤 ({gradeData.grade})
            </span>
          </div>
        </div>

        {/* Center: Key Child Metric Pills */}
        <div className="hidden sm:flex items-center gap-2 text-xs">
          <div className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-lg">
            <span className="text-slate-500 font-bold mr-1">KReaD:</span>
            <span className="font-black text-emerald-700">{gradeData.complexity_metrics.current_kread}</span>
            <span className="text-slate-400 text-[10px] ml-0.5">/ {gradeData.complexity_metrics.kread_target}</span>
          </div>

          <div className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-lg">
            <span className="text-slate-500 font-bold mr-1">6차원 진단:</span>
            <span className="font-black text-slate-800">{xr.overall_score}점</span>
            <span className="text-emerald-600 font-bold ml-1 text-[11px]">({xr.percentile})</span>
          </div>
        </div>

        {/* Right: Actions */}
        <div className="flex items-center gap-2">
          <button
            onClick={handlePrint}
            className="text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-50 hover:bg-slate-100 text-slate-700 border border-slate-200 transition cursor-pointer"
          >
            🖨️ 인쇄
          </button>
          <button
            onClick={() => setActiveRole('landing')}
            className="text-xs font-bold px-2.5 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition cursor-pointer"
            title="메인 홈으로 이동"
          >
            🏠 홈
          </button>
        </div>
      </div>
    </header>
  );
};
