import pytest


def test_get_genres(jambase):
    genres = jambase.get_genres()

    try:
        response_json = genres.json()
    except genres.JSONDecodeError:
        pytest.fail("Response content is not valid JSON")

    assert 'genres' in response_json
