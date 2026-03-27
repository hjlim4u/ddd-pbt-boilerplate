# PBT / TDD 라우팅 기준

## 핵심 전제

모든 코드를 PBT로 테스트하지 않는다. 모든 코드를 TDD로만 테스트하지도 않는다.
제약사항의 성격에 따라 **가장 효과적인 테스트 방식**을 선택한다.

PBT가 "모든 유효한 입력에서 성립"을 검증한다면,
TDD는 "이 특정 시나리오가 의도한 대로 동작"을 검증한다.
둘은 경쟁이 아니라 보완 관계다.

## 4문항 판단

제약사항 하나에 대해 아래 질문에 답한다:

| # | 질문 | 판단 기준 |
|---|------|----------|
| Q1 | 규칙이 "모든 X에 대해 Y가 성립"으로 표현되는가? | 일반 명제 가능 여부 |
| Q2 | 입력 공간이 넓은가? (수십 가지 이상의 유효 조합) | 조합 폭발 여부 |
| Q3 | shrink된 반례가 디버깅에 유의미한가? | 최소 반례의 가치 |
| Q4 | 구현과 독립된 검증 방법(oracle)이 있는가? | 독립 검증 가능 여부 |

판정:
- **3~4개 Yes → PBT** (tests/properties/)
- **0~1개 Yes → TDD** (tests/unit/)
- **2개 Yes → Mixed** (PBT + TDD 예제 보완)

## DDD 구성 요소별 기본 성향

### Value Object → PBT 우선

입력 공간이 넓고 불변식이 뚜렷하다.
Money의 amount는 0~999999.99 범위의 Decimal이고,
currency는 5개 이상의 유효 값이 있으므로 조합이 수만 가지다.
사람이 10개의 예제를 쓰는 것보다 Hypothesis가 50개를 생성하는 게 낫다.

```
ORD_INV_MONEY_AMOUNT_NONNEG (Money.amount >= 0):
  Q1=Y (모든 Money에 대해 성립)
  Q2=Y (Decimal × Currency 조합)
  Q3=Y (경계값 0.00, -0.01이 반례로 유의미)
  Q4=Y (amount >= 0은 구현 독립적으로 검증 가능)
  → PBT
```

대표 property 유형:
- **Round-trip**: `serialize(deserialize(x)) == x` — 모든 직렬화 경로
- **Commutativity**: `a + b == b + a` — 교환법칙이 성립해야 하는 연산
- **Identity**: `a + zero == a` — 항등원 보존

### Entity 상태 전이 → Mixed

핵심 불변식은 PBT(stateful)로, 구체적 시나리오는 TDD로 테스트한다.

Batch의 allocate/deallocate는 어떤 명령 시퀀스 이후에도
available_quantity >= 0이어야 한다 (ORD_INV_BATCH_AVAILABLE_QUANTITY_NONNEG). 이것은 Hypothesis의
RuleBasedStateMachine으로 테스트한다.

```python
class BatchAllocationMachine(RuleBasedStateMachine):
    @rule(qty=st.integers(min_value=1, max_value=30))
    def allocate(self, qty):
        ...
    @invariant()
    def available_never_negative(self):
        assert self.batch.available_quantity >= 0
```

동시에 "2개 Batch에 걸친 주문 취소" 같은 구체적 시나리오는
TDD로 고정한다. 이런 시나리오는 PBT가 우연히 생성하기 어렵고,
비즈니스 요구사항을 문서화하는 역할도 한다.

### 도메인 정책 → 일반화 가능하면 PBT, 예외 많으면 TDD

```
ORD_POL_ALLOC_REQUIRES_MATCHING_SKU (SKU 일치 검증):
  Q1=Y ("모든 배정에서 SKU가 일치해야 한다")
  Q2=Y (SKU 문자열 조합이 넓음)
  Q3=Y (불일치 SKU가 반례로 유의미)
  Q4=Y (sku_batch != sku_line이면 실패)
  → PBT

ORD_POL_ORDER_CANCEL_RELEASES_ALLOC (주문 취소 시 배정 해제):
  Q1=Y ("모든 취소에서 배정이 해제되어야 한다")
  Q2=N (취소 시나리오 자체는 제한적)
  Q3=N (shrink보다 구체 시나리오가 더 유의미)
  Q4=Y (취소 전후 가용 수량 비교로 검증 가능)
  → Mixed (2개 Yes)
```

### 서비스 오케스트레이션 → TDD 우선

여러 Entity와 외부 의존성을 조합하는 흐름은
예제 기반 시나리오가 더 읽기 쉽고 의도가 명확하다.

```python
def test_allocate_to_earliest_batch(self):
    """ETA가 빠른 Batch에 우선 배정."""
    early = Batch("B-EARLY", "WIDGET", 50, eta=date(2024, 1, 1))
    late = Batch("B-LATE", "WIDGET", 50, eta=date(2024, 6, 1))
    line = OrderLine(order_id="O-001", sku="WIDGET", quantity=10)
    ref = allocate(line, [late, early])
    assert ref == "B-EARLY"
```

### 외부 어댑터 (DB, API) → TDD 전용

Property보다 프로토콜 적합성, 스키마, 실패 처리, 재시도, 멱등성 계약이 중요하다.

## Property 추출 절차

Property는 **구현 코드가 아니라 도메인 서사(`docs/<scope>/`)와 카탈로그(`src/catalog/`)에서 추출**한다.
이것이 핵심 규칙이다.

구현 코드를 먼저 보고 property를 만들면,
버그를 포함한 현재 구현을 정당화하는 "동어반복 테스트"가 나온다.
예: 코드가 `available = purchased - allocated`이면
테스트도 `assert available == purchased - allocated`가 되어
"나누기 대신 빼기를 써야 하는가?"라는 본질적 질문을 검증하지 못한다.

property-extractor skill이 이 절차를 자동화한다:
1. `src/catalog/`에서 제약사항·모델·`doc_file` 확인
2. `docs/<scope>/*.md`에서 관련 서사 읽기
3. 기존 Property는 카탈로그 `PROPERTIES`에서 확인 (이미 커버된 것 제외)
4. **src/domain/ 코드는 읽지 않음**
5. 4문항 라우팅 수행
6. property 후보 생성

## Hypothesis 프로파일

개발 환경에 따라 PBT 실행 강도를 조절한다:

```python
# conftest.py에 설정됨
settings.register_profile("dev",     max_examples=50,   deadline=400)
settings.register_profile("ci",      max_examples=300,  deadline=None)
settings.register_profile("nightly", max_examples=5000, deadline=None)
```

- `dev`: 로컬에서 빠른 피드백. 50개 예제면 대부분의 명백한 버그를 잡는다.
- `ci`: PR 머지 전 검증. 300개면 엣지 케이스 대부분을 커버한다.
- `nightly`: 릴리스 전 야간 빌드. 5000개로 철저하게 탐색한다.

환경변수로 선택: `HYPOTHESIS_PROFILE=ci pytest tests/properties/`

## 운영 중 실패 대응

1. 장애 재현하는 **예제 기반 회귀 테스트**를 먼저 추가 (tests/unit/)
2. "이 버그가 더 일반적인 규칙 위반인가?" 검토
3. 일반화 가능하면 카탈로그에 제약사항 추가 및 `docs/<scope>/` 서사 갱신 → property 추출 → PBT 추가
4. PBT에 `@example()`로 원래 장애 케이스도 고정

```python
@given(qty=st.integers(min_value=1, max_value=200))
@example(qty=101)  # 실제 장애 케이스 고정
def test_allocation_respects_capacity(qty):
    ...
```
