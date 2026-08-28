from abc import ABC, abstractmethod
from typing import Any

from src.core.shared.enums.token_type import Token


class TokenService(ABC):
    @abstractmethod
    def generate_token(self, payload: dict[str, Any], token_type: Token) -> str:
        raise NotImplementedError()
