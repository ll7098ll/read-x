import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';

interface PlanetInfo {
  id: string;
  subject: string;
  name: string;
  grade: string;
  slotId: string;
  concept: string;
  structure: string;
  kread: number;
  color: string;
  icon: string;
  terraformedPercent: number;
}

interface GalaxyExpeditionMapProps {
  onClose: () => void;
}

export const GalaxyExpeditionMap: React.FC<GalaxyExpeditionMapProps> = ({ onClose }) => {
  const { selectGradeAndSlot, completedSlots } = useCoursewareStore();

  const planets: PlanetInfo[] = [
    {
      id: 'sci',
      subject: '과학',
      name: '아쿠아-테라 (열수지 행성)',
      grade: '초등 6학년',
      slotId: 'G6-EXP-V2-2',
      concept: '지구 열수지 평형과 북극 해빙의 알베도 양(+)의 피드백',
      structure: '다단계 연쇄 인과',
      kread: 980,
      color: 'from-cyan-500 to-blue-700',
      icon: '❄️',
      terraformedPercent: completedSlots['G6-EXP-V2-2'] ? 100 : 75,
    },
    {
      id: 'soc',
      subject: '사회',
      name: '폴리스-마켓 (시장 경제 행성)',
      grade: '초등 6학년',
      slotId: 'G6-EXP-V1-1',
      concept: '시장 가격 결정과 수요·공급 곡선의 가격 탄력성',
      structure: '원인-결과 & 그래프',
      kread: 950,
      color: 'from-amber-500 to-orange-700',
      icon: '📈',
      terraformedPercent: completedSlots['G6-EXP-V1-1'] ? 100 : 60,
    },
    {
      id: 'mor',
      subject: '도덕',
      name: '디케-에티카 (정의 철학 행성)',
      grade: '초등 6학년',
      slotId: 'G6-EXP-V3-1',
      concept: '자율주행 자동차의 트롤리 딜레마 (공리주의 vs 의무론)',
      structure: '딜레마 비교 & 가치평가',
      kread: 960,
      color: 'from-purple-500 to-indigo-800',
      icon: '⚖️',
      terraformedPercent: completedSlots['G6-EXP-V3-1'] ? 100 : 50,
    },
    {
      id: 'pra',
      subject: '실과',
      name: '테크노-메이커 (알고리즘 행성)',
      grade: '초등 5학년',
      slotId: 'G5-EXP-V1-3',
      concept: '소프트웨어 알고리즘의 3대 구조(순차·선택·반복)와 3D 프린팅',
      structure: '순서·과정 & 분류',
      kread: 910,
      color: 'from-emerald-500 to-teal-800',
      icon: '💻',
      terraformedPercent: completedSlots['G5-EXP-V1-3'] ? 100 : 80,
    },
    {
      id: 'mat',
      subject: '수학',
      name: '뉴턴-라티오 (비와 비율 행성)',
      grade: '초등 5학년',
      slotId: 'G5-EXP-V2-1',
      concept: '규칙과 대응, 두 변수 사이의 종속 관계와 비율 그래프 해석',
      structure: '인과 사슬 & 수식',
      kread: 920,
      color: 'from-blue-600 to-indigo-900',
      icon: '📐',
      terraformedPercent: completedSlots['G5-EXP-V2-1'] ? 100 : 45,
    },
    {
      id: 'mus',
      subject: '음악',
      name: '하모니아 (음파 물리 행성)',
      grade: '초등 3학년',
      slotId: 'G3-EXP-V1-3',
      concept: '악기 소리의 발생 원리(진동수와 공명) 및 12평균율',
      structure: '전체-부분 & 비교대조',
      kread: 840,
      color: 'from-pink-500 to-rose-700',
      icon: '🎵',
      terraformedPercent: completedSlots['G3-EXP-V1-3'] ? 100 : 65,
    },
    {
      id: 'art',
      subject: '미술',
      name: '퍼스펙티바 (원근법 미학 행성)',
      grade: '초등 4학년',
      slotId: 'G4-EXP-V1-2',
      concept: '선원근법(소실점)과 공기원근법의 공간 표현 및 색의 감산혼합',
      structure: '비교·대조 & 문제해결',
      kread: 870,
      color: 'from-yellow-400 to-amber-600',
      icon: '🎨',
      terraformedPercent: completedSlots['G4-EXP-V1-2'] ? 100 : 55,
    },
    {
      id: 'pe',
      subject: '체육',
      name: '키네틱스 (인체 지레 행성)',
      grade: '초등 5학년',
      slotId: 'G5-EXP-V1-2',
      concept: '인체 관절의 1·2·3종 지레 원리와 축구공 마그누스 효과',
      structure: '전체-부분 & 원리적용',
      kread: 900,
      color: 'from-lime-500 to-emerald-700',
      icon: '⚽',
      terraformedPercent: completedSlots['G5-EXP-V1-2'] ? 100 : 70,
    },
    {
      id: 'kor',
      subject: '국어',
      name: '로그스 (문해 독서 수도 행성)',
      grade: '초등 6학년',
      slotId: 'G6-EXP-V3-2',
      concept: '비문학 설명문 16대 하위기능 통합 독해 및 2층 비판적 첨삭',
      structure: '복합 설명 담화',
      kread: 990,
      color: 'from-violet-600 to-purple-900',
      icon: '📚',
      terraformedPercent: completedSlots['G6-EXP-V3-2'] ? 100 : 90,
    },
  ];

  const [selectedPlanet, setSelectedPlanet] = useState<PlanetInfo>(planets[0]);

  const handleLaunchExpedition = (planet: PlanetInfo) => {
    const gNum = parseInt(planet.grade.replace(/[^0-9]/g, '')) || 6;
    selectGradeAndSlot(gNum, planet.slotId, 'studio');
    onClose();
  };

  const avgTerraform = Math.round(
    planets.reduce((acc, p) => acc + p.terraformedPercent, 0) / planets.length
  );

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-slate-900 border-2 border-indigo-500/80 rounded-3xl max-w-4xl w-full p-6 text-white shadow-2xl relative flex flex-col max-h-[90vh] overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between pb-3 border-b border-slate-800 shrink-0">
          <div className="flex items-center gap-2.5">
            <span className="w-9 h-9 rounded-xl bg-indigo-600 text-white flex items-center justify-center text-lg font-black shadow-md">
              🌌
            </span>
            <div>
              <h3 className="font-black text-base text-indigo-300">
                지식 행성 테라포밍 은하계 원정대 (Literacy Galaxy Expedition)
              </h3>
              <p className="text-[11px] text-slate-400">
                초등 9대 전 교과 설명문 지문을 마스터하여 황폐한 행성에 문명을 꽃피우세요!
              </p>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <span className="px-3 py-1 bg-indigo-950 border border-indigo-400 text-indigo-300 rounded-full text-xs font-mono font-bold">
              은하계 정화율: {avgTerraform}%
            </span>
            <button
              onClick={onClose}
              className="text-slate-400 hover:text-white text-lg font-bold p-1 cursor-pointer"
            >
              ✕
            </button>
          </div>
        </div>

        {/* Galaxy Body: Left Planet Orbit Grid + Right Planet Detail Inspector */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 py-4 overflow-y-auto flex-1">
          {/* Planets Orbit Grid (7 cols) */}
          <div className="lg:col-span-7 grid grid-cols-3 gap-3">
            {planets.map((planet) => {
              const isSelected = selectedPlanet.id === planet.id;
              const isFullyTerraformed = planet.terraformedPercent >= 100;

              return (
                <div
                  key={planet.id}
                  onClick={() => setSelectedPlanet(planet)}
                  className={`p-3 rounded-2xl border cursor-pointer transition-all flex flex-col items-center text-center justify-between min-h-[120px] ${
                    isSelected
                      ? 'bg-slate-800 border-indigo-400 ring-2 ring-indigo-400/80 scale-102 shadow-lg'
                      : 'bg-slate-800/50 border-slate-700/80 hover:bg-slate-800/80 hover:border-slate-600'
                  }`}
                >
                  {/* Planet Sphere Icon */}
                  <div
                    className={`w-12 h-12 rounded-full bg-gradient-to-br ${planet.color} flex items-center justify-center text-xl shadow-md border-2 ${
                      isFullyTerraformed ? 'border-amber-400 animate-pulse' : 'border-white/30'
                    }`}
                  >
                    {planet.icon}
                  </div>

                  <div className="mt-2">
                    <div className="text-[11px] font-bold text-slate-400">{planet.subject}</div>
                    <div className="text-xs font-black text-slate-100 truncate max-w-[90px]">
                      {planet.name.split(' ')[0]}
                    </div>
                  </div>

                  {/* Terraforming Progress Bar */}
                  <div className="w-full mt-2">
                    <div className="w-full h-1.5 bg-slate-700 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-emerald-400 transition-all"
                        style={{ width: `${planet.terraformedPercent}%` }}
                      />
                    </div>
                    <span className="text-[10px] text-slate-400 font-mono">
                      {planet.terraformedPercent}%
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Selected Planet Inspector Panel (5 cols) */}
          <div className="lg:col-span-5 bg-slate-800/90 border border-slate-700 rounded-2xl p-4 flex flex-col justify-between space-y-3">
            <div className="space-y-3">
              <div className="flex items-center gap-3">
                <div
                  className={`w-14 h-14 rounded-full bg-gradient-to-br ${selectedPlanet.color} flex items-center justify-center text-2xl shadow-lg border-2 border-white/40 shrink-0`}
                >
                  {selectedPlanet.icon}
                </div>
                <div>
                  <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-900 text-indigo-300">
                    [{selectedPlanet.subject}] {selectedPlanet.grade}
                  </span>
                  <h4 className="text-base font-black text-white mt-0.5">
                    {selectedPlanet.name}
                  </h4>
                  <span className="text-[11px] font-mono text-slate-400">
                    KReaD {selectedPlanet.kread}
                  </span>
                </div>
              </div>

              <div className="space-y-2 text-xs">
                <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80">
                  <span className="text-slate-400 font-bold block mb-0.5">🧬 핵심 교과 개념</span>
                  <span className="text-slate-100 font-semibold leading-relaxed">
                    {selectedPlanet.concept}
                  </span>
                </div>

                <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-700/80 flex justify-between">
                  <div>
                    <span className="text-slate-400 font-bold block mb-0.5">🧩 설명 담화 구조</span>
                    <span className="text-slate-200 font-semibold">{selectedPlanet.structure}</span>
                  </div>
                  <div className="text-right">
                    <span className="text-slate-400 font-bold block mb-0.5">슬롯 코드</span>
                    <span className="text-indigo-300 font-mono font-bold">
                      {selectedPlanet.slotId}
                    </span>
                  </div>
                </div>

                <div className="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-500/40 text-emerald-200">
                  <div className="flex justify-between font-bold mb-1">
                    <span>🌱 행성 테라포밍(지식 정화도)</span>
                    <span className="font-mono">{selectedPlanet.terraformedPercent}%</span>
                  </div>
                  <p className="text-[11px] text-emerald-300/90 leading-tight">
                    {selectedPlanet.terraformedPercent >= 100
                      ? '축하합니다! 이 행성의 설명문 지문과 실전 수능 문항을 완전히 정복하여 푸른 생태계가 복원되었습니다.'
                      : '아직 학습하지 않은 단서와 도해 슬롯이 남아있습니다. 탐사를 시작해 문명을 번영시키세요!'}
                  </p>
                </div>
              </div>
            </div>

            <button
              onClick={() => handleLaunchExpedition(selectedPlanet)}
              className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-black text-xs transition shadow-lg flex items-center justify-center gap-2 cursor-pointer mt-2"
            >
              <span>🚀 「{selectedPlanet.name.split(' ')[0]}」 교과 지문 탐사 출발하기</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
