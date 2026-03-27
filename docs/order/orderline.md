---
model_id: V-02
scope: @order
constraints: [FMT-02]
properties: [P-007]
events: []
depends_on: []
---

# OrderLine [V-02]

Order 안의 개별 상품 항목이다. SKU와 수량의 조합으로 정의된다.
order_id + sku 조합으로 동등성을 판단한다. "장바구니 항목"과는 다른 도메인 개념이다.

구조적 관계는 `src/catalog/order.py`의 `ORDER_LINE` 객체를 본다.

## 필드

- order_id: str - 소속 Order의 ID
- sku: str - 상품 식별자 (대문자 영숫자와 하이픈, 최대 20자)
- quantity: int - 주문 수량 (> 0)

## 형식 제약

SKU는 대문자 영숫자와 하이픈만, 최대 20자여야 한다 (예: BLUE-CHAIR-XL).

## Property-Based 검증 관점

- 유효한 SKU는 생성 가능하고, 형식이 맞지 않는 SKU는 거부된다 (P-007).
- Batch에 배정할 때는 Batch의 SKU와 일치해야 한다. SKU 일치 검증은 Batch·OrderLine 경계에서 다룬다 (P-006, 주로 Batch 서사와 함께 읽는다).

## 관계

Order에 포함되며, Batch의 allocations 집합에 배정될 수 있다.
