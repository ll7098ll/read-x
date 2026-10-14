import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { speakKoreanText } from '../../utils/ttsEngine';
import { ParentInstantGlanceModal } from './ParentInstantGlanceModal';
import type { GradeData, SubskillMeta } from '../../types/courseware';

interface ParentXRayReportViewProps {
  gradeData: GradeData;
  subskillMeta: SubskillMeta[];
}

export const ParentXRayReportView: React.FC<ParentXRayReportViewProps> = ({
  gradeData,
  subskillMeta,
}) => {
  const { smartScores, setActiveRole, setStudentMode } = useCoursewareStore();
  const [copiedPrompt, setCopiedPrompt] = useState(false);
  const [showMobileGlance, setShowMobileGlance] = useState(false);

  const xr = gradeData.xray_overview;
  const dr = gradeData.diagnosis_report;
  const comm = gradeData.commercial;
  const ba = comm.before_after;
  const habit = comm.reading_habit;
  const talk = comm.parent_table_talk;
  const currentSmart = smartScores[gradeData.grade_num] ?? xr.overall_score;

  const criticalSkills = xr.subskill_matrix.filter((s) => s.state === 'critical');
  const masteredSkills = xr.subskill_matrix.filter((s) => s.state === 'mastered');

  const handleCopyQuestion = () => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(talk.parent_question);
      setCopiedPrompt(true);
      setTimeout(() => setCopiedPrompt(false), 2000);
    }
  };

  return (
    <div className="space-y-4">
      {/* Top Action Strip */}
      <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm flex flex-wrap items-center justify-between gap-3 print-card">
        <div>
          <div className="flex items-center gap-2">
            <span className="px-2.5 py-0.5 rounded-full text-xs font-extrabold bg-indigo-100 text-indigo-800">
              학부모 전용 정밀 진단·성장 리포트
            </span>
            <span className="text-xs font-bold text-slate-500">
              발행 기준: 2022 개정 교육과정 · KReaD 한국어 이독성 지수 · KICE 평가원 루브릭
            </span>
          </div>
          <h2 className="text-base md:text-lg font-black text-slate-900 mt-1">
            👨‍👩‍👧 {gradeData.persona_label.split(' · ')[0]} 학생의 설명문 문해력 X-Ray 종합 진단서
          </h2>
        </div>

        <div className="flex items-center gap-2 no-print">
          <button
            onClick={() => setShowMobileGlance(true)}
            className="px-3.5 py-2 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 font-black text-xs transition shadow-xs flex items-center gap-1.5 cursor-pointer"
          >
            <span>📱 모바일 알림톡 미리보기</span>
          </button>
          <button
            onClick={() => window.print()}
            className="px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold text-xs border border-slate-300 transition cursor-pointer"
          >
            🖨️ 진단 리포트 인쇄 / PDF 저장
          </button>
          <button
            onClick={() => {
              setActiveRole('student');
              setStudentMode('clinic');
            }}
            className="px-3.5 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-extrabold text-xs shadow transition"
          >
            💊 처방 클리닉 화면 직접 보기 ➔
          </button>
        </div>
      </div>

      {/* Row 1: Before/After Intervention Efficacy Slope + Reading Habit Telemetry */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* Card A: Before / After Prescription Growth Slope */}
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm print-card">
          <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100">
            <span className="font-black text-sm md:text-base text-slate-900">
              📈 [처방 전·후 성장 슬로프] 1:1 맞춤형 클리닉 처방 효과 검증
            </span>
            <span className="px-2 py-0.5 rounded text-xs font-extrabold bg-emerald-100 text-emerald-800">
              전이 검증 완료
            </span>
          </div>

          <div className="grid grid-cols-2 gap-3 mb-4">
            <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <div className="text-xs font-bold text-slate-500">
                집중 처방 위계 ({gradeData.slot_id})
              </div>
              <div className="flex items-baseline gap-2 mt-1">
                <span className="text-sm font-bold text-rose-600 line-through">
                  처방 전 {ba.before_score}점
                </span>
                <span className="text-slate-400">➔</span>
                <span className="text-xl font-black text-emerald-600">
                  처방 후 {ba.after_score}점
                </span>
              </div>
              <div className="h-2 bg-slate-200 rounded-full overflow-hidden mt-2 flex">
                <div
                  className="bg-rose-400 h-full"
                  style={{ width: `${ba.before_score}%` }}
                />
                <div
                  className="bg-emerald-500 h-full"
                  style={{ width: `${ba.after_score - ba.before_score}%` }}
                />
              </div>
              <div className="text-[11px] font-bold text-emerald-700 mt-1">
                ▲ +{ba.after_score - ba.before_score}점 급상승 (심각 결손 ➔ 마스터)
              </div>
            </div>

            <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200">
              <div className="text-xs font-bold text-slate-500">
                한국어 읽기 지수 (KReaD) 변화
              </div>
              <div className="flex items-baseline gap-2 mt-1">
                <span className="text-sm font-bold text-rose-600">
                  {ba.before_kread}
                </span>
                <span className="text-slate-400">➔</span>
                <span className="text-xl font-black text-blue-600">
                  {ba.after_kread}
                </span>
              </div>
              <div className="text-[11px] text-slate-600 mt-1.5">
                {gradeData.grade} 권장 표준 대역:{' '}
                <b>
                  KReaD {ba.kread_min} ~ {ba.kread_max}
                </b>
              </div>
              <div className="text-[11px] font-bold text-blue-700 mt-0.5">
                ✅ 학년 권장 이독성 안정권 진입!
              </div>
            </div>
          </div>

          <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-xs text-emerald-950 flex flex-wrap items-center justify-between gap-2">
            <div>
              <span className="font-black">🛡️ 획득한 오답 방어 면역:</span>{' '}
              <b>{ba.mastered_trap}</b> 완전 극복
            </div>
            <span className="px-2 py-0.5 rounded bg-emerald-600 text-white font-black text-[11px]">
              현재 종합 SmartScore {currentSmart}점
            </span>
          </div>
        </div>

        {/* Card B: Reading Habit & Telemetry Profile */}
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm print-card">
          <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100">
            <span className="font-black text-sm md:text-base text-slate-900">
              ⏱️ [독해 행동 프로파일] 지문 정독 시간 및 풀이 습관 텔레메트리
            </span>
            <span
              className={`px-2.5 py-0.5 rounded text-xs font-extrabold ${
                habit.badge_color === 'red'
                  ? 'bg-rose-100 text-rose-800'
                  : 'bg-amber-100 text-amber-800'
              }`}
            >
              {habit.type}
            </span>
          </div>

          <div className="grid grid-cols-3 gap-2.5 mb-3.5 text-center">
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <div className="text-[11px] font-bold text-slate-500">학생 평균 정독 시간</div>
              <div className="text-lg font-black text-rose-600 mt-0.5">
                {habit.avg_reading_sec}초
              </div>
            </div>
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <div className="text-[11px] font-bold text-slate-500">학년 권장 정독 시간</div>
              <div className="text-lg font-black text-blue-600 mt-0.5">
                {habit.target_reading_sec}초
              </div>
            </div>
            <div className="p-3 rounded-xl bg-slate-50 border border-slate-200">
              <div className="text-[11px] font-bold text-slate-500">1차 시도 정답률</div>
              <div className="text-lg font-black text-amber-600 mt-0.5">
                {habit.accuracy_first_try}%
              </div>
            </div>
          </div>

          <div className="p-3.5 rounded-xl bg-amber-50/90 border-l-4 border-amber-500 text-xs md:text-[13px] text-amber-950 leading-relaxed">
            <div className="font-black mb-1">🔎 AI 독해 습관 정밀 분석 소견:</div>
            {habit.habit_comment}
          </div>
        </div>
      </div>

      {/* Row 2: 4-Domain Balance & Top Vulnerable Subskills */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
        {/* 4 Domains Balance */}
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm print-card">
          <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100">
            <span className="font-black text-sm md:text-base text-slate-900">
              📊 [4대 영역 균형도] 사실 · 추론 · 비판 · 표현(쓰기) 성취 진단
            </span>
            <span className="text-xs font-bold text-slate-500">100점 만점 기준</span>
          </div>

          <div className="space-y-3">
            {dr.domain_scores.map((ds, idx) => {
              const barCls =
                ds.status === 'danger'
                  ? 'bg-rose-600'
                  : ds.status === 'warn'
                  ? 'bg-amber-500'
                  : 'bg-emerald-600';
              return (
                <div key={idx} className="space-y-1">
                  <div className="flex justify-between text-xs font-extrabold">
                    <span className="text-slate-900">{ds.domain}</span>
                    <span
                      className={
                        ds.status === 'danger'
                          ? 'text-rose-600'
                          : ds.status === 'warn'
                          ? 'text-amber-600'
                          : 'text-emerald-600'
                      }
                    >
                      {ds.score}점
                    </span>
                  </div>
                  <div className="h-2.5 bg-slate-200 rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full ${barCls}`}
                      style={{ width: `${ds.score}%` }}
                    />
                  </div>
                  <div className="text-[11px] text-slate-600">• {ds.comment}</div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Strengths vs Priority Prescription Subskills */}
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm print-card">
          <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-100">
            <span className="font-black text-sm md:text-base text-slate-900">
              🎯 [강점 & 집중 보완 기능] 16대 설명문 하위기능 핵심 요약
            </span>
            <span className="text-xs font-bold text-slate-500">맞춤 클리닉 직결</span>
          </div>

          <div className="space-y-3 text-xs">
            <div className="p-3 rounded-xl bg-rose-50 border border-rose-200">
              <div className="font-black text-rose-900 mb-1.5">
                🔴 최우선 보완이 필요한 하위기능 ({criticalSkills.length}개):
              </div>
              <div className="space-y-1.5">
                {criticalSkills.map((sk) => {
                  const meta = subskillMeta.find((m) => m.code === sk.code);
                  return (
                    <div key={sk.code} className="bg-white p-2 rounded-lg border border-rose-200">
                      <div className="font-extrabold text-rose-800">
                        [{sk.code}] {meta?.name} ({sk.score}점)
                      </div>
                      <div className="text-slate-600 mt-0.5">{sk.why}</div>
                    </div>
                  );
                })}
              </div>
            </div>

            <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200">
              <div className="font-black text-emerald-900 mb-1.5">
                🟢 이미 탄탄하게 마스터한 강점 기능 ({masteredSkills.length}개):
              </div>
              <div className="flex flex-wrap gap-1.5">
                {masteredSkills.map((sk) => {
                  const meta = subskillMeta.find((m) => m.code === sk.code);
                  return (
                    <span
                      key={sk.code}
                      className="px-2.5 py-1 rounded-lg bg-white border border-emerald-300 text-emerald-900 font-bold"
                    >
                      [{sk.code}] {meta?.name} ({sk.score}점)
                    </span>
                  );
                })}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Row 3: 5-Minute Home Table-Talk Coaching Script Card */}
      <div className="bg-gradient-to-br from-indigo-950 via-slate-900 to-blue-950 text-white rounded-2xl p-5 shadow-md border border-indigo-700/50 print-card">
        <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3.5 border-b border-white/15">
          <div>
            <span className="px-2.5 py-0.5 rounded-full text-[11px] font-extrabold bg-amber-400 text-slate-950">
              가정 연계 5분 문해력 코칭 스크립트
            </span>
            <h3 className="text-base md:text-lg font-black mt-1 text-white">
              🍽️ {talk.title}
            </h3>
          </div>
          <div className="flex items-center gap-2 no-print">
            <button
              onClick={() => speakKoreanText(talk.parent_question, 0.95)}
              className="px-3 py-1.5 rounded-xl bg-white/10 hover:bg-white/20 text-white text-xs font-extrabold border border-white/20 transition"
            >
              🔊 질문 예시 음성으로 듣기
            </button>
            <button
              onClick={handleCopyQuestion}
              className="px-3 py-1.5 rounded-xl bg-amber-400 hover:bg-amber-300 text-slate-950 text-xs font-black transition"
            >
              {copiedPrompt ? '✅ 질문 복사 완료!' : '📋 학부모 질문 복사하기'}
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5 text-xs md:text-sm">
          <div className="bg-white/10 rounded-xl p-3.5 border border-white/10">
            <div className="font-black text-sky-300 mb-1">🕒 ① 대화 상황 & 타이밍</div>
            <p className="text-slate-200 leading-relaxed">{talk.situation}</p>
          </div>

          <div className="bg-white/10 rounded-xl p-3.5 border border-amber-400/40">
            <div className="font-black text-amber-300 mb-1">💬 ② 부모님이 이렇게 질문해 보세요</div>
            <p className="text-white font-bold leading-relaxed">{talk.parent_question}</p>
          </div>

          <div className="bg-white/10 rounded-xl p-3.5 border border-emerald-400/40">
            <div className="font-black text-emerald-300 mb-1">👦 ③ 아이의 기대 답변 & 칭찬 포인트</div>
            <p className="text-emerald-100 leading-relaxed mb-2">{talk.expected_answer}</p>
            <div className="text-[11px] bg-slate-950/60 p-2 rounded-lg text-amber-200">
              💡 <b>코칭 팁:</b> {talk.coaching_tip}
            </div>
          </div>
        </div>
      </div>

      {/* Mobile Kakao AlimTalk Instant Web Card Modal */}
      {showMobileGlance && (
        <ParentInstantGlanceModal
          gradeData={gradeData}
          onClose={() => setShowMobileGlance(false)}
        />
      )}
    </div>
  );
};
