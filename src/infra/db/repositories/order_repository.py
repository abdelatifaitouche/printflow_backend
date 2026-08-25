from src.features.orders.infra.print_order_repository import IPrintOrderRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.orders.infra.models.print_job import PrintJob as JobDB
from src.features.orders.infra.models.print_order import PrintOrder as OrderDB
from src.features.orders.domain.print_order import PrintOrder as OrderEntity
from src.features.orders.domain.print_job import PrintJob as JobEntity


class PrintOrderRepository(IPrintOrderRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def _to_orm(self):
        return

    def _to_domain(self):
        return

    async def get(self):
        return

    async def save(self, order: OrderEntity):
        order_db = OrderDB(id=order.id, status=order.status)

        jobs_db = [
            JobDB(
                id=job.id,
                product_id=job.product_id,
                status=job.status,
                print_order_id=job.print_order_id,
                quantity=job.quantity,
            )
            for job in order.print_jobs
        ]
        self.db.add_all([order_db, *jobs_db])
        await self.db.flush()
        return order
