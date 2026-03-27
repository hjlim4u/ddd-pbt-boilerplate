---
name: integrity-checker
description: >
  카탈로그·코드·테스트 간 정합성 검증.
  "빠뜨리지 마라" 원칙의 자동 검증 도구.
  작업 완료 시점이나 커밋 전에 사용.
---

## 검증 항목

1. **카탈로그 내부 정합성**: catalog 내 ID 교차 참조가 모두 유효한가?
   - DomainModel.constraints → Constraint 존재 여부
   - DomainModel.properties → Property 존재 여부
   - DomainModel.events → DomainEvent 존재 여부
   - DomainModel.depends_on → DomainModel 존재 여부
   - Property.source → Constraint 존재 여부
   - Property.source로부터 모델 역추적이 가능한지

2. **문서 경로 메타데이터 정합성**: `DomainModel.doc_file`이 실제로 존재하는가?

3. **Property test_file 존재**: 카탈로그의 `test_file` 경로가 실제로 존재하는가?

4. **제약사항 → 테스트 추적성**: 카탈로그의 모든 제약사항 ID가 최소 1개의 테스트 파일에서 참조되는가?

5. **코드 ID → 카탈로그 역방향**: 구현 코드 docstring에 사용된 ID가 모두 카탈로그에 정의되어 있는가?

6. **고아 Property**: 카탈로그에 정의되었지만 어떤 Constraint도 참조하지 않는 Property가 있는가?

7. **문서 frontmatter ↔ catalog 일치**: `model_id`, `scope`, `constraints`, `properties`, `events`, `depends_on`이 일치하는가?

## 실행 방법

### 스크립트 방식 (빠른 확인)

```bash
python3 .agents/skills/integrity-checker/scripts/check_sync.py
```

### 에이전트 방식 (깊은 확인)

`src/catalog/`, `src/domain/`, `tests/`, 각 모델의 `doc_file`을 읽고 위 항목을 확인한다.
Gemini CLI의 1M 컨텍스트가 이 작업에 적합하다.

## 출력 형식

```json
{
  "status": "PASS | ISSUES_FOUND | ERROR",
  "catalog_errors": ["order_model_order.constraints → INV-99 not defined in catalog"],
  "missing_tests": ["INV-XX — no test references this ID"],
  "orphan_ids": ["P-XXX — no constraint references it"],
  "unconstrained_code": ["INV-99 — in code but not in catalog"]
}
```
