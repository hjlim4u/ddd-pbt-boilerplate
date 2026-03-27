---
model_id: ORD_V_ORDER_LINE
scope: @order
constraints: [ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20]
properties: [ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION]
events: []
depends_on: []
---
<!-- catalog-anchor: ORD_V_ORDER_LINE -->
# OrderLine

Order 안의 개별 상품 항목이다. SKU와 수량의 조합으로 정의된다.
order_id + sku 조합으로 동등성을 판단한다. "장바구니 항목"과는 다른 도메인 개념이다.

구조적 관계는 `src/catalog/order/` 패키지와 문서의 `catalog-anchor` 주석을 통해 추적한다.

## 필드

<!-- catalog-anchor: ORD_F_ORDER_LINE_ORDER_ID -->
- order_id: str - 소속 Order의 ID

<!-- catalog-anchor: ORD_F_ORDER_LINE_SKU -->
- sku: str - 상품 식별자 (대문자 영숫자와 하이픈, 최대 20자)

<!-- catalog-anchor: ORD_F_ORDER_LINE_QUANTITY -->
- quantity: int - 주문 수량 (> 0)

## 형식 제약

<!-- catalog-anchor: ORD_FMT_ORDER_LINE_SKU_UPPER_ALNUM_HYPHEN_MAX20 -->
### SKU 형식은 제한된다

SKU는 대문자 영숫자와 하이픈만, 최대 20자여야 한다 (예: BLUE-CHAIR-XL).

## Property-Based 검증 관점

<!-- catalog-anchor: ORD_P_ORDER_LINE_SKU_FORMAT_VALIDATION -->
### SKU 형식 검증

유효한 SKU는 생성 가능하고, 형식이 맞지 않는 SKU는 거부된다.
SKU 일치 규칙은 Batch 문서에서 canonical하게 다룬다.

## 관계

Order에 포함되며, Batch의 allocations 집합에 배정될 수 있다.
