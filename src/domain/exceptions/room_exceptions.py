from dataclasses import dataclass

from domain.common.base_exception import AppException


@dataclass(eq=False, frozen=True)
class EmptyRoomNameException(AppException):
    @property
    def message(self):
        return "Room name must be not empty"


@dataclass(eq=False, frozen=True)
class RoomNameLengthException(AppException):
    error_info: str

    @property
    def message(self):
        return f"Max length of room name has been reached. Current length {len(self.error_info)}"


@dataclass(eq=False, frozen=True)
class RoomParticipantsQuantityException(AppException):
    error_info: int

    @property
    def message(self):
        return f"Participants quantity should be greater equal 2 and less equal 10. Current quantity {self.error_info}"
