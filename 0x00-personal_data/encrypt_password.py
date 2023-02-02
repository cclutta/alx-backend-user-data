#!/usr/bin/env python3
""" Encrypt password module """

import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes password
    """
    return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Checks if password is valid. """
    return bcrypt.checkpw(str.encode(password), hashed_password)

