#!/usr/bin/python3
"""sends a request and displays value X-Request-Id in header response.
   response.info() show all information and with an if find X-request or
   print(response.getheader("X-Request-Id"))
"""

from urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    header = response.info()
if "X-Request-Id" in header:
    print(header['X-Request-Id'])
