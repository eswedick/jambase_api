from dataclasses import dataclass
from jambase_api.Classes.country import Country


@dataclass
class State:
    type: str
    identifier: str
    name: str
    alternateName: str
    country: Country
    numUpcomingEvents: int
