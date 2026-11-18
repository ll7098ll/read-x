import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import { practiceStorage } from "./useReadingWorkspace";
import { validRubric, type Rubric } from "../services/reportMetrics";
import {
  defaultDemoStudentId,
  demoClasses,
  demoStudents,
  type DemoReview,
} from "../data/demoAcademy";
type DemoAcademyState = {
  teacherView: string;
  setTeacherView: (view: string) => void;
  selectedStudentId: string;
  selectedClassId: string;
  reviews: Record<string, DemoReview>;
  releases: Record<string, boolean>;
  consultationNotes: Record<string, string>;
  selectStudent: (id: string) => void;
  selectClass: (id: string) => void;
  saveReview: (
    id: string,
    note: string,
    next: string,
    rubric?: Rubric,
  ) => boolean;
  releaseReport: (id: string) => boolean;
  saveConsultation: (id: string, note: string) => void;
};
/** Synthetic operation scenarios never write into learner attempts or real courseware scores. */
export const useDemoAcademy = create<DemoAcademyState>()(
  persist(
    (set, get) => ({
      teacherView: "today",
      setTeacherView: (teacherView) => set({ teacherView }),
      selectedStudentId: defaultDemoStudentId,
      selectedClassId: "explore",
      reviews: {},
      releases: {},
      consultationNotes: {},
      selectStudent: (id) => {
        const s = demoStudents.find((s) => s.id === id);
        if (s) set({ selectedStudentId: id, selectedClassId: s.classId });
      },
      selectClass: (id) => {
        if (demoClasses.some((c) => c.id === id)) set({ selectedClassId: id });
      },
      saveReview: (id, note, next, rubric) => {
        const s = demoStudents.find((s) => s.id === id);
        if (
          !s ||
          s.status !== "submitted" ||
          !note.trim() ||
          !next.trim() ||
          (rubric !== undefined && !validRubric(rubric))
        )
          return false;
        set((state) => ({
          reviews: {
            ...state.reviews,
            [id]: {
              note: note.trim(),
              next: next.trim(),
              savedAt: new Date().toISOString(),
              ...(rubric ? { rubric } : {}),
            },
          },
        }));
        return true;
      },
      releaseReport: (id) => {
        const s = demoStudents.find((s) => s.id === id);
        if (
          !s ||
          s.status !== "submitted" ||
          (!s.reviewed && !get().reviews[id])
        )
          return false;
        set((state) => ({ releases: { ...state.releases, [id]: true } }));
        return true;
      },
      saveConsultation: (id, note) =>
        set((s) => ({
          consultationNotes: { ...s.consultationNotes, [id]: note },
        })),
    }),
    {
      name: "readx_academy_mock_v1",
      storage: createJSONStorage(() => practiceStorage),
      version: 1,
      merge: (persisted, current) => {
        const p = persisted as Partial<DemoAcademyState> | undefined;
        return {
          ...current,
          ...p,
          teacherView: [
            "today",
            "review",
            "class",
            "library",
            "curriculum",
            "reports",
          ].includes(p?.teacherView || "")
            ? p!.teacherView!
            : "today",
          selectedStudentId: demoStudents.some(
            (s) => s.id === p?.selectedStudentId,
          )
            ? p!.selectedStudentId!
            : current.selectedStudentId,
          selectedClassId: demoClasses.some((c) => c.id === p?.selectedClassId)
            ? p!.selectedClassId!
            : current.selectedClassId,
          reviews: p?.reviews && typeof p.reviews === "object" ? p.reviews : {},
          releases:
            p?.releases && typeof p.releases === "object" ? p.releases : {},
          consultationNotes:
            p?.consultationNotes && typeof p.consultationNotes === "object"
              ? p.consultationNotes
              : {},
        };
      },
    },
  ),
);
