from dataclasses import dataclass

from domain.common.base_value_obj import BaseValueObject
from domain.exceptions.room_exceptions import RoomParticipantsQuantityException


@dataclass(frozen=True)
class RoomMaxParticipants(BaseValueObject[int]):
    MIN_PARTICIPANTS = 2
    MAX_PARTICIPANTS = 10

    def _validate(self) -> None:
        if not self.MAX_PARTICIPANTS <= self.value <= self.MAX_PARTICIPANTS:
            raise RoomParticipantsQuantityException(self.value)

    def as_generic_type(self) -> int:
        return self.value
