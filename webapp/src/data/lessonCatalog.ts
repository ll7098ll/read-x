import raw from './commercialMasterData.json';
import { normalizeSlotPackage, normalizeCommonSlot } from '../services/contentSchema';
import type { CommercialMasterData } from '../types/courseware';

// One content boundary for the app, authoring tools and tests. Raw sources remain untouched.
export const masterData: CommercialMasterData = {
  ...raw as unknown as CommercialMasterData,
  expository_slots_96: raw.expository_slots_96.map(normalizeSlotPackage),
  common_slots_36: raw.common_slots_36.map(normalizeCommonSlot),
};
const ids = [...masterData.expository_slots_96.map(s => s.slot_id), ...masterData.common_slots_36.map(s => s.code)];
if (new Set(ids).size !== ids.length) throw new Error('수업 코드가 중복됩니다.');

export function findLesson(id: string) {
  return masterData.expository_slots_96.find(s => s.slot_id === id) || masterData.common_slots_36.find(s => s.code === id) || null;
}
