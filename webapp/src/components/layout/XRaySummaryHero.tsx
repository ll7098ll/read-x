import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';

interface XRaySummaryHeroProps {
  gradeData: GradeData;
}

export const XRaySummaryHero: React.FC<XRaySummaryHeroProps> = ({ gradeData }) => {
  const { smartScores, activeRole, setStudentMode, setActiveRole } = useCoursewareStore();
  const xr = gradeData.xray_overview;
  const currentSmart = smartScores[gradeData.grade_num] ?? xr.overall_score;
  const habit = gradeData.commercial.reading_habit;

  return (
    <div className="bg-gradient-to-r from-slate-900 via-slate-800 to-indigo-950 text-white rounded-2xl p-4 md:p-5 mb-4 shadow-md border border-slate-700/80 print-card">
      {/* Top Row: Persona Info + KReaD & SmartScore Badges */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-3.5 border-b border-white/15">
        <div className="flex items-center gap-3.5">
          <div className="w-12 h-12 rounded-2xl bg-blue-600/30 border-2 border-blue-400 flex items-center justify-center font-black text-base text-blue-200 shrink-0 shadow-inner">
            {gradeData.grade}
          </div>
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <h2 className="text-base md:text-lg font-black tracking-tight text-white">
                {gradeData.persona_label}
              </h2>
              <span className="px-2.5 py-0.5 rounded-md text-xs font-extrabold bg-blue-500/25 text-blue-200 border border-blue-400/30">
                집중 타깃: {gradeData.slot_id} ({gradeData.layer})
              </span>
              <span className="px-2.5 py-0.5 rounded-md text-xs font-extrabold bg-amber-500/25 text-amber-200 border border-amber-400/30">
                초기 진단 {xr.overall_score}점 ({xr.percentile}) ➔ 현재 SmartScore {currentSmart}점
              </span>
            </div>
            <p className="text-xs text-slate-300 mt-1">
              교과 연계 단원: <b className="text-white">{gradeData.curriculum_concept.subject} — {gradeData.curriculum_concept.unit} ({gradeData.curriculum_concept.concept})</b>
              <span className="mx-2 text-slate-500">|</span>
              독해 습관 유형: <b className="text-amber-300">{habit.type}</b>
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2.5 flex-wrap">
          <div className="bg-white/10 backdrop-blur px-3 py-1.5 rounded-xl border border-white/15 text-xs">
            <div>
              현재 읽기 지수: <b className="text-rose-300">KReaD {gradeData.complexity_metrics.current_kread}</b>
            </div>
            <div>
              학년 권장 목표: <b className="text-sky-300">KReaD {gradeData.complexity_metrics.kread_target}</b>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Row: Where & Why/How 10-Second X-Ray Cards */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-3 mt-3.5">
        <div className="bg-slate-950/55 rounded-xl p-3 border border-white/10 border-l-4 border-l-rose-400">
          <div className="text-xs font-extrabold text-rose-300 mb-1 flex items-center justify-between">
            <span>📍 [어디가 부족한가? — 결손 위치(Where) 정밀 진단]</span>
            <span className="text-[11px] bg-rose-500/20 text-rose-200 px-2 py-0.5 rounded">위계 결손 좌표</span>
          </div>
          <p className="text-xs md:text-[13px] text-slate-200 leading-relaxed">{xr.where_summary}</p>
        </div>

        <div className="bg-slate-950/55 rounded-xl p-3 border border-white/10 border-l-4 border-l-amber-400">
          <div className="text-xs font-extrabold text-amber-300 mb-1 flex items-center justify-between">
            <span>🧠 [왜·어떻게 틀리는가? — 인지 병목·오답 메커니즘(How) 진단]</span>
            <span className="text-[11px] bg-amber-500/20 text-amber-200 px-2 py-0.5 rounded">Dick & Carey 병목</span>
          </div>
          <p className="text-xs md:text-[13px] text-slate-200 leading-relaxed">{xr.how_summary}</p>
        </div>
      </div>
    </div>
  );
};
