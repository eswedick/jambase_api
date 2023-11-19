from .base import JamBaseBase


class JamBaseEvents(JamBaseBase):
    def search_by_venue_name(self, venue_name, **kwargs):
        """Search for events by venue"""
        kwargs["venueName"] = venue_name
        return self.call_api_get("events", kwargs=kwargs)

    def get_events_by_artist_name(self, artist_name, **kwargs):
        """Search for events by artist name"""
        kwargs["artistName"] = artist_name
        return self.call_api_get("events", kwargs=kwargs)

    def get_events_by_artist(self, artist_data_source, artist_id, **kwargs):
        """Search for events by artist"""
        kwargs["artistId"] = artist_data_source + ":" + artist_id
        return self.call_api_get("events", kwargs=kwargs)

    def get_events_by_city(self, city_id, **kwargs):
        """Search for events by city."""
        kwargs["geoCityId"] = "jambase:" + str(city_id)
        return self.call_api_get("events", kwargs=kwargs)

    def get_event(self, event_data_source, event_id, **kwargs):
        """Get event data by data source and id"""
        return self.call_api_get(
            "events/id/" + event_data_source + ":" + event_id, kwargs=kwargs
        )
