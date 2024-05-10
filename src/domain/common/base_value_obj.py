from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self._validate()

    @abstractmethod
    def _validate(self):
        pass

    @abstractmethod
    def as_generic_type(self):
        pass
