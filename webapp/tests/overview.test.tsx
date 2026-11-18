import React from 'react';
import test from 'node:test';
import assert from 'node:assert/strict';
import { renderToStaticMarkup } from 'react-dom/server';
import { OverviewReport } from '../src/components/common/OverviewDashboard';

test('운영 리포트는 실제 0점과 관찰 없음, 보호자 공개 범위를 구분해 표시한다',()=>{
  const none={numerator:0,denominator:0,percent:null},zero={numerator:0,denominator:1,percent:0};
  const totals={assigned:1,readingAssigned:1,examsAssigned:0,overdue:null,completion:null,published:{numerator:1,denominator:1,percent:100},firstChoice:zero,firstEvidence:none,hints:none,teacherExplanation:none,revisions:0};
  const data={user:{role:'parent',name:'보호자'},organizationName:'검증 학원',startDate:'2026-11-01',endDate:'2026-11-14',scope:'공개된 자녀 수행 결과',basis:'배정일 기준',asOf:1794614400000,totals,weekly:[],skills:[],goals:[],followups:{assigned:0,completed:0,confirmedTransfer:none},byStudent:[],records:[{id:'assignment:student',kind:'lesson',runId:'run-id',studentName:'연결 자녀',className:'A반',title:'수업',assignedAt:1794614400000,status:'published',sample:{prompt:'설명',firstReason:'<img src=x onerror=alert(1)>',latestReason:'<img src=x onerror=alert(1)>',writing:'내 글',teacherNote:'공개한 의견'}}]};
  const html=renderToStaticMarkup(<OverviewReport data={data}/>);
  assert.ok(html.includes('0%'));assert.ok(html.includes('—'));assert.ok(html.includes('확인할 기록 없음'));
  assert.ok(html.includes('#/parent/classes/run-id'));assert.ok(html.includes('공개한 의견'));
  assert.ok(!html.includes('학생별 수업과 지도'));assert.ok(!html.includes('검토 대기 0건'));
  assert.ok(!html.includes('<img src=x'));assert.ok(html.includes('&lt;img'));
  assert.ok(!html.includes('NaN'));
});
