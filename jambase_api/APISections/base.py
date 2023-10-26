import requests


class JamBaseBase:
    def __init__(
            self,
            api_key=None,
            server_url="https://www.jambase.com/jb-api/v1/",
            ssl_verify=True,
            proxies=None,
            timeout=30,
            session=None,
            client_certs=None,
    ):

        self.headers = {"Accept": "application/json", "User-Agent": "Python_JamBase_API/1.0 (eswedick@gmail.com)"}
        self.api_key = api_key
        self.server_url = server_url
        self.proxies = proxies
        self.ssl_verify = ssl_verify
        self.cert = client_certs
        self.timeout = timeout
        self.req = session or requests

    @staticmethod
    def __reduce_kwargs(kwargs):
        if "kwargs" in kwargs:
            for arg in kwargs["kwargs"].keys():
                kwargs[arg] = kwargs["kwargs"][arg]

            del kwargs["kwargs"]
        return kwargs

    def call_api_get(self, method, **kwargs):
        args = self.__reduce_kwargs(kwargs)
        url = self.server_url + method
        # convert to key[]=val1&key[]=val2 for args like key=[val1, val2], else key=val
        params = "&".join(
            "&".join(i + "[]=" + j for j in args[i])
            if isinstance(args[i], list)
            else i + "=" + str(args[i])
            for i in args
        )
        return self.req.get(
            "%s?%s" % (url, params) + "apikey=" + self.api_key,
            headers=self.headers,
            verify=self.ssl_verify,
            cert=self.cert,
            proxies=self.proxies,
            timeout=self.timeout,
        )
