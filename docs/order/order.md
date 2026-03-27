---
model_id: E-01
scope: @order
constraints: [INV-02, POL-01]
properties: [P-004]
events: [EV-01, EV-02]
depends_on: [V-01, V-02]
---

# Order [E-01]

고객이 결제를 완료한 구매 건을 나타내는 집합체(Aggregate Root)이다.
주문 생성·취소 행위를 책임지며, 상태 변화를 이벤트로 기록한다.

구조적 관계(제약사항·Property·이벤트 ID)는 `src/catalog/order.py`의 `ORDER` 객체를 본다.

## 필드

- id: str - UUID
- customer_id: str - 주문자 식별자
- order_lines: list[OrderLine] - 최소 1개의 항목을 가져야 한다
- created_at: datetime - 생성 시각
- pending_events: list[OrderCreated | OrderCancelled] - 아직 발행되지 않은 도메인 이벤트

## 불변 조건

유효한 Order는 항상 하나 이상의 OrderLine을 포함해야 한다.
빈 주문은 도메인에서 허용되지 않는다. "요청"이나 "장바구니"와 구별되는 지점이다.

## 비즈니스 규칙

주문이 성립하면 OrderCreated 이벤트가 발행되어 재고 배정 프로세스를 시작하는 신호가 된다.

주문이 취소되면 해당 주문에 묶인 모든 재고 배정이 해제되어야 한다.
이 규칙은 Batch 쪽 배정 상태와 함께 맞물려 동작한다 (POL-03).

## 도메인 이벤트

### OrderCreated [EV-01]

주문이 생성되었음을 나타낸다.
고객이 결제를 완료한 순간 발행되며, 재고 배정 프로세스를 시작하는 신호가 된다.

- 페이로드: order_id, customer_id, order_lines[], timestamp
- 트리거: 고객이 결제 완료 시
- 후속: 재고 배정 시작

### OrderCancelled [EV-02]

주문이 취소되었음을 나타낸다.
이 이벤트가 발행되면 해당 주문에 배정된 모든 재고가 해제되어야 한다.

- 페이로드: order_id, reason, timestamp
- 트리거: 고객 취소 또는 결제 실패
- 후속: 배정된 재고 해제

## Property-Based 검증 관점

유효한 Order는 항상 `len(order_lines) >= 1`이다.
Mixed 테스트 전략으로 불변식과 시나리오를 함께 다룬다.

## 관계

Order는 하나 이상의 OrderLine을 포함한다.
Money 등 다른 값 객체와의 연산은 주문 항목·가격 계산 맥락에서 이루어진다.
