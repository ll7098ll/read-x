import React from 'react';
import test from 'node:test';
import assert from 'node:assert/strict';
import { renderToStaticMarkup } from 'react-dom/server';
import { readExamRoute, examPath, learningHomePath, learningPath, isLearningRoute, homePath, isHomeRoute } from '../src/services/examNavigation';
import { BrandHeader } from '../src/components/layout/BrandHeader';
import { AccountForm } from '../src/components/exam/AccountForms';
import { ExamEntryCard } from '../src/components/exam/ExamEntryCard';
import type { ExamRole, ExamUser } from '../src/types/exam';

test('기존 모의고사 주소와 세 역할 경로가 동일 기능을 열고 일반 학습 경로는 유지한다', () => {
  assert.deepEqual(readExamRoute('#/exams'), { active: true, role: null });
  for (const role of ['student', 'teacher', 'parent'] as ExamRole[]) {
    assert.deepEqual(readExamRoute(examPath(role)), { active: true, role });
    assert.equal(readExamRoute(learningHomePath(role)).active, false);
  }
  for (const hash of ['#/student/assessment', '#/student/studio/G5-01', '#/teacher', '#/parent', '#/exams-fake', '#/director/exams']) assert.equal(readExamRoute(hash).active, false);
});

test('경로의 요청 역할보다 로그인한 역할을 사용하고 실제 역할의 배움터로 돌아간다', () => {
  const user: ExamUser = { id: 'teacher-a', name: '담당 교사', username: 'teacher_a', role: 'teacher', tenantId: 'class-a', className: '초5', childIds: [] };
  const html = renderToStaticMarkup(<BrandHeader exam={{ user, role: 'student', reading: false, busy: false, onLogout() {}, onOverview() {} }}/>);
  assert.ok(html.includes('선생님 수업실'));
  assert.ok(html.includes('href="#/teacher/classes"'));
  assert.ok(!html.includes('href="#/student/portal"'));
  assert.ok(html.includes('aria-label="Read X 리드엑스"'));
  assert.ok(html.includes('로그아웃'));
});

test('로그인 전 역할별 진입 카드에 가상 성적이나 학생 수를 표시하지 않는다', () => {
  for (const role of ['student', 'teacher', 'parent'] as ExamRole[]) {
    const html = renderToStaticMarkup(<ExamEntryCard role={role}/>);
    assert.ok(html.includes(`href="${examPath(role)}"`));
    assert.ok(!html.includes('<dd>'), 'API 결과 전에는 수치 없음');
    assert.ok(html.includes('24문항'));
  }
});


test('운영 로그인과 초기 설정은 계정 폼을 표시하고 체험 자동 로그인 문구를 쓰지 않는다', () => {
  for (const setup of [false, true]) {
    const html = renderToStaticMarkup(<AccountForm setup={setup} busy={false} onSubmit={() => {}}/>);
    assert.ok(html.includes('name="username"'));
    assert.ok(html.includes('type="password"'));
    assert.equal(html.includes('name="className"'), setup);
    assert.ok(!html.includes('계정 없이'));
  }
  const html = renderToStaticMarkup(<ExamEntryCard role="student"/>);
  assert.ok(html.includes('계정별 서버 저장'));
  assert.ok(!html.includes('계정 없이 바로 체험'));
});


test('실제 읽기 수업 경로는 공통 계정 화면으로 연결하고 체험 홈과 구분한다', () => {
  for (const role of ['student','teacher','parent'] as ExamRole[]) {
    assert.deepEqual(readExamRoute(learningPath(role)), { active:true, role });
    assert.equal(isLearningRoute(learningPath(role)),true);
    assert.equal(isLearningRoute(examPath(role)),false);
  }
  assert.equal(readExamRoute('#/teacher/classes-fake').active,false);
});


test('공통 운영 홈과 개별 수업·평가 주소는 계정 화면으로 연결한다',()=>{
  for(const role of ['student','teacher','parent'] as ExamRole[]){
    assert.deepEqual(readExamRoute(homePath(role)),{active:true,role});
    assert.equal(isHomeRoute(homePath(role)),true);
    assert.equal(readExamRoute(learningPath(role)+'/record-id').active,true);
    assert.equal(readExamRoute(examPath(role)+'/record-id').active,true);
  }
  assert.equal(readExamRoute('#/teacher/home-fake').active,false);
});
