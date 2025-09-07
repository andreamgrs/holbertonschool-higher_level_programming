#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            num = str("FizzBuzz")
        elif num % 5 == 0:
            num = str("Buzz")
        elif num % 3 == 0:
            num = str("Fizz")
        print("{} ".format(num), end="")
