#!/usr/bin/python3
"""
sends a request and displays value X-Request-Id in header response.
response.info() show all information and with an if find X-request or
print(response.getheader("X-Request-Id"))
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader("X-Request-Id"))
