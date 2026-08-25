from abc import ABC, abstractmethod


class IPrintOrderRepository(ABC):
    @abstractmethod
    async def save(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError()
