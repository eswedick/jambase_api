from jambase_api.Enums.genre import Genre


def test_get_genres(jambase):
    json = jambase.get_genres()["genres"]

    response_genres = [genre["identifier"] for genre in json]

    for value in Genre:
        assert value.value in response_genres
