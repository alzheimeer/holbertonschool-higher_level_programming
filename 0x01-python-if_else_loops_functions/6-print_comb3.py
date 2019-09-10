#!/usr/bin/python3
for i in range(1, 100):
    b = i % 10
    a = int(i / 10) % 10
    if a >= b:
        continue
    else:
        if i == 89:
            print("{}".format(i))
        else:
            print("{:02}".format(i), end=', ')
