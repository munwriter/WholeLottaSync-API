from dataclasses import dataclass

from domain.common.base_value_obj import BaseValueObject
from domain.exceptions.user_exceptions import UsernameLengthException


@dataclass(frozen=True)
class Username(BaseValueObject[str]):
    MIN_LENGTH = 3
    MAX_LENGTH = 40

    def _validate(self) -> None:
        if not self.MIN_LENGTH <= len(self.value) <= self.MAX_LENGTH:
            raise UsernameLengthException(self.value)

    def as_generic_type(self) -> str:
        return self.value
