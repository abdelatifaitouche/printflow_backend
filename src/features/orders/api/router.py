from fastapi import APIRouter, Depends
from uuid import UUID
from src.features.orders.api.dependencies.dependencies import get_uc
from src.features.orders.application.print_order_uc import PrintOrderUC
from src.features.orders.api.commands.write_commands import CreateOrderCommand
from src.features.orders.application.dtos.print_order import PrintOrderDTO, PrintJobDTO

router = APIRouter(prefix="/order")


@router.post("")
async def place_new_order(data: CreateOrderCommand, uc: PrintOrderUC = Depends(get_uc)):
    return await uc.place_new_order(
        data=PrintOrderDTO(
            jobs=[
                PrintJobDTO(quantity=job.quantity, product_id=job.product_id)
                for job in data.jobs
            ],
        )
    )


@router.get("/{order_id}")
async def get_order_details():
    return


@router.get("")
async def list_orders():
    return


@router.patch("/{order_id}/confirm")
async def confirm_order(
    order_id: UUID,
    uc: PrintOrderUC = Depends(get_uc),
):
    return await uc.confirm_order(order_id)
