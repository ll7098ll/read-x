# 기여 안내

현재 실행·구조는 [개발 환경](docs/DEVELOPMENT.md)과 [시스템 구조](docs/ARCHITECTURE.md)를 따른다.

1. 작업 브랜치를 만들고 변경 목적과 범위를 정한다.
2. 코드와 문서를 함께 수정한다. 원고는 [집필 규칙](docs/CONTENT_AUTHORING_RULES.md)을 따른다.
3. 루트의 `python -X utf8 scripts/check_repository.py`, `webapp`의 `npm ci`와 `npm run build`를 실행한다.
4. 콘텐츠 변경 시 루트의 `python -X utf8 -m unittest discover -s tests -v`와 제작분 검증을 실행한다.
5. PR에 이유·동작 변화·실행한 검사·남은 한계를 적는다. 실행하지 않은 검사를 통과로 적지 않는다.

운영 준비 검사는 현재 `ready:false`가 기대 상태다. 실제 증거 없이 검토자·해시·상태를 채우지 않는다. 가상 자료만 사용하며 DB·키·학생 응답·동의 문서를 커밋하지 않는다.

날짜별 기획·구현 기록은 당시 상태를 보존한다. 현재 안내는 README와 `docs/PROJECT_STATUS.md`를 갱신한다. 새 Markdown은 `docs/README.md` 목차에 추가한다.

포괄적인 재사용 라이선스는 지정하지 않았다. [권리 안내](RIGHTS.md)를 먼저 확인한다.
