from src.infra.db.engine import engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


async def get_db():
    async with SessionLocal() as session:
        yield session
