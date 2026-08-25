from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID
from src.features.product_catalogue.domain.product_states import ProductState
from datetime import datetime


@dataclass(frozen=True)
class UpdateProduct:
    product_name: str | None = None
    unit_price: Decimal | None = None


@dataclass(frozen=True)
class CreateProduct:
    product_name: str
    unit_price: Decimal
    stock_init: int


@dataclass
class ProductListDTO:
    id: UUID
    product_name: str
    unit_price: Decimal
    stock: int
    status: ProductState


@dataclass
class ProductRead:
    id: UUID
    product_name: str
    unit_price: Decimal
    stock: int
    status: ProductState
    created_at: datetime
    updated_at: datetime
