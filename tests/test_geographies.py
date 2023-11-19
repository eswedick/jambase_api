from jambase_api.Classes.administrative_area import Metro
from jambase_api.Enums.state import StateCode
from jambase_api.Enums.country_iso2 import CountryCodeIso2


def test_search_cities(jambase):
    pass


def test_get_metros(jambase):
    json = jambase.get_metros()["metros"]

    metros = [Metro(**metro_data) for metro_data in json]

    assert metros


def test_get_states(jambase):
    json = jambase.get_states()["states"]

    response_states = [state["identifier"] for state in json]

    for value in StateCode:
        assert value.value in response_states

    for state in response_states:
        assert any(member.value == state for member in StateCode)


def test_get_countries(jambase):
    json = jambase.get_countries()["countries"]

    response_countries = [country["identifier"] for country in json]

    for value in CountryCodeIso2:
        assert value.value in response_countries

    for country in response_countries:
        try:
            assert any(member.value == country for member in CountryCodeIso2)
        except AssertionError as e:
            print("Country in response not in Enum: {country}", country)
