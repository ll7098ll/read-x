import React, { useState } from 'react';

/** Presentation preferences shared by practice and assigned lessons. */
export function ReadingDisplay({ children }: { children: React.ReactNode }) {
  const [large, setLarge] = useState(false);
  return <div className="reading-display" data-text-size={large ? 'large' : 'normal'}>
    <div className="reading-display-tools" role="group" aria-label="본문 글자 크기">
      <span>편안하게 읽기</span>
      <button type="button" aria-pressed={!large} onClick={() => setLarge(false)}>기본 글씨</button>
      <button type="button" aria-pressed={large} onClick={() => setLarge(true)}>큰 글씨</button>
    </div>
    {children}
  </div>;
}
