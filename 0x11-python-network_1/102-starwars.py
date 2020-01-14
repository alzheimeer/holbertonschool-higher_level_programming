#!/usr/bin/python3
"""
search request to the Star Wars API
"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://swapi.co/api/people'
    params = {'search': sys.argv[1]}
    r = requests.get(url, params=params)
    d = r.json()
    print("Number of results: {}".format(d['count']))
    c = d['results']
    for x in c:
        print(x['name'])
        for film in x['films']:
            print("\t{}".format(requests.get(film).json()['title']))
    # Loop for reading next pages
    while d['next'] is not None:
        d = requests.get(d['next']).json()
        h = d['results']
        for c in h:
            print(c['name'])

            for film in x['films']:
                print("\t{}".format(requests.get(film).json()['title']))
