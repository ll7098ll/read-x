import type { CommercialMasterData } from '../types/courseware';
import type { ContentLibrary, ConceptRecord } from '../types/contentLibrary';

/** Initial index only: 96 existing passages are NOT the complete national concept list. */
export function buildContentLibrary(data: CommercialMasterData): ContentLibrary {
  const concepts = new Map<string, ConceptRecord>();
  const passages: ContentLibrary['passages'] = [];
  const goals: ContentLibrary['goals'] = [];
  for (const slot of data.expository_slots_96 || []) {
    const gradeBand = slot.grade_num <= 2 ? '1-2' : slot.grade_num <= 4 ? '3-4' : '5-6';
    const c = slot.curriculum_concept;
    // Exact source claims are preserved; verified taxonomy IDs replace these after editorial review.
    const id = `concept:${gradeBand}:${encodeURIComponent([c.subject,c.unit,c.concept].join('|'))}`;
    concepts.set(id, { id, curriculum: '2022-revised', gradeBand, subjectClaim: c.subject, unitClaim: c.unit, name: c.concept,
      standardRefs: [], reviewState: 'needs_review' });
    goals.push({ id: slot.slot_id, grade: slot.grade_num, name: slot.sub_skill_name, performanceGoal: slot.mager_goal,
      prerequisiteGoalIds: slot.prereq_com_code ? [slot.prereq_com_code] : [], rubricState: 'needs_review',
      thinkingGuides: [
        { stage: 'notice', instruction: slot.prototype_step1_2.step1_mission },
        { stage: 'connect', instruction: slot.prototype_step1_2.step2_mission },
      ] });
    passages.push({ id: `passage:${slot.slot_id}:001`, version: 1, title: slot.real_csat_test.passage_title, grade: slot.grade_num,
      paragraphs: slot.real_csat_test.paragraphs, conceptIds: [id], goalIds: [slot.slot_id], structure: c.text_structure,
      sourceLessonId: slot.slot_id, reviewState: 'needs_review',
      provenance: { source: `commercialMasterData.json#${slot.slot_id}`, copyrightReview: 'needs_review', factualReview: 'needs_review' } });
  }
  return { schemaVersion: '1.0', concepts: [...concepts.values()], goals, passages, sources: [
    { id: 'moe-2022-33', title: '초중등학교 교육과정 총론 및 각론 고시', edition: '교육부 고시 제2022-33호',
      url: 'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=141&boardSeq=93458&lev=0', verification: 'notice_verified' },
    { id: 'nec-2026-1', title: '초중등학교 교육과정 일부개정 고시', edition: '국가교육위원회 고시 제2026-1호',
      url: 'https://ncic.re.kr/bbs/ncicnotice/view/1859.do?page=0&searchkey=&searchword=', verification: 'notice_verified' },
  ] };
}

export function passagesForGoal(library: ContentLibrary, goalId: string, options: { excludeIds?: string[]; approvedOnly?: boolean } = {}) {
  return library.passages.filter(p => p.goalIds.includes(goalId) && !options.excludeIds?.includes(p.id)
    && (!options.approvedOnly || p.reviewState === 'approved'));
}
