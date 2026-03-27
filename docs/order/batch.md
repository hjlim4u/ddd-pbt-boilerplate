<!-- catalog-anchor: order_model_batch -->
# Batch

창고에 입고된 상품 묶음이다. reference(고유 식별자)로 구별되며,
OrderLine을 배정(allocate)하거나 해제(deallocate)하는 책임을 갖는다.
가용 수량은 `purchased_quantity - Σ(배정된 수량)`으로 계산된다.

구조적 관계는 `src/catalog/order/` 패키지와 문서의 `catalog-anchor` 주석을 통해 추적한다.

## 필드

<!-- catalog-anchor: order_model_batch_field_reference -->
- reference: str - 배치 고유 식별자

<!-- catalog-anchor: order_model_batch_field_sku -->
- sku: str - 이 배치에 속한 상품 종류

<!-- catalog-anchor: order_model_batch_field_purchased_quantity -->
- purchased_quantity: int - 입고된 총 수량 (> 0)

<!-- catalog-anchor: order_model_batch_field_eta -->
- eta: date | None - 입고 예정일. None이면 재고 보유 중(in-stock)

<!-- catalog-anchor: order_model_batch_field_allocations -->
- allocations: set[OrderLine] - 현재 배정된 주문 항목 집합

<!-- catalog-anchor: order_model_batch_field_pending_events -->
- pending_events: list[OutOfStock] - 아직 발행되지 않은 도메인 이벤트

## 불변 조건

<!-- catalog-anchor: order_constraint_batch_available_quantity_non_negative -->
### 가용 수량은 음수가 될 수 없다

가용 수량은 절대 음수가 될 수 없다.
어떤 유효한 배정·해제 시퀀스를 거쳐도 이 불변식은 유지된다.

<!-- catalog-anchor: order_constraint_batch_allocation_idempotent -->
### 같은 배정 요청은 한 번만 반영된다

같은 OrderLine을 같은 Batch에 두 번 배정하면 두 번째 시도는 상태를 바꾸지 않는다.
재시도·중복 요청을 안전하게 처리할 수 있는 근거가 된다.

## 비즈니스 규칙

<!-- catalog-anchor: order_constraint_allocation_requires_matching_sku -->
### 배정 시 SKU가 일치해야 한다

배정 시 Batch의 SKU와 OrderLine의 SKU가 반드시 일치해야 한다.
SKU가 맞지 않으면 배정할 수 없다.

주문 취소 시 모든 배정이 해제된다는 규칙은 Order 문서에서 canonical하게 다룬다.

## 도메인 이벤트

<!-- catalog-anchor: order_event_out_of_stock -->
### OutOfStock

특정 SKU의 재고가 부족하여 배정에 실패했음을 나타낸다.
외부 시스템(알림, 재발주 등)이 이 이벤트를 구독하여 후속 처리를 담당한다.

- 페이로드: sku, requested_quantity, timestamp
- 트리거: 배정 시 가용 수량 부족
- 후속: 주문자에게 알림

OrderCancelled 이벤트의 canonical 설명은 Order 문서에 둔다.

## Property-Based 검증 관점

<!-- catalog-anchor: order_property_batch_available_quantity_non_negative -->
### 가용 수량 비음수

가용 수량 비음수는 stateful PBT로 검증한다.

<!-- catalog-anchor: order_property_batch_allocation_idempotent -->
### 배정 멱등성

같은 요청을 반복해도 상태 변화가 한 번만 일어나는지 본다.

<!-- catalog-anchor: order_property_allocation_requires_matching_sku -->
### SKU 일치 검증

SKU가 다른 OrderLine은 Batch에 배정할 수 없어야 한다.

## 관계

Batch는 배정된 OrderLine의 집합을 유지한다.
Order와는 주문 취소·배정 해제 시나리오에서 간접적으로 연결된다.