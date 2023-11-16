from enum import Enum


class EventStatus(Enum):
    SCHEDULED = "scheduled"
    POSTPONED = "postponed"
    RESCHEDULED = "rescheduled"
    CANCELLED = "cancelled"
