#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while True:
            if i < x:
                print(my_list[i])
                i += 1
            else:
                print()
                return i
    except IndexError:
        print("out of index")
        return i
