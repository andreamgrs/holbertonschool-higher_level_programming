#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for var in my_string:
        if var != 'c' and var != 'C':
            result = result + var
    return result
