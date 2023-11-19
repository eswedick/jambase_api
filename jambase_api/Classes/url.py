from dataclasses import dataclass

from ..Enums import url_type


@dataclass
class Url:
    identifier: url_type
    url: str
