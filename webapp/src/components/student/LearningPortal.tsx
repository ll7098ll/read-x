import React, { useEffect, useRef, useState } from 'react';
import { ArrowRight, ArrowLeft, Plus, Search, RefreshCw, BookOpen } from 'lucide-react';
import { examApi } from '../../services/examApi';
import type { ExamUser } from '../../types/exam';
import type { ProgressiveLesson } from '../../data/progressiveReading';
import type { ProgressiveRun } from '../../services/progressiveReading';
import type { ReadingLevel } from '../../data/readingPolicy';
import { draftStore } from '../../services/draftCache';
import { ProgressiveLessonView } from './ProgressiveReadingStudio';
import { PlacementJourney } from './PlacementJourney';
import { CalibrationApplicationPanel } from '../teacher/CalibrationApplicationPanel';
import { PilotWorkspace } from '../teacher/PilotWorkspace';

const levelNames = { supported: '도움글', standard: '기준글', challenge: '도전글' };
const when = (at: number) => new Date(at).toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' });
export function LearningPortal({ user, users, classes=[], initialRunId='' }: { user: ExamUser; users: ExamUser[]; classes?: any[]; initialRunId?: string }) {
  const [classId,setClassId]=useState(classes.find(c=>c.active)?.id || '');
  const [data, setData] = useState<any>({ assignments: [], runs: [] });
  const [catalog, setCatalog] = useState<any[]>([]), [detail, setDetail] = useState<any>(null);
  const [preview, setPreview] = useState<any>(null), [grade, setGrade] = useState(5);
  const [error, setError] = useState(''), [busy, setBusy] = useState(false);
  const [query,setQuery]=useState(''),[view,setView]=useState('all'),[showComposer,setShowComposer]=useState(false);
  const assignmentRuns=(id:string)=>data.runs.filter(r=>r.assignmentId===id);
  const needsReview=(id:string)=>assignmentRuns(id).some(r=>r.status==='submitted');
  const unfinished=(a:any)=>a.studentIds.some(id=>{const r=assignmentRuns(a.id).find(r=>r.studentId===id);return !r||r.status==='in_progress';});
  const visibleAssignments=data.assignments.filter(a=>a.title.toLowerCase().includes(query.trim().toLowerCase())&&(view==='all'||(view==='active'?unfinished(a):user.role==='teacher'?needsReview(a.id):!unfinished(a))));
  const refresh = async () => {
    setData(await examApi('/learning/dashboard'));
    if (user.role === 'teacher') setCatalog((await examApi('/learning/catalog')).lessons);
  };
  useEffect(() => { void (async()=>{await refresh();if(initialRunId)await open(initialRunId);})().catch(e=>setError(e.message)); }, [user.id,initialRunId]);
  const act = async (fn: () => Promise<void>) => { if (busy) return; setBusy(true); setError(''); try { await fn(); } catch (e) { setError(e.message); } finally { setBusy(false); } };
  const open = async (id: string) => {setDetail(await examApi(`/learning/runs/${id}`));window.scrollTo(0,0);};
  return <section className="ex-app workspace-learning">
    {error && <p className="ex-error" role="alert">{error}</p>}
    {detail ? <><button className="ex-back" disabled={busy} onClick={() => act(async () => { setDetail(null); await refresh(); window.scrollTo({top:0,behavior:"instant" as ScrollBehavior}); })}><ArrowLeft size={16}/> 수업 목록으로</button>
      {user.role === 'student' && detail.status === 'in_progress' ? <LearningPlayer key={detail.id} initial={detail} user={user} onSubmitted={setDetail}/> : <LearningReport key={detail.id} detail={detail} user={user} busy={busy} onReview={body => act(async () => setDetail(await examApi(`/learning/runs/${detail.id}/review`, body)))} onRevoke={() => act(async () => { await examApi(`/learning/runs/${detail.id}/revoke`, {}); await open(detail.id); })}/>}
    </> : <>
      <PilotWorkspace key={user.id} user={user}/>
      <CalibrationApplicationPanel key={user.id} user={user}/>
      <PlacementJourney user={user} onChanged={refresh} onStart={async (id:string)=>{setDetail(await examApi(`/learning/assignments/${id}/start`,{}));window.scrollTo(0,0);}}/>
      <header className="workspace-heading"><div><p className="rx-eyebrow">{user.role==='teacher'?'선생님 수업실':user.role==='parent'?'우리 아이의 배움':'나의 배움터'}</p><h1>{user.role === 'teacher' ? '한 편의 글, 깊어지는 수업.' : user.role === 'parent' ? '아이의 읽기를 함께 따라가요.' : '오늘의 읽기를 시작해요.'}</h1><p>{user.role==='teacher'?'수업을 배정하고, 학생이 남긴 근거와 설명을 살펴보세요.':user.role==='parent'?'선생님이 공개한 아이의 응답과 지도 의견을 확인하세요.':'내게 도착한 수업을 고르고, 하던 읽기를 이어가요.'}</p></div><div className="ex-actions">{user.role==='teacher'&&<button className="ex-primary" onClick={()=>setShowComposer(!showComposer)} aria-expanded={showComposer} aria-controls="lesson-composer"><Plus size={17}/>{showComposer?'수업 준비 닫기':'새 수업 준비'}</button>}<button disabled={busy} aria-label="수업 목록 새로고침" onClick={() => act(refresh)}><RefreshCw size={17}/><span>새로고침</span></button></div></header>
      <div className="workspace-summary-strip"><span><b>{data.assignments.length}</b> {user.role==='parent'?'배정된 수업':'전체 수업'}</span>{user.role!=='parent'&&<span><b>{data.assignments.filter(unfinished).length}</b> 진행할 수업</span>}<span><b>{user.role==='teacher'?data.runs.filter(r=>r.status==='submitted').length:data.runs.filter(r=>r.status!=='in_progress').length}</b> {user.role==='teacher'?'검토 대기 응답':user.role==='parent'?'공개된 기록':'제출한 기록'}</span></div>
      {user.role === 'teacher' && showComposer && <section id="lesson-composer" className="ex-card workspace-composer"><h2>지문 검토와 수업 배정</h2>{!!classes.length&&<label>배정할 반<select value={classId} onChange={e=>setClassId(e.target.value)}>{classes.filter(c=>c.active).map(c=><option key={c.id} value={c.id}>{c.name}</option>)}</select></label>}<label>학년<select value={grade} onChange={e => { setGrade(Number(e.target.value)); setPreview(null); }}>{[1,2,3,4,5,6].map(g => <option key={g} value={g}>{g}학년</option>)}</select></label>
        <label>수업<select value={preview?.lesson.id || ''} onChange={e => { const id = e.target.value; if (id) void act(async () => setPreview(await examApi(`/learning/catalog/${id}`))); else setPreview(null); }}><option value="">검토할 수업 선택</option>{catalog.filter(l => l.grade === grade).map(l => <option key={l.id} value={l.id}>{l.title} · {l.approved ? '시범 승인' : '검토 대기'}</option>)}</select></label>
        {preview && <TeacherLesson key={preview.lesson.id} preview={preview} approved={!!catalog.find(l => l.id === preview.lesson.id)?.approved} students={users.filter(u => u.role === 'student' && (!classId || u.classId===classId) && u.active!==false && (!u.studentStatus || u.studentStatus==='enrolled') && (!u.consentStatus||['granted','synthetic'].includes(u.consentStatus)))} busy={busy} onApprove={body => act(async () => { await examApi('/learning/approvals', body); await refresh(); })} onAssign={body => act(async () => { await examApi('/learning/assignments', body); setPreview(null); await refresh(); })}/>}
      </section>}
      <div className="workspace-list-toolbar"><nav className="workspace-list-tabs" aria-label="수업 보기">{(user.role==='parent'?[['all','모든 수업']]:[['all','전체'],['active','진행할 수업'],['done',user.role==='teacher'?'검토 대기':'제출한 수업']]).map(([id,label])=><button key={id} aria-pressed={view===id} onClick={()=>setView(id)}>{label}</button>)}</nav><label className="workspace-search"><Search size={18}/><input aria-label="배정된 수업 검색" placeholder="수업 이름으로 찾기" value={query} onChange={e=>setQuery(e.target.value)}/></label></div>
      {!visibleAssignments.length && <div className="ex-empty"><BookOpen size={28}/><h2>{data.assignments.length?'조건에 맞는 수업이 없어요':'아직 배정된 수업이 없어요'}</h2><p>{data.assignments.length?'검색어나 보기 조건을 바꿔 보세요.':user.role==='teacher'?'새 수업 준비에서 지문을 고르고 학생에게 배정하세요.':'수업이 배정되면 이곳에서 확인할 수 있어요.'}</p></div>}
      {visibleAssignments.map(a => <section className="ex-card workspace-assignment" key={a.id}><div className="workspace-assignment-heading"><span className="workspace-course-index"><BookOpen size={22}/></span><div><span className="rx-eyebrow">교과 읽기 · {a.grade}학년</span><h2>{a.title}</h2></div></div><p className="workspace-assignment-meta">{a.grade}학년 · {levelNames[a.level]} · 제출 기한 {when(a.dueAt)}</p>
        {user.role === 'teacher' && <button disabled={busy} onClick={() => act(async () => { await examApi(`/learning/assignments/${a.id}/extend`, { dueAt:Math.max(Date.now(),a.dueAt)+7*86400000, reason:'추가 학습 시간 제공' }); await refresh(); })}>제출 기한 7일 연장</button>}
        {user.role === 'student' ? <button className="ex-primary" disabled={busy} onClick={() => act(async () => {setDetail(await examApi(`/learning/assignments/${a.id}/start`, {}));window.scrollTo({top:0,behavior:"instant" as ScrollBehavior});})}>{assignmentRuns(a.id).some(r=>r.status==='in_progress')?'이어서 읽기':assignmentRuns(a.id).length?'수업 기록 보기':'읽기 시작하기'} <ArrowRight size={17}/></button> : <>
          {a.studentIds.map(id => { const r = data.runs.find(r => r.assignmentId === a.id && r.studentId === id); return <div className="ex-followup-row" key={id}><b>{users.find(u => u.id === id)?.name || '학생'}</b><span className="workspace-status" data-status={r?.status || 'not_started'}>{!r ? user.role === 'parent' ? '아직 공개된 기록이 없습니다.' : '시작 전' : r.status === 'in_progress' ? '학습 중' : r.status === 'submitted' ? '교사 검토 대기' : '검토·공개 기록'}</span>{r && <button disabled={busy} onClick={() => act(() => open(r.id))}>수업 기록 보기</button>}</div>; })}
        </>}
      </section>)}
    </>}
  </section>;
}

