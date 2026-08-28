import jwt
from uuid import uuid4
from src.core.config import settings
from src.features.identity.application.ports.token_service import TokenService
from src.core.shared.enums.token_type import Token


class JwtTokenService(TokenService):
    def __init__(self):
        self.JWT_SECRET_KEY: str = settings.JWT_SECRET_KEY
        self.JWT_ALGO: str = settings.JWT_ALGO
        self.ACCESS_TOKEN_DURATION: int = settings.ACCESS_TOKEN_DURATION
        self.REFRESH_TOKEN_DURATION: int = settings.REFRESH_TOKEN_DURATION

    def generate_token(self, payload, token_type: Token) -> str:
        match token_type:
            case Token.ACCESS:
                return self._generate_access_token(payload)
            case Token.REFRESH:
                return self._generate_refresh_token(payload)
            case _:
                raise ValueError("Invalid Token Type")

    def _generate_access_token(self, payload) -> str:

        payload["jti"] = uuid4()

        token: str = jwt.encode(
            payload,
            key=self.JWT_SECRET_KEY,
            algorithm=self.JWT_ALGO,
        )

        return token

    def _generate_refresh_token(self, payload) -> str:
        return ""
