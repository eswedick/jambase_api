from jambase_api.Enums.event_data_source import EventDataSource
from jambase_api.Enums.stream_data_source import StreamDataSource
from jambase_api.Enums.artist_data_source import ArtistDataSource
from jambase_api.Enums.venue_data_source import VenueDataSource


def test_event_data_sources(jambase):
    json = jambase.get_event_data_sources()["dataSources"]

    response_sources = [source["identifier"] for source in json]

    for value in EventDataSource:
        assert value.value in response_sources

    for source in response_sources:
        assert any(member.value == source for member in EventDataSource)


def test_stream_data_sources(jambase):
    json = jambase.get_stream_data_sources()["dataSources"]

    response_sources = [source["identifier"] for source in json]

    for value in StreamDataSource:
        assert value.value in response_sources

    for source in response_sources:
        assert any(member.value == source for member in StreamDataSource)


def test_artist_data_sources(jambase):
    json = jambase.get_arist_data_sources()["dataSources"]

    response_sources = [source["identifier"] for source in json]

    for value in ArtistDataSource:
        assert value.value in response_sources

    for source in response_sources:
        assert any(member.value == source for member in ArtistDataSource)


def test_venue_data_sources(jambase):
    json = jambase.get_venue_data_sources()["dataSources"]

    response_sources = [source["identifier"] for source in json]

    for value in VenueDataSource:
        assert value.value in response_sources

    for source in response_sources:
        assert any(member.value == source for member in VenueDataSource)

