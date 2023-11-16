from dataclasses import dataclass, field
from decimal import Decimal


@dataclass
class PriceSpecification:
    type: str = field(metadata={"name": "@type"})
    minPrice: Decimal
    maxPrice: Decimal
    price: Decimal
    priceCurrency: str
