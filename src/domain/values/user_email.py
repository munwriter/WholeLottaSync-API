from dataclasses import dataclass

from email_validator import EmailNotValidError, validate_email

from domain.common.base_value_obj import BaseValueObject
from domain.exceptions.user_credentials import InvalidEmailException


@dataclass(frozen=True)
class UserEmail(BaseValueObject[str]):
    value: str

    def _validate(self) -> None:
        try:
            validate_email(self.value, check_deliverability=False)
        except EmailNotValidError as e:
            raise InvalidEmailException from e

    def as_generic_type(self) -> str:
        return self.value
