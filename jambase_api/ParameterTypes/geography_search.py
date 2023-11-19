from enum import Enum


class GeographySearch(Enum):
    """List of possible parameters to pass into the Geography API section"""

    artistHasUpcomingEvents = "artistHasUpcomingEvents"
    dateModifiedFrom = "dateModifiedFrom"
    datePublishedFrom = "datePublishedFrom"
    expandExternalIdentifiers = "expandExternalIdentifiers"
    page = "page"
    perPage = "perPage"
