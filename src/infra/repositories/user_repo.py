from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.base_user_repo import BaseUserRepository
from application.common.dtos import CreateUserOutputDTO
from domain.entities.user import User
from infra.persistence.models.user import DBUser
from infra.repositories.mappers.user_mapper import user_entity_to_db_user


@dataclass(frozen=True, repr=False, eq=False)
class SAUserRepository(BaseUserRepository):
    session: AsyncSession

    async def create_user(self, user: User) -> CreateUserOutputDTO:
        db_user = user_entity_to_db_user(user)
        await self.session.add(db_user)
        # TODO to separated mapper
        return CreateUserOutputDTO(
            user.id,
            user.username.as_generic_type(),
            user.email.as_generic_type(),
        )

    async def is_username_exist(self, username: str) -> bool:
        query = select(DBUser).where(DBUser.username == username)
        res = await self.session.execute(query)
        return bool(res)

    async def is_email_exist(self, email: str) -> bool:
        query = select(DBUser).where(DBUser.email == email)
        res = await self.session.execute(query)
        return bool(res)
