#!/usr/bin/env python3
"""
Filtered Logger module
"""
import logging
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ That returns the log message obfuscated. """
    for field in fields:
        message = re.sub(fr'{field}=([^=]*){separator}',
                         fr'{field}={redaction}{separator}', message)
    return message
