from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.orders.domain.print_order_states import PrintOrderState
from src.features.orders.domain.print_job import PrintJob


@dataclass
class PrintOrder:
    id: UUID
    print_jobs: list[PrintJob]
    status: PrintOrderState

    @classmethod
    def create(cls) -> "PrintOrder":
        order = cls(
            id=uuid4(),
            print_jobs=[],
            status=PrintOrderState.PENDING,
        )
        return order

    def add_jobs(self, jobs: list[PrintJob]):
        self.print_jobs = jobs

    @property
    def total_price(self):
        total: int = 0
        for job in self.print_jobs:
            total += job.price * job.quantity
        return total

    def confirm_order(self):
        if self.status != PrintOrderState.PENDING:
            raise ValueError(
                "Cannot confirm a non pending order",
            )

        for job in self.print_jobs:
            job.push_to_print_queue()

        self.status = PrintOrderState.CONFIRMED

    def start_printing(self):
        return
