# 백업·삭제 원장·격리 복원 운영 절차

2026년 11월 18일. 개발 검증용 절차이며 실제 학원 명의·담당자·국내 저장소·권한·암호화 볼륨·키 보관소·법률 검토·복구 훈련을 완료한 문서는 아니다. 실제 개인정보를 공개 Sites나 개발 자료에 반입하지 않는다. 가상 자료의 분리 환경에서 먼저 연습한다.

## 준비

프로젝트 `webapp`에서 명령을 실행한다. 개발 검증은 Node.js v24.14.0에서 수행했으며 운영 런타임도 검증한 버전으로 고정하고 별도 확인한다. 운영 서버와 테스트/빌드는 환경 변수·키·DB·저장소를 분리한다. 운영 환경 변수를 가진 프로세스에서 개발 검사를 그대로 실행하지 않는다.

`READX_MFA_KEYS`, `READX_AUDIT_KEYS`, `READX_DATA_KEYS`, `READX_RECOVERY_KEYS`, `READX_BACKUP_KEYS`는 각각 독립적인 `{activeId,keys}` 구성이며 키 값은 32바이트 Base64다. 실제 값은 비밀 관리 체계에서 주입한다. 코드·명령 인수·문서·일반 로그·백업 파일과 같은 위치에 저장하지 않는다. 각 파일의 이전 키 ID를 검증·복호화할 수 있을 때까지 필요한 이전 키를 보존하고 교체·유실 복구를 연습한다. 키를 성급하게 제거하면 이전 원장·사본·백업을 사용할 수 없다.

운영 DB, 별도 삭제 원장, 암호화 백업, 기준점 파일, 암복호화 단계 디렉터리에 대한 실제 국내 보관·ACL·암호화 볼륨·관리자 접근을 확인한다. 원장과 기준점을 다른 폴더에 두는 것만으로 별도 장치·변경 방지·외부 복제가 검증되지 않는다. 백업 파일명·문서 번호에 실명·연락처·주민번호를 넣지 않는다.

다음은 경로와 검토 번호의 예시다. 실제 경로는 운영 계획에 따라 준비하며 이 문서가 해당 폴더를 만들거나 실제 배포한 것은 아니다.

```powershell
$academyDb = 'C:\ReadXPrivate\db\academy.sqlite'
$erasureJournal = 'D:\ReadXPrivate\recovery\erasure.recovery.ndjson'
$evidenceDirectory = 'D:\ReadXPrivate\anchors\review-2026-11-18'
$reviewReference = 'OPS-REVIEW-001'
```

## 첫 기준점 또는 이전 삭제 이력 이관

기존 서버·구버전 작성자를 중지하고 원본과 키를 별도로 보전한다. 새로운 첫 운영자는 기존 `server/bootstrap-owner.mjs`의 비공개 stdin 절차를 따른다. 이전 계정이 있는 DB에 새 운영자를 임의 추가하지 않는다.

이전 삭제 이력이 있으면 원본 삭제 요청·대상·실제 제거·별도 보존 자료를 사람이 확인한다. 초기 기준점이 아직 없는 경우에만 명시적으로 다음을 사용한다. 운영 키 5종은 먼저 주입되어 있어야 한다. 기준점 보관 폴더는 미리 준비하고 기존 파일이 없는 새 폴더를 선택한다.

```powershell
node server/recovery-maintenance.mjs --db $academyDb --journal $erasureJournal --action adopt --review-reference $reviewReference --confirmed --initialize-anchor-baseline --checkpoint-dir $evidenceDirectory
```

`--initialize-anchor-baseline`은 기존 원장·기준점을 초기화하는 옵션이 아니다. 기존 검증 상태나 외부 원장이 있으면 이를 없애서 새로 만들지 않는다. 이관은 과거 원장을 복원한 증거와 구분하여 현재 시각·문서 번호로 남긴다. 원본 근거나 필요한 사본이 없으면 진행하지 못한다.

명령이 만든 `recovery-anchor.json`, `audit-anchor.json`을 실제 변경 방지·분리 보관 체계에 보전한다. 운영 시작에는 `READX_RECOVERY_JOURNAL`, `READX_RECOVERY_ANCHOR`, `READX_AUDIT_ANCHOR`를 설정한다. 파일은 이전 증거 위에 덮어쓰지 않고 검토한 새 버전으로 관리한다. 이미 기준점이 있는 운영 검증에는 `--anchor`와 `--audit-anchor`로 현재 보관한 기준점을 제공한다.

## 현재 상태 확인과 기준점 저장

```powershell
node server/recovery-maintenance.mjs --db $academyDb --journal $erasureJournal --action verify --review-reference $reviewReference --confirmed --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR
node server/recovery-maintenance.mjs --db $academyDb --journal $erasureJournal --action checkpoint --review-reference $reviewReference --confirmed --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR --checkpoint-dir $evidenceDirectory
```

