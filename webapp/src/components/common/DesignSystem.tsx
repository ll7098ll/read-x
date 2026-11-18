import React, { useEffect, useRef } from "react";
import {
  X,
  ArrowUpRight,
  BookOpen,
  ScanLine,
  GitBranch,
  PenLine,
  Check,
} from "lucide-react";
import { ReadXBrand, ReadXSymbol } from "../brand/ReadXBrand";
import { READ_X_COLORS, READ_X_STEPS } from "../brand/readXSystem";

export function Dialog({
  title,
  onClose,
  children,
  wide = false,
}: {
  title: string;
  onClose: () => void;
  children: React.ReactNode;
  wide?: boolean;
}) {
  const ref = useRef<HTMLDialogElement>(null);
  useEffect(() => {
    const dialog = ref.current;
    const opener = document.activeElement instanceof HTMLElement ? document.activeElement : null;
    dialog?.showModal();
    return () => { dialog?.close(); if (opener?.isConnected) opener.focus(); };
  }, []);
  return (
    <dialog
      ref={ref}
      className={`rx-dialog ${wide ? "rx-dialog-wide" : ""}`}
      aria-label={title}
      onCancel={(event) => { event.preventDefault(); onClose(); }}
      onClick={(e) => {
        if (e.target === e.currentTarget) onClose();
      }}
    >
      <div className="rx-dialog-head">
        <h2>{title}</h2>
        <button className="rx-icon-button" onClick={onClose} aria-label="닫기">
          <X size={20} />
        </button>
      </div>
      <div className="rx-dialog-body">{children}</div>
    </dialog>
  );
}

export function PageHeading({
  eyebrow,
  title,
  description,
  action,
}: {
  eyebrow: string;
  title: string;
  description?: string;
  action?: React.ReactNode;
}) {
  return (
    <div className="rx-page-heading">
      <div>
        <p className="rx-eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        {description && <p className="rx-page-description">{description}</p>}
      </div>
      {action}
    </div>
  );
}

export function EmptyState({
  title,
  description,
  action,
}: {
  title: string;
  description: string;
  action?: React.ReactNode;
}) {
  return (
    <div className="rx-empty">
      <BookOpen size={30} strokeWidth={1.5} />
      <h3>{title}</h3>
      <p>{description}</p>
      {action}
    </div>
  );
}

export function ThinkingPath({ active = -1 }: { active?: number }) {
  return (
    <ol className="rx-thinking-path" aria-label="읽기 사고 과정">
      {[
        { Icon: ScanLine, text: "단서 찾기" },
        { Icon: GitBranch, text: "생각 연결" },
        { Icon: Check, text: "판단하기" },
        { Icon: PenLine, text: "내 말로 설명" },
      ].map(({ Icon, text }, i) => (
        <li key={text} className={active === i ? "is-active" : ""}>
          <span>
            <Icon size={17} />
          </span>
          <b>{text}</b>
          {i < 3 && <i aria-hidden="true">→</i>}
        </li>
      ))}
    </ol>
  );
}

export function BrandGuide({ onClose }: { onClose: () => void }) {
  return <Dialog title="Read X 브랜드 가이드" onClose={onClose} wide>
    <div className="rx-brand-guide-hero"><ReadXBrand dark/><h3>읽으라고 하기 전에,<br/>읽는 방법부터.</h3><p>Read X · 리드엑스 — 읽는 방법을 배우는 문해력 코스웨어</p></div>
    <section className="rx-guide-section"><p className="rx-eyebrow">01 · IDENTITY</p><h3>글과 생각이 만나는 X</h3><p>글의 단서와 나의 생각이 만나 이해가 되는 순간. 교차하는 두 획과 발견을 뜻하는 라임색으로 Read X의 학습 경험을 표현합니다.</p><div className="rx-logo-specimens"><ReadXSymbol/><ReadXBrand/><ReadXSymbol mono/></div></section>
    <section className="rx-guide-section"><p className="rx-eyebrow">02 · COLOR</p><h3>차분한 읽기, 선명한 다음 행동</h3><div className="rx-swatch-grid">{READ_X_COLORS.map(c=><div key={c.name}><span style={{background:c.hex}}/><b>{c.name}</b><code>{c.hex}</code><small>{c.meaning}</small></div>)}</div></section>
    <section className="rx-guide-section"><p className="rx-eyebrow">03 · EXPERIENCE</p><h3>처음에는 함께, 다음에는 스스로</h3><div className="rx-guide-principles">{READ_X_STEPS.map(s=><p key={s.title}><b>{s.title}</b>{s.description}</p>)}</div></section>
    <div className="rx-dialog-actions"><a className="rx-button rx-button-primary" href="#/brand" onClick={onClose}>전체 UI/UX 킷 열기 <ArrowUpRight size={16}/></a><a className="rx-button" href={`${import.meta.env.BASE_URL || '/'}brand/read-x-kit.zip`} download>CI · 테마 킷 다운로드</a></div>
    <p className="rx-fine-print">공식 표기는 Read X, 국문은 리드엑스입니다. 로고·색·글자·컴포넌트 상태·화면 설계의 기준은 전체 킷에서 확인할 수 있습니다.</p>
  </Dialog>;
}
