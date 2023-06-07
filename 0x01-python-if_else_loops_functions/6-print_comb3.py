#!/usr/bin/python3
for x in range(0, 9):
    for a in range(x + 1, 10):
        print("{:d}".format(x), end="")
        if x == 8 and a == 9:
            print("{:d}".format(a), end='\n')
        else:
            print("{:d}".format(a), end=", ")
