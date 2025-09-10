#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    if len(set_1) == 0:
        return set_2
    if len(set_2) == 0:
        return set_1
    for element1 in set_1:
        if element1 not in set_2:
            new_set.append(element1)
        for element2 in set_2:
            if element2 not in set_1:
                new_set.append(element2)
    return set(new_set)
#return set_1 ^ set_2
