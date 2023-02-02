#!/usr/bin/env python3
"""
Filtered Logger module
"""
import logging
import re
import os
import mysql.connector
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Formats string. """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ Returns logging.Logger Object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(ch)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns MYSQLConnection object. """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME") or "root"
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD") or ""
    host = os.getenv("PERSONAL_DATA_DB_HOST") or "localhost"
    dbname = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=dbname)
