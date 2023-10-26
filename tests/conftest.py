import pytest
import os
from jambase_api.jambase import JamBase
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def jambase():
    _jambase = JamBase(api_key=os.getenv('API_KEY'))
    return _jambase
