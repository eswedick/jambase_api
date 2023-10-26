from enum import Enum


class AttendanceMode(Enum):
    offline = "offline"
    online = "online"
    mixed = "mixed"