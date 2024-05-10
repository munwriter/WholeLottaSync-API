import datetime

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class DBUser(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    email: Mapped[str] = mapped_column(default=None)
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.UTC)
    )