체크포인트 저장마다 새 보관 폴더를 사용한다. 알려진 기준점 이후의 모든 이력 보전을 이 명령 한 번으로 증명하지 않는다. 실제 보관·점검·갱신 주기를 정하고 결과를 보호한다. 서버와 파일을 함께 과거로 되돌리는 공격·사고에는 분리 보관한 기준점과 외부 증거가 필요하다.

## 백업 생성

미리 검토한 보존 종료 시각을 ISO8601로 정한다. 고정된 예시 일수를 법정 기간으로 사용하지 않는다. 새 파일 경로를 선택한다.

```powershell
$backupFile = 'D:\ReadXPrivate\backups\reviewed-snapshot.readxbackup'
$backupExpiry = '검토하여 정한 ISO8601 보존 종료 시각'
node server/encrypted-backup.mjs --action backup --db $academyDb --journal $erasureJournal --out $backupFile --expires-at $backupExpiry --review-reference $reviewReference --confirmed
```

성공 결과의 `backupId`, DB 식별자, 전체 파일 `sha256`, 보존 종료일과 원장·접속기록 기준점을 보호된 목록에 기록한다. 파일과 키를 다른 위치에 보전한다. 기존 파일을 덮어쓰지 않는다. 업무 기록·별도 보존 사본·키 변경 뒤에 어떤 최신 백업이 필요한지 확인한다. 로컬 파일 생성만으로 외부 복제·국내 보관·보관소 불변성·정기 실행·복구 훈련을 완료하지 않는다.

작업 중에는 API가 일시 중지될 수 있다. 실제 수업 시간·복구 목표와 용량을 기준으로 운영 일정을 정한다. 일시 평문 SQLite 단계 파일은 비공개 암호화 볼륨에 있어야 한다. 정상 및 처리 가능한 오류 경로의 정리를 검사했지만 프로세스 강제 종료·전원 차단 뒤의 잔여 파일 처리는 실제 절차·장치 검증이 필요하다.

## 새 경로로 격리 복원

기존 서버를 중지하고 복원할 파일의 보호된 목록·해시·키 버전과 최신 별도 원장을 확인한다. 현재 운영 DB 위에 파일을 복사하지 않는다. 원본 백업·원장·기준점·키를 먼저 보전한다.

```powershell
$restoredDb = 'C:\ReadXPrivate\restore\verified-new.sqlite'
$expectedBackupHash = '보호된 목록에서 확인한 64자리 sha256'
node server/encrypted-backup.mjs --action restore --archive $backupFile --target $restoredDb --expected-sha256 $expectedBackupHash --journal $erasureJournal --review-reference $reviewReference --confirmed --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR
```

해시·GCM 인증·이미지 무결성·DB/기준점·삭제 재적용·최신 별도 보존 자료·SQLite 정리가 모두 통과해야 격리가 풀린다. 만료 또는 파기 준비/결과가 기록된 같은 백업 ID는 재사용하지 않는다. 별도 보존 사본이 없거나 오래된 버전이면 최신 자료가 있는 검증 백업을 찾는다. 삭제 원장에서 사본 원문을 만들어 낼 수 없다.

접속기록 기준점보다 오래된 백업이면 누락한 이후 접속기록의 보전도 검증해야 한다. 현재 도구에는 외부 접속기록 아카이브 자동 병합 기능이 없다. 실패한 격리를 잠금 파일 삭제로 우회하지 않는다. `ok` 결과도 전체 운영 준비 승인이 아니며 실제 RPO/RTO·권한·키·로그·국내 보관·현장 검증을 따로 확인한다.

직접 준비한 격리 DB에 재처리하거나 SQLite 정리만 검토할 때는 다음을 사용한다. 원본을 덮어쓰는 복원 명령이 아니다.

```powershell
node server/recovery-maintenance.mjs --db $restoredDb --journal $erasureJournal --action replay --review-reference $reviewReference --confirmed --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR
node server/recovery-maintenance.mjs --db $academyDb --journal $erasureJournal --action compact --review-reference $reviewReference --confirmed --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR
```

WAL 읽기 연결이 정리를 막으면 완료로 처리하지 않는다. 이 절차의 파일 제거·WAL 비움은 장치·SSD·스냅샷·다른 사본의 물리적 파기 증명과 구분한다.

## 복원 뒤 계정과 보호자 재확인

원본·복원 DB를 동시에 서비스하지 않는다. 새 DB에는 이전 세션·초안 키·복구 코드·MFA 복구 코드와 보호자 이용 권한을 그대로 재사용하지 않는다.

신뢰된 서버 담당자가 실제 운영자의 본인·현재 권한을 확인한 뒤 첫 원장 복구를 진행한다.

