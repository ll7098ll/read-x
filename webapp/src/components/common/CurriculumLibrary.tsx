import React, { useEffect, useState } from "react";
import { ArrowLeft, ArrowRight, Search, ExternalLink } from "lucide-react";
import { LearningIllustration } from "../brand/LearningIllustration";
import { ReadingLevelReview } from "./ReadingLevelReview";
import { CorpusReadingStudio } from "../student/CorpusReadingStudio";
import { corpusLessonByPassage } from "../../data/corpusReading";
import { assessPassage, readingLevelLabels, type ReadingLevel } from "../../data/readingPolicy";
import {
  usePracticeState,
  useReadingStorageStatus,
} from "../../store/useReadingWorkspace";

export interface CatalogPassage {
  id: string;
  version: number;
  title: string;
  grade: number;
  semester?: number;
  subject: string;
  conceptNames: string[];
  goalIds: string[];
  paragraphs: string[];
  origin: string;
  purpose: string;
  pairId?: string;
  goalName?: string;
  reviewState: string;
  table?: { caption: string; headers: string[]; rows: (string | number)[][] };
  teacherThinkingModel?: { evidenceQuote: string; reasoning: string };
  independentCheck?: {
    prompt: string;
    expectedAnswer: string;
    evidenceQuote: string;
  };
  writingPrompt?: string;
  diagnostic?: { items: unknown[] };
  revisedLessonId?: string;
  readingVariants?: Record<ReadingLevel,string[]>;
}
export const catalogSubjects = [
  "국어",
  "수학",
  "사회",
  "과학",
  "통합",
  "슬기로운 생활",
  "실과",
  "음악",
  "체육",
  "도덕",
];
export function subjectLabels(subject: string) {
  return catalogSubjects.filter((s) => subject.includes(s));
}
export function filterCatalog(
  passages: CatalogPassage[],
  query: string,
  grade: string,
  subject: string,
  collection: string,
) {
  const needle = query.trim().toLocaleLowerCase();
  return passages.filter(
    (p) =>
      (!grade || p.grade === +grade) &&
      (!subject || subjectLabels(p.subject).includes(subject)) &&
      (collection !== "new" || p.origin === "신규 집필") &&
      (collection !== "activity" || !!p.diagnostic) &&
      (!needle ||
        [p.title, p.subject, ...p.conceptNames, ...p.goalIds, ...p.paragraphs]
          .join(" ")
          .toLocaleLowerCase()
          .includes(needle)),
  );
}
const base = "./curriculum/";

