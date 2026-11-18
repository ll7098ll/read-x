import React, { useState } from 'react';
import { GuidedResponse } from './GuidedResponse';
import type { WritingWorkbenchData, ChoiceWritingData } from '../../types/courseware';

interface WritingWorkbenchProps {
  data: WritingWorkbenchData;
  draftKey?: string;
  onChoiceSelect?: (choiceId: string, isCorrect: boolean) => void;
}

const ChoiceWriting: React.FC<WritingWorkbenchProps & { data: ChoiceWritingData }> = ({
  data,
  onChoiceSelect,
}) => {
  const [selectedChoiceId, setSelectedChoiceId] = useState<string | null>(null);
  const [activeConditions, setActiveConditions] = useState<boolean[]>(
    data.conditions.map(() => false)
  );

  const selectedChoice = data.choices.find((c) => c.id === selectedChoiceId);

  const handleSelectChoice = (choiceId: string) => {
    setSelectedChoiceId(choiceId);
    const choice = data.choices.find((c) => c.id === choiceId);
    if (choice) {
      setActiveConditions(choice.cond_check);
      onChoiceSelect?.(choiceId, choice.is_correct);
    }
  };

  return (
    <div className="writing-workbench bg-white rounded-2xl border border-teal-200 shadow-sm p-4 space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-teal-100">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 bg-teal-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-6 • 작문 워크벤치
          </span>
          <h4 className="font-bold text-sm text-slate-900">{data.title}</h4>
        </div>
        <span className="text-xs px-2 py-0.5 rounded-full bg-teal-50 text-teal-800 border border-teal-200 font-bold">
          단계: {data.code} ({data.mode})
        </span>
      </div>

      {/* Conditions Checklist (Traffic Light Checker) */}
      <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
        <div className="text-xs font-bold text-slate-700 flex items-center justify-between">
          <span>🚦 작문 조건 신호등 검증기</span>
          <span className="text-[11px] text-slate-400 font-normal">
            선택된 초안에 따라 충족 여부가 실시간 변경됩니다
          </span>
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
          {data.conditions.map((cond, cIdx) => {
            const isSatisfied = activeConditions[cIdx];
            return (
              <div
                key={cIdx}
                className={`p-2 rounded-lg border text-xs flex items-center gap-2 transition-all ${
                  isSatisfied
                    ? 'bg-emerald-50 border-emerald-300 text-emerald-900 font-bold'
                    : 'bg-white border-slate-200 text-slate-500'
                }`}
              >
                <span
                  className={`w-3 h-3 rounded-full flex items-center justify-center shrink-0 ${
                    isSatisfied ? 'bg-emerald-500 ring-2 ring-emerald-200' : 'bg-slate-300'
                  }`}
                />
                <span className="truncate">{cond}</span>
              </div>
            );
          })}
        </div>
      </div>

      {/* Draft Prefix / Prompt */}
      {data.draft_prefix && (
        <div className="p-3 bg-teal-50/50 rounded-xl border border-teal-100 text-xs text-slate-800 space-y-1">
          <div className="font-bold text-teal-900">✍️ 작문 도입부 / 맥락:</div>
          <p className="italic leading-relaxed">{data.draft_prefix}</p>
        </div>
      )}

      {/* Writing Choices Selection */}
      <div className="space-y-2.5">
        <div className="text-xs font-bold text-slate-700">
          📝 이어 쓸 문맥 / 개요 블록 선택:
        </div>
        {data.choices.map((choice) => {
          const isSelected = selectedChoiceId === choice.id;
          return (
            <div
              key={choice.id}
              onClick={() => handleSelectChoice(choice.id)}
              className={`p-3 rounded-xl border text-xs cursor-pointer transition-all ${
                isSelected
                  ? choice.is_correct
                    ? 'bg-emerald-50 border-emerald-500 ring-2 ring-emerald-200 text-emerald-950 font-bold shadow-xs'
                    : 'bg-rose-50 border-rose-400 ring-2 ring-rose-200 text-rose-950 font-bold shadow-xs'
                  : 'bg-white border-slate-200 hover:border-teal-300 hover:bg-slate-50 text-slate-800'
              }`}
            >
              <div className="flex items-start gap-2">
                <span className="px-2 py-0.5 rounded bg-slate-200 text-slate-700 text-[10px] font-mono shrink-0">
                  {choice.id}
                </span>
                <span className="flex-1 leading-relaxed">{choice.text}</span>
              </div>

              {isSelected && (
                <div
                  className={`mt-2.5 pt-2 border-t text-[11.5px] font-normal leading-relaxed ${
                    choice.is_correct
                      ? 'border-emerald-200 text-emerald-800'
                      : 'border-rose-200 text-rose-800'
                  }`}
                >
                  <b>{choice.is_correct ? '✅ 피드백:' : '⚠️ 주의:'}</b> {choice.feedback}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export const WritingWorkbench: React.FC<WritingWorkbenchProps> = props => {
  if (props.data.activityType === 'free_response') return <GuidedResponse
    title={props.data.title} instruction={props.data.guide} template={props.data.template} draftKey={props.draftKey} />;
  return <ChoiceWriting {...props} data={props.data} />;
};
