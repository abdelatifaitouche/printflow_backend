from fastapi import APIRouter
from src.features.product_catalogue.api.router import router as product_catalgoue_router
from src.features.orders.api.router import router as order_router
from src.features.storage.api.router import router as document_router
from src.features.crm.api.router import router as crm_router

router = APIRouter(prefix="/api/v1")

router.include_router(order_router)
router.include_router(document_router)
router.include_router(crm_router)
router.include_router(product_catalgoue_router)
