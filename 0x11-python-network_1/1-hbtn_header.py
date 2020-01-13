#!/usr/bin/python3
"""
sends a request and displays value X-Request-Id in header response.
response.info() show all information and with an if find X-request or
print(response.getheader("X-Request-Id"))
"""

from urllib import request
import sys

url=sys.argv[1]
if __name__ == "__main__":
    with request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
