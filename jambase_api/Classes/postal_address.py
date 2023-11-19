from dataclasses import dataclass
from state import State
from country import Country


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

