export type RoleType = 'landing' | 'student' | 'parent' | 'teacher' | 'admin';
export type StudentModeType = 'portal' | 'clinic' | 'studio' | 'cbt_exam' | 'onboarding_cat';
export type TeacherTabType = 'matrix' | 'gallery' | 'standards' | 'hierarchy';
export type ReaderThemeType = 'paper' | 'sepia' | 'dark';
export type FontSizeType = 'sm' | 'md' | 'lg';
export type HighlightColorType = 'yellow' | 'blue' | 'pink';

export interface SubskillMeta {
  code: string;
  domain: string;
  name: string;
  desc: string;
}

export interface CurriculumConcept {
  subject: string;
  unit: string;
  concept: string;
  text_structure: string;
}

export interface ComplexityMetrics {
  kread_target: string;
  current_kread: string;
  para_count: string;
  char_count: string;
  eojeol_count: string;
  vocab_profile: string;
  csat_scaling: string;
}

export interface DiagnosticOption {
  no: number;
  text: string;
  is_correct: boolean;
  trap: string;
}

export interface DiagnosticQuestion {
  q_no: number;
  target_code: string;
  target_skill: string;
  stem: string;
  options: DiagnosticOption[];
  student_selected: number;
}

export interface DiagnosticTest {
  passage_title: string;
  passage_spec: string;
  paragraphs: string[];
  questions: DiagnosticQuestion[];
}

export interface DomainScore {
  domain: string;
  score: number;
  status: 'good' | 'warn' | 'danger';
  comment: string;
}

export interface BottleneckInfo {
  step1_rate: number;
  step2_rate: number;
  step3_rate: number;
  diagnosis_title: string;
  diagnosis_detail: string;
}

export interface TrapRadarItem {
  code: string;
  name: string;
  vuln: number;
}

export interface BacktrackingNode {
  grade: string;
  code: string;
  title: string;
  status: 'review' | 'target' | 'next';
}

export interface DiagnosisReport {
  domain_scores: DomainScore[];
  bottleneck: BottleneckInfo;
  trap_radar: TrapRadarItem[];
  backtracking_path: BacktrackingNode[];
}

export interface Step0Remedial {
  badge: string;
  rule_box: string;
  mini_question: string;
  choices: string[];
  correct: string;
  feedback: string;
}

export interface ClozeBlank {
  id: string;
  correct: string;
  options: string[];
}

export interface Step12Drill {
  badge: string;
  passage_snippet: string;
  think_aloud_prompt: string;
  cloze_sentences: string[];
  blanks: ClozeBlank[];
}

export interface VaccineItem {
  statement: string;
  answer: 'O' | 'X';
  reason: string;
}

export interface Step3Vaccine {
  badge: string;
  desc: string;
  items: VaccineItem[];
}

export interface PrescriptionClinic {
  rx_title: string;
  rx_reason: string;
  step0_remedial: Step0Remedial;
  step1_2_drill: Step12Drill;
  step3_vaccine: Step3Vaccine;
}

export interface VocabNote {
  word: string;
  tier: string;
  desc: string;
}

export interface CsatOption {
  no: number;
  text: string;
  is_correct: boolean;
  formula: string;
  explanation: string;
}

export interface CsatQuestion {
  q_no: number;
  archetype: string;
  stem: string;
  bogi: string | null;
  options: CsatOption[];
}

export interface RealCsatTest {
  test_title: string;
  passage_spec: string;
  passage_title: string;
  paragraphs: string[];
  vocab_notes: VocabNote[];
  visual_html: string;
  questions: CsatQuestion[];
}

export interface VocabSyntaxDiag {
  category: string;
  score: number;
  status: 'good' | 'warn' | 'danger';
  detail: string;
}

export interface TextStructureDiag {
  structure: string;
  score: number;
  status: 'good' | 'warn' | 'danger';
}

export interface SubskillCell {
  code: string;
  score: number;
  state: 'critical' | 'fragile' | 'mastered';
  why: string;
}

export interface XRayOverview {
  overall_score: number;
  percentile: string;
  where_summary: string;
  how_summary: string;
  vocab_syntax_diag: VocabSyntaxDiag[];
  text_structure_diag: TextStructureDiag[];
  subskill_matrix: SubskillCell[];
}

export interface ReadingHabitProfile {
  type: string;
  badge_color: string;
  avg_reading_sec: number;
  target_reading_sec: number;
  accuracy_first_try: number;
  habit_comment: string;
}

export interface BeforeAfterMetrics {
  before_score: number;
  after_score: number;
  before_kread: number;
  after_kread: number;
  kread_min: number;
  kread_max: number;
  mastered_trap: string;
}

export interface ParentTableTalk {
  title: string;
  situation: string;
  parent_question: string;
  expected_answer: string;
  coaching_tip: string;
}

export interface HottextCueItem {
  cue_id: string;
  text: string;
  role: string;
  para_idx: number;
}

export interface GraphicOrganizerNode {
  slot_id: string;
  header: string;
  sub: string;
  correct: string;
}

export interface GraphicOrganizerData {
  structure_type: string;
  title: string;
  instruction: string;
  nodes: GraphicOrganizerNode[];
  word_bank: string[];
}

export interface EbsrOption {
  no: number;
  text: string;
  is_correct: boolean;
}

export interface EbsrQuestionData {
  archetype: string;
  part_a_stem: string;
  part_a_options: EbsrOption[];
  part_b_stem: string;
  part_b_options: EbsrOption[];
  explanation: string;
}

export interface WritingChoice {
  id: string;
  text: string;
  is_correct: boolean;
  cond_check: boolean[];
  feedback: string;
}

