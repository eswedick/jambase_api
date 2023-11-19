from dataclasses import dataclass, field

from ..Enums.country_iso2 import CountryCodeIso2
from ..Enums.country_iso3 import CountryCodeIso3


@dataclass
class Country:
    type: str = field(metadata={"name": "@type"})
    identifier: CountryCodeIso2
    name: str
    alternateName: CountryCodeIso3
    numUpcomingEvents: int
