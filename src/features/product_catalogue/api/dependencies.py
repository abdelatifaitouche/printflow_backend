from fastapi import Depends
from src.features.product_catalogue.infra.repositories.product_repository import (
    ProductRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.session import get_db
from src.infra.db.unit_of_work import UnitOfWork
from src.features.product_catalogue.application.product_uc import ProductUC
from src.features.product_catalogue.services.product_query_service import (
    ProductQueryService,
)


def get_uc(db: AsyncSession = Depends(get_db)) -> ProductUC:
    product_repo: ProductRepository = ProductRepository(session=db)
    uow = UnitOfWork(session=db)
    return ProductUC(uow, product_repo)


def get_query_service(db: AsyncSession = Depends(get_db)):
    return ProductQueryService(db)
