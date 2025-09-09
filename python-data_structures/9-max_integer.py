#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list) - 1
    if len(my_list) == 0:
        return None
    else:
        max_int = my_list[0]
        for cont in my_list[1:]:
            if cont > max_int:
                max_int = cont
        return (max_int)
