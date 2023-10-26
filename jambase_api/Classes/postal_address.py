from dataclasses import dataclass
from jambase_api.Classes.state import State
from jambase_api.Classes.country import Country


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

