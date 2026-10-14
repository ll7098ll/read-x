import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';

interface OnboardingCatModalProps {
  gradeData: GradeData;
  onClose: () => void;
}

interface CatItem {
  id: string;
  level: 'easy' | 'medium' | 'hard';
  domain: string;
  kreadWeight: number;
  passageSnippet: string;
  stem: string;
  options: {
    no: number;
    text: string;
    isCorrect: boolean;
    trapCode?: string;
  }[];
  explanation: string;
}

export const OnboardingCatModal: React.FC<OnboardingCatModalProps> = ({
  gradeData,
  onClose,
}) => {
  const {
    setActiveSlotId,
    setStudentMode,
    boostSmartScore,
    dynamicSubskillScores,
  } = useCoursewareStore();

  // CAT Question Pool (Adaptive 3-Tier Branching)
  const catPool: Record<string, CatItem> = {
    // Stage 1 (Initial Medium Anchor)
    stage1_medium: {
      id: 'CAT-S1-M',
      level: 'medium',
      domain: '어휘 및 사실적 이해 (V / F)',
      kreadWeight: 880,
      passageSnippet: `인공지능(AI) 신경망에서 '가중치(Weight)'는 뉴런 사이의 연결 강도를 의미한다. 학습이 진행될수록 오차를 줄이는 방향으로 이 가중치가 미세하게 갱신되며, 마치 인간 뇌의 시냅스가 강화되는 원리와 유사하다.`,
      stem: '윗글의 내용과 일치하지 않는 것은 무엇인가요?',
      options: [
        { no: 1, text: '신경망의 가중치는 뉴런 간 연결 강도를 나타낸다.', isCorrect: false, trapCode: 'D1' },
        { no: 2, text: '학습 과정에서 가중치는 오차를 줄이도록 갱신된다.', isCorrect: false, trapCode: 'D1' },
        { no: 3, text: '인공지능 학습은 인간 뇌의 시냅스 강화와 유사한 방식으로 작동한다.', isCorrect: false, trapCode: 'D1' },
        { no: 4, text: '가중치는 학습 초기부터 한 번 정해지면 영구히 고정된다.', isCorrect: true },
      ],
      explanation: '본문에서 "학습이 진행될수록 가중치가 미세하게 갱신된다"고 하였으므로, 영구히 고정된다는 4번 선지가 일치하지 않는 정답입니다.',
    },

    // Stage 2 - Branch A (Hard: from Stage 1 Correct)
    stage2_hard: {
      id: 'CAT-S2-H',
      level: 'hard',
      domain: '심화 인과 추론 및 구조 파악 (I / S)',
      kreadWeight: 1050,
      passageSnippet: `기억 장치의 계층 구조에서 CPU 레지스터와 메인 메모리 사이의 속도 격차를 완화하기 위해 캐시 메모리가 도입되었다. 캐시는 '시간 지역성(최근 참조된 데이터가 곧 다시 참조됨)'과 '공간 지역성(참조된 데이터 인근이 연속 참조됨)'이라는 원리를 전제로 작동한다. 만약 프로그램이 메모리를 완전히 무작위로 순회한다면 캐시의 효용성은 급격히 감소한다.`,
      stem: '윗글을 바탕으로 추론할 때, 캐시 메모리의 효율이 가장 떨어지는 상황은?',
      options: [
        { no: 1, text: '반복문에서 동일한 변수를 연속해서 여러 번 조회할 때', isCorrect: false, trapCode: 'D2' },
        { no: 2, text: '배열(Array)의 인접한 주소들을 순차적으로 순회하며 계산할 때', isCorrect: false, trapCode: 'D2' },
        { no: 3, text: '대용량 데이터베이스를 공간적 연속성 없이 난수(Random) 주소로 호출할 때', isCorrect: true },
        { no: 4, text: 'CPU 레지스터의 용량이 부족하여 캐시 메모리에 데이터를 보관할 때', isCorrect: false, trapCode: 'D3' },
      ],
      explanation: '지문에서 "완전히 무작위로 순회한다면 캐시의 효용성이 급격히 감소한다"고 명시했으므로 3번 상황이 캐시 적중률이 가장 낮습니다.',
    },

    // Stage 2 - Branch B (Easy: from Stage 1 Incorrect)
    stage2_easy: {
      id: 'CAT-S2-E',
      level: 'easy',
      domain: '핵심 어휘 맥락 추론 (V)',
      kreadWeight: 750,
      passageSnippet: `식물은 낮 동안 엽록체에서 햇빛 에너지를 받아 이산화탄소와 물을 포도당과 산소로 전환하는 '광합성'을 수행한다. 이 과정에서 발생한 산소는 잎의 기공을 통해 외부로 방출된다.`,
      stem: '식물이 광합성을 통해 만들어내는 산소는 어디를 통해 방출되나요?',
      options: [
        { no: 1, text: '뿌리의 털', isCorrect: false, trapCode: 'D1' },
        { no: 2, text: '줄기의 물관', isCorrect: false, trapCode: 'D1' },
        { no: 3, text: '잎의 기공', isCorrect: true },
        { no: 4, text: '꽃의 꽃가루', isCorrect: false, trapCode: 'D1' },
      ],
      explanation: '지문 마지막 문장에 "산소는 잎의 기공을 통해 외부로 방출된다"고 직접 진술되어 있습니다.',
    },

    // Stage 3 - Branch A (Master Hard: from Stage 2 Hard Correct)
    stage3_master: {
      id: 'CAT-S3-MH',
      level: 'hard',
      domain: '수능형 비판·평가 및 논리적 비약 탐지 (E / M)',
      kreadWeight: 1180,
      passageSnippet: `어떤 연구팀은 "초콜릿 소비량이 높은 국가일수록 노벨상 수상자 배출 수가 많다"는 상관관계를 발표하며, 국민 지능을 위해 초콜릿 섭취를 장려해야 한다고 주장했다. 그러나 이는 '국가의 경제적 부(소득 수준)'라는 제3의 혼란 변인을 간과한 것이다. 부유한 국가일수록 교육 연구비 투자가 많아 노벨상 수상자가 많고, 동시에 고급 기호식품인 초콜릿 소비도 많을 뿐이다.`,
      stem: '연구팀 주장의 논리적 오류를 가장 정확하게 지적한 것은?',
      options: [
        { no: 1, text: '초콜릿의 성분이 뇌 인지 기능에 전혀 무해하다는 사실을 증명하지 못했다.', isCorrect: false, trapCode: 'D4' },
        { no: 2, text: '단순한 상관관계를 인과관계로 착각하고 공통 원인(경제 수준)을 통제하지 못했다.', isCorrect: true },
        { no: 3, text: '노벨상 수상자의 국적별 초콜릿 섭취 통계를 표본 조사하지 않았다.', isCorrect: false, trapCode: 'D3' },
        { no: 4, text: '가난한 국가에서도 노벨 평화상 수상자가 나온 반례를 무시했다.', isCorrect: false, trapCode: 'D5' },
      ],
      explanation: '상관관계와 인과관계를 혼동하고 제3의 잠재 변수(경제력)를 간과한 전형적인 논리 오류를 지적한 2번이 정답입니다.',
    },

    // Stage 3 - Branch B (Intermediate: from mixed results)
    stage3_intermediate: {
      id: 'CAT-S3-INT',
      level: 'medium',
      domain: '문단 간 전개 방식 및 핵심 주장 (S)',
      kreadWeight: 920,
      passageSnippet: `스마트폰의 블루라이트는 멜라토닌 분비를 억제하여 수면을 방해한다. 따라서 자기 전 1시간 동안 화면을 멀리하면 숙면을 취할 수 있다. 반면, 최근 출시된 야간 모드 필터는 이 유해 파장을 차단하여 생체 리듬의 교란을 최소화해 준다.`,
      stem: '윗글의 중심 내용으로 가장 알맞은 것은?',
      options: [
        { no: 1, text: '블루라이트가 수면에 미치는 영향과 이를 줄이기 위한 대처법', isCorrect: true },
        { no: 2, text: '야간 모드 필터의 원리와 액정 화면의 제작 공정', isCorrect: false, trapCode: 'D2' },
        { no: 3, text: '멜라토닌 호르몬의 분비 경로와 인체 대사 과정', isCorrect: false, trapCode: 'D2' },
        { no: 4, text: '스마트폰 사용 시간과 청소년 시력 저하의 관계', isCorrect: false, trapCode: 'D3' },
      ],
      explanation: '글 전체는 블루라이트의 수면 방해 영향과 스마트폰 멀리하기/필터 사용 등의 대처법을 다루고 있으므로 1번이 핵심입니다.',
    },

    // Stage 3 - Branch C (Foundation: from Stage 2 Easy)
    stage3_foundation: {
      id: 'CAT-S3-FND',
      level: 'easy',
      domain: '지문 내 인과 관계 직접 확인 (F)',
      kreadWeight: 680,
      passageSnippet: `겨울철 호수의 물은 표면부터 얼기 시작한다. 물은 4℃일 때 밀도가 가장 크기 때문에, 차가워진 표면 물이 아래로 내려가지 않고 얼음이 되어 위를 덮음으로써 물속 생명체들이 추위로부터 보호받을 수 있다.`,
      stem: '겨울에 호수의 물속 생명체들이 얼어 죽지 않고 살아남을 수 있는 이유는?',
      options: [
        { no: 1, text: '호수 바닥에 온천이 솟아나기 때문이다.', isCorrect: false, trapCode: 'D3' },
        { no: 2, text: '호수 표면의 얼음이 단열재 역할을 하여 아래 물을 덮어주기 때문이다.', isCorrect: true },
        { no: 3, text: '겨울에는 물고기들이 숨을 쉬지 않아도 되기 때문이다.', isCorrect: false, trapCode: 'D3' },
        { no: 4, text: '물은 0℃에서 가장 밀도가 커져 바닥으로 가라앉기 때문이다.', isCorrect: false, trapCode: 'D1' },
      ],
      explanation: '표면부터 얼어 위를 덮음으로써 물속을 보호한다는 본문의 인과 관계에 부합하는 것은 2번입니다.',
    },
  };

  // Adaptive test state
  const [currentStage, setCurrentStage] = useState<number>(1);
  const [currentItemKey, setCurrentItemKey] = useState<string>('stage1_medium');
  const [selectedOptionNo, setSelectedOptionNo] = useState<number | null>(null);
  const [answersHistory, setAnswersHistory] = useState<
    Array<{ key: string; isCorrect: boolean; kread: number; trap?: string }>
  >([]);
  const [testCompleted, setTestCompleted] = useState<boolean>(false);

  // Result metrics
  const [calculatedKread, setCalculatedKread] = useState<number>(850);
  const [detectedTrap, setDetectedTrap] = useState<string>('D1');
  const [prescribedSlot, setPrescribedSlot] = useState<string>('G5-EXP-I1-1');

  const currentItem = catPool[currentItemKey] || catPool.stage1_medium;

  const handleSelectOption = (no: number) => {
    setSelectedOptionNo(no);
  };

  const handleNextStep = () => {
    if (selectedOptionNo === null) return;

    const chosenOption = currentItem.options.find((o) => o.no === selectedOptionNo);
    const isCorrect = !!chosenOption?.isCorrect;
    const trap = chosenOption?.trapCode || 'D1';

    const newHistory = [
      ...answersHistory,
      {
        key: currentItemKey,
        isCorrect,
        kread: currentItem.kreadWeight,
        trap: isCorrect ? undefined : trap,
      },
    ];
    setAnswersHistory(newHistory);
    setSelectedOptionNo(null);

    // Adaptive Branching Logic
    if (currentStage === 1) {
      // Stage 1 -> Stage 2
      setCurrentStage(2);
      if (isCorrect) {
        setCurrentItemKey('stage2_hard');
      } else {
        setCurrentItemKey('stage2_easy');
      }
    } else if (currentStage === 2) {
      // Stage 2 -> Stage 3
      setCurrentStage(3);
      const stage1Correct = newHistory[0].isCorrect;
      if (stage1Correct && isCorrect) {
        setCurrentItemKey('stage3_master');
      } else if (!stage1Correct && !isCorrect) {
        setCurrentItemKey('stage3_foundation');
      } else {
        setCurrentItemKey('stage3_intermediate');
      }
    } else {
      // Test Completed -> Calculate Result
      const correctCount = newHistory.filter((h) => h.isCorrect).length;
      let finalKread = 850;
      let targetSlot = 'G5-EXP-I1-1';

      if (correctCount === 3) {
        finalKread = 1140;
        targetSlot = 'G5-EXP-E1-1'; // 심화 비판/평가
      } else if (correctCount === 2) {
        finalKread = 980;
        targetSlot = 'G5-EXP-S1-1'; // 구조 분석
      } else if (correctCount === 1) {
        finalKread = 820;
        targetSlot = 'G5-EXP-V1-1'; // 어휘 보강
      } else {
        finalKread = 690;
        targetSlot = 'G5-EXP-V1-1'; // 기초 재활
      }

      const lastTrap = newHistory.find((h) => !h.isCorrect)?.trap || 'D3';
      setCalculatedKread(finalKread);
      setDetectedTrap(lastTrap);
      setPrescribedSlot(targetSlot);
      setTestCompleted(true);
    }
  };

  const handleApplyPrescription = () => {
    setActiveSlotId(prescribedSlot);
    boostSmartScore(gradeData.grade_num, Math.floor(calculatedKread / 12));
    setStudentMode('clinic');
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-3 sm:p-5 overflow-y-auto">
      <div className="bg-white w-full max-w-2xl rounded-2xl shadow-2xl border border-slate-300 overflow-hidden my-auto flex flex-col">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 via-indigo-600 to-slate-900 text-white px-5 py-4 flex items-center justify-between border-b border-blue-400/30">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-white/10 backdrop-blur border border-white/20 flex items-center justify-center text-xl font-black">
              🎯
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h2 className="font-black text-base sm:text-lg">
                  ReadX-Ray CAT 온보딩 적응형 진단
                </h2>
                <span className="text-[10px] px-2 py-0.5 rounded-full bg-emerald-400 text-slate-950 font-black">
                  MODE 1 · ADAPTIVE CAT
                </span>
              </div>
              <p className="text-xs text-blue-150 text-indigo-100">
                3문항 적응형 실시간 분기로 학생의 정확한 KReaD 시작 지수와 취약 함정을 판정합니다.
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 text-white flex items-center justify-center text-sm font-bold transition cursor-pointer"
          >
            ✕
          </button>
        </div>

        {/* Body */}
        {!testCompleted ? (
          <div className="p-5 sm:p-6 space-y-4">
            {/* Progress Step Bar */}
            <div className="flex items-center justify-between text-xs pb-3 border-b border-slate-100">
              <div className="flex items-center gap-2">
                <span className="font-black text-indigo-700">문항 {currentStage} / 3</span>
                <span className="text-slate-400">·</span>
                <span className="font-bold text-slate-600">진단 영역: {currentItem.domain}</span>
              </div>
              <div className="flex items-center gap-1.5">
                {[1, 2, 3].map((step) => (
                  <div
                    key={step}
                    className={`w-6 h-6 rounded-full flex items-center justify-center text-[11px] font-black transition ${
                      currentStage === step
                        ? 'bg-indigo-600 text-white shadow-sm'
                        : currentStage > step
                        ? 'bg-emerald-500 text-white'
                        : 'bg-slate-200 text-slate-500'
                    }`}
                  >
                    {currentStage > step ? '✓' : step}
                  </div>
                ))}
              </div>
            </div>

            {/* Passage Snippet Box */}
            <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 text-slate-800 text-xs sm:text-sm leading-relaxed font-serif">
              <div className="text-[11px] font-sans font-bold text-slate-400 mb-1 flex items-center justify-between">
                <span>[진단 지문 텍스트]</span>
                <span className="font-mono text-indigo-600 font-bold">
                  난이도 가중치: KReaD {currentItem.kreadWeight}
                </span>
              </div>
              {currentItem.passageSnippet}
            </div>

            {/* Question Stem */}
            <div className="font-black text-sm text-slate-900 pt-1">
              Q{currentStage}. {currentItem.stem}
            </div>

            {/* Options List */}
            <div className="space-y-2 pt-1">
              {currentItem.options.map((opt) => (
                <button
                  key={opt.no}
                  onClick={() => handleSelectOption(opt.no)}
                  className={`w-full text-left p-3 rounded-xl border text-xs sm:text-sm transition flex items-center justify-between cursor-pointer ${
                    selectedOptionNo === opt.no
                      ? 'bg-indigo-50 border-indigo-600 text-indigo-950 font-black shadow-xs ring-2 ring-indigo-500/20'
                      : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-700 font-medium'
                  }`}
                >
                  <div className="flex items-center gap-2.5">
                    <span
                      className={`w-5 h-5 rounded-full flex items-center justify-center text-xs font-black ${
                        selectedOptionNo === opt.no
                          ? 'bg-indigo-600 text-white'
                          : 'bg-slate-200 text-slate-600'
                      }`}
                    >
                      {opt.no}
                    </span>
                    <span>{opt.text}</span>
                  </div>
                  {selectedOptionNo === opt.no && (
                    <span className="text-indigo-600 font-bold text-xs">선택됨</span>
                  )}
                </button>
              ))}
            </div>

            {/* Bottom Action */}
            <div className="pt-3 flex items-center justify-between border-t border-slate-100">
              <span className="text-[11px] text-slate-400">
                💡 응답 결과에 따라 다음 문항의 KReaD 난이도가 자동 조절됩니다.
              </span>
              <button
                disabled={selectedOptionNo === null}
                onClick={handleNextStep}
                className={`px-5 py-2.5 rounded-xl text-xs font-black transition shadow ${
                  selectedOptionNo !== null
                    ? 'bg-indigo-600 hover:bg-indigo-500 text-white cursor-pointer'
                    : 'bg-slate-200 text-slate-400 cursor-not-allowed'
                }`}
              >
                {currentStage === 3 ? '최종 진단 결과 판정 ➔' : '다음 적응형 문항으로 ➔'}
              </button>
            </div>
          </div>
        ) : (
          /* Test Complete Result View */
          <div className="p-6 space-y-5 animate-fade-in">
            <div className="text-center py-2">
              <div className="w-14 h-14 mx-auto rounded-2xl bg-gradient-to-tr from-emerald-400 to-indigo-600 flex items-center justify-center text-3xl shadow-lg mb-2">
                🎉
              </div>
              <h3 className="text-lg font-black text-slate-900">
                CAT 온보딩 문해력 적응형 진단 완료!
              </h3>
              <p className="text-xs text-slate-500 mt-0.5">
                3개 적응형 문항 반응 분석을 통해 학생의 시작 독서 레벨과 처방 슬롯이 도출되었습니다.
              </p>
            </div>

            {/* Key Metrics Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div className="p-3.5 rounded-xl bg-blue-50 border border-blue-200 text-center">
                <div className="text-[11px] font-bold text-blue-700">시작 KReaD 독서지수</div>
                <div className="text-2xl font-black text-blue-900 mt-1">
                  {calculatedKread}{' '}
                  <span className="text-xs font-normal text-blue-600">KReaD</span>
                </div>
                <div className="text-[10px] text-blue-700 font-bold mt-1">
                  {calculatedKread >= 1000
                    ? '동학년 상위 5% 최상위권'
                    : calculatedKread >= 850
                    ? '초등 5학년 적정 수준'
                    : '기초 보강 권장'}
                </div>
              </div>

              <div className="p-3.5 rounded-xl bg-rose-50 border border-rose-200 text-center">
                <div className="text-[11px] font-bold text-rose-700">핵심 방어 함정</div>
                <div className="text-2xl font-black text-rose-900 mt-1">{detectedTrap}</div>
                <div className="text-[10px] text-rose-700 font-bold mt-1">
                  {detectedTrap === 'D3'
                    ? '전제 왜곡 및 비약 주의'
                    : detectedTrap === 'D1'
                    ? '미세 사실 불일치 착오'
                    : '조건부 인과 혼동'}
                </div>
              </div>

              <div className="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200 text-center">
                <div className="text-[11px] font-bold text-emerald-700">처방 1차 추천 슬롯</div>
                <div className="text-xl font-black text-emerald-900 mt-1.5 font-mono">
                  {prescribedSlot}
                </div>
                <div className="text-[10px] text-emerald-700 font-bold mt-1">
                  1:1 맞춤형 클리닉 시작
                </div>
              </div>
            </div>

            {/* Prescribed Roadmap Action Box */}
            <div className="p-4 rounded-xl bg-slate-900 text-white text-xs space-y-2">
              <div className="font-black text-emerald-300 flex items-center justify-between">
                <span>🚀 원클릭 맞춤형 16차시 코스 자동 배정</span>
                <span className="text-[11px] text-slate-400">Dick & Carey 수행목표 연동</span>
              </div>
              <p className="text-slate-300 text-[11px] leading-relaxed">
                진단 결과에 따라 결손 위험이 있는 영역을 보강하기 위해{' '}
                <b className="text-white">[{prescribedSlot}]</b> 슬롯의 징검다리 클리닉으로 이동합니다.
                오답 백신 6종 및 TEI 상호작용 학습이 준비되어 있습니다.
              </p>
            </div>

            {/* Actions */}
            <div className="flex items-center justify-end gap-2 pt-2">
              <button
                onClick={onClose}
                className="px-4 py-2 rounded-xl text-xs font-bold text-slate-600 hover:bg-slate-100 cursor-pointer"
              >
                닫기
              </button>
              <button
                onClick={handleApplyPrescription}
                className="px-5 py-2 rounded-xl text-xs font-black bg-indigo-600 hover:bg-indigo-500 text-white shadow-md transition cursor-pointer"
              >
                맞춤형 클리닉으로 지금 시작하기 ➔
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
