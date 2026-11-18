import type { SlotLessonPackage, CommonRemedialSlot, ReferenceNode } from '../types/courseware';
import { organizerLabels } from './organizerLabels';

type ObjectValue = Record<string, unknown>;
const object = (v: unknown): ObjectValue => v && typeof v === 'object' && !Array.isArray(v) ? v as ObjectValue : {};
const list = (v: unknown): unknown[] => Array.isArray(v) ? v : [];
const string = (v: unknown): v is string => typeof v === 'string' && v.trim().length > 0;
const plain = (v: string) => v.replace(/<[^>]*>/g, '');
const circled = '①②③④⑤⑥⑦⑧⑨⑩';

export interface ItemValidationResult { isValid: boolean; errors: string[]; warnings: string[] }

/** Runtime contract, not educational approval. Accepts unknown input without crashing. */
export function validateSlotPackage(input: unknown): ItemValidationResult {
  const errors: string[] = [], warnings: string[] = [];
  const require = (condition: unknown, path: string) => { if (!condition) errors.push(path); };
  const text = (v: unknown, path: string) => require(string(v), `${path}: 내용이 필요합니다.`);
  const strings = (v: unknown, path: string) => require(Array.isArray(v) && v.length > 0 && v.every(string), `${path}: 비어 있지 않은 문자열 목록이 필요합니다.`);
  const rows = (v: unknown, path: string): ObjectValue[] => {
    require(Array.isArray(v) && v.length > 0, `${path}: 항목이 필요합니다.`);
    return list(v).map(object);
  };
  const unique = (values: unknown[], path: string) => require(new Set(values).size === values.length, `${path}: 식별자가 중복됩니다.`);
  const options = (v: unknown, path: string) => {
    const opts = rows(v, path);
    require(opts.length >= 2, `${path}: 선택지가 두 개 이상 필요합니다.`);
    unique(opts.map(o => o.no), path);
    opts.forEach(o => {
      require(Number.isInteger(o.no) && Number(o.no) > 0, `${path}: 선지 번호가 필요합니다.`);
      text(o.text, `${path}.text`);
      require(typeof o.is_correct === 'boolean', `${path}: 정답 여부가 필요합니다.`);
    });
    require(opts.filter(o => o.is_correct === true).length === 1, `${path}: 정답은 정확히 하나여야 합니다.`);
    return opts;
  };
  const slot = object(input), test = object(slot.real_csat_test), commercial = object(slot.commercial), clinic = object(slot.prescription_clinic);
  require(slot.schema_version === '1.0', 'schema_version: 지원하지 않는 데이터 규격입니다.');
  require(Number.isInteger(slot.grade_num) && Number(slot.grade_num) >= 1 && Number(slot.grade_num) <= 6, 'grade_num: 1~6학년만 지원합니다.');
  text(slot.slot_id, 'slot_id');
  require(slot.slot_id === `G${slot.grade_num}-EXP-${slot.subskill_code}`, 'slot_id: 학년·세부목표 코드가 일치하지 않습니다.');
  text(slot.sub_skill_name, 'sub_skill_name'); text(slot.mager_goal, 'mager_goal');
  const mission = object(slot.prototype_step1_2);
  text(mission.step1_mission, 'prototype.step1_mission'); text(mission.step2_mission, 'prototype.step2_mission');
  const concept = object(slot.curriculum_concept);
  ['subject','unit','concept','text_structure'].forEach(k => text(concept[k], `curriculum_concept.${k}`));
  text(test.passage_title, 'passage_title'); strings(test.paragraphs, 'paragraphs');
  require(typeof test.visual_html === 'string', 'visual_html: 문자열이 필요합니다.');
  require(Array.isArray(test.vocab_notes), 'vocab_notes: 목록이 필요합니다.');
  list(test.vocab_notes).map(object).forEach(v => ['word','tier','desc'].forEach(k => text(v[k], `vocab_notes.${k}`)));
  const questions = rows(test.questions, 'questions'); unique(questions.map(q => q.q_no), 'questions.q_no');
  questions.forEach(q => {
    require(Number.isInteger(q.q_no) && Number(q.q_no) > 0, 'questions.q_no: 문항 번호가 필요합니다.');
    text(q.stem, 'questions.stem');
    options(q.options, `questions.${q.q_no}.options`).forEach(o => {
      require(typeof o.formula === 'string', 'options.formula: 문자열이 필요합니다.');
      text(o.explanation, 'options.explanation');
      if (typeof o.explanation === 'string' && o.explanation.length < 10) warnings.push(`문항 ${q.q_no}: 짧은 해설을 편집 검수하세요.`);
    });
  });
  const ebsr = object(commercial.ebsr_question);
  ['a','b'].forEach(part => {
    text(ebsr[`part_${part}_stem`], `ebsr.part_${part}_stem`);
    options(ebsr[`part_${part}_options`], `ebsr.part_${part}_options`);
  });
  require(typeof ebsr.explanation === 'string', 'ebsr.explanation: 문자열이 필요합니다.');
  const go = object(commercial.graphic_organizer);
  const reference = (values: unknown, depth = 0) => {
    if (depth > 12) { errors.push('organizer: 자료 계층이 너무 깊습니다.'); return; }
    rows(values, 'organizer.sections').forEach(n => {
      text(n.label, 'organizer.label');
      if (n.children !== undefined) reference(n.children, depth + 1);
      else text(n.text, 'organizer.text');
    });
  };
  text(go.title, 'organizer.title'); text(go.structure_type, 'organizer.structure_type');
  if (go.activityType === 'reference') reference(go.sections);
  else if (go.activityType === 'card_sort') {
    strings(go.word_bank, 'organizer.word_bank');
    const nodes = rows(go.nodes, 'organizer.nodes'); unique(nodes.map(n => n.slot_id), 'organizer.nodes');
    nodes.forEach(n => {
      ['slot_id','header','correct'].forEach(k => text(n[k], `organizer.${k}`));
      require(list(go.word_bank).includes(n.correct), 'organizer: 정답 카드가 보관함에 없습니다.');
    });
  } else errors.push('organizer.activityType: 활동 종류가 필요합니다.');
  const writing = object(commercial.writing_workbench);
  text(writing.title, 'writing.title');
  if (writing.activityType === 'free_response') {
    text(writing.guide, 'writing.guide'); text(writing.template, 'writing.template');
  } else if (writing.activityType === 'choice') {
    strings(writing.conditions, 'writing.conditions');
    const choices = rows(writing.choices, 'writing.choices'); unique(choices.map(c => c.id), 'writing.choices');
    choices.forEach(c => {
      ['id','text','feedback'].forEach(k => text(c[k], `writing.${k}`));
      require(typeof c.is_correct === 'boolean', 'writing.is_correct: 정답 여부가 필요합니다.');
      require(Array.isArray(c.cond_check) && c.cond_check.length === list(writing.conditions).length && c.cond_check.every(v => typeof v === 'boolean'), 'writing.cond_check: 조건별 결과가 필요합니다.');
    });
    require(choices.filter(c => c.is_correct === true).length === 1, 'writing: 정답은 정확히 하나여야 합니다.');
  } else errors.push('writing.activityType: 활동 종류가 필요합니다.');
  const step0 = object(clinic.step0_remedial), drill = object(clinic.step1_2_drill);
  if (step0.activityType === 'rule') text(step0.rule, 'clinic.rule');
  else if (step0.activityType === 'choice') {
    ['rule_box','mini_question','correct','feedback'].forEach(k => text(step0[k], `clinic.${k}`));
    strings(step0.choices, 'clinic.choices'); require(list(step0.choices).includes(step0.correct), 'clinic.correct: 정답 선택지가 없습니다.');
  } else errors.push('clinic.step0.activityType: 활동 종류가 필요합니다.');
  if (drill.activityType === 'guided_response') text(drill.task, 'clinic.task');
  else if (drill.activityType === 'cloze') {
    text(drill.think_aloud_prompt, 'clinic.think_aloud_prompt'); strings(drill.cloze_sentences, 'clinic.cloze_sentences');
    const blanks = rows(drill.blanks, 'clinic.blanks'); unique(blanks.map(b => b.id), 'clinic.blanks');
    const sentences = list(drill.cloze_sentences).join(' ');
    const ids = [...sentences.matchAll(/\{(\w+)\}/g)].map(m => m[1]);
    blanks.forEach(b => {
      text(b.id, 'clinic.blank.id'); strings(b.options, 'clinic.blank.options');
      require(list(b.options).includes(b.correct), 'clinic.blank.correct: 정답 선택지가 없습니다.');
      require(ids.includes(String(b.id)), 'clinic.blank: 문장에 대응하는 빈칸이 없습니다.');
    });
    ids.forEach(id => require(blanks.some(b => b.id === id), `clinic.blank: ${id} 정의가 없습니다.`));
  } else errors.push('clinic.drill.activityType: 활동 종류가 필요합니다.');
  rows(object(clinic.step3_vaccine).items, 'clinic.ox').forEach(v => {
    text(v.statement, 'clinic.ox.statement'); text(v.reason, 'clinic.ox.reason');
    require(v.answer === 'O' || v.answer === 'X', 'clinic.ox.answer: O 또는 X만 지원합니다.');
  });
  const paragraphs = list(test.paragraphs).filter(string).map(plain);
  require(Array.isArray(commercial.question_scaffolding), 'question_scaffolding: 목록이 필요합니다.');
  list(commercial.question_scaffolding).map(object).forEach(s => {
    require(questions.some(q => q.q_no === s.q_no), 'scaffolding: 대응 문항이 없습니다.');
    require(Number.isInteger(s.target_para_idx) && string(s.spotlight_quote) && paragraphs[Number(s.target_para_idx)]?.includes(String(s.spotlight_quote)), 'scaffolding: 근거 인용이 해당 문단과 일치하지 않습니다.');
  });
  require(Array.isArray(commercial.Interactive_hottext_cues), 'hottext: 목록이 필요합니다.');
  list(commercial.Interactive_hottext_cues).map(object).forEach(c => require(Number.isInteger(c.para_idx) && string(c.text) && paragraphs[Number(c.para_idx)]?.includes(String(c.text)), 'hottext: 단서가 해당 문단에 없습니다.'));
  return { isValid: errors.length === 0, errors, warnings };
}

