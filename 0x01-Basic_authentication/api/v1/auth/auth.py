#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ The class auth. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth method. """

        if path and not path.endswith("/"):
            path += "/"
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path is None:
            return True
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization method. """
        if request is None:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method. """
        return None
