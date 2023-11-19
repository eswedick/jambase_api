from enum import Enum


class EventSearch(Enum):
    """List of possible parameters to pass into the Event API section"""

    artistHasUpcomingEvents = "artistHasUpcomingEvents"
    dateModifiedFrom = "dateModifiedFrom"
    datePublishedFrom = "datePublishedFrom"
    expandExternalIdentifiers = "expandExternalIdentifiers"
    page = "page"
    perPage = "perPage"
