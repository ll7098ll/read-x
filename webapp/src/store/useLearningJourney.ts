import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import { practiceStorage } from "./useReadingWorkspace";
import {
  createJourneyAttempt,
  enterJourneyStage,
  editJourneyResponse,
  submitJourneyResponse,
  type JourneyAttempt,
  type JourneyResponse,
  type JourneySubmission,
  type JourneyAnnotation,
  saveJourneyAnnotation,
} from "../services/learningJourney";
import type { JourneyStage, TaskId } from "../data/learningJourney";
import type { ReadingLevel } from "../data/readingPolicy";
import { rememberAnnotations, undoAnnotations } from "../services/annotations";

type JourneyStore = {
  attempts: JourneyAttempt[];
  activeId: string | null;
  seenPassages: string[];
  start: (level?: ReadingLevel) => void;
  annotate: (annotation: JourneyAnnotation) => void;
  removeAnnotation: (id: string) => void;
  undoAnnotation: () => void;
  navigate: (stage: JourneyStage) => void;
  model: (step: number) => void;
  edit: (
    task: TaskId,
    update: Partial<
      Pick<JourneyResponse, "evidence" | "answer" | "reason" | "helpLevel">
    >,
  ) => void;
  submit: (task: TaskId) => void;
  write: (text: string) => void;
  saveRevision: () => void;
  reflect: (text: string) => void;
  review: (
    attemptId: string,
    task: TaskId,
    submissionId: string,
    review: NonNullable<JourneySubmission["review"]>,
  ) => void;
};
export const useLearningJourney = create<JourneyStore>()(
  persist(
    (set) => {
      const change = (fn: (a: JourneyAttempt) => JourneyAttempt) =>
        set((s) => ({
          attempts: s.attempts.map((a) => (a.id === s.activeId ? fn(a) : a)),
        }));
      return {
        attempts: [],
        activeId: null,
        seenPassages: [],
        start: (level = "standard") =>
          set((s) => {
            const a = createJourneyAttempt(
              crypto.randomUUID(),
              new Date().toISOString(),
              level,
            );
            return { attempts: [...s.attempts, a], activeId: a.id };
          }),
        annotate: (annotation) => change(a => saveJourneyAnnotation(a, annotation)),
        removeAnnotation: (id) => change(a => rememberAnnotations(a, (a.annotations || []).filter(n => n.id !== id))),
        undoAnnotation: () => change(undoAnnotations),
        navigate: (stage) =>
          set((s) => {
            const current = s.attempts.find((a) => a.id === s.activeId);
            if (!current) return s;
            const next = enterJourneyStage(current, stage, s.seenPassages);
            return {
              attempts: s.attempts.map((a) =>
                a.id === current.id ? next.attempt : a,
              ),
              seenPassages: next.seen,
            };
          }),
        model: (step) =>
          change((a) => ({ ...a, modelStep: Math.max(0, Math.min(2, step)) })),
        edit: (task, update) =>
          change((a) => editJourneyResponse(a, task, update)),
        submit: (task) =>
          change((a) =>
            submitJourneyResponse(
              a,
              task,
              crypto.randomUUID(),
              new Date().toISOString(),
            ),
          ),
        write: (writing) => change((a) => ({ ...a, writing })),
        saveRevision: () =>
          change((a) => {
            if (!a.writing.trim()) return a;
            const evidence = [
              ...new Set(
                ["guided", "faded"].flatMap(
                  (t) => a.responses[t as TaskId]?.evidence || [],
                ),
              ),
            ];
            const last = a.revisions.slice(-1)[0];
            if (
              last?.text === a.writing &&
              JSON.stringify(last.evidence) === JSON.stringify(evidence)
            )
              return a;
            return {
              ...a,
              revisions: [
                ...a.revisions,
                { text: a.writing, evidence, at: new Date().toISOString() },
              ],
            };
          }),
        reflect: (reflection) => change((a) => ({ ...a, reflection })),
        review: (attemptId, task, submissionId, review) =>
          set((s) => ({
            attempts: s.attempts.map((a) => {
              const r = a.responses[task];
              if (a.id !== attemptId || !r) return a;
              return {
                ...a,
                responses: {
                  ...a.responses,
                  [task]: {
                    ...r,
                    submissions: r.submissions.map((x) =>
                      x.id === submissionId ? { ...x, review } : x,
                    ),
                  },
                },
              };
            }),
          })),
      };
    },
    {
      name: "readx_learning_journey_demo_v1",
      storage: createJSONStorage(() => practiceStorage),
      version: 1,
    },
  ),
);
