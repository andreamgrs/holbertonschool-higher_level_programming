#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for sets in set_1:
        for sets_2 in set_2:
            if sets == sets_2:
                new_set.append(sets)
    return new_set
#return set_1 & set_2