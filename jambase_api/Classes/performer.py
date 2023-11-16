from dataclasses import dataclass
from typing import List
from jambase_api.Classes.external_identifier import ExternalIdentifier
from jambase_api.Classes.place import Place
from jambase_api.Enums.band_or_musician import BandOrMusician
from jambase_api.Classes.geo_coordinates import GeoCoordinates
from jambase_api.Classes.postal_address import PostalAddress
from jambase_api.Enums.genre import Genre
from jambase_api.Classes.url import Url
from jambase_api.Classes.music_group import MusicGroup
from jambase_api.Enums.attendance_mode import AttendanceMode
from jambase_api.Classes.offer import Offer
from jambase_api.Enums.event_status import EventStatus


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
    #events: List[Event]
    isPermanentlyClosed: bool
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]


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
    #performer: List[Performer]
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
    name: str
    identifier: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
    member: List[MusicGroup]
    memberOf: List[MusicGroup]
    foundingLocation: Place
    foundingDate: str
    genre: List[Genre]
    events: List[PerformerConcert]
    bandOrMusician: BandOrMusician
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]
    performanceDate: str
    performanceRank: int
    isHeadliner: bool
    dateIsConfirmed: bool
