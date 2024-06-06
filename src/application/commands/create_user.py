from dataclasses import dataclass

from application.common.base_command_handler import CommandHandler
from application.common.base_pwd_hasher import BasePasswordHasher
from application.common.base_user_repo import BaseUserRepository
from application.common.dtos import CreateUserInputDTO, CreateUserOutputDTO
from domain.entities.user import User
from domain.values.user.user_email import UserEmail
from domain.values.user.user_hashed_pwd import UserHashedPassword
from domain.values.user.user_name import Username


@dataclass(frozen=True, repr=False, eq=False)
class CreateUser(CommandHandler[CreateUserInputDTO, CreateUserOutputDTO]):
    user_repo: BaseUserRepository
    pwd_hasher: BasePasswordHasher

    async def handle(self, command: CreateUserInputDTO) -> CreateUserOutputDTO:
        if self.user_repo.is_username_exist(command.username):
            raise  # TODO Exception
        if self.user_repo.is_email_exist(command.email):
            raise  # TODO Exception

        username = Username(command.username)
        email = UserEmail(command.email)
        hashed_password = UserHashedPassword(self.pwd_hasher.hash_pwd(command.password))
        user = User(username, hashed_password, email)
        user_dto = await self.user_repo.create_user(user)
        # TODO commit changes
        return user_dto
