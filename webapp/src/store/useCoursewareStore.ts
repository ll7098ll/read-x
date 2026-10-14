import { create } from 'zustand';
import { persist } from 'zustand/middleware';
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
  saveCustomSlotToDb: (slot: SlotLessonPackage) => void;
  deleteCustomSlotFromDb: (slotId: string) => void;

  unlockVaccine: (code: string) => void;
  saveVocabWord: (vocab: VocabNote, grade: string) => void;
  removeVocabWord: (word: string) => void;
  addClueNote: (gradeNum: number, text: string, color: HighlightColorType, tag: string) => void;
  removeClueNote: (gradeNum: number, id: string) => void;
  markStepComplete: (gradeNum: number, step: 'diag' | 'clinic' | 'studio') => void;
  setDiagSimChoice: (gradeIdx: number, qIdx: number, optNo: number) => void;
  assignTeacherClinic: (studentIds: string[]) => void;
  assignTaskToStudent: (task: Omit<StudentAssignment, 'id' | 'status'>) => void;
  completeStudentAssignment: (taskId: string, score: number) => void;
  resetDemoProgress: () => void;
}

const INITIAL_ASSIGNMENTS: StudentAssignment[] = [
  {
    id: 'TASK-001',
    title: 'G5-EXP-I1-1 [과학] 인공지능 신경망의 가중치 갱신 인과 추론 및 EBSR 2단계 풀이',
    slotId: 'G5-EXP-I1-1',
    type: 'reading',
    assignedBy: '김성진 담임선생님 (대치초 5학년 2반)',
    dueDate: '오늘 18:00까지',
    status: 'pending',
    trapWarning: 'D4 다단계 논리적 비약 주의 (본문 전제 확인 필수)',
  },
  {
    id: 'TASK-002',
    title: 'G5-COM-A3 [선수결손] 교과 전문어 의미망 & 사고구술 빈칸 조립 징검다리 클리닉',
    slotId: 'G5-COM-A3',
    type: 'clinic',
    assignedBy: '김성진 담임선생님 (대치초 5학년 2반)',
    dueDate: '2026.10.12',
    status: 'completed',
    score: 95,
    completedAt: '어제 16:42 제출 완료 (우수)',
    trapWarning: 'D3 전제 왜곡 방어 성공',
  },
  {
    id: 'TASK-003',
    title: 'G5-EXP-S1-2 [사회/구조] 환율 변동과 무역 수지 Meyer 6대 텍스트 구조도 노드 조립',
    slotId: 'G5-EXP-S1-2',
    type: 'reading',
    assignedBy: 'AI 적응형 엔진 추천',
    dueDate: '내일 15:00까지',
    status: 'pending',
    trapWarning: '문제-해결 구조 인과 노드 매핑',
  },
  {
    id: 'TASK-004',
    title: '10초 스피드 어휘 듀얼 배틀 (초등 5학년 2학기 전교과 핵심 어휘 10선)',
    slotId: 'G5-EXP-V1-1',
    type: 'vocab',
    assignedBy: 'AI 라이벌 챌린지',
    dueDate: '오늘 21:00까지',
    status: 'pending',
  },
  {
    id: 'TASK-005',
    title: 'CAT 3문항 적응형 온보딩 독서 레벨 진단 평가',
    slotId: 'G5-EXP-I1-1',
    type: 'cat',
    assignedBy: 'ReadX AI 평가원',
    dueDate: '완료됨',
    status: 'completed',
    score: 92,
    completedAt: '2026.10.10 완료 (KReaD 940 판정)',
  },
];

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
    (set) => ({
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
      customSlotsById: {},

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

      boostSmartScore: (gradeNum, delta, slotId) =>
        set((state) => {
          const current = state.smartScores[gradeNum] ?? 60;
          const next = Math.min(100, Math.max(30, current + delta));
          const targetSlot = slotId || state.activeSlotId || `G${gradeNum}-EXP-V1-1`;
          const curSlotScore = state.dynamicSubskillScores[targetSlot] ?? 65;
          const nextSlotScore = Math.min(100, Math.max(30, curSlotScore + delta * 2));
          return {
            smartScores: {
              ...state.smartScores,
              [gradeNum]: next,
            },
            dynamicSubskillScores: {
              ...state.dynamicSubskillScores,
              [targetSlot]: nextSlotScore,
            },
          };
        }),

      updateSubskillScore: (slotId, newScore) =>
        set((state) => ({
          dynamicSubskillScores: {
            ...state.dynamicSubskillScores,
            [slotId]: Math.min(100, Math.max(0, newScore)),
          },
        })),

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
            timestamp: new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
          };
          return {
            attemptLogs: [newEntry, ...state.attemptLogs].slice(0, 100),
          };
        }),

      saveCustomSlotToDb: (slot) =>
        set((state) => ({
          customSlotsById: {
            ...state.customSlotsById,
            [slot.slot_id]: {
              ...slot,
              updated_at: new Date().toISOString(),
            },
          },
        })),

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

      assignTaskToStudent: (task) =>
        set((state) => ({
          assignments: [
            {
              ...task,
              id: `TASK-${Date.now()}`,
              status: 'pending',
            },
            ...state.assignments,
          ],
        })),

      completeStudentAssignment: (taskId, score) =>
        set((state) => ({
          assignments: state.assignments.map((a) =>
            a.id === taskId
              ? {
                  ...a,
                  status: 'completed',
                  score,
                  completedAt: '방금 전 제출 완료',
                }
              : a
          ),
        })),

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
      name: 'readxray_pro_production_store_v4',
      onRehydrateStorage: () => (state) => {
        if (state) {
          const validRoles: RoleType[] = ['landing', 'student', 'parent', 'teacher', 'admin'];
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
