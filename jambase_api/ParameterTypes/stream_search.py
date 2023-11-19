from enum import Enum


class StreamSearch(Enum):
    """List of possible parameters to pass into the Stream API section"""

    artistId = "artistId"
    artistName = "artistName"
    dateModifiedFrom = "dateModifiedFrom"
    datePublishedFrom = "datePublishedFrom"
    eventDateFrom = "eventDateFrom"
    eventDatePreset = "eventDatePreset"
    eventDateTo = "eventDateTo"
    expandArtistSameAs = "expandArtistSameAs"
    expandExternalIdentifiers = "expandExternalIdentifiers"
    streamDataSource = "streamDataSource"
