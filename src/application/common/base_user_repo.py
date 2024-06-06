from abc import ABC, abstractmethod

from application.common.dtos import CreateUserOutputDTO
from domain.entities.user import User


class BaseUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> CreateUserOutputDTO:
        pass

    @abstractmethod
    async def is_username_exist(self, username: str) -> bool:
        pass

    @abstractmethod
    async def is_email_exist(self, username: str) -> bool:
        pass
