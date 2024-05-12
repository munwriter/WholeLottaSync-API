from dataclasses import dataclass

from domain.common.base_value_obj import BaseValueObject


@dataclass(frozen=True)
class UserHashedPassword(BaseValueObject[str]):
    def _validate(self) -> None:
        pass

    def as_generic_type(self) -> str:
        return self.value
