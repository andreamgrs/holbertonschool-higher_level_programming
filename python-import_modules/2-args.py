#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1
if __name__ == "__main__":
    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument".format(num_args))
        print("{}: {}".format(num_args, sys.argv[1]))
    else:
        print("{} argument".format(num_args))
        for num in range(1, num_args + 1):
            print("{}: {}".format(num, sys.argv[num]))
