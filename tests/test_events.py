from jambase_api.Classes.event import Event
from jambase_api.Enums.event_data_source import EventDataSource


def test_search_events_by_artist_name(jambase):
    response = jambase.get_events_by_artist_name("taylor swift")

    events = [Event(**event) for event in response["events"]]

    assert events


def test_get_event(jambase):
    res = jambase.get_events_by_artist_name("adele")
    events = [Event(**event) for event in res["events"]]

    response = jambase.get_event(EventDataSource.JAMBASE.value, events[0].identifier.split(':')[1])

    event = Event(**response["event"])

    assert event


def test_search_by_venue_name(jambase):
    res = jambase.search_by_venue_name("Madison Square Garden")
    events = [Event(**event) for event in res["events"]]

    assert events


def test_get_events_for_artist(jambase):
    res = jambase.get_events_by_artist(EventDataSource.JAMBASE.value, "44745")
    events = [Event(**event) for event in res["events"]]

    assert events


def test_get_events_by_city(jambase):
    res = jambase.get_events_by_city("4223296")
    events = [Event(**event) for event in res["events"]]

    assert events
