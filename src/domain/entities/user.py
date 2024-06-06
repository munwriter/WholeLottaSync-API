from __future__ import annotations

from dataclasses import dataclass, field

from domain.common.base_entity import BaseEntity
from domain.values.user.user_email import UserEmail
from domain.values.user.user_hashed_pwd import UserHashedPassword
from domain.values.user.user_name import Username


@dataclass(frozen=True, eq=False)
class User(BaseEntity):
    username: Username
    hashed_password: UserHashedPassword
    email: UserEmail
    friends: set[User] = field(default_factory=set, kw_only=True)
