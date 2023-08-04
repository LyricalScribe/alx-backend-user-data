#!/usr/bin/env python3
"""Process of Regex-ing"""
import re
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
