#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenargv = len(sys.argv)
    if lenargv == 1:
        print("{} arguments.".format(lenargv - 1))
    elif lenargv == 2:
        print("{} argument:".format(lenargv - 1))
        print("{}: {}".format(lenargv - 1, sys.argv[1]))
    else:
        print("{} arguments:".format(lenargv - 1))
        for i in range(1, lenargv):
            print("{}: {}".format(i, sys.argv[i]))
            lenargv += 1
