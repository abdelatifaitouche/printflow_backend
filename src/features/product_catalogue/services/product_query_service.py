from sqlalchemy.ext.asyncio import AsyncSession
from src.features.product_catalogue.infra.models.product import Product as ProductDB
from src.features.product_catalogue.application.dtos.product import (
    ProductListDTO,
    ProductRead,
)
from src.api.utils.pagination import Pagination, PaginatedResult
from src.features.product_catalogue.api.filters.product_filters import ProductFilters
from sqlalchemy import select, Select, func
from uuid import UUID
from typing import Any


class ProductQueryService:
    def __init__(self, db: AsyncSession):
        self.db: AsyncSession = db

    def _apply_filters(self, stmt: Select[Any], filters: ProductFilters) -> Select[Any]:

        if filters.status:
            stmt = stmt.where(ProductDB.status == filters.status)

        return stmt

    def _apply_pagination(self, stmt: Select[Any], pagination: Pagination):
        return stmt.offset(pagination.offset).limit(pagination.size)

    async def list(
        self, pagination: Pagination, filters: ProductFilters
    ) -> PaginatedResult:
        stmt = select(
            ProductDB.id,
            ProductDB.product_name,
            ProductDB.available_quantity,
            ProductDB.unit_price,
            ProductDB.status,
        )

        count_stmt = select(func.count()).select_from(ProductDB)

        count_stmt = self._apply_filters(count_stmt, filters)

        total: int = await self.db.scalar(count_stmt) or 0

        if total == 0:
            return PaginatedResult(
                page=pagination.page,
                size=pagination.size,
                total=total,
                items=[],
            )

        stmt = self._apply_filters(stmt, filters)

        stmt = self._apply_pagination(stmt, pagination)

        stmt = stmt.order_by(ProductDB.created_at)

        results = (await self.db.execute(stmt)).all()

        items: list[ProductListDTO] = [
            ProductListDTO(
                id=product.id,
                product_name=product.product_name,
                unit_price=product.unit_price,
                stock=product.available_quantity,
                status=product.status,
            )
            for product in results
        ]

        return PaginatedResult(
            page=pagination.page,
            size=pagination.size,
            total=total,
            items=items,
        )

    async def get_product_details(self, product_id: UUID):
        stmt = select(ProductDB).where(ProductDB.id == product_id)

        result = (await self.db.execute(stmt)).scalar_one_or_none()

        if not result:
            return None

        return ProductRead(
            id=result.id,
            product_name=result.product_name,
            unit_price=result.unit_price,
            status=result.status,
            stock=result.available_quantity,
            created_at=result.created_at,
            updated_at=result.updated_at,
        )
