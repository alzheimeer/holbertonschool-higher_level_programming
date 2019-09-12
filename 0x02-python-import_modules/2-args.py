#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    xlen = len(sys.argv)
    z = sys.argv
    if xlen == 1:
        print("{} arguments.".format(xlen - 1))
    elif xlen == 2:
        print("{} argument:".format(xlen - 1))
        print("{}: {}".format(1, z[1]))
    else:
        print("{} arguments:".format(xlen - 1))
        for i in range(1, xlen):
            print("{}: {}".format(i, z[i]))
