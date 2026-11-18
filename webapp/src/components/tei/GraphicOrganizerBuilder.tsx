import React, { useState } from 'react';
import type { GraphicOrganizerData, CardSortOrganizerData, ReferenceNode } from '../../types/courseware';

interface GraphicOrganizerBuilderProps {
  data: GraphicOrganizerData;
  onComplete?: (isFullyCorrect: boolean) => void;
}

const CardSortOrganizer: React.FC<GraphicOrganizerBuilderProps & { data: CardSortOrganizerData }> = ({
  data,
  onComplete,
}) => {
  const [placedItems, setPlacedItems] = useState<Record<string, string>>({});
  const [selectedWord, setSelectedWord] = useState<string | null>(null);
  const [isSubmitted, setIsSubmitted] = useState<boolean>(false);

  const handleSlotClick = (slotId: string) => {
    if (isSubmitted) return;
    if (selectedWord) {
      setPlacedItems((prev) => ({ ...prev, [slotId]: selectedWord }));
      setSelectedWord(null);
    } else if (placedItems[slotId]) {
      // Remove item back to bank
      const next = { ...placedItems };
      delete next[slotId];
      setPlacedItems(next);
    }
  };

  const handleWordBankClick = (word: string) => {
    if (isSubmitted) return;
    setSelectedWord(selectedWord === word ? null : word);
  };

  const isAllFilled = data.nodes.every((n) => placedItems[n.slot_id]);

  const handleSubmit = () => {
    setIsSubmitted(true);
    const allCorrect = data.nodes.every(
      (n) => placedItems[n.slot_id] === n.correct
    );
    onComplete?.(allCorrect);
  };

  const handleReset = () => {
    setPlacedItems({});
    setSelectedWord(null);
    setIsSubmitted(false);
  };

  return (
    <div className="graphic-organizer-builder bg-white rounded-2xl border border-emerald-200 shadow-sm p-4 space-y-4">
      {/* Header */}
      <div className="flex items-center justify-between pb-3 border-b border-emerald-100">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 bg-emerald-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-4 • 구조 도해
          </span>
          <h4 className="font-bold text-sm text-slate-900">
            {data.title || 'Meyer 6대 설명 구조 그래픽 오거나이저'}
          </h4>
        </div>
        <span className="text-xs px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-800 border border-emerald-200 font-semibold">
          구조: {data.structure_type}
        </span>
      </div>

      <div className="text-xs text-slate-600 bg-emerald-50/60 p-2.5 rounded-xl border border-emerald-100 font-medium">
        📌 <b>활동 안내</b>: {data.instruction || '하단 단어 보관함에서 알맞은 개념을 선택하여 도해조직자의 빈 슬롯에 배치하세요.'}
      </div>

      {/* Graphic Organizer Slots Canvas */}
      <div className="p-4 bg-slate-50/80 rounded-xl border border-slate-200">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {data.nodes.map((node) => {
            const placed = placedItems[node.slot_id];
            const isCorrect = isSubmitted && placed === node.correct;
            const isWrong = isSubmitted && placed !== node.correct;

            let slotStyle = 'border-dashed border-emerald-300 bg-white hover:bg-emerald-50/50';
            if (isSubmitted) {
              if (isCorrect) {
                slotStyle = 'border-solid border-emerald-500 bg-emerald-50 text-emerald-950 font-bold';
              } else if (isWrong) {
                slotStyle = 'border-solid border-rose-400 bg-rose-50 text-rose-950';
              }
            } else if (placed) {
              slotStyle = 'border-solid border-emerald-600 bg-emerald-100/70 text-emerald-950 font-bold shadow-xs';
            } else if (selectedWord) {
              slotStyle = 'border-solid border-emerald-400 bg-emerald-50/90 animate-pulse';
            }

            return (
              <div
                key={node.slot_id}
                onClick={() => handleSlotClick(node.slot_id)}
                className={`p-3 rounded-xl border text-xs cursor-pointer transition-all flex flex-col justify-between min-h-[90px] ${slotStyle}`}
              >
                <div>
                  <div className="font-bold text-slate-700 flex items-center justify-between mb-1">
                    <span>{node.header}</span>
                    <span className="text-[10px] text-slate-400">#{node.slot_id}</span>
                  </div>
                  <div className="text-[11px] text-slate-500 line-clamp-2">
                    {node.sub}
                  </div>
                </div>

                <div className="pt-2 border-t border-slate-200/60 mt-2 flex items-center justify-between">
                  {placed ? (
                    <span className="font-bold text-slate-900 flex items-center gap-1">
                      <span>{placed}</span>
                      {isSubmitted && (
                        <span>{isCorrect ? '✅' : `❌ (정답: ${node.correct})`}</span>
                      )}
                    </span>
                  ) : (
                    <span className="text-[11px] text-slate-400 italic">
                      {selectedWord ? '여기를 터치하여 배치 📥' : '빈 슬롯 (터치)'}
                    </span>
                  )}
                  {placed && !isSubmitted && (
                    <span className="text-[10px] text-slate-400 hover:text-rose-500">
                      ✕ 취소
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Word Bank Dock */}
      <div className="p-3 bg-slate-100 rounded-xl border border-slate-200 space-y-2">
        <div className="flex items-center justify-between text-xs font-bold text-slate-700">
          <span>📦 개념어 보관함 (터치하여 선택 후 슬롯에 배치)</span>
          {isSubmitted && (
            <button
              onClick={handleReset}
              className="text-[11px] text-slate-600 underline hover:text-slate-900"
            >
              다시 배치하기 ↺
            </button>
          )}
        </div>
        <div className="flex flex-wrap gap-2">
          {data.word_bank.map((word, wIdx) => {
            const isPlaced = Object.values(placedItems).includes(word);
            const isSelected = selectedWord === word;

            return (
              <button
                key={wIdx}
                disabled={isPlaced || isSubmitted}
                onClick={() => handleWordBankClick(word)}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold border transition-all ${
                  isPlaced
                    ? 'bg-slate-200 text-slate-400 border-slate-300 line-through cursor-not-allowed'
                    : isSelected
                    ? 'bg-emerald-600 text-white border-emerald-700 shadow-md ring-2 ring-emerald-300'
                    : 'bg-white text-slate-800 border-slate-300 hover:border-emerald-400 shadow-xs'
                }`}
              >
                {word}
              </button>
            );
          })}
        </div>
      </div>

      {/* Submit / Reset Actions */}
      {!isSubmitted ? (
        <div className="flex justify-end pt-1">
          <button
            onClick={handleSubmit}
            disabled={!isAllFilled}
            className={`px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-sm ${
              isAllFilled
                ? 'bg-emerald-600 hover:bg-emerald-700 text-white cursor-pointer hover:shadow-md'
                : 'bg-slate-200 text-slate-400 cursor-not-allowed'
            }`}
          >
            도해조직자 완성 및 검증하기
          </button>
        </div>
      ) : (
        <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl text-xs text-emerald-900 flex items-center justify-between">
          <span>
            {data.nodes.every((n) => placedItems[n.slot_id] === n.correct)
              ? '🎉 축하합니다! 글의 구조를 완벽하게 도해화했습니다.'
              : '⚠️ 일부 개념의 배치가 어긋났습니다. 위의 정답 표시를 확인하세요.'}
          </span>
        </div>
      )}
    </div>
  );
};

function ReferenceOutline({ nodes }: { nodes: ReferenceNode[] }) {
  return <ul className="space-y-3">{nodes.map((node, i) => <li key={i} className="border-l-2 border-emerald-200 pl-3">
    <span className="font-semibold text-emerald-900">{node.label}</span>
    {node.text && <p className="mt-1 leading-relaxed text-slate-700">{node.text}</p>}
    {node.children && <div className="mt-2"><ReferenceOutline nodes={node.children} /></div>}
  </li>)}</ul>;
}

export const GraphicOrganizerBuilder: React.FC<GraphicOrganizerBuilderProps> = props => {
  if (props.data.activityType === 'reference') return <section className="bg-white border border-emerald-200 rounded-2xl p-5 space-y-4">
    <h3 className="font-bold text-lg">{props.data.title}</h3>
    <p className="text-sm text-slate-600">함께 읽는 생각 정리 자료예요. 본문의 어느 부분을 연결했는지 짚고, 내 말로 설명해 보세요.</p>
    <ReferenceOutline nodes={props.data.sections} />
  </section>;
  return <CardSortOrganizer {...props} data={props.data} />;
};