function PassageView({
  passage: p,
  pair,
  onBack,
  onPair,
  onWorkshop,
}: {
  passage: CatalogPassage;
  pair?: CatalogPassage;
  onBack: () => void;
  onPair: () => void;
  onWorkshop: () => void;
}) {
  const [answer, setAnswer] = usePracticeState(
    p.id,
    `catalog-answer-v${p.version}`,
    "",
  );
  const [evidence, setEvidence] = usePracticeState(
    p.id,
    `catalog-evidence-v${p.version}`,
    "",
  );
  const [writing, setWriting] = usePracticeState(
    p.id,
    `catalog-writing-v${p.version}`,
    "",
  );
  const [modelSeen, setModelSeen] = usePracticeState(
    p.id,
    `catalog-model-seen-v${p.version}`,
    false,
  );
  const failed = useReadingStorageStatus((s) => s.failed);
  return (
    <section>
      <div className="rx-catalog-toolbar">
        <button className="rx-button" onClick={onBack}>
          <ArrowLeft size={17} /> 지문 목록
        </button>
        <span className="rx-badge">
          검토용 초안 · {p.grade}학년 {p.semester ? `${p.semester}학기` : ""}
        </span>
      </div>
      <div className="rx-catalog-reading">
        <article className="rx-catalog-paper">
          <p className="rx-eyebrow">
            {p.subject} · {p.conceptNames.join(" · ")}
          </p>
          <h2>{p.title}</h2>
          {p.paragraphs.map((text, i) => (
            <p className="rx-catalog-paragraph" key={i}>
              <small>{String(i + 1).padStart(2, "0")}</small>
              {text.replace(/<[^>]*>/g, "")}
            </p>
          ))}
          {p.table && (
            <div className="rx-table-scroll">
              <table>
                <caption>{p.table.caption}</caption>
                <thead>
                  <tr>
                    {p.table.headers.map((h, i) => (
                      <th key={i}>{h}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {p.table.rows.map((r, i) => (
                    <tr key={i}>
                      {r.map((v, j) => (
                        <td key={j}>{v}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </article>
        <aside className="rx-catalog-activities">
          <div className="rx-catalog-goal">
            <LearningIllustration kind="target" />
            <div>
              <p className="rx-eyebrow">이 글에서 연습할 읽기</p>
              <h3>{p.goalName || "본문의 근거를 찾아 설명하기"}</h3>
              <p>{p.goalIds.join(" · ")}</p>
            </div>
          </div>
          {p.diagnostic ? (
            <>
              <h3>읽기 사고 과정을 함께 따라가요</h3>
              <p>
                혼자 쓴 답과 근거를 먼저 남기고, 생각 시범과 단계별 힌트를
                살펴보세요. 짝 지문에서 새로 적용한 기록도 구분해 보관합니다.
              </p>
              <button
                className="rx-button rx-button-primary"
                onClick={onWorkshop}
              >
                진단·사고 과정 활동 열기 <ArrowRight size={17} />
              </button>
              <p className="rx-fine-print">
                {p.diagnostic.items.length}개 관찰 문항 · 교사 검토용 체험
              </p>
            </>
          ) : p.independentCheck ? (
            <>
              <h3>{p.independentCheck.prompt}</h3>
              <label className="rx-field">
                내가 생각한 답
                <textarea
                  value={answer}
                  onChange={(e) => setAnswer(e.target.value)}
                  rows={3}
                />
              </label>
              <label className="rx-field">
                본문에서 찾은 근거
                <textarea
                  value={evidence}
                  onChange={(e) => setEvidence(e.target.value)}
                  rows={3}
                />
              </label>
              {p.teacherThinkingModel && (
                <details
                  onToggle={(e) => {
                    if (e.currentTarget.open) setModelSeen(true);
                  }}
                >
                  <summary>생각하는 방법 살펴보기</summary>
                  <blockquote>
                    {p.teacherThinkingModel.evidenceQuote}
                  </blockquote>
                  <p>{p.teacherThinkingModel.reasoning}</p>
                  <p className="rx-fine-print">
                    시범을 열어 본 이후의 연습입니다.
                  </p>
                </details>
              )}
              <h3>내 말로 정리하기</h3>
              <p>{p.writingPrompt}</p>
              <label className="rx-field">
                나의 설명
                <textarea
                  value={writing}
                  onChange={(e) => setWriting(e.target.value)}
                  rows={4}
                />
              </label>
              <p className="rx-fine-print" role="status">
                {failed
                  ? "이 브라우저에서 저장할 수 없습니다. 작성한 내용을 따로 복사해 주세요."
                  : "응답은 이 브라우저에 자동 보관됩니다."}{" "}
                {modelSeen
                  ? "생각 시범 열람 이력이 있습니다."
                  : "자동 채점은 하지 않습니다."}
              </p>
            </>
          ) : (
            <p>
              기존 수업 자료의 본문입니다. 수업 자료 메뉴에서 해당 목표의 활동을
              확인할 수 있습니다.
            </p>
          )}
          {pair && (
            <button className="rx-button rx-catalog-pair" onClick={onPair}>
              <LearningIllustration kind="transfer" />
              <span>
                같은 목표, 다른 글<br />
                <b>{pair.title}</b>
              </span>
              <ArrowRight size={18} />
            </button>
          )}
        </aside>
      </div>
    </section>
  );
}

export function CurriculumLibrary() {
  const [passages, setPassages] = useState<CatalogPassage[]>([]),
    [error, setError] = useState("");
  const [query, setQuery] = useState(""),
    [grade, setGrade] = useState(""),
    [subject, setSubject] = useState(""),
    [collection, setCollection] = useState("all");
  const [selected, setSelected] = useState<string | null>(null),
    [frame, setFrame] = useState<{ url: string; title: string } | null>(null);
  const [retry, setRetry] = useState(0);
  const [readingLevel, setReadingLevel] = useState<ReadingLevel>("standard");
  useEffect(() => {
    const controller = new AbortController();
    setError("");
    fetch(`${base}passages.json`, { signal: controller.signal })
      .then((r) => {
        if (!r.ok) throw new Error();
        return r.json();
      })
      .then((data) => {
        if (!Array.isArray(data.passages)) throw new Error();
        setPassages(data.passages);
      })
      .catch((e) => {
        if (e.name !== "AbortError")
          setError("자료를 불러오지 못했습니다. 다시 시도해 주세요.");
      });
    return () => controller.abort();
  }, [retry]);
  const p = passages.find((x) => x.id === selected),
    pair = p?.pairId
      ? passages.find((x) => x.pairId === p.pairId && x.id !== p.id)
      : undefined;
  const filtered = filterCatalog(passages, query, grade, subject, collection);
  const readingPassages = passages.map(p=>({...p,paragraphs:p.readingVariants?.[readingLevel] || p.paragraphs}));
  const revisedLesson = p ? corpusLessonByPassage.get(p.id) : undefined;
  if (p && revisedLesson && !frame) return <CorpusReadingStudio key={p.id} lesson={revisedLesson} initialLevel={readingLevel} onBack={()=>setSelected(null)}/>;
  if (frame)
    return (
      <section className="rx-catalog-embedded">
        <div className="rx-catalog-toolbar">
          <button className="rx-button" onClick={() => setFrame(null)}>
            <ArrowLeft size={17} /> 자료실로 돌아가기
          </button>
          <a
            className="rx-text-link"
            href={frame.url}
            target="_blank"
            rel="noreferrer"
          >
            새 창에서 보기 <ExternalLink size={16} />
          </a>
        </div>
        <iframe title={frame.title} src={frame.url} />
      </section>
    );
  if (p)
    return (
      <PassageView
        key={p.id}
        passage={p}
        pair={pair}
        onBack={() => setSelected(null)}
        onPair={() => setSelected(pair?.id || null)}
        onWorkshop={() =>
          setFrame({
            url: `${base}reading-workshop.html#${encodeURIComponent(p.id)}`,
            title: "교과 읽기 진단과 사고 과정 활동",
          })
        }
      />
    );
  return (
    <section className="rx-catalog">
      <header className="rx-catalog-banner">
        <LearningIllustration kind="library" />
        <div>
          <p className="rx-eyebrow">READX CURRICULUM LIBRARY</p>
          <h2>교과의 개념이, 읽기의 재료로.</h2>
          <p>
            학년과 교과를 골라 글을 만나고, 같은 읽기 목표를 다른 글에 적용해
            보세요.
          </p>
        </div>
        <button
          className="rx-button"
          onClick={() =>
            setFrame({
              url: `${base}curriculum-library.html`,
              title: "교과 개념 지도와 교육과정 원장",
            })
          }
        >
          개념·교육과정 원장 <ArrowRight size={17} />
        </button>
      </header>
      <div className="rx-catalog-counts">
        <span>
          <b>{passages.length || "—"}</b> 전체 지문
        </span>
        <span>
          <b>
            {passages.filter((p) => p.revisedLessonId).length || "—"}
          </b>{" "}
          개정 지문
        </span>
        <span>
          <b>
            {passages.reduce(
              (n, p) => n + (p.diagnostic?.items.length || 0),
              0,
            ) || "—"}
          </b>{" "}
          사고 과정 문항
        </span>
        <p>교사 검수·학생 난도 보정 전의 체험 자료입니다.</p>
      </div>
      <div className="rx-catalog-filters">
        <label className="rx-catalog-search">
          <Search size={18} />
          <input
            aria-label="지문 검색"
            placeholder="제목, 교과 개념, 본문, 목표 검색"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
        </label>
        <select
          aria-label="자료 학년"
          value={grade}
          onChange={(e) => setGrade(e.target.value)}
        >
          <option value="">모든 학년</option>
          {[1, 2, 3, 4, 5, 6].map((g) => (
            <option key={g} value={g}>
              {g}학년
            </option>
          ))}
        </select>
        <select
          aria-label="자료 교과"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        >
          <option value="">모든 교과</option>
          {[...new Set(passages.flatMap((p) => subjectLabels(p.subject)))]
            .sort()
            .map((s) => (
              <option key={s}>{s}</option>
            ))}
        </select>
        <select
          aria-label="자료 구성"
          value={collection}
          onChange={(e) => setCollection(e.target.value)}
        >
          <option value="all">전체 지문</option>
          <option value="new">신규 집필 48편</option>
          <option value="activity">단계별 읽기 활동 포함</option>
        </select>
      </div>
      <ReadingLevelReview passages={readingPassages} grade={grade} level={readingLevel} onLevel={setReadingLevel} />
      {error ? (
        <div role="alert">
          <p>{error}</p>
          <button className="rx-button" onClick={() => setRetry((x) => x + 1)}>
            다시 불러오기
          </button>
        </div>
      ) : (
        <p className="rx-catalog-result" role="status">
          {passages.length
            ? `${filtered.length}편의 글을 찾았어요.`
            : "자료를 불러오고 있어요."}
        </p>
      )}
      <div className="rx-catalog-grid">
        {filtered.map((original) => {const p={...original,paragraphs:original.readingVariants?.[readingLevel] || original.paragraphs};return (
          <button
            className="rx-catalog-card"
            key={p.id}
            onClick={() => setSelected(p.id)}
          >
            <div className="rx-catalog-card-top">
              <LearningIllustration
                kind={
                  p.subject.includes("과학")
                    ? "search"
                    : p.subject.includes("수학")
                      ? "target"
                      : p.subject.includes("사회")
                        ? "transfer"
                        : "book"
                }
              />
              <span>
                {p.grade}학년 ·{" "}
                {subjectLabels(p.subject).join(" · ") || p.subject}
              </span>
            </div>
            <h3>{p.title}</h3>
            <p>{p.conceptNames.join(" · ")}</p>
            <p className="rx-passage-assessment">{assessPassage(p.paragraphs, p.grade, readingLevel).chars}자 · {p.paragraphs.length}문단 · {readingLevelLabels[readingLevel]} 대비 {assessPassage(p.paragraphs, p.grade, readingLevel).lengthLabel}</p>
            <div className="rx-catalog-card-foot">
              <span>
                {p.diagnostic
                  ? "시범 · 함께 · 스스로 읽기"
                  : p.origin === "신규 집필"
                    ? "읽기 · 자기 설명 활동"
                    : "기존 읽기 자료"}
              </span>
              <ArrowRight size={17} />
            </div>
          </button>
        );})}
      </div>
      {!error && passages.length > 0 && !filtered.length && (
        <p className="rx-empty">
          검색 조건에 맞는 글이 없어요. 다른 낱말이나 학년을 골라 보세요.
        </p>
      )}
    </section>
  );
}
