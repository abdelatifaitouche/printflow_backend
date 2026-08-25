from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.orders.domain.print_job_states import PrintJobState


@dataclass
class PrintJob:
    id: UUID
    product: str
    quantity: int
    status: PrintJobState
    print_order_id: UUID

    @classmethod
    def create(cls, product: str, quantity: int, print_order_id: UUID):

        if not quantity or quantity <= 0:
            raise ValueError(
                "Invalid Quantity",
            )

        return cls(
            id=uuid4(),
            product=product,
            quantity=quantity,
            print_order_id=print_order_id,
            status=PrintJobState.WAIT_FOR_PRINTING,
        )

    @property
    def price(self):
        return self.quantity * 10

    def push_to_print_queue(self):
        if self.status != PrintJobState.PENDING:
            raise ValueError(
                "Cannot push a none pending job to queue",
            )
        self.status = PrintJobState.WAIT_FOR_PRINTING
