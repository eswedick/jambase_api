from .base import JamBaseBase


class JamBaseGenres(JamBaseBase):
    def get_genres(self):
        """Returns all Genres in Alphabetical order"""
        return self.call_api_get("genres")
