#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

from urllib import request, parse
import sys

a = sys.argv[1]
b = parse.urlencode({"email": sys.argv[2]}).encode()
with request.urlopen(a, b) as response:
    print(response.read().decode('utf-8'))
