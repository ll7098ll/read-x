import { journeyTextExtensions } from "./journeyTextExtensions";
import { readingLevels, type ReadingLevel } from "./readingPolicy";
export const JOURNEY_SLOT = "G5-EXP-V1-1";
export const JOURNEY_VERSION = 2;
export const JOURNEY_GOAL = "설명하는 말을 찾아, 내 말로 정확히 정리해요";
export const journeyStages = [
  {
    id: "start",
    label: "오늘의 목표",
    title: "글 속의 말이, 내 생각이 되도록.",
    description:
      "정의를 찾고 설명하는 방법을 배운 뒤, 다른 글에서도 사용해 봐요.",
  },
  {
    id: "model",
    label: "시범 보기",
    title: "어디를, 왜 읽는지 함께 볼까요?",
    description: "선생님이 용질의 뜻을 찾는 과정을 따라가 봐요.",
  },
  {
    id: "guided",
    label: "같이 해보기",
    title: "이번에는 네가 근거를 찾아봐요.",
    description: "용매를 설명하는 문장을 고르고, 그렇게 생각한 이유를 적어요.",
  },
  {
    id: "faded",
    label: "도움 줄이기",
    title: "새로운 낱말도 같은 방법으로.",
    description:
      "이번에는 표시된 단서 없이 시작해요. 필요하면 도움을 펼쳐도 괜찮아요.",
  },
  {
    id: "writing",
    label: "내 말로 정리",
    title: "찾아낸 근거를, 나의 문장으로.",
    description:
      "앞에서 고른 근거와 설명을 보며 두 낱말의 뜻을 정리하고 고쳐 봐요.",
  },
  {
    id: "independent",
    label: "스스로 해보기",
    title: "이제, 스스로 해볼 차례예요.",
    description: "도서관에 관한 글에서 같은 방법을 사용해 봐요.",
  },
  {
    id: "transfer",
    label: "새 글에 적용",
    title: "다른 주제에서도 해낼 수 있을까요?",
    description:
      "이번에는 물건이 우리에게 오는 과정을 읽어요. 정의를 찾는 방법은 같아요.",
  },
  {
    id: "reflection",
    label: "돌아보기",
    title: "오늘, 네 생각은 이렇게 이어졌어요.",
    description: "무엇을 보고 어떻게 설명했는지, 남긴 기록을 함께 살펴봐요.",
  },
] as const;
export type JourneyStage = (typeof journeyStages)[number]["id"];
export type TaskId = "guided" | "faded" | "independent" | "transfer";
export type JourneyPassage = {
  id: string;
  version: number;
  title: string;
  subject: string;
  paragraphs: { id: string; sentences: { id: string; text: string }[] }[];
};
export const legacyJourneyPassages: Record<string, JourneyPassage> = {
  solution: {
    id: "readx-definition-solution",
    version: 1,
    title: "물에 녹는 것, 녹이는 것",
    subject: "과학 · 용해와 용액",
    paragraphs: [
      {
        id: "solution-p1",
        sentences: [
          {
            id: "solution-1",
            text: "어떤 물질이 다른 물질에 골고루 녹아 들어가는 현상을 용해라고 합니다.",
          },
          {
            id: "solution-2",
            text: "이때 녹는 물질을 용질, 녹이는 물질을 용매라고 합니다.",
          },
        ],
      },
      {
        id: "solution-p2",
        sentences: [
          {
            id: "solution-3",
            text: "소금이 물에 녹을 때 소금은 용질이고 물은 용매입니다.",
          },
          {
            id: "solution-4",
            text: "용질과 용매가 골고루 섞인 혼합물을 용액이라고 합니다.",
          },
          {
            id: "solution-5",
            text: "소금이 물에 골고루 녹아 만들어진 소금물은 용액의 한 예입니다.",
          },
        ],
      },
      {
        id: "solution-p3",
        sentences: [
          {
            id: "solution-6",
            text: "용질, 용매, 용액은 서로 관련이 있지만 같은 뜻은 아닙니다.",
          },
          {
            id: "solution-7",
            text: "무엇이 녹고 무엇이 녹이는지 구별하면 각 낱말의 뜻을 이해할 수 있습니다.",
          },
        ],
      },
    ],
  },
  evaporation: {
    id: "readx-definition-evaporation",
    version: 1,
    title: "젖은 수건은 어떻게 마를까?",
    subject: "과학 · 물의 상태 변화",
    paragraphs: [
      {
        id: "evap-p1",
        sentences: [
          {
            id: "evap-1",
            text: "젖은 수건을 널어 두면 시간이 지나면서 수건에 있던 물이 줄어듭니다.",
          },
          {
            id: "evap-2",
            text: "액체의 표면에서 물질이 기체로 변하는 현상을 증발이라고 합니다.",
          },
        ],
      },
      {
        id: "evap-p2",
        sentences: [
          {
            id: "evap-3",
            text: "수건의 물이 수증기가 되어 공기 중으로 퍼지는 것은 증발의 예입니다.",
          },
          { id: "evap-4", text: "물이 끓지 않아도 증발은 일어납니다." },
          {
            id: "evap-5",
            text: "바닥에 고인 물이 서서히 마르는 모습에서도 증발을 관찰할 수 있습니다.",
          },
        ],
      },
    ],
  },
  library: {
    id: "readx-definition-library",
    version: 1,
    title: "도서관에서 책의 자리를 찾는 법",
    subject: "생활 · 도서관 이용",
    paragraphs: [
      {
        id: "library-p1",
        sentences: [
          {
            id: "library-1",
            text: "도서관은 사람들이 원하는 책을 찾기 쉽도록 책을 일정한 기준에 따라 정리합니다.",
          },
          {
            id: "library-2",
            text: "책의 주제나 지은이 등에 따라 붙여 책을 구별하고 서가의 위치를 찾는 데 사용하는 기호를 청구기호라고 합니다.",
          },
        ],
      },
      {
        id: "library-p2",
        sentences: [
          {
            id: "library-3",
            text: "청구기호는 보통 책등에 붙인 표지에서 볼 수 있습니다.",
          },
          {
            id: "library-4",
            text: "검색 화면에서 청구기호를 확인한 뒤 서가의 안내와 비교하면 책을 찾는 데 도움이 됩니다.",
          },
          {
            id: "library-5",
            text: "도서관에서 책을 빌리는 일은 대출이라고 합니다.",
          },
        ],
      },
    ],
  },
  distribution: {
    id: "readx-definition-distribution",
    version: 1,
    title: "사과가 우리 식탁에 오기까지",
    subject: "사회 · 생산과 소비",
    paragraphs: [
      {
        id: "distribution-p1",
        sentences: [
          {
            id: "distribution-1",
            text: "과수원에서는 농부가 사과를 기르고 수확합니다.",
          },
          {
            id: "distribution-2",
            text: "사람에게 필요한 물건을 만들거나 기르는 활동을 생산이라고 합니다.",
          },
        ],
      },
      {
        id: "distribution-p2",
        sentences: [
          {
            id: "distribution-3",
            text: "생산한 물건이 소비자에게 전달되는 과정을 유통이라고 합니다.",
          },
          {
            id: "distribution-4",
            text: "수확한 사과를 운반하고 가게에서 판매하는 일은 유통 과정에 포함됩니다.",
          },
          {
            id: "distribution-5",
            text: "사람들이 생활에 필요한 물건이나 서비스를 이용하는 활동은 소비라고 합니다.",
          },
        ],
      },
    ],
  },
};
const passageSets = Object.fromEntries(readingLevels.map((level, levelIndex) => [level,
  Object.fromEntries(Object.entries(legacyJourneyPassages).map(([key, p]) => [key, {
    ...p, version: 2, id: `${p.id}-${level}`,
    paragraphs: [...p.paragraphs, ...readingLevels.slice(0, levelIndex + 1).flatMap(layer =>
      journeyTextExtensions[key][layer].map((text, i) => ({
        id: `${key}-${layer}-p${i}`,
        sentences: text.split(/(?<=[.!?])\s+/).map((s, j) => ({ id: `${key}-${layer}-${i}-${j}`, text: s.trim() })),
      })))],
  }]))
])) as Record<ReadingLevel, Record<string, JourneyPassage>>;
export const journeyPassages = passageSets.standard;
export function getJourneyPassages(attempt?: { version: number; readingLevel?: ReadingLevel }) {
  return attempt?.version === 1 ? legacyJourneyPassages : passageSets[attempt?.readingLevel || "standard"];
}
/** Content variants share concepts and evidence: switching level is prior exposure. */
export function passageFamily(id: string) { return id.replace(/-(supported|standard|challenge)$/, ""); }
export const journeyTasks: Record<
  TaskId,
  {
    passage: keyof typeof journeyPassages;
    target: string;
    prompt: string;
    acceptableEvidence: string[];
    supportingEvidence: string[];
    hints: string[];
    feedback: string;
  }
