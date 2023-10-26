from jambase_api.APISections.base import JamBaseBase
from jambase_api.Classes.stream import Stream


class JamBaseStreams(JamBaseBase):
    def search_by_artist_name(self, **kwargs):
        """Search upcoming streams"""
        return self.call_api_get("streams/", kwargs=kwargs)

    def get_stream(self, stream_data_source, stream_id, **kwargs):
        """Gets upcoming stream data by data source and id"""
        return Stream(**self.call_api_get("stream/id/"+stream_data_source+":"+stream_id, kwargs=kwargs))
