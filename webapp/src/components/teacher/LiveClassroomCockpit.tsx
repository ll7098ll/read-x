import React, { useState, useEffect } from 'react';
import type { TeacherRosterStudent } from '../../types/courseware';

interface LiveClassroomCockpitProps {
  roster: TeacherRosterStudent[];
  lessonTitle?: string;
  onClose?: () => void;
}

interface LiveStudentStatus {
  id: string;
  name: string;
  currentPara: number;
  highlightCount: number;
  lastTrap: string | null;
  status: 'reading' | 'solving' | 'trapped' | 'mastered';
}

export const LiveClassroomCockpit: React.FC<LiveClassroomCockpitProps> = ({
  roster,
  lessonTitle = '초등 5학년 과학 [신경계와 인공신경망]',
  onClose,
}) => {
  // Simulated live state for 12 active students
  const [liveStudents, setLiveStudents] = useState<LiveStudentStatus[]>([]);
  const [broadcastMsg, setBroadcastMsg] = useState<string | null>(null);

  useEffect(() => {
    const initial: LiveStudentStatus[] = roster.slice(0, 12).map((st, idx) => ({
      id: st.student_id,
      name: st.name,
      currentPara: (idx % 4) + 1,
      highlightCount: Math.floor(Math.random() * 5) + 1,
      lastTrap: idx === 1 ? 'D1 (인과 역전)' : idx === 5 ? 'D4 (속성 교차)' : null,
      status: idx === 1 || idx === 5 ? 'trapped' : idx % 3 === 0 ? 'mastered' : 'reading',
    }));
    setLiveStudents(initial);

    // Heartbeat simulation: students move through paragraphs
    const interval = setInterval(() => {
      setLiveStudents((prev) =>
        prev.map((s) => {
          if (s.status === 'trapped') return s;
          const nextPara = s.currentPara >= 4 ? 4 : s.currentPara + (Math.random() > 0.7 ? 1 : 0);
          return {
            ...s,
            currentPara: nextPara,
            highlightCount: s.highlightCount + (Math.random() > 0.8 ? 1 : 0),
          };
        })
      );
    }, 4000);

    return () => clearInterval(interval);
  }, [roster]);

  const handleSendHintToStudent = (studentName: string) => {
    setBroadcastMsg(`🚀 [${studentName}] 학생의 화면으로 1단계 단서 스포트라이트 힌트가 전송되었습니다.`);
    setTimeout(() => setBroadcastMsg(null), 3000);
  };

  const handleBroadcastScaffolding = () => {
    setBroadcastMsg('📢 학급 전체 학생에게 「사고구술 공식 힌트」를 동시 전송했습니다.');
    setTimeout(() => setBroadcastMsg(null), 3500);
  };

  return (
    <div className="bg-white rounded-3xl border border-slate-200/80 p-6 shadow-xs space-y-4 font-sans text-slate-800">
      {/* Cockpit Header */}
      <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-100">
        <div className="flex items-center gap-3">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
          <div>
            <div className="flex items-center gap-2">
              <h3 className="text-base font-black text-slate-900 tracking-tight">
                실시간 독서 관제 조종석 (Live Cockpit)
              </h3>
              <span className="px-2 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-[10px] font-bold">
                12명 동시 모니터링 중
              </span>
            </div>
            <p className="text-xs text-slate-500 mt-0.5">
              수업: <b className="text-indigo-700">{lessonTitle}</b>
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={handleBroadcastScaffolding}
            className="px-3.5 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold transition shadow-xs cursor-pointer"
          >
            📢 전체 힌트 일괄 전송
          </button>
          {onClose && (
            <button
              onClick={onClose}
              className="text-slate-400 hover:text-slate-700 font-bold text-sm p-1"
            >
              ✕
            </button>
          )}
        </div>
      </div>

      {broadcastMsg && (
        <div className="p-3 bg-indigo-50 border border-indigo-200 text-indigo-900 text-xs font-bold rounded-xl animate-fade-in flex items-center justify-between">
          <span>{broadcastMsg}</span>
          <button onClick={() => setBroadcastMsg(null)} className="text-indigo-400 hover:text-indigo-700">
            ✕
          </button>
        </div>
      )}

      {/* 12-Student Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
        {liveStudents.map((st) => {
          const isTrapped = st.status === 'trapped';
          const isMastered = st.status === 'mastered';

          return (
            <div
              key={st.id}
              className={`p-4 rounded-2xl border transition-all ${
                isTrapped
                  ? 'bg-rose-50/70 border-rose-300 ring-1 ring-rose-300'
                  : isMastered
                  ? 'bg-emerald-50/50 border-emerald-200'
                  : 'bg-slate-50/70 border-slate-200/80 hover:bg-slate-100/50'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="font-bold text-sm text-slate-900">{st.name}</span>
                <span
                  className={`text-[10px] font-bold px-1.5 py-0.5 rounded ${
                    isTrapped
                      ? 'bg-rose-100 text-rose-800'
                      : isMastered
                      ? 'bg-emerald-100 text-emerald-800'
                      : 'bg-blue-100 text-blue-800'
                  }`}
                >
                  {isTrapped ? '⚠️ 함정 정체' : isMastered ? '완전 정복' : '정독 중'}
                </span>
              </div>

              <div className="space-y-1 text-xs text-slate-600">
                <div className="flex justify-between">
                  <span>현재 위치:</span>
                  <b className="text-slate-900">{st.currentPara}문단 독서 중</b>
                </div>
                <div className="flex justify-between">
                  <span>형광펜 수집:</span>
                  <b>{st.highlightCount}개 단서</b>
                </div>
                {st.lastTrap && (
                  <div className="text-rose-700 font-bold text-[11px] pt-1 border-t border-rose-200">
                    병목: {st.lastTrap}
                  </div>
                )}
              </div>

              {isTrapped && (
                <button
                  onClick={() => handleSendHintToStudent(st.name)}
                  className="mt-3 w-full py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-xs transition cursor-pointer"
                >
                  스포트라이트 힌트 전송 ➔
                </button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
