from dataclasses import dataclass


@dataclass
class ExternalIdentifier:
    source: str
    identifier: str
