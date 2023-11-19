from dataclasses import dataclass

from ..Enums.country_iso2 import CountryCodeIso2
from ..Enums.state import StateCode


@dataclass
class Address:
    addressRegion: StateCode
    addressCountry: CountryCodeIso2
