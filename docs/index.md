# Domain Index

## Scope Registry

| Scope | 설명 | Catalog | Docs Dir |
|------|------|---------|----------|
| `@<scope>` | 현재 프로젝트의 Bounded Context 설명 | `src/catalog/<scope>/` | `docs/<scope>/` |

에이전트는 먼저 Scope Registry에서 스코프별 카탈로그와 문서 루트를 찾고,
그 다음 `src/catalog/`의 객체 메타데이터(`doc_file`)를 따라간다.

이 파일은 특정 예시 도메인의 정본이 아니라, 현재 프로젝트의 스코프 지도를 적는 엔트리 문서다.
실제 프로젝트에서는 아래 섹션들을 현재 스코프의 ID와 경로로 채운다.

## 모델 요약

| ID | 이름 | 유형 | 영역 | 서사 파일 |
|----|------|------|------|-----------|
| `E-XX` / `V-XX` | 현재 모델명 | Entity / ValueObject | `@<scope>` | `docs/<scope>/<model>.md` |

모델 간 구조적 관계는 `src/catalog/`의 `CATALOG`와 스코프별 패키지에서 관리한다.

## 제약사항 요약

| ID | 분류 | 설명 | 적용 모델 |
|----|------|------|-----------|
| `INV-XX` / `POL-XX` / `FMT-XX` | invariant / policy / format | 현재 규칙 설명 | `E-XX`, `V-XX`, ... |

## Property 요약

| ID | 이름 | 테스트 방식 | 근거 제약 | 테스트 파일 |
|----|------|-------------|-----------|-------------|
| `P-XXX` | 현재 Property 이름 | PBT / TDD / Mixed | `INV-XX`, `POL-XX`, ... | `tests/...` |

## 이벤트 요약

| ID | 이름 | 트리거 |
|----|------|--------|
| `EV-XX` | 현재 이벤트 이름 | 현재 이벤트 발생 조건 |

## 개념 서사

| 모델 ID | 서사 파일 |
|---------|-----------|
| `E-XX` / `V-XX` | `docs/<scope>/<model>.md` |

각 파일에는 해당 개념의 필드 설명, 불변 조건·정책 서사, 관련 이벤트·Property 관점이 한곳에 모여 있다.

## 기타

| 종류 | 경로 | 설명 |
|------|------|------|
| 용어집 | [glossary.md](glossary.md) | 도메인 용어 정의 |
| 카탈로그 엔트리포인트 | `src/catalog/__init__.py` | `CATALOG` 메타데이터 + 영향 분석 API |
| 스코프 카탈로그 | `src/catalog/<scope>/` | 해당 스코프의 구조화된 도메인 지식 |
| 구현 | `src/domain/` | 도메인 구현 |
| PBT | `tests/properties/` | Property-Based Tests |
| TDD | `tests/unit/` | 예제 기반 단위 테스트 |

## 방법론

| 문서 | 설명 |
|------|------|
| [lightweight-ddd.md](methodology/lightweight-ddd.md) | DDD 적용 범위와 ID 체계 |
| [test-routing.md](methodology/test-routing.md) | PBT/TDD 라우팅 기준 |
| [orchestrator.md](methodology/orchestrator.md) | Orchestrator 자율 판단 기준 |
| [context-discovery.md](methodology/context-discovery.md) | 3-Layer 컨텍스트 아키텍처 |
| [sub-agent-dispatch.md](methodology/sub-agent-dispatch.md) | Sub-agent 호출 패턴 |
