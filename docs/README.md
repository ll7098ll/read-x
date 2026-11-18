# Read X 문서 목차

정리 기준: 2026-11-18. 현재 안내 → 세부 구현 → 날짜별 기록 순서로 읽습니다. 날짜별 문서는 당시 상태를 보존하며 최신 코드의 완료 증거로 일괄 해석하지 않습니다.

[프로젝트 README](../README.md) · [최신 현황](PROJECT_STATUS.md) · [실행 방법](DEVELOPMENT.md) · [공개 계획](GITHUB_PUBLICATION_PLAN_2026-11-18.md)

## 문서 우선순위

현재 실행은 개발 환경·구조·현황, 디자인은 Read X v3를 따릅니다. 과거 PRD의 Firebase·PWA·WASM·예상 출시 일정은 계획 자료입니다. `output/`의 교재·리포트는 검토용 산출물이며 실제 학생 자료를 추가하지 않습니다. 제외한 작업 로그·배포 압축본 경로는 본문에서 코드로 표기합니다.

## 현재 안내

- [GitHub 공개 검증 기록](PUBLICATION_VERIFICATION_2026-11-18.md)

- [변경 기록](<../CHANGELOG.md>) — `CHANGELOG.md`
- [CI_AND_UI_UX_THEME_KIT_MASTER](<../CI_AND_UI_UX_THEME_KIT_MASTER.md>) — `CI_AND_UI_UX_THEME_KIT_MASTER.md`
- [기여 안내](<../CONTRIBUTING.md>) — `CONTRIBUTING.md`
- [DEVELOPMENT_PLAN_READX](<../DEVELOPMENT_PLAN_READX.md>) — `DEVELOPMENT_PLAN_READX.md`
- [Google_Stitch_UIUX_Design_Prompt_Guide](<../Google_Stitch_UIUX_Design_Prompt_Guide.md>) — `Google_Stitch_UIUX_Design_Prompt_Guide.md`
- [PRD_2022개정_교과개념_설명문_문해력_코스웨어](<../PRD_2022개정_교과개념_설명문_문해력_코스웨어.md>) — `PRD_2022개정_교과개념_설명문_문해력_코스웨어.md`
- [PRD_문해력_코스웨어_상용화_마스터](<../PRD_문해력_코스웨어_상용화_마스터.md>) — `PRD_문해력_코스웨어_상용화_마스터.md`
- [Read X · 리드엑스](<../README.md>) — `README.md`
- [코드·문서·학습 자료 이용 범위](<../RIGHTS.md>) — `RIGHTS.md`
- [보안 안내](<../SECURITY.md>) — `SECURITY.md`
- [UI_UX_COMPONENT_DEVELOPMENT_SPEC](<../UI_UX_COMPONENT_DEVELOPMENT_SPEC.md>) — `UI_UX_COMPONENT_DEVELOPMENT_SPEC.md`
- [다양한 주제 콘텐츠 제작분 03](<../data/content_authoring/batch_03/README.md>) — `data/content_authoring/batch_03/README.md`
- [국어 전체 은행 확장 1차](<../data/content_authoring/expansion_v2_01/README.md>) — `data/content_authoring/expansion_v2_01/README.md`
- [사실 기반 설명글 확장 2차](<../data/content_authoring/expansion_v2_02/README.md>) — `data/content_authoring/expansion_v2_02/README.md`
- [실제 쓰기 수행 확장 3차](<../data/content_authoring/expansion_v2_03/README.md>) — `data/content_authoring/expansion_v2_03/README.md`
- [문학 읽기 확장 4차](<../data/content_authoring/expansion_v2_04/README.md>) — `data/content_authoring/expansion_v2_04/README.md`
- [언어·문장 확장 원고 05](<../data/content_authoring/expansion_v2_05/README.md>) — `data/content_authoring/expansion_v2_05/README.md`
- [실제 시각 자료를 포함한 매체 읽기 확장 06](<../data/content_authoring/expansion_v2_06/README.md>) — `data/content_authoring/expansion_v2_06/README.md`
- [듣고 직접 말하는 확장 원고 07](<../data/content_authoring/expansion_v2_07/README.md>) — `data/content_authoring/expansion_v2_07/README.md`
- [사실과 조건을 대조하는 설명글 확장 08](<../data/content_authoring/expansion_v2_08/README.md>) — `data/content_authoring/expansion_v2_08/README.md`
- [쓰기 기능 확장 09차 · 실제 집필 및 검토 기록](<../data/content_authoring/expansion_v2_09/README.md>) — `data/content_authoring/expansion_v2_09/README.md`
- [국어 여섯 단계 대표 제작 진행 기록](<../data/content_authoring/pilot_v2/README.md>) — `data/content_authoring/pilot_v2/README.md`
- [현재 시스템 구조](<ARCHITECTURE.md>) — `docs/ARCHITECTURE.md`
- [데이터와 콘텐츠 안내](<CONTENT.md>) — `docs/CONTENT.md`
- [리드엑스 콘텐츠 생성과 검수 규칙](<CONTENT_AUTHORING_RULES.md>) — `docs/CONTENT_AUTHORING_RULES.md`
- [배포와 운영 설정](<DEPLOYMENT.md>) — `docs/DEPLOYMENT.md`
- [개발 환경과 검증](<DEVELOPMENT.md>) — `docs/DEVELOPMENT.md`
- [GitHub 공개 및 문서 정비 계획](<GITHUB_PUBLICATION_PLAN_2026-11-18.md>) — `docs/GITHUB_PUBLICATION_PLAN_2026-11-18.md`
- [프로젝트 현황](<PROJECT_STATUS.md>) — `docs/PROJECT_STATUS.md`
- [Read X — 브랜드 CI · UI/UX 테마 킷 v3](<READ_X_BRAND_UI_UX_KIT_V3.md>) — `docs/READ_X_BRAND_UI_UX_KIT_V3.md`
- [Read X UI/UX 컴포넌트 · 화면 명세 v3](<READ_X_COMPONENT_SPEC_V3.md>) — `docs/READ_X_COMPONENT_SPEC_V3.md`
- [백업·삭제 원장·격리 복원 운영 절차](<RECOVERY_OPERATIONS_2026-11-18.md>) — `docs/RECOVERY_OPERATIONS_2026-11-18.md`

