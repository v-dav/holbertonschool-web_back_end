#!/usr/bin/env python3
"""
A module with a class to manage API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    A class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A documentation string for the public method"""
        return False

    def authorization_header(self, request=None) -> str:
        """A public method fo authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method current_user"""
        return None
