#!/usr/bin/env python3
""" Module of Session Auth
"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """ Session Authentication class. """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for a user ID. """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns user ID based on a session ID. """
        if session_id is None or type(session_id) is not str:
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """ returns a User instance based on a cookie value. """
        u_id = self.user_id_for_session_id(self.session_cookie(request))
        if u_id:
            return User.get(u_id)

    def destroy_session(self, request=None):
        """ that deletes the user session. """
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if self.user_id_for_session_id(session_id):
                    del self.user_id_by_session_id[session_id]
                    return True
        return False
