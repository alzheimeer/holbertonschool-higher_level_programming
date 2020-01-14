#!/usr/bin/python3
"""
 Github adv
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = (requests.get(url).json())[:10]
    for u in r:
        print("{}: {}".format(u['sha'], u['commit']['author']['name']))
