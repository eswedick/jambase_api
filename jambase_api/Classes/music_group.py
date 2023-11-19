from dataclasses import dataclass
from typing import List

from ..Enums.band_or_musician import BandOrMusician
from ..Enums.genre import Genre
from .member import Member
from .place import Place
from .url import Url


@dataclass
class MusicGroup:
    type: str
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
    # events: List[Union[Concert, Festival, Stream]]
    xbandOrMusician: BandOrMusician
    xnumUpcomingEvents: int
