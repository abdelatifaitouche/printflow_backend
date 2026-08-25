from enum import StrEnum


class ProductState(StrEnum):
    AVAILABLE = "AVAILABLE"
    OUT_OF_STOCK = "OUT_OF_STOCK"
    NON_AVAILABLE = "NON_AVAILABLE"
