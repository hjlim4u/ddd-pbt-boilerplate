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
3. 반환된 각 ID에 대해 `CATALOG.get_*`, `CATALOG.doc_file_for_model()`, `CATALOG.doc_files_for_constraint()` 등으로 문서 경로를 확인한다.
4. `src/domain/`에서 이 ID가 docstring에 언급된 구현 코드를 찾는다.
5. `tests/`에서 이 ID가 docstring에 언급된 테스트를 찾는다.

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

- 영향 조회의 1차 정본은 `src/catalog/`다. docs/ grep은 경로와 구현 확인용 보조 단계다.
- 구현·테스트 코드에서 ID를 grep하는 것은 여전히 유효하다.
