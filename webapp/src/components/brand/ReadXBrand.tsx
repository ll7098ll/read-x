import React from 'react';

/** Read X: text and thought cross to become understanding. */
export function ReadXSymbol({ className = '', mono = false }: { className?: string; mono?: boolean }) {
  return <svg className={className} viewBox="0 0 64 64" fill="none" aria-hidden="true">
    <rect width="64" height="64" rx="16" fill={mono ? 'currentColor' : '#DDF58A'}/>
    <path d="M19 18L45 46" stroke={mono ? 'white' : '#202D40'} strokeWidth="8" strokeLinecap="round"/>
    <path d="M45 18L19 46" stroke={mono ? 'currentColor' : '#DDF58A'} strokeWidth="14" strokeLinecap="round"/>
    <path d="M45 18L19 46" stroke={mono ? 'white' : '#3157D5'} strokeWidth="8" strokeLinecap="round"/>
  </svg>;
}

export function ReadXBrand({ dark = false, compact = false }: { dark?: boolean; compact?: boolean }) {
  return <span className={`rx-brand ${dark ? 'rx-brand-dark' : ''} ${compact ? 'rx-brand-compact' : ''}`} aria-label="Read X 리드엑스">
    <ReadXSymbol className="rx-brand-symbol"/>
    <span className="rx-wordmark">Read<span className="rx-wordmark-x"> X</span></span>
  </span>;
}
