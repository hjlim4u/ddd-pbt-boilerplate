# Domain Index

## Scope Registry

| Scope | 설명 | Catalog | Docs Dir |
|------|------|---------|----------|
| @order | 주문 생성, 라인 관리, 주문 취소 | `src/catalog/order.py` | `docs/order/` |

에이전트는 먼저 Scope Registry에서 스코프별 카탈로그와 문서 루트를 찾고,
그 다음 `src/catalog/`의 객체 메타데이터(`doc_file`)를 따라간다.

## 모델 요약

| ID | 이름 | 유형 | 영역 | 서사 파일 |
|----|------|------|------|-----------|
| E-01 | Order | Entity | @order | `docs/order/order.md` |
| E-02 | Batch | Entity | @order | `docs/order/batch.md` |
| V-01 | Money | VO | @order | `docs/order/money.md` |
| V-02 | OrderLine | VO | @order | `docs/order/orderline.md` |

모델 간 구조적 관계(제약사항, Property, 이벤트 참조)는 `src/catalog/`의 `CATALOG`와 스코프별 파일에서 관리한다.

## 제약사항 요약

| ID | 분류 | 설명 | 적용 모델 |
|----|------|------|-----------|
| INV-01 | invariant | Batch의 가용 수량은 절대 음수가 될 수 없다 | E-02 |
| INV-02 | invariant | Order는 최소 1개의 OrderLine을 가져야 한다 | E-01 |
| INV-03 | invariant | Money의 amount는 0 이상이어야 한다 | V-01 |
| INV-04 | invariant | 같은 OrderLine을 같은 Batch에 두 번 배정하면 두 번째는 무시된다 (멱등성) | E-02 |
| POL-01 | policy | Order 생성 시 OrderCreated 이벤트가 발행된다 | E-01 |
| POL-02 | policy | 배정 시 SKU가 일치해야 한다 | E-02 |
| POL-03 | policy | 주문 취소 시 모든 배정이 해제되어야 한다 | E-01, E-02 |
| FMT-01 | format | Currency는 ISO 4217 3자리 대문자 코드 | V-01 |
| FMT-02 | format | SKU는 대문자 영숫자 + 하이픈, 최대 20자 | V-02 |

## Property 요약

| ID | 이름 | 테스트 방식 | 근거 제약 | 테스트 파일 |
|----|------|-------------|-----------|-------------|
| P-001 | Money 직렬화 왕복 | PBT | INV-03, FMT-01 | `tests/properties/test_money_properties.py` |
| P-002 | Money 덧셈 교환법칙 | PBT | INV-03 | `tests/properties/test_money_properties.py` |
| P-003 | Batch 가용 수량 비음수 | PBT | INV-01 | `tests/properties/test_batch_properties.py` |
| P-004 | Order 최소 항목 | Mixed | INV-02 | `tests/unit/test_order.py` |
| P-005 | 배정 멱등성 | PBT | INV-04 | `tests/properties/test_batch_properties.py` |
| P-006 | SKU 일치 검증 | PBT | POL-02 | `tests/properties/test_batch_properties.py` |
| P-007 | OrderLine SKU 형식 검증 | PBT | FMT-02 | `tests/properties/test_orderline_properties.py` |

## 이벤트 요약

| ID | 이름 | 트리거 |
|----|------|--------|
| EV-01 | OrderCreated | 고객이 결제 완료 시 |
| EV-02 | OrderCancelled | 고객 취소 또는 결제 실패 |
| EV-03 | OutOfStock | 배정 시 가용 수량 부족 |

## 개념 서사

| 모델 ID | 서사 파일 |
|---------|-----------|
| E-01 | [docs/order/order.md](order/order.md) |
| E-02 | [docs/order/batch.md](order/batch.md) |
| V-01 | [docs/order/money.md](order/money.md) |
| V-02 | [docs/order/orderline.md](order/orderline.md) |

각 파일에는 해당 개념의 필드 설명, 불변 조건·정책 서사, 관련 이벤트·Property 관점이 한곳에 모여 있다.

## 기타

| 종류 | 경로 | 설명 |
|------|------|------|
| 용어집 | [glossary.md](glossary.md) | 도메인 용어 정의 |
| 카탈로그 엔트리포인트 | `src/catalog/__init__.py` | `CATALOG` 조회 API |
| 스코프 카탈로그 | `src/catalog/order.py` | `@order`의 구조화된 도메인 지식 |
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
