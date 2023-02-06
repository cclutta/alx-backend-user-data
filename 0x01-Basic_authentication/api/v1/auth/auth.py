#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ The class auth. """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require auth method. """
        require = False
        if path is None:
            require = True
        if len(excluded_paths) == 0 or excluded_paths is None:
            require = True
        return require

    def authorization_header(self, request=None) -> str:
        """ Authorization method. """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method. """
        return None
