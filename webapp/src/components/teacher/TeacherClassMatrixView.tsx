import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { LiveClassroomCockpit } from './LiveClassroomCockpit';
import type {
  CommercialMasterData,
  TeacherRosterStudent,
  HierarchyGoal,
} from '../../types/courseware';

interface TeacherClassMatrixViewProps {
  data: CommercialMasterData;
}

export const TeacherClassMatrixView: React.FC<TeacherClassMatrixViewProps> = ({ data }) => {
  const {
    teacherTab,
    setActiveRole,
    setActiveGradeIdx,
    setStudentMode,
    selectGradeAndSlot,
    teacherClinicAssigned,
    assignTeacherClinic,
  } = useCoursewareStore();

  // Tab 1: Class Matrix state
  const [showLiveCockpit, setShowLiveCockpit] = useState(false);
  const [triageFilter, setTriageFilter] = useState<'ALL' | 'critical' | 'fragile' | 'guessing' | 'mastered'>('ALL');
  const [selectedStudentIds, setSelectedStudentIds] = useState<string[]>(['stu-01', 'stu-02', 'stu-03', 'stu-07']);
  const [drawerStudent, setDrawerStudent] = useState<TeacherRosterStudent | null>(null);
  const [batchBannerMsg, setBatchBannerMsg] = useState<string | null>(null);

  // Tab 4: 96 + 36 Hierarchy Explorer state
  const [sheetFilter, setSheetFilter] = useState<'expository' | 'common' | 'all'>('expository');
  const [gradeFilter, setGradeFilter] = useState<string>('ALL');
  const [domainFilter, setDomainFilter] = useState<string>('ALL');
  const [keyword, setKeyword] = useState<string>('');

  const roster = data.teacher_class_roster;
  const filteredRoster = roster.filter((st) =>
    triageFilter === 'ALL' ? true : st.triage === triageFilter
  );

  const toggleSelectStudent = (id: string) => {
    setSelectedStudentIds((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]
    );
  };

  const handleBatchAssign = () => {
    if (selectedStudentIds.length === 0) return;
    assignTeacherClinic(selectedStudentIds);
    setBatchBannerMsg(
      `✅ 선택된 ${selectedStudentIds.length}명의 학생에게 결손 위계 맞춤형 1:1 처방 클리닉 및 오답 백신 세트가 일괄 배정되었습니다!`
    );
    setTimeout(() => setBatchBannerMsg(null), 4000);
  };

  const handleJumpToPersona = (personaIdx: number, mode: 'portal' | 'clinic' | 'studio') => {
    setActiveGradeIdx(personaIdx);
    setStudentMode(mode);
    setActiveRole('student');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleJumpFromGradeStr = (gradeStr: string, goalCode?: string) => {
    const gNum = parseInt(gradeStr.replace(/[^0-9]/g, ''), 10) || 5;
    if (goalCode && goalCode.includes('-EXP-')) {
      selectGradeAndSlot(gNum, goalCode, 'studio');
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }
    const idx = data.grades_data.findIndex((g) => g.grade_num === gNum);
    if (idx !== -1) {
      handleJumpToPersona(idx, 'portal');
    }
  };

  // Hierarchy filtering
  const rawHierarchyRows: HierarchyGoal[] =
    sheetFilter === 'expository'
      ? data.hierarchy.expository
      : sheetFilter === 'common'
      ? data.hierarchy.common
      : [...data.hierarchy.expository, ...data.hierarchy.common];

  const filteredHierarchy = rawHierarchyRows.filter((r) => {
    if (gradeFilter !== 'ALL' && r.grade !== gradeFilter) return false;
    if (domainFilter !== 'ALL' && !(r.domain || '').includes(domainFilter)) return false;
    if (keyword.trim()) {
      const kw = keyword.trim().toLowerCase();
      const hay = `${r.code} ${r.sub_skill_name} ${r.layer} ${r.dc_step1} ${r.dc_step2} ${r.dc_step3} ${r.mager_reading} ${r.mager_writing || ''}`.toLowerCase();
      if (!hay.includes(kw)) return false;
    }
    return true;
  });

  return (
    <div className="space-y-4">
      {/* =================================================================== */}
      {/* SUB-TAB 1: 학급 16하위기능 마스터리 히트맵 & 일괄 처방 콘솔 */}
      {/* =================================================================== */}
      {teacherTab === 'matrix' && (
        <div className="space-y-4">
          {/* Early Warning Triage Bar & Batch Action Header */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div>
                <span className="px-2.5 py-0.5 rounded-full text-xs font-extrabold bg-indigo-100 text-indigo-800">
                  교사 전용 학급 Learning Analytics 콘솔
                </span>
                <h2 className="text-base md:text-lg font-black text-slate-900 mt-1">
                  👩‍🏫 학급 전체 16대 하위기능(V1-1~W5) 마스터리 히트맵 & 조기 경보(Triage) 처방 시스템
                </h2>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <button
                  onClick={() => setShowLiveCockpit(!showLiveCockpit)}
                  className="px-3.5 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-amber-300 text-xs font-black shadow transition flex items-center gap-1.5 cursor-pointer border border-slate-700"
                >
                  <span>📡 라이브 교실 조종석 {showLiveCockpit ? '닫기 ▲' : '열기 ▼'}</span>
                </button>
                <button
                  onClick={handleBatchAssign}
                  className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-extrabold shadow transition cursor-pointer"
                >
                  💊 선택 학생 ({selectedStudentIds.length}명) 1-Click 맞춤 클리닉 일괄 배정
                </button>
              </div>
            </div>

            {/* Live Classroom Cockpit Render */}
            {showLiveCockpit && (
              <div className="pt-2 animate-in fade-in">
                <LiveClassroomCockpit
                  roster={roster}
                  onClose={() => setShowLiveCockpit(false)}
                />
              </div>
            )}

            {batchBannerMsg && (
              <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-400 text-emerald-950 text-xs font-black">
                {batchBannerMsg}
              </div>
            )}

            {/* Triage Filter Pills */}
            <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-slate-100">
              <div className="flex flex-wrap gap-1.5">
                {[
                  { id: 'ALL', label: `전체 학생 (${roster.length}명)` },
                  {
                    id: 'critical',
                    label: `🔴 긴급 처방 필요 (${roster.filter((s) => s.triage === 'critical').length}명)`,
                  },
                  {
                    id: 'fragile',
                    label: `🟠 주의·보강 필요 (${roster.filter((s) => s.triage === 'fragile').length}명)`,
                  },
                  {
                    id: 'guessing',
                    label: `⚡ 성급한 찍기 의심 (${roster.filter((s) => s.triage === 'guessing').length}명)`,
                  },
                  {
                    id: 'mastered',
                    label: `🟢 마스터 순항군 (${roster.filter((s) => s.triage === 'mastered').length}명)`,
                  },
                ].map((f) => (
                  <button
                    key={f.id}
                    onClick={() => setTriageFilter(f.id as typeof triageFilter)}
                    className={`px-3 py-1.5 rounded-xl text-xs font-extrabold border transition ${
                      triageFilter === f.id
                        ? 'bg-slate-900 text-white border-slate-900'
                        : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                    }`}
                  >
                    {f.label}
                  </button>
                ))}
              </div>

              <div className="flex items-center gap-3 text-xs font-bold text-slate-600">
                <span>🔴 50점 미만(결손)</span>
                <span>🟡 50~69점(불안정)</span>
                <span>🟢 70점 이상(마스터)</span>
              </div>
            </div>
          </div>

          {/* Class Mastery Heatmap Matrix Table */}
          <div className="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm overflow-x-auto">
            <table className="w-full border-collapse text-xs min-w-[1150px]">
              <thead>
                <tr className="bg-slate-100 text-slate-800 border-b border-slate-300">
                  <th className="p-2.5 text-center w-10">선택</th>
                  <th className="p-2.5 text-left w-48">학생명 (학년 · 상태)</th>
                  <th className="p-2.5 text-center w-28">KReaD / Smart</th>
                  <th className="p-2.5 text-left w-48">독해 습관 & 최다 오답 함정</th>
                  {data.subskill_16_meta.map((sk) => (
                    <th
                      key={sk.code}
                      title={`${sk.code}: ${sk.name} (${sk.desc})`}
                      className="p-1.5 text-center font-black w-11 border-l border-slate-200"
                    >
                      {sk.code}
                    </th>
                  ))}
                  <th className="p-2.5 text-center w-40 border-l border-slate-200">
                    맞춤 처방 / 화면 전환
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                {filteredRoster.map((st) => {
                  const isChecked = selectedStudentIds.includes(st.student_id);
                  const isAssigned =
                    teacherClinicAssigned[st.student_id] || st.clinic_completed;

                  return (
                    <tr
                      key={st.student_id}
                      className="hover:bg-blue-50/40 transition"
                    >
                      <td className="p-2 text-center">
                        <input
                          type="checkbox"
                          checked={isChecked}
                          onChange={() => toggleSelectStudent(st.student_id)}
                          className="w-4 h-4 accent-indigo-600 cursor-pointer"
                        />
                      </td>
                      <td className="p-2.5">
                        <div className="font-black text-slate-900">{st.name}</div>
                        <div className="flex items-center gap-1.5 mt-0.5">
                          <span
                            className={`px-1.5 py-0.5 rounded text-[10px] font-extrabold ${
                              st.triage === 'critical'
                                ? 'bg-rose-100 text-rose-800'
                                : st.triage === 'guessing'
                                ? 'bg-purple-100 text-purple-800'
                                : st.triage === 'fragile'
                                ? 'bg-amber-100 text-amber-800'
                                : 'bg-emerald-100 text-emerald-800'
                            }`}
                          >
                            {st.triage_label}
                          </span>
                        </div>
                      </td>
                      <td className="p-2 text-center">
                        <div className="font-extrabold text-slate-900">
                          KReaD {st.kread}{' '}
                          <span className="text-[10px] text-slate-500">/{st.kread_target}</span>
                        </div>
                        <div className="text-[11px] font-black text-blue-700">
                          SmartScore {st.smart_score}점
                        </div>
                      </td>
                      <td className="p-2">
                        <div className="font-bold text-slate-800 truncate max-w-[200px]" title={st.reading_habit}>
                          {st.reading_habit}
                        </div>
                        <div className="text-[11px] text-rose-700 font-semibold truncate max-w-[200px]" title={st.top_trap}>
                          함정: {st.top_trap}
                        </div>
                      </td>

                      {/* 16 Subskills Heatmap Cells */}
                      {st.scores_16.map((sc, idx) => {
                        const cellCls =
                          sc <= 50
                            ? 'bg-rose-100 text-rose-900 font-black border border-rose-300'
                            : sc < 70
                            ? 'bg-amber-50 text-amber-900 font-bold'
                            : 'bg-emerald-50/70 text-emerald-800 font-semibold';
                        return (
                          <td
                            key={idx}
                            onClick={() => setDrawerStudent(st)}
                            className={`p-1 text-center cursor-pointer border-l border-slate-100 ${cellCls}`}
                            title={`${data.subskill_16_meta[idx]?.code} (${data.subskill_16_meta[idx]?.name}): ${sc}점`}
                          >
                            {sc}
                          </td>
                        );
                      })}

                      <td className="p-2 text-center border-l border-slate-200 space-y-1">
                        <div className="flex items-center justify-center gap-1">
                          <button
                            onClick={() => setDrawerStudent(st)}
                            className={`px-2 py-1 rounded text-[11px] font-extrabold transition ${
                              isAssigned
                                ? 'bg-emerald-100 text-emerald-800 border border-emerald-300'
                                : 'bg-indigo-600 text-white hover:bg-indigo-700'
                            }`}
                          >
                            {isAssigned ? '✅ 처방 배정됨' : '💊 처방 상세'}
                          </button>
                          <button
                            onClick={() => handleJumpToPersona(st.persona_idx, 'portal')}
                            className="px-2 py-1 rounded text-[11px] font-extrabold bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300"
                          >
                            X-Ray ➔
                          </button>
                        </div>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>

          {/* Selected Student Prescription Detail Drawer Card */}
          {drawerStudent && (
            <div className="bg-slate-900 text-white rounded-2xl p-5 shadow-lg border border-indigo-500/50 flex flex-wrap items-center justify-between gap-4">
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <span className="px-2 py-0.5 rounded bg-amber-400 text-slate-950 font-black text-xs">
                    개인별 맞춤 처방 패키지 상세
                  </span>
                  <span className="font-black text-base">{drawerStudent.name}</span>
                  <span className="text-xs text-slate-300">({drawerStudent.triage_label})</span>
                </div>
                <div className="text-xs text-slate-300">
                  • <b>취약 하위기능 Top 3:</b> {drawerStudent.weak_skills.join(', ')} |{' '}
                  <b>집중 취약 함정:</b> {drawerStudent.top_trap}
                </div>
                <div className="text-xs text-sky-300 font-bold">
                  • <b>자동 매칭된 처방 클리닉:</b> {drawerStudent.assigned_clinic}
                </div>
              </div>

              <div className="flex flex-wrap items-center gap-2">
                <button
                  onClick={() => {
                    assignTeacherClinic([drawerStudent.student_id]);
                    setBatchBannerMsg(
                      `✅ ${drawerStudent.name} 학생에게 [${drawerStudent.assigned_clinic}] 패키지가 즉시 배정되었습니다!`
                    );
                  }}
                  className="px-3.5 py-2 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-black text-xs transition"
                >
                  ✅ 이 학생에게 처방 클리닉 즉시 발송
                </button>
                <button
                  onClick={() => handleJumpToPersona(drawerStudent.persona_idx, 'clinic')}
                  className="px-3.5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-extrabold text-xs transition"
                >
                  💊 이 학생의 클리닉 화면 열기 ➔
                </button>
                <button
                  onClick={() => setDrawerStudent(null)}
                  className="px-2.5 py-2 rounded-xl bg-slate-800 text-slate-300 text-xs font-bold"
                >
                  닫기 ✕
                </button>
              </div>
            </div>
          )}
        </div>
      )}

      {/* =================================================================== */}
      {/* SUB-TAB 2: 1~6학년 프로토타입 전 단원 한눈에 비교 갤러리 (View 2 보존) */}
      {/* =================================================================== */}
      {teacherTab === 'gallery' && (
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100">
            <span className="font-black text-base text-slate-900">
              📚 초등 1~6학년 학년별 대표 단원 프로토타입 한눈에 비교하기 (총 6개 학년 플래그십 세트)
            </span>
            <span className="px-2.5 py-0.5 rounded text-xs font-extrabold bg-blue-100 text-blue-800">
              각 단원 클릭 시 진단 · 처방 · 스플릿 리더 즉시 연동
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {data.grades_data.map((g, idx) => (
              <div
                key={g.id}
                className="border border-slate-200 rounded-2xl p-4 bg-slate-50/70 hover:border-blue-400 transition flex flex-col justify-between space-y-3"
              >
                <div>
                  <div className="flex flex-wrap items-center justify-between gap-2 mb-2">
                    <span className="px-2.5 py-0.5 rounded-md text-xs font-extrabold bg-blue-100 text-blue-800">
                      {g.grade} · {g.slot_id} ({g.layer})
                    </span>
                    <span className="text-xs font-bold text-slate-500">
                      {g.persona_label}
                    </span>
                  </div>

                  <h3 className="font-black text-base text-slate-900 mb-1.5">
                    「{g.real_csat_test.passage_title}」
                  </h3>

                  <div className="text-xs text-slate-600 space-y-1 mb-3">
                    <div>
                      • <b>교과 개념:</b> {g.curriculum_concept.subject} ({g.curriculum_concept.concept})
                    </div>
                    <div>
                      • <b>복잡도 규격:</b> {g.complexity_metrics.para_count} · {g.complexity_metrics.char_count} · KReaD {g.complexity_metrics.kread_target}
                    </div>
                    <div>
                      • <b>문항 구성:</b> {g.complexity_metrics.csat_scaling} (실전 문항 {g.real_csat_test.questions.length}개 + EBSR + TEI-4 구조도 + 작문 워크벤치 탑재)
                    </div>
                  </div>

                  <div
                    className="bg-white border border-slate-200 rounded-xl p-3 text-xs text-slate-700 leading-relaxed max-h-28 overflow-y-auto"
                    dangerouslySetInnerHTML={{ __html: g.real_csat_test.paragraphs[0] }}
                  />
                </div>

                <div className="flex flex-wrap gap-2 pt-2 border-t border-slate-200/80">
                  <button
                    onClick={() => handleJumpToPersona(idx, 'portal')}
                    className="flex-1 py-1.5 px-2.5 rounded-lg bg-white hover:bg-blue-50 text-blue-800 border border-blue-300 text-xs font-extrabold transition"
                  >
                    🔬 1단계 X-Ray 진단
                  </button>
                  <button
                    onClick={() => handleJumpToPersona(idx, 'clinic')}
                    className="flex-1 py-1.5 px-2.5 rounded-lg bg-white hover:bg-indigo-50 text-indigo-800 border border-indigo-300 text-xs font-extrabold transition"
                  >
                    💊 2단계 처방 클리닉
                  </button>
                  <button
                    onClick={() => handleJumpToPersona(idx, 'studio')}
                    className="flex-1 py-1.5 px-2.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-xs font-extrabold transition"
                  >
                    ✍️ 3단계 실전 스튜디오 ➔
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* =================================================================== */}
      {/* SUB-TAB 3: 지문 복잡도·어휘 등급 & 수능 문항 스케일링 설계 표준 (View 3 보존 + 5장르 아키텍처) */}
      {/* =================================================================== */}
      {teacherTab === 'standards' && (
        <div className="space-y-4">
          {/* 5-Genre 516-Goal Modular Architecture Card */}
          <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3 border-b border-slate-100">
              <span className="font-black text-base text-slate-900">
                🏛️ [전 장르 516개 마스터 위계 아키텍처] 설명문 플래그십 완결 + 5대 장르 확장 구조
              </span>
              <span className="px-2.5 py-0.5 rounded text-xs font-extrabold bg-emerald-100 text-emerald-800">
                총 516개 수행목표 데이터 규격 호환
              </span>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              {data.genre_summary.map((gs) => (
                <div
                  key={gs.id}
                  className={`p-3.5 rounded-xl border text-xs ${
                    gs.status === 'active'
                      ? 'bg-blue-50/70 border-blue-400'
                      : 'bg-slate-50 border-slate-200'
                  }`}
                >
                  <div className="flex items-center justify-between font-black text-sm text-slate-900 mb-1">
                    <span>{gs.name}</span>
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-extrabold ${
                        gs.status === 'active'
                          ? 'bg-blue-600 text-white'
                          : 'bg-slate-200 text-slate-700'
                      }`}
                    >
                      {gs.count}개 목표 · {gs.badge}
                    </span>
                  </div>
                  <p className="text-slate-600">{gs.desc}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Track 2 Quantitative & Qualitative Complexity Table */}
          <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm overflow-x-auto">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3 border-b border-slate-100">
              <span className="font-black text-base text-slate-900">
                📏 [Track 2 표준] 초등 1~6학년 설명문 지문 정량·정성 복잡도 규격표
              </span>
              <span className="px-2.5 py-0.5 rounded text-xs font-extrabold bg-blue-100 text-blue-800">
                KReaD · 김광해 어휘 등급 · 2022 개정 교육과정 반영
              </span>
            </div>

            <table className="w-full border-collapse text-xs">
              <thead>
                <tr className="bg-slate-100 text-slate-800 border-b border-slate-300">
                  <th className="p-2.5 text-left">학년 (학년군)</th>
                  <th className="p-2.5 text-left">KReaD 지수</th>
                  <th className="p-2.5 text-left">문단 수 / 문장 수</th>
                  <th className="p-2.5 text-left">글자 수 (공백 포함)</th>
                  <th className="p-2.5 text-left">어절 수 (문장당 평균)</th>
                  <th className="p-2.5 text-left">어휘 등급 배합 (Tier 1 : Tier 2 : Tier 3)</th>
                  <th className="p-2.5 text-left">시각 매체 자료 복잡도</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                <tr>
                  <td className="p-2.5 font-black">1학년 (초저)</td>
                  <td className="p-2.5">800 ~ 890</td>
                  <td className="p-2.5">1문단 (3~5문장)</td>
                  <td className="p-2.5">100 ~ 180자</td>
                  <td className="p-2.5">25~45어절 (5~7어절)</td>
                  <td className="p-2.5"><b>90% : 7% : 3%</b> (김광해 1등급 일상어 중심)</td>
                  <td className="p-2.5">직관적 삽화 · 부위별 명칭 선 잇기 그림</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">2학년 (초저)</td>
                  <td className="p-2.5">900 ~ 990</td>
                  <td className="p-2.5">2문단 (5~7문장)</td>
                  <td className="p-2.5">200 ~ 300자</td>
                  <td className="p-2.5">50~75어절 (7~8어절)</td>
                  <td className="p-2.5"><b>85% : 10% : 5%</b> (순서·이유 담화표지 도입)</td>
                  <td className="p-2.5">3~4단계 과정 화살표 그림 · 1차원 간단한 표</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">3학년 (초중)</td>
                  <td className="p-2.5">1000 ~ 1090</td>
                  <td className="p-2.5">3문단 (8~11문장)</td>
                  <td className="p-2.5">320 ~ 450자</td>
                  <td className="p-2.5">80~110어절 (8~10어절)</td>
                  <td className="p-2.5"><b>78% : 15% : 7%</b> (김광해 2등급 · 다의어·개념어)</td>
                  <td className="p-2.5">2차원 비교표(행×열) · 기초 구조도</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">4학년 (초중)</td>
                  <td className="p-2.5">1100 ~ 1190</td>
                  <td className="p-2.5">3~4문단 (11~15문장)</td>
                  <td className="p-2.5">450 ~ 600자</td>
                  <td className="p-2.5">110~150어절 (9~11어절)</td>
                  <td className="p-2.5"><b>72% : 18% : 10%</b> (비례·증감 사고 도구어)</td>
                  <td className="p-2.5">막대그래프 · 꺾은선그래프 (시계열 추세)</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">5학년 (초고)</td>
                  <td className="p-2.5">1200 ~ 1290</td>
                  <td className="p-2.5">4~5문단 (14~18문장)</td>
                  <td className="p-2.5">600 ~ 750자</td>
                  <td className="p-2.5">150~190어절 (10~12어절)</td>
                  <td className="p-2.5"><b>65% : 22% : 13%</b> (김광해 3등급 · 한자 개념어)</td>
                  <td className="p-2.5">원그래프·띠그래프(비율) · 다중 비교표</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">6학년 (초고)</td>
                  <td className="p-2.5">1300 ~ 1390</td>
                  <td className="p-2.5">5~6문단 (17~22문장)</td>
                  <td className="p-2.5">750 ~ 950자</td>
                  <td className="p-2.5">190~240어절 (11~13어절)</td>
                  <td className="p-2.5"><b>60% : 25% : 15%</b> (중등 브릿지 전문 개념어)</td>
                  <td className="p-2.5">복합 통계 그래프 · 연쇄 인과(되먹임) 모식도</td>
                </tr>
              </tbody>
            </table>
          </div>

          {/* Track 3 KICE CSAT Scaling & D1~D6 Distractor Engineering Table */}
          <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm overflow-x-auto">
            <div className="flex flex-wrap items-center justify-between gap-2 pb-3 mb-3 border-b border-slate-100">
              <span className="font-black text-base text-slate-900">
                🎯 [Track 3 표준] 한국교육과정평가원(KICE) 수능형 문항 학년군별 스케일링 & 매력적 오답 6대 공식
              </span>
              <span className="px-2.5 py-0.5 rounded text-xs font-extrabold bg-purple-100 text-purple-800">
                독서(비문학) V1~V3 + 화법과 작문 W1~W5
              </span>
            </div>

            <table className="w-full border-collapse text-xs mb-4">
              <thead>
                <tr className="bg-slate-100 text-slate-800 border-b border-slate-300">
                  <th className="p-2.5 text-left">스케일링 요소</th>
                  <th className="p-2.5 text-left">초저 (1~2학년군: 수능 입문기)</th>
                  <th className="p-2.5 text-left">초중 (3~4학년군: 수능 기본기)</th>
                  <th className="p-2.5 text-left">초고 (5~6학년군: 수능 실전기)</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                <tr>
                  <td className="p-2.5 font-black">선지 구성 수</td>
                  <td className="p-2.5"><b>3지선다</b> (정답 1 + 매력적 오답 2)</td>
                  <td className="p-2.5"><b>4지선다</b> (정답 1 + 매력적 오답 3)</td>
                  <td className="p-2.5"><b>5지선다</b> (평가원 수능 동일 규격)</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">발문(Stem) 스타일</td>
                  <td className="p-2.5">친화형 의문문 (“윗글의 내용과 <u>같은/다른</u> 것은 무엇인가요?”)</td>
                  <td className="p-2.5">수능 기본형 (“윗글을 읽고 알 수 있는 내용으로 가장 <u>알맞은</u> 것은?”)</td>
                  <td className="p-2.5">수능 실전형 (“윗글에 대한 이해로 적절하지 <u>않은</u> 것은?”, “&lt;보기&gt;를 바탕으로 추론한 것은?”)</td>
                </tr>
                <tr>
                  <td className="p-2.5 font-black">&lt;보기&gt; 박스 설계</td>
                  <td className="p-2.5">일상 경험·동물 관찰 짧은 상황 (2문장)</td>
                  <td className="p-2.5">교과서 탐구 실험 조건·단일 표/그래프</td>
                  <td className="p-2.5">복합 실험·편향된 매체 글·학생 작문 초고 (㉠~㉤ 퇴고)</td>
                </tr>
              </tbody>
            </table>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-2.5 text-xs">
              {data.distractor_6_meta.map((dm) => (
                <div key={dm.code} className="p-3 rounded-xl bg-slate-50 border border-slate-200">
                  <div className="font-black text-rose-800 mb-1">
                    [{dm.code}] {dm.name}
                  </div>
                  <div className="text-slate-600">{dm.formula}</div>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* =================================================================== */}
      {/* SUB-TAB 4: 설명문 96개 + 공통기초 36개 마스터 위계 탐색기 (View 4 보존 & 완벽 작동) */}
      {/* =================================================================== */}
      {teacherTab === 'hierarchy' && (
        <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
          <div className="flex flex-wrap items-center justify-between gap-2 pb-3 border-b border-slate-100">
            <div>
              <span className="font-black text-base text-slate-900">
                🗂️ `8_설명문_1_6학년` (96개) & `4_공통기초_1_6학년` (36개) 총 132개 마스터 위계 탐색기
              </span>
              <p className="text-xs text-slate-500 mt-0.5">
                모든 위계 코드의 교육과정 근거, Dick & Carey 3단계 인지 과정, 읽기(이해) 및 쓰기(표현) Mager 수행목표를 전수 조회할 수 있습니다.
              </p>
            </div>
            <span className="px-2.5 py-1 rounded-lg text-xs font-extrabold bg-emerald-100 text-emerald-800">
              검색된 위계 목표: 총 {filteredHierarchy.length}개
            </span>
          </div>

          {/* Filter Bar */}
          <div className="flex flex-wrap gap-2.5 bg-slate-50 p-3 rounded-xl border border-slate-200 text-xs">
            <select
              value={sheetFilter}
              onChange={(e) => setSheetFilter(e.target.value as 'expository' | 'common' | 'all')}
              className="px-3 py-2 rounded-lg border border-slate-300 bg-white font-bold text-slate-800"
            >
              <option value="expository">8_설명문_1_6학년 (96개 목표)</option>
              <option value="common">4_공통기초_1_6학년 (36개 목표)</option>
              <option value="all">설명문 + 공통기초 전체 (132개 목표)</option>
            </select>

            <select
              value={gradeFilter}
              onChange={(e) => setGradeFilter(e.target.value)}
              className="px-3 py-2 rounded-lg border border-slate-300 bg-white font-bold text-slate-800"
            >
              <option value="ALL">전체 학년 (1~6학년)</option>
              <option value="1학년">1학년</option>
              <option value="2학년">2학년</option>
              <option value="3학년">3학년</option>
              <option value="4학년">4학년</option>
              <option value="5학년">5학년</option>
              <option value="6학년">6학년</option>
            </select>

            <select
              value={domainFilter}
              onChange={(e) => setDomainFilter(e.target.value)}
              className="px-3 py-2 rounded-lg border border-slate-300 bg-white font-bold text-slate-800"
            >
              <option value="ALL">전체 영역 (공통·V1·V2·V3·W)</option>
              <option value="공통">0. 공통 기초 (A1~A6)</option>
              <option value="사실적">1. 사실적 이해 (V1)</option>
              <option value="추론적">2. 추론적 이해 (V2)</option>
              <option value="비판적">3. 비판적 이해 (V3)</option>
              <option value="표현">4. 표현하기/쓰기 (W)</option>
            </select>

            <input
              type="text"
              value={keyword}
              onChange={(e) => setKeyword(e.target.value)}
              placeholder="위계 코드(G5-EXP-V3-2), 하위기능명, Dick&Carey, Mager 목표 검색..."
              className="flex-1 min-w-[240px] px-3 py-2 rounded-lg border border-slate-300 bg-white font-medium text-slate-800 focus:outline-none focus:border-blue-600"
            />
          </div>

          {/* Hierarchy Table */}
          <div className="overflow-x-auto max-h-[680px] overflow-y-auto border border-slate-200 rounded-xl">
            <table className="w-full border-collapse text-xs">
              <thead className="sticky top-0 bg-slate-100 text-slate-800 border-b border-slate-300 z-10">
                <tr>
                  <th className="p-2.5 text-left w-28">위계 코드</th>
                  <th className="p-2.5 text-left w-24">학년 (체험)</th>
                  <th className="p-2.5 text-left w-36">영역 / 층위</th>
                  <th className="p-2.5 text-left w-44">세부 하위기능명</th>
                  <th className="p-2.5 text-left">Dick & Carey 3단계 (Step 1 ➔ Step 2 ➔ Step 3)</th>
                  <th className="p-2.5 text-left">이해(독해) & 표현(쓰기) Mager 수행목표</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-200">
                {filteredHierarchy.map((r) => (
                  <tr key={r.code} className="hover:bg-slate-50 transition align-top">
                    <td className="p-2.5 font-black text-blue-900">{r.code}</td>
                    <td className="p-2.5">
                      <div className="font-bold text-slate-900">{r.grade}</div>
                      <button
                        onClick={() => handleJumpFromGradeStr(r.grade)}
                        className="mt-1 px-2 py-1 rounded bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-300 font-extrabold text-[11px] transition"
                      >
                        진단·처방 체험 ➔
                      </button>
                    </td>
                    <td className="p-2.5">
                      <div className="font-bold text-slate-800">{r.domain}</div>
                      <div className="text-[11px] text-blue-700 font-semibold mt-0.5">{r.layer}</div>
                    </td>
                    <td className="p-2.5">
                      <div className="font-black text-slate-900">{r.sub_skill_name}</div>
                      {r.curriculum_basis && (
                        <div className="text-[11px] text-slate-500 mt-1 line-clamp-2" title={r.curriculum_basis}>
                          {r.curriculum_basis}
                        </div>
                      )}
                    </td>
                    <td className="p-2.5 space-y-1 text-slate-700 leading-relaxed">
                      <div>
                        • <b className="text-slate-900">Step 1:</b> {r.dc_step1}
                      </div>
                      <div>
                        • <b className="text-slate-900">Step 2:</b> {r.dc_step2}
                      </div>
                      <div>
                        • <b className="text-slate-900">Step 3:</b> {r.dc_step3}
                      </div>
                    </td>
                    <td className="p-2.5 space-y-1.5 text-slate-700 leading-relaxed">
                      <div>
                        <span className="px-1.5 py-0.5 rounded bg-blue-100 text-blue-900 font-extrabold text-[10px] mr-1">
                          이해(읽기)
                        </span>
                        {r.mager_reading}
                      </div>
                      {r.mager_writing && (
                        <div>
                          <span className="px-1.5 py-0.5 rounded bg-emerald-100 text-emerald-900 font-extrabold text-[10px] mr-1">
                            표현(쓰기)
                          </span>
                          {r.mager_writing}
                        </div>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
