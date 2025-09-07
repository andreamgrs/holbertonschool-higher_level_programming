#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastnum = number % 10
    else:
        lastnum = number % -10
        lastnum = -lastnum
    print("{}".format(lastnum), end="")
    return lastnum
