from jambase_api.APISections.base import JamBaseBase


class JamBaseVenues(JamBaseBase):
    def search_by_name(self, venue_name, **kwargs):
        """Search for venues by name"""
        kwargs["venueName"] = venue_name
        return self.call_api_get("venues", kwargs=kwargs)

    def search_by_city(self, city_id, **kwargs):
        """Search for venues by city"""
        kwargs["getCityId"] = city_id
        return self.call_api_get("venues", kwargs=kwargs)

    def get_venue(self, venue_data_source, venue_id, **kwargs):
        """Get venue data by data source and id"""
        return self.call_api_get("venues/id/"+venue_data_source+":"+venue_id, kwargs=kwargs)
