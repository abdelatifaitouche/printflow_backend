from pydantic import BaseModel
from uuid import UUID


class CreateJobCommand(BaseModel):
    product_id: UUID
    quantity: int


class CreateOrderCommand(BaseModel):
    jobs: list[CreateJobCommand]
