from dataclasses import dataclass
from typing import List

from .url import Url


@dataclass
class Organization:
    identifier: str
    disambiguatingDescription: str
    name: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
