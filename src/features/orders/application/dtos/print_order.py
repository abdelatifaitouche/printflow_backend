from dataclasses import dataclass


@dataclass(frozen=True)
class PrintJobDTO:
    price: int
    quantity: int


@dataclass(frozen=True)
class PrintOrderDTO:
    jobs: list[PrintJobDTO]
