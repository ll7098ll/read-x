import React from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import type { GradeData } from '../../types/courseware';
import { GraphicOrganizerBuilder } from '../tei/GraphicOrganizerBuilder';
import { ChoicePractice, ClinicDrill, VaccinePractice } from './ClinicActivities';

export const AdaptiveClinicStudio: React.FC<{ gradeData: GradeData }> = ({ gradeData }) => {
  const setStudentMode = useCoursewareStore(s => s.setStudentMode);
  const rx = gradeData.prescription_clinic;
  const step0 = rx.step0_remedial;
  return <article className="space-y-5 max-w-5xl mx-auto">
    <header className="rounded-2xl bg-white border p-6 space-y-3">
      <p className="text-sm text-teal-700">목표에 맞춰 생각 연습하기</p>
      <h2 className="text-2xl font-bold">{rx.rx_title}</h2><p className="leading-relaxed">{rx.rx_reason}</p>
      <button type="button" onClick={() => setStudentMode('studio')} className="rounded-xl bg-blue-700 text-white px-4 py-3">본문으로 돌아가기</button>
    </header>
    <section className="rounded-2xl bg-white border p-5 space-y-4">
      <h3 className="text-lg font-bold">1. 필요한 생각 떠올리기</h3>
      <p className="rounded-xl bg-amber-50 p-4">{step0.activityType === 'rule' ? step0.rule : step0.rule_box}</p>
      {step0.activityType === 'choice' && <ChoicePractice question={step0.mini_question} choices={step0.choices} correct={step0.correct} feedback={step0.feedback} />}
    </section>
    <section className="rounded-2xl bg-white border p-5 space-y-4">
      <h3 className="text-lg font-bold">2. 단서를 찾아 관계 연결하기</h3>
      <ClinicDrill key={gradeData.slot_id} drill={rx.step1_2_drill} draftKey={`${gradeData.slot_id}:clinic`} />
    </section>
    <GraphicOrganizerBuilder key={gradeData.slot_id} data={gradeData.commercial.graphic_organizer} />
    <section className="rounded-2xl bg-white border p-5 space-y-4">
      <h3 className="text-lg font-bold">3. 내 판단과 글의 근거 확인하기</h3>
      <p>{rx.step3_vaccine.desc}</p><VaccinePractice items={rx.step3_vaccine.items} />
    </section>
  </article>;
};
