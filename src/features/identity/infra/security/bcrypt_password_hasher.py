import bcrypt
from src.features.identity.application.ports.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(
            password.encode("utf-8"),
            salt=bcrypt.gensalt(12),
        ).decode("utf-8")

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
