import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { findLesson, masterData } from '../data/lessonCatalog';
import { normalizeSlotPackage } from '../services/contentSchema';

export const DEMO_STORAGE_KEY = 'readxray_demo_store_v1';

function legacyContentDrafts(): Record<string, SlotLessonPackage> {
  try {
    if (typeof localStorage === 'undefined' || localStorage.getItem(DEMO_STORAGE_KEY)) return {};
    const legacy = JSON.parse(localStorage.getItem('readxray_pro_production_store_v4') || '{}');
    const drafts: Record<string, SlotLessonPackage> = {};
    for (const [id, value] of Object.entries(legacy.state?.customSlotsById || {})) {
      try { const slot = normalizeSlotPackage(value); if (slot.slot_id === id) drafts[id] = slot; } catch { /* The original remains in the legacy key for recovery. */ }
    }
    return drafts;
  } catch { return {}; }
}
import type {
  RoleType,
  StudentModeType,
  TeacherTabType,
  ReaderThemeType,
  FontSizeType,
  HighlightColorType,
  ClueNoteItem,
  VocabNote,
  SlotLessonPackage,
  QuestionAttemptLog,
  StudentAssignment,
} from '../types/courseware';

interface CoursewareState {
  // Navigation & Active Slot State
  activeRole: RoleType;
  activeGradeIdx: number; // 0 (1학년) ~ 5 (6학년), default 4 (5학년)
  activeSlotId: string | null; // e.g., 'G5-EXP-V3-2' (any of the 96 Expository slots)
  activeCommonCode: string | null; // e.g., 'G5-COM-A1' (any of the 36 Common Foundation slots)
  studentMode: StudentModeType;
  teacherTab: TeacherTabType;
  selectedSubskillIdx: number;

  // Reader Ergonomics State
  readerTheme: ReaderThemeType;
  fontSize: FontSizeType;
  showParaNumbers: boolean;
  showSlashChunking: boolean;
  showFocusRuler: boolean;
  cueHighlightMode: boolean;
  activeHighlightColor: HighlightColorType;
  ttsRate: number;
  isStylusMode: boolean;
  isEyeBeaconMode: boolean;
  isTwoColumnMode: boolean;

  // Gamification, Telemetry & Mastery State
  smartScores: Record<number, number>; // grade_num -> 0~100
  dynamicSubskillScores: Record<string, number>; // 'G5-EXP-V3-2' -> 0~100
  completedSlots: Record<string, { clinic: boolean; studio: boolean; examScore?: number }>;
  attemptLogs: QuestionAttemptLog[];
  streakDays: number;
  unlockedVaccines: string[]; // ['D1', 'D2', ...]
  savedVocab: Array<VocabNote & { grade: string }>;
  clueNotesByGrade: Record<number, ClueNoteItem[]>;
  completedStepsByGrade: Record<number, { diag: boolean; clinic: boolean; studio: boolean }>;

  // Interactive Diagnostic Simulator Choices (gradeIdx-qIdx -> optionNo)
  diagSimChoices: Record<string, number>;

  // Teacher Clinic Assignments (student_id -> assigned status)
  teacherClinicAssigned: Record<string, boolean>;

  // Assignments & Task Loop
  assignments: StudentAssignment[];

  // Custom / Edited Item Bank DB Store (slot_id -> SlotLessonPackage)
  customSlotsById: Record<string, SlotLessonPackage>;

  responseDrafts: Record<string, string>;
  saveResponseDraft: (key: string, text: string) => void;

  // Actions
  setActiveRole: (role: RoleType) => void;
  setActiveGradeIdx: (idx: number) => void;
  setActiveSlotId: (slotId: string | null) => void;
  setActiveCommonCode: (code: string | null) => void;
  selectGradeAndSlot: (gradeNum: number, slotId: string, mode?: StudentModeType) => void;
  setStudentMode: (mode: StudentModeType) => void;
  setTeacherTab: (tab: TeacherTabType) => void;
  setSelectedSubskillIdx: (idx: number) => void;

  setReaderTheme: (theme: ReaderThemeType) => void;
  setFontSize: (size: FontSizeType) => void;
  toggleParaNumbers: () => void;
  toggleSlashChunking: () => void;
  toggleFocusRuler: () => void;
  toggleCueHighlightMode: () => void;
  setActiveHighlightColor: (color: HighlightColorType) => void;
  setTtsRate: (rate: number) => void;
  toggleStylusMode: () => void;
  toggleEyeBeaconMode: () => void;
  toggleTwoColumnMode: () => void;

  boostSmartScore: (gradeNum: number, delta: number, slotId?: string) => void;
  updateSubskillScore: (slotId: string, newScore: number) => void;
  markSlotCompleted: (slotId: string, kind: 'clinic' | 'studio', examScore?: number) => void;
  recordAttemptLog: (log: Omit<QuestionAttemptLog, 'id' | 'timestamp'>) => void;
  saveCustomSlotToDb: (slot: SlotLessonPackage) => boolean;
  deleteCustomSlotFromDb: (slotId: string) => void;

