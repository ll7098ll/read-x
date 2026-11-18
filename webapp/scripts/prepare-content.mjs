import { readFile, writeFile, mkdir, copyFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { existsSync } from "node:fs";
import { compileCorpus } from "./compile-corpus.mjs";
const app = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const root = existsSync(path.join(app, "content-sources"))
  ? path.join(app, "content-sources")
  : path.resolve(app, "..");
const destination = path.join(app, "public", "curriculum");
await mkdir(destination, { recursive: true });
const corpus = await compileCorpus(root, app);
if (new Set(corpus.passages.map((p) => p.id)).size !== corpus.passages.length)
  throw new Error("Duplicate passage IDs");
await writeFile(
  path.join(destination, "passages.json"),
  JSON.stringify(corpus),
);
const drafts = JSON.parse(
  await readFile(
    path.join(root, "data/curriculum_2022/passage_drafts_batch_02.json"),
    "utf8",
  ),
);
let workshop = await readFile(
  path.join(root, "scripts/reading_workshop_template.html"),
  "utf8",
);
workshop = workshop.replace(
  "__LESSON_DATA__",
  JSON.stringify(drafts).replaceAll("</", "<\\/"),
);
workshop = workshop
  .replace(
    "</style>",
    `
/* Shared ReadX presentation; original activities and observation storage are preserved. */
:root{color:#182f43;background:#f8fafc;font-size:16px}header{background:#142b43}header p,header a{color:#e2edf6}.body{font-size:20px;line-height:2;color:#192f40}.meta,.small,.status,caption,footer{color:#425568;font-size:14px}.paper{background:#fcfbf7}.paper,.lesson{border-color:#d9e2ea}.note{font-size:14px}label{font-size:15px}.pno{color:#425568}.tag{color:#135e54}.question h4{font-size:18px}button.active{background:#1d4ed8}.step strong{color:#16614f}textarea:focus-visible,button:focus-visible,summary:focus-visible,select:focus-visible{outline:3px solid #1d4ed8}
</style>`,
  )
  .replace(
    "READX-RAY · 교사용 검토 자료",
    "ReadX · 교과 읽기 활동 · 검토용 체험",
  );
await writeFile(path.join(destination, "reading-workshop.html"), workshop);
const librarySource = path.join(
  root,
  "outputs/01a138a0-43ff-7451-bf36-fcef9c677ac6/curriculum-library.html",
);
let library = await readFile(librarySource, "utf8");
library = library.replaceAll(
  "reading-workshop-batch-02.html",
  "reading-workshop.html",
);
await writeFile(path.join(destination, "curriculum-library.html"), library);
console.log(
  `ReadX content: ${corpus.passages.length} passages; ${corpus.revisionCoverage.revised} revised, ${corpus.revisionCoverage.practiceQuestions} practice questions.`,
);
