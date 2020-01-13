#!/usr/bin/python3
"""
Prints error code
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if response.status_code > 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
