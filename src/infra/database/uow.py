from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from application.common.base_uow import BaseUOW
from infra.database.config import BaseDBSettings


@dataclass(repr=False, eq=False, frozen=True)
class SqlAlchemyUOW(BaseUOW):
    __db_config: BaseDBSettings

    def __post_init__(self) -> None:
        engine = create_async_engine(url=self.__db_config.DB_DSN)
        self._session_factory = async_sessionmaker(
            engine,
            expire_on_commit=False,
            class_=AsyncSession,
        )
        self.session = None

    async def __aenter__(self) -> None:
        self.session = self._session_factory()

    async def __aexit__(self, *args) -> None:
        await self.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
