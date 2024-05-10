from __future__ import annotations

from dataclasses import dataclass, field

from domain.common.base_entity import BaseEntity
from domain.common.base_pwd_hasher import IPasswordHasher
from domain.values.user_email import UserEmail
from domain.values.user_name import Username


@dataclass(frozen=True, eq=False)
class User(BaseEntity):
    username: Username
    hashed_password: str
    email: UserEmail
    # friends: set[User] = field(default_factory=set)

    @classmethod
    def create_from_raw_password(
        cls,
        username: Username,
        email: UserEmail,
        raw_password: str,
        password_hasher: IPasswordHasher,
    ) -> User:
        hashed_password = password_hasher.hash_pwd(raw_password)
        return cls(username, hashed_password, email)
