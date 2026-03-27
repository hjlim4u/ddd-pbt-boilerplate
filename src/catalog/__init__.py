"""도메인 카탈로그 패키지.

구현 코드(src/domain/)에 의존하지 않는 순수 도메인 지식 객체.
docs/ 문서를 Source of Truth로 삼아 도메인 모델·제약사항·Property·이벤트·용어를
Python 객체로 표현한다.

Usage:
    from src.catalog import CATALOG
    from src.catalog import order

    money_model = order.MONEY
    inv_01 = order.INV_01
"""

from dataclasses import dataclass

from src.catalog.types import (
    Constraint,
    DomainEvent,
    DomainModel,
    GlossaryTerm,
    ModelField,
    Property,
)
from src.catalog import order as _order


@dataclass(frozen=True)
class DomainCatalog:
    """전체 도메인 카탈로그. 모든 스코프의 도메인 지식을 통합한다."""

    models: tuple[DomainModel, ...]
    constraints: tuple[Constraint, ...]
    properties: tuple[Property, ...]
    events: tuple[DomainEvent, ...]
    glossary: tuple[GlossaryTerm, ...]

    def get_model(self, model_id: str) -> DomainModel:
        for m in self.models:
            if m.id == model_id:
                return m
        raise KeyError(f"Model not found: {model_id}")

    def get_constraint(self, constraint_id: str) -> Constraint:
        for c in self.constraints:
            if c.id == constraint_id:
                return c
        raise KeyError(f"Constraint not found: {constraint_id}")

    def get_property(self, property_id: str) -> Property:
        for p in self.properties:
            if p.id == property_id:
                return p
        raise KeyError(f"Property not found: {property_id}")

    def get_event(self, event_id: str) -> DomainEvent:
        for e in self.events:
            if e.id == event_id:
                return e
        raise KeyError(f"Event not found: {event_id}")

    def models_for_constraint(self, constraint_id: str) -> tuple[DomainModel, ...]:
        """특정 제약사항이 적용되는 모델 목록을 반환한다."""
        return tuple(m for m in self.models if constraint_id in m.constraints)

    def constraints_for_model(self, model_id: str) -> tuple[Constraint, ...]:
        """특정 모델에 적용되는 제약사항 목록을 반환한다."""
        return tuple(c for c in self.constraints if model_id in c.applies_to)

    def properties_for_model(self, model_id: str) -> tuple[Property, ...]:
        """특정 모델과 연결된 Property 목록을 반환한다."""
        return tuple(p for p in self.properties if model_id in p.models)

    def doc_file_for_model(self, model_id: str) -> str:
        """특정 모델의 개념 서사 파일 경로를 반환한다."""
        return self.get_model(model_id).doc_file

    def doc_files_for_constraint(self, constraint_id: str) -> tuple[str, ...]:
        """특정 제약사항과 연결된 개념 서사 파일 목록을 반환한다."""
        return tuple(
            dict.fromkeys(
                self.get_model(model_id).doc_file
                for model_id in self.get_constraint(constraint_id).applies_to
            )
        )

    def doc_files_for_property(self, property_id: str) -> tuple[str, ...]:
        """특정 Property와 연결된 개념 서사 파일 목록을 반환한다."""
        return tuple(
            dict.fromkeys(
                self.get_model(model_id).doc_file
                for model_id in self.get_property(property_id).models
            )
        )

    def impact_of(self, target_id: str) -> dict[str, tuple[str, ...]]:
        """target_id 변경 시 영향받는 항목을 반환한다.

        모델 ID, 제약사항 ID, Property ID, 이벤트 ID 모두 허용.
        """
        affected_models = tuple(
            m.id for m in self.models
            if target_id in m.constraints
            or target_id in m.properties
            or target_id in m.events
            or target_id in m.depends_on
        )
        affected_constraints = tuple(
            c.id for c in self.constraints
            if target_id in c.applies_to or target_id in c.properties
        )
        affected_properties = tuple(
            p.id for p in self.properties
            if target_id in p.source or target_id in p.models
        )
        affected_events = tuple(
            e.id for e in self.events
            if target_id in e.related_models
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
