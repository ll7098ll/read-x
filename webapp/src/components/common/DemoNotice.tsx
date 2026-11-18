import React from 'react';
import { Info } from 'lucide-react';
import { examDemo } from '../../services/examApi';
export function DemoNotice() {
  return <aside className="rx-demo-notice" aria-label="체험 데이터 안내"><Info size={14}/><p><strong>체험 공간</strong><span>{examDemo?' 이 사이트는 가상 자료로 체험합니다. 실명·연락처·실제 학생 기록을 입력하지 마세요. 입력한 체험 기록은 이 브라우저에 남을 수 있습니다. 실제 학원 계정과 연결되지 않습니다.':' 이 화면의 학생·학원 명단과 운영 현황은 예시입니다. 실제 읽기 수업과 모의고사는 학원 계정으로 로그인하여 이용해 주세요.'}</span></p></aside>;
}

