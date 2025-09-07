#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sum = add(a, b)
subs = sub(a, b)
multi = mul(a, b)
divi = div(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, subs))
    print("{} * {} = {}".format(a, b, multi))
    print("{} / {} = {}".format(a, b, divi))
