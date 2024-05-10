from __future__ import annotations

from abc import ABC
from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4


@dataclass(frozen=True)
class BaseEntity(ABC):
    id: UUID = field(default=uuid4(), kw_only=True)
    created_at: datetime = field(default=datetime.now(UTC), kw_only=True)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseEntity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
