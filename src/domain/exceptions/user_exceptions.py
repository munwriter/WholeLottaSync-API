from dataclasses import dataclass

from domain.common.base_exception import AppException


@dataclass(eq=False, frozen=True)
class InvalidEmailException(AppException):
    @property
    def message(self):
        return "Invalid email"


@dataclass(eq=False, frozen=True)
class UsernameLengthException(AppException):
    error_info: str

    @property
    def message(self):
        return f"Max/min length of username has been reached/not reached. Current length {len(self.error_info)}"
