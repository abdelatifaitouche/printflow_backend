from fastapi import APIRouter
from src.features.product_catalogue.api.router import router as product_catalgoue_router

router = APIRouter(prefix="/api/v1")

router.include_router(product_catalgoue_router)
