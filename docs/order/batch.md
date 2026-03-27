---
model_id: E-02
scope: @order
constraints: [INV-01, INV-04, POL-02, POL-03]
properties: [P-003, P-005, P-006]
events: [EV-03]
depends_on: [V-02]
---

# Batch [E-02]

창고에 입고된 상품 묶음이다. reference(고유 식별자)로 구별되며,
OrderLine을 배정(allocate)하거나 해제(deallocate)하는 책임을 갖는다.
가용 수량은 `purchased_quantity - Σ(배정된 수량)`으로 계산된다.

구조적 관계는 `src/catalog/order.py`의 `BATCH` 객체를 본다.

## 필드

- reference: str - 배치 고유 식별자
- sku: str - 이 배치에 속한 상품 종류
- purchased_quantity: int - 입고된 총 수량 (> 0)
- eta: date | None - 입고 예정일. None이면 재고 보유 중(in-stock)
- allocations: set[OrderLine] - 현재 배정된 주문 항목 집합
- pending_events: list[OutOfStock] - 아직 발행되지 않은 도메인 이벤트

## 불변 조건

가용 수량은 절대 음수가 될 수 없다.
어떤 유효한 배정·해제 시퀀스를 거쳐도 이 불변식은 유지된다 (P-003, stateful PBT).

같은 OrderLine을 같은 Batch에 두 번 배정하면 두 번째 시도는 상태를 바꾸지 않는다.
재시도·중복 요청을 안전하게 처리할 수 있는 근거가 된다.

## 비즈니스 규칙

배정 시 Batch의 SKU와 OrderLine의 SKU가 반드시 일치해야 한다.
SKU가 맞지 않으면 배정할 수 없다 (P-006).

주문이 취소되면 해당 주문에 속한 OrderLine에 대한 모든 배정이 해제되어야 한다.
Batch 입장에서는 allocations에서 해당 라인이 제거되고 가용 수량이 복구된다.

## 도메인 이벤트

### OutOfStock [EV-03]

특정 SKU의 재고가 부족하여 배정에 실패했음을 나타낸다.
외부 시스템(알림, 재발주 등)이 이 이벤트를 구독하여 후속 처리를 담당한다.

- 페이로드: sku, requested_quantity, timestamp
- 트리거: 배정 시 가용 수량 부족
- 후속: 주문자에게 알림

## Property-Based 검증 관점

- 가용 수량 비음수, 배정 멱등성, SKU 일치는 PBT로 입력 공간을 넓게 커버한다.

## 관계

Batch는 배정된 OrderLine의 집합을 유지한다.
Order와는 주문 취소·배정 해제 시나리오에서 간접적으로 연결된다.
