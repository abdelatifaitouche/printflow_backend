from pydantic import BaseModel
from typing import Any


class Pagination(BaseModel):
    page: int = 1
    size: int = 10

    @property
    def offset(self):
        return (self.page - 1) * self.size


class PaginatedResult(BaseModel):
    page: int
    size: int
    total: int
    items: list[Any]

    model_config = {
        "from_attributes": True,
    }
