#!/usr/bin/env python3
"""The Authentication Module"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """A function that hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a unique UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ The constructor method for the class"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ User registration method"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(user.email))
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """ Credentials validation method"""
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Method to create the session ID"""
        try:
            user = self._db.find_user_by(email=email)
            user_uuid = _generate_uuid()
            self._db.update_user(user.id, session_id=user_uuid)
            return user_uuid
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Find user by session ID"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
