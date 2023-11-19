from dataclasses import dataclass, field
from typing import List

from jambase_api.Enums.attendance_mode import AttendanceMode
from jambase_api.Enums.event_status import EventStatus

from .external_identifier import ExternalIdentifier
from .geo_coordinates import GeoCoordinates
from .offer import Offer
from .performer import Performer
from .postal_address import PostalAddress
from .url import Url


@dataclass
class EventMusicVenue:
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
class Event:
    type: str
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
    location: EventMusicVenue
    offers: List[Offer]
    performer: List[Performer]
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    xstreamIds: List[str] = field(default_factory=list)
    xheadlinerInSupport: bool = False
    xpromoImage: str = ""
    xcustomTitle: str = ""
    xsubtitle: str = ""
