# -*-coding:utf8-*-

from .APISections.artists import JamBaseArtists
from .APISections.events import JamBaseEvents
from .APISections.genres import JamBaseGenres
from .APISections.geographies import JamBaseGeographies
from .APISections.lookups import JamBaseDataSources
from .APISections.streams import JamBaseStreams
from .APISections.venues import JamBaseVenues


class JamBase(
    JamBaseArtists,
    JamBaseDataSources,
    JamBaseEvents,
    JamBaseGenres,
    JamBaseGeographies,
    JamBaseStreams,
    JamBaseVenues,
):
    pass
