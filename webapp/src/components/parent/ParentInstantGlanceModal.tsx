import React from 'react';
import type { GradeData } from '../../types/courseware';

interface ParentInstantGlanceModalProps {
  gradeData: GradeData;
  onClose: () => void;
}

export const ParentInstantGlanceModal: React.FC<ParentInstantGlanceModalProps> = ({
  gradeData,
  onClose,
}) => {
  const xr = gradeData.xray_overview;
  const ba = gradeData.commercial.before_after;
  const talk = gradeData.commercial.parent_table_talk;

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-sm flex items-center justify-center p-3 animate-in fade-in">
      {/* Mobile Device Frame */}
      <div className="bg-slate-900 border-4 border-slate-700 rounded-[40px] max-w-sm w-full p-3 shadow-2xl relative overflow-hidden flex flex-col max-h-[92vh]">
        {/* Phone Notch / Speaker bar */}
        <div className="w-24 h-4 bg-slate-800 rounded-full mx-auto mb-2 shrink-0 flex items-center justify-center">
          <div className="w-3 h-3 rounded-full bg-slate-900 mr-2" />
          <div className="w-8 h-1 bg-slate-700 rounded-full" />
        </div>

        {/* Smartphone Screen Content */}
        <div className="bg-[#FCFBF7] rounded-[30px] p-4 text-slate-900 flex-1 overflow-y-auto space-y-3.5 shadow-inner">
          {/* Top Kakao AlimTalk Banner */}
          <div className="bg-[#FEE500] text-[#3C1E1E] p-2.5 rounded-2xl flex items-center justify-between shadow-xs">
            <div className="flex items-center gap-2">
              <span className="w-6 h-6 rounded-full bg-[#3C1E1E] text-[#FEE500] flex items-center justify-center text-xs font-black">
                TALK
              </span>
              <span className="text-xs font-black">카카오 알림톡 도착</span>
            </div>
            <button
              onClick={onClose}
              className="text-[#3C1E1E] font-bold text-xs p-1 cursor-pointer"
            >
              ✕
            </button>
          </div>

          {/* Report Header */}
          <div className="text-center pt-1">
            <span className="text-[11px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded-full border border-blue-200">
              {gradeData.grade} 맞춤 문해력 리포트
            </span>
            <h4 className="text-base font-black text-slate-900 mt-1">
              오늘의 10초 X-Ray 진단
            </h4>
            <p className="text-[11px] text-slate-500 font-mono">
              수록 지문: 「{gradeData.real_csat_test.passage_title}」
            </p>
          </div>

          {/* Where · Why · How 10-Second Summary Card */}
          <div className="bg-white rounded-2xl p-3 border border-slate-200 shadow-xs space-y-2 text-xs">
            <div className="flex items-start gap-2">
              <span className="px-1.5 py-0.5 rounded bg-rose-100 text-rose-800 font-bold shrink-0 text-[10px]">
                어디가
              </span>
              <span className="font-bold text-slate-800">{xr.where_summary}</span>
            </div>
            <div className="flex items-start gap-2">
              <span className="px-1.5 py-0.5 rounded bg-amber-100 text-amber-800 font-bold shrink-0 text-[10px]">
                왜·어떻게
              </span>
              <span className="text-slate-700 leading-snug">{xr.how_summary}</span>
            </div>
          </div>

          {/* Before ➔ After Growth Metric Slope */}
          <div className="bg-emerald-50 rounded-2xl p-3 border border-emerald-200 space-y-1.5 text-xs text-emerald-950">
            <div className="font-bold flex justify-between items-center">
              <span>📈 1:1 처방 전후 성장</span>
              <span className="text-[10px] bg-emerald-200 text-emerald-900 px-2 py-0.5 rounded-full font-bold">
                백신 통과 완료
              </span>
            </div>
            <div className="grid grid-cols-2 gap-2 text-center pt-1">
              <div className="bg-white/80 p-2 rounded-xl">
                <span className="text-[10px] text-slate-500 block">처방 전</span>
                <span className="font-bold text-sm text-slate-700">{ba.before_score}점</span>
              </div>
              <div className="bg-white/80 p-2 rounded-xl border border-emerald-300">
                <span className="text-[10px] text-emerald-700 font-bold block">처방 후</span>
                <span className="font-black text-sm text-emerald-600">{ba.after_score}점 🎉</span>
              </div>
            </div>
            <div className="text-[11px] text-center pt-1 text-emerald-800 font-medium">
              KReaD 지수: <b>{ba.before_kread}</b> ➔ <b>{ba.after_kread}</b> (면역 획득: {ba.mastered_trap})
            </div>
          </div>

          {/* Dinner Table Coaching Card */}
          <div className="bg-indigo-50/80 rounded-2xl p-3 border border-indigo-200 space-y-2 text-xs">
            <div className="font-bold text-indigo-950 flex items-center gap-1.5">
              <span>🏠 오늘 저녁 5분 식탁 질문</span>
            </div>
            <div className="p-2 rounded-xl bg-white border border-indigo-100 text-[11.5px] font-bold text-indigo-900 leading-snug">
              💬 "{talk.parent_question}"
            </div>
            <div className="text-[11px] text-slate-600 leading-snug">
              <b>💡 기대 답변 예시:</b> {talk.expected_answer}
            </div>
            <div className="text-[10px] text-slate-500 italic bg-white/60 p-1.5 rounded-lg">
              칭찬 팁: {talk.coaching_tip}
            </div>
          </div>

          {/* Action Footer */}
          <div className="pt-1">
            <button
              onClick={onClose}
              className="w-full py-2.5 rounded-xl bg-slate-900 text-white font-bold text-xs shadow-md cursor-pointer"
            >
              확인 완료 (창 닫기)
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
