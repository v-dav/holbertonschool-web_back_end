#!/usr/bin/env python3
""" A module with Session Class authentication"""

from api.v1.auth.basic_auth import BasicAuth
import uuid


class SessionAuth(BasicAuth):
    """A Session Class class for authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """An instance method for creating sessionID"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns user_id based on session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)
