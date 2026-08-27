from fastapi import Depends

from src.features.orders.infra.print_order_repository import PrintOrderRepository

from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.session import get_db
from src.features.orders.application.print_order_uc import PrintOrderUC
from src.infra.db.unit_of_work import UnitOfWork


def get_uc(db: AsyncSession = Depends(get_db)) -> PrintOrderUC:
    repo: PrintOrderRepository = PrintOrderRepository(db)
    uow: UnitOfWork = UnitOfWork(db)
    return PrintOrderUC(uow, repo)
