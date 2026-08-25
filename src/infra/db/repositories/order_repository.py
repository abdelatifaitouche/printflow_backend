from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.features.orders.domain.print_job import PrintJob as JobEntity
from src.features.orders.domain.print_order import PrintOrder as OrderEntity
from src.features.orders.infra.models.print_job import PrintJob as JobDB
from src.features.orders.infra.models.print_order import PrintOrder as OrderDB
from src.features.orders.infra.print_order_repository import IPrintOrderRepository


class PrintOrderRepository(IPrintOrderRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def _job_to_orm(self, job: JobEntity) -> JobDB:
        return JobDB(
            id=job.id,
            product_id=job.product_id,
            status=job.status,
            print_order_id=job.print_order_id,
            quantity=job.quantity,
        )

    def _job_to_domain(self, job: JobDB) -> JobEntity:
        return JobEntity(
            id=job.id,
            product_id=job.product_id,
            status=job.status,
            print_order_id=job.print_order_id,
            quantity=job.quantity,
        )

    def _order_to_domain(self, order: OrderDB) -> OrderEntity:
        return OrderEntity(
            id=order.id,
            status=order.status,
            print_jobs=[self._job_to_domain(job) for job in order.jobs],
        )

    async def get(self, order_id: UUID) -> OrderEntity | None:
        stmt = (
            select(OrderDB)
            .where(OrderDB.id == order_id)
            .options(selectinload(OrderDB.jobs))
        )
        order = (await self.db.execute(stmt)).scalar_one_or_none()
        if not order:
            return None
        return self._order_to_domain(order)

    async def save(self, order: OrderEntity) -> OrderEntity:
        stmt = (
            select(OrderDB)
            .where(OrderDB.id == order.id)
            .options(selectinload(OrderDB.jobs))
        )
        order_db = (await self.db.execute(stmt)).scalar_one_or_none()

        if order_db is None:
            # --- create path ---
            order_db = OrderDB(id=order.id, status=order.status)
            order_db.jobs = [self._job_to_orm(job) for job in order.print_jobs]
            self.db.add(order_db)
        else:
            # --- update path ---
            order_db.status = order.status

            existing_jobs_by_id = {job.id: job for job in order_db.jobs}
            incoming_ids = {job.id for job in order.print_jobs}

            for job in order.print_jobs:
                existing_job = existing_jobs_by_id.get(job.id)
                if existing_job is not None:
                    # update in place - keeps it tracked, no duplicate insert
                    existing_job.product_id = job.product_id
                    existing_job.status = job.status
                    existing_job.quantity = job.quantity
                else:
                    # new job on this order - append to the collection so
                    # SQLAlchemy's cascade handles the insert on flush
                    order_db.jobs.append(self._job_to_orm(job))

            # jobs removed from the domain entity get removed from the ORM
            # collection too, so the "delete-orphan" cascade actually fires -
            # deleting from the session directly is NOT enough, SQLAlchemy
            # only cascades deletes for items detached from the parent's
            # own collection.
            order_db.jobs = [
                job for job in order_db.jobs if job.id in incoming_ids or job.id is None
            ]

        await self.db.flush()
        return self._order_to_domain(order_db)
