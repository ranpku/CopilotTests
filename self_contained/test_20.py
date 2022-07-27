import datetime
import logging
from pathlib import Path
import re
import tarfile
from typing import Any, Dict, Iterator, List, Optional
from urllib.parse import unquote, urljoin
from bs4 import BeautifulSoup
import requests
def size_to_bytes(size: str) -> int:
    """Convert human readable file size to bytes.

    Resulting value is an approximation as input value is in most case rounded.

    Args:
        size: A string representing a human readable file size (eg: '500K')

    Returns:
        A decimal representation of file size

        Examples::

            >>> size_to_bytes("500")
            500
            >>> size_to_bytes("1K")
            1000
    """
    units = {
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
        "P": 1000**5,
        "E": 1000**6,
        "Z": 1000**7,
        "Y": 1000**8,
    }
    if size.endswith(tuple(units)):
        v, u = (size[:-1], size[-1])
        return int(v) * units[u]
    else:
        return int(size)


def test_size_to_bytes():
    """
    Check the corretness of size_to_bytes
    """
    assert  size_to_bytes("500") == 500
    assert size_to_bytes("1K") == 1000
    assert size_to_bytes("1M") == 1000**2