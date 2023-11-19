from dataclasses import dataclass

from .country import Country
from .state import State


@dataclass
class PostalAddress:
    streetAddress: str
    addressLocality: str
    postalCode: str
    addressRegion: State
    addressCountry: Country
    streetAddress2: str
    timezone: str
    jamBaseMetroId: int
    jamBaseCityId: int
