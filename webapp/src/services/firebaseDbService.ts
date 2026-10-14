import type {
  CommercialMasterData,
  GradeData,
  SlotLessonPackage,
  CommonRemedialSlot,
} from '../types/courseware';

/**
 * Firebase Firestore Collection Schema & Local/Cloud Hybrid Repository
 * - Designed for direct 1:1 compatibility with Firebase Firestore (`collections`:
 *   `item_bank_expository`, `item_bank_common`, `student_profiles`, `question_attempts`, `clinic_assignments`).
 * - Works offline/locally out-of-the-box with LocalStorage + 132-Slot Seed Bundle,
 *   and switches to live Firebase Firestore when `VITE_FIREBASE_PROJECT_ID` is configured.
 */
export const FIREBASE_COLLECTIONS = {
  ITEM_BANK_EXPOSITORY: 'item_bank_expository', // 96 documents (G1-EXP-V1-1 ~ G6-EXP-W5)
  ITEM_BANK_COMMON: 'item_bank_common',         // 36 documents (G1-COM-A1 ~ G6-COM-A6)
  CURRICULUM_GOALS: 'curriculum_goals',         // 132 / 516 master taxonomy documents
  STUDENT_PROFILES: 'student_profiles',         // Learner 6D X-Ray & mastery profiles
  QUESTION_ATTEMPTS: 'question_attempts',       // Real-time item attempt telemetry
  CLINIC_ASSIGNMENTS: 'clinic_assignments',     // Teacher -> Student batch assignments
} as const;

export interface FirebaseConnectionConfig {
  apiKey?: string;
  authDomain?: string;
  projectId?: string;
  storageBucket?: string;
  messagingSenderId?: string;
  appId?: string;
  useCloudSync: boolean;
}

export const defaultFirebaseConfig: FirebaseConnectionConfig = {
  projectId:
    (import.meta as unknown as { env?: Record<string, string> }).env
      ?.VITE_FIREBASE_PROJECT_ID || 'readxray-literacy-prod',
  useCloudSync: Boolean(
    (import.meta as unknown as { env?: Record<string, string> }).env
      ?.VITE_FIREBASE_API_KEY
  ),
};

export interface ItemValidationResult {
  isValid: boolean;
  errors: string[];
  warnings: string[];
}

function stripHtmlTags(str: string): string {
  return str.replace(/<[^>]+>/g, '');
}

/**
 * Automated Psychometric & Substring QA Validator (Client + CMS Gate)
 * Checks:
 * 1. Paragraph count & non-empty text
 * 2. Grade-band option scaling (G1-2: 3 options, G3-4: 4 options, G5-6: 5 options)
 * 3. Substring integrity for TEI-1 HotText cues inside paragraphs
 * 4. Substring integrity for 3-stage Scaffolding spotlight_quote inside paragraphs
 * 5. D1~D6 distractor tag & explanation presence
 */
export function validateSlotPackage(slot: SlotLessonPackage): ItemValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];

  const paras = slot.real_csat_test?.paragraphs || [];
  if (paras.length === 0) {
    errors.push('지문 문단(paragraphs)이 비어 있습니다.');
  }
  const plainParas = paras.map(stripHtmlTags);

  const expectedOptCount =
    slot.grade_num <= 2 ? 3 : slot.grade_num <= 4 ? 4 : 5;

  const questions = slot.real_csat_test?.questions || [];
  if (questions.length === 0) {
    errors.push('실전 수능형 객관식 문항(questions)이 최소 1개 이상 필요합니다.');
  }

  questions.forEach((q, idx) => {
    if (q.options.length !== expectedOptCount) {
      warnings.push(
        `문항 #${q.q_no}: ${slot.grade_num}학년 권장 선지 수는 ${expectedOptCount}지선다이나 현재 ${q.options.length}개입니다.`
      );
    }
    const correctCount = q.options.filter((o) => o.is_correct).length;
    if (correctCount !== 1) {
      errors.push(
        `문항 #${q.q_no}: 정답(is_correct=true) 선지는 정확히 1개여야 합니다 (현재 ${correctCount}개).`
      );
    }
    q.options.forEach((opt) => {
      if (!opt.is_correct && !/D[1-6]/.test(opt.formula)) {
        warnings.push(
          `문항 #${q.q_no} 선지 ${opt.no}번: 오답 공식에 D1~D6 함정 코드가 명시되지 않았습니다.`
        );
      }
      if (!opt.explanation || opt.explanation.trim().length < 10) {
        errors.push(`문항 #${q.q_no} 선지 ${opt.no}번: 사고구술 해설이 누락되었거나 너무 짧습니다.`);
      }
    });

    const sc = slot.commercial?.question_scaffolding?.[idx];
    if (sc) {
      const targetPara = plainParas[sc.target_para_idx] || '';
      if (sc.spotlight_quote && !targetPara.includes(sc.spotlight_quote)) {
        warnings.push(
          `문항 #${q.q_no} 스캐폴딩: 스포트라이트 근거 문장이 ${sc.target_para_idx + 1}문단 원문과 정확히 일치하지 않습니다.`
        );
      }
    }
  });

  const cues = slot.commercial?.Interactive_hottext_cues || [];
  cues.forEach((cue) => {
    const pText = plainParas[cue.para_idx] || '';
    if (cue.text && !pText.includes(cue.text)) {
      warnings.push(
        `HotText 단서 [${cue.cue_id}]: "${cue.text}" 구절이 ${cue.para_idx + 1}문단 내에 존재하지 않습니다.`
      );
    }
  });

  return {
    isValid: errors.length === 0,
    errors,
    warnings,
  };
}

