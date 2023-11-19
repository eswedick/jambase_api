from dataclasses import dataclass, field
from geo_coordinates import GeoCoordinates
from address import Address
from administrative_area import Metro


@dataclass
class City:
    type: str
    identifier: str
    name: str
    geo: GeoCoordinates
    address: Address
    timezone: str
    containedInPlace: Metro
    numUpcomingEvents: int
