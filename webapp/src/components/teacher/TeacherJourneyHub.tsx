import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { CommercialMasterData, TeacherRosterStudent } from '../../types/courseware';
import { LiveClassroomCockpit } from './LiveClassroomCockpit';
import { BrandedCounselingReportModal } from '../admin/BrandedCounselingReportModal';

interface TeacherJourneyHubProps {
  data: CommercialMasterData;
}

export const TeacherJourneyHub: React.FC<TeacherJourneyHubProps> = ({ data }) => {
  const { assignTaskToStudent, assignTeacherClinic } = useCoursewareStore();
  const roster: TeacherRosterStudent[] = data.teacher_class_roster || [];

  const [activeTab, setActiveTab] = useState<'diagnosis' | 'results' | 'prescription' | 'trends' | 'full_report'>('diagnosis');
  const [selectedStudentId, setSelectedStudentId] = useState<string>(roster[0]?.student_id || 'STU-001');
  const [prescribeSlot, setPrescribeSlot] = useState<string>('G5-EXP-I1-1');
  const [prescribeNote, setPrescribeNote] = useState<string>('D4 논리적 비약 방어 및 EBSR 2단계 근거 매핑 집중 훈련');
  const [assignedBanner, setAssignedBanner] = useState<string | null>(null);
  const [showCounselingModal, setShowCounselingModal] = useState(false);

  const currentStudent = roster.find((s) => s.student_id === selectedStudentId) || roster[0];

  const handleSendPrescription = () => {
    assignTaskToStudent({
      title: `${prescribeSlot} 맞춤 처방 과제 (${currentStudent.name} 학생)`,
      slotId: prescribeSlot,
      type: prescribeSlot.includes('COM') ? 'clinic' : 'reading',
      assignedBy: '김성진 담임선생님',
      dueDate: '오늘 21:00까지',
      trapWarning: prescribeNote,
    });

    assignTeacherClinic([currentStudent.student_id]);

    setAssignedBanner(
      `🎉 [${currentStudent.name}] 학생에게 [${prescribeSlot}] 맞춤 과제가 성공적으로 배정되었습니다!`
    );
    setTimeout(() => setAssignedBanner(null), 4000);
  };

  return (
    <div className="space-y-5 font-sans">
      {/* 1. Clean Navigation Segmented Tab Bar */}
      <div className="bg-white rounded-2xl border border-slate-200/80 p-2 shadow-2xs flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-1.5 bg-slate-100/80 p-1 rounded-xl overflow-x-auto">
          <button
            onClick={() => setActiveTab('diagnosis')}
            className={`px-3.5 py-2 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
              activeTab === 'diagnosis'
                ? 'bg-white text-indigo-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            🔍 1. 진단 모니터링
          </button>

          <button
            onClick={() => setActiveTab('results')}
            className={`px-3.5 py-2 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
              activeTab === 'results'
                ? 'bg-white text-indigo-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📊 2. 결과 리포트 조회
          </button>

          <button
            onClick={() => setActiveTab('prescription')}
            className={`px-3.5 py-2 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
              activeTab === 'prescription'
                ? 'bg-white text-rose-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            💊 3. 맞춤 처방 & 과제 배정
          </button>

          <button
            onClick={() => setActiveTab('trends')}
            className={`px-3.5 py-2 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
              activeTab === 'trends'
                ? 'bg-white text-indigo-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📈 4. 성장 추이 통계
          </button>

          <button
            onClick={() => setActiveTab('full_report')}
            className={`px-3.5 py-2 rounded-lg text-xs font-bold transition cursor-pointer whitespace-nowrap ${
              activeTab === 'full_report'
                ? 'bg-white text-amber-800 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            🖨️ 5. 종합 리포트 발행
          </button>
        </div>

        <div className="text-xs font-bold text-slate-500">
          서울 대치초 5학년 2반 · 재적 {roster.length}명
        </div>
      </div>

      {assignedBanner && (
        <div className="p-3.5 bg-emerald-600 text-white font-bold text-xs rounded-xl shadow-xs flex items-center justify-between animate-fade-in">
          <span>{assignedBanner}</span>
          <button onClick={() => setAssignedBanner(null)} className="text-white hover:opacity-80">
            ✕
          </button>
        </div>
      )}

      {/* ================= STEP 1: 🔍 진단 모니터링 ================= */}
      {activeTab === 'diagnosis' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div>
                <span className="text-[11px] font-bold text-indigo-600 tracking-wider uppercase block">
                  STEP 1 · LIVE RADAR COCKPIT
                </span>
                <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight mt-0.5">
                  학급 원생 25명 진단 현황 및 실시간 관제 조종석
                </h2>
                <p className="text-xs text-slate-500 mt-1">
                  원생들의 진단 완료율과 실시간 독서 진행 문단, 오답 병목 구간을 관제합니다.
                </p>
              </div>

              <div className="flex items-center gap-2">
                <div className="bg-slate-50 border border-slate-200/80 px-3.5 py-2 rounded-2xl text-xs">
                  진단 완료: <b className="text-emerald-700">22 / 25명 (88%)</b>
                </div>
                <div className="bg-slate-50 border border-slate-200/80 px-3.5 py-2 rounded-2xl text-xs">
                  실시간 접속: <b className="text-blue-600">18명 독서 중</b>
                </div>
              </div>
            </div>
          </div>

          <LiveClassroomCockpit roster={roster} />
        </div>
      )}

      {/* ================= STEP 2: 📊 결과 리포트 조회 ================= */}
      {activeTab === 'results' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-5 shadow-xs flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <span className="text-xs font-bold text-slate-700">분석 원생:</span>
              <select
                value={selectedStudentId}
                onChange={(e) => setSelectedStudentId(e.target.value)}
                className="bg-slate-50 border border-slate-200 rounded-xl px-3 py-1.5 text-xs font-bold text-slate-800 outline-none"
              >
                {roster.map((st) => (
                  <option key={st.student_id} value={st.student_id}>
                    {st.name} ({st.grade} · KReaD {st.kread} · {st.triage_label})
                  </option>
                ))}
              </select>
            </div>

            <button
              onClick={() => setActiveTab('prescription')}
              className="text-xs font-bold px-4 py-2 rounded-xl bg-rose-600 hover:bg-rose-500 text-white shadow-xs transition cursor-pointer"
            >
              이 학생에게 맞춤 처방 배정하기 ➔
            </button>
          </div>

          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div className="flex flex-wrap items-start justify-between gap-4 pb-4 border-b border-slate-100">
              <div className="flex items-center gap-3.5">
                <div className="w-11 h-11 rounded-2xl bg-indigo-50 text-indigo-700 flex items-center justify-center font-black text-lg border border-indigo-200">
                  {currentStudent.name.charAt(0)}
                </div>
                <div>
                  <h3 className="text-lg font-black text-slate-900 tracking-tight">
                    {currentStudent.name} 학생 6차원 X-Ray 결과 리포트
                  </h3>
                  <p className="text-xs text-slate-500">
                    KReaD 독서지수: <b className="text-indigo-600">{currentStudent.kread}</b> (목표 {currentStudent.kread_target}) · 성취 점수: <b className="text-emerald-600">{currentStudent.smart_score}점</b>
                  </p>
                </div>
              </div>

              <span
                className={`text-xs font-bold px-3 py-1 rounded-xl ${
                  currentStudent.triage === 'critical'
                    ? 'bg-rose-50 text-rose-800 border border-rose-200'
                    : currentStudent.triage === 'fragile'
                    ? 'bg-amber-50 text-amber-800 border border-amber-200'
                    : 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                }`}
              >
                트리아지: {currentStudent.triage_label}
              </span>
            </div>

            {/* 6D Scores */}
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
              {[
                { name: '어휘 (V)', score: Math.min(100, currentStudent.smart_score + 5), status: '우수' },
                { name: '사실 (F)', score: Math.min(100, currentStudent.smart_score + 10), status: '최우수' },
                { name: '추론 (I)', score: Math.max(40, currentStudent.smart_score - 18), status: '취약' },
                { name: '구조 (S)', score: Math.max(50, currentStudent.smart_score - 5), status: '양호' },
                { name: '비판 (E)', score: Math.max(45, currentStudent.smart_score - 8), status: '양호' },
                { name: '메타 (M)', score: Math.max(40, currentStudent.smart_score - 12), status: '보통' },
              ].map((dom, idx) => (
                <div key={idx} className="p-3.5 rounded-2xl bg-slate-50/70 border border-slate-200/80 text-center">
                  <span className="text-[11px] font-bold text-slate-500 block">{dom.name}</span>
                  <span className="text-xl font-black text-slate-900 mt-0.5 block">{dom.score}점</span>
                  <span
                    className={`text-[10px] font-bold px-1.5 py-0.5 rounded mt-1 inline-block ${
                      dom.status === '취약'
                        ? 'bg-rose-100 text-rose-700'
                        : 'bg-slate-200 text-slate-700'
                    }`}
                  >
                    {dom.status}
                  </span>
                </div>
              ))}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div className="p-4 rounded-2xl bg-rose-50/60 border border-rose-200 space-y-1">
                <span className="font-bold text-rose-900 block">⚠️ 최다 유발 오답 함정</span>
                <p className="text-rose-800 leading-relaxed">
                  <b>{currentStudent.top_trap}</b>: 본문에 명시되지 않은 전제를 자의적으로 확장하여 오답 선지를 정답으로 오판하는 비율이 높습니다.
                </p>
              </div>

              <div className="p-4 rounded-2xl bg-blue-50/60 border border-blue-200 space-y-1">
                <span className="font-bold text-blue-900 block">📖 독서 행동 프로파일</span>
                <p className="text-blue-800 leading-relaxed">
                  <b>{currentStudent.reading_habit}</b>: 지문 완독 속도는 빠르나, 다단계 추론 문항에서 본문 재확인 빈도가 낮습니다.
                </p>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ================= STEP 3: 💊 맞춤 처방 및 과제 배정 ================= */}
      {activeTab === 'prescription' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div className="border-b border-slate-100 pb-3">
              <h2 className="text-lg font-black text-slate-900 tracking-tight">
                1:1 맞춤형 약점 처방 및 과제 배정 콘솔
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                진단 결과 결손이 발견된 학생에게 보충 클리닉 또는 정규 차시를 배정합니다. 학생의 '오늘의 과제함'으로 즉시 전송됩니다.
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1.5">
                  1. 처방 대상 원생
                </label>
                <select
                  value={selectedStudentId}
                  onChange={(e) => setSelectedStudentId(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 outline-none"
                >
                  {roster.map((st) => (
                    <option key={st.student_id} value={st.student_id}>
                      {st.name} ({st.grade} · {st.triage_label})
                    </option>
                  ))}
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1.5">
                  2. 추천 처방 슬롯
                </label>
                <select
                  value={prescribeSlot}
                  onChange={(e) => setPrescribeSlot(e.target.value)}
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-bold text-slate-800 outline-none"
                >
                  <option value="G5-EXP-I1-1">G5-EXP-I1-1 인과 추론 핵심 지문 (수능형)</option>
                  <option value="G5-COM-A3">G5-COM-A3 어휘 의미망 사고구술 빈칸 (선수 결손)</option>
                  <option value="G5-EXP-S1-2">G5-EXP-S1-2 Meyer 6대 구조도 노드 조립</option>
                  <option value="G5-EXP-E1-1">G5-EXP-E1-1 비판적 반론 재구성 (심화)</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1.5">
                  3. 지도 코멘트 및 함정 주의
                </label>
                <input
                  type="text"
                  value={prescribeNote}
                  onChange={(e) => setPrescribeNote(e.target.value)}
                  placeholder="예: D4 논리적 비약 주의..."
                  className="w-full bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-medium text-slate-800 outline-none"
                />
              </div>
            </div>

            <div className="pt-3 flex items-center justify-between border-t border-slate-100">
              <span className="text-[11px] text-slate-500">
                💡 배정 시 학생 계정과 학부모 리포트에 '신규 과제 배정'이 실시간 동기화됩니다.
              </span>
              <button
                onClick={handleSendPrescription}
                className="px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-xs transition flex items-center gap-1.5 cursor-pointer"
              >
                <span>🚀 학생에게 과제 처방 전송하기</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ================= STEP 4: 📈 성장 추이 및 통계 ================= */}
      {activeTab === 'trends' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-5">
            <div>
              <h2 className="text-lg font-black text-slate-900 tracking-tight">
                12주차 종단 KReaD 성장 곡선 및 오답 함정 감소율 추이
              </h2>
              <p className="text-xs text-slate-500 mt-0.5">
                학급 25명의 평균 독서지수 변화 및 평가원 6대 오답 함정 극복 추이입니다.
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-4 gap-3">
              <div className="p-4 rounded-2xl bg-slate-50/70 border border-slate-200/80 text-center">
                <span className="text-xs font-bold text-slate-500">초기 진단</span>
                <span className="text-xl font-black text-slate-800 block mt-1">820 KReaD</span>
                <span className="text-[10px] text-slate-400">1주차 기준</span>
              </div>
              <div className="p-4 rounded-2xl bg-blue-50/70 border border-blue-200/80 text-center">
                <span className="text-xs font-bold text-blue-700">중간 점검</span>
                <span className="text-xl font-black text-blue-900 block mt-1">910 KReaD</span>
                <span className="text-[10px] text-blue-600 font-bold">+90점 상승</span>
              </div>
              <div className="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-200/80 text-center">
                <span className="text-xs font-bold text-indigo-700">현재 달성</span>
                <span className="text-xl font-black text-indigo-900 block mt-1">980 KReaD</span>
                <span className="text-[10px] text-indigo-600 font-bold">+160점 상승</span>
              </div>
              <div className="p-4 rounded-2xl bg-emerald-50/70 border border-emerald-200/80 text-center">
                <span className="text-xs font-bold text-emerald-700">12주 목표</span>
                <span className="text-xl font-black text-emerald-900 block mt-1">1050 KReaD</span>
                <span className="text-[10px] text-emerald-600 font-bold">목표 달성률 85%</span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ================= STEP 5: 🖨️ 종합 리포트 발행 ================= */}
      {activeTab === 'full_report' && (
        <div className="space-y-4">
          <div className="bg-white rounded-3xl border border-slate-200/80 p-8 shadow-xs text-center space-y-4">
            <div className="text-4xl">🖨️</div>
            <div>
              <h2 className="text-xl font-black text-slate-900">
                학부모 상담용 공식 직인 성적표 발행
              </h2>
              <p className="text-xs text-slate-500 max-w-md mx-auto mt-1">
                원생의 6차원 X-Ray 진단, KReaD 독서지수 변화, 오답 백신 보유 현황이 학원장 공식 직인과 함께 A4 규격으로 출력됩니다.
              </p>
            </div>

            <button
              onClick={() => setShowCounselingModal(true)}
              className="px-6 py-3 rounded-2xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs shadow-xs transition cursor-pointer"
            >
              📄 직인 날인 심층 상담 성적표 인쇄 모달 열기
            </button>
          </div>
        </div>
      )}

      {/* Counseling Report Modal */}
      {showCounselingModal && (
        <BrandedCounselingReportModal
          data={data}
          onClose={() => setShowCounselingModal(false)}
        />
      )}
    </div>
  );
};
