from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, UUID, String, Integer, Enum
import uuid
from src.infra.db.base import Base
from src.features.orders.domain.print_job_states import PrintJobState


class PrintJob(Base):
    __tablename__ = "print_jobs"

    product_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=True,
    )

    product: Mapped["Product"] = relationship(back_populates="print_jobs")

    quantity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    status: Mapped[PrintJobState] = mapped_column(
        Enum(PrintJobState),
        default=PrintJobState.PENDING,
    )

    print_order_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("print_orders.id"), nullable=False
    )
    print_order: Mapped["PrintOrder"] = relationship(back_populates="jobs")
