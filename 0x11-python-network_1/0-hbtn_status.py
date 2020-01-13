#!/usr/bin/python3
""" https://intranet.hbtn.io/status """

from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as response:
    r = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode("utf-8")))
