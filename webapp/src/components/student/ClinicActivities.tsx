import React, { useState } from 'react';
import type { PrescriptionClinic, VaccineItem, CommonRemedialSlot } from '../../types/courseware';
import { InlineClozeBuilder } from '../tei/InlineClozeBuilder';
import { GuidedResponse } from '../tei/GuidedResponse';

export function ChoicePractice({ question, choices, correct, feedback }: {
  question: string; choices: string[]; correct: string; feedback: string;
}) {
  const [picked, setPicked] = useState<string | null>(null);
  return <section className="space-y-3">
    <h3 className="font-semibold">{question}</h3>
    <div className="flex flex-wrap gap-2">{choices.map(choice => <button key={choice} type="button" aria-pressed={picked === choice}
      onClick={() => setPicked(choice)} className={`rounded-xl border px-4 py-3 text-left ${picked === choice ? 'bg-blue-100 border-blue-500' : 'bg-white border-slate-300'}`}>{choice}</button>)}</div>
    {picked !== null && <p role="status" className="rounded-xl bg-slate-50 p-3">{picked === correct ? '맞았어요. ' : '근거를 다시 확인해 보세요. '}{feedback}</p>}
  </section>;
}

export function VaccinePractice({ items }: { items: VaccineItem[] }) {
  return <div className="space-y-5">{items.map((item, i) => <ChoicePractice key={i} question={item.statement}
    choices={['O','X']} correct={item.answer} feedback={item.reason} />)}</div>;
}

export function ClinicDrill({ drill, draftKey }: { drill: PrescriptionClinic['step1_2_drill']; draftKey?: string }) {
  return drill.activityType === 'guided_response'
    ? <GuidedResponse title="생각을 따라 연습하기" instruction={drill.task} draftKey={draftKey} />
    : <section className="space-y-3"><p className="leading-relaxed">{drill.passage_snippet.replace(/<[^>]*>/g, '')}</p>
      <InlineClozeBuilder promptTitle={drill.think_aloud_prompt} sentences={drill.cloze_sentences} blanks={drill.blanks} /></section>;
}

export function CommonFoundationStudio({ data }: { data: CommonRemedialSlot }) {
  return <article className="max-w-3xl mx-auto rounded-2xl border bg-white p-6 space-y-6">
    <p className="text-sm text-teal-700">기초 다지기 · {data.grade}</p><h2 className="text-2xl font-bold">{data.title}</h2>
    <p className="rounded-xl bg-amber-50 p-4 leading-relaxed">{data.rule_box}</p>
    <p className="leading-loose text-lg">{data.passage_snippet}</p>
    <ChoicePractice question={data.mini_question} choices={data.choices} correct={data.correct} feedback={data.feedback} />
    <VaccinePractice items={data.ox_items} />
  </article>;
}
