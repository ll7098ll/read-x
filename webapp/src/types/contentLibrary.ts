/** Literacy goals describe what the learner does; curriculum concepts supply the topic. */
export type ThinkingStage = 'notice' | 'connect' | 'judge' | 'express';
export type SupportLevel = 'modelled' | 'guided' | 'prompted' | 'independent';
export type ReviewState = 'needs_review' | 'approved';

export interface CurriculumSource {
  id: string; title: string; url: string; edition: string;
  verification: 'notice_verified' | 'full_text_verified';
}
export interface ConceptRecord {
  id: string; curriculum: '2022-revised'; gradeBand: '1-2' | '3-4' | '5-6';
  subjectClaim: string; unitClaim: string; name: string;
  standardRefs: Array<{ sourceId: string; code: string; locator: string }>;
  reviewState: ReviewState;
}
export interface LiteracyGoalRecord {
  id: string; grade: number; name: string; performanceGoal: string; prerequisiteGoalIds: string[];
  // Existing guidance is an authoring input, not a fully scripted think-aloud model.
  thinkingGuides: Array<{ stage: ThinkingStage; instruction: string }>;
  rubricState: ReviewState;
}
export interface PassageRecord {
  id: string; version: number; title: string; grade: number; paragraphs: string[];
  conceptIds: string[]; goalIds: string[]; structure: string;
  sourceLessonId: string; reviewState: ReviewState;
  provenance: { source: string; copyrightReview: ReviewState; factualReview: ReviewState };
}
export interface ContentLibrary {
  schemaVersion: '1.0'; sources: CurriculumSource[]; concepts: ConceptRecord[];
  goals: LiteracyGoalRecord[]; passages: PassageRecord[];
}

/** Raw observations. A correct answer alone is never evidence of every thinking stage. */
export interface ProcessObservation {
  eventId: string; learnerId: string; goalId: string; passageId: string; passageVersion: number;
  activityId: string; stage: ThinkingStage; support: SupportLevel;
  purpose: 'practice' | 'independent_check' | 'transfer_check';
  passageExposure: 'new' | 'practiced' | 'unknown';
  outcome: 'success' | 'needs_support' | 'pending_review';
  response: string; evidenceRefs: string[]; observedAt: string;
}
