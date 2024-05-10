import bcrypt

from domain.common.base_pwd_hasher import IPasswordHasher


class BcryptPasswordHasher(IPasswordHasher):
    @staticmethod
    def hash_pwd(raw_pwd: str) -> str:
        salt = bcrypt.gensalt()
        hashed_pwd = bcrypt.hashpw(raw_pwd.encode(), salt)
        return hashed_pwd.hex()

    @staticmethod
    def verify_pwd(raw_pwd: str, hashed_pwd: str) -> bool:
        hashed_pwd_in_bytes = bytes.fromhex(hashed_pwd)
        raw_pwd_in_bytes = raw_pwd.encode()
        return bcrypt.checkpw(raw_pwd_in_bytes, hashed_pwd_in_bytes)
