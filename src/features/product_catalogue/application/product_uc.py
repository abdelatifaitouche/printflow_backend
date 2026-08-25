from src.features.product_catalogue.infra.repositories.product_repository import (
    IProductRepository,
)
from src.core.shared.interfaces.unit_of_work import IUnitOfWork
from src.features.product_catalogue.domain.product import Product
from src.features.product_catalogue.application.dtos.product import (
    CreateProduct,
    UpdateProduct,
)
from src.features.product_catalogue.domain.product_states import ProductState
from uuid import UUID


class ProductUC:
    def __init__(self, uow: IUnitOfWork, product_repo: IProductRepository):
        self.product_repo = product_repo
        self.uow = uow

    async def create_product(self, data: CreateProduct) -> Product:
        product = Product.create(
            product_name=data.product_name,
            unit_price=data.unit_price,
            available_stock=data.stock_init,
        )
        async with self.uow:
            product = await self.product_repo.save(product)
            return product

    async def update_product(self, product_id: UUID, data: UpdateProduct):
        product: Product | None = await self.product_repo.get(product_id)

        if not product:
            raise ValueError(f"Product with ID {product_id} Not Found")

        async with self.uow:
            product.update(
                product_name=data.product_name,
                unit_price=data.unit_price,
            )
            product = await self.product_repo.save(product)
        return product

    async def update_product_state(self, product_id: UUID, product_state: ProductState):
        async with self.uow:
            product: Product | None = await self.product_repo.get(product_id)

            if not product:
                raise ValueError("Product Not Found")

            match product_state:
                case ProductState.NON_AVAILABLE:
                    product.mark_as_non_available()
                case ProductState.AVAILABLE:
                    product.mark_as_available()
                case ProductState.OUT_OF_STOCK:
                    product.mark_out_of_stock()
                case _:
                    raise ValueError("Unkonw state")

            product = await self.product_repo.save(product)

        return product
