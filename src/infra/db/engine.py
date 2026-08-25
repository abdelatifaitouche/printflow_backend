from sqlalchemy.ext.asyncio import create_async_engine
from src.core.config import settings

print(repr(settings.DATABASE_URL))


engine = create_async_engine(url=settings.DATABASE_URL, echo=True)
