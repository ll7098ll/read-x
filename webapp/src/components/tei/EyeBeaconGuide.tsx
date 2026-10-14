import React, { useState, useEffect } from 'react';

interface EyeBeaconGuideProps {
  isActive: boolean;
  totalParagraphs: number;
  currentParaIdx: number;
  onParaChange?: (nextIdx: number) => void;
}

export const EyeBeaconGuide: React.FC<EyeBeaconGuideProps> = ({
  isActive,
  totalParagraphs,
  currentParaIdx,
  onParaChange,
}) => {
  const [isPlaying, setIsPlaying] = useState<boolean>(true);
  const [speed, setSpeed] = useState<'slow' | 'normal' | 'fast'>('normal');

  const intervalMs = speed === 'slow' ? 12000 : speed === 'fast' ? 5000 : 8000;

  useEffect(() => {
    if (!isActive || !isPlaying) return;

    const timer = setInterval(() => {
      onParaChange?.((currentParaIdx + 1) % totalParagraphs);
    }, intervalMs);

    return () => clearInterval(timer);
  }, [isActive, isPlaying, speed, currentParaIdx, totalParagraphs, onParaChange, intervalMs]);

  if (!isActive) return null;

  return (
    <div className="eye-beacon-guide-pill flex items-center gap-2 p-1.5 px-3 bg-amber-500/10 border border-amber-400/50 rounded-xl text-xs text-amber-950 font-bold backdrop-blur-xs shadow-xs animate-in fade-in">
      <div className="flex items-center gap-1.5">
        <span className="relative flex h-3 w-3">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
          <span className="relative inline-flex rounded-full h-3 w-3 bg-amber-500"></span>
        </span>
        <span>💡 시선 유도 비콘 작동 중</span>
      </div>

      <div className="flex items-center gap-1.5 pl-2 border-l border-amber-300">
        <button
          onClick={() => setIsPlaying(!isPlaying)}
          className="hover:text-amber-800 cursor-pointer"
        >
          {isPlaying ? '일시정지 ⏸' : '재생 ▶'}
        </button>

        <span className="text-slate-300">|</span>

        <select
          value={speed}
          onChange={(e) => setSpeed(e.target.value as 'slow' | 'normal' | 'fast')}
          className="bg-transparent text-[11px] font-bold outline-none cursor-pointer"
        >
          <option value="slow">느린 속도 (초저 권장)</option>
          <option value="normal">보통 속도</option>
          <option value="fast">빠른 속도 (초고 권장)</option>
        </select>
      </div>
    </div>
  );
};
