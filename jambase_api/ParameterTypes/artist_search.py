from enum import Enum


class ArtistSearch(Enum):
    """List of possible parameters to pass into the Artist API section"""

    artistId = "artistId"
    artistName = "artistName"
    artistHasUpcomingEvents = "artistHasUpcomingEvents"
    dateModifiedFrom = "dateModifiedFrom"
    datePublishedFrom = "datePublishedFrom"
    artistDataSource = "artistDataSource"
    eventDateFrom = "eventDateFrom"
    eventDatePreset = "eventDatePreset"
    eventDateTo = "eventDateTo"
    eventType = "eventType"
    expandArtistSameAs = "expandArtistSameAs"
    expandExternalIdentifiers = "expandExternalIdentifiers"
    genreSlug = "genreSlug"
    geoCityId = "geoCityId"
    geoCountryIso2 = "geoCountryIso2"
    geoCountryIso3 = "geoCountryIso3"
    geoIp = "geoIp"
    geoLatitude = "geoLatitude"
    geoLongitude = "geoLongitude"
    geoMetroId = "geoMetroId"
    geoRadiusAmount = "geoRadiusAmount"
    geoRadiusUnits = "geoRadiusUnits"
    geoStateIso = "geoStateIso"
    page = "page"
    perPage = "perPage"
    venueId = "venueId"
    venueName = "venueName"
