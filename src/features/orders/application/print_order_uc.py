from src.features.orders.domain.print_order import PrintOrder
from src.features.orders.domain.print_job import PrintJob
from src.features.orders.application.dtos.print_order import PrintOrderDTO, PrintJobDTO
from src.features.orders.infra.print_order_repository import IPrintOrderRepository
from src.core.shared.interfaces.unit_of_work import IUnitOfWork


class PrintOrderUC:
    def __init__(self, uow: IUnitOfWork, print_order_repository: IPrintOrderRepository):
        self.print_order_repository = print_order_repository
        self.uow: IUnitOfWork = uow

    async def place_new_order(self, data: PrintOrderDTO) -> PrintOrder:
        async with self.uow:
            print_order = PrintOrder.create()
            jobs = [
                PrintJob.create(
                    product_id=job.product_id,
                    quantity=job.quantity,
                    print_order_id=print_order.id,
                )
                for job in data.jobs
            ]

            print_order.add_jobs(jobs)

            print_order = await self.print_order_repository.save(print_order)
        return print_order
