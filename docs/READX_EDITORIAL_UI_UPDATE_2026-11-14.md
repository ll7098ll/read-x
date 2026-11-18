# ReadX editorial UI revision — 2026-11-14

<!-- readx-document-context -->
> 작성 당시의 설계·조사·구현 기록입니다. 현재 기능과 운영 상태는 최신 현황을 우선합니다. [문서 목차](README.md) · [최신 현황](PROJECT_STATUS.md)


## Direction

Revised the earlier Reading Garden treatment in response to feedback about generic generated-site styling, readability, and excessive decoration. The landing page now uses editorial typography, white space, a restrained forest-green accent, thin dividers, and photographic subject covers. The existing ReadX identity and application behavior remain connected.

## Implementation

- Rebuilt `MainLandingPage.tsx`: focused hero, direct role entry, grade-filtered lesson previews, interactive thinking example, and clear next actions.
- Replaced `reading-garden.css` with the editorial system and responsive rules. Main explanatory text is 17–18 px; metadata is secondary. Focus indicators and reduced-motion behavior are included.
- Updated the student welcome panel and account wrapper to the same typography and photographic language. Overview metrics use simpler surfaces.
- Installed local Pretendard Variable with its OFL license; no font CDN request is required.
- Added five original generated photographic assets: reading, nature, discovery, culture, and music. Topic classification uses the lesson title, subject, unit, and concept.
- Preserved the existing public-demo notice, privacy-related content, authentication actions, lesson data, and role routing.

## Assets and references

Runtime images: `webapp/public/brand/editorial/*.webp`.
Generated originals: `output/editorial-design/*-source.png`.
Exact image prompts, built-in generation tool, font source, and visual research references: `output/editorial-design/asset-manifest.json`.

## Validation

- Frontend regression suite: 79 passed, 0 failed (`output/editorial-design/ui-tests.log`).
- TypeScript build passed.
- Vite production build passed. Built-exam privacy boundary and automatic external-resource checks passed; all five WebP assets and the relative local font URL were confirmed in `webapp/dist`.
- Browser checks: 1440 px desktop and 390 px mobile viewport, no document horizontal overflow; local font and displayed images load.
- Verified grade filtering, opening an actual grade-1 reading lesson, section navigation, advancing the thinking example, and account-entry routing.
- Account entry showed the existing first-teacher setup state on the uninitialized local server; no account was created or submitted.
- Screenshots: `output/editorial-design/desktop.jpg`, `mobile.jpg`, and `full-page.jpg`.

Changes are local source and build artifacts. No hosted site was published by this revision.