function TeacherLesson({ preview, approved, students, busy, onApprove, onAssign }: any) {
  const lesson: ProgressiveLesson = preview.lesson;
  const [level, setLevel] = useState<ReadingLevel>('standard');
  const ps = ['supported','standard','challenge'].slice(0, ['supported','standard','challenge'].indexOf(level)+1).flatMap(l => lesson.layers[l]);
  return <>
    <label>글 수준<select value={level} onChange={e => setLevel(e.target.value as ReadingLevel)}>{Object.entries(levelNames).map(([v,n]) => <option key={v} value={v}>{n}</option>)}</select></label>
    <details><summary>전체 지문과 문항·해설 검토</summary><h3>{lesson.title}</h3>{ps.map(p => <p key={p.id}>{p.text}</p>)}{(lesson.levelQuestions?.[level] || lesson.questions).map(q => <article key={q.id}><h4>{q.prompt}</h4>{q.scenario && <p>{q.scenario}</p>}<ol>{q.options.map((o,i) => <li key={i}>{o}{i === q.answer ? ' · 정답' : ''}<p>{q.optionReasons[i]}</p></li>)}</ol><p>{q.explanation}</p></article>)}</details>
    {!approved ? <form onSubmit={e => { e.preventDefault(); const f = new FormData(e.currentTarget); onApprove({ lessonId: lesson.id, contentHash: preview.contentHash, note: String(f.get('note')), pilot: true }); }}><p>교사 검토 대기 콘텐츠입니다. 학년·정답·근거·설명을 확인한 후 시범 수업으로 승인해 주세요.</p><label>검토 의견<textarea name="note" required maxLength={2000}/></label><label><input type="checkbox" required/> 지문과 문항을 검토했고 시범 수업 배정에 동의합니다.</label><button disabled={busy}>검토 기록과 시범 승인</button></form> : <form onSubmit={e => { e.preventDefault(); const f = new FormData(e.currentTarget); onAssign({ lessonId: lesson.id, level, title: String(f.get('title')), dueAt: Date.now()+Number(f.get('days'))*86400000, studentIds: f.getAll('student') }); }}><label>과제 이름<input name="title" defaultValue={lesson.title} required maxLength={100}/></label><label>제출 기간<select name="days"><option value="7">7일</option><option value="14">14일</option><option value="1">1일</option></select></label><fieldset><legend>배정 학생</legend>{students.map(s => <label className="ex-check" key={s.id}><input type="checkbox" name="student" value={s.id}/>{s.name}</label>)}</fieldset><button className="ex-primary" disabled={busy}>선택한 학생에게 수업 배정</button></form>}
  </>;
}

