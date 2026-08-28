from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from src.features.identity.application.ports.user_repository import UserRepository
from src.features.identity.domain.user import User as UserEntity
from src.features.identity.infra.models.user import User as UserDB


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    def _to_orm(self, user: UserEntity) -> UserDB:
        return UserDB(
            id=user.id,
            email=user.email.value,
            password_hash=user.password_hash,
            status=user.status,
            first_login=user.first_login,
        )

    async def save(self, user_entity: UserEntity):
        user_db: UserDB = self._to_orm(user_entity)
        self.db.add(user_db)
        await self.db.flush()

    async def get_by_id(self, user_id: UUID):
        return

    async def get_by_email(self, email: str):
        return
