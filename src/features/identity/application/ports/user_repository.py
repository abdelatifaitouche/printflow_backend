from abc import ABC, abstractmethod
from src.features.identity.domain.user import User
from uuid import UUID


class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, user_entity: User):
        raise NotImplementedError()
