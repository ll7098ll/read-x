import {
  getJourneyPassages,
  passageFamily,
  journeyStages,
  journeyTasks,
  JOURNEY_SLOT,
  JOURNEY_VERSION,
  isTaskStage,
  type JourneyStage,
  type TaskId,
} from "../data/learningJourney";
import type { ProcessObservation, SupportLevel } from "../types/contentLibrary";
import type { ReadingLevel } from "../data/readingPolicy";
import { validAnnotation, rememberAnnotations, updateAnnotationList, type ReadingAnnotation } from "./annotations";
export { annotationKinds } from "./annotations";

export type JourneyAnnotation = ReadingAnnotation;

export type JourneySubmission = {
  id: string;
  at: string;
  evidence: string[];
  answer: string;
  reason: string;
  helpLevel: number;
  passageId: string;
  passageVersion: number;
  evidenceQuotes: Record<string, string>;
  support: SupportLevel;
  exposure: "new" | "practiced";
  evidenceMatch: boolean;
  annotations?: JourneyAnnotation[];
  readingLevel?: ReadingLevel;
  review?: { outcome: "success" | "needs_support"; note: string; at: string };
};
export type JourneyResponse = {
  evidence: string[];
  answer: string;
  reason: string;
  helpLevel: number;
  submissions: JourneySubmission[];
};
export type JourneyAttempt = {
  id: string;
  version: number;
  createdAt: string;
  stage: JourneyStage;
  reached: number;
  modelStep: number;
  exposures: Record<string, "new" | "practiced">;
  responses: Partial<Record<TaskId, JourneyResponse>>;
  writing: string;
  revisions: { text: string; at: string; evidence: string[] }[];
  reflection: string;
  readingLevel?: ReadingLevel;
  annotations?: JourneyAnnotation[];
  annotationHistory?: JourneyAnnotation[][];
};
export const emptyResponse = (): JourneyResponse => ({
  evidence: [],
  answer: "",
  reason: "",
  helpLevel: 0,
  submissions: [],
});
export function saveJourneyAnnotation(attempt: JourneyAttempt, annotation: JourneyAnnotation): JourneyAttempt {
  const passage = Object.values(getJourneyPassages(attempt)).find(p => p.id === annotation.passageId);
  if (!passage || !validAnnotation(passage, annotation)) return attempt;
  return rememberAnnotations(attempt, updateAnnotationList(attempt.annotations || [], annotation));
}
export function createJourneyAttempt(id: string, at: string, readingLevel: ReadingLevel = "standard"): JourneyAttempt {
  return {
    id,
    version: JOURNEY_VERSION,
    createdAt: at,
    stage: "start",
    reached: 0,
    modelStep: 0,
    exposures: {},
    responses: {},
    writing: "",
    revisions: [],
    reflection: "",
    readingLevel,
    annotations: [],
  };
}
export function enterJourneyStage(
  attempt: JourneyAttempt,
  stage: JourneyStage,
  seen: string[],
): { attempt: JourneyAttempt; seen: string[] } {
  const journeyPassages = getJourneyPassages(attempt);
  const task = isTaskStage(stage) ? journeyTasks[stage] : null;
  const passage = task
    ? journeyPassages[task.passage]
    : stage === "model"
      ? journeyPassages.solution
      : null;
  const key = passage ? `${passage.id}@${passage.version}` : "";
  return {
    attempt: {
      ...attempt,
      stage,
      reached: Math.max(
        attempt.reached,
        journeyStages.findIndex((s) => s.id === stage),
      ),
      exposures:
        key && !attempt.exposures[key]
          ? {
              ...attempt.exposures,
              [key]: seen.some(k => passageFamily(k.split("@")[0]) === passageFamily(passage!.id)) ? "practiced" : "new",
            }
          : attempt.exposures,
    },
    seen: key && !seen.includes(key) ? [...seen, key] : seen,
  };
}
export function editJourneyResponse(
  attempt: JourneyAttempt,
  task: TaskId,
  update: Partial<
    Pick<JourneyResponse, "evidence" | "answer" | "reason" | "helpLevel">
  >,
): JourneyAttempt {
  const current = attempt.responses[task] || emptyResponse();
  const journeyPassages = getJourneyPassages(attempt);
  const validIds = journeyPassages[
    journeyTasks[task].passage
  ].paragraphs.flatMap((p) => p.sentences.map((s) => s.id));
  return {
    ...attempt,
    responses: {
      ...attempt.responses,
      [task]: {
        ...current,
        ...update,
        evidence: update.evidence
          ? [...new Set(update.evidence)].filter((id) => validIds.includes(id))
          : current.evidence,
        helpLevel: Math.max(
          current.helpLevel,
          Math.min(3, update.helpLevel ?? current.helpLevel),
        ),
      },
    },
  };
}
export function submitJourneyResponse(
  attempt: JourneyAttempt,
  task: TaskId,
  id: string,
  at: string,
): JourneyAttempt {
  const r = attempt.responses[task];
  if (!r || !r.answer.trim() || !r.reason.trim() || !r.evidence.length)
    return attempt;
  if (r.submissions.some((s) => s.id === id)) return attempt;
  const last = r.submissions.slice(-1)[0];
  if (
    last &&
    last.answer === r.answer &&
    last.reason === r.reason &&
    JSON.stringify(last.evidence) === JSON.stringify(r.evidence) &&
    last.helpLevel === r.helpLevel &&
    JSON.stringify(last.annotations || []) === JSON.stringify((attempt.annotations || []).filter(a => a.passageId === getJourneyPassages(attempt)[journeyTasks[task].passage].id))
  )
    return attempt;
  const passage = getJourneyPassages(attempt)[journeyTasks[task].passage];
  // Feedback already seen and repeat passages cannot become fresh independent evidence.
  const exposure =
    !r.submissions.length &&
    attempt.exposures[`${passage.id}@${passage.version}`] === "new"
      ? "new"
      : "practiced";
  const support: SupportLevel = r.helpLevel
    ? "guided"
    : task === "guided"
      ? "guided"
      : task === "faded"
        ? "prompted"
        : "independent";
  const submission: JourneySubmission = {
    id,
    at,
    evidence: [...r.evidence],
    answer: r.answer,
    reason: r.reason,
    helpLevel: r.helpLevel,
    support,
    exposure,
    passageId: passage.id,
    passageVersion: passage.version,
    readingLevel: attempt.readingLevel,
    annotations: (attempt.annotations || []).filter(a => a.passageId === passage.id).map(a => ({ ...a })),
    evidenceQuotes: Object.fromEntries(
      passage.paragraphs
        .flatMap((p) => p.sentences)
        .filter((s) => r.evidence.includes(s.id))
        .map((s) => [s.id, s.text]),
    ),
    evidenceMatch:
      journeyTasks[task].acceptableEvidence.every((x) =>
        r.evidence.includes(x),
      ) &&
      r.evidence.every((x) =>
        [...journeyTasks[task].acceptableEvidence, ...journeyTasks[task].supportingEvidence].includes(x),
      ),
  };
  return {
    ...attempt,
    responses: {
      ...attempt.responses,
      [task]: { ...r, submissions: [...r.submissions, submission] },
    },
  };
}
export function responseChanged(r: JourneyResponse, annotations?: JourneyAnnotation[]) {
  const last = r.submissions.slice(-1)[0];
  return (
    !last ||
    last.answer !== r.answer ||
    last.reason !== r.reason ||
    JSON.stringify(last.evidence) !== JSON.stringify(r.evidence) ||
    last.helpLevel !== r.helpLevel ||
    (annotations !== undefined && JSON.stringify(last.annotations || []) !== JSON.stringify(annotations))
  );
}
export function journeyObservations(
  attempt: JourneyAttempt,
): ProcessObservation[] {
  return (
    Object.entries(attempt.responses) as [TaskId, JourneyResponse][]
  ).flatMap(([task, response]) =>
    response.submissions.map((s) => {
      const passage = getJourneyPassages(attempt)[journeyTasks[task].passage];
      return {
        eventId: s.id,
        learnerId: "local-demo-learner",
        goalId: JOURNEY_SLOT,
        passageId: s.passageId || passage.id,
        passageVersion: s.passageVersion || passage.version,
        activityId: `${attempt.id}:${task}`,
        stage: "express" as const,
        support: s.support,
        purpose:
          task === "independent"
            ? ("independent_check" as const)
            : task === "transfer"
              ? ("transfer_check" as const)
              : ("practice" as const),
        passageExposure: s.exposure,
        outcome: s.review?.outcome || ("pending_review" as const),
        response: `${s.answer}\n선택 이유: ${s.reason}`,
        evidenceRefs: s.evidence,
        observedAt: s.at,
      };
    }),
  );
}
