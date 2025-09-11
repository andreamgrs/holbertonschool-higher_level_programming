#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for k, val in new_dic.items():
        new_dic[k] = val * 2
    return (new_dic)
