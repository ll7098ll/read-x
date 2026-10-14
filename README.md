# 📚 문해력 코스웨어 프로젝트 (ReadX-Ray Pro)

> **2022 개정 교육과정 초등 1~6학년 문해력 교과서 기반 적응형 코스웨어**  
> 본 프로젝트는 '문해력 교과서'의 탄탄한 516개 하위기능 목표 위계와 단원별 지문·성취기준을 기반으로 분리·구축된 **독립 코스웨어 프로젝트**입니다.

---

## 🌟 프로젝트 개요

- **명칭**: ReadX-Ray Pro (초등 1~6학년 맞춤형 적응형 문해력 코스웨어)
- **기반 자산**: 2022 개정 초등 국어 교육과정 및 '문해력 교과서' 전 학년 목표 위계 매트릭스
- **핵심 엔진**:
  - **132개 슬롯 아이템 뱅크**: 96개 교과개념 설명문 슬롯 + 36개 공통 언어·사고 기초 슬롯 (A1~A6)
  - **7대 TEI (Technology-Enhanced Item) 문항 시스템**: HotText 단서 발굴, EBSR 2단계 근거 연동, 사고구술 빈칸(Cloze), 6대 설명구조 그래픽 조직자 등
  - **3단계 점진적 스캐폴딩(Progressive Hinting)** 및 맞춤형 처방 클리닉
  - **React 18 + Vite + Tailwind CSS** 기반 현대적 웹앱 클라이언트
  - **Google Cloud / Firebase Firestore** 연동 지원 스키마

---

## 📁 디렉터리 구조

```text
문해력 코스웨어 프로젝트/
├── webapp/                             # [프론트엔드] React 18 + Vite 코스웨어 웹 애플리케이션
│   ├── src/
│   │   ├── components/                 # 코스웨어 학습 UI (진단, 처방, 실전, 리포트 등)
│   │   ├── data/
│   │   │   └── commercialMasterData.json # 132슬롯 마스터 데이터 번들
│   │   ├── services/                   # Firebase / API 서비스
│   │   ├── store/                      # Zustand 상태 관리
│   │   └── types/                      # TypeScript 타입 정의
│   ├── package.json
│   └── vite.config.ts
│
├── data/                               # [데이터] 코스웨어 데이터셋 및 아이템 뱅크
│   ├── item_bank/                      # g1 ~ g6 각 학년별 22개 슬롯 (총 132슬롯 JSON)
│   ├── firestore_seed_132_db.json      # Firestore 시드용 통합 데이터
│   ├── expository_courseware_hierarchy.json # 설명문 및 공통 기초 위계 정의
│   └── unified_courseware_master_data.json
│
├── scripts/                            # [파이프라인] 데이터 생성, 컴파일 및 QA 검증 스크립트
│   ├── compile_and_validate_132_db.py  # 132슬롯 마스터 병합 및 심리측정/무결성 자동 QA
│   ├── gen_g1.py ~ gen_g6.py           # 학년별 아이템 생성기
│   ├── build_commercial_dataset.py     # 상용화 데이터셋 빌더
│   └── build_mega_master_whitepaper_prd.py
│
├── docs/                               # [기획/스펙] 코스웨어 PRD 및 UI/UX 디자인 가이드
│   ├── PRD_문해력_코스웨어_상용화_마스터.md
│   ├── PRD_2022개정_교과개념_설명문_문해력_코스웨어.md
│   ├── UI_UX_COMPONENT_DEVELOPMENT_SPEC.md
│   ├── Google_Stitch_UIUX_Design_Prompt_Guide.md
│   ├── DEVELOPMENT_PLAN_READX.md
│   └── CI_AND_UI_UX_THEME_KIT_MASTER.md
│
├── textbook_reference/                 # [원천 자산] 기반이 된 문해력 교과서 레퍼런스
│   ├── 초1_6학년_문해력_하위기능_및_목표위계_마스터.json  # 516개 목표 위계 마스터
│   ├── 초1_6학년_장르별_문해력_하위기능_및_목표위계_마스터.xlsx
│   ├── new_goals_matrix.json
│   ├── 문해력 교과서 백서.html
│   ├── data/
│   │   ├── units/                      # 1~6학년 교과서 단원 원문 및 지문
│   │   └── g6_master_hierarchy.json
│   └── docs/                           # 교과서 철학, 텍스트 선정, 레이아웃 기획 문서
│
├── 초1_6학년_문해력_하위기능_및_목표위계_마스터.json       # 루트 바로가기 참조
├── 초1_6학년_장르별_문해력_하위기능_및_목표위계_마스터.xlsx   # 루트 바로가기 참조
├── new_goals_matrix.json               # 루트 바로가기 참조
├── courseware_master_whitepaper_prd.html # 코스웨어 종합 백서 인터랙티브 리포트
├── firestore.rules                     # Firebase 보안 규칙
└── README.md
```

---

## 🚀 빠른 시작 (Quick Start)

### 1. 코스웨어 웹앱 실행
```bash
cd webapp
npm install      # (필요시)
npm run dev      # 로컬 개발 서버 실행 (http://localhost:5173)
```

### 2. 코스웨어 빌드
```bash
cd webapp
npm run build    # 단일 HTML 번들 또는 정적 파일 빌드
```

### 3. 아이템 뱅크 데이터 컴파일 및 자동 QA 검증
코스웨어 132개 슬롯의 문항 무결성, 난이도 공식, 선지 길이, 단서 텍스트 일치 여부를 자동 검증합니다.
```bash
python scripts/compile_and_validate_132_db.py
```
검증 통과 시 `webapp/src/data/commercialMasterData.json` 및 `data/firestore_seed_132_db.json`이 자동으로 최신화됩니다.

---

## 📌 문해력 교과서와의 연계 및 확장
- 본 코스웨어는 **문해력 교과서**의 단원 지문과 6개 학년 위계 매트릭스를 모태로 제작되었습니다.
- 교과서의 원문과 단원별 세부 성취기준은 `textbook_reference/` 폴더에서 상시 확인할 수 있으며, 향후 타 장르(논설문, 서사문 등)로의 코스웨어 확장 시에도 동일한 원천 데이터를 활용할 수 있습니다.
