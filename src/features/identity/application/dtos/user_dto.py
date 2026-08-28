from dataclasses import dataclass


@dataclass(frozen=True)
class LoginUser:
    email: str
    password: str


@dataclass(frozen=True)
class CreateUser:
    email: str
    password: str
