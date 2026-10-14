# 프로젝트 파일 점검 색인

2026-10-14 점검 시점의 파일 목록이다. 기존 파일 167개와 이번에 추가한 진단 스크립트 2개를 구분한다. 의존성·빌드 결과·캐시·이 점검 결과 폴더는 제외했다.

아래 검사는 파일 형식별 기본 검사다. 모든 행에 대한 수동 의미 검토나 교육내용 검수 완료를 뜻하지 않는다. 핵심 코드의 상세 발견 사항과 96개 설명문 데이터의 렌더 검사는 [점검 보고서](../../docs/COMMERCIAL_READINESS_AUDIT_2026-10-14.md)를 함께 본다. 원본 해시는 [inventory.json](./inventory.json)에 있다.

## 기존 프로젝트 파일

| 경로 | 기본 검사 | 크기(bytes) |
| --- | --- | ---: |
| `.gitignore` | 텍스트 읽기·패턴/구조 검사 | 484 |
| `CI_AND_UI_UX_THEME_KIT_MASTER.md` | 텍스트 읽기·패턴/구조 검사 | 20801 |
| `courseware_master_whitepaper_prd.html` | 텍스트 읽기·패턴/구조 검사 | 357748 |
| `data/expository_courseware_hierarchy.json` | JSON 파싱 | 267285 |
| `data/firestore_seed_132_db.json` | JSON 파싱 | 1985380 |
| `data/item_bank/g1_item_bank.json` | JSON 파싱 | 303139 |
| `data/item_bank/g2_item_bank.json` | JSON 파싱 | 228574 |
| `data/item_bank/g3_item_bank.json` | JSON 파싱 | 379237 |
| `data/item_bank/g4_item_bank.json` | JSON 파싱 | 291803 |
| `data/item_bank/g5_item_bank.json` | JSON 파싱 | 332621 |
| `data/item_bank/g6_item_bank.json` | JSON 파싱 | 369897 |
| `data/parsed_96_curriculum_specs.json` | JSON 파싱 | 83225 |
| `data/unified_courseware_master_data.json` | JSON 파싱 | 189961 |
| `DEVELOPMENT_PLAN_READX.md` | 텍스트 읽기·패턴/구조 검사 | 21529 |
| `docs/CI_AND_UI_UX_THEME_KIT_MASTER.md` | 텍스트 읽기·패턴/구조 검사 | 20801 |
| `docs/DEVELOPMENT_PLAN_READX.md` | 텍스트 읽기·패턴/구조 검사 | 21529 |
| `docs/Google_Stitch_UIUX_Design_Prompt_Guide.md` | 텍스트 읽기·패턴/구조 검사 | 109624 |
| `docs/PRD_2022개정_교과개념_설명문_문해력_코스웨어.md` | 텍스트 읽기·패턴/구조 검사 | 45890 |
| `docs/PRD_문해력_코스웨어_상용화_마스터.md` | 텍스트 읽기·패턴/구조 검사 | 28534 |
| `docs/UI_UX_COMPONENT_DEVELOPMENT_SPEC.md` | 텍스트 읽기·패턴/구조 검사 | 21951 |
| `firestore.rules` | 텍스트 읽기·패턴/구조 검사 | 1428 |
| `Google_Stitch_UIUX_Design_Prompt_Guide.md` | 텍스트 읽기·패턴/구조 검사 | 109624 |
| `new_goals_matrix.json` | JSON 파싱 | 422022 |
| `output/expository_literacy_courseware.html` | 텍스트 읽기·패턴/구조 검사 | 756087 |
| `output/readxray_pro_commercial_v2.html` | 텍스트 읽기·패턴/구조 검사 | 756087 |
| `output/readxray_visual_theme_kit.html` | 텍스트 읽기·패턴/구조 검사 | 35767 |
| `PRD_2022개정_교과개념_설명문_문해력_코스웨어.md` | 텍스트 읽기·패턴/구조 검사 | 45890 |
| `PRD_문해력_코스웨어_상용화_마스터.md` | 텍스트 읽기·패턴/구조 검사 | 28534 |
| `README.md` | 텍스트 읽기·패턴/구조 검사 | 5664 |
| `research/courseware_track1_curriculum_concepts_96slots.md` | 텍스트 읽기·패턴/구조 검사 | 137143 |
| `research/courseware_track2_passage_complexity_vocab_standards.md` | 텍스트 읽기·패턴/구조 검사 | 47311 |
| `research/courseware_track3_csat_question_and_courseware_schema.md` | 텍스트 읽기·패턴/구조 검사 | 65591 |
| `research/courseware_track4_commercial_product_ux_tei_dashboard_research.md` | 텍스트 읽기·패턴/구조 검사 | 32905 |
| `scripts/build_commercial_dataset.py` | Python AST 구문 검사 | 74810 |
| `scripts/build_courseware_whitepaper_html.py` | Python AST 구문 검사 | 19988 |
| `scripts/build_mega_master_whitepaper_prd.py` | Python AST 구문 검사 | 55021 |
| `scripts/build_unified_courseware.py` | Python AST 구문 검사 | 201409 |
| `scripts/capture_screenshots.py` | Python AST 구문 검사 | 8281 |
| `scripts/compile_and_validate_132_db.py` | Python AST 구문 검사 | 8690 |
| `scripts/enrich_diagnostic_xray_data.py` | Python AST 구문 검사 | 41493 |
| `scripts/gen_g1.py` | Python AST 구문 검사 | 61421 |
| `scripts/gen_g2.py` | Python AST 구문 검사 | 130369 |
| `scripts/gen_g3.py` | Python AST 구문 검사 | 77373 |
| `scripts/gen_g4.py` | Python AST 구문 검사 | 150788 |
| `scripts/gen_g5.py` | Python AST 구문 검사 | 45035 |
| `scripts/gen_g5_complete.py` | Python AST 구문 검사 | 121343 |
| `scripts/gen_g6.py` | Python AST 구문 검사 | 14076 |
| `scripts/gen_g6_slots_v1.py` | Python AST 구문 검사 | 47902 |
| `scripts/gen_g6_slots_v2.py` | Python AST 구문 검사 | 47896 |
| `scripts/gen_g6_slots_v3.py` | Python AST 구문 검사 | 37531 |
| `scripts/gen_g6_slots_w.py` | Python AST 구문 검사 | 49254 |
| `scripts/gen_item_bank_g1_g2.py` | Python AST 구문 검사 | 159012 |
| `scripts/gen_item_bank_g3_g4.py` | Python AST 구문 검사 | 211709 |
| `scripts/inspect_hierarchy_common.py` | Python AST 구문 검사 | 501 |
| `scripts/inspect_progress.py` | Python AST 구문 검사 | 743 |
| `scripts/item_bank_schema_helper.py` | Python AST 구문 검사 | 11462 |
| `scripts/parse_curriculum.py` | Python AST 구문 검사 | 1582 |
| `scripts/render_all_in_one_html.py` | Python AST 구문 검사 | 67257 |
| `scripts/update_stitch_guide_v6.py` | Python AST 구문 검사 | 109589 |
| `textbook_reference/data/g6_master_hierarchy.json` | JSON 파싱 | 318831 |
| `textbook_reference/data/units/unit1_poetry/batch1_v1.py` | Python AST 구문 검사 | 87896 |
| `textbook_reference/data/units/unit1_poetry/batch2_v2.py` | Python AST 구문 검사 | 81840 |
| `textbook_reference/data/units/unit1_poetry/batch3_v3.py` | Python AST 구문 검사 | 63474 |
| `textbook_reference/data/units/unit1_poetry/batch4_w.py` | Python AST 구문 검사 | 100548 |
| `textbook_reference/data/units/unit1_poetry/build_unit1.py` | Python AST 구문 검사 | 2935 |
| `textbook_reference/data/units/unit1_poetry/hierarchy.json` | JSON 파싱 | 56462 |
| `textbook_reference/data/units/unit1_poetry/lessons_all.json` | JSON 파싱 | 327070 |
| `textbook_reference/data/units/unit2_narrative/batch1_v1.py` | Python AST 구문 검사 | 108069 |
| `textbook_reference/data/units/unit2_narrative/batch2_v2.py` | Python AST 구문 검사 | 93564 |
| `textbook_reference/data/units/unit2_narrative/batch3_v3.py` | Python AST 구문 검사 | 75969 |
| `textbook_reference/data/units/unit2_narrative/batch4_w.py` | Python AST 구문 검사 | 108222 |
| `textbook_reference/data/units/unit2_narrative/build_unit2.py` | Python AST 구문 검사 | 2545 |
| `textbook_reference/data/units/unit2_narrative/hierarchy.json` | JSON 파싱 | 67977 |
| `textbook_reference/data/units/unit2_narrative/lessons_all.json` | JSON 파싱 | 378373 |
| `textbook_reference/data/units/unit3_essay/batch1_v1.py` | Python AST 구문 검사 | 95824 |
| `textbook_reference/data/units/unit3_essay/batch2_v2.py` | Python AST 구문 검사 | 87785 |
| `textbook_reference/data/units/unit3_essay/batch3_v3.py` | Python AST 구문 검사 | 65849 |
| `textbook_reference/data/units/unit3_essay/batch4_w.py` | Python AST 구문 검사 | 100825 |
| `textbook_reference/data/units/unit3_essay/build_unit3.py` | Python AST 구문 검사 | 3104 |
| `textbook_reference/data/units/unit3_essay/hierarchy.json` | JSON 파싱 | 68095 |
| `textbook_reference/data/units/unit3_essay/lessons_all.json` | JSON 파싱 | 342300 |
| `textbook_reference/data/units/unit4_expository/__init__.py` | Python AST 구문 검사 | 188 |
| `textbook_reference/data/units/unit4_expository/batch1_v1.py` | Python AST 구문 검사 | 110963 |
| `textbook_reference/data/units/unit4_expository/batch2_v2.py` | Python AST 구문 검사 | 103231 |
| `textbook_reference/data/units/unit4_expository/batch3_v3.py` | Python AST 구문 검사 | 82920 |
| `textbook_reference/data/units/unit4_expository/batch4_w.py` | Python AST 구문 검사 | 122793 |
| `textbook_reference/data/units/unit4_expository/build_unit4.py` | Python AST 구문 검사 | 3142 |
| `textbook_reference/data/units/unit4_expository/hierarchy.json` | JSON 파싱 | 79095 |
| `textbook_reference/data/units/unit4_expository/lessons_all.json` | JSON 파싱 | 411505 |
| `textbook_reference/data/units/unit5_argumentative/batch1_v1.py` | Python AST 구문 검사 | 101510 |
| `textbook_reference/data/units/unit5_argumentative/batch2_v2.py` | Python AST 구문 검사 | 95730 |
| `textbook_reference/data/units/unit5_argumentative/batch3_v3.py` | Python AST 구문 검사 | 77327 |
| `textbook_reference/data/units/unit5_argumentative/batch4_w.py` | Python AST 구문 검사 | 110218 |
| `textbook_reference/data/units/unit5_argumentative/build_unit5.py` | Python AST 구문 검사 | 2093 |
| `textbook_reference/data/units/unit5_argumentative/hierarchy.json` | JSON 파싱 | 78508 |
| `textbook_reference/data/units/unit5_argumentative/lessons_all.json` | JSON 파싱 | 377850 |
| `textbook_reference/docs/01_기획과_철학/01_교육과정_설계_철학_및_나선형_위계.md` | 텍스트 읽기·패턴/구조 검사 | 21786 |
| `textbook_reference/docs/01_기획과_철학/02_점진적_책임이양(GRR)_및_사고구술_이론.md` | 텍스트 읽기·패턴/구조 검사 | 37717 |
| `textbook_reference/docs/02_텍스트_선정_및_원문_검증/01_5대장르_텍스트_선정_종합_보고서.md` | 텍스트 읽기·패턴/구조 검사 | 20907 |
| `textbook_reference/docs/02_텍스트_선정_및_원문_검증/02_문학_트랙A_시_수필_원문_검증.md` | 텍스트 읽기·패턴/구조 검사 | 61713 |
| `textbook_reference/docs/02_텍스트_선정_및_원문_검증/03_문학_트랙B_이야기_꼴뚜기_검증.md` | 텍스트 읽기·패턴/구조 검사 | 62514 |
| `textbook_reference/docs/02_텍스트_선정_및_원문_검증/04_비문학_트랙C_설명문_과학환경_검증.md` | 텍스트 읽기·패턴/구조 검사 | 139345 |
| `textbook_reference/docs/02_텍스트_선정_및_원문_검증/05_비문학_트랙D_논설문_시사통계_검증.md` | 텍스트 읽기·패턴/구조 검사 | 105047 |
| `textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/01_다각도_레이아웃_옵션_비교_및_마스터플랜.md` | 텍스트 읽기·패턴/구조 검사 | 29997 |
| `textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/02_읽기_쓰기_1대1_수평전이_및_2층첨삭노트.md` | 텍스트 읽기·패턴/구조 검사 | 60414 |
| `textbook_reference/docs/04_교사용_지도서_설계_컨셉/01_교사용_지도서_6대_모듈_및_수업_운영_모델.md` | 텍스트 읽기·패턴/구조 검사 | 12675 |
| `textbook_reference/docs/05_AI_에이전트_개발_과정/01_멀티_서브에이전트_병렬_협업_파이프라인.md` | 텍스트 읽기·패턴/구조 검사 | 8236 |
| `textbook_reference/new_goals_matrix.json` | JSON 파싱 | 422022 |
| `textbook_reference/교과서_index.html` | 텍스트 읽기·패턴/구조 검사 | 92445 |
| `textbook_reference/문해력 교과서 백서.html` | 텍스트 읽기·패턴/구조 검사 | 869368 |
| `textbook_reference/초1_6학년_문해력_하위기능_및_목표위계_마스터.json` | JSON 파싱 | 1007127 |
| `textbook_reference/초1_6학년_장르별_문해력_하위기능_및_목표위계_마스터.xlsx` | xlsx_zip_ok / 셀별 내용·수식·레이아웃은 미검수 | 995216 |
| `UI_UX_COMPONENT_DEVELOPMENT_SPEC.md` | 텍스트 읽기·패턴/구조 검사 | 21951 |
| `webapp/index.html` | 텍스트 읽기·패턴/구조 검사 | 1577 |
| `webapp/package-lock.json` | JSON 파싱 | 95122 |
| `webapp/package.json` | JSON 파싱 | 650 |
| `webapp/postcss.config.js` | 텍스트 읽기·패턴/구조 검사 | 80 |
| `webapp/src/App.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 6953 |
| `webapp/src/components/admin/AcademySeatBillingCard.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 16637 |
| `webapp/src/components/admin/BrandedCounselingReportModal.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 22508 |
| `webapp/src/components/admin/ItemBankAdminStudio.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 38907 |
| `webapp/src/components/common/ErrorBoundary.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 3353 |
| `webapp/src/components/layout/AdminHeader.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 2570 |
| `webapp/src/components/layout/MainLandingPage.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 18261 |
| `webapp/src/components/layout/ParentHeader.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 3065 |
| `webapp/src/components/layout/RoleGatewayModal.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 9404 |
| `webapp/src/components/layout/StudentHeader.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 3841 |
| `webapp/src/components/layout/TeacherHeader.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 2612 |
| `webapp/src/components/layout/TopGlobalNav.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 13111 |
| `webapp/src/components/layout/XRaySummaryHero.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 4206 |
| `webapp/src/components/parent/ParentInstantGlanceModal.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 5965 |
| `webapp/src/components/parent/ParentJourneyHub.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 16767 |
| `webapp/src/components/parent/ParentXRayReportView.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 16820 |
| `webapp/src/components/student/AdaptiveClinicStudio.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 21716 |
| `webapp/src/components/student/CbtMockExamStudio.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 21744 |
| `webapp/src/components/student/GalaxyExpeditionMap.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 12919 |
| `webapp/src/components/student/OnboardingCatModal.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 22944 |
| `webapp/src/components/student/SplitScreenStudio.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 39731 |
| `webapp/src/components/student/StudentJourneyHub.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 19135 |
| `webapp/src/components/student/StudentPortalDashboard.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 41437 |
| `webapp/src/components/student/VocabDuelArena.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 11549 |
| `webapp/src/components/teacher/LiveClassroomCockpit.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 6882 |
| `webapp/src/components/teacher/TeacherClassMatrixView.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 39835 |
| `webapp/src/components/teacher/TeacherJourneyHub.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 19977 |
| `webapp/src/components/tei/EBSRQuestionCard.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 8266 |
| `webapp/src/components/tei/EyeBeaconGuide.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 2343 |
| `webapp/src/components/tei/GraphicOrganizerBuilder.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 8171 |
| `webapp/src/components/tei/HotTextPassage.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 6143 |
| `webapp/src/components/tei/index.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 335 |
| `webapp/src/components/tei/InlineClozeBuilder.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 6484 |
| `webapp/src/components/tei/MultiSourceTabViewer.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 6673 |
| `webapp/src/components/tei/RedPenProofreader.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 5830 |
| `webapp/src/components/tei/StylusInkingLayer.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 3704 |
| `webapp/src/components/tei/WritingWorkbench.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 5262 |
| `webapp/src/data/commercialMasterData.json` | JSON 파싱 | 2440859 |
| `webapp/src/index.css` | 텍스트 읽기·패턴/구조 검사 | 2093 |
| `webapp/src/main.tsx` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 346 |
| `webapp/src/services/firebaseDbService.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 11687 |
| `webapp/src/store/useCoursewareStore.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 18199 |
| `webapp/src/types/courseware.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 10280 |
| `webapp/src/utils/ttsEngine.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 1212 |
| `webapp/src/vite-env.d.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 38 |
| `webapp/tailwind.config.js` | 텍스트 읽기·패턴/구조 검사 | 1518 |
| `webapp/tsconfig.json` | JSON 파싱 | 511 |
| `webapp/vite.config.ts` | 텍스트 읽기·패턴/구조 검사 / TypeScript 프로젝트 빌드 대상(전체 빌드 실패) | 284 |
| `초1_6학년_문해력_하위기능_및_목표위계_마스터.json` | JSON 파싱 | 1007127 |
| `초1_6학년_장르별_문해력_하위기능_및_목표위계_마스터.xlsx` | xlsx_zip_ok / 셀별 내용·수식·레이아웃은 미검수 | 995216 |

## 이번에 추가한 진단 스크립트

| 경로 | 기본 검사 | 크기(bytes) |
| --- | --- | ---: |
| `scripts/audit_commercial_readiness.py` | Python AST 구문 검사 | 11786 |
| `scripts/audit_runtime_contracts.mjs` | 목록·해시 확인 / 실제 실행으로 480회 초기 렌더 검사 | 4189 |

## 해석과 재실행

- JSON 파싱 통과는 화면 계약이나 정답의 타당성 통과를 뜻하지 않는다.
- Python 구문 통과는 생성기를 실행했다는 뜻이 아니다. 원본을 덮어쓰는 생성기는 실행하지 않았다.
- TypeScript 파일은 같은 프로젝트 빌드에서 검사했다. 파일별 단독 빌드 합격 판정은 하지 않았다.
- Markdown·HTML·CSS의 기본 검사와 핵심 문서·코드에 대한 수동 검토는 구분한다.
- 후속 문서 두 개와 이 색인은 초기 169개 스냅샷 이후 작성되었다. 진단 스크립트를 다시 실행하면 그 시점의 파일 수가 바뀔 수 있다.
