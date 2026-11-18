import {RestoreAccountPanel} from './RestoreAccountPanel';
import React, { useEffect, useRef, useState } from 'react';
import { ArrowLeft, ArrowRight, BookOpen, CheckCircle2, Clock3, GraduationCap, HeartHandshake, Printer, RefreshCw, ShieldCheck, Users } from 'lucide-react';
import { examApi, examDemo } from '../../services/examApi';
import { draftStore } from '../../services/draftCache';
import type { ExamDashboard, ExamDetail, ExamForm, ExamFollowup, ExamPassage, ExamRole, ExamStatistics, ExamUser } from '../../types/exam';
import '../../exam.css';
import { BrandHeader } from '../layout/BrandHeader';
import { PageHeading, Dialog } from '../common/DesignSystem';
import { AccountForm, RosterForm } from './AccountForms';
import { MfaPanel } from './MfaPanel';
import {RestrictedAccountPanel} from './RestrictedAccountPanel';
import {ExportPurposeFields,exportPurpose} from './ExportPurpose';
import { OverviewDashboard } from '../common/OverviewDashboard';
import { OrganizationPanel } from '../admin/OrganizationPanel';
import { LearningPortal } from '../student/LearningPortal';
import { examPath, learningPath, isLearningRoute, managementPath, isManagementRoute, homePath, isHomeRoute } from '../../services/examNavigation';

