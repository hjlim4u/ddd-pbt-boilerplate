---
name: domain-scout
description: >
  도메인 컨텍스트를 파악할 때 사용.
  카탈로그(src/catalog/)에서 구조적 관계를 조회하고,
  docs/<scope>/에서 개념별 서사를 읽어 요약을 반환한다.
  새 작업을 시작하거나, 특정 모델/제약사항의 맥락을 이해해야 할 때 호출.
---

## 절차

1. `from src.catalog import CATALOG`를 기준으로 대상 ID(E-01, INV-03, P-005 등)에 해당하는 객체를 찾는다.
2. 찾은 객체의 필드에서 관련 ID 목록을 수집한다:
   - DomainModel: `.constraints`, `.properties`, `.events`, `.depends_on`, `.doc_file`
   - Constraint: `.applies_to`, `.properties`, `CATALOG.doc_files_for_constraint(id)`
   - Property: `.source`, `.models`, `.test_file`, `CATALOG.doc_files_for_property(id)`
3. 문서 경로는 `docs/index.md`의 Scope Registry와 카탈로그의 `doc_file`을 우선 사용한다.
4. 필요한 `docs/<scope>/*.md`만 읽어 필드·불변 조건·정책·이벤트·Property 관점을 파악한다.
   - 여러 모델에 걸친 제약(POL-03 등)은 `CATALOG.doc_files_for_constraint(id)`로 여러 문서를 함께 읽는다.
5. 카탈로그의 `test_file` 필드로 테스트 파일 존재 여부를 확인한다.
6. `src/domain/`에서 관련 구현 코드가 있는지 확인한다.

## 반환 형식

- 관련 모델: [ID + 이름 + model_type + doc_file]
- 관련 제약사항: [ID + category + 한 줄 설명 + doc_files]
- 관련 Property: [ID + test_mode + test_file]
- 관련 테스트 파일: [파일 경로 목록 (존재 여부 포함)]
- 관련 소스 파일: [파일 경로 목록]
- 빈 곳: 제약사항은 있지만 테스트가 없는 항목 등

## 주의

- 구조적 관계(refs)는 반드시 `src/catalog/`의 Python 객체에서 읽어라. docs/는 서사 정본이다.
- 경로는 하드코딩하지 말고 `doc_file`과 Scope Registry를 따라가라.
- 유형별 단일 파일(models.md, constraints.md 등)은 사용하지 않는다. 개념별 `docs/<scope>/*.md`가 서사의 정본이다.
