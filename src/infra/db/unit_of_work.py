from sqlalchemy.ext.asyncio import AsyncSession
from src.core.shared.interfaces.unit_of_work import IUnitOfWork


class UnitOfWork(IUnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        try:
            if exc_type is not None:
                await self.rollback()
            else:
                await self.commit()
        except Exception:
            await self.rollback()
            raise
        finally:
            await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
