#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search > len(my_list):
        return my_list
    new_list = my_list.copy()
    for num in new_list:
        if num == search:
            my_index = new_list.index(search)
            del new_list[my_index]
            new_list.insert(my_index, replace)
    return new_list