export interface ProofreadItem {
  marker: string;
  tier: string;
  original: string;
  action_label: string;
  corrected: string;
  status_note: string;
}

export interface WritingWorkbenchData {
  mode: string;
  code: string;
  title: string;
  conditions: string[];
  draft_prefix: string;
  choices: WritingChoice[];
  proofread_items?: ProofreadItem[];
}

export interface QuestionScaffolding {
  q_no: number;
  target_para_idx: number;
  spotlight_quote: string;
  step1_hint: string;
  step2_hint: string;
}

export interface CommercialEnrichment {
  reading_habit: ReadingHabitProfile;
  before_after: BeforeAfterMetrics;
  parent_table_talk: ParentTableTalk;
  Interactive_hottext_cues: HottextCueItem[];
  graphic_organizer: GraphicOrganizerData;
  ebsr_question: EbsrQuestionData;
  writing_workbench: WritingWorkbenchData;
  question_scaffolding: QuestionScaffolding[];
}

export interface SlotLessonPackage {
  id: string;
  slot_id: string; // e.g., 'G5-EXP-V2-3'
  grade_num: number;
  grade: string;
  grade_band: string;
  domain: string;
  layer: string;
  subskill_code: string; // 'V1-1' ~ 'W5'
  sub_skill_name: string;
  prereq_com_code?: string; // e.g., 'G4-COM-A5'
  curriculum_concept: CurriculumConcept;
  complexity_metrics: ComplexityMetrics;
  mager_goal: string;
  mager_writing?: string;
  dc_steps?: {
    step1: string;
    step2: string;
    step3: string;
  };
  student_summary: string;
  prototype_step1_2: {
    step1_mission: string;
    step2_mission: string;
  };
  real_csat_test: RealCsatTest;
  prescription_clinic: PrescriptionClinic;
  commercial: CommercialEnrichment;
  status?: 'draft' | 'reviewed' | 'published';
  version?: number;
  updated_at?: string;
}

export interface CommonRemedialSlot {
  code: string; // e.g., 'G1-COM-A1' ~ 'G6-COM-A6'
  grade_num: number;
  grade: string;
  genre: string;
  domain: string;
  layer: string;
  sub_skill_name: string;
  curriculum_basis: string;
  dc_step1: string;
  dc_step2: string;
  dc_step3: string;
  mager_reading: string;
  mager_writing?: string;
  title: string;
  rule_box: string;
  passage_snippet: string;
  mini_question: string;
  choices: string[];
  correct: string;
  feedback: string;
  ox_items: VaccineItem[];
  status?: 'draft' | 'reviewed' | 'published';
}

export interface GradeData {
  id: string;
  grade_num: number;
  grade: string;
  grade_band: string;
  persona_label: string;
  slot_id: string;
  domain: string;
  layer: string;
  sub_skill_name: string;
  curriculum_concept: CurriculumConcept;
  complexity_metrics: ComplexityMetrics;
  mager_goal: string;
  student_summary: string;
  diagnostic_test: DiagnosticTest;
  diagnosis_report: DiagnosisReport;
  prescription_clinic: PrescriptionClinic;
  real_csat_test: RealCsatTest;
  xray_overview: XRayOverview;
  prototype_step1_2: {
    step1_mission: string;
    step2_mission: string;
  };
  commercial: CommercialEnrichment;
}

export interface HierarchyGoal {
  code: string;
  grade: string;
  genre: string;
  domain: string;
  layer: string;
  sub_skill_name: string;
  curriculum_basis: string;
  dc_step1: string;
  dc_step2: string;
  dc_step3: string;
  mager_reading: string;
  mager_writing?: string;
  vertical_link?: string;
  horizontal_link?: string;
}

export interface GenreSummaryItem {
  id: string;
  name: string;
  count: number;
  status: 'active' | 'extensible';
  badge: string;
  desc: string;
}

export interface TeacherRosterStudent {
  student_id: string;
  name: string;
  grade: string;
  persona_idx: number;
  triage: 'critical' | 'fragile' | 'guessing' | 'mastered';
  triage_label: string;
  kread: number;
  kread_target: number;
  smart_score: number;
  reading_habit: string;
  weak_skills: string[];
  top_trap: string;
  assigned_clinic: string;
  clinic_completed: boolean;
  scores_16: number[];
}

export interface DistractorMeta {
  code: string;
  name: string;
  formula: string;
  vaccine_name: string;
}

export interface QuestionAttemptLog {
  id: string;
  slot_id: string;
  grade_num: number;
  subskill_code: string;
  q_no: number;
  selected_option: number;
  is_correct: boolean;
  trap_code: string;
  reading_time_sec: number;
  scaffolding_used: number;
  timestamp: string;
}

export interface CommercialMasterData {
  subskill_16_meta: SubskillMeta[];
  grades_data: GradeData[];
  expository_slots_96?: SlotLessonPackage[];
  common_slots_36?: CommonRemedialSlot[];
  hierarchy: {
    expository: HierarchyGoal[];
    common: HierarchyGoal[];
  };
  genre_summary: GenreSummaryItem[];
  teacher_class_roster: TeacherRosterStudent[];
  distractor_6_meta: DistractorMeta[];
}

export interface ClueNoteItem {
  id: string;
  text: string;
  color: HighlightColorType;
  tag: string;
  createdAt: string;
}

export interface StudentAssignment {
  id: string;
  title: string;
  slotId: string;
  type: 'reading' | 'clinic' | 'vocab' | 'cat';
  assignedBy: string;
  dueDate: string;
  status: 'pending' | 'completed';
  score?: number;
  completedAt?: string;
  trapWarning?: string;
}

