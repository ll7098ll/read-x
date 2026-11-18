import type { ExamRole } from '../types/exam';

export const examRoleLabels: Record<ExamRole, string> = { student: '나의 배움터', teacher: '선생님 수업실', parent: '우리 아이의 배움' };
export function readExamRoute(hash: string): { active: boolean; role: ExamRole | null } {
  if (/^#\/(?:exams|home)(?:\/|$)/.test(hash)) return { active: true, role: null };
  const match = /^#\/(student|teacher|parent)\/(?:exams|classes|manage|account|home)(?:\/|$)/.exec(hash);
  return { active: !!match, role: match ? match[1] as ExamRole : null };
}
export const examPath = (role?: ExamRole | null) => role ? `#/${role}/exams` : '#/exams';
export const learningHomePath = (role: ExamRole) => role === 'student' ? '#/student/portal' : `#/${role}`;

// Links choose a screen; authenticated API sessions remain the only role authority.
export const enterExam = (role: ExamRole) => { window.location.hash = examPath(role); };

export const learningPath = (role: ExamRole) => `#/${role}/classes`;
export const isLearningRoute = (hash: string) => /^#\/(student|teacher|parent)\/classes(?:\/|$)/.test(hash);

export const isManagementRoute = (hash: string) => /^#\/(student|teacher|parent)\/(manage|account)(?:\/|$)/.test(hash);
export const managementPath = (role: ExamRole) => `#/${role}/${role === 'teacher' ? 'manage' : 'account'}`;

export const homePath = (role: ExamRole) => `#/${role}/home`;
export const isHomeRoute = (hash: string) => /^#\/(?:home|(?:student|teacher|parent)\/home)(?:\/|$)/.test(hash);
