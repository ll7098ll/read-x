import React, { useState } from 'react';
import type { TeacherRosterStudent, CommercialMasterData } from '../../types/courseware';

interface AcademySeatBillingCardProps {
  data: CommercialMasterData;
  onOpenReportModal?: () => void;
}

interface EnrolledStudentRow {
  id: string;
  name: string;
  grade: string;
  parentPhone: string;
  enrolledAt: string;
  progressPercent: number;
  kread: number;
  seatActive: boolean;
}

export const AcademySeatBillingCard: React.FC<AcademySeatBillingCardProps> = ({
  data,
  onOpenReportModal,
}) => {
  // Seat Billing Quota
  const totalSeats = 50;
  const initialRoster = (data.teacher_class_roster || []).map((st, idx) => ({
    id: st.student_id,
    name: st.name,
    grade: st.grade,
    parentPhone: `010-${(1234 + idx * 77).toString().padStart(4, '0')}-${(5678 + idx * 33).toString().padStart(4, '0')}`,
    enrolledAt: `2026.0${(idx % 9) + 1}.15`,
    progressPercent: Math.min(100, Math.floor(st.smart_score * 0.9 + (idx % 15))),
    kread: st.kread,
    seatActive: true,
  }));

  const [students, setStudents] = useState<EnrolledStudentRow[]>(initialRoster);
  const [filterGrade, setFilterGrade] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [showBulkModal, setShowBulkModal] = useState<boolean>(false);
  const [bulkInputText, setBulkInputText] = useState<string>('');
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  const activeSeatCount = students.filter((s) => s.seatActive).length;
  const availableSeats = totalSeats - activeSeatCount;
  const seatUsagePercent = Math.round((activeSeatCount / totalSeats) * 100);

  const handleToggleSeat = (id: string) => {
    setStudents((prev) =>
      prev.map((s) => (s.id === id ? { ...s, seatActive: !s.seatActive } : s))
    );
  };

  const handleApplyBulkImport = () => {
    const lines = bulkInputText
      .split('\n')
      .map((l) => l.trim())
      .filter((l) => l.length > 0);

    if (lines.length === 0) return;

    const newRows: EnrolledStudentRow[] = [];
    lines.forEach((line, idx) => {
      const parts = line.split(/[,;\t]/).map((p) => p.trim());
      if (parts.length >= 2) {
        newRows.push({
          id: `STU-NEW-${Date.now()}-${idx}`,
          name: parts[0] || `신규원생${idx + 1}`,
          grade: parts[1] || '초등 5학년',
          parentPhone: parts[2] || '010-0000-0000',
          enrolledAt: '2026.10.13',
          progressPercent: 0,
          kread: 850,
          seatActive: true,
        });
      }
    });

    if (newRows.length > availableSeats) {
      alert(
        `⚠️ 잔여 가용 좌석(${availableSeats}석)을 초과했습니다. 최대 ${availableSeats}명만 등록됩니다.`
      );
      newRows.splice(availableSeats);
    }

    setStudents((prev) => [...newRows, ...prev]);
    setShowBulkModal(false);
    setBulkInputText('');
    setToastMessage(`🎉 신규 원생 ${newRows.length}명이 성공적으로 등록 및 좌석 배정되었습니다!`);
    setTimeout(() => setToastMessage(null), 4000);
  };

  const filteredStudents = students.filter((s) => {
    if (filterGrade !== 'ALL' && !s.grade.includes(filterGrade)) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.trim().toLowerCase();
      if (!s.name.toLowerCase().includes(q) && !s.parentPhone.includes(q)) return false;
    }
    return true;
  });

  return (
    <div className="space-y-4">
      {/* Toast Notification */}
      {toastMessage && (
        <div className="p-3 bg-emerald-600 text-white font-extrabold text-xs rounded-xl shadow-md flex items-center justify-between animate-fade-in">
          <span>{toastMessage}</span>
          <button onClick={() => setToastMessage(null)} className="text-white hover:opacity-80">
            ✕
          </button>
        </div>
      )}

      {/* Row 1: Academy B2B Plan & Seat Quota Overview Card */}
      <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-2xl p-5 shadow-lg border border-indigo-900/60">
        <div className="flex flex-wrap items-center justify-between gap-4 pb-4 border-b border-indigo-800/50">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-xl bg-gradient-to-tr from-amber-400 to-amber-600 flex items-center justify-center font-black text-2xl shadow-md text-slate-950">
              🏢
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="text-lg font-black tracking-tight text-white">
                  ReadX-Ray Pro Academy Enterprise
                </h2>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-bold">
                  B2B ACTIVE
                </span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 font-mono">
                  SCREEN 20 · SEAT BILLING
                </span>
              </div>
              <p className="text-xs text-indigo-200 mt-0.5">
                계약 기관: 서울 대치 리드엑스레이 수능문해력 학원 본원 · 만료 예정일: 2026.12.31 (D-82)
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowBulkModal(true)}
              className="text-xs font-black px-3.5 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition flex items-center gap-1.5 cursor-pointer"
            >
              <span>📥 원생 엑셀/CSV 일괄 등록</span>
            </button>
            {onOpenReportModal && (
              <button
                onClick={onOpenReportModal}
                className="text-xs font-black px-3.5 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 shadow-md transition flex items-center gap-1.5 cursor-pointer"
              >
                <span>🖨️ 프리미엄 상담 성적표 발행</span>
              </button>
            )}
          </div>
        </div>

        {/* Seat Usage Metrics Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4">
          <div className="bg-white/5 border border-white/10 rounded-xl p-3">
            <div className="text-[11px] font-bold text-slate-400">총 라이선스 계약 좌석</div>
            <div className="text-2xl font-black text-white mt-1">
              {totalSeats} <span className="text-xs font-normal text-slate-400">Seats</span>
            </div>
          </div>
          <div className="bg-white/5 border border-white/10 rounded-xl p-3">
            <div className="text-[11px] font-bold text-slate-400">현재 활성 배정 원생</div>
            <div className="text-2xl font-black text-emerald-400 mt-1">
              {activeSeatCount} <span className="text-xs font-normal text-slate-400">명</span>
            </div>
          </div>
          <div className="bg-white/5 border border-white/10 rounded-xl p-3">
            <div className="text-[11px] font-bold text-slate-400">가용 잔여 좌석</div>
            <div className="text-2xl font-black text-amber-400 mt-1">
              {availableSeats} <span className="text-xs font-normal text-slate-400">Seats 남음</span>
            </div>
          </div>
          <div className="bg-white/5 border border-white/10 rounded-xl p-3">
            <div className="text-[11px] font-bold text-slate-400">좌석 가동률</div>
            <div className="text-2xl font-black text-indigo-300 mt-1">
              {seatUsagePercent}%
            </div>
            <div className="w-full h-1.5 bg-slate-700 rounded-full mt-1.5 overflow-hidden">
              <div
                className={`h-full rounded-full ${
                  seatUsagePercent > 90 ? 'bg-rose-500' : 'bg-indigo-400'
                }`}
                style={{ width: `${seatUsagePercent}%` }}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Row 2: Roster & Seat Management Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
        {/* Table Header Controls */}
        <div className="p-4 border-b border-slate-200 flex flex-wrap items-center justify-between gap-3 bg-slate-50">
          <div className="flex items-center gap-2 flex-wrap">
            <span className="text-xs font-black text-slate-700">원생 명부 및 좌석 제어 ({filteredStudents.length}명)</span>
            <div className="flex items-center gap-1 bg-white border border-slate-300 rounded-lg p-0.5 text-xs font-bold text-slate-600">
              {['ALL', '1학년', '2학년', '3학년', '4학년', '5학년', '6학년'].map((g) => (
                <button
                  key={g}
                  onClick={() => setFilterGrade(g)}
                  className={`px-2 py-1 rounded cursor-pointer ${
                    filterGrade === g ? 'bg-indigo-600 text-white font-black' : 'hover:bg-slate-100'
                  }`}
                >
                  {g === 'ALL' ? '전체 학년' : g}
                </button>
              ))}
            </div>
          </div>

          <div className="flex items-center gap-2">
            <input
              type="text"
              placeholder="원생 성명 또는 연락처 검색..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="text-xs px-3 py-1.5 rounded-lg border border-slate-300 bg-white font-medium text-slate-800 placeholder-slate-400 focus:ring-2 focus:ring-indigo-500 outline-none w-56"
            />
          </div>
        </div>

        {/* Table Data */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-100 text-slate-700 font-black border-b border-slate-200">
              <tr>
                <th className="py-2.5 px-3">원생 성명</th>
                <th className="py-2.5 px-3">학년</th>
                <th className="py-2.5 px-3">학부모 연락처</th>
                <th className="py-2.5 px-3">등록일자</th>
                <th className="py-2.5 px-3">KReaD 지수</th>
                <th className="py-2.5 px-3">16차시 코스 진도</th>
                <th className="py-2.5 px-3 text-center">B2B 좌석 상태</th>
                <th className="py-2.5 px-3 text-right">상담 관리</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 text-slate-800">
              {filteredStudents.map((st) => (
                <tr key={st.id} className="hover:bg-slate-50/80 transition">
                  <td className="py-2.5 px-3 font-black text-slate-900 flex items-center gap-1.5">
                    <span className="w-6 h-6 rounded-full bg-indigo-100 text-indigo-700 flex items-center justify-center text-[10px] font-black">
                      {st.name.charAt(0)}
                    </span>
                    <span>{st.name}</span>
                  </td>
                  <td className="py-2.5 px-3 font-semibold text-slate-600">{st.grade}</td>
                  <td className="py-2.5 px-3 font-mono text-slate-500">{st.parentPhone}</td>
                  <td className="py-2.5 px-3 font-mono text-slate-500">{st.enrolledAt}</td>
                  <td className="py-2.5 px-3">
                    <span className="font-black text-blue-700 bg-blue-50 px-2 py-0.5 rounded border border-blue-200">
                      {st.kread}
                    </span>
                  </td>
                  <td className="py-2.5 px-3">
                    <div className="flex items-center gap-2">
                      <div className="w-20 h-2 bg-slate-200 rounded-full overflow-hidden">
                        <div
                          className="h-full bg-emerald-500 rounded-full"
                          style={{ width: `${st.progressPercent}%` }}
                        />
                      </div>
                      <span className="font-mono font-bold text-slate-600 text-[11px]">
                        {st.progressPercent}%
                      </span>
                    </div>
                  </td>
                  <td className="py-2.5 px-3 text-center">
                    <button
                      onClick={() => handleToggleSeat(st.id)}
                      className={`px-2.5 py-1 rounded-md text-[11px] font-black transition cursor-pointer ${
                        st.seatActive
                          ? 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200 border border-emerald-300'
                          : 'bg-slate-200 text-slate-500 hover:bg-slate-300'
                      }`}
                    >
                      {st.seatActive ? '● 사용 중' : '○ 회수됨'}
                    </button>
                  </td>
                  <td className="py-2.5 px-3 text-right">
                    {onOpenReportModal && (
                      <button
                        onClick={onOpenReportModal}
                        className="text-[11px] font-bold px-2 py-1 rounded bg-blue-50 text-blue-700 hover:bg-blue-100 border border-blue-200 transition cursor-pointer"
                      >
                        성적표 발행 ↗
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Bulk Import Modal */}
      {showBulkModal && (
        <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white w-full max-w-xl rounded-2xl shadow-2xl border border-slate-300 p-5 space-y-4">
            <div className="flex items-center justify-between pb-3 border-b border-slate-200">
              <h3 className="font-black text-base text-slate-900 flex items-center gap-2">
                <span>📥 원생 명단 일괄 등록 (CSV / 엑셀 붙여넣기)</span>
              </h3>
              <button
                onClick={() => setShowBulkModal(false)}
                className="text-slate-400 hover:text-slate-700 text-sm font-bold"
              >
                ✕
              </button>
            </div>

            <div className="text-xs text-slate-600 space-y-1.5">
              <p className="font-bold">
                아래 텍스트 상자에 원생 정보를 쉼표(,) 또는 탭(Tab)으로 구분하여 입력해주세요.
              </p>
              <p className="text-[11px] text-slate-500 font-mono bg-slate-100 p-2 rounded">
                형식: 이름, 학년, 학부모연락처 (예: 박지훈, 초등 5학년, 010-8888-9999)
              </p>
            </div>

            <textarea
              rows={6}
              value={bulkInputText}
              onChange={(e) => setBulkInputText(e.target.value)}
              placeholder="김서연, 초등 4학년, 010-1111-2222&#10;이도현, 초등 5학년, 010-3333-4444&#10;최수아, 초등 6학년, 010-5555-6666"
              className="w-full p-3 rounded-xl border border-slate-300 text-xs font-mono focus:ring-2 focus:ring-indigo-500 outline-none"
            />

            <div className="flex items-center justify-between pt-2">
              <button
                onClick={() =>
                  setBulkInputText(
                    `윤민우, 초등 4학년, 010-2345-6789\n송예은, 초등 5학년, 010-3456-7890\n배준호, 초등 6학년, 010-4567-8901`
                  )
                }
                className="text-xs font-bold text-indigo-600 hover:underline cursor-pointer"
              >
                + 샘플 3명 채우기
              </button>

              <div className="flex items-center gap-2">
                <button
                  onClick={() => setShowBulkModal(false)}
                  className="px-3 py-1.5 rounded-lg text-xs font-bold text-slate-600 hover:bg-slate-100"
                >
                  취소
                </button>
                <button
                  onClick={handleApplyBulkImport}
                  className="px-4 py-1.5 rounded-lg text-xs font-black bg-indigo-600 hover:bg-indigo-500 text-white shadow"
                >
                  일괄 좌석 배정 실행
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
