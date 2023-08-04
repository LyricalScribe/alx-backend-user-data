#!/usr/bin/env python3
"""Process of Regex-ing"""
import re
import logging
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """Returns the log message obfuscated"""
    return re.sub(
        r'{}(?={})'.format('|'.join(fields), re.escape(separator)),
        redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, field: tuple):
        """init methode"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Format method to filter values in incoming log records
        """
        record.msg = filter_datum(
            self.fields,
            self.REDACTION,
            record.msg,
            self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
