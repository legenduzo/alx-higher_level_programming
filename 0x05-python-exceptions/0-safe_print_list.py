#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count < x:
                count += 1
                print(item, end="")
            else:
                break
        print("\n")
    finally:
        return count
