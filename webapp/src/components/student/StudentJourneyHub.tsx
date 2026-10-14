import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData, SlotLessonPackage } from '../../types/courseware';
import { VocabDuelArena } from './VocabDuelArena';
import { GalaxyExpeditionMap } from './GalaxyExpeditionMap';
import { OnboardingCatModal } from './OnboardingCatModal';

interface StudentJourneyHubProps {
  gradeData: GradeData;
  gradeSlots16: SlotLessonPackage[];
}

export const StudentJourneyHub: React.FC<StudentJourneyHubProps> = ({
  gradeData,
  gradeSlots16,
}) => {
  const {
    assignments,
    selectGradeAndSlot,
    setStudentMode,
    completeStudentAssignment,
    unlockedVaccines,
    streakDays,
    smartScores,
    savedVocab,
  } = useCoursewareStore();

  const [activeTab, setActiveTab] = useState<'todo' | 'completed' | 'progress'>('todo');
  const [showVocabDuel, setShowVocabDuel] = useState(false);
  const [showGalaxyMap, setShowGalaxyMap] = useState(false);
  const [showCatModal, setShowCatModal] = useState(false);

  const pendingAssignments = assignments.filter((a) => a.status === 'pending');
  const completedAssignments = assignments.filter((a) => a.status === 'completed');

  const currentSmart = smartScores[gradeData.grade_num] ?? gradeData.xray_overview.overall_score;

  const handleStartAssignment = (slotId: string, type: string, taskId: string) => {
    if (type === 'vocab') {
      setShowVocabDuel(true);
      return;
    }
    if (type === 'cat') {
      setShowCatModal(true);
      return;
    }
    if (type === 'clinic') {
      selectGradeAndSlot(gradeData.grade_num, slotId, 'clinic');
    } else {
      selectGradeAndSlot(gradeData.grade_num, slotId, 'studio');
    }
  };

  const handleSimulateSubmit = (taskId: string) => {
    completeStudentAssignment(taskId, 92);
  };

  return (
    <div className="space-y-5 font-sans">
      {/* 1. Clean Segmented Navigation Tab Bar */}
      <div className="bg-white rounded-2xl border border-slate-200/80 p-2 shadow-2xs flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-1.5 bg-slate-100/80 p-1 rounded-xl">
          <button
            onClick={() => setActiveTab('todo')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${
              activeTab === 'todo'
                ? 'bg-white text-blue-600 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>📝 오늘의 배정 과제함</span>
            <span
              className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                activeTab === 'todo' ? 'bg-blue-50 text-blue-700' : 'bg-slate-200 text-slate-700'
              }`}
            >
              {pendingAssignments.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('completed')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${
              activeTab === 'completed'
                ? 'bg-white text-emerald-600 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>✅ 완료 과제 & 오답노트</span>
            <span
              className={`px-2 py-0.5 rounded-full text-[10px] font-bold ${
                activeTab === 'completed' ? 'bg-emerald-50 text-emerald-700' : 'bg-slate-200 text-slate-700'
              }`}
            >
              {completedAssignments.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('progress')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${
              activeTab === 'progress'
                ? 'bg-white text-indigo-600 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>📈 내 진도 & 성장 트래커</span>
          </button>
        </div>

        {/* Quick Gamification Micro-Buttons */}
        <div className="flex items-center gap-1.5">
          <button
            onClick={() => setShowVocabDuel(true)}
            className="text-xs font-bold px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200/80 transition flex items-center gap-1 cursor-pointer"
          >
            <span>⚡ 10초 어휘 듀얼</span>
          </button>
          <button
            onClick={() => setShowGalaxyMap(true)}
            className="text-xs font-bold px-3 py-1.5 rounded-xl bg-indigo-50 hover:bg-indigo-100 text-indigo-900 border border-indigo-200/80 transition flex items-center gap-1 cursor-pointer"
          >
            <span>🌌 은하계 원정대</span>
          </button>
        </div>
      </div>

      {/* ================= TAB 1: 📝 오늘의 과제함 ================= */}
      {activeTab === 'todo' && (
        <div className="space-y-4">
          {/* Hero Mission Summary Card */}
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div className="space-y-1">
                <span className="text-[11px] font-bold text-blue-600 tracking-wider uppercase">
                  DAILY MISSION QUEUE
                </span>
                <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight">
                  오늘 해결할 과제가 <span className="text-blue-600">{pendingAssignments.length}개</span> 남아있습니다
                </h2>
                <p className="text-xs text-slate-500">
                  선생님과 6차원 X-Ray AI가 나의 사고 회로 취약점을 보강하기 위해 맞춤 배정한 일일 과제입니다.
                </p>
              </div>

              <div className="bg-slate-50 border border-slate-200/80 rounded-2xl p-4 text-right min-w-[170px]">
                <span className="text-[11px] font-bold text-slate-500 block">오늘의 과제 달성률</span>
                <span className="text-2xl font-black text-blue-600 mt-0.5 block">
                  {completedAssignments.length} <span className="text-slate-400 text-sm font-normal">/ {assignments.length}개 완료</span>
                </span>
              </div>
            </div>

            {/* Ergonomic Studio Quick Jump Banner */}
            <div className="pt-3.5 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3 text-xs">
              <div className="flex items-center gap-2 text-slate-600">
                <span className="font-bold text-slate-900 flex items-center gap-1">
                  <span>🎨</span>
                  <span>지문 독서 스튜디오:</span>
                </span>
                <span className="text-slate-500">
                  3색 형광펜 · 의미단위 끊어읽기(/) · 문단 집중리더가 본문 독서 시 완벽 지원됩니다.
                </span>
              </div>

              <button
                onClick={() => setStudentMode('studio')}
                className="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-xs transition flex items-center gap-1.5 cursor-pointer"
              >
                <span>📖 독서 스튜디오 바로가기 ➔</span>
              </button>
            </div>
          </div>

          {/* Assignments List Cards */}
          <div className="grid grid-cols-1 gap-3">
            {pendingAssignments.length === 0 ? (
              <div className="bg-white rounded-3xl border border-slate-200/80 p-10 text-center text-slate-500 space-y-2">
                <div className="text-3xl">🎉</div>
                <div className="font-black text-base text-slate-900">
                  오늘 배정된 모든 과제를 완벽하게 마쳤습니다!
                </div>
                <p className="text-xs text-slate-500 max-w-md mx-auto">
                  완료 과제 탭에서 오답노트를 복습하거나, 상단의 10초 어휘 듀얼에 도전해 보세요.
                </p>
              </div>
            ) : (
              pendingAssignments.map((task) => (
                <div
                  key={task.id}
                  className="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-xs hover:border-blue-300 transition flex flex-col md:flex-row md:items-center justify-between gap-4"
                >
                  <div className="space-y-1.5 flex-1">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span
                        className={`text-[10px] font-bold px-2 py-0.5 rounded-md ${
                          task.type === 'reading'
                            ? 'bg-blue-50 text-blue-700 border border-blue-200'
                            : task.type === 'clinic'
                            ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
                            : 'bg-amber-50 text-amber-700 border border-amber-200'
                        }`}
                      >
                        {task.type === 'reading'
                          ? '정규 독서과제'
                          : task.type === 'clinic'
                          ? '약점 클리닉'
                          : '어휘 훈련'}
                      </span>
                      <span className="text-xs font-bold text-slate-500 font-mono">
                        {task.slotId}
                      </span>
                      <span className="text-xs text-rose-600 font-bold bg-rose-50 px-2 py-0.5 rounded border border-rose-200/60">
                        기한: {task.dueDate}
                      </span>
                      {task.trapWarning && (
                        <span className="text-xs font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded border border-amber-200/80">
                          {task.trapWarning}
                        </span>
                      )}
                    </div>

                    <h3 className="text-base font-black text-slate-900 tracking-tight">
                      {task.title}
                    </h3>

                    <p className="text-xs text-slate-500">
                      배정: <b className="text-slate-700">{task.assignedBy}</b> · 1:1 맞춤 처방 연동
                    </p>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-2 shrink-0">
                    <button
                      onClick={() => handleSimulateSubmit(task.id)}
                      className="text-xs font-bold px-3 py-2 rounded-xl bg-slate-50 hover:bg-slate-100 text-slate-600 border border-slate-200 transition cursor-pointer"
                      title="실제 풀이 없이 완료 상태로 제출 시뮬레이션"
                    >
                      ✓ 제출 완료 처리
                    </button>
                    <button
                      onClick={() => handleStartAssignment(task.slotId, task.type, task.id)}
                      className="text-xs font-bold px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white shadow-xs transition flex items-center gap-1.5 cursor-pointer"
                    >
                      <span>▶ 과제 시작하기</span>
                    </button>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      )}

      {/* ================= TAB 2: ✅ 완료 과제 & 오답노트 ================= */}
      {activeTab === 'completed' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-5 shadow-xs flex items-center justify-between gap-3">
            <div>
              <h2 className="text-base font-black text-slate-900">
                제출 완료된 과제 성적표 및 오답노트 ({completedAssignments.length}건)
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                풀이를 완료한 과제의 점수, 획득한 오답 백신, 수능형 해설을 다시 복습할 수 있습니다.
              </p>
            </div>
            <span className="text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-xl border border-emerald-200">
              평균 92점 성취
            </span>
          </div>

          <div className="grid grid-cols-1 gap-3">
            {completedAssignments.map((task) => (
              <div
                key={task.id}
                className="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-xs space-y-3"
              >
                <div className="flex flex-wrap items-center justify-between gap-2 pb-2.5 border-b border-slate-100">
                  <div className="flex items-center gap-2">
                    <span className="w-5 h-5 rounded-full bg-emerald-500 text-white flex items-center justify-center text-xs font-bold">
                      ✓
                    </span>
                    <span className="font-black text-sm text-slate-900">{task.title}</span>
                    <span className="text-xs text-slate-500 font-mono">({task.slotId})</span>
                  </div>

                  <div className="flex items-center gap-2">
                    <span className="text-xs font-black text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-md border border-emerald-200">
                      점수: {task.score ?? 92}점
                    </span>
                    <span className="text-xs text-slate-400">제출 완료</span>
                  </div>
                </div>

                <div className="text-xs text-slate-600 leading-relaxed bg-slate-50/70 p-3 rounded-xl border border-slate-200/60">
                  <span className="font-bold text-slate-900 mr-1.5">💡 수능 오답 백신 해설:</span>
                  이 지문은 평가원 고난도 유형인 인과 전도(D2)와 속성 교차(D4) 함정이 설계되어 있습니다. 본문 2문단과 4문단의 중심 논증 구조를 정확히 짚어냄으로써 함정을 완벽히 방어했습니다.
                </div>

                <div className="flex justify-end gap-2 pt-1">
                  <button
                    onClick={() => selectGradeAndSlot(gradeData.grade_num, task.slotId, 'studio')}
                    className="text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 transition cursor-pointer"
                  >
                    지문 다시 읽기 ➔
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* ================= TAB 3: 📈 내 진도 & 성장 트래커 ================= */}
      {activeTab === 'progress' && (
        <div className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-white rounded-3xl border border-slate-200/80 p-5 shadow-xs space-y-1 text-center">
              <span className="text-xs font-bold text-slate-500">현재 SmartScore</span>
              <span className="text-3xl font-black text-blue-600 block mt-1">{currentSmart}점</span>
              <span className="text-xs text-emerald-600 font-bold">+14점 상승 중</span>
            </div>

            <div className="bg-white rounded-3xl border border-slate-200/80 p-5 shadow-xs space-y-1 text-center">
              <span className="text-xs font-bold text-slate-500">연속 학습 일수</span>
              <span className="text-3xl font-black text-amber-500 block mt-1">{streakDays}일 연속</span>
              <span className="text-xs text-slate-400 font-medium">매일 15분 루틴 실천</span>
            </div>

            <div className="bg-white rounded-3xl border border-slate-200/80 p-5 shadow-xs space-y-1 text-center">
              <span className="text-xs font-bold text-slate-500">획득 오답 백신</span>
              <span className="text-3xl font-black text-emerald-600 block mt-1">{unlockedVaccines.length} / 6종</span>
              <span className="text-xs text-emerald-600 font-bold">D1·D2·D4 면역 획득</span>
            </div>
          </div>

          {/* 16-Slot Curriculum Progress Table */}
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 shadow-xs space-y-4">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-base font-black text-slate-900">
                  {gradeData.grade} 16개 핵심 위계 패키지 이수 현황
                </h3>
                <p className="text-xs text-slate-500">
                  정규 설명문 슬롯과 취약 결손 보강 클리닉 슬롯의 전체 진척도입니다.
                </p>
              </div>
              <span className="text-xs font-bold text-blue-600 bg-blue-50 px-3 py-1 rounded-xl border border-blue-200">
                이수율 62.5%
              </span>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-8 gap-2">
              {gradeSlots16.slice(0, 16).map((slot, idx) => {
                const isCurrent = slot.slot_id === gradeData.slot_id;
                const isPassed = idx < 10;
                return (
                  <button
                    key={slot.slot_id}
                    onClick={() => selectGradeAndSlot(gradeData.grade_num, slot.slot_id, 'studio')}
                    className={`p-3 rounded-2xl border text-center transition cursor-pointer ${
                      isCurrent
                        ? 'bg-blue-600 text-white border-blue-600 shadow-xs'
                        : isPassed
                        ? 'bg-emerald-50 text-emerald-900 border-emerald-200 hover:bg-emerald-100'
                        : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100'
                    }`}
                  >
                    <div className="text-[10px] font-bold opacity-80">#{idx + 1}</div>
                    <div className="text-xs font-black truncate mt-0.5">{slot.slot_id}</div>
                    <div className="text-[10px] font-bold mt-1">
                      {isPassed ? '✓ 완료' : '진행전'}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}

      {/* Gamification Modals */}
      {showVocabDuel && (
        <VocabDuelArena
          vocabList={gradeData.real_csat_test.vocab_notes || []}
          onClose={() => setShowVocabDuel(false)}
        />
      )}
      {showGalaxyMap && (
        <GalaxyExpeditionMap onClose={() => setShowGalaxyMap(false)} />
      )}
      {showCatModal && (
        <OnboardingCatModal
          gradeData={gradeData}
          onClose={() => setShowCatModal(false)}
        />
      )}
    </div>
  );
};
