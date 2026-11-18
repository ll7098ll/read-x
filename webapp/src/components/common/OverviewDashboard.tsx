import React, { useEffect, useRef, useState } from 'react';
import { ArrowUpRight, MessageCircle, Search } from 'lucide-react';
import { examApi } from '../../services/examApi';
import { examPath, learningPath, managementPath } from '../../services/examNavigation';
import type { ExamUser } from '../../types/exam';
import '../../overview.css';
import {ExportPurposeFields,exportPurpose} from '../exam/ExportPurpose';

type Ratio = { numerator:number;denominator:number;percent:number|null };
const day = (at:number) => new Date(at+9*3600000).toISOString().slice(0,10);
const text = (r?:Ratio) => r?.percent == null ? '—' : `${r.percent}%`;
const count = (r?:Ratio) => !r?.denominator ? '확인할 기록 없음' : `${r.numerator} / ${r.denominator}`;
const status = { not_started:'시작 전',in_progress:'학습 중',submitted:'제출·검토 대기',reviewed:'교사 검토',published:'보호자 공개',awaiting_release:'아직 공개된 결과 없음' };
const date = (at:number) => new Date(at).toLocaleString('ko-KR',{timeZone:'Asia/Seoul'});
function Metric({label,value,description}:{label:string;value?:Ratio;description:string}) {
  return <article className="ov-metric"><h3>{label}</h3><strong>{text(value)}</strong><span>{count(value)}</span><details><summary>집계 기준</summary><p>{description}</p></details></article>;
}
export function OverviewDashboard({ user }:{user:ExamUser}) {
  const [filters,setFilters]=useState({startDate:day(Date.now()-27*86400000),endDate:day(Date.now()),classId:'',studentId:''});
  const [data,setData]=useState<any>(null),[options,setOptions]=useState<any>({classes:[],students:[]});
  const [error,setError]=useState(''),[busy,setBusy]=useState(false),[refresh,setRefresh]=useState(0),[message,setMessage]=useState('');
  const generation=useRef(0);
  useEffect(()=>{
    const id=++generation.current;setBusy(true);setError('');setData(null);
    void examApi('/overview',filters).then(d=>{if(id===generation.current){setData(d);setOptions({classes:d.classes,students:d.students});}}).catch(e=>{if(id===generation.current)setError(e.message);}).finally(()=>{if(id===generation.current)setBusy(false);});
    return ()=>{generation.current++;};
  },[user.id,filters.startDate,filters.endDate,filters.classId,filters.studentId,refresh]);
  return <section className="ov-dashboard">
    <header className="ov-heading"><div><p className="rx-eyebrow">{user.role==='teacher'?'선생님 수업실':user.role==='parent'?'우리 아이의 배움':'나의 배움터'}</p><h1>{user.role==='student'?`${user.name}님, 오늘도 한 편 읽어 볼까요?`:user.role==='parent'?'아이의 생각이 자라는 순간.':'오늘의 수업, 다음 배움까지.'}</h1><p>{user.role==='teacher'?'살펴볼 응답을 확인하고, 학생에게 필요한 다음 수업을 준비하세요.':user.role==='parent'?'아이가 남긴 생각과 선생님의 피드백을 함께 살펴보세요.':'하던 수업을 이어가고, 선생님의 피드백을 만나 보세요.'}</p></div><nav aria-label="학습 바로가기" className="no-print"><a className="rx-button rx-button-primary" href={learningPath(user.role)}>{user.role==='teacher'?'수업 준비·응답 검토':user.role==='parent'?'아이의 읽기 기록':'나의 읽기 수업'}<ArrowUpRight size={18}/></a><a className="rx-button" href={examPath(user.role)}>모의고사</a>{user.role==='teacher'&&<a className="rx-button" href={managementPath(user.role)}>반·학생 관리</a>}</nav></header>
    <div className="workspace-period no-print"><span>살펴볼 기간</span>{[7,28,90].map(days=><button key={days} type="button" aria-pressed={filters.startDate===day(Date.now()-(days-1)*86400000)&&filters.endDate===day(Date.now())} onClick={()=>setFilters({...filters,startDate:day(Date.now()-(days-1)*86400000),endDate:day(Date.now())})}>최근 {days===28?'4주':days===90?'3개월':'7일'}</button>)}</div>
    <details className="workspace-filter-options no-print"><summary>기간·학생 상세 설정 <span>{filters.startDate} ~ {filters.endDate}</span></summary><form className="ov-filters" onSubmit={e=>{e.preventDefault();setRefresh(v=>v+1);}}>
      <label>배정 시작일<input type="date" required value={filters.startDate} onChange={e=>setFilters({...filters,startDate:e.target.value})}/></label><label>배정 종료일<input type="date" required value={filters.endDate} onChange={e=>setFilters({...filters,endDate:e.target.value})}/></label>
      {user.role==='teacher'&&<label>반<select value={filters.classId} onChange={e=>setFilters({...filters,classId:e.target.value,studentId:''})}><option value="">담당 범위 전체</option>{options.classes.map(c=><option key={c.id} value={c.id}>{c.name}{c.active?'':' · 종료'}</option>)}</select></label>}
      {user.role!=='student'&&<label>{user.role==='parent'?'자녀':'학생'}<select value={filters.studentId} onChange={e=>setFilters({...filters,studentId:e.target.value})}><option value="">전체</option>{options.students.map(s=><option key={s.id} value={s.id}>{s.name}</option>)}</select></label>}
      <button disabled={busy}>새로고침</button>
    </form></details>
    {busy&&<p role="status">기록을 불러오는 중입니다.</p>}{error&&<p className="ex-error" role="alert">{error}</p>}{message&&<p className="ex-success no-print" role="status">{message}</p>}
    {data&&<><form className="ex-card no-print" onSubmit={async e=>{e.preventDefault();if(busy)return;const f=new FormData(e.currentTarget),kind=String(f.get('kind'));setBusy(true);setError('');try{const stamp=generation.current;const d=await examApi('/overview/'+kind,{...filters,...exportPurpose(f)});if(stamp!==generation.current)throw Error('조회 조건이 바뀌었습니다. 최신 범위를 확인한 뒤 다시 시도해 주세요.');if(kind==='export'){const url=URL.createObjectURL(new Blob([d.csv],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download=`ReadX-${data.startDate}-${data.endDate}.csv`;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);setMessage(`${d.records}건의 CSV 전달을 기록했습니다. 파일은 안전하게 보관하세요.`);}else{setData(d);setTimeout(()=>window.print(),100);setMessage('현재 권한으로 인쇄 준비 요청을 기록했습니다.');}}catch(e){setError(e.message);}finally{setBusy(false);}}}><fieldset disabled={busy}><legend>현재 조회 범위 내보내기</legend>{user.role==='teacher'&&<ExportPurposeFields/>}<label>형식<select name="kind"><option value="export">CSV 파일</option><option value="print">인쇄 / PDF</option></select></label><p>화면의 검색·상태 필터와 별개로 선택한 기간·반·학생의 전체 조회 범위를 사용합니다.</p><button>범위 확인 후 내보내기</button></fieldset></form><OverviewReport data={data}/></>}
  </section>;
}

export function OverviewReport({data:d}:{data:any}) {
  const parent=d.user.role==='parent',teacher=d.user.role==='teacher';
  const [query,setQuery]=useState('');
  const [recordFilter,setRecordFilter]=useState('all');
  const visibleRecords=d.records.filter(r=>(`${r.studentName} ${r.className} ${r.title}`.toLowerCase().includes(query.trim().toLowerCase()))&&(recordFilter==='all'||r.status===recordFilter));
  const latestFeedback=[...d.records].filter(r=>r.sample?.teacherNote).sort((a,b)=>(b.publishedAt||b.submittedAt||0)-(a.publishedAt||a.submittedAt||0))[0];
  const jump=(id:string)=>document.getElementById(id)?.scrollIntoView({behavior:'auto',block:'start'});
  const recordPath=r=>`${r.kind==='lesson'?learningPath(d.user.role):examPath(d.user.role)}${r.runId?'/'+r.runId:''}`;
  const reviewTodo=teacher?d.records.filter(r=>r.submittedAt&&(r.kind==='lesson'?r.reviewedCount<r.questionCount:!r.publishedAt)):[];
  const unfinished=d.records.filter(r=>!r.submittedAt&&r.status!=='awaiting_release');
  return <div className="ov-report">
    <div className="ov-report-meta"><div><p>{d.organizationName} · {d.startDate} ~ {d.endDate}</p><details className="workspace-data-basis"><summary>조회 기준 살펴보기</summary><p>{d.scope} · {d.basis}<br/>기준 시각 {date(d.asOf)}</p></details></div></div>
    <div className="ov-counts"><span>배정 {d.totals.assigned}건</span><span>읽기 수업 {d.totals.readingAssigned}건</span><span>모의고사 {d.totals.examsAssigned}건</span>{!parent&&<span>기한이 지난 미제출 {d.totals.overdue}건</span>}</div>
    {teacher&&<section className="ex-card workspace-priority"><h2>먼저 살펴볼 응답</h2><p>읽기 수업 검토 대기 {d.totals.pendingReview}건 · 수정 응답이 있는 활동 {d.totals.revisions}개</p>{!reviewTodo.length?<p>현재 확인할 제출 기록이 없습니다.</p>:<ul className="ov-todo">{reviewTodo.slice(0,12).map(r=><li key={r.id}><a href={recordPath(r)}>{r.studentName} · {r.title}</a><span>{r.kind==='lesson'?'활동별 설명 검토':'평가 결과와 보호자 공개 확인'}</span></li>)}</ul>}</section>}
    {d.user.role==='student'&&<section className="ex-card workspace-priority"><h2>이어서 할 학습</h2>{!unfinished.length?<p>조회 기간에 남은 미제출 과제가 없습니다.</p>:<ul className="ov-todo">{unfinished.map(r=><li key={r.id}><a href={recordPath(r)}>{r.title}</a><span>{status[r.status]} · 기한 {date(r.dueAt)}</span></li>)}</ul>}</section>}
    {parent&&<section className="workspace-family-note"><MessageCircle size={25}/><div><span className="rx-eyebrow">선생님과 이어가는 배움</span><h2>{latestFeedback?'가장 최근에 도착한 피드백':'아이의 속도에 맞춰 함께 읽어요.'}</h2><p>{latestFeedback?.sample.teacherNote||'“어느 문장에서 그렇게 생각했니?” 오늘 읽은 글에서 아이가 찾은 이유를 들어 주세요.'}</p>{latestFeedback&&<a href={recordPath(latestFeedback)}>아이의 응답과 함께 보기 <ArrowUpRight size={17}/></a>}</div></section>}
    <nav className="workspace-jump no-print" aria-label="리포트 바로가기"><button onClick={()=>jump('overview-summary')}>배움 요약</button><button onClick={()=>jump('overview-observations')}>읽기 과정</button><button onClick={()=>jump('overview-records')}>과제별 기록 <span>{d.records.length}</span></button></nav>
    <section id="overview-summary" className="ov-metrics" aria-label="학습 기록 요약">
      <Metric label={parent?'공개된 과제':'과제 제출'} value={parent?d.totals.published:d.totals.completion} description={parent?'공개된 결과 ÷ 기간 안에 배정한 과제':'제출한 과제 ÷ 기간 안에 배정한 과제'}/>
      <Metric label="읽기 첫 선택 답" value={d.totals.firstChoice} description="첫 선택 답 정답 ÷ 선택형 첫 응답. 서술형은 제외합니다."/>
      <Metric label="첫 근거 확인" value={d.totals.firstEvidence} description="필요한 근거를 포함한 첫 응답 ÷ 근거 확인이 가능한 첫 응답"/>
      <Metric label="도움 질문 사용" value={d.totals.hints} description="도움 질문을 사용한 첫 응답 ÷ 확인한 첫 응답. 수업 조건과 함께 봅니다."/>
      <Metric label="교사 설명 확인" value={d.totals.teacherExplanation} description="설명·근거가 적절하다고 검토한 활동 ÷ 교사가 검토한 활동. 미검토는 제외합니다."/>
      <Metric label="모의고사 정답" value={d.totals.examAccuracy} description="조회 권한이 있는 평가의 정답 수 ÷ 해당 평가의 전체 문항. 미응답은 오답에 포함합니다."/>
    </section>
    {!d.records.length&&<p className="ex-empty">이 기간에 배정된 과제가 없습니다. 기간과 조회 범위를 확인해 주세요.</p>}
    <section className="ex-card"><h2>배정 주차별 수행 기록</h2><p>각 주에 배정한 과제의 현재 결과입니다. 지문과 도움 조건이 달라 정답률 차이를 실력의 증가·감소로 단정하지 않습니다.</p><div className="ov-table"><table><thead><tr><th>배정 주</th><th>과제</th><th>{parent?'공개':'제출'}</th><th>첫 선택 답</th><th>첫 근거</th><th>교사 설명 확인</th></tr></thead><tbody>{d.weekly.map(w=><tr key={w.start}><th>{w.start} 주</th><td>{w.assigned}건</td><td>{count(parent?w.published:w.completion)}</td><td>{count(w.firstChoice)} · {text(w.firstChoice)}</td><td>{count(w.firstEvidence)} · {text(w.firstEvidence)}</td><td>{count(w.teacherExplanation)}</td></tr>)}</tbody></table></div></section>
    <section id="overview-observations" className="ov-two"><div className="ex-card"><h2>읽기 행동별 관찰</h2>{d.skills.length?d.skills.map(s=><div className="ov-observation" key={s.id}><h3>{s.title}</h3><p>첫 근거 {count(s.firstEvidence)} · 교사 설명 확인 {count(s.teacherExplanation)}</p>{s.firstEvidence.denominator>0&&<progress value={s.firstEvidence.numerator} max={s.firstEvidence.denominator} aria-label={`${s.title} 첫 근거 포함 ${count(s.firstEvidence)}`}/>}</div>):<p>제출·공개된 읽기 활동이 없습니다.</p>}</div><div className="ex-card"><h2>수업 목표별 관찰</h2><p>실제로 배정한 수업의 목표입니다. 전체 문해력 목표의 달성 판정은 아닙니다.</p>{d.goals.length?d.goals.map(g=><div className="ov-observation" key={g.id}><h3>{g.title}</h3><p>관찰한 응답 {g.responses}개 · 첫 근거 {count(g.firstEvidence)} · 설명 확인 {count(g.teacherExplanation)}</p></div>):<p>관찰한 목표가 없습니다.</p>}</div></section>
    <section className="ex-card"><h2>보충 학습과 새 글 확인</h2><p>평가 후 보충 배정 {d.followups.assigned}개 · 보충 확인 활동 완료 {d.followups.completed}개</p><p>새 글에서 선택 답과 교사 근거 검토를 함께 확인한 수행: {count(d.followups.confirmedTransfer)}{d.followups.confirmedTransfer.denominator>0?' · '+text(d.followups.confirmedTransfer):''}</p><p>이미 본 글과 교사 검토 전 응답은 새 글 확인 성공으로 집계하지 않습니다.</p></section>
    {teacher&&<section className="ex-card"><h2>학생별 수업과 지도</h2><div className="ov-table"><table><thead><tr><th>학생</th><th>배정</th><th>제출</th><th>검토 대기</th><th>첫 선택 답</th><th>첫 근거</th></tr></thead><tbody>{d.byStudent.map(s=><tr key={s.id}><th>{s.name}</th><td>{s.assigned}</td><td>{count(s.completion)}</td><td>{s.pendingReview}건</td><td>{count(s.firstChoice)}</td><td>{count(s.firstEvidence)}</td></tr>)}</tbody></table></div></section>}
    <section id="overview-records" className="ex-card"><div className="ex-section-title"><div><p className="rx-eyebrow">학습의 발자취</p><h2>과제별 기록</h2></div><span className="workspace-result-count" role="status">{visibleRecords.length}건</span></div><div className="workspace-record-filter no-print"><label className="workspace-search"><Search size={18}/><input aria-label="학생 또는 과제 검색" placeholder="학생 이름, 반, 과제 이름 검색" value={query} onChange={e=>setQuery(e.target.value)}/></label><label>진행 상태<select value={recordFilter} onChange={e=>setRecordFilter(e.target.value)}><option value="all">전체 상태</option>{Object.entries(status).filter(([key])=>d.records.some(r=>r.status===key)).map(([key,label])=><option key={key} value={key}>{label}</option>)}</select></label></div>{!visibleRecords.length&&<p className="ex-empty">조건에 맞는 기록이 없습니다. 검색어나 진행 상태를 바꿔 보세요.</p>}<div className="ov-table"><table><thead><tr><th>학생·반</th><th>과제</th><th>상태</th><th>기록</th></tr></thead><tbody>{visibleRecords.map(r=><tr key={r.id}><th>{r.studentName}<small>{r.className}</small></th><td>{r.kind==='lesson'?'읽기 수업':'모의고사'} · {r.title}<small>{day(r.assignedAt)} 배정</small></td><td><span className="workspace-status" data-status={r.status}>{status[r.status]}</span></td><td>{r.runId?<a href={recordPath(r)}>답안·피드백 보기</a>:parent?'공개 후 확인':<a href={recordPath(r)}>배정 목록 보기</a>}</td></tr>)}</tbody></table></div>
      {visibleRecords.filter(r=>r.sample).map(r=><details key={r.id} className="ov-sample"><summary>{r.studentName} · {r.title} · 실제 응답과 의견</summary>{r.sample.prompt&&<><h3>{r.sample.prompt}</h3><p>첫 설명: {r.sample.firstReason}</p>{r.sample.latestReason!==r.sample.firstReason&&<p>고친 설명: {r.sample.latestReason}</p>}<p>내 말로 설명한 글: {r.sample.writing}</p></>}{r.sample.teacherNote&&<p>선생님 의견: {r.sample.teacherNote}</p>}</details>)}
    </section>
    {parent&&<p className="ov-policy">공개되지 않은 결과와 수정 중인 교사 의견은 표시하지 않습니다. 공개 회수나 보호자 연결 변경은 다음 조회부터 반영됩니다.</p>}
  </div>;
}
