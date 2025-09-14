#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cont = 0
    while cont < x:
        try:
            print("{:d}".format(my_list[cont]), end="")
        except IndexError:
            pass
        except TypeError:
            pass
        else:
            cont = cont + 1
    print()
    return cont
