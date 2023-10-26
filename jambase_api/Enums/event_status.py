from enum import Enum


class EventStatus(Enum):
    scheduled = "scheduled"
    postponed = "postponed"
    rescheduled = "rescheduled"
    cancelled = "cancelled"