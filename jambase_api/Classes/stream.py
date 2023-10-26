from dataclasses import dataclass
from typing import List
from jambase_api.Classes.concert import Concert
from jambase_api.Classes.music_venue import MusicVenue
from jambase_api.Classes.offer import Offer
from jambase_api.Classes.performer import Performer
from jambase_api.Classes.url import Url

from jambase_api.Enums.attendance_mode import AttendanceMode
from jambase_api.Enums.event_status import EventStatus


@dataclass
class Stream:
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
    location: MusicVenue
    offers: List[Offer]
    performer: List[Performer]
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    x_promoImage: str
    type: str
    isLiveBroadcast: bool
    broadcastOfEvent: List[Concert]
    x_customTitle: str
