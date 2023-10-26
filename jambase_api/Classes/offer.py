from dataclasses import dataclass
from typing import List
from jambase_api.Classes.organization import Organization
from jambase_api.Classes.price_specification import PriceSpecification
from jambase_api.Classes.url import Url


@dataclass
class Offer:
    name: str
    identifier: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
    category: str
    priceSpecification: PriceSpecification
    seller: Organization
    validFrom: str
