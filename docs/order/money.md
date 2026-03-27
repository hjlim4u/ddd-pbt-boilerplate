---
model_id: ORD_V_MONEY
scope: @order
constraints: [ORD_INV_MONEY_AMOUNT_NONNEG, ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER]
properties: [ORD_P_MONEY_SERIALIZATION_ROUND_TRIP, ORD_P_MONEY_ADDITION_COMMUTATIVE]
events: []
depends_on: []
---
<!-- catalog-anchor: ORD_V_MONEY -->
# Money

금액과 통화를 하나의 단위로 묶은 값 객체이다.
통화가 다른 Money 간 연산은 허용하지 않는다. 단순 숫자가 아니라 통화 정보가 도메인 의미를 갖는다.

구조적 관계는 `src/catalog/order/` 패키지와 문서의 `catalog-anchor` 주석을 통해 추적한다.

## 필드

<!-- catalog-anchor: ORD_F_MONEY_AMOUNT -->
- amount: Decimal - 소수점 2자리 이하의 금액

<!-- catalog-anchor: ORD_F_MONEY_CURRENCY -->
- currency: str - ISO 4217 3자리 대문자 통화 코드 (예: KRW, USD)

- 연산: `__add__`, `__sub__` - 같은 currency끼리만 허용

## 불변 조건

<!-- catalog-anchor: ORD_INV_MONEY_AMOUNT_NONNEG -->
### amount는 음수가 될 수 없다

amount는 항상 0 이상이어야 한다.

## 형식 제약

<!-- catalog-anchor: ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER -->
### Currency는 ISO 4217 대문자 코드다

Currency는 ISO 4217 3자리 대문자 코드여야 한다 (예: KRW, USD, EUR).

## Property-Based 검증 관점

<!-- catalog-anchor: ORD_P_MONEY_SERIALIZATION_ROUND_TRIP -->
### 직렬화 왕복

직렬화 후 역직렬화하면 원래 값과 동일해야 한다.
`ORD_INV_MONEY_AMOUNT_NONNEG`와 `ORD_FMT_MONEY_CURRENCY_ISO4217_UPPER`가 함께 보존되는지 본다.

<!-- catalog-anchor: ORD_P_MONEY_ADDITION_COMMUTATIVE -->
### 덧셈 교환법칙

같은 통화의 덧셈은 교환법칙이 성립한다.

## 관계

Order·주문 항목과 가격 계산 맥락에서 함께 쓰인다.
