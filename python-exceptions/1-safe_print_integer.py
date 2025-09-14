#!/usr/bin/python3
def safe_print_integer(value):
    if value in range(-6789, 67890):
        try:
            print("{:d}".format(value))
            return True
        except:
            return False