> = {
  guided: {
    passage: "solution",
    target: "용매",
    prompt: "용매는 무엇인가요? 뜻을 설명하는 문장을 근거로 골라 보세요.",
    acceptableEvidence: ["solution-2"],
    supportingEvidence: ["solution-3", "solution-supported-2-1", "solution-supported-2-2"],
    hints: [
      "질문에서 뜻을 묻는 낱말은 무엇인가요?",
      "첫 문단에서 녹는 쪽과 녹이는 쪽을 구별해 보세요.",
      "“녹는 물질을 용질, 녹이는 물질을 용매”라는 두 설명을 비교해 보세요.",
    ],
    feedback: "녹는 쪽과 녹이는 쪽을 바꾸어 쓰지 않았는지 확인해 봐요.",
  },
  faded: {
    passage: "evaporation",
    target: "증발",
    prompt: "증발은 어떤 현상인가요? 예시와 정의를 구별해 설명해 보세요.",
    acceptableEvidence: ["evap-2"],
    supportingEvidence: ["evap-3", "evap-4", "evap-5", "evaporation-supported-1-2"],
    hints: [
      "특정 수건의 모습과 현상 자체의 뜻은 어떻게 다를까요?",
      "“현상을 증발이라고 합니다” 앞에 어떤 설명이 있나요?",
      "액체의 어느 부분에서, 어떤 상태로 변하는지 찾아보세요.",
    ],
    feedback:
      "액체의 표면에서 기체로 변한다는 뜻이 내 설명에도 들어 있는지 확인해 봐요.",
  },
  independent: {
    passage: "library",
    target: "청구기호",
    prompt: "청구기호는 무엇인가요? 글의 근거를 들어 내 말로 설명해 보세요.",
    acceptableEvidence: ["library-2"],
    supportingEvidence: ["library-4", "library-supported-1-2"],
    hints: [
      "책등에 붙어 있다는 정보와 청구기호 자체의 뜻을 구별해 보세요.",
      "첫 문단에서 “기호” 앞의 설명을 살펴보세요.",
      "책을 구별하고 위치를 찾는 데 쓰인다는 점을 설명에 연결해 보세요.",
    ],
    feedback:
      "표지가 붙은 위치만 설명했는지, 책을 구별하고 찾는 역할까지 설명했는지 살펴봐요.",
  },
  transfer: {
    passage: "distribution",
    target: "유통",
    prompt:
      "유통은 어떤 과정인가요? 생산·소비와 구별할 수 있도록 설명해 보세요.",
    acceptableEvidence: ["distribution-3"],
    supportingEvidence: ["distribution-4", "distribution-supported-0-0", "distribution-supported-0-1"],
    hints: [
      "만드는 일, 전달되는 과정, 이용하는 일을 구별해 보세요.",
      "두 번째 문단에서 유통의 뜻을 직접 설명하는 문장을 찾아보세요.",
      "생산한 물건이 누구에게 전달되는지 확인해 보세요.",
    ],
    feedback:
      "물건을 만드는 활동과 소비자에게 전달되는 과정을 구별했는지 확인해 봐요.",
  },
};
export const modelSteps = [
  {
    label: "먼저, 질문을 확인해요",
    quote: "용질은 무엇일까?",
    thought:
      "질문은 용질의 뜻을 묻고 있어. 소금의 모양보다, 용질이라는 말을 설명하는 부분을 찾아야겠어.",
    anchor: "solution-2",
    marking: { kind: "target", quote: "용질", label: "□ 설명할 대상" },
  },
  {
    label: "설명하는 말을 연결해요",
    quote: "녹는 물질을 용질",
    thought:
      "여기 “녹는 물질”이 용질을 설명하네. 바로 뒤의 “녹이는 물질”은 용매의 설명이니까 구별해서 읽어야 해.",
    anchor: "solution-2",
    marking: { kind: "evidence", quote: "녹는 물질", label: "밑줄 · 뜻을 알려 주는 말" },
  },
  {
    label: "내 설명을 원문과 비교해요",
    quote: "용질은 다른 물질에 녹는 물질이야.",
    thought:
      "소금은 그 예가 될 수 있겠구나. 내 설명에서 “녹는”과 “녹이는”을 바꾸지 않았는지 다시 확인하자.",
    anchor: "solution-3",
    marking: { kind: "link", quote: "소금은 용질", label: "→ 정의와 예 연결" },
  },
];
export function getSentence(id: string, attempt?: { version: number; readingLevel?: ReadingLevel }) {
  return Object.values(getJourneyPassages(attempt))
    .flatMap((p) => p.paragraphs.flatMap((x) => x.sentences))
    .find((s) => s.id === id);
}
export function isTaskStage(stage: JourneyStage): stage is TaskId {
  return stage in journeyTasks;
}
