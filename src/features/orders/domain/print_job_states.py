from enum import StrEnum


class PrintJobState(StrEnum):
    PENDING = "PENDING"
    WAIT_FOR_PRINTING = "WAIT_FOR_PRINTING"
    READY = "READY"
    CANCELLED = "CANCELLED"
