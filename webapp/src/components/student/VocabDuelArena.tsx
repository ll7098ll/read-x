import React, { useState, useEffect } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { speakKoreanText } from '../../utils/ttsEngine';
import type { VocabNote } from '../../types/courseware';

interface VocabDuelArenaProps {
  vocabList: VocabNote[];
  onClose: () => void;
}

interface DuelQuestion {
  word: string;
  tier: string;
  definition: string;
  options: string[];
  correctOption: string;
}

export const VocabDuelArena: React.FC<VocabDuelArenaProps> = ({
  vocabList,
  onClose,
}) => {
  const { boostSmartScore, activeGradeIdx } = useCoursewareStore();
  const gradeNum = activeGradeIdx + 1;

  // Generate 5 rapid questions from vocab list
  const [questions, setQuestions] = useState<DuelQuestion[]>([]);
  const [currentQIdx, setCurrentQIdx] = useState<number>(0);
  const [timeLeft, setTimeLeft] = useState<number>(10);
  const [studentScore, setStudentScore] = useState<number>(0);
  const [aiScore, setAiScore] = useState<number>(0);
  const [combo, setCombo] = useState<number>(0);
  const [isGameOver, setIsGameOver] = useState<boolean>(false);
  const [feedback, setFeedback] = useState<{ isCorrect: boolean; text: string } | null>(null);

  // Fallback vocabulary pool if list is small
  const defaultPool: VocabNote[] = [
    { word: '알베도', tier: 'Tier 3 (교과개념)', desc: '지표면이나 물체가 태양빛을 반사하는 비율' },
    { word: '복사 평형', tier: 'Tier 3 (교과개념)', desc: '지구가 흡수하는 태양 복사열과 방출하는 지구 복사열이 같은 상태' },
    { word: '기공', tier: 'Tier 3 (교과개념)', desc: '식물 잎 뒷면에서 수증기와 공기가 드나드는 통로' },
    { word: '증산 작용', tier: 'Tier 3 (교과개념)', desc: '식물체 안의 물이 잎의 기공을 통해 기체 상태로 증발하는 현상' },
    { word: '탄력성', tier: 'Tier 2 (사고어휘)', desc: '가격이나 환경 변화에 따라 수요나 공급이 반응하는 민감도' },
    { word: '가산혼합', tier: 'Tier 3 (교과개념)', desc: '빛의 삼원색(빨강, 초록, 파랑)을 섞을수록 밝아지는 혼합 방식' },
  ];

  const pool = vocabList.length >= 4 ? vocabList : defaultPool;

  useEffect(() => {
    // Build 5 randomized questions
    const generated: DuelQuestion[] = pool.slice(0, 5).map((v, idx) => {
      // Pick 3 distractors
      const otherWords = pool.filter((o) => o.word !== v.word).map((o) => o.word);
      const distractors = otherWords.slice(0, 3);
      while (distractors.length < 3) {
        distractors.push(`개념어-${distractors.length + 1}`);
      }
      const shuffledOptions = [v.word, ...distractors].sort(() => Math.random() - 0.5);

      return {
        word: v.word,
        tier: v.tier,
        definition: v.desc,
        options: shuffledOptions,
        correctOption: v.word,
      };
    });

    setQuestions(generated);
    setCurrentQIdx(0);
    setTimeLeft(10);
    setStudentScore(0);
    setAiScore(0);
    setCombo(0);
    setIsGameOver(false);
  }, [vocabList]);

  // 10s Timer Loop
  useEffect(() => {
    if (isGameOver || questions.length === 0) return;

    if (timeLeft <= 0) {
      handleAnswer(''); // Timeout treated as wrong
      return;
    }

    const timer = setInterval(() => {
      setTimeLeft((prev) => prev - 1);
    }, 1000);

    return () => clearInterval(timer);
  }, [timeLeft, isGameOver, currentQIdx, questions.length]);

  const currentQ = questions[currentQIdx];

  const handleAnswer = (pickedWord: string) => {
    if (!currentQ || isGameOver) return;

    const isCorrect = pickedWord === currentQ.correctOption;
    // AI has 75% random chance to be correct
    const aiCorrect = Math.random() < 0.75;

    if (isCorrect) {
      const addedPoints = 100 + combo * 20;
      setStudentScore((prev) => prev + addedPoints);
      setCombo((prev) => prev + 1);
      setFeedback({ isCorrect: true, text: `🎉 정답! +${addedPoints}점 (콤보 x${combo + 1})` });
    } else {
      setCombo(0);
      setFeedback({ isCorrect: false, text: `⚠️ 땡! 정답은 [${currentQ.correctOption}] 입니다.` });
    }

    if (aiCorrect) {
      setAiScore((prev) => prev + 90);
    }

    // Delay before next question
    setTimeout(() => {
      setFeedback(null);
      if (currentQIdx + 1 < questions.length) {
        setCurrentQIdx((prev) => prev + 1);
        setTimeLeft(10);
      } else {
        setIsGameOver(true);
        if (studentScore >= aiScore) {
          boostSmartScore(gradeNum, 10);
        }
      }
    }, 1200);
  };

  return (
    <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4 animate-in fade-in">
      <div className="bg-slate-900 border-2 border-amber-500 rounded-3xl max-w-xl w-full p-6 text-white shadow-2xl relative overflow-hidden">
        {/* Top Header */}
        <div className="flex items-center justify-between pb-4 border-b border-slate-800">
          <div className="flex items-center gap-2">
            <span className="w-8 h-8 rounded-xl bg-amber-500 text-slate-950 flex items-center justify-center font-black text-sm">
              ⚡
            </span>
            <div>
              <h3 className="font-black text-base text-amber-300">
                온디바이스 10초 어휘 듀얼 (Vocab Duel Arena)
              </h3>
              <p className="text-[11px] text-slate-400">
                AI 라이벌 '리디봇'과 펼치는 10초 스피드 교과 개념어 배틀
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white text-lg font-bold p-1 cursor-pointer"
          >
            ✕
          </button>
        </div>

        {/* Score Board vs AI */}
        <div className="grid grid-cols-2 gap-3 my-4">
          <div className="p-3 rounded-2xl bg-blue-950/70 border border-blue-500/50 text-center">
            <div className="text-xs font-bold text-blue-300">👦 나 (도전자)</div>
            <div className="text-2xl font-black font-mono text-blue-400">{studentScore}점</div>
            {combo > 1 && (
              <span className="text-[10px] bg-amber-500 text-slate-950 font-black px-1.5 py-0.5 rounded-full">
                🔥 {combo} COMBO
              </span>
            )}
          </div>

          <div className="p-3 rounded-2xl bg-rose-950/70 border border-rose-500/50 text-center">
            <div className="text-xs font-bold text-rose-300">🤖 AI 라이벌 (리디봇)</div>
            <div className="text-2xl font-black font-mono text-rose-400">{aiScore}점</div>
            <span className="text-[10px] text-slate-400 font-bold">정답률 75% 인공지능</span>
          </div>
        </div>

        {!isGameOver ? (
          currentQ && (
            <div className="space-y-4">
              {/* Question & Timer Bar */}
              <div className="space-y-2">
                <div className="flex items-center justify-between text-xs font-bold">
                  <span className="text-amber-400">
                    라운드 {currentQIdx + 1} / {questions.length}
                  </span>
                  <span
                    className={`font-mono text-sm font-black px-2 py-0.5 rounded-md ${
                      timeLeft <= 3 ? 'bg-rose-600 text-white animate-ping' : 'bg-slate-800 text-amber-300'
                    }`}
                  >
                    ⏱️ {timeLeft}초
                  </span>
                </div>
                {/* Timer Progress Bar */}
                <div className="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                  <div
                    className={`h-full transition-all duration-1000 ${
                      timeLeft <= 3 ? 'bg-rose-500' : 'bg-amber-400'
                    }`}
                    style={{ width: `${(timeLeft / 10) * 100}%` }}
                  />
                </div>
              </div>

              {/* Definition Prompt Box */}
              <div className="p-4 rounded-2xl bg-slate-800/90 border border-slate-700 text-center space-y-1">
                <span className="text-[11px] font-bold px-2 py-0.5 rounded bg-blue-900/60 text-blue-300">
                  {currentQ.tier}
                </span>
                <p className="text-sm font-bold text-slate-100 pt-2 leading-relaxed">
                  "{currentQ.definition}"
                </p>
                <button
                  onClick={() => speakKoreanText(currentQ.definition, 1.0)}
                  className="text-[11px] text-amber-300 underline pt-1"
                >
                  🔊 문제 음성 듣기
                </button>
              </div>

              {/* Options 4 Grid */}
              <div className="grid grid-cols-2 gap-2.5">
                {currentQ.options.map((opt, oIdx) => (
                  <button
                    key={oIdx}
                    onClick={() => handleAnswer(opt)}
                    className="p-3.5 rounded-xl bg-slate-800 hover:bg-amber-500 hover:text-slate-950 border border-slate-700 text-sm font-black transition-all active:scale-95 cursor-pointer shadow-sm"
                  >
                    {opt}
                  </button>
                ))}
              </div>

              {/* Instant Feedback Pill */}
              {feedback && (
                <div
                  className={`p-2.5 rounded-xl text-center text-xs font-bold animate-in fade-in ${
                    feedback.isCorrect
                      ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500'
                      : 'bg-rose-500/20 text-rose-300 border border-rose-500'
                  }`}
                >
                  {feedback.text}
                </div>
              )}
            </div>
          )
        ) : (
          /* Game Over Result Screen */
          <div className="text-center py-6 space-y-4 animate-in zoom-in-95">
            <div className="text-4xl">
              {studentScore >= aiScore ? '🏆' : '💪'}
            </div>
            <h4 className="text-xl font-black text-amber-300">
              {studentScore >= aiScore
                ? '축하합니다! AI 라이벌에게 승리했습니다!'
                : '아쉽네요! 다음 번엔 반드시 이겨보세요!'}
            </h4>
            <p className="text-xs text-slate-300">
              최종 스코어: <b>{studentScore}점</b> vs AI <b>{aiScore}점</b>
              {studentScore >= aiScore && ' (보상: SmartScore +10점 획득 🎉)'}
            </p>
            <div className="flex justify-center gap-3 pt-2">
              <button
                onClick={() => {
                  setCurrentQIdx(0);
                  setTimeLeft(10);
                  setStudentScore(0);
                  setAiScore(0);
                  setCombo(0);
                  setIsGameOver(false);
                }}
                className="px-5 py-2.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs cursor-pointer shadow-md"
              >
                다시 대결하기 🔄
              </button>
              <button
                onClick={onClose}
                className="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs cursor-pointer"
              >
                닫기 ✕
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
