from __future__ import annotations

from dataclasses import dataclass, field

from domain.common.base_entity import BaseEntity
from domain.entities.user import User
from domain.values.room.room_accessibility import RoomAccessibility
from domain.values.room.room_max_participants import RoomMaxParticipants
from domain.values.room.room_name import RoomName


@dataclass(frozen=True, eq=False)
class Room(BaseEntity):
    name: RoomName
    max_participants_quantity: RoomMaxParticipants
    private: RoomAccessibility = field(default=RoomAccessibility(False), kw_only=True)
    users: set[User] = field(default_factory=set, kw_only=True)