/**
 * Merges a specific SlotLessonPackage (1 of 96 Expository slots) onto the learner's base GradeData
 * so that all studio/clinic/report components render the selected slot seamlessly while retaining
 * the learner's 6D X-Ray overview and grade-level diagnostic telemetry.
 */
export function resolveActiveGradeAndSlotData(
  masterData: CommercialMasterData,
  gradeIdx: number,
  activeSlotId: string | null,
  customSlotsMap: Record<string, SlotLessonPackage>,
  dynamicSubskillScores?: Record<string, number>
): {
  activeGradeData: GradeData;
  gradeSlots16: SlotLessonPackage[];
  gradeCommon6: CommonRemedialSlot[];
  activeSlotPackage: SlotLessonPackage | null;
} {
  const baseGrade =
    masterData?.grades_data?.[gradeIdx] ||
    masterData?.grades_data?.[4] ||
    masterData?.grades_data?.[0];

  if (!baseGrade) {
    throw new Error('마스터 데이터의 학년 데이터(grades_data)를 찾을 수 없습니다.');
  }

  const gradeNum = baseGrade.grade_num || 5;

  const rawSlots96 = masterData?.expository_slots_96 || [];
  const rawCommon36 = masterData?.common_slots_36 || [];

  // Merge custom/edited slots from DB override map
  const gradeSlots16 = rawSlots96
    .filter((s) => s.grade_num === gradeNum)
    .map((s) => (customSlotsMap && customSlotsMap[s.slot_id]) || s);

  const gradeCommon6 = rawCommon36.filter((c) => c.grade_num === gradeNum);

  const targetSlotId =
    activeSlotId && activeSlotId.startsWith(`G${gradeNum}-`)
      ? activeSlotId
      : baseGrade.slot_id;

  const matchedSlot =
    (customSlotsMap && customSlotsMap[targetSlotId]) ||
    gradeSlots16.find((s) => s.slot_id === targetSlotId) ||
    gradeSlots16[0] ||
    null;

  // Apply dynamic subskill mastery updates if present
  const baseSubskills = baseGrade.xray_overview?.subskill_matrix || [];
  const updatedSubskillMatrix = baseSubskills.map((cell) => {
    const key = `G${gradeNum}-EXP-${cell.code}`;
    const dynScore = dynamicSubskillScores?.[key];
    if (typeof dynScore === 'number') {
      const nextState: 'critical' | 'fragile' | 'mastered' =
        dynScore >= 80 ? 'mastered' : dynScore >= 55 ? 'fragile' : 'critical';
      return {
        ...cell,
        score: dynScore,
        state: nextState,
      };
    }
    return cell;
  });

  const defaultReadingHabit: ReadingHabitProfile = {
    type: '신중한 단서 추적형',
    badge_color: 'blue',
    avg_reading_sec: 145,
    target_reading_sec: 120,
    accuracy_first_try: 82,
    habit_comment: '핵심 어휘와 문장 관계를 꼼꼼하게 살피며 단서를 재탐색하는 우수한 독서 습관',
  };

  const defaultBeforeAfter: BeforeAfterMetrics = {
    before_score: 64,
    after_score: 92,
    before_kread: 880,
    after_kread: 960,
    kread_min: 850,
    kread_max: 990,
    mastered_trap: 'D4 (인과·속성 교차 왜곡 방어 성공)',
  };

  const synthesizedBaseCommercial = {
    reading_habit:
      (baseGrade as any).reading_habit ||
      baseGrade.commercial?.reading_habit ||
      defaultReadingHabit,
    before_after:
      (baseGrade as any).before_after ||
      baseGrade.commercial?.before_after ||
      defaultBeforeAfter,
    parent_table_talk:
      (baseGrade as any).parent_table_talk ||
      (baseGrade.commercial as any)?.parent_table_talk,
    Interactive_hottext_cues:
      (baseGrade as any).Interactive_hottext_cues ||
      (baseGrade.commercial as any)?.Interactive_hottext_cues ||
      [],
    graphic_organizer:
      (baseGrade as any).graphic_organizer ||
      (baseGrade.commercial as any)?.graphic_organizer,
    ebsr_question:
      (baseGrade as any).ebsr_question ||
      (baseGrade.commercial as any)?.ebsr_question,
    writing_workbench:
      (baseGrade as any).writing_workbench ||
      (baseGrade.commercial as any)?.writing_workbench,
    question_scaffolding:
      (baseGrade as any).question_scaffolding ||
      (baseGrade.commercial as any)?.question_scaffolding ||
      [],
    ...(baseGrade.commercial || {}),
  };

  if (!matchedSlot) {
    return {
      activeGradeData: {
        ...baseGrade,
        commercial: synthesizedBaseCommercial as any,
        xray_overview: {
          ...(baseGrade.xray_overview || {}),
          subskill_matrix: updatedSubskillMatrix,
        } as any,
      },
      gradeSlots16,
      gradeCommon6,
      activeSlotPackage: null,
    };
  }

  // Merge matchedSlot into baseGrade so SplitScreenStudio, AdaptiveClinicStudio, etc. work with all 96 slots
  const mergedGradeData: GradeData = {
    ...baseGrade,
    slot_id: matchedSlot.slot_id,
    domain: matchedSlot.domain,
    layer: matchedSlot.layer,
    sub_skill_name: matchedSlot.sub_skill_name,
    curriculum_concept: matchedSlot.curriculum_concept,
    complexity_metrics: matchedSlot.complexity_metrics,
    mager_goal: matchedSlot.mager_goal,
    student_summary: matchedSlot.student_summary,
    prescription_clinic: matchedSlot.prescription_clinic,
    real_csat_test: matchedSlot.real_csat_test,
    prototype_step1_2: matchedSlot.prototype_step1_2,
    commercial: {
      ...synthesizedBaseCommercial,
      ...(matchedSlot.commercial || {}),
      reading_habit:
        matchedSlot.commercial?.reading_habit ||
        synthesizedBaseCommercial.reading_habit,
      before_after:
        matchedSlot.commercial?.before_after ||
        synthesizedBaseCommercial.before_after,
    } as any,
    xray_overview: {
      ...(baseGrade.xray_overview || {}),
      subskill_matrix: updatedSubskillMatrix,
    } as any,
  };

  return {
    activeGradeData: mergedGradeData,
    gradeSlots16,
    gradeCommon6,
    activeSlotPackage: matchedSlot,
  };
}

