from dataclasses import dataclass
from typing import List
from jambase_api.Classes.address import Address
from jambase_api.Classes.city import City
from jambase_api.Classes.geo_coordinates import GeoCoordinates


@dataclass
class AdministrativeArea:
    type: str
    identifier: str
    name: str
    geo: GeoCoordinates
    address: Address
    containsPlace: List[City]
    primaryCityId: int
    numUpcomingEvents: int
