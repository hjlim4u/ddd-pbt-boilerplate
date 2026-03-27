---
name: impact-tracer
description: >
  특정 모델이나 제약사항을 변경할 때 영향 범위를 추적.
  "E-01을 수정하면 어떤 제약사항, property, 테스트, 코드가 영향받는가?"를 파악할 때 사용.
---

## 절차

1. 변경 대상 ID를 받는다 (예: E-01, INV-03, P-005, EV-02).
2. `src/catalog/__init__.py`의 `CATALOG.impact_of(target_id)`를 호출하여 영향 범위를 즉시 조회한다:
   ```python
   from src.catalog import CATALOG
   impact = CATALOG.impact_of("INV-03")
   # → {"models": (...), "constraints": (...), "properties": (...), "events": (...)}
   ```
3. 반환된 각 ID에 대해 스코프 카탈로그 심볼과 `DomainModel.doc_file`을 직접 읽어 문서 경로를 확인한다. 제약사항과 Property는 각 `DomainModel.constraints` / `DomainModel.properties` 역탐색으로 연결 문서를 모은다.
4. `src/domain/`에서는 관련 심볼 정의·참조를 우선 찾고, 필요하면 docstring의 ID 문자열을 보조 검색한다.
5. `tests/`에서도 관련 테스트 심볼과 참조를 우선 찾고, 필요하면 ID 문자열을 보조 검색한다.

## 반환 형식

- 직접 영향 (catalog에서 이 ID를 참조하는 항목들):
  - 영향받는 모델: [ID + 이름 + doc_file]
  - 영향받는 제약사항: [ID + 설명 + doc_files]
  - 영향받는 Property: [ID + test_file]
  - 영향받는 이벤트: [ID + 이름]
- 구현 영향:
  - 수정이 필요한 src/domain/ 파일 목록
  - 수정이 필요한 tests/ 파일 목록
- 문서 영향:
  - 서사 업데이트가 필요한 docs/ 파일 목록

## 주의

- 영향 조회의 1차 정본은 `src/catalog/`다. 카탈로그와 구현 탐색은 LSP 심볼/참조 탐색을 우선 사용한다.
- 텍스트 검색은 markdown 서사 발췌나 docstring의 raw ID 확인이 필요할 때만 보조적으로 사용한다.
