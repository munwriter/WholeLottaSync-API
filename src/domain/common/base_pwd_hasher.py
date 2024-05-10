from abc import ABC, abstractmethod


class IPasswordHasher(ABC):
    @staticmethod
    @abstractmethod
    def hash_pwd(raw_pwd: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def verify_pwd(raw_pwd: str, hashed_pwd: str) -> bool:
        pass
