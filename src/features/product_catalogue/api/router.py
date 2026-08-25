from fastapi import APIRouter, Depends, status
from src.features.product_catalogue.api.commands.write_commands import (
    CreateProductCommand,
    UpdateProductCommand,
    UpdateProductStateCommand,
)
from src.features.product_catalogue.api.dependencies import get_uc, get_query_service
from src.features.product_catalogue.application.product_uc import ProductUC
from src.features.product_catalogue.application.dtos.product import (
    CreateProduct,
    UpdateProduct,
)
from src.features.product_catalogue.services.product_query_service import (
    ProductQueryService,
)
from src.features.product_catalogue.api.filters.product_filters import ProductFilters
from src.api.utils.pagination import Pagination
from uuid import UUID

router = APIRouter(prefix="/product")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: CreateProductCommand, uc: ProductUC = Depends(get_uc)
):
    return await uc.create_product(
        CreateProduct(
            product_name=product_data.product_name,
            unit_price=product_data.unit_price,
            stock_init=product_data.stock_init,
        ),
    )


@router.get("/{product_id}")
async def get_product(
    product_id: UUID,
    queries: ProductQueryService = Depends(get_query_service),
):
    return await queries.get_product_details(product_id)


@router.get("", status_code=status.HTTP_200_OK)
async def list_products(
    pagination: Pagination = Depends(),
    filters: ProductFilters = Depends(),
    queries: ProductQueryService = Depends(get_query_service),
):
    return await queries.list(
        pagination=pagination,
        filters=filters,
    )


@router.patch("/{product_id}/", status_code=status.HTTP_200_OK)
async def update_product(
    product_id: UUID,
    data: UpdateProductCommand,
    uc: ProductUC = Depends(get_uc),
):
    return await uc.update_product(
        product_id=product_id,
        data=UpdateProduct(
            product_name=data.product_name,
            unit_price=data.unit_price,
        ),
    )


@router.patch("/{product_id}/status/")
async def update_product_state(
    product_id: UUID,
    data: UpdateProductStateCommand,
    uc: ProductUC = Depends(get_uc),
):
    return await uc.update_product_state(
        product_id,
        product_state=data.status,
    )
