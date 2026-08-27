from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.orders.domain.print_job_states import PrintJobState


class PrintJob:
    def __init__(
        self,
        id: UUID,
        product_id: UUID,
        quantity: int,
        status: PrintJobState,
        print_order_id: UUID,
    ):
        self.id = id
        self.product_id = product_id
        self.quantity = quantity
        self.status = status
        self.print_order_id = print_order_id

    @classmethod
    def create(cls, product_id: UUID, quantity: int, print_order_id: UUID):

        if not quantity or quantity <= 0:
            raise ValueError(
                "Invalid Quantity",
            )

        return cls(
            id=uuid4(),
            product_id=product_id,
            quantity=quantity,
            print_order_id=print_order_id,
            status=PrintJobState.PENDING,
        )

    @property
    def price(self):
        return (
            self.quantity * 10
        )  # the 10 here is temporary it should reflect the product selected price

    def push_to_print_queue(self):
        if self.status != PrintJobState.PENDING:
            raise ValueError(
                "Cannot push a none pending job to queue",
            )
        self.status = PrintJobState.WAIT_FOR_PRINTING
