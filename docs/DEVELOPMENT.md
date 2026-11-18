# 개발 환경과 검증

기준일: 2026-11-18. 앱 명령은 `webapp/`에서 실행한다.

## 요구 환경과 설치

Node.js **24.14.0** (`node:sqlite` 사용), npm, 데이터 검사용 Python 3.12. 루트 `.nvmrc`와 `webapp/.node-version`에 Node 버전을 고정한다. Firebase 계정·외부 API 키 없이 기본 로컬 기능을 실행할 수 있다.

```bash
git clone https://github.com/ll7098ll/read-x.git
cd read-x/webapp
npm ci
npm run dev
```

기본 개발 주소는 `http://localhost:5173`이다. 사용 중이면 Vite가 표시한 포트를 따른다. 기본 모드는 Vite API 플러그인과 로컬 계정 서버를 연결하고 `.exam-data/`에 개발 자료를 만든다. 가상 자료만 사용한다.

## 빌드와 계정 서버

```bash
npm run build
npm run serve:exam
```

`http://127.0.0.1:5186/#/exams`에서 개발용 첫 교사·반을 등록한다. 교사/운영자는 인증앱 MFA를 완료해야 학생 기록에 접근한다. 학생/보호자 연결→배정→학생 응시→교사 검토·공개 순서다. 읽기 수업은 `#/teacher/classes`, `#/student/classes`, `#/parent/classes`에서 이용한다.

`npm run preview`는 정적 파일 확인용이다. 계정 API 검증은 `serve:exam`을 사용한다. 운영 시작은 [배포 안내](DEPLOYMENT.md)를 따른다.

## 정적 가상 체험판

PowerShell:

```powershell
$env:VITE_EXAM_MODE = 'demo'
npm run build
npm run preview
Remove-Item Env:VITE_EXAM_MODE
```

POSIX 셸은 `VITE_EXAM_MODE=demo npm run build`를 사용한다. 기본 모드로 돌아올 때 환경 변수를 해제하고 재빌드한다. 체험판은 실제 계정 DB와 연결하지 않는다.

`webapp/.env.example`은 Vite 설정 예시다. **Node 서버는 `.env`를 자동으로 읽지 않는다.** 서버 변수는 셸 또는 비밀 관리 도구로 주입한다. `VITE_` 변수에는 비밀을 넣지 않는다.

## 검사

| 위치 | 명령 | 범위 |
| --- | --- | --- |
| 루트 | `python -X utf8 scripts/check_repository.py` | 공개 대상·비밀 패턴·Markdown 상대 링크 |
| webapp | `npm run build` | 콘텐츠 준비→TypeScript→UI/도메인→서버→Vite→경계 검사 |
| webapp | `npm test` | UI·학습 도메인 검사 |
| webapp | `npm run test:exam` | 계정·학습·보안·복구 서버 검사 |
| 루트 | `python -X utf8 -m unittest discover -s tests -v` | 교육과정·원문 근거·매체 전달 검사 |
| webapp | `npm run check:readiness` | 운영 증거. 현재 `ready:false`, 종료 코드 1이 기대 상태 |

빌드는 생성 JSON/공개 학습 자료를 갱신할 수 있다. `git diff`를 확인한다. [콘텐츠 안내](CONTENT.md)에 원고와 생성 경로가 있다.

## 문제 해결

- `node:sqlite` 오류: `node --version`과 고정 버전을 확인한다.
- `npm ci` 실패: 패키지 레지스트리 연결을 확인한다. 잠금 파일을 임의 재생성하지 않는다.
- 자료실 HTML 누락: `outputs/` 빌드 입력도 복제했는지 확인한다.
- 키·원장 오류: 임의 키나 잠금 파일 삭제로 우회하지 않는다. 원본을 보전하고 [복구 절차](RECOVERY_OPERATIONS_2026-11-18.md)를 확인한다.
- 자동 검사는 실제 브라우저·단말·인쇄 확인을 대신하지 않는다.
