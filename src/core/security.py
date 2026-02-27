from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerifyMismatchError
from werkzeug.security import check_password_hash

_password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    return _password_hasher.hash(password)


def verify_password(password_hash: str, password: str) -> bool:
    if password_hash.startswith("scrypt:"):
        return check_password_hash(password_hash, password)
    try:
        return _password_hasher.verify(password_hash, password)
    except (InvalidHashError, VerifyMismatchError):
        return False
