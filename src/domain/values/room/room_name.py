from dataclasses import dataclass

from domain.common.base_value_obj import BaseValueObject
from domain.exceptions.room_exceptions import (
    EmptyRoomNameException,
    RoomNameLengthException,
)


@dataclass(frozen=True)
class RoomName(BaseValueObject[str]):
    MAX_LENGTH = 70

    def _validate(self) -> None:
        if not self.value:
            raise EmptyRoomNameException()

        if len(self.value) > 70:
            raise RoomNameLengthException(self.value)

    def as_generic_type(self) -> str:
        return self.value
