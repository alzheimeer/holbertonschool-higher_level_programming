#!/usr/bin/python3
"""
search request to the Star Wars API
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    params = (('search', sys.argv[1]),)
    r = requests.get(url, params=params)
    d = r.json()
    print("Number of results: {}".format(d['count']))
    c = d['results']
    for x in c:
        print(x['name'])