## 운영 구현 이력

- [실제 로그인과 평가 운영 첫 개발 묶음](<PRODUCTION_BATCH_01_2026-11-14.md>) — `docs/PRODUCTION_BATCH_01_2026-11-14.md`
- [계정 기반 읽기 수업과 교사 검토 연결](<PRODUCTION_BATCH_02_2026-11-14.md>) — `docs/PRODUCTION_BATCH_02_2026-11-14.md`
- [실제 학원 운영과 계정 복구](<PRODUCTION_BATCH_03_2026-11-14.md>) — `docs/PRODUCTION_BATCH_03_2026-11-14.md`
- [공통 운영 홈 실제 기록 리포트와 개인정보 운영 기준](<PRODUCTION_BATCH_04_2026-11-14.md>) — `docs/PRODUCTION_BATCH_04_2026-11-14.md`
- [다섯 번째 개발 묶음: 보호자 확인·동의와 이용 제어](<PRODUCTION_BATCH_05_2026-11-14.md>) — `docs/PRODUCTION_BATCH_05_2026-11-14.md`
- [여섯 번째 개발 묶음: 기기 초안 보호와 로그아웃](<PRODUCTION_BATCH_06_2026-11-14.md>) — `docs/PRODUCTION_BATCH_06_2026-11-14.md`
- [일곱 번째 개발 묶음 — 교사·운영자 추가 인증과 안전한 초기 등록](<PRODUCTION_BATCH_07_2026-11-15.md>) — `docs/PRODUCTION_BATCH_07_2026-11-15.md`
- [여덟 번째 개발 묶음 — 개인정보 접속·파일 전달 기록](<PRODUCTION_BATCH_08_2026-11-17.md>) — `docs/PRODUCTION_BATCH_08_2026-11-17.md`
- [아홉 번째 개발 묶음 — 개인정보 권리 요청과 검토 사본](<PRODUCTION_BATCH_09_2026-11-17.md>) — `docs/PRODUCTION_BATCH_09_2026-11-17.md`
- [열 번째 개발 묶음 — 일반 서비스 처리정지와 해제](<PRODUCTION_BATCH_10_2026-11-17.md>) — `docs/PRODUCTION_BATCH_10_2026-11-17.md`
- [열한 번째 개발 묶음 — 운영 자료 삭제와 별도 보존](<PRODUCTION_BATCH_11_2026-11-18.md>) — `docs/PRODUCTION_BATCH_11_2026-11-18.md`
- [열두 번째 개발 묶음 — 삭제 원장·암호화 백업·격리 복원](<PRODUCTION_BATCH_12_2026-11-18.md>) — `docs/PRODUCTION_BATCH_12_2026-11-18.md`
- [13차 구현: 접속기록 암호화 보관과 복원 병합](<PRODUCTION_BATCH_13_2026-11-18.md>) — `docs/PRODUCTION_BATCH_13_2026-11-18.md`
- [14차 구현: 만료 접속기록 보관본 제거와 복원 재사용 차단](<PRODUCTION_BATCH_14_2026-11-18.md>) — `docs/PRODUCTION_BATCH_14_2026-11-18.md`

