from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import UUID, DateTime, func
from datetime import datetime
import uuid


class Base(DeclarativeBase):
    """
    Base Model Class for the app's db models

    Shared:
        id : UUID primary key
        created_at & updated_at: Datetime for auditing
    """

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
