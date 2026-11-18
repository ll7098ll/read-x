export const READ_X_COLORS = [
  { name: 'Ink', hex: '#202D40', token: 'ink', meaning: '제목 · 본문 · 구조', light: true },
  { name: 'Action blue', hex: '#3157D5', token: 'action', meaning: '주요 행동 · 현재 단계', light: true },
  { name: 'Discovery lime', hex: '#DDF58A', token: 'discovery', meaning: '발견 · 브랜드 포인트', light: false },
  { name: 'Reading paper', hex: '#F7F8F2', token: 'paper', meaning: '읽기 바탕 · 여백', light: false },
  { name: 'Thinking lilac', hex: '#EEEAFE', token: 'connection', meaning: '연결 · 생각 시범', light: false },
  { name: 'Evidence yellow', hex: '#FFF0B3', token: 'evidence', meaning: '선택한 근거 · 표시', light: false },
] as const;

export const READ_X_STEPS = [
  { title: '시범 보기', short: '시범', description: '어디를 보고 어떻게 생각하는지 먼저 살펴봐요.' },
  { title: '함께 읽기', short: '함께', description: '질문을 따라 단서를 찾고 이유를 연결해요.' },
  { title: '혼자 읽기', short: '혼자', description: '새로운 글에 같은 읽기 방법을 써 봐요.' },
  { title: '돌아보기', short: '돌아보기', description: '내가 쓴 방법과 다음에 해 볼 일을 남겨요.' },
] as const;
