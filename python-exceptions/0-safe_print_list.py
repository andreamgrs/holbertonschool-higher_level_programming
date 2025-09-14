#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cont = 0
    while cont < x:
        try:
            print("{:d}".format(my_list[cont]), end="")
            cont = cont + 1
        except:
            break
    print()
    return cont
