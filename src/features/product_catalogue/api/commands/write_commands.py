from pydantic import BaseModel
from decimal import Decimal
from src.features.product_catalogue.domain.product_states import ProductState


class CreateProductCommand(BaseModel):
    product_name: str
    unit_price: Decimal
    stock_init: int


class UpdateProductCommand(BaseModel):
    product_name: str | None = None
    unit_price: Decimal | None = None


class UpdateProductStateCommand(BaseModel):
    status: ProductState
