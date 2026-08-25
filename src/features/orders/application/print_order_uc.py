from src.features.orders.domain.print_order import PrintOrder
from src.features.orders.domain.print_job import PrintJob
from src.features.orders.application.dtos.print_order import PrintOrderDTO, PrintJobDTO
from src.features.orders.infra.print_order_repository import PrintOrderRepository
from src.core.shared.interfaces.unit_of_work import IUnitOfWork


class PrintOrderUC:
    def __init__(self, uow: IUnitOfWork, print_order_repository: PrintOrderRepository):
        self.print_order_repository = print_order_repository
        self.uow: IUnitOfWork = uow

    def place_new_order(self, data: PrintOrderDTO) -> PrintOrder:
        return print_order
