from dataclasses import dataclass
from uuid import UUID

from .base_command import BaseCommand


@dataclass(frozen=True)
class BaseOutputDTO:
    id: UUID


@dataclass(frozen=True)
class CreateUserInputDTO(BaseCommand):
    username: str
    password: str
    email: str


@dataclass(frozen=True)
class CreateUserOutputDTO(BaseOutputDTO):
    username: str
    email: str
