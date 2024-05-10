from dataclasses import dataclass


@dataclass(eq=False, frozen=True)
class AppException(Exception):
    @property
    def message(self):
        return "An error occurred during execution"
