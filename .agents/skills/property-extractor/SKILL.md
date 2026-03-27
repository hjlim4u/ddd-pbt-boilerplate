---
name: property-extractor
description: >
  새 제약사항이 추가되었을 때 Property 후보를 추출.
  도메인 문서와 카탈로그만을 근거로 삼는다. 구현 코드는 읽지 않는다.
---

## 절차

1. 대상 제약사항 ID를 `from src.catalog import CATALOG`로 찾아 `Constraint` 객체와 `applies_to` 모델을 확인한다.
2. 각 적용 모델의 서사를 `CATALOG.doc_files_for_constraint(id)`와 `docs/index.md` Scope Registry를 기준으로 읽는다.
3. 기존 Property는 카탈로그의 `PROPERTIES` 또는 `CATALOG.properties`에서 확인한다.
4. 구현 코드(`src/domain/`)는 읽지 않는다.

5. 각 새 제약사항에 대해 4문항 판단:
   Q1. "모든 X에 대해 Y가 성립"으로 표현 가능한가?
   Q2. 입력 공간이 넓은가?
   Q3. shrink된 반례가 유의미한가?
   Q4. 구현과 독립된 검증 방법이 있는가?
   → 3개+ Yes = PBT / 0~1 Yes = TDD / 2 Yes = Mixed

6. Property 후보를 카탈로그 객체 형태로 생성:
   ```python
   Property(
       id="P-XXX",           # 기존 최대 번호 + 1
       name="...",
       source=("INV-XX",),   # 제약사항 ID
       models=("E-XX",),     # 적용 모델 ID
       category="invariant", # invariant / round-trip / idempotence / metamorphic / policy
       description="...",
       test_mode="PBT",      # PBT / TDD / Mixed
       test_file="tests/properties/test_xxx.py",
   )
   ```

## 주의

- 구현 코드를 보면 "현재 버그를 정당화하는 테스트"가 나올 수 있다.
  반드시 `docs/<scope>/` 서사와 `src/catalog/` 카탈로그만을 근거로 삼아라.
- 생성된 Property 후보는 스코프 카탈로그와 관련 개념의 `doc_file`에 함께 기록한다.
