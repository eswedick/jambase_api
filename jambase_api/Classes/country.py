from dataclasses import dataclass
from jambase_api.Enums.country_iso2 import CountryCodeIso2
from jambase_api.Enums.country_iso3 import CountryCodeIso3


@dataclass
class Country:
    type: str
    identifier: CountryCodeIso2
    name: str
    alternateName: CountryCodeIso3
    numUpcomingEvents: int
