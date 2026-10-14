import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';

interface TeacherHeaderProps {
  grades: GradeData[];
  onOpenRoleGateway: () => void;
}

export const TeacherHeader: React.FC<TeacherHeaderProps> = ({
  grades,
  onOpenRoleGateway,
}) => {
  const {
    activeGradeIdx,
    setActiveGradeIdx,
    setActiveRole,
  } = useCoursewareStore();

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 text-slate-800 shadow-2xs no-print">
      <div className="max-w-[1500px] mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Left: Brand & Class Info */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-indigo-600 text-white flex items-center justify-center font-black text-sm shadow-xs">
            RX
          </div>
          <div className="flex items-center gap-2">
            <span className="font-black text-sm sm:text-base text-slate-900 tracking-tight">
              교사 콘솔
            </span>
            <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 border border-indigo-200">
              대치초 5학년 2반
            </span>
          </div>
        </div>

        {/* Center: Curricular Grade Selector */}
        <div className="flex items-center gap-1.5 bg-slate-100/80 p-1 rounded-xl border border-slate-200/60 overflow-x-auto">
          <span className="text-[11px] font-bold text-slate-500 px-1 hidden md:inline">학년:</span>
          {grades.map((g, idx) => (
            <button
              key={g.id}
              onClick={() => setActiveGradeIdx(idx)}
              className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
                activeGradeIdx === idx
                  ? 'bg-white text-indigo-700 shadow-xs'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              {g.grade_num}학년
            </button>
          ))}
        </div>

        {/* Right: Quick Action */}
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
