#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result = result + chr(ord(c) - 32)
        else:
            result = result + c
    print("{}".format(result))
