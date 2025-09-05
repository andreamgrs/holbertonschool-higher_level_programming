#!/usr/bin/python3
def islower(c):
    for up in range(97, 123):
        if ord(c) == up:
            return True
    return False
