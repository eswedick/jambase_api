from dataclasses import dataclass
from jambase_api.Enums.state import StateCode
from jambase_api.Enums.country_iso2 import CountryCodeIso2


@dataclass
class Address:
    addressRegion: StateCode
    addressCountry: CountryCodeIso2
