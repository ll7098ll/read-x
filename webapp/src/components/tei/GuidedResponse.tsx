import React, { useState } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';

export function GuidedResponse({ title, instruction, template, draftKey }: {
  title: string; instruction: string; template?: string; draftKey?: string;
}) {
  const { responseDrafts, saveResponseDraft } = useCoursewareStore();
  const [preview, setPreview] = useState('');
  const [saveError, setSaveError] = useState(false);
  const value = draftKey ? responseDrafts[draftKey] || '' : preview;
  return <section className="rounded-2xl bg-white border border-teal-200 p-5 space-y-4">
    <h3 className="text-lg font-bold text-slate-900">{title}</h3>
    <p className="leading-relaxed text-slate-700">{instruction}</p>
    {template && <div className="rounded-xl bg-teal-50 p-3 text-sm"><b>문장 틀</b><p className="mt-2">{template}</p></div>}
    <label className="block font-semibold text-sm">내 생각과 근거
      <textarea className="mt-2 w-full rounded-xl border border-slate-300 p-3 text-base leading-relaxed min-h-40 focus:ring-2 focus:ring-teal-600"
        value={value} maxLength={10000} placeholder="어디를 보고, 왜 그렇게 생각했는지 적어 보세요."
        onChange={e => {
          if (!draftKey) { setPreview(e.target.value); return; }
          try { saveResponseDraft(draftKey, e.target.value); setSaveError(false); }
          catch { setSaveError(true); }
        }} />
    </label>
    <p role={saveError ? 'alert' : 'status'} className="text-xs text-slate-500">{saveError ? '기기에 저장하지 못했어요. 작성한 문장을 복사해 보관한 뒤 저장 공간을 확인해 주세요.' : draftKey ? '이 기기의 체험용 초안으로 보관합니다. 교사에게 제출된 답안은 아닙니다.' : '미리보기 답안입니다.'} 서술한 내용은 교사의 확인이 필요해요.</p>
  </section>;
}
