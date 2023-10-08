#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > len(my_list) - 1
    or not isinstance(my_list, list)):
        return my_list

    nl = my_list[:]
    nl[idx] = element
    return nl
