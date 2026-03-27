---
model_id: V-01
scope: @order
constraints: [INV-03, FMT-01]
properties: [P-001, P-002]
events: []
depends_on: []
---

# Money [V-01]

금액과 통화를 하나의 단위로 묶은 값 객체이다.
통화가 다른 Money 간 연산은 허용하지 않는다. 단순 숫자가 아니라 통화 정보가 도메인 의미를 갖는다.

구조적 관계는 `src/catalog/order.py`의 `MONEY` 객체를 본다.

## 필드

- amount: Decimal - 소수점 2자리 이하의 금액
- currency: str - ISO 4217 3자리 대문자 통화 코드 (예: KRW, USD)
- 연산: `__add__`, `__sub__` - 같은 currency끼리만 허용

## 불변 조건

amount는 항상 0 이상이어야 한다.

## 형식 제약

Currency는 ISO 4217 3자리 대문자 코드여야 한다 (예: KRW, USD, EUR).

## Property-Based 검증 관점

직렬화 후 역직렬화하면 원래 값과 동일해야 한다.
INV-03의 금액 규칙과 FMT-01의 통화 형식이 함께 보존되는지 본다.

같은 통화의 덧셈은 교환법칙이 성립한다.

## 관계

Order·주문 항목과 가격 계산 맥락에서 함께 쓰인다.
