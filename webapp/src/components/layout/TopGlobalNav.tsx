import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type {
  GradeData,
  RoleType,
  StudentModeType,
  TeacherTabType,
  SlotLessonPackage,
} from '../../types/courseware';

interface TopGlobalNavProps {
  grades: GradeData[];
  gradeSlots16: SlotLessonPackage[];
  totalDbSlots: number;
}

export const TopGlobalNav: React.FC<TopGlobalNavProps> = ({
  grades,
  gradeSlots16,
  totalDbSlots,
}) => {
  const {
    activeRole,
    setActiveRole,
    activeGradeIdx,
    setActiveGradeIdx,
    activeSlotId,
    setActiveSlotId,
    studentMode,
    setStudentMode,
    teacherTab,
    setTeacherTab,
    smartScores,
    streakDays,
    unlockedVaccines,
    savedVocab,
    resetDemoProgress,
  } = useCoursewareStore();

  const currentGrade = grades[activeGradeIdx] || grades[4];
  const currentSmartScore =
    smartScores[currentGrade.grade_num] ?? currentGrade.xray_overview.overall_score;

  const activeSlotObj =
    gradeSlots16.find((s) => s.slot_id === (activeSlotId || currentGrade.slot_id)) ||
    gradeSlots16[0];

  const roles: Array<{ id: RoleType; label: string; sub: string }> = [
    { id: 'student', label: '👦 학생 학습 포털', sub: '16차시 코스맵 · 클리닉 · 스튜디오 · CBT' },
    { id: 'parent', label: '👨‍👩‍👧 학부모 리포트', sub: '10초 요약 · 6차원 X-Ray · 식탁 코칭' },
    { id: 'teacher', label: '👩‍🏫 교사 클래스 콘솔', sub: '학급 히트맵 · 일괄 처방 · 132위계' },
    { id: 'admin', label: '🏢 학원장 B2B & 문항 CMS', sub: `좌석 라이선스 · 상담 성적표 · ${totalDbSlots}슬롯 DB` },
  ];

  const studentSteps: Array<{ id: StudentModeType; num: number; title: string; sub: string }> = [
    {
      id: 'portal',
      num: 1,
      title: '① 6차원 X-Ray 진단 & 16차시 코스 맵',
      sub: '내 학년 16대 하위기능 전 차시 선택 · 6차원 X-Ray · 공통기초 6종',
    },
    {
      id: 'clinic',
      num: 2,
      title: '② 1:1 맞춤형 약점 처방 클리닉',
      sub: '선수 결손 징검다리 · 사고구술 Cloze · 6대 구조도 · 오답 백신 O/X',
    },
    {
      id: 'studio',
      num: 3,
      title: '③ 스플릿 리더 & 실전 수능·작문 스튜디오',
      sub: '7종 독서 도구 · 3단계 점진적 스캐폴딩 · EBSR · 빨간펜 퇴고 워크벤치',
    },
    {
      id: 'cbt_exam',
      num: 4,
      title: '④ KICE CBT 실전 모의고사',
      sub: '스캐폴딩 해제 · 제한시간 타이머 · OMR 답안지 · 전 선지 D1~D6 해부',
    },
  ];

  const teacherTabs: Array<{ id: TeacherTabType; label: string }> = [
    { id: 'matrix', label: '📊 학급 16하위기능 히트맵 & 일괄 처방 콘솔' },
    { id: 'gallery', label: '📚 1~6학년 대표 단원 비교뷰' },
    { id: 'standards', label: '📐 지문 복잡도(KReaD) & 수능 문항 설계 표준' },
    { id: 'hierarchy', label: '🗂️ 설명문 96개 + 공통기초 36개 마스터 위계 탐색기' },
  ];

  return (
    <header className="sticky top-0 z-40 bg-slate-900 text-white shadow-lg border-b border-slate-700 no-print">
      {/* Row 1: Brand + Live Telemetry + 4-Role Switcher */}
      <div className="max-w-[1600px] mx-auto px-4 py-2.5 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-500 to-indigo-600 flex items-center justify-center font-black text-lg shadow-md border border-blue-400/40">
            RX
          </div>
          <div>
            <div className="flex items-center gap-2 flex-wrap">
              <span className="font-extrabold text-base md:text-lg tracking-tight">
                ReadX-Ray Pro <span className="text-emerald-400">v3.0 Production</span>
              </span>
              <span className="text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-400/30 px-2 py-0.5 rounded-full">
                132슬롯 Item Bank DB (설명문 96 + 공통기초 36) 완비
              </span>
            </div>
            <p className="text-xs text-slate-400 hidden sm:block">
              6차원 X-Ray 정밀 진단 ➔ 132슬롯 전수 커리큘럼 ➔ 1:1 적응형 클리닉 ➔ 7대 TEI & KICE CBT 실전 모의고사
            </p>
          </div>
        </div>

        {/* Live Learner Telemetry Pills */}
        <div className="flex items-center gap-2 flex-wrap">
          <div className="bg-slate-800/90 border border-slate-700 rounded-lg px-2.5 py-1 text-xs flex items-center gap-1.5">
            <span className="text-amber-400 font-bold">⚡ SmartScore</span>
            <span className="font-black text-white text-sm">{currentSmartScore}</span>
            <span className="text-slate-400">/ 100</span>
          </div>
          <div className="bg-slate-800/90 border border-slate-700 rounded-lg px-2.5 py-1 text-xs flex items-center gap-1.5">
            <span className="text-orange-400 font-bold">🔥 스트릭</span>
            <span className="font-extrabold text-white">{streakDays}일</span>
          </div>
          <div className="bg-slate-800/90 border border-slate-700 rounded-lg px-2.5 py-1 text-xs flex items-center gap-1.5">
            <span className="text-emerald-400 font-bold">🛡️ 백신</span>
            <span className="font-extrabold text-white">{unlockedVaccines.length}/6종</span>
          </div>
          <div className="bg-slate-800/90 border border-slate-700 rounded-lg px-2.5 py-1 text-xs flex items-center gap-1.5">
            <span className="text-sky-400 font-bold">📒 단어장</span>
            <span className="font-extrabold text-white">{savedVocab.length}개</span>
          </div>
          <button
            onClick={resetDemoProgress}
            title="학습 이력 초기화"
            className="text-[11px] bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-600 px-2 py-1 rounded-lg transition"
          >
            🔄 이력 초기화
          </button>
        </div>

        {/* 4-Role Portal Switcher */}
        <nav className="flex items-center gap-1 bg-slate-950/70 p-1 rounded-xl border border-slate-800">
          {roles.map((r) => {
            const active = activeRole === r.id;
            return (
              <button
                key={r.id}
                onClick={() => setActiveRole(r.id)}
                className={`px-2.5 py-1.5 rounded-lg text-left transition-all ${
                  active
                    ? 'bg-blue-600 text-white shadow-sm ring-1 ring-blue-400'
                    : 'text-slate-300 hover:text-white hover:bg-slate-800/60'
                }`}
              >
                <div className="text-xs font-extrabold leading-tight">{r.label}</div>
                <div
                  className={`text-[10px] hidden 2xl:block ${
                    active ? 'text-blue-100' : 'text-slate-400'
                  }`}
                >
                  {r.sub}
                </div>
              </button>
            );
          })}
        </nav>
      </div>

      {/* Row 2: Grade 1~6 Context & 16-Slot Direct Selector Bar */}
      <div className="bg-slate-800/95 border-t border-slate-700/80 px-4 py-2">
        <div className="max-w-[1600px] mx-auto flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-extrabold text-blue-300">
              🎓 학습 학년 선택:
            </span>
            <div className="flex flex-wrap gap-1.5">
              {grades.map((g, idx) => {
                const isSelected = idx === activeGradeIdx;
                const sc = smartScores[g.grade_num] ?? g.xray_overview.overall_score;
                return (
                  <button
                    key={g.id}
                    onClick={() => setActiveGradeIdx(idx)}
                    className={`px-2.5 py-1 rounded-full text-xs font-extrabold transition-all flex items-center gap-1.5 border ${
                      isSelected
                        ? 'bg-amber-400 text-slate-950 border-amber-300 shadow-sm'
                        : 'bg-slate-900/90 text-slate-200 border-slate-600 hover:border-blue-400 hover:text-white'
                    }`}
                  >
                    <span>{g.grade}</span>
                    <span className="opacity-80">·</span>
                    <span>{g.persona_label.split(' · ')[0].replace(/^초\d\s/, '')}</span>
                    <span
                      className={`text-[10px] px-1.5 py-0.2 rounded-full font-black ${
                        isSelected
                          ? 'bg-slate-900 text-amber-300'
                          : sc >= 80
                          ? 'bg-emerald-900/70 text-emerald-300'
                          : 'bg-rose-900/70 text-rose-300'
                      }`}
                    >
                      {sc}점
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* 16-Lesson Direct Slot Picker for Current Grade */}
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-extrabold text-emerald-300">
              📚 현재 선택 차시 ({currentGrade.grade} 16개 위계 중 선택):
            </span>
            <select
              value={activeSlotObj?.slot_id || currentGrade.slot_id}
              onChange={(e) => setActiveSlotId(e.target.value)}
              className="bg-slate-900 text-white text-xs font-extrabold px-3 py-1.5 rounded-lg border border-slate-600 focus:outline-none focus:border-amber-400"
            >
              {gradeSlots16.map((slot, sIdx) => (
                <option key={slot.slot_id} value={slot.slot_id}>
                  {sIdx + 1}차시 [{slot.slot_id}] {slot.real_csat_test?.passage_title} ({slot.subskill_code})
                </option>
              ))}
            </select>
            <span className="text-[11px] bg-slate-900 px-2.5 py-1 rounded-lg border border-slate-700 text-sky-300 font-bold hidden xl:inline-block">
              KReaD {currentGrade.complexity_metrics.current_kread} (목표 {currentGrade.complexity_metrics.kread_target})
            </span>
          </div>
        </div>
      </div>

      {/* Row 3: Context Sub-Navigation (Student 4-Mode Loop OR Teacher 4-Tab Bar) */}
      {activeRole === 'student' && (
        <div className="bg-white text-slate-900 border-t border-slate-200 px-4 py-2 shadow-sm">
          <div className="max-w-[1600px] mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-2">
            {studentSteps.map((step) => {
              const active = studentMode === step.id;
              return (
                <button
                  key={step.id}
                  onClick={() => setStudentMode(step.id)}
                  className={`flex items-center gap-2.5 p-2 rounded-xl border text-left transition-all ${
                    active
                      ? 'bg-blue-50/90 border-blue-600 ring-1 ring-blue-600 shadow-sm'
                      : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  <div
                    className={`w-7 h-7 rounded-full flex items-center justify-center font-black text-xs shrink-0 ${
                      active ? 'bg-blue-600 text-white' : 'bg-slate-300 text-slate-700'
                    }`}
                  >
                    {step.num}
                  </div>
                  <div className="min-w-0">
                    <div
                      className={`text-xs font-extrabold truncate ${
                        active ? 'text-blue-900' : 'text-slate-800'
                      }`}
                    >
                      {step.title}
                    </div>
                    <div className="text-[11px] text-slate-500 truncate">{step.sub}</div>
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      )}

      {activeRole === 'teacher' && (
        <div className="bg-white text-slate-900 border-t border-slate-200 px-4 py-2 shadow-sm">
          <div className="max-w-[1600px] mx-auto flex flex-wrap gap-2">
            {teacherTabs.map((tab) => {
              const active = teacherTab === tab.id;
              return (
                <button
                  key={tab.id}
                  onClick={() => setTeacherTab(tab.id)}
                  className={`px-3.5 py-1.5 rounded-lg text-xs font-extrabold border transition-all ${
                    active
                      ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                      : 'bg-slate-50 text-slate-700 border-slate-300 hover:bg-slate-100'
                  }`}
                >
                  {tab.label}
                </button>
              );
            })}
          </div>
        </div>
      )}
    </header>
  );
};
