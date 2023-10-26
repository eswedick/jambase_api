from dataclasses import dataclass


@dataclass
class GeoCoordinates:
    type: str
    latitude: float
    longitude: float
