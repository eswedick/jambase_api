from dataclasses import dataclass
from typing import List

from .geo_coordinates import GeoCoordinates
from .postal_address import PostalAddress
from .url import Url


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
