from dataclasses import dataclass

from domain.common.base_exception import AppException


@dataclass(eq=False, frozen=True)
class EmailAlreadyExistException(AppException):
    @property
    def message(self):
        return "This email already taken"
