import React, { useState } from 'react';
import { ArrowRight, ArrowUpRight, ChevronDown } from 'lucide-react';
import { ReadXBrand } from '../brand/ReadXBrand';
import { ThinkingPreview } from '../common/ThinkingPreview';
import { ReadingMethodDemo } from '../brand/ReadingMethodDemo';
import { READ_X_STEPS } from '../brand/readXSystem';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import { masterData } from '../../data/lessonCatalog';
import { revisedLessonForSlot } from '../../data/corpusReading';
import { examDemo } from '../../services/examApi';
import { managementPath, homePath } from '../../services/examNavigation';
import type { ExamRole } from '../../types/exam';
import type { RoleType, SlotLessonPackage } from '../../types/courseware';

const art = `${import.meta.env.BASE_URL}brand/editorial`;
const roles = [
  { role: 'student', name: '학생', title: '나의 배움터', description: '오늘의 읽기를 시작해요' },
  { role: 'teacher', name: '선생님', title: '수업과 학생 관리', description: '수업 준비부터 피드백까지' },
  { role: 'parent', name: '학부모', title: '우리 아이의 기록', description: '배움의 과정을 함께 살펴요' },
] as const;
function lessonImage(lesson: SlotLessonPackage) {
  const topic = [revisedLessonForSlot(lesson.slot_id)?.title, lesson.curriculum_concept.subject, lesson.curriculum_concept.unit, lesson.curriculum_concept.concept].join(' ');
  if (/음악|악기|소리 내는/.test(topic)) return 'music';
  if (/문화유산|전통|문화/.test(topic)) return 'culture';
  if (/식물|꽃|자연|채소|계절|강낭콩|생태|동물|온실/.test(topic)) return 'nature';
  if (/과학|물질|온도|용해|알갱이|행성|암석|연소/.test(topic)) return 'discovery';
  return 'reading';
}
function readingGoal(name: string) {
  const label = name.split('(')[0].trim();
  return ({ '내용 확인': '글에서 중요한 정보를 찾아요.', '관계 확인': '문장과 문장의 관계를 연결해요.', '구조 확인': '내용이 짜인 방식을 살펴봐요.' } as Record<string, string>)[label] || label;
}
export function MainLandingPage({ totalDbSlots }: { totalDbSlots: number }) {
  const { setActiveRole, setStudentMode, selectGradeAndSlot } = useCoursewareStore();
  const [grade, setGrade] = useState(3);
  const lessons = (masterData.expository_slots_96 || []).filter(s => s.grade_num === grade).slice(0, 3);
  const enter = (role: RoleType) => {
    if (!examDemo && role === 'director') { window.location.hash = managementPath('teacher'); return; }
    if (!examDemo && ['student', 'teacher', 'parent'].includes(role)) { window.location.hash = homePath(role as ExamRole); return; }
    if (role === 'student') setStudentMode('portal');
    setActiveRole(role);
    window.scrollTo(0, 0);
  };
  const previewLesson = (slotId: string) => {
    selectGradeAndSlot(grade, slotId, 'studio');
    setActiveRole('student');
    window.scrollTo(0, 0);
  };
  return <div className="editorial-home">
    <header className="editorial-header">
      <div className="editorial-container editorial-header-inner">
        <a href="#/landing" aria-label="Read X 홈"><ReadXBrand compact/></a>
        <nav aria-label="주요 메뉴"><a href="#library">읽기 둘러보기</a><a href="#learning">수업의 방식</a><a href="#start">나의 공간</a></nav>
        <button className="editorial-header-login" onClick={() => enter('student')}>{examDemo ? '체험 시작' : '로그인'} <ArrowUpRight size={18}/></button>
      </div>
    </header>
    <main id="main-content" tabIndex={-1}>
      {examDemo && <details className="editorial-demo editorial-container"><summary><span><i/> 공개 체험판 · 가상 자료로 둘러보세요</span><span>이용 안내 <ChevronDown size={15}/></span></summary><div><p>실명·연락처·실제 학생 기록은 입력하지 마세요. 체험 기록은 이 브라우저에 남을 수 있습니다.</p><p>학생·보호자 계정, 교사 배정, 제출, 검토와 보호자 리포트를 서버에 구현하고 검증하고 있습니다. 안내문 버전별 동의·철회, 학생 이용 제어, 교사·운영자 인증앱 2단계 인증, 개인정보 조회·내보내기 기록과 권리 요청·검토 사본 제공, 일반 서비스 처리정지·해제, 운영 자료 삭제·별도 보존, 암호화 백업과 복원 후 삭제 재처리도 개발에 반영했습니다.</p><p>이 공개 체험판은 실제 학원 계정과 연결되지 않습니다. 국내 운영 서버와 개인정보·보안·법률·운영 검토가 준비된 뒤 실제 이용 기능을 열 예정입니다.</p></div></details>}
      <section className="editorial-hero editorial-container" aria-labelledby="editorial-title">
        <div className="editorial-hero-copy">
          <p className="editorial-label">읽는 방법을 배우는 문해력 코스웨어 · Read X</p>
          <h1 id="editorial-title">읽으라고 하기 전에,<br/><span>읽는 방법부터.</span></h1>
          <p className="editorial-intro">어디부터 읽어야 할지 막막할 때,<br className="editorial-wide-break"/> 단서를 찾고 생각을 잇는 방법을 하나씩 배워요.</p>
          <div className="editorial-actions"><button className="editorial-button" onClick={() => enter('student')}>학습 시작하기 <ArrowUpRight size={20}/></button><a className="editorial-text-link" href="#library">수업 먼저 만나보기 <ArrowRight size={19}/></a></div>
          <div className="editorial-hero-foot"><span>시범 보기</span><i/><span>함께 읽기</span><i/><span>혼자 읽기</span><span className="editorial-hero-foot-note">내가 쓸 수 있는 읽기 방법이 생겨요</span></div>
        </div>
        <figure className="editorial-hero-figure readx-home-figure"><ReadingMethodDemo/><figcaption><span>짧은 시범으로 읽는 방법을 만나 보세요</span><span>READ X</span></figcaption></figure>
      </section>

      <section className="editorial-roles editorial-container" id="start" aria-labelledby="role-title">
        <h2 id="role-title">나의 공간<br/><span>바로 시작하기</span></h2>
        {roles.map(({ role, name, title, description }) => <button className="editorial-role" key={role} onClick={() => enter(role)}><span className="editorial-role-name">{name}</span><strong>{title} <ArrowUpRight size={21}/></strong><span className="editorial-role-description">{description}</span></button>)}
      </section>

      <section className="editorial-library editorial-container" id="library" aria-labelledby="library-title">
        <div className="editorial-section-heading"><div><span className="editorial-section-number">01 / 읽는 방법을 만나는 글</span><h2 id="library-title">한 편의 글, 하나의 읽는 방법.</h2></div><p>학년에 맞는 글에서<br/>오늘 연습할 방법을 찾아보세요.</p></div>
        <div className="editorial-library-toolbar"><div className="editorial-grade-filter" role="group" aria-label="미리 볼 수업 학년">{[1,2,3,4,5,6].map(g => <button key={g} aria-pressed={grade === g} onClick={() => setGrade(g)}>{g}학년</button>)}</div><span>초등 {grade}학년 · 수업 미리보기</span></div>
        <div className="editorial-lesson-grid" aria-live="polite">
          {lessons.map(lesson => <button className="editorial-lesson" key={lesson.slot_id} onClick={() => previewLesson(lesson.slot_id)}>
            <div className="editorial-lesson-image"><img src={`${art}/${lessonImage(lesson)}.webp`} width="1536" height="1024" loading="lazy" alt=""/><span className="editorial-lesson-open" aria-hidden="true"><ArrowUpRight size={24}/></span></div>
            <div className="editorial-lesson-meta"><span>{lesson.curriculum_concept.subject.replace(/\s*\([^)]*\)/g, '').trim()}</span><span>읽기 체험</span></div>
            <h3>{revisedLessonForSlot(lesson.slot_id)?.title || lesson.real_csat_test.passage_title}</h3>
            <p>{readingGoal(lesson.sub_skill_name)}</p>
          </button>)}
        </div>
        <p className="editorial-library-note">체험 기록은 이 기기에 저장됩니다. 배정받은 수업과 선생님의 피드백은 로그인 후 확인하세요.</p>
      </section>

      <section className="editorial-method" id="learning" aria-labelledby="method-title">
        <div className="editorial-container">
          <div className="editorial-section-heading"><div><span className="editorial-section-number">02 / Read X의 학습 흐름</span><h2 id="method-title">처음에는 함께,<br/>다음에는 스스로.</h2></div><p>어디를 보고, 어떻게 생각하는지.<br/>시범과 연습을 거쳐 나의 읽기 방법을 만듭니다.</p></div>
          <div className="editorial-method-grid">
            <ol className="editorial-method-steps">{READ_X_STEPS.map(({title,description},i)=><li key={title}><span>0{i+1}</span><div><h3>{title}</h3><p>{description}</p></div></li>)}</ol>
            <div className="editorial-demo-lesson"><div className="editorial-demo-lesson-header"><span>수업을 직접 살펴보세요</span><span>생각 시범</span></div><ThinkingPreview/></div>
          </div>
        </div>
      </section>

      <section className="editorial-closing editorial-container"><div><span className="editorial-section-number">다음 페이지는, 나의 배움터에서.</span><h2>오늘도 한 편,<br/>생각이 깊어지는 시간.</h2></div><div><p>학생의 읽기, 선생님의 지도, 가정의 대화.<br/>하나의 배움으로 이어집니다.</p><button className="editorial-button" onClick={() => enter('teacher')}>선생님 수업실 <ArrowUpRight size={20}/></button><a className="editorial-text-link" href="#/exams">문해력 모의고사 <ArrowRight size={18}/></a></div></section>
      <footer className="editorial-footer"><div className="editorial-container"><div className="editorial-footer-top"><ReadXBrand compact/><p>읽는 방법을 알면, 읽는 힘이 자랍니다.</p><nav aria-label="운영 및 자료 메뉴"><a href="#/brand">브랜드 · UI/UX 킷 <ArrowUpRight size={15}/></a><button onClick={() => enter('director')}>학원 운영실 <ArrowUpRight size={15}/></button><button onClick={() => enter('admin')}>콘텐츠 자료실 체험 <ArrowUpRight size={15}/></button></nav></div><div className="editorial-footer-bottom"><span>Read X · 리드엑스</span><span>초등 1–6학년 · 기존 수업 자료 {totalDbSlots}개 기반</span></div></div></footer>
    </main>
  </div>;
}
