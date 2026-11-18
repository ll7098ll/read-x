import type { ProcessObservation, ThinkingStage } from '../types/contentLibrary';

/** Describes observed performance, without inventing calibrated mastery thresholds. */
export function summarizeProcessEvidence(observations: ProcessObservation[], learnerId: string, goalId: string) {
  const unique = new Map<string, ProcessObservation>();
  for (const observation of observations) {
    if (observation.learnerId !== learnerId || observation.goalId !== goalId) continue;
    // Preserve the first received event; duplicate delivery cannot increase counts.
    if (!unique.has(observation.eventId)) unique.set(observation.eventId, observation);
  }
  const stages: ThinkingStage[] = ['notice','connect','judge','express'];
  return stages.map(stage => {
    const rows = [...unique.values()].filter(o => o.stage === stage);
    const guided = rows.filter(o => o.support !== 'independent' && o.outcome === 'success');
    const independent = rows.filter(o => o.support === 'independent' && o.purpose !== 'practice' && o.outcome === 'success');
    const transfer = independent.filter(o => o.purpose === 'transfer_check' && o.passageExposure === 'new');
    return { stage, observations: rows.length, guidedSuccess: guided.length, independentSuccess: independent.length,
      transferPassageIds: [...new Set(transfer.map(o => o.passageId))],
      needsSupport: rows.filter(o => o.outcome === 'needs_support').length,
      pendingReview: rows.filter(o => o.outcome === 'pending_review').length,
      state: rows.length ? 'observed' as const : 'no_evidence' as const };
  });
}
