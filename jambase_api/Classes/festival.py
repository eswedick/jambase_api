from dataclasses import dataclass, field
from typing import List
from jambase_api.Enums.festival_lineup_display_option import FestivalLineupDisplayOption
from jambase_api.Classes.url import Url
from jambase_api.Enums.event_status import EventStatus
from jambase_api.Classes.music_venue import MusicVenue
from jambase_api.Classes.offer import Offer
from jambase_api.Classes.performer import Performer
from jambase_api.Enums.attendance_mode import AttendanceMode


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
