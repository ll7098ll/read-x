import { buildContentLibrary } from '../../data/contentLibrary';
import React, { useState, useEffect, useMemo } from 'react';
import { useCoursewareStore } from '../../store/useCoursewareStore';
import {
  validateSlotPackage,
  exportFirestoreBundleJson,
  FIREBASE_COLLECTIONS,
} from '../../services/firebaseDbService';
import { BrandedCounselingReportModal } from './BrandedCounselingReportModal';
import { AcademySeatBillingCard } from './AcademySeatBillingCard';
import { PageHeading } from '../common/DesignSystem';
import { ThinkingLessonWorkbench } from './ThinkingLessonWorkbench';
import { Download, Library, Building2, Printer } from 'lucide-react';
import type {
  CommercialMasterData,
  SlotLessonPackage,
  CommonRemedialSlot,
} from '../../types/courseware';

interface ItemBankAdminStudioProps {
  data: CommercialMasterData;
}

export const ItemBankAdminStudio: React.FC<ItemBankAdminStudioProps> = ({ data }) => {
  const {
    customSlotsById,
    saveCustomSlotToDb,
    deleteCustomSlotFromDb,
    selectGradeAndSlot,
  } = useCoursewareStore();

  const library = useMemo(() => buildContentLibrary(data), [data]);
  const [adminSubTab, setAdminSubTab] = useState<'item_bank' | 'seat_billing'>('item_bank');
  const [showReportModal, setShowReportModal] = useState<boolean>(false);
  const [collectionTab, setCollectionTab] = useState<'expository' | 'common'>('expository');
  const [gradeFilter, setGradeFilter] = useState<number | 'ALL'>('ALL');
  const [domainFilter, setDomainFilter] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');

  // Merge base 96 slots with custom DB overrides
  const allExpositorySlots: SlotLessonPackage[] = (data.expository_slots_96 || []).map(
    (s) => customSlotsById[s.slot_id] || s
  );
  const allCommonSlots: CommonRemedialSlot[] = data.common_slots_36 || [];

  const filteredExp = allExpositorySlots.filter((s) => {
    if (gradeFilter !== 'ALL' && s.grade_num !== gradeFilter) return false;
    if (domainFilter !== 'ALL' && !s.subskill_code.startsWith(domainFilter)) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.trim().toLowerCase();
      const hay = `${s.slot_id} ${s.sub_skill_name} ${s.real_csat_test?.passage_title || ''} ${s.curriculum_concept?.concept || ''} ${s.curriculum_concept?.subject || ''}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });

  const filteredCom = allCommonSlots.filter((c) => {
    if (gradeFilter !== 'ALL' && c.grade_num !== gradeFilter) return false;
    if (searchQuery.trim()) {
      const q = searchQuery.trim().toLowerCase();
      const hay = `${c.code} ${c.title} ${c.sub_skill_name} ${c.rule_box}`.toLowerCase();
      if (!hay.includes(q)) return false;
    }
    return true;
  });

  const [selectedSlotId, setSelectedSlotId] = useState<string>(
    allExpositorySlots[0]?.slot_id || 'G5-EXP-V3-2'
  );
  const [selectedCommonCode, setSelectedCommonCode] = useState<string>(
    allCommonSlots[0]?.code || 'G1-COM-A1'
  );
  const [rightMode, setRightMode] = useState<'inspect' | 'editor'>('inspect');
  const [saveBanner, setSaveBanner] = useState<string | null>(null);

  const activeExpSlot =
    allExpositorySlots.find((s) => s.slot_id === selectedSlotId) ||
    allExpositorySlots[0];
  const activeComSlot =
    allCommonSlots.find((c) => c.code === selectedCommonCode) ||
    allCommonSlots[0];

  // Editable draft state for the Authoring Workbench
  const [draftSlot, setDraftSlot] = useState<SlotLessonPackage | null>(
    activeExpSlot ? JSON.parse(JSON.stringify(activeExpSlot)) : null
  );

  useEffect(() => {
    if (activeExpSlot) {
      setDraftSlot(JSON.parse(JSON.stringify(activeExpSlot)));
    }
  }, [selectedSlotId, customSlotsById]);

  const qaResult = draftSlot ? validateSlotPackage(draftSlot) : { isValid: true, errors: [], warnings: [] };

  const handleSaveToDb = () => {
    if (!draftSlot) return;
    if (!qaResult.isValid || !saveCustomSlotToDb(draftSlot)) {
      setSaveBanner('저장하지 않았습니다. 데이터 검증 오류와 수업 코드를 확인해 주세요.');
      return;
    }
    setSaveBanner(
      `✅ [${draftSlot.slot_id}] 수업 초안을 이 기기의 체험 저장소에 저장했습니다. 서버에는 전송되지 않았습니다.`
    );
    setTimeout(() => setSaveBanner(null), 4000);
  };

  const handleExportFirestoreJson = () => {
    const jsonStr = exportFirestoreBundleJson(data, customSlotsById);
    const blob = new Blob([jsonStr], { type: 'application/json;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `firestore_seed_132_item_bank_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const totalQuestionsCount =
    allExpositorySlots.reduce(
      (acc, s) => acc + (s.real_csat_test?.questions?.length || 0) + 1 + (s.prescription_clinic?.step3_vaccine?.items?.length || 0),
      0
    ) + allCommonSlots.length * 4;

  return (
    <div className="space-y-4 font-sans text-slate-800">
      <PageHeading eyebrow="CONTENT STUDIO" title="좋은 수업의 바탕을 만듭니다." description="세부목표, 교과 개념, 지문을 연결하고 수업 자료를 다듬어요." />
      <ThinkingLessonWorkbench />
      <section className="rounded-2xl bg-teal-50 border border-teal-200 p-5 space-y-2">
        <h2 className="font-bold text-lg">세부목표와 교과 개념으로 연결하는 지문 자료실</h2>
        <p>{library.goals.length}개 세부목표 · {library.concepts.length}개 개념 후보 · {library.passages.length}개 기존 지문</p>
        <p className="text-sm text-slate-600">하나의 목표에 여러 소재와 난도의 지문을 연결합니다. 현재 목록은 기존 자료에서 가져온 후보이며, 2022 개정 교육과정 전체 목록이 아닙니다. 공식 성취기준·출처·내용 검수가 필요합니다.</p>
      </section>
      {/* Clean DB Telemetry & Authoring CMS Banner */}
      <div className="bg-white rounded-3xl border border-slate-200/80 p-6 sm:p-7 shadow-xs space-y-4">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-2.5 py-0.5 rounded-md text-[11px] font-bold bg-amber-50 text-amber-800 border border-amber-200">
                READX CONTENT LIBRARY
              </span>
              <span className="text-xs text-slate-400 font-mono hidden md:inline">
                이 기기의 콘텐츠 작업 공간
              </span>
            </div>
            <h2 className="text-xl sm:text-2xl font-black text-slate-900 tracking-tight mt-1">
              수업 자료 편집과 검토
            </h2>
            <p className="text-xs text-slate-500 mt-1">
              초등 1~6학년의 기존 자료를 살펴보고, 초안을 저장하거나 파일로 내보냅니다.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2.5">
            <div className="bg-slate-50 border border-slate-200/80 rounded-2xl px-3.5 py-2 text-xs">
              <div className="text-slate-500 font-bold">등록 자료</div>
              <div className="font-black text-slate-900 text-sm mt-0.5">
                {allExpositorySlots.length + allCommonSlots.length}개
              </div>
            </div>
            <div className="bg-slate-50 border border-slate-200/80 rounded-2xl px-3.5 py-2 text-xs">
              <div className="text-slate-500 font-bold">객관식 문항</div>
              <div className="font-black text-blue-600 text-sm mt-0.5">
                {allExpositorySlots.reduce((n,s)=>n+(s.real_csat_test?.questions?.length||0),0)}개
              </div>
            </div>
            <button
              onClick={handleExportFirestoreJson}
              className="px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs shadow-xs transition flex items-center gap-1.5 cursor-pointer"
            >
              <Download size={15}/><span>자료 파일 내보내기</span>
            </button>
          </div>
        </div>

        {saveBanner && (
          <div className="mt-3 p-3 rounded-xl bg-emerald-950 border border-emerald-500 text-emerald-200 text-xs font-black">
            {saveBanner}
          </div>
        )}
      </div>

      {/* Admin Hub Multi-Module Navigation Tabs */}
      <div className="bg-white rounded-2xl border border-slate-200/80 p-2 shadow-2xs flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-1.5 bg-slate-100/80 p-1 rounded-xl">
          <button
            onClick={() => setAdminSubTab('item_bank')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-1.5 cursor-pointer ${
              adminSubTab === 'item_bank'
                ? 'bg-white text-slate-900 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <Library size={16}/><span>수업 자료실</span>
          </button>
          <button
            onClick={() => setAdminSubTab('seat_billing')}
            className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-1.5 cursor-pointer ${
              adminSubTab === 'seat_billing'
                ? 'bg-white text-indigo-700 shadow-xs'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <Building2 size={16}/><span>학원 운영 예시</span>
            <span className="text-[10px] px-1.5 py-0.5 rounded bg-indigo-50 text-indigo-700 font-bold border border-indigo-200">
              체험
            </span>
          </button>
        </div>

        <button
          onClick={() => setShowReportModal(true)}
          className="px-4 py-2 rounded-xl text-xs font-bold bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200/80 transition flex items-center gap-1.5 cursor-pointer"
        >
          <Printer size={16}/><span>상담 보고서 예시</span>
        </button>
      </div>

      {adminSubTab === 'seat_billing' ? (
        <AcademySeatBillingCard
          data={data}
          onOpenReportModal={() => setShowReportModal(true)}
        />
      ) : (
        /* Main 12-Column CMS Workspace */
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-4 items-start">
          {/* Left 4 Columns: 132-Slot DB Browser & Filter */}
          <div className="lg:col-span-4 bg-white rounded-2xl border border-slate-200 p-4 shadow-sm space-y-3">
          {/* Collection Tabs */}
          <div className="grid grid-cols-2 gap-1.5 bg-slate-100 p-1 rounded-xl">
            <button
              onClick={() => setCollectionTab('expository')}
              className={`py-2 rounded-lg text-xs font-black transition ${
                collectionTab === 'expository'
                  ? 'bg-slate-900 text-white shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              📘 설명문 정규 차시 ({allExpositorySlots.length})
            </button>
            <button
              onClick={() => setCollectionTab('common')}
              className={`py-2 rounded-lg text-xs font-black transition ${
                collectionTab === 'common'
                  ? 'bg-slate-900 text-white shadow-sm'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              🪜 공통기초 모듈 ({allCommonSlots.length})
            </button>
          </div>

          {/* Grade & Domain Filter Pills */}
          <div className="space-y-2">
            <div className="flex flex-wrap gap-1">
              {(['ALL', 1, 2, 3, 4, 5, 6] as const).map((g) => (
                <button
                  key={String(g)}
                  onClick={() => setGradeFilter(g)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-extrabold border transition ${
                    gradeFilter === g
                      ? 'bg-blue-600 text-white border-blue-600'
                      : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                  }`}
                >
                  {g === 'ALL' ? '전 학년' : `${g}학년`}
                </button>
              ))}
            </div>

            {collectionTab === 'expository' && (
              <div className="flex flex-wrap gap-1">
                {[
                  { id: 'ALL', label: '전 영역(16)' },
                  { id: 'V1', label: '사실적(V1)' },
                  { id: 'V2', label: '추론적(V2)' },
                  { id: 'V3', label: '비판적(V3)' },
                  { id: 'W', label: '작문·퇴고(W)' },
                ].map((d) => (
                  <button
                    key={d.id}
                    onClick={() => setDomainFilter(d.id)}
                    className={`px-2 py-1 rounded-lg text-[11px] font-extrabold border transition ${
                      domainFilter === d.id
                        ? 'bg-indigo-600 text-white border-indigo-600'
                        : 'bg-slate-50 text-slate-600 border-slate-200 hover:bg-slate-100'
                    }`}
                  >
                    {d.label}
                  </button>
                ))}
              </div>
            )}

            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="슬롯 코드(G5-EXP-V2-3), 제목, 교과 개념 검색..."
              aria-label="콘텐츠 자료 검색"
              className="w-full px-3 py-2 rounded-xl border border-slate-300 text-xs focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
          </div>

          {/* Slot List */}
          <div className="max-h-[68vh] overflow-y-auto space-y-1.5 pr-1">
            {collectionTab === 'expository' ? (
              filteredExp.map((slot) => {
                const isSelected = slot.slot_id === activeExpSlot?.slot_id;
                const isCustomEdited = Boolean(customSlotsById[slot.slot_id]);
                return (
                  <button
                    key={slot.slot_id}
                    onClick={() => setSelectedSlotId(slot.slot_id)}
                    className={`w-full text-left p-2.5 rounded-xl border transition ${
                      isSelected
                        ? 'bg-blue-50 border-blue-600 ring-1 ring-blue-600'
                        : 'bg-white border-slate-200 hover:bg-slate-50'
                    }`}
                  >
                    <div className="flex items-center justify-between gap-1">
                      <span className="font-black text-xs text-blue-900">
                        {slot.slot_id}
                      </span>
                      <div className="flex items-center gap-1">
                        {isCustomEdited && (
                          <span className="px-1.5 py-0.5 rounded bg-amber-100 text-amber-800 text-[10px] font-black">
                            DB 수정됨
                          </span>
                        )}
                        <span className="px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 text-[10px] font-bold">
                          KReaD {slot.complexity_metrics.current_kread}
                        </span>
                      </div>
                    </div>
                    <div className="font-extrabold text-xs text-slate-900 mt-1 truncate">
                      {slot.real_csat_test?.passage_title}
                    </div>
                    <div className="text-[11px] text-slate-500 truncate mt-0.5">
                      {slot.curriculum_concept?.subject} · {slot.sub_skill_name}
                    </div>
                  </button>
                );
              })
            ) : (
              filteredCom.map((com) => {
                const isSelected = com.code === activeComSlot?.code;
                return (
                  <button
                    key={com.code}
                    onClick={() => setSelectedCommonCode(com.code)}
                    className={`w-full text-left p-2.5 rounded-xl border transition ${
                      isSelected
                        ? 'bg-indigo-50 border-indigo-600 ring-1 ring-indigo-600'
                        : 'bg-white border-slate-200 hover:bg-slate-50'
                    }`}
                  >
                    <div className="flex items-center justify-between">
                      <span className="font-black text-xs text-indigo-900">
                        {com.code}
                      </span>
                      <span className="px-1.5 py-0.5 rounded bg-indigo-100 text-indigo-800 text-[10px] font-bold">
                        {com.grade} 공통기초
                      </span>
                    </div>
                    <div className="font-extrabold text-xs text-slate-900 mt-1 truncate">
                      {com.title}
                    </div>
                    <div className="text-[11px] text-slate-500 truncate mt-0.5">
                      {com.layer}
                    </div>
                  </button>
                );
              })
            )}
          </div>
        </div>

        {/* Right 8 Columns: Slot Inspector & Interactive Item Authoring Editor */}
        <div className="lg:col-span-8 bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">
          {collectionTab === 'expository' && activeExpSlot && draftSlot ? (
            <>
              {/* Header & Mode Switch */}
              <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-200">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="px-2.5 py-0.5 rounded-lg bg-blue-600 text-white text-xs font-black">
                      {activeExpSlot.slot_id}
                    </span>
                    <span className="text-xs font-bold text-slate-500">
                      {activeExpSlot.grade_band} · {activeExpSlot.domain} · {activeExpSlot.curriculum_concept.subject} ({activeExpSlot.curriculum_concept.unit})
                    </span>
                  </div>
                  <h3 className="text-base md:text-lg font-black text-slate-900 mt-1">
                    {activeExpSlot.real_csat_test.passage_title}
                  </h3>
                </div>

                <div className="flex flex-wrap items-center gap-2">
                  <div className="bg-slate-100 p-1 rounded-xl flex items-center gap-1">
                    <button
                      onClick={() => setRightMode('inspect')}
                      className={`px-3 py-1.5 rounded-lg text-xs font-black transition ${
                        rightMode === 'inspect'
                          ? 'bg-white text-slate-900 shadow-sm'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      👁️ DB 문항 패키지 상세 검수
                    </button>
                    <button
                      onClick={() => setRightMode('editor')}
                      className={`px-3 py-1.5 rounded-lg text-xs font-black transition ${
                        rightMode === 'editor'
                          ? 'bg-white text-blue-700 shadow-sm'
                          : 'text-slate-600 hover:text-slate-900'
                      }`}
                    >
                      ✍️ 문항 출제·수정 에디터
                    </button>
                  </div>

                  <button
                    onClick={() =>
                      selectGradeAndSlot(
                        activeExpSlot.grade_num,
                        activeExpSlot.slot_id,
                        'studio'
                      )
                    }
                    className="px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-black shadow transition"
                  >
                    🚀 학생 스튜디오에서 실행 ➔
                  </button>
                </div>
              </div>

              {/* Automated Psychometric QA Gate Status Bar */}
              <div
                className={`p-3 rounded-xl border text-xs flex flex-wrap items-center justify-between gap-2 ${
                  qaResult.isValid
                    ? 'bg-emerald-50 border-emerald-300 text-emerald-950'
                    : 'bg-rose-50 border-rose-300 text-rose-950'
                }`}
              >
                <div className="font-black flex items-center gap-2">
                  <span>
                    {qaResult.isValid
                      ? '데이터 형식·참조 검사 통과 · 교육내용·출처·난도 검수는 별도 필요'
                      : `🚨 [검수 오류 ${qaResult.errors.length}건] 문항 저장 전 아래 항목을 확인하세요`}
                  </span>
                </div>
                <span className="text-[11px] font-bold opacity-80">
                  {activeExpSlot.real_csat_test.passage_spec}
                </span>
              </div>

              {qaResult.errors.length > 0 && <ul role="alert" className="list-disc pl-6 text-sm text-rose-800 space-y-1">{qaResult.errors.map((error, i) => <li key={i}>{error}</li>)}</ul>}
              {qaResult.warnings.length > 0 && <ul className="list-disc pl-6 text-sm text-amber-900 space-y-1">{qaResult.warnings.map((warning, i) => <li key={i}>{warning}</li>)}</ul>}
              {rightMode === 'inspect' ? (
                <div className="space-y-4">
                  {/* Mager Goal & Dick & Carey 3-Step Spec */}
                  <div className="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-2 text-xs">
                    <div className="font-black text-slate-900">
                      🎯 Mager 수행목표: <span className="font-normal text-slate-700">{activeExpSlot.mager_goal}</span>
                    </div>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-2 pt-1">
                      <div className="p-2.5 rounded-lg bg-white border border-slate-200">
                        <div className="font-black text-blue-700 mb-0.5">Step 1 · 단서 포착 (TEI-1)</div>
                        <div className="text-slate-600">{activeExpSlot.prototype_step1_2.step1_mission}</div>
                      </div>
                      <div className="p-2.5 rounded-lg bg-white border border-slate-200">
                        <div className="font-black text-indigo-700 mb-0.5">Step 2 · 구조 연결 (TEI-3/4)</div>
                        <div className="text-slate-600">{activeExpSlot.prototype_step1_2.step2_mission}</div>
                      </div>
                      <div className="p-2.5 rounded-lg bg-white border border-slate-200">
                        <div className="font-black text-emerald-700 mb-0.5">Step 3 · 선수 역추적 & 백신</div>
                        <div className="text-slate-600">
                          선수 위계: <b>{activeExpSlot.prereq_com_code || '공통기초'}</b> · 클리닉 3단계 탑재
                        </div>
                      </div>
                    </div>
                  </div>

                  {/* Passage & HotText Cues Preview */}
                  <div className="p-4 rounded-xl bg-[#FCFBF7] border border-slate-300 space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="font-black text-xs text-slate-800">
                        📖 수록 지문 원문 ({activeExpSlot.real_csat_test.paragraphs.length}문단)
                      </span>
                      <span className="text-[11px] font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded">
                        HotText 단서 {activeExpSlot.commercial.Interactive_hottext_cues.length}개 매핑됨
                      </span>
                    </div>
                    <div className="space-y-2 text-xs md:text-sm text-slate-900 leading-relaxed">
                      {activeExpSlot.real_csat_test.paragraphs.map((p, idx) => (
                        <p key={idx}>
                          <b className="text-blue-600 mr-1">[{idx + 1}문단]</b>
                          <span dangerouslySetInnerHTML={{ __html: p }} />
                        </p>
                      ))}
                    </div>
                    {activeExpSlot.real_csat_test.visual_html && (
                      <div
                        className="mt-3 p-3 bg-white rounded-xl border border-slate-200 text-xs"
                        dangerouslySetInnerHTML={{
                          __html: activeExpSlot.real_csat_test.visual_html,
                        }}
                      />
                    )}
                  </div>

                  {/* CSAT Questions + D1~D6 Formulas + 3-Stage Scaffolding */}
                  <div className="space-y-3">
                    <h4 className="font-black text-sm text-slate-900">
                      📝 수록 수능형 실전 문항 ({activeExpSlot.real_csat_test.questions.length}문항) & 3단계 점진적 스캐폴딩 명세
                    </h4>
                    {activeExpSlot.real_csat_test.questions.map((q, qIdx) => {
                      const sc = activeExpSlot.commercial.question_scaffolding?.[qIdx];
                      return (
                        <div
                          key={q.q_no}
                          className="p-4 rounded-xl border border-slate-200 bg-slate-50/60 space-y-2.5 text-xs"
                        >
                          <div className="flex items-center justify-between">
                            <span className="font-black text-indigo-800">
                              문항 #{q.q_no} · {q.archetype}
                            </span>
                            {sc && (
                              <span className="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold text-[11px]">
                                스포트라이트 근거: {sc.target_para_idx + 1}문단
                              </span>
                            )}
                          </div>
                          <div
                            className="font-black text-slate-900 text-sm"
                            dangerouslySetInnerHTML={{ __html: q.stem }}
                          />
                          {q.bogi && (
                            <div
                              className="p-2.5 rounded-lg bg-white border border-slate-200"
                              dangerouslySetInnerHTML={{ __html: q.bogi }}
                            />
                          )}
                          <div className="space-y-1.5">
                            {q.options.map((opt) => (
                              <div
                                key={opt.no}
                                className={`p-2.5 rounded-lg border ${
                                  opt.is_correct
                                    ? 'bg-emerald-50 border-emerald-400 text-emerald-950'
                                    : 'bg-white border-slate-200 text-slate-800'
                                }`}
                              >
                                <div className="flex items-center justify-between font-bold">
                                  <span>
                                    {opt.no}. {opt.text}
                                  </span>
                                  <span
                                    className={`px-2 py-0.5 rounded text-[10px] font-black shrink-0 ml-2 ${
                                      opt.is_correct
                                        ? 'bg-emerald-600 text-white'
                                        : 'bg-rose-100 text-rose-800'
                                    }`}
                                  >
                                    {opt.formula}
                                  </span>
                                </div>
                                <div className="text-[11px] text-slate-600 mt-1">
                                  💡 {opt.explanation}
                                </div>
                              </div>
                            ))}
                          </div>
                          {sc && (
                            <div className="p-2.5 rounded-lg bg-amber-50/80 border border-amber-200 text-[11px] space-y-1">
                              <div>
                                <b>🔍 본문 자동 스포트라이트 문장:</b> “{sc.spotlight_quote}”
                              </div>
                              <div>
                                <b>1차 오답 힌트:</b> {sc.step1_hint}
                              </div>
                              <div>
                                <b>2차 오답 힌트:</b> {sc.step2_hint}
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              ) : (
                /* Interactive Item Authoring & Editing Form */
                <div className="space-y-4 text-xs">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div>
                      <label className="block font-black text-slate-700 mb-1">
                        지문 제목 (Passage Title)
                      </label>
                      <input
                        type="text"
                        value={draftSlot.real_csat_test.passage_title}
                        onChange={(e) =>
                          setDraftSlot({
                            ...draftSlot,
                            real_csat_test: {
                              ...draftSlot.real_csat_test,
                              passage_title: e.target.value,
                            },
                          })
                        }
                        className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold"
                      />
                    </div>
                    <div>
                      <label className="block font-black text-slate-700 mb-1">
                        연계 교과 및 핵심 개념
                      </label>
                      <input
                        type="text"
                        value={draftSlot.curriculum_concept.concept}
                        onChange={(e) =>
                          setDraftSlot({
                            ...draftSlot,
                            curriculum_concept: {
                              ...draftSlot.curriculum_concept,
                              concept: e.target.value,
                            },
                          })
                        }
                        className="w-full px-3 py-2 rounded-xl border border-slate-300"
                      />
                    </div>
                  </div>

                  {/* Paragraph Editor */}
                  <div>
                    <label className="block font-black text-slate-700 mb-1">
                      지문 문단 편집 (문단별 줄바꿈 구분)
                    </label>
                    <textarea
                      rows={6}
                      value={draftSlot.real_csat_test.paragraphs.join('\n\n')}
                      onChange={(e) =>
                        setDraftSlot({
                          ...draftSlot,
                          real_csat_test: {
                            ...draftSlot.real_csat_test,
                            paragraphs: e.target.value
                              .split(/\n\s*\n/)
                              .map((p) => p.trim())
                              .filter(Boolean),
                          },
                        })
                      }
                      className="w-full p-3 rounded-xl border border-slate-300 leading-relaxed"
                    />
                  </div>

                  {/* Question #1 & #2 Editor */}
                  {draftSlot.real_csat_test.questions.map((q, qIdx) => (
                    <div
                      key={q.q_no}
                      className="p-4 rounded-xl bg-slate-50 border border-slate-200 space-y-3"
                    >
                      <div className="font-black text-indigo-800">
                        ✏️ 실전 문항 #{q.q_no} 출제·수정
                      </div>
                      <div>
                        <label className="block font-bold text-slate-700 mb-1">
                          발문 (Question Stem)
                        </label>
                        <input
                          type="text"
                          value={q.stem}
                          onChange={(e) => {
                            const nextQs = [...draftSlot.real_csat_test.questions];
                            nextQs[qIdx] = { ...q, stem: e.target.value };
                            setDraftSlot({
                              ...draftSlot,
                              real_csat_test: {
                                ...draftSlot.real_csat_test,
                                questions: nextQs,
                              },
                            });
                          }}
                          className="w-full px-3 py-2 rounded-lg border border-slate-300 font-bold bg-white"
                        />
                      </div>

                      <div className="space-y-2">
                        <div className="font-bold text-slate-700">
                          선지 및 D1~D6 오답 공식·해설
                        </div>
                        {q.options.map((opt, oIdx) => (
                          <div
                            key={opt.no}
                            className="p-2.5 rounded-lg bg-white border border-slate-200 space-y-1.5"
                          >
                            <div className="flex items-center gap-2">
                              <span className="font-black text-slate-700 w-6">
                                {opt.no}번
                              </span>
                              <input
                                type="text"
                                value={opt.text}
                                onChange={(e) => {
                                  const nextQs = [...draftSlot.real_csat_test.questions];
                                  const nextOpts = [...q.options];
                                  nextOpts[oIdx] = { ...opt, text: e.target.value };
                                  nextQs[qIdx] = { ...q, options: nextOpts };
                                  setDraftSlot({
                                    ...draftSlot,
                                    real_csat_test: {
                                      ...draftSlot.real_csat_test,
                                      questions: nextQs,
                                    },
                                  });
                                }}
                                className="flex-1 px-2.5 py-1.5 rounded border border-slate-300"
                              />
                              <input
                                type="text"
                                value={opt.formula}
                                onChange={(e) => {
                                  const nextQs = [...draftSlot.real_csat_test.questions];
                                  const nextOpts = [...q.options];
                                  nextOpts[oIdx] = { ...opt, formula: e.target.value };
                                  nextQs[qIdx] = { ...q, options: nextOpts };
                                  setDraftSlot({
                                    ...draftSlot,
                                    real_csat_test: {
                                      ...draftSlot.real_csat_test,
                                      questions: nextQs,
                                    },
                                  });
                                }}
                                className="w-40 px-2 py-1.5 rounded border border-slate-300 text-[11px] font-bold"
                                placeholder="예: D1 인과 역전 함정"
                              />
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  ))}

                  <div className="flex items-center justify-between pt-2">
                    {customSlotsById[draftSlot.slot_id] ? (
                      <button
                        onClick={() => deleteCustomSlotFromDb(draftSlot.slot_id)}
                        className="px-3.5 py-2 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold"
                      >
                        🔄 초기 마스터 데이터로 복원
                      </button>
                    ) : (
                      <div />
                    )}
                    <button
                      onClick={handleSaveToDb}
                      className="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-black shadow transition"
                    >
                      💾 문항 뱅크 DB에 저장 및 즉시 배포
                    </button>
                  </div>
                </div>
              )}
            </>
          ) : (
            /* Common Foundation 36 Slot Inspector */
            activeComSlot && (
              <div className="space-y-4">
                <div className="flex items-center justify-between pb-3 border-b border-slate-200">
                  <div>
                    <span className="px-2.5 py-0.5 rounded-lg bg-indigo-600 text-white text-xs font-black">
                      {activeComSlot.code}
                    </span>
                    <h3 className="text-base md:text-lg font-black text-slate-900 mt-1">
                      {activeComSlot.title}
                    </h3>
                    <p className="text-xs text-slate-500 mt-0.5">
                      {activeComSlot.layer} · {activeComSlot.curriculum_basis}
                    </p>
                  </div>
                </div>

                <div className="p-4 rounded-xl bg-amber-50 border border-amber-200 text-xs space-y-1.5">
                  <div className="font-black text-amber-950">📌 핵심 원리 공식 (Rule Box)</div>
                  <div className="text-amber-900 leading-relaxed">{activeComSlot.rule_box}</div>
                </div>

                <div className="p-4 rounded-xl bg-slate-50 border border-slate-200 text-xs space-y-2">
                  <div className="font-black text-slate-900">📖 예문 및 징검다리 확인 문항</div>
                  <div className="p-3 rounded-lg bg-white border border-slate-200 text-slate-800">
                    {activeComSlot.passage_snippet}
                  </div>
                  <div className="font-bold text-slate-900 pt-1">
                    Q. {activeComSlot.mini_question}
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {activeComSlot.choices.map((ch) => (
                      <span
                        key={ch}
                        className={`px-3 py-1.5 rounded-lg border font-bold ${
                          ch === activeComSlot.correct
                            ? 'bg-emerald-100 border-emerald-500 text-emerald-950'
                            : 'bg-white border-slate-200 text-slate-700'
                        }`}
                      >
                        {ch} {ch === activeComSlot.correct && '⭕'}
                      </span>
                    ))}
                  </div>
                  <div className="text-slate-600 pt-1">💡 {activeComSlot.feedback}</div>
                </div>
              </div>
            )
          )}
        </div>
      </div>
      )}

      {/* Screen 22: Branded Counseling Report Modal */}
      {showReportModal && (
        <BrandedCounselingReportModal
          data={data}
          onClose={() => setShowReportModal(false)}
        />
      )}
    </div>
  );
};

