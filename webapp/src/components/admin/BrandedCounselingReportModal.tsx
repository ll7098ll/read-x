import { DemoNotice } from '../common/DemoNotice';
import { ReadXSymbol } from '../brand/ReadXBrand';
import React, { useState } from 'react';
import type { TeacherRosterStudent, CommercialMasterData } from '../../types/courseware';

interface BrandedCounselingReportModalProps {
  data: CommercialMasterData;
  onClose: () => void;
}

export const BrandedCounselingReportModal: React.FC<BrandedCounselingReportModalProps> = ({
  data,
  onClose,
}) => {
  const roster = data.teacher_class_roster || [];
  const [selectedStudentId, setSelectedStudentId] = useState<string>(
    roster[0]?.student_id || 'STU-001'
  );

  // Academy Branding Customization State
  const [academyName, setAcademyName] = useState('서울 대치 리드엑스 수능문해력 학원');
  const [directorName, setDirectorName] = useState('체험 원장');
  const [phoneContact, setPhoneContact] = useState('연락처 입력');
  const [consultantName, setConsultantName] = useState('수석 연구원 이은우');
  const [includeSeal, setIncludeSeal] = useState(true);
  const [reportSerial] = useState(`RX-A4-${Math.floor(100000 + Math.random() * 900000)}`);
  const [examDate, setExamDate] = useState('2026년 10월 13일');

  // Selected Student
  const currentStudent =
    roster.find((st) => st.student_id === selectedStudentId) || roster[0];

  // Presets for Director Opinion
  const opinionPresets = [
    {
      title: '① 어휘·개념 결손 집중형',
      text: `본 학생(${currentStudent?.name || '학생'})은 문맥 파악 및 지문 전체 흐름에 대한 직관은 우수하나, 학년 권장 교과 전문 어휘 및 미세한 어휘 의미 분별력에서 일시적 결손이 관찰됩니다. 특히 전제 왜곡(D3) 함정에 대한 방어율이 낮으므로, 12주간 매칭된 공통기초(A1~A6) 어휘 클리닉을 선행 이수할 것을 강력히 권장합니다.`,
    },
    {
      title: '② 추론 비약·함정 방어형',
      text: `본 학생(${currentStudent?.name || '학생'})은 사실적 정보 추출 속도는 상위 10% 이내이나, 다단계 논리적 비약(D4) 및 인과 관계의 자의적 해석 경향이 관찰됩니다. 수능 국어 고난도 킬러 문항 대비를 위해 지문 내 '단서 핫텍스트'를 정확히 스포트라이트하고 EBSR 2단계 근거 매핑 훈련을 6주간 집중 이수하도록 처방합니다.`,
    },
    {
      title: '③ 상위 1% 수능 비문학 도약형',
      text: `본 학생(${currentStudent?.name || '학생'})은 KReaD 독서 지수 ${currentStudent?.kread || 980}으로 동학년 최상위권의 안정적인 독해력 궤도에 진입해 있습니다. 구조도 요약(Meyer 구조) 및 비판적 반론 재구성(W4)을 중심으로 한 심화 융합 지문(과학·철학) 훈련을 통해 초등 단계에서 수능 비문학 실전 감각을 완성할 수 있습니다.`,
    },
  ];

  const [opinionText, setOpinionText] = useState(opinionPresets[1].text);
  const [isCopied, setIsCopied] = useState(false);

  const handlePrint = () => {
    window.print();
  };

  const handleCopyLink = () => {
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 3000);
  };

  // Domain radar scores approximation
  const domains = [
    { name: '어휘 정밀도 (V)', score: Math.min(100, (currentStudent?.smart_score || 75) + 4), grade: '1등급' },
    { name: '사실적 이해 (F)', score: Math.min(100, (currentStudent?.smart_score || 75) + 12), grade: '1등급' },
    { name: '추론적 독해 (I)', score: Math.max(40, (currentStudent?.smart_score || 75) - 15), grade: '3등급' },
    { name: '구조 분석 (S)', score: Math.max(50, (currentStudent?.smart_score || 75) - 6), grade: '2등급' },
    { name: '비판·평가 (E)', score: Math.max(45, (currentStudent?.smart_score || 75) - 8), grade: '2등급' },
    { name: '메타인지 (M)', score: Math.max(40, (currentStudent?.smart_score || 75) - 18), grade: '3등급' },
  ];

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-2 sm:p-4 overflow-y-auto">
      <div className="bg-white w-full max-w-5xl rounded-2xl shadow-2xl border border-slate-300 overflow-hidden my-auto flex flex-col max-h-[96vh]">
        {/* Modal Top Control Bar (Screen 22 - Non-printing toolbar) */}
        <div className="bg-slate-900 text-white px-5 py-3.5 flex flex-wrap items-center justify-between gap-3 border-b border-slate-800 no-print">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-lg bg-gradient-to-tr from-amber-500 to-indigo-600 flex items-center justify-center font-black text-sm">
              🏢
            </div>
            <div>
              <h2 className="font-black text-sm sm:text-base flex items-center gap-2">
                <span>학원 상담 리포트 미리보기</span>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 font-mono">
                  SCREEN 22 · B2B COUNSELING REPORT
                </span>
              </h2>
              <p className="text-[11px] text-slate-400">
                학원 로고·원장 직인·AI 맞춤 소견서가 포함된 A4 체험용 상담 예시를 즉시 인쇄하거나 PDF로 저장합니다.
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={handleCopyLink}
              className="text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center gap-1.5 cursor-pointer"
            >
              <span>{isCopied ? '공유 기능은 아직 준비 중입니다' : '학부모 공유 준비 중'}</span>
            </button>
            <button
              onClick={handlePrint}
              className="text-xs font-black px-4 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white shadow-md transition flex items-center gap-1.5 cursor-pointer"
            >
              <span>🖨️ A4 성적표 인쇄 / PDF</span>
            </button>
            <button
              onClick={onClose}
              className="text-xs font-bold px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition cursor-pointer"
            >
              ✕ 닫기
            </button>
          </div>
        </div>

        {/* Builder Settings (Non-printing Configuration Area) */}
        <div className="bg-slate-50 border-b border-slate-200 p-4 text-xs no-print">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            <div>
              <label className="block font-black text-slate-700 mb-1">👤 상담 대상 학생 선택</label>
              <select
                value={selectedStudentId}
                onChange={(e) => setSelectedStudentId(e.target.value)}
                className="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 font-bold text-slate-800 focus:ring-2 focus:ring-blue-500 outline-none"
              >
                {roster.map((st) => (
                  <option key={st.student_id} value={st.student_id}>
                    {st.name} ({st.grade} · KReaD {st.kread} · {st.triage_label})
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block font-black text-slate-700 mb-1">🏢 학원명 브랜딩</label>
              <input
                type="text"
                value={academyName}
                onChange={(e) => setAcademyName(e.target.value)}
                className="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 font-bold text-slate-800 focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div>
              <label className="block font-black text-slate-700 mb-1">✒️ 원장 / 대표 명의</label>
              <input
                type="text"
                value={directorName}
                onChange={(e) => setDirectorName(e.target.value)}
                className="w-full bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 font-bold text-slate-800 focus:ring-2 focus:ring-blue-500 outline-none"
              />
            </div>

            <div className="flex items-center justify-between gap-2 pt-4">
              <label className="flex items-center gap-2 cursor-pointer font-extrabold text-slate-700">
                <input
                  type="checkbox"
                  checked={includeSeal}
                  onChange={(e) => setIncludeSeal(e.target.checked)}
                  className="rounded text-blue-600 focus:ring-blue-500"
                />
                <span>디지털 원장 직인 날인</span>
              </label>
              <span className="text-[11px] text-slate-500">일련번호: {reportSerial}</span>
            </div>
          </div>

          <div className="mt-3 pt-3 border-t border-slate-200 flex flex-wrap items-center gap-2">
            <span className="font-black text-slate-600">💡 원장 상담 소견 프리셋 추천:</span>
            {opinionPresets.map((preset, idx) => (
              <button
                key={idx}
                onClick={() => setOpinionText(preset.text)}
                className="text-[11px] font-bold px-2.5 py-1 rounded-md bg-white hover:bg-blue-50 text-slate-700 border border-slate-300 hover:border-blue-400 transition cursor-pointer"
              >
                {preset.title}
              </button>
            ))}
          </div>
        </div>

        <DemoNotice />
        {/* Printable Official Report Document (A4 Styling) */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-8 bg-slate-200 print:bg-white print:p-0 print:overflow-visible">
          <div className="max-w-[800px] mx-auto bg-white p-8 sm:p-10 rounded-xl shadow-lg border border-slate-300 print:border-none print:shadow-none print:rounded-none print:p-6 print:max-w-none text-slate-900 font-sans">
            {/* Header: Academy Brand Watermark & Report Serial */}
            <div className="flex items-start justify-between border-b-2 border-slate-900 pb-5 mb-6">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <ReadXSymbol className="w-8 h-8" />
                  <span className="text-xs font-extrabold tracking-wider text-slate-500 uppercase">
                    READ X · LEARNING REPORT DEMO
                  </span>
                </div>
                <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
                  [체험 예시 · 실제 진단 아님]
                  {academyName}
                </h1>
                <p className="text-xs text-slate-600 mt-1 font-semibold">
                  2022 개정 국어과 교육과정 · 수능 비문학 6대 오답공학 기반 1:1 맞춤형 정밀 진단 결과서
                </p>
              </div>

              <div className="text-right text-xs">
                <div className="font-mono text-slate-500 font-bold">문서번호: {reportSerial}</div>
                <div className="font-bold text-slate-700 mt-0.5">검사일자: {examDate}</div>
                <div className="font-bold text-blue-700 mt-0.5">상담담당: {consultantName}</div>
              </div>
            </div>

            {/* Student Profile & Key Metrics Banner */}
            <div className="bg-slate-50 rounded-xl border border-slate-200 p-4 mb-6">
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
                <div className="p-2 border-r border-slate-200 last:border-none">
                  <div className="text-[11px] font-bold text-slate-500">학생 성명 / 학년</div>
                  <div className="text-base font-black text-slate-900 mt-0.5">
                    {currentStudent?.name || '홍길동'} 학생 ({currentStudent?.grade || '초등 5학년'})
                  </div>
                </div>
                <div className="p-2 border-r border-slate-200 last:border-none">
                  <div className="text-[11px] font-bold text-slate-500">KReaD 한국어 독서지수</div>
                  <div className="text-base font-black text-blue-700 mt-0.5 flex items-center justify-center gap-1">
                    <span>{currentStudent?.kread || 940}</span>
                    <span className="text-[10px] text-slate-500 font-normal">
                      (목표 {currentStudent?.kread_target || 1050})
                    </span>
                  </div>
                </div>
                <div className="p-2 border-r border-slate-200 last:border-none">
                  <div className="text-[11px] font-bold text-slate-500">종합 스마트 지수</div>
                  <div className="text-base font-black text-emerald-700 mt-0.5">
                    {currentStudent?.smart_score || 82}점 <span className="text-xs font-normal text-slate-500">(상위 12%)</span>
                  </div>
                </div>
                <div className="p-2">
                  <div className="text-[11px] font-bold text-slate-500">문해력 트리아지 등급</div>
                  <div className="text-sm font-black text-amber-700 mt-0.5">
                    {currentStudent?.triage_label || '위태형 (주의)'}
                  </div>
                </div>
              </div>
            </div>

            {/* Section 1: 6D Cognitive Domain Radar Breakdown */}
            <div className="mb-6">
              <h3 className="text-sm font-black text-slate-900 mb-3 flex items-center gap-2 border-l-4 border-blue-600 pl-2">
                <span>1. 6차원 인지 X-Ray 영역별 성취도 정밀 분석</span>
                <span className="text-xs font-normal text-slate-500">
                  (한국어 수능 비문학 6대 핵심 역량 평가)
                </span>
              </h3>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {domains.map((dom, idx) => (
                  <div
                    key={idx}
                    className="p-3 rounded-lg border border-slate-200 bg-white flex items-center justify-between"
                  >
                    <div className="flex-1 pr-3">
                      <div className="flex items-center justify-between text-xs font-bold text-slate-800 mb-1">
                        <span>{dom.name}</span>
                        <span className="font-mono text-blue-700">{dom.score}점</span>
                      </div>
                      <div className="w-full h-2 bg-slate-100 rounded-full overflow-hidden">
                        <div
                          className={`h-full rounded-full ${
                            dom.score >= 80
                              ? 'bg-emerald-500'
                              : dom.score >= 65
                              ? 'bg-blue-500'
                              : 'bg-amber-500'
                          }`}
                          style={{ width: `${dom.score}%` }}
                        />
                      </div>
                    </div>
                    <span
                      className={`text-[11px] font-extrabold px-2 py-0.5 rounded ${
                        dom.grade === '1등급'
                          ? 'bg-blue-100 text-blue-800'
                          : dom.grade === '2등급'
                          ? 'bg-emerald-100 text-emerald-800'
                          : 'bg-amber-100 text-amber-800'
                      }`}
                    >
                      {dom.grade}
                    </span>
                  </div>
                ))}
              </div>
            </div>

            {/* Section 2: Trap Analysis & Vulnerability */}
            <div className="mb-6">
              <h3 className="text-sm font-black text-slate-900 mb-3 flex items-center gap-2 border-l-4 border-amber-600 pl-2">
                <span>2. KICE 수능형 6대 오답 함정 취약도 및 독서 행동 프로파일</span>
              </h3>

              <div className="p-4 rounded-xl bg-amber-50/60 border border-amber-200 text-xs">
                <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                  <div>
                    <span className="font-bold text-slate-600 block mb-0.5">최다 오답 함정:</span>
                    <span className="font-black text-rose-700 text-sm">
                      {currentStudent?.top_trap || 'D3 (전제 왜곡 및 비약)'}
                    </span>
                  </div>
                  <div>
                    <span className="font-bold text-slate-600 block mb-0.5">평균 지문 완독 소요시간:</span>
                    <span className="font-black text-slate-800 text-sm">
                      {currentStudent?.reading_habit || '속독형 (2분 10초 · 재독률 낮음)'}
                    </span>
                  </div>
                  <div>
                    <span className="font-bold text-slate-600 block mb-0.5">처방 클리닉 배정:</span>
                    <span className="font-black text-blue-800 text-sm">
                      {currentStudent?.assigned_clinic || '선수 공통기초 G5-COM-A5 구조도 요약'}
                    </span>
                  </div>
                </div>
              </div>
            </div>

            {/* Section 3: Director Custom Counseling Opinion */}
            <div className="mb-6">
              <h3 className="text-sm font-black text-slate-900 mb-2 flex items-center justify-between border-l-4 border-indigo-600 pl-2">
                <span>3. 원장 맞춤형 종합 상담 소견 및 향후 지도 계획</span>
                <span className="text-[11px] font-normal text-slate-400 no-print">
                  (클릭하여 수정 가능)
                </span>
              </h3>

              <textarea
                value={opinionText}
                onChange={(e) => setOpinionText(e.target.value)}
                rows={4}
                className="w-full p-3.5 rounded-xl border border-slate-300 bg-slate-50/50 text-slate-800 text-xs leading-relaxed font-medium focus:bg-white focus:ring-2 focus:ring-blue-500 outline-none transition resize-none print:bg-white print:border-slate-300"
              />
            </div>

            {/* Section 4: 12-Week Prescribed Roadmap */}
            <div className="mb-8">
              <h3 className="text-sm font-black text-slate-900 mb-2 border-l-4 border-emerald-600 pl-2">
                <span>4. 맞춤형 12주 집중 처방 로드맵</span>
              </h3>
              <div className="border border-slate-200 rounded-xl overflow-hidden text-xs">
                <table className="w-full text-left">
                  <thead className="bg-slate-100 text-slate-700 font-extrabold border-b border-slate-200">
                    <tr>
                      <th className="py-2 px-3">주차</th>
                      <th className="py-2 px-3">학습 단계</th>
                      <th className="py-2 px-3">핵심 학습 목표 및 슬롯</th>
                      <th className="py-2 px-3">적용 엔진</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-100 text-slate-800 font-medium">
                    <tr>
                      <td className="py-2 px-3 font-bold text-blue-700">1~4주차</td>
                      <td className="py-2 px-3">선수 결손 교정</td>
                      <td className="py-2 px-3">공통기초 A3 어휘 의미망 & 사고구술 빈칸 조립</td>
                      <td className="py-2 px-3">Inline Cloze + 어휘 듀얼</td>
                    </tr>
                    <tr>
                      <td className="py-2 px-3 font-bold text-indigo-700">5~8주차</td>
                      <td className="py-2 px-3">구조적 독해 심화</td>
                      <td className="py-2 px-3">Meyer 6대 구조도 노드 배치 & EBSR 2단계 추론</td>
                      <td className="py-2 px-3">Graphic Organizer + EBSR</td>
                    </tr>
                    <tr>
                      <td className="py-2 px-3 font-bold text-emerald-700">9~12주차</td>
                      <td className="py-2 px-3">실전 수능형 도약</td>
                      <td className="py-2 px-3">다중 텍스트 교차 분석 + 5종 교정부호 작문 퇴고</td>
                      <td className="py-2 px-3">Multi-Source Tab + RedPen</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            {/* Official Footer: Director Signature & Seal */}
            <div className="pt-6 border-t-2 border-slate-900 flex items-end justify-between">
              <div>
                <div className="text-xs font-bold text-slate-500">발행 기관: {academyName}</div>
                <div className="text-xs text-slate-500 mt-0.5">문의 및 상담 예약: ☎ {phoneContact}</div>
                <div className="text-[10px] text-slate-400 mt-1">
                  * Read X 상담 보고서 화면 예시입니다. 공인 평가 결과나 실제 학생의 학습 기록이 아닙니다.
                </div>
              </div>

              <div className="flex items-center gap-3">
                <div className="text-right">
                  <div className="text-xs text-slate-500 font-bold">원장 / 검수위원</div>
                  <div className="text-sm font-black text-slate-900">{directorName}</div>
                </div>

                {includeSeal && (
                  <div className="w-16 h-16 rounded-full border-2 border-rose-600 text-rose-600 flex flex-col items-center justify-center font-serif font-black text-[10px] leading-tight select-none rotate-[-8deg] shadow-xs">
                    <span className="tracking-widest">문해력</span>
                    <span className="text-xs">【印】</span>
                    <span className="text-[9px]">검증필</span>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
