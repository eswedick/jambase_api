from dataclasses import dataclass
from typing import List, Union
from jambase_api.Classes.external_identifier import ExternalIdentifier
from jambase_api.Classes.place import Place
from jambase_api.Classes.concert import Concert
from jambase_api.Classes.festival import Festival
from jambase_api.Classes.stream import Stream
from jambase_api.Classes.member import Member
from jambase_api.Enums.band_or_musician import BandOrMusician
from jambase_api.Enums.genre import Genre
from jambase_api.Classes.url import Url


@dataclass
class MusicGroup:
    name: str
    identifier: str
    url: str
    image: str
    sameAs: List[Url]
    datePublished: str
    dateModified: str
    member: List[Member]
    memberOf: List[Member]
    foundingLocation: Place
    foundingDate: str
    genre: List[Genre]
    events: List[Union[Concert, Festival, Stream]]
    bandOrMusician: BandOrMusician
    numUpcomingEvents: int
    externalIdentifiers: List[ExternalIdentifier]
