import pytest
import os
from jambase_api.jambase import JamBase
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def test_get_genres():
    _jambase = JamBase(api_key=os.getenv('API_KEY'))
    genres = _jambase.get_genres()

    try:
        response_json = genres.json()
    except genres.JSONDecodeError:
        pytest.fail("Response content is not valid JSON")

    assert 'genres' in response_json
