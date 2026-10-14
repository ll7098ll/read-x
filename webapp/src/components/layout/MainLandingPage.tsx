import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { RoleType } from '../../types/courseware';

interface MainLandingPageProps {
  totalDbSlots: number;
}

export const MainLandingPage: React.FC<MainLandingPageProps> = ({ totalDbSlots }) => {
  const { setActiveRole } = useCoursewareStore();

  const handleSelectRole = (role: RoleType) => {
    setActiveRole(role);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 flex flex-col font-sans selection:bg-blue-600 selection:text-white">
      {/* Top Global Header */}
      <header className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-slate-200/80 px-4 sm:px-8 py-3.5">
        <div className="max-w-[1300px] mx-auto flex items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center font-black text-lg text-white shadow-sm">
              RX
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-black text-lg tracking-tight text-slate-900">
                  ReadX-Ray Pro
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200">
                  2022 개정 초등 전 교과
                </span>
              </div>
            </div>
          </div>

          {/* Quick Role Navigation */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            <button
              onClick={() => handleSelectRole('student')}
              className="text-xs font-bold px-3 py-1.5 rounded-lg text-slate-600 hover:text-blue-700 hover:bg-blue-50 transition cursor-pointer"
            >
              👦 학생
            </button>
            <button
              onClick={() => handleSelectRole('parent')}
              className="text-xs font-bold px-3 py-1.5 rounded-lg text-slate-600 hover:text-emerald-700 hover:bg-emerald-50 transition cursor-pointer"
            >
              👨‍👩‍👧 학부모
            </button>
            <button
              onClick={() => handleSelectRole('teacher')}
              className="text-xs font-bold px-3 py-1.5 rounded-lg text-slate-600 hover:text-indigo-700 hover:bg-indigo-50 transition cursor-pointer"
            >
              👩‍🏫 교사
            </button>
            <button
              onClick={() => handleSelectRole('admin')}
              className="text-xs font-bold px-3 py-1.5 rounded-lg text-slate-600 hover:text-amber-700 hover:bg-amber-50 transition cursor-pointer"
            >
              🏢 학원장
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 max-w-[1300px] w-full mx-auto px-4 sm:px-8 py-10 sm:py-14 space-y-16 sm:space-y-20">
        {/* Clean Hero Section */}
        <section className="text-center space-y-5 max-w-3xl mx-auto">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200/80 text-xs font-bold text-blue-800">
            <span className="w-2 h-2 rounded-full bg-blue-600 animate-pulse" />
            <span>수능 1등급 문해력 완성을 위한 초등 전 교과 코스웨어</span>
          </div>

          <h1 className="text-3xl sm:text-5xl font-black tracking-tight text-slate-900 leading-tight">
            어디서 왜 틀리는지 밝히는<br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600">
              6차원 X-Ray 문해력 스튜디오
            </span>
          </h1>

          <p className="text-sm sm:text-base text-slate-600 leading-relaxed max-w-xl mx-auto">
            국어·사회·과학 9대 전 교과 설명문 132슬롯과 수능형 평가원 오답공학(D1~D6)으로 학생, 학부모, 교사 모두에게 가장 명쾌한 문해력 여정을 제공합니다.
          </p>

          {/* Core Metrics Pill Strip */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-2 text-center">
            <div className="bg-white border border-slate-200/90 rounded-xl p-3.5 shadow-xs">
              <span className="text-[11px] font-bold text-slate-500 block">전 교과 설명문</span>
              <span className="text-xl sm:text-2xl font-black text-blue-600 mt-0.5 block">
                {totalDbSlots} 슬롯
              </span>
            </div>
            <div className="bg-white border border-slate-200/90 rounded-xl p-3.5 shadow-xs">
              <span className="text-[11px] font-bold text-slate-500 block">글로벌 TEI 엔진</span>
              <span className="text-xl sm:text-2xl font-black text-emerald-600 mt-0.5 block">
                7종 완비
              </span>
            </div>
            <div className="bg-white border border-slate-200/90 rounded-xl p-3.5 shadow-xs">
              <span className="text-[11px] font-bold text-slate-500 block">수능 오답공학</span>
              <span className="text-xl sm:text-2xl font-black text-amber-600 mt-0.5 block">
                D1~D6 백신
              </span>
            </div>
            <div className="bg-white border border-slate-200/90 rounded-xl p-3.5 shadow-xs">
              <span className="text-[11px] font-bold text-slate-500 block">온디바이스 AI</span>
              <span className="text-xl sm:text-2xl font-black text-indigo-600 mt-0.5 block">
                $0 클라우드
              </span>
            </div>
          </div>
        </section>

        {/* 4 Role Gateway Cards (Grand Central Entry) */}
        <section className="space-y-6">
          <div className="text-center">
            <h2 className="text-xl sm:text-2xl font-black text-slate-900">
              사용자 주체를 선택하여 입장하세요
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 mt-1">
              각 사용자 맞춤형 전용 화면으로 바로 연결됩니다. 언제든 상단의 홈 버튼으로 돌아올 수 있습니다.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
            {/* 1. Student Card */}
            <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm hover:shadow-md hover:border-blue-400 transition-all flex flex-col justify-between group">
              <div className="space-y-3">
                <div className="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-2xl group-hover:scale-105 transition">
                  👦
                </div>
                <div>
                  <span className="text-[11px] font-bold text-blue-600">STUDENT</span>
                  <h3 className="text-lg font-black text-slate-900 mt-0.5">학생 학습관</h3>
                  <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">
                    오늘 배정된 과제를 풀고, 인체공학적 독서 스튜디오에서 형광펜·끊어읽기·초점 자로 글에 온전히 몰입합니다.
                  </p>
                </div>
                <div className="pt-2 border-t border-slate-100 text-xs text-slate-600 space-y-1">
                  <div className="flex items-center gap-1.5">
                    <span className="text-blue-500 font-bold">✓</span> 오늘의 배정 과제함
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-blue-500 font-bold">✓</span> 클린 독서 & 수능형 문제 풀이
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-blue-500 font-bold">✓</span> 오답노트 & 10초 어휘 듀얼
                  </div>
                </div>
              </div>

              <button
                onClick={() => handleSelectRole('student')}
                className="mt-6 w-full py-2.5 px-4 rounded-xl bg-blue-600 hover:bg-blue-500 text-white font-black text-xs shadow-sm transition flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>학생으로 시작하기</span>
                <span>➔</span>
              </button>
            </div>

            {/* 2. Parent Card */}
            <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm hover:shadow-md hover:border-emerald-400 transition-all flex flex-col justify-between group">
              <div className="space-y-3">
                <div className="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-2xl group-hover:scale-105 transition">
                  👨‍👩‍👧
                </div>
                <div>
                  <span className="text-[11px] font-bold text-emerald-600">PARENT</span>
                  <h3 className="text-lg font-black text-slate-900 mt-0.5">학부모 리포트</h3>
                  <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">
                    자녀의 오늘 과제 완료 상태와 6차원 X-Ray 진단 결과, 그리고 식탁에서 나눌 대화 가이드를 확인합니다.
                  </p>
                </div>
                <div className="pt-2 border-t border-slate-100 text-xs text-slate-600 space-y-1">
                  <div className="flex items-center gap-1.5">
                    <span className="text-emerald-500 font-bold">✓</span> 오늘의 학습 완료 실시간 확인
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-emerald-500 font-bold">✓</span> 6차원 X-Ray 정밀 진단서
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-emerald-500 font-bold">✓</span> 밥상머리 대화 코칭 가이드
                  </div>
                </div>
              </div>

              <button
                onClick={() => handleSelectRole('parent')}
                className="mt-6 w-full py-2.5 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs shadow-sm transition flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>학부모로 시작하기</span>
                <span>➔</span>
              </button>
            </div>

            {/* 3. Teacher Card */}
            <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm hover:shadow-md hover:border-indigo-400 transition-all flex flex-col justify-between group">
              <div className="space-y-3">
                <div className="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-2xl group-hover:scale-105 transition">
                  👩‍🏫
                </div>
                <div>
                  <span className="text-[11px] font-bold text-indigo-600">TEACHER</span>
                  <h3 className="text-lg font-black text-slate-900 mt-0.5">교사 콘솔</h3>
                  <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">
                    학급 25명의 진단 현황과 실시간 독서 병목을 관제하고, 취약 학생에게 1:1 맞춤 과제를 원클릭 처방합니다.
                  </p>
                </div>
                <div className="pt-2 border-t border-slate-100 text-xs text-slate-600 space-y-1">
                  <div className="flex items-center gap-1.5">
                    <span className="text-indigo-500 font-bold">✓</span> 25명 원생 실시간 관제 조종석
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-indigo-500 font-bold">✓</span> 취약 학생 1:1 맞춤 과제 원클릭 배정
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-indigo-500 font-bold">✓</span> 학급 12주 KReaD 성장 통계
                  </div>
                </div>
              </div>

              <button
                onClick={() => handleSelectRole('teacher')}
                className="mt-6 w-full py-2.5 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-black text-xs shadow-sm transition flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>교사로 시작하기</span>
                <span>➔</span>
              </button>
            </div>

            {/* 4. Academy Admin Card */}
            <div className="bg-white rounded-2xl border border-slate-200/90 p-6 shadow-sm hover:shadow-md hover:border-amber-400 transition-all flex flex-col justify-between group">
              <div className="space-y-3">
                <div className="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-2xl group-hover:scale-105 transition">
                  🏢
                </div>
                <div>
                  <span className="text-[11px] font-bold text-amber-600">ACADEMY ADMIN</span>
                  <h3 className="text-lg font-black text-slate-900 mt-0.5">학원장 허브</h3>
                  <p className="text-xs text-slate-500 mt-1.5 leading-relaxed">
                    132개 슬롯 전수 문항 CMS를 관리하고, 학원 브랜딩 직인이 날인된 프리미엄 상담 성적표를 인쇄합니다.
                  </p>
                </div>
                <div className="pt-2 border-t border-slate-100 text-xs text-slate-600 space-y-1">
                  <div className="flex items-center gap-1.5">
                    <span className="text-amber-500 font-bold">✓</span> 132슬롯 마스터 문항 은행 CMS
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-amber-500 font-bold">✓</span> B2B 200좌석 라이선스 관리
                  </div>
                  <div className="flex items-center gap-1.5">
                    <span className="text-amber-500 font-bold">✓</span> 직인 날인 심층 상담 성적표 출력
                  </div>
                </div>
              </div>

              <button
                onClick={() => handleSelectRole('admin')}
                className="mt-6 w-full py-2.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs shadow-sm transition flex items-center justify-center gap-1.5 cursor-pointer"
              >
                <span>학원장으로 시작하기</span>
                <span>➔</span>
              </button>
            </div>
          </div>
        </section>

        {/* 3 Core Differentiator Features (Clean Minimalist Grid) */}
        <section className="bg-white rounded-3xl border border-slate-200/90 p-8 sm:p-10 shadow-sm space-y-8">
          <div className="text-center max-w-xl mx-auto space-y-1">
            <h2 className="text-xl sm:text-2xl font-black text-slate-900">
              ReadX-Ray의 3대 핵심 기술
            </h2>
            <p className="text-xs sm:text-sm text-slate-500">
              단순 문제 풀이를 넘어 인지적 독해 역량을 근본적으로 훈련합니다.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-slate-50/70 rounded-2xl p-6 border border-slate-200/60 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center font-black text-sm">
                01
              </div>
              <h3 className="text-base font-black text-slate-900">6차원 정밀 X-Ray 진단</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                어휘(V)·사실(F)·추론(I)·구조(S)·비판(C)·메타인지(M) 6개 축으로 분석하여 학생의 취약 지점을 투명하게 시각화합니다.
              </p>
            </div>

            <div className="bg-slate-50/70 rounded-2xl p-6 border border-slate-200/60 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center font-black text-sm">
                02
              </div>
              <h3 className="text-base font-black text-slate-900">7대 인터랙티브 TEI 엔진</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                단순 5지선다를 탈피하여 EBSR(근거 매핑), 사고구술 빈칸, 6대 담화 도해 조직도, 빨간펜 첨삭 퇴고 실습을 지원합니다.
              </p>
            </div>

            <div className="bg-slate-50/70 rounded-2xl p-6 border border-slate-200/60 space-y-3">
              <div className="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-black text-sm">
                03
              </div>
              <h3 className="text-base font-black text-slate-900">KICE 수능 오답공학 백신 (D1~D6)</h3>
              <p className="text-xs text-slate-600 leading-relaxed">
                평가원이 출제하는 6대 매력적 오답 함정을 과학적으로 분류하고, 오답 선택 시 즉각적인 백신 해설을 처방합니다.
              </p>
            </div>
          </div>
        </section>
      </main>

      {/* Minimal Footer */}
      <footer className="border-t border-slate-200 bg-white py-6 px-4 text-center text-xs text-slate-500">
        <div className="max-w-[1300px] mx-auto flex flex-wrap items-center justify-between gap-3">
          <div className="font-bold text-slate-700">
            ReadX-Ray Pro · 2022 개정 초등 전 교과 수능형 문해력 코스웨어
          </div>
          <div className="text-slate-400">
            Designed with Google Stitch Design Principles
          </div>
        </div>
      </footer>
    </div>
  );
};
