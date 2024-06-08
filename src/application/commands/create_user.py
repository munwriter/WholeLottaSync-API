from dataclasses import dataclass
from typing import Type

from application.common.base_command_handler import CommandHandler
from application.common.base_pwd_hasher import BasePasswordHasher
from application.common.base_uow import BaseUOW
from application.common.base_user_repo import BaseUserRepository
from application.common.dtos import CreateUserInputDTO, CreateUserOutputDTO
from application.exceptions.email_already_exist_exception import (
    EmailAlreadyExistException,
)
from application.exceptions.username_already_exist_exception import (
    UsernameAlreadyExistException,
)
from domain.entities.user import User
from domain.values.user.user_email import UserEmail
from domain.values.user.user_hashed_pwd import UserHashedPassword
from domain.values.user.user_name import Username


@dataclass(frozen=True, repr=False, eq=False)
class CreateUser(CommandHandler[CreateUserInputDTO, CreateUserOutputDTO]):
    uow: BaseUOW
    user_repo: Type[BaseUserRepository]
    pwd_hasher: BasePasswordHasher

    async def handle(self, command: CreateUserInputDTO) -> CreateUserOutputDTO:
        async with self.uow:
            user_repo = self.user_repo(self.uow.session)
            if await user_repo.is_username_exist(command.username):
                raise UsernameAlreadyExistException()
            if await user_repo.is_email_exist(command.email):
                raise EmailAlreadyExistException()

            username = Username(command.username)
            email = UserEmail(command.email)
            hashed_password = UserHashedPassword(self.pwd_hasher.hash_pwd(command.password))
            user = User(username, hashed_password, email)
            user_dto = await user_repo.create_user(user)
            await self.uow.commit()

        return user_dto
