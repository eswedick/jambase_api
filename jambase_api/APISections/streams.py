from .base import JamBaseBase


class JamBaseStreams(JamBaseBase):
    def search_streams(self, **kwargs):
        """Search upcoming streams"""
        return self.call_api_get("streams/", kwargs=kwargs)

    def get_stream(self, stream_data_source, stream_id, **kwargs):
        """Gets upcoming stream data by data source and id"""
        return self.call_api_get(
            "streams/id/" + stream_data_source + ":" + stream_id, kwargs=kwargs
        )
