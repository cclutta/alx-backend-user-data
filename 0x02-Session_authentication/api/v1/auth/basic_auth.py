#!/usr/bin/env python3
""" Module of Basic Auth
"""
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from models.user import User
from base64 import b64decode


class BasicAuth(Auth):
    """ Basic auth class defn. """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ returns the Base64 part of the Auth header. """
        if authorization_header and type(authorization_header) is str:
            if authorization_header.startswith("Basic "):
                return authorization_header[6:]
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ that retursn the user email and password. """
        if decoded_base64_authorization_header:
            if type(decoded_base64_authorization_header) is str:
                if ":" in decoded_base64_authorization_header:
                    user = decoded_base64_authorization_header.split(":", 1)
                    return (user[0], user[1])
        return (None, None)

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ Decodes base 64. """
        if base64_authorization_header \
                and type(base64_authorization_header) is str:
            try:
                return b64decode(base64_authorization_header).decode('utf-8')
            except Exception:
                return None
        return None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ that returns the User instance based on his email and password. """
        if user_email and type(user_email) is str:
            if user_pwd and type(user_pwd) is str:
                try:
                    usr = User.search({"email": user_email})
                    if len(usr):
                        usr = usr[0]
                        if usr.is_valid_password(user_pwd):
                            return usr
                        else:
                            return None
                except Exception:
                    return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieves the User instance for a request. """
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        dcdheader = self.decode_base64_authorization_header(b64header)
        credentials = self.extract_user_credentials(dcdheader)
        return self.user_object_from_credentials(*credentials)
