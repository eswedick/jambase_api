from .base import JamBaseBase


class JamBaseArtists(JamBaseBase):
    def search_by_artist_name(self, artist_name, **kwargs):
        """Search for artists by name"""
        kwargs["artistName"] = artist_name
        return self.call_api_get("artists", kwargs=kwargs)

    def search_by_genre(self, genre, **kwargs):
        """Search for artists by genre. Valid values are contained in Enums.Genre"""
        kwargs["genreSlug"] = genre.value
        return self.call_api_get("artists", kwargs=kwargs)

    def get_artist(self, artist_data_source, artist_id, **kwargs):
        """Gets an artist data by data source and id"""
        return self.call_api_get(
            "artists/id/" + artist_data_source + ":" + str(artist_id), kwargs=kwargs
        )
