from dataclasses import dataclass

from .address import Address
from .geo_coordinates import GeoCoordinates


@dataclass
class MetroCity:
    type: str
    identifier: str
    name: str
    geo: GeoCoordinates
    address: Address
    timezone: str
    xcontainedInPlace: []
    xnumUpcomingEvents: int


@dataclass
class Metro:
    type: str
    identifier: str
    name: str
    geo: GeoCoordinates
    address: Address
    # containsPlace: List[MetroCity]
    xprimaryCityId: int
    xnumUpcomingEvents: int
