import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { RoleType } from '../../types/courseware';

interface RoleGatewayModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const RoleGatewayModal: React.FC<RoleGatewayModalProps> = ({
  isOpen,
  onClose,
}) => {
  const { activeRole, setActiveRole } = useCoursewareStore();

  if (!isOpen) return null;

  const roles: Array<{
    id: RoleType;
    icon: string;
    title: string;
    sub: string;
    target: string;
    badge: string;
    badgeColor: string;
    themeColor: string;
    features: string[];
    actionLabel: string;
  }> = [
    {
      id: 'student',
      icon: '👦',
      title: '학생 학습관',
      sub: 'Student Learning Portal',
      target: '초등 1~6학년 학생',
      badge: '몰입형 인터랙티브 학습',
      badgeColor: 'bg-blue-100 text-blue-800 border-blue-200',
      themeColor: 'hover:border-blue-500 hover:ring-2 hover:ring-blue-500/20 group-hover:text-blue-600',
      features: [
        '내 학년 16차시 인터랙티브 코스 맵',
        '선수 결손 보강 1:1 맞춤 약점 처방 클리닉',
        '7대 TEI 엔진 & 수능 비문학 스플릿 리더',
        '10초 어휘 듀얼 배틀 & 은하계 테라포밍 맵',
      ],
      actionLabel: '학생 전용관 입장 ➔',
    },
    {
      id: 'parent',
      icon: '👨‍👩‍👧',
      title: '학부모 리포트 센터',
      sub: 'Parent Diagnostic & Coaching Care',
      target: '학부모 및 보호자',
      badge: '가정 연계 안심 코칭',
      badgeColor: 'bg-emerald-100 text-emerald-800 border-emerald-200',
      themeColor: 'hover:border-emerald-500 hover:ring-2 hover:ring-emerald-500/20 group-hover:text-emerald-600',
      features: [
        '10초 인스턴트 요약 (Where/Why/How 인지 분석)',
        '6차원 X-Ray 상세 진단표 & KReaD 성장 지표',
        '밥상머리 대화(Table Talk) 1:1 가정 코칭 가이드',
        '스마트폰 카카오 알림톡 웹카드 & A4 인쇄',
      ],
      actionLabel: '학부모 센터 입장 ➔',
    },
    {
      id: 'teacher',
      icon: '👩‍🏫',
      title: '교사 클래스 콘솔',
      sub: 'Teacher Live Cockpit & LMS',
      target: '학교 교사 및 지도 강사',
      badge: '학급 실시간 지도·처방',
      badgeColor: 'bg-indigo-100 text-indigo-800 border-indigo-200',
      themeColor: 'hover:border-indigo-500 hover:ring-2 hover:ring-indigo-500/20 group-hover:text-indigo-600',
      features: [
        '학급 25명 16대 하위기능 정밀 성취도 히트맵',
        '실시간 교실 조종석: 원생 독서 레이더 & 1:1 힌트 전송',
        '초등 1~6학년 대표 단원 비교 & KReaD 복잡도 표준',
        '설명문 96개 + 공통기초 36개 132슬롯 위계 마스터',
      ],
      actionLabel: '교사 콘솔 입장 ➔',
    },
    {
      id: 'admin',
      icon: '🏢',
      title: '학원장 B2B 허브',
      sub: 'Academy Director & Operations',
      target: '학원장 및 교육기관 운영자',
      badge: '좌석 관리 & 상담 성적표',
      badgeColor: 'bg-amber-100 text-amber-800 border-amber-200',
      themeColor: 'hover:border-amber-500 hover:ring-2 hover:ring-amber-500/20 group-hover:text-amber-600',
      features: [
        'B2B 좌석(Seat) 라이선스 쿼터 & 원생 엑셀 일괄 등록',
        '학원 브랜드 로고 & 원장 직인 날인 프리미엄 상담 성적표',
        '132슬롯 Item Bank 데이터베이스 CMS & 출제 워크벤치',
        '5대 QA 게이트 무결성 검증 & Firestore DB 동기화',
      ],
      actionLabel: '학원장 허브 입장 ➔',
    },
  ];

  const handleSelectRole = (role: RoleType) => {
    setActiveRole(role);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-5 overflow-y-auto animate-fade-in">
      <div className="bg-white w-full max-w-5xl rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-auto flex flex-col">
        {/* Modal Top Brand Bar */}
        <div className="bg-slate-900 text-white p-6 sm:p-8 flex flex-wrap items-center justify-between gap-4 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2 mb-2">
              <span className="w-8 h-8 rounded-xl bg-gradient-to-tr from-blue-500 to-indigo-600 flex items-center justify-center font-black text-sm">
                RX
              </span>
              <span className="text-xs font-mono font-bold tracking-wider text-emerald-400">
                READ X PERSONA GATEWAY
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-black tracking-tight text-white">
              이용하실 사용자 주체(페르소나)를 선택해 주세요
            </h2>
            <p className="text-xs sm:text-sm text-slate-400 mt-1">
              선택한 주체에 맞추어 불필요한 관리자/타 사용자 메뉴가 완전히 배제된 <b>맞춤형 독립 화면</b>이 렌더링됩니다.
            </p>
          </div>

          <button
            onClick={onClose}
            className="w-10 h-10 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-lg font-bold transition cursor-pointer"
          >
            ✕
          </button>
        </div>

        {/* 4 Dedicated Stakeholder Cards Grid */}
        <div className="p-6 sm:p-8 bg-slate-50 grid grid-cols-1 md:grid-cols-2 gap-5">
          {roles.map((r) => {
            const isCurrent = activeRole === r.id;
            return (
              <div
                key={r.id}
                onClick={() => handleSelectRole(r.id)}
                className={`bg-white rounded-2xl p-6 border-2 transition-all cursor-pointer flex flex-col justify-between group shadow-sm hover:shadow-xl ${
                  isCurrent
                    ? 'border-blue-600 ring-2 ring-blue-500/30'
                    : 'border-slate-200 ' + r.themeColor
                }`}
              >
                <div>
                  <div className="flex items-start justify-between gap-3 mb-3">
                    <div className="flex items-center gap-3">
                      <div className="w-12 h-12 rounded-2xl bg-slate-100 flex items-center justify-center text-2xl shadow-inner group-hover:scale-110 transition-transform">
                        {r.icon}
                      </div>
                      <div>
                        <h3 className="text-lg font-black text-slate-900 group-hover:text-blue-600 transition-colors">
                          {r.title}
                        </h3>
                        <p className="text-[11px] font-mono text-slate-400 font-bold">{r.sub}</p>
                      </div>
                    </div>

                    <span
                      className={`text-[10px] font-extrabold px-2.5 py-1 rounded-full border ${r.badgeColor}`}
                    >
                      {r.badge}
                    </span>
                  </div>

                  <div className="text-xs text-slate-500 mb-4 font-bold flex items-center gap-1.5">
                    <span>대상:</span>
                    <span className="text-slate-800 bg-slate-100 px-2 py-0.5 rounded-md">
                      {r.target}
                    </span>
                    {isCurrent && (
                      <span className="ml-auto text-[11px] font-black text-blue-600 bg-blue-50 px-2 py-0.5 rounded-md">
                        ● 현재 접속 중
                      </span>
                    )}
                  </div>

                  {/* Key Features Bullet Points */}
                  <ul className="space-y-2 mb-6">
                    {r.features.map((feat, idx) => (
                      <li
                        key={idx}
                        className="text-xs text-slate-700 flex items-center gap-2 font-medium"
                      >
                        <span className="w-1.5 h-1.5 rounded-full bg-blue-500 shrink-0" />
                        <span>{feat}</span>
                      </li>
                    ))}
                  </ul>
                </div>

                <button
                  type="button"
                  className={`w-full py-3 rounded-xl text-xs font-black transition-all flex items-center justify-center gap-2 shadow-xs ${
                    isCurrent
                      ? 'bg-blue-600 text-white shadow-md'
                      : 'bg-slate-900 text-white group-hover:bg-blue-600'
                  }`}
                >
                  <span>{r.actionLabel}</span>
                </button>
              </div>
            );
          })}
        </div>

        {/* Footer Guidance */}
        <div className="bg-white px-6 py-4 border-t border-slate-200 flex flex-wrap items-center justify-between text-xs text-slate-500">
          <div>
            💡 언제든 화면 상단 우측의 <b>[🔄 사용자 전환]</b> 버튼을 통해 다른 주체로 이동할 수 있습니다.
          </div>
          <div className="font-mono text-[11px]">
            Read X 4-Persona Unified Architecture
          </div>
        </div>
      </div>
    </div>
  );
};