```powershell
node server/recover-owner.mjs --db $restoredDb --username 기존원장아이디 --restore-identity-and-role-verified --restore-reference 'IDENTITY-RESTORE-001'
```

일회용 코드를 보호된 경로로 본인에게 전달하고 15분 안에 이전과 다른 새 비밀번호를 설정한다. 코드·새 비밀번호를 로그나 문서에 남기지 않는다. 등록된 인증앱이 있던 계정은 추가 본인 확인 뒤 MFA 복구를 진행한다.

```powershell
node server/recover-mfa.mjs --db $restoredDb --username 기존원장아이디 --verified-identity --reference 'MFA-RESTORE-001' --reason '실제 본인·현재 운영 권한 확인'
```

MFA 복구 발급은 기존 로그인을 회수한다. 새 비밀번호로 다시 로그인한 후 서버 복구 코드를 입력하고 새 인증앱을 등록한다. 이후 원장이 다른 계정의 실제 본인·재직/담당 범위·이용 자격·보호자 관계를 확인하여 복구 코드를 발급한다. 법정대리인 확인·동의도 다시 진행한다. 자동 연결이나 체크박스만으로 법률 검토가 끝났다고 보지 않는다.

## 만료 백업 파일 제거

보존 종료·보존 예외·다른 사본·키와 실제 처리를 먼저 검토한다. 파일과 보호된 목록의 해시를 확인한 후 실행한다.

```powershell
node server/encrypted-backup.mjs --action purge --db $academyDb --journal $erasureJournal --archive $backupFile --expected-sha256 $expectedBackupHash --review-reference $reviewReference --confirmed
```

검증한 준비 기록이 있어야 이미 없어진 파일의 제거 결과를 재확인할 수 있다. 결과는 해당 파일 경로의 부재와 기록을 뜻한다. 다른 복제본·매체의 삭제, 볼륨 키 폐기·물리적 파기까지 완료했다고 표시하지 않는다. 모든 보관 위치를 실제 원장으로 관리하고 별도 증거를 남긴다.

## 장애 판단

- `RECOVERY_SYNC_REQUIRED`: DB 변경은 확정되었을 수 있다. 같은 작업을 새 식별자로 반복하지 말고 원본·접속기록·전달 대기 상태를 보전한 뒤 동기화와 요청 상태를 확인한다.
- `.restore.pending`: 필요한 검증이 끝나지 않았다. 서비스 시작을 강제로 우회하지 않는다.
- 잘린/누락 원장·틀린 키·불일치 기준점: 새 빈 원장이나 임의 키로 대체하지 않는다. 검증된 분리 보관 자료와 키를 복구한다.
- 잔여 잠금·단계 파일: 살아 있는 프로세스와 구버전 작성자, 작업 소유권·평문 잔여물을 먼저 확인한다. PID·파일 이름만 믿고 다른 프로세스나 사용자의 파일을 제거하지 않는다.

명령에 `--confirmed`와 문서 번호를 넣었다는 사실이 실제 사람·문서의 진위나 운영 적합성을 자동 증명하지 않는다. 운영 책임자 지정·교육·권한·사고 대응·복구 훈련과 23개 준비 통제의 실제 증거가 남아 있다.


## 13차 추가: 백업 이후 접속기록 보전과 병합

전체 DB 백업과 별도로 원래 접속기록 전체를 암호화해 보관한다. 주기·보관 종료일·예외·권한·외부 저장 위치·복구 허용 손실 시간은 실제 운영자가 결정하고 검토한다. 아래 날짜와 경로 변수는 실제 결정값으로 설정해야 한다. 자동 실행이나 업체 연결은 아직 구성하지 않았다.

```powershell
# 기존 프로젝트 DB/외부 비공개 디렉터리, 보호된 감사 기준점과 독립 키가 준비된 상태
$auditArchive = 'D:/ReadX-private/audit/새로운보관번호.readxaudit'
$auditExpires = '실제_검토한_미래_ISO8601_보존종료일'
$auditReceipt = node server/access-archive.mjs --db $academyDb --out $auditArchive --expires-at $auditExpires --review-reference $reviewReference --confirmed --audit-anchor $env:READX_AUDIT_ANCHOR | ConvertFrom-Json
```

성공 반환을 확인하고 보관본 자체, 반환의 `sha256`, `checkpoint`, `archiveId`, `expiresAt`, 실제 외부 저장·점검 결과를 별도의 보호 원장에 보관한다. 기준점과 해시를 파일 옆에만 두는 것으로 변경 방지를 보장하지 않는다. `checkpoint`를 보관본과 짝이 맞는 새 감사 기준점 파일로 보관한다. 브라우저의 기간별 JSON 내려받기는 복원용 전체 보관본을 대신하지 않는다. 보관본은 최소 메타데이터만 담아도 계정 식별자·접속지가 있으므로 개인정보로 관리한다.

