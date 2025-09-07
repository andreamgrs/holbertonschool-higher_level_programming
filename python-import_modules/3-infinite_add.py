#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1
if __name__ == "__main__":
    if num_args == 0:
        print("{}".format(num_args))
    else:
        sum_total = 0
        for cont in range(1, num_args + 1):
            sum_total = sum_total + int(sys.argv[cont])
        print("{}".format(sum_total))
