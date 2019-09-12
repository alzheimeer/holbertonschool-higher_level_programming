#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargs = len(sys.argv)
    if lenargs == 1:
        print("{} arguments.".format(lenargs - 1))
    elif lenargs == 2:
        print("{} argument:".format(lenargs - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(lenargs - 1))
        for i in range(1, lenargs):
            print("{}: {}".format(i, sys.argv[i]))
