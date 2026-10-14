import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData, StudentModeType } from '../../types/courseware';

interface StudentHeaderProps {
  gradeData: GradeData;
  onOpenRoleGateway: () => void;
  onOpenCatModal: () => void;
}

export const StudentHeader: React.FC<StudentHeaderProps> = ({
  gradeData,
  onOpenRoleGateway,
  onOpenCatModal,
}) => {
  const {
    studentMode,
    setStudentMode,
    smartScores,
    streakDays,
    setActiveRole,
  } = useCoursewareStore();

  const currentSmartScore =
    smartScores[gradeData.grade_num] ?? gradeData.xray_overview.overall_score;

  const modes: Array<{ id: StudentModeType; label: string }> = [
    { id: 'portal', label: '📝 과제함 & 진도' },
    { id: 'studio', label: '📖 독서 스튜디오' },
    { id: 'clinic', label: '🩹 1:1 클리닉' },
    { id: 'cbt_exam', label: '✍️ CBT 모의고사' },
  ];

  return (
    <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/90 text-slate-800 shadow-2xs no-print">
      <div className="max-w-[1500px] mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
        {/* Left: Brand & Student Name */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-xl bg-blue-600 text-white flex items-center justify-center font-black text-sm shadow-xs">
            RX
          </div>
          <div className="flex items-center gap-2">
            <span className="font-black text-sm sm:text-base text-slate-900 tracking-tight">
              학생 학습관
            </span>
            <span className="text-[11px] font-bold px-2 py-0.5 rounded-md bg-blue-50 text-blue-700 border border-blue-200">
              {gradeData.grade} 김도윤
            </span>
          </div>
        </div>

        {/* Center: Clean Segmented Mode Tabs */}
        <div className="flex items-center bg-slate-100/80 p-1 rounded-xl border border-slate-200/60 overflow-x-auto">
          {modes.map((m) => {
            const isActive = studentMode === m.id;
            return (
              <button
                key={m.id}
                onClick={() => setStudentMode(m.id)}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition whitespace-nowrap cursor-pointer ${
                  isActive
                    ? 'bg-white text-blue-600 shadow-xs'
                    : 'text-slate-600 hover:text-slate-900'
                }`}
              >
                {m.label}
              </button>
            );
          })}
        </div>

        {/* Right: Key Metric & Quick Actions */}
        <div className="flex items-center gap-2">
          {/* SmartScore Pill */}
          <div className="hidden sm:flex items-center gap-1.5 bg-slate-50 border border-slate-200/80 px-2.5 py-1 rounded-lg text-xs">
            <span className="text-amber-500 font-bold">⚡</span>
            <span className="font-black text-slate-800">{currentSmartScore}점</span>
            <span className="text-slate-400">·</span>
            <span className="font-bold text-slate-500">{streakDays}일 연속</span>
          </div>

          <button
            onClick={onOpenCatModal}
            className="text-xs font-bold px-3 py-1.5 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 transition cursor-pointer"
          >
            🎯 CAT 진단
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
