#!/usr/bin/env python3
"""Module for encrypting passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """A function that hashes the password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
