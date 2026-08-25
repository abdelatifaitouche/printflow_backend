from enum import StrEnum


class PrintOrderState(StrEnum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    DELIVRED = "DELIVRED"
    CANCELLED = "CANCELLED"
