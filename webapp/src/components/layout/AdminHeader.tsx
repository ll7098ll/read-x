import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';

interface AdminHeaderProps {
  totalDbSlots: number;
  onOpenRoleGateway: () => void;
}

export const AdminHeader: React.FC<AdminHeaderProps> = ({
  totalDbSlots,
  onOpenRoleGateway,
}) => {
  const { setActiveRole } = useCoursewareStore();

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 text-slate-800 shadow-2xs no-print">
      <div className="max-w-[1500px] mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Left: Brand & Institution Info */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-amber-500 text-slate-950 flex items-center justify-center font-black text-sm shadow-xs">
            RX
          </div>
          <div className="flex items-center gap-2">
            <span className="font-black text-sm sm:text-base text-slate-900 tracking-tight">
              학원장 허브
            </span>
            <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-amber-50 text-amber-800 border border-amber-200">
              대치 본원 B2B
            </span>
          </div>
        </div>

        {/* Center: Quota & DB Indicators */}
        <div className="hidden sm:flex items-center gap-2 text-xs">
          <div className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-lg">
            <span className="text-slate-500 font-bold mr-1">좌석 라이선스:</span>
            <span className="font-black text-slate-800">34 / 50석</span>
            <span className="text-emerald-600 font-bold ml-1 text-[11px]">(가용 16석)</span>
          </div>

          <div className="bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-lg">
            <span className="text-slate-500 font-bold mr-1">Item Bank DB:</span>
            <span className="font-black text-blue-600">{totalDbSlots} / 132슬롯</span>
            <span className="text-emerald-600 font-bold ml-1 text-[10px]">(완비)</span>
          </div>
        </div>

        {/* Right: Actions */}
        <div className="flex items-center gap-2">
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
