# 경량 DDD 적용 범위

## 왜 경량인가

전통적 DDD는 Bounded Context, Aggregate Root, Repository, Unit of Work, Domain Service,
Anti-Corruption Layer, Context Map 등 풍부한 전략적·전술적 패턴을 제안한다.
그러나 이 boilerplate가 대상으로 하는 가벼운 서비스에서는 이 모든 것을 도입하면
패턴 유지 비용이 도메인 복잡도를 초과한다.

이 방법론의 판단 기준은 단순하다:
**"이 구조가 없으면 AI agent가 잘못된 코드를 생성하는가?"**
그렇다면 도입하고, 아니면 생략한다.

## 도입하는 것

| 요소 | 목적 | 형태 |
|------|------|------|
| 용어집 | AI가 용어를 혼동하지 않도록 고정 | glossary.md |
| 개념별 서사 | 필드·규칙·이벤트·Property 맥락을 한곳에 서술 | docs/<scope>/*.md (예: docs/order/order.md) |
| 구조적 관계 | ID 교차 참조의 정본 | src/catalog/<scope>.py + src/catalog/__init__.py |

이 조합이 AI agent에게 "도메인을 이해할 수 있는 최소한의 구조"를 제공한다.

## 도입하지 않는 것

| 요소 | 이유 |
|------|------|
| Bounded Context 분리 | 가벼운 서비스에서는 단일 컨텍스트로 충분. 서비스가 커지면 @scope 태그로 영역을 구분하되, 별도 패키지로 분리하지는 않음 |
| Aggregate Root 패턴 | 엔티티 간 관계를 카탈로그와 개념 서사에 명시하면 충분. 트랜잭션 경계를 코드로 강제할 필요가 없는 규모 |
| Repository / Unit of Work | ORM이나 간단한 DAO로 충분 |
| Domain Service 레이어 분리 | 비즈니스 로직이 모델 메서드 안에 있으면 됨. services.py는 존재하지만 별도 레이어가 아니라 편의상 모은 것 |
| Anti-Corruption Layer | 외부 시스템이 적으면 불필요 |
| Context Map | 컨텍스트가 하나이므로 불필요 |

## ID 기반 교차 참조

경량 DDD에서 가장 중요한 설계 결정은 **모든 artifact에 고유 ID를 부여하고 교차 참조하는 것**이다.

```
ID 체계:
  E-XX    Entity (E-01 Order, E-02 Batch)
  V-XX    Value Object (V-01 Money, V-02 OrderLine)
  EV-XX   도메인 이벤트 (EV-01 OrderCreated)
  INV-XX  불변식 (INV-01 가용 수량 비음수)
  POL-XX  정책 (POL-01 ETA 우선 배정)
  FMT-XX  형식 (FMT-01 ISO 4217)
  P-XXX   Property (P-001 Money round-trip)
  @name   영역 태그 (@order, @inventory)
```

교차 참조는 **카탈로그**(`src/catalog/<scope>.py`, `src/catalog/__init__.py`)의 `DomainModel`, `Constraint`, `Property` 객체 필드로 기록한다.
서사는 **개념별** `docs/<scope>/*.md`에 유지한다.

이 구조의 효과:
- **agent가 영향 범위를 즉시 파악**: `CATALOG.impact_of("E-02")` 등으로 연결된 ID를 조회
- **integrity-checker가 자동 검증**: 카탈로그 내부 참조와 코드·테스트 ID를 스크립트가 탐지
- **서사는 한 개념 파일로 읽기 쉬움**: `doc_file` 한 경로로 개념 맥락 파악

## 구현 패턴

### Value Object — Pydantic frozen model

불변성과 유효성 검증을 선언적으로 보장한다.
Pydantic의 Field 제약이 곧 카탈로그의 해당 제약사항(INV/FMT)과 1:1 대응한다.

```python
class Money(BaseModel):
    """[V-01] INV-03: amount >= 0, FMT-01: ISO 4217."""
    model_config = ConfigDict(frozen=True)
    amount: Decimal = Field(ge=0, decimal_places=2)      # ← INV-03
    currency: str = Field(min_length=3, max_length=3,
                          pattern=r"^[A-Z]{3}$")          # ← FMT-01
```

### Entity — Python dataclass

프레임워크 의존 없이 순수 Python으로 도메인 로직을 표현한다.
`__post_init__`에서 불변식을 검증한다.

```python
@dataclass
class Order:
    """[E-01] INV-02: 최소 1개 OrderLine 필수."""
    id: str
    customer_id: str
    order_lines: list[OrderLine]

    def __post_init__(self):
        if not self.order_lines:  # ← INV-02
            raise InvalidOrderError("Order must have at least one OrderLine")
```

### 도메인 레이어 격리 원칙

`src/domain/` 안의 코드는 외부 의존성(DB, API, 프레임워크)을 import하지 않는다.
이것이 PBT를 가능하게 하는 전제조건이다.
도메인 로직이 외부 I/O에 의존하면, Hypothesis가 수천 개의 입력을 생성해도
매번 DB를 호출해야 하므로 테스트가 느려지거나 불가능해진다.

## 확장 경로

도메인이 복잡해지면 다음 순서로 점진적으로 확장한다:

1. **모델 15개 이하**: 현재 평탄한 구조 유지. ID + refs만 추가.
2. **모델 15~40개**: index.md + 영역별 파일 분리 (models/order.md, models/inventory.md).
3. **모델 40개 이상**: 모델 카드 (cards/E-01-order.md). 모델 하나당 파일 하나.

전환은 점진적으로 한다. 한 번에 재구성하지 않고, 가장 복잡한 영역부터 분리한다.
