from dataclasses import dataclass, field


@dataclass
class Member:
    type: str = field(metadata={"name": "@type"})
    name: str
    identifier: str
    image: str
    url: str