## 학습·평가·콘텐츠 설계와 구현

- [ReadX-Ray 학원과 공부방용 제품 개발 계획](<ACADEMY_PRODUCT_ROADMAP_2026-10-14.md>) — `docs/ACADEMY_PRODUCT_ROADMAP_2026-10-14.md`
- [초1~6 학년별 진단·배치·4주 학습·성취 확인](<ALL_GRADE_LEARNING_IMPLEMENTATION_2026-11-17.md>) — `docs/ALL_GRADE_LEARNING_IMPLEMENTATION_2026-11-17.md`
- [초1~6 진단·성취 확인 자료 편집 검수](<ASSESSMENT_EDITORIAL_REVIEW_2026-11-17.md>) — `docs/ASSESSMENT_EDITORIAL_REVIEW_2026-11-17.md`
- [승인된 파일럿 보정의 실제 진단·배치·자료 선정 적용](<CALIBRATION_APPLICATION_2026-11-18.md>) — `docs/CALIBRATION_APPLICATION_2026-11-18.md`
- [교사 검수·수업 파일럿·문항 난도 보정](<CLASSROOM_PILOT_IMPLEMENTATION_2026-11-18.md>) — `docs/CLASSROOM_PILOT_IMPLEMENTATION_2026-11-18.md`
- [ReadX-Ray 학원용 제품 상용화 점검](<COMMERCIAL_READINESS_AUDIT_2026-10-14.md>) — `docs/COMMERCIAL_READINESS_AUDIT_2026-10-14.md`
- [교과 지문 2차 확장 — 2026-10-14](<CONTENT_EXPANSION_BATCH_02_2026-10-14.md>) — `docs/CONTENT_EXPANSION_BATCH_02_2026-10-14.md`
- [리드엑스 실제 학습 콘텐츠 제작 계획](<CONTENT_PRODUCTION_PLAN_2026-11-14.md>) — `docs/CONTENT_PRODUCTION_PLAN_2026-11-14.md`
- [학년·학기별 교과 개념 원장과 지문 1차 집필](<CURRICULUM_CONTENT_INVENTORY_2026-10-14.md>) — `docs/CURRICULUM_CONTENT_INVENTORY_2026-10-14.md`
- [초등 수능형 모의고사와 학생 대시보드 개발 계획](<ELEMENTARY_MOCK_EXAM_AND_DASHBOARD_PLAN_2026-10-15.md>) — `docs/ELEMENTARY_MOCK_EXAM_AND_DASHBOARD_PLAN_2026-10-15.md`
- [초3~4 4주 학습·성취 확인·다음 단계 이동](<FOUR_WEEK_COURSE_IMPLEMENTATION_2026-11-15.md>) — `docs/FOUR_WEEK_COURSE_IMPLEMENTATION_2026-11-15.md`
- [초5 1회차 모의고사 구현 및 실행 안내](<G5_MOCK_EXAM_01_IMPLEMENTATION_2026-10-24.md>) — `docs/G5_MOCK_EXAM_01_IMPLEMENTATION_2026-10-24.md`
- [세부목표·사고 과정·교과 지문 설계](<GOAL_PROCESS_CONTENT_STRATEGY.md>) — `docs/GOAL_PROCESS_CONTENT_STRATEGY.md`
- [초1부터 초6까지 수능형 모의고사와 세 역할 화면 구현 계획](<GRADE_MOCK_EXAM_FULL_PRODUCT_PLAN_2026-10-24.md>) — `docs/GRADE_MOCK_EXAM_FULL_PRODUCT_PLAN_2026-10-24.md`
- [학원·공부방 제품 1차 기반 구현](<IMPLEMENTATION_01_2026-10-14.md>) — `docs/IMPLEMENTATION_01_2026-10-14.md`
- [학년 내 국어 학습 단계와 대규모 콘텐츠 제작 계획](<KOREAN_CONTENT_ARCHITECTURE_V2_2026-11-14.md>) — `docs/KOREAN_CONTENT_ARCHITECTURE_V2_2026-11-14.md`
- [Read X 레벨 테스트·배치·학습 전 과정 설계](<PLACEMENT_AND_LEARNING_COURSE_DESIGN_2026-11-14.md>) — `docs/PLACEMENT_AND_LEARNING_COURSE_DESIGN_2026-11-14.md`
- [초3~4 시작 진단 → 코스 배치 → 첫 학습 구현](<PLACEMENT_JOURNEY_IMPLEMENTATION_2026-11-15.md>) — `docs/PLACEMENT_JOURNEY_IMPLEMENTATION_2026-11-15.md`
- [학원 실사용을 위한 개인정보 법률 보안 운영 계획](<PRIVACY_SECURITY_OPERATIONS_PLAN_2026-11-14.md>) — `docs/PRIVACY_SECURITY_OPERATIONS_PLAN_2026-11-14.md`
- [리드엑스 실제 학원 운영 전환 계획](<PRODUCTION_IMPLEMENTATION_PLAN_2026-11-14.md>) — `docs/PRODUCTION_IMPLEMENTATION_PLAN_2026-11-14.md`
- [지문·문항 품질 개선 계획과 구현 기준](<READING_QUALITY_REVISION_PLAN_2026-10-14.md>) — `docs/READING_QUALITY_REVISION_PLAN_2026-10-14.md`
- [ReadX 통합 현황과 다음 개발 순서](<READX_INTEGRATION_AND_RELEASE_2026-10-14.md>) — `docs/READX_INTEGRATION_AND_RELEASE_2026-10-14.md`
- [ReadX 사고 과정 수업 1차 개편 기록](<READX_LEARNING_EXPERIENCE_IMPLEMENTATION_2026-10-14.md>) — `docs/READX_LEARNING_EXPERIENCE_IMPLEMENTATION_2026-10-14.md`
- [ReadX 학습 철학을 담는 UI·UX 설계 계획](<READX_LEARNING_EXPERIENCE_PLAN_2026-10-14.md>) — `docs/READX_LEARNING_EXPERIENCE_PLAN_2026-10-14.md`
- [사이트 반영 기록](<SITE_RELEASE_2026-11-14.md>) — `docs/SITE_RELEASE_2026-11-14.md`
- [초등 고학년 미니 모의고사와 학생 대시보드 구현](<STUDENT_MINI_EXAM_IMPLEMENTATION_2026-10-15.md>) — `docs/STUDENT_MINI_EXAM_IMPLEMENTATION_2026-10-15.md`
- [ReadX 사고구술 중심 UI와 학습 기록 연결 구현](<THINKING_EXPERIENCE_IMPLEMENTATION_2026-10-16.md>) — `docs/THINKING_EXPERIENCE_IMPLEMENTATION_2026-10-16.md`
- [ReadX 사고구술과 어노테이션 학습 경험 상세 설계](<THINK_ALOUD_ANNOTATION_EXPERIENCE_SPEC_2026-10-15.md>) — `docs/THINK_ALOUD_ANNOTATION_EXPERIENCE_SPEC_2026-10-15.md`

