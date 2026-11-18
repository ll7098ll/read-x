import records from "./corpusLessons.generated.json";
import type { ProgressiveLesson } from "./progressiveReading";
export const corpusLessons = records as unknown as ProgressiveLesson[];
export const corpusLessonByPassage = new Map(corpusLessons.map(l=>[l.sourcePassageId!,l]));
export function revisedLessonForSlot(slotId: string) {
  return corpusLessonByPassage.get(`passage:${slotId}:001`);
}
