from jambase_api.Enums.artist_data_source import ArtistDataSource
from jambase_api.Classes.music_group import MusicGroup
from jambase_api.Enums.genre import Genre


def test_get_artist(jambase):
    response = jambase.get_artist(ArtistDataSource.JAMBASE.value, 41232)

    artist = MusicGroup(**response["artist"])

    assert artist


def test_search_by_genre(jambase):
    response = jambase.search_by_genre(Genre.JAM_BAND)

    artists = [MusicGroup(**artist) for artist in response["artists"]]

    assert artists


def test_search_by_artist_name(jambase):
    response = jambase.search_by_artist_name("phish")

    artists = [MusicGroup(**artist) for artist in response["artists"]]

    assert artists

