from dataclasses import dataclass

from .organization import Organization
from .price_specification import PriceSpecification


@dataclass
class Offer:
    type: str
    name: str
    identifier: str
    url: str
    datePublished: str
    dateModified: str
    category: str
    priceSpecification: PriceSpecification
    seller: Organization
    validFrom: str
