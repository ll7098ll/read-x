import { create } from "zustand";
import { createJSONStorage, persist } from "zustand/middleware";
import { modelSteps, JOURNEY_VERSION } from "../data/learningJourney";
import { practiceStorage } from "./useReadingWorkspace";

type ScriptState = { version: number; draft: string[]; applied: string[] | null; appliedAt: string | null; edit: (step: number, text: string) => void; apply: () => void; reset: () => void };
export const useThinkingScript = create<ScriptState>()(persist(set=>({
  version:JOURNEY_VERSION,draft:modelSteps.map(m=>m.thought),applied:null,appliedAt:null,
  edit:(step,text)=>set(s=>({draft:modelSteps.map((m,i)=>i===step?text:s.draft[i]??m.thought)})),
  apply:()=>set(s=>s.draft.length===modelSteps.length&&s.draft.every(t=>t.trim())?{applied:s.draft.map(t=>t.trim()),appliedAt:new Date().toISOString(),version:JOURNEY_VERSION}:s),
  reset:()=>set({draft:modelSteps.map(m=>m.thought),applied:null,appliedAt:null,version:JOURNEY_VERSION}),
}),{name:"readx_thinking_script_v1",storage:createJSONStorage(()=>practiceStorage)}));

export function useModelScript() {
  const script=useThinkingScript();
  return modelSteps.map((m,i)=>({...m,thought:script.version===JOURNEY_VERSION&&script.applied?.[i]?.trim()?script.applied[i]:m.thought}));
}
