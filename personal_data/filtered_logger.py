#!/usr/bin/env python3
"""Regex-ing module to obfuscate log messages"""

import re


def filter_datum(fields: list[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """A function used to obfuscate the log message"""
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message