## 브랜드·UI 설계와 구현

- [ReadX Reading Garden UI 업데이트](<READING_GARDEN_UI_UPDATE_2026-11-14.md>) — `docs/READING_GARDEN_UI_UPDATE_2026-11-14.md`
- [ReadX 디자인 시스템 v2 — 구현 및 검증 기록](<READX_DESIGN_SYSTEM_V2.md>) — `docs/READX_DESIGN_SYSTEM_V2.md`
- [ReadX editorial UI revision — 2026-11-14](<READX_EDITORIAL_UI_UPDATE_2026-11-14.md>) — `docs/READX_EDITORIAL_UI_UPDATE_2026-11-14.md`
- [ReadX 실사용 화면 디자인 통합](<READX_PRODUCT_UI_UPDATE_2026-11-14.md>) — `docs/READX_PRODUCT_UI_UPDATE_2026-11-14.md`
- [ReadX 전체 UI UX와 사고구술 학습 경험 개선 계획](<READ_LEARNEY_UIUX_REPORT_PLAN_2026-10-15.md>) — `docs/READ_LEARNEY_UIUX_REPORT_PLAN_2026-10-15.md`
- [Read X 브랜드 · UI/UX 킷 v3 적용 기록](<READ_X_V3_IMPLEMENTATION.md>) — `docs/READ_X_V3_IMPLEMENTATION.md`
- [ReadX-Ray 전체 UI UX 개선 및 기능 확장 실행 계획](<UI_UX_IMPROVEMENT_AND_FEATURE_PLAN_2026-10-14.md>) — `docs/UI_UX_IMPROVEMENT_AND_FEATURE_PLAN_2026-10-14.md`

