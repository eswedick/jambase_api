from .base import JamBaseBase


class JamBaseDataSources(JamBaseBase):
    def get_event_data_sources(self):
        """Returns all Event Data Sources in Alphabetical order"""
        return self.call_api_get("lookups/event-data-sources/")

    def get_stream_data_sources(self):
        """Returns all Stream Data Sources in Alphabetical order"""
        return self.call_api_get("lookups/stream-data-sources/")

    def get_arist_data_sources(self):
        """Returns all Artist Data Sources in Alphabetical order"""
        return self.call_api_get("lookups/artist-data-sources/")

    def get_venue_data_sources(self):
        """Returns all Venue Data Sources in Alphabetical order"""
        return self.call_api_get("lookups/venue-data-sources/")
