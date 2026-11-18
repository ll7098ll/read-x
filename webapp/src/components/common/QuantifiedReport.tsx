import React, { useState } from "react";
import { Download, BarChart3, ClipboardCheck, Info } from "lucide-react";
import {
  demoStudents,
  demoClasses,
  type DemoStudent,
} from "../../data/demoAcademy";
import {
  demoReportRecords,
  reportPeriods,
  reportWeeks,
} from "../../data/demoReportRecords";
import { useDemoAcademy } from "../../store/useDemoAcademy";
import {
  percentText,
  reportCsv,
  rubricCriteria,
  summarizeReport,
  type ReportSummary,
  type Ratio,
} from "../../services/reportMetrics";

export function MetricCards({
  summary: s,
  previous,
}: {
  summary: ReportSummary;
  previous?: ReportSummary;
}) {
  const metrics: {
    key:
      | "completion"
      | "answer"
      | "evidence"
      | "help"
      | "independent"
      | "transfer";
    label: string;
    unit: string;
    definition: string;
  }[] = [
    {
      key: "completion",
      label: "활동 제출률",
      unit: "활동",
      definition: "제출 활동 ÷ 배정 활동",
    },
    {
      key: "answer",
      label: "첫 선택 정답률",
      unit: "문항",
      definition: "첫 선택 정답 ÷ 선택형 제출 문항",
    },
    {
      key: "evidence",
      label: "첫 근거 일치율",
      unit: "응답",
      definition: "기준 근거와 일치 ÷ 근거 평가 응답",
    },
    {
      key: "help",
      label: "도움 사용률",
      unit: "활동",
      definition: "첫 제출 전 도움 사용 ÷ 제출 활동",
    },
    {
      key: "independent",
      label: "독립 응답률",
      unit: "응답",
      definition: "독립 조건·도움 0회 ÷ 제출 활동",
    },
    {
      key: "transfer",
      label: "새 글 적용 확인율",
      unit: "응답",
      definition: "교사 수행 확인 ÷ 새 글·독립 첫 응답 중 검토 완료",
    },
  ];
  return (
    <div className="qr-metrics">
      {metrics.map((m) => {
        const r = s[m.key],
          prev = previous?.[m.key],
          delta =
            prev?.percent != null && r.percent != null
              ? Math.round(
                  (r.numerator / r.denominator -
                    prev.numerator / prev.denominator) *
                    1000,
                ) / 10
              : null;
        return (
          <article key={m.key} className={`qr-metric qr-${m.key}`}>
            <div className="qr-metric-label">
              {m.label}
              <span>
                {m.key === "transfer"
                  ? "교사 확인"
                  : m.key === "answer" || m.key === "evidence"
                    ? "기준 대조"
                    : "행동 기록"}
              </span>
            </div>
            <strong>{percentText(r)}</strong>
            <p className="qr-fraction">
              {r.numerator} / {r.denominator}
              {m.unit}{" "}
              {r.denominator > 0 && r.denominator < 5 && <em>관찰 수 적음</em>}
            </p>
            <p>{m.definition}</p>
            {delta !== null && (
              <small>
                직전 기간 대비 {delta > 0 ? "+" : ""}
                {delta}%p{" "}
                <span>
                  (이전 {percentText(prev!)} · {prev!.denominator} →{" "}
                  {r.denominator}
                  {m.unit})
                </span>
              </small>
            )}
            {r.denominator === 0 && <small>집계 가능한 기록이 없습니다.</small>}
            {m.key === "transfer" && (
              <small>
                교사 확인 대기 {s.transferPending}건 · 분모에서 제외
              </small>
            )}
          </article>
        );
      })}
    </div>
  );
}