## 초기 PRD·과거 설계

- [CI_AND_UI_UX_THEME_KIT_MASTER 문서 안내](<CI_AND_UI_UX_THEME_KIT_MASTER.md>) — `docs/CI_AND_UI_UX_THEME_KIT_MASTER.md`
- [🚀 [ReadX-Ray Pro] 문해력 코스웨어 상용화 실제 개발 계획서 (Software Development Plan)](<DEVELOPMENT_PLAN_READX.md>) — `docs/DEVELOPMENT_PLAN_READX.md`
- [🎨 [UI/UX Design Spec & Stitch Prompt Guide] 초등 수능형 설명문 문해력 코스웨어 「ReadX (리드엑스)」 24대 마이크로 화면 완전판 명세서 (v6.0)](<Google_Stitch_UIUX_Design_Prompt_Guide.md>) — `docs/Google_Stitch_UIUX_Design_Prompt_Guide.md`
- [📘 [Master Commercial PRD & Software Architecture Spec] 2022 개정 전교과 설명문 수능형 문해력 코스웨어 「ReadX (리드엑스)」 완전판 명세서 (v6.0 Ultimate Edition)](<PRD_2022개정_교과개념_설명문_문해력_코스웨어.md>) — `docs/PRD_2022개정_교과개념_설명문_문해력_코스웨어.md`
- [📋 [Master PRD] 초등 수능형 설명문 적응형 코스웨어 「ReadX (리드엑스)」 상용화 공학 명세서 (v1.0)](<PRD_문해력_코스웨어_상용화_마스터.md>) — `docs/PRD_문해력_코스웨어_상용화_마스터.md`
- [UI_UX_COMPONENT_DEVELOPMENT_SPEC 문서 안내](<UI_UX_COMPONENT_DEVELOPMENT_SPEC.md>) — `docs/UI_UX_COMPONENT_DEVELOPMENT_SPEC.md`
- [💎 리드엑스레이(ReadX-Ray) Pro — 공식 CI 및 UI/UX 테마 킷 마스터 규격서 (v1.0)](<archive/CI_AND_UI_UX_THEME_KIT_MASTER_PRE_V3.md>) — `docs/archive/CI_AND_UI_UX_THEME_KIT_MASTER_PRE_V3.md`
- [🎨 [ReadX-Ray Pro] 단계별 UI/UX 컴포넌트 개발 상세 명세서 & 차세대 혁신 제안 (Component Spec & Advanced Features)](<archive/UI_UX_COMPONENT_DEVELOPMENT_SPEC_PRE_V3.md>) — `docs/archive/UI_UX_COMPONENT_DEVELOPMENT_SPEC_PRE_V3.md`

