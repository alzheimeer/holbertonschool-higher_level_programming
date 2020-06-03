#!/usr/bin/python3
import sys
"""prints logs"""


def imp(fs, e0, e1, e2, e3, e4, e5, e6, e7):
    """Method to print"""
    print("File size: {0}".format(fs))
    print("200: {0}".format(e0))
    print("301: {0}".format(e1))
    print("400: {0}".format(e2))
    print("401: {0}".format(e3))
    print("403: {0}".format(e4))
    print("404: {0}".format(e5))
    print("405: {0}".format(e6))
    print("500: {0}".format(e7))

if __name__ == "__main__":
    """MAIN"""
    c = 0
    e0 = 0
    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    fs = 0
    line = sys.stdin.readline()
    try:
        while line:
            if c == 10:
                imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
                c = 0

            s = line.split()
            n = s[7]
            if n == "200":
                e0 = e0 + 1
            elif n == "301":
                e1 = e1 + 1
            elif n == "400":
                e2 = e2 + 1
            elif n == "401":
                e3 = e3 + 1
            elif n == "403":
                e4 = e4 + 1
            elif n == "404":
                e5 = e5 + 1
            elif n == "405":
                e6 = e6 + 1
            elif n == "500":
                e7 = e7 + 1
            fs = fs + int(s[8])
            line = sys.stdin.readline()
            c = c + 1
    except KeyboardInterrupt:
        imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
        raise
    imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
