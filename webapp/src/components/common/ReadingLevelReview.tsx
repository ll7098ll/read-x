import React from "react";
import { assessPassage, passageMetrics, readingPolicy, readingLevels, readingLevelLabels, type ReadingLevel } from "../../data/readingPolicy";

export function ReadingLevelReview({ passages, grade, level, onLevel }: {
  passages: { grade: number; paragraphs: string[] }[]; grade: string; level: ReadingLevel; onLevel: (l: ReadingLevel) => void;
}) {
  return <details className="rx-reading-review" open>
    <summary>학년·수준별 분량과 어휘 검토</summary>
    <p>설명문 편집용 제안 기준입니다. 글자 수만으로 읽기 수준을 판정하지 않아요. 개정 지문은 수준을 고르면 실제 본문과 분량이 바뀝니다. 교사 검토와 학생의 읽기 결과로 난도를 보정합니다.</p>
    <div className="lj-reader-modes">{readingLevels.map(l => <button key={l} aria-pressed={level === l} onClick={() => onLevel(l)}>{readingLevelLabels[l]} 기준으로 살피기</button>)}</div>
    <div className="rx-table-scroll"><table><thead><tr><th>학년</th><th>현재 중앙값</th><th>{readingLevelLabels[level]} 목표 분량</th><th>보강 검토</th><th>어휘·문장 조절</th></tr></thead><tbody>
      {readingPolicy.filter(p => !grade || p.grade === +grade).map(p => {
        const rows = passages.filter(x => x.grade === p.grade);
        const lengths = rows.map(x => passageMetrics(x.paragraphs).chars).sort((a, b) => a - b);
        const mid = Math.floor(lengths.length / 2);
        const median = lengths.length ? (lengths.length % 2 ? lengths[mid] : (lengths[mid - 1] + lengths[mid]) / 2) : 0;
        const [min, max] = p.ranges[readingLevels.indexOf(level)];
        return <tr key={p.grade}><th>{p.grade}학년</th><td>{lengths.length ? `${Math.round(median).toLocaleString()}자` : "—"}</td><td>{min.toLocaleString()}~{max.toLocaleString()}자</td><td>{rows.filter(x => assessPassage(x.paragraphs, p.grade, level).lengthLabel === "분량 보강 검토").length} / {rows.length}편</td><td>{p.vocabulary}<small>{p.concepts} · 문장당 평균 {p.sentenceWords.join("~")}어절을 출발점으로 검토</small></td></tr>;
      })}
    </tbody></table></div>
    <p>공백 포함·본문만 계산(제목·표 제외). 도움글은 개념을 유지하며 문장을 나누고 쉬운 예를 붙입니다. 도전글은 비교·조건·반례를 더합니다. 낯선 어휘·배경지식·문단 연결의 부담은 교사 검토와 학생의 실제 읽기로 확인합니다.</p>
  </details>;
}
