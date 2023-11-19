from dataclasses import dataclass
from typing import List

from ..Enums.attendance_mode import AttendanceMode
from ..Enums.band_or_musician import BandOrMusician
from ..Enums.event_status import EventStatus
from ..Enums.genre import Genre
from .external_identifier import ExternalIdentifier
from .geo_coordinates import GeoCoordinates
from .music_group import MusicGroup
from .offer import Offer
from .place import Place
from .postal_address import PostalAddress
from .url import Url


@dataclass
class PerformerConcertMusicVenue:
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
class StreamPerformer:
    type: str
    name: str
    identifier: str
    url: str
    image: str
    datePublished: str
    dateModified: str
    xbandOrMusician: BandOrMusician
    xnumUpcomingEvents: int
    genre: Genre
    xperformanceDate: str
    xperformanceRank: int
    xisHealiner: bool
    xdateIsConfirmed: bool


@dataclass
class PerformerConcert:
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
    location: PerformerConcertMusicVenue
    offers: List[Offer]
    # performer: List[Performer]
    eventAttendanceMode: AttendanceMode
    isAccessibleForFree: bool
    promoImage: str
    type: str
    externalIdentifiers: List[ExternalIdentifier]
    customTitle: str
    subtitle: str
    headlinerInSupport: bool
    streamIds: List[str]


@dataclass
class Performer:
    type: str
    name: str
    identifier: str
    url: str
    image: str
    datePublished: str
    dateModified: str
    member: List[MusicGroup]
    memberOf: List[MusicGroup]
    foundingLocation: Place
    foundingDate: str
    genre: List[Genre]
    events: List[PerformerConcert]
    xbandOrMusician: BandOrMusician
    xnumUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]
    xperformanceDate: str
    xperformanceRank: int
    xisHeadliner: bool
    xdateIsConfirmed: bool
