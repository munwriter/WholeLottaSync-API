from __future__ import annotations

import datetime

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

friendship_table = Table(
    "friendship",
    Base.metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("friend_id", ForeignKey("user.id"), primary_key=True),
)


class DBUser(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    email: Mapped[str] = mapped_column(default=None)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.UTC)
    )
    friends: Mapped[set[DBUser]] = relationship(
        "DBUser",
        secondary=friendship_table,
        primaryjoin=id == friendship_table.c.user_id,
        secondaryjoin=id == friendship_table.c.friend_id,
        backref="friend_of",
    )