  unlockVaccine: (code: string) => void;
  saveVocabWord: (vocab: VocabNote, grade: string) => void;
  removeVocabWord: (word: string) => void;
  addClueNote: (gradeNum: number, text: string, color: HighlightColorType, tag: string) => void;
  removeClueNote: (gradeNum: number, id: string) => void;
  markStepComplete: (gradeNum: number, step: 'diag' | 'clinic' | 'studio') => void;
  setDiagSimChoice: (gradeIdx: number, qIdx: number, optNo: number) => void;
  assignTeacherClinic: (studentIds: string[]) => void;
  assignTaskToStudent: (task: Omit<StudentAssignment, 'id' | 'status'>) => boolean;
  completeStudentAssignment: (taskId: string, score: number) => void;
  resetDemoProgress: () => void;
}

const INITIAL_ASSIGNMENTS: StudentAssignment[] = ['G5-EXP-V1-1', 'G5-COM-A3', 'G5-EXP-V2-2'].map((id, i) => {
  const lesson = findLesson(id)!;
  return {
    id: `DEMO-TASK-${i + 1}`, title: 'real_csat_test' in lesson ? lesson.real_csat_test.passage_title : lesson.title,
    slotId: id, type: id.includes('-COM-') ? 'clinic' : 'reading', assignedBy: '체험 선생님', dueDate: '체험 과제', status: 'pending',
  };
});

const INITIAL_SMART_SCORES: Record<number, number> = {
  1: 64,
  2: 66,
  3: 65,
  4: 63,
  5: 61,
  6: 64,
};

const DEFAULT_SLOT_BY_GRADE: Record<number, string> = {
  1: 'G1-EXP-V1-2',
  2: 'G2-EXP-V1-3',
  3: 'G3-EXP-V1-2',
  4: 'G4-EXP-V2-3',
  5: 'G5-EXP-V3-2',
  6: 'G6-EXP-V2-2',
};

const INITIAL_CLUE_NOTES: Record<number, ClueNoteItem[]> = {
  1: [
    { id: 'init-1', text: '이 동물은 = 코끼리 (지시어 연결)', color: 'yellow', tag: '지시어 단서', createdAt: '방금 전' },
  ],
  2: [
    { id: 'init-2', text: '얼마 뒤 ➔ 뒷다리가 먼저 자라나고 이어서 앞다리가 나옴', color: 'blue', tag: '순서 표지', createdAt: '방금 전' },
  ],
  3: [
    { id: 'init-3', text: '세기는 떨리는 폭, 반면에 높낮이는 떨리는 빠르기', color: 'blue', tag: '비교·대조', createdAt: '방금 전' },
  ],
  4: [
    { id: 'init-4', text: '햇빛↑ + 기온↑ + 습도↓(건조) = 증산 작용 활발(오후 2시)', color: 'yellow', tag: '실험 조건', createdAt: '방금 전' },
  ],
  5: [
    { id: 'init-5', text: '병원성 미생물 1% 미만 / 분해자: 유기물 ➔ 무기물 분해', color: 'yellow', tag: '핵심 명제', createdAt: '방금 전' },
    { id: 'init-5b', text: '4대 평가 준거: 정확성 · 출처 공신력 · 서술 객관성 · 관점 공정성', color: 'blue', tag: '비판 준거', createdAt: '방금 전' },
  ],
  6: [
    { id: 'init-6', text: '해빙 감소(알베도 80%➔10%↓) ➔ 태양열 흡수 증가(90%↑) ➔ 양(+)의 되먹임', color: 'yellow', tag: '연쇄 인과', createdAt: '방금 전' },
  ],
};

