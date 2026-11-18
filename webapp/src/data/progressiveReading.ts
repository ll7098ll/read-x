import { readingLevels, thinkingLadder, type ReadingLevel } from "./readingPolicy";
export { thinkingLadder } from "./readingPolicy";
import type { JourneyPassage } from "./learningJourney";
import { progressiveTexts } from "./progressiveTexts";
import { progressiveQuestions } from "./progressiveQuestions";
export type ReadingParagraph = { id: string; text: string };
export type ProgressiveQuestion = {
  id: string; skill: typeof thinkingLadder[number]; prompt: string; scenario?: string;
  responseKind?: "explanation";
  options: string[]; answer: number; evidence: string[]; hints: [string, string, string];
  explanation: string; optionReasons: string[];
};
export type ProgressiveLesson = {
  id: string; grade: number; title: string; concept: string;
  version?: number; sourcePassageId?: string; goalIds?: string[];
  layers: Record<ReadingLevel, ReadingParagraph[]>;
  vocabulary: { word: string; meaning: string }[];
  model: { paragraph: string; quote: string; kind: "target" | "evidence" | "link"; thought: string }[];
  questions: ProgressiveQuestion[];
  levelQuestions?: Partial<Record<ReadingLevel, ProgressiveQuestion[]>>;
};
export function progressiveLessonAtLevel(lesson: ProgressiveLesson, level: ReadingLevel): ProgressiveLesson {
  const questions = lesson.levelQuestions?.[level];
  return questions ? {...lesson, questions} : lesson;
}
export function progressivePassage(lesson: ProgressiveLesson, level: ReadingLevel): JourneyPassage {
  return { id: `${lesson.id}-${level}`, version: lesson.version || 1, title: lesson.title, subject: lesson.concept,
    paragraphs: readingLevels.slice(0, readingLevels.indexOf(level) + 1).flatMap(l => lesson.layers[l]).map(p => ({id:p.id, sentences:[{id:p.id,text:p.text}]})) };
}
export const progressiveLessons: ProgressiveLesson[] = progressiveTexts.map(text => ({...text,questions:progressiveQuestions[text.grade]}));
