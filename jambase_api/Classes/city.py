from dataclasses import dataclass, field
from jambase_api.Classes.geo_coordinates import GeoCoordinates
from jambase_api.Classes.address import Address
from jambase_api.Classes.administrative_area import AdministrativeArea


@dataclass
class City:
    type: str = field(metadata={"name": "@type"})
    identifier: str
    name: str
    geo: GeoCoordinates
    address: Address
    timezone: str
    containedInPlace: AdministrativeArea
    numUpcomingEvents: int
