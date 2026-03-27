<!-- catalog-anchor: order_model_order -->
# Order

고객이 결제를 완료한 구매 건을 나타내는 집합체(Aggregate Root)이다.
주문 생성·취소 행위를 책임지며, 상태 변화를 이벤트로 기록한다.

구조적 관계는 `src/catalog/order/` 패키지와 문서의 `catalog-anchor` 주석을 통해 추적한다.

## 필드

<!-- catalog-anchor: order_model_order_field_id -->
- id: str - UUID

<!-- catalog-anchor: order_model_order_field_customer_id -->
- customer_id: str - 주문자 식별자

<!-- catalog-anchor: order_model_order_field_order_lines -->
- order_lines: list[OrderLine] - 최소 1개의 항목을 가져야 한다

<!-- catalog-anchor: order_model_order_field_created_at -->
- created_at: datetime - 생성 시각

<!-- catalog-anchor: order_model_order_field_pending_events -->
- pending_events: list[OrderCreated | OrderCancelled] - 아직 발행되지 않은 도메인 이벤트

## 불변 조건

<!-- catalog-anchor: order_constraint_order_requires_at_least_one_order_line -->
### 최소 한 개의 주문 항목이 필요하다

유효한 Order는 항상 하나 이상의 OrderLine을 포함해야 한다.
빈 주문은 도메인에서 허용되지 않는다. "요청"이나 "장바구니"와 구별되는 지점이다.

## 비즈니스 규칙

<!-- catalog-anchor: order_constraint_order_creation_publishes_order_created -->
### 주문 생성은 OrderCreated 이벤트를 발행한다

주문이 성립하면 OrderCreated 이벤트가 발행되어 재고 배정 프로세스를 시작하는 신호가 된다.

<!-- catalog-anchor: order_constraint_order_cancellation_releases_allocations -->
### 주문 취소는 모든 배정을 해제한다

주문이 취소되면 해당 주문에 묶인 모든 재고 배정이 해제되어야 한다.
이 규칙은 Batch 쪽 배정 상태와 함께 맞물려 동작한다.

## 도메인 이벤트

<!-- catalog-anchor: order_event_order_created -->
### OrderCreated

주문이 생성되었음을 나타낸다.
고객이 결제를 완료한 순간 발행되며, 재고 배정 프로세스를 시작하는 신호가 된다.

- 페이로드: order_id, customer_id, order_lines[], timestamp
- 트리거: 고객이 결제 완료 시
- 후속: 재고 배정 시작

<!-- catalog-anchor: order_event_order_cancelled -->
### OrderCancelled

주문이 취소되었음을 나타낸다.
이 이벤트가 발행되면 해당 주문에 배정된 모든 재고가 해제되어야 한다.

- 페이로드: order_id, reason, timestamp
- 트리거: 고객 취소 또는 결제 실패
- 후속: 배정된 재고 해제

## Property-Based 검증 관점

<!-- catalog-anchor: order_property_order_requires_at_least_one_order_line -->
### 최소 주문 항목 보장

유효한 Order는 항상 `len(order_lines) >= 1`이다.
Mixed 테스트 전략으로 불변식과 시나리오를 함께 다룬다.

## 관계

Order는 하나 이상의 OrderLine을 포함한다.
Money 등 다른 값 객체와의 연산은 주문 항목·가격 계산 맥락에서 이루어진다.