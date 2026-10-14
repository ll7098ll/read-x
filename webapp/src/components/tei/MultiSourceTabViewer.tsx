import React, { useState } from 'react';

interface MultiSourceTabViewerProps {
  passageTitle: string;
  passageHtml: string | React.ReactNode;
  visualHtml?: string;
  chartDataTitle?: string;
  chartPoints?: Array<{ label: string; value: string; linkedParaText: string }>;
  onPointHover?: (linkedText: string | null) => void;
}

export const MultiSourceTabViewer: React.FC<MultiSourceTabViewerProps> = ({
  passageTitle,
  passageHtml,
  visualHtml,
  chartDataTitle = '교과 연계 시각·통계 분석 자료',
  chartPoints = [],
  onPointHover,
}) => {
  const [activeTab, setActiveTab] = useState<'passage' | 'visual' | 'split'>('passage');
  const [hoveredPoint, setHoveredPoint] = useState<string | null>(null);

  const handlePointEnter = (linkedText: string) => {
    setHoveredPoint(linkedText);
    onPointHover?.(linkedText);
  };

  const handlePointLeave = () => {
    setHoveredPoint(null);
    onPointHover?.(null);
  };

  return (
    <div className="multi-source-tab-viewer bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden space-y-0">
      {/* Tab Navigation Header */}
      <div className="flex items-center justify-between px-4 py-2.5 bg-slate-50 border-b border-slate-200">
        <div className="flex items-center gap-1.5">
          <span className="px-2 py-0.5 bg-violet-700 text-white rounded-md text-[11px] font-black uppercase tracking-wider">
            TEI-5 • 다중 매체
          </span>
          <span className="font-bold text-xs text-slate-800 hidden sm:inline">
            복합 자료 교차 분석기
          </span>
        </div>

        <div className="flex items-center gap-1 bg-slate-200/80 p-0.5 rounded-lg text-xs font-bold">
          <button
            onClick={() => setActiveTab('passage')}
            className={`px-3 py-1 rounded-md transition-all ${
              activeTab === 'passage'
                ? 'bg-white text-violet-900 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📄 (가) 본문
          </button>
          <button
            onClick={() => setActiveTab('visual')}
            className={`px-3 py-1 rounded-md transition-all ${
              activeTab === 'visual'
                ? 'bg-white text-violet-900 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📊 (나) 도표/시각
          </button>
          <button
            onClick={() => setActiveTab('split')}
            className={`px-3 py-1 rounded-md transition-all ${
              activeTab === 'split'
                ? 'bg-white text-violet-900 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            ⚖️ 통합 비교 (1:1)
          </button>
        </div>
      </div>

      {/* Main Content Area */}
      <div className="p-4">
        {activeTab === 'passage' && (
          <div className="space-y-3">
            <h3 className="font-bold text-base text-slate-900 border-b pb-2">
              (가) {passageTitle}
            </h3>
            <div className="text-sm leading-relaxed text-slate-800">
              {passageHtml}
            </div>
          </div>
        )}

        {activeTab === 'visual' && (
          <div className="space-y-3">
            <h3 className="font-bold text-base text-slate-900 border-b pb-2">
              (나) {chartDataTitle}
            </h3>
            {visualHtml ? (
              <div
                className="p-3 bg-slate-50 rounded-xl border border-slate-200"
                dangerouslySetInnerHTML={{ __html: visualHtml }}
              />
            ) : (
              <div className="p-6 bg-slate-50 rounded-xl border border-slate-200 text-center text-slate-500 text-xs">
                시각 자료 렌더러
              </div>
            )}

            {/* Interactive Points Sync */}
            {chartPoints.length > 0 && (
              <div className="mt-4 p-3 bg-violet-50/60 rounded-xl border border-violet-100 space-y-2">
                <div className="text-xs font-bold text-violet-950">
                  🔍 도표 세부 지표 호버 연동 (마우스 오버 시 본문 원리와 연결)
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                  {chartPoints.map((pt, idx) => (
                    <div
                      key={idx}
                      onMouseEnter={() => handlePointEnter(pt.linkedParaText)}
                      onMouseLeave={handlePointLeave}
                      className={`p-2.5 rounded-lg border text-xs cursor-pointer transition-all ${
                        hoveredPoint === pt.linkedParaText
                          ? 'bg-violet-600 text-white border-violet-700 shadow-sm'
                          : 'bg-white text-slate-800 border-slate-200 hover:border-violet-300'
                      }`}
                    >
                      <div className="font-bold flex justify-between">
                        <span>{pt.label}</span>
                        <span className="font-mono">{pt.value}</span>
                      </div>
                      <div className="text-[11px] opacity-80 line-clamp-1 mt-0.5">
                        연동 원리: {pt.linkedParaText}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'split' && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
              <div className="font-bold text-xs text-slate-700 border-b pb-1">
                📄 (가) 본문 요약
              </div>
              <div className="text-xs leading-relaxed text-slate-800 max-h-[350px] overflow-y-auto">
                {passageHtml}
              </div>
            </div>

            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200 space-y-2">
              <div className="font-bold text-xs text-slate-700 border-b pb-1">
                📊 (나) 시각 자료 및 도표
              </div>
              <div className="max-h-[350px] overflow-y-auto">
                {visualHtml ? (
                  <div dangerouslySetInnerHTML={{ __html: visualHtml }} />
                ) : (
                  <div className="p-4 text-center text-xs text-slate-400">
                    시각 자료
                  </div>
                )}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
