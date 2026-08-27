from src.core.shared.interfaces.unit_of_work import IUnitOfWork

from src.features.identity.application.ports.user_repository import UserRepository
from src.features.identity.application.ports.password_hasher import PasswordHasher

from src.features.identity.domain.user import User
from src.features.identity.domain.value_objects.email import Email
from src.features.identity.application.dtos.user_dto import CreateUser


class UserUC:
    def __init__(
        self,
        uow: IUnitOfWork,
        user_repo: UserRepository,
        password_hashed: PasswordHasher,
    ):
        self.uow = uow
        self.user_repo = user_repo
        self.password_hashed = password_hashed

    async def register_user(self, data: CreateUser):
        async with self.uow:
            user: User | None = await self.user_repo.get_by_email(data.email)

            if user:
                raise Exception("Invalid Credentials")

            hashed_password: str = self.password_hashed.hash_password(data.password)

            user = User.create(
                Email(data.email),
                password_hash=hashed_password,
            )

            user = await self.user_repo.save(user)

        return user

    async def login(self):
        pass
