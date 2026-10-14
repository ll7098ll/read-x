"""Read-only project/content audit; writes evidence only under output/audit.

This checks structure and references, not educational validity or psychometrics.
It never imports generators or rewrites the item bank.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "audit"
EXCLUDED = {"node_modules", "dist", "__pycache__", ".git", ".venv"}
SKILLS = ["V1-1", "V1-2", "V1-3", "V1-4", "V2-1", "V2-2", "V2-3", "V2-4", "V3-1", "V3-2", "V3-3", "W1", "W2", "W3", "W4", "W5"]


def plain(value):
    return re.sub(r"<[^>]+>", "", value)


def main():
    inventory, parse_errors = [], []
    by_hash = defaultdict(list)
    loaded = {}
    scan_counts = Counter()
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(p in EXCLUDED for p in path.relative_to(ROOT).parts):
            continue
        if OUT in path.parents or path.suffix == ".tsbuildinfo":
            continue
        rel = path.relative_to(ROOT).as_posix()
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        by_hash[digest].append(rel)
        entry = {"path": rel, "bytes": len(raw), "sha256": digest}
        if path.suffix in {".json", ".py", ".tsx", ".ts", ".js", ".css", ".html", ".md", ".rules"} or path.name == ".gitignore":
            try:
                content = raw.decode("utf-8-sig")
                entry["lines"] = len(content.splitlines())
                if path.suffix == ".json":
                    loaded[rel] = json.loads(content)
                    entry["check"] = "json_parse_ok"
                elif path.suffix == ".py":
                    ast.parse(content, filename=rel)
                    entry["check"] = "python_ast_ok"
                else:
                    entry["check"] = "text_scan_ok"
                if rel.startswith("webapp/src/") and path.suffix != ".json":
                    for label, pattern in {
                        "html_injection_sites": r"dangerouslySetInnerHTML",
                        "random_calls": r"Math\.random\(",
                        "alert_calls": r"\balert\(",
                        "any_type_uses": r"\bas any\b|:\s*any\b",
                        "aria_attributes": r"aria-[a-z-]+=",
                    }.items():
                        scan_counts[label] += len(re.findall(pattern, content))
            except Exception as exc:
                parse_errors.append({"path": rel, "error": str(exc)})
                entry["check"] = "parse_error"
        elif path.suffix == ".xlsx":
            with zipfile.ZipFile(path) as archive:
                bad = archive.testzip()
                entry["check"] = "xlsx_zip_ok" if bad is None else "xlsx_zip_error"
                entry["worksheets"] = len([n for n in archive.namelist() if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)])
        else:
            entry["check"] = "inventory_only"
        inventory.append(entry)

    master = loaded["webapp/src/data/commercialMasterData.json"]
    slots = master.get("expository_slots_96", [])
    commons = master.get("common_slots_36", [])
    slot_ids = {s["slot_id"] for s in slots}
    common_ids = {c["code"] for c in commons}
    findings = []

    def issue(kind, location, detail):
        findings.append({"kind": kind, "location": location, "detail": detail})

    def check_options(options, location, expected=None):
        if sum(bool(o.get("is_correct")) for o in options) != 1:
            issue("answer_count", location, "Must contain exactly one correct option")
        if expected is not None and len(options) != expected:
            issue("option_count", location, f"Expected {expected}, got {len(options)}")
        ids = [o.get("no") for o in options]
        if any(not isinstance(n, int) for n in ids):
            issue("missing_option_number", location, "UI requires numeric no; some records use label instead")
        elif len(ids) != len(set(ids)):
            issue("duplicate_option_id", location, str(ids))

    counts = Counter()
    answers = defaultdict(Counter)
    metadata_gaps = Counter()
    for grade in range(1, 7):
        expected = {f"G{grade}-EXP-{s}" for s in SKILLS}
        present = {s["slot_id"] for s in slots if s["grade_num"] == grade}
        for missing in sorted(expected - present):
            issue("missing_slot", missing, "Expected expository slot")
        for unexpected in sorted(present - expected):
            issue("unexpected_slot", unexpected, "Not in expected hierarchy")
    if len(slot_ids) != len(slots) or len(common_ids) != len(commons):
        issue("duplicate_content_id", "master", "Non-unique slot IDs")
    for s in slots:
        sid = s["slot_id"]
        g = s["grade_num"]
        expected_opts = 3 if g < 3 else 4 if g < 5 else 5
        paragraphs = [plain(p) for p in s.get("real_csat_test", {}).get("paragraphs", [])]
        for key in ["status", "version", "source", "license", "reviewed_by"]:
            if not s.get(key):
                metadata_gaps[key] += 1
        if not paragraphs:
            issue("empty_passage", sid, "No paragraphs")
        prereq = s.get("prereq_com_code")
        if prereq and prereq not in common_ids:
            issue("missing_prerequisite", sid, prereq)
        commercial = s.get("commercial", {})
        for cue in commercial.get("Interactive_hottext_cues", []):
            counts["hottext_cues"] += 1
            idx = cue.get("para_idx", -1)
            if not (0 <= idx < len(paragraphs)) or not cue.get("text") or cue["text"] not in paragraphs[idx]:
                issue("hottext_substring", sid, cue)
        questions = s.get("real_csat_test", {}).get("questions", [])
        counts["questions"] += len(questions)
        for q in questions:
            loc = f"{sid}/Q{q.get('q_no')}"
            opts = q.get("options", [])
            check_options(opts, loc, expected_opts)
            for opt in opts:
                if opt.get("is_correct"):
                    answers[g][str(opt.get("no", opt.get("label")))] += 1
                elif not re.search(r"D[1-6]", opt.get("formula", "")):
                    issue("missing_trap_code", loc, opt.get("no"))
                if len(opt.get("explanation", "").strip()) < 10:
                    issue("short_explanation", loc, opt.get("no"))
        for sc in commercial.get("question_scaffolding", []):
            counts["scaffolding_quotes"] += 1
            idx = sc.get("target_para_idx", -1)
            if not (0 <= idx < len(paragraphs)) or not sc.get("spotlight_quote") or sc["spotlight_quote"] not in paragraphs[idx]:
                issue("scaffold_substring", sid, sc.get("q_no"))
        if len(commercial.get("question_scaffolding", [])) != len(questions):
            issue("scaffold_count", sid, "One scaffold per question expected")
        ebsr = commercial.get("ebsr_question", {})
        for part in ["part_a_options", "part_b_options"]:
            if not isinstance(ebsr.get(part), list):
                issue("missing_ebsr_part_contract", sid, part)
            else:
                check_options(ebsr[part], f"{sid}/{part}")
        organizer = commercial.get("graphic_organizer", {})
        if not isinstance(organizer.get("nodes"), list) or not isinstance(organizer.get("word_bank"), list):
            issue("missing_organizer_contract", sid, "nodes and word_bank required by renderer")
        for node in organizer.get("nodes", []):
            if node.get("correct") not in organizer.get("word_bank", []):
                issue("organizer_answer_missing", sid, node.get("slot_id"))
        clinic = s.get("prescription_clinic", {})
        mini = clinic.get("step0_remedial", {})
        if not isinstance(mini.get("choices"), list) or "correct" not in mini:
            issue("missing_clinic_contract", sid, "step0_remedial.choices/correct missing")
        elif mini.get("correct") not in mini.get("choices", []):
            issue("clinic_answer_missing", sid, mini.get("correct"))
        drill = clinic.get("step1_2_drill", {})
        if not isinstance(drill.get("blanks"), list) or not isinstance(drill.get("cloze_sentences"), list):
            issue("missing_cloze_contract", sid, "blanks and cloze_sentences required by renderer")
        writing = commercial.get("writing_workbench", {})
        if not isinstance(writing.get("conditions"), list) or not isinstance(writing.get("choices"), list):
            issue("missing_writing_contract", sid, "conditions and choices required by renderer")
        for blank in drill.get("blanks", []):
            if blank.get("correct") not in blank.get("options", []):
                issue("cloze_answer_missing", sid, blank.get("id"))
    for c in commons:
        if c.get("correct") not in c.get("choices", []):
            issue("common_answer_representation_mismatch", c["code"], {"correct": c.get("correct"), "choices": c.get("choices")})

    bank_drift = []
    for g in range(1, 7):
        bank = loaded[f"data/item_bank/g{g}_item_bank.json"]
        for item in bank.get("expository_slots", []):
            other = next((s for s in slots if s["slot_id"] == item["slot_id"]), None)
            if item != other:
                bank_drift.append(item["slot_id"])
    seed = loaded["data/firestore_seed_132_db.json"]
    seed_exp = seed.get("collections", {}).get("item_bank_expository", {})
    seed_drift = [s["slot_id"] for s in slots if seed_exp.get(s["slot_id"]) != s]
    store_text = (ROOT / "webapp/src/store/useCoursewareStore.ts").read_text(encoding="utf-8")
    initial = store_text.split("const INITIAL_ASSIGNMENTS:", 1)[1].split("const INITIAL_SMART_SCORES", 1)[0]
    task_refs = re.findall(r"slotId:\s*'([^']+)'", initial)
    missing_task_refs = sorted(set(task_refs) - slot_ids - common_ids)

    summary = {
        "date": "2026-10-14",
        "scope": "Project files plus audit scripts; excludes dependencies, dist, caches and audit evidence",
        "inventory_files": len(inventory),
        "files_by_extension": dict(Counter(Path(e["path"]).suffix or "[none]" for e in inventory)),
        "parse_errors": parse_errors,
        "source_scan_counts": dict(scan_counts),
        "expository_slots": len(slots), "common_slots": len(commons),
        "grade_summaries": len(master.get("grades_data", [])),
        "teacher_roster": len(master.get("teacher_class_roster", [])),
        "content_counts": dict(counts),
        "answer_positions_by_grade": {str(g): dict(v) for g, v in answers.items()},
        "content_issue_counts": dict(Counter(i["kind"] for i in findings)),
        "content_issues": findings,
        "slot_metadata_gaps": dict(metadata_gaps),
        "bank_vs_bundle_drift": bank_drift,
        "seed_vs_bundle_drift": seed_drift,
        "missing_initial_assignment_targets": missing_task_refs,
        "identical_file_groups": [v for v in by_hash.values() if len(v) > 1],
        "limits": ["Structural validation cannot establish factual correctness, rights clearance, curriculum alignment or valid diagnosis.", "XLSX: ZIP integrity and sheet count only; HTML: source scan, not every generated page rendered."],
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / "content-audit.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    console = {k: v for k, v in summary.items() if k not in {"content_issues", "identical_file_groups"}}
    print(json.dumps(console, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
