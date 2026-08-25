from src.infra.db.base import Base
from sqlalchemy import String, Integer, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.features.product_catalogue.domain.product_states import ProductState

from decimal import Decimal


class Product(Base):
    __tablename__ = "products"

    product_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2),
        nullable=False,
    )
    available_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )
    status: Mapped[ProductState] = mapped_column(
        Enum(ProductState), nullable=False, default=ProductState.AVAILABLE
    )

    print_jobs: Mapped[list["PrintJob"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
    )
