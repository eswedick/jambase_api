from dataclasses import dataclass
from typing import List

from ..Enums.attendance_mode import AttendanceMode
from ..Enums.event_status import EventStatus
from .external_identifier import ExternalIdentifier
from .geo_coordinates import GeoCoordinates
from .offer import Offer
from .performer import Performer
from .postal_address import PostalAddress
from .url import Url


@dataclass
class ConcertMusicVenue:
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
    # events: List[Event]
    isPermanentlyClosed: bool
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]


@dataclass
class Concert:
    name: str
    identifier: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
    eventStatus: EventStatus
    startDate: str
    endDate: str
    previousStartDate: str
    doorTime: str
    location: ConcertMusicVenue
    offers: List[Offer]
    performer: List[Performer]
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    promoImage: str
    type: str
    externalIdentifiers: List[ExternalIdentifier]
    customTitle: str
    subtitle: str
    headlinerInSupport: bool
    streamIds: List[str]
