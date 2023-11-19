from .base import JamBaseBase


class JamBaseGeographies(JamBaseBase):
    def search_cities(self, **kwargs):
        """Search for cities. Results will be returned in order of most to least upcoming events in the city,
        and then alphabetically city name in the case of a tie."""
        return self.call_api_get("geographies/cities", kwargs=kwargs)

    def get_metros(self, **kwargs):
        """Returns all Metros in Alphabetical order by identifier"""
        return self.call_api_get("geographies/metros", kwargs=kwargs)

    def get_states(self, **kwargs):
        """Returns all States/Regions in Alphabetical order by identifier"""
        return self.call_api_get("geographies/states", kwargs=kwargs)

    def get_countries(self, **kwargs):
        """Returns all Countries in alphabetical order by ISO2"""
        return self.call_api_get("geographies/countries", kwargs=kwargs)
