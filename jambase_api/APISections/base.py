import urllib.parse

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
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "Python_JamBase_API/1.0 (eswedick@gmail.com)",
        }
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
        params_string = urllib.parse.urlencode(args)
        url_with_params = "%s?apikey=%s%s" % (
            url,
            self.api_key,
            "&" + params_string if params_string else "",
        )

        response = self.req.get(
            url_with_params,
            headers=self.headers,
            verify=self.ssl_verify,
            cert=self.cert,
            proxies=self.proxies,
            timeout=self.timeout,
        )

        # return response.json()
        return self.remove_chars_from_keys(response.json(), "@-")

    @staticmethod
    def remove_chars_from_keys(obj, chars_to_remove):
        if isinstance(obj, dict):
            new_obj = {}
            for key, value in obj.items():
                new_key = key.translate(str.maketrans("", "", chars_to_remove))
                new_obj[new_key] = JamBaseBase.remove_chars_from_keys(
                    value, chars_to_remove
                )
            return new_obj
        elif isinstance(obj, list):
            return [
                JamBaseBase.remove_chars_from_keys(item, chars_to_remove)
                for item in obj
            ]
        else:
            return obj
