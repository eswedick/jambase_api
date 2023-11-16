from dataclasses import dataclass, field
from jambase_api.Classes.country import Country


@dataclass
class State:
    type: str = field(metadata={"name": "@type"})
    identifier: str
    name: str
    alternateName: str
    country: Country
    numUpcomingEvents: int
