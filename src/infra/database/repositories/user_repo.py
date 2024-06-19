from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.common.base_user_repo import BaseUserRepository
from application.common.dtos import CreateUserOutputDTO
from domain.entities.user import User
from infra.database.persistence.models.user import DBUser
from infra.database.repositories.mappers.user_mapper import user_entity_to_db_user


@dataclass(frozen=True, repr=False, eq=False)
class SAUserRepository(BaseUserRepository):
    __session: AsyncSession

    async def create_user(self, user: User) -> CreateUserOutputDTO:
        db_user = user_entity_to_db_user(user)
        async with self.__session.begin():
            await self.__session.add(db_user) # type: ignore
        # TODO to separated mapper
        return CreateUserOutputDTO(
            user.id,
            user.username.as_generic_type(),
            user.email.as_generic_type(),
        )

    async def is_username_exist(self, username: str) -> bool:
        query = select(DBUser).where(DBUser.username == username)
        res = await self.__session.execute(query)
        return bool(res.scalars().all())

    async def is_email_exist(self, email: str) -> bool:
        query = select(DBUser).where(DBUser.email == email)
        res = await self.__session.execute(query)
        return bool(res.scalars().all())
