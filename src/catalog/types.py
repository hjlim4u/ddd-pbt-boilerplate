"""도메인 카탈로그 타입 정의.

구현 코드(src/domain/)에 의존하지 않는 순수 데이터 타입.
도메인 개념을 Python 객체로 표현하여 LSP/AST 기반 탐색을 지원한다.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelField:
    """도메인 모델의 단일 필드 정의."""

    id: str
    """필드 ID이자 정본 문서 앵커 키. Python 변수명으로 사용 가능한 snake_case 형식."""

    name: str
    type_hint: str
    description: str = ""


@dataclass(frozen=True)
class DomainModel:
    """도메인 모델 카탈로그 항목 (Entity 또는 Value Object).

    Source of Truth (서사): docs/<scope>/*.md, docs/index.md.
    구조: src/catalog/<scope>/ 패키지
    """

    id: str
    """모델 ID이자 정본 문서 앵커 키. Python 변수명으로 사용 가능한 snake_case 형식."""

    name: str
    """Python 클래스 이름과 일치하는 모델 이름."""

    model_type: str
    """'Entity' 또는 'ValueObject'."""

    scope: str
    """소속 Bounded Context. 예: '@order'."""

    fields: tuple[ModelField, ...]
    """모델이 갖는 필드 목록."""

    doc_file: str
    """이 모델의 개념 서사 파일 경로. 예: 'docs/order/order.md'."""

    constraints: tuple[Constraint, ...] = ()
    """이 모델에 적용되는 제약사항 객체 목록."""

    properties: tuple[Property, ...] = ()
    """이 모델과 연결된 Property 객체 목록."""

    events: tuple[DomainEvent, ...] = ()
    """이 모델이 발행하거나 관련된 이벤트 객체 목록."""

    depends_on: tuple[DomainModel, ...] = ()
    """이 모델이 의존하는 다른 모델 객체 목록."""


@dataclass(frozen=True)
class Constraint:
    """비즈니스 제약사항 카탈로그 항목.

    Source of Truth (서사): 적용 모델의 docs/<scope>/*.md.
    구조: src/catalog/<scope>/constraints.py
    """

    id: str
    """제약사항 ID이자 정본 문서 앵커 키. Python 변수명으로 사용 가능한 snake_case 형식."""

    category: str
    """'invariant' | 'policy' | 'format'."""

    description: str
    """제약사항의 한 줄 설명."""


@dataclass(frozen=True)
class Property:
    """Property-Based Test 카탈로그 항목.

    Source of Truth (서사): 관련 모델의 docs/<scope>/*.md (Property 관점).
    구조: src/catalog/<scope>/properties.py
    """

    id: str
    """Property ID이자 정본 문서 앵커 키. Python 변수명으로 사용 가능한 snake_case 형식."""

    name: str
    """Property 이름."""

    source: tuple[Constraint, ...]
    """이 Property가 검증하는 제약사항 객체 목록."""

    category: str
    """'invariant' | 'round-trip' | 'idempotence' | 'metamorphic' | 'policy'."""

    description: str
    """Property가 검증하는 내용 한 줄 설명."""

    test_mode: str
    """'PBT' | 'TDD' | 'Mixed'."""

    test_file: str
    """대응하는 테스트 파일 경로."""


@dataclass(frozen=True)
class DomainEvent:
    """도메인 이벤트 카탈로그 항목.

    Source of Truth (서사): 관련 모델의 docs/<scope>/*.md (이벤트 섹션).
    구조: src/catalog/<scope>/events.py
    """

    id: str
    """이벤트 ID이자 정본 문서 앵커 키. Python 변수명으로 사용 가능한 snake_case 형식."""

    name: str
    """Python 클래스 이름과 일치하는 이벤트 이름."""

    scope: str
    """소속 Bounded Context. 예: '@order'."""

    payload: tuple[str, ...]
    """이벤트 페이로드 필드 이름 목록."""

    trigger: str
    """이벤트가 발행되는 조건."""

    subsequent: str
    """이벤트 발행 후 이어지는 처리."""


@dataclass(frozen=True)
class GlossaryTerm:
    """도메인 용어집 항목.

    Source of Truth: docs/glossary.md
    """

    id: str
    """용어 ID. G-XX 형식."""

    term: str
    """용어 이름."""

    definition: str
    """용어의 도메인 정의. '~이다' + '~이 아니다' 형식 권장."""
