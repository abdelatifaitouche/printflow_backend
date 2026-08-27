from uuid import UUID, uuid4
from src.features.identity.domain.value_objects.email import Email
from src.features.identity.domain.enums import UserState

from typing import Self


class User:
    def __init__(
        self,
        id: UUID,
        email: Email,
        password_hash: str,
        status: UserState,
        first_login: bool,
    ):
        self.id: UUID = id
        self.email: Email = email
        self.password_hash: str = password_hash
        self.status: UserState = status
        self.first_login: bool = first_login

    @classmethod
    def create(
        cls,
        email: Email,
        password_hash: str,
    ) -> Self:
        user = cls(
            id=uuid4(),
            email=email,
            password_hash=password_hash,
            status=UserState.PENDING,
            first_login=False,
        )

        return user

    def suspend_user(self):
        return

    def activate_user(self):
        return

    def block_user(self):
        return

    def change_email(self):
        return

    def change_password(self):
        return
