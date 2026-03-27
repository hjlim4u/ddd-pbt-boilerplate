"""@order scope glossary terms."""

from src.catalog.types import GlossaryTerm


GLOSSARY: tuple[GlossaryTerm, ...] = (
    GlossaryTerm(
        id="G-01",
        term="Order",
        definition="고객이 결제를 완료한 구매 건. '요청'이나 '장바구니'와 다름.",
    ),
    GlossaryTerm(
        id="G-02",
        term="OrderLine",
        definition="Order 안의 개별 상품 항목. SKU + 수량으로 구성. '장바구니 항목'과 다름.",
    ),
    GlossaryTerm(
        id="G-03",
        term="Batch",
        definition="창고에 입고된 상품 묶음. reference로 식별. '주문'과 다름.",
    ),
    GlossaryTerm(
        id="G-04",
        term="Allocation",
        definition="OrderLine을 특정 Batch에 배정하는 행위. 가용 수량을 감소시킴.",
    ),
    GlossaryTerm(
        id="G-05",
        term="Money",
        definition="금액 + 통화의 불변 조합. 단순 숫자가 아니라 통화 정보를 포함.",
    ),
    GlossaryTerm(
        id="G-06",
        term="SKU",
        definition="Stock Keeping Unit. 상품 변형의 고유 식별자 (모델+사이즈+색상).",
    ),
)

__all__ = ["GLOSSARY"]
