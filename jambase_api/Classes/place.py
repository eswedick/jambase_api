from dataclasses import dataclass, field


@dataclass
class Place:
    type: str = field(metadata={"name": "@type"})
    name: str
