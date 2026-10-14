import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData, SubskillMeta } from '../../types/courseware';
import { ParentInstantGlanceModal } from './ParentInstantGlanceModal';

interface ParentJourneyHubProps {
  gradeData: GradeData;
  subskillMeta: SubskillMeta[];
}

export const ParentJourneyHub: React.FC<ParentJourneyHubProps> = ({
  gradeData,
  subskillMeta,
}) => {
  const { assignments, smartScores, streakDays, unlockedVaccines } = useCoursewareStore();

  const [activeTab, setActiveTab] = useState<'today_activity' | 'xray_detail' | 'growth_trend' | 'table_talk'>('today_activity');
  const [showMobileModal, setShowMobileModal] = useState(false);

  const xr = gradeData.xray_overview;
  const currentSmart = smartScores[gradeData.grade_num] ?? xr.overall_score;

  const completedTasks = assignments.filter((a) => a.status === 'completed');
  const pendingTasks = assignments.filter((a) => a.status === 'pending');

  return (
    <div className="space-y-5 font-sans">
      {/* 1. Clean Navigation Segmented Tab Bar */}
      <div className="bg-white rounded-2xl border border-slate-200/80 p-2 shadow-2xs flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-1.5 bg-slate-100/80 p-1 rounded-xl">
          <button
            onClick={() => setActiveTab('today_activity')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${
              activeTab === 'today_activity'
                ? 'bg-white text-emerald-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>🔔 오늘 자녀 활동 현황</span>
            <span
              className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                activeTab === 'today_activity' ? 'bg-emerald-50 text-emerald-700' : 'bg-slate-200 text-slate-700'
              }`}
            >
              {completedTasks.length}건 완료
            </span>
          </button>

          <button
            onClick={() => setActiveTab('xray_detail')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer ${
              activeTab === 'xray_detail'
                ? 'bg-white text-emerald-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>📋 6차원 X-Ray 진단서</span>
          </button>

          <button
            onClick={() => setActiveTab('growth_trend')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer ${
              activeTab === 'growth_trend'
                ? 'bg-white text-emerald-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>📈 주간·월간 성장 추이</span>
          </button>

          <button
            onClick={() => setActiveTab('table_talk')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer ${
              activeTab === 'table_talk'
                ? 'bg-white text-emerald-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>🍽️ 밥상머리 대화 가이드</span>
          </button>
        </div>

        <button
          onClick={() => setShowMobileModal(true)}
          className="text-xs font-bold px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200/80 transition flex items-center gap-1.5 cursor-pointer"
        >
          <span>📱 모바일 알림톡 미리보기</span>
        </button>
      </div>

      {/* ================= TAB 1: 🔔 오늘 자녀 활동 현황 ================= */}
      {activeTab === 'today_activity' && (
        <div className="space-y-4">
          {/* Summary Hero Card */}
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div className="space-y-1">
                <span className="text-[11px] font-bold text-emerald-600 tracking-wider uppercase">
                  TODAY'S CHILD ACTIVITY
                </span>
                <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
                  오늘 김도윤 학생이 <span className="text-emerald-600">{completedTasks.length}건</span>의 과제를 완수했습니다
                </h2>
                <p className="text-xs text-slate-500">
                  학교와 학원에서 배정된 수능형 설명문 독해 과제를 성실하게 수행하고 있습니다.
                </p>
              </div>

              <div className="flex items-center gap-2">
                <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 text-center min-w-[120px]">
                  <span className="text-[11px] font-bold text-slate-500 block">과제 완수</span>
                  <span className="text-xl font-black text-emerald-600 mt-0.5 block">
                    {completedTasks.length} / {assignments.length}건
                  </span>
                </div>
                <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 text-center min-w-[120px]">
                  <span className="text-[11px] font-bold text-slate-500 block">연속 실천</span>
                  <span className="text-xl font-black text-amber-500 mt-0.5 block">
                    🔥 {streakDays}일차
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Activity Cards List */}
          <div className="grid grid-cols-1 gap-3">
            {completedTasks.map((task) => (
              <div
                key={task.id}
                className="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-xs space-y-3"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 border-b border-slate-100">
                  <div className="flex items-center gap-2.5">
                    <span className="w-6 h-6 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold">
                      ✓
                    </span>
                    <div>
                      <h3 className="font-black text-sm text-slate-900">{task.title}</h3>
                      <span className="text-[11px] text-slate-400 font-mono">
                        {task.completedAt} · 배정: {task.assignedBy}
                      </span>
                    </div>
                  </div>

                  <span className="text-xs font-black text-emerald-700 bg-emerald-50 px-3 py-1 rounded-xl border border-emerald-200">
                    획득 성적: {task.score}점
                  </span>
                </div>

                <div className="p-3.5 rounded-xl bg-slate-50/70 border border-slate-200/60 text-xs leading-relaxed space-y-1">
                  <span className="font-bold text-slate-800 block">
                    👨‍🏫 담임 선생님 지도 코멘트: "정확한 근거 문장 매핑으로 고난도 비약 함정을 훌륭히 극복했습니다."
                  </span>
                  <p className="text-slate-600">
                    오늘 아이가 수능형 설명문을 차분히 완독하고, 주장-근거 연동 문항을 우수한 성적으로 통과했습니다.
                  </p>
                </div>
              </div>
            ))}

            {pendingTasks.map((task) => (
              <div
                key={task.id}
                className="bg-white rounded-2xl border border-slate-200/60 p-4 shadow-2xs flex items-center justify-between text-xs opacity-70"
              >
                <div className="flex items-center gap-2.5">
                  <span className="w-5 h-5 rounded-full bg-slate-100 text-slate-400 flex items-center justify-center font-bold text-xs">
                    ⏳
                  </span>
                  <div>
                    <span className="font-bold text-slate-800">{task.title}</span>
                    <span className="text-slate-400 block text-[11px]">기한: {task.dueDate}</span>
                  </div>
                </div>
                <span className="text-slate-500 font-bold bg-slate-100 px-2.5 py-1 rounded-lg">
                  진행 예정
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ================= TAB 2: 📋 6차원 X-Ray 진단서 ================= */}
      {activeTab === 'xray_detail' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div>
              <h2 className="text-lg font-black text-slate-900 tracking-tight">
                김도윤 학생 6차원 인지 X-Ray 정밀 진단 리포트
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                동학년 전국 백분위 상위 {xr.percentile} 수준이며, 세부 영역별 균형도를 분석한 결과입니다.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80 space-y-1.5">
                <span className="font-black text-slate-900 block text-sm">📍 취약 위치 (Where)</span>
                <p className="text-slate-600 leading-relaxed">{xr.where_summary}</p>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80 space-y-1.5">
                <span className="font-black text-slate-900 block text-sm">🧠 오답 메커니즘 (Why & How)</span>
                <p className="text-slate-600 leading-relaxed">{xr.how_summary}</p>
              </div>
            </div>

            {/* 6D Radar Bars */}
            <div className="pt-2 space-y-3">
              <span className="text-xs font-black text-slate-800 block">
                6대 인지 영역별 세부 성취도:
              </span>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { name: '어휘 정밀도 (V)', score: 85, grade: '1등급' },
                  { name: '사실적 정보 추출 (F)', score: 92, grade: '1등급' },
                  { name: '인과 추론 (I)', score: 58, grade: '3등급 (보강 권장)' },
                  { name: '구조 분석 (S)', score: 76, grade: '2등급' },
                  { name: '비판적 평가 (E)', score: 68, grade: '2등급' },
                  { name: '메타인지 조절 (M)', score: 64, grade: '2등급' },
                ].map((dom, idx) => (
                  <div
                    key={idx}
                    className="p-3.5 rounded-xl border border-slate-200/80 bg-white flex items-center justify-between text-xs"
                  >
                    <span className="font-bold text-slate-800">{dom.name}</span>
                    <span className="font-black text-emerald-700">{dom.score}점 ({dom.grade})</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ================= TAB 3: 📈 주간·월간 성장 추이 ================= */}
      {activeTab === 'growth_trend' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div>
              <h2 className="text-lg font-black text-slate-900 tracking-tight">
                최근 4주간 KReaD 독서지수 성장 추이
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                체계적인 1:1 맞춤 클리닉을 통해 고난도 어휘 및 추론 영역이 지속 상승하고 있습니다.
              </p>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80">
                <span className="text-slate-400 text-xs block">1주 전</span>
                <span className="text-xl font-black text-slate-700 mt-1 block">850</span>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80">
                <span className="text-slate-400 text-xs block">2주 전</span>
                <span className="text-xl font-black text-slate-700 mt-1 block">890</span>
              </div>
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80">
                <span className="text-slate-400 text-xs block">3주 전</span>
                <span className="text-xl font-black text-slate-700 mt-1 block">915</span>
              </div>
              <div className="p-4 rounded-2xl bg-emerald-50 border border-emerald-200">
                <span className="text-emerald-700 text-xs font-bold block">현재 지수</span>
                <span className="text-2xl font-black text-emerald-900 mt-0.5 block">940</span>
                <span className="text-[11px] text-emerald-700 font-bold block mt-0.5">+90점 상승 🚀</span>
              </div>
            </div>

            <p className="text-xs text-slate-500 leading-relaxed bg-slate-50/70 p-4 rounded-2xl border border-slate-200/60">
              * 지난 4주간 꾸준한 약점 처방 클리닉 이수를 통해 KReaD 한국어 독서지수가 850에서 940으로 대폭 향상되었으며, 초등 5학년 권장 독서 궤도에 완벽하게 안착했습니다.
            </p>
          </div>
        </div>
      )}

      {/* ================= TAB 4: 🍽️ 밥상머리 대화 가이드 ================= */}
      {activeTab === 'table_talk' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div className="border-b border-slate-100 pb-3">
              <h2 className="text-lg font-black text-slate-900 tracking-tight">
                오늘 저녁 식탁에서 아이와 나눌 수 있는 밥상머리 대화 가이드
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                오늘 아이가 읽은 설명문 「{gradeData.real_csat_test.passage_title}」을 바탕으로 자연스럽게 대화를 이끌어 보세요.
              </p>
            </div>

            <div className="space-y-3">
              <div className="p-4 rounded-2xl bg-emerald-50/60 border border-emerald-200/80 text-xs space-y-2">
                <span className="font-black text-emerald-950 block text-sm">
                  Q1. "도윤아, 오늘 지문에서 인공지능이 스스로 학습할 때 가중치가 왜 중요하다고 했어?"
                </span>
                <p className="text-slate-700 leading-relaxed">
                  💡 <b>기대 답변</b>: "가중치가 뉴런 사이의 연결 강도인데, 오차를 줄이려고 계속 미세하게 바뀌는 원리라고 했어요!"
                </p>
                <p className="text-emerald-800 font-bold text-[11px]">
                  👏 <b>칭찬 코칭 팁</b>: 인간의 뇌 시냅스와 비교해서 설명해낸 점을 구체적으로 칭찬해 주세요.
                </p>
              </div>

              <div className="p-4 rounded-2xl bg-blue-50/60 border border-blue-200/80 text-xs space-y-2">
                <span className="font-black text-blue-950 block text-sm">
                  Q2. "글쓴이가 주장한 내용 중에서 혹시 논리적인 비약이 있었던 부분은 없었니?"
                </span>
                <p className="text-slate-700 leading-relaxed">
                  💡 <b>기대 답변</b>: "초콜릿 소비가 많다고 노벨상을 잘 탄다는 건 경제력이라는 다른 원인을 놓친 비약이라고 찾았어요!"
                </p>
                <p className="text-blue-800 font-bold text-[11px]">
                  👏 <b>칭찬 코칭 팁</b>: 상관관계와 인과관계를 구별해 낸 논리적 사고력을 높이 평가해 주세요.
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Modal */}
      {showMobileModal && (
        <ParentInstantGlanceModal
          gradeData={gradeData}
          onClose={() => setShowMobileModal(false)}
        />
      )}
    </div>
  );
};
