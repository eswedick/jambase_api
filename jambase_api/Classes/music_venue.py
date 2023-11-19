from dataclasses import dataclass
from typing import List
from jambase_api.Classes.geo_coordinates import GeoCoordinates
from jambase_api.Classes.postal_address import PostalAddress
from jambase_api.Classes.url import Url


@dataclass
class MusicVenue:
    type: str
    name: str
    identifier: str
    url: str
    image: str
    datePublished: str
    dateModified: str
    address: PostalAddress
    geo: GeoCoordinates
    sameAs: List[Url]
    maximumAttendeeCapacity: int
    xisPermanentlyClosed: bool
    xnumUpcomingEvents: int


