#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {'q': q}
    r = requests.post(url, data)

    try:
        d = r.json()
        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id"), d.get("name")))
    except ValueError:
        print("Not a valid JSON")
