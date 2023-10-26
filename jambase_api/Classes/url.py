from dataclasses import dataclass

from jambase_api.Enums import url_type


@dataclass
class Url:
    identifier: url_type
    url: str
