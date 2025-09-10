#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    my_index = new_list.index(search)
    del new_list[my_index]
    new_list.insert(my_index, replace)
    return new_list
