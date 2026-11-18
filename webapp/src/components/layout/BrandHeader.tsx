import React from 'react';
import { ArrowLeft, BookOpen, GraduationCap, HeartHandshake, LibraryBig, Home, ClipboardCheck, LogOut } from 'lucide-react';
import { ReadXBrand } from '../brand/ReadXBrand';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { examPath, learningHomePath, learningPath, isLearningRoute, managementPath, isManagementRoute, homePath, isHomeRoute } from '../../services/examNavigation';
import type { ExamRole, ExamUser } from '../../types/exam';

type ExamHeader = { user: ExamUser | null; role: ExamRole | null; reading: boolean; busy: boolean; demo?: boolean; onLogout?: () => void; onOverview: () => void };

export function BrandHeader({ exam }: { exam?: ExamHeader }) {
  const { activeRole, studentMode, activeGradeIdx, setStudentMode } = useCoursewareStore();
  const role = exam?.user?.role || exam?.role || activeRole;
  const learning = exam ? exam.reading : activeRole === 'student' && !['portal', 'assessment'].includes(studentMode);
  const roles = {
    student: { label: '나의 배움터', Icon: BookOpen },
    teacher: { label: '선생님 수업실', Icon: GraduationCap },
    parent: { label: '우리 아이의 배움', Icon: HeartHandshake },
    director: { label: '학원 운영실', Icon: GraduationCap },
    admin: { label: '콘텐츠 관리실', Icon: LibraryBig },
    landing: { label: 'ReadX', Icon: Home },
  };
  const { label, Icon } = roles[role];
  const inHome = !!exam && typeof window !== 'undefined' && isHomeRoute(window.location?.hash || '');
  const inManagement = !!exam && typeof window !== 'undefined' && isManagementRoute(window.location?.hash || '');
  const inLearning = !!exam && typeof window !== 'undefined' && isLearningRoute(window.location?.hash || '');
  const assessmentRole = ['student', 'teacher', 'parent'].includes(role) ? role as ExamRole : null;
  return <header className={`rx-header no-print ${learning ? 'rx-header-reading' : ''}`}>
    <div className="rx-header-inner">
      <a className="rx-brand-link" href={exam?.user && !exam.demo ? homePath(exam.user.role) : "#/landing"} aria-label="Read X 홈"><ReadXBrand compact/></a>
      <div className="rx-header-context"><span aria-hidden="true"/><Icon size={17}/><b>{label}</b></div>
      {(assessmentRole || exam) && <nav className="rx-module-nav" aria-label="리드엑스 학습 메뉴">
        {exam?.user && !exam.demo && <a href={homePath(exam.user.role)} aria-current={inHome?'page':undefined}>학습 현황</a>}
        <a href={assessmentRole ? exam && !exam.demo ? learningPath(assessmentRole) : learningHomePath(assessmentRole) : '#/landing'} aria-current={!exam || inLearning ? 'page' : undefined}>{assessmentRole === 'teacher' ? '수업과 기록' : assessmentRole === 'parent' ? '배움 기록' : '읽기 학습'}</a>
        {exam ? <button aria-current={!inLearning && !inManagement && !inHome ? 'page' : undefined} disabled={exam.busy} onClick={exam.onOverview}><ClipboardCheck size={15}/> 모의고사</button> : <a href={examPath(assessmentRole)}><ClipboardCheck size={15}/> 모의고사</a>}
        {exam?.user && !exam.demo && <a href={managementPath(exam.user.role)} aria-current={inManagement?'page':undefined}>{exam.user.role==='teacher' ? exam.user.isOwner?'학원 운영':'반 운영' : '계정 설정'}</a>}
      </nav>}
      <div className="rx-header-actions">
        {exam ? <>{exam.demo ? <span className="rx-context-pill">계정 없이 체험</span> : exam.user ? <><span className="rx-context-pill">{exam.user.name}</span><button className="rx-header-back" disabled={exam.busy} onClick={exam.onLogout}><LogOut size={15}/><span>로그아웃</span></button></> : <span className="rx-context-pill">초5 · 1회차</span>}</> : learning ? <button className="rx-header-back" onClick={() => setStudentMode('portal')}><ArrowLeft size={16}/> 학습 목록</button> : <><span className="rx-context-pill">{activeRole === 'student' ? `${activeGradeIdx + 1}학년 체험` : '학원·공부방 체험'}</span><a className="rx-header-back" href="#/landing"><Home size={16}/><span>Read X 홈</span></a></>}
      </div>
    </div>
  </header>;
}
