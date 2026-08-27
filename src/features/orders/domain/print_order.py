from uuid import UUID, uuid4

from src.features.orders.domain.print_order_states import PrintOrderState
from src.features.orders.domain.print_job import PrintJob

from typing import Self


class PrintOrder:
    def __init__(self, id: UUID, print_jobs: list[PrintJob], status: PrintOrderState):
        self.id: UUID = id
        self.print_jobs: list[PrintJob] = print_jobs
        self.status: PrintOrderState = status

    @classmethod
    def create(cls) -> Self:
        order = cls(
            id=uuid4(),
            print_jobs=[],
            status=PrintOrderState.PENDING,
        )
        return order

    @property
    def total_price(self):
        return sum(job.price for job in self.print_jobs)

    def confirm_order(self):
        if self.status != PrintOrderState.PENDING:
            raise ValueError(
                "Cannot confirm a non pending order",
            )

        if not self.print_jobs:
            raise ValueError(
                "Cannot confirm an order without jobs",
            )

        for job in self.print_jobs:
            job.push_to_print_queue()

        self.status = PrintOrderState.CONFIRMED
