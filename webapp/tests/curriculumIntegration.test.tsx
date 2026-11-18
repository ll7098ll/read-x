import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync, existsSync } from "node:fs";
import {
  filterCatalog,
  type CatalogPassage,
} from "../src/components/common/CurriculumLibrary";

const corpus = JSON.parse(
  readFileSync("public/curriculum/passages.json", "utf8"),
);
const passages: CatalogPassage[] = corpus.passages;
const baselineRoot = existsSync('content-sources') ? 'content-sources/' : '../';
const baseline = JSON.parse(readFileSync(baselineRoot+'data/curriculum_2022/revisions/baseline-v1.json', 'utf8'));
const revisions = JSON.parse(readFileSync('src/data/corpusLessons.generated.json', 'utf8'));
test("통합 자료실은 원본 144편과 각 편집본의 문항, 서로 다른 짝 지문을 보존한다", () => {
  assert.equal(passages.length, 144);
  assert.equal(new Set(passages.map((p) => p.id)).size, 144);
  assert.equal(passages.filter((p) => p.origin === "신규 집필").length, 48);
  assert.equal(
    passages.reduce((n, p) => n + (p.diagnostic?.items.length || 0), 0),
    baseline.passages.reduce((n: number, p: CatalogPassage) => n + (revisions.find((r: any) => r.sourcePassageId === p.id)?.questions.length ?? p.diagnostic?.items.length ?? 0), 0),
  );
  for (const p of passages.filter((p) => p.pairId)) {
    const pair = passages.filter((x) => x.pairId === p.pairId);
    assert.equal(pair.length, 2);
    assert.deepEqual(pair[0].goalIds, pair[1].goalIds);
    assert.notDeepEqual(pair[0].paragraphs, pair[1].paragraphs);
    assert.ok(pair.every((x) => x.reviewState !== "approved"));
  }
});
test("교과 필터는 복합 교과를 포함하고 학년·활동·본문 검색을 함께 적용한다", () => {
  const science = filterCatalog(passages, "", "", "과학", "all");
  assert.ok(science.some((p) => p.subject !== "과학"));
  assert.ok(science.every((p) => p.subject.includes("과학")));
  const fixture: CatalogPassage[] = [
    { ...passages[0], id: 'match', grade: 3, subject: '수학', diagnostic: { items: [{}] } },
    { ...passages[0], id: 'wrong-grade', grade: 4, subject: '수학', diagnostic: { items: [{}] } },
    { ...passages[0], id: 'wrong-subject', grade: 3, subject: '과학', diagnostic: { items: [{}] } },
    { ...passages[0], id: 'without-activity', grade: 3, subject: '수학', diagnostic: undefined },
  ];
  assert.deepEqual(filterCatalog(fixture, '', '3', '수학', 'activity').map(p => p.id), ['match']);
  const p = passages[0];
  assert.ok(
    filterCatalog(
      passages,
      p.paragraphs[0].slice(0, 15),
      String(p.grade),
      "",
      "all",
    ).some((x) => x.id === p.id),
  );
  assert.equal(
    filterCatalog(passages, "no-such-readx-passage", "", "", "all").length,
    0,
  );
});
