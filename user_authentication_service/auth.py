#!/usr/bin/env python3
"""The Authentication Module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """A function that hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
