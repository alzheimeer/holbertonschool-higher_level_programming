#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    xlen = len(sys.argv)
    suma = 0
    if xlen == 1:
        print("0")
    elif xlen == 2:
        print("{}".format(sys.argv[1]))
    else:
        for i in range(1, xlen):
            suma = int(sys.argv[i]) + suma
        print("{}".format(suma))