## 연구 자료

- [초등 수능형 모의고사와 학생 성적 분석 조사](<../research/ELEMENTARY_MOCK_EXAM_AND_DASHBOARD_RESEARCH_2026-10-15.md>) — `research/ELEMENTARY_MOCK_EXAM_AND_DASHBOARD_RESEARCH_2026-10-15.md`
- [국어 콘텐츠의 학년 내 단계와 대규모 문항 은행 설계 조사](<../research/KOREAN_LITERACY_PROGRESSION_RESEARCH_2026-11-14.md>) — `research/KOREAN_LITERACY_PROGRESSION_RESEARCH_2026-11-14.md`
- [READ와 러니의 학습 화면과 리포트 조사](<../research/READ_LEARNEY_BENCHMARK_2026-10-15.md>) — `research/READ_LEARNEY_BENCHMARK_2026-10-15.md`
- [[Track 1 조사 보고서] 초등 1~6학년 학년별·교과별 핵심 개념 매트릭스 및 설명문 16대 하위기능·6대 구조 96차시 매핑 설계](<../research/courseware_track1_curriculum_concepts_96slots.md>) — `research/courseware_track1_curriculum_concepts_96slots.md`
- [courseware_track2_passage_complexity_vocab_standards](<../research/courseware_track2_passage_complexity_vocab_standards.md>) — `research/courseware_track2_passage_complexity_vocab_standards.md`
- [[Track 3 심층 조사 보고서] 수능(CSAT) 스타일 비문학(독서)·작문 문항의 초등 1~6학년 스케일링 설계 및 코스웨어 아키텍처](<../research/courseware_track3_csat_question_and_courseware_schema.md>) — `research/courseware_track3_csat_question_and_courseware_schema.md`
- [[Track 4 종합 심층 조사 보고서] 상용 출시 수준(Production-Ready) 문해력 코스웨어 고도화를 위한 글로벌 벤치마킹 · 서비스 여정 · 차세대 TEI 문항 · 대시보드 UI/UX 마스터 리서치](<../research/courseware_track4_commercial_product_ux_tei_dashboard_research.md>) — `research/courseware_track4_commercial_product_ux_tei_dashboard_research.md`

## 교과서 참조 문서

