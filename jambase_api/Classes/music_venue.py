from dataclasses import dataclass
from typing import List
from jambase_api.Classes.event import Event
from jambase_api.Classes.external_identifier import ExternalIdentifier
from jambase_api.Classes.geo_coordinates import GeoCoordinates
from jambase_api.Classes.postal_address import PostalAddress
from jambase_api.Classes.url import Url





@dataclass
class MusicVenue:
    identifier: str
    disambiguatingDescription: str
    name: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
    maximumAttendeeCapacity: int
    address: PostalAddress
    geo: GeoCoordinates
    events: List[Event]
    isPermanentlyClosed: bool
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]


