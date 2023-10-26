from dataclasses import dataclass
from decimal import Decimal


@dataclass
class PriceSpecification:
    type: str
    minPrice: Decimal
    maxPrice: Decimal
    price: Decimal
    priceCurrency: str
