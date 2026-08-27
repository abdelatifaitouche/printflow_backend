from dataclasses import dataclass


@dataclass(frozen=True)
class CreateUser:
    email: str
    password: str
