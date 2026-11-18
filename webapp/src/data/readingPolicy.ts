/** Editorial starting points for Korean expository passages, not calibrated grade norms.
 * Counts include spaces, exclude markup/tables/title, and join paragraphs with one space.
 */
export const readingLevels = ["supported", "standard", "challenge"] as const;
export const thinkingLadder = ["직접 확인", "정보 연결", "추론", "근거 판단", "새 상황 적용"] as const;
export type ReadingLevel = typeof readingLevels[number];
export const readingLevelLabels: Record<ReadingLevel, string> = {
  supported: "도움글", standard: "기준글", challenge: "도전글",
};
export const readingPolicy = [
  { grade: 1, ranges: [[150, 250], [250, 400], [400, 550]], sentenceWords: [3, 7], vocabulary: "생활에서 쓰는 구체어 중심. 낯선 말은 문장 바로 옆에서 풀어 줍니다.", concepts: "새 핵심어 1~2개", structure: "대상 하나, 특징을 직접 설명하는 2~4문단" },
  { grade: 2, ranges: [[250, 400], [400, 600], [600, 800]], sentenceWords: [4, 9], vocabulary: "생활어에 기초 교과어를 더하고, 같은 뜻의 쉬운 말을 함께 씁니다.", concepts: "새 핵심어 2~3개", structure: "시간 순서·단순 비교가 있는 3~5문단" },
  { grade: 3, ranges: [[400, 600], [600, 850], [850, 1100]], sentenceWords: [6, 12], vocabulary: "교과 개념어를 예와 함께 설명합니다. 지시어가 가리키는 말을 가까이 둡니다.", concepts: "새 핵심어 3~4개", structure: "정의·예시·원인을 연결하는 4~6문단" },
  { grade: 4, ranges: [[550, 800], [800, 1100], [1100, 1400]], sentenceWords: [7, 14], vocabulary: "한자어와 관계어를 도입하고, 문맥과 낱말 짜임으로 뜻을 짐작하게 합니다.", concepts: "새 핵심어 3~5개", structure: "비교·인과와 문단 사이 연결이 있는 4~7문단" },
  { grade: 5, ranges: [[700, 1000], [1100, 1500], [1500, 1900]], sentenceWords: [8, 17], vocabulary: "교과어·추상어를 구별해 읽습니다. 정의와 예시, 조건과 결과를 연결합니다.", concepts: "새 핵심어 4~6개", structure: "개념 설명·비교·조건·반례가 있는 5~9문단" },
  { grade: 6, ranges: [[900, 1200], [1400, 1800], [1800, 2300]], sentenceWords: [9, 20], vocabulary: "학습 도구어·추상 개념어와 다의어를 문맥에서 판별하고, 주장과 근거의 범위를 점검합니다.", concepts: "새 핵심어 5~7개", structure: "복합 인과·관점 비교·조건 판단이 있는 6~10문단" },
] as const;

export function passageMetrics(paragraphs: string[]) {
  const clean = paragraphs.map(p => p.replace(/<[^>]*>/g, "").replace(/&nbsp;/g, " ").replace(/&amp;/g, "&").trim());
  const text = clean.join(" ");
  const sentences = text.match(/[^.!?。！？]+(?:[.!?。！？]+|$)/g)?.filter(s => s.trim()) || [];
  const words = text.split(/\s+/).filter(Boolean).length;
  return { chars: Array.from(text).length, words, paragraphs: clean.filter(Boolean).length, sentences: sentences.length,
    wordsPerSentence: sentences.length ? Math.round(words / sentences.length * 10) / 10 : 0 };
}

export function assessPassage(paragraphs: string[], grade: number, level: ReadingLevel = "standard") {
  const metrics = passageMetrics(paragraphs);
  const policy = readingPolicy.find(p => p.grade === grade);
  if (!policy) return { ...metrics, range: null, lengthLabel: "학년 확인 필요" };
  const range = policy.ranges[readingLevels.indexOf(level)];
  return { ...metrics, range, lengthLabel: metrics.chars < range[0] ? "분량 보강 검토" : metrics.chars > range[1] ? "분절·축약 검토" : "분량 범위 안" };
}
