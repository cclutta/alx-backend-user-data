#!/usr/bin/env python3
"""
Filtered Logger module
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ That returns the log message obfuscated. """
    for field in fields:
        message = re.sub(fr'{field}=([^=]*){separator}',
                         fr'{field}={redaction}{separator}', message)
    return message
