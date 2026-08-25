from abc import ABC, abstractmethod


class IUnitOfWork(ABC):
    """Unit of work interface."""

    async def __aenter__(self) -> "IUnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def rollback(self) -> None:
        raise NotImplementedError
