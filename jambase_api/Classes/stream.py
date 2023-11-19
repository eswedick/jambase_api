from dataclasses import dataclass
from typing import List

from ..Enums.attendance_mode import AttendanceMode
from ..Enums.event_status import EventStatus
from .concert import Concert
from .music_venue import MusicVenue
from .offer import Offer
from .performer import StreamPerformer
from .url import Url


@dataclass
class Stream:
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
    location: MusicVenue
    offers: List[Offer]
    performer: List[StreamPerformer]
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    isLiveBroadcast: bool
    xcustomTitle: str
    broadcastOfEvent: List[Concert]
