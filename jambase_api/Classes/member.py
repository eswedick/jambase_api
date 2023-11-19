from dataclasses import dataclass


@dataclass
class Member:
    type: str
    name: str
    identifier: str
    image: str
    url: str
