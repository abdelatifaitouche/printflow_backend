from src.features.identity.application.ports.user_repository import UserRepository
from src.features.identity.domain.user import User
from src.features.identity.domain.value_objects.email import Email
from src.features.identity.application.dtos.user_dto import CreateUser


class UserUC:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def register_user(self, data: CreateUser):
        pass

    async def login(self):
        pass
