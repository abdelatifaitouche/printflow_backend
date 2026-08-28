from src.infra.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Enum
from src.features.identity.domain.enums import UserState


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    status: Mapped[UserState] = mapped_column(
        Enum(UserState),
        nullable=False,
        default=UserState.PENDING,
    )
    first_login: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
