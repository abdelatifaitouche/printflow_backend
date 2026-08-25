from abc import ABC, abstractmethod


class PrintOrderRepository(ABC):
    @abstractmethod
    def save(self, *args, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get(self, *args, **kwargs):
        raise NotImplementedError()
