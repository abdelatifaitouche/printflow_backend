from abc import ABC, abstractmethod


class IProductRepository(ABC):
    async def save(self, *args, **kwargs):
        raise NotImplementedError()

    async def get(self, *args, **kwargs):
        raise NotImplementedError()
