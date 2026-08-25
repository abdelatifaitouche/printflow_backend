from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class PrintJobDTO:
    quantity: int
    product_id: UUID


@dataclass(frozen=True)
class PrintOrderDTO:
    jobs: list[PrintJobDTO]