function normalizeOptions(input: unknown): unknown[] {
  return list(input).map(value => {
    const opt = object(value);
    const no = opt.no ?? (typeof opt.label === 'string' ? circled.indexOf(opt.label) + 1 : 0);
    return { ...opt, no };
  });
}

function referenceNode(label: string, value: unknown): ReferenceNode {
  if (typeof value === 'string') return { label, text: value };
  if (Array.isArray(value)) return { label, children: value.map((v, i) => referenceNode(`${i + 1}`, v)) };
  if (value && typeof value === 'object') return { label, children: Object.entries(value).map(([key, v]) => {
    const translated = organizerLabels[key] || (/[가-힣]/.test(key) ? key : null);
    if (!translated) throw new Error(`구조 자료의 항목 이름을 검수해 주세요: ${key}`);
    return referenceNode(translated, v);
  }) };
  throw new Error(`구조 자료에 지원하지 않는 값이 있습니다: ${label}`);
}

/** Lossless, explicit legacy adapter. Does not modify or re-author source passages. */
export function normalizeSlotPackage(input: unknown): SlotLessonPackage {
  const s = object(input), c = object(s.commercial), rx = object(s.prescription_clinic);
  if (s.schema_version !== undefined && s.schema_version !== '1.0') throw new Error('지원하지 않는 수업 규격 버전입니다.');
  const e = object(c.ebsr_question), g = object(c.graphic_organizer), w = object(c.writing_workbench);
  const step0 = object(rx.step0_remedial), drill = object(rx.step1_2_drill), vaccine = object(rx.step3_vaccine);
  const test = object(s.real_csat_test);
  const candidate = s.schema_version === '1.0' ? s : {
    ...s, schema_version: '1.0',
    real_csat_test: {
      ...test,
      vocab_notes: list(test.vocab_notes).map(v => ({ ...object(v), desc: object(v).desc || object(v).definition, tier: object(v).tier || '낱말 풀이' })),
      questions: list(test.questions).map(q => ({ ...object(q), options: normalizeOptions(object(q).options) })),
    },
    prescription_clinic: {
      ...rx, rx_title: rx.rx_title || `${s.sub_skill_name} 연습`, rx_reason: rx.rx_reason || s.mager_goal,
      step0_remedial: { ...step0, activityType: 'rule' in step0 ? 'rule' : 'choice' },
      step1_2_drill: { ...drill, activityType: 'task' in drill ? 'guided_response' : 'cloze' },
      step3_vaccine: { ...vaccine, badge: vaccine.badge || '생각 확인', desc: vaccine.desc || '글의 근거와 맞는지 확인해 보세요.', items: vaccine.items || vaccine.ox_quiz },
    },
    commercial: {
      ...c,
      ebsr_question: {
        ...e, archetype: e.archetype || '답과 근거 연결', explanation: e.explanation || '',
        part_a_stem: e.part_a_stem || object(e.part_a).stem,
        part_b_stem: e.part_b_stem || object(e.part_b).stem,
        part_a_options: normalizeOptions(e.part_a_options || object(e.part_a).options),
        part_b_options: normalizeOptions(e.part_b_options || object(e.part_b).options),
      },
      graphic_organizer: Array.isArray(g.nodes) ? { ...g, activityType: 'card_sort' } : {
        activityType: 'reference', structure_type: g.structure_type, title: g.diagram_type || g.type || g.title,
        sections: referenceNode('생각 정리', Object.fromEntries(Object.entries(g).filter(([k]) => !['structure_type','diagram_type','type'].includes(k)))).children,
      },
      writing_workbench: 'task_title' in w ? { activityType: 'free_response', title: w.task_title, guide: w.guide, template: w.template } : { ...w, activityType: 'choice' },
    },
  };
  const result = validateSlotPackage(candidate);
  if (!result.isValid) throw new Error(`[${s.slot_id || '알 수 없는 수업'}] ${result.errors.join('\n')}`);
  return candidate as unknown as SlotLessonPackage;
}

export function normalizeCommonSlot(input: unknown): CommonRemedialSlot {
  const s = object(input), choices = list(s.choices);
  const matches = choices.filter(c => c === s.correct || (typeof c === 'string' && typeof s.correct === 'string' && c.startsWith(`${s.correct} `)));
  if (!/^G[1-6]-COM-A[1-6]$/.test(String(s.code)) || !String(s.code).startsWith(`G${s.grade_num}-`) || !choices.every(string) || matches.length !== 1 || !string(s.mini_question) || !Array.isArray(s.ox_items)) {
    throw new Error(`[${s.code}] 공통기초의 코드·문항·정답을 확인해 주세요.`);
  }
  for (const value of s.ox_items) {
    const item = object(value);
    if (!string(item.statement) || !string(item.reason) || !['O','X'].includes(String(item.answer))) throw new Error(`[${s.code}] OX 문항을 확인해 주세요.`);
  }
  return { ...s, correct: matches[0] } as unknown as CommonRemedialSlot;
}
