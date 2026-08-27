from src.features.product_catalogue.application.ports.product_repository import (
    IProductRepository,
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID, uuid4
from src.features.product_catalogue.infra.models.product import Product as ProductDB
from src.features.product_catalogue.domain.product import Product as ProductEntity


class ProductRepository(IProductRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    def _to_orm(self, product: ProductEntity) -> ProductDB:
        return ProductDB(
            id=product.id,
            product_name=product.product_name,
            unit_price=product.unit_price,
            status=product.status,
            available_quantity=product.available_stock,
        )

    def _to_domain(self, orm: ProductDB) -> ProductEntity:
        return ProductEntity(
            id=orm.id,
            product_name=orm.product_name,
            unit_price=orm.unit_price,
            available_stock=orm.available_quantity,
            status=orm.status,
        )

    async def get(self, product_id: UUID) -> ProductEntity | None:
        stmt = select(ProductDB).where(ProductDB.id == product_id)
        product = (await self.session.execute(stmt)).scalar_one_or_none()

        if not product:
            return None

        return self._to_domain(product)

    async def save(self, product: ProductEntity) -> ProductEntity:
        existing = await self.session.get(ProductDB, product.id)

        if existing is not None:
            existing.product_name = product.product_name
            existing.unit_price = product.unit_price
            existing.status = product.status
            existing.available_quantity = product.available_stock
        else:
            existing = self._to_orm(product)
            self.session.add(existing)

        await self.session.flush()
        return self._to_domain(existing)
