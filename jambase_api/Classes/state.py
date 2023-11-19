from dataclasses import dataclass, field

from .country import Country


@dataclass
class State:
    type: str = field(metadata={"name": "@type"})
    identifier: str
    name: str
    alternateName: str
    country: Country
    numUpcomingEvents: int
