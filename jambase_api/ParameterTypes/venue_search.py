from enum import Enum


class VenueSearch(Enum):
    """List of possible parameters to pass into the Venue API section"""

    artistHasUpcomingEvents = "artistHasUpcomingEvents"
    dateModifiedFrom = "dateModifiedFrom"
    datePublishedFrom = "datePublishedFrom"
    expandExternalIdentifiers = "expandExternalIdentifiers"
    page = "page"
    perPage = "perPage"
