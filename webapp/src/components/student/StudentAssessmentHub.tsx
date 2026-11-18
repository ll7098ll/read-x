import { ExamEntryCard } from "../exam/ExamEntryCard";
import React, { useEffect, useState } from 'react';
import { ArrowLeft, ArrowRight, BookOpen, CalendarDays, Check, CheckCircle2, Clock3, Download, Flag, History, Target, TrendingUp } from 'lucide-react';
import { miniExamForms, miniGoals, transferChecks } from '../../data/miniExams';
import { goalProgress, kstDay, miniHistory, miniItems, miniScore, transferSuccess } from '../../services/miniExam';
import { useStudentAssessment, useAssessmentStorageStatus } from '../../store/useStudentAssessment';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { LearningEvidenceReport } from '../common/LearningEvidenceReport';
import type { AssessmentView, MiniExamAttempt, MiniGrade, MiniQuestion } from '../../types/miniExam';

const views: [AssessmentView, string][] = [['overview', '학습 한눈에'], ['exams', '미니 모의고사'], ['report', '성적 분석'], ['goals', '나의 목표'], ['history', '학습이력']];
const goalName = (key: string) => miniGoals.find(g => g.key === key)?.title || key;
const dateText = (at: number) => new Intl.DateTimeFormat('ko-KR', { timeZone: 'Asia/Seoul', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' }).format(at);
const clockText = (seconds: number) => `${Math.floor(Math.max(0, seconds) / 60).toString().padStart(2, '0')}:${Math.floor(Math.max(0, seconds) % 60).toString().padStart(2, '0')}`;
const finished = (attempts: MiniExamAttempt[], grade: MiniGrade) => attempts.filter(a => a.form.grade === grade && a.status !== 'in_progress').sort((a, b) => b.submittedAt! - a.submittedAt!);

function Empty({ title, children, action }: { title: string; children: React.ReactNode; action?: React.ReactNode }) {
  return <div className="mx-empty"><BookOpen size={28}/><h3>{title}</h3><p>{children}</p>{action}</div>;
}
function PracticeNote() {
  return <p className="mx-note">개인 연습 · 이 브라우저에 저장돼요. 시범 문항으로 독서 수행을 확인하며, 교사 콘텐츠 검수 전입니다.</p>;
}
function SkillBars({ attempt }: { attempt: MiniExamAttempt }) {
  return <div className="mx-skill-bars">{miniScore(attempt).skills.map(s => <div key={s.skill}>
    <div><span>{s.skill}</span><strong>{s.total ? `${s.correct}/${s.total} · ${s.percent}%` : '출제되지 않음'}</strong></div>
    <div className="mx-track" aria-hidden="true"><span style={{ width: `${s.percent || 0}%` }}/></div>
  </div>)}</div>;
}

export function AssessmentEntryCards({ grade }: { grade: number }) {
  const { attempts, checks, remediations, setView } = useStudentAssessment();
  const { setStudentMode } = useCoursewareStore();
  const g: MiniGrade = grade === 6 ? 6 : 5;
  const latest = finished(attempts, g)[0];
  const achieved = miniGoals.filter(goal => goalProgress(goal.key, g, attempts, checks, remediations, Date.now()).achieved).length;
  const open = (view: AssessmentView) => { setView(view); setStudentMode('assessment'); };
  return <section className="mx-entry" aria-label="미니 모의고사와 나의 성장">
    <div className="mx-section-heading"><div><p className="rx-eyebrow">READ · CHECK · GROW</p><h2>짧게 연습하고, 나의 기록을 살펴요</h2></div><button className="rx-text-link" onClick={() => open('overview')}>개인 연습 기록 <ArrowRight size={16}/></button></div>
    <div className="mx-entry-grid">
      <button className="mx-entry-card mx-entry-feature" onClick={() => open('exams')}><BookOpen/><span>초5·6 수능형 독서</span><strong>미니 모의고사</strong><small>3개 지문 · 12문항 · 25분</small><ArrowRight className="mx-card-arrow"/></button>
      <button className="mx-entry-card" onClick={() => open('report')}><TrendingUp/><span>최근 성적</span><strong>{latest ? `${miniScore(latest).percent}점` : '첫 기록을 기다려요'}</strong><small>{latest ? `${g}학년 · ${miniScore(latest).correct}/12 정답` : '문제를 풀면 분석이 시작돼요'}</small></button>
      <button className="mx-entry-card" onClick={() => open('goals')}><Target/><span>현재 목표</span><strong>{achieved} / 3개 기준 충족</strong><small>비교 · 조건과 결과 · 자료 판단</small></button>
    </div>
  </section>;
}

export function StudentAssessmentHub() {
  const store = useStudentAssessment();
  const { activeGradeIdx, setActiveGradeIdx } = useCoursewareStore();
  const grade: MiniGrade = activeGradeIdx === 5 ? 6 : 5;
  const error = useAssessmentStorageStatus(s => s.error);
  const [start, setStart] = useState(''), [end, setEnd] = useState('');
  useEffect(() => { store.expire(); const timer = setInterval(() => useStudentAssessment.getState().expire(), 1000); return () => clearInterval(timer); }, []);
  const screen = store.screen;
  const screenId = 'id' in screen ? screen.id : '';
  useEffect(() => { document.getElementById('main-content')?.scrollIntoView({ block: 'start' }); }, [screen.kind, screenId, store.view]);
  const currentAttempt = 'id' in screen ? store.attempts.find(a => a.id === screen.id) : undefined;
  const filtered = finished(store.attempts, grade).filter(a => (!start || kstDay(a.submittedAt!) >= start) && (!end || kstDay(a.submittedAt!) <= end));
  const badRange = !!(start && end && start > end);
  const exportRecords = () => {
    const blob = new Blob([JSON.stringify({ schemaVersion: 1, exportedAt: new Date().toISOString(), scope: 'local-practice', attempts: store.attempts, remediations: store.remediations, checks: store.checks }, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob), a = document.createElement('a'); a.href = url; a.download = `ReadX_개인학습기록_${kstDay(Date.now())}.json`; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <div className="mx-hub">
    {error && <div className="mx-alert" role="alert">{error} <button className="rx-text-link" onClick={exportRecords}>기록 내보내기</button></div>}
    {screen.kind !== 'dashboard' ? <>
      <button className="rx-text-link mx-back" onClick={() => store.setView(screen.kind === 'exam' ? 'exams' : screen.kind === 'result' ? 'report' : 'goals')}><ArrowLeft size={17}/> 대시보드로</button>
      {screen.kind === 'exam' && currentAttempt && (currentAttempt.status === 'in_progress' ? <MiniExamPlayer attempt={currentAttempt}/> : <MiniExamResult attempt={currentAttempt}/>)}
      {screen.kind === 'result' && currentAttempt && (currentAttempt.status === 'in_progress' ? <MiniExamPlayer attempt={currentAttempt}/> : <MiniExamResult attempt={currentAttempt}/>)}
      {screen.kind === 'remediation' && <RemediationPlayer id={screen.id}/>}
      {screen.kind === 'transfer' && <TransferPlayer id={screen.id}/>}
      {['exam', 'result'].includes(screen.kind) && !currentAttempt && <Empty title="응시 기록을 찾을 수 없어요">대시보드에서 시험을 선택해 주세요.</Empty>}
    </> : <>
      <header className="mx-heading"><div><p className="rx-eyebrow">MY LEARNING DASHBOARD</p><h1>읽고, 확인하고, 한 걸음 더</h1><p>내가 풀었던 문제에서 다음 학습을 찾아요.</p></div>
        <label className="mx-grade">모의고사 학년<select value={grade} onChange={e => setActiveGradeIdx(Number(e.target.value) - 1)}><option value={5}>초등 5학년</option><option value={6}>초등 6학년</option></select></label>
      </header>
      <ExamEntryCard role="student"/>
      <nav className="mx-tabs" aria-label="학생 분석 메뉴">{views.map(([id, label]) => <button key={id} aria-current={store.view === id ? 'page' : undefined} onClick={() => store.setView(id)}>{label}</button>)}</nav>
      {['overview', 'report', 'history'].includes(store.view) && <div className="mx-range"><CalendarDays size={17}/><label>시작일<input type="date" value={start} onChange={e => setStart(e.target.value)}/></label><span>~</span><label>종료일<input type="date" value={end} onChange={e => setEnd(e.target.value)}/></label>
        <button onClick={() => { setStart(`${kstDay(Date.now()).slice(0, 7)}-01`); setEnd(kstDay(Date.now())); }}>이번 달</button><button onClick={() => { setStart(''); setEnd(''); }}>전체 기간</button>
      </div>}
      {badRange && <p className="mx-alert" role="alert">종료일은 시작일 이후로 선택해 주세요.</p>}
      {store.view === 'overview' && <Overview grade={grade} attempts={badRange ? [] : filtered}/>}
      {store.view === 'exams' && <ExamList grade={grade}/>}
      {store.view === 'report' && <GrowthReport grade={grade} attempts={badRange ? [] : filtered}/>}
      {store.view === 'goals' && <GoalCards grade={grade}/>}
      {store.view === 'history' && <HistoryPanel grade={grade} start={start} end={end} badRange={badRange}/>}
      <PracticeNote/>
      <button className="rx-text-link mx-export" onClick={exportRecords}><Download size={16}/> 내 학습 기록 내보내기</button>
    </>}
  </div>;
}

function ExamList({ grade }: { grade: MiniGrade }) {
  const { attempts, start, open } = useStudentAssessment();
  const form = miniExamForms.find(f => f.grade === grade)!;
  const pending = attempts.find(a => a.form.grade === grade && a.status === 'in_progress');
  const count = finished(attempts, grade).length;
  return <section className="mx-panel mx-exam-intro">
    <div><span className="mx-badge">독서 · 개인 실전 연습</span><h2>{form.title}</h2><p>글의 단서를 찾고, 관계를 연결하고, 자료에 맞게 판단해 보세요.</p></div>
    <div className="mx-exam-spec"><span><BookOpen/> 지문 3개</span><span><CheckCircle2/> 5지선다 12문항</span><span><Clock3/> 25분</span></div>
    <div className="mx-topic-grid">{form.passages.map(p => <article key={p.id}><small>{p.subject}</small><h3>{p.title}</h3><p>{p.questions.length}문항</p></article>)}</div>
    <ul className="mx-instructions"><li>시험을 시작하면 시간이 흐르고, 다시 열어도 남은 시간부터 이어져요.</li><li>선택한 답과 다시 볼 문항은 이 기기에 자동 저장돼요.</li><li>제출하거나 시간이 끝나면 답이 잠기고 해설을 볼 수 있어요.</li>{count > 0 && <li>같은 시험을 다시 풀면 재응시로 기록돼요. 이미 본 글은 새로운 목표 확인 근거에 더하지 않아요.</li>}</ul>
    <button className="rx-button rx-button-primary" onClick={() => pending ? open({ kind: 'exam', id: pending.id }) : start(grade)}>{pending ? '이어서 풀기' : count ? '같은 시험 다시 풀기' : '미니 모의고사 시작'} <ArrowRight size={17}/></button>
    <PracticeNote/>
  </section>;
}

function Overview({ grade, attempts }: { grade: MiniGrade; attempts: MiniExamAttempt[] }) {
  const { checks, remediations, attempts: all, setView, open, start } = useStudentAssessment();
  const latest = attempts[0];
  const active = all.find(a => a.form.grade === grade && a.status === 'in_progress');
  const progress = miniGoals.map(g => goalProgress(g.key, grade, all, checks, remediations, Date.now()));
  const history = miniHistory(all, remediations, checks, grade);
  return <>
    <div className="mx-summary-grid">
      <section className="mx-summary mx-summary-primary"><span>최근 미니 모의고사</span><strong>{latest ? `${miniScore(latest).percent}점` : '아직 성적이 없어요'}</strong><p>{latest ? `${miniScore(latest).correct}/${miniScore(latest).total} 정답 · ${dateText(latest.submittedAt!)}` : '첫 응시 후 내 강점과 다음 목표를 확인해요.'}</p><button onClick={() => latest ? open({ kind: 'result', id: latest.id }) : start(grade)}>{latest ? '성적표 보기' : '첫 시험 시작'} <ArrowRight size={16}/></button></section>
      <section className="mx-summary"><Target/><span>현재 목표 · 전체 누적</span><strong>{progress.filter(g => g.achieved).length}<small> / 3개</small></strong><p>선택형 수행 확인 기준 충족</p><button className="rx-text-link" onClick={() => setView('goals')}>근거와 남은 확인 보기 <ArrowRight size={16}/></button></section>
      <section className="mx-summary"><History/><span>학습이력 · 전체 누적</span><strong>{history.length}<small>건</small></strong><p>응시 · 보충학습 · 새 글 확인</p><button className="rx-text-link" onClick={() => setView('history')}>내 기록 살펴보기 <ArrowRight size={16}/></button></section>
    </div>
    {active && <div className="mx-resume"><Clock3/><div><strong>풀고 있는 미니 모의고사가 있어요</strong><p>{active.form.title} · {Object.keys(active.answers).length}/12 응답</p></div><button className="rx-button" onClick={() => open({ kind: 'exam', id: active.id })}>이어서 풀기</button></div>}
    <div className="mx-two-columns"><section className="mx-panel"><div className="mx-section-heading"><h2>사고 수준별 수행</h2><button className="rx-text-link" onClick={() => setView('report')}>자세히 <ArrowRight size={16}/></button></div>{latest ? <><p className="mx-muted">최근 시험 · 정답 수 / 출제 문항 수</p><SkillBars attempt={latest}/></> : <Empty title="어떤 문제에 강할까요?">시험을 제출하면 실제 응답으로 분석해요.</Empty>}</section>
      <section className="mx-panel"><div className="mx-section-heading"><h2>최근 회차 기록</h2><TrendingUp size={20}/></div><AttemptChart attempts={attempts}/></section></div>
    <ReviewQueue grade={grade}/>
    <section className="mx-panel"><div className="mx-section-heading"><h2>현재 목표와 다음 한 걸음</h2><button className="rx-text-link" onClick={() => setView('goals')}>전체 목표 <ArrowRight size={16}/></button></div><GoalCards grade={grade} compact/></section>
  </>;
}

export function MiniExamPlayer({ attempt }: { attempt: MiniExamAttempt }) {
  const { answer, flag, submit, activePassage, setPassage } = useStudentAssessment();
  const [now, setNow] = useState(Date.now()), [confirm, setConfirm] = useState(false), [large, setLarge] = useState(false);
  const [mobilePane, setMobilePane] = useState<'reading' | 'questions'>('reading');
  useEffect(() => { const timer = setInterval(() => { setNow(Date.now()); useStudentAssessment.getState().expire(); }, 1000); return () => clearInterval(timer); }, []);
  const items = miniItems(attempt.form), pIndex = Math.min(activePassage, attempt.form.passages.length - 1), passage = attempt.form.passages[pIndex];
  const remaining = Math.max(0, Math.ceil((attempt.deadlineAt - now) / 1000));
  const jump = (index: number, id?: string) => { setPassage(index); setMobilePane(id ? 'questions' : 'reading'); requestAnimationFrame(() => (id ? document.getElementById(`mini-${id}`) : document.querySelector('.mx-exam-bar'))?.scrollIntoView({ block: 'start', behavior: 'smooth' })); };
  return <div className={`mx-player ${large ? 'mx-large' : ''}`}>
    <header className="mx-exam-bar"><div><span className="mx-badge">초{attempt.form.grade} · 독서 미니</span><h1>{attempt.form.title}</h1></div><div className="mx-exam-tools"><strong role="timer" aria-label="남은 시간">{clockText(remaining)}</strong><span>{Object.keys(attempt.answers).length}/{items.length} 응답</span><button className="rx-button" aria-pressed={large} onClick={() => setLarge(!large)}>큰 글자</button><button className="rx-button rx-button-primary" onClick={() => setConfirm(true)}>답안 제출</button></div></header>
    <p className="mx-save-status"><CheckCircle2 size={15}/> 답안은 선택할 때마다 기기에 저장돼요. 시험이 끝나면 해설이 열려요.</p>
    {confirm && <section className="mx-confirm" aria-label="제출 전 확인"><h2>답안을 제출할까요?</h2><p>{items.length - Object.keys(attempt.answers).length ? `아직 답하지 않은 문제가 ${items.length - Object.keys(attempt.answers).length}개 있어요. 미응답은 0점으로 기록돼요.` : '모든 문항에 답했어요.'} 제출 후에는 답을 바꿀 수 없어요.</p><div className="mx-actions"><button className="rx-button" onClick={() => setConfirm(false)}>계속 풀기</button><button className="rx-button rx-button-primary" onClick={() => submit(attempt.id)}>제출 확정</button></div></section>}
    <nav className="mx-passage-tabs" aria-label="지문 선택">{attempt.form.passages.map((p, i) => <button key={p.id} aria-current={i === pIndex ? 'page' : undefined} onClick={() => jump(i)}>{i + 1}. {p.title}</button>)}</nav>
    <nav className="mx-mobile-switch" aria-label="지문과 문제 전환"><button aria-pressed={mobilePane === 'reading'} onClick={() => setMobilePane('reading')}>지문 보기</button><button aria-pressed={mobilePane === 'questions'} onClick={() => setMobilePane('questions')}>문제 풀기</button></nav>
    <div className="mx-exam-layout" data-mobile-pane={mobilePane}><article className="mx-reading mx-panel"><span className="mx-badge">지문 {pIndex + 1} / {attempt.form.passages.length}</span><h2>{passage.title}</h2>{passage.paragraphs.map((p, i) => <p key={p.id}><span className="mx-paragraph-no">{i + 1}</span>{p.text}</p>)}<button className="rx-button rx-button-primary mx-mobile-read-done" onClick={() => { setMobilePane('questions'); requestAnimationFrame(() => document.querySelector('.mx-mobile-switch')?.scrollIntoView({block:'start'})); }}>이 지문 문제 풀기 <ArrowRight size={16}/></button></article>
      <div className="mx-questions"><nav className="mx-omr mx-panel" aria-label="답안 현황">{items.map(({ question: q, passage: p }, i) => <button key={q.id} aria-label={`${i + 1}번 · ${attempt.answers[q.id] === undefined ? '미응답' : `${attempt.answers[q.id] + 1}번 선택`}${attempt.flagged.includes(q.id) ? ' · 다시 볼 문항' : ''}`} data-answered={attempt.answers[q.id] !== undefined} onClick={() => jump(attempt.form.passages.indexOf(p), q.id)}>{i + 1}{attempt.flagged.includes(q.id) && <Flag size={10}/>}</button>)}</nav>
        {passage.questions.map(q => <article id={`mini-${q.id}`} className="mx-panel mx-question" key={q.id}><div className="mx-question-top"><span>문항 {items.findIndex(i => i.question.id === q.id) + 1}</span><button className="rx-text-link" aria-pressed={attempt.flagged.includes(q.id)} onClick={() => flag(attempt.id, q.id)}><Flag size={15}/>{attempt.flagged.includes(q.id) ? '표시됨' : '다시 보기'}</button></div><QuestionChoices question={q} selected={attempt.answers[q.id] ?? null} onChange={choice => answer(attempt.id, q.id, choice)} name={`${attempt.id}-${q.id}`}/></article>)}
        <div className="mx-actions"><button className="rx-button" disabled={pIndex === 0} onClick={() => jump(pIndex - 1)}>이전 지문</button>{pIndex < attempt.form.passages.length - 1 ? <button className="rx-button rx-button-primary" onClick={() => jump(pIndex + 1)}>다음 지문 <ArrowRight size={16}/></button> : <button className="rx-button rx-button-primary" onClick={() => setConfirm(true)}>답안 제출</button>}</div>
      </div></div>
  </div>;
}

function QuestionChoices({ question, selected, onChange, name, disabled = false }: { question: MiniQuestion; selected: number | null; onChange: (choice: number) => void; name: string; disabled?: boolean }) {
  return <fieldset className="mx-choice-field" disabled={disabled}><legend>{question.prompt}</legend>{question.scenario && <div className="mx-scenario"><strong>보기</strong><p>{question.scenario}</p></div>}<div className="mx-options">{question.options.map((option, i) => <label key={i} data-selected={selected === i}><input type="radio" name={name} value={i} checked={selected === i} onChange={() => onChange(i)}/><span className="mx-option-no">{i + 1}</span><span>{option}</span></label>)}</div></fieldset>;
}

export function MiniExamResult({ attempt }: { attempt: MiniExamAttempt }) {
  const score = miniScore(attempt), { beginRemediation, setView } = useStudentAssessment();
  return <div className="mx-result"><header className="mx-heading"><div><p className="rx-eyebrow">MY EXAM REPORT</p><h1>이번 읽기의 결과를 확인해요</h1><p>{attempt.form.title} · {dateText(attempt.submittedAt ?? attempt.startedAt)}{attempt.status === 'auto_submitted' ? ' · 시간 종료 제출' : ''}</p></div><button className="rx-button" onClick={() => setView('goals')}>목표 현황 <Target size={17}/></button></header>
    <div className="mx-score-banner"><div><span>100점 환산 점수</span><strong>{score.percent}<small>점</small></strong><p>원점수 {score.correct}/{score.total} · 문항당 1점</p></div><dl><div><dt>정답</dt><dd>{score.correct}개</dd></div><div><dt>오답</dt><dd>{score.wrong}개</dd></div><div><dt>미응답</dt><dd>{score.unanswered}개</dd></div><div><dt>경과 시간</dt><dd>{clockText(score.elapsedSec)}</dd></div></dl></div>
    <p className="mx-note">{attempt.freshFamilies.length ? '처음 응시한 글의 결과를 목표 확인 근거로 연결했어요.' : '이미 본 글의 재응시예요. 점수는 이력에 남고 새로운 독립 수행 증거에는 더하지 않아요.'} 해설을 읽은 뒤의 복습은 최초 성적을 바꾸지 않아요.</p>
    <div className="mx-two-columns"><section className="mx-panel"><h2>사고 수준별 수행</h2><SkillBars attempt={attempt}/></section><section className="mx-panel"><h2>지문별 정답 수</h2>{attempt.form.passages.map(p => { const rows = score.results.filter(r => r.passage.id === p.id); return <div className="mx-passage-result" key={p.id}><span>{p.title}</span><strong>{rows.filter(r => r.outcome === 'correct').length}/{rows.length}</strong></div>; })}<p className="mx-note">이번 미니판은 독서만 다뤄요. 문학·언어와 매체 성적은 산출하지 않아요.</p></section></div>
    <section className="mx-panel"><h2>문항별 결과와 해설</h2><div className="mx-result-items">{score.results.map((r, index) => <details key={r.question.id}><summary><span className={`mx-outcome mx-${r.outcome}`}>{r.outcome === 'correct' ? '정답' : r.outcome === 'wrong' ? '오답' : '미응답'}</span><span>{index + 1}. {r.question.prompt}<small>{goalName(r.question.goal)} · {r.question.skill}</small></span><b>{r.choice === null ? '—' : `${r.choice + 1}번`} / 정답 {r.question.answer + 1}번</b></summary><div className="mx-explanation"><p>{r.question.explanation}</p><h3>본문 근거</h3>{r.passage.paragraphs.filter(p => r.question.evidence.includes(p.id)).map(p => <blockquote key={p.id}>{p.text}</blockquote>)}<h3>선지를 하나씩 확인해요</h3><ol>{r.question.options.map((option, i) => <li key={i}><strong>{option}</strong><p>{r.question.optionReasons[i]}</p></li>)}</ol><button className="rx-button" onClick={() => beginRemediation(attempt.id, r.question.id)}>이 문항 보충학습 <ArrowRight size={16}/></button></div></details>)}</div></section>
    <ReviewQueue grade={attempt.form.grade} attempt={attempt}/>
  </div>;
}

function AttemptChart({ attempts }: { attempts: MiniExamAttempt[] }) {
  if (!attempts.length) return <Empty title="첫 회차 기록을 기다려요">시험을 제출하면 회차별 성적을 살펴볼 수 있어요.</Empty>;
  const last = attempts.slice(0, 6).reverse();
  return <><ol className="mx-attempt-chart" aria-label="최근 응시 점수, 100점 만점">{last.map((a, i) => <li key={a.id}><strong>{miniScore(a).percent}</strong><div aria-hidden="true"><span style={{ height: `${miniScore(a).percent}%` }}/></div><small>{kstDay(a.submittedAt!).slice(5)}<br/>{a.freshFamilies.length ? '첫 응시' : '재응시'}</small></li>)}</ol><p className="mx-note">각 점수는 해당 응시의 기록이에요. 재응시와 시험지 난도의 차이를 실력 상승으로 계산하지 않아요.</p></>;
}
function GrowthReport({ grade, attempts }: { grade: MiniGrade; attempts: MiniExamAttempt[] }) {
  const [id, setId] = useState('');
  const { open } = useStudentAssessment();
  const selected = attempts.find(a => a.id === id) || attempts[0];
  if (!selected) return <section className="mx-panel"><Empty title="선택한 기간의 성적이 없어요" action={<button className="rx-button" onClick={() => useStudentAssessment.getState().setView('exams')}>모의고사 살펴보기</button>}>초{grade} 시험을 제출하거나 기간을 넓혀 보세요.</Empty></section>;
  const score = miniScore(selected);
  return <><section className="mx-panel"><div className="mx-section-heading"><h2>응시별 성적</h2><label>분석할 응시<select value={selected.id} onChange={e => setId(e.target.value)}>{attempts.map(a => <option value={a.id} key={a.id}>{dateText(a.submittedAt!)} · {miniScore(a).percent}점{a.freshFamilies.length ? '' : ' · 재응시'}</option>)}</select></label></div><div className="mx-report-summary"><strong>{score.percent}<small>점</small></strong><p>{score.correct}/{score.total} 정답 · 오답 {score.wrong} · 미응답 {score.unanswered}<br/>{selected.form.title}</p><button className="rx-button" onClick={() => open({ kind: 'result', id: selected.id })}>문항별 성적표 <ArrowRight size={16}/></button></div><SkillBars attempt={selected}/></section><section className="mx-panel"><h2>최근 회차 기록</h2><AttemptChart attempts={attempts}/></section><ReviewQueue grade={grade} attempt={selected}/></>;
}

function GoalCards({ grade, compact = false }: { grade: MiniGrade; compact?: boolean }) {
  const { attempts, checks, remediations, beginCheck } = useStudentAssessment();
  const labels = { unobserved: '아직 확인하지 않았어요', collecting: '혼자 수행한 증거를 모으고 있어요', independent: '혼자 수행 기준을 충족했어요', transfer: '새 글에도 적용했어요', maintained: '시간이 지나도 할 수 있어요' };
  return <div className={compact ? '' : 'mx-goals-page'}>{!compact && <div className="mx-section-heading"><div><h2>이번 학습의 목표 3개</h2><p className="mx-muted">전체 누적 · 선택형 독서 수행 기준으로 확인해요.</p></div><Target/></div>}
    <div className="mx-goal-grid">{miniGoals.map(goal => {
      const p = goalProgress(goal.key, grade, attempts, checks, remediations, Date.now());
      const bank = transferChecks.filter(c => c.grade === grade && c.goal === goal.key);
      const next = bank.find(c => !checks.some(a => a.check.id === c.id)) || bank.find(c => checks.some(a => a.check.id === c.id && !a.submittedAt));
      const hasExam = finished(attempts, grade).length > 0;
      return <article key={goal.key} className="mx-goal-card" data-achieved={p.achieved}><div className="mx-goal-icon">{p.achieved ? <CheckCircle2/> : <Target/>}</div><h3>{goal.title}</h3><span className="mx-goal-state">{p.state === 'unobserved' && p.guided ? '도움받아 연습하고 있어요' : labels[p.state]}</span>{p.needsRecheck && <span className="mx-badge">최근 재확인 필요</span>}<p>{goal.criterion}</p>
        <dl><div><dt>독립 확인 성공</dt><dd>{p.success}/{p.total}건</dd></div><div><dt>최근 확인 성공</dt><dd>{p.recentSuccess}/{p.recentTotal}건</dd></div><div><dt>최근 글 계열</dt><dd>{p.families}/3개</dd></div><div><dt>새 글 적용 성공</dt><dd>{p.transferFamilies}/2개</dd></div><div><dt>보충학습 완료</dt><dd>{p.guided}건</dd></div></dl>
        <div className="mx-track" aria-label={`목표 확인 진행: ${Math.min(p.families, 3)}/3개 글 계열`}><span style={{ width: `${Math.min(p.families / 3, 1) * 100}%` }}/></div>
        <p className="mx-goal-next">{!hasExam ? '미니 모의고사에서 첫 증거를 남겨요.' : next ? '다른 소재의 글에서 답과 근거를 함께 확인해요.' : '준비된 새 글 2편의 확인이 끝났어요. 기록을 살펴보세요.'}</p>
        {!hasExam ? <button className="rx-button" onClick={() => useStudentAssessment.getState().setView('exams')}>첫 확인 시작</button> : next ? <button className="rx-button" onClick={() => beginCheck(next.id)}>{checks.some(a => a.check.id === next.id) ? '새 글 확인 이어서' : '새 글로 확인하기'} <ArrowRight size={15}/></button> : <button className="rx-text-link" onClick={() => { const c = checks.find(c => c.check.id === bank[0].id); if (c) useStudentAssessment.getState().open({ kind: 'transfer', id: c.id }); }}>확인 기록 보기 <ArrowRight size={15}/></button>}
        {!compact && <details className="mx-goal-evidence"><summary>확인 기준과 증거 보기</summary><p>최근 28일의 서로 다른 글 계열 3개·세션 2회에서 5건 이상 확인하고, 최근 5건 중 4건 이상 성공하며 마지막 확인도 성공하면 독립 수행 기준을 충족해요.</p><p>새 글 2편에서 답과 근거까지 성공하면 적용을 확인해요. 이 기준은 개인 연습용이며 설명·쓰기 능력과는 별도로 봐요.</p>{p.evidence.length ? <ul>{p.evidence.map(e => <li key={e.id}>{dateText(e.at)} · {e.transfer ? '새 글' : '모의고사'} · {e.success ? '성공' : '추가 확인'}</li>)}</ul> : <p>아직 유효한 첫 응답이 없어요.</p>}</details>}
      </article>;
    })}</div>{!compact && <p className="mx-note">기준을 충족한 기록은 한 번의 실수로 지우지 않아요. 도움을 받은 복습과 이미 본 글은 새 독립 수행 증거에 합치지 않아요. 장기 유지와 교사 설명 평가는 추가 확인이 필요해요.</p>}</div>;
}

function ReviewQueue({ grade, attempt }: { grade: MiniGrade; attempt?: MiniExamAttempt }) {
  const { attempts, remediations, beginRemediation, setView } = useStudentAssessment();
  const latest = attempt || finished(attempts, grade)[0];
  if (!latest) return null;
  const rows = miniScore(latest).results.filter(r => r.outcome !== 'correct');
  return <section className="mx-panel"><div className="mx-section-heading"><div><p className="rx-eyebrow">NEXT STEP</p><h2>결과에서 이어지는 보충학습</h2></div><span className="mx-badge">선택한 시험 기준</span></div>{rows.length ? <div className="mx-review-list">{rows.map(r => { const review = remediations.find(a => a.attemptId === latest.id && a.questionId === r.question.id); return <article key={r.question.id}><span className={`mx-outcome mx-${r.outcome}`}>{r.outcome === 'unanswered' ? '미응답' : '오답'}</span><div><h3>{goalName(r.question.goal)}</h3><p>{r.passage.title} · {r.question.prompt}</p><small>{review?.completedAt ? '보충학습 완료 · 새 글에서 확인해 보세요' : '단서 찾기 → 관계 연결 → 조건 점검'}</small></div><button className="rx-button" onClick={() => beginRemediation(latest.id, r.question.id)}>{review?.completedAt ? '복습 기록' : review ? '이어서 복습' : '보충학습'}</button></article>; })}</div> : <div className="mx-success"><CheckCircle2/><p>이번 시험의 모든 문항에 답했어요. 다른 소재에서도 할 수 있는지 확인해 보세요.</p><button className="rx-button" onClick={() => setView('goals')}>새 글에서 목표 확인</button></div>}</section>;
}

function RemediationPlayer({ id }: { id: string }) {
  const { remediations, attempts, advanceRemediation, answerRemediation, setView, beginCheck, checks } = useStudentAssessment();
  const r = remediations.find(r => r.id === id), a = r && attempts.find(a => a.id === r.attemptId);
  const item = a && miniItems(a.form).find(i => i.question.id === r?.questionId);
  if (!r || !item) return <Empty title="보충학습을 찾을 수 없어요">성적표에서 문항을 다시 선택해 주세요.</Empty>;
  const goal = miniGoals.find(g => g.key === r.goal)!;
  const next = transferChecks.find(c => c.grade === r.grade && c.goal === r.goal && !checks.some(a => a.check.id === c.id));
  return <section className="mx-panel mx-review-player"><p className="rx-eyebrow">GUIDED PRACTICE</p><h1>{goal.title}</h1><p>{item.passage.title}의 단서를 다시 살펴봐요.</p><ol className="mx-step-list">{goal.steps.map((s, i) => <li key={s} data-active={i <= r.step}><span>{i + 1}</span>{s}{i < r.step && <Check size={16}/>}</li>)}</ol>
    <article className="mx-guidance"><h2>{['단서를 찾아요', '관계를 연결해요', '조건을 점검해요'][r.step]}</h2><p>{goal.steps[r.step]}</p>{item.passage.paragraphs.filter(p => item.question.evidence.includes(p.id)).map(p => <blockquote key={p.id}>{p.text}</blockquote>)}{r.step >= 1 && <p className="mx-model">생각 시범 · {item.question.explanation}</p>}{r.step < 2 && <button className="rx-button rx-button-primary" onClick={() => advanceRemediation(id)}>읽고 다음 단계로 <ArrowRight size={16}/></button>}</article>
    {r.step === 2 && <><h2>다시 골라 보세요</h2><QuestionChoices question={item.question} selected={r.choice} onChange={choice => answerRemediation(id, choice)} name={`review-${id}`} disabled={!!r.completedAt}/>{r.tries > 0 && !r.completedAt && r.choice !== null && <p className="mx-alert" role="status">{item.question.optionReasons[r.choice]} 본문 근거와 비교해 다시 골라 보세요.</p>}{r.completedAt && <div className="mx-success" role="status"><CheckCircle2/><div><h3>도움받아 복습했어요</h3><p>최초 시험 성적은 그대로 보관돼요. 다음에는 새 글에서 혼자 확인해 보세요.</p></div><button className="rx-button rx-button-primary" onClick={() => next ? beginCheck(next.id) : setView('goals')}>{next ? '새 글로 확인하기' : '목표 현황 보기'}</button></div>}</>}
  </section>;
}

function TransferPlayer({ id }: { id: string }) {
  const { checks, editCheck, submitCheck, setView } = useStudentAssessment();
  const a = checks.find(c => c.id === id);
  if (!a) return <Empty title="새 글 확인을 찾을 수 없어요">목표 화면에서 글을 선택해 주세요.</Empty>;
  const q = a.check.question;
  return <section className="mx-panel mx-transfer-player"><p className="rx-eyebrow">TRY A NEW TEXT</p><h1>{a.check.title}</h1><p>{goalName(a.check.goal)} · 답을 고르고 뒷받침하는 문단을 모두 선택해 주세요.</p>{!a.fresh && <p className="mx-note">같은 글 계열을 이미 시작한 기록이 있어요. 이번 응답은 개인 연습으로 보관해요.</p>}
    <div className="mx-transfer-text">{a.check.paragraphs.map((p, i) => <p key={p.id}><span className="mx-paragraph-no">{i + 1}</span>{p.text}</p>)}</div>
    <QuestionChoices question={q} selected={a.choice} onChange={choice => editCheck(id, { choice })} name={`transfer-${id}`} disabled={!!a.submittedAt}/>
    <fieldset className="mx-evidence-select" disabled={!!a.submittedAt}><legend>답을 뒷받침하는 문단은? 필요한 문단을 모두 선택해요.</legend>{a.check.paragraphs.map((p, i) => <label key={p.id}><input type="checkbox" checked={a.evidence.includes(p.id)} onChange={() => editCheck(id, { evidence: a.evidence.includes(p.id) ? a.evidence.filter(e => e !== p.id) : [...a.evidence, p.id] })}/>{i + 1}문단</label>)}</fieldset>
    {!a.submittedAt ? <button className="rx-button rx-button-primary" disabled={a.choice === null || !a.evidence.length} onClick={() => submitCheck(id)}>답과 근거 제출</button> : <div className={transferSuccess(a) ? 'mx-success' : 'mx-guidance'} role="status"><h2>{transferSuccess(a) ? '답과 근거를 함께 확인했어요' : '답과 근거를 다시 살펴봐요'}</h2><p>내 답 {a.choice! + 1}번 · 정답 {q.answer + 1}번 · 근거 예시 {q.evidence.map(e => a.check.paragraphs.findIndex(p => p.id === e) + 1).join(', ')}문단</p><p>{q.explanation}</p>{a.choice !== q.answer && a.choice !== null && <p>{q.optionReasons[a.choice]}</p>}<button className="rx-button" onClick={() => setView('goals')}>목표와 증거 확인 <ArrowRight size={16}/></button></div>}
  </section>;
}

function HistoryPanel({ grade, start, end, badRange }: { grade: MiniGrade; start: string; end: string; badRange: boolean }) {
  const { attempts, checks, remediations, open } = useStudentAssessment();
  const [kind, setKind] = useState('all');
  const all = miniHistory(attempts, remediations, checks, grade);
  const rows = badRange ? [] : all.filter(r => (!start || kstDay(r.at) >= start) && (!end || kstDay(r.at) <= end) && (kind === 'all' || r.kind.includes(kind)));
  const today = kstDay(Date.now()), date = new Date(`${today}T00:00:00Z`);
  const days = Array.from({ length: 28 }, (_, i) => { const d = new Date(date); d.setUTCDate(d.getUTCDate() - 27 + i); return d.toISOString().slice(0, 10); });
  return <><section className="mx-panel"><h2>최근 4주 학습 달력</h2><p className="mx-muted">초{grade}의 응시·보충학습·새 글 확인 날짜예요. 아래 목록의 기간 필터와 별개로 최근 28일을 보여 줘요.</p><div className="mx-calendar">{days.map(day => { const count = all.filter(r => kstDay(r.at) === day).length; return <div key={day} data-count={count > 0} title={`${day} · ${count}건`}><span>{Number(day.slice(-2))}</span><small>{count ? `${count}건` : '—'}</small></div>; })}</div></section>
    <section className="mx-panel"><div className="mx-section-heading"><h2>나의 학습이력 <span className="mx-badge">{rows.length}건</span></h2><label>활동 종류<select value={kind} onChange={e => setKind(e.target.value)}><option value="all">모든 활동</option><option>모의고사</option><option>보충학습</option><option>새 글 확인</option></select></label></div>{rows.length ? <ol className="mx-history">{rows.map(r => <li key={`${r.screen}-${r.id}`}><span className="mx-history-dot"/><div><small>{dateText(r.at)} · {r.kind}</small><h3>{r.title}</h3><p>{r.detail}</p></div><button className="rx-button" onClick={() => open({ kind: r.screen, id: r.id })}>{r.detail.includes('진행') || r.kind.includes('진행') ? '이어서' : '기록 보기'}</button></li>)}</ol> : <Empty title="선택한 기간의 활동이 없어요">기간을 넓히거나 첫 미니 모의고사를 시작해 보세요.</Empty>}</section>
    <details className="mx-panel mx-other-records"><summary>읽기 수업의 생각·근거 기록도 살펴보기</summary><LearningEvidenceReport audience="student"/></details>
  </>;
}
