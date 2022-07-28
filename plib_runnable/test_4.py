"""
    Gopad OpenAPI

    API definition for Gopad  # noqa: E501

    The version of the OpenAPI document: 1.0.0-alpha1
    Generated by: https://openapi-generator.tech
"""


import io
import json
import logging
import re
import ssl
from urllib.parse import urlencode
from urllib.parse import urlparse
from urllib.request import proxy_bypass_environment
import urllib3
import ipaddress

# end of class RESTClientObject
def is_ipv4(target):
    """ Test if IPv4 address or not
    """
    try:
       chk = ipaddress.IPv4Address(target)
       return True
    except ipaddress.AddressValueError:
       return False



def test_is_ipv4():
    """Check the correctness of is_ipv4
    """
    assert is_ipv4('127.0.0.1') == True
    assert is_ipv4('127.0.0.256') == False
    assert is_ipv4('fe80:0000:0001:0000:0440:44ff:1233:5678') == False
    assert is_ipv4('12.134.25.123') == True
    assert is_ipv4(' ') == False
    assert is_ipv4('ipv4') == False