# 배포와 운영 설정

기준일: 2026-11-18. 소스 공개, 가상 정적 체험판, 실제 계정 서버 운영을 구분한다.

## 정적 체험판

[개발 환경](DEVELOPMENT.md)의 `VITE_EXAM_MODE=demo`로 빌드한 `webapp/dist/`만 정적 호스팅에 게시한다. DB·키·원장·백업은 넣지 않는다. GitHub Actions는 검사만 하며 서비스 자동 배포는 하지 않는다.

기존 Sites 이력은 [사이트 반영 기록](SITE_RELEASE_2026-11-14.md)에 있다. 이번 GitHub 공개는 해당 사이트를 재배포하지 않는다. 과거 사이트 버전을 최신 Git 커밋으로 간주하지 않는다.

## 계정 서버

로컬은 `npm run build` 후 `npm run serve:exam`이다. 운영은 분리 환경에서 검토 증거를 준비한 뒤 `npm run start:production`을 실행한다. 현재 23개 통제가 미완료이므로 운영 시작 차단이 기대 동작이다.

| 환경 변수 | 용도 |
| --- | --- |
| `READX_EXAM_DB` | 개발/테스트와 분리된 비공개 SQLite 절대 경로 |
| `READX_EXAM_HOST`, `READX_EXAM_PORT` | 기본 `127.0.0.1:5186` |
| `READX_PUBLIC_ORIGIN` | 운영 HTTPS 원점 |
| `READX_COOKIE_SECURE` | 운영 Secure 쿠키 `1` |
| `READX_READINESS_MANIFEST` | 담당자·검토 증거·번들 해시 명세 |
| `READX_MFA_KEYS` | 독립 MFA 암호화 키 |
| `READX_AUDIT_KEYS` | 독립 접속기록 검증 키 |
| `READX_DATA_KEYS` | 독립 권리 요청/사본 암호화 키 |
| `READX_RECOVERY_KEYS` | 독립 삭제·복원 원장 검증 키 |
| `READX_BACKUP_KEYS` | 독립 백업/보관본 암호화 키 |
| `READX_RECOVERY_JOURNAL` | DB 밖 별도 삭제 원장 |
| `READX_RECOVERY_ANCHOR`, `READX_AUDIT_ANCHOR` | 분리 보관한 기준점 파일 |
| `READX_TRUSTED_PROXY_IPS` | 신뢰 프록시 IP. 형식은 `server/access-context.mjs` 확인 |

키 구성은 각각 `{activeId, keys}`이며 값은 32바이트 Base64다. 실제 키를 코드·GitHub·명령 인수·로그에 남기지 않는다. 서버는 `.env`를 자동으로 읽지 않으며 운영 시작 도구가 `READX_RUNTIME=production`을 설정한다.

첫 운영자는 `server/bootstrap-owner.mjs`의 비공개 stdin 절차를 사용한다. 이미 계정이 있는 DB에는 첫 운영자를 추가하지 않는다. [운영 전환 계획](PRODUCTION_IMPLEMENTATION_PLAN_2026-11-14.md)과 [복구 운영 절차](RECOVERY_OPERATIONS_2026-11-18.md)에 따라 MFA·관계 확인·키·보관·복구를 준비한다.

## 변경과 복원

검증한 커밋·잠금 파일·번들 해시·승인 증거를 함께 관리한다. DB·원장·키 버전과 호환되지 않는 과거 코드로 임의 되돌리지 않는다. 과거 DB 파일 복사 대신 새 경로로 격리 복원하고 삭제 이력·접속기록·계정/보호자 관계를 재확인한다.
