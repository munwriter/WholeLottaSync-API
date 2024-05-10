from dataclasses import dataclass

from domain.common.base_entity import BaseEntity
from domain.values.user_email import UserEmail
from domain.values.user_name import Username


@dataclass
class User(BaseEntity):
    username: Username
    hashed_password: str
    email: UserEmail
