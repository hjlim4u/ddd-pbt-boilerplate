"""도메인 카탈로그 패키지.

구현 코드(src/domain/)에 의존하지 않는 순수 도메인 지식 객체.
docs/ 문서를 Source of Truth로 삼아 도메인 모델·제약사항·Property·이벤트·용어를
Python 객체로 표현한다.

Usage:
    from src.catalog import CATALOG
    from src.catalog import order

    money_model = order.ORD_V_MONEY
    amount_rule = order.ORD_INV_MONEY_AMOUNT_NONNEG
"""

from dataclasses import dataclass

from src.catalog import order as _order
from src.catalog.types import (
    Constraint,
    DomainEvent,
    DomainModel,
    GlossaryTerm,
    ModelField,
    Property,
)


@dataclass(frozen=True)
class DomainCatalog:
    """전체 도메인 카탈로그. 모든 스코프의 도메인 지식을 통합한다."""

    models: tuple[DomainModel, ...]
    constraints: tuple[Constraint, ...]
    properties: tuple[Property, ...]
    events: tuple[DomainEvent, ...]
    glossary: tuple[GlossaryTerm, ...]

    def impact_of(self, target_id: str) -> dict[str, tuple[str, ...]]:
        """target_id 변경 시 영향받는 항목을 반환한다.

        모델 ID, 제약사항 ID, Property ID, 이벤트 ID 모두 허용.
        """
        affected_models = tuple(
            model.id
            for model in self.models
            if any(constraint.id == target_id for constraint in model.constraints)
            or any(prop.id == target_id for prop in model.properties)
            or any(event.id == target_id for event in model.events)
            or any(dependency.id == target_id for dependency in model.depends_on)
        )
        affected_constraints = tuple(
            constraint.id
            for constraint in self.constraints
            if any(
                model.id == target_id and constraint in model.constraints
                for model in self.models
            )
            or any(prop.id == target_id and constraint in prop.source for prop in self.properties)
        )
        affected_properties = tuple(
            prop.id
            for prop in self.properties
            if any(constraint.id == target_id for constraint in prop.source)
            or any(model.id == target_id and prop in model.properties for model in self.models)
        )
        affected_events = tuple(
            event.id
            for event in self.events
            if any(model.id == target_id and event in model.events for model in self.models)
        )
        return {
            "models": affected_models,
            "constraints": affected_constraints,
            "properties": affected_properties,
            "events": affected_events,
        }


CATALOG = DomainCatalog(
    models=_order.MODELS,
    constraints=_order.CONSTRAINTS,
    properties=_order.PROPERTIES,
    events=_order.EVENTS,
    glossary=_order.GLOSSARY,
)

__all__ = [
    "CATALOG",
    "DomainCatalog",
    "DomainModel",
    "ModelField",
    "Constraint",
    "Property",
    "DomainEvent",
    "GlossaryTerm",
    "order",
]