function LearningPlayer({ initial, user, onSubmitted }: any) {
  const key = `readx-learning:${user.id}:${initial.id}`;
  const store=draftStore(user.id);
  const [current, setCurrent] = useState<any>({ run: initial.run, writing: initial.writing, revision: initial.revision, dirty: false, request: null, editVersion: 0 });
  const latest = useRef(current), inFlight = useRef<Promise<boolean> | null>(null);
  const [status, setStatus] = useState('서버 저장 완료'),[hydrated,setHydrated]=useState(false),hydratedRef=useRef(false);
  const [cacheStatus,setCacheStatus]=useState('암호화 초안 확인 중'),[cacheError,setCacheError]=useState('');
  const cacheVersion=useRef(0);
  const [error, setError] = useState(''), [submitting, setSubmitting] = useState(false);
  const conflict = useRef(false);
  const [conflictDraft, setConflictDraft] = useState<any>(null);
  const cache=(name:string,next:any)=>{const version=++cacheVersion.current;setCacheStatus('기기 초안 암호화 중');void store.set(name,next).then(()=>{if(version===cacheVersion.current){setCacheStatus('암호화 기기 초안 · 복구 유효 12시간');setCacheError('');}}).catch(e=>{if(version===cacheVersion.current){setCacheStatus('기기 초안 보관 미확인 · 현재 화면에만 입력 유지');setCacheError(e.message);}});};
  const update = (next: any) => { latest.current = next; setCurrent(next); cache(key,next); };
  useEffect(()=>{let alive=true;void (async()=>{
    try{const [saved,backup]=await Promise.all([store.get(key),store.get(key+':conflict')]);if(!alive)return;setConflictDraft(backup);
      if(saved&&(saved.revision===initial.revision||saved.request?.mutationId===initial.lastMutationId)){const restored={...saved,revision:initial.revision,request:saved.request?.mutationId===initial.lastMutationId?null:saved.request};latest.current=restored;setCurrent(restored);setStatus(restored.dirty?'기기 초안 복구 · 서버 저장 대기':'서버 저장 완료');setCacheStatus('암호화 기기 초안 복구 완료');}
      else if(saved){setConflictDraft(saved);cache(key+':conflict',saved);}
      else setCacheStatus('현재 입력은 서버에 자동 저장합니다. 기기 초안은 암호화하여 보관합니다.');
    }catch(e){if(alive){setCacheError(e.message);setCacheStatus('기기 초안 복구 미확인 · 서버 기록 사용');}}
    finally{if(alive){hydratedRef.current=true;setHydrated(true);}}
  })();return()=>{alive=false;};},[key]);
  const setRun: React.Dispatch<React.SetStateAction<ProgressiveRun>> = action => { const old = latest.current; update({ ...old, run: typeof action === 'function' ? action(old.run) : action, dirty: true, editVersion: (old.editVersion || 0)+1 }); setStatus('현재 입력 보관 · 서버 저장 대기'); };
  const save = (): Promise<boolean> => {
    if(!hydratedRef.current)return Promise.resolve(false);
    if (conflict.current) return Promise.resolve(false);
    if (inFlight.current) return inFlight.current;
    if (!latest.current.dirty) return Promise.resolve(true);
    const before = latest.current;
    const request = before.request || { editVersion: before.editVersion || 0, revision: before.revision, mutationId: crypto.randomUUID(), run: JSON.parse(JSON.stringify(before.run, (key,value) => ['passageSnapshot','questionSnapshot','annotationHistory','archives'].includes(key) ? undefined : value)), writing: before.writing };
    update({ ...before, request }); setStatus('서버 저장 중…');
    const job = (async () => {
      try {
        const saved = await examApi(`/learning/runs/${initial.id}/save`, request);
        const newer = (latest.current.editVersion || 0) !== request.editVersion;
        update({ ...latest.current, run: newer ? latest.current.run : { ...saved.run, annotationHistory: latest.current.run.annotationHistory }, revision: saved.revision, request: null, dirty: newer });
        setStatus(newer ? '추가 입력 저장 대기' : '서버 저장 완료'); setError(''); return true;
      } catch (e) { if (e.status === 409) { conflict.current = true; setConflictDraft(structuredClone(latest.current)); cache(key+':conflict',latest.current); } setStatus('현재 입력 유지 · 서버 저장 미확인'); setError(e.message); return false; }
      finally { inFlight.current = null; }
    })();
    inFlight.current = job; return job;
  };
  const saveRef = useRef(save); saveRef.current = save;
  useEffect(() => {
    const timer = setInterval(() => { void saveRef.current(); }, 1800);
    const unload = (e: BeforeUnloadEvent) => { if (latest.current.dirty) { e.preventDefault(); e.returnValue = ''; } };
    window.addEventListener('beforeunload', unload);
    return () => { clearInterval(timer); window.removeEventListener('beforeunload', unload); };
  }, []);
  return <div className="workspace-player">
    <header className="pr-heading"><h1>{initial.assignment.title}</h1>{initial.lesson.grade<=2&&<p>짧은 낱말이나 한 문장으로 내 생각을 적어도 괜찮아요. 시범을 보고 선생님과 함께 연습해요.</p>}<p>{levelNames[initial.assignment.level]} · 제출 기한 {when(initial.assignment.dueAt)}</p><div className="workspace-save-status"><p role="status">{status}</p><details><summary>저장 안내</summary><p>{cacheStatus}</p></details><button onClick={() => void save()} disabled={submitting||!hydrated}>{error?"저장 재시도":"지금 저장"}</button></div></header>
    {error && <p role="alert" className="ex-error">{error}</p>}
    {cacheError&&<p role="alert" className="ex-error">{cacheError} 서버 저장 완료를 확인하기 전에는 이 화면을 닫지 마세요.</p>}
    {!hydrated&&<p role="status">보관된 초안을 확인하고 있습니다.</p>}
    {conflictDraft && <section className="ex-card"><h2>다른 화면에서 수업 기록이 바뀌었습니다</h2><p>현재 입력을 아래에 보관했습니다. 서버 기록을 다시 불러온 뒤 필요한 내용을 비교해 옮겨 주세요.</p><details><summary>보관한 내 설명과 답</summary><p>{conflictDraft.writing}</p>{Object.entries(conflictDraft.run.responses).map(([id,r]: any) => <p key={id}>{r.reason}</p>)}</details><button disabled={submitting || !conflict.current} onClick={async () => { try { const fresh = await examApi(`/learning/runs/${initial.id}`); if (fresh.status !== 'in_progress') { onSubmitted(fresh); return; } conflict.current = false; update({ run:fresh.run, writing:fresh.writing, revision:fresh.revision, dirty:false, request:null, editVersion:0 }); setStatus('최신 서버 기록을 불러왔습니다.'); setError(''); } catch (e) { setError(e.message); } }}>최신 서버 기록 불러오기</button></section>}
    {hydrated&&<fieldset className="workspace-player-content" disabled={submitting || conflict.current}><ProgressiveLessonView sourceLesson={initial.lesson} level={initial.assignment.level} run={current.run} setRun={setRun} serverManaged/>
      <section className="ex-card workspace-final-writing"><p className="rx-eyebrow">마지막으로 정리해요</p><h2>오늘의 읽기를 나의 말로.</h2><label>내 말로 설명하기<textarea rows={initial.lesson.grade<=2?2:5} value={current.writing} maxLength={10000} placeholder={initial.lesson.grade<=2?"오늘 배운 것을 짧게 적어요.":"오늘 배운 관계나 판단 방법을 내 말로 설명해요."} onChange={e => { update({ ...latest.current, writing: e.target.value, dirty: true, editVersion: (latest.current.editVersion || 0)+1 }); setStatus('현재 입력 보관 · 서버 저장 대기'); }}/></label>
        <p>제출 후에는 선생님이 답과 근거, 설명을 함께 검토합니다.</p>
        <button className="ex-primary" disabled={submitting||!hydrated} onClick={async () => { setSubmitting(true); try { for (let i=0; i<3 && latest.current.dirty; i++) if (!await save()) return; if (latest.current.dirty) return; const submitted = await examApi(`/learning/runs/${initial.id}/submit`, { revision: latest.current.revision }); try { await Promise.all([store.remove(key),store.remove(key+':conflict')]); } catch {} onSubmitted(submitted); } catch (e) { setError(e.message); } finally { setSubmitting(false); } }}>{submitting ? '저장·제출 중…' : '수업 제출'}</button>
      </section>
    </fieldset>}
  </div>;
}

