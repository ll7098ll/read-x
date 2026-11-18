// Korean TTS (Text-to-Speech) Controller using Web Speech API

export function stripHtmlTags(html: string): string {
  return html
    .replace(/<[^>]*>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

export function speakKoreanText(
  rawText: string,
  rate: number = 1.0,
  onEnd?: () => void,
  onError?: () => void
): void {
  if (typeof window === 'undefined' || !('speechSynthesis' in window)) {
    if (onEnd) onEnd();
    return;
  }

  window.speechSynthesis.cancel();
  const cleanText = stripHtmlTags(rawText);
  if (!cleanText) {
    if (onEnd) onEnd();
    return;
  }

  // A remote/system-default voice can send the text to an external provider.
  const koVoice = window.speechSynthesis.getVoices().find(v => v.localService === true && v.lang.toLowerCase().startsWith('ko'));
  if (!koVoice) { onEnd?.(); onError?.(); return; }
  const utterance = new SpeechSynthesisUtterance(cleanText);
  utterance.lang = 'ko-KR';
  utterance.rate = rate;
  utterance.pitch = 1.0;

  utterance.voice = koVoice;

  utterance.onend = () => {
    if (onEnd) onEnd();
  };
  utterance.onerror = (event) => {
    if (onEnd) onEnd();
    if (event.error !== 'canceled' && event.error !== 'interrupted') onError?.();
  };

  window.speechSynthesis.speak(utterance);
}

export function stopKoreanSpeech(): void {
  if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
    window.speechSynthesis.cancel();
  }
}
