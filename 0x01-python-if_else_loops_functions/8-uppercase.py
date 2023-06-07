#!/usr/bin/python3
def uppercase(str):
    for b in str:
        if ord('a') <= ord(b) <= ord('z'):
            b = chr(ord(b) - (ord('a') - ord('A')))
        print("{:s}".format(b), end='')
    print("")
