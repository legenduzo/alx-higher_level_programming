#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    d = {x: a_dictionary[x] for x in sorted(a_dictionary)}
    for key in d:
        print(f"{key}: {d[key]}")
