from dataclasses import dataclass
from typing import List
from jambase_api.Enums.attendance_mode import AttendanceMode
from jambase_api.Enums.event_status import EventStatus
from jambase_api.Classes.external_identifier import ExternalIdentifier
from jambase_api.Classes.music_venue import MusicVenue
from jambase_api.Classes.offer import Offer
from jambase_api.Classes.performer import Performer
from jambase_api.Classes.place import Place
from jambase_api.Classes.url import Url


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
    location: Place
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
