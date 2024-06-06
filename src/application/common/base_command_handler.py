from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from .base_command import BaseCommand

InputDTO = TypeVar("InputDTO", bound=BaseCommand)
OutputDTO = TypeVar("OutputDTO", bound=Any)


@dataclass(frozen=True)
class CommandHandler(ABC, Generic[InputDTO, OutputDTO]):

    @abstractmethod
    async def handle(self, command: InputDTO) -> OutputDTO:
        pass
