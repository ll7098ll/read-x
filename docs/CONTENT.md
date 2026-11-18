# 데이터와 콘텐츠 안내

기준일: 2026-11-18. 수량의 단위와 승인 상태를 함께 확인한다.

| 자산 | 기준 경로 | 의미 |
| --- | --- | --- |
| 목표 위계 | `textbook_reference/`와 루트 마스터 JSON | 기존 교과서 516개 하위기능 목표 기반 |
| 초기 슬롯 | `data/item_bank/`, `webapp/src/data/commercialMasterData.json` | 설명문 96 + 공통 기초 36 = 132슬롯 |
| 교육과정 | `data/curriculum_2022/` | 성취기준·교과 개념·배치 원장·개정 지문 |
| 개정 읽기 | `data/curriculum_2022/revisions/` | 144지문·432개 수준별 변형·720개 기본 연습 문항 |
| 확장 원고 | `data/content_authoring/` | 제작분별 원고·편집 이력·README |
| 교재 전달본 | `output/pilot-v2/`, `output/expansion-v2-*/` | 학생/교사 HTML·활동지·검증 결과 |
| 자료실 입력 | `outputs/01a138a0-43ff-7451-bf36-fcef9c677ac6/curriculum-library.html` | 앱 빌드가 읽는 HTML 입력 |

2026-11-18 공급 보고서 기준 국어 V2는 대표 제작분과 확장 01~10를 합해 **342자료·1,478문항·72기능**이다. 승인 자료 0, 학생 보정 자료 0이며 기존 batch03·계획·버전 이력은 이 합계에서 제외한다.

각 제작분 README와 `sets.json`이 원고 범위의 기준이다. 전체 공급 현황은 `output/content-bank-v2/readiness.json`과 [제작 계획](CONTENT_PRODUCTION_PLAN_2026-11-14.md)을 따른다. 원고 존재는 앱 연결·교사 승인·학생 보정 완료를 뜻하지 않는다.

## 편집 순서

1. [집필 규칙](CONTENT_AUTHORING_RULES.md)에 따라 목표·근거·해설·버전을 수정한다.
2. 수정 전 원고와 편집 기록을 보존한다. 생성 파일만 직접 수정하지 않는다.
3. 제작분 README의 명령으로 학생용·교사용 자료를 함께 갱신한다.
4. 구조·전달 검사와 원고/산출물 해시를 확인한다.
5. 교사 승인과 실제 학생 관찰은 자동 검사와 구분해 기록한다.

앱 읽기 자료는 `webapp`의 `npm run prepare:content`로 준비한다. 초기 132슬롯 재컴파일은 루트의 `python -X utf8 scripts/compile_and_validate_132_db.py`다. 최신 읽기·확장 원고 전체를 대신 생성하는 명령은 아니다.

연구 요약·출처는 `research/`에 보존한다. 외부 다운로드 PDF/HWP/ZIP 원본은 공개에서 제외한다. 기존 추출·인용·교과서 자산의 권리를 일괄 보장하지 않는다. [권리 안내](../RIGHTS.md)를 따른다.

가상 상황·수치·교사용 예시를 실제 기관·학생 실증 자료로 소개하지 않는다. 실제 학생 응답·이름·연락처·동의 증거를 저장소에 추가하지 않는다. 공개 평가 자료의 사전 노출 가능성을 고려한다.
