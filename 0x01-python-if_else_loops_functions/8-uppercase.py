#!/usr/bin/python3
def uppercase(str):
    str += '\n'
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
