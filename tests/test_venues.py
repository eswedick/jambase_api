from jambase_api.Classes.music_venue import MusicVenue
from jambase_api.Enums.venue_data_source import VenueDataSource


def test_search_by_name(jambase):
    response = jambase.search_venue_by_name('Madison Square Garden')

    venues = [MusicVenue(**venue) for venue in response["venues"]]

    assert venues


def test_get_venue(jambase):
    response = jambase.get_venue(VenueDataSource.JAMBASE.value, '62108')

    venue = MusicVenue(**response["venue"])

    assert venue

