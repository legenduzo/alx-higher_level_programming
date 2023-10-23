#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    for n in range(x):
        count += 1
        try:
            if count <= x:
                print("{:d}".format(my_list[n]), end="")
                printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed
