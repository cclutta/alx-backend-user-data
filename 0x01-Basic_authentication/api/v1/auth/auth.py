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
        for item in excluded_paths:
            if '*' in item:
                item = item.replace('*', '.*')
                item = item.replace('/', r'\/')
                if re.compile(item).match(path) is not None:
                    return False
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization method. """
        if request and "Authorization" in request.headers:
            return request.headers.get("Authorization", default=None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user method. """
        return None
