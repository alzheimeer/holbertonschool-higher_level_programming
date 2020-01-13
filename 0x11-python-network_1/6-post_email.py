#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={'email': argv[2]})
    print(response.text)
