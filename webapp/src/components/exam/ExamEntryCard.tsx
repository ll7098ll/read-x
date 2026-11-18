import React, { useEffect, useState } from 'react';
import { ArrowRight, BookOpenCheck, Clock3, ShieldCheck } from 'lucide-react';
import { examApi, examDemo } from '../../services/examApi';
import { examPath, examRoleLabels } from '../../services/examNavigation';
import type { ExamDashboard, ExamRole, ExamUser } from '../../types/exam';

const copy = {
  student: { title: '읽은 만큼, 스스로 확인해요', body: '배정된 모의고사를 풀고, 내 답의 근거와 다음 학습을 살펴봐요.', action: '나의 모의고사' },
  teacher: { title: '수업에서 평가, 다음 지도까지', body: '초5 1회차를 배정하고 문항별 응답을 살펴보세요. 지도 의견은 보호자 리포트로 이어집니다.', action: '모의고사 운영' },
  parent: { title: '아이의 답에서 다음 배움을 찾아요', body: '학생 화면에서 제출한 문항별 결과와 지도 의견, 보충학습 진행을 함께 확인하세요.', action: '자녀 모의고사 리포트' },
};

export function ExamEntryCard({ role }: { role: ExamRole }) {
  const [user, setUser] = useState<ExamUser | null>(null), [data, setData] = useState<ExamDashboard | null>(null);
  const [loaded, setLoaded] = useState(false), [offline, setOffline] = useState(false);
  useEffect(() => {
    let current = true;
    const refresh = async () => {
      try {
        const s = await examApi('/session', undefined, role);
        const d = s.user?.role === role ? await examApi<ExamDashboard>('/dashboard', undefined, role) : null;
        if (current) { setUser(s.user); setData(d); setOffline(false); }
      } catch { if (current) { setUser(null); setData(null); setOffline(true); } }
      finally { if (current) setLoaded(true); }
    };
    void refresh(); window.addEventListener('focus', refresh);
    const timer = setInterval(refresh, 15000);
    return () => { current = false; clearInterval(timer); window.removeEventListener('focus', refresh); };
  }, [role]);
  const text = copy[role];
  const active = data?.attempts.filter(a => a.status === 'in_progress').length || 0;
  const submitted = data?.attempts.filter(a => a.status !== 'in_progress').length || 0;
  const remaining = data?.followups.filter(f => !f.completedAt).length || 0;
  const stats = !data ? [] : role === 'teacher' ? [['배정 회차', data.assignments.length], ['제출 기록', submitted], ['응시 중', active]] : role === 'parent' ? [['공개 리포트', submitted], ['다음 학습', remaining]] : [['배정 회차', data.assignments.length], ['응시 중', active], ['다음 학습', remaining]];
  return <section className="rx-exam-entry-card" aria-label={`${examRoleLabels[role]} 모의고사 연결`}>
    <div className="rx-exam-entry-copy"><span className="rx-eyebrow"><BookOpenCheck size={16}/> READX ASSESSMENT · 초5 1회차</span><h2>{text.title}</h2><p>{text.body}</p><div className="rx-exam-entry-facts"><span><BookOpenCheck size={15}/> 6개 지문 · 24문항</span><span><Clock3 size={15}/> 45분</span><span><ShieldCheck size={15}/> {examDemo ? "계정 없이 바로 체험" : "계정별 서버 저장"}</span></div></div>
    <div className="rx-exam-entry-action">
      {data && <><span className="rx-exam-account">{data.user.name} · {data.user.className}</span><dl>{stats.map(([label, value]) => <div key={label}><dt>{label}</dt><dd>{value}</dd></div>)}</dl></>}
      <a className={`rx-button ${role === 'student' ? 'rx-button-gold' : 'rx-button-primary'}`} href={examPath(user?.role || role)}>{user && user.role !== role ? `${examRoleLabels[user.role]} 모의고사` : text.action}<ArrowRight size={17}/></a>
      <small>{!loaded ? '계정과 기록을 확인하고 있어요.' : offline ? '서버 연결을 확인한 뒤 모의고사를 열어 주세요.' : !user ? examDemo ? '계정 없이 체험할 수 있습니다.' : '로그인하면 배정된 시험과 공개 리포트를 확인할 수 있습니다.' : user.role !== role ? `${examRoleLabels[user.role]} 계정이 연결되어 있습니다.` : examDemo ? '이 브라우저의 체험 기록' : '서버 기록 · 자동 업데이트'}</small>
    </div>
  </section>;
}
