from pydantic import BaseModel
from src.features.product_catalogue.domain.product_states import ProductState


class ProductFilters(BaseModel):
    status: ProductState | None = None
