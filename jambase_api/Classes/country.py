from dataclasses import dataclass, field
from jambase_api.Enums.country_iso2 import CountryCodeIso2
from jambase_api.Enums.country_iso3 import CountryCodeIso3


@dataclass
class Country:
    type: str = field(metadata={"name": "@type"})
    identifier: CountryCodeIso2
    name: str
    alternateName: CountryCodeIso3
    numUpcomingEvents: int
