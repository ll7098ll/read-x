import { create } from "zustand";
import {
  persist,
  createJSONStorage,
  type StateStorage,
} from "zustand/middleware";
import { useState, useEffect, Dispatch, SetStateAction } from "react";

type ReadingWorkspace = {
  sessions: Record<string, Record<string, unknown>>;
  lastSlotId: string | null;
  save: (slotId: string, key: string, value: unknown) => void;
  visit: (slotId: string) => void;
};
export const useReadingStorageStatus = create<{ failed: boolean }>(() => ({
  failed: false,
}));
export const practiceStorage: StateStorage = {
  getItem: (key) => {
    try {
      return localStorage.getItem(key);
    } catch {
      useReadingStorageStatus.setState({ failed: true });
      return null;
    }
  },
  setItem: (key, value) => {
    try {
      localStorage.setItem(key, value);
      useReadingStorageStatus.setState({ failed: false });
    } catch {
      useReadingStorageStatus.setState({ failed: true });
    }
  },
  removeItem: (key) => {
    try {
      localStorage.removeItem(key);
    } catch {
      useReadingStorageStatus.setState({ failed: true });
    }
  },
};
export const useReadingWorkspace = create<ReadingWorkspace>()(
  persist(
    (set) => ({
      sessions: {},
      lastSlotId: null,
      save: (slotId, key, value) =>
        set((s) => ({
          sessions: {
            ...s.sessions,
            [slotId]: { ...s.sessions[slotId], [key]: value },
          },
        })),
      visit: (lastSlotId) => set({ lastSlotId }),
    }),
    {
      name: "readx_reading_workspace_v1",
      storage: createJSONStorage(() => practiceStorage),
    },
  ),
);

/** UI-only practice recovery, kept separate from official assessment records. */
export function usePracticeState<T>(
  slotId: string,
  key: string,
  initial: T,
): [T, Dispatch<SetStateAction<T>>] {
  const [value, setValue] = useState<T>(() => {
    const saved = useReadingWorkspace.getState().sessions[slotId]?.[key];
    return saved === undefined ? initial : (saved as T);
  });
  useEffect(() => {
    useReadingWorkspace.getState().save(slotId, key, value);
  }, [slotId, key, value]);
  return [value, setValue];
}