const date = (at?: number) => at ? new Intl.DateTimeFormat('ko-KR', { timeZone: 'Asia/Seoul', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit', hour12: false }).format(at) : '—';
const roleNames = { teacher: '교사 수업실', student: '학생 시험실', parent: '학부모 리포트' };
const field = (data: FormData, key: string) => String(data.get(key) || '');
const localDate = (time: number) => new Date(time + 9 * 3600000).toISOString().slice(0, 16);
const fromKst = (value: string) => new Date(`${value}:00+09:00`).getTime();
const status = (value: string) => value === 'in_progress' ? '응시 중' : value === 'auto_submitted' ? '시간 종료 제출' : '제출 완료';

function Empty({ children }: { children: React.ReactNode }) { return <div className="ex-empty"><BookOpen size={28}/><p>{children}</p></div>; }
function ErrorMessage({ message }: { message: string }) { return message ? <div className="ex-error" role="alert">{message}</div> : null; }
export function ExamPortal({ requestedRole = null }: { requestedRole?: ExamRole | null }) {
  const [session, setSession] = useState<{ user: ExamUser | null; setupRequired: boolean; auth?:{stage:string} } | null>(null);
  const [dashboard, setDashboard] = useState<ExamDashboard | null>(null);
  const [detail, setDetail] = useState<ExamDetail | null>(null);
  const [error, setError] = useState(''), [busy, setBusy] = useState(false), [message, setMessage] = useState('');
  const [ready, setReady] = useState(false);
  const refresh = async () => { const d = await examApi<ExamDashboard>('/dashboard'); setDashboard(d); setSession({ user: d.user, setupRequired: false }); return d; };
  const init = async () => {
    try { const s = await examApi('/session'); setSession(s); if (s.user&&!s.user.processingRestricted&&!s.user.restoreCredentialHold&&(!s.auth||s.auth.stage==='full')) await refresh();else setDashboard(null); setError(''); }
    catch (e) { setError(e.message); } finally { setReady(true); }
  };
  useEffect(() => { init(); }, []);
  useEffect(()=>{const cleared=()=>{setSession({user:null,setupRequired:false});setDashboard(null);setDetail(null);};window.addEventListener('readx-private-session-cleared',cleared);return()=>window.removeEventListener('readx-private-session-cleared',cleared);},[]);
  useEffect(()=>{const required=()=>{setDetail(null);void init();};window.addEventListener('readx-mfa-required',required);window.addEventListener('readx-processing-changed',required);window.addEventListener('readx-restore-required',required);return()=>{window.removeEventListener('readx-mfa-required',required);window.removeEventListener('readx-processing-changed',required);window.removeEventListener('readx-restore-required',required);};},[]);
  const mfaGate=!!session?.user&&!session.user.restoreCredentialHold&&!!session.auth&&session.auth.stage!=='full';
  useEffect(() => {
    if (!session?.user || session.user.processingRestricted || session.user.restoreCredentialHold || detail || mfaGate) return;
    const timer = setInterval(() => { refresh().catch(e => { setError(e.message); if (e.status === 401) { setSession({ user: null, setupRequired: false }); setDashboard(null); } }); }, 15000);
    return () => clearInterval(timer);
  }, [session?.user?.id, !!detail,mfaGate,session?.user?.processingRestricted]);
  useEffect(()=>{if(examDemo||!session?.user||mfaGate)return;const timer=setInterval(()=>{void examApi('/session').then(s=>{if(!s.user||!!s.user.processingRestricted!==!!session.user.processingRestricted||!!s.user.restoreCredentialHold!==!!session.user.restoreCredentialHold||JSON.stringify(s.user.childIds)!==JSON.stringify(session.user.childIds)){setDetail(null);setDashboard(null);setSession(s);if(s.user&&!s.user.processingRestricted)void init();}}).catch(e=>setError(e.message));},15000);return()=>clearInterval(timer);},[session?.user?.id,session?.user?.processingRestricted,session?.user?.restoreCredentialHold,JSON.stringify(session?.user?.childIds),mfaGate]);
  const run = async (action: () => Promise<void>) => {
    if (busy) return; setBusy(true); setError(''); setMessage('');
    try { await action(); } catch (e) { setError(e.message); if (e.status === 401) { setSession({ user: null, setupRequired: false }); setDashboard(null); setDetail(null); } } finally { setBusy(false); }
  };
  const open = async (id: string, questionId?: string) => { const d = await examApi<ExamDetail>(`/attempts/${id}`); setDetail({ ...d, initialQuestionId: questionId }); window.scrollTo(0, 0); };
  const user = session?.user;
  const homeMode = !examDemo && isHomeRoute(window.location.hash);
  const recordId = /\/(?:exams|classes)\/([a-z0-9-]+)$/i.exec(window.location.hash)?.[1] || '';
  const managementMode = !examDemo && isManagementRoute(window.location.hash);
  const learningMode = !examDemo && isLearningRoute(window.location.hash);
  useEffect(() => {
    if (user && !window.location.hash.startsWith((homeMode ? homePath(user.role) : managementMode ? managementPath(user.role) : learningMode ? learningPath(user.role) : examPath(user.role))+'/') && window.location.hash !== (homeMode ? homePath(user.role) : managementMode ? managementPath(user.role) : learningMode ? learningPath(user.role) : examPath(user.role))) {
      window.history.replaceState(null, '', homeMode ? homePath(user.role) : managementMode ? managementPath(user.role) : learningMode ? learningPath(user.role) : examPath(user.role));
      window.dispatchEvent(new Event('hashchange'));
    }
  }, [user?.role, requestedRole, learningMode, managementMode, homeMode]);
  useEffect(() => { const previous=document.title; document.title=homeMode?'ReadX · 배움 기록':learningMode?'ReadX · 읽기 수업':managementMode?'ReadX · 학원 운영':'ReadX · 초5 모의고사 센터'; return ()=>{document.title=previous;}; },[homeMode,learningMode,managementMode]);
  useEffect(()=>{if(user && !user.processingRestricted && !mfaGate && recordId && !homeMode && !learningMode && !managementMode) void run(()=>open(recordId));},[recordId,user?.id,homeMode,learningMode,managementMode,mfaGate]);
  const reading = user?.role === 'student' && detail?.attempt.status === 'in_progress';
  return <>
    <BrandHeader exam={{ user: user || null, role: requestedRole, reading, busy, demo: examDemo, onLogout: () => run(async () => { await examApi('/logout', {}); setSession({ user: null, setupRequired: false }); setDashboard(null); setDetail(null); }), onOverview: () => run(async () => { if (learningMode || managementMode || homeMode) window.location.hash = examPath(user.role); setDetail(null); if (user) await refresh(); }) }}/>
    <main id="main-content" className={`rx-workspace ex-app ${reading ? "rx-workspace-reading" : ""}`} tabIndex={-1}>
      {examDemo && <div className="ex-demo-bar no-print"><div><strong>계정 없이 모의고사 체험</strong><p>답안은 이 브라우저에 저장됩니다. 제출하면 결과가 바로 열려요.</p></div><nav aria-label="모의고사 체험 역할">{(['student', 'teacher', 'parent'] as ExamRole[]).map(role => <a key={role} href={examPath(role)} aria-current={(user?.role || requestedRole || 'student') === role ? 'page' : undefined}>{role === 'student' ? '학생' : role === 'teacher' ? '교사' : '학부모'}</a>)}</nav></div>}
      <ErrorMessage message={error}/>{message && <div className="ex-success" role="status">{message}</div>}
      {!examDemo&&user?.role==='parent'&&!managementMode&&<p className="workspace-account-note"><a href={managementPath('parent')}>보호자 확인·동의와 연결 자녀 관리</a> · 계정 설정에서 안내문 확인, 동의 선택, 철회를 진행할 수 있습니다.</p>}
      {!ready ? <Empty>모의고사 센터를 여는 중입니다.</Empty> : !session || !user ? <AccountForm setup={!!session?.setupRequired} busy={busy} onSubmit={(body) => run(async () => { await examApi(session?.setupRequired ? "/setup" : "/login", body); await init(); })}/> : user.restoreCredentialHold ? <RestoreAccountPanel user={user} onChanged={init}/> : mfaGate ? <MfaPanel user={user} onChanged={init} gate/> : user.processingRestricted ? <RestrictedAccountPanel user={user} onChanged={init}/> : !dashboard ? <Empty>학급 정보를 불러오는 중입니다.</Empty> : homeMode ? <OverviewDashboard user={user}/> : managementMode ? <OrganizationPanel user={user} onChanged={init}/> : learningMode ? <LearningPortal user={user} users={dashboard.users} classes={dashboard.classes || []} initialRunId={recordId}/> : detail ? <>
          <button className="ex-back no-print" onClick={() => run(async () => { setDetail(null); await refresh(); })}><ArrowLeft size={16}/> 모의고사 목록</button>
          {user.role === 'student' && detail.attempt.status === 'in_progress' ? <ExamPlayer key={detail.attempt.id} detail={detail} user={user} onFinish={() => open(detail.attempt.id)}/> :
            <ResultView key={detail.attempt.id} detail={detail} role={user.role} busy={busy} onAction={action => run(async () => { await action(); await open(detail.attempt.id); await refresh(); })}/>}
        </> : <>
          <PageHeading eyebrow={`${user.className} · READX ASSESSMENT`} title={user.role === 'teacher' ? '우리 반의 읽기를 살펴요' : user.role === 'parent' ? '아이의 답에서 시작하는 대화' : `${user.name}의 모의고사`} description={user.role === 'teacher' ? '시험 배정부터 문항 분석, 후속 지도까지 연결합니다.' : user.role === 'parent' ? '학생 화면에서 제출한 결과와 다음 학습을 확인하세요.' : '차분히 읽고, 생각하고, 나의 답을 남겨 보세요.'} action={<button disabled={busy} onClick={() => run(async () => { await refresh(); setMessage('최신 기록을 불러왔습니다.'); })}><RefreshCw size={16}/> 새로고침</button>}/>
          <div className="ex-meta"><span><BookOpen size={15}/> 24문항</span><span><Clock3 size={15}/> 45분</span><span><ShieldCheck size={15}/> 답안 자동 저장</span><span>교사 검토용 시범 문항</span></div>
          {user.role === 'teacher' ? <TeacherDashboard dashboard={dashboard} busy={busy} onOpen={id => run(() => open(id))} onAction={action => run(async () => { await action(); await refresh(); })}/> :
            <LearnerDashboard dashboard={dashboard} busy={busy} onOpen={(id, questionId) => run(() => open(id, questionId))} onStart={id => run(async () => { const a = await examApi(`/assignments/${id}/start`, {}); await open(a.attempt.id); await refresh(); })}/>}
        </>}
      <p className="ex-report-method">창작 시범 문항 · 전국 순위나 공인 문해력 등급을 산출하지 않습니다.</p>
    </main>
  </>;
}

function TeacherDashboard({ dashboard: d, busy, onAction, onOpen }: { dashboard: ExamDashboard; busy: boolean; onAction: (a: () => Promise<void>) => void; onOpen: (id: string) => void }) {
  const [tab, setTab] = useState('exams'), [selected, setSelected] = useState<string[]>([]);
  const [stats, setStats] = useState<ExamStatistics | null>(null), [statsId, setStatsId] = useState('');
  const [preview, setPreview] = useState<ExamForm | null>(null);
  const [classId,setClassId] = useState(d.classes?.find(c=>c.active)?.id || '');
  const roster = d.users.filter(u => u.role === 'student' && (!classId || u.classId===classId));
  const pupils = roster.filter(u => u.active!==false && (!u.studentStatus || u.studentStatus==='enrolled') && (!u.validUntil || u.validUntil>d.serverNow) && (!u.consentStatus || ['granted','synthetic'].includes(u.consentStatus)));
  const name = (id: string) => d.users.find(u => u.id === id)?.name || '학생';
  const submitted = d.attempts.filter(a => a.status !== 'in_progress');
  const loadStats = (id: string) => onAction(async () => { setStats(await examApi(`/assignments/${id}/statistics`)); setStatsId(id); });
  return <>
    {!!d.classes?.length && <label>현재 반<select value={classId} onChange={e=>{setClassId(e.target.value);setSelected([]);}}>{d.classes.filter(c=>c.active).map(c=><option value={c.id} key={c.id}>{c.name}</option>)}</select></label>}
    <div className="ex-summary"><div><span>우리 반 학생</span><strong>{pupils.length}<small>명</small></strong></div><div><span>배정 회차</span><strong>{d.assignments.length}<small>회</small></strong></div><div><span>제출된 응시</span><strong>{submitted.length}<small>건</small></strong></div><div><span>보호자 공개 대기</span><strong>{submitted.filter(a => !a.parentPublishedAt).length}<small>건</small></strong></div></div>
    <nav className="ex-tabs no-print" aria-label="교사 모의고사 메뉴">{[['exams', '시험 운영'], ['roster', '학생·보호자'], ['analysis', '문항 분석']].map(([key, label]) => <button key={key} aria-current={tab === key ? 'page' : undefined} onClick={() => { setTab(key); setPreview(null); }}>{label}</button>)}</nav>
    {tab === 'roster' && <section className="ex-card"><h2><Users size={20}/> 학생과 보호자</h2>{!examDemo && <RosterForm key={`${roster.length}-${classId}`} classes={d.classes} initialClassId={classId} busy={busy} onSubmit={body => onAction(async () => { await examApi("/roster", body); })}/>}{roster.map(p => <article className="ex-person" key={p.id}><strong>{p.name}</strong><small>보호자 · {d.users.filter(u => u.role === 'parent' && u.childIds.includes(p.id)).map(u => u.name).join(', ')||'확인·동의 대기'}</small></article>)}</section>}
    {tab === 'exams' && <>
      <section className="ex-card"><div className="ex-section-title"><div><span className="ex-eyebrow">G5 · ROUND 01</span><h2>초5 수능형 문해력 모의고사 01</h2><p>독서 12 · 문학 8 · 언어·매체 4문항</p></div><button disabled={busy} onClick={() => onAction(async () => { const r = await examApi('/form'); setPreview(preview ? null : r.form); })}><BookOpen size={17}/>{preview ? '미리보기 닫기' : '시험지·해설 검토'}</button></div>
        {preview && <div className="ex-preview">{preview.passages.map(p => <section key={p.id}><Passage passage={p}/>{p.questions.map((q: any) => <div className="ex-preview-question" key={q.id}><strong>{q.number}. {q.prompt}</strong>{q.scenario && <blockquote>{q.scenario}</blockquote>}<ol>{q.options.map((o, i) => <li key={i}>{o}{i === q.answer && ' ✓ 정답'}<small>{q.reasons[i]}</small></li>)}</ol><p>{q.explanation}</p></div>)}</section>)}</div>}
        <form onSubmit={e => { e.preventDefault(); const f = new FormData(e.currentTarget); onAction(async () => { await examApi('/assignments', { title: field(f, 'title'), opensAt: fromKst(field(f, 'opens')), closesAt: fromKst(field(f, 'closes')), studentIds: selected }); setSelected([]); }); }}>
          <div className="ex-fields"><label>회차 이름<input name="title" defaultValue="초5 01회 · 우리 반 평가" required maxLength={100}/></label><label>응시 시작 (한국 시간)<input name="opens" type="datetime-local" defaultValue={localDate(d.serverNow - 60000)} required/></label><label>응시 마감 (한국 시간)<input name="closes" type="datetime-local" defaultValue={localDate(d.serverNow + 7 * 86400000)} required/></label></div>
          <fieldset><legend>배정 학생 {selected.length}명</legend>{pupils.length ? <><label className="ex-check"><input type="checkbox" checked={selected.length === pupils.length} onChange={e => setSelected(e.target.checked ? pupils.map(p => p.id) : [])}/> 전체 선택</label><div className="ex-student-checks">{pupils.map(p => <label className="ex-check" key={p.id}><input type="checkbox" checked={selected.includes(p.id)} onChange={e => setSelected(e.target.checked ? [...selected, p.id] : selected.filter(id => id !== p.id))}/>{p.name}</label>)}</div></> : <p>학생·보호자 메뉴에서 학생을 먼저 등록해 주세요.</p>}</fieldset>
          <p className="ex-muted">교사 검토용 시범 문항입니다. 출제 내용을 확인한 뒤 배정하세요. 응시는 45분이며 회차 마감이 더 이르면 그때 종료됩니다.</p><button className="ex-primary" disabled={busy || !selected.length}>선택한 학생에게 시험 배정 <ArrowRight size={16}/></button>
        </form></section>
      <h2 className="ex-heading">배정한 시험과 응시 현황</h2>{!d.assignments.length && <Empty>학생을 선택하고 첫 시험을 배정해 주세요.</Empty>}
      {d.assignments.map(a => <section key={a.id} className="ex-card"><div className="ex-section-title"><div><h3>{a.title}</h3><p>{date(a.opensAt)} ~ {date(a.closesAt)} · {a.studentIds.length}명</p></div><span className="ex-badge">{a.studentPublishedAt ? '학생 결과 공개' : '결과 비공개'}</span></div>
        <div className="ex-table-wrap"><table><thead><tr><th>학생</th><th>상태</th><th>저장 답안</th><th>최근 저장</th><th>보호자</th><th>결과</th></tr></thead><tbody>{a.studentIds.map(id => { const attempt = d.attempts.find(v => v.assignmentId === a.id && v.studentId === id); return <tr key={id}><td>{name(id)}</td><td>{attempt ? status(attempt.status) : a.closedAt ? '미응시 · 종료' : '미응시'}</td><td>{attempt ? `${attempt.answered}/24` : '—'}</td><td>{date(attempt?.lastSavedAt)}</td><td>{attempt?.parentPublishedAt ? '공개' : '비공개'}</td><td>{attempt && <button disabled={busy} onClick={() => onOpen(attempt.id)}>{attempt.status === 'in_progress' ? '진행 보기' : '개인 리포트'}</button>}</td></tr>; })}</tbody></table></div>
        {!a.studentPublishedAt && <div className="ex-release"><p>결과를 공개하면 이 회차는 종료되어 미응시 학생은 새로 시작할 수 없습니다. 응시 중인 학생이 있으면 공개되지 않습니다.</p><button disabled={busy} onClick={() => { if (window.confirm('이 회차를 종료하고 학생에게 정답·해설을 공개할까요? 미응시 학생은 이후 시작할 수 없습니다.')) onAction(async () => { await examApi(`/assignments/${a.id}/release`, {}); }); }}>회차 종료하고 학생 결과 공개</button></div>}
      </section>)}
    </>}
    {tab === 'analysis' && <section className="ex-card"><div className="ex-section-title"><h2>실제 답안으로 보는 문항 분석</h2><select aria-label="분석 회차" value={statsId} onChange={e => loadStats(e.target.value)}><option value="">회차 선택</option>{d.assignments.map(a => <option key={a.id} value={a.id}>{a.title}</option>)}</select>{statsId && <button disabled={busy} onClick={() => loadStats(statsId)}>통계 새로고침</button>}</div>
      {!stats ? <Empty>분석할 회차를 선택하세요.</Empty> : <><p>이 반의 유효 제출자 <strong>{stats.count}명</strong> / 배정 {stats.assignedCount}명 · 미제출은 정답률 분모에서 제외합니다.</p>{!stats.count ? <Empty>아직 제출된 답안이 없습니다.</Empty> : stats.rows.map(q => <details className="ex-item-stat" key={q.id}><summary><span>{String(q.number).padStart(2, '0')}</span><b>{q.prompt}</b><em>{q.correct}/{stats.count} 정답 · {Math.round(q.correct / stats.count * 100)}%</em></summary><p className="ex-muted">{q.goal} · 학생 이름을 누르면 해당 응시의 문항별 리포트로 이동합니다.</p>{q.choices.map((c, i) => <div className="ex-distribution" key={i}><div><b>{i + 1} {i === q.answer && '✓'}</b><span>{c.label}</span><strong>{c.count}명</strong></div><progress value={c.count} max={stats.count}/><div className="ex-name-list">{c.studentIds.map(id => <button key={id} onClick={() => { const a = d.attempts.find(a => a.assignmentId === statsId && a.studentId === id); if (a) onOpen(a.id); }}>{name(id)}</button>)}</div></div>)}<p>미응답 {q.unanswered.length}명 · {q.unanswered.map(name).join(', ') || '없음'}</p></details>)}</>}
    </section>}
  </>;
}

function LearnerDashboard({ dashboard: d, busy, onOpen, onStart }: { dashboard: ExamDashboard; busy: boolean; onOpen: (id: string, questionId?: string) => void; onStart: (id: string) => void }) {
  const [retryError, setRetryError] = useState('');
  const [intro, setIntro] = useState(''), [child, setChild] = useState(d.user.childIds?.[0] || d.user.id);
  const parent = d.user.role === 'parent';
  const studentId = parent ? child : d.user.id;
  const assignments = d.assignments.filter(a => a.studentIds.includes(studentId));
  return <>{parent && <label className="ex-child-select">연결 자녀<select value={child} onChange={e => setChild(e.target.value)}>{d.users.filter(u => u.role === 'student').map(u => <option key={u.id} value={u.id}>{u.name}</option>)}</select></label>}
    {!assignments.length && <Empty>{parent ? '연결 자녀에게 배정된 시험이 아직 없습니다.' : '아직 배정된 시험이 없어요. 선생님의 안내를 기다려 주세요.'}</Empty>}
    <div className="ex-exam-cards">{assignments.map(a => { const attempt = d.attempts.find(v => v.assignmentId === a.id && v.studentId === studentId); const available = d.serverNow >= a.opensAt && d.serverNow < a.closesAt && !a.closedAt;
      return <section className="ex-card ex-exam-card" key={a.id}><span className="ex-eyebrow">GRADE 5 · ROUND 01</span><h2>{a.title}</h2><p>독서 · 문학 · 언어와 매체</p><div className="ex-card-facts"><span>24문항</span><span>45분</span><span>5지선다</span></div><p className="ex-muted">응시 기간 (한국 시간)<br/>{date(a.opensAt)} ~ {date(a.closesAt)}</p>
        {parent ? attempt ? <><span className="ex-badge">공개된 시험 결과</span><button className="ex-primary" disabled={busy} onClick={() => onOpen(attempt.id)}>자녀 리포트 보기 <ArrowRight size={16}/></button></> : <p className="ex-waiting">선생님이 결과를 공개하면 자녀 리포트가 여기에 연결됩니다.</p> :
          attempt ? <><span className="ex-badge">{status(attempt.status)}</span><button className="ex-primary" disabled={busy} onClick={() => onOpen(attempt.id)}>{attempt.status === 'in_progress' ? '이어서 풀기' : a.studentPublishedAt ? '성적·문항 리포트' : '제출 확인·공개 대기'}<ArrowRight size={16}/></button></> : <button className="ex-primary" disabled={busy || !available} onClick={() => setIntro(a.id)}>{available ? '응시 안내 보기' : a.closedAt || d.serverNow >= a.closesAt ? '응시 종료' : '시작 전'}</button>}
        {intro === a.id && <div className="ex-intro"><h3>시작 전에 확인해요</h3><ul><li>6개 지문 묶음과 24문항을 풀어요.</li><li>답은 자동 저장되고, 제출 전에는 바꿀 수 있어요.</li><li>시작하면 시간이 흐르며 창을 닫아도 멈추지 않아요.</li><li>남은 응시 가능 시간: 최대 {Math.min(45, Math.max(0, Math.floor((a.closesAt - d.serverNow) / 60000)))}분.</li><li>제출 후 선생님이 결과를 공개하면 정답·해설과 리포트를 볼 수 있어요.</li></ul><button className="ex-primary" disabled={busy} onClick={() => onStart(a.id)}>시험 시작</button><button onClick={() => setIntro('')}>나중에 시작</button></div>}
      </section>;
    })}</div>
    {examDemo && !parent && <button className="ex-secondary" disabled={busy} onClick={async () => { try { setRetryError(''); const next = await examApi('/demo/new', {}); onStart(next.assignment.id); } catch (e) { setRetryError(e.message); } }}><RefreshCw size={16}/> 새로 응시하기</button>}
    <ErrorMessage message={retryError}/>
    <h2 className="ex-heading">다음 학습</h2>{!d.followups.some(f => f.studentId === studentId) ? <Empty>선생님이 문항에 맞는 보충학습을 배정하면 여기에 표시됩니다.</Empty> : d.followups.filter(f => f.studentId === studentId).map(f => <article className="ex-followup-row" key={f.id}><div><strong>{f.goal}</strong><p>{f.completedAt ? `새 글 확인 완료 · 선택 답 ${f.result?.correct ? '정답' : '오답'} · 작성 근거는 교사 확인 대상` : f.reviewedAt ? '원문 복습 완료 · 새 글 확인 대기' : '문항 근거 다시 보기'}</p></div><button disabled={busy} onClick={() => onOpen(f.attemptId, f.questionId)}>{parent ? '학습 기록 보기' : '리포트에서 학습하기'}</button></article>)}
  </>;
}

function Passage({ passage: p, evidence = [] }: { passage: ExamPassage; evidence?: string[] }) {
  return <article className="ex-passage"><span className="ex-eyebrow">{p.domain} · {p.questions[0].number}–{p.questions[p.questions.length - 1].number}번</span><h2>{p.title}</h2>{p.paragraphs.map((para, i) => <p key={para.id} id={`evidence-${para.id}`} className={evidence.includes(para.id) ? 'ex-evidence' : ''}><span className="ex-paragraph-number">{i + 1}</span>{para.text}</p>)}{p.table && <div className={evidence.includes(p.table.id) ? 'ex-evidence ex-table-wrap' : 'ex-table-wrap'}><table><caption>{p.table.caption}</caption><thead><tr>{p.table.columns.map(c => <th key={c}>{c}</th>)}</tr></thead><tbody>{p.table.rows.map((row, i) => <tr key={i}>{row.map((c, j) => <td key={j}>{c}</td>)}</tr>)}</tbody></table></div>}</article>;
}

type Pending = { id: string; choice: number | null; seq: number };
function ExamPlayer({ detail: d, user, onFinish }: { detail: ExamDetail; user: ExamUser; onFinish: () => Promise<void> }) {
  const key = `readx-exam-pending:${user.id}:${d.attempt.id}`;
  const store=draftStore(user.id);
  const pending = useRef<Record<string, Pending>>({}), sequences = useRef({ ...d.attempt.itemSeq });
  const [answers, setAnswers] = useState({ ...d.attempt.answers }), [flags, setFlags] = useState(d.attempt.flags || []);
  const flagRef = useRef(flags), dirtyFlags = useRef(false), inFlight = useRef<Promise<boolean> | null>(null);
  const [pIndex, setPIndex] = useState(0), [pane, setPane] = useState('reading'), [large, setLarge] = useState(false);
  const [hydrated,setHydrated]=useState(false),hydratedRef=useRef(false),cacheVersion=useRef(0);
  const [cacheStatus,setCacheStatus]=useState(examDemo?'체험 초안 확인 중':'암호화 초안 확인 중'),[cacheError,setCacheError]=useState('');
  const position = useRef(pIndex);
  const [error, setError] = useState(''), [saveState, setSaveState] = useState(examDemo ? '브라우저 저장 완료' : '서버 저장 완료'), [confirm, setConfirm] = useState(false), [submitting, setSubmitting] = useState(false);
  const [remaining, setRemaining] = useState(Math.max(0, Math.ceil((d.attempt.deadlineAt - d.serverNow) / 1000)));
  const clockStart = useRef(performance.now()), finished = useRef(false);
  const passages = d.form.passages, items = passages.flatMap(p => p.questions), current = passages[pIndex];
  const cache = () => {if(!hydratedRef.current)return;const version=++cacheVersion.current;setCacheStatus(examDemo?'체험 초안 저장 중':'기기 초안 암호화 중');void store.set(key,{pending:pending.current,flags:flagRef.current,dirtyFlags:dirtyFlags.current,position:position.current}).then(()=>{if(version===cacheVersion.current){setCacheStatus(examDemo?'이 브라우저에 체험 초안 보관':'암호화 기기 초안 · 복구 유효 12시간');setCacheError('');}}).catch(e=>{if(version===cacheVersion.current){setCacheStatus('기기 초안 보관 미확인 · 현재 화면에만 입력 유지');setCacheError(e.message);}});};
  useEffect(() => {
    let alive=true;
    void (async()=>{try {
      const saved = await store.get(key);if(!alive)return;
      if (saved) { const restored = { ...d.attempt.answers };
        for (const c of Object.values(saved.pending || {}) as Pending[]) if (items.some(q => q.id === c.id) && Number.isSafeInteger(c.seq) && c.seq > (sequences.current[c.id] || 0) && (c.choice === null || Number.isInteger(c.choice) && c.choice >= 0 && c.choice < 5)) { pending.current[c.id] = c; sequences.current[c.id] = c.seq; restored[c.id] = c.choice; }
        if (saved.dirtyFlags && Array.isArray(saved.flags) && saved.flags.every(id => items.some(q => q.id === id))) { flagRef.current = saved.flags; dirtyFlags.current = true; setFlags(saved.flags); }
        const n=saved.position;if(Number.isInteger(n)&&n>=0&&n<passages.length){position.current=n;setPIndex(n);}
        setAnswers(restored); if (Object.keys(pending.current).length || dirtyFlags.current) setSaveState('기기 초안 복구 · 서버 저장 대기');
      }
      setCacheStatus(saved?examDemo?'체험 초안 복구 완료':'암호화 기기 초안 복구 완료':'보관된 기기 초안 없음');
    } catch(e) {if(alive){setCacheError(e.message);setCacheStatus('기기 초안 복구 미확인 · 서버 기록 사용');}}
    finally{if(alive){hydratedRef.current=true;setHydrated(true);}}
    })();return()=>{alive=false;};
  }, [key]);
  useEffect(() => { position.current = pIndex; if(hydrated)cache(); }, [pIndex,hydrated]);
  const sync = (): Promise<boolean> => {
    if(!hydratedRef.current)return Promise.resolve(false);
    if (inFlight.current) return inFlight.current;
    const changes = Object.values(pending.current), sentFlags = [...flagRef.current], hadFlags = dirtyFlags.current;
    if (!changes.length && !hadFlags) return Promise.resolve(true);
    setSaveState('서버에 저장 중…');
    const job = (async () => {
      try {
        const r = await examApi(`/attempts/${d.attempt.id}/answers`, { changes, ...(hadFlags ? { flags: sentFlags } : {}) }, 'student');
        for (const c of changes) if (r.itemSeq[c.id] >= c.seq && pending.current[c.id]?.seq === c.seq) { delete pending.current[c.id]; sequences.current[c.id] = r.itemSeq[c.id]; setAnswers(a => ({ ...a, [c.id]: r.answers[c.id] })); }
        if (hadFlags && JSON.stringify(sentFlags) === JSON.stringify(flagRef.current)) dirtyFlags.current = false;
        cache(); setError(''); setSaveState(Object.keys(pending.current).length || dirtyFlags.current ? '추가 답안 저장 대기' : `서버 저장 완료 · ${date(r.savedAt)}`); return true;
      } catch (e) { setError(e.message); setSaveState('현재 입력 유지 · 서버 저장 미확인'); return false; }
      finally { inFlight.current = null; }
    })();
    inFlight.current = job; return job;
  };
  const syncRef = useRef(sync); syncRef.current = sync;
  useEffect(() => {
    const timer = setInterval(() => { void syncRef.current(); }, 1500);
    const beforeLeave = (e: BeforeUnloadEvent) => { if (Object.keys(pending.current).length || dirtyFlags.current) { e.preventDefault(); e.returnValue = ''; } };
    window.addEventListener('beforeunload', beforeLeave);
    const online = () => { void syncRef.current(); }; window.addEventListener('online', online);
    return () => { clearInterval(timer); window.removeEventListener('beforeunload', beforeLeave); window.removeEventListener('online', online); };
  }, []);
  useEffect(() => {
    const timer = setInterval(async () => {
      const left = Math.max(0, Math.ceil((d.attempt.deadlineAt - d.serverNow - (performance.now() - clockStart.current)) / 1000)); setRemaining(left);
      if (!left && !finished.current) { finished.current = true; try { await examApi(`/attempts/${d.attempt.id}/submit`, {}); await onFinish(); } catch (e) { setError(e.message); finished.current = false; } }
    }, 1000); return () => clearInterval(timer);
  }, []);
  const choose = (id: string, choice: number | null) => {
    if (!remaining || submitting || !hydratedRef.current) return;
    const seq = (sequences.current[id] || 0) + 1; sequences.current[id] = seq;
    pending.current[id] = { id, choice, seq }; setAnswers(a => ({ ...a, [id]: choice })); setSaveState('현재 입력 보관 · 서버 저장 대기'); cache();
  };
  const flag = (id: string) => { const next = flagRef.current.includes(id) ? flagRef.current.filter(v => v !== id) : [...flagRef.current, id]; flagRef.current = next; dirtyFlags.current = true; setFlags(next); cache(); setSaveState('표시 저장 대기'); };
  const submit = async () => {
    setSubmitting(true); try {
      if (!await sync()) return;
      if (Object.keys(pending.current).length || dirtyFlags.current) { if (!await sync()) return; }
      await examApi(`/attempts/${d.attempt.id}/submit`, {}); try { await store.remove(key); } catch { /* Server submission is already confirmed. */ } await onFinish();
    } catch (e) { setError(e.message); } finally { setSubmitting(false); }
  };
  const answered = items.filter(q => answers[q.id] != null).length;
  if(!hydrated)return <section className="ex-card" role="status">서버 답안과 보관된 초안을 확인하고 있습니다. 제한 시간은 계속 흐릅니다.</section>;
  return <section className={`ex-player ${large ? 'ex-large' : ''}`}>
    <div className="ex-exam-bar"><div><span className="ex-eyebrow">초5 · 01회</span><h1>{d.assignment.title}</h1><small role="status">{examDemo ? saveState.replace(/서버/g, "브라우저") : saveState}</small></div><div className="ex-timer" role="timer" aria-label={`남은 시간 ${Math.floor(remaining / 60)}분 ${remaining % 60}초`}><Clock3 size={20}/>{Math.floor(remaining / 60)}:{String(remaining % 60).padStart(2, '0')}</div><button aria-pressed={large} onClick={() => setLarge(!large)}>큰 글자 {large ? '켜짐' : '보기'}</button><button disabled={submitting} onClick={() => { void sync(); }}>저장 재시도</button></div>
    <ErrorMessage message={error}/><p role="status">{cacheStatus}</p>{cacheError&&<p className="ex-error" role="alert">{cacheError} 서버 저장 완료를 확인하기 전에는 이 화면을 닫지 마세요.</p>}<div className="ex-mobile-tabs"><button aria-pressed={pane === 'reading'} onClick={() => setPane('reading')}>지문 보기</button><button aria-pressed={pane === 'questions'} onClick={() => setPane('questions')}>문제 보기</button></div>
    <div className="ex-player-grid"><div className={`ex-reading-column ${pane === 'reading' ? 'ex-mobile-active' : ''}`}><Passage passage={current}/></div><div className={`ex-questions-column ${pane === 'questions' ? 'ex-mobile-active' : ''}`}>{current.questions.map(q => <article className="ex-question" id={`question-${q.id}`} key={q.id}><div className="ex-question-heading"><span>문항 {q.number}</span><button aria-pressed={flags.includes(q.id)} onClick={() => flag(q.id)}>{flags.includes(q.id) ? '★ 다시 보기 표시됨' : '☆ 다시 보기'}</button></div><h3>{q.prompt}</h3>{q.scenario && <blockquote><b>보기</b>{q.scenario}</blockquote>}<fieldset disabled={!remaining || submitting}><legend className="ex-sr">{q.number}번 답 선택</legend>{q.options.map((o, i) => <label className={`ex-option ${answers[q.id] === i ? 'selected' : ''}`} key={i}><input type="radio" name={q.id} checked={answers[q.id] === i} onChange={() => choose(q.id, i)}/><span>{i + 1}</span><b>{o}</b></label>)}</fieldset><button className="ex-clear" disabled={answers[q.id] == null || submitting} onClick={() => choose(q.id, null)}>선택 지우기</button></article>)}</div><aside className="ex-answer-map"><h3>답안 현황 <span>{answered}/24</span></h3><div className="ex-number-grid">{items.map(q => <button key={q.id} className={`${answers[q.id] != null ? 'answered' : ''} ${current.questions.some(c => c.id === q.id) ? 'current' : ''}`} aria-label={`${q.number}번 ${answers[q.id] == null ? '미응답' : '답 선택됨'} ${flags.includes(q.id) ? '다시 보기' : ''}`} onClick={() => { setPIndex(passages.findIndex(p => p.questions.some(v => v.id === q.id))); setPane('questions'); setTimeout(() => document.getElementById(`question-${q.id}`)?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 30); }}>{q.number}{flags.includes(q.id) && <sup>★</sup>}</button>)}</div><p>채운 칸: 답 선택<br/>★ 다시 보기 표시</p><div className="ex-passage-nav"><button disabled={!pIndex} onClick={() => { setPIndex(pIndex - 1); setPane('reading'); window.scrollTo(0, 0); }}>이전 지문</button><button disabled={pIndex === passages.length - 1} onClick={() => { setPIndex(pIndex + 1); setPane('reading'); window.scrollTo(0, 0); }}>다음 지문</button></div><button className="ex-primary" disabled={submitting || !remaining} onClick={() => setConfirm(true)}>답안 제출</button></aside></div>
    {confirm && <Dialog title="답안을 제출할까요?" onClose={() => { if (!submitting) setConfirm(false); }}><section className="ex-app ex-submit-dialog"><p>답한 문제 {answered}개 · 미응답 {24 - answered}개 · 다시 보기 표시 {flags.length}개</p><p>미응답은 0점으로 처리됩니다. 제출한 답은 바꿀 수 없어요.</p>{24 - answered > 0 && <div className="ex-number-grid">{items.filter(q => answers[q.id] == null).map(q => <button key={q.id} onClick={() => { setPIndex(passages.findIndex(p => p.questions.some(v => v.id === q.id))); setPane('questions'); setConfirm(false); }}>{q.number}</button>)}</div>}<ErrorMessage message={error}/><div className="ex-actions"><button autoFocus disabled={submitting} onClick={() => setConfirm(false)}>계속 풀기</button><button className="ex-primary" disabled={submitting} onClick={submit}>{submitting ? '저장·제출 중…' : '최종 제출'}</button></div></section></Dialog>}
  </section>;
}

function ResultView({ detail: original, role, busy, onAction }: { detail: ExamDetail; role: ExamRole; busy: boolean; onAction: (a: () => Promise<void>) => void }) {
  const [printDetail,setPrintDetail]=useState<ExamDetail|null>(null),[printBusy,setPrintBusy]=useState(false),[printError,setPrintError]=useState('');const d=printDetail||original;
  const [filter, setFilter] = useState('all'), [selected, setSelected] = useState(d.initialQuestionId || ''), [note, setNote] = useState(d.attempt.note || '');
  const [printing, setPrinting] = useState(false);
  const [unsynced,setUnsynced] = useState<number[]>([]),[recoveryError,setRecoveryError]=useState('');
  useEffect(()=>{if(role!=='student')return;let alive=true;void draftStore(d.attempt.studentId).get(`readx-exam-pending:${d.attempt.studentId}:${d.attempt.id}`).then(saved=>{if(!alive)return;setUnsynced((Object.values(saved?.pending||{}) as Pending[]).filter(c=>c.seq>(d.attempt.itemSeq?.[c.id]||0)).map(c=>d.form.passages.flatMap(p=>p.questions).find(q=>q.id===c.id)?.number).filter(Boolean));}).catch(e=>{if(alive)setRecoveryError(e.message);});return()=>{alive=false;};},[d.attempt.id,role]);
  const recoveryNotice = <>{recoveryError&&<p className="ex-error" role="alert">기기 초안 복구는 확인하지 못했습니다. {recoveryError} 리포트에는 서버에 저장된 답안을 사용합니다.</p>}{!!unsynced.length&&<div className="ex-error" role="alert">서버 저장을 확인하지 못한 답안이 기기에 남아 있습니다: {unsynced.join(', ')}번. 채점에는 마감 전에 서버에 저장된 답안이 사용됩니다. 이 화면을 선생님에게 보여 주세요.</div>}</>;
  useEffect(() => {
    const finish = () => {setPrinting(false);setPrintDetail(null);};
    window.addEventListener('afterprint', finish);
    return () => window.removeEventListener('afterprint', finish);
  }, []);
  useEffect(() => { if (printing) { const timer = setTimeout(() => window.print(), 100); return () => clearTimeout(timer); } }, [printing]);
  useEffect(() => { if (d.initialQuestionId) document.getElementById(`report-${d.initialQuestionId}`)?.scrollIntoView({ block: 'start' }); }, []);
  const report = d.report;
  if (!report) return <section className="ex-card ex-waiting-result">{recoveryNotice}<CheckCircle2 size={42}/><h1>{d.attempt.status === 'in_progress' ? '학생이 응시하고 있습니다' : '답안이 제출되었습니다'}</h1><p>{d.studentName} · {d.assignment.title}</p><p>{d.attempt.status === 'in_progress' ? `${d.attempt.answered}/24개 답안 저장 · 최근 저장 ${date(d.attempt.lastSavedAt)}` : `제출 시각 ${date(d.attempt.submittedAt)}`}</p><p>선생님이 회차 결과를 공개하면 성적과 해설을 확인할 수 있습니다.</p><button disabled={busy} onClick={() => onAction(async () => {})}>최신 상태 확인</button></section>;
  const rows = report.rows.filter(q => printing || filter === 'all' || filter === 'review' && q.outcome !== 'correct' || q.outcome === filter);
  return <div className="ex-report">{recoveryNotice}<PageHeading eyebrow={`${roleNames[role]} · 채점 버전 ${report.version}`} title={`${d.studentName}의 모의고사 리포트`} description={`${d.assignment.title} · ${date(d.attempt.submittedAt)} 제출`} action={<form className="no-print" onSubmit={e=>{e.preventDefault();const f=new FormData(e.currentTarget);if(printBusy)return;setPrintBusy(true);setPrintError('');void examApi(`/attempts/${d.attempt.id}/print`,exportPurpose(f)).then(fresh=>{if(!fresh.report)throw Error("현재 공개된 리포트가 없습니다.");setPrintDetail(fresh);setPrinting(true);}).catch(e=>setPrintError(e.message)).finally(()=>setPrintBusy(false));}}>{role==='teacher'&&!examDemo&&<ExportPurposeFields/>}{printError&&<p className="ex-error" role="alert">{printError}</p>}<button disabled={busy||printBusy}><Printer size={16}/> 인쇄 / PDF 준비</button></form>}/>
    <div className="ex-score-hero"><div><span>이번 시험의 결과</span><strong>{report.percent}<small>/ 100</small></strong><p>{report.correct}/{report.total}문항 정답</p></div><div className="ex-score-details"><span>정답 <b>{report.correct}</b></span><span>오답 <b>{report.wrong}</b></span><span>미응답 <b>{report.unanswered}</b></span><span>응시 시간 <b>{Math.floor(report.elapsedSec / 60)}분 {report.elapsedSec % 60}초</b></span></div></div>
    <div className="ex-two"><section className="ex-card"><h2>영역별로 살펴보기</h2>{report.domains.map(s => <div className="ex-skill" key={s.label}><div><strong>{s.label}</strong><span>{s.correct}/{s.total} · {s.percent}%</span></div><progress value={s.correct} max={s.total}/></div>)}</section><section className="ex-card"><h2>이번에 확인한 읽기 행동</h2>{report.skills.map(s => <div className="ex-skill" key={s.label}><div><strong>{s.label}</strong><span>{s.correct}/{s.total}</span></div><progress value={s.correct} max={s.total}/></div>)}<p className="ex-muted">이 시험에서 확인한 문항의 결과입니다. 확인하지 않은 능력까지 판정하지 않습니다.</p></section></div>
    <section className="ex-card"><h2>{role === 'parent' ? '아이와 함께 살펴볼 점' : '확인한 목표와 다음 학습'}</h2><div className="ex-goals">{report.goals.map(g => <article key={g.label}><b>{g.label}</b><strong>{g.correct}/{g.total}</strong><p>{g.correct === g.total ? '이번 문항에서 모두 정답을 골랐어요.' : '틀리거나 비운 문항의 근거를 다시 살펴봐요.'}</p><button className="no-print" onClick={() => { const q = report.rows.find(q => q.goal === g.label && q.outcome !== 'correct') || report.rows.find(q => q.goal === g.label); setFilter('all'); setSelected(q.id); setTimeout(() => document.getElementById(`report-${q.id}`)?.scrollIntoView({ behavior: 'smooth' }), 30); }}>관련 문항 보기</button></article>)}</div></section>
    {(d.attempt.note || role === 'teacher') && <section className="ex-card"><h2><GraduationCap size={21}/> 선생님의 지도 의견</h2>{role === 'teacher' ? <><label>학생·보호자에게 전할 관찰과 다음 활동<textarea rows={4} value={note} maxLength={2000} onChange={e => setNote(e.target.value)} placeholder="실제 응답 문항을 근거로 지도 의견을 적어 주세요."/></label><div className="ex-actions no-print"><button disabled={busy} onClick={() => onAction(async () => { await examApi(`/attempts/${d.attempt.id}/review`, { note }); })}>의견 저장</button><button className="ex-primary" disabled={busy || !d.assignment.studentPublishedAt || !note.trim()} onClick={() => onAction(async () => { await examApi(`/attempts/${d.attempt.id}/review`, { note, publish: true }); })}>이 의견과 결과를 보호자에게 공개</button>{d.attempt.parentPublishedAt && <button disabled={busy} onClick={() => onAction(async () => { await examApi(`/attempts/${d.attempt.id}/review`, { note, revoke: true }); })}>보호자 공개 회수</button>}</div><p className="ex-muted">{d.attempt.parentPublishedAt ? `보호자 공개 ${date(d.attempt.parentPublishedAt)}. 수정한 의견은 다시 공개해야 보호자에게 반영됩니다.` : '공개하면 연결된 보호자가 자신의 계정으로 리포트를 확인할 수 있습니다.'}</p></> : <p className="ex-note-text">{d.attempt.note}</p>}</section>}
    <section className="ex-card"><div className="ex-section-title"><div><span className="ex-eyebrow">ANSWER → EVIDENCE → NEXT STEP</span><h2>문항별 리포트</h2></div><select className="no-print" aria-label="문항 필터" value={filter} onChange={e => setFilter(e.target.value)}><option value="all">모든 문항</option><option value="review">오답·미응답</option><option value="correct">정답</option><option value="wrong">오답</option><option value="unanswered">미응답</option></select></div>
      {!rows.length && <Empty>이 조건에 해당하는 문항이 없습니다.</Empty>}{rows.map(q => { const p = d.form.passages.find(p => p.id === q.passageId); const followup = d.followups.find(f => f.questionId === q.id); return <details className="ex-report-item" key={q.id} id={`report-${q.id}`} open={printing || selected === q.id} onToggle={e => { if (!printing && e.currentTarget.open && selected !== q.id) setSelected(q.id); }}><summary onClick={e => { e.preventDefault(); setSelected(selected === q.id ? '' : q.id); }}><span className={`ex-outcome ${q.outcome}`}>{q.outcome === 'correct' ? '정답' : q.outcome === 'wrong' ? '오답' : '미응답'}</span><b>{q.number}. {q.prompt}</b><small>내 답 {q.choice === null ? '없음' : q.choice + 1} · 정답 {q.answer + 1}</small></summary><div className="ex-item-body"><p className="ex-muted">{q.domain} · {q.skill} · {q.goal}</p>{q.scenario && <blockquote><b>보기</b>{q.scenario}</blockquote>}<div className="ex-two"><div><h3>선지마다 이유가 있어요</h3>{q.options.map((o, i) => <div key={i} className={`ex-choice-report ${i === q.answer ? 'is-answer' : ''} ${i === q.choice ? 'is-choice' : ''}`}><strong>{i + 1}. {o}</strong><span>{i === q.answer && '✓ 정답 '}{i === q.choice && '● 내 선택'}</span><p>{q.reasons[i]}</p></div>)}</div><div><h3>판단의 근거</h3>{q.evidence.map(id => <blockquote className="ex-evidence" key={id}>{p.paragraphs.find(p => p.id === id)?.text || `${p.table?.caption}: ${p.table?.rows.map(row => row.join(' · ')).join(' / ')}`}</blockquote>)}<h3>이렇게 생각해 보세요</h3><p>{q.explanation}</p><p className="ex-observation">{q.outcome === 'correct' ? '이번 문항의 정답을 골랐습니다. 판단에 쓴 근거도 확인해 보세요.' : q.choice === null ? '답을 남기지 않았습니다. 내용을 이해하지 못했다고 단정하지 않고 추가로 확인합니다.' : `선택한 선지에서 확인할 점: ${q.reasons[q.choice]} 실제 생각은 후속 질문으로 확인합니다.`}</p>{role === 'parent' && <div className="ex-family-question"><HeartHandshake size={18}/><strong>함께 나눌 질문</strong><p>“어느 문장을 보면 이 답을 판단할 수 있을까? 다른 답 하나는 왜 고르지 않았는지 말해 줄래?”</p></div>}
      {role === 'teacher' && <button className="no-print" disabled={busy || !!followup || !d.assignment.studentPublishedAt} onClick={() => onAction(async () => { await examApi(`/attempts/${d.attempt.id}/followups`, { questionId: q.id }); })}>{followup ? '보충학습 배정됨' : '이 문항 보충·새 글 확인 배정'}</button>}</div></div><details className="ex-source-text"><summary>전체 지문과 근거 위치 펼치기</summary><Passage passage={p} evidence={q.evidence}/></details>{followup && <Followup key={`${followup.id}:${followup.reviewedAt}:${followup.completedAt}`} followup={followup} role={role} busy={busy} onAction={onAction}/>}</div></details>; })}
    </section>
    <p className="ex-report-method">문항당 1점 · 미응답 0점 · 환산점수 = 정답 수 ÷ 24 × 100 (소수 첫째 자리). 새 글 확인은 이 시험 점수에 합산하지 않습니다.</p>
  </div>;
}

function Followup({ followup: f, role, busy, onAction }: { followup: ExamFollowup; role: ExamRole; busy: boolean; onAction: (a: () => Promise<void>) => void }) {
  const [reflection, setReflection] = useState(f.reflection || ''), [choice, setChoice] = useState<number | null>(null), [evidence, setEvidence] = useState('');
  return <section className="ex-followup"><h3>다음 학습 · {f.goal}</h3>{f.reflection && <div><b>원문 복습에서 남긴 생각</b><p>{f.reflection}</p></div>}
    {role === 'student' && !f.reviewedAt && <><p>위의 본문 근거와 선지 해설을 보고, 다시 알게 된 점을 한 문장으로 적어요.</p><label>나의 복습 메모<textarea value={reflection} onChange={e => setReflection(e.target.value)} maxLength={1000} rows={3}/></label><button className="ex-primary" disabled={busy || !reflection.trim()} onClick={() => onAction(async () => { await examApi(`/followups/${f.id}/review`, { reflection }); })}>복습 기록하고 새 글 열기</button></>}
    {f.reviewedAt && f.transfer && <><h4>{f.transfer.title} <span className="ex-badge">{f.fresh ? '새 글 확인' : '이전에 열린 글 · 추가 연습'}</span></h4><p className="ex-transfer-text">{f.transfer.text}</p><strong>{f.transfer.prompt}</strong>{f.completedAt ? <><p>선택 답 {f.result.choice + 1} · 정답 {f.result.answer + 1} · {f.result.correct ? '정답 확인' : '다시 살펴보기'}</p><p>작성한 근거: {f.result.evidence}</p><blockquote>{f.result.expectedEvidence}</blockquote><p>{f.result.explanation}</p><small>작성 근거는 교사 검토 대상입니다. 선택 정답만으로 목표 달성을 확정하지 않습니다.</small></> : role === 'student' ? <><fieldset><legend>새 글의 답 선택</legend>{f.transfer.options.map((o, i) => <label className="ex-option" key={i}><input name={f.id} type="radio" checked={choice === i} onChange={() => setChoice(i)}/><span>{i + 1}</span><b>{o}</b></label>)}</fieldset><label>판단에 사용한 본문 근거<textarea rows={3} value={evidence} onChange={e => setEvidence(e.target.value)} maxLength={1000}/></label><button className="ex-primary" disabled={busy || choice === null || !evidence.trim()} onClick={() => onAction(async () => { await examApi(`/followups/${f.id}/complete`, { choice, evidence }); })}>답과 근거 제출</button></> : <p>새 글 확인을 기다리고 있습니다.</p>}</>}
    {!f.reviewedAt && role !== 'student' && <p>학생이 원문 복습을 시작하면 수행 기록이 연결됩니다.</p>}
    {f.teacherReview && <div className="ex-teacher-feedback"><strong>교사 근거 검토 · {f.teacherReview.outcome === 'supported' ? '적절한 근거 확인' : '추가 확인 필요'}</strong><p>{f.teacherReview.comment}</p><small>{f.teacherReview.teacherName} · {date(f.teacherReview.at)}</small></div>}
    {f.completedAt && role === 'teacher' && <form className="no-print" onSubmit={e => { e.preventDefault(); const data = new FormData(e.currentTarget); onAction(async () => { await examApi(`/followups/${f.id}/feedback`, { outcome: field(data, 'outcome'), comment: field(data, 'comment') }); }); }}><h4>새 글의 작성 근거 검토</h4><label>판단<select name="outcome" defaultValue={f.teacherReview?.outcome || 'supported'}><option value="supported">적절한 근거 확인</option><option value="needs_review">추가 확인 필요</option></select></label><label>후속 지도 의견<textarea name="comment" required maxLength={1000} defaultValue={f.teacherReview?.comment || ''}/></label><button disabled={busy}>근거 검토 저장</button></form>}
  </section>;
}

