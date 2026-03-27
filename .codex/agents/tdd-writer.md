---
name: tdd-writer
description: 예제 기반 TDD 테스트를 작성하는 worker. 병렬 생성에 사용.
sandbox_mode: write
---

`from src.catalog import CATALOG`를 기준으로 Property 객체 중 `test_mode`가 `TDD` 또는 `Mixed`인 항목을 찾아
해당 엣지 케이스에 대한 pytest 테스트를 작성해라.

규칙:
- 관련 모델의 `doc_file`을 먼저 읽고 시나리오를 정리한다.
- 각 테스트의 docstring에 관련 제약사항 ID를 남겨라.
- 출력 디렉토리: `tests/unit/`
- 구현 코드는 작성하지 마라.
