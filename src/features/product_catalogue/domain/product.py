from dataclasses import dataclass
from uuid import UUID, uuid4
from src.features.product_catalogue.domain.product_states import ProductState
from decimal import Decimal


@dataclass
class Product:
    id: UUID
    product_name: str
    unit_price: Decimal
    status: ProductState
    available_stock: int

    @classmethod
    def create(cls, *, product_name: str, unit_price: Decimal, available_stock: int):
        if unit_price <= 0 or not unit_price:
            raise ValueError("Invalid Unit price for product")
        return cls(
            id=uuid4(),
            product_name=product_name,
            status=ProductState.AVAILABLE,
            unit_price=unit_price,
            available_stock=available_stock,
        )

    def update(self, *, product_name: str | None, unit_price: Decimal | None):

        if product_name and product_name.strip() == "":
            raise ValueError("Invalid Product Name")

        if unit_price and unit_price <= 0:
            raise ValueError("Invalid Product Price")

        if unit_price:
            self.unit_price = unit_price

        if product_name:
            self.product_name = product_name

    def restock(self, quantity: int):
        if quantity <= 0:
            raise ValueError("Invalid Product Quantity added")

        if self.status == ProductState.OUT_OF_STOCK:
            self.mark_as_available()

        self.available_stock += quantity
        return self.available_stock

    def reduce_stock(self, quantity: int):
        if self.status == ProductState.OUT_OF_STOCK:
            raise ValueError("Product is out of stock")

        if self.available_stock < quantity:
            raise ValueError("Not Enough in stock, please refill")

        self.available_stock -= quantity

        if self.available_stock == 0:
            self.mark_out_of_stock()
        return self.available_stock

    def mark_out_of_stock(self):
        """may add some events later from this"""
        self.status = ProductState.OUT_OF_STOCK

    def mark_as_non_available(self):
        """may add some events later from this"""

        self.status = ProductState.NON_AVAILABLE

    def mark_as_available(self):
        self.status = ProductState.AVAILABLE