export const useCoursewareStore = create<CoursewareState>()(
  persist(
    (set, get) => ({
      activeRole: 'landing',
      activeGradeIdx: 4, // 초5 기본 선택
      activeSlotId: 'G5-EXP-V3-2',
      activeCommonCode: null,
      studentMode: 'portal',
      teacherTab: 'matrix',
      selectedSubskillIdx: 9, // V3-2 index

      readerTheme: 'paper',
      fontSize: 'md',
      showParaNumbers: true,
      showSlashChunking: false,
      showFocusRuler: false,
      cueHighlightMode: false,
      activeHighlightColor: 'yellow',
      ttsRate: 1.0,
      isStylusMode: false,
      isEyeBeaconMode: false,
      isTwoColumnMode: false,

      smartScores: { ...INITIAL_SMART_SCORES },
      dynamicSubskillScores: {},
      completedSlots: {},
      attemptLogs: [],
      streakDays: 14,
      unlockedVaccines: ['D1', 'D4', 'D5'],
      savedVocab: [
        { word: '유기물', tier: 'Tier 3 (교과개념)', desc: '생물체를 이루거나 생물이 만들어 내는 영양 물질', grade: '5학년' },
        { word: '알베도', tier: 'Tier 3 (교과개념)', desc: '지표면이나 물체가 태양빛을 반사하는 비율', grade: '6학년' },
        { word: '기공', tier: 'Tier 3 (교과개념)', desc: '식물 잎 뒷면에서 공기와 수증기가 드나드는 작은 구멍', grade: '4학년' },
      ],
      clueNotesByGrade: { ...INITIAL_CLUE_NOTES },
      completedStepsByGrade: {
        1: { diag: true, clinic: false, studio: false },
        2: { diag: true, clinic: false, studio: false },
        3: { diag: true, clinic: false, studio: false },
        4: { diag: true, clinic: false, studio: false },
        5: { diag: true, clinic: false, studio: false },
        6: { diag: true, clinic: false, studio: false },
      },
      diagSimChoices: {},
      teacherClinicAssigned: {
        'stu-08': true,
        'stu-10': true,
      },
      assignments: [...INITIAL_ASSIGNMENTS],
      customSlotsById: legacyContentDrafts(),
      responseDrafts: {},
      saveResponseDraft: (key, text) => set(state => ({ responseDrafts: { ...state.responseDrafts, [key]: text } })),

      setActiveRole: (role) => set({ activeRole: role }),
      setActiveGradeIdx: (idx) => {
        const gradeNum = idx + 1;
        set({
          activeGradeIdx: idx,
          activeSlotId: DEFAULT_SLOT_BY_GRADE[gradeNum] || `G${gradeNum}-EXP-V1-1`,
          selectedSubskillIdx: 0,
        });
      },
      setActiveSlotId: (slotId) => set({ activeSlotId: slotId }),
      setActiveCommonCode: (code) => set({ activeCommonCode: code }),
      selectGradeAndSlot: (gradeNum, slotId, mode) =>
        set((state) => ({
          activeGradeIdx: Math.max(0, Math.min(5, gradeNum - 1)),
          activeSlotId: slotId,
          studentMode: mode ?? state.studentMode,
          activeRole: mode ? 'student' : state.activeRole,
        })),
      setStudentMode: (mode) => set({ studentMode: mode }),
      setTeacherTab: (tab) => set({ teacherTab: tab }),
      setSelectedSubskillIdx: (idx) => set({ selectedSubskillIdx: idx }),

      setReaderTheme: (theme) => set({ readerTheme: theme }),
      setFontSize: (size) => set({ fontSize: size }),
      toggleParaNumbers: () => set((s) => ({ showParaNumbers: !s.showParaNumbers })),
      toggleSlashChunking: () => set((s) => ({ showSlashChunking: !s.showSlashChunking })),
      toggleFocusRuler: () => set((s) => ({ showFocusRuler: !s.showFocusRuler })),
      toggleCueHighlightMode: () => set((s) => ({ cueHighlightMode: !s.cueHighlightMode })),
      setActiveHighlightColor: (color) => set({ activeHighlightColor: color }),
      setTtsRate: (rate) => set({ ttsRate: rate }),
      toggleStylusMode: () => set((s) => ({ isStylusMode: !s.isStylusMode })),
      toggleEyeBeaconMode: () => set((s) => ({ isEyeBeaconMode: !s.isEyeBeaconMode })),
      toggleTwoColumnMode: () => set((s) => ({ isTwoColumnMode: !s.isTwoColumnMode })),

      // Legacy reward calls must not manufacture a diagnostic score.
      // The displayed historical scores belong only to the explicitly labelled demo.
      boostSmartScore: () => {},
      updateSubskillScore: () => {},

      markSlotCompleted: (slotId, kind, examScore) =>
        set((state) => {
          const prev = state.completedSlots[slotId] || { clinic: false, studio: false };
          return {
            completedSlots: {
              ...state.completedSlots,
              [slotId]: {
                ...prev,
                [kind]: true,
                ...(typeof examScore === 'number' ? { examScore } : {}),
              },
            },
          };
        }),

      recordAttemptLog: (log) =>
        set((state) => {
          const newEntry: QuestionAttemptLog = {
            ...log,
            id: `att-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
            timestamp: new Date().toISOString(),
          };
          return {
            attemptLogs: [newEntry, ...state.attemptLogs].slice(0, 100),
          };
        }),

      saveCustomSlotToDb: (slot) => {
        try {
          const normalized = normalizeSlotPackage(slot);
          if (!masterData.expository_slots_96.some(s => s.slot_id === normalized.slot_id && s.grade_num === normalized.grade_num)) return false;
          set(state => ({ customSlotsById: { ...state.customSlotsById, [normalized.slot_id]: { ...normalized, updated_at: new Date().toISOString() } } }));
          return true;
        } catch { return false; }
      },

      deleteCustomSlotFromDb: (slotId) =>
        set((state) => {
          const next = { ...state.customSlotsById };
          delete next[slotId];
          return { customSlotsById: next };
        }),

      unlockVaccine: (code) =>
        set((state) => {
          if (state.unlockedVaccines.includes(code)) return state;
          return { unlockedVaccines: [...state.unlockedVaccines, code] };
        }),

      saveVocabWord: (vocab, grade) =>
        set((state) => {
          if (state.savedVocab.some((v) => v.word === vocab.word)) return state;
          return { savedVocab: [{ ...vocab, grade }, ...state.savedVocab] };
        }),

      removeVocabWord: (word) =>
        set((state) => ({
          savedVocab: state.savedVocab.filter((v) => v.word !== word),
        })),

      addClueNote: (gradeNum, text, color, tag) =>
        set((state) => {
          const list = state.clueNotesByGrade[gradeNum] || [];
          if (list.some((item) => item.text === text)) return state;
          const newItem: ClueNoteItem = {
            id: `clue-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
            text,
            color,
            tag,
            createdAt: '방금 추가됨',
          };
          return {
            clueNotesByGrade: {
              ...state.clueNotesByGrade,
              [gradeNum]: [newItem, ...list],
            },
          };
        }),

      removeClueNote: (gradeNum, id) =>
        set((state) => ({
          clueNotesByGrade: {
            ...state.clueNotesByGrade,
            [gradeNum]: (state.clueNotesByGrade[gradeNum] || []).filter((c) => c.id !== id),
          },
        })),

      markStepComplete: (gradeNum, step) =>
        set((state) => ({
          completedStepsByGrade: {
            ...state.completedStepsByGrade,
            [gradeNum]: {
              ...(state.completedStepsByGrade[gradeNum] || { diag: true, clinic: false, studio: false }),
              [step]: true,
            },
          },
        })),

      setDiagSimChoice: (gradeIdx, qIdx, optNo) =>
        set((state) => ({
          diagSimChoices: {
            ...state.diagSimChoices,
            [`${gradeIdx}-${qIdx}`]: optNo,
          },
        })),

      assignTeacherClinic: (studentIds) =>
        set((state) => {
          const next = { ...state.teacherClinicAssigned };
          studentIds.forEach((id) => {
            next[id] = true;
          });
          return { teacherClinicAssigned: next };
        }),

      assignTaskToStudent: (task) => {
        const lesson = get().customSlotsById[task.slotId] || findLesson(task.slotId);
        if (!lesson || lesson.status !== 'published') return false;
        if ('real_csat_test' in lesson) {
          try { if (normalizeSlotPackage(lesson).slot_id !== task.slotId) return false; } catch { return false; }
        }
        if (task.slotId.includes('-COM-') && task.type !== 'clinic') return false;
        const title = 'real_csat_test' in lesson ? lesson.real_csat_test.passage_title : lesson.title;
        set(state => ({ assignments: [{ ...task, title, id: `DEMO-TASK-${crypto.randomUUID()}`, status: 'pending' }, ...state.assignments] }));
        return true;
      },

      completeStudentAssignment: () => {},

      resetDemoProgress: () =>
        set({
          assignments: [...INITIAL_ASSIGNMENTS],
          smartScores: { ...INITIAL_SMART_SCORES },
          dynamicSubskillScores: {},
          completedSlots: {},
          attemptLogs: [],
          unlockedVaccines: ['D1', 'D4', 'D5'],
          clueNotesByGrade: { ...INITIAL_CLUE_NOTES },
          diagSimChoices: {},
          completedStepsByGrade: {
            1: { diag: true, clinic: false, studio: false },
            2: { diag: true, clinic: false, studio: false },
            3: { diag: true, clinic: false, studio: false },
            4: { diag: true, clinic: false, studio: false },
            5: { diag: true, clinic: false, studio: false },
            6: { diag: true, clinic: false, studio: false },
          },
        }),
    }),
    {
      name: DEMO_STORAGE_KEY,
      onRehydrateStorage: () => (state) => {
        if (state) {
          const validRoles: RoleType[] = ['landing', 'student', 'parent', 'teacher', 'director', 'admin'];
          if (!validRoles.includes(state.activeRole)) {
            state.activeRole = 'landing';
          }
          if (typeof state.activeGradeIdx !== 'number' || state.activeGradeIdx < 0 || state.activeGradeIdx > 5) {
            state.activeGradeIdx = 4;
          }
          if (!state.assignments || !Array.isArray(state.assignments)) {
            state.assignments = [...INITIAL_ASSIGNMENTS];
          }
        }
      },
    }
  )
);
