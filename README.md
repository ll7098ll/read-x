# Read X · 리드엑스

**읽는 방법을 배우는 초등 1~6학년 문해력 코스웨어.**

2022 개정 교육과정과 문해력 목표 위계를 바탕으로 글의 단서를 찾고, 관계를 설명하고, 자기 글로 표현하는 학습을 제공합니다. 학생의 진단·배치·수업·성취 확인과 교사 검토, 보호자 결과 공개, 학원 운영 기능을 함께 개발합니다.

**현재 기준: 2026-11-18, 운영 구현 14차까지의 소스와 최신 집필 자료.** 가상 자료로 개발·검증 중이며 실제 학생 개인정보 운영 준비 23개 통제는 미완료입니다. [현재 구현과 한계](docs/PROJECT_STATUS.md)를 먼저 확인하세요.

[문서 목차](docs/README.md) · [개발 환경](docs/DEVELOPMENT.md) · [시스템 구조](docs/ARCHITECTURE.md) · [콘텐츠 안내](docs/CONTENT.md) · [공개 계획](docs/GITHUB_PUBLICATION_PLAN_2026-11-18.md) · [변경 기록](CHANGELOG.md)

## 주요 기능

| 사용자 | 기능 |
| --- | --- |
| 학생 | 시작 진단, 읽기 수업, 근거 표시·사고구술·도해·쓰기, 4주 학습, 성취 확인, 모의고사 |
| 교사 | 문항·원고 검수, 반·학생 관리, 수업/시험 배정, 제출 검토·결과 공개, 파일럿 관찰과 보정 승인 |
| 보호자 | 확인·동의·연결 후 공개된 자녀 결과와 학습 과정 확인 |
| 원장 | 기관·반·계정·출석·상담, 권리 요청·보존/삭제·접속기록 검토 |

초1~6의 36개 코스·108개 학습 수업 연결·288개 성취 확인 학년판을 제공합니다. 저학년 교사 구두 관찰과 승인 보정 적용을 포함합니다. 이 수량은 교육 효과나 실제 학생 난도 검증 완료를 뜻하지 않습니다.

## 빠른 시작

Node.js **24.14.0**을 사용합니다. `node:sqlite` 기반 서버가 포함되어 있습니다.

```bash
git clone https://github.com/ll7098ll/read-x.git
cd read-x/webapp
npm ci
npm run dev
```

개발 주소는 `http://localhost:5173`입니다. 가상 자료로 첫 교사·반을 등록하고 인증앱 MFA를 설정합니다. Firebase 계정이나 외부 API 키는 필요하지 않습니다.

전체 빌드·검사 후 계정 서버를 실행하려면:

```bash
npm run build
npm run serve:exam
```

`http://127.0.0.1:5186/#/exams`에서 시작합니다. 계정 기반 읽기 수업 경로는 `#/teacher/classes`, `#/student/classes`, `#/parent/classes`입니다. 정적 가상 체험판 설정과 문제 해결은 [개발 환경](docs/DEVELOPMENT.md)에 있습니다.

## 기술과 파일 구성

React 18 · TypeScript 5.6 · Vite 6 · Tailwind CSS 3 · Zustand 5, Node.js HTTP · SQLite를 사용합니다. 디자인 기준은 [Read X v3](docs/READ_X_BRAND_UI_UX_KIT_V3.md)이며 `#/brand`에서 브랜드 킷을 확인할 수 있습니다.

초기 Firebase/Firestore 스키마와 내보내기 자료도 보존되어 있으나 기본 계정 서버는 SQLite입니다. 과거 PRD의 Firebase 동기화·Kiwi WASM·PWA·결제/문자 연동은 현재 완료 기능과 구분합니다.

```text
webapp/             React 앱, Node 서버, 공유 로직, 앱/서버 테스트
data/               교육과정·목표·아이템 뱅크·집필 원고
scripts/            콘텐츠 생성·편집·검수·저장소 검사
tests/              교육과정·매체 전달 Python 검사
docs/               현재 안내와 날짜별 설계·구현 이력
research/           연구 요약·출처·일부 원문 추출 자료
textbook_reference/ 기존 문해력 교과서 참조 자산
output/             교재·리포트·브랜드 전달본과 검증 결과
outputs/            교과 자료실 등 일부 앱 빌드 입력
```

## 콘텐츠와 검증

초기 132슬롯(설명문 96 + 공통 기초 36), 개정 교과 읽기 144지문(432개 수준별 변형·720개 기본 연습 문항), 국어 확장 원고는 서로 다른 자산입니다. 각 제작분의 원고·교사용 해설·학생용 자료·편집 이력은 [콘텐츠 안내](docs/CONTENT.md)와 [전체 Markdown 목차](docs/README.md)를 따릅니다.

루트에서 문서·공개 대상 검사와 교육과정 검사를 실행합니다.

```bash
python -m pip install -r requirements-test.txt
python -X utf8 scripts/check_repository.py
python -X utf8 -m unittest discover -s tests -v
```

`webapp`의 `npm run build`는 콘텐츠 준비, TypeScript, UI/도메인·서버 검사, 번들 빌드, 외부 자동 리소스·비공개 파일 경계 검사를 포함합니다. GitHub Actions에서도 핵심 검사를 실행합니다.

## 공개·운영 범위

시험 정답·채점 코드·교사용 해설은 공개 개발 자료입니다. 비공개 고부담 평가에는 별도 신규 문항과 비공개 공급 경로가 필요합니다. 로컬 DB·실제 키·복구 원장·백업·환경 파일·작업 로그·다운로드 원본은 공개 대상에서 제외합니다.

운영 준비 검사는 `webapp`의 `npm run check:readiness`입니다. 현재 `ready:false`가 기대 상태이며 실제 담당자·검토·보관/키 운영·현장 검증 증거 없이 통과시키지 않습니다. [배포](docs/DEPLOYMENT.md) · [복구 운영 절차](docs/RECOVERY_OPERATIONS_2026-11-18.md) · [보안](SECURITY.md)을 확인하세요.

포괄적인 오픈소스 재사용 라이선스는 아직 지정하지 않았습니다. 코드·학습 자료·외부 인용·폰트 등의 이용 범위는 [권리 안내](RIGHTS.md), 변경 제안은 [기여 안내](CONTRIBUTING.md)를 따릅니다.
