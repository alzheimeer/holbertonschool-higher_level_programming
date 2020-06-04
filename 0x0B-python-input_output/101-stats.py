#!/usr/bin/python3
"""prints logs"""
import sys


def imp(fs, e0, e1, e2, e3, e4, e5, e6, e7):
    """Method to print"""
    print("File size: {}".format(fs))
    if (e0 > 0):
        print("200: {}".format(e0))
    if (e1 > 0):
        print("301: {}".format(e1))
    if (e2 > 0):
        print("400: {}".format(e2))
    if (e3 > 0):
        print("401: {}".format(e3))
    if (e4 > 0):
        print("403: {}".format(e4))
    if (e5 > 0):
        print("404: {}".format(e5))
    if (e6 > 0):
        print("405: {}".format(e6))
    if (e7 > 0):
        print("500: {}".format(e7))

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
            s = line.split()
            if len(s) > 6:
                if c == 10:
                    imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
                    c = 0

                n = s[-2]
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
                fs = fs + int(s[-1])
                line = sys.stdin.readline()
                c = c + 1
    except KeyboardInterrupt:
        imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
        raise
    imp(fs, e0, e1, e2, e3, e4, e5, e6, e7)