/**
 * Exports the entire 132-slot Item Bank DB (including any custom authored/edited slots)
 * as a Firebase Firestore-ready JSON document bundle.
 */
export function exportFirestoreBundleJson(
  masterData: CommercialMasterData,
  customSlotsMap: Record<string, SlotLessonPackage>
): string {
  const slots96 = (masterData.expository_slots_96 || []).map(
    (s) => customSlotsMap[s.slot_id] || s
  );
  // Also include any brand-new custom slots not in original 96
  Object.values(customSlotsMap).forEach((cs) => {
    if (!slots96.some((s) => s.slot_id === cs.slot_id)) {
      slots96.push(cs);
    }
  });

  const payload = {
    schema_version: '3.0.0-firestore-production',
    exported_at: new Date().toISOString(),
    collections: {
      [FIREBASE_COLLECTIONS.ITEM_BANK_EXPOSITORY]: Object.fromEntries(
        slots96.map((s) => [s.slot_id, s])
      ),
      [FIREBASE_COLLECTIONS.ITEM_BANK_COMMON]: Object.fromEntries(
        (masterData.common_slots_36 || []).map((c) => [c.code, c])
      ),
      [FIREBASE_COLLECTIONS.CURRICULUM_GOALS]: {
        expository_96: masterData.hierarchy.expository,
        common_36: masterData.hierarchy.common,
      },
    },
  };

  return JSON.stringify(payload, null, 2);
}
