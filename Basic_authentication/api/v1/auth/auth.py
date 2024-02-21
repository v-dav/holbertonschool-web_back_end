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
        """A public method that checks if path requieres authorization"""
        if (path is None or
                excluded_paths is None or
                excluded_paths == []):
            return True

        if not path.endswith('/'):
            path = path + '/'

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """A public method fo authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method current_user"""
        return None