복원에는 검증한 최신 보관본·별도 해시·짝이 맞는 감사 기준점 파일을 사용한다. 기존 복원 명령에 두 옵션을 추가한다.

```powershell
node server/encrypted-backup.mjs --action restore --archive $backupFile --target $restoredDb --expected-sha256 $expectedBackupHash --journal $erasureJournal --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR --access-archive $auditArchive --access-archive-sha256 $expectedAuditArchiveHash --review-reference $reviewReference --confirmed
# 이미 별도로 격리한 원본 SQLite 복원본을 검토하는 경우
node server/recovery-maintenance.mjs --action replay --db $restoredDb --journal $erasureJournal --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR --access-archive $auditArchive --access-archive-sha256 $expectedAuditArchiveHash --review-reference $reviewReference --confirmed
```

명령은 누락된 원래 기록만 추가하고 공통 앞부분이 다른 기록은 거부한다. 오래된/다른 DB/변조/만료/틀린 키/불일치 해시/최신 기준점 미충족은 격리를 유지한다. 보관본이 없다고 기준점을 과거 것으로 바꿔 우회하지 않는다. 병합 뒤에도 삭제 원장 재적용·필요한 법정 보존 사본 확인·계정/MFA/보호자 재확인을 모두 수행한다. 반환의 새 기준점도 보호된 원장에 추가한다.

운영 서버의 키·보관본은 공개 소스/웹 경로 밖에 두고 실제 OS 권한·암호화 저장소를 구성한다. 한 보관본의 직렬화 한도는 64 MiB다. 한도 전에 분할/장기 보관 구조를 검토해야 한다. 자동 보관·실시간 전송·만료 파일/다른 사본 파기·경보·전원 차단·현장 복구 훈련은 별도 미완료 작업이다. `expiresAt` 경과는 일반 복원 거부를 뜻하며 실제 파일 제거를 뜻하지 않는다.


## 14차 추가: 만료 접속기록 보관 파일 제거

보존 종료·보존 예외와 실제 파기 검토 문서, 모든 보관 위치, 대상 파일의 별도 해시를 확인한다. 운영 환경에는 기존 독립 `READX_BACKUP_KEYS`, `READX_AUDIT_KEYS`, `READX_RECOVERY_KEYS`와 DB 밖 삭제 원장이 필요하다. 명령을 실행할 서버 관리 권한도 실제로 제한해야 한다.

```powershell
node server/access-archive.mjs --action purge --db $academyDb --archive $auditArchive --expected-sha256 $expectedAuditArchiveHash --journal $erasureJournal --anchor $env:READX_RECOVERY_ANCHOR --audit-anchor $env:READX_AUDIT_ANCHOR --review-reference $reviewReference --confirmed --holds-cleared
```

`--holds-cleared`는 해당 사본에 유지해야 할 실제 보존 예외가 없는 것을 검토했다는 표시다. 법률 판단을 자동 수행하지 않는다. 보존 중인 파일, 틀린 해시·키·서명·다른 DB, 손상 원장·기준점은 거부한다. 준비 기록을 DB와 별도 삭제 원장에 먼저 확정한 뒤 파일을 제거한다. 원장 전달이 실패하면 같은 준비를 확인·동기화한 후 재시도하며 새 요청 식별자를 만들어 반복하지 않는다.

파일 제거 뒤 완료 기록에 장애가 나면 실제 파일은 없을 수 있다. 원본 DB·별도 원장·접속기록을 보전하고 같은 명령과 해시로 이어간다. 검증된 준비 기록 없이 파일이 없다는 사실만으로 제거 완료로 간주하지 않는다. 반환의 작업 ID·보관본 ID·검토 문서·기록과 실제 다른 사본의 처리 결과를 보호된 원장에 관리한다.

원장에 파기 준비/완료가 있는 보관본 ID는 격리 복원에서 재사용할 수 없다. 파일명을 바꾸거나 과거 기준 시각으로 되돌려 우회하지 않는다. 이미 완료한 경로의 재실행은 중복 완료를 만들지 않으며, 동일 파일이 다시 나타나면 별도 작업으로 제거한다. 이전 버전 복원 도구는 새 사건 종류를 처리하지 못할 수 있으므로 최신 검증 소스를 사용한다.

`fileAbsent:true`는 해당 일반 파일의 부재만 확인한다. `databaseAccessLogsPurged:false`, `otherCopiesDisposed:false`, `mediaSanitizationCertified:false`는 유지한다. 운영 DB 접속기록·다른 파일·백업·외부 사본·SSD 매체가 모두 파기됐다는 증명으로 사용하지 않는다. 이 명령은 자동 정기 실행·외부 저장소 연결·물리적 파기 인증을 구성하지 않는다.
