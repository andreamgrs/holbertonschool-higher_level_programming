#!/usr/bin/python3
exclude = [101, 113]
for a in range(97, 123):
    if a not in exclude:
        print("{}".format(chr(a)), end="")
