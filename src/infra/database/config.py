from abc import ABC, abstractmethod

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BaseDBSettings(ABC):
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_NAME: str

    @property
    @abstractmethod
    def DB_DSN(self) -> str:
        pass


class PostgresDBSettings(BaseDBSettings, BaseSettings):
    DB_USERNAME: str
    DB_PASSWORD: SecretStr
    DB_HOST: str
    DB_NAME: str

    @property
    def DB_DSN(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}/{self.DB_NAME}"