export function RubricProfile({
  summary: s,
  pendingLabel = "미채점",
}: {
  summary: ReportSummary;
  pendingLabel?: string;
}) {
  return (
    <div className="qr-rubric-profile">
      {rubricCriteria.map((c, i) => {
        const value = s.criterionAverages[i];
        return (
          <div key={c.name}>
            <div>
              <span>{c.name}</span>
              <b>
                {value === null ? "—" : value.toFixed(1)} <small>/ 2점</small>
              </b>
            </div>
            <div
              className="ad-track"
              role="meter"
              aria-label={`${c.name} 기준별 평균`}
              aria-valuemin={0}
              aria-valuemax={2}
              aria-valuenow={value ?? 0}
              aria-valuetext={
                value === null
                  ? "채점 기록 없음"
                  : `${value.toFixed(1)}점, ${s.reviewed}건 평균`
              }
            >
              <i style={{ width: `${(value ?? 0) * 50}%` }} />
            </div>
          </div>
        );
      })}
      <p>
        기준별 채점 {s.reviewed}건 · {pendingLabel} {s.pending}건<br />
        수정 응답이 있으면 최근 응답의 채점을 표시합니다.
      </p>
    </div>
  );
}

export function ReportMethodology() {
  return (
    <details className="qr-method">
      <summary>
        <Info size={17} /> 산출 기준과 채점표
      </summary>
      <div className="qr-method-body">
        <p>
          <b>첫 응답 기준:</b> 선택 정답·근거 일치·도움 사용은 첫 제출을
          기준으로 계산합니다. 수정한 답으로 최초 정답률을 높이지 않습니다. 독립
          응답률은 정답 여부가 아닌 수행 조건입니다.
        </p>
        <p>
          <b>새 글 적용:</b> 처음 보는 글의 독립 단계에서 도움 없이 남긴 첫
          응답만 집계합니다. 교사 확인 전 기록은 대기로 남기며, 검토 완료 응답만
          확인율의 분모에 포함합니다.
        </p>
        <p>
          <b>설명 평가:</b> 아래 네 항목을 각각 0~2점으로 확인합니다. 합계는 8점
          만점이며, 채점된 응답의 평균을 표시합니다. 메모만 저장된 응답은 채점
          완료로 간주하지 않습니다.
        </p>
        <div className="qr-table-wrap">
          <table>
            <caption>ReadX 체험용 응답 채점 기준 · v1</caption>
            <thead>
              <tr>
                <th>항목</th>
                <th>0점</th>
                <th>1점</th>
                <th>2점</th>
              </tr>
            </thead>
            <tbody>
              {rubricCriteria.map((c) => (
                <tr key={c.name}>
                  <th>{c.name}</th>
                  {c.levels.map((l) => (
                    <td key={l}>{l}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p>
          백분율은 정수로, 기간 차이는 소수 첫째 자리로 반올림합니다. 기간
          비교는 관찰 결과의 변화입니다. 문항·지문 난도가 같다고 보장하지
          않으므로 능력 상승이나 하락으로 단정하지 않습니다. 백분위·학년
          수준·종합 문해력 점수는 산출하지 않습니다. 반 전체 비율은 학생별
          비율의 평균이 아닌 응답 건수를 합쳐 계산합니다.
        </p>
      </div>
    </details>
  );
}

export function QuantifiedReport({
  students,
  audience = "teacher",
}: {
  students: DemoStudent[];
  audience?: "teacher" | "parent";
}) {
  const { reviews, releases } = useDemoAcademy();
  const [periodId, setPeriodId] = useState("week");
  const period = reportPeriods.find((p) => p.id === periodId)!;
  const records = demoReportRecords(students, reviews, releases, audience);
  const summary = summarizeReport(records, period.start, period.end);
  const previous = period.previousStart
    ? summarizeReport(records, period.previousStart, period.previousEnd)
    : undefined;
  const names = Object.fromEntries(students.map((s) => [s.id, s.name]));
  const exportRows = () => {
    const blob = new Blob([reportCsv(summary.rows, names)], {
      type: "text/csv;charset=utf-8;",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `ReadX_예시학습기록_${period.start}_${period.end}.csv`;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return (
    <section className="qr-report" aria-label="수치로 보는 학습 리포트">
      <header className="qr-header">
        <div>
          <p className="rx-eyebrow">EVIDENCE → MEASUREMENT → NEXT STEP</p>
          <h2>수치로 보는 학습 과정</h2>
          <p>
            {period.start.replace(/-/g, ".")} — {period.end.replace(/-/g, ".")}{" "}
            ·{" "}
            {students.length === 1
              ? students[0].name
              : `${students.length}명 합산`}{" "}
            · 가상 예시
          </p>
        </div>
        <div className="qr-tools no-print">
          <label>
            집계 기간
            <select
              aria-label="리포트 집계 기간"
              value={periodId}
              onChange={(e) => setPeriodId(e.target.value)}
            >
              {reportPeriods.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.label}
                </option>
              ))}
            </select>
          </label>
          <button className="rx-button" onClick={exportRows}>
            <Download size={16} /> 집계 기록 CSV
          </button>
        </div>
      </header>
      <div className="qr-evidence-strip">
        <ClipboardCheck size={19} />
        <span>
          <b>{summary.submitted}건 제출</b> / {summary.assigned}건 배정
        </span>
        <span>
          기준별 채점 <b>{summary.reviewed}건</b>
        </span>
        <span>
          {audience === "parent" ? "미채점·미공개" : "미채점"}{" "}
          <b>{summary.pending}건</b>
        </span>
        <span>
          수정한 활동 <b>{summary.corrections}건</b>
        </span>
      </div>
      <MetricCards summary={summary} previous={previous} />
      <div className="qr-analysis-grid">
        <section className="ad-card">
          <p className="rx-eyebrow">RESPONSE RUBRIC</p>
          <div className="qr-score-heading">
            <h3>근거를 갖춘 설명</h3>
            <strong>
              {summary.rubricAverage === null
                ? "—"
                : summary.rubricAverage.toFixed(1)}
              <small> / 8점</small>
            </strong>
          </div>
          <p className="qr-caption">
            최근 응답의 기준별 평균 · 채점 {summary.reviewed}건
          </p>
          <RubricProfile
            summary={summary}
            pendingLabel={audience === "parent" ? "미채점·미공개" : "미채점"}
          />
        </section>
        <section className="ad-card">
          <p className="rx-eyebrow">FOUR-WEEK RECORD</p>
          <h3>첫 응답의 근거 일치율 추이</h3>
          <div className="qr-trend">
            {reportWeeks.map((w) => {
              const m = summarizeReport(records, w.start, w.end).evidence;
              return (
                <div key={w.start}>
                  <b>{percentText(m)}</b>
                  <div className="qr-trend-track">
                    <i style={{ height: `${m.percent ?? 0}%` }} />
                  </div>
                  <span>{w.label}</span>
                  <small>
                    {m.numerator}/{m.denominator}응답
                  </small>
                </div>
              );
            })}
          </div>
          <p className="qr-caption">
            각 주의 첫 응답을 집계합니다. 서로 다른 글의 관찰이며, 동일 난도
            검사의 향상도는 아닙니다.
          </p>
        </section>
      </div>
      <div className="qr-next">
        <BarChart3 size={22} />
        <div>
          <b>다음 확인할 기록</b>
          <p>
            {summary.pending
              ? audience === "parent"
                ? `설명 ${summary.pending}건은 채점 또는 공개 전입니다. 공개된 응답의 근거와 설명을 함께 살펴보세요. `
                : `미채점 ${summary.pending}건의 설명을 네 가지 기준으로 먼저 확인하세요. `
              : "채점된 응답의 기준별 결과를 바탕으로 다음 연습을 정해 보세요. "}
            {summary.transferPending
              ? `새 글 적용 중 ${summary.transferPending}건은 아직 교사 확인 전입니다.`
              : summary.transfer.denominator < 5
                ? `새 글 독립 확인이 ${summary.transfer.denominator}건입니다. 다른 글에서도 관찰을 더 모아 보세요.`
                : "새 글에서 확인되지 않은 응답의 근거와 설명을 살펴보세요."}
          </p>
        </div>
      </div>
      <ReportMethodology />
      <details className="qr-ledger">
        <summary>집계에 사용한 활동별 기록 · {summary.rows.length}건</summary>
        <p>
          선택 정답·근거·도움은 첫 제출 기준, 설명 점수는 최근 응답 기준입니다.
          ‘—’는 해당 문항 없음 또는 미확정입니다.
        </p>
        <div className="qr-table-wrap">
          <table>
            <caption>{period.label} · 가상 예시 활동 원장</caption>
            <thead>
              <tr>
                <th>날짜 · 학생</th>
                <th>활동</th>
                <th>첫 선택</th>
                <th>첫 근거</th>
                <th>도움</th>
                <th>독립 조건</th>
                <th>새 글 적용</th>
                <th>설명 / 8</th>
              </tr>
            </thead>
            <tbody>
              {summary.rows.map((r) => (
                <tr key={r.id}>
                  <td>
                    {r.date.slice(5)}
                    <small>{names[r.learnerId]}</small>
                  </td>
                  <td>
                    {r.title}
                    <small>
                      {r.goal} ·{" "}
                      {r.initial
                        ? r.revised
                          ? "수정 기록 있음"
                          : "첫 응답"
                        : "미제출"}
                    </small>
                  </td>
                  <td>
                    {r.initial?.choiceCorrect === true
                      ? "정답"
                      : r.initial?.choiceCorrect === false
                        ? "오답"
                        : "—"}
                  </td>
                  <td>{flag(r.initial?.evidenceCorrect)}</td>
                  <td>{r.initial ? `${r.initial.hints}회` : "—"}</td>
                  <td>
                    {r.initial
                      ? r.initial.independent && r.initial.hints === 0
                        ? "독립"
                        : "안내·도움"
                      : "—"}
                  </td>
                  <td>
                    {r.initial?.transfer &&
                    r.initial.fresh &&
                    r.initial.independent &&
                    r.initial.hints === 0
                      ? r.initial.confirmed === null
                        ? "확인 대기"
                        : r.initial.confirmed
                          ? "수행 확인"
                          : "추가 연습"
                      : "대상 아님"}
                  </td>
                  <td>
                    {r.rubric ? r.rubric.reduce((a, b) => a + b, 0) : "—"}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </section>
  );
}
function flag(value: boolean | null | undefined) {
  return value === true ? "일치" : value === false ? "불일치" : "—";
}

export function TeacherQuantifiedReport() {
  const { selectedClassId, selectedStudentId, selectClass, selectStudent } =
    useDemoAcademy();
  const [all, setAll] = useState(false);
  const students = demoStudents.filter((s) => s.classId === selectedClassId),
    student = students.find((s) => s.id === selectedStudentId) || students[0];
  return (
    <>
      <div className="qr-selectors">
        <label>
          살펴볼 반
          <select
            aria-label="분석할 반"
            value={selectedClassId}
            onChange={(e) => selectClass(e.target.value)}
          >
            {demoClasses.map((c) => (
              <option key={c.id} value={c.id}>
                {c.name} · {c.grade}학년
              </option>
            ))}
          </select>
        </label>
        <label>
          분석 대상
          <select
            aria-label="분석할 학생"
            value={all ? "all" : student.id}
            onChange={(e) => {
              setAll(e.target.value === "all");
              if (e.target.value !== "all") selectStudent(e.target.value);
            }}
          >
            <option value="all">반 전체 합산</option>
            {students.map((s) => (
              <option key={s.id} value={s.id}>
                {s.name}
              </option>
            ))}
          </select>
        </label>
      </div>
      <QuantifiedReport students={all ? students : [student]} />
    </>
  );
}
export function DirectorQuantifiedReport() {
  const [classId, setClassId] = useState("all");
  return (
    <>
      <div className="qr-selectors">
        <label>
          분석할 반
          <select
            aria-label="학원 분석 범위"
            value={classId}
            onChange={(e) => setClassId(e.target.value)}
          >
            <option value="all">학원 전체 · 24명 합산</option>
            {demoClasses.map((c) => (
              <option key={c.id} value={c.id}>
                {c.name} · {c.grade}학년
              </option>
            ))}
          </select>
        </label>
      </div>
      <QuantifiedReport
        students={demoStudents.filter(
          (s) => classId === "all" || s.classId === classId,
        )}
      />
    </>
  );
}
