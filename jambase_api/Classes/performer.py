from dataclasses import dataclass
from typing import List
from jambase_api.Classes.external_identifier import ExternalIdentifier
from jambase_api.Classes.place import Place
from jambase_api.Classes.concert import Concert
from jambase_api.Enums.band_or_musician import BandOrMusician
from jambase_api.Enums.genre import Genre
from jambase_api.Classes.url import Url
from jambase_api.Classes.music_group import MusicGroup


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
    events: List[Concert]
    bandOrMusician: BandOrMusician
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]
    performanceDate: str
    performanceRank: int
    isHeadliner: bool
    dateIsConfirmed: bool
