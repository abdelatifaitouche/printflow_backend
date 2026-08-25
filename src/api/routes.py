from fastapi import APIRouter
from src.features.product_catalogue.api.router import router as product_catalgoue_router
from src.features.orders.api.router import router as order_router

router = APIRouter(prefix="/api/v1")

router.include_router(order_router)
router.include_router(product_catalgoue_router)
