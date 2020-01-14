#!/usr/bin/python3
"""
 Github credentials
"""
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    p = sys.argv[2]
    url = "https://api.github.com/users/{}".format(user)
    r = requests.get(url, auth=(user, p))
    try:
        print(r.json().get("id"))
    except ValueError:
        print("Not a valid JSON")
