from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum
from src.features.orders.domain.print_order_states import PrintOrderState


class PrintOrder(Base):
    __tablename__ = "print_orders"

    status: Mapped[PrintOrderState] = mapped_column(
        Enum(PrintOrderState),
        nullable=False,
        default=PrintOrderState.PENDING,
    )

    jobs: Mapped[list["PrintJob"]] = relationship(
        back_populates="print_order",
        cascade="all, delete-orphan",
    )
