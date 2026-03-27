---
name: doc-sync
description: >
  새 도메인 개념을 추가하거나 기존 개념을 변경할 때 문서와 카탈로그를 동기화.
  docs/ (서사)와 src/catalog/ (구조) 두 곳을 항상 함께 갱신한다.
---

## 이중 트랙 원칙

- `docs/<scope>/*.md` = 왜 이 개념이 존재하는가. 개념별 서사를 담는다.
- `src/catalog/` = 개념들이 어떻게 연결되는가. 구조적 관계와 문서 경로 메타데이터를 담는다.

모든 변경은 두 트랙을 동시에 갱신해야 한다.

---

## 새 모델 추가 시

- `docs/<scope>/<concept>.md`
  - frontmatter: `model_id`, `scope`, `constraints`, `properties`, `events`, `depends_on`
  - 본문: 필드, ID별 규칙 앵커, 이벤트, Property 관점
- `docs/glossary.md`
  - 새 용어 추가
- `src/catalog/<scope>.py`
  - `DomainModel(...)` 추가: `doc_file`, `constraints`, `properties`, `events`, `depends_on` 모두 명시
- `docs/index.md`
  - Scope Registry, 모델 요약, 서사 파일 요약 갱신

---

## 새 제약사항 추가 시

- 관련 `doc_file`
  - 불변 조건 / 비즈니스 규칙 / 형식 제약 섹션에 서사 추가
- `src/catalog/<scope>.py`
  - `Constraint(...)` 추가
  - 적용 모델의 `DomainModel.constraints`에 ID 추가

---

## 새 Property 추가 시

- 관련 `doc_file`
  - Property-Based 검증 관점 섹션에 서사 추가
- `src/catalog/<scope>.py`
  - `Property(...)` 추가
  - 연결된 `Constraint.properties` 및 `DomainModel.properties` 갱신

---

## 새 이벤트 추가 시

- 관련 `doc_file`
  - 도메인 이벤트 섹션에 서사 추가
- `src/catalog/<scope>.py`
  - `DomainEvent(...)` 추가
  - 관련 모델의 `events` 갱신
