from dataclasses import dataclass, field
from typing import List

from ..Enums.attendance_mode import AttendanceMode
from ..Enums.event_status import EventStatus
from ..Enums.festival_lineup_display_option import FestivalLineupDisplayOption
from .music_venue import MusicVenue
from .offer import Offer
from .performer import Performer
from .url import Url


@dataclass
class Festival:
    type: str = field(metadata={"name": "@type"})
    lineupDisplayOptions: FestivalLineupDisplayOption
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
    performer: Performer
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    promoImage: str
