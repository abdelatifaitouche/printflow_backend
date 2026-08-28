from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.infra.db.session import get_db
from src.infra.db.unit_of_work import UnitOfWork
from src.features.identity.application.user_usecases import UserUC
from src.features.identity.infra.repositories.user_repository import (
    SqlAlchemyUserRepository,
)
from src.features.identity.infra.security.bcrypt_password_hasher import (
    BcryptPasswordHasher,
)


def get_uc(db: AsyncSession = Depends(get_db)):
    uow: UnitOfWork = UnitOfWork(db)
    repo = SqlAlchemyUserRepository(db)
    hasher = BcryptPasswordHasher()
    return UserUC(
        uow,
        repo,
        hasher,
    )