function LearningReport({ detail: d, user, busy, onReview, onRevoke }: any) {
  const [reviews, setReviews] = useState(d.reviews || {}), [note, setNote] = useState(d.note || '');
  const reportRef = useRef<HTMLElement>(null);
  useEffect(() => {
    let previous: Array<{ element: HTMLDetailsElement; open: boolean }> = [];
    const expandForPrint = () => {
      previous = Array.from(reportRef.current?.querySelectorAll<HTMLDetailsElement>('.workspace-response-record') || []).map(element => ({ element, open: element.open }));
      previous.forEach(({element}) => { element.open = true; });
    };
    const restore = () => { previous.forEach(({element,open}) => { element.open = open; }); previous = []; };
    window.addEventListener('beforeprint', expandForPrint);
    window.addEventListener('afterprint', restore);
    return () => { window.removeEventListener('beforeprint', expandForPrint); window.removeEventListener('afterprint', restore); restore(); };
  }, []);
  const teacher = user.role === 'teacher', submitted = d.status !== 'in_progress';
  return <section ref={reportRef} className="ex-report workspace-learning-report"><h1>{d.studentName}의 읽기 수업 기록</h1><p>{d.assignment.title} · {levelNames[d.assignment.level]} · {d.report.submitted}/{d.report.total}개 활동 응답</p><p>처음 답·도움·수정 답을 함께 확인합니다. 같은 글의 연습을 새 글 독립 수행으로 집계하지 않습니다.</p>
    {!teacher&&<section className="ex-card workspace-report-note"><p className="rx-eyebrow">선생님과 이어가는 배움</p><h2>선생님의 종합 의견</h2><p>{d.note || '선생님이 검토하면 피드백이 표시됩니다.'}</p></section>}
    {d.report.rows.map((row,index) => <details className="ex-card workspace-response-record" open={teacher || undefined} key={row.questionId}><summary><span>{String(index+1).padStart(2,'0')}</span><b>{row.skill}</b><span>{row.review?'피드백 있음':'설명 검토 전'}</span></summary><h3>{row.prompt}</h3>{row.submissions.map((s,i) => <article className="pr-record" key={s.id}><b>{i === 0 ? '첫 응답' : `${i}번째 수정`} · 도움 {s.hintLevel}단계</b><p>선택 답: {s.choice === null ? '서술 응답' : s.choice+1} · 선택 확인: {s.choiceMatch === null ? '교사 검토 대상' : s.choiceMatch ? '맞음' : '다시 확인'} · 필요 근거 {s.evidenceMatch ? '포함' : '추가 확인'}</p><p>내 설명: {s.reason}</p><p>근거: {s.evidence.map(id => { const p = Object.values(d.lesson.layers).flat().find((p: any) => p.id === id) as any; return p?.text || id; }).join(' / ')}</p>{s.annotations?.map(a => <p key={a.id}>생각 표시: {a.quote} · {a.note}</p>)}</article>)}
      {teacher && submitted ? <><label>설명과 근거 판단<select value={reviews[row.questionId]?.outcome || ''} onChange={e => setReviews({ ...reviews, [row.questionId]: { ...reviews[row.questionId], outcome: e.target.value } })}><option value="">판단 선택</option><option value="success">적절한 설명과 근거 확인</option><option value="needs_support">다음 지도가 필요함</option></select></label><label>지도 의견<textarea maxLength={2000} value={reviews[row.questionId]?.note || ''} onChange={e => setReviews({ ...reviews, [row.questionId]: { ...reviews[row.questionId], note: e.target.value } })}/></label></> : row.review ? <p className="ex-success">선생님 의견: {row.review.note}</p> : <p>교사 검토 전</p>}
    </details>)}
    <section className="ex-card"><h2>내 말로 설명하기</h2><p className="ex-note-text">{d.writing || '작성 전'}</p>{teacher && <details><summary>글 수정 기록 {d.writingHistory?.length || 0}개</summary>{d.writingHistory?.map((w,i) => <p key={i}>{when(w.at)} · {w.text}</p>)}</details>}</section>
    {teacher && submitted ? <section className="ex-card"><label>종합 지도 의견<textarea value={note} maxLength={2000} onChange={e => setNote(e.target.value)}/></label><div className="ex-actions"><button disabled={busy} onClick={() => onReview({ reviews, note, revision: d.revision })}>검토 저장</button><button className="ex-primary" disabled={busy} onClick={() => onReview({ reviews, note, publish: true, revision: d.revision })}>검토 결과를 보호자에게 공개</button>{d.publishedAt && <button disabled={busy} onClick={onRevoke}>보호자 공개 회수</button>}</div></section> : null}
  </section>;
}