- [📊 01. 초1~6학년 종적·횡적 문해력 위계(516단위) 및 6학년 86개 마스터 위계 해설서](<../textbook_reference/docs/01_기획과_철학/01_교육과정_설계_철학_및_나선형_위계.md>) — `textbook_reference/docs/01_기획과_철학/01_교육과정_설계_철학_및_나선형_위계.md`
- [[Track 2 심층 조사 보고서] 질문(Questioning) + 사고구술(Think-Aloud) 기반 읽기·쓰기 사고과정 프로토콜](<../textbook_reference/docs/01_기획과_철학/02_점진적_책임이양(GRR)_및_사고구술_이론.md>) — `textbook_reference/docs/01_기획과_철학/02_점진적_책임이양(GRR)_및_사고구술_이론.md`
- [🏆 초등학교 6학년 문해력 교과서 (5대 장르·70차시) 텍스트 선정 조사 종합 보고서](<../textbook_reference/docs/02_텍스트_선정_및_원문_검증/01_5대장르_텍스트_선정_종합_보고서.md>) — `textbook_reference/docs/02_텍스트_선정_및_원문_검증/01_5대장르_텍스트_선정_종합_보고서.md`
- [📘 [Track A 심층 조사 및 원문 검증 보고서] 시(Poetry) & 수필(Essay) 후보 작품 전수 비교 및 선정안](<../textbook_reference/docs/02_텍스트_선정_및_원문_검증/02_문학_트랙A_시_수필_원문_검증.md>) — `textbook_reference/docs/02_텍스트_선정_및_원문_검증/02_문학_트랙A_시_수필_원문_검증.md`
- [📗 [Track B 조사 보고서] 이야기(Narrative) 중·단편 창작동화 후보 발굴 및 차시 분절·원문 검증서](<../textbook_reference/docs/02_텍스트_선정_및_원문_검증/03_문학_트랙B_이야기_꼴뚜기_검증.md>) — `textbook_reference/docs/02_텍스트_선정_및_원문_검증/03_문학_트랙B_이야기_꼴뚜기_검증.md`
- [[Track C: 설명문(Expository)] 기출판 진정성 텍스트 발굴 및 구조·단서 검증 보고서](<../textbook_reference/docs/02_텍스트_선정_및_원문_검증/04_비문학_트랙C_설명문_과학환경_검증.md>) — `textbook_reference/docs/02_텍스트_선정_및_원문_검증/04_비문학_트랙C_설명문_과학환경_검증.md`
- [📓 [Track D 심층 조사 및 원문 검증 보고서]](<../textbook_reference/docs/02_텍스트_선정_및_원문_검증/05_비문학_트랙D_논설문_시사통계_검증.md>) — `textbook_reference/docs/02_텍스트_선정_및_원문_검증/05_비문학_트랙D_논설문_시사통계_검증.md`
- [🎨 초등 6학년 문해력 교과서 「읽고 생각하고 표현하고」](<../textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/01_다각도_레이아웃_옵션_비교_및_마스터플랜.md>) — `textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/01_다각도_레이아웃_옵션_비교_및_마스터플랜.md`
- [[Track 3 심층 조사 보고서] 최적화된 교과서 레이아웃, 편집 체제 및 시각적 스캐폴딩 구성요소](<../textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/02_읽기_쓰기_1대1_수평전이_및_2층첨삭노트.md>) — `textbook_reference/docs/03_교과서_구성_및_레이아웃_디자인/02_읽기_쓰기_1대1_수평전이_및_2층첨삭노트.md`
- [👩‍🏫 04. 교사용 지도서(Teacher's Guide) 6대 모듈 활용 매뉴얼 및 40분 수업 운영 모델](<../textbook_reference/docs/04_교사용_지도서_설계_컨셉/01_교사용_지도서_6대_모듈_및_수업_운영_모델.md>) — `textbook_reference/docs/04_교사용_지도서_설계_컨셉/01_교사용_지도서_6대_모듈_및_수업_운영_모델.md`
- [🤖 05. 멀티 서브에이전트(Subagent) 병렬 집필·조판 엔지니어링 아키텍처](<../textbook_reference/docs/05_AI_에이전트_개발_과정/01_멀티_서브에이전트_병렬_협업_파이프라인.md>) — `textbook_reference/docs/05_AI_에이전트_개발_과정/01_멀티_서브에이전트_병렬_협업_파이프라인.md`

## 브랜드 전달본

- [Read X UI/UX 컴포넌트 · 화면 명세 v3](<../output/read-x-v3/read-x-components.md>) — `output/read-x-v3/read-x-components.md`
- [Read X — 브랜드 CI · UI/UX 테마 킷 v3](<../output/read-x-v3/read-x-guidelines.md>) — `output/read-x-v3/read-x-guidelines.md`
- [Read X UI/UX 컴포넌트 · 화면 명세 v3](<../webapp/public/brand/read-x-components.md>) — `webapp/public/brand/read-x-components.md`
- [Read X — 브랜드 CI · UI/UX 테마 킷 v3](<../webapp/public/brand/read-x-guidelines.md>) — `webapp/public/brand/read-x-guidelines.md`

## 기타 문서

- [다양한 주제 읽기와 쓰기 문제집](<../output/content-batch-03/전체_콘텐츠와_해설.md>) — `output/content-batch-03/전체_콘텐츠와_해설.md`
