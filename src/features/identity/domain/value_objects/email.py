from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError


@dataclass
class Email:
    value: str

    def __post_init__(self) -> None:
        try:
            result = validate_email(
                self.value,
                check_deliverability=False,
            )
        except EmailNotValidError as exc:
            raise ValueError(str(exc)) from exc

        object.__setattr__(self, "value", result.normalized)
