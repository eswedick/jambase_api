from jambase_api.Classes.stream import Stream
from jambase_api.Enums.stream_data_source import StreamDataSource


def test_search_stream_by_name(jambase):
    response = jambase.search_streams()
    streams = [Stream(**stream) for stream in response["streams"]]

    assert streams


def test_get_stream(jambase):
    response = jambase.get_stream(StreamDataSource.JAMBASE.value, "11197143")

    stream = Stream(**response["stream"])

    assert stream
